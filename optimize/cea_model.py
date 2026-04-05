"""Pure Python reimplementation of GiveWell's ITN CEA calculation chain.

Covers only the paths connecting the 6 high-impact parameters identified by the
red-team pipeline (Phase 2) to the final cost-effectiveness output.  Everything
else is held constant at GiveWell's default values, read once from the
spreadsheet and hardcoded here.

No spreadsheet dependency at runtime — safe to call thousands of times.

Source: data/InsecticideCEA.xlsx (GiveWell, 2024)
Formula references use the format  Sheet!Cell.
"""
from __future__ import annotations

import math
from dataclasses import dataclass


# ---------------------------------------------------------------------------
# Per-country constants  (Main CEA sheet, columns I-P, data_only values)
# These are held fixed — the optimizer does not vary them.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class CountryParams:
    """Fixed per-country parameters read from InsecticideCEA.xlsx."""

    name: str
    # Main CEA!{col}55-57 — person-years of net coverage by age group
    person_years_u5: float
    person_years_5_14: float
    person_years_over14: float
    # Main CEA!{col}70 — annual malaria mortality rate among 1-59-month-olds
    direct_malaria_mortality_u5: float
    # Main CEA!{col}73 — mortality reduction from SMC
    smc_reduction: float
    # Main CEA!{col}75 — baseline proportion sleeping under nets
    baseline_net_coverage: float
    # Main CEA!{col}80-81 — national malaria deaths for over-5 ratio
    malaria_deaths_u5_national: float
    total_malaria_deaths_national: float
    # Main CEA!{col}88-89 — malaria incidence in absence of distribution
    incidence_u5_no_nets: float
    incidence_5_14_no_nets: float
    # Main CEA!{col}66 — default insecticide resistance adjustment
    default_insecticide_resistance: float
    # Simple CEA!{col}32-35 — final adjustment factors
    additional_benefits_adj: float
    grantee_adj: float
    leverage_adj: float
    funging_adj: float
    # Main CEA!H8 — grant size (same for all countries)
    grant_size: float


COUNTRIES: dict[str, CountryParams] = {
    "chad": CountryParams(
        name="Chad",
        person_years_u5=129412.3492,
        person_years_5_14=193280.5856,
        person_years_over14=314098.9324,
        direct_malaria_mortality_u5=0.001318997688,
        smc_reduction=0.00091339,
        baseline_net_coverage=0.313,
        malaria_deaths_u5_national=4525.732446,
        total_malaria_deaths_national=7194.19944,
        incidence_u5_no_nets=0.2389634809,
        incidence_5_14_no_nets=0.2389634809,
        default_insecticide_resistance=-0.5859760227,
        additional_benefits_adj=0.529,
        grantee_adj=-0.04,
        leverage_adj=-0.008308060237,
        funging_adj=-0.0302403437,
        grant_size=1_000_000.0,
    ),
    "drc": CountryParams(
        name="DRC",
        person_years_u5=45449.47245,
        person_years_5_14=80250.57883,
        person_years_over14=166650.0428,
        direct_malaria_mortality_u5=0.00305644734,
        smc_reduction=0.0,
        baseline_net_coverage=0.591,
        malaria_deaths_u5_national=44077.9481,
        total_malaria_deaths_national=57160.15456,
        incidence_u5_no_nets=1.312088155,
        incidence_5_14_no_nets=0.5349874334,
        default_insecticide_resistance=-0.03767823997,
        additional_benefits_adj=0.479,
        grantee_adj=-0.04,
        leverage_adj=-0.004114250426,
        funging_adj=-0.1461607338,
        grant_size=1_000_000.0,
    ),
    "guinea": CountryParams(
        name="Guinea",
        person_years_u5=110993.7459,
        person_years_5_14=184858.5474,
        person_years_over14=358861.6255,
        direct_malaria_mortality_u5=0.003673911359,
        smc_reduction=0.0,
        baseline_net_coverage=0.586,
        malaria_deaths_u5_national=8181.102532,
        total_malaria_deaths_national=11336.50112,
        incidence_u5_no_nets=0.979056497,
        incidence_5_14_no_nets=0.408530636,
        default_insecticide_resistance=-0.2070227136,
        additional_benefits_adj=0.379,
        grantee_adj=-0.04,
        leverage_adj=-0.001382525591,
        funging_adj=-0.3003019883,
        grant_size=1_000_000.0,
    ),
    "nigeria_gf": CountryParams(
        name="Nigeria (GF)",
        person_years_u5=89661.02727,
        person_years_5_14=161088.9121,
        person_years_over14=323843.7427,
        direct_malaria_mortality_u5=0.002704804276,
        smc_reduction=0.0006345738285,
        baseline_net_coverage=0.51,
        malaria_deaths_u5_national=44919.36,
        total_malaria_deaths_national=77647.61,
        incidence_u5_no_nets=0.8300257314,
        incidence_5_14_no_nets=0.3611326964,
        default_insecticide_resistance=-0.1353111037,
        additional_benefits_adj=0.479,
        grantee_adj=-0.04,
        leverage_adj=-0.001698012775,
        funging_adj=-0.280617756,
        grant_size=1_000_000.0,
    ),
    "nigeria_pmi": CountryParams(
        name="Nigeria (PMI)",
        person_years_u5=60080.33523,
        person_years_5_14=107942.9506,
        person_years_over14=217002.205,
        direct_malaria_mortality_u5=0.002906550552,
        smc_reduction=0.001422761968,
        baseline_net_coverage=0.471,
        malaria_deaths_u5_national=30014.76,
        total_malaria_deaths_national=55752.71,
        incidence_u5_no_nets=0.9873421779,
        incidence_5_14_no_nets=0.420057953,
        default_insecticide_resistance=-0.1353111037,
        additional_benefits_adj=0.479,
        grantee_adj=-0.04,
        leverage_adj=-0.003159222382,
        funging_adj=-0.1400660492,
        grant_size=1_000_000.0,
    ),
    "south_sudan": CountryParams(
        name="South Sudan",
        person_years_u5=50664.55547,
        person_years_5_14=88611.89783,
        person_years_over14=170882.4112,
        direct_malaria_mortality_u5=0.002516179553,
        smc_reduction=0.000434442,
        baseline_net_coverage=0.494,
        malaria_deaths_u5_national=4010.303592,
        total_malaria_deaths_national=5109.313152,
        incidence_u5_no_nets=0.7352142562,
        incidence_5_14_no_nets=0.3116497861,
        default_insecticide_resistance=-0.3073066123,
        additional_benefits_adj=0.379,
        grantee_adj=-0.04,
        leverage_adj=-0.01129290244,
        funging_adj=-0.05985331551,
        grant_size=1_000_000.0,
    ),
    "togo": CountryParams(
        name="Togo",
        person_years_u5=85287.89807,
        person_years_5_14=155510.4192,
        person_years_over14=365208.9451,
        direct_malaria_mortality_u5=0.001639136168,
        smc_reduction=0.0007102489736,
        baseline_net_coverage=0.795,
        malaria_deaths_u5_national=1880.407943,
        total_malaria_deaths_national=5436.187861,
        incidence_u5_no_nets=1.064869351,
        incidence_5_14_no_nets=0.4466842516,
        default_insecticide_resistance=-0.3290596923,
        additional_benefits_adj=0.379,
        grantee_adj=-0.04,
        leverage_adj=-0.001691670199,
        funging_adj=-0.4161821599,
        grant_size=1_000_000.0,
    ),
    "uganda": CountryParams(
        name="Uganda",
        person_years_u5=88749.31535,
        person_years_5_14=150062.0132,
        person_years_over14=275900.9934,
        direct_malaria_mortality_u5=0.002350482231,
        smc_reduction=0.0,
        baseline_net_coverage=0.704,
        malaria_deaths_u5_national=17385.76538,
        total_malaria_deaths_national=22586.59252,
        incidence_u5_no_nets=1.026211123,
        incidence_5_14_no_nets=0.4290397227,
        default_insecticide_resistance=-0.1149838304,
        additional_benefits_adj=0.379,
        grantee_adj=-0.04,
        leverage_adj=-0.001853405826,
        funging_adj=-0.319351647,
        grant_size=1_000_000.0,
    ),
}


# ---------------------------------------------------------------------------
# Shared constants  (Main CEA sheet, column H)
# ---------------------------------------------------------------------------

# Main CEA!H35 — proportion of distributed nets used in Pryce et al. trials
NET_USAGE_TRIAL: float = 0.7

# Main CEA!H36 — default adjustment for program vs. trial usage (OPTIMIZABLE)
DEFAULT_NET_USAGE_ADJ: float = -0.10

# Main CEA!H37 — derived: NET_USAGE_TRIAL * (1 + NET_USAGE_ADJ)
# Baseline = 0.7 * 0.9 = 0.63
DEFAULT_NET_USAGE_PROGRAM: float = 0.63

# Main CEA!H62 — incidence reduction from Pryce et al. (OPTIMIZABLE)
DEFAULT_INCIDENCE_REDUCTION: float = 0.45

# Main CEA!H64 — internal validity adjustment
DEFAULT_INTERNAL_VALIDITY: float = -0.05

# Main CEA!H65 — external validity adjustment (OPTIMIZABLE)
DEFAULT_EXTERNAL_VALIDITY: float = -0.05

# Main CEA!H68 — ratio of mortality reduction to incidence reduction
MORTALITY_INCIDENCE_RATIO: float = 1.0

# Main CEA!H71 — indirect deaths per direct death (OPTIMIZABLE)
DEFAULT_INDIRECT_DEATHS_MULTIPLIER: float = 0.75

# Main CEA!H84 — relative efficacy for over-5 mortality (OPTIMIZABLE)
DEFAULT_OVER5_RELATIVE_EFFICACY: float = 0.80

# Main CEA!H96 — increase in annual income per malaria case averted
INCOME_PER_CASE: float = 0.0058088

# Main CEA!H98 — years between distribution and income benefits
YEARS_TO_BENEFITS: int = 10

# Main CEA!H99 — discount rate for future benefits
DISCOUNT_RATE: float = 0.04

# Main CEA!H101 — expected years long-term benefits last
BENEFIT_DURATION: int = 40

# Main CEA!H103 — multiplier for resource sharing within households
HOUSEHOLD_MULTIPLIER: float = 2.0

# Main CEA!H112 — moral weight: value of averting under-5 death
MORAL_WEIGHT_U5: float = 116.25262

# Main CEA!H116 — moral weight: value of averting over-5 death
MORAL_WEIGHT_OVER5: float = 73.1914

# Main CEA!H120 — value of increasing ln(consumption) by 1 unit for 1 year
LN_CONSUMPTION_VALUE: float = 1.442695041

# Main CEA!H144 — units of value per dollar, GiveDirectly benchmark
BENCHMARK: float = 0.00333


# ---------------------------------------------------------------------------
# Formula chain
# ---------------------------------------------------------------------------

def _expected_reduction(
    incidence_reduction: float,
    internal_validity: float,
    external_validity: float,
    insecticide_resistance: float,
) -> float:
    """Expected reduction in malaria incidence for net sleepers.

    Formula (Main CEA!H63 through {col}67):
        implied = incidence_reduction / NET_USAGE_TRIAL        # H63
        result  = implied * (1+iv) * (1+ev) * (1+resistance)  # {col}67
    """
    implied = incidence_reduction / NET_USAGE_TRIAL
    return implied * (1 + internal_validity) * (1 + external_validity) * (1 + insecticide_resistance)


def _annuity_due_factor() -> float:
    """Present value of annuity-due (payments at start of period).

    Used in Main CEA!H102:
        ordinary = (1 - (1+r)^(-n)) / r
        annuity_due = ordinary * (1+r)
    """
    r = DISCOUNT_RATE
    n = BENEFIT_DURATION
    ordinary = (1 - (1 + r) ** (-n)) / r
    return ordinary * (1 + r)


def _scale_person_years(
    base_py: float,
    net_usage_adj: float,
) -> float:
    """Scale person-years to reflect a different net usage adjustment.

    Person-years are proportional to net_usage_program = NET_USAGE_TRIAL * (1 + net_usage_adj).
    The spreadsheet bakes in the default (0.63). We rescale linearly:
        new_py = base_py * (new_usage / baseline_usage)

    Source: Main CEA rows 35-37, 38, 42, 44, 55-57.
    """
    new_usage = NET_USAGE_TRIAL * (1 + net_usage_adj)
    return base_py * (new_usage / DEFAULT_NET_USAGE_PROGRAM)


def compute_country_ce(
    country_key: str,
    *,
    incidence_reduction: float = DEFAULT_INCIDENCE_REDUCTION,
    net_usage_adj: float = DEFAULT_NET_USAGE_ADJ,
    insecticide_resistance: float | None = None,
    indirect_deaths_multiplier: float = DEFAULT_INDIRECT_DEATHS_MULTIPLIER,
    external_validity: float = DEFAULT_EXTERNAL_VALIDITY,
    over5_relative_efficacy: float = DEFAULT_OVER5_RELATIVE_EFFICACY,
) -> dict[str, float]:
    """Compute ITN cost-effectiveness for one country program.

    Returns dict with:
        - ce_multiple: cost-effectiveness in multiples of GiveDirectly (higher = better)
        - deaths_averted: total deaths averted per $1M grant
        - deaths_averted_u5: under-5 deaths averted per $1M grant
        - cost_per_life_saved: dollars per life saved (before final adjustments)
        - units_of_value: total units of value generated
    """
    c = COUNTRIES[country_key]

    if insecticide_resistance is None:
        insecticide_resistance = c.default_insecticide_resistance

    # Scale person-years if net usage adjustment differs from default
    py_u5 = _scale_person_years(c.person_years_u5, net_usage_adj)
    py_5_14 = _scale_person_years(c.person_years_5_14, net_usage_adj)

    # --- Expected reduction (Main CEA rows 62-69) ---
    exp_red = _expected_reduction(
        incidence_reduction, DEFAULT_INTERNAL_VALIDITY,
        external_validity, insecticide_resistance,
    )
    exp_mort_red = exp_red * MORTALITY_INCIDENCE_RATIO  # Main CEA!{col}69

    # --- Malaria mortality in absence of nets (Main CEA rows 70-76) ---
    # Row 72: total mortality rate = direct * (1 + indirect)
    total_mort = c.direct_malaria_mortality_u5 * (1 + indirect_deaths_multiplier)
    # Row 74: adjusted for SMC
    adj_mort = total_mort - c.smc_reduction
    # Row 76: mortality in absence of nets = adj_mort / (1 - baseline_coverage * exp_mort_red)
    denom = 1 - c.baseline_net_coverage * exp_mort_red
    if denom <= 0:
        denom = 1e-9
    mort_no_nets = adj_mort / denom

    # --- Under-5 deaths averted (Main CEA!{col}77) ---
    deaths_u5 = py_u5 * mort_no_nets * exp_mort_red

    # --- Over-5 deaths averted (Main CEA rows 80-85) ---
    over5_deaths_national = (
        c.total_malaria_deaths_national - c.malaria_deaths_u5_national
    )
    if c.malaria_deaths_u5_national > 0:
        over5_ratio = over5_deaths_national / c.malaria_deaths_u5_national  # {col}83
    else:
        over5_ratio = 0.0
    deaths_over5 = deaths_u5 * over5_ratio * over5_relative_efficacy  # {col}85

    total_deaths = deaths_u5 + deaths_over5

    # --- Development benefits: long-term income (Main CEA rows 88-107) ---
    cases_u5 = py_u5 * c.incidence_u5_no_nets * exp_red        # {col}92
    cases_5_14 = py_5_14 * c.incidence_5_14_no_nets * exp_red   # {col}93
    total_cases = cases_u5 + cases_5_14

    # Main CEA!H97: adjusted ln(income) per case averted
    adj_income = math.log(1 + INCOME_PER_CASE)
    # Main CEA!H100: discounted
    discounted = adj_income * (1 / (1 + DISCOUNT_RATE)) ** YEARS_TO_BENEFITS
    # Main CEA!H102: PV per case (individual)
    pv_per_case = discounted * _annuity_due_factor()
    # Main CEA!H104: PV per case (with household multiplier)
    pv_total_per_case = pv_per_case * HOUSEHOLD_MULTIPLIER
    # Main CEA!{col}107: total development value
    dev_value = total_cases * pv_total_per_case * LN_CONSUMPTION_VALUE

    # --- Total value (Main CEA rows 112-142) ---
    u5_value = deaths_u5 * MORAL_WEIGHT_U5       # {col}113
    over5_value = deaths_over5 * MORAL_WEIGHT_OVER5  # {col}117
    total_value = u5_value + over5_value + dev_value  # {col}142

    # --- Initial CE (Main CEA rows 143-145) ---
    uv_per_dollar = total_value / c.grant_size   # {col}143
    initial_ce = uv_per_dollar / BENCHMARK       # {col}145

    # --- Final CE with adjustments (Main CEA rows 172-203) ---
    final_ce = (
        initial_ce
        * (1 + c.additional_benefits_adj)       # intervention-level adj
        * (1 + c.grantee_adj)                   # grantee-level adj
        * (1 + c.leverage_adj + c.funging_adj)  # leverage/funging
    )

    # --- Cost per life saved (Main CEA!{col}155) ---
    cost_per_life = c.grant_size / total_deaths if total_deaths > 0 else float("inf")

    return {
        "ce_multiple": final_ce,
        "deaths_averted": total_deaths,
        "deaths_averted_u5": deaths_u5,
        "cost_per_life_saved": cost_per_life,
        "units_of_value": total_value,
    }
