# VAS (Vitamin A Supplementation) Support — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add Vitamin A Supplementation as the 4th intervention in the GiveWell red team pipeline, with a spreadsheet reader class, config integration, and pipeline wiring.

**Architecture:** `VASCEA` class in `pipeline/spreadsheet.py` reads pre-computed CE multiples and parameters from the VAS xlsx file, produces a rich `get_parameter_summary()` for LLM agents. Config and pipeline wiring point the existing 6-stage pipeline at VAS. No formula chain replication — read final values directly.

**Tech Stack:** Python 3.12, openpyxl, pytest, pathlib

---

## Design Decision: No Formula Chain Replication

`WaterCEA`, `ITNCEA`, and `MalariaCEA` replicate their spreadsheet formula chains in Python. This enabled 0% error baseline reproduction and the Bayesian optimization extension on ITNs (varying parameters programmatically and recomputing CE).

**VASCEA intentionally does not replicate the formula chain.** The VAS model spans 5+ sheets with 37 location columns, cross-sheet DUMMYFUNCTION references, and a multi-step external validity adjustment using proxy indicators. Replicating it would be ~300 lines of fragile code for a model that no pipeline stage exercises computationally — the Quantifier agent consumes `get_parameter_summary()` text, not Python values.

**Trade-off:** Any future "Bayesian sweep on VAS parameters" would require a full formula-chain implementation. This is a known debt. If that becomes a goal, start from `Simple CEA` rows 10-37 (the cleanest self-contained chain).

---

## Inspection Provenance

All assertion values in this plan were extracted from live spreadsheet reads during the planning session (2026-04-08). Key verifications performed:

- `data_only=True` resolves DUMMYFUNCTION cells in Inputs rows 24-27 to matching numeric values (cross-checked against Counterfactual mortality sheet)
- Sensitivity analysis uses 3-column groups (25th/Best/75th) per location, with 21 Nigerian locations x 3 = 63 columns bridging the gap between Niger (col 27) and Angola (col 93)
- Main CEA row 4 and Simple CEA row 37 return identical CE multiples (cross-checked for Burkina Faso: both 6.851640881)
- 21 Nigerian entries in cols Q-AK (20 states + FCT/Abuja), yielding 21 non-zero final CE values
- Togo has no VAD survey data (both year and prevalence are "-")

---

## File Map

| Action | File | Responsibility |
|--------|------|----------------|
| Create | `data/VASCEA.xlsx` (symlink) | Symlink to the long-named VAS spreadsheet |
| Modify | `pipeline/spreadsheet.py` | Add `VASLocationParams` dataclass and `VASCEA` class |
| Modify | `pipeline/config.py` | Add `"vas"` entry to `INTERVENTION_URLS` |
| Modify | `pipeline/run_pipeline.py` | Import `VASCEA`, add to `cea_classes` dict |
| Modify | `tests/test_spreadsheet.py` | Add `TestVASCEAReading` test class |

---

### Task 1: Create VASCEA.xlsx symlink

**Files:**
- Create: `data/VASCEA.xlsx` (symlink to `data/GiveWell, CEA of vitamin A supplementation, 2024 v2 (public).xlsx`)

- [ ] **Step 1: Create the symlink**

```bash
cd /home/tsondo/projects/givewell_redteam/data
ln -s "GiveWell, CEA of vitamin A supplementation, 2024 v2 (public).xlsx" VASCEA.xlsx
```

- [ ] **Step 2: Verify the symlink resolves**

```bash
ls -la data/VASCEA.xlsx
python -c "
import openpyxl
wb = openpyxl.load_workbook('data/VASCEA.xlsx', data_only=True)
print('Sheets:', wb.sheetnames)
wb.close()
"
```

Expected: prints `['Key', 'Main CEA', 'Counterfactual mortality', 'External validity', 'LeverageFunging', 'GBD estimates', 'Inputs', 'Simple CEA', 'Sensitivity analysis']`

- [ ] **Step 3: Commit**

```bash
git add data/VASCEA.xlsx
git commit -m "data: add VASCEA.xlsx symlink for pipeline naming consistency"
```

---

### Task 2: Write failing tests for VASCEA

**Files:**
- Modify: `tests/test_spreadsheet.py`

- [ ] **Step 1: Write the test class**

Add at the end of `tests/test_spreadsheet.py`:

```python
from pipeline.spreadsheet import VASCEA

VAS_DATA_PATH = Path(__file__).parent.parent / "data" / "VASCEA.xlsx"

_VAS_EXPECTED_SHEETS = {
    "Key", "Main CEA", "Counterfactual mortality", "External validity",
    "LeverageFunging", "GBD estimates", "Inputs", "Simple CEA",
    "Sensitivity analysis",
}


@pytest.fixture(scope="module")
def vas_cea() -> VASCEA:
    """Load the VAS CEA once for all tests in the module."""
    return VASCEA(VAS_DATA_PATH)


class TestVASCEAReading:
    """Verify that VAS parameters are correctly read from the spreadsheet."""

    def test_required_sheets_present(self) -> None:
        """All 5 sheets that VASCEA reads must exist in the workbook."""
        import openpyxl
        wb = openpyxl.load_workbook(str(VAS_DATA_PATH), data_only=True)
        actual = set(wb.sheetnames)
        wb.close()
        missing = _VAS_EXPECTED_SHEETS - actual
        assert not missing, f"Missing sheets: {missing}"

    def test_locations_loaded(self, vas_cea: VASCEA) -> None:
        """12 non-Nigerian locations + 1 aggregated Nigeria = 13 entries."""
        assert "burkina_faso" in vas_cea.locations
        assert "angola" in vas_cea.locations
        assert "nigeria" in vas_cea.locations
        assert len(vas_cea.locations) == 13

    def test_ce_multiple_burkina_faso(self, vas_cea: VASCEA) -> None:
        """Cross-check: Burkina Faso CE from Simple CEA row 37 col I."""
        loc = vas_cea.locations["burkina_faso"]
        assert loc.ce_multiple == pytest.approx(6.851640881, rel=1e-4)

    def test_ce_multiple_niger(self, vas_cea: VASCEA) -> None:
        """Niger has the highest non-Nigerian CE multiple at ~79x."""
        loc = vas_cea.locations["niger"]
        assert loc.ce_multiple == pytest.approx(79.13069972, rel=1e-4)

    def test_ce_multiple_angola(self, vas_cea: VASCEA) -> None:
        """Angola (Nutrition International) at ~3.69x."""
        loc = vas_cea.locations["angola"]
        assert loc.ce_multiple == pytest.approx(3.690803672, rel=1e-4)

    def test_ce_matches_main_cea_header(self, vas_cea: VASCEA) -> None:
        """Hand-verify: Burkina Faso CE matches Main CEA row 4 (the header echo)."""
        import openpyxl
        wb = openpyxl.load_workbook(str(VAS_DATA_PATH), data_only=True)
        main_cea_val = float(wb["Main CEA"].cell(row=4, column=9).value)
        wb.close()
        assert vas_cea.locations["burkina_faso"].ce_multiple == pytest.approx(
            main_cea_val, rel=1e-6
        )

    def test_cost_per_supplement_burkina_faso(self, vas_cea: VASCEA) -> None:
        loc = vas_cea.locations["burkina_faso"]
        assert loc.cost_per_supplement == pytest.approx(1.5410928, rel=1e-4)

    def test_vad_survey_year_angola(self, vas_cea: VASCEA) -> None:
        """Angola's VAD survey is from 1999 — must be flagged as stale."""
        loc = vas_cea.locations["angola"]
        assert loc.vad_survey_year == 1999

    def test_vad_survey_year_chad(self, vas_cea: VASCEA) -> None:
        loc = vas_cea.locations["chad"]
        assert loc.vad_survey_year == 2008

    def test_vad_survey_year_togo_missing(self, vas_cea: VASCEA) -> None:
        """Togo has no VAD survey (cell is '-')."""
        loc = vas_cea.locations["togo"]
        assert loc.vad_survey_year == 0

    def test_nigeria_is_aggregated(self, vas_cea: VASCEA) -> None:
        """Nigeria aggregates 21 locations (20 states + FCT) into min/max/mean."""
        loc = vas_cea.locations["nigeria"]
        assert loc.n_states == 21
        assert loc.ce_multiple_min == pytest.approx(1.3704, rel=1e-2)
        assert loc.ce_multiple_max == pytest.approx(38.2464, rel=1e-2)
        assert loc.ce_multiple_mean == pytest.approx(6.9547, rel=1e-2)

    def test_nigeria_initial_ce_differs_from_final(self, vas_cea: VASCEA) -> None:
        """Initial CE (before adjustments) must be computed separately, not copied from final."""
        loc = vas_cea.locations["nigeria"]
        # Mean initial CE across 21 states is 5.4081, vs final mean 6.9547
        assert loc.initial_ce_multiple == pytest.approx(5.4081, rel=1e-2)
        assert loc.initial_ce_multiple != pytest.approx(loc.ce_multiple, rel=1e-2)

    def test_nigeria_states_exposed(self, vas_cea: VASCEA) -> None:
        """Individual state CE values should be accessible for the summary."""
        assert len(vas_cea.nigeria_states) == 21
        assert "Sokoto" in vas_cea.nigeria_states
        assert vas_cea.nigeria_states["Sokoto"] == pytest.approx(38.2464, rel=1e-2)
        assert "FCT (Abuja)" in vas_cea.nigeria_states

    def test_shared_params(self, vas_cea: VASCEA) -> None:
        assert vas_cea.grant_size == pytest.approx(1_000_000, rel=1e-6)
        assert vas_cea.rounds_per_year == pytest.approx(2.0, rel=1e-6)
        assert vas_cea.moral_value_under5 == pytest.approx(118.73259, rel=1e-4)

    def test_sensitivity_mortality_effect(self, vas_cea: VASCEA) -> None:
        """Mortality effect is the highest-variance parameter: -80%/+75%."""
        sens = vas_cea.sensitivity["burkina_faso"]
        mort_effect = sens["effect_of_vas_on_mortality"]
        assert mort_effect["pct_change_25th"] == pytest.approx(-0.80, rel=1e-2)
        assert mort_effect["pct_change_75th"] == pytest.approx(0.75, rel=1e-2)

    def test_compute_ce_rejects_overrides(self, vas_cea: VASCEA) -> None:
        """compute_cost_effectiveness must refuse overrides (no formula chain)."""
        with pytest.raises(NotImplementedError):
            vas_cea.compute_cost_effectiveness("burkina_faso", relative_risk=0.5)

    def test_compute_ce_without_overrides(self, vas_cea: VASCEA) -> None:
        """Without overrides, returns the pre-computed CE multiple."""
        ce = vas_cea.compute_cost_effectiveness("burkina_faso")
        assert ce == pytest.approx(6.851640881, rel=1e-4)

    def test_parameter_summary_completeness(self, vas_cea: VASCEA) -> None:
        """Summary must contain all 13 location names and key structural flags."""
        summary = vas_cea.get_parameter_summary()
        assert len(summary) > 500

        # All 13 locations present
        for name in [
            "Burkina Faso", "Cameroon", "Cote d'Ivoire", "DRC", "Guinea",
            "Madagascar", "Mali", "Niger", "Angola", "Chad", "Togo", "Uganda",
            "Nigeria",
        ]:
            assert name in summary, f"Missing location: {name}"

        # Stale survey flags
        assert "1999" in summary  # Angola
        assert "2008" in summary  # Chad

        # Nigeria range string
        import re
        assert re.search(r"range: \d+\.\d+.+\d+\.\d+", summary), \
            "Nigeria range string missing from summary"

        # Per-state breakdown present
        assert "Sokoto" in summary
        assert "Anambra" in summary
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd /home/tsondo/projects/givewell_redteam
python -m pytest tests/test_spreadsheet.py::TestVASCEAReading -v 2>&1 | head -30
```

Expected: `ImportError: cannot import name 'VASCEA' from 'pipeline.spreadsheet'`

- [ ] **Step 3: Commit**

```bash
git add tests/test_spreadsheet.py
git commit -m "test: add failing tests for VASCEA spreadsheet reader"
```

---

### Task 3: Implement VASLocationParams and VASCEA class

**Files:**
- Modify: `pipeline/spreadsheet.py` — add at the end of the file, after the `MalariaCEA` class

- [ ] **Step 1: Add the VASLocationParams dataclass**

Add after the `MalariaCEA` class (after line 983):

```python
# ---------------------------------------------------------------------------
# VAS (Vitamin A Supplementation) CEA
# ---------------------------------------------------------------------------


@dataclass
class VASLocationParams:
    """Per-location parameters for VAS CEA."""

    name: str
    grantee: str  # "Helen Keller International" or "Nutrition International"

    # Final CE (from Simple CEA row 37)
    ce_multiple: float

    # Initial CE before adjustments (Simple CEA row 21)
    initial_ce_multiple: float

    # Cost (Inputs sheet)
    cost_per_supplement: float  # row 18
    pct_costs_grantee: float  # row 11
    pct_costs_ni: float  # row 12 (Nutrition International capsule procurement)
    pct_costs_govt_financial: float  # row 14
    pct_costs_govt_inkind: float  # row 15

    # Mortality (Counterfactual mortality sheet)
    total_under5_deaths: float  # row 8
    early_neonatal_deaths: float  # row 9
    late_neonatal_deaths: float  # row 10
    post_neonatal_deaths: float  # row 11
    mortality_rate_6_59mo: float  # row 24 (annual rate among 6-59mo)

    # External validity
    vad_prevalence: float  # External validity row 8
    vad_survey_year: int  # External validity row 9
    estimated_vad_2021: float  # External validity row 46
    pct_under5_6_59mo: float  # Counterfactual mortality row 22

    # Adjustments (Simple CEA rows 31-34)
    adj_additional_benefits: float  # row 31
    adj_grantee_factors: float  # row 32
    adj_leverage: float  # row 33
    adj_funging: float  # row 34

    # Nigeria aggregation (only populated for the "nigeria" aggregate entry)
    ce_multiple_min: float = 0.0
    ce_multiple_max: float = 0.0
    ce_multiple_mean: float = 0.0
    n_states: int = 0
```

- [ ] **Step 2: Add the VASCEA class — __init__ and reading methods**

Add directly after the `VASLocationParams` dataclass:

```python
class VASCEA:
    """Reads GiveWell VAS CEA and produces a rich parameter summary.

    Unlike WaterCEA/ITNCEA/MalariaCEA, this class reads pre-computed CE
    multiples rather than replicating the formula chain. This is a deliberate
    trade-off: the VAS model spans 5+ sheets with 37 location columns and
    cross-sheet DUMMYFUNCTION references, making replication fragile and
    unnecessary — the pipeline agents consume get_parameter_summary() text,
    not Python computations.

    Consequence: compute_cost_effectiveness() raises NotImplementedError if
    overrides are passed. Any future Bayesian optimization on VAS parameters
    would require a full formula-chain implementation.

    Location layout (Inputs/Simple CEA sheets):
        Col I-P: HKI countries (Burkina Faso through Niger)
        Col Q-AK: 21 Nigerian locations (20 states + FCT), aggregated as one entry
        Col AL-AO: Nutrition International countries (Angola, Chad, Togo, Uganda)
    """

    # Non-Nigerian locations: key -> (column index in Inputs/Simple CEA, grantee)
    _LOC_COLS: dict[str, tuple[int, str]] = {
        "burkina_faso": (9, "Helen Keller International"),
        "cameroon": (10, "Helen Keller International"),
        "cote_divoire": (11, "Helen Keller International"),
        "drc": (12, "Helen Keller International"),
        "guinea": (13, "Helen Keller International"),
        "madagascar": (14, "Helen Keller International"),
        "mali": (15, "Helen Keller International"),
        "niger": (16, "Helen Keller International"),
        "angola": (38, "Nutrition International"),
        "chad": (39, "Nutrition International"),
        "togo": (40, "Nutrition International"),
        "uganda": (41, "Nutrition International"),
    }

    _LOC_NAMES: dict[str, str] = {
        "burkina_faso": "Burkina Faso",
        "cameroon": "Cameroon",
        "cote_divoire": "Cote d'Ivoire",
        "drc": "DRC",
        "guinea": "Guinea",
        "madagascar": "Madagascar",
        "mali": "Mali",
        "niger": "Niger",
        "angola": "Angola",
        "chad": "Chad",
        "togo": "Togo",
        "uganda": "Uganda",
    }

    # Nigerian location columns: Q=17 through AK=37 (20 states + FCT)
    _NIGERIA_COLS: dict[str, int] = {
        "Adamawa": 17, "Akwa Ibom": 18, "Anambra": 19, "Benue": 20,
        "Delta": 21, "Ebonyi": 22, "Edo": 23, "Ekiti": 24,
        "Imo": 25, "Kogi": 26, "Nasarawa": 27, "Ogun": 28,
        "Osun": 29, "Rivers": 30, "Taraba": 31, "Kaduna": 32,
        "Niger": 33, "Plateau": 34, "Sokoto": 35, "Kebbi": 36,
        "FCT (Abuja)": 37,
    }

    # Sensitivity analysis: location -> start column (3 cols each: 25th, best, 75th)
    # Gap between Niger (col 27) and Angola (col 93) spans 21 Nigerian locations x 3 = 63 cols
    _SENS_COLS: dict[str, int] = {
        "burkina_faso": 6, "cameroon": 9, "cote_divoire": 12,
        "drc": 15, "guinea": 18, "madagascar": 21,
        "mali": 24, "niger": 27,
        "angola": 93, "chad": 96, "togo": 99, "uganda": 102,
    }

    # Sensitivity parameter rows (percentage-change section, rows 56-67)
    _SENS_ROWS: dict[str, int] = {
        "cost_per_person": 56,
        "counterfactual_coverage": 57,
        "mortality_rate": 58,
        "effect_of_vas_on_mortality": 59,
        "developmental_benefits": 62,
        "additional_benefits_downsides": 65,
        "grantee_factors": 66,
        "funging": 67,
    }

    def __init__(self, path: Path) -> None:
        self._path = Path(path)
        wb = openpyxl.load_workbook(str(self._path), data_only=True)
        self._read_shared(wb)
        self._read_locations(wb)
        self._read_nigeria_aggregate(wb)
        self._read_sensitivity(wb)
        wb.close()

    def _safe_float(self, ws: Any, row: int, col: int, default: float = 0.0) -> float:
        """Read a cell as float, returning default for None or non-numeric values."""
        val = ws.cell(row=row, column=col).value
        if val is None or val == "-" or val == "":
            return default
        try:
            return float(val)
        except (ValueError, TypeError):
            return default

    def _safe_int(self, ws: Any, row: int, col: int, default: int = 0) -> int:
        """Read a cell as int, returning default for None or non-numeric values."""
        val = ws.cell(row=row, column=col).value
        if val is None or val == "-" or val == "" or val == "n/a":
            return default
        try:
            return int(float(val))
        except (ValueError, TypeError):
            return default

    def _read_shared(self, wb: openpyxl.Workbook) -> None:
        """Read shared (non-location-specific) parameters."""
        inp = wb["Inputs"]
        sc = wb["Simple CEA"]
        cm = wb["Counterfactual mortality"]

        self.grant_size: float = float(inp.cell(row=8, column=8).value)  # H8
        self.rounds_per_year: float = float(inp.cell(row=19, column=8).value)  # H19
        self.moral_value_under5: float = float(sc.cell(row=20, column=8).value)  # Simple CEA H20
        # Used in Counterfactual mortality to split post-neonatal deaths into
        # 1-5mo (VAS-ineligible) and 6-59mo (VAS-eligible). Surfaced in summary
        # because it directly affects the denominator of lives-saved calculations.
        self.prop_postneonatal_1_5mo: float = float(cm.cell(row=14, column=8).value)  # CM H14

    def _read_locations(self, wb: openpyxl.Workbook) -> None:
        """Read per-location parameters for all non-Nigerian locations."""
        inp = wb["Inputs"]
        sc = wb["Simple CEA"]
        cm = wb["Counterfactual mortality"]
        ev = wb["External validity"]

        self.locations: dict[str, VASLocationParams] = {}

        for key, (col, grantee) in self._LOC_COLS.items():
            self.locations[key] = VASLocationParams(
                name=self._LOC_NAMES[key],
                grantee=grantee,
                ce_multiple=self._safe_float(sc, 37, col),
                initial_ce_multiple=self._safe_float(sc, 21, col),
                cost_per_supplement=self._safe_float(inp, 18, col),
                pct_costs_grantee=self._safe_float(inp, 11, col),
                pct_costs_ni=self._safe_float(inp, 12, col),
                pct_costs_govt_financial=self._safe_float(inp, 14, col),
                pct_costs_govt_inkind=self._safe_float(inp, 15, col),
                total_under5_deaths=self._safe_float(cm, 8, col),
                early_neonatal_deaths=self._safe_float(cm, 9, col),
                late_neonatal_deaths=self._safe_float(cm, 10, col),
                post_neonatal_deaths=self._safe_float(cm, 11, col),
                mortality_rate_6_59mo=self._safe_float(cm, 24, col),
                vad_prevalence=self._safe_float(ev, 8, col),
                vad_survey_year=self._safe_int(ev, 9, col),
                estimated_vad_2021=self._safe_float(ev, 46, col),
                pct_under5_6_59mo=self._safe_float(cm, 22, col),
                adj_additional_benefits=self._safe_float(sc, 31, col),
                adj_grantee_factors=self._safe_float(sc, 32, col),
                adj_leverage=self._safe_float(sc, 33, col),
                adj_funging=self._safe_float(sc, 34, col),
            )

    def _read_nigeria_aggregate(self, wb: openpyxl.Workbook) -> None:
        """Aggregate 21 Nigerian locations (20 states + FCT) into a single summary entry."""
        sc = wb["Simple CEA"]
        inp = wb["Inputs"]
        cm = wb["Counterfactual mortality"]
        ev = wb["External validity"]

        state_final_ce: list[float] = []
        state_initial_ce: list[float] = []
        state_costs: list[float] = []
        total_deaths = 0.0
        total_early_neo = 0.0
        total_late_neo = 0.0
        total_post_neo = 0.0

        self.nigeria_states: dict[str, float] = {}

        for state_name, col in self._NIGERIA_COLS.items():
            final_ce = self._safe_float(sc, 37, col)
            initial_ce = self._safe_float(sc, 21, col)
            if final_ce > 0:
                state_final_ce.append(final_ce)
                self.nigeria_states[state_name] = final_ce
            if initial_ce > 0:
                state_initial_ce.append(initial_ce)
            cost = self._safe_float(inp, 18, col)
            if cost > 0:
                state_costs.append(cost)
            total_deaths += self._safe_float(cm, 8, col)
            total_early_neo += self._safe_float(cm, 9, col)
            total_late_neo += self._safe_float(cm, 10, col)
            total_post_neo += self._safe_float(cm, 11, col)

        # Use first Nigerian location column (Q=17) for shared fields
        first_col = 17
        mean_final = sum(state_final_ce) / len(state_final_ce) if state_final_ce else 0.0
        mean_initial = sum(state_initial_ce) / len(state_initial_ce) if state_initial_ce else 0.0

        self.locations["nigeria"] = VASLocationParams(
            name="Nigeria (20 states + FCT)",
            grantee="Helen Keller International",
            ce_multiple=mean_final,
            initial_ce_multiple=mean_initial,
            cost_per_supplement=sum(state_costs) / len(state_costs) if state_costs else 0.0,
            pct_costs_grantee=self._safe_float(inp, 11, first_col),
            pct_costs_ni=self._safe_float(inp, 12, first_col),
            pct_costs_govt_financial=self._safe_float(inp, 14, first_col),
            pct_costs_govt_inkind=self._safe_float(inp, 15, first_col),
            total_under5_deaths=total_deaths,
            early_neonatal_deaths=total_early_neo,
            late_neonatal_deaths=total_late_neo,
            post_neonatal_deaths=total_post_neo,
            mortality_rate_6_59mo=self._safe_float(cm, 24, first_col),
            vad_prevalence=self._safe_float(ev, 8, first_col),
            vad_survey_year=self._safe_int(ev, 9, first_col),
            estimated_vad_2021=self._safe_float(ev, 46, first_col),
            pct_under5_6_59mo=self._safe_float(cm, 22, first_col),
            adj_additional_benefits=self._safe_float(sc, 31, first_col),
            adj_grantee_factors=self._safe_float(sc, 32, first_col),
            adj_leverage=self._safe_float(sc, 33, first_col),
            adj_funging=self._safe_float(sc, 34, first_col),
            ce_multiple_min=min(state_final_ce) if state_final_ce else 0.0,
            ce_multiple_max=max(state_final_ce) if state_final_ce else 0.0,
            ce_multiple_mean=mean_final,
            n_states=len(state_final_ce),
        )

    def _read_sensitivity(self, wb: openpyxl.Workbook) -> None:
        """Read sensitivity percentage changes from the Sensitivity analysis sheet."""
        sa = wb["Sensitivity analysis"]

        self.sensitivity: dict[str, dict[str, dict[str, float]]] = {}
        for loc_key, start_col in self._SENS_COLS.items():
            loc_sens: dict[str, dict[str, float]] = {}
            for param_name, row in self._SENS_ROWS.items():
                pct_25th = self._safe_float(sa, row, start_col)      # 25th percentile col
                pct_75th = self._safe_float(sa, row, start_col + 2)  # 75th percentile col
                loc_sens[param_name] = {
                    "pct_change_25th": pct_25th,
                    "pct_change_75th": pct_75th,
                }
            self.sensitivity[loc_key] = loc_sens
```

- [ ] **Step 3: Add the get_parameter_summary method to VASCEA**

Add as a method of the `VASCEA` class:

```python
    def get_parameter_summary(self) -> str:
        """Return a rich markdown summary for LLM agent consumption."""
        lines: list[str] = []
        lines.append("# Vitamin A Supplementation (VAS) CEA — Parameter Summary\n")

        lines.append("## Model Overview\n")
        lines.append(
            "This CEA estimates the cost-effectiveness of vitamin A supplementation "
            "programs funded via Helen Keller International (HKI) and Nutrition "
            "International (NI). It covers 37 location columns: 8 HKI countries, "
            "21 Nigerian locations (20 states + FCT, HKI), and 4 NI countries. "
            "The model calculates cost-effectiveness as multiples of GiveDirectly's "
            "unconditional cash transfer program.\n"
        )

        lines.append("## Key Shared Parameters\n")
        lines.append(f"- **Grant size:** ${self.grant_size:,.0f}")
        lines.append(f"- **Supplementation rounds per year:** {self.rounds_per_year:.0f}")
        lines.append(f"- **Moral value of averting an under-5 death:** {self.moral_value_under5:.5f} UoV")
        lines.append(
            f"- **Proportion of post-neonatal deaths among 1-5 month-olds:** "
            f"{self.prop_postneonatal_1_5mo:.2f} (used to estimate VAS-eligible "
            f"6-59 month mortality from total under-5 mortality)"
        )
        lines.append("")

        lines.append("## Per-Location Parameters\n")
        lines.append(
            "| Location | Grantee | CE Multiple (x-cash) | Cost/Supplement | "
            "VAD Prevalence | VAD Survey Year | Mortality Rate (6-59mo) |"
        )
        lines.append("|---|---|---|---|---|---|---|")

        for key in list(self._LOC_COLS.keys()) + ["nigeria"]:
            loc = self.locations[key]
            if key == "nigeria":
                ce_str = (
                    f"{loc.ce_multiple_mean:.2f} "
                    f"(range: {loc.ce_multiple_min:.2f}-{loc.ce_multiple_max:.2f}, "
                    f"{loc.n_states} locations)"
                )
            else:
                ce_str = f"{loc.ce_multiple:.2f}"
            year_str = str(loc.vad_survey_year) if loc.vad_survey_year > 0 else "N/A"
            vad_str = f"{loc.vad_prevalence:.1%}" if loc.vad_prevalence > 0 else "N/A"
            mort_str = f"{loc.mortality_rate_6_59mo:.6f}" if loc.mortality_rate_6_59mo > 0 else "N/A"
            lines.append(
                f"| {loc.name} | {loc.grantee} | {ce_str} | "
                f"${loc.cost_per_supplement:.2f} | {vad_str} | {year_str} | {mort_str} |"
            )
        lines.append("")

        # Per-state Nigeria breakdown
        lines.append("### Nigerian State/FCT Breakdown\n")
        lines.append("| State/Territory | CE Multiple (x-cash) |")
        lines.append("|---|---|")
        for state_name, ce in sorted(self.nigeria_states.items(), key=lambda x: -x[1]):
            lines.append(f"| {state_name} | {ce:.2f} |")
        lines.append("")

        lines.append("## Adjustment Factors (from Simple CEA)\n")
        lines.append(
            "| Location | Additional Benefits | Grantee Factors | Leverage | Funging |"
        )
        lines.append("|---|---|---|---|---|")
        for key in list(self._LOC_COLS.keys()) + ["nigeria"]:
            loc = self.locations[key]
            lines.append(
                f"| {loc.name} | {loc.adj_additional_benefits:.3f} | "
                f"{loc.adj_grantee_factors:+.3f} | "
                f"{loc.adj_leverage:+.4f} | {loc.adj_funging:+.4f} |"
            )
        lines.append("")

        lines.append("## Sensitivity Analysis — Highest-Variance Parameters\n")
        lines.append(
            "Percentage change in final CE when each parameter moves to its "
            "25th or 75th percentile value:\n"
        )
        for loc_key, loc_name in [("burkina_faso", "Burkina Faso"), ("angola", "Angola")]:
            if loc_key not in self.sensitivity:
                continue
            sens = self.sensitivity[loc_key]
            lines.append(f"### {loc_name}\n")
            lines.append("| Parameter | 25th %ile Change | 75th %ile Change |")
            lines.append("|---|---|---|")
            for param, vals in sens.items():
                label = param.replace("_", " ").title()
                lines.append(
                    f"| {label} | {vals['pct_change_25th']:+.1%} | "
                    f"{vals['pct_change_75th']:+.1%} |"
                )
            lines.append("")

        lines.append("## Structural Concerns\n")

        # Flag stale VAD surveys
        stale_surveys: list[str] = []
        for key, loc in self.locations.items():
            if 0 < loc.vad_survey_year < 2015:
                stale_surveys.append(
                    f"- **{loc.name}**: VAD survey from {loc.vad_survey_year} "
                    f"({2024 - loc.vad_survey_year} years old). Estimated 2021 "
                    f"prevalence ({loc.estimated_vad_2021:.1%}) is extrapolated "
                    f"from proxy indicators, not direct measurement."
                )
        if stale_surveys:
            lines.append("### Stale VAD Prevalence Data\n")
            lines.extend(stale_surveys)
            lines.append("")

        lines.append("### DUMMYFUNCTION Cells in Inputs Sheet\n")
        lines.append(
            "Inputs rows 24-27 (mortality data) use `IFERROR(DUMMYFUNCTION(...))` "
            "formulas that resolve to numeric fallback values. These values match "
            "the raw GBD data in the Counterfactual mortality sheet. The pipeline "
            "reads from Counterfactual mortality directly.\n"
        )

        lines.append("### Nigerian State Disaggregation Asymmetry\n")
        ng = self.locations["nigeria"]
        lines.append(
            f"21 Nigerian locations (20 states + FCT) have individual columns "
            f"but share many national-level parameters. CE multiples range from "
            f"{ng.ce_multiple_min:.2f}x to {ng.ce_multiple_max:.2f}x, a "
            f"{ng.ce_multiple_max / ng.ce_multiple_min:.0f}x spread driven "
            f"primarily by cost and mortality differences. See the per-state "
            f"table above for the full breakdown.\n"
        )

        lines.append("### Static Mortality Effect\n")
        lines.append(
            "The VAS mortality effect estimate is applied as a single scalar "
            "across all locations. This is the highest-variance parameter in the "
            "sensitivity analysis (25th/75th percentile: -80%/+75% change in CE). "
            "Temporal trends in disease burden are not modeled.\n"
        )

        lines.append("### VAD Deficiency as Mediator\n")
        lines.append(
            "The external validity adjustment uses proxy indicators (stunting, "
            "wasting, poverty rates) rather than direct VAD measurement for most "
            "locations. Changes in these proxies are weighted equally (1/3 each) "
            "to estimate changes in VAD prevalence over time.\n"
        )

        return "\n".join(lines)
```

- [ ] **Step 4: Add interface methods that fail loud on misuse**

```python
    def compute_cost_effectiveness(self, program_key: str, **overrides: float) -> float:
        """Return the pre-computed CE multiple for a location.

        Raises NotImplementedError if overrides are passed — VASCEA reads
        pre-computed values and cannot recompute with different parameters.
        """
        if overrides:
            raise NotImplementedError(
                "VASCEA reads pre-computed CE multiples and cannot recompute "
                "with overrides. A full formula-chain implementation would be "
                "needed for parameter sweeps."
            )
        return self.locations[program_key].ce_multiple

    def detect_cap_binding(self, program_key: str, **overrides: float) -> bool:
        """No plausibility cap concept in the VAS model."""
        return False

    def run_sensitivity(
        self,
        program_key: str,
        parameter_name: str,
        low: float,
        central: float,
        high: float,
    ) -> dict[str, Any]:
        """Return pre-computed sensitivity data from the Sensitivity analysis sheet.

        Unlike WaterCEA/ITNCEA, this returns spreadsheet-sourced percentage changes
        rather than recomputing CE at each parameter value.
        """
        if program_key in self.sensitivity and parameter_name in self.sensitivity[program_key]:
            sens = self.sensitivity[program_key][parameter_name]
            baseline = self.locations[program_key].ce_multiple
            return {
                "parameter_name": parameter_name,
                "baseline": baseline,
                "cap_binds_baseline": False,
                "low": baseline * (1 + sens["pct_change_25th"]),
                "central": baseline,
                "high": baseline * (1 + sens["pct_change_75th"]),
                "pct_change_low": sens["pct_change_25th"] * 100,
                "pct_change_central": 0.0,
                "pct_change_high": sens["pct_change_75th"] * 100,
                "cap_binds_low": False,
                "cap_binds_central": False,
                "cap_binds_high": False,
            }
        return {
            "parameter_name": parameter_name,
            "baseline": self.locations.get(program_key, self.locations["burkina_faso"]).ce_multiple,
        }
```

- [ ] **Step 5: Run tests**

```bash
cd /home/tsondo/projects/givewell_redteam
python -m pytest tests/test_spreadsheet.py::TestVASCEAReading -v
```

Expected: all 19 tests pass.

- [ ] **Step 6: Commit**

```bash
git add pipeline/spreadsheet.py
git commit -m "feat: add VASCEA spreadsheet reader with parameter summary"
```

---

### Task 4: Wire VAS into config.py and run_pipeline.py

**Files:**
- Modify: `pipeline/config.py:61-77` — add `"vas"` to `INTERVENTION_URLS`
- Modify: `pipeline/run_pipeline.py:33` — import `VASCEA`, add to `cea_classes`

- [ ] **Step 1: Add VAS to INTERVENTION_URLS in config.py**

After the `"smc"` entry (line 76), add:

```python
    "vas": {
        "report": "https://www.givewell.org/international/technical/programs/vitamin-A",
        "baseline": "",
        "spreadsheet": "VASCEA.xlsx",
    },
```

- [ ] **Step 2: Update run_pipeline.py imports**

Change line 33 from:
```python
from pipeline.spreadsheet import ITNCEA, MalariaCEA, WaterCEA
```
to:
```python
from pipeline.spreadsheet import ITNCEA, MalariaCEA, VASCEA, WaterCEA
```

- [ ] **Step 3: Add VASCEA to cea_classes dict**

Change lines 125-129 from:
```python
    cea_classes = {
        "water-chlorination": WaterCEA,
        "itns": ITNCEA,
        "smc": MalariaCEA,
    }
```
to:
```python
    cea_classes = {
        "water-chlorination": WaterCEA,
        "itns": ITNCEA,
        "smc": MalariaCEA,
        "vas": VASCEA,
    }
```

- [ ] **Step 4: Verify the CLI accepts "vas" as an intervention**

```bash
cd /home/tsondo/projects/givewell_redteam
python -m pipeline.run_pipeline --help 2>&1 | grep -A1 intervention
python -c "
from pipeline.config import INTERVENTION_URLS
assert 'vas' in INTERVENTION_URLS
print('VAS config entry:', INTERVENTION_URLS['vas'])
"
```

Expected: `vas` appears in choices, config entry prints correctly.

- [ ] **Step 5: Commit**

```bash
git add pipeline/config.py pipeline/run_pipeline.py
git commit -m "feat: wire VAS intervention into pipeline config and orchestrator"
```

---

### Task 5: Integration tests and pipeline smoke test

**Files:** None (verification only)

- [ ] **Step 1: Run full test suite**

```bash
cd /home/tsondo/projects/givewell_redteam
python -m pytest tests/ -v
```

Expected: all existing tests (Water, ITN) plus 19 new VAS tests pass. Zero regressions.

- [ ] **Step 2: Smoke-test the orchestrator's call path into VASCEA**

This exercises the same code path `run_pipeline.py` uses to load and summarize the CEA, without making API calls:

```bash
python -c "
from pipeline.config import DATA_DIR, INTERVENTION_URLS
from pipeline.spreadsheet import ITNCEA, MalariaCEA, VASCEA, WaterCEA

# Replicate the exact logic from run_pipeline.py lines 123-133
urls = INTERVENTION_URLS['vas']
spreadsheet_path = DATA_DIR / urls['spreadsheet']
cea_classes = {
    'water-chlorination': WaterCEA,
    'itns': ITNCEA,
    'smc': MalariaCEA,
    'vas': VASCEA,
}
cea_cls = cea_classes['vas']
cea = cea_cls(spreadsheet_path)
summary = cea.get_parameter_summary()

# Validate the summary the agents will receive
assert 'Burkina Faso' in summary
assert 'Nigeria' in summary
assert '1999' in summary  # Angola stale survey
assert 'Sokoto' in summary  # per-state table
print(f'Summary length: {len(summary)} chars')
print('First 500 chars:')
print(summary[:500])
print('...')
print('SMOKE TEST PASSED')
"
```

Expected: `SMOKE TEST PASSED` with a summary of ~3000-5000 chars.

- [ ] **Step 3: Print full summary for manual review**

```bash
python -c "
from pipeline.spreadsheet import VASCEA
from pathlib import Path
cea = VASCEA(Path('data/VASCEA.xlsx'))
print(cea.get_parameter_summary())
"
```

Expected: full summary with all sections (overview, shared params, per-location table, Nigeria breakdown, adjustments, sensitivity, structural concerns).

- [ ] **Step 4: Commit if any fixes were needed**

Only if changes were required to fix test failures.

---

## Carry-Over Reminders

- **No API access required for Tasks 1-5.** The API key can stay deactivated until the actual pipeline run.
- **When running the full pipeline** (`python pipeline/run_pipeline.py vas`), confirm the Verifier batching optimization from SMC is active — that's the ~70% cost lever.
- **Empty baseline is expected.** `baseline=""` will be passed to the Decomposer and Synthesizer. The prompts handle this gracefully (skip comparison section).
