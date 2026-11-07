"""Regression tests for failures seen in cg-tb-statins run #01 (Claude 5.5 models).

Each fixture mirrors the shape of real run #01 output.
"""
from types import SimpleNamespace
from unittest.mock import patch

import pytest

from pipeline import agents
from pipeline.agents import parse_decomposer_output, parse_quantifier_output
from pipeline.botec import TBStatinsBOTEC
from pipeline.config import DATA_DIR, OUTPUT_TOKEN_MULTIPLIER
from pipeline.schemas import CandidateCritique, PipelineStats, VerifiedCritique

DECOMPOSER = """## THREAD 1: Effect size
**SCOPE:** effect.
**KEY PARAMETERS:** `relative_reduction`
**WHAT CG ALREADY ACCOUNTS FOR:**
- Labels 10% as assumed.
**WHAT CG DOES NOT ACCOUNT FOR:**
- No shrinkage.
**DATA SOURCES TO EXAMINE:**
- Trials.
**MATERIALITY THRESHOLD:** 0.066 crosses the bar.
**KNOWN CONCERNS ALREADY SURFACED:**
- None.

## THREAD 3 (Structural/Methodological): Speedup framework and horizon
**SCOPE:** speedup.
**KEY PARAMETERS:** `speedup_years`
**WHAT CG ALREADY ACCOUNTS FOR:**
- Explicit 1-year speedup.
**WHAT CG DOES NOT ACCOUNT FOR:**
- No adoption ramp.
**DATA SOURCES TO EXAMINE:**
- Pipeline reports.
**MATERIALITY THRESHOLD:** any change in speedup is linear.
**KNOWN CONCERNS ALREADY SURFACED:**
- None.
"""


def test_annotated_thread_header_is_kept() -> None:
    out = parse_decomposer_output(DECOMPOSER)
    assert [t.name for t in out.threads] == [
        "Effect size",
        "Speedup framework and horizon",
    ]


def test_funder_named_sections_reach_investigators() -> None:
    out = parse_decomposer_output(DECOMPOSER)
    ctx = out.threads[1].context_md
    assert "Explicit 1-year speedup." in ctx
    assert "No adoption ramp." in ctx


QUANTIFIER_PROSE = """## Parameter Mapping
- **`relative_reduction`**: current 0.10.

## Plausible Range

**`relative_reduction`:** current value 0.10. Plausible range is **0.05–0.10** under the critique.

**Important caveat:** the 10% is an assumption.

## Materiality Verdict: **BORDERLINE**
"""


def _critique() -> VerifiedCritique:
    return VerifiedCritique(
        original=CandidateCritique(
            thread_name="t", title="Winner's curse", hypothesis="h", mechanism="m",
            parameters_affected=["relative_reduction"], suggested_evidence=[],
            estimated_direction="decreases", estimated_magnitude="medium",
        ),
        verdict="verified", evidence_found=[], evidence_strength="moderate",
        counter_evidence=[], caveats=[], revised_hypothesis=None,
    )


def test_prose_range_runs_real_sensitivity() -> None:
    cea = TBStatinsBOTEC(DATA_DIR / "cg-tb-statins" / "botec_params.json")
    q = parse_quantifier_output(QUANTIFIER_PROSE, _critique(), cea)
    sens = q.sensitivity_results["tb_statins/relative_reduction"]
    assert sens["low"] == pytest.approx(sens["baseline"] / 2)
    assert q.materiality == "material"


def test_mismapped_current_value_is_refused() -> None:
    cea = TBStatinsBOTEC(DATA_DIR / "cg-tb-statins" / "botec_params.json")
    with pytest.raises(ValueError):
        # e.g. a per-participant cost of $500 mapped onto all_in_cost ($7M)
        cea.run_sensitivity("tb_statins", "all_in_cost", 500, 500, 1000)


def _fake_response(stop_reason: str) -> SimpleNamespace:
    return SimpleNamespace(
        content=[SimpleNamespace(type="thinking", thinking=""), SimpleNamespace(type="text", text="out")],
        usage=SimpleNamespace(input_tokens=10, output_tokens=20),
        stop_reason=stop_reason,
    )


def test_truncation_is_recorded_and_caps_are_scaled() -> None:
    stats = PipelineStats()
    with patch.object(agents.client.messages, "create", return_value=_fake_response("max_tokens")) as create:
        text = agents.call_api("m", "s", "u", stats, "decomposer", max_tokens=8192)
    assert text == "out"
    assert stats.truncated_calls == ["decomposer"]
    kwargs = create.call_args.kwargs
    assert kwargs["max_tokens"] == 8192 * OUTPUT_TOKEN_MULTIPLIER
    assert "timeout" in kwargs  # long non-streaming requests need an explicit timeout


def test_complete_call_is_not_flagged() -> None:
    stats = PipelineStats()
    with patch.object(agents.client.messages, "create", return_value=_fake_response("end_turn")):
        agents.call_api("m", "s", "u", stats, "investigator-1", max_tokens=1000)
    assert stats.truncated_calls == []
