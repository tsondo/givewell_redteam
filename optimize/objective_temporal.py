"""Temporal CEA objective function for Bayesian optimization.

Wraps the temporal model into the dict-in/dict-out interface
expected by bayesian_opt.py.
"""
from __future__ import annotations

from optimize.cea_model import (
    DEFAULT_EXTERNAL_VALIDITY,
    DEFAULT_INCIDENCE_REDUCTION,
    DEFAULT_INDIRECT_DEATHS_MULTIPLIER,
    DEFAULT_NET_USAGE_ADJ,
    DEFAULT_OVER5_RELATIVE_EFFICACY,
)
from optimize.cea_model_temporal import compute_temporal_cea


DEFAULT_COUNTRY: str = "chad"


def evaluate_temporal_cea(
    params: dict[str, float],
    country: str = DEFAULT_COUNTRY,
) -> dict[str, float]:
    """Evaluate temporal CEA with parameters from the optimizer.

    Args:
        params: Dict with keys from the 11-dimensional search space:
            Original 5:
                incidence_reduction, net_usage_adj, external_validity,
                indirect_deaths_multiplier, over5_relative_efficacy
            Temporal 5+1:
                distribution_interval_months, fixed_logistics_fraction,
                tau_physical, tau_insecticide, tau_usage

        country: Country program key.

    Returns:
        Dict with cost_per_daly (primary objective), plus secondary metrics.
    """
    result = compute_temporal_cea(
        country,
        # Temporal parameters
        distribution_interval_months=params.get("distribution_interval_months", 30),
        fixed_logistics_fraction=params.get("fixed_logistics_fraction", 0.15),
        tau_physical=params.get("tau_physical", 20.5),
        tau_insecticide=params.get("tau_insecticide", 15.0),
        tau_usage=params.get("tau_usage", 48.0),
        # Original 5 parameters
        incidence_reduction=params.get("incidence_reduction", DEFAULT_INCIDENCE_REDUCTION),
        net_usage_adj=params.get("net_usage_adj", DEFAULT_NET_USAGE_ADJ),
        external_validity=params.get("external_validity", DEFAULT_EXTERNAL_VALIDITY),
        indirect_deaths_multiplier=params.get("indirect_deaths_multiplier", DEFAULT_INDIRECT_DEATHS_MULTIPLIER),
        over5_relative_efficacy=params.get("over5_relative_efficacy", DEFAULT_OVER5_RELATIVE_EFFICACY),
    )

    return {
        "cost_per_daly": result["cost_per_daly"],
        "deaths_averted_per_million": result["deaths_averted_per_million"],
        "total_program_cost": result["total_program_cost"],
        "average_net_efficacy": result["average_net_efficacy"],
        "num_distribution_cycles": result["num_distribution_cycles"],
    }
