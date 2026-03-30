"""Tests for the CEA spreadsheet reader against known WaterCEA.xlsx values."""
from __future__ import annotations

import math
from pathlib import Path

import pytest

from pipeline.spreadsheet import WaterCEA

DATA_PATH = Path(__file__).parent.parent / "data" / "WaterCEA.xlsx"


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
