# Phase 2: Temporal Dynamics Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add net degradation and distribution frequency as a design variable to the ITN CEA, creating a genuine cost-vs-efficacy trade-off the Bayesian optimizer can exploit.

**Architecture:** A temporal model (`cea_model_temporal.py`) computes time-weighted average net efficacy over a multi-year program horizon using exponential decay for physical survival, insecticide potency, and usage. This efficacy scaling factor modulates the static model's mortality reduction. Distribution cost includes a fixed logistics overhead per cycle, creating the cost-vs-frequency trade-off. A new objective function (`objective_temporal.py`) wraps this for the existing Bayesian optimizer. Cost basis is derived from the static model's $1M-grant-per-person-year math (option b), avoiding spreadsheet extraction.

**Tech Stack:** Python 3.14, numpy, scipy, scikit-learn (same as Phase 1). Must install scipy + scikit-learn into venv first.

---

### Task 1: Install missing dependencies

**Files:**
- None (venv only)

The Phase 1 optimization code depends on scipy and scikit-learn, but they're not currently installed in the venv. Install them before any code runs.

- [ ] **Step 1: Install scipy and scikit-learn**

```bash
.venv/bin/pip install scipy scikit-learn
```

- [ ] **Step 2: Verify Phase 1 still works**

```bash
.venv/bin/python -c "from optimize.bayesian_opt import optimize_country; print('OK')"
```

Expected: `OK`

- [ ] **Step 3: Verify Phase 1 tests pass**

```bash
.venv/bin/python optimize/test_objective.py
```

Expected: `ALL PASS` for baseline reproduction and perturbation sanity checks.

---

### Task 2: Temporal decay model — tests

**Files:**
- Create: `optimize/test_temporal.py`

Write tests first. These verify the decay curves and the time-integration logic before any implementation exists.

- [ ] **Step 1: Write decay curve calibration tests**

```python
"""Tests for the temporal ITN CEA model.

Verifies decay calibrations, time integration, and baseline reproduction.
"""
from __future__ import annotations

import math


def test_physical_survival_calibration():
    """tau_physical=20.5 should give ~31% survival at 24 months (AMF data)."""
    from optimize.cea_model_temporal import physical_survival

    tau = 20.5
    result = physical_survival(24, tau)
    assert abs(result - 0.31) < 0.02, f"Expected ~0.31, got {result:.4f}"

    # At t=0, survival should be 1.0
    assert physical_survival(0, tau) == 1.0


def test_usage_calibration():
    """tau_usage=48 with u0=0.80 should give ~0.65 at 12 months (AMF data)."""
    from optimize.cea_model_temporal import usage_rate

    result = usage_rate(12, u0=0.80, tau_usage=48)
    assert abs(result - 0.65) < 0.03, f"Expected ~0.65, got {result:.4f}"

    # At t=0, usage should be u0
    assert usage_rate(0, u0=0.80, tau_usage=48) == 0.80


def test_insecticide_decay():
    """Insecticide efficacy should decay faster than physical survival."""
    from optimize.cea_model_temporal import insecticide_efficacy

    tau = 15  # midpoint of 12-18 range
    at_12 = insecticide_efficacy(12, tau)
    at_24 = insecticide_efficacy(24, tau)

    # Should be meaningfully decayed by 12 months
    assert at_12 < 0.50, f"Expected <0.50 at 12mo, got {at_12:.4f}"
    # Should be much lower at 24 months
    assert at_24 < at_12, "24-month efficacy should be less than 12-month"


def test_combined_efficacy_decays_monotonically():
    """Combined efficacy should decrease over time."""
    from optimize.cea_model_temporal import net_efficacy

    tau_p, tau_i, tau_u = 20.5, 15.0, 48.0
    prev = net_efficacy(0, tau_p, tau_i, tau_u, u0=0.80)
    for t in range(1, 49):
        curr = net_efficacy(t, tau_p, tau_i, tau_u, u0=0.80)
        assert curr < prev, f"Efficacy increased at month {t}: {prev:.4f} -> {curr:.4f}"
        prev = curr


if __name__ == "__main__":
    test_physical_survival_calibration()
    test_usage_calibration()
    test_insecticide_decay()
    test_combined_efficacy_decays_monotonically()
    print("All decay curve tests PASSED")
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
.venv/bin/python optimize/test_temporal.py
```

Expected: `ModuleNotFoundError: No module named 'optimize.cea_model_temporal'`

---

### Task 3: Temporal decay model — implementation

**Files:**
- Create: `optimize/cea_model_temporal.py`

Implement the decay functions and the time-integrated CEA. This is the core of Phase 2.

- [ ] **Step 1: Write the decay primitives and time integration**

```python
"""Temporal extension of ITN CEA model — net degradation over time.

Adds time-varying efficacy (physical survival, insecticide decay, usage decline)
and distribution frequency as a design variable. Composes with the static model
from cea_model.py via an efficacy scaling factor.

Calibration sources:
    - Physical survival: AMF data — ~31% of nets in usable condition at 24 months
      → tau_physical ≈ 20.5 months (exp(-24/20.5) ≈ 0.31)
    - Insecticide efficacy: WHO durability monitoring — typically decays faster
      than physical integrity → tau_insecticide ≈ 12-18 months
    - Usage: AMF post-distribution monitoring — ~80% at 0 months, ~65% at 12 months
      → tau_usage ≈ 48 months (slow decline)
"""
from __future__ import annotations

import math

from optimize.cea_model import (
    COUNTRIES,
    CountryParams,
    DEFAULT_EXTERNAL_VALIDITY,
    DEFAULT_INCIDENCE_REDUCTION,
    DEFAULT_INDIRECT_DEATHS_MULTIPLIER,
    DEFAULT_NET_USAGE_ADJ,
    DEFAULT_OVER5_RELATIVE_EFFICACY,
    compute_country_ce,
)


# ---------------------------------------------------------------------------
# Decay primitives
# ---------------------------------------------------------------------------

def physical_survival(t_months: float, tau_physical: float) -> float:
    """Fraction of nets physically intact at age t months.

    Model: exp(-t / tau_physical)
    Calibrated so ~31% survive at 24 months → tau ≈ 20.5
    """
    return math.exp(-t_months / tau_physical)


def insecticide_efficacy(t_months: float, tau_insecticide: float) -> float:
    """Fraction of insecticide killing power remaining at age t months.

    Model: exp(-t / tau_insecticide)
    Typically faster decay than physical survival (tau ≈ 12-18 months).
    """
    return math.exp(-t_months / tau_insecticide)


def usage_rate(t_months: float, u0: float, tau_usage: float) -> float:
    """Fraction of households with intact nets actually using them at age t.

    Model: u0 * exp(-t / tau_usage)
    Calibrated: u0=0.80, ~0.65 at 12 months → tau ≈ 48 months.
    """
    return u0 * math.exp(-t_months / tau_usage)


def net_efficacy(
    t_months: float,
    tau_physical: float,
    tau_insecticide: float,
    tau_usage: float,
    u0: float = 0.80,
) -> float:
    """Combined net efficacy at age t months.

    efficacy(t) = physical_survival(t) * insecticide_efficacy(t) * usage(t)
    """
    return (
        physical_survival(t_months, tau_physical)
        * insecticide_efficacy(t_months, tau_insecticide)
        * usage_rate(t_months, u0, tau_usage)
    )


# ---------------------------------------------------------------------------
# Time integration
# ---------------------------------------------------------------------------

def integrate_efficacy_over_cycle(
    interval_months: int,
    tau_physical: float,
    tau_insecticide: float,
    tau_usage: float,
    u0: float = 0.80,
    dt: float = 0.5,
) -> float:
    """Compute average efficacy over one distribution cycle using trapezoidal rule.

    Args:
        interval_months: Length of one distribution cycle (D).
        tau_physical, tau_insecticide, tau_usage: Decay time constants.
        u0: Initial usage rate post-distribution.
        dt: Integration step size in months.

    Returns:
        Time-weighted average efficacy over the cycle (0 to 1).
    """
    n_steps = max(1, int(interval_months / dt))
    actual_dt = interval_months / n_steps

    total = 0.0
    e_prev = net_efficacy(0, tau_physical, tau_insecticide, tau_usage, u0)
    for i in range(1, n_steps + 1):
        t = i * actual_dt
        e_curr = net_efficacy(t, tau_physical, tau_insecticide, tau_usage, u0)
        total += (e_prev + e_curr) / 2.0 * actual_dt
        e_prev = e_curr

    return total / interval_months


# ---------------------------------------------------------------------------
# Cost model
# ---------------------------------------------------------------------------

def derive_cost_per_person_year(country_key: str) -> float:
    """Derive implied cost per person-year of protection from the static model.

    The static model assumes $1M grant produces a fixed number of person-years
    (sum of u5 + 5-14 + over14 at default usage). We back-calculate:
        cost_per_py = grant_size / total_person_years

    This avoids needing per-net costs from the spreadsheet.
    """
    c = COUNTRIES[country_key]
    total_py = c.person_years_u5 + c.person_years_5_14 + c.person_years_over14
    return c.grant_size / total_py


# ---------------------------------------------------------------------------
# Temporal CEA
# ---------------------------------------------------------------------------

def compute_temporal_cea(
    country_key: str,
    *,
    distribution_interval_months: int = 30,
    fixed_logistics_fraction: float = 0.15,
    tau_physical: float = 20.5,
    tau_insecticide: float = 15.0,
    tau_usage: float = 48.0,
    program_years: int = 10,
    # Original 5 parameters (passed through to static model)
    incidence_reduction: float = DEFAULT_INCIDENCE_REDUCTION,
    net_usage_adj: float = DEFAULT_NET_USAGE_ADJ,
    external_validity: float = DEFAULT_EXTERNAL_VALIDITY,
    indirect_deaths_multiplier: float = DEFAULT_INDIRECT_DEATHS_MULTIPLIER,
    over5_relative_efficacy: float = DEFAULT_OVER5_RELATIVE_EFFICACY,
) -> dict[str, float]:
    """Compute CEA with net degradation over time.

    The temporal model replaces the mortality reduction pathway only.
    It computes a time-weighted average efficacy, then scales the static
    model's deaths_averted by this factor. Everything downstream (value of
    life, income effects, DALY conversion) uses the original calculation chain.

    The cost side uses a derived cost-per-person-year-of-protection basis,
    with a fixed logistics overhead per distribution cycle.

    Args:
        country_key: Country program key.
        distribution_interval_months: How often nets are distributed (12-48).
        fixed_logistics_fraction: Logistics overhead per cycle as fraction of
            variable cost (0.05-0.30).
        tau_physical: Physical survival time constant (15-30 months).
        tau_insecticide: Insecticide decay time constant (8-24 months).
        tau_usage: Usage decay time constant (30-72 months).
        program_years: Program horizon in years (default 10).
        incidence_reduction ... over5_relative_efficacy: Original 5 CEA params.

    Returns:
        Dict with cost_per_daly, deaths_averted_per_million, total_program_cost,
        average_net_efficacy, num_distribution_cycles, ce_scaling_factor.
    """
    c = COUNTRIES[country_key]

    # --- Time integration ---
    # Average efficacy over one distribution cycle (same for all cycles
    # since full replacement resets to initial levels)
    avg_efficacy = integrate_efficacy_over_cycle(
        distribution_interval_months, tau_physical, tau_insecticide, tau_usage,
    )

    # --- Static model baseline (what the static model assumes) ---
    # The static model implicitly assumes constant efficacy = 1.0 over the net
    # lifespan. The scaling factor is how much realized protection the temporal
    # model delivers relative to this assumption.
    efficacy_scaling = avg_efficacy

    # Get static model results with the original 5 parameters
    static_result = compute_country_ce(
        country_key,
        incidence_reduction=incidence_reduction,
        net_usage_adj=net_usage_adj,
        external_validity=external_validity,
        indirect_deaths_multiplier=indirect_deaths_multiplier,
        over5_relative_efficacy=over5_relative_efficacy,
    )

    # Scale deaths averted by the efficacy scaling factor
    # This is the core composition: temporal layer modulates realized protection
    deaths_averted_scaled = static_result["deaths_averted"] * efficacy_scaling

    # --- Cost model ---
    cost_per_py = derive_cost_per_person_year(country_key)
    total_py = c.person_years_u5 + c.person_years_5_14 + c.person_years_over14

    # Number of distribution cycles over the program horizon
    program_months = program_years * 12
    num_cycles = math.ceil(program_months / distribution_interval_months)

    # Cost per cycle: variable (nets) + fixed logistics overhead
    variable_cost_per_cycle = cost_per_py * total_py  # = grant_size for one cycle
    fixed_cost_per_cycle = variable_cost_per_cycle * fixed_logistics_fraction
    cost_per_cycle = variable_cost_per_cycle + fixed_cost_per_cycle

    total_program_cost = num_cycles * cost_per_cycle

    # Deaths averted over the full program horizon
    # Static model gives deaths per single grant cycle. Scale by program years
    # relative to the implied cycle length (30 months = 2.5 years in static model),
    # then by efficacy scaling.
    static_cycle_years = 30.0 / 12.0  # 2.5 years — GiveWell's implicit cycle
    deaths_over_horizon = deaths_averted_scaled * (program_years / static_cycle_years)

    # --- DALY conversion ---
    dalys_per_death = 29.02
    total_dalys = deaths_over_horizon * dalys_per_death
    cost_per_daly = total_program_cost / total_dalys if total_dalys > 0 else float("inf")

    return {
        "cost_per_daly": cost_per_daly,
        "deaths_averted_per_million": deaths_averted_scaled,  # per single cycle, for comparability
        "total_program_cost": total_program_cost,
        "average_net_efficacy": avg_efficacy,
        "num_distribution_cycles": num_cycles,
        "ce_scaling_factor": efficacy_scaling,
    }
```

- [ ] **Step 2: Run decay curve tests**

```bash
.venv/bin/python optimize/test_temporal.py
```

Expected: `All decay curve tests PASSED`

- [ ] **Step 3: Commit**

```bash
git add optimize/cea_model_temporal.py optimize/test_temporal.py
git commit -m "feat: add temporal decay model with calibrated net degradation curves

Exponential decay for physical survival (tau=20.5, AMF data),
insecticide efficacy (tau=15), and usage (tau=48, AMF data).
Time integration via trapezoidal rule. Composes with static model
via efficacy scaling factor.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

### Task 4: Baseline reproduction test

**Files:**
- Modify: `optimize/test_temporal.py`

Add a test that verifies the temporal model approximately reproduces Phase 1 baselines when decay is disabled (very high tau values).

- [ ] **Step 1: Add baseline reproduction test to test_temporal.py**

Append to the existing test file:

```python
def test_baseline_reproduction():
    """With very high tau (no decay) and D=30, temporal model should
    approximate Phase 1 static baselines within 10%.

    Uses Phase 1 result JSONs as comparison targets.
    """
    import json
    from pathlib import Path

    from optimize.cea_model_temporal import compute_temporal_cea

    results_dir = Path("optimize/results")

    # Test Chad and Guinea (the two countries we'll optimize in Phase 2)
    for country_key in ("chad", "guinea"):
        # Load Phase 1 baseline
        with open(results_dir / f"{country_key}.json") as f:
            phase1 = json.load(f)
        baseline_daly = phase1["minimize"]["baseline_metrics"]["cost_per_daly"]

        # Run temporal model with effectively no decay (tau=10000)
        # and zero logistics overhead to match static model assumptions
        result = compute_temporal_cea(
            country_key,
            distribution_interval_months=30,
            fixed_logistics_fraction=0.0,
            tau_physical=10000.0,
            tau_insecticide=10000.0,
            tau_usage=10000.0,
        )

        temporal_daly = result["cost_per_daly"]
        error_pct = abs(temporal_daly - baseline_daly) / baseline_daly * 100

        print(f"{country_key}: Phase 1 $/DALY={baseline_daly:.2f}, "
              f"Temporal $/DALY={temporal_daly:.2f}, error={error_pct:.1f}%")

        assert error_pct < 10.0, (
            f"{country_key}: temporal model diverges {error_pct:.1f}% from "
            f"Phase 1 baseline (threshold: 10%)"
        )

    print("Baseline reproduction test PASSED")
```

Update the `__main__` block:

```python
if __name__ == "__main__":
    test_physical_survival_calibration()
    test_usage_calibration()
    test_insecticide_decay()
    test_combined_efficacy_decays_monotonically()
    print("All decay curve tests PASSED")
    print()
    test_baseline_reproduction()
```

- [ ] **Step 2: Run and verify baseline reproduction**

```bash
.venv/bin/python optimize/test_temporal.py
```

Expected: Both Chad and Guinea within 10% of Phase 1 baselines. If the error is larger, the issue is likely in the cost normalization (the program-horizon scaling of deaths). Debug by comparing `deaths_averted_per_million` and `total_program_cost` independently against the static model's outputs.

- [ ] **Step 3: Commit**

```bash
git add optimize/test_temporal.py
git commit -m "test: add baseline reproduction test for temporal model

Verifies temporal model with no-decay params reproduces Phase 1
static baselines within 10% for Chad and Guinea.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

### Task 5: Temporal objective function

**Files:**
- Create: `optimize/objective_temporal.py`

Wrap the temporal model into the dict-in/dict-out interface the Bayesian optimizer expects.

- [ ] **Step 1: Write the objective function**

```python
"""Temporal CEA objective function for Bayesian optimization.

Wraps the temporal model into the dict-in/dict-out interface
expected by bayesian_opt.py.
"""
from __future__ import annotations

from optimize.cea_model_temporal import compute_temporal_cea


DEFAULT_COUNTRY: str = "chad"


def evaluate_temporal_cea(
    params: dict[str, float],
    country: str = DEFAULT_COUNTRY,
) -> dict[str, float]:
    """Evaluate temporal CEA with parameters from the optimizer.

    Args:
        params: Dict with keys from the 11-dimensional search space:
            Original 5:
                incidence_reduction, net_usage_adj, external_validity,
                indirect_deaths_multiplier, over5_relative_efficacy
            Temporal 5:
                distribution_interval_months, fixed_logistics_fraction,
                tau_physical, tau_insecticide, tau_usage

        country: Country program key.

    Returns:
        Dict with cost_per_daly (primary objective), plus secondary metrics.
    """
    from optimize.cea_model import (
        DEFAULT_EXTERNAL_VALIDITY,
        DEFAULT_INCIDENCE_REDUCTION,
        DEFAULT_INDIRECT_DEATHS_MULTIPLIER,
        DEFAULT_NET_USAGE_ADJ,
        DEFAULT_OVER5_RELATIVE_EFFICACY,
    )

    result = compute_temporal_cea(
        country,
        # Temporal parameters
        distribution_interval_months=int(params.get("distribution_interval_months", 30)),
        fixed_logistics_fraction=params.get("fixed_logistics_fraction", 0.15),
        tau_physical=params.get("tau_physical", 20.5),
        tau_insecticide=params.get("tau_insecticide", 15.0),
        tau_usage=params.get("tau_usage", 48.0),
        # Original 5 parameters
        incidence_reduction=params.get("incidence_reduction", DEFAULT_INCIDENCE_REDUCTION),
        net_usage_adj=params.get("net_usage_adj", DEFAULT_NET_USAGE_ADJ),
        external_validity=params.get("external_validity", DEFAULT_EXTERNAL_VALIDITY),
        indirect_deaths_multiplier=params.get("indirect_deaths_multiplier", DEFAULT_INDIRECT_DEATHS_MULTIPLIER),
        over5_relative_efficacy=params.get("over5_relative_efficacy", DEFAULT_OVER5_RELATIVE_EFFICACY),
    )

    return {
        "cost_per_daly": result["cost_per_daly"],
        "deaths_averted_per_million": result["deaths_averted_per_million"],
        "total_program_cost": result["total_program_cost"],
        "average_net_efficacy": result["average_net_efficacy"],
        "num_distribution_cycles": result["num_distribution_cycles"],
    }
```

- [ ] **Step 2: Smoke test the objective**

```bash
.venv/bin/python -c "
from optimize.objective_temporal import evaluate_temporal_cea
# Default params
r = evaluate_temporal_cea({})
print(f'Default: \$/DALY={r[\"cost_per_daly\"]:.2f}, avg_efficacy={r[\"average_net_efficacy\"]:.3f}, cycles={r[\"num_distribution_cycles\"]}')
# More frequent distribution
r2 = evaluate_temporal_cea({'distribution_interval_months': 18})
print(f'18-month: \$/DALY={r2[\"cost_per_daly\"]:.2f}, avg_efficacy={r2[\"average_net_efficacy\"]:.3f}, cycles={r2[\"num_distribution_cycles\"]}')
# Less frequent distribution
r3 = evaluate_temporal_cea({'distribution_interval_months': 42})
print(f'42-month: \$/DALY={r3[\"cost_per_daly\"]:.2f}, avg_efficacy={r3[\"average_net_efficacy\"]:.3f}, cycles={r3[\"num_distribution_cycles\"]}')
"
```

Expected: 18-month should have higher avg_efficacy but more cycles; 42-month should have lower efficacy but fewer cycles. The cost_per_daly should NOT be monotonic — that's the whole point.

- [ ] **Step 3: Commit**

```bash
git add optimize/objective_temporal.py
git commit -m "feat: add temporal CEA objective function for optimizer

11-dimensional interface: 5 original CEA params + distribution_interval
+ 4 decay/cost params. Returns cost_per_daly as primary objective.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

### Task 6: Temporal Bayesian optimizer + runner

**Files:**
- Create: `optimize/bayesian_opt_temporal.py`
- Create: `optimize/run_temporal.py`

Adapt the Phase 1 optimizer for the 11-dimensional temporal search space. Create a runner that targets Chad + Guinea first.

- [ ] **Step 1: Write the temporal optimizer**

```python
"""GP-based Bayesian optimization for the temporal ITN CEA model.

Extends the Phase 1 optimizer to the 11-dimensional temporal search space.
Uses the same Sobol + GP + EI architecture.
"""
from __future__ import annotations

import warnings
from dataclasses import dataclass

import numpy as np
from scipy.optimize import minimize as scipy_minimize
from scipy.stats import norm, qmc
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern, ConstantKernel

from optimize.cea_model import COUNTRIES
from optimize.objective_temporal import evaluate_temporal_cea


@dataclass(frozen=True)
class ParamSpec:
    name: str
    lo: float
    hi: float


SEARCH_SPACE: list[ParamSpec] = [
    # Original 5 parameters
    ParamSpec("incidence_reduction", 0.25, 0.50),
    ParamSpec("net_usage_adj", -0.30, 0.0),
    ParamSpec("external_validity", -0.25, 0.0),
    ParamSpec("indirect_deaths_multiplier", 0.40, 1.00),
    ParamSpec("over5_relative_efficacy", 0.40, 1.00),
    # Design variable
    ParamSpec("distribution_interval_months", 12.0, 48.0),
    # Temporal parameters
    ParamSpec("fixed_logistics_fraction", 0.05, 0.30),
    ParamSpec("tau_physical", 15.0, 30.0),
    ParamSpec("tau_insecticide", 8.0, 24.0),
    ParamSpec("tau_usage", 30.0, 72.0),
]

PARAM_NAMES: list[str] = [p.name for p in SEARCH_SPACE]
N_PARAMS: int = len(SEARCH_SPACE)


def _to_unit(x: np.ndarray) -> np.ndarray:
    lo = np.array([p.lo for p in SEARCH_SPACE])
    hi = np.array([p.hi for p in SEARCH_SPACE])
    return (x - lo) / (hi - lo)


def _from_unit(u: np.ndarray) -> np.ndarray:
    lo = np.array([p.lo for p in SEARCH_SPACE])
    hi = np.array([p.hi for p in SEARCH_SPACE])
    return lo + u * (hi - lo)


def _x_to_params(x: np.ndarray) -> dict[str, float]:
    return {name: float(x[i]) for i, name in enumerate(PARAM_NAMES)}


def _expected_improvement(
    X_candidates: np.ndarray,
    gp: GaussianProcessRegressor,
    best_y: float,
    direction: str,
) -> np.ndarray:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        mu, sigma = gp.predict(X_candidates, return_std=True)
    sigma = np.maximum(sigma, 1e-9)
    if direction == "minimize":
        improvement = best_y - mu
    else:
        improvement = mu - best_y
    z = improvement / sigma
    return improvement * norm.cdf(z) + sigma * norm.pdf(z)


def _propose_next(
    gp: GaussianProcessRegressor,
    best_y: float,
    direction: str,
    n_restarts: int = 15,
) -> np.ndarray:
    """Find point in [0,1]^d maximizing EI. More restarts for higher-dim space."""
    best_ei = -1.0
    best_x = None
    for _ in range(n_restarts):
        x0 = np.random.rand(N_PARAMS)
        def neg_ei(x: np.ndarray) -> float:
            return -_expected_improvement(x.reshape(1, -1), gp, best_y, direction)[0]
        result = scipy_minimize(neg_ei, x0, bounds=[(0, 1)] * N_PARAMS, method="L-BFGS-B")
        if -result.fun > best_ei:
            best_ei = -result.fun
            best_x = result.x
    return np.clip(best_x, 0, 1)


def optimize_country_temporal(
    country_key: str,
    direction: str = "minimize",
    n_sobol: int = 25,
    n_bo: int = 75,
    seed: int = 42,
    verbose: bool = True,
) -> dict:
    """Run Bayesian optimization on the temporal CEA for one country.

    Args:
        country_key: Country program key.
        direction: "minimize" or "maximize" cost_per_daly.
        n_sobol: Sobol initialization trials (default 25 for 10D).
        n_bo: GP-based trials (default 75).
        seed: Random seed.
        verbose: Print progress.

    Returns:
        Dict with best_params, best_metrics, baseline_metrics, trial_history.
    """
    assert country_key in COUNTRIES, f"Unknown country: {country_key}"
    assert direction in ("minimize", "maximize")

    rng = np.random.RandomState(seed)
    np.random.seed(seed)
    n_total = n_sobol + n_bo

    # Baseline: temporal model at default params
    baseline = evaluate_temporal_cea({}, country=country_key)

    if verbose:
        label = "MIN" if direction == "minimize" else "MAX"
        print(f"  [{label}] {COUNTRIES[country_key].name}: "
              f"baseline $/DALY = {baseline['cost_per_daly']:.2f}")

    # --- Phase 1: Sobol initialization ---
    sampler = qmc.Sobol(d=N_PARAMS, scramble=True, seed=seed)
    sobol_unit = sampler.random(n_sobol)

    X_unit = []
    X_raw = []
    Y = []

    for i in range(n_sobol):
        raw = _from_unit(sobol_unit[i])
        params = _x_to_params(raw)
        result = evaluate_temporal_cea(params, country=country_key)
        X_unit.append(sobol_unit[i])
        X_raw.append(raw)
        Y.append(result["cost_per_daly"])

    X_unit_arr = np.array(X_unit)
    Y_arr = np.array(Y)

    if direction == "minimize":
        best_idx = int(np.argmin(Y_arr))
    else:
        best_idx = int(np.argmax(Y_arr))
    best_y = Y_arr[best_idx]

    if verbose:
        print(f"         Sobol best $/DALY = {best_y:.2f} (trial {best_idx + 1})")

    # --- Phase 2: GP-based Bayesian optimization ---
    kernel = ConstantKernel(1.0) * Matern(nu=2.5, length_scale=np.ones(N_PARAMS))

    for i in range(n_bo):
        gp = GaussianProcessRegressor(
            kernel=kernel,
            n_restarts_optimizer=3,
            normalize_y=True,
            random_state=rng,
        )
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            gp.fit(X_unit_arr, Y_arr)

        next_unit = _propose_next(gp, best_y, direction)
        next_raw = _from_unit(next_unit)
        params = _x_to_params(next_raw)
        result = evaluate_temporal_cea(params, country=country_key)
        y = result["cost_per_daly"]

        X_unit_arr = np.vstack([X_unit_arr, next_unit])
        X_raw.append(next_raw)
        Y.append(y)
        Y_arr = np.append(Y_arr, y)

        if direction == "minimize" and y < best_y:
            best_y = y
            best_idx = len(Y) - 1
        elif direction == "maximize" and y > best_y:
            best_y = y
            best_idx = len(Y) - 1

        if verbose and (i + 1) % 25 == 0:
            print(f"         BO trial {i + 1}/{n_bo}, best $/DALY = {best_y:.2f}")

    if verbose:
        print(f"         Final best $/DALY = {best_y:.2f} "
              f"(trial {best_idx + 1}/{n_total})")

    # --- Collect results ---
    best_raw = X_raw[best_idx]
    best_params = _x_to_params(best_raw)
    best_metrics = evaluate_temporal_cea(best_params, country=country_key)

    at_bound = {}
    for j, spec in enumerate(SEARCH_SPACE):
        val = best_raw[j]
        if abs(val - spec.lo) < 1e-6 * (spec.hi - spec.lo):
            at_bound[spec.name] = "lower"
        elif abs(val - spec.hi) < 1e-6 * (spec.hi - spec.lo):
            at_bound[spec.name] = "upper"

    trial_history = []
    for idx in range(len(Y)):
        trial_history.append({
            "trial": idx + 1,
            "phase": "sobol" if idx < n_sobol else "bayesian",
            "params": _x_to_params(X_raw[idx]),
            "cost_per_daly": Y[idx],
        })

    return {
        "country": country_key,
        "country_name": COUNTRIES[country_key].name,
        "direction": direction,
        "best_params": best_params,
        "best_metrics": best_metrics,
        "baseline_metrics": baseline,
        "at_bound": at_bound,
        "n_trials": n_total,
        "trial_history": trial_history,
    }
```

- [ ] **Step 2: Write the runner**

```python
"""Entry point for temporal ITN CEA optimization.

Usage:
    python -m optimize.run_temporal                     # Chad + Guinea (validation)
    python -m optimize.run_temporal --country chad      # single country
    python -m optimize.run_temporal --all               # all 8 countries
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np

from optimize.bayesian_opt_temporal import (
    PARAM_NAMES,
    SEARCH_SPACE,
    optimize_country_temporal,
)
from optimize.cea_model import COUNTRIES

RESULTS_DIR = Path("optimize/results")
VALIDATION_COUNTRIES = ["chad", "guinea"]

N_SOBOL = 25
N_BO = 75


def _serialize(obj: object) -> object:
    """JSON serializer that handles numpy types."""
    if isinstance(obj, (np.floating, float)):
        return float(obj)
    if isinstance(obj, (np.integer, int)):
        return int(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    raise TypeError(f"Not serializable: {type(obj)}")


def run_country(country_key: str) -> dict:
    """Run both minimize and maximize for one country."""
    print(f"\n{'='*60}")
    print(f"  TEMPORAL: {COUNTRIES[country_key].name}")
    print(f"{'='*60}")

    results = {}
    for direction in ("minimize", "maximize"):
        t0 = time.time()
        result = optimize_country_temporal(
            country_key,
            direction=direction,
            n_sobol=N_SOBOL,
            n_bo=N_BO,
            seed=42,
            verbose=True,
        )
        elapsed = time.time() - t0
        result["elapsed_seconds"] = round(elapsed, 1)
        results[direction] = result
        print(f"         ({elapsed:.1f}s)")

    # Save per-country JSON
    out_path = RESULTS_DIR / f"{country_key}_temporal.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=_serialize)

    return results


def generate_temporal_summary(all_results: dict[str, dict]) -> str:
    """Generate temporal_summary.md comparing static vs temporal models."""
    lines = [
        "# Phase 2: Temporal Dynamics — Optimization Summary",
        "",
        "Net degradation (physical survival, insecticide decay, usage decline) ×",
        "distribution frequency as design variable.",
        f"Each country: {N_SOBOL} Sobol + {N_BO} BO = {N_SOBOL + N_BO} trials, "
        "both minimize and maximize cost_per_daly.",
        "",
    ]

    # --- Section 1: Optimal distribution intervals ---
    lines += [
        "## Optimal Distribution Intervals",
        "",
        "Does the optimizer find a non-trivial optimum for distribution frequency?",
        "",
        "| Country | Direction | Optimal Interval (months) | At Bound? | "
        "Default 30mo $/DALY | Optimized $/DALY | Improvement |",
        "|---------|-----------|:---:|:---:|---:|---:|---:|",
    ]

    for key in all_results:
        for direction, label in [("minimize", "Best"), ("maximize", "Worst")]:
            d = all_results[key][direction]
            interval = d["best_params"]["distribution_interval_months"]
            at_bound = "distribution_interval_months" in d.get("at_bound", {})
            bound_marker = " (bound)" if at_bound else ""
            baseline_daly = d["baseline_metrics"]["cost_per_daly"]
            best_daly = d["best_metrics"]["cost_per_daly"]
            if direction == "minimize":
                improvement = (baseline_daly - best_daly) / baseline_daly * 100
            else:
                improvement = (best_daly - baseline_daly) / baseline_daly * 100
            lines.append(
                f"| {COUNTRIES[key].name} | {label} | "
                f"{interval:.1f}{bound_marker} | "
                f"{'Yes' if at_bound else 'No'} | "
                f"${baseline_daly:.0f} | ${best_daly:.0f} | {improvement:.1f}% |"
            )

    # --- Section 2: Static vs Temporal comparison ---
    lines += [
        "",
        "## Static vs Temporal Comparison",
        "",
        "Phase 1 static CE vs temporal CE at default 30-month cycle vs optimized.",
        "",
        "| Country | Static $/DALY (Phase 1) | Temporal $/DALY (D=30) | "
        "Temporal $/DALY (optimized) | Optimal D |",
        "|---------|---:|---:|---:|:---:|",
    ]

    for key in all_results:
        # Load Phase 1 baseline
        phase1_path = RESULTS_DIR / f"{key}.json"
        phase1_daly = "N/A"
        try:
            with open(phase1_path) as f:
                phase1 = json.load(f)
            phase1_daly = f"${phase1['minimize']['baseline_metrics']['cost_per_daly']:.0f}"
        except (FileNotFoundError, KeyError):
            pass

        d = all_results[key]["minimize"]
        temporal_default = d["baseline_metrics"]["cost_per_daly"]
        temporal_opt = d["best_metrics"]["cost_per_daly"]
        opt_interval = d["best_params"]["distribution_interval_months"]

        lines.append(
            f"| {COUNTRIES[key].name} | {phase1_daly} | "
            f"${temporal_default:.0f} | ${temporal_opt:.0f} | {opt_interval:.0f}mo |"
        )

    # --- Section 3: Which decay parameters matter most ---
    lines += [
        "",
        "## Decay Parameter Sensitivity",
        "",
        "Which decay parameters the optimizer pushes hardest (best-case direction).",
        "",
        "| Country | tau_physical | tau_insecticide | tau_usage | logistics_frac | interval |",
        "|---------|:---:|:---:|:---:|:---:|:---:|",
    ]

    for key in all_results:
        d = all_results[key]["minimize"]
        p = d["best_params"]
        ab = d.get("at_bound", {})
        def fmt(name: str) -> str:
            val = p[name]
            marker = " *" if name in ab else ""
            return f"{val:.1f}{marker}"
        lines.append(
            f"| {COUNTRIES[key].name} | "
            f"{fmt('tau_physical')} | {fmt('tau_insecticide')} | "
            f"{fmt('tau_usage')} | {p['fixed_logistics_fraction']:.2f} | "
            f"{p['distribution_interval_months']:.0f}mo |"
        )

    # --- Section 4: Non-monotonicity check ---
    lines += [
        "",
        "## Non-Monotonicity Analysis",
        "",
        "Parameters hitting bounds in the temporal model. Interior optima (not at bound) ",
        "indicate genuine trade-offs — the whole point of Phase 2.",
        "",
        "| Parameter | Hit Lower | Hit Upper | Interior Optima | Total Runs |",
        "|-----------|:-:|:-:|:-:|:-:|",
    ]

    n_runs = len(all_results) * 2  # both directions
    bound_counts: dict[str, dict[str, int]] = {
        name: {"lower": 0, "upper": 0} for name in PARAM_NAMES
    }
    for key in all_results:
        for direction in ("minimize", "maximize"):
            for name, side in all_results[key][direction].get("at_bound", {}).items():
                bound_counts[name][side] += 1

    for name in PARAM_NAMES:
        lo = bound_counts[name]["lower"]
        hi = bound_counts[name]["upper"]
        interior = n_runs - lo - hi
        lines.append(f"| {name} | {lo} | {hi} | {interior} | {n_runs} |")

    # --- Note about remaining countries ---
    if len(all_results) < len(COUNTRIES):
        run_names = [COUNTRIES[k].name for k in all_results]
        remaining = [COUNTRIES[k].name for k in COUNTRIES if k not in all_results]
        lines += [
            "",
            f"## Note",
            "",
            f"Optimization ran for {', '.join(run_names)} only (validation set). ",
            f"Remaining countries ({', '.join(remaining)}) should be run if results ",
            "show non-trivial behavior.",
        ]

    lines += [
        "",
        "---",
        "",
        "Generated by `optimize/run_temporal.py`.",
        "",
        "\\* = parameter at search space boundary",
    ]

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run temporal ITN CEA optimization")
    parser.add_argument("--country", type=str, default=None, help="Single country key")
    parser.add_argument("--all", action="store_true", help="Run all 8 countries")
    args = parser.parse_args()

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    if args.all:
        countries = list(COUNTRIES.keys())
    elif args.country:
        countries = [args.country]
    else:
        countries = VALIDATION_COUNTRIES

    all_results: dict[str, dict] = {}

    t_start = time.time()
    for key in countries:
        all_results[key] = run_country(key)
    total_time = time.time() - t_start

    print(f"\n{'='*60}")
    print(f"  DONE — {len(countries)} countries, {total_time:.1f}s total")
    print(f"{'='*60}")

    # Generate summary
    summary = generate_temporal_summary(all_results)
    summary_path = RESULTS_DIR / "temporal_summary.md"
    summary_path.write_text(summary)
    print(f"\nSummary written to {summary_path}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 3: Smoke-test the optimizer on Chad minimize only (fast check)**

```bash
.venv/bin/python -c "
from optimize.bayesian_opt_temporal import optimize_country_temporal
r = optimize_country_temporal('chad', direction='minimize', n_sobol=5, n_bo=5, verbose=True)
print(f'Best interval: {r[\"best_params\"][\"distribution_interval_months\"]:.0f} months')
print(f'Best \$/DALY: {r[\"best_metrics\"][\"cost_per_daly\"]:.2f}')
print(f'At bound: {r[\"at_bound\"]}')
"
```

Expected: Runs without errors. Best interval may or may not be at a bound with only 10 trials — the full 100-trial run will reveal the real answer.

- [ ] **Step 4: Commit**

```bash
git add optimize/bayesian_opt_temporal.py optimize/run_temporal.py
git commit -m "feat: add temporal Bayesian optimizer and runner

11-dimensional search space (5 original + distribution_interval +
4 decay/cost params). 25 Sobol + 75 BO trials per direction.
Defaults to Chad + Guinea validation set.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

### Task 7: Run the full optimization (Chad + Guinea)

**Files:**
- Creates: `optimize/results/chad_temporal.json`, `optimize/results/guinea_temporal.json`, `optimize/results/temporal_summary.md`

- [ ] **Step 1: Run the optimization**

```bash
.venv/bin/python -m optimize.run_temporal
```

This runs Chad + Guinea, both directions, ~100 trials each = ~400 total evaluations. Should take 2-10 minutes depending on GP fitting time.

Expected output: Per-country results printed to console, JSON files saved, `temporal_summary.md` generated.

- [ ] **Step 2: Inspect results — check for interior optima**

```bash
.venv/bin/python -c "
import json
for country in ('chad', 'guinea'):
    with open(f'optimize/results/{country}_temporal.json') as f:
        r = json.load(f)
    for d in ('minimize', 'maximize'):
        p = r[d]['best_params']
        ab = r[d].get('at_bound', {})
        interval = p['distribution_interval_months']
        at_bound = 'distribution_interval_months' in ab
        print(f'{country} {d}: interval={interval:.1f}mo, at_bound={at_bound}')
        print(f'  $/DALY: baseline={r[d][\"baseline_metrics\"][\"cost_per_daly\"]:.2f}, best={r[d][\"best_metrics\"][\"cost_per_daly\"]:.2f}')
        print(f'  avg_efficacy={r[d][\"best_metrics\"][\"average_net_efficacy\"]:.3f}')
"
```

The key finding: Is `distribution_interval_months` at a bound (12 or 48) or at an interior value? Interior = genuine trade-off found.

- [ ] **Step 3: Commit results**

```bash
git add optimize/results/chad_temporal.json optimize/results/guinea_temporal.json optimize/results/temporal_summary.md
git commit -m "results: Phase 2 temporal optimization for Chad and Guinea

Bidirectional optimization with net degradation and distribution
frequency as design variable. See temporal_summary.md for analysis.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

### Task 8: Review results and decide on remaining countries

**Files:**
- Possibly modifies: `optimize/results/temporal_summary.md`

This is a judgment call, not code.

- [ ] **Step 1: Read temporal_summary.md**

Read the generated summary. Key questions:
1. Did distribution_interval_months land at an interior optimum for either country?
2. Did any of the original 5 parameters stop hitting bounds (i.e., did temporal dynamics create parameter interactions)?
3. Is the cost_per_daly at the optimized interval meaningfully different from the default 30-month cycle?

- [ ] **Step 2: Decide whether to run remaining 6 countries**

If Chad and/or Guinea show interesting behavior (interior optima, non-monotonicity in any parameter), run all 8:

```bash
.venv/bin/python -m optimize.run_temporal --all
```

Then regenerate the summary. If results are all monotonic, document that finding and do not run the remaining countries — the result is still informative.

- [ ] **Step 3: Final commit**

```bash
git add optimize/results/
git commit -m "results: Phase 2 temporal dynamics complete

[Include 1-sentence finding: interior optimum found / all monotonic]

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```
