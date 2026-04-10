"""Tests for pipeline.agents."""
import json
from pathlib import Path

import pytest

from pipeline.agents import (
    JUDGE_FAILURE_MODE_TYPES,
    _build_synthesizer_user_message,
    _compute_judge_audit_aggregate,
    _format_rejected_critiques_for_synthesizer,
    _parse_batched_verifier_output,
    parse_linker_output,
    parse_verifier_output,
    run_linker,
)
from pipeline.schemas import (
    CandidateCritique,
    CritiqueDependency,
    DebatedCritique,
    DecomposerOutput,
    InvestigationThread,
    JudgeAudit,
    LinkerOutput,
    PipelineStats,
    QuantifiedCritique,
    VerifiedCritique,
)


FIXTURES = Path(__file__).parent / "fixtures"


def _make_critique(title: str) -> CandidateCritique:
    """Construct a minimal CandidateCritique for parser testing."""
    return CandidateCritique(
        thread_name="test_thread",
        title=title,
        hypothesis="test hypothesis",
        mechanism="test mechanism",
        parameters_affected=["test_param"],
        suggested_evidence=["test evidence"],
        estimated_direction="uncertain",
        estimated_magnitude="unknown",
    )


class TestVerifierBatchParserDeduplication:
    """Regression test for the verifier batch parser duplicate bug.

    The verifier model sometimes produces a detailed analysis section
    followed by a "---" separator and a summary restatement that repeats
    each "## Critique N:" header. Without deduplication, the parser
    counts each critique twice. This was discovered in the VAS run
    (3 duplicates) and the ITN run (2 duplicates).
    """

    def test_summary_restatement_not_double_counted(self):
        fixture_path = FIXTURES / "verifier_batch_with_summary_restatement.txt"
        raw_text = fixture_path.read_text()

        # Sanity check: the fixture should contain 6 critique headers
        # (3 detailed + 3 restated). If this fails, the fixture is wrong.
        assert raw_text.count("## Critique") == 6, (
            "Fixture should contain 6 '## Critique' headers "
            "(3 detailed analysis + 3 summary restatement)"
        )

        batch = [
            _make_critique("Cold Chain Failures During Distribution Creating Spotty Potency"),
            _make_critique("Record-Keeping Inflation Due to Performance Incentives"),
            _make_critique("Marginal Supplements Target Higher-Cost Remote Populations"),
        ]

        results = _parse_batched_verifier_output(raw_text, batch)

        assert len(results) == 3, (
            f"Expected 3 parsed entries (one per batch critique), got {len(results)}. "
            f"The parser is double-counting the summary restatement section."
        )

        result_titles = [r.original.title for r in results]
        assert result_titles == [c.title for c in batch], (
            f"Expected results in batch order, got {result_titles}"
        )


class TestVerifierVerdictMapping:
    """Test that parse_verifier_output maps verdict strings correctly."""

    VERIFIED_TEXT = (
        "**OVERALL VERDICT: VERIFIED**\n"
        "The claims are well-supported.\n\n"
        "**EVIDENCE FOUND:**\n- Study confirms the effect.\n\n"
        "**CLAIM CHECK:**\n- Main claim: VERIFIED\n"
    )
    PARTIAL_TEXT = (
        "**OVERALL VERDICT: PARTIALLY VERIFIED**\n"
        "Some claims are supported.\n\n"
        "**EVIDENCE FOUND:**\n- Partial support found.\n\n"
        "**CLAIM CHECK:**\n- Main claim: PARTIALLY VERIFIED\n"
    )
    REJECTED_TEXT = (
        "**OVERALL VERDICT: REJECTED**\n"
        "Evidence contradicts the hypothesis.\n\n"
        "**EVIDENCE FOUND:**\n- Counter-evidence found.\n\n"
        "**CLAIM CHECK:**\n- Main claim: REJECTED by data\n"
    )
    UNVERIFIABLE_TEXT = (
        "**OVERALL VERDICT: UNVERIFIABLE**\n"
        "No evidence found either way.\n\n"
        "**EVIDENCE FOUND:**\n\n"
        "**CLAIM CHECK:**\n- Main claim: UNVERIFIABLE\n"
    )

    @pytest.mark.parametrize(
        "text, expected_verdict",
        [
            (VERIFIED_TEXT, "verified"),
            (PARTIAL_TEXT, "partially_verified"),
            (REJECTED_TEXT, "rejected"),
            (UNVERIFIABLE_TEXT, "unverified"),
        ],
        ids=["verified", "partially_verified", "rejected", "unverified"],
    )
    def test_verdict_mapping(self, text, expected_verdict):
        critique = _make_critique("Test Critique")
        result = parse_verifier_output(text, critique)
        assert result.verdict == expected_verdict

    def test_verdict_filter_separates_correctly(self):
        """Simulate the run_verifier verdict filter: verified/partially go to
        the kept list, rejected/unverified go to the rejected list."""
        texts = [self.VERIFIED_TEXT, self.PARTIAL_TEXT, self.REJECTED_TEXT, self.UNVERIFIABLE_TEXT]
        titles = ["Verified One", "Partial One", "Rejected One", "Unverifiable One"]

        verified = []
        rejected = []
        for text, title in zip(texts, titles):
            result = parse_verifier_output(text, _make_critique(title))
            if result.verdict in ("verified", "partially_verified"):
                verified.append(result)
            else:
                rejected.append(result)

        assert len(verified) == 2
        assert len(rejected) == 2
        assert {r.original.title for r in verified} == {"Verified One", "Partial One"}
        assert {r.original.title for r in rejected} == {"Rejected One", "Unverifiable One"}


class TestFormatRejectedCritiquesForSynthesizer:
    """Test that _format_rejected_critiques_for_synthesizer produces
    correctly structured input for the synthesizer prompt."""

    def _make_verified(self, title: str, verdict: str, evidence: list[str] | None = None) -> VerifiedCritique:
        return VerifiedCritique(
            original=_make_critique(title),
            verdict=verdict,
            evidence_found=evidence or [],
            evidence_strength="weak",
            counter_evidence=[],
            caveats=["Claim: UNVERIFIABLE"],
            revised_hypothesis=None,
        )

    def test_includes_both_sections(self):
        rejected = [
            self._make_verified("Open Q", "unverified"),
            self._make_verified("Dead End", "rejected", ["Contradicted by data"]),
        ]
        result = _format_rejected_critiques_for_synthesizer(rejected)
        assert "Verdict: UNVERIFIABLE" in result
        assert "Verdict: REJECTED" in result
        assert "Open Q" in result
        assert "Dead End" in result

    def test_empty_rejected_shows_none(self):
        result = _format_rejected_critiques_for_synthesizer([])
        assert "(none)" in result

    def test_only_unverifiable(self):
        rejected = [self._make_verified("Open Q", "unverified")]
        result = _format_rejected_critiques_for_synthesizer(rejected)
        assert "Open Q" in result
        # REJECTED section should show (none)
        sections = result.split("### Verdict: REJECTED")
        assert len(sections) == 2
        assert "(none)" in sections[1]

    def test_only_rejected(self):
        rejected = [self._make_verified("Dead End", "rejected", ["Counter-evidence"])]
        result = _format_rejected_critiques_for_synthesizer(rejected)
        assert "Dead End" in result
        # UNVERIFIABLE section should show (none)
        sections = result.split("### Verdict: UNVERIFIABLE")
        assert len(sections) == 2
        unverifiable_part = sections[1].split("### Verdict: REJECTED")[0]
        assert "(none)" in unverifiable_part


# ---------------------------------------------------------------------------
# Linker stage tests
# ---------------------------------------------------------------------------


def _make_verified_critique(
    title: str,
    verdict: str = "partially_verified",
    evidence: list[str] | None = None,
    caveats: list[str] | None = None,
    revised: str | None = None,
) -> VerifiedCritique:
    return VerifiedCritique(
        original=_make_critique(title),
        verdict=verdict,
        evidence_found=evidence or [],
        evidence_strength="moderate",
        counter_evidence=[],
        caveats=caveats or [],
        revised_hypothesis=revised,
    )


def _make_debated_critique(
    title: str,
    surviving_strength: str = "moderate",
    advocate_failures: list[str] | None = None,
    challenger_failures: list[str] | None = None,
) -> DebatedCritique:
    ver = _make_verified_critique(title)
    quant = QuantifiedCritique(
        critique=ver,
        target_parameters=[],
        alternative_range=[],
        sensitivity_results={"cost_per_daly_mid": 50.0},
        materiality="material",
        interaction_effects=[],
    )
    audit = JudgeAudit(
        advocate_failures=advocate_failures or [],
        challenger_failures=challenger_failures or [],
        surviving_strength=surviving_strength,
        verdict_justification="Fake justification for tests.",
        recommended_action="CONCLUDE NOW: fake action.",
        action_feasibility="actionable_now",
        debate_resolved="Fake resolved.",
        debate_unresolved="Fake unresolved.",
    )
    return DebatedCritique(
        critique=quant,
        advocate_defense="fake defense",
        challenger_rebuttal="fake rebuttal",
        surviving_strength=surviving_strength,
        key_unresolved=[],
        recommended_action="CONCLUDE NOW: fake action.",
        advocate_self_assessment="partial",
        judge_audit=audit,
    )


class TestParseLinkerOutput:
    """Tests for parse_linker_output covering the three relationship types,
    the (none found) marker, malformed entries, and deduplication."""

    def test_three_relationship_types_extracted(self):
        text = """Preamble.

## DEPENDENCIES

### Dependency 1
surviving: Coverage rate overestimated
rejected: Threshold effects in VAD prevalence
verdict: unverified
relationship: depends_on
confidence: high
justification: The coverage argument references the threshold mechanism directly.

### Dependency 2
surviving: Mortality effect magnitude
rejected: Admin data double-counting
verdict: rejected
relationship: engages_with
confidence: medium
justification: The mortality argument mentions admin data without relying on it.

### Dependency 3
surviving: Compliance drops at scale
rejected: Supervision quality is durable
verdict: rejected
relationship: contradicts
confidence: low
justification: Directly contradicts the supervision claim.
"""
        out = parse_linker_output(text)
        assert len(out.dependencies) == 3

        by_rel = {d.relationship: d for d in out.dependencies}
        assert "depends_on" in by_rel
        assert "engages_with" in by_rel
        assert "contradicts" in by_rel

        depends = by_rel["depends_on"]
        assert depends.surviving_critique_title == "Coverage rate overestimated"
        assert depends.rejected_critique_title == "Threshold effects in VAD prevalence"
        assert depends.rejected_critique_verdict == "unverified"
        assert depends.confidence == "high"
        assert "threshold" in depends.justification.lower()

        engages = by_rel["engages_with"]
        assert engages.rejected_critique_verdict == "rejected"
        assert engages.confidence == "medium"

        contradicts = by_rel["contradicts"]
        assert contradicts.confidence == "low"

    def test_none_found_returns_empty(self):
        text = """## DEPENDENCIES

(none found)
"""
        out = parse_linker_output(text)
        assert out.dependencies == []
        assert out.n_dependencies_found == 0

    def test_missing_dependencies_section_returns_empty(self):
        out = parse_linker_output("No structured output from the model.")
        assert out.dependencies == []

    def test_malformed_relationship_is_skipped(self):
        text = """## DEPENDENCIES

### Dependency 1
surviving: A
rejected: B
verdict: unverified
relationship: made_up_value
confidence: high
justification: bad entry

### Dependency 2
surviving: Good one
rejected: Good rejected
verdict: rejected
relationship: depends_on
confidence: high
justification: valid
"""
        out = parse_linker_output(text)
        assert len(out.dependencies) == 1
        assert out.dependencies[0].surviving_critique_title == "Good one"

    def test_malformed_verdict_is_skipped(self):
        text = """## DEPENDENCIES

### Dependency 1
surviving: A
rejected: B
verdict: unverifiable
relationship: depends_on
confidence: high
justification: wrong verdict label
"""
        out = parse_linker_output(text)
        assert len(out.dependencies) == 0

    def test_missing_title_is_skipped(self):
        text = """## DEPENDENCIES

### Dependency 1
surviving:
rejected: B
verdict: unverified
relationship: depends_on
confidence: high
justification: no surviving title
"""
        out = parse_linker_output(text)
        assert len(out.dependencies) == 0

    def test_invalid_confidence_defaults_to_medium(self):
        text = """## DEPENDENCIES

### Dependency 1
surviving: A
rejected: B
verdict: unverified
relationship: depends_on
confidence: totally_sure
justification: weird confidence value
"""
        out = parse_linker_output(text)
        assert len(out.dependencies) == 1
        assert out.dependencies[0].confidence == "medium"

    def test_deduplication_on_pair(self):
        text = """## DEPENDENCIES

### Dependency 1
surviving: Same Surviving
rejected: Same Rejected
verdict: unverified
relationship: depends_on
confidence: high
justification: first mention

### Dependency 2
surviving: Same Surviving
rejected: Same Rejected
verdict: unverified
relationship: engages_with
confidence: medium
justification: second mention
"""
        out = parse_linker_output(text)
        assert len(out.dependencies) == 1
        # First encountered wins on dedup
        assert out.dependencies[0].relationship == "depends_on"


class TestRunLinkerShortCircuit:
    """The linker must short-circuit without an API call when either input
    is empty, and it must still write a zero-state artifact so resume works."""

    def _redirect_results(self, monkeypatch, tmp_path):
        """Point pipeline.agents.RESULTS_DIR at tmp_path for the test."""
        import pipeline.agents as agents_module
        monkeypatch.setattr(agents_module, "RESULTS_DIR", tmp_path)

    def test_empty_surviving_short_circuits(self, monkeypatch, tmp_path):
        self._redirect_results(monkeypatch, tmp_path)
        stats = PipelineStats()

        result = run_linker(
            surviving_critiques=[],
            rejected_critiques=[_make_verified_critique("rej", verdict="unverified")],
            stats=stats,
            intervention="test-intervention",
        )

        assert result.dependencies == []
        assert result.n_surviving_critiques_examined == 0
        assert result.n_rejected_critiques_available == 1
        assert result.n_dependencies_found == 0
        assert stats.total_input_tokens == 0  # no API call made

        # Zero-state artifact exists
        artifact = tmp_path / "test-intervention" / "05b-linker.json"
        assert artifact.exists()
        data = json.loads(artifact.read_text())
        assert data["n_surviving_critiques_examined"] == 0
        assert data["n_rejected_critiques_available"] == 1

        md_artifact = tmp_path / "test-intervention" / "05b-linker.md"
        assert md_artifact.exists()
        assert "short-circuit" in md_artifact.read_text().lower()

    def test_empty_rejected_short_circuits(self, monkeypatch, tmp_path):
        self._redirect_results(monkeypatch, tmp_path)
        stats = PipelineStats()

        result = run_linker(
            surviving_critiques=[_make_debated_critique("surv")],
            rejected_critiques=[],
            stats=stats,
            intervention="test-intervention",
        )

        assert result.dependencies == []
        assert result.n_surviving_critiques_examined == 1
        assert result.n_rejected_critiques_available == 0
        assert stats.total_input_tokens == 0

        artifact = tmp_path / "test-intervention" / "05b-linker.json"
        assert artifact.exists()

    def test_both_empty_short_circuits(self, monkeypatch, tmp_path):
        self._redirect_results(monkeypatch, tmp_path)
        stats = PipelineStats()

        result = run_linker(
            surviving_critiques=[],
            rejected_critiques=[],
            stats=stats,
            intervention="test-intervention",
        )

        assert result.dependencies == []
        assert result.n_surviving_critiques_examined == 0
        assert result.n_rejected_critiques_available == 0
        assert stats.total_input_tokens == 0

        artifact = tmp_path / "test-intervention" / "05b-linker.json"
        assert artifact.exists()


# ---------------------------------------------------------------------------
# Judge audit aggregate tests
# ---------------------------------------------------------------------------


class TestComputeJudgeAuditAggregate:
    def test_empty_input(self):
        agg = _compute_judge_audit_aggregate([])
        assert agg["total_debates"] == 0
        assert agg["sound_synthesis_noted_count"] == 0
        assert all(agg["failure_mode_counts"][t] == 0 for t in JUDGE_FAILURE_MODE_TYPES)
        assert agg["most_common_advocate_failure"] == "(none)"
        assert agg["most_common_challenger_failure"] == "(none)"

    def test_sound_synthesis_separated_from_failures(self):
        """sound_synthesis_noted is a positive marker and must NOT appear in
        failure_mode_counts, only in sound_synthesis_noted_count."""
        dc = _make_debated_critique(
            "title",
            advocate_failures=[
                "sound_synthesis_noted: good framing",
                "whataboutism: deflects",
            ],
            challenger_failures=[
                "sound_synthesis_noted: clean rebuttal",
                "strawmanning: rebuts non-claim",
            ],
        )
        agg = _compute_judge_audit_aggregate([dc])
        assert agg["total_debates"] == 1
        assert agg["sound_synthesis_noted_count"] == 2
        assert agg["failure_mode_counts"]["whataboutism"] == 1
        assert agg["failure_mode_counts"]["strawmanning"] == 1
        # Must not be keyed into failure_mode_counts
        assert "sound_synthesis_noted" not in agg["failure_mode_counts"]

    def test_most_common_per_side(self):
        dc1 = _make_debated_critique(
            "t1",
            advocate_failures=["whataboutism: x", "whataboutism: y"],
            challenger_failures=["strawmanning: z"],
        )
        dc2 = _make_debated_critique(
            "t2",
            advocate_failures=["whataboutism: a"],
            challenger_failures=["strawmanning: b", "strawmanning: c"],
        )
        agg = _compute_judge_audit_aggregate([dc1, dc2])
        assert agg["most_common_advocate_failure"] == "whataboutism"
        assert agg["most_common_challenger_failure"] == "strawmanning"
        assert agg["failure_mode_counts"]["whataboutism"] == 3
        assert agg["failure_mode_counts"]["strawmanning"] == 3
        assert agg["total_debates"] == 2

    def test_debates_without_judge_audit_skipped(self):
        """Legacy pre-judge critiques have judge_audit=None and should not
        contribute to the total count."""
        dc_with = _make_debated_critique("with", advocate_failures=["whataboutism: x"])
        dc_without = _make_debated_critique("without")
        dc_without.judge_audit = None

        agg = _compute_judge_audit_aggregate([dc_with, dc_without])
        assert agg["total_debates"] == 1  # only dc_with counted
        assert agg["failure_mode_counts"]["whataboutism"] == 1

    def test_unknown_failure_type_ignored(self):
        """Unknown failure type strings (not in the nine real types and not
        sound_synthesis_noted) should be silently ignored, not crash."""
        dc = _make_debated_critique(
            "title",
            advocate_failures=["some_unknown_type: noise"],
        )
        agg = _compute_judge_audit_aggregate([dc])
        assert agg["total_debates"] == 1
        assert all(agg["failure_mode_counts"][t] == 0 for t in JUDGE_FAILURE_MODE_TYPES)


# ---------------------------------------------------------------------------
# Synthesizer user message builder tests
# ---------------------------------------------------------------------------


class TestBuildSynthesizerUserMessage:
    """Contract tests for _build_synthesizer_user_message. The synthesizer
    prompt depends on specific section headers and pre-computed counts;
    these tests pin that contract without making an API call."""

    def _decomposer(self, n_threads: int = 3) -> DecomposerOutput:
        threads = [
            InvestigationThread(
                name=f"Thread {i}",
                scope="",
                key_questions=[],
                cea_parameters_affected=[],
                relevant_sources=[],
                out_of_scope="",
                context_md="",
            )
            for i in range(1, n_threads + 1)
        ]
        return DecomposerOutput(threads=threads, exclusion_list=[], cea_parameter_map="")

    def test_all_required_sections_present(self):
        debated = [
            _make_debated_critique(
                "Finding A",
                advocate_failures=["whataboutism: x"],
                challenger_failures=["strawmanning: y"],
            )
        ]
        rejected = [
            _make_verified_critique("Open Q", verdict="unverified"),
            _make_verified_critique("Dead End", verdict="rejected", evidence=["contradicted"]),
        ]
        dep = CritiqueDependency(
            surviving_critique_title="Finding A",
            rejected_critique_title="Open Q",
            rejected_critique_verdict="unverified",
            relationship="depends_on",
            justification="Finding A relies on the Open Q claim.",
            confidence="high",
        )
        linker = LinkerOutput(
            dependencies=[dep],
            n_surviving_critiques_examined=1,
            n_rejected_critiques_available=2,
            n_dependencies_found=1,
        )
        decomp = self._decomposer(n_threads=3)

        msg = _build_synthesizer_user_message(
            debated=debated,
            all_critiques_count=10,
            verified_count=5,
            rejected_critiques=rejected,
            linker_output=linker,
            decomposer_output=decomp,
            baseline_output="[baseline]",
        )

        # Pipeline Summary with pre-computed counts
        assert "## Pipeline Summary" in msg
        assert "Investigation threads examined: 3" in msg
        assert "Candidate critiques generated: 10" in msg
        assert "Verified critiques: 5" in msg
        assert "Rejected by verifier: 2" in msg
        assert "Critiques surviving adversarial review: 1" in msg
        assert "Dependencies identified: 1" in msg

        # Decomposer Output
        assert "## Decomposer Output" in msg
        assert "- Thread 1" in msg
        assert "- Thread 3" in msg

        # Surviving and Rejected sections
        assert "## Surviving Critiques" in msg
        assert "### Finding A" in msg
        assert "## Rejected Critiques" in msg
        assert "Verdict: UNVERIFIABLE" in msg
        assert "Verdict: REJECTED" in msg
        assert "Open Q" in msg
        assert "Dead End" in msg

        # Dependencies
        assert "## Critique Dependencies (from linker)" in msg
        assert "surviving: Finding A" in msg
        assert "rejected: Open Q" in msg
        assert "verdict: UNVERIFIABLE" in msg  # human-facing label
        assert "relationship: depends_on" in msg
        assert "confidence: high" in msg

        # Judge audit aggregate
        assert "## Judge Audit Aggregate" in msg
        assert "Total critiques debated: 1" in msg
        assert "whataboutism: 1" in msg
        assert "strawmanning: 1" in msg
        # sound_synthesis_noted row should NOT appear (it's separate)
        failure_mode_section = msg.split("## Judge Audit Aggregate")[1].split("## Baseline")[0]
        assert "sound_synthesis_noted: " not in failure_mode_section
        assert "Most common Advocate failure: whataboutism" in msg
        assert "Most common Challenger failure: strawmanning" in msg

        # Baseline at the end
        assert "[baseline]" in msg

    def test_empty_dependencies_message(self):
        debated = [_make_debated_critique("Finding A")]
        linker_empty = LinkerOutput(
            dependencies=[],
            n_surviving_critiques_examined=1,
            n_rejected_critiques_available=0,
            n_dependencies_found=0,
        )
        msg = _build_synthesizer_user_message(
            debated=debated,
            all_critiques_count=3,
            verified_count=2,
            rejected_critiques=[],
            linker_output=linker_empty,
            decomposer_output=self._decomposer(n_threads=2),
            baseline_output="",
        )
        assert "## Critique Dependencies (from linker)" in msg
        assert "(no dependencies identified)" in msg
        assert "Dependencies identified: 0" in msg

    def test_rejected_verdict_split_in_message(self):
        """The rejected section must be split by verdict type even with
        a mix of unverified and rejected critiques."""
        debated = [_make_debated_critique("Finding A")]
        rejected = [
            _make_verified_critique("U1", verdict="unverified"),
            _make_verified_critique("U2", verdict="unverified"),
            _make_verified_critique("R1", verdict="rejected", evidence=["counter"]),
        ]
        linker = LinkerOutput(
            dependencies=[],
            n_surviving_critiques_examined=1,
            n_rejected_critiques_available=3,
            n_dependencies_found=0,
        )
        msg = _build_synthesizer_user_message(
            debated=debated,
            all_critiques_count=5,
            verified_count=1,
            rejected_critiques=rejected,
            linker_output=linker,
            decomposer_output=self._decomposer(n_threads=1),
            baseline_output="",
        )
        # U1 and U2 in UNVERIFIABLE section; R1 in REJECTED section
        unverifiable_section = msg.split("Verdict: UNVERIFIABLE")[1].split("Verdict: REJECTED")[0]
        assert "U1" in unverifiable_section
        assert "U2" in unverifiable_section
        assert "R1" not in unverifiable_section

        rejected_section = msg.split("Verdict: REJECTED")[1].split("## Critique Dependencies")[0]
        assert "R1" in rejected_section
        assert "U1" not in rejected_section
