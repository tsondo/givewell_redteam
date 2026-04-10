"""Tests for pipeline.agents."""
import json
from pathlib import Path

import pytest

from pipeline.agents import (
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
