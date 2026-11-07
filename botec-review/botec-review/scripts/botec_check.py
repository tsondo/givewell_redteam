#!/usr/bin/env python3
"""Rebuild a BOTEC from a JSON spec and run one-way sensitivity and break-even analysis.

Standard library only. Usage:

    python botec_check.py model.json            # markdown report to stdout
    python botec_check.py model.json --json     # machine-readable results

Spec format (see the skill's SKILL.md for a full example):

    {
      "title": "Statins for TB",
      "output": "sroi",                      # name of the final step
      "bar": 2000,                           # optional decision threshold
      "higher_is_better": true,              # false for cost-per-outcome metrics
      "stated_result": 3000,                 # optional: the BOTEC's own bottom line
      "params": {
        "p_success": {"value": 0.4, "low": 0.25, "high": 0.5,
                      "unit": "probability", "basis": "judgment"}
      },
      "steps": [                             # evaluated in order; may use params and earlier steps
        ["benefit", "deaths * dalys_per_death * op_per_daly"],
        ["sroi", "benefit / all_in_cost * p_success"]
      ],
      "scenarios": {                         # optional named sets of overrides
        "author_revised": {"p_success": 0.3, "speedup_years": 3}
      },
      "checks": [                            # optional side calculations shown separately;
        ["n_per_arm", "..."]                 # they may use params and steps but never feed the output
      ]
    }

A parameter with no low/high (a fixed convention, or a new factor you only want to use in
scenarios) is listed as fixed and left out of the sensitivity table and break-even search.

Formulas allow + - * / ** and parentheses, numbers, names, and the functions
min, max, abs, log, exp, sqrt.
"""
from __future__ import annotations

import ast
import json
import math
import sys
from pathlib import Path
from typing import Any

_FUNCS = {"min": min, "max": max, "abs": abs, "log": math.log, "exp": math.exp, "sqrt": math.sqrt}
_BINOPS = {ast.Add: lambda a, b: a + b, ast.Sub: lambda a, b: a - b, ast.Mult: lambda a, b: a * b,
           ast.Div: lambda a, b: a / b, ast.Pow: lambda a, b: a ** b}


def _eval(node: ast.AST, env: dict[str, float]) -> float:
    if isinstance(node, ast.Expression):
        return _eval(node.body, env)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    if isinstance(node, ast.Name):
        if node.id not in env:
            raise ValueError(f"unknown name '{node.id}'")
        return env[node.id]
    if isinstance(node, ast.BinOp) and type(node.op) in _BINOPS:
        return _BINOPS[type(node.op)](_eval(node.left, env), _eval(node.right, env))
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
        v = _eval(node.operand, env)
        return -v if isinstance(node.op, ast.USub) else v
    if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
            and node.func.id in _FUNCS and not node.keywords):
        return float(_FUNCS[node.func.id](*[_eval(a, env) for a in node.args]))
    raise ValueError(f"unsupported expression: {ast.dump(node)[:80]}")


def evaluate(spec: dict[str, Any], overrides: dict[str, float] | None = None) -> dict[str, float]:
    """Return every step's value, with optional parameter overrides."""
    overrides = overrides or {}
    unknown = set(overrides) - set(spec["params"])
    if unknown:
        raise ValueError(f"unknown parameters in overrides: {sorted(unknown)}")
    env = {k: float(v["value"]) for k, v in spec["params"].items()}
    env.update({k: float(v) for k, v in overrides.items()})
    for name, formula in spec["steps"]:
        env[name] = _eval(ast.parse(formula, mode="eval"), env)
    return env


def checks(spec: dict[str, Any]) -> dict[str, float]:
    """Evaluate side calculations that don't feed the output."""
    env = evaluate(spec)
    out: dict[str, float] = {}
    for name, formula in spec.get("checks") or []:
        env[name] = out[name] = _eval(ast.parse(formula, mode="eval"), env)
    return out


def result(spec: dict[str, Any], overrides: dict[str, float] | None = None) -> float:
    return evaluate(spec, overrides)[spec["output"]]


def _passes(spec: dict[str, Any], value: float) -> bool | None:
    bar = spec.get("bar")
    if bar is None:
        return None
    return value >= bar if spec.get("higher_is_better", True) else value <= bar


def break_even(spec: dict[str, Any], param: str, iters: int = 200) -> float | None:
    """Value of `param` (others fixed) at which the output equals the bar, or None.

    Searches upward and downward from the current value, up to 1000x either way
    (and through zero to negative values only if the current value is negative).
    """
    bar = spec.get("bar")
    if bar is None:
        return None
    x0 = float(spec["params"][param]["value"])

    def g(x: float) -> float:
        try:
            return result(spec, {param: x}) - bar
        except (ZeroDivisionError, ValueError, OverflowError):
            return math.nan

    g0 = g(x0)
    if math.isnan(g0) or g0 == 0:
        return x0 if g0 == 0 else None
    candidates = []
    if x0 > 0:
        candidates = [x0 * f for f in (0.5, 0.25, 0.1, 0.01, 0.001, 0.0)] + \
                     [x0 * f for f in (2, 4, 10, 100, 1000)]
    elif x0 < 0:
        candidates = [x0 * f for f in (0.5, 0.1, 0.0, 2, 10, 1000)]
    else:
        candidates = [1e-6, 1e-3, 1, 1e3, 1e6, -1e-3, -1, -1e3]
    best: float | None = None
    for c in candidates:
        gc = g(c)
        if math.isnan(gc) or (gc > 0) == (g0 > 0):
            continue
        lo, hi = (x0, c)
        glo = g0
        for _ in range(iters):
            mid = (lo + hi) / 2
            gm = g(mid)
            if math.isnan(gm):
                break
            if (gm > 0) == (glo > 0):
                lo, glo = mid, gm
            else:
                hi = mid
            if abs(hi - lo) <= 1e-12 * max(1.0, abs(x0)):
                break
        root = (lo + hi) / 2
        if best is None or abs(root - x0) < abs(best - x0):
            best = root
    return best


def analyze(spec: dict[str, Any]) -> dict[str, Any]:
    base = result(spec)
    out: dict[str, Any] = {"title": spec.get("title", ""), "output": spec["output"],
                           "result": base, "bar": spec.get("bar"),
                           "passes_bar": _passes(spec, base),
                           "stated_result": spec.get("stated_result"),
                           "intermediates": {n: evaluate(spec)[n] for n, _ in spec["steps"]},
                           "checks": checks(spec), "fixed": [], "params": []}
    stated = spec.get("stated_result")
    if stated:
        out["pct_vs_stated"] = (base - stated) / stated * 100
    for name, p in spec["params"].items():
        if p.get("low") is None and p.get("high") is None:
            out["fixed"].append({"name": name, "value": p["value"], "unit": p.get("unit", ""),
                                 "basis": p.get("basis", "")})
            continue
        row: dict[str, Any] = {"name": name, "value": p["value"], "unit": p.get("unit", ""),
                               "basis": p.get("basis", ""), "low": p.get("low"), "high": p.get("high")}
        for label in ("low", "high"):
            if p.get(label) is not None:
                v = result(spec, {name: p[label]})
                row[f"result_{label}"] = v
                row[f"pct_{label}"] = (v - base) / base * 100 if base else None
                row[f"passes_{label}"] = _passes(spec, v)
        if row.get("result_low") is not None and row.get("result_high") is not None:
            row["swing"] = abs(row["result_high"] - row["result_low"])
        else:
            row["swing"] = 0.0
        be = break_even(spec, name)
        row["break_even"] = be
        lo, hi = p.get("low"), p.get("high")
        row["break_even_in_range"] = (be is not None and lo is not None and hi is not None
                                      and min(lo, hi) <= be <= max(lo, hi))
        out["params"].append(row)
    out["params"].sort(key=lambda r: r["swing"], reverse=True)
    out["scenarios"] = {}
    for sname, ov in (spec.get("scenarios") or {}).items():
        v = result(spec, ov)
        out["scenarios"][sname] = {"overrides": ov, "result": v,
                                   "pct": (v - base) / base * 100 if base else None,
                                   "passes_bar": _passes(spec, v)}
    return out


def _fmt(x: Any) -> str:
    if x is None:
        return "–"
    if isinstance(x, bool):
        return "yes" if x else "no"
    x = float(x)
    if x == 0:
        return "0"
    a = abs(x)
    if a >= 1e9:
        return f"{x/1e9:.3g}B"
    if a >= 1e6:
        return f"{x/1e6:.3g}M"
    if a >= 100:
        return f"{x:,.0f}"
    return f"{x:.3g}"


def _pct(x: Any) -> str:
    return "–" if x is None else f"{x:+.0f}%"


def to_markdown(a: dict[str, Any]) -> str:
    lines = [f"## Model check: {a['title']}" if a["title"] else "## Model check", ""]
    line = f"Rebuilt {a['output']}: **{_fmt(a['result'])}**"
    if a.get("stated_result"):
        line += f" (stated: {_fmt(a['stated_result'])}, {_pct(a['pct_vs_stated'])})"
    if a.get("bar") is not None:
        line += f". Bar: {_fmt(a['bar'])}; {'passes' if a['passes_bar'] else 'does not pass'}."
    lines += [line, "", "Intermediate steps: " + "; ".join(
        f"{k} = {_fmt(v)}" for k, v in a["intermediates"].items()), ""]
    if a["checks"]:
        lines += ["Side checks (do not feed the result): " + "; ".join(
            f"{k} = {_fmt(v)}" for k, v in a["checks"].items()), ""]
    if a["fixed"]:
        lines += ["Fixed (no range, not varied): " + "; ".join(
            f"{r['name']} = {_fmt(r['value'])} {r['unit']}".strip() for r in a["fixed"]), ""]
    lines += ["| Parameter | Value | Range | Result at low / high | Change | Break-even | Break-even in range? |",
              "|---|---|---|---|---|---|---|"]
    for r in a["params"]:
        rng = f"{_fmt(r['low'])}–{_fmt(r['high'])}" if r["low"] is not None else "–"
        res = f"{_fmt(r.get('result_low'))} / {_fmt(r.get('result_high'))}"
        chg = f"{_pct(r.get('pct_low'))} / {_pct(r.get('pct_high'))}"
        be = _fmt(r["break_even"]) if r["break_even"] is not None else "none within 1000x"
        lines.append(f"| {r['name']} | {_fmt(r['value'])} {r['unit']} | {rng} | {res} | {chg} | {be} | "
                     f"{'**yes**' if r['break_even_in_range'] else 'no'} |")
    if a["scenarios"]:
        lines += ["", "| Scenario | Overrides | Result | Change | Passes bar |", "|---|---|---|---|---|"]
        for s, v in a["scenarios"].items():
            ov = ", ".join(f"{k}={_fmt(x)}" for k, x in v["overrides"].items())
            lines.append(f"| {s} | {ov} | {_fmt(v['result'])} | {_pct(v['pct'])} | {_fmt(v['passes_bar'])} |")
    lines += ["", "Rows are sorted by swing. Each row changes one parameter and holds the rest at "
              "their stated values; swings do not add up."]
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    spec = json.loads(Path(argv[0]).read_text(encoding="utf-8"))
    a = analyze(spec)
    print(json.dumps(a, indent=2) if "--json" in argv else to_markdown(a))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
