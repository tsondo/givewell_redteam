# Temporal ITN CEA Optimization Summary

Bayesian optimization of 10 parameters (5 original + distribution interval + logistics fraction + 3 decay time constants).
Each country: 25 Sobol + 75 Bayesian = 100 trials, both minimize and maximize cost_per_daly.

## Optimal Distribution Intervals

| Country | Direction | Optimal Interval | At Bound? | Default $/DALY | Optimized $/DALY | Improvement % |
|---------|-----------|:----------------:|:---------:|--------------:|-----------------:|--------------:|
| Chad | Best | 48.0 mo | Yes* | $2387 | $1039 | 56.5% |
| Chad | Worst | 30.8 mo | No | $2387 | $24545 | 928.2% |
| DRC | Best | 42.3 mo | No | $657 | $294 | 55.3% |
| DRC | Worst | 30.8 mo | No | $657 | $6407 | 875.0% |
| Guinea | Best | 45.7 mo | No | $280 | $124 | 55.6% |
| Guinea | Worst | 46.1 mo | No | $280 | $2968 | 959.9% |
| Nigeria (GF) | Best | 42.7 mo | No | $420 | $173 | 58.9% |
| Nigeria (GF) | Worst | 37.1 mo | No | $420 | $5306 | 1163.2% |
| Nigeria (PMI) | Best | 42.7 mo | No | $676 | $281 | 58.4% |
| Nigeria (PMI) | Worst | 30.8 mo | No | $676 | $7614 | 1026.9% |
| South Sudan | Best | 48.0 mo | Yes* | $1340 | $611 | 54.4% |
| South Sudan | Worst | 30.8 mo | No | $1340 | $11906 | 788.6% |
| Togo | Best | 31.0 mo | No | $632 | $228 | 63.9% |
| Togo | Worst | 37.1 mo | No | $632 | $10241 | 1521.1% |
| Uganda | Best | 30.7 mo | No | $453 | $181 | 60.1% |
| Uganda | Worst | 46.1 mo | No | $453 | $5115 | 1029.7% |

## Static vs Temporal Comparison

Phase 1 static model vs temporal model (D=30 default) vs temporal optimized.

| Country | Static $/DALY (Phase 1) | Temporal $/DALY (D=30) | Temporal $/DALY (optimized) | Optimal D |
|---------|------------------------:|------------------------:|----------------------------:|----------:|
| Chad | $499 | $2387 | $1039 | 48.0 mo |
| DRC | $137 | $657 | $294 | 42.3 mo |
| Guinea | $59 | $280 | $124 | 45.7 mo |
| Nigeria (GF) | $88 | $420 | $173 | 42.7 mo |
| Nigeria (PMI) | $141 | $676 | $281 | 42.7 mo |
| South Sudan | $280 | $1340 | $611 | 48.0 mo |
| Togo | $132 | $632 | $228 | 31.0 mo |
| Uganda | $95 | $453 | $181 | 30.7 mo |

## Decay Parameter Sensitivity

Which temporal parameters does the optimizer push hardest (best-case direction)?

### Chad (best case)

- **distribution_interval_months**: 48.00 (range [12.0, 48.0], position: 100%) *
- **fixed_logistics_fraction**: 0.05 (range [0.05, 0.3], position: 0%) *
- **tau_physical**: 30.00 (range [15.0, 30.0], position: 100%) *
- **tau_insecticide**: 20.54 (range [8.0, 24.0], position: 78%)
- **tau_usage**: 72.00 (range [30.0, 72.0], position: 100%) *

### DRC (best case)

- **distribution_interval_months**: 42.31 (range [12.0, 48.0], position: 84%)
- **fixed_logistics_fraction**: 0.05 (range [0.05, 0.3], position: 0%) *
- **tau_physical**: 30.00 (range [15.0, 30.0], position: 100%) *
- **tau_insecticide**: 24.00 (range [8.0, 24.0], position: 100%) *
- **tau_usage**: 36.88 (range [30.0, 72.0], position: 16%)

### Guinea (best case)

- **distribution_interval_months**: 45.74 (range [12.0, 48.0], position: 94%)
- **fixed_logistics_fraction**: 0.13 (range [0.05, 0.3], position: 31%)
- **tau_physical**: 30.00 (range [15.0, 30.0], position: 100%) *
- **tau_insecticide**: 23.03 (range [8.0, 24.0], position: 94%)
- **tau_usage**: 72.00 (range [30.0, 72.0], position: 100%) *

### Nigeria (GF) (best case)

- **distribution_interval_months**: 42.65 (range [12.0, 48.0], position: 85%)
- **fixed_logistics_fraction**: 0.07 (range [0.05, 0.3], position: 8%)
- **tau_physical**: 30.00 (range [15.0, 30.0], position: 100%) *
- **tau_insecticide**: 24.00 (range [8.0, 24.0], position: 100%) *
- **tau_usage**: 64.33 (range [30.0, 72.0], position: 82%)

### Nigeria (PMI) (best case)

- **distribution_interval_months**: 42.65 (range [12.0, 48.0], position: 85%)
- **fixed_logistics_fraction**: 0.14 (range [0.05, 0.3], position: 36%)
- **tau_physical**: 30.00 (range [15.0, 30.0], position: 100%) *
- **tau_insecticide**: 24.00 (range [8.0, 24.0], position: 100%) *
- **tau_usage**: 72.00 (range [30.0, 72.0], position: 100%) *

### South Sudan (best case)

- **distribution_interval_months**: 48.00 (range [12.0, 48.0], position: 100%) *
- **fixed_logistics_fraction**: 0.05 (range [0.05, 0.3], position: 0%) *
- **tau_physical**: 30.00 (range [15.0, 30.0], position: 100%) *
- **tau_insecticide**: 24.00 (range [8.0, 24.0], position: 100%) *
- **tau_usage**: 72.00 (range [30.0, 72.0], position: 100%) *

### Togo (best case)

- **distribution_interval_months**: 30.99 (range [12.0, 48.0], position: 53%)
- **fixed_logistics_fraction**: 0.05 (range [0.05, 0.3], position: 0%) *
- **tau_physical**: 25.38 (range [15.0, 30.0], position: 69%)
- **tau_insecticide**: 22.79 (range [8.0, 24.0], position: 92%)
- **tau_usage**: 72.00 (range [30.0, 72.0], position: 100%) *

### Uganda (best case)

- **distribution_interval_months**: 30.69 (range [12.0, 48.0], position: 52%)
- **fixed_logistics_fraction**: 0.05 (range [0.05, 0.3], position: 0%) *
- **tau_physical**: 30.00 (range [15.0, 30.0], position: 100%) *
- **tau_insecticide**: 24.00 (range [8.0, 24.0], position: 100%) *
- **tau_usage**: 72.00 (range [30.0, 72.0], position: 100%) *

## Non-Monotonicity Analysis

Parameters at interior optima (not hitting bounds) indicate genuine trade-offs.

| Parameter | At Lower Bound | At Upper Bound | Interior Optima | Total Runs (16) |
|-----------|:-:|:-:|:-:|:-:|
| incidence_reduction | 8 | 7 | 1 | 16 |
| net_usage_adj | 8 | 8 | 0 | 16 |
| external_validity | 8 | 7 | 1 | 16 |
| indirect_deaths_multiplier | 8 | 8 | 0 | 16 |
| over5_relative_efficacy | 8 | 4 | 4 | 16 |
| distribution_interval_months | 0 | 2 | 14 | 16 |
| fixed_logistics_fraction | 5 | 8 | 3 | 16 |
| tau_physical | 8 | 7 | 1 | 16 |
| tau_insecticide | 8 | 5 | 3 | 16 |
| tau_usage | 8 | 6 | 2 | 16 |

Parameters with mostly interior optima: **distribution_interval_months** — these show genuine non-monotonic behavior.

---

\* = parameter at search space boundary

Generated by `optimize/run_temporal.py`.