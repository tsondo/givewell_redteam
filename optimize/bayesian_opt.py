"""GP-based Bayesian optimization loop for ITN CEA parameters.

Uses Sobol quasi-random initialization + sklearn Gaussian Process surrogate +
Expected Improvement acquisition function.  No Ax/PyTorch dependency.
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
from optimize.objective import evaluate_cea


# ---------------------------------------------------------------------------
# Search space definition (5 active parameters, insecticide_resistance excluded)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class ParamSpec:
    name: str
    lo: float
    hi: float


SEARCH_SPACE: list[ParamSpec] = [
    ParamSpec("incidence_reduction", 0.25, 0.50),
    ParamSpec("net_usage_adj", -0.30, 0.0),
    ParamSpec("external_validity", -0.25, 0.0),
    ParamSpec("indirect_deaths_multiplier", 0.40, 1.00),
    ParamSpec("over5_relative_efficacy", 0.40, 1.00),
]

PARAM_NAMES: list[str] = [p.name for p in SEARCH_SPACE]
N_PARAMS: int = len(SEARCH_SPACE)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _to_unit(x: np.ndarray) -> np.ndarray:
    """Map raw parameter values to [0, 1] for GP fitting."""
    lo = np.array([p.lo for p in SEARCH_SPACE])
    hi = np.array([p.hi for p in SEARCH_SPACE])
    return (x - lo) / (hi - lo)


def _from_unit(u: np.ndarray) -> np.ndarray:
    """Map [0, 1] values back to raw parameter space."""
    lo = np.array([p.lo for p in SEARCH_SPACE])
    hi = np.array([p.hi for p in SEARCH_SPACE])
    return lo + u * (hi - lo)


def _x_to_params(x: np.ndarray) -> dict[str, float]:
    """Convert a raw parameter vector to the dict evaluate_cea expects."""
    return {name: float(x[i]) for i, name in enumerate(PARAM_NAMES)}


def _expected_improvement(
    X_candidates: np.ndarray,
    gp: GaussianProcessRegressor,
    best_y: float,
    direction: str,
) -> np.ndarray:
    """Compute Expected Improvement for candidate points.

    For minimize: EI = E[max(best_y - Y, 0)]
    For maximize: EI = E[max(Y - best_y, 0)]
    """
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        mu, sigma = gp.predict(X_candidates, return_std=True)

    sigma = np.maximum(sigma, 1e-9)

    if direction == "minimize":
        improvement = best_y - mu
    else:
        improvement = mu - best_y

    z = improvement / sigma
    ei = improvement * norm.cdf(z) + sigma * norm.pdf(z)
    return ei


def _propose_next(
    gp: GaussianProcessRegressor,
    best_y: float,
    direction: str,
    n_restarts: int = 10,
) -> np.ndarray:
    """Find the point in [0,1]^d that maximizes Expected Improvement."""
    dim = N_PARAMS
    best_ei = -1.0
    best_x = None

    for _ in range(n_restarts):
        x0 = np.random.rand(dim)

        def neg_ei(x: np.ndarray) -> float:
            ei = _expected_improvement(
                x.reshape(1, -1), gp, best_y, direction,
            )
            return -ei[0]

        result = scipy_minimize(
            neg_ei,
            x0,
            bounds=[(0, 1)] * dim,
            method="L-BFGS-B",
        )
        if -result.fun > best_ei:
            best_ei = -result.fun
            best_x = result.x

    return np.clip(best_x, 0, 1)


# ---------------------------------------------------------------------------
# Main optimization loop
# ---------------------------------------------------------------------------

def optimize_country(
    country_key: str,
    direction: str = "minimize",
    n_sobol: int = 15,
    n_bo: int = 35,
    seed: int = 42,
    verbose: bool = True,
) -> dict:
    """Run Bayesian optimization for one country in one direction.

    Args:
        country_key: One of the 8 country keys from COUNTRIES.
        direction: "minimize" (best case CE) or "maximize" (worst case CE).
        n_sobol: Number of Sobol quasi-random initial trials.
        n_bo: Number of GP-based Bayesian optimization trials.
        seed: Random seed for reproducibility.
        verbose: Print progress.

    Returns:
        Dict with best_params, best_metrics, baseline_metrics, trial_history.
    """
    assert country_key in COUNTRIES, f"Unknown country: {country_key}"
    assert direction in ("minimize", "maximize")

    rng = np.random.RandomState(seed)
    np.random.seed(seed)
    n_total = n_sobol + n_bo

    # Baseline evaluation
    baseline = evaluate_cea({}, country=country_key)

    if verbose:
        label = "MIN" if direction == "minimize" else "MAX"
        print(f"  [{label}] {COUNTRIES[country_key].name}: "
              f"baseline $/DALY = {baseline['cost_per_daly']:.2f}")

    # --- Phase 1: Sobol initialization ---
    sampler = qmc.Sobol(d=N_PARAMS, scramble=True, seed=seed)
    sobol_unit = sampler.random(n_sobol)  # shape (n_sobol, N_PARAMS) in [0,1]

    X_unit = []   # normalized points
    X_raw = []    # raw parameter values
    Y = []        # cost_per_daly observations

    for i in range(n_sobol):
        raw = _from_unit(sobol_unit[i])
        params = _x_to_params(raw)
        result = evaluate_cea(params, country=country_key)
        X_unit.append(sobol_unit[i])
        X_raw.append(raw)
        Y.append(result["cost_per_daly"])

    X_unit_arr = np.array(X_unit)
    Y_arr = np.array(Y)

    # Track best
    if direction == "minimize":
        best_idx = int(np.argmin(Y_arr))
    else:
        best_idx = int(np.argmax(Y_arr))
    best_y = Y_arr[best_idx]

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

        # Propose next point
        next_unit = _propose_next(gp, best_y, direction)
        next_raw = _from_unit(next_unit)
        params = _x_to_params(next_raw)
        result = evaluate_cea(params, country=country_key)
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

    if verbose:
        print(f"         best $/DALY = {best_y:.2f} "
              f"(trial {best_idx + 1}/{n_total})")

    # --- Collect results ---
    best_raw = X_raw[best_idx]
    best_params = _x_to_params(best_raw)
    best_metrics = evaluate_cea(best_params, country=country_key)

    # Check for parameters hitting bounds
    at_bound = {}
    for j, spec in enumerate(SEARCH_SPACE):
        val = best_raw[j]
        if abs(val - spec.lo) < 1e-6 * (spec.hi - spec.lo):
            at_bound[spec.name] = "lower"
        elif abs(val - spec.hi) < 1e-6 * (spec.hi - spec.lo):
            at_bound[spec.name] = "upper"

    # Trial history
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
