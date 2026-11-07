"""Tests for the prose-BOTEC CEA reader and the source loader."""
from pathlib import Path

import pytest

from pipeline.agents import _map_parameter_name, parse_quantifier_output
from pipeline.botec import TBStatinsBOTEC
from pipeline.config import DATA_DIR, INTERVENTION_URLS
from pipeline.run_pipeline import load_source
from pipeline.schemas import CandidateCritique, PipelineStats, VerifiedCritique
from pipeline.spreadsheet import CEAReader

PARAMS = DATA_DIR / "cg-tb-statins" / "botec_params.json"


@pytest.fixture
def botec() -> TBStatinsBOTEC:
    return TBStatinsBOTEC(PARAMS)


def test_conforms_to_cea_reader(botec: TBStatinsBOTEC) -> None:
    assert isinstance(botec, CEAReader)


def test_reproduces_published_bottom_line(botec: TBStatinsBOTEC) -> None:
    c = botec.compute_components()
    # Published: ~19,900 deaths/yr, ~539,500 DALYs, $OP 54bn, ~3,000x.
    assert c["deaths_per_year"] == pytest.approx(19_900, rel=0.01)
    assert c["dalys"] == pytest.approx(539_500, rel=0.01)
    assert c["benefit_op"] == pytest.approx(54e9, rel=0.02)
    assert botec.compute_cost_effectiveness("tb_statins") == pytest.approx(3_000, rel=0.03)


def test_percent_inputs_are_normalized(botec: TBStatinsBOTEC) -> None:
    as_fraction = botec.compute_cost_effectiveness("tb_statins", p_success=0.3)
    as_percent = botec.compute_cost_effectiveness("tb_statins", p_success=30)
    assert as_fraction == pytest.approx(as_percent)


def test_unknown_parameter_raises(botec: TBStatinsBOTEC) -> None:
    with pytest.raises(KeyError):
        botec.compute_cost_effectiveness("tb_statins", relative_risk=0.9)


def test_sensitivity_reports_bar_crossing(botec: TBStatinsBOTEC) -> None:
    r = botec.run_sensitivity("tb_statins", "p_success", 0.2, 0.4, 0.5)
    assert r["low"] < 2000 < r["baseline"]
    assert r["crosses_bar_low"] is True
    assert r["crosses_bar_high"] is False


def test_own_name_map_takes_precedence(botec: TBStatinsBOTEC) -> None:
    # The default GiveWell map sends "mortality reduction" to relative_risk.
    assert _map_parameter_name("Mortality reduction") == "relative_risk"
    assert _map_parameter_name("Mortality reduction", botec.PARAM_NAME_MAP) == "relative_reduction"
    assert _map_parameter_name("Probability of success", botec.PARAM_NAME_MAP) == "p_success"
    assert _map_parameter_name("Speedup (years)", botec.PARAM_NAME_MAP) == "speedup_years"


def test_quantifier_output_runs_real_sensitivity(botec: TBStatinsBOTEC) -> None:
    text = (
        "PARAMETER MAPPING:\n"
        "- **Probability of success**: p_success, current 0.40\n\n"
        "PLAUSIBLE RANGE:\n"
        "1. **Probability of success**: Current value = 0.40. Plausible range = [0.25, 0.45].\n\n"
        "MATERIALITY VERDICT:\nYES\n"
    )
    critique = VerifiedCritique(
        original=CandidateCritique(
            thread_name="t", title="Success probability is optimistic", hypothesis="h",
            mechanism="m", parameters_affected=["p_success"], suggested_evidence=[],
            estimated_direction="decreases", estimated_magnitude="medium",
        ),
        verdict="verified", evidence_found=[], evidence_strength="moderate",
        counter_evidence=[], caveats=[], revised_hypothesis="",
    )
    q = parse_quantifier_output(text, critique, botec)
    key = "tb_statins/p_success"
    assert key in q.sensitivity_results
    assert q.sensitivity_results[key]["pct_change_low"] == pytest.approx(-37.5)
    assert q.materiality == "material"


def test_load_source_handles_empty_and_file() -> None:
    stats = PipelineStats()
    assert load_source("", stats) == ""
    report = load_source(INTERVENTION_URLS["cg-tb-statins"]["report"], stats)
    assert "Trialing statins" in report
    assert stats.total_cost == 0.0  # no API call made


def test_report_contains_no_held_out_followups() -> None:
    report = (DATA_DIR / "cg-tb-statins" / "report.md").read_text(encoding="utf-8")
    for phrase in ("Updates since", "Limitations", "18 years"):
        assert phrase not in report
