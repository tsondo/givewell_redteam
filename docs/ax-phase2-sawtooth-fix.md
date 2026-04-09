# Task: Fix Sawtooth Artifact in Temporal Model and Re-Run

## Problem

The temporal model uses `ceil(program_months / D)` for cycle count, which creates a sawtooth pattern in cost_per_daly vs. distribution_interval. D=40 appears optimal partly because `ceil(120/40) = 3` while `ceil(120/30) = 4` — the optimizer exploits integer cycle boundaries rather than finding genuine efficacy-vs-cost trade-offs.

## Fix

**Prorate the final cycle.** If the program horizon doesn't divide evenly by D:

- The final cycle still incurs **full distribution cost** (you can't do half a campaign)
- But the final cycle only provides **partial benefit** — nets are used for fewer than D months before the program ends

Concretely, for `program_months = 120` and `D = 40`:
- 3 full cycles, no partial cycle. Same as before.

For `program_months = 120` and `D = 35`:
- `120 / 35 = 3.43` → 3 full cycles (months 0–105) plus 1 partial cycle starting at month 105
- Partial cycle duration: `120 - 105 = 15 months` (out of 35)
- Partial cycle cost: **full** `cost_per_cycle` (same as other cycles)
- Partial cycle efficacy: integrate decay from 0 to 15 months only (not full 35)
- Partial cycle person-years: `(15 / D) × full_cycle_person_years` adjusted by the partial efficacy integral

## Implementation

Modify `compute_temporal_cea` in `optimize/cea_model_temporal.py`:

```python
# Instead of:
num_cycles = math.ceil(program_months / distribution_interval_months)
# ... uniform treatment of all cycles

# Do:
num_full_cycles = program_months // distribution_interval_months
remainder_months = program_months % distribution_interval_months

# Full cycles: each has the same average efficacy (full replacement resets)
avg_efficacy_full = integrate_efficacy_over_cycle(
    distribution_interval_months, tau_physical, tau_insecticide, tau_usage
)
full_cycle_months = num_full_cycles * distribution_interval_months

# Partial final cycle (if any)
if remainder_months > 0:
    avg_efficacy_partial = integrate_efficacy_over_cycle(
        remainder_months, tau_physical, tau_insecticide, tau_usage
    )
    total_num_cycles = num_full_cycles + 1  # cost: pay for full distribution
    # Time-weighted average efficacy across the entire horizon
    total_efficacy_months = (
        avg_efficacy_full * full_cycle_months +
        avg_efficacy_partial * remainder_months
    )
    avg_efficacy = total_efficacy_months / program_months
else:
    total_num_cycles = num_full_cycles
    avg_efficacy = avg_efficacy_full

# Cost: every cycle (including partial) costs the same
total_program_cost = total_num_cycles * cost_per_cycle
```

The key insight: `integrate_efficacy_over_cycle` already works for any duration — just call it with `remainder_months` instead of `distribution_interval_months` for the partial cycle. No new functions needed.

## After fixing

### 1. Re-run the decay curve and baseline reproduction tests

```bash
.venv/bin/python optimize/test_temporal.py
```

The baseline reproduction test should still pass (D=30 divides 120 evenly, so there's no partial cycle at the default).

### 2. Re-run the logistics sensitivity sweep

```bash
.venv/bin/python optimize/logistics_sensitivity.py
```

Verify the sawtooth is gone — cost_per_daly vs. D should now be smooth. The plot should show a clean U-shaped (or monotonic) curve instead of jagged steps.

### 3. Re-run the full Phase 2 optimization (all 8 countries)

```bash
.venv/bin/python -m optimize.run_temporal --all
```

This regenerates all result JSONs and temporal_summary.md. The optimal intervals may shift now that the divisor artifact is removed.

### 4. Re-run logistics sensitivity with updated results

```bash
.venv/bin/python optimize/logistics_sensitivity.py
```

Update the sensitivity table and plot with the corrected model.

### 5. Commit everything

```bash
git add optimize/cea_model_temporal.py optimize/test_temporal.py optimize/logistics_sensitivity.py optimize/results/
git commit -m "fix: prorate final distribution cycle to remove sawtooth artifact

ceil(program_months/D) created discontinuities in cost_per_daly at
integer cycle boundaries. Now: full cycles get full cost + full
efficacy integration; partial final cycle gets full cost but only
partial efficacy (integrated over remainder months).

Re-ran all 8 countries + logistics sensitivity with corrected model.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

## Constraints

- Only modify `optimize/cea_model_temporal.py` — the fix is entirely within `compute_temporal_cea`.
- Do not modify Phase 1 files, the optimizer, or the objective function wrapper.
- The fix should not change the baseline reproduction test result (D=30 divides 120 evenly).
- Same venv, no new dependencies, no API key.
