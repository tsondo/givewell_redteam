"""Tests for pipeline.agents."""
from pathlib import Path

import pytest

from pipeline.agents import (
    _format_rejected_critiques_for_synthesizer,
    _parse_batched_verifier_output,
    parse_verifier_output,
)
from pipeline.schemas import CandidateCritique, VerifiedCritique


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
