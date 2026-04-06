# Task: Phase 2 — Add Temporal Dynamics (Net Degradation × Distribution Frequency)

## Context

Phase 1 is complete. The Bayesian optimization found that all 5 parameters in GiveWell's CEA are monotonic — no trade-offs, no interactions, no local optima. The CEA is a multiplicative chain where every parameter independently pushes cost-effectiveness in one direction. Optimization was trivial; the real output was the per-country uncertainty ranges.

**Why this matters:** The monotonicity result is a structural finding about the model, not a failure of the optimizer. Real intervention design *has* trade-offs that GiveWell's static CEA cannot capture. Phase 2 introduces one: **net degradation over time vs. distribution frequency**, which creates a genuine optimization surface with curvature.

**The trade-off:** Nets degrade. Distributing more frequently improves average efficacy but costs more per cycle. There's an optimal frequency that depends on the degradation curve, cost structure, and local malaria burden. This is the kind of problem where a GP surrogate earns its keep.

## Evidence from our pipeline (results/insecticide-treated-nets/)

The red-teaming pipeline found:
- GiveWell's CEA uses an implicit 2.5-year net lifespan and 70% usage as static parameters
- WHO durability monitoring: median net survival 2.0–2.6 years depending on use environment
- AMF post-distribution monitoring: usage drops from ~80% at 8 months to 64-69% at 12 months; only 31% of nets in usable condition at 24 months
- The Verifier confirmed that "the strong influence of net-use environment and behavioral factors" on physical survival can vary by up to 2 years for the same net brand
- The Adversarial stage conceded: "The core mechanism is valid" — nets degrade and the model doesn't capture it

## What to build

### 1. Extend `optimize/cea_model.py` with a temporal model

**Do not modify the existing functions** — they're validated at 0% error. Add new functions alongside them in a separate file.

Create `optimize/cea_model_temporal.py` that imports baseline constants from `cea_model.py` and adds a time-varying calculation over a multi-year program horizon:

```python
def compute_temporal_cea(
    params: dict[str, float],
    country_index: int,
    program_years: int = 10,
    distribution_interval_months: int = 30,  # new design variable
) -> dict[str, float]:
    """
    Compute CEA with net degradation over time.
    
    New design variable:
        distribution_interval_months: How often nets are distributed (12-48 months).
        GiveWell default is ~30 months (2.5 year cycle).
    
    Returns:
        cost_per_daly, deaths_averted_per_million, total_program_cost,
        average_net_efficacy (time-weighted), num_distribution_cycles
    """
```

**The degradation model:**

Use an exponential decay for net efficacy as a function of net age in months:

```
efficacy(t) = physical_survival(t) × insecticide_efficacy(t) × usage(t)
```

Where:
- `physical_survival(t)` = fraction of nets still physically intact at age t months
  - Model as: `exp(-t / tau_physical)` where tau_physical is calibrated to WHO data
  - Calibrate so that ~31% survive at 24 months (AMF data) → tau_physical ≈ 20.5 months
  - `tau_physical` is a **free parameter** the optimizer explores within bounds (±30% → range 15 to 30). Unlike `insecticide_resistance` in Phase 1 (monotonic by definition), `tau_physical` interacts with `distribution_interval` — a shorter tau makes frequent redistribution more valuable, but at higher cost. That interaction is exactly the curvature we're looking for.

- `insecticide_efficacy(t)` = chemical killing power remaining at age t months
  - Model as: `exp(-t / tau_insecticide)` 
  - Calibrate to published insecticide decay data (typically faster than physical decay)
  - A reasonable starting point: tau_insecticide ≈ 12-18 months

- `usage(t)` = fraction of households with intact nets that actually use them
  - Model as: `u_0 × exp(-t / tau_usage)` where u_0 = 0.80 (initial post-distribution usage)
  - Calibrate so usage ≈ 0.65 at 12 months (AMF data) → tau_usage ≈ 48 months (slow decay)

**Net replacement model:**

Each distribution is a **full replacement** — all old nets are replaced with new ones, resetting efficacy to initial levels. This matches how mass campaigns actually work (distribute to all households, not just those whose nets failed). Do not model residual old-net stock; we don't have good data on household-level net inventory management, and the added complexity wouldn't change the optimization finding meaningfully.

**The time integration:**

For a given `distribution_interval_months` (call it D):
1. At month 0, distribute nets. Efficacy starts high.
2. Efficacy decays continuously until month D, when new nets arrive.
3. New distribution fully replaces old nets — efficacy resets to initial levels.
4. Repeat over `program_years`.
5. Compute total person-years of effective protection = integral of efficacy(t) over the program horizon.
6. Compute total cost = (number of distribution cycles) × (cost per distribution cycle).
7. Cost per distribution cycle scales with the existing per-net costs from the CEA, but add a fixed logistics overhead per cycle (this is the key non-linearity — more frequent distribution means more logistics events).

**Population and cost framing:**

Fix the target population (use a representative population size from the existing CEA data for each country). Hold nets-per-cycle constant — each cycle distributes the same number of nets (full replacement). Let total program cost float as a function of the number of cycles:

```
total_cost = num_cycles × cost_per_cycle
num_cycles = ceil(program_years × 12 / distribution_interval_months)
```

Do NOT use the $1M grant framing from the static model — it's awkward for temporal analysis. Instead, `distribution_interval_months` is the lever that directly trades total cost against cumulative efficacy.

**The logistics cost:**

This is where the trade-off bites. Model distribution cost as:

```
cost_per_cycle = variable_cost_per_net × nets_needed + fixed_logistics_cost_per_cycle
```

Where:
- `variable_cost_per_net`: from GiveWell's existing cost data
- `nets_needed`: depends on target population and coverage (constant across cycles since we do full replacement)
- `fixed_logistics_cost_per_cycle`: a new parameter representing supply chain, transport, community health worker mobilization costs per distribution event. This is the term that penalizes frequent redistribution.
- Start with `fixed_logistics_cost_per_cycle` as a fraction of total variable cost (e.g., 10-25%). This is uncertain — make it a parameter the optimizer can explore.

**Composition with original parameters:**

The temporal model **replaces the mortality reduction pathway only**. Instead of a static reduction parameter, it integrates time-varying efficacy over the horizon to produce an *effective average mortality reduction*. Everything downstream — value of statistical life, income effects, DALY calculations — still uses the original calculation chain from `cea_model.py` with the original 5 parameters. Think of it as: the temporal model feeds a time-weighted average into the same downstream math.

### 2. Write the new objective function

Create `optimize/objective_temporal.py`:

```python
def evaluate_temporal_cea(params: dict[str, float]) -> dict[str, float]:
    """
    Temporal CEA objective function.
    
    params includes the original 5 CEA parameters PLUS:
        - distribution_interval_months: 12 to 48 (the key design variable)
        - fixed_logistics_fraction: 0.05 to 0.30 (cost overhead per cycle)
        - tau_physical: 15 to 30 (net physical survival rate, free parameter)
        - tau_insecticide: 8 to 24 (insecticide decay rate)
        - tau_usage: 30 to 72 (usage decay rate)
    
    Returns:
        cost_per_daly, deaths_averted, total_cost, average_efficacy,
        num_distribution_cycles
    """
```

### 3. Verify the temporal model reproduces the static baseline

When `distribution_interval_months=30` and decay parameters are calibrated to match the static model's assumptions (i.e., effectively no decay — set tau values very high), the temporal model should approximately reproduce the Phase 1 baseline. It won't be exact — the temporal model integrates over a continuous curve while the static model uses point estimates — but it should be within 5-10%.

Use the **Phase 1 baseline values from the existing result JSONs** (`optimize/results/{country}.json`) as the comparison target. They're already validated at 0% error against the spreadsheet. Do not recompute from `compute_country_ce`.

### 4. Run bidirectional optimization with the temporal model

Use the same scipy/sklearn Bayesian optimization from Phase 1 (`optimize/bayesian_opt.py`). The search space is now larger (5 original params + 5 temporal params + distribution_interval as design variable = 11 dimensions).

**Start with Chad + Guinea only** to validate the model and confirm the optimizer finds non-trivial behavior before running all 8 countries. Chad (lowest CE at 4.82x, hardest case) and Guinea (highest CE at 22.79x) bracket the range. If both produce interesting results, run the remaining 6.

Run both directions (minimize and maximize cost_per_daly). The objective is still **cost_per_daly**, now computed from the temporal integration rather than the static formula. Track `average_efficacy` and `num_distribution_cycles` as secondary metrics for interpretability.

Increase Sobol points to 25 and GP trials to 75 for the larger space (~100 total trials per run).

**The key question we're answering:** Does the optimizer find a non-trivial optimal distribution frequency? I.e., is there an interior optimum where distributing every X months is better than the default 30-month cycle? Or is distribution frequency also monotonic (more frequent is always better, or less frequent is always better)?

If there IS an interior optimum, that's a concrete, actionable finding: "For country X, redistributing nets every Y months instead of every 30 months would improve cost-effectiveness by Z%."

If distribution frequency is ALSO monotonic, that's still informative — it means the trade-off between logistics cost and efficacy decay isn't balanced at realistic parameter values, and we should document which direction wins and why.

### 5. Produce the comparison

Write `optimize/results/temporal_summary.md` with:
- Per-country optimal distribution intervals (or note if monotonic)
- Comparison: static CE (from Phase 1 result JSONs) vs. temporal CE at default 30-month cycle vs. temporal CE at optimized interval
- Which decay parameters matter most (physical survival? insecticide? usage?)
- Whether the optimizer now finds non-monotonic behavior in any parameter (the whole point of Phase 2)
- If Chad + Guinea show interesting results, include a note that the remaining 6 countries should be run

## Output

- `optimize/cea_model_temporal.py` — temporal extension (separate file, imports from cea_model.py for baseline constants)
- `optimize/objective_temporal.py` — temporal objective function
- `optimize/test_temporal.py` — baseline reproduction test + decay curve sanity checks
- `optimize/results/temporal_summary.md` — analysis and comparison

## Constraints

- Same Python 3.11/3.12 venv as Phase 1
- Dependencies: same as Phase 1 (scikit-learn, scipy). No new dependencies.
- Do not modify Phase 1 files — extend, don't replace.
- The decay parameter calibrations (tau values) are approximate. Document your calibration reasoning and cite the pipeline evidence. Getting the shape right matters more than nailing exact values — the optimizer will explore the space.
- No API key needed. All computation is local.
