"""Tests for pipeline.agents."""
from pathlib import Path

import pytest

from pipeline.agents import _parse_batched_verifier_output
from pipeline.schemas import CandidateCritique


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
