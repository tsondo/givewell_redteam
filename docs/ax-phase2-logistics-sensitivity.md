# Task: Logistics Cost Sensitivity Analysis

## Context

Phase 2 found genuine non-monotonic behavior in distribution_interval_months, with three country clusters (long-cycle, medium-cycle, short-cycle). But the optimal intervals and the ~2x cost-effectiveness finding both depend on `fixed_logistics_fraction` — the least empirically grounded parameter in the model (range 0.05–0.30, no field data behind it).

Before publishing, we need to show whether the findings are robust to logistics cost assumptions or are artifacts of a made-up parameter. This is a quick sensitivity check, not a new optimization.

## What to build

### 1. Write `optimize/logistics_sensitivity.py`

For **three representative countries** (one per cluster):
- **Chad** (long-cycle, optimal D=48)
- **Guinea** (medium-cycle, optimal D=46)
- **Togo** (short-cycle, optimal D=31)

At **three logistics cost levels**:
- Low: `fixed_logistics_fraction = 0.05`
- Mid: `fixed_logistics_fraction = 0.15` (Phase 2 default)
- High: `fixed_logistics_fraction = 0.25`

For each (country, logistics_cost) pair:
1. Evaluate `compute_temporal_cea` across a sweep of `distribution_interval_months` from 12 to 48 in steps of 2 months — hold all other parameters at their Phase 2 best-case (minimize) values from the result JSONs
2. Find the interval that minimizes cost_per_daly
3. Record the optimal interval, the cost_per_daly at that interval, and the cost_per_daly at the default 30-month cycle

This is a grid sweep, not a full optimization — we're only varying one parameter (distribution_interval) across 19 values. No GP needed. Should run in seconds.

### 2. Produce the output table

Write `optimize/results/logistics_sensitivity.md`:

```
## Logistics Cost Sensitivity

How optimal distribution interval shifts with logistics cost assumptions.

| Country | Logistics Frac | Optimal D (months) | $/DALY at Optimal D | $/DALY at D=30 |
|---------|:-:|:-:|--:|--:|
| Chad    | 0.05 | ?? | $?? | $?? |
| Chad    | 0.15 | ?? | $?? | $?? |
| Chad    | 0.25 | ?? | $?? | $?? |
| Guinea  | 0.05 | ?? | $?? | $?? |
| ...     | ...  | .. | ... | ... |
```

Then a brief interpretation:
- Do the three clusters hold across logistics assumptions, or do they collapse/flip?
- At what logistics cost does "distribute as frequently as possible" (D=12) become optimal? At what cost does "distribute as infrequently as possible" (D=48) win?
- How much does cost_per_daly vary across logistics assumptions at the same interval?

### 3. Bonus: plot the curves if easy

If convenient, generate a simple matplotlib/ASCII visualization showing cost_per_daly vs. distribution_interval for each (country, logistics_frac) combination — 9 curves total on one chart (3 countries × 3 logistics levels). Save as `optimize/results/logistics_sensitivity.png` or just print ASCII. This isn't required but would be useful for the blog post.

## Output

- `optimize/logistics_sensitivity.py` — the sweep script
- `optimize/results/logistics_sensitivity.md` — table and interpretation
- (optional) `optimize/results/logistics_sensitivity.png` — visualization

## Constraints

- Same venv as Phase 2. No new dependencies (matplotlib is fine if already installed, otherwise skip the plot).
- Read Phase 2 best-case parameters from `optimize/results/{country}_temporal.json` — don't hardcode them.
- Do not modify any Phase 2 files.
- No API key needed. All local computation.
- This should take under 5 minutes total including runtime.
