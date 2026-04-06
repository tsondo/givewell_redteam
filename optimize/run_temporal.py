"""Entry point for temporal Bayesian optimization of ITN CEA.

Usage:
    python -m optimize.run_temporal                     # Chad + Guinea (validation)
    python -m optimize.run_temporal --country chad      # single country
    python -m optimize.run_temporal --all               # all 8 countries
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from optimize.bayesian_opt_temporal import (
    optimize_country_temporal,
    SEARCH_SPACE,
    PARAM_NAMES,
)
from optimize.cea_model import COUNTRIES

RESULTS_DIR = Path("optimize/results")

VALIDATION_COUNTRIES = ["chad", "guinea"]

N_SOBOL = 25
N_BO = 75


def _serialize(obj: object) -> object:
    """JSON serializer that handles numpy types."""
    import numpy as np
    if isinstance(obj, np.floating):
        return float(obj)
    if isinstance(obj, np.integer):
        return int(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    raise TypeError(f"Not serializable: {type(obj)}")


def run_country(country_key: str) -> dict:
    """Run both minimize and maximize for one country (temporal model)."""
    print(f"\n{'='*60}")
    print(f"  {COUNTRIES[country_key].name} (temporal)")
    print(f"{'='*60}")

    results = {}
    for direction in ("minimize", "maximize"):
        t0 = time.time()
        result = optimize_country_temporal(
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
    out_path = RESULTS_DIR / f"{country_key}_temporal.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=_serialize)

    return results


def generate_temporal_summary(all_results: dict[str, dict]) -> str:
    """Generate the temporal_summary.md content."""
    countries_run = list(all_results.keys())
    all_country_keys = list(COUNTRIES.keys())

    lines = [
        "# Temporal ITN CEA Optimization Summary",
        "",
        "Bayesian optimization of 10 parameters (5 original + distribution interval + "
        "logistics fraction + 3 decay time constants).",
        f"Each country: {N_SOBOL} Sobol + {N_BO} Bayesian = {N_SOBOL + N_BO} trials, "
        "both minimize and maximize cost_per_daly.",
        "",
    ]

    # --- Section 1: Optimal Distribution Intervals ---
    lines += [
        "## Optimal Distribution Intervals",
        "",
        "| Country | Direction | Optimal Interval | At Bound? | "
        "Default $/DALY | Optimized $/DALY | Improvement % |",
        "|---------|-----------|:----------------:|:---------:|"
        "--------------:|-----------------:|--------------:|",
    ]

    for key in countries_run:
        r = all_results[key]
        for direction, label in [("minimize", "Best"), ("maximize", "Worst")]:
            d = r[direction]
            interval = d["best_params"]["distribution_interval_months"]
            at_bound_interval = "distribution_interval_months" in d.get("at_bound", {})
            bound_marker = "Yes*" if at_bound_interval else "No"
            default_daly = d["baseline_metrics"]["cost_per_daly"]
            optimized_daly = d["best_metrics"]["cost_per_daly"]

            if direction == "minimize":
                improvement = (default_daly - optimized_daly) / default_daly * 100
            else:
                improvement = (optimized_daly - default_daly) / default_daly * 100

            lines.append(
                f"| {COUNTRIES[key].name} | {label} | {interval:.1f} mo | "
                f"{bound_marker} | ${default_daly:.0f} | "
                f"${optimized_daly:.0f} | {improvement:.1f}% |"
            )

    # --- Section 2: Static vs Temporal Comparison ---
    lines += [
        "",
        "## Static vs Temporal Comparison",
        "",
        "Phase 1 static model vs temporal model (D=30 default) vs temporal optimized.",
        "",
        "| Country | Static $/DALY (Phase 1) | Temporal $/DALY (D=30) | "
        "Temporal $/DALY (optimized) | Optimal D |",
        "|---------|------------------------:|------------------------:|"
        "----------------------------:|----------:|",
    ]

    for key in countries_run:
        r = all_results[key]
        # Load Phase 1 baseline from static results
        phase1_path = RESULTS_DIR / f"{key}.json"
        static_daly = "N/A"
        if phase1_path.exists():
            with open(phase1_path) as f:
                phase1 = json.load(f)
            static_daly = f"${phase1['minimize']['baseline_metrics']['cost_per_daly']:.0f}"

        temporal_default_daly = r["minimize"]["baseline_metrics"]["cost_per_daly"]
        temporal_opt_daly = r["minimize"]["best_metrics"]["cost_per_daly"]
        optimal_d = r["minimize"]["best_params"]["distribution_interval_months"]

        lines.append(
            f"| {COUNTRIES[key].name} | {static_daly} | "
            f"${temporal_default_daly:.0f} | ${temporal_opt_daly:.0f} | "
            f"{optimal_d:.1f} mo |"
        )

    # --- Section 3: Decay Parameter Sensitivity ---
    lines += [
        "",
        "## Decay Parameter Sensitivity",
        "",
        "Which temporal parameters does the optimizer push hardest (best-case direction)?",
        "",
    ]

    temporal_params = [
        "distribution_interval_months",
        "fixed_logistics_fraction",
        "tau_physical",
        "tau_insecticide",
        "tau_usage",
    ]

    for key in countries_run:
        d = all_results[key]["minimize"]
        lines.append(f"### {COUNTRIES[key].name} (best case)")
        lines.append("")
        for pname in temporal_params:
            spec = next(s for s in SEARCH_SPACE if s.name == pname)
            val = d["best_params"][pname]
            at_bound = pname in d.get("at_bound", {})
            bound_side = d.get("at_bound", {}).get(pname, "")
            range_width = spec.hi - spec.lo
            normalized_pos = (val - spec.lo) / range_width
            marker = " *" if at_bound else ""
            lines.append(
                f"- **{pname}**: {val:.2f} "
                f"(range [{spec.lo}, {spec.hi}], "
                f"position: {normalized_pos:.0%}){marker}"
            )
        lines.append("")

    # --- Section 4: Non-Monotonicity Analysis ---
    lines += [
        "## Non-Monotonicity Analysis",
        "",
        "Parameters at interior optima (not hitting bounds) indicate genuine trade-offs.",
        "",
    ]

    bound_counts: dict[str, dict[str, int]] = {
        name: {"lower": 0, "upper": 0, "interior": 0} for name in PARAM_NAMES
    }
    total_runs = len(countries_run) * 2  # minimize + maximize

    for key in countries_run:
        for direction in ("minimize", "maximize"):
            d = all_results[key][direction]
            at_bound = d.get("at_bound", {})
            for name in PARAM_NAMES:
                if name in at_bound:
                    bound_counts[name][at_bound[name]] += 1
                else:
                    bound_counts[name]["interior"] += 1

    lines.append(
        "| Parameter | At Lower Bound | At Upper Bound | "
        f"Interior Optima | Total Runs ({total_runs}) |"
    )
    lines.append("|-----------|:-:|:-:|:-:|:-:|")
    for name in PARAM_NAMES:
        lo = bound_counts[name]["lower"]
        hi = bound_counts[name]["upper"]
        interior = bound_counts[name]["interior"]
        lines.append(f"| {name} | {lo} | {hi} | {interior} | {lo + hi + interior} |")

    lines.append("")
    interior_params = [
        name for name in PARAM_NAMES
        if bound_counts[name]["interior"] > total_runs // 2
    ]
    if interior_params:
        lines.append(
            f"Parameters with mostly interior optima: "
            f"**{', '.join(interior_params)}** — these show genuine non-monotonic behavior."
        )
    else:
        lines.append(
            "Most parameters hit bounds, suggesting monotonic influence within the search space."
        )

    # --- Note about missing countries ---
    if set(countries_run) != set(all_country_keys):
        remaining = [k for k in all_country_keys if k not in countries_run]
        remaining_names = [COUNTRIES[k].name for k in remaining]
        lines += [
            "",
            f"**Note:** Only {len(countries_run)} of {len(all_country_keys)} countries were run. "
            f"Remaining: {', '.join(remaining_names)}.",
        ]

    lines += [
        "",
        "---",
        "",
        "\\* = parameter at search space boundary",
        "",
        "Generated by `optimize/run_temporal.py`.",
    ]

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run temporal ITN CEA Bayesian optimization"
    )
    parser.add_argument(
        "--country", type=str, default=None,
        help="Single country key to optimize",
    )
    parser.add_argument(
        "--all", action="store_true", dest="run_all",
        help="Run all 8 countries (default: Chad + Guinea validation only)",
    )
    args = parser.parse_args()

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    if args.country:
        countries = [args.country]
    elif args.run_all:
        countries = list(COUNTRIES.keys())
    else:
        countries = VALIDATION_COUNTRIES

    all_results: dict[str, dict] = {}

    t_start = time.time()
    for key in countries:
        all_results[key] = run_country(key)
    total_time = time.time() - t_start

    print(f"\n{'='*60}")
    print(f"  DONE — {len(countries)} countries, {total_time:.1f}s total")
    print(f"{'='*60}")

    # Generate summary
    summary = generate_temporal_summary(all_results)
    summary_path = RESULTS_DIR / "temporal_summary.md"
    summary_path.write_text(summary)
    print(f"\nSummary written to {summary_path}")


if __name__ == "__main__":
    main()
