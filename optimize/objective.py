"""Callable objective function for Bayesian optimization of ITN CEA parameters.

Interface designed for Ax/BOTorch: dict[str, float] in, dict[str, float] out.
"""
from __future__ import annotations

from optimize.cea_model import (
    COUNTRIES,
    DEFAULT_EXTERNAL_VALIDITY,
    DEFAULT_INCIDENCE_REDUCTION,
    DEFAULT_INDIRECT_DEATHS_MULTIPLIER,
    DEFAULT_NET_USAGE_ADJ,
    DEFAULT_OVER5_RELATIVE_EFFICACY,
    compute_country_ce,
)


# The default country to evaluate.  Chad is GiveWell's first-listed AMF program
# and has the most conservative CE (4.82x), making it a good stress-test target.
DEFAULT_COUNTRY: str = "chad"


def evaluate_cea(
    params: dict[str, float],
    country: str = DEFAULT_COUNTRY,
) -> dict[str, float]:
    """Modify CEA parameters and return cost-effectiveness metrics.

    Args:
        params: Dict mapping parameter names to values.  Supported keys:
            - incidence_reduction  (default 0.45)
            - net_usage_adj        (default -0.10)
            - insecticide_resistance (default: country-specific)
            - indirect_deaths_multiplier (default 0.75)
            - external_validity    (default -0.05)
            - over5_relative_efficacy (default 0.80)
        country: Country program key (default "chad").

    Returns:
        Dict with:
            - cost_per_daly: float (lower is better) — estimated from cost per
              life saved using WHO standard 29.02 DALYs per malaria death
            - deaths_averted_per_million: float (higher is better)
            - ce_multiple: float — multiples of GiveDirectly benchmark
    """
    result = compute_country_ce(
        country,
        incidence_reduction=params.get("incidence_reduction", DEFAULT_INCIDENCE_REDUCTION),
        net_usage_adj=params.get("net_usage_adj", DEFAULT_NET_USAGE_ADJ),
        insecticide_resistance=params.get("insecticide_resistance"),
        indirect_deaths_multiplier=params.get("indirect_deaths_multiplier", DEFAULT_INDIRECT_DEATHS_MULTIPLIER),
        external_validity=params.get("external_validity", DEFAULT_EXTERNAL_VALIDITY),
        over5_relative_efficacy=params.get("over5_relative_efficacy", DEFAULT_OVER5_RELATIVE_EFFICACY),
    )

    # Convert cost per life saved → cost per DALY averted.
    # WHO/GBD: average malaria death in sub-Saharan Africa ≈ 29.02 DALYs
    # (heavily weighted toward under-5 deaths with ~70 YLL each, offset by
    #  over-5 deaths with fewer YLL).  This is a standard conversion factor.
    dalys_per_death = 29.02
    cost_per_daly = result["cost_per_life_saved"] / dalys_per_death

    return {
        "cost_per_daly": cost_per_daly,
        "deaths_averted_per_million": result["deaths_averted"],
        "ce_multiple": result["ce_multiple"],
    }


def evaluate_cea_all_countries(
    params: dict[str, float],
) -> dict[str, dict[str, float]]:
    """Run evaluate_cea across all 8 country programs.

    Returns dict keyed by country name, each containing the standard metrics.
    Useful for understanding how parameter changes propagate across the portfolio.
    """
    return {key: evaluate_cea(params, country=key) for key in COUNTRIES}
