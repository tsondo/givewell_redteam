# CLAUDE Code Instruction: Phase 4 — Vitamin A Supplementation (VAS)

## Context

This is Phase 4 of the GiveWell Red Team pipeline. Phases 1–3 covered water
chlorination, ITNs, and SMC. The pipeline architecture, prompts, config, and
spreadsheet reader are already built and working at
`/home/tsondo/projects/givewell_redteam/`.

You are adding support for a new intervention: **Vitamin A Supplementation
(VAS)**, funded via Helen Keller International and Nutrition International.

---

## Before You Do Anything

1. Read `CLAUDE.md` in the repo root.
2. Read `docs/architecture.md`.
3. Read `pipeline/config.py` — you will be adding an entry here.
4. Read `pipeline/spreadsheet.py` — you will be adding a `VASCEA` class here.
5. Read the existing CEA classes (`WaterCEA`, `ITNCEA`, `MalariaCEA`) to
   understand the pattern before writing anything new.

Do not write code until you have read all five files and produced a plan.

---

## Task 1: Place the Spreadsheet

The VAS CEA spreadsheet has already been inspected.
 Location:  '/home/tsondo/projects/givewell_redteam/data/GiveWell, CEA of vitamin A supplementation, 2024 v2 (public).xlsx'
```

## Task 2: Understand the Spreadsheet Structure

The VAS spreadsheet has 9 sheets:

| Sheet | Purpose |
|---|---|
| Key | Terminology and sheet guide |
| Main CEA | Primary calculations (37 location columns) |
| Counterfactual mortality | Under-5 mortality calculations per location |
| External validity | VAD prevalence and proxy adjustments |
| LeverageFunging | Upstream/downstream spending adjustments |
| GBD estimates | Raw GBD 2021 mortality and VAD prevalence data |
| Inputs | All manually-entered parameters (your primary read target) |
| Simple CEA | Simplified version for sensitivity |
| Sensitivity analysis | 25th/75th percentile ranges for all key inputs |

**Critical structural note:** The `Inputs` sheet uses
`IFERROR(__xludf.DUMMYFUNCTION(...))` for mortality inputs (rows 24–27). These
evaluate to their IFERROR fallback values when read with openpyxl. The actual
mortality values live as raw data in `GBD estimates` and must be read from
there directly.

**Location structure:** 37 columns spanning:
- HKI: Burkina Faso, Cameroon, Côte d'Ivoire, DRC, Guinea, Madagascar, Mali, Niger
- HKI Nigeria: 20 states (Adamawa through FCT/Abuja)
- Nutrition International: Angola, Chad, Togo, Uganda

Column mapping (Inputs sheet, row 2–3 headers):
- Col H = All locations (aggregate)
- Col I = Burkina Faso
- Col J = Cameroon
- Col K = Côte d'Ivoire
- Col L = DRC
- Col M = Guinea
- Col N = Madagascar
- Col O = Mali
- Col P = Niger
- Cols Q–AK = Nigerian states (20 states)
- Col AL = Angola
- Col AM = Chad
- Col AN = Togo
- Col AO = Uganda

---

## Task 3: Write VASCEA in pipeline/spreadsheet.py

Add a `VASCEA` class following the pattern of `MalariaCEA`. Use
`data_only=True` when loading — this reads computed cell values, not formulas.

The class must implement `get_parameter_summary() -> str` returning a
structured text summary that the Decomposer and Quantifier agents can use.

**Key parameters to extract from `Inputs` sheet:**

From row 8: Grant size (col H = $1,000,000 placeholder — note this)
From row 11: % costs covered by grantee (per location)
From row 12: % costs covered by Nutrition International (per location)
From row 18: Cost per VAS supplement delivered (per location — highly variable,
  e.g. Burkina Faso ~$1.54, Niger ~$0.49, DRC ~$0.57)
From row 19: Supplementation rounds per year (col H = 2.0)

**Mortality parameters — read from GBD estimates sheet directly:**

The GBD sheet has raw mortality data in a wide multi-table layout starting at
row 2. You need:
- All-cause under-5 deaths (2021) by country
- Early neonatal, late neonatal, post-neonatal breakdowns
- VAD prevalence rates (GBD 2019 and 2021) by country/age group

Use pandas to read this sheet, then extract the relevant rows by filtering on
location names.

**External validity parameters from External validity sheet:**

From row 8: VAD prevalence from latest national survey (per location)
From row 9: Year of latest VAD survey (per location) — **flag any surveys
  older than 10 years as a structural concern**
From row 22: Estimated proportion of under-5s who are 6–59 months (per location)

**Sensitivity ranges from Sensitivity analysis sheet:**

Row 11: Effect of VAS on under-5 mortality: 25th = -80%, 75th = +75% of best
  guess — this is the single highest-variance parameter
Row 8: Cost per person reached: range varies by location
Row 9: Counterfactual coverage: varies significantly by location

**The `get_parameter_summary()` method must include:**

1. Model overview: what the CEA calculates, how many locations, grantees
2. Key shared parameters (mortality effect, moral weights, benchmark)
3. Per-location table: country, cost/supplement, VAD survey year, VAD
   prevalence, estimated CE multiple
4. Sensitivity analysis summary: which parameters drive the most variance
5. Structural flags already identified:
   - VAD survey staleness (Angola 1999, Chad 2008 — read these dynamically)
   - DUMMYFUNCTION cells in Inputs rows 24–27 (note what they resolve to)
   - 20-state Nigerian disaggregation vs. national-level parameters for
     most other countries

---

## Task 4: Add VAS to config.py

Add to `INTERVENTION_URLS`:

```python
"vas": {
    "report": "https://www.givewell.org/international/technical/programs/vitamin-A",
    "baseline": "",   # No GiveWell AI baseline exists yet for VAS
    "spreadsheet": "VASCEA.xlsx",
},
```

Add to the `cea_classes` dict in `run_pipeline.py`:

```python
"vas": VASCEA,
```

Import `VASCEA` at the top of `run_pipeline.py`.

---

## Task 5: Test the Spreadsheet Reader

Before running the full pipeline:

```bash
cd /home/tsondo/projects/givewell_redteam
python -c "
from pipeline.spreadsheet import VASCEA
from pathlib import Path
cea = VASCEA(Path('data/VASCEA.xlsx'))
print(cea.get_parameter_summary())
"
```

The output must:
- Print without errors
- Show per-location cost data for all major locations
- Flag the stale VAD surveys
- Include the sensitivity ranges

Fix any issues before proceeding.

---

## Task 6: Run the Pipeline

Once the spreadsheet reader is verified:

```bash
cd /home/tsondo/projects/givewell_redteam
python pipeline/run_pipeline.py vas
```

The pipeline will:
1. Fetch the VAS intervention report from givewell.org
2. Run the Decomposer (no baseline AI output available — pass empty string)
3. Run Investigators against each thread
4. Run Verifier with web search
5. Run Quantifier against the spreadsheet
6. Run Adversarial pair
7. Run Synthesizer

All intermediate outputs save to `results/vas/`.

---

## Task 7: Log and Report

After the run completes, print:

```
=== Phase 4: VAS Complete ===
Candidate critiques:    N
Verified critiques:     N  (signal rate: X%)
Quantified critiques:   N
Surviving critiques:    N
Total cost:             $X.XX
Output:                 results/vas/final-report.md
```

---

## Constraints (same as all prior phases)

- API key in `.env` via python-dotenv. Activate it before running.
- No agent frameworks. Direct Anthropic SDK calls only.
- No streaming.
- Save after every stage — if the pipeline fails, `--resume-from` must work.
- openpyxl is read-only/inspection only. The runtime model has no spreadsheet
  dependency.
- Use `claude-opus-4-20250514` for Decomposer, Quantifier, Synthesizer.
- Use `claude-sonnet-4-20250514` for Investigators, Verifier, Adversarial.
- Log token usage and cost per API call.

---

## Known Structural Issues to Watch For

These were identified during spreadsheet inspection and should surface as
critiques if the pipeline is working correctly:

1. **Stale VAD prevalence data**: Angola survey from 1999, Chad from 2008.
   If these don't appear as verified critiques, something is wrong.
2. **Static mortality effect**: The 19% trial average is applied with a
   single location-adjustment scalar. Temporal trends in disease burden
   are not modeled.
3. **Nigerian state disaggregation asymmetry**: 20 Nigerian states have
   individual columns but share many national-level parameters.
4. **Publication bias adjustment**: The podcast (April 2, 2026) flagged
   this as unresolved. The model may not fully capture this uncertainty.
5. **VAD deficiency as mediator**: The external validity adjustment uses
   proxy indicators (stunting, wasting, poverty) rather than direct VAD
   measurement for most locations.
