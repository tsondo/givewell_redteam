"""Entry point for per-country bidirectional Bayesian optimization of ITN CEA.

Usage:
    python -m optimize.run_optimization              # all 8 countries, both directions
    python -m optimize.run_optimization --country chad  # single country
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from optimize.bayesian_opt import optimize_country, SEARCH_SPACE, PARAM_NAMES
from optimize.cea_model import COUNTRIES

RESULTS_DIR = Path("optimize/results")

# Use 16 Sobol (power of 2) + 34 BO = 50 total trials
N_SOBOL = 16
N_BO = 34


def _serialize(obj: object) -> object:
    """JSON serializer that handles numpy types."""
    import numpy as np
    if isinstance(obj, (np.floating, float)):
        return float(obj)
    if isinstance(obj, (np.integer, int)):
        return int(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    raise TypeError(f"Not serializable: {type(obj)}")


def run_country(country_key: str) -> dict:
    """Run both minimize and maximize for one country."""
    print(f"\n{'='*60}")
    print(f"  {COUNTRIES[country_key].name}")
    print(f"{'='*60}")

    results = {}
    for direction in ("minimize", "maximize"):
        t0 = time.time()
        result = optimize_country(
            country_key,
            direction=direction,
            n_sobol=N_SOBOL,
            n_bo=N_BO,
            seed=42,
            verbose=True,
        )
        elapsed = time.time() - t0
        result["elapsed_seconds"] = round(elapsed, 1)
        results[direction] = result
        print(f"         ({elapsed:.1f}s)")

    # Save per-country JSON
    out_path = RESULTS_DIR / f"{country_key}.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=_serialize)

    return results


def generate_summary(all_results: dict[str, dict]) -> str:
    """Generate the optimization_summary.md content."""
    lines = [
        "# ITN CEA Optimization Summary",
        "",
        "Bayesian optimization of 5 high-impact parameters identified by the red-team pipeline.",
        f"Each country: {N_SOBOL} Sobol + {N_BO} Bayesian = {N_SOBOL + N_BO} trials, "
        "both minimize and maximize cost_per_daly.",
        "",
        "## Decision-Relevant Uncertainty Ranges",
        "",
        "GiveWell's point estimate vs. the range of defensible alternative assumptions.",
        "",
        "| Country | Best Case CE | GiveWell Default CE | Worst Case CE | "
        "Uncertainty Range | Best $/DALY | Default $/DALY | Worst $/DALY |",
        "|---------|-------------|--------------------:|---------------|"
        "-------------------|------------|---------------:|-------------|",
    ]

    for key in COUNTRIES:
        r = all_results[key]
        mn = r["minimize"]
        mx = r["maximize"]
        baseline_ce = mn["baseline_metrics"]["ce_multiple"]
        best_ce = mn["best_metrics"]["ce_multiple"]
        worst_ce = mx["best_metrics"]["ce_multiple"]
        uncertainty = best_ce - worst_ce

        baseline_daly = mn["baseline_metrics"]["cost_per_daly"]
        best_daly = mn["best_metrics"]["cost_per_daly"]
        worst_daly = mx["best_metrics"]["cost_per_daly"]

        lines.append(
            f"| {COUNTRIES[key].name} | {best_ce:.2f}x | {baseline_ce:.2f}x | "
            f"{worst_ce:.2f}x | {uncertainty:.2f}x | "
            f"${best_daly:.0f} | ${baseline_daly:.0f} | ${worst_daly:.0f} |"
        )

    # Parameter divergence table
    lines += [
        "",
        "## Key Parameter Shifts",
        "",
        "Best-case (minimize $/DALY) vs. worst-case (maximize $/DALY) parameter values.",
        "Parameters hitting bounds are marked with ▸.",
        "",
    ]

    # Build per-country parameter comparison
    lines.append(
        "| Country | Direction | " +
        " | ".join(PARAM_NAMES) + " |"
    )
    lines.append(
        "|---------|-----------|" +
        "|".join(["-----------" for _ in PARAM_NAMES]) + "|"
    )

    for key in COUNTRIES:
        r = all_results[key]
        for direction, label in [("minimize", "Best"), ("maximize", "Worst")]:
            d = r[direction]
            params = d["best_params"]
            at_bound = d.get("at_bound", {})
            cells = []
            for name in PARAM_NAMES:
                val = params[name]
                marker = " ▸" if name in at_bound else ""
                cells.append(f"{val:.3f}{marker}")
            lines.append(
                f"| {COUNTRIES[key].name} | {label} | " +
                " | ".join(cells) + " |"
            )

    # Default values row
    from optimize.cea_model import (
        DEFAULT_INCIDENCE_REDUCTION, DEFAULT_NET_USAGE_ADJ,
        DEFAULT_EXTERNAL_VALIDITY, DEFAULT_INDIRECT_DEATHS_MULTIPLIER,
        DEFAULT_OVER5_RELATIVE_EFFICACY,
    )
    defaults = {
        "incidence_reduction": DEFAULT_INCIDENCE_REDUCTION,
        "net_usage_adj": DEFAULT_NET_USAGE_ADJ,
        "external_validity": DEFAULT_EXTERNAL_VALIDITY,
        "indirect_deaths_multiplier": DEFAULT_INDIRECT_DEATHS_MULTIPLIER,
        "over5_relative_efficacy": DEFAULT_OVER5_RELATIVE_EFFICACY,
    }
    cells = [f"{defaults[name]:.3f}" for name in PARAM_NAMES]
    lines.append(
        "| **GiveWell Default** | — | " +
        " | ".join(cells) + " |"
    )

    # Bound-hitting analysis
    lines += [
        "",
        "## Parameters Hitting Bounds",
        "",
        "Parameters pushed to their search space boundary suggest monotonic influence",
        "or bounds that may be too tight.",
        "",
    ]

    bound_counts: dict[str, dict[str, int]] = {
        name: {"lower": 0, "upper": 0} for name in PARAM_NAMES
    }
    for key in COUNTRIES:
        for direction in ("minimize", "maximize"):
            d = all_results[key][direction]
            for name, side in d.get("at_bound", {}).items():
                bound_counts[name][side] += 1

    lines.append("| Parameter | Hit Lower Bound | Hit Upper Bound | Total Hits (of 16 runs) |")
    lines.append("|-----------|:-:|:-:|:-:|")
    for name in PARAM_NAMES:
        lo = bound_counts[name]["lower"]
        hi = bound_counts[name]["upper"]
        total = lo + hi
        lines.append(f"| {name} | {lo} | {hi} | {total} |")

    # Cross-country convergence
    lines += [
        "",
        "## Cross-Country Convergence",
        "",
        "Do different countries converge on similar parameter shifts, or diverge?",
        "",
    ]

    for direction, label in [("minimize", "Best case"), ("maximize", "Worst case")]:
        lines.append(f"### {label}")
        lines.append("")
        for name in PARAM_NAMES:
            vals = [
                all_results[key][direction]["best_params"][name]
                for key in COUNTRIES
            ]
            mean = sum(vals) / len(vals)
            spread = max(vals) - min(vals)
            spec = next(s for s in SEARCH_SPACE if s.name == name)
            range_width = spec.hi - spec.lo
            convergence = 1.0 - (spread / range_width) if range_width > 0 else 1.0
            lines.append(
                f"- **{name}**: mean={mean:.3f}, spread={spread:.3f} "
                f"(convergence: {'high' if convergence > 0.8 else 'moderate' if convergence > 0.5 else 'low'})"
            )
        lines.append("")

    lines += [
        "---",
        "",
        "Generated by `optimize/run_optimization.py`.",
    ]

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run ITN CEA Bayesian optimization")
    parser.add_argument("--country", type=str, default=None, help="Single country key to optimize")
    args = parser.parse_args()

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    countries = [args.country] if args.country else list(COUNTRIES.keys())
    all_results: dict[str, dict] = {}

    t_start = time.time()
    for key in countries:
        all_results[key] = run_country(key)
    total_time = time.time() - t_start

    print(f"\n{'='*60}")
    print(f"  DONE — {len(countries)} countries, {total_time:.1f}s total")
    print(f"{'='*60}")

    # Generate summary if we ran all countries
    if len(countries) == len(COUNTRIES):
        summary = generate_summary(all_results)
        summary_path = RESULTS_DIR / "optimization_summary.md"
        summary_path.write_text(summary)
        print(f"\nSummary written to {summary_path}")


if __name__ == "__main__":
    main()
