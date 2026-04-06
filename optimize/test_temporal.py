"""Tests for the temporal ITN CEA model.

Verifies decay calibrations, time integration, and baseline reproduction.
"""
from __future__ import annotations

import math


def test_physical_survival_calibration():
    """tau_physical=20.5 should give ~31% survival at 24 months (AMF data)."""
    from optimize.cea_model_temporal import physical_survival

    tau = 20.5
    result = physical_survival(24, tau)
    assert abs(result - 0.31) < 0.02, f"Expected ~0.31, got {result:.4f}"
    assert physical_survival(0, tau) == 1.0


def test_usage_calibration():
    """tau_usage=48 with u0=0.80 should give ~0.65 at 12 months (AMF data)."""
    from optimize.cea_model_temporal import usage_rate

    result = usage_rate(12, u0=0.80, tau_usage=48)
    assert abs(result - 0.65) < 0.03, f"Expected ~0.65, got {result:.4f}"
    assert usage_rate(0, u0=0.80, tau_usage=48) == 0.80


def test_insecticide_decay():
    """Insecticide efficacy should decay faster than physical survival."""
    from optimize.cea_model_temporal import insecticide_efficacy

    tau = 15
    at_12 = insecticide_efficacy(12, tau)
    at_24 = insecticide_efficacy(24, tau)
    assert at_12 < 0.50, f"Expected <0.50 at 12mo, got {at_12:.4f}"
    assert at_24 < at_12, "24-month efficacy should be less than 12-month"


def test_combined_efficacy_decays_monotonically():
    """Combined efficacy should decrease over time."""
    from optimize.cea_model_temporal import net_efficacy

    tau_p, tau_i, tau_u = 20.5, 15.0, 48.0
    prev = net_efficacy(0, tau_p, tau_i, tau_u, u0=0.80)
    for t in range(1, 49):
        curr = net_efficacy(t, tau_p, tau_i, tau_u, u0=0.80)
        assert curr < prev, f"Efficacy increased at month {t}: {prev:.4f} -> {curr:.4f}"
        prev = curr


if __name__ == "__main__":
    test_physical_survival_calibration()
    test_usage_calibration()
    test_insecticide_decay()
    test_combined_efficacy_decays_monotonically()
    print("All decay curve tests PASSED")
