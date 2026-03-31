"""CEA spreadsheet readers and sensitivity analysis for GiveWell interventions.

Provides WaterCEA (water chlorination) and ITNCEA (insecticide-treated nets)
classes that replicate critical formula chains in Python and run sensitivity
analysis when parameters change.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import openpyxl


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class ProgramParams:
    """Country/program-specific parameters read from the spreadsheet."""

    name: str
    # Demographics
    pop_under5: float
    pop_5_14: float
    baseline_mortality_under5: float
    baseline_mortality_over5: float

    # Validity
    external_validity: float
    plausibility_cap: float
    morbidity_ext_validity: float

    # Moral weights
    moral_weight_under5: float
    moral_weight_over5: float
    moral_weight_yld: float  # always 2.3 but read from sheet

    # Adult mortality
    adult_mortality_scaling: float

    # Morbidity
    ylds_per_100k: float
    yld_under5: float
    yld_5_14: float

    # Development effects
    dev_base: float  # units of value per treatment-year from SMC
    dev_chlorination_pct: float  # chlorination as % of SMC

    # Medical costs averted
    baseline_diarrhea_incidence: float
    cost_per_under5_diarrhea: float
    consumption: float  # annual consumption per capita
    iv_medical: float
    ev_medical: float
    value_doubling: float
    mills_reincke: float  # shared but read per-program for safety

    # Cost
    cost_per_person: float
    cash_benchmark: float

    # DSW adjustment factors (only used for DSW programs)
    downside_factor: float = 1.0
    excluded_effects_factor: float = 1.0

    # DSW leverage/funging
    has_leverage_adjustment: bool = False
    prob_govt_replace: float = 0.0
    prob_other_phil_replace: float = 0.0
    prob_upstream_stays: float = 0.0
    prob_not_exist: float = 0.0
    frac_govt_replace: float = 1.0
    frac_other_phil: float = 1.0
    frac_upstream: float = 0.0
    frac_not_exist: float = 0.0
    ce_govt: float = 0.0
    ce_other_phil: float = 0.0
    govt_costs: float = 0.0
    other_donor_upstream: float = 0.0


@dataclass
class SensitivityResult:
    """Result of a sensitivity analysis run."""

    parameter_name: str
    baseline: float
    low: float
    central: float
    high: float
    pct_change_low: float
    pct_change_central: float
    pct_change_high: float
    cap_binds_baseline: bool
    cap_binds_low: bool
    cap_binds_central: bool
    cap_binds_high: bool


# ---------------------------------------------------------------------------
# Main class
# ---------------------------------------------------------------------------

class WaterCEA:
    """Reads GiveWell Water Chlorination CEA and replicates the formula chain."""

    PROGRAMS = ("ilc_kenya", "dsw_kenya", "dsw_uganda", "dsw_malawi")

    def __init__(self, path: Path) -> None:
        self._path = Path(path)
        wb = openpyxl.load_workbook(str(self._path), data_only=True)
        self._read_shared_params(wb)
        self._read_program_params(wb)
        wb.close()

    # ------------------------------------------------------------------
    # Reading helpers
    # ------------------------------------------------------------------

    def _cell(self, ws: Any, ref: str) -> Any:
        """Read a cell value, raising if None."""
        val = ws[ref].value
        if val is None:
            raise ValueError(f"Cell {ws.title}!{ref} is None")
        return val

    def _read_shared_params(self, wb: openpyxl.Workbook) -> None:
        mort = wb["Mortality effect size"]
        self.pooled_ln_rr: float = float(self._cell(mort, "B10"))
        self.relative_risk: float = float(self._cell(mort, "B11"))

        iv = wb["Internal validity adjustment"]
        self.internal_validity_under5: float = float(self._cell(iv, "B6"))
        self.internal_validity_over5: float = float(self._cell(iv, "B7"))
        self.internal_validity_morbidity: float = float(self._cell(iv, "E3"))
        self.mills_reincke: float = float(self._cell(iv, "B23"))

        morb = wb["Morbidity effect size"]
        self.adjusted_diarrhea_rr: float = float(self._cell(morb, "B7"))

    def _read_program_params(self, wb: openpyxl.Workbook) -> None:
        self.programs: dict[str, ProgramParams] = {}
        self._read_ilc_kenya(wb)
        self._read_dsw(wb, "dsw_kenya", "B")
        self._read_dsw(wb, "dsw_uganda", "C")
        self._read_dsw(wb, "dsw_malawi", "D")

    def _read_ilc_kenya(self, wb: openpyxl.Workbook) -> None:
        ws = wb["ILC Kenya"]
        ev_ws = wb["External validity adjustment"]
        mw = wb["Moral weights"]
        am = wb["Adult mortality scaling factor"]
        iv = wb["Internal validity adjustment"]

        self.programs["ilc_kenya"] = ProgramParams(
            name="ILC Kenya",
            pop_under5=float(self._cell(ws, "B3")),
            pop_5_14=float(self._cell(ws, "B42")),
            baseline_mortality_under5=float(self._cell(ws, "B4")),
            baseline_mortality_over5=float(self._cell(ws, "B17")),
            external_validity=float(self._cell(ev_ws, "B6")),
            plausibility_cap=float(self._cell(iv, "B11")),
            morbidity_ext_validity=float(self._cell(ev_ws, "B29")),
            moral_weight_under5=float(self._cell(mw, "B3")),
            moral_weight_over5=float(self._cell(mw, "B7")),
            moral_weight_yld=float(self._cell(ws, "B35")),
            adult_mortality_scaling=float(self._cell(am, "B17")),
            ylds_per_100k=float(self._cell(ws, "B29")),
            yld_under5=float(self._cell(ws, "B43")),
            yld_5_14=float(self._cell(ws, "B44")),
            dev_base=float(self._cell(ws, "B39")),
            dev_chlorination_pct=float(self._cell(ws, "B40")),
            baseline_diarrhea_incidence=float(self._cell(ws, "B52")),
            cost_per_under5_diarrhea=float(self._cell(ws, "B55")),
            consumption=float(self._cell(ws, "B63")),
            iv_medical=float(self._cell(ws, "B60")),
            ev_medical=float(self._cell(ws, "B61")),
            value_doubling=float(self._cell(ws, "B65")),
            mills_reincke=float(self._cell(ws, "B58")),
            cost_per_person=float(self._cell(ws, "B72")),
            cash_benchmark=float(self._cell(ws, "B77")),
        )

    def _read_dsw(self, wb: openpyxl.Workbook, key: str, col: str) -> None:
        ws = wb["DSW"]
        ev_ws = wb["External validity adjustment"]
        mw = wb["Moral weights"]
        am = wb["Adult mortality scaling factor"]
        iv = wb["Internal validity adjustment"]

        # Map column to country index for moral weights and adult mortality
        col_map = {"B": "B", "C": "C", "D": "D"}
        am_col = col_map[col]

        # Plausibility caps: B12=Kenya, B13=Uganda, B14=Malawi
        cap_row = {"B": 12, "C": 13, "D": 14}[col]

        # Moral weights: under5 = B3(Kenya), B4(Uganda), B5(Malawi)
        mw_u5_row = {"B": 3, "C": 4, "D": 5}[col]
        # over5 = B7(Kenya), B8(Uganda), B9(Malawi)
        mw_o5_row = {"B": 7, "C": 8, "D": 9}[col]

        # External validity for mortality
        ev_row = {"B": 11, "C": 16, "D": 21}[col]
        # External validity for morbidity
        morb_ev_row = {"B": 33, "C": 37, "D": 41}[col]

        # DSW consumption: row 65 has adjusted consumption
        consumption = float(self._cell(ws, f"{col}65"))

        self.programs[key] = ProgramParams(
            name=f"DSW {col_map[col]}",
            pop_under5=float(self._cell(ws, f"{col}3")),
            pop_5_14=float(self._cell(ws, f"{col}42")),
            baseline_mortality_under5=float(self._cell(ws, f"{col}4")),
            baseline_mortality_over5=float(self._cell(ws, f"{col}17")),
            external_validity=float(self._cell(ev_ws, f"B{ev_row}")),
            plausibility_cap=float(self._cell(iv, f"B{cap_row}")),
            morbidity_ext_validity=float(self._cell(ev_ws, f"B{morb_ev_row}")),
            moral_weight_under5=float(self._cell(mw, f"B{mw_u5_row}")),
            moral_weight_over5=float(self._cell(mw, f"B{mw_o5_row}")),
            moral_weight_yld=float(self._cell(ws, f"{col}35")),
            adult_mortality_scaling=float(self._cell(am, f"{am_col}17")),
            ylds_per_100k=float(self._cell(ws, f"{col}29")),
            yld_under5=float(self._cell(ws, f"{col}43")),
            yld_5_14=float(self._cell(ws, f"{col}44")),
            dev_base=float(self._cell(ws, f"{col}39")),
            dev_chlorination_pct=float(self._cell(ws, f"{col}40")),
            baseline_diarrhea_incidence=float(self._cell(ws, f"{col}52")),
            cost_per_under5_diarrhea=float(self._cell(ws, f"{col}55")),
            consumption=consumption,
            iv_medical=float(self._cell(ws, f"{col}60")),
            ev_medical=float(self._cell(ws, f"{col}61")),
            value_doubling=float(self._cell(ws, f"{col}67")),
            mills_reincke=float(self._cell(ws, f"{col}58")),
            cost_per_person=float(self._cell(ws, f"{col}74")),
            cash_benchmark=float(self._cell(ws, f"{col}79")),
            # DSW adjustments
            downside_factor=float(self._cell(ws, f"{col}101")),
            excluded_effects_factor=float(self._cell(ws, f"{col}108")),
            # Leverage/funging
            has_leverage_adjustment=True,
            prob_govt_replace=float(self._cell(ws, f"{col}120")),
            prob_other_phil_replace=float(self._cell(ws, f"{col}121")),
            prob_upstream_stays=float(self._cell(ws, f"{col}122")),
            prob_not_exist=float(self._cell(ws, f"{col}123")),
            frac_govt_replace=float(self._cell(ws, f"{col}126")),
            frac_other_phil=float(self._cell(ws, f"{col}127")),
            frac_upstream=float(self._cell(ws, f"{col}128")),
            frac_not_exist=float(self._cell(ws, f"{col}129")),
            ce_govt=float(self._cell(ws, f"{col}133")),
            ce_other_phil=float(self._cell(ws, f"{col}134")),
            govt_costs=float(self._cell(ws, f"{col}112")),
            other_donor_upstream=float(self._cell(ws, f"{col}117")),
        )

    # ------------------------------------------------------------------
    # Formula chain
    # ------------------------------------------------------------------

    def compute_cost_effectiveness(
        self,
        program_key: str,
        **overrides: float,
    ) -> float:
        """Compute cost-effectiveness in multiples of GiveDirectly cash.

        Supported overrides:
            relative_risk, internal_validity_under5, internal_validity_over5,
            external_validity, plausibility_cap, internal_validity_morbidity,
            morbidity_ext_validity, mills_reincke
        """
        p = self.programs[program_key]

        rr = overrides.get("relative_risk", self.relative_risk)
        iv_u5 = overrides.get("internal_validity_under5", self.internal_validity_under5)
        iv_o5 = overrides.get("internal_validity_over5", self.internal_validity_over5)
        ev = overrides.get("external_validity", p.external_validity)
        cap = overrides.get("plausibility_cap", p.plausibility_cap)
        iv_morb = overrides.get("internal_validity_morbidity", self.internal_validity_morbidity)
        morb_ev = overrides.get("morbidity_ext_validity", p.morbidity_ext_validity)
        mr = overrides.get("mills_reincke", p.mills_reincke)

        # --- Under-5 mortality ---
        initial_estimate = (1 - rr) * iv_u5 * ev
        final_estimate = min(initial_estimate, cap)
        u5_deaths_per_100k = p.pop_under5 * p.baseline_mortality_under5 * final_estimate * 100_000
        u5_uv = u5_deaths_per_100k * p.moral_weight_under5

        # --- Over-5 mortality ---
        pop_over5 = 1 - p.pop_under5
        if initial_estimate > 0:
            cap_ratio = final_estimate / initial_estimate
        else:
            cap_ratio = 1.0
        o5_deaths_per_100k = (
            pop_over5
            * p.baseline_mortality_over5
            * (1 - rr)
            * p.adult_mortality_scaling
            * iv_o5
            * ev
            * cap_ratio
            * 100_000
        )
        o5_uv = o5_deaths_per_100k * p.moral_weight_over5

        # --- Morbidity ---
        morbidity_reduction = (1 - self.adjusted_diarrhea_rr) * iv_morb * morb_ev
        ylds_averted = p.ylds_per_100k * morbidity_reduction
        morb_uv = ylds_averted * p.moral_weight_yld

        # --- Development effects ---
        burden_ratio = p.yld_5_14 / p.yld_under5 if p.yld_under5 > 0 else 0.0
        raw_dev_uv = (
            (p.dev_base * p.dev_chlorination_pct * p.pop_under5)
            + (p.dev_base * p.dev_chlorination_pct * p.pop_5_14 * burden_ratio)
        ) * 100_000
        dev_uv = raw_dev_uv * iv_u5 * ev

        # --- Medical costs averted ---
        averted_cases = p.baseline_diarrhea_incidence * morbidity_reduction
        cost_per_u5 = averted_cases * (p.cost_per_under5_diarrhea / morbidity_reduction) if morbidity_reduction > 0 else 0.0
        # Actually: cost_per_u5 is read from spreadsheet directly as annual cost averted per under-5
        # The formula: B55 is pre-computed. B54 = B52 * B53. Then B55 is separate.
        # B57 = B55 * B56. Let me re-derive:
        # cost_per_person = cost_per_under5_diarrhea * pop_under5
        cost_per_person_served = p.cost_per_under5_diarrhea * p.pop_under5
        total_cost_averted = cost_per_person_served * mr
        adjusted_cost = total_cost_averted * p.iv_medical * p.ev_medical
        ln_consumption_increase = math.log(p.consumption + adjusted_cost) - math.log(p.consumption)
        value_per_ln_unit = p.value_doubling / math.log(2)
        uv_medical_per_person = ln_consumption_increase * value_per_ln_unit
        medical_uv = uv_medical_per_person * 100_000

        # --- Total units of value per 100k ---
        total_uv_per_100k = u5_uv + o5_uv + morb_uv + dev_uv + medical_uv

        # --- Cost-effectiveness ---
        uv_per_dollar = (total_uv_per_100k / 100_000) / p.cost_per_person
        uv_per_10k = uv_per_dollar * 10_000

        # --- DSW adjustments ---
        if p.has_leverage_adjustment:
            # Apply downside and excluded-effects adjustments
            adjusted_uv_per_10k = uv_per_10k * p.downside_factor * p.excluded_effects_factor

            # Leverage/funging: compute counterfactual value
            # Scenario UV values (what would happen in absence of DSW spending)
            cost_pp = p.cost_per_person  # annual cost per person served

            # Government replaces
            uv_govt = (adjusted_uv_per_10k * p.frac_govt_replace) - (
                p.ce_govt * cost_pp * p.frac_govt_replace * 10_000
            )

            # Other philanthropic actors replace
            uv_other_phil = (adjusted_uv_per_10k * p.frac_other_phil) - (
                p.ce_other_phil * cost_pp * p.frac_other_phil * 10_000
            )

            # Other actors' upstream costs stay the same
            uv_upstream = (adjusted_uv_per_10k * p.frac_upstream) + (
                (p.other_donor_upstream * p.ce_govt * 10_000) * (1 - p.frac_upstream)
            )

            # Program would not exist
            uv_not_exist = (adjusted_uv_per_10k * p.frac_not_exist) + (
                p.ce_govt * p.govt_costs * 10_000
            )

            # Counterfactual value (weighted by scenario probabilities)
            counterfactual = (
                p.prob_govt_replace * uv_govt
                + p.prob_other_phil_replace * uv_other_phil
                + p.prob_upstream_stays * uv_upstream
                + p.prob_not_exist * uv_not_exist
            )

            # Units of value attributed to DSW spending
            attributed_uv = adjusted_uv_per_10k - counterfactual
            ce_multiple = attributed_uv / p.cash_benchmark
        else:
            ce_multiple = uv_per_10k / p.cash_benchmark

        return ce_multiple

    def detect_cap_binding(self, program_key: str, **overrides: float) -> bool:
        """Return True if the plausibility cap binds for this program."""
        p = self.programs[program_key]

        rr = overrides.get("relative_risk", self.relative_risk)
        iv_u5 = overrides.get("internal_validity_under5", self.internal_validity_under5)
        ev = overrides.get("external_validity", p.external_validity)
        cap = overrides.get("plausibility_cap", p.plausibility_cap)

        initial_estimate = (1 - rr) * iv_u5 * ev
        return initial_estimate > cap

    def run_sensitivity(
        self,
        program_key: str,
        parameter_name: str,
        low: float,
        central: float,
        high: float,
    ) -> dict[str, Any]:
        """Run sensitivity analysis for a single parameter.

        Returns dict with baseline CE, CE at low/central/high,
        percentage changes, and cap binding info.
        """
        baseline_ce = self.compute_cost_effectiveness(program_key)
        cap_binds_baseline = self.detect_cap_binding(program_key)

        results: dict[str, float | bool | str] = {
            "parameter_name": parameter_name,
            "baseline": baseline_ce,
            "cap_binds_baseline": cap_binds_baseline,
        }

        for label, value in [("low", low), ("central", central), ("high", high)]:
            ce = self.compute_cost_effectiveness(program_key, **{parameter_name: value})
            cap_binds = self.detect_cap_binding(program_key, **{parameter_name: value})
            pct_change = ((ce - baseline_ce) / baseline_ce) * 100 if baseline_ce != 0 else 0.0
            results[label] = ce
            results[f"pct_change_{label}"] = pct_change
            results[f"cap_binds_{label}"] = cap_binds

        return results

    def get_parameter_summary(self) -> str:
        """Return a human-readable markdown summary of key parameters and baseline CE."""
        lines: list[str] = []
        lines.append("# Water Chlorination CEA — Parameter Summary\n")

        lines.append("## Shared Parameters\n")
        lines.append(f"- **Pooled ln(RR):** {self.pooled_ln_rr:.10f}")
        lines.append(f"- **Relative risk of all-cause mortality:** {self.relative_risk:.10f}")
        lines.append(f"- **Internal validity, under-5 mortality:** {self.internal_validity_under5:.10f}")
        lines.append(f"- **Internal validity, over-5 mortality:** {self.internal_validity_over5:.10f}")
        lines.append(f"- **Internal validity, morbidity:** {self.internal_validity_morbidity:.4f}")
        lines.append(f"- **Adjusted diarrhea RR:** {self.adjusted_diarrhea_rr:.4f}")
        lines.append(f"- **Mills-Reincke multiplier:** {self.mills_reincke:.10f}")
        lines.append("")

        lines.append("## Program-Specific Parameters\n")
        for key in self.PROGRAMS:
            p = self.programs[key]
            ce = self.compute_cost_effectiveness(key)
            cap_binds = self.detect_cap_binding(key)
            lines.append(f"### {p.name}\n")
            lines.append(f"- **Cost-effectiveness (x cash):** {ce:.4f}")
            lines.append(f"- **External validity:** {p.external_validity:.10f}")
            lines.append(f"- **Plausibility cap:** {p.plausibility_cap:.4f} (binds: {cap_binds})")
            lines.append(f"- **Pop under-5:** {p.pop_under5:.4f}")
            lines.append(f"- **Baseline mortality under-5:** {p.baseline_mortality_under5:.10f}")
            lines.append(f"- **Baseline mortality over-5:** {p.baseline_mortality_over5:.10f}")
            lines.append(f"- **Adult mortality scaling:** {p.adult_mortality_scaling:.10f}")
            lines.append(f"- **Moral weight under-5:** {p.moral_weight_under5:.4f}")
            lines.append(f"- **Moral weight over-5:** {p.moral_weight_over5:.4f}")
            lines.append(f"- **Cost per person:** {p.cost_per_person:.10f}")
            lines.append(f"- **Consumption:** {p.consumption:.4f}")
            lines.append("")

        return "\n".join(lines)


# ---------------------------------------------------------------------------
# ITN (Insecticide-Treated Nets) CEA
# ---------------------------------------------------------------------------


@dataclass
class ITNProgramParams:
    """Country/program-specific parameters for ITN CEA."""

    name: str
    # Coverage (person-years from Main CEA rows 55-57)
    person_years_u5: float
    person_years_5_14: float
    person_years_over14: float
    # Mortality (rows 70, 73-75, 80-81)
    direct_malaria_mortality_u5: float
    smc_reduction: float
    baseline_net_coverage: float
    malaria_deaths_u5_national: float
    total_malaria_deaths_national: float
    # Incidence (rows 88-89, from Counterfactual malaria sheet)
    incidence_u5_no_nets: float
    incidence_5_14_no_nets: float
    # Per-country resistance (row 66)
    insecticide_resistance: float
    # Final adjustments (Simple CEA rows 32-35)
    additional_benefits_adj: float
    grantee_adj: float
    leverage_adj: float
    funging_adj: float
    # Grant (row 8)
    grant_size: float


class ITNCEA:
    """Reads GiveWell ITN (insecticide-treated nets) CEA and replicates the formula chain.

    Columnar layout: 8 programs across columns I-P of InsecticideCEA.xlsx.
    """

    PROGRAMS = (
        "chad", "drc", "guinea", "nigeria_gf",
        "nigeria_pmi", "south_sudan", "togo", "uganda",
    )

    _COL_MAP: dict[str, str] = {
        "chad": "I", "drc": "J", "guinea": "K", "nigeria_gf": "L",
        "nigeria_pmi": "M", "south_sudan": "N", "togo": "O", "uganda": "P",
    }

    _NAMES: dict[str, str] = {
        "chad": "Chad", "drc": "DRC", "guinea": "Guinea",
        "nigeria_gf": "Nigeria (GF)", "nigeria_pmi": "Nigeria (PMI)",
        "south_sudan": "South Sudan", "togo": "Togo", "uganda": "Uganda",
    }

    def __init__(self, path: Path) -> None:
        self._path = Path(path)
        wb = openpyxl.load_workbook(str(self._path), data_only=True)
        self._read_shared_params(wb)
        self._read_program_params(wb)
        wb.close()

    # ------------------------------------------------------------------
    # Reading helpers
    # ------------------------------------------------------------------

    def _cell(self, ws: Any, ref: str) -> Any:
        val = ws[ref].value
        if val is None:
            raise ValueError(f"Cell {ws.title}!{ref} is None")
        return val

    def _read_shared_params(self, wb: openpyxl.Workbook) -> None:
        ws = wb["Main CEA"]
        self.incidence_reduction: float = float(self._cell(ws, "H62"))
        self.net_usage_trial: float = float(self._cell(ws, "H35"))
        self.internal_validity: float = float(self._cell(ws, "H64"))
        self.external_validity: float = float(self._cell(ws, "H65"))
        self.mortality_incidence_ratio: float = float(self._cell(ws, "H68"))
        self.indirect_deaths_multiplier: float = float(self._cell(ws, "H71"))
        self.over5_relative_efficacy: float = float(self._cell(ws, "H84"))
        self.income_per_case: float = float(self._cell(ws, "H96"))
        self.years_to_benefits: int = int(self._cell(ws, "H98"))
        self.discount_rate: float = float(self._cell(ws, "H99"))
        self.benefit_duration: int = int(self._cell(ws, "H101"))
        self.household_multiplier: float = float(self._cell(ws, "H103"))
        self.moral_weight_u5: float = float(self._cell(ws, "H112"))
        self.moral_weight_over5: float = float(self._cell(ws, "H116"))
        self.ln_consumption_value: float = float(self._cell(ws, "H120"))
        self.benchmark: float = float(self._cell(ws, "H144"))

    def _read_program_params(self, wb: openpyxl.Workbook) -> None:
        ws = wb["Main CEA"]
        sc = wb["Simple CEA"]
        self.programs: dict[str, ITNProgramParams] = {}
        for key, col in self._COL_MAP.items():
            self.programs[key] = ITNProgramParams(
                name=self._NAMES[key],
                person_years_u5=float(self._cell(ws, f"{col}55")),
                person_years_5_14=float(self._cell(ws, f"{col}56")),
                person_years_over14=float(self._cell(ws, f"{col}57")),
                direct_malaria_mortality_u5=float(self._cell(ws, f"{col}70")),
                smc_reduction=float(self._cell(ws, f"{col}73")),
                baseline_net_coverage=float(self._cell(ws, f"{col}75")),
                malaria_deaths_u5_national=float(self._cell(ws, f"{col}80")),
                total_malaria_deaths_national=float(self._cell(ws, f"{col}81")),
                incidence_u5_no_nets=float(self._cell(ws, f"{col}88")),
                incidence_5_14_no_nets=float(self._cell(ws, f"{col}89")),
                insecticide_resistance=float(self._cell(ws, f"{col}66")),
                additional_benefits_adj=float(self._cell(sc, f"{col}32")),
                grantee_adj=float(self._cell(sc, f"{col}33")),
                leverage_adj=float(self._cell(sc, f"{col}34")),
                funging_adj=float(self._cell(sc, f"{col}35")),
                grant_size=float(self._cell(ws, "H8")),
            )

    # ------------------------------------------------------------------
    # Formula chain
    # ------------------------------------------------------------------

    def _expected_reduction(
        self,
        incidence_reduction: float,
        internal_validity: float,
        external_validity: float,
        insecticide_resistance: float,
    ) -> float:
        """Compute expected reduction in malaria incidence/mortality for net sleepers."""
        implied = incidence_reduction / self.net_usage_trial
        return (
            implied
            * (1 + internal_validity)
            * (1 + external_validity)
            * (1 + insecticide_resistance)
        )

    def _annuity_due_factor(self) -> float:
        """Present value of annuity-due (payments at start of period)."""
        r = self.discount_rate
        n = self.benefit_duration
        ordinary = (1 - (1 + r) ** (-n)) / r
        return ordinary * (1 + r)

    def compute_cost_effectiveness(
        self,
        program_key: str,
        **overrides: float,
    ) -> float:
        """Compute cost-effectiveness in multiples of GiveDirectly cash.

        Supported overrides:
            incidence_reduction, internal_validity, external_validity,
            insecticide_resistance, indirect_deaths_multiplier,
            moral_weight_under5, moral_weight_over5
        """
        p = self.programs[program_key]

        ir = overrides.get("incidence_reduction", self.incidence_reduction)
        iv = overrides.get("internal_validity", self.internal_validity)
        ev = overrides.get("external_validity", self.external_validity)
        resist = overrides.get("insecticide_resistance", p.insecticide_resistance)
        indirect = overrides.get("indirect_deaths_multiplier", self.indirect_deaths_multiplier)
        mw_u5 = overrides.get("moral_weight_under5", self.moral_weight_u5)
        mw_o5 = overrides.get("moral_weight_over5", self.moral_weight_over5)

        # --- Expected reduction ---
        exp_red = self._expected_reduction(ir, iv, ev, resist)
        exp_mort_red = exp_red * self.mortality_incidence_ratio

        # --- Malaria mortality in absence of nets ---
        total_mort = p.direct_malaria_mortality_u5 * (1 + indirect)
        adj_mort = total_mort - p.smc_reduction
        denom = 1 - p.baseline_net_coverage * exp_mort_red
        if denom <= 0:
            denom = 1e-9  # avoid division by zero for extreme parameters
        mort_no_nets = adj_mort / denom

        # --- Under-5 deaths averted ---
        deaths_u5 = p.person_years_u5 * mort_no_nets * exp_mort_red

        # --- Over-5 deaths averted ---
        over5_deaths_national = (
            p.total_malaria_deaths_national - p.malaria_deaths_u5_national
        )
        if p.malaria_deaths_u5_national > 0:
            over5_ratio = over5_deaths_national / p.malaria_deaths_u5_national
        else:
            over5_ratio = 0.0
        deaths_over5 = deaths_u5 * over5_ratio * self.over5_relative_efficacy

        # --- Development benefits (long-term income) ---
        cases_u5 = p.person_years_u5 * p.incidence_u5_no_nets * exp_red
        cases_5_14 = p.person_years_5_14 * p.incidence_5_14_no_nets * exp_red
        total_cases = cases_u5 + cases_5_14

        adj_income = math.log(1 + self.income_per_case)
        discounted = adj_income * (1 / (1 + self.discount_rate)) ** self.years_to_benefits
        pv_per_case = discounted * self._annuity_due_factor() * self.household_multiplier
        dev_value = total_cases * pv_per_case * self.ln_consumption_value

        # --- Total value ---
        u5_value = deaths_u5 * mw_u5
        over5_value = deaths_over5 * mw_o5
        total_value = u5_value + over5_value + dev_value

        # --- Initial CE (before final adjustments) ---
        uv_per_dollar = total_value / p.grant_size
        initial_ce = uv_per_dollar / self.benchmark

        # --- Final CE (with project-level adjustments) ---
        final_ce = (
            initial_ce
            * (1 + p.additional_benefits_adj)
            * (1 + p.grantee_adj)
            * (1 + p.leverage_adj + p.funging_adj)
        )

        return final_ce

    def detect_cap_binding(self, program_key: str, **overrides: float) -> bool:
        """ITN CEA does not use plausibility caps."""
        return False

    def run_sensitivity(
        self,
        program_key: str,
        parameter_name: str,
        low: float,
        central: float,
        high: float,
    ) -> dict[str, Any]:
        """Run sensitivity analysis for a single parameter.

        Returns dict with baseline CE, CE at low/central/high,
        percentage changes, and cap binding info.
        """
        baseline_ce = self.compute_cost_effectiveness(program_key)

        results: dict[str, float | bool | str] = {
            "parameter_name": parameter_name,
            "baseline": baseline_ce,
            "cap_binds_baseline": False,
        }

        for label, value in [("low", low), ("central", central), ("high", high)]:
            ce = self.compute_cost_effectiveness(program_key, **{parameter_name: value})
            pct_change = ((ce - baseline_ce) / baseline_ce) * 100 if baseline_ce != 0 else 0.0
            results[label] = ce
            results[f"pct_change_{label}"] = pct_change
            results[f"cap_binds_{label}"] = False

        return results

    def get_parameter_summary(self) -> str:
        """Return a human-readable markdown summary of key parameters and baseline CE."""
        lines: list[str] = []
        lines.append("# Insecticide-Treated Nets CEA — Parameter Summary\n")

        lines.append("## Shared Parameters\n")
        lines.append(f"- **Malaria incidence reduction (Pryce et al.):** {self.incidence_reduction}")
        lines.append(f"- **Net usage in trials:** {self.net_usage_trial}")
        lines.append(f"- **Internal validity adjustment:** {self.internal_validity}")
        lines.append(f"- **External validity adjustment:** {self.external_validity}")
        lines.append(f"- **Indirect deaths per direct death:** {self.indirect_deaths_multiplier}")
        lines.append(f"- **Over-5 relative efficacy:** {self.over5_relative_efficacy}")
        lines.append(f"- **Moral weight under-5:** {self.moral_weight_u5:.4f}")
        lines.append(f"- **Moral weight over-5:** {self.moral_weight_over5:.4f}")
        lines.append(f"- **Income per case averted:** {self.income_per_case}")
        lines.append(f"- **Discount rate:** {self.discount_rate}")
        lines.append(f"- **Benchmark (UoV/$):** {self.benchmark}")
        lines.append("")

        lines.append("## Program-Specific Parameters\n")
        for key in self.PROGRAMS:
            p = self.programs[key]
            ce = self.compute_cost_effectiveness(key)
            lines.append(f"### {p.name}\n")
            lines.append(f"- **Cost-effectiveness (x cash):** {ce:.2f}")
            lines.append(f"- **Insecticide resistance:** {p.insecticide_resistance:.4f}")
            lines.append(f"- **Direct malaria mortality (u5):** {p.direct_malaria_mortality_u5:.6f}")
            lines.append(f"- **SMC reduction:** {p.smc_reduction:.6f}")
            lines.append(f"- **Baseline net coverage:** {p.baseline_net_coverage:.3f}")
            lines.append(f"- **Person-years u5:** {p.person_years_u5:.0f}")
            lines.append(f"- **Person-years 5-14:** {p.person_years_5_14:.0f}")
            lines.append(f"- **Additional benefits adj:** {p.additional_benefits_adj}")
            lines.append(f"- **Leverage + funging adj:** {p.leverage_adj + p.funging_adj:.4f}")
            lines.append("")

        return "\n".join(lines)
