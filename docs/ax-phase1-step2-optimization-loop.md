# Task: Wire the ITN Objective Function to Ax and Run Per-Country Optimization

## Context

Step 1 is complete. We have:
- `optimize/cea_model.py` — pure Python CEA calculation chain, 0% error vs. spreadsheet across all 8 countries
- `optimize/objective.py` — `evaluate_cea(params)` returning `cost_per_daly`, `deaths_averted_per_million`, `ce_multiple`
- `optimize/parameter_map.json` — 6 parameters with defaults and plausible ranges
- Baseline CE spread: 4.82x (Chad) to 22.79x (Guinea)

**Parameter scope change:** Remove `insecticide_resistance` from the search space. It's monotonic (optimizer will always push to the "least resistance" bound) and bounded on the good side by current evidence — not a real design variable. Keep it as a tracked constant at each country's default value. That leaves **5 parameters** to optimize.

We're adapting Meta's Ax/BOxCrete approach, using Gaussian process surrogates + Bayesian optimization. BOxCrete repo for reference: https://github.com/facebookresearch/SustainableConcrete

The 4.8x–22.8x CE spread across countries means a single global optimum is meaningless. **Optimize per-country** — run a separate optimization for each of the 8 country programs.

**Run optimization in both directions** for each country:
- **Minimize** cost_per_daly → best defensible case (most optimistic CE under plausible parameters)
- **Maximize** cost_per_daly → worst defensible case (the red team perspective)

The spread between min and max is the real finding: the **decision-relevant uncertainty range** for each country under defensible alternative assumptions.

## Steps

### 1. Set up the optimization framework

**Use scipy + sklearn directly** — skip Ax/PyTorch. The objective function is pure Python scalars, not tensors.

```bash
pip install scikit-learn
```

scipy is already available. The components:
- `scipy.stats.qmc.Sobol` — quasi-random initial exploration
- `sklearn.gaussian_process.GaussianProcessRegressor` — GP surrogate
- Expected Improvement acquisition function — implement manually (~10 lines)

Read `optimize/parameter_map.json` to define the search space. Use the 5 active parameters (exclude `insecticide_resistance`). For parameters with multiplier-style ranges, apply the multiplier to each country's default to get absolute bounds per country.

Create `optimize/bayesian_opt.py` with the optimization loop.

### 2. Write the optimization loop

In `optimize/bayesian_opt.py`, implement:

```python
def optimize_country(country_index: int, direction: str = "minimize") -> dict:
    """
    Run Bayesian optimization for one country in one direction.
    
    Args:
        country_index: 0-7 corresponding to columns I-P
        direction: "minimize" (best case) or "maximize" (worst case)
    
    Returns:
        Dict with best_params, best_metrics, trial_history
    """
```

The loop:
1. Generate 15 Sobol points across the 5-parameter space for initial exploration
2. Evaluate each point via `evaluate_cea()`
3. Fit a GP surrogate to observed (params → cost_per_daly) pairs
4. Use Expected Improvement to propose the next point (negate EI for maximize direction)
5. Evaluate, update GP, repeat for 35 more iterations
6. Return best found

For the GP: use `sklearn.gaussian_process.GaussianProcessRegressor` with a Matern kernel (nu=2.5). Normalize inputs to [0,1] before fitting.

### 3. Run per-country optimization (both directions)

For each of the 8 countries, run **two** optimization passes:
- Minimize cost_per_daly → best defensible CE
- Maximize cost_per_daly → worst defensible CE

That's 16 runs total (8 countries × 2 directions), 50 trials each.

Create `optimize/run_optimization.py` as the entry point. It should:
- Accept an optional `--country` flag to run a single country (for testing)
- Default to running all 8 sequentially, both directions
- Save results to `optimize/results/` as JSON — one file per country containing both min and max results

### 4. Compare against GiveWell baselines

After optimization, produce a comparison table:

```
Country | Best Case CE | GiveWell Default CE | Worst Case CE | Uncertainty Range | Key Parameter Divergences
--------|-------------|---------------------|---------------|-------------------|-------------------------
Guinea  | ??x         | 22.79x              | ??x           | ??x               | param1: best=0.7, worst=0.3
Chad    | ??x         | 4.82x               | ??x           | ??x               | param1: best=0.3, worst=0.7
...
```

Frame the summary as: "GiveWell's point estimate is X. Under defensible alternative assumptions, CE ranges from Y to Z."

Write this to `optimize/results/optimization_summary.md`.

Flag any case where the optimizer pushes a parameter to its bound — that suggests the bound may be too tight or the parameter has monotonic influence (which is useful to know but not a real "optimization" — it just means the current default is suboptimal in an obvious direction).

### 5. Sanity check the results

For each country's best-found configuration:
- Verify the optimized parameters are within plausible ranges (not just mathematically valid but defensible with evidence)
- Check whether different countries converge on similar parameter shifts or diverge — this tells us whether the intervention should be configured differently by region
- Note any parameters the optimizer mostly ignores (low sensitivity)

## Output

When done, we should have:
- `optimize/bayesian_opt.py` — GP-based Bayesian optimization loop (scipy/sklearn, no Ax dependency)
- `optimize/run_optimization.py` — entry point for per-country bidirectional optimization
- `optimize/results/{country}.json` — per-country results (best-case params, worst-case params, metrics, trial histories)
- `optimize/results/optimization_summary.md` — comparison table and analysis framed as decision-relevant uncertainty ranges

## Constraints

- Dependencies: scikit-learn (new), scipy (already available). No Ax, no PyTorch.
- **Use a Python 3.12 or 3.11 venv** for this module — not 3.14. Create a separate venv if needed.
- Do not modify `optimize/cea_model.py` or `optimize/objective.py` — treat step 1 outputs as stable.
- Keep total runtime reasonable — 50 trials × 16 runs with a pure Python objective should complete in well under a minute.
- Print progress as it runs so we can see what's happening.
