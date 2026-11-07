"""Tests for the botec-review helper script (stdlib unittest; run with python -m pytest or unittest)."""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "botec-review" / "scripts"))

import botec_check as bc  # noqa: E402

TB = json.loads((ROOT / "tests" / "fixtures" / "tb-statins.json").read_text(encoding="utf-8"))


class TestEvaluate(unittest.TestCase):
    def test_reproduces_published_tb_result(self) -> None:
        # CG's arithmetic: 19,800 deaths x 27 x 100k / 7M x 0.4 = ~3,055x ("about 3,000x")
        self.assertAlmostEqual(bc.result(TB), 3054.857, places=2)

    def test_override(self) -> None:
        self.assertAlmostEqual(bc.result(TB, {"p_success": 0.2}), bc.result(TB) / 2)

    def test_unknown_override_rejected(self) -> None:
        with self.assertRaises(ValueError):
            bc.result(TB, {"nope": 1})

    def test_unsafe_expression_rejected(self) -> None:
        bad = {**TB, "steps": [["sroi", "__import__('os').system('true')"]]}
        with self.assertRaises(ValueError):
            bc.result(bad)

    def test_functions_allowed(self) -> None:
        spec = {"output": "y", "params": {"x": {"value": 4}}, "steps": [["y", "sqrt(x) + max(x, 1)"]]}
        self.assertEqual(bc.result(spec), 6.0)


class TestBreakEven(unittest.TestCase):
    def test_linear_param(self) -> None:
        # SROI is linear in p_success: break-even = 0.4 * 2000 / 3054.86
        be = bc.break_even(TB, "p_success")
        self.assertAlmostEqual(be, 0.4 * 2000 / bc.result(TB), places=6)

    def test_inverse_param(self) -> None:
        be = bc.break_even(TB, "all_in_cost")
        self.assertAlmostEqual(be, 7e6 * bc.result(TB) / 2000, delta=1)

    def test_no_bar(self) -> None:
        spec = {**TB}
        spec.pop("bar")
        self.assertIsNone(bc.break_even(spec, "p_success"))

    def test_lower_is_better(self) -> None:
        spec = {"output": "cost_per_life", "bar": 5000, "higher_is_better": False,
                "params": {"cost": {"value": 1e6, "low": 8e5, "high": 2e6}, "lives": {"value": 250}},
                "steps": [["cost_per_life", "cost / lives"]]}
        a = bc.analyze(spec)
        self.assertTrue(a["passes_bar"])
        cost_row = next(r for r in a["params"] if r["name"] == "cost")
        self.assertAlmostEqual(cost_row["break_even"], 1.25e6, delta=1)
        self.assertTrue(cost_row["break_even_in_range"])
        self.assertFalse(cost_row["passes_high"])


class TestAnalyze(unittest.TestCase):
    def test_sorted_by_swing_and_flags(self) -> None:
        a = bc.analyze(TB)
        swings = [r["swing"] for r in a["params"]]
        self.assertEqual(swings, sorted(swings, reverse=True))
        self.assertEqual(a["params"][0]["name"], "speedup_years")
        p = next(r for r in a["params"] if r["name"] == "p_success")
        self.assertTrue(p["break_even_in_range"])
        self.assertAlmostEqual(a["pct_vs_stated"], 1.83, places=1)

    def test_scenarios(self) -> None:
        spec = {**TB, "scenarios": {"revised": {"p_success": 0.3, "speedup_years": 3}}}
        a = bc.analyze(spec)
        self.assertAlmostEqual(a["scenarios"]["revised"]["result"], bc.result(TB) * 0.75 * 3)

    def test_markdown_renders(self) -> None:
        md = bc.to_markdown(bc.analyze(TB))
        self.assertIn("| speedup_years |", md)
        self.assertIn("Rebuilt sroi: **3,055**", md)


class TestChecksAndFixed(unittest.TestCase):
    def test_fixed_params_not_varied(self) -> None:
        a = bc.analyze(TB)
        self.assertNotIn("op_per_daly", [r["name"] for r in a["params"]])
        self.assertEqual(a["fixed"][0]["name"], "op_per_daly")

    def test_checks_do_not_feed_output(self) -> None:
        spec = {**TB, "checks": [["deaths_x2", "deaths_averted_per_year * 2"]]}
        a = bc.analyze(spec)
        self.assertAlmostEqual(a["checks"]["deaths_x2"], 39600)
        self.assertAlmostEqual(a["result"], bc.result(TB))
        self.assertIn("Side checks", bc.to_markdown(a))


if __name__ == "__main__":
    unittest.main()
