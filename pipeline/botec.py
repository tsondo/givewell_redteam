"""CEA reader for prose back-of-the-envelope calculations (BOTECs).

GiveWell CEAs arrive as spreadsheets and are read by the classes in
spreadsheet.py. Some funders publish their analyses as short prose BOTECs
instead. This module replicates such a BOTEC as an explicit formula chain so
the quantifier stage can run real sensitivity analysis against it, through the
same CEAReader protocol the spreadsheet classes implement.

Parameters are loaded from a JSON file so the published numbers live in data/
alongside the other inputs, not in code.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

# Parameters that are fractions. The quantifier often writes these as
# percentages ("40%" or "30"); values above 1 are converted to fractions so a
# "30" for p_success is read as 0.30, not as a 30x multiplier.
_FRACTION_PARAMS: frozenset[str] = frozenset({
    "decline_per_year",
    "adult_uptake",
    "baseline_mortality",
    "relative_reduction",
    "p_success",
})


class TBStatinsBOTEC:
    """Coefficient Giving's TB statins sample BOTEC (May 2025).

    Formula chain, as published:
        eligible   = eligible_people_at_8y * (1 - decline_per_year) ** (years_to_adoption - 8)
        treated    = eligible * adult_uptake
        deaths/yr  = treated * baseline_mortality * relative_reduction
        benefit    = deaths/yr * speedup_years * dalys_per_death * op_per_daly   ($OP)
        SROI       = benefit / all_in_cost * p_success

    The output is social return on investment (higher is better), not a
    multiple of cash. CG's Global Health and Wellbeing bar is about 2,000x.
    """

    PROGRAMS: tuple[str, ...] = ("tb_statins",)
    BAR: float = 2000.0

    # Human-readable names the quantifier may use -> parameter keys.
    # Substring match on the lowercased name; more specific keys first.
    PARAM_NAME_MAP: dict[str, str] = {
        "eligible": "eligible_people_at_8y",
        "people who could benefit": "eligible_people_at_8y",
        "patients per year": "eligible_people_at_8y",
        "years to adoption": "years_to_adoption",
        "years_to_adoption": "years_to_adoption",
        "time to adoption": "years_to_adoption",
        "adoption timeline": "years_to_adoption",
        "phase iii completion": "years_to_adoption",
        "decline": "decline_per_year",
        "uptake": "adult_uptake",
        "baseline mortality": "baseline_mortality",
        "case fatality": "baseline_mortality",
        "tb mortality": "baseline_mortality",
        "relative reduction": "relative_reduction",
        "relative mortality reduction": "relative_reduction",
        "mortality reduction": "relative_reduction",
        "treatment effect": "relative_reduction",
        "effect size": "relative_reduction",
        "dalys per death": "dalys_per_death",
        "dalys_per_death": "dalys_per_death",
        "value per daly": "op_per_daly",
        "per daly": "op_per_daly",
        "speedup": "speedup_years",
        "acceleration": "speedup_years",
        "all-in cost": "all_in_cost",
        "all_in_cost": "all_in_cost",
        "total cost": "all_in_cost",
        "cost": "all_in_cost",
        "probability of success": "p_success",
        "p_success": "p_success",
        "success probability": "p_success",
    }

    def __init__(self, path: Path) -> None:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        self.params: dict[str, float] = {k: float(v) for k, v in data["parameters"].items()}
        self.source: str = data.get("source", "")
        self.published_sroi: float = float(data.get("published_sroi", 0.0))

    def _normalize(self, key: str, value: float) -> float:
        if key in _FRACTION_PARAMS and value > 1.0:
            return value / 100.0
        return value

    def compute_components(self, **overrides: float) -> dict[str, float]:
        unknown = set(overrides) - set(self.params)
        if unknown:
            raise KeyError(f"unknown BOTEC parameters: {sorted(unknown)}")
        p = {**self.params, **{k: self._normalize(k, v) for k, v in overrides.items()}}
        eligible = p["eligible_people_at_8y"] * (1 - p["decline_per_year"]) ** (p["years_to_adoption"] - 8)
        treated = eligible * p["adult_uptake"]
        deaths = treated * p["baseline_mortality"] * p["relative_reduction"]
        dalys = deaths * p["speedup_years"] * p["dalys_per_death"]
        benefit = dalys * p["op_per_daly"]
        sroi = benefit / p["all_in_cost"] * p["p_success"]
        return {"eligible": eligible, "treated": treated, "deaths_per_year": deaths,
                "dalys": dalys, "benefit_op": benefit, "sroi": sroi}

    def compute_cost_effectiveness(self, program_key: str, **overrides: float) -> float:
        if program_key not in self.PROGRAMS:
            raise KeyError(program_key)
        return self.compute_components(**overrides)["sroi"]

    def detect_cap_binding(self, program_key: str, **overrides: float) -> bool:
        """No plausibility cap in this BOTEC."""
        return False

    def run_sensitivity(
        self,
        program_key: str,
        parameter_name: str,
        low: float,
        central: float,
        high: float,
    ) -> dict[str, Any]:
        baseline = self.compute_cost_effectiveness(program_key)
        results: dict[str, Any] = {
            "parameter_name": parameter_name,
            "baseline": baseline,
            "cap_binds_baseline": False,
        }
        for label, value in (("low", low), ("central", central), ("high", high)):
            ce = self.compute_cost_effectiveness(program_key, **{parameter_name: value})
            results[label] = ce
            results[f"pct_change_{label}"] = (ce - baseline) / baseline * 100 if baseline else 0.0
            results[f"cap_binds_{label}"] = False
            results[f"crosses_bar_{label}"] = (ce < self.BAR) != (baseline < self.BAR)
        return results

    def get_parameter_summary(self) -> str:
        c = self.compute_components()
        p = self.params
        lines = [
            "# TB statins BOTEC (Coefficient Giving) — Parameter Summary\n",
            "Units: Open Phil dollars ($OP). 1 DALY = $OP 100,000. Output is SROI "
            "(expected $OP per dollar of all-in cost; higher is better). "
            f"Funding bar: {self.BAR:,.0f}x.\n",
            "## Parameters (names are the model's parameter keys)\n",
            f"- **eligible_people_at_8y:** {p['eligible_people_at_8y']:,.0f} drug-susceptible TB patients/yr when Phase III finishes",
            f"- **years_to_adoption:** {p['years_to_adoption']:g} years from grant to adoption",
            f"- **decline_per_year:** {p['decline_per_year']:.2f} annual decline in new TB cases",
            f"- **adult_uptake:** {p['adult_uptake']:.2f}",
            f"- **baseline_mortality:** {p['baseline_mortality']:.2f} among treated drug-susceptible patients",
            f"- **relative_reduction:** {p['relative_reduction']:.2f} relative mortality reduction from atorvastatin",
            f"- **dalys_per_death:** {p['dalys_per_death']:g}",
            f"- **op_per_daly:** {p['op_per_daly']:,.0f}",
            f"- **speedup_years:** {p['speedup_years']:g} years of accelerated adoption credited to the grant",
            f"- **all_in_cost:** ${p['all_in_cost']:,.0f} (all funders, through Phase III and guideline change)",
            f"- **p_success:** {p['p_success']:.2f} probability Phase II and III both succeed",
            "",
            "## Formula chain\n",
            "eligible = eligible_people_at_8y x (1 - decline_per_year)^(years_to_adoption - 8); "
            "treated = eligible x adult_uptake; deaths/yr = treated x baseline_mortality x relative_reduction; "
            "benefit = deaths/yr x speedup_years x dalys_per_death x op_per_daly; "
            "SROI = benefit / all_in_cost x p_success. No time discounting; only mortality is valued.",
            "",
            "## Baseline outputs\n",
            f"- **Deaths averted per year:** {c['deaths_per_year']:,.0f}",
            f"- **DALYs credited:** {c['dalys']:,.0f}",
            f"- **Benefit:** $OP {c['benefit_op']:,.0f}",
            f"- **SROI:** {c['sroi']:,.0f}x (published: about {self.published_sroi:,.0f}x)",
        ]
        return "\n".join(lines)
