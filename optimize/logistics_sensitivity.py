"""Logistics cost sensitivity analysis for Phase 2 temporal model.

Sweeps distribution_interval_months across logistics cost levels for three
representative countries (one per cluster) to test whether findings are
robust to the least empirically grounded parameter.

Usage:
    python -m optimize.logistics_sensitivity
"""
from __future__ import annotations

import json
from pathlib import Path

from optimize.cea_model import COUNTRIES
from optimize.cea_model_temporal import compute_temporal_cea

RESULTS_DIR = Path("optimize/results")

# One country per cluster from Phase 2 findings
REPRESENTATIVE_COUNTRIES = ["chad", "guinea", "togo"]

LOGISTICS_LEVELS = [0.05, 0.15, 0.25]

# Sweep range: 12 to 48 months in steps of 2
INTERVALS = list(range(12, 50, 2))


def load_best_params(country_key: str) -> dict[str, float]:
    """Load Phase 2 best-case (minimize) parameters from result JSON."""
    path = RESULTS_DIR / f"{country_key}_temporal.json"
    with open(path) as f:
        data = json.load(f)
    return data["minimize"]["best_params"]


def sweep_country(
    country_key: str,
    base_params: dict[str, float],
    logistics_frac: float,
) -> list[dict[str, float]]:
    """Sweep distribution_interval_months for one (country, logistics) pair."""
    results = []
    for interval in INTERVALS:
        result = compute_temporal_cea(
            country_key,
            distribution_interval_months=interval,
            fixed_logistics_fraction=logistics_frac,
            tau_physical=base_params["tau_physical"],
            tau_insecticide=base_params["tau_insecticide"],
            tau_usage=base_params["tau_usage"],
            incidence_reduction=base_params["incidence_reduction"],
            net_usage_adj=base_params["net_usage_adj"],
            external_validity=base_params["external_validity"],
            indirect_deaths_multiplier=base_params["indirect_deaths_multiplier"],
            over5_relative_efficacy=base_params["over5_relative_efficacy"],
        )
        results.append({
            "interval": interval,
            "cost_per_daly": result["cost_per_daly"],
            "avg_efficacy": result["average_net_efficacy"],
            "num_cycles": result["num_distribution_cycles"],
        })
    return results


def find_optimal(sweep: list[dict[str, float]]) -> dict[str, float]:
    """Find the interval that minimizes cost_per_daly."""
    best = min(sweep, key=lambda x: x["cost_per_daly"])
    at_30 = next(x for x in sweep if x["interval"] == 30)
    return {
        "optimal_interval": best["interval"],
        "daly_at_optimal": best["cost_per_daly"],
        "daly_at_30": at_30["cost_per_daly"],
    }


def generate_report(all_results: dict) -> str:
    """Generate logistics_sensitivity.md."""
    lines = [
        "# Logistics Cost Sensitivity Analysis",
        "",
        "How optimal distribution interval shifts with logistics cost assumptions.",
        "All other parameters held at Phase 2 best-case (minimize) values.",
        "",
        "## Results",
        "",
        "| Country | Logistics Frac | Optimal D (months) | $/DALY at Optimal D | $/DALY at D=30 |",
        "|---------|:-:|:-:|--:|--:|",
    ]

    for country_key in REPRESENTATIVE_COUNTRIES:
        name = COUNTRIES[country_key].name
        for lf in LOGISTICS_LEVELS:
            r = all_results[country_key][lf]
            lines.append(
                f"| {name} | {lf:.2f} | {r['optimal_interval']} | "
                f"${r['daly_at_optimal']:.0f} | ${r['daly_at_30']:.0f} |"
            )

    # Interpretation
    lines += [
        "",
        "## Interpretation",
        "",
    ]

    # Check cluster stability
    lines.append("### Do the three clusters hold?")
    lines.append("")
    for country_key in REPRESENTATIVE_COUNTRIES:
        name = COUNTRIES[country_key].name
        intervals = [
            all_results[country_key][lf]["optimal_interval"]
            for lf in LOGISTICS_LEVELS
        ]
        lines.append(
            f"- **{name}**: optimal D = {intervals[0]}mo (low) → "
            f"{intervals[1]}mo (mid) → {intervals[2]}mo (high logistics)"
        )
    lines.append("")

    # Check extremes
    lines.append("### When do extremes win?")
    lines.append("")
    for country_key in REPRESENTATIVE_COUNTRIES:
        name = COUNTRIES[country_key].name
        for lf in LOGISTICS_LEVELS:
            opt = all_results[country_key][lf]["optimal_interval"]
            if opt == 12:
                lines.append(
                    f"- **{name}** at logistics={lf:.2f}: "
                    f"D=12 (most frequent) is optimal"
                )
            elif opt == 48:
                lines.append(
                    f"- **{name}** at logistics={lf:.2f}: "
                    f"D=48 (least frequent) is optimal"
                )
    lines.append("")

    # Cost sensitivity
    lines.append("### Cost sensitivity at fixed interval")
    lines.append("")
    lines.append(
        "How much does $/DALY vary across logistics assumptions at D=30?"
    )
    lines.append("")
    for country_key in REPRESENTATIVE_COUNTRIES:
        name = COUNTRIES[country_key].name
        dalys = [
            all_results[country_key][lf]["daly_at_30"]
            for lf in LOGISTICS_LEVELS
        ]
        spread = max(dalys) - min(dalys)
        pct = spread / min(dalys) * 100
        lines.append(
            f"- **{name}**: ${min(dalys):.0f} (low) → ${max(dalys):.0f} (high), "
            f"spread = ${spread:.0f} ({pct:.0f}%)"
        )

    # Print sweep curves as ASCII table for reference
    lines += [
        "",
        "## Full Sweep Data",
        "",
        "Cost per DALY at each interval (months) for each (country, logistics) combination.",
        "",
    ]

    for country_key in REPRESENTATIVE_COUNTRIES:
        name = COUNTRIES[country_key].name
        lines.append(f"### {name}")
        lines.append("")
        header = "| D (mo) | " + " | ".join(f"LF={lf:.2f}" for lf in LOGISTICS_LEVELS) + " |"
        sep = "|--------|" + "|".join("--------:" for _ in LOGISTICS_LEVELS) + "|"
        lines.append(header)
        lines.append(sep)
        for interval in INTERVALS:
            cells = []
            for lf in LOGISTICS_LEVELS:
                sweep = all_results[country_key][f"sweep_{lf}"]
                point = next(x for x in sweep if x["interval"] == interval)
                cells.append(f"${point['cost_per_daly']:.0f}")
            lines.append(f"| {interval} | " + " | ".join(cells) + " |")
        lines.append("")

    lines += [
        "---",
        "",
        "Generated by `optimize/logistics_sensitivity.py`.",
    ]

    return "\n".join(lines)


def main() -> None:
    all_results: dict = {}

    for country_key in REPRESENTATIVE_COUNTRIES:
        base_params = load_best_params(country_key)
        all_results[country_key] = {}

        print(f"{COUNTRIES[country_key].name}:")
        for lf in LOGISTICS_LEVELS:
            sweep = sweep_country(country_key, base_params, lf)
            all_results[country_key][f"sweep_{lf}"] = sweep
            optimal = find_optimal(sweep)
            all_results[country_key][lf] = optimal
            print(
                f"  LF={lf:.2f}: optimal D={optimal['optimal_interval']}mo, "
                f"$/DALY=${optimal['daly_at_optimal']:.0f} "
                f"(vs ${optimal['daly_at_30']:.0f} at D=30)"
            )

    report = generate_report(all_results)
    out_path = RESULTS_DIR / "logistics_sensitivity.md"
    out_path.write_text(report)
    print(f"\nReport written to {out_path}")


if __name__ == "__main__":
    main()
