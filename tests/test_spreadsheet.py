"""Tests for the CEA spreadsheet reader against known WaterCEA.xlsx values."""
from __future__ import annotations

import math
from pathlib import Path

import pytest

from pipeline.spreadsheet import ITNCEA, WaterCEA

DATA_PATH = Path(__file__).parent.parent / "data" / "WaterCEA.xlsx"
ITN_DATA_PATH = Path(__file__).parent.parent / "data" / "InsecticideCEA.xlsx"


@pytest.fixture(scope="module")
def cea() -> WaterCEA:
    """Load the CEA once for all tests in the module."""
    return WaterCEA(DATA_PATH)


# -----------------------------------------------------------------------
# TestWaterCEAReading
# -----------------------------------------------------------------------

class TestWaterCEAReading:
    """Verify that parameters are correctly read from the spreadsheet."""

    def test_pooled_relative_risk(self, cea: WaterCEA) -> None:
        assert cea.relative_risk == pytest.approx(0.8638932195, rel=1e-6)

    def test_internal_validity_under5(self, cea: WaterCEA) -> None:
        assert cea.internal_validity_under5 == pytest.approx(0.7957578162, rel=1e-6)

    def test_internal_validity_over5(self, cea: WaterCEA) -> None:
        assert cea.internal_validity_over5 == pytest.approx(0.504149833, rel=1e-6)

    def test_external_validity_ilc_kenya(self, cea: WaterCEA) -> None:
        assert cea.programs["ilc_kenya"].external_validity == pytest.approx(
            1.213858014, rel=1e-6
        )

    def test_external_validity_dsw_kenya(self, cea: WaterCEA) -> None:
        assert cea.programs["dsw_kenya"].external_validity == pytest.approx(
            0.5582511733, rel=1e-6
        )

    def test_plausibility_cap_ilc_kenya(self, cea: WaterCEA) -> None:
        assert cea.programs["ilc_kenya"].plausibility_cap == pytest.approx(0.109, rel=1e-6)

    def test_plausibility_cap_dsw_kenya(self, cea: WaterCEA) -> None:
        assert cea.programs["dsw_kenya"].plausibility_cap == pytest.approx(0.056, rel=1e-6)

    def test_baseline_ce_ilc_kenya(self, cea: WaterCEA) -> None:
        ce = cea.compute_cost_effectiveness("ilc_kenya")
        assert ce == pytest.approx(7.60245168, rel=1e-3)

    def test_baseline_ce_dsw_kenya(self, cea: WaterCEA) -> None:
        ce = cea.compute_cost_effectiveness("dsw_kenya")
        assert ce == pytest.approx(4.421618553, rel=1e-3)

    def test_baseline_ce_dsw_uganda(self, cea: WaterCEA) -> None:
        ce = cea.compute_cost_effectiveness("dsw_uganda")
        assert ce == pytest.approx(7.015706986, rel=1e-3)

    def test_baseline_ce_dsw_malawi(self, cea: WaterCEA) -> None:
        ce = cea.compute_cost_effectiveness("dsw_malawi")
        assert ce == pytest.approx(8.657297146, rel=1e-3)

    def test_cap_binds_ilc_kenya(self, cea: WaterCEA) -> None:
        assert cea.detect_cap_binding("ilc_kenya") is True

    def test_list_programs(self, cea: WaterCEA) -> None:
        expected = {"ilc_kenya", "dsw_kenya", "dsw_uganda", "dsw_malawi"}
        assert set(cea.programs.keys()) == expected

    def test_parameter_summary(self, cea: WaterCEA) -> None:
        summary = cea.get_parameter_summary()
        assert len(summary) > 0
        assert "relative" in summary.lower() or "Relative" in summary


# -----------------------------------------------------------------------
# TestSensitivityAnalysis
# -----------------------------------------------------------------------

class TestSensitivityAnalysis:
    """Verify sensitivity analysis behaviour, especially cap binding."""

    def test_weaker_rr_lowers_ce(self, cea: WaterCEA) -> None:
        """With RR=0.90 (weaker effect), ILC Kenya CE should drop meaningfully.

        At RR=0.90 the plausibility cap no longer binds, but the under-5
        initial estimate is still below the cap so the overall effect is
        moderate (~5%). We verify CE drops by at least 3%.
        """
        baseline = cea.compute_cost_effectiveness("ilc_kenya")
        weaker = cea.compute_cost_effectiveness("ilc_kenya", relative_risk=0.90)
        pct_drop = ((baseline - weaker) / baseline) * 100
        assert pct_drop > 3, f"Expected >3% drop, got {pct_drop:.1f}%"

    def test_cap_binding_detection(self, cea: WaterCEA) -> None:
        """ILC Kenya cap should bind at baseline."""
        assert cea.detect_cap_binding("ilc_kenya") is True

    def test_cap_not_binding_with_weaker_rr(self, cea: WaterCEA) -> None:
        """ILC Kenya cap should NOT bind at RR=0.90."""
        assert cea.detect_cap_binding("ilc_kenya", relative_risk=0.90) is False

    def test_run_sensitivity_returns_expected_keys(self, cea: WaterCEA) -> None:
        result = cea.run_sensitivity(
            "ilc_kenya", "relative_risk", low=0.90, central=0.8639, high=0.80
        )
        expected_keys = {
            "parameter_name",
            "baseline",
            "low",
            "central",
            "high",
            "pct_change_low",
            "pct_change_central",
            "pct_change_high",
            "cap_binds_baseline",
            "cap_binds_low",
            "cap_binds_central",
            "cap_binds_high",
        }
        assert expected_keys.issubset(set(result.keys()))

    def test_stronger_rr_capped(self, cea: WaterCEA) -> None:
        """Strengthening RR when cap binds should NOT change under-5 mortality
        contribution, so overall CE change should be very small for ILC Kenya."""
        baseline = cea.compute_cost_effectiveness("ilc_kenya")
        # Stronger RR (lower value = bigger effect)
        stronger = cea.compute_cost_effectiveness("ilc_kenya", relative_risk=0.80)
        # When cap binds, under-5 mortality is unchanged. Over-5 mortality
        # changes through cap_ratio, and development effects stay the same
        # (IV and EV unchanged). Medical costs stay the same.
        # So the change should be very small (only through over-5 cap_ratio).
        pct_change = abs((stronger - baseline) / baseline) * 100
        # The cap ratio changes: with stronger RR, initial_estimate increases,
        # so cap_ratio = cap/initial decreases, which actually LOWERS over-5 UV.
        # Net effect: CE should barely change or decrease slightly.
        assert pct_change < 5, f"Expected <5% change when cap binds, got {pct_change:.1f}%"


# -----------------------------------------------------------------------
# ITN CEA fixtures
# -----------------------------------------------------------------------


@pytest.fixture(scope="module")
def itn_cea() -> ITNCEA:
    """Load the ITN CEA once for all tests in the module."""
    return ITNCEA(ITN_DATA_PATH)


# -----------------------------------------------------------------------
# TestITNCEAReading
# -----------------------------------------------------------------------


class TestITNCEAReading:
    """Verify that ITNCEA reads parameters and computes baseline CE correctly."""

    # Validation targets from Simple CEA R38, cols I-P
    EXPECTED_CE = {
        "chad": 4.82,
        "drc": 14.63,
        "guinea": 22.79,
        "nigeria_gf": 16.78,
        "nigeria_pmi": 13.25,
        "south_sudan": 7.16,
        "togo": 8.81,
        "uganda": 15.60,
    }

    @pytest.mark.parametrize("program,expected", list(EXPECTED_CE.items()))
    def test_baseline_ce(self, itn_cea: ITNCEA, program: str, expected: float) -> None:
        ce = itn_cea.compute_cost_effectiveness(program)
        assert ce == pytest.approx(expected, rel=1e-2), (
            f"{program}: expected {expected}, got {ce:.4f}"
        )

    def test_list_programs(self, itn_cea: ITNCEA) -> None:
        expected = {
            "chad", "drc", "guinea", "nigeria_gf",
            "nigeria_pmi", "south_sudan", "togo", "uganda",
        }
        assert set(itn_cea.programs.keys()) == expected

    def test_shared_params(self, itn_cea: ITNCEA) -> None:
        assert itn_cea.incidence_reduction == pytest.approx(0.45, rel=1e-6)
        assert itn_cea.internal_validity == pytest.approx(-0.05, rel=1e-6)
        assert itn_cea.external_validity == pytest.approx(-0.05, rel=1e-6)
        assert itn_cea.indirect_deaths_multiplier == pytest.approx(0.75, rel=1e-6)
        assert itn_cea.moral_weight_u5 == pytest.approx(116.25262, rel=1e-4)

    def test_insecticide_resistance_varies(self, itn_cea: ITNCEA) -> None:
        """Resistance varies dramatically across countries."""
        resistances = [itn_cea.programs[k].insecticide_resistance for k in itn_cea.PROGRAMS]
        assert min(resistances) < -0.5  # South Sudan or Chad
        assert max(resistances) > -0.12  # DRC

    def test_parameter_summary(self, itn_cea: ITNCEA) -> None:
        summary = itn_cea.get_parameter_summary()
        assert len(summary) > 0
        assert "insecticide resistance" in summary.lower()
        assert "Chad" in summary

    def test_cap_never_binds(self, itn_cea: ITNCEA) -> None:
        for key in itn_cea.PROGRAMS:
            assert itn_cea.detect_cap_binding(key) is False


# -----------------------------------------------------------------------
# TestITNCEASensitivity
# -----------------------------------------------------------------------


class TestITNCEASensitivity:
    """Verify sensitivity analysis for ITN CEA."""

    def test_weaker_incidence_reduction_lowers_ce(self, itn_cea: ITNCEA) -> None:
        baseline = itn_cea.compute_cost_effectiveness("drc")
        weaker = itn_cea.compute_cost_effectiveness("drc", incidence_reduction=0.30)
        assert weaker < baseline, "Weaker incidence reduction should lower CE"

    def test_worse_resistance_lowers_ce(self, itn_cea: ITNCEA) -> None:
        baseline = itn_cea.compute_cost_effectiveness("drc")
        worse = itn_cea.compute_cost_effectiveness("drc", insecticide_resistance=-0.50)
        assert worse < baseline, "Worse insecticide resistance should lower CE"

    def test_higher_indirect_multiplier_raises_ce(self, itn_cea: ITNCEA) -> None:
        baseline = itn_cea.compute_cost_effectiveness("chad")
        higher = itn_cea.compute_cost_effectiveness("chad", indirect_deaths_multiplier=1.0)
        assert higher > baseline, "Higher indirect multiplier should raise CE"

    def test_run_sensitivity_returns_expected_keys(self, itn_cea: ITNCEA) -> None:
        result = itn_cea.run_sensitivity(
            "chad", "incidence_reduction", low=0.30, central=0.45, high=0.60
        )
        expected_keys = {
            "parameter_name", "baseline",
            "low", "central", "high",
            "pct_change_low", "pct_change_central", "pct_change_high",
            "cap_binds_baseline", "cap_binds_low", "cap_binds_central", "cap_binds_high",
        }
        assert expected_keys.issubset(set(result.keys()))

    def test_run_sensitivity_nonempty(self, itn_cea: ITNCEA) -> None:
        result = itn_cea.run_sensitivity(
            "guinea", "insecticide_resistance", low=-0.40, central=-0.207, high=-0.10
        )
        assert result["baseline"] > 0
        assert result["pct_change_low"] != 0.0

    def test_sensitivity_direction_incidence(self, itn_cea: ITNCEA) -> None:
        """Lowering incidence_reduction should lower CE (negative pct_change_low)."""
        result = itn_cea.run_sensitivity(
            "uganda", "incidence_reduction", low=0.30, central=0.45, high=0.60
        )
        assert result["pct_change_low"] < 0, "Lower incidence reduction → lower CE"
        assert result["pct_change_high"] > 0, "Higher incidence reduction → higher CE"
