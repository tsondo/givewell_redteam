"""Temporal ITN CEA model — adds net degradation over time to the static model.

Composes with the static model in cea_model.py via a scaling factor:
the temporal layer modulates how much of the static model's assumed
protection is actually realized over a distribution cycle, accounting
for physical decay, insecticide loss, and declining usage.

Phase 2: creates a genuine cost-vs-efficacy trade-off by trading
distribution frequency against net degradation.
"""
from __future__ import annotations

import math

from optimize.cea_model import (
    COUNTRIES,
    CountryParams,
    DEFAULT_EXTERNAL_VALIDITY,
    DEFAULT_INCIDENCE_REDUCTION,
    DEFAULT_INDIRECT_DEATHS_MULTIPLIER,
    DEFAULT_NET_USAGE_ADJ,
    DEFAULT_OVER5_RELATIVE_EFFICACY,
    compute_country_ce,
)


# ---------------------------------------------------------------------------
# Decay primitives
# ---------------------------------------------------------------------------

def physical_survival(t_months: float, tau_physical: float) -> float:
    """Fraction of nets still physically intact at time t.

    Calibrated to ~31% survival at 24 months (AMF monitoring data).
    tau_physical ≈ 20.5 months.
    """
    if t_months == 0:
        return 1.0
    return math.exp(-t_months / tau_physical)


def insecticide_efficacy(t_months: float, tau_insecticide: float) -> float:
    """Fraction of original insecticide efficacy remaining at time t.

    Decays faster than physical survival; tau ≈ 12-18 months.
    """
    if t_months == 0:
        return 1.0
    return math.exp(-t_months / tau_insecticide)


def usage_rate(t_months: float, u0: float, tau_usage: float) -> float:
    """Fraction of households still using the net at time t.

    Starts at u0 (initial uptake) and decays slowly.
    Calibrated to ~0.65 at 12 months with u0=0.80, tau_usage≈48.
    """
    if t_months == 0:
        return u0
    return u0 * math.exp(-t_months / tau_usage)


def net_efficacy(
    t_months: float,
    tau_physical: float,
    tau_insecticide: float,
    tau_usage: float,
    u0: float = 0.80,
) -> float:
    """Combined net efficacy at time t — product of all three decay factors."""
    return (
        physical_survival(t_months, tau_physical)
        * insecticide_efficacy(t_months, tau_insecticide)
        * usage_rate(t_months, u0, tau_usage)
    )


# ---------------------------------------------------------------------------
# Time integration
# ---------------------------------------------------------------------------

def integrate_efficacy_over_cycle(
    interval_months: float,
    tau_physical: float,
    tau_insecticide: float,
    tau_usage: float,
    u0: float = 0.80,
    dt: float = 0.5,
) -> float:
    """Time-weighted average efficacy over one distribution cycle.

    Uses trapezoidal rule to integrate net_efficacy from 0 to interval_months.
    Returns a value in [0, 1] representing average protection realized.
    """
    n_steps = max(1, int(interval_months / dt))
    actual_dt = interval_months / n_steps

    total = 0.0
    prev_val = net_efficacy(0, tau_physical, tau_insecticide, tau_usage, u0)
    for i in range(1, n_steps + 1):
        t = i * actual_dt
        curr_val = net_efficacy(t, tau_physical, tau_insecticide, tau_usage, u0)
        total += (prev_val + curr_val) * 0.5 * actual_dt
        prev_val = curr_val

    # Normalize to get average (divide integral by interval length)
    # Also normalize by initial efficacy (u0) so result is relative to
    # the static model's assumption of constant protection
    initial = net_efficacy(0, tau_physical, tau_insecticide, tau_usage, u0)
    if initial == 0 or interval_months == 0:
        return 0.0
    return total / (interval_months * initial)


# ---------------------------------------------------------------------------
# Cost derivation
# ---------------------------------------------------------------------------

def derive_cost_per_person_year(country_key: str) -> float:
    """Back-calculate cost per person-year from the static model.

    Uses: cost_per_py = grant_size / total_person_years
    This avoids needing per-net costs from the spreadsheet.
    """
    c = COUNTRIES[country_key]
    total_py = c.person_years_u5 + c.person_years_5_14 + c.person_years_over14
    return c.grant_size / total_py


# ---------------------------------------------------------------------------
# Main temporal CEA function
# ---------------------------------------------------------------------------

def compute_temporal_cea(
    country_key: str,
    *,
    distribution_interval_months: float = 30,
    fixed_logistics_fraction: float = 0.15,
    tau_physical: float = 20.5,
    tau_insecticide: float = 15.0,
    tau_usage: float = 48.0,
    program_years: float = 10,
    incidence_reduction: float = DEFAULT_INCIDENCE_REDUCTION,
    net_usage_adj: float = DEFAULT_NET_USAGE_ADJ,
    external_validity: float = DEFAULT_EXTERNAL_VALIDITY,
    indirect_deaths_multiplier: float = DEFAULT_INDIRECT_DEATHS_MULTIPLIER,
    over5_relative_efficacy: float = DEFAULT_OVER5_RELATIVE_EFFICACY,
) -> dict[str, float]:
    """Compute temporal ITN cost-effectiveness for one country program.

    Composes with the static model: computes time-weighted average net
    efficacy over a distribution cycle, then scales the static model's
    deaths averted by that factor.

    Returns dict with:
        - cost_per_daly: cost per DALY averted
        - deaths_averted_per_million: deaths averted per single cycle (for comparability)
        - total_program_cost: total cost over program horizon
        - average_net_efficacy: time-weighted average efficacy (0-1)
        - num_distribution_cycles: number of distribution rounds
        - ce_scaling_factor: the temporal scaling applied to static results
    """
    program_months = program_years * 12
    D = distribution_interval_months

    # --- Temporal scaling: prorate final cycle to avoid sawtooth artifact ---
    # Full cycles: each has identical average efficacy (full replacement resets)
    avg_efficacy_full = integrate_efficacy_over_cycle(
        D, tau_physical, tau_insecticide, tau_usage,
    )
    num_full_cycles = int(program_months // D)
    remainder_months = program_months - num_full_cycles * D

    if remainder_months > 1e-6:
        # Partial final cycle: full distribution cost, but only partial benefit
        avg_efficacy_partial = integrate_efficacy_over_cycle(
            remainder_months, tau_physical, tau_insecticide, tau_usage,
        )
        num_cycles = num_full_cycles + 1
        full_cycle_months = num_full_cycles * D
        total_efficacy_months = (
            avg_efficacy_full * full_cycle_months
            + avg_efficacy_partial * remainder_months
        )
        avg_efficacy = total_efficacy_months / program_months
    else:
        num_cycles = num_full_cycles
        avg_efficacy = avg_efficacy_full

    # --- Static model results ---
    static_result = compute_country_ce(
        country_key,
        incidence_reduction=incidence_reduction,
        net_usage_adj=net_usage_adj,
        external_validity=external_validity,
        indirect_deaths_multiplier=indirect_deaths_multiplier,
        over5_relative_efficacy=over5_relative_efficacy,
    )

    # Scale deaths averted by temporal efficacy
    deaths_averted_scaled = static_result["deaths_averted"] * avg_efficacy

    # --- Cost model ---
    # Every cycle (including partial) incurs full distribution cost
    cost_per_py = derive_cost_per_person_year(country_key)
    c = COUNTRIES[country_key]
    total_py = c.person_years_u5 + c.person_years_5_14 + c.person_years_over14
    variable_cost_per_cycle = cost_per_py * total_py  # = grant_size
    cost_per_cycle = variable_cost_per_cycle * (1 + fixed_logistics_fraction)
    total_program_cost = num_cycles * cost_per_cycle

    # --- Deaths over horizon ---
    # GiveWell's implicit cycle length is 30 months (2.5 years)
    static_cycle_years = 30.0 / 12.0

    # Both deaths and costs scale by the same factor (num_cycles at D=30),
    # so cost_per_daly cancels out for baseline reproduction. The linear
    # assumption is approximate but self-consistent.
    deaths_over_horizon = deaths_averted_scaled * (program_years / static_cycle_years)

    # --- DALY conversion ---
    dalys_per_death = 29.02  # same constant as optimize/objective.py:60
    total_dalys = deaths_over_horizon * dalys_per_death
    cost_per_daly = total_program_cost / total_dalys if total_dalys > 0 else float("inf")

    return {
        "cost_per_daly": cost_per_daly,
        "deaths_averted_per_million": deaths_averted_scaled,
        "total_program_cost": total_program_cost,
        "average_net_efficacy": avg_efficacy,
        "num_distribution_cycles": num_cycles,
        "ce_scaling_factor": avg_efficacy,
    }
