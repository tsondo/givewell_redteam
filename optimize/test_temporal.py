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


def test_baseline_reproduction():
    """With very high tau (no decay) and D=30, temporal model should
    approximate Phase 1 static baselines within 10%.

    Uses Phase 1 result JSONs as comparison targets (validated at 0% error
    against the spreadsheet).
    """
    import json
    from pathlib import Path

    from optimize.cea_model_temporal import compute_temporal_cea

    results_dir = Path("optimize/results")

    print("=" * 70)
    print("BASELINE REPRODUCTION TEST (temporal vs Phase 1 static)")
    print("=" * 70)
    print(f"{'Country':<12} {'Phase1 $/DALY':>14} {'Temporal $/DALY':>16} {'Error %':>10} {'Pass?':>7}")
    print("-" * 70)

    all_pass = True
    for country_key in ("chad", "guinea"):
        with open(results_dir / f"{country_key}.json") as f:
            phase1 = json.load(f)
        baseline_daly = phase1["minimize"]["baseline_metrics"]["cost_per_daly"]

        # No decay (tau=10000) and zero logistics → should match static model
        result = compute_temporal_cea(
            country_key,
            distribution_interval_months=30,
            fixed_logistics_fraction=0.0,
            tau_physical=10000.0,
            tau_insecticide=10000.0,
            tau_usage=10000.0,
        )

        temporal_daly = result["cost_per_daly"]
        error_pct = abs(temporal_daly - baseline_daly) / baseline_daly * 100
        passed = error_pct < 10.0

        if not passed:
            all_pass = False

        print(
            f"{country_key:<12} "
            f"${baseline_daly:>13.2f} "
            f"${temporal_daly:>15.2f} "
            f"{error_pct:>9.1f}% "
            f"{'  OK' if passed else ' FAIL':>7}"
        )

        # Diagnostic: print components separately for debugging
        print(f"  components: deaths_averted_scaled={result['deaths_averted_per_million']:.4f}, "
              f"total_cost=${result['total_program_cost']:.0f}, "
              f"cycles={result['num_distribution_cycles']}, "
              f"efficacy_scaling={result['ce_scaling_factor']:.6f}")

    print("-" * 70)
    print(f"Result: {'ALL PASS' if all_pass else 'SOME FAILED'}")
    print()
    assert all_pass, "Baseline reproduction failed (threshold: 10%)"


if __name__ == "__main__":
    test_physical_survival_calibration()
    test_usage_calibration()
    test_insecticide_decay()
    test_combined_efficacy_decays_monotonically()
    print("All decay curve tests PASSED")
    print()
    test_baseline_reproduction()
