# Temporal ITN CEA Optimization Summary

Bayesian optimization of 10 parameters (5 original + distribution interval + logistics fraction + 3 decay time constants).
Each country: 25 Sobol + 75 Bayesian = 100 trials, both minimize and maximize cost_per_daly.

## Optimal Distribution Intervals

| Country | Direction | Optimal Interval | At Bound? | Default $/DALY | Optimized $/DALY | Improvement % |
|---------|-----------|:----------------:|:---------:|--------------:|-----------------:|--------------:|
| Chad | Best | 42.3 mo | No | $2387 | $819 | 65.7% |
| Chad | Worst | 30.8 mo | No | $2387 | $23630 | 889.9% |
| DRC | Best | 48.0 mo | Yes* | $657 | $253 | 61.4% |
| DRC | Worst | 30.8 mo | No | $657 | $6242 | 849.9% |
| Guinea | Best | 48.0 mo | Yes* | $280 | $103 | 63.3% |
| Guinea | Worst | 30.8 mo | No | $280 | $2578 | 820.8% |
| Nigeria (GF) | Best | 45.2 mo | No | $420 | $164 | 60.9% |
| Nigeria (GF) | Worst | 30.8 mo | No | $420 | $4298 | 923.4% |
| Nigeria (PMI) | Best | 45.1 mo | No | $676 | $244 | 64.0% |
| Nigeria (PMI) | Worst | 30.8 mo | No | $676 | $7418 | 997.9% |
| South Sudan | Best | 48.0 mo | Yes* | $1340 | $515 | 61.5% |
| South Sudan | Worst | 12.0 mo | Yes* | $1340 | $12420 | 827.0% |
| Togo | Best | 45.2 mo | No | $632 | $209 | 66.9% |
| Togo | Worst | 30.8 mo | No | $632 | $8293 | 1212.7% |
| Uganda | Best | 45.3 mo | No | $453 | $160 | 64.7% |
| Uganda | Worst | 12.0 mo | Yes* | $453 | $4757 | 950.8% |

## Static vs Temporal Comparison

Phase 1 static model vs temporal model (D=30 default) vs temporal optimized.

| Country | Static $/DALY (Phase 1) | Temporal $/DALY (D=30) | Temporal $/DALY (optimized) | Optimal D |
|---------|------------------------:|------------------------:|----------------------------:|----------:|
| Chad | $499 | $2387 | $819 | 42.3 mo |
| DRC | $137 | $657 | $253 | 48.0 mo |
| Guinea | $59 | $280 | $103 | 48.0 mo |
| Nigeria (GF) | $88 | $420 | $164 | 45.2 mo |
| Nigeria (PMI) | $141 | $676 | $244 | 45.1 mo |
| South Sudan | $280 | $1340 | $515 | 48.0 mo |
| Togo | $132 | $632 | $209 | 45.2 mo |
| Uganda | $95 | $453 | $160 | 45.3 mo |

## Decay Parameter Sensitivity

Which temporal parameters does the optimizer push hardest (best-case direction)?

### Chad (best case)

- **distribution_interval_months**: 42.31 (range [12.0, 48.0], position: 84%)
- **fixed_logistics_fraction**: 0.05 (range [0.05, 0.3], position: 0%) *
- **tau_physical**: 30.00 (range [15.0, 30.0], position: 100%) *
- **tau_insecticide**: 24.00 (range [8.0, 24.0], position: 100%) *
- **tau_usage**: 72.00 (range [30.0, 72.0], position: 100%) *

### DRC (best case)

- **distribution_interval_months**: 48.00 (range [12.0, 48.0], position: 100%) *
- **fixed_logistics_fraction**: 0.11 (range [0.05, 0.3], position: 24%)
- **tau_physical**: 30.00 (range [15.0, 30.0], position: 100%) *
- **tau_insecticide**: 23.64 (range [8.0, 24.0], position: 98%)
- **tau_usage**: 72.00 (range [30.0, 72.0], position: 100%) *

### Guinea (best case)

- **distribution_interval_months**: 48.00 (range [12.0, 48.0], position: 100%) *
- **fixed_logistics_fraction**: 0.05 (range [0.05, 0.3], position: 0%) *
- **tau_physical**: 30.00 (range [15.0, 30.0], position: 100%) *
- **tau_insecticide**: 24.00 (range [8.0, 24.0], position: 100%) *
- **tau_usage**: 72.00 (range [30.0, 72.0], position: 100%) *

### Nigeria (GF) (best case)

- **distribution_interval_months**: 45.19 (range [12.0, 48.0], position: 92%)
- **fixed_logistics_fraction**: 0.19 (range [0.05, 0.3], position: 55%)
- **tau_physical**: 30.00 (range [15.0, 30.0], position: 100%) *
- **tau_insecticide**: 24.00 (range [8.0, 24.0], position: 100%) *
- **tau_usage**: 72.00 (range [30.0, 72.0], position: 100%) *

### Nigeria (PMI) (best case)

- **distribution_interval_months**: 45.14 (range [12.0, 48.0], position: 92%)
- **fixed_logistics_fraction**: 0.05 (range [0.05, 0.3], position: 0%) *
- **tau_physical**: 30.00 (range [15.0, 30.0], position: 100%) *
- **tau_insecticide**: 24.00 (range [8.0, 24.0], position: 100%) *
- **tau_usage**: 72.00 (range [30.0, 72.0], position: 100%) *

### South Sudan (best case)

- **distribution_interval_months**: 48.00 (range [12.0, 48.0], position: 100%) *
- **fixed_logistics_fraction**: 0.05 (range [0.05, 0.3], position: 0%) *
- **tau_physical**: 27.79 (range [15.0, 30.0], position: 85%)
- **tau_insecticide**: 24.00 (range [8.0, 24.0], position: 100%) *
- **tau_usage**: 72.00 (range [30.0, 72.0], position: 100%) *

### Togo (best case)

- **distribution_interval_months**: 45.18 (range [12.0, 48.0], position: 92%)
- **fixed_logistics_fraction**: 0.05 (range [0.05, 0.3], position: 0%) *
- **tau_physical**: 26.06 (range [15.0, 30.0], position: 74%)
- **tau_insecticide**: 24.00 (range [8.0, 24.0], position: 100%) *
- **tau_usage**: 72.00 (range [30.0, 72.0], position: 100%) *

### Uganda (best case)

- **distribution_interval_months**: 45.31 (range [12.0, 48.0], position: 93%)
- **fixed_logistics_fraction**: 0.05 (range [0.05, 0.3], position: 0%) *
- **tau_physical**: 30.00 (range [15.0, 30.0], position: 100%) *
- **tau_insecticide**: 24.00 (range [8.0, 24.0], position: 100%) *
- **tau_usage**: 72.00 (range [30.0, 72.0], position: 100%) *

## Non-Monotonicity Analysis

Parameters at interior optima (not hitting bounds) indicate genuine trade-offs.

| Parameter | At Lower Bound | At Upper Bound | Interior Optima | Total Runs (16) |
|-----------|:-:|:-:|:-:|:-:|
| incidence_reduction | 8 | 8 | 0 | 16 |
| net_usage_adj | 8 | 8 | 0 | 16 |
| external_validity | 7 | 8 | 1 | 16 |
| indirect_deaths_multiplier | 8 | 8 | 0 | 16 |
| over5_relative_efficacy | 8 | 7 | 1 | 16 |
| distribution_interval_months | 2 | 3 | 11 | 16 |
| fixed_logistics_fraction | 6 | 8 | 2 | 16 |
| tau_physical | 8 | 6 | 2 | 16 |
| tau_insecticide | 8 | 7 | 1 | 16 |
| tau_usage | 8 | 8 | 0 | 16 |

Parameters with mostly interior optima: **distribution_interval_months** — these show genuine non-monotonic behavior.

---

\* = parameter at search space boundary

Generated by `optimize/run_temporal.py`.