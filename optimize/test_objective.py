"""Verification tests for the ITN CEA objective function.

Step 3: Baseline reproduction — assert Python model matches spreadsheet defaults.
Step 4: Perturbation sanity checks — verify directional correctness.
"""
from __future__ import annotations

from optimize.cea_model import COUNTRIES, compute_country_ce
from optimize.objective import evaluate_cea, evaluate_cea_all_countries


# ---------------------------------------------------------------------------
# Step 3: Baseline reproduction
# ---------------------------------------------------------------------------

# Expected CE multiples from InsecticideCEA.xlsx (Main CEA!{col}4, data_only)
EXPECTED_CE = {
    "chad": 4.820299402,
    "drc": 14.62902526,
    "guinea": 22.79223041,
    "nigeria_gf": 16.77873555,
    "nigeria_pmi": 13.25042655,
    "south_sudan": 7.163000,
    "togo": 8.806165,
    "uganda": 15.603040,
}


def test_baseline_reproduction() -> None:
    """Verify that default parameters reproduce the spreadsheet's CE values."""
    print("=" * 70)
    print("BASELINE REPRODUCTION TEST")
    print("=" * 70)
    print(f"{'Country':<18} {'Expected':>12} {'Actual':>12} {'Error %':>10} {'Pass?':>7}")
    print("-" * 70)

    all_pass = True
    for key in COUNTRIES:
        result = compute_country_ce(key)
        actual = result["ce_multiple"]
        expected = EXPECTED_CE[key]
        error_pct = abs(actual - expected) / expected * 100

        passed = error_pct < 2.0  # 2% tolerance
        if not passed:
            all_pass = False

        print(
            f"{COUNTRIES[key].name:<18} "
            f"{expected:>12.6f} "
            f"{actual:>12.6f} "
            f"{error_pct:>9.4f}% "
            f"{'  OK' if passed else ' FAIL':>7}"
        )

    print("-" * 70)
    print(f"Result: {'ALL PASS' if all_pass else 'SOME FAILED'}")
    print()
    assert all_pass, "Baseline reproduction failed for one or more countries"


# ---------------------------------------------------------------------------
# Step 4: Perturbation sanity checks
# ---------------------------------------------------------------------------

def test_perturbation_sanity() -> None:
    """Verify directional correctness of parameter perturbations."""
    print("=" * 70)
    print("PERTURBATION SANITY CHECKS (Chad)")
    print("=" * 70)

    country = "chad"
    baseline = evaluate_cea({}, country=country)

    perturbations = [
        {
            "name": "Increase incidence_reduction (0.45 → 0.55)",
            "params": {"incidence_reduction": 0.55},
            "expect_deaths": "increase",
            "expect_cost_per_daly": "decrease",
            "why": "Higher efficacy → more deaths averted → lower cost/DALY",
        },
        {
            "name": "Worsen insecticide_resistance (-0.586 → -0.75)",
            "params": {"insecticide_resistance": -0.75},
            "expect_deaths": "decrease",
            "expect_cost_per_daly": "increase",
            "why": "More resistance → less effective → fewer deaths averted",
        },
        {
            "name": "Worsen net_usage_adj (-0.10 → -0.25)",
            "params": {"net_usage_adj": -0.25},
            "expect_deaths": "decrease",
            "expect_cost_per_daly": "increase",
            "why": "Lower usage → fewer person-years covered → fewer deaths averted",
        },
    ]

    print(
        f"{'Perturbation':<50} "
        f"{'Base deaths':>12} {'New deaths':>12} {'Direction':>10} {'Pass?':>6}"
    )
    print("-" * 100)

    all_pass = True
    for p in perturbations:
        result = evaluate_cea(p["params"], country=country)

        if p["expect_deaths"] == "increase":
            direction_ok = result["deaths_averted_per_million"] > baseline["deaths_averted_per_million"]
        else:
            direction_ok = result["deaths_averted_per_million"] < baseline["deaths_averted_per_million"]

        if not direction_ok:
            all_pass = False

        print(
            f"{p['name']:<50} "
            f"{baseline['deaths_averted_per_million']:>12.4f} "
            f"{result['deaths_averted_per_million']:>12.4f} "
            f"{'↑' if result['deaths_averted_per_million'] > baseline['deaths_averted_per_million'] else '↓':>10} "
            f"{'  OK' if direction_ok else ' FAIL':>6}"
        )

    print("-" * 100)

    # Also print the full baseline metrics for reference
    print()
    print("Baseline metrics (Chad, default params):")
    for k, v in baseline.items():
        print(f"  {k}: {v:.4f}")

    print()
    print(f"Result: {'ALL PASS' if all_pass else 'SOME FAILED'}")
    print()
    assert all_pass, "Perturbation sanity check failed"


# ---------------------------------------------------------------------------
# Step 4b: All-countries overview
# ---------------------------------------------------------------------------

def test_all_countries_overview() -> None:
    """Print CE metrics for all countries at default params."""
    print("=" * 70)
    print("ALL-COUNTRIES OVERVIEW (default params)")
    print("=" * 70)
    results = evaluate_cea_all_countries({})
    print(
        f"{'Country':<18} "
        f"{'CE (x cash)':>12} "
        f"{'Deaths/$1M':>12} "
        f"{'$/DALY':>12}"
    )
    print("-" * 58)
    for key in COUNTRIES:
        r = results[key]
        print(
            f"{COUNTRIES[key].name:<18} "
            f"{r['ce_multiple']:>12.2f} "
            f"{r['deaths_averted_per_million']:>12.2f} "
            f"{r['cost_per_daly']:>12.2f}"
        )
    print()


if __name__ == "__main__":
    test_baseline_reproduction()
    test_perturbation_sanity()
    test_all_countries_overview()
