# Task: Build the ITN CEA Objective Function

## Context

We're adapting Meta's Ax/BOxCrete Bayesian optimization framework to optimize global health interventions. Before we can run any optimization, we need a callable objective function that takes intervention parameters and returns cost-effectiveness metrics.

The existing red-teaming pipeline already has spreadsheet integration via `pipeline/spreadsheet.py` (openpyxl + pandas). The CEA spreadsheet is at `data/InsecticideCEA.xlsx`. Reuse that code where possible.

## Steps

### 1. Load and explore `data/InsecticideCEA.xlsx`

Map the spreadsheet structure. Identify:
- Which sheets contain the CEA model (vs. documentation/source data)
- Where the input parameters live (cell references)
- Where the output metrics live (cost per DALY averted, deaths averted, cost-effectiveness ratio)
- Which parameters our pipeline's Phase 2 results flagged as high-impact (check `results/insecticide-treated-nets/` for the Quantifier and Synthesizer outputs — look for parameters that produced the largest cost-effectiveness swings)

Produce a parameter map: a table of `(parameter_name, sheet, cell, current_value, description)` for the 5-8 most impactful input parameters.

### 2. Write `optimize/objective.py`

Create a function with this interface:

```python
def evaluate_cea(params: dict[str, float]) -> dict[str, float]:
    """
    Modify CEA spreadsheet parameters, recalculate, and return metrics.
    
    Args:
        params: Dict mapping parameter names to values.
                Keys match the parameter_name column from step 1.
    
    Returns:
        Dict with at least:
        - cost_per_daly: float (lower is better)
        - deaths_averted_per_million: float (higher is better)
    """
```

Implementation notes:
- Do NOT use openpyxl for evaluation at runtime. Excel formula recalculation is fragile and slow — we'll be calling this function thousands of times during optimization.
- Instead, read the spreadsheet once to extract the CEA formulas and their relationships, then reimplement the calculation chain as a pure Python/numpy model in `optimize/cea_model.py`.
- The Python model should be fast (no file I/O per call), transparent (each formula step documented with its source cell reference), and testable.
- Use openpyxl only in step 1 to inspect the spreadsheet structure and extract the formulas. The runtime objective function should have zero spreadsheet dependency.
- Document every formula you extract: source sheet, cell reference, the Excel formula, and your Python equivalent.

### 3. Verify baseline reproduction

Write a test that:
- Calls `evaluate_cea()` with GiveWell's default parameter values
- Asserts the output matches GiveWell's published cost-effectiveness estimate for ITNs (within 1-2% tolerance for floating point)
- Print both expected and actual values

If it doesn't match, debug until it does. This is the foundation everything else builds on — it must be correct.

### 4. Manual perturbation sanity check

Pick 2-3 parameters and perturb them in directions where the effect is obvious:
- Increase coverage → deaths averted should increase
- Increase cost per net → cost per DALY should increase  
- Decrease net efficacy → deaths averted should decrease

Print a small table showing `(parameter, baseline_value, perturbed_value, baseline_output, perturbed_output, direction_correct)`.

## Output

When done, we should have:
- `optimize/cea_model.py` — pure Python reimplementation of GiveWell's ITN CEA calculation chain (no spreadsheet dependency, fast enough for thousands of calls)
- `optimize/objective.py` — the callable objective function wrapping the model
- `optimize/parameter_map.json` — the parameter map from step 1
- `optimize/test_objective.py` — the verification tests from steps 3-4
- A brief summary of what you found in the spreadsheet structure and the formulas you extracted

## Constraints

- Python 3.14 venv, same as existing pipeline
- Dependencies: openpyxl and pandas for spreadsheet inspection only (step 1), numpy for the runtime model
- Do not modify anything in `data/` — treat as read-only
- Do not modify anything in `pipeline/` or `prompts/` — existing pipeline code is stable
