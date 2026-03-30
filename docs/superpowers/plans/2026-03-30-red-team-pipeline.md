# Red Team Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build `pipeline/` — a Python CLI that orchestrates six AI agent stages via the Anthropic API, passes structured outputs between them, runs sensitivity analysis against CEA spreadsheets, and produces a ranked critique report for GiveWell's cost-effectiveness analyses.

**Architecture:** Linear six-stage pipeline (Decomposer → Investigators → Verifier → Quantifier → Adversarial Pair → Synthesizer). Each stage is a separate API call with its own system prompt, scoped inputs, and parsed structured output. The spreadsheet module replicates the critical formula chain (mortality → adjustments → cost-effectiveness) in Python for sensitivity analysis. All stages save intermediate JSON + markdown to `results/{intervention}/`.

**Tech Stack:** Python 3.12, anthropic SDK, openpyxl, pandas, python-dotenv. No frameworks.

---

## Planning Checklist Answers

**1. How will you parse structured output from each API call?**

Each prompt already uses labeled sections (e.g., `THREAD [N]:`, `CRITIQUE [N]:`, `HYPOTHESIS:`, `VERDICT:`). We parse with regex on these section headers. Each stage gets a dedicated `parse_*` function in `agents.py` that extracts sections into the corresponding dataclass. If the API returns unparseable output, we log the raw response, save it to disk, and raise a `ParseError` with the stage name — the `--resume-from` flag lets the user retry after inspecting.

**2. How will you handle the spreadsheet formula chain?**

Option A for the critical path, Option C for everything else. The critical path is:

```
Mortality effect size (meta-analysis pooling)
  → Internal validity adjustment (bundled interventions)
  → External validity adjustment (deaths linked to water quality × adherence)
  → Final mortality reduction = MIN(initial_estimate, plausibility_cap)
  → Deaths averted = pop_fraction × baseline_mortality × reduction × 100,000
  → Units of value = deaths_averted × moral_weight
  → Sum all benefit categories → divide by cost → units of value per dollar
```

This chain is fully replicable from the formulas I've extracted. The `AVERAGE.WEIGHTED` Google Sheets functions (used in meta-analysis pooling, baseline mortality, adult mortality scaling) are stored as `DUMMYFUNCTION` with hardcoded fallbacks — we'll read the cached values for those and replicate the weighted average in Python for sensitivity analysis when those specific parameters change.

Development effects and medical costs averted use the same adjustment chain, so they'll be replicated too (the formulas are straightforward). The DSW tab has additional leverage/funging adjustments pulled via `IMPORTRANGE` from an external sheet — those cached values will be read as constants.

**3. How will you handle the Verifier's web search results?**

The Anthropic API returns web search results as `tool_use` and `tool_result` content blocks interleaved with text. We pass `tools=[{"type": "web_search_20250305", "name": "web_search"}]` and process the response by iterating through content blocks, extracting text blocks for the verification report. The search results themselves are consumed by the model — we don't need to parse them; we parse the model's text output which includes its citations and verdicts.

**4. File naming convention for intermediate outputs?**

```
results/{intervention}/
  01-decomposer.json          # Machine-readable structured output
  01-decomposer.md            # Human-readable formatted output
  02-investigators.json
  02-investigators.md
  03-verifier.json
  03-verifier.md
  04-quantifier.json
  04-quantifier.md
  05-adversarial.json
  05-adversarial.md
  06-synthesizer.md            # Final report (markdown only — this IS the deliverable)
  pipeline.log                 # Timestamped log with token usage and costs
```

**5. How will `--resume-from` work?**

Each stage's JSON output is self-contained (contains everything the next stage needs). `--resume-from verifier` loads `03-verifier.json` and continues from stage 4. The CLI arg maps to a stage number; we load the JSON for all completed stages and start execution at the specified stage. Serialization uses `dataclasses.asdict()` → `json.dumps()` for writing and a `from_dict()` classmethod on each dataclass for reading.

**6. Parallel Investigator calls?**

Sequential. Six threads at ~30s each = ~3 minutes. Not worth async complexity for a pipeline that runs once per intervention.

---

## Plan Self-Critique

**Likely failure points:**
- **Unparseable API output.** The model may not follow the exact section format. Mitigation: parse loosely (regex for section headers, not exact formatting), and save raw output alongside parsed output so a human can fix and re-run.
- **Plausibility cap binding.** When `MIN(initial_estimate, cap)` selects the cap, changing upstream parameters has zero effect on the final estimate. The sensitivity analysis must detect this and report "parameter change has no effect because plausibility cap binds." Already handled in the plan — Task 3 explicitly checks for cap binding.
- **Web search rate limits on Verifier.** Many sequential searches could hit rate limits. Mitigation: exponential backoff with 2 retries, same as all other API calls.
- **Intervention report fetch failures.** The GiveWell website could be down or return unexpected HTML. Mitigation: the pipeline will use web fetch via requests or the Anthropic API's web search. If fetch fails, we error clearly with the URL.

**Assumptions about spreadsheet structure:**
- The formula chain is identical across programs (ILC Kenya, DSW Kenya/Uganda/Malawi) — confirmed by inspecting both tabs. DSW has additional leverage/funging adjustments not in ILC.
- Cached `DUMMYFUNCTION` values in the .xlsx are current and correct. This is a reasonable assumption since GiveWell published these spreadsheets.
- The `IMPORTRANGE` values (costs, funging) are baked into the .xlsx as cached values. We treat them as constants.

**Is the sensitivity calculation correct?**
Walk-through for ILC Kenya under-5 mortality:
1. `relative_risk = exp(pooled_ln_rr)` = exp(-0.1463) = 0.8639
2. `initial_estimate = (1 - 0.8639) * 0.7958 * 1.2139` = 0.1315
3. `plausibility_cap` = 0.109
4. `final_estimate = min(0.1315, 0.109)` = 0.109 (cap binds)
5. `deaths_averted_per_100k = 0.128 * 0.00831 * 0.109 * 100000` = 11.59
6. `units_of_value = 11.59 * 107.99` = 1252.0

This matches the spreadsheet values exactly. Sensitivity: if we increase `relative_risk` to 0.90 (weaker effect), `initial_estimate` = (1-0.90)*0.7958*1.2139 = 0.0966, which is below the cap, so `final_estimate` = 0.0966 and the cap no longer binds. This is the kind of nonlinearity the Quantifier must handle.

---

## File Structure

```
pipeline/
  __init__.py          # Empty
  config.py            # API keys, model IDs, paths, thresholds
  schemas.py           # Dataclasses for all inter-stage data
  spreadsheet.py       # CEA reading + sensitivity analysis engine
  agents.py            # One function per pipeline stage (API calls + parsing)
  run_pipeline.py      # CLI orchestrator with --resume-from
tests/
  __init__.py          # Empty
  test_spreadsheet.py  # Unit tests for CEA reading and sensitivity
  test_schemas.py      # Round-trip serialization tests
  test_parsing.py      # Tests for parsing agent output text into dataclasses
```

---

## Task 1: Project Scaffolding and Config

**Files:**
- Create: `pipeline/__init__.py`
- Create: `pipeline/config.py`
- Create: `requirements.txt`

- [ ] **Step 1: Create requirements.txt**

```
anthropic>=0.42.0
openpyxl>=3.1.0
pandas>=2.0.0
python-dotenv>=1.0.0
```

- [ ] **Step 2: Create pipeline/__init__.py**

Empty file.

- [ ] **Step 3: Create pipeline/config.py**

```python
"""Pipeline configuration. API keys loaded from .env via python-dotenv."""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# API
ANTHROPIC_API_KEY: str = os.environ["ANTHROPIC_API_KEY"]
OPUS_MODEL: str = "claude-opus-4-20250115"
SONNET_MODEL: str = "claude-sonnet-4-20250514"

# Paths
REPO_ROOT: Path = Path(__file__).parent.parent
PROMPTS_DIR: Path = REPO_ROOT / "prompts"
DATA_DIR: Path = REPO_ROOT / "data"
RESULTS_DIR: Path = REPO_ROOT / "results"

# Pipeline settings
MAX_RETRIES: int = 2
MAX_TOKENS_DECOMPOSER: int = 8192
MAX_TOKENS_INVESTIGATOR: int = 4096
MAX_TOKENS_VERIFIER: int = 4096
MAX_TOKENS_QUANTIFIER: int = 8192
MAX_TOKENS_ADVERSARIAL: int = 3072
MAX_TOKENS_SYNTHESIZER: int = 8192

# Cost thresholds (warn, don't stop)
COST_WARNING_PER_INTERVENTION: float = 15.0

# Materiality thresholds
MATERIALITY_THRESHOLD: float = 0.01   # 1% change = "notable"
HIGH_MATERIALITY_THRESHOLD: float = 0.10  # 10% change = "material"

# Pricing per million tokens (as of 2025)
PRICING: dict[str, dict[str, float]] = {
    OPUS_MODEL: {"input": 15.0, "output": 75.0},
    SONNET_MODEL: {"input": 3.0, "output": 15.0},
}

# Intervention source URLs
INTERVENTION_URLS: dict[str, dict[str, str]] = {
    "water-chlorination": {
        "report": "https://www.givewell.org/international/technical/programs/water-quality-interventions",
        "baseline": "https://docs.google.com/document/d/1l8baZ_9zQ3FDmmEI50L0T2KqzoEhow6lNXjgLKUhGUg/",
        "spreadsheet": "WaterCEA.xlsx",
    },
    "itns": {
        "report": "https://www.givewell.org/international/technical/programs/insecticide-treated-nets",
        "baseline": "https://docs.google.com/document/d/16iIzH_KneLjlRSAc-2ZLO4aWdNB48CZ0LWH7sRe8yFo/",
        "spreadsheet": "InsecticideCEA.xlsx",
    },
    "smc": {
        "report": "https://www.givewell.org/international/technical/programs/seasonal-malaria-chemoprevention",
        "baseline": "https://docs.google.com/document/d/1562HtXfGOQ3EYOWgDnCAV_s6uF2zbPmRAqZ817_lNpA/",
        "spreadsheet": "MalariaCEA.xlsx",
    },
}
```

- [ ] **Step 4: Verify config loads**

Run: `cd /home/tsondo/projects/givewell_redteam && python -c "from pipeline.config import *; print(f'Key loaded: {ANTHROPIC_API_KEY[:8]}...'); print(f'Prompts dir exists: {PROMPTS_DIR.exists()}')"`

Expected: Key prefix prints, prompts dir confirmed.

- [ ] **Step 5: Commit**

```bash
git add requirements.txt pipeline/__init__.py pipeline/config.py
git commit -m "feat: add pipeline config and project scaffolding"
```

---

## Task 2: Schemas (Dataclasses for Inter-Stage Data)

**Files:**
- Create: `pipeline/schemas.py`
- Create: `tests/__init__.py`
- Create: `tests/test_schemas.py`

- [ ] **Step 1: Write the round-trip serialization test**

```python
"""Tests for schema serialization round-trips."""

import json
from pipeline.schemas import (
    InvestigationThread,
    DecomposerOutput,
    CandidateCritique,
    VerifiedCritique,
    QuantifiedCritique,
    DebatedCritique,
)


def test_decomposer_output_round_trip():
    thread = InvestigationThread(
        name="External Validity",
        scope="Examine whether trial evidence generalizes.",
        key_questions=["Does the Kremer meta-analysis apply to Kenya?"],
        cea_parameters_affected=["relative_risk", "external_validity_adjustment"],
        relevant_sources=["Kremer et al. 2022"],
        out_of_scope="Implementation fidelity",
        context_md="# Investigation Thread: External Validity\n\n## Scope\nExamine...",
    )
    output = DecomposerOutput(
        threads=[thread],
        exclusion_list=["Chlorine taste aversion already addressed"],
        cea_parameter_map="Relative risk: 0.864, sourced from Mortality effect size tab",
    )
    serialized = json.dumps(output.to_dict())
    restored = DecomposerOutput.from_dict(json.loads(serialized))
    assert restored.threads[0].name == "External Validity"
    assert restored.exclusion_list == output.exclusion_list
    assert restored.cea_parameter_map == output.cea_parameter_map


def test_candidate_critique_round_trip():
    critique = CandidateCritique(
        thread_name="External Validity",
        title="Trial populations differ from program populations",
        hypothesis="The Kremer trials were conducted in different settings.",
        mechanism="Baseline mortality rates differ, changing absolute effect.",
        parameters_affected=["external_validity_adjustment"],
        suggested_evidence=["Compare trial vs program demographics"],
        estimated_direction="decreases",
        estimated_magnitude="medium",
    )
    serialized = json.dumps(critique.to_dict())
    restored = CandidateCritique.from_dict(json.loads(serialized))
    assert restored.title == critique.title
    assert restored.parameters_affected == ["external_validity_adjustment"]


def test_verified_critique_round_trip():
    original = CandidateCritique(
        thread_name="T1",
        title="Test",
        hypothesis="H",
        mechanism="M",
        parameters_affected=["p1"],
        suggested_evidence=["s1"],
        estimated_direction="decreases",
        estimated_magnitude="medium",
    )
    verified = VerifiedCritique(
        original=original,
        verdict="verified",
        evidence_found=["Smith et al. 2023 confirms..."],
        evidence_strength="moderate",
        counter_evidence=[],
        caveats=["Small sample"],
        revised_hypothesis=None,
    )
    serialized = json.dumps(verified.to_dict())
    restored = VerifiedCritique.from_dict(json.loads(serialized))
    assert restored.verdict == "verified"
    assert restored.original.title == "Test"


def test_quantified_critique_round_trip():
    original = CandidateCritique(
        thread_name="T1", title="Test", hypothesis="H", mechanism="M",
        parameters_affected=["p1"], suggested_evidence=["s1"],
        estimated_direction="decreases", estimated_magnitude="medium",
    )
    verified = VerifiedCritique(
        original=original, verdict="verified",
        evidence_found=["evidence"], evidence_strength="moderate",
        counter_evidence=[], caveats=[], revised_hypothesis=None,
    )
    quantified = QuantifiedCritique(
        critique=verified,
        target_parameters=[{"name": "relative_risk", "cell_ref": "B5", "current_value": 0.864}],
        alternative_range=[{"name": "relative_risk", "low": 0.85, "central": 0.90, "high": 0.95, "justification": "Based on..."}],
        sensitivity_results={"baseline": 7.60, "central_alt": 6.50, "best_case": 7.20, "worst_case": 5.80},
        materiality="material",
        interaction_effects=[],
    )
    serialized = json.dumps(quantified.to_dict())
    restored = QuantifiedCritique.from_dict(json.loads(serialized))
    assert restored.materiality == "material"
    assert restored.sensitivity_results["baseline"] == 7.60


def test_debated_critique_round_trip():
    original = CandidateCritique(
        thread_name="T1", title="Test", hypothesis="H", mechanism="M",
        parameters_affected=["p1"], suggested_evidence=["s1"],
        estimated_direction="decreases", estimated_magnitude="medium",
    )
    verified = VerifiedCritique(
        original=original, verdict="verified",
        evidence_found=["evidence"], evidence_strength="moderate",
        counter_evidence=[], caveats=[], revised_hypothesis=None,
    )
    quantified = QuantifiedCritique(
        critique=verified,
        target_parameters=[{"name": "rr", "cell_ref": "B5", "current_value": 0.864}],
        alternative_range=[{"name": "rr", "low": 0.85, "central": 0.90, "high": 0.95, "justification": "..."}],
        sensitivity_results={"baseline": 7.60, "central_alt": 6.50, "best_case": 7.20, "worst_case": 5.80},
        materiality="material",
        interaction_effects=[],
    )
    debated = DebatedCritique(
        critique=quantified,
        advocate_defense="GiveWell already applies a 25% adjustment...",
        challenger_rebuttal="The adjustment doesn't capture this specific...",
        surviving_strength="moderate",
        key_unresolved=["Whether the adjustment is sufficient"],
        recommended_action="investigate",
    )
    serialized = json.dumps(debated.to_dict())
    restored = DebatedCritique.from_dict(json.loads(serialized))
    assert restored.surviving_strength == "moderate"
    assert restored.critique.materiality == "material"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /home/tsondo/projects/givewell_redteam && python -m pytest tests/test_schemas.py -v`

Expected: FAIL — `ModuleNotFoundError: No module named 'pipeline.schemas'`

- [ ] **Step 3: Implement schemas.py**

```python
"""Dataclasses for structured data passed between pipeline stages."""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any


@dataclass
class InvestigationThread:
    name: str
    scope: str
    key_questions: list[str]
    cea_parameters_affected: list[str]
    relevant_sources: list[str]
    out_of_scope: str
    context_md: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> InvestigationThread:
        return cls(**d)


@dataclass
class DecomposerOutput:
    threads: list[InvestigationThread]
    exclusion_list: list[str]
    cea_parameter_map: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "threads": [t.to_dict() for t in self.threads],
            "exclusion_list": self.exclusion_list,
            "cea_parameter_map": self.cea_parameter_map,
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> DecomposerOutput:
        return cls(
            threads=[InvestigationThread.from_dict(t) for t in d["threads"]],
            exclusion_list=d["exclusion_list"],
            cea_parameter_map=d["cea_parameter_map"],
        )


@dataclass
class CandidateCritique:
    thread_name: str
    title: str
    hypothesis: str
    mechanism: str
    parameters_affected: list[str]
    suggested_evidence: list[str]
    estimated_direction: str  # "increases" | "decreases" | "uncertain"
    estimated_magnitude: str  # "large" | "medium" | "small" | "unknown"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> CandidateCritique:
        return cls(**d)


@dataclass
class VerifiedCritique:
    original: CandidateCritique
    verdict: str  # "verified" | "partially_verified" | "unverified"
    evidence_found: list[str]
    evidence_strength: str  # "strong" | "moderate" | "weak"
    counter_evidence: list[str]
    caveats: list[str]
    revised_hypothesis: str | None

    def to_dict(self) -> dict[str, Any]:
        return {
            "original": self.original.to_dict(),
            "verdict": self.verdict,
            "evidence_found": self.evidence_found,
            "evidence_strength": self.evidence_strength,
            "counter_evidence": self.counter_evidence,
            "caveats": self.caveats,
            "revised_hypothesis": self.revised_hypothesis,
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> VerifiedCritique:
        return cls(
            original=CandidateCritique.from_dict(d["original"]),
            verdict=d["verdict"],
            evidence_found=d["evidence_found"],
            evidence_strength=d["evidence_strength"],
            counter_evidence=d["counter_evidence"],
            caveats=d["caveats"],
            revised_hypothesis=d.get("revised_hypothesis"),
        )


@dataclass
class QuantifiedCritique:
    critique: VerifiedCritique
    target_parameters: list[dict[str, Any]]
    alternative_range: list[dict[str, Any]]
    sensitivity_results: dict[str, Any]
    materiality: str  # "material" | "notable" | "immaterial"
    interaction_effects: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "critique": self.critique.to_dict(),
            "target_parameters": self.target_parameters,
            "alternative_range": self.alternative_range,
            "sensitivity_results": self.sensitivity_results,
            "materiality": self.materiality,
            "interaction_effects": self.interaction_effects,
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> QuantifiedCritique:
        return cls(
            critique=VerifiedCritique.from_dict(d["critique"]),
            target_parameters=d["target_parameters"],
            alternative_range=d["alternative_range"],
            sensitivity_results=d["sensitivity_results"],
            materiality=d["materiality"],
            interaction_effects=d["interaction_effects"],
        )


@dataclass
class DebatedCritique:
    critique: QuantifiedCritique
    advocate_defense: str
    challenger_rebuttal: str
    surviving_strength: str  # "strong" | "moderate" | "weak"
    key_unresolved: list[str]
    recommended_action: str  # "investigate" | "adjust_model" | "monitor" | "dismiss"

    def to_dict(self) -> dict[str, Any]:
        return {
            "critique": self.critique.to_dict(),
            "advocate_defense": self.advocate_defense,
            "challenger_rebuttal": self.challenger_rebuttal,
            "surviving_strength": self.surviving_strength,
            "key_unresolved": self.key_unresolved,
            "recommended_action": self.recommended_action,
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> DebatedCritique:
        return cls(
            critique=QuantifiedCritique.from_dict(d["critique"]),
            advocate_defense=d["advocate_defense"],
            challenger_rebuttal=d["challenger_rebuttal"],
            surviving_strength=d["surviving_strength"],
            key_unresolved=d["key_unresolved"],
            recommended_action=d["recommended_action"],
        )


@dataclass
class PipelineStats:
    """Tracks token usage and costs across the pipeline run."""
    total_input_tokens: int = 0
    total_output_tokens: int = 0
    total_cost: float = 0.0
    stage_costs: dict[str, float] = field(default_factory=dict)

    def record_call(self, stage: str, model: str, input_tokens: int, output_tokens: int, pricing: dict[str, dict[str, float]]) -> float:
        """Record an API call and return its cost."""
        rates = pricing.get(model, {"input": 15.0, "output": 75.0})
        cost = (input_tokens * rates["input"] + output_tokens * rates["output"]) / 1_000_000
        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens
        self.total_cost += cost
        self.stage_costs[stage] = self.stage_costs.get(stage, 0.0) + cost
        return cost

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> PipelineStats:
        return cls(**d)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd /home/tsondo/projects/givewell_redteam && python -m pytest tests/test_schemas.py -v`

Expected: All 5 tests PASS.

- [ ] **Step 5: Commit**

```bash
git add pipeline/schemas.py tests/__init__.py tests/test_schemas.py
git commit -m "feat: add dataclass schemas for all pipeline stages"
```

---

## Task 3: Spreadsheet Module — CEA Reader

**Files:**
- Create: `pipeline/spreadsheet.py`
- Create: `tests/test_spreadsheet.py`

This is the riskiest component. We build it in two sub-tasks: reading (this task) and sensitivity analysis (Task 4).

- [ ] **Step 1: Write the CEA reading tests**

```python
"""Tests for spreadsheet reading and sensitivity analysis."""

import math
from pathlib import Path
from pipeline.spreadsheet import WaterCEA

CEA_PATH = Path(__file__).parent.parent / "data" / "WaterCEA.xlsx"


class TestWaterCEAReading:
    """Test that we correctly read all key parameters from WaterCEA.xlsx."""

    def setup_method(self):
        self.cea = WaterCEA(CEA_PATH)

    def test_pooled_relative_risk(self):
        """Mortality effect size tab: pooled ln(RR) → RR."""
        assert math.isclose(self.cea.relative_risk, 0.8638932195, rel_tol=1e-6)

    def test_internal_validity_under5(self):
        """Internal validity adjustment for under-5 mortality."""
        assert math.isclose(self.cea.internal_validity_under5, 0.7957578162, rel_tol=1e-6)

    def test_internal_validity_over5(self):
        """Internal validity adjustment for over-5 mortality."""
        assert math.isclose(self.cea.internal_validity_over5, 0.504149833, rel_tol=1e-6)

    def test_external_validity_ilc_kenya(self):
        """External validity adjustment for ILC Kenya."""
        assert math.isclose(self.cea.programs["ilc_kenya"]["external_validity"], 1.213858014, rel_tol=1e-6)

    def test_external_validity_dsw_kenya(self):
        """External validity adjustment for DSW Kenya."""
        assert math.isclose(self.cea.programs["dsw_kenya"]["external_validity"], 0.5582511733, rel_tol=1e-6)

    def test_plausibility_cap_ilc_kenya(self):
        """Plausibility cap for ILC Kenya."""
        assert math.isclose(self.cea.programs["ilc_kenya"]["plausibility_cap"], 0.109, rel_tol=1e-6)

    def test_plausibility_cap_dsw_kenya(self):
        """Plausibility cap for DSW Kenya."""
        assert math.isclose(self.cea.programs["dsw_kenya"]["plausibility_cap"], 0.056, rel_tol=1e-6)

    def test_baseline_cost_effectiveness_ilc_kenya(self):
        """End-to-end: ILC Kenya cost-effectiveness in multiples of cash."""
        result = self.cea.compute_cost_effectiveness("ilc_kenya")
        assert math.isclose(result, 7.60245168, rel_tol=1e-3)

    def test_baseline_cost_effectiveness_dsw_kenya(self):
        """End-to-end: DSW Kenya cost-effectiveness (long-term)."""
        result = self.cea.compute_cost_effectiveness("dsw_kenya")
        assert math.isclose(result, 4.421618553, rel_tol=1e-3)

    def test_baseline_cost_effectiveness_dsw_uganda(self):
        """End-to-end: DSW Uganda cost-effectiveness (long-term)."""
        result = self.cea.compute_cost_effectiveness("dsw_uganda")
        assert math.isclose(result, 7.015706986, rel_tol=1e-3)

    def test_baseline_cost_effectiveness_dsw_malawi(self):
        """End-to-end: DSW Malawi cost-effectiveness (long-term)."""
        result = self.cea.compute_cost_effectiveness("dsw_malawi")
        assert math.isclose(result, 8.657297146, rel_tol=1e-3)

    def test_cap_binds_ilc_kenya(self):
        """ILC Kenya: plausibility cap should bind (initial > cap)."""
        program = self.cea.programs["ilc_kenya"]
        initial = (1 - self.cea.relative_risk) * self.cea.internal_validity_under5 * program["external_validity"]
        assert initial > program["plausibility_cap"]

    def test_parameter_summary(self):
        """get_parameter_summary returns a non-empty string."""
        summary = self.cea.get_parameter_summary()
        assert "relative_risk" in summary or "Relative risk" in summary
        assert len(summary) > 200

    def test_list_programs(self):
        """All four programs are loaded."""
        assert set(self.cea.programs.keys()) == {"ilc_kenya", "dsw_kenya", "dsw_uganda", "dsw_malawi"}
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /home/tsondo/projects/givewell_redteam && python -m pytest tests/test_spreadsheet.py::TestWaterCEAReading -v`

Expected: FAIL — `ImportError`

- [ ] **Step 3: Implement WaterCEA class — reading**

```python
"""CEA spreadsheet reading and sensitivity analysis for water chlorination."""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import openpyxl


def _val(ws: Any, cell: str) -> float:
    """Read a numeric cell value, raising if None."""
    v = ws[cell].value
    if v is None:
        raise ValueError(f"Cell {cell} in sheet '{ws.title}' is empty")
    return float(v)


@dataclass
class ProgramParams:
    """Parameters for one program-country combination."""
    name: str
    pop_under5_frac: float
    baseline_mortality_under5: float
    external_validity: float
    plausibility_cap: float
    # Over-5
    pop_over5_frac: float
    baseline_mortality_over5: float
    adult_mortality_scaling: float
    # Morbidity
    ylds_per_100k: float
    morbidity_ext_validity: float
    # Development effects
    dev_effects_base_uv_per_100k: float  # pre-adjustment
    # Medical costs
    baseline_diarrhea_incidence: float
    medical_cost_per_under5: float
    medical_cost_iv_adj: float  # Internal validity (Mills-Reincke multiplier)
    medical_cost_ev_adj: float  # External validity
    # Moral weights
    moral_weight_under5: float
    moral_weight_over5: float
    moral_weight_yld: float
    # Cost
    cost_per_person: float
    givewell_cash_benchmark: float


class WaterCEA:
    """Reads and computes the water chlorination CEA from an xlsx file.

    Replicates the critical formula chain:
      mortality effect → internal validity → external validity → plausibility cap
      → deaths averted → units of value → cost-effectiveness
    """

    def __init__(self, path: Path) -> None:
        self.path = path
        wb_data = openpyxl.load_workbook(path, data_only=True)

        # --- Mortality effect size ---
        ms = wb_data["Mortality effect size"]
        self.pooled_ln_rr: float = _val(ms, "B10")
        self.relative_risk: float = math.exp(self.pooled_ln_rr)

        # Trial data for meta-analysis replication
        self.trials: list[dict[str, Any]] = []
        for row_num in range(4, 9):  # Rows 4-8: 5 trials
            trial_name = ms.cell(row=row_num, column=1).value
            if trial_name is None:
                continue
            self.trials.append({
                "name": trial_name,
                "control_n": _val(ms, f"E{row_num}"),
                "control_deaths": _val(ms, f"F{row_num}"),
                "treatment_n": _val(ms, f"H{row_num}"),
                "treatment_deaths": float(ms.cell(row=row_num, column=9).value or 0),
            })

        # --- Internal validity ---
        iv = wb_data["Internal validity adjustment"]
        self.internal_validity_under5: float = _val(iv, "B6")
        self.internal_validity_over5: float = _val(iv, "B7")
        self.internal_validity_morbidity: float = _val(iv, "E3")
        self.mills_reincke_multiplier: float = _val(iv, "B23")

        # Plausibility caps per program
        self._plausibility_caps = {
            "ilc_kenya": _val(iv, "B11"),
            "dsw_kenya": _val(iv, "B12"),
            "dsw_uganda": _val(iv, "B13"),
            "dsw_malawi": _val(iv, "B14"),
        }

        # --- Morbidity effect size ---
        morb = wb_data["Morbidity effect size"]
        self.diarrhea_rr: float = _val(morb, "B3")
        self.morbidity_self_report_adj: float = _val(morb, "B6")
        self.adjusted_diarrhea_rr: float = _val(morb, "B7")

        # --- External validity ---
        ev = wb_data["External validity adjustment"]
        self._ext_validity = {
            "ilc_kenya": _val(ev, "B6"),
            "dsw_kenya": _val(ev, "B11"),
            "dsw_uganda": _val(ev, "B16"),
            "dsw_malawi": _val(ev, "B21"),
        }
        self._morb_ext_validity = {
            "ilc_kenya": _val(ev, "B29"),
            "dsw_kenya": _val(ev, "B33"),
            "dsw_uganda": _val(ev, "B37"),
            "dsw_malawi": _val(ev, "B41"),
        }

        # --- Moral weights ---
        mw = wb_data["Moral weights"]
        moral_weights_under5 = {
            "ilc_kenya": _val(mw, "B3"),
            "dsw_kenya": _val(mw, "B3"),
            "dsw_uganda": _val(mw, "B4"),
            "dsw_malawi": _val(mw, "B5"),
        }
        moral_weights_over5 = {
            "ilc_kenya": _val(mw, "B7"),
            "dsw_kenya": _val(mw, "B7"),
            "dsw_uganda": _val(mw, "B8"),
            "dsw_malawi": _val(mw, "B9"),
        }
        moral_weight_yld = _val(mw, "B11")

        # --- Adult mortality scaling ---
        ams = wb_data["Adult mortality scaling factor"]
        adult_scaling = {
            "ilc_kenya": _val(ams, "B17"),
            "dsw_kenya": _val(ams, "B17"),
            "dsw_uganda": _val(ams, "C17"),
            "dsw_malawi": _val(ams, "D17"),
        }

        # --- Program-specific parameters ---
        # ILC Kenya
        ilc = wb_data["ILC Kenya"]
        dsw = wb_data["DSW"]

        # Development effects constants (same for all programs)
        dev_base_per_treatment_year = _val(ilc, "B39")  # 0.126
        dev_chlorination_pct_of_smc = _val(ilc, "B40")  # 0.44

        self.programs: dict[str, ProgramParams] = {}

        # ILC Kenya
        self.programs["ilc_kenya"] = ProgramParams(
            name="ILC Kenya",
            pop_under5_frac=_val(ilc, "B3"),
            baseline_mortality_under5=_val(ilc, "B4"),
            external_validity=self._ext_validity["ilc_kenya"],
            plausibility_cap=self._plausibility_caps["ilc_kenya"],
            pop_over5_frac=_val(ilc, "B16"),
            baseline_mortality_over5=_val(ilc, "B17"),
            adult_mortality_scaling=adult_scaling["ilc_kenya"],
            ylds_per_100k=_val(ilc, "B29"),
            morbidity_ext_validity=self._morb_ext_validity["ilc_kenya"],
            dev_effects_base_uv_per_100k=_val(ilc, "B46"),
            baseline_diarrhea_incidence=_val(ilc, "B52"),
            medical_cost_per_under5=_val(ilc, "B55"),
            medical_cost_iv_adj=1.0,  # ILC uses 1.0 for medical cost IV
            medical_cost_ev_adj=_val(ilc, "B61"),
            moral_weight_under5=moral_weights_under5["ilc_kenya"],
            moral_weight_over5=moral_weights_over5["ilc_kenya"],
            moral_weight_yld=moral_weight_yld,
            cost_per_person=_val(ilc, "B72"),
            givewell_cash_benchmark=_val(ilc, "B77"),
        )

        # DSW programs (Kenya, Uganda, Malawi in columns B, C, D)
        col_map = {"dsw_kenya": "B", "dsw_uganda": "C", "dsw_malawi": "D"}
        country_names = {"dsw_kenya": "DSW Kenya", "dsw_uganda": "DSW Uganda", "dsw_malawi": "DSW Malawi"}

        for prog_key, col in col_map.items():
            self.programs[prog_key] = ProgramParams(
                name=country_names[prog_key],
                pop_under5_frac=_val(dsw, f"{col}3"),
                baseline_mortality_under5=_val(dsw, f"{col}4"),
                external_validity=self._ext_validity[prog_key],
                plausibility_cap=self._plausibility_caps[prog_key],
                pop_over5_frac=float(1 - _val(dsw, f"{col}3")),
                baseline_mortality_over5=_val(dsw, f"{col}17"),
                adult_mortality_scaling=adult_scaling[prog_key],
                ylds_per_100k=_val(dsw, f"{col}29"),
                morbidity_ext_validity=self._morb_ext_validity[prog_key],
                dev_effects_base_uv_per_100k=_val(dsw, f"{col}46"),
                baseline_diarrhea_incidence=_val(dsw, f"{col}52"),
                medical_cost_per_under5=_val(dsw, f"{col}55"),
                medical_cost_iv_adj=1.0,
                medical_cost_ev_adj=_val(dsw, f"{col}61"),
                moral_weight_under5=moral_weights_under5[prog_key],
                moral_weight_over5=moral_weights_over5[prog_key],
                moral_weight_yld=moral_weight_yld,
                cost_per_person=_val(dsw, f"{col}74"),
                givewell_cash_benchmark=_val(dsw, f"{col}79"),
            )

        # Store dev effects constants
        self._dev_base = dev_base_per_treatment_year
        self._dev_chlorination_pct = dev_chlorination_pct_of_smc

        wb_data.close()

    def compute_cost_effectiveness(
        self,
        program_key: str,
        *,
        relative_risk: float | None = None,
        internal_validity_under5: float | None = None,
        internal_validity_over5: float | None = None,
        external_validity: float | None = None,
        plausibility_cap: float | None = None,
        internal_validity_morbidity: float | None = None,
        morbidity_ext_validity: float | None = None,
    ) -> float:
        """Compute cost-effectiveness for a program, optionally overriding parameters.

        Returns: cost-effectiveness in multiples of GiveDirectly cash.
        """
        p = self.programs[program_key]
        rr = relative_risk if relative_risk is not None else self.relative_risk
        iv_u5 = internal_validity_under5 if internal_validity_under5 is not None else self.internal_validity_under5
        iv_o5 = internal_validity_over5 if internal_validity_over5 is not None else self.internal_validity_over5
        ev = external_validity if external_validity is not None else p.external_validity
        cap = plausibility_cap if plausibility_cap is not None else p.plausibility_cap
        iv_morb = internal_validity_morbidity if internal_validity_morbidity is not None else self.internal_validity_morbidity
        morb_ev = morbidity_ext_validity if morbidity_ext_validity is not None else p.morbidity_ext_validity

        # --- Under-5 mortality ---
        initial_estimate = (1 - rr) * iv_u5 * ev
        final_estimate = min(initial_estimate, cap)
        u5_deaths_per_100k = p.pop_under5_frac * p.baseline_mortality_under5 * final_estimate * 100_000
        u5_uv = u5_deaths_per_100k * p.moral_weight_under5

        # --- Over-5 mortality ---
        cap_ratio = final_estimate / initial_estimate if initial_estimate > 0 else 1.0
        o5_deaths_per_100k = (
            p.pop_over5_frac
            * p.baseline_mortality_over5
            * (1 - rr)
            * p.adult_mortality_scaling
            * iv_o5
            * ev
            * cap_ratio
            * 100_000
        )
        o5_uv = o5_deaths_per_100k * p.moral_weight_over5

        # --- Morbidity ---
        morbidity_reduction = (1 - self.adjusted_diarrhea_rr) * iv_morb * morb_ev
        morbidity_ylds_averted_per_100k = p.ylds_per_100k * morbidity_reduction
        morb_uv = morbidity_ylds_averted_per_100k * p.moral_weight_yld

        # --- Development effects ---
        dev_uv = p.dev_effects_base_uv_per_100k * iv_u5 * ev

        # --- Medical costs averted ---
        diarrhea_cases_averted = p.baseline_diarrhea_incidence * morbidity_reduction
        cost_per_under5 = p.medical_cost_per_under5
        cost_per_person = cost_per_under5 * p.pop_under5_frac
        mills_reincke = self.mills_reincke_multiplier
        total_cost_averted = cost_per_person * mills_reincke * p.medical_cost_iv_adj * p.medical_cost_ev_adj
        avg_consumption = p.cost_per_person  # Approximation — read from cell
        # For ILC Kenya, consumption is 99.82*12 = 1197.84
        # We need to read this properly — let me use the formula from the spreadsheet
        # ln(consumption + cost_averted) - ln(consumption)
        # For now, use the per-100k approach matching the spreadsheet
        med_uv = self._compute_medical_costs_uv(p, morbidity_reduction)

        # --- Total ---
        total_uv_per_100k = u5_uv + o5_uv + morb_uv + dev_uv + med_uv
        uv_per_dollar = (total_uv_per_100k / 100_000) / p.cost_per_person
        return uv_per_dollar * 10_000 / p.givewell_cash_benchmark

    def _compute_medical_costs_uv(self, p: ProgramParams, morbidity_reduction: float) -> float:
        """Compute units of value from medical costs averted per 100,000 people."""
        diarrhea_averted_per_u5 = p.baseline_diarrhea_incidence * morbidity_reduction
        cost_averted_per_u5 = p.medical_cost_per_under5
        cost_per_person = cost_averted_per_u5 * p.pop_under5_frac
        total_cost_averted = cost_per_person * self.mills_reincke_multiplier
        adjusted = total_cost_averted * p.medical_cost_iv_adj * p.medical_cost_ev_adj

        # ln(consumption) approach — approximate consumption from cost_per_person data
        # The spreadsheet uses country-specific consumption. We'll read from the program tab.
        # For simplicity, we read the cached unit value from the spreadsheet
        # and scale it proportionally with morbidity_reduction changes.
        # This is the one place where we use the cached values approach (Option C-ish).
        # The medical costs formula chain involves ln(consumption + X) - ln(consumption),
        # which we CAN replicate, but the consumption values come from external data.
        # Let's replicate it properly.

        # We store consumption per program in __init__. Let me add that.
        # For now, return the cached value scaled by morbidity_reduction ratio.
        return self._medical_costs_cache.get(p.name, 0.0)

    def get_parameter_summary(self) -> str:
        """Generate a human-readable summary of CEA parameters for the Decomposer."""
        lines = [
            "# Water Chlorination CEA Parameter Summary",
            "",
            "## Mortality Effect Size",
            f"- Pooled ln(relative risk): {self.pooled_ln_rr:.6f}",
            f"- Relative risk of all-cause mortality: {self.relative_risk:.6f}",
            f"- Based on {len(self.trials)} trials: {', '.join(t['name'] for t in self.trials)}",
            "",
            "## Internal Validity Adjustments",
            f"- Under-5 mortality (bundled interventions): {self.internal_validity_under5:.6f}",
            f"- Over-5 mortality: {self.internal_validity_over5:.6f}",
            f"- Morbidity: {self.internal_validity_morbidity}",
            f"- Mills-Reincke multiplier: {self.mills_reincke_multiplier:.6f}",
            "",
            "## Programs",
        ]
        for key, p in self.programs.items():
            result = self.compute_cost_effectiveness(key)
            lines.extend([
                f"",
                f"### {p.name}",
                f"- External validity adjustment: {p.external_validity:.6f}",
                f"- Plausibility cap: {p.plausibility_cap}",
                f"- Cost per person: ${p.cost_per_person:.4f}",
                f"- **Cost-effectiveness (multiples of cash): {result:.2f}**",
            ])
        return "\n".join(lines)
```

**Note:** The medical costs computation needs the consumption-per-capita values. I'll fix this in the actual implementation by reading those cells during `__init__`. The key insight is that the medical costs path uses `ln(consumption + averted) - ln(consumption)`, which requires country-specific consumption data. We'll read those cached values from the ILC/DSW tabs.

This skeleton will need refinement during implementation — the test will tell us where the numbers don't match. The important thing is the tests verify against the known spreadsheet values.

- [ ] **Step 4: Run tests, iterate until baseline cost-effectiveness matches**

Run: `cd /home/tsondo/projects/givewell_redteam && python -m pytest tests/test_spreadsheet.py::TestWaterCEAReading -v`

Iterate on the implementation until all 12 tests pass. The hardest ones will be the end-to-end cost-effectiveness tests — those require the full formula chain to be correct.

- [ ] **Step 5: Commit**

```bash
git add pipeline/spreadsheet.py tests/test_spreadsheet.py
git commit -m "feat: add CEA spreadsheet reader with formula chain replication"
```

---

## Task 4: Spreadsheet Module — Sensitivity Analysis

**Files:**
- Modify: `pipeline/spreadsheet.py`
- Modify: `tests/test_spreadsheet.py`

- [ ] **Step 1: Write sensitivity analysis tests**

Add to `tests/test_spreadsheet.py`:

```python
class TestSensitivityAnalysis:
    """Test sensitivity analysis computations."""

    def setup_method(self):
        self.cea = WaterCEA(CEA_PATH)

    def test_weaker_relative_risk_ilc_kenya(self):
        """Weakening relative risk from 0.864 to 0.90 should lower CE."""
        baseline = self.cea.compute_cost_effectiveness("ilc_kenya")
        weaker = self.cea.compute_cost_effectiveness("ilc_kenya", relative_risk=0.90)
        assert weaker < baseline
        # With RR=0.90, initial_estimate = (1-0.90)*0.796*1.214 = 0.0966
        # This is below cap of 0.109, so cap no longer binds
        # CE should drop substantially
        assert weaker < baseline * 0.85  # At least 15% drop

    def test_cap_binding_detection(self):
        """detect_cap_binding returns True when cap binds."""
        assert self.cea.detect_cap_binding("ilc_kenya") is True

    def test_cap_not_binding_with_weaker_rr(self):
        """With weaker RR, cap should not bind for ILC Kenya."""
        assert self.cea.detect_cap_binding("ilc_kenya", relative_risk=0.90) is False

    def test_run_sensitivity(self):
        """run_sensitivity returns a dict with expected keys."""
        result = self.cea.run_sensitivity(
            program_key="ilc_kenya",
            parameter_name="relative_risk",
            low=0.85,
            central=0.90,
            high=0.95,
        )
        assert "baseline" in result
        assert "low" in result
        assert "central" in result
        assert "high" in result
        assert "pct_change_central" in result
        assert "cap_binds_baseline" in result
        assert "cap_binds_at_value" in result
        assert result["baseline"] > result["central"]  # weaker effect → lower CE

    def test_sensitivity_stronger_rr_increases_ce(self):
        """Strengthening relative risk should increase CE (up to cap)."""
        result = self.cea.run_sensitivity(
            program_key="ilc_kenya",
            parameter_name="relative_risk",
            low=0.80,
            central=0.82,
            high=0.85,
        )
        # Cap still binds at these values for ILC Kenya, so CE shouldn't change
        assert math.isclose(result["baseline"], result["central"], rel_tol=1e-3)

    def test_internal_validity_sensitivity(self):
        """Changing internal validity should affect CE."""
        result = self.cea.run_sensitivity(
            program_key="dsw_kenya",
            parameter_name="internal_validity_under5",
            low=0.5,
            central=0.6,
            high=0.7,
        )
        # DSW Kenya: check that cap doesn't bind at baseline
        # initial = (1-0.864)*0.796*0.558 = 0.0605, cap = 0.056
        # Cap binds at baseline! So changing IV won't help for under-5 mortality
        # But it affects development effects and over-5 mortality
        assert result["low"] < result["baseline"]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /home/tsondo/projects/givewell_redteam && python -m pytest tests/test_spreadsheet.py::TestSensitivityAnalysis -v`

Expected: FAIL — `detect_cap_binding` and `run_sensitivity` not defined.

- [ ] **Step 3: Implement sensitivity methods**

Add to `WaterCEA` class:

```python
def detect_cap_binding(
    self, program_key: str, *, relative_risk: float | None = None,
    internal_validity_under5: float | None = None,
    external_validity: float | None = None,
) -> bool:
    """Check whether the plausibility cap binds for under-5 mortality."""
    p = self.programs[program_key]
    rr = relative_risk or self.relative_risk
    iv = internal_validity_under5 or self.internal_validity_under5
    ev = external_validity or p.external_validity
    initial = (1 - rr) * iv * ev
    return initial > p.plausibility_cap

def run_sensitivity(
    self,
    program_key: str,
    parameter_name: str,
    low: float,
    central: float,
    high: float,
) -> dict[str, Any]:
    """Run sensitivity analysis on a single parameter.

    Returns dict with baseline, low, central, high CE values,
    percentage changes, and cap binding info.
    """
    baseline = self.compute_cost_effectiveness(program_key)

    results = {}
    for label, value in [("low", low), ("central", central), ("high", high)]:
        ce = self.compute_cost_effectiveness(program_key, **{parameter_name: value})
        results[label] = ce

    return {
        "baseline": baseline,
        **results,
        "pct_change_low": (results["low"] - baseline) / baseline,
        "pct_change_central": (results["central"] - baseline) / baseline,
        "pct_change_high": (results["high"] - baseline) / baseline,
        "cap_binds_baseline": self.detect_cap_binding(program_key),
        "cap_binds_at_value": {
            "low": self.detect_cap_binding(program_key, **{parameter_name: low}) if parameter_name in ("relative_risk", "internal_validity_under5", "external_validity") else None,
            "central": self.detect_cap_binding(program_key, **{parameter_name: central}) if parameter_name in ("relative_risk", "internal_validity_under5", "external_validity") else None,
            "high": self.detect_cap_binding(program_key, **{parameter_name: high}) if parameter_name in ("relative_risk", "internal_validity_under5", "external_validity") else None,
        },
    }
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd /home/tsondo/projects/givewell_redteam && python -m pytest tests/test_spreadsheet.py -v`

Expected: All tests pass.

- [ ] **Step 5: Commit**

```bash
git add pipeline/spreadsheet.py tests/test_spreadsheet.py
git commit -m "feat: add sensitivity analysis to CEA spreadsheet module"
```

---

## Task 5: Agent Callers — API Utility and Decomposer

**Files:**
- Create: `pipeline/agents.py`
- Create: `tests/test_parsing.py`

- [ ] **Step 1: Write parsing tests for Decomposer output**

```python
"""Tests for parsing agent output text into dataclasses."""

from pipeline.agents import parse_decomposer_output


SAMPLE_DECOMPOSER_OUTPUT = """
THREAD 1: External Validity of Trial Evidence

SCOPE: Examine whether the mortality trials in the Kremer et al. meta-analysis generalize to current DSW and ILC program settings in Kenya, Uganda, and Malawi.

KEY PARAMETERS: relative_risk, external_validity_adjustment

WHAT GIVEWELL ALREADY ACCOUNTS FOR: GiveWell applies an external validity adjustment that accounts for differences in water-quality-linked deaths and adherence between trial settings and program settings.

WHAT GIVEWELL DOES NOT ACCOUNT FOR: Whether the adjustment fully captures differences in water source types, urbanization rates, and baseline health infrastructure between trial and program contexts.

DATA SOURCES TO EXAMINE: Kremer et al. 2022, Reller 2003, Null 2018, Luby 2018

MATERIALITY THRESHOLD: A change of >15% in the external validity adjustment would shift cost per DALY by >10%.

KNOWN CONCERNS ALREADY SURFACED: General external validity concerns are acknowledged in GiveWell's report.

THREAD 2: Plausibility Cap Methodology

SCOPE: Examine whether the plausibility cap is appropriately set and whether it masks important parameter sensitivity.

KEY PARAMETERS: plausibility_cap, internal_validity_adjustment

WHAT GIVEWELL ALREADY ACCOUNTS FOR: The cap is explicitly designed to prevent implausibly large mortality estimates.

WHAT GIVEWELL DOES NOT ACCOUNT FOR: Whether the cap is too conservative or too generous, and whether it creates a false sense of precision.

DATA SOURCES TO EXAMINE: Internal validity adjustment methodology, comparison with other GiveWell CEAs

MATERIALITY THRESHOLD: If the cap is binding and the uncapped estimate differs by >20%, the cap methodology itself becomes material.

KNOWN CONCERNS ALREADY SURFACED: None specific to cap methodology.

DEPENDENCY MAP: Thread 1 findings about external validity directly affect Thread 2's analysis of whether the cap binds appropriately.

RECOMMENDED SEQUENCING: Thread 1 should run first as its findings inform the plausibility cap analysis.

CEA PARAMETER MAP:
The water chlorination CEA calculates units of value per dollar for ILC Kenya and DSW in Kenya, Uganda, and Malawi. Key parameters:
- Pooled relative risk: 0.864 (from meta-analysis of 5 trials)
- Internal validity adjustment: 0.796 (for bundled interventions)
- External validity adjustment: varies by program (1.21 for ILC Kenya, 0.56-1.11 for DSW)
- Plausibility cap: varies (0.056-0.109)

EXCLUSION LIST:
- Chlorine taste aversion (addressed in adherence data)
- General concerns about RCT quality (addressed by internal validity adjustment)
"""


def test_parse_decomposer_basic():
    result = parse_decomposer_output(SAMPLE_DECOMPOSER_OUTPUT)
    assert len(result.threads) == 2
    assert result.threads[0].name == "External Validity of Trial Evidence"
    assert "relative_risk" in result.threads[0].scope or "relative_risk" in str(result.threads[0].key_questions)
    assert len(result.exclusion_list) >= 1
    assert "CEA" in result.cea_parameter_map or "parameter" in result.cea_parameter_map.lower()


def test_parse_decomposer_thread_has_context_md():
    result = parse_decomposer_output(SAMPLE_DECOMPOSER_OUTPUT)
    for thread in result.threads:
        assert len(thread.context_md) > 50
        assert thread.name in thread.context_md
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /home/tsondo/projects/givewell_redteam && python -m pytest tests/test_parsing.py -v`

Expected: FAIL — `ImportError`

- [ ] **Step 3: Implement agents.py with API utility and Decomposer**

```python
"""Agent caller functions — one per pipeline stage."""

from __future__ import annotations

import json
import logging
import re
import time
from pathlib import Path
from typing import Any

import anthropic

from pipeline.config import (
    ANTHROPIC_API_KEY,
    OPUS_MODEL,
    SONNET_MODEL,
    PROMPTS_DIR,
    RESULTS_DIR,
    MAX_RETRIES,
    MAX_TOKENS_DECOMPOSER,
    MAX_TOKENS_INVESTIGATOR,
    MAX_TOKENS_VERIFIER,
    MAX_TOKENS_QUANTIFIER,
    MAX_TOKENS_ADVERSARIAL,
    MAX_TOKENS_SYNTHESIZER,
    PRICING,
    COST_WARNING_PER_INTERVENTION,
)
from pipeline.schemas import (
    InvestigationThread,
    DecomposerOutput,
    CandidateCritique,
    VerifiedCritique,
    QuantifiedCritique,
    DebatedCritique,
    PipelineStats,
)

logger = logging.getLogger("pipeline")

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)


def call_api(
    model: str,
    system: str,
    user_message: str,
    stats: PipelineStats,
    stage: str,
    max_tokens: int,
    tools: list[dict] | None = None,
) -> str:
    """Call Anthropic API with retries and cost tracking. Returns text response."""
    for attempt in range(MAX_RETRIES + 1):
        try:
            kwargs: dict[str, Any] = {
                "model": model,
                "max_tokens": max_tokens,
                "system": system,
                "messages": [{"role": "user", "content": user_message}],
            }
            if tools:
                kwargs["tools"] = tools

            response = client.messages.create(**kwargs)

            # Track costs
            usage = response.usage
            cost = stats.record_call(
                stage, model, usage.input_tokens, usage.output_tokens, PRICING
            )
            logger.info(
                f"[{stage}] {model} | {usage.input_tokens} in / {usage.output_tokens} out | ${cost:.4f} | cumulative ${stats.total_cost:.4f}"
            )
            if stats.total_cost > COST_WARNING_PER_INTERVENTION:
                logger.warning(
                    f"WARNING: Cumulative cost ${stats.total_cost:.2f} exceeds ${COST_WARNING_PER_INTERVENTION:.0f} threshold"
                )

            # Extract text from response
            text_parts = []
            for block in response.content:
                if block.type == "text":
                    text_parts.append(block.text)
            return "\n".join(text_parts)

        except anthropic.RateLimitError:
            if attempt < MAX_RETRIES:
                wait = 2 ** (attempt + 1)
                logger.warning(f"Rate limited, retrying in {wait}s...")
                time.sleep(wait)
            else:
                raise
        except anthropic.APIError as e:
            if attempt < MAX_RETRIES:
                wait = 2 ** (attempt + 1)
                logger.warning(f"API error: {e}, retrying in {wait}s...")
                time.sleep(wait)
            else:
                raise
    raise RuntimeError("Unreachable")


def load_prompt(filename: str) -> str:
    """Load a prompt file from the prompts directory."""
    return (PROMPTS_DIR / filename).read_text()


def save_stage_output(
    intervention: str, stage_num: int, stage_name: str, data: Any, raw_text: str
) -> None:
    """Save both JSON and markdown outputs for a stage."""
    output_dir = RESULTS_DIR / intervention
    output_dir.mkdir(parents=True, exist_ok=True)

    prefix = f"{stage_num:02d}-{stage_name}"

    # JSON (structured)
    if hasattr(data, "to_dict"):
        json_path = output_dir / f"{prefix}.json"
        json_path.write_text(json.dumps(data.to_dict(), indent=2))
        logger.info(f"Saved {json_path}")
    elif isinstance(data, list) and data and hasattr(data[0], "to_dict"):
        json_path = output_dir / f"{prefix}.json"
        json_path.write_text(json.dumps([d.to_dict() for d in data], indent=2))
        logger.info(f"Saved {json_path}")

    # Markdown (human-readable)
    md_path = output_dir / f"{prefix}.md"
    md_path.write_text(raw_text)
    logger.info(f"Saved {md_path}")


# --- Parsing Functions ---


def parse_decomposer_output(text: str) -> DecomposerOutput:
    """Parse the Decomposer's text output into a DecomposerOutput."""
    threads: list[InvestigationThread] = []

    # Split into thread sections
    thread_sections = re.split(r"THREAD\s+\d+:\s*", text)
    # First element is preamble (before THREAD 1), skip it
    thread_sections = [s.strip() for s in thread_sections[1:] if s.strip()]

    for section in thread_sections:
        lines = section.split("\n")
        name = lines[0].strip()

        # Extract named sections
        def extract_section(section_text: str, header: str) -> str:
            pattern = rf"{header}:\s*(.*?)(?=\n[A-Z][A-Z ]+:|$)"
            match = re.search(pattern, section_text, re.DOTALL)
            return match.group(1).strip() if match else ""

        scope = extract_section(section, "SCOPE")
        key_params_text = extract_section(section, "KEY PARAMETERS")
        already = extract_section(section, "WHAT GIVEWELL ALREADY ACCOUNTS FOR")
        not_accounted = extract_section(section, "WHAT GIVEWELL DOES NOT ACCOUNT FOR")
        sources_text = extract_section(section, "DATA SOURCES TO EXAMINE")
        materiality = extract_section(section, "MATERIALITY THRESHOLD")
        known = extract_section(section, "KNOWN CONCERNS ALREADY SURFACED")

        # Parse lists
        key_params = [p.strip() for p in re.split(r"[,\n]", key_params_text) if p.strip()]
        sources = [s.strip() for s in re.split(r"[,\n]", sources_text) if s.strip()]

        # Build CONTEXT.md
        context_md = f"""# Investigation Thread: {name}

## Scope
{scope}

## Out of Scope
(Other threads handle other aspects of the analysis.)

## CEA Parameters in Play
{key_params_text}

## What GiveWell Already Accounts For
{already}
DO NOT re-raise these as critiques.

## What GiveWell Does Not Account For
{not_accounted}

## Key Source Materials
{sources_text}

## Definition of "Material Critique"
{materiality}

## Known Concerns Already Surfaced
{known}
"""

        key_questions = []
        if not_accounted:
            key_questions.append(not_accounted[:200])

        threads.append(InvestigationThread(
            name=name,
            scope=scope,
            key_questions=key_questions,
            cea_parameters_affected=key_params,
            relevant_sources=sources,
            out_of_scope="Other threads",
            context_md=context_md,
        ))

    # Extract exclusion list
    exclusion_list: list[str] = []
    excl_match = re.search(r"EXCLUSION LIST:\s*(.*?)(?=\n[A-Z][A-Z ]+:|$)", text, re.DOTALL)
    if excl_match:
        for line in excl_match.group(1).strip().split("\n"):
            line = line.strip().lstrip("- ")
            if line:
                exclusion_list.append(line)

    # Extract CEA parameter map
    cea_map = ""
    map_match = re.search(r"CEA PARAMETER MAP:\s*(.*?)(?=\nEXCLUSION LIST:|$)", text, re.DOTALL)
    if map_match:
        cea_map = map_match.group(1).strip()

    return DecomposerOutput(
        threads=threads,
        exclusion_list=exclusion_list,
        cea_parameter_map=cea_map,
    )


# --- Stage Runners ---


def run_decomposer(
    intervention_report: str,
    cea_summary: str,
    baseline_output: str | None,
    stats: PipelineStats,
    intervention: str,
) -> tuple[DecomposerOutput, str]:
    """Stage 1: Decompose the analysis into investigation threads."""
    system = load_prompt("decomposer.md")

    user_parts = [
        "## Intervention Report\n\n" + intervention_report,
        "\n\n## CEA Parameter Summary\n\n" + cea_summary,
    ]
    if baseline_output:
        user_parts.append("\n\n## GiveWell's Previous AI Red Teaming Output\n\n" + baseline_output)

    user_message = "\n".join(user_parts)

    raw = call_api(OPUS_MODEL, system, user_message, stats, "decomposer", MAX_TOKENS_DECOMPOSER)
    parsed = parse_decomposer_output(raw)

    save_stage_output(intervention, 1, "decomposer", parsed, raw)
    return parsed, raw
```

- [ ] **Step 4: Run parsing tests**

Run: `cd /home/tsondo/projects/givewell_redteam && python -m pytest tests/test_parsing.py -v`

Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add pipeline/agents.py tests/test_parsing.py
git commit -m "feat: add API utility, decomposer caller, and output parsing"
```

---

## Task 6: Agent Callers — Investigators, Verifier, Quantifier

**Files:**
- Modify: `pipeline/agents.py`
- Modify: `tests/test_parsing.py`

- [ ] **Step 1: Write parsing tests for Investigator and Verifier output**

Add to `tests/test_parsing.py`:

```python
from pipeline.agents import parse_investigator_output, parse_verifier_output

SAMPLE_INVESTIGATOR_OUTPUT = """
CRITIQUE 1: Water Source Type Mismatch

HYPOTHESIS: The trials in the Kremer meta-analysis predominantly used point-of-use chlorination with stored water, while DSW uses source-level dispensers. The effectiveness of source chlorination versus point-of-use may differ due to recontamination during transport and storage.

MECHANISM: If source chlorination is less effective than point-of-use (due to residual chlorine decay during transport), the actual mortality reduction could be smaller than the trial-based estimate. This would reduce the relative risk parameter, lowering cost-effectiveness.

EVIDENCE: UNGROUNDED — needs verification. The concern is based on the logical distinction between source and point-of-use treatment, but I cannot cite a specific study comparing mortality outcomes between these delivery methods.

STRENGTH: MEDIUM

NOVELTY CHECK: Not on the exclusion list. GiveWell's adherence adjustment partially captures this (lower measured chlorine at point of use), but doesn't explicitly model the source-vs-POU distinction.

CRITIQUE 2: Seasonal Efficacy Variation

HYPOTHESIS: Chlorination effectiveness varies seasonally with water turbidity. During rainy seasons, higher turbidity may reduce chlorine efficacy, meaning the annual average effect is lower than suggested by trials that may not fully capture seasonal variation.

MECHANISM: Would reduce the effective relative risk across the year, lowering the mortality effect and cost-effectiveness.

EVIDENCE: Si et al. 2022 discusses turbidity effects on chlorination. WHO guidelines note chlorine demand increases with turbidity.

STRENGTH: HIGH

NOVELTY CHECK: Not on the exclusion list. This is a distinct mechanism from general adherence concerns.

SUMMARY: The most important finding is the potential seasonal variation in efficacy, which could systematically bias the annual mortality estimate.

RECOMMENDED VERIFICATION PRIORITIES: Critique 2 (seasonal efficacy) should be verified first as it has the strongest evidence base and clearest mechanism.
"""


def test_parse_investigator_output():
    critiques = parse_investigator_output(SAMPLE_INVESTIGATOR_OUTPUT, "External Validity")
    assert len(critiques) == 2
    assert critiques[0].title == "Water Source Type Mismatch"
    assert critiques[0].thread_name == "External Validity"
    assert "source chlorination" in critiques[0].hypothesis.lower() or "source" in critiques[0].hypothesis.lower()
    assert critiques[1].title == "Seasonal Efficacy Variation"


SAMPLE_VERIFIER_OUTPUT = """
CRITIQUE: Seasonal Efficacy Variation

CITATION CHECK:
- Si et al. 2022: VERIFIED — Paper exists and discusses impact of turbidity on chlorine demand.
- WHO guidelines: VERIFIED — WHO drinking water quality guidelines confirm higher chlorine demand in turbid water.

CLAIM CHECK:
- Chlorination effectiveness varies with turbidity: VERIFIED — well established in water chemistry literature.
- Seasonal variation could reduce annual average effect: PLAUSIBLE — logical inference, no direct mortality study.

EVIDENCE FOUND:
- Lantagne et al. 2011 found free chlorine residual drops below protective levels when turbidity exceeds 10 NTU.
- EPA guidelines recommend pre-sedimentation for water above 10 NTU before chlorination.

OVERALL VERDICT: PARTIALLY VERIFIED
Core hypothesis about turbidity-efficacy relationship is verified. The link to mortality reduction is plausible but not directly studied. Seasonal variation in effectiveness is well-established for chlorine chemistry but the magnitude of its effect on mortality outcomes is uncertain.

REVISED CRITIQUE:
The seasonal variation in water turbidity may reduce the average annual effectiveness of chlorination programs. While the chlorine chemistry is well-established, the magnitude of mortality impact during high-turbidity seasons has not been directly measured in the trials underlying the meta-analysis.
"""


def test_parse_verifier_output():
    original = CandidateCritique(
        thread_name="Ext Validity", title="Seasonal Efficacy Variation",
        hypothesis="H", mechanism="M", parameters_affected=["rr"],
        suggested_evidence=["Si et al. 2022"], estimated_direction="decreases",
        estimated_magnitude="medium",
    )
    verified = parse_verifier_output(SAMPLE_VERIFIER_OUTPUT, original)
    assert verified.verdict == "partially_verified"
    assert len(verified.evidence_found) >= 1
    assert verified.evidence_strength in ("strong", "moderate", "weak")
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /home/tsondo/projects/givewell_redteam && python -m pytest tests/test_parsing.py -v`

Expected: FAIL on new tests.

- [ ] **Step 3: Implement Investigator, Verifier, and Quantifier parsing + callers**

Add to `pipeline/agents.py`:

```python
def parse_investigator_output(text: str, thread_name: str) -> list[CandidateCritique]:
    """Parse Investigator text into CandidateCritiques."""
    critiques: list[CandidateCritique] = []

    sections = re.split(r"CRITIQUE\s+\d+:\s*", text)
    sections = [s.strip() for s in sections[1:] if s.strip()]

    for section in sections:
        lines = section.split("\n")
        title = lines[0].strip()

        def extract(header: str) -> str:
            pattern = rf"{header}:\s*(.*?)(?=\n[A-Z][A-Z ]+:|SUMMARY:|RECOMMENDED|$)"
            match = re.search(pattern, section, re.DOTALL)
            return match.group(1).strip() if match else ""

        hypothesis = extract("HYPOTHESIS")
        mechanism = extract("MECHANISM")
        evidence_text = extract("EVIDENCE")
        strength = extract("STRENGTH").strip().upper()
        novelty = extract("NOVELTY CHECK")

        # Infer direction from mechanism text
        direction = "uncertain"
        mech_lower = mechanism.lower()
        if "lower" in mech_lower or "reduc" in mech_lower or "decreas" in mech_lower:
            direction = "decreases"
        elif "increas" in mech_lower or "higher" in mech_lower:
            direction = "increases"

        # Infer magnitude from strength
        magnitude_map = {"HIGH": "large", "MEDIUM": "medium", "LOW": "small"}
        magnitude = magnitude_map.get(strength, "unknown")

        # Extract any parameter names mentioned
        params = []
        for param_name in ["relative_risk", "external_validity", "internal_validity",
                          "plausibility_cap", "adherence", "mortality", "morbidity", "cost"]:
            if param_name in section.lower():
                params.append(param_name)

        critiques.append(CandidateCritique(
            thread_name=thread_name,
            title=title,
            hypothesis=hypothesis,
            mechanism=mechanism,
            parameters_affected=params if params else ["unknown"],
            suggested_evidence=[e.strip() for e in evidence_text.split("\n") if e.strip() and not e.strip().startswith("UNGROUNDED")],
            estimated_direction=direction,
            estimated_magnitude=magnitude,
        ))

    return critiques


def parse_verifier_output(text: str, original: CandidateCritique) -> VerifiedCritique:
    """Parse Verifier text into a VerifiedCritique."""
    # Extract verdict
    verdict_match = re.search(r"OVERALL VERDICT:\s*(VERIFIED|PARTIALLY VERIFIED|UNVERIFIABLE|REJECTED)", text, re.IGNORECASE)
    verdict_raw = verdict_match.group(1).strip().upper() if verdict_match else "unverified"
    verdict_map = {
        "VERIFIED": "verified",
        "PARTIALLY VERIFIED": "partially_verified",
        "UNVERIFIABLE": "unverified",
        "REJECTED": "unverified",
    }
    verdict = verdict_map.get(verdict_raw, "unverified")

    # Extract evidence found
    evidence_section = ""
    ev_match = re.search(r"EVIDENCE FOUND:\s*(.*?)(?=\nOVERALL VERDICT:|$)", text, re.DOTALL)
    if ev_match:
        evidence_section = ev_match.group(1).strip()
    evidence_found = [line.strip().lstrip("- ") for line in evidence_section.split("\n") if line.strip() and line.strip() != "-"]

    # Determine evidence strength from verdict context
    verdict_context = ""
    if verdict_match:
        verdict_context = text[verdict_match.end():].strip()[:500]
    if "well-established" in verdict_context.lower() or "strong" in verdict_context.lower():
        strength = "strong"
    elif "plausible" in verdict_context.lower() or "uncertain" in verdict_context.lower():
        strength = "moderate"
    else:
        strength = "weak"

    # Extract revised hypothesis
    revised = None
    rev_match = re.search(r"REVISED CRITIQUE:\s*(.*?)$", text, re.DOTALL)
    if rev_match and verdict == "partially_verified":
        revised = rev_match.group(1).strip()

    # Extract counter-evidence and caveats
    counter = []
    caveats = []
    claim_section = ""
    claim_match = re.search(r"CLAIM CHECK:\s*(.*?)(?=\nEVIDENCE FOUND:|$)", text, re.DOTALL)
    if claim_match:
        claim_section = claim_match.group(1)
        for line in claim_section.split("\n"):
            if "PLAUSIBLE" in line.upper() or "UNVERIFIABLE" in line.upper():
                caveats.append(line.strip().lstrip("- "))

    return VerifiedCritique(
        original=original,
        verdict=verdict,
        evidence_found=evidence_found,
        evidence_strength=strength,
        counter_evidence=counter,
        caveats=caveats,
        revised_hypothesis=revised,
    )


def run_investigators(
    threads: list[InvestigationThread],
    exclusion_list: list[str],
    stats: PipelineStats,
    intervention: str,
) -> tuple[list[CandidateCritique], str]:
    """Stage 2: Run one Investigator per thread (sequential)."""
    template = load_prompt("investigator-template.md")
    all_critiques: list[CandidateCritique] = []
    all_raw: list[str] = []

    for i, thread in enumerate(threads):
        logger.info(f"Running Investigator {i+1}/{len(threads)}: {thread.name}")

        system = template.replace("{{CONTEXT_MD}}", thread.context_md)
        user_message = (
            f"## Thread: {thread.name}\n\n"
            f"## Context\n\n{thread.context_md}\n\n"
            f"## Exclusion List\n\n"
            + "\n".join(f"- {e}" for e in exclusion_list)
        )

        raw = call_api(SONNET_MODEL, system, user_message, stats, f"investigator-{i+1}", MAX_TOKENS_INVESTIGATOR)
        critiques = parse_investigator_output(raw, thread.name)
        all_critiques.extend(critiques)
        all_raw.append(f"## Thread: {thread.name}\n\n{raw}")

    combined_raw = "\n\n---\n\n".join(all_raw)
    save_stage_output(intervention, 2, "investigators", all_critiques, combined_raw)
    return all_critiques, combined_raw


def run_verifier(
    critiques: list[CandidateCritique],
    stats: PipelineStats,
    intervention: str,
) -> tuple[list[VerifiedCritique], str]:
    """Stage 3: Verify each critique individually with web search."""
    system = load_prompt("verifier.md")
    verified: list[VerifiedCritique] = []
    all_raw: list[str] = []

    for i, critique in enumerate(critiques):
        logger.info(f"Verifying critique {i+1}/{len(critiques)}: {critique.title}")

        user_message = (
            f"## Candidate Critique\n\n"
            f"**Title:** {critique.title}\n"
            f"**Thread:** {critique.thread_name}\n"
            f"**Hypothesis:** {critique.hypothesis}\n"
            f"**Mechanism:** {critique.mechanism}\n"
            f"**Suggested Evidence:** {', '.join(critique.suggested_evidence)}\n"
            f"**Estimated Direction:** {critique.estimated_direction}\n"
            f"**Estimated Magnitude:** {critique.estimated_magnitude}\n"
        )

        raw = call_api(
            SONNET_MODEL, system, user_message, stats,
            f"verifier-{i+1}", MAX_TOKENS_VERIFIER,
            tools=[{"type": "web_search_20250305", "name": "web_search"}],
        )

        v = parse_verifier_output(raw, critique)
        verified.append(v)
        all_raw.append(f"## {critique.title}\n\n{raw}")

        if v.verdict == "unverified":
            logger.info(f"  → UNVERIFIED (will be logged but not passed forward)")
        else:
            logger.info(f"  → {v.verdict.upper()} ({v.evidence_strength} evidence)")

    # Filter: keep verified + partially_verified
    passing = [v for v in verified if v.verdict in ("verified", "partially_verified")]
    logger.info(f"Verifier: {len(passing)}/{len(verified)} critiques passed")

    combined_raw = "\n\n---\n\n".join(all_raw)
    save_stage_output(intervention, 3, "verifier", verified, combined_raw)
    return passing, combined_raw


def run_quantifier(
    critiques: list[VerifiedCritique],
    cea: Any,  # WaterCEA instance
    cea_parameter_map: str,
    stats: PipelineStats,
    intervention: str,
) -> tuple[list[QuantifiedCritique], str]:
    """Stage 4: Quantify impact of each verified critique against the CEA."""
    system = load_prompt("quantifier.md")
    quantified: list[QuantifiedCritique] = []
    all_raw: list[str] = []

    cea_summary = cea.get_parameter_summary()

    for i, critique in enumerate(critiques):
        logger.info(f"Quantifying critique {i+1}/{len(critiques)}: {critique.original.title}")

        user_message = (
            f"## Verified Critique\n\n"
            f"**Title:** {critique.original.title}\n"
            f"**Hypothesis:** {critique.revised_hypothesis or critique.original.hypothesis}\n"
            f"**Mechanism:** {critique.original.mechanism}\n"
            f"**Evidence:** {'; '.join(critique.evidence_found)}\n"
            f"**Evidence Strength:** {critique.evidence_strength}\n"
            f"**Parameters Affected:** {', '.join(critique.original.parameters_affected)}\n\n"
            f"## CEA Parameter Map\n\n{cea_parameter_map}\n\n"
            f"## CEA Data\n\n{cea_summary}\n"
        )

        raw = call_api(OPUS_MODEL, system, user_message, stats, f"quantifier-{i+1}", MAX_TOKENS_QUANTIFIER)

        # Parse the Quantifier's suggested parameter ranges, then run actual sensitivity
        q = _parse_and_run_quantifier(raw, critique, cea)
        quantified.append(q)
        all_raw.append(f"## {critique.original.title}\n\n{raw}")

    combined_raw = "\n\n---\n\n".join(all_raw)
    save_stage_output(intervention, 4, "quantifier", quantified, combined_raw)
    return quantified, combined_raw


def _parse_and_run_quantifier(
    raw: str, critique: VerifiedCritique, cea: Any
) -> QuantifiedCritique:
    """Parse Quantifier output and run actual sensitivity analysis.

    The Quantifier API call identifies which parameters to change and suggests
    ranges. We then run the actual computation in Python.
    """
    # Extract parameter mapping from API response
    # Look for PARAMETER MAPPING, PLAUSIBLE RANGE, MATERIALITY sections
    target_params: list[dict[str, Any]] = []
    alt_range: list[dict[str, Any]] = []

    # Try to extract suggested parameter values
    # The Quantifier's output will mention specific parameter names and values.
    # We do a best-effort parse and fall back to the critique's stated parameters.
    param_section = ""
    pm_match = re.search(r"PARAMETER MAPPING:\s*(.*?)(?=PLAUSIBLE RANGE:|SENSITIVITY|$)", raw, re.DOTALL)
    if pm_match:
        param_section = pm_match.group(1)

    range_section = ""
    pr_match = re.search(r"PLAUSIBLE RANGE:\s*(.*?)(?=SENSITIVITY|BOTTOM-LINE|$)", raw, re.DOTALL)
    if pr_match:
        range_section = pr_match.group(1)

    # Extract numbers from the range section
    # Look for patterns like "low: 0.85" "high: 0.95" "current: 0.864"
    numbers = re.findall(r"(\d+\.?\d*)", range_section)

    # Run sensitivity for each affected parameter
    sensitivity_results: dict[str, Any] = {}
    for param in critique.original.parameters_affected:
        if param in ("relative_risk", "internal_validity_under5", "internal_validity_over5",
                     "external_validity", "plausibility_cap", "internal_validity_morbidity",
                     "morbidity_ext_validity"):
            # Run across all programs
            for prog_key in cea.programs:
                baseline = cea.compute_cost_effectiveness(prog_key)
                sensitivity_results[f"{prog_key}_baseline"] = baseline

    # Default: use the critique's stated parameters with reasonable perturbations
    baseline_ce = cea.compute_cost_effectiveness("ilc_kenya")
    sensitivity_results["baseline"] = baseline_ce

    # Determine materiality
    max_pct_change = 0.0
    for key, val in sensitivity_results.items():
        if key != "baseline" and "baseline" not in key:
            pct = abs(val - baseline_ce) / baseline_ce if baseline_ce else 0
            max_pct_change = max(max_pct_change, pct)

    if max_pct_change >= 0.10:
        materiality = "material"
    elif max_pct_change >= 0.01:
        materiality = "notable"
    else:
        materiality = "immaterial"

    return QuantifiedCritique(
        critique=critique,
        target_parameters=target_params,
        alternative_range=alt_range,
        sensitivity_results=sensitivity_results,
        materiality=materiality,
        interaction_effects=[],
    )
```

**Important implementation note:** The `_parse_and_run_quantifier` function above is a skeleton. During actual implementation, it needs to:
1. Parse the Quantifier API response more carefully to extract specific parameter names and suggested ranges
2. Map those to `compute_cost_effectiveness()` keyword arguments
3. Run `cea.run_sensitivity()` with the extracted ranges
4. Compute materiality across all programs

The tests for this will be integration tests (requiring actual API calls), so we test the parsing logic separately and verify the sensitivity calculations through the spreadsheet tests.

- [ ] **Step 4: Run tests**

Run: `cd /home/tsondo/projects/givewell_redteam && python -m pytest tests/test_parsing.py -v`

Expected: All tests pass.

- [ ] **Step 5: Commit**

```bash
git add pipeline/agents.py tests/test_parsing.py
git commit -m "feat: add investigator, verifier, and quantifier agent callers"
```

---

## Task 7: Agent Callers — Adversarial Pair and Synthesizer

**Files:**
- Modify: `pipeline/agents.py`

- [ ] **Step 1: Implement Adversarial and Synthesizer callers**

Add to `pipeline/agents.py`:

```python
def run_adversarial(
    critiques: list[QuantifiedCritique],
    intervention_report: str,
    cea_parameter_map: str,
    stats: PipelineStats,
    intervention: str,
) -> tuple[list[DebatedCritique], str]:
    """Stage 5: Adversarial debate for each quantified critique."""
    advocate_prompt = load_prompt("adversarial-advocate.md")
    challenger_prompt = load_prompt("adversarial-challenger.md")
    debated: list[DebatedCritique] = []
    all_raw: list[str] = []

    for i, q in enumerate(critiques):
        if q.materiality == "immaterial":
            logger.info(f"Skipping immaterial critique: {q.critique.original.title}")
            continue

        title = q.critique.original.title
        logger.info(f"Adversarial debate {i+1}/{len(critiques)}: {title}")

        critique_summary = (
            f"**Title:** {title}\n"
            f"**Hypothesis:** {q.critique.revised_hypothesis or q.critique.original.hypothesis}\n"
            f"**Mechanism:** {q.critique.original.mechanism}\n"
            f"**Evidence:** {'; '.join(q.critique.evidence_found)}\n"
            f"**Evidence Strength:** {q.critique.evidence_strength}\n"
            f"**Sensitivity Results:** {json.dumps(q.sensitivity_results, indent=2)}\n"
            f"**Materiality:** {q.materiality}\n"
        )

        # Advocate
        advocate_user = (
            f"## Quantified Critique\n\n{critique_summary}\n\n"
            f"## GiveWell's Intervention Report (excerpts)\n\n{intervention_report[:3000]}\n\n"
            f"## CEA Parameter Map\n\n{cea_parameter_map}\n"
        )
        advocate_raw = call_api(
            SONNET_MODEL, advocate_prompt, advocate_user, stats,
            f"advocate-{i+1}", MAX_TOKENS_ADVERSARIAL,
        )

        # Challenger
        challenger_user = (
            f"## Quantified Critique\n\n{critique_summary}\n\n"
            f"## Advocate's Defense\n\n{advocate_raw}\n\n"
            f"## Verification Evidence\n\n{'; '.join(q.critique.evidence_found)}\n"
        )
        challenger_raw = call_api(
            SONNET_MODEL, challenger_prompt, challenger_user, stats,
            f"challenger-{i+1}", MAX_TOKENS_ADVERSARIAL,
        )

        # Parse surviving strength from Challenger output
        strength = "moderate"
        strength_match = re.search(r"SURVIVING STRENGTH:\s*(Strong|Moderate|Weak)", challenger_raw, re.IGNORECASE)
        if strength_match:
            strength = strength_match.group(1).strip().lower()

        # Parse recommended action
        action = "investigate"
        action_match = re.search(r"RECOMMENDED ACTION:\s*\[?(.*?)\]?$", challenger_raw, re.MULTILINE | re.IGNORECASE)
        if action_match:
            action_text = action_match.group(1).strip().lower()
            for a in ("investigate", "adjust_model", "monitor", "dismiss"):
                if a.replace("_", " ") in action_text or a in action_text:
                    action = a
                    break

        # Parse key unresolved
        unresolved: list[str] = []
        unr_match = re.search(r"KEY UNRESOLVED QUESTIONS:\s*(.*?)(?=SURVIVING STRENGTH:|$)", challenger_raw, re.DOTALL)
        if unr_match:
            for line in unr_match.group(1).strip().split("\n"):
                line = line.strip().lstrip("- ")
                if line:
                    unresolved.append(line)

        debated.append(DebatedCritique(
            critique=q,
            advocate_defense=advocate_raw,
            challenger_rebuttal=challenger_raw,
            surviving_strength=strength,
            key_unresolved=unresolved,
            recommended_action=action,
        ))

        combined = f"## {title}\n\n### Advocate\n{advocate_raw}\n\n### Challenger\n{challenger_raw}"
        all_raw.append(combined)

    combined_raw = "\n\n---\n\n".join(all_raw)
    save_stage_output(intervention, 5, "adversarial", debated, combined_raw)
    return debated, combined_raw


def run_synthesizer(
    debated: list[DebatedCritique],
    all_critiques_count: int,
    verified_count: int,
    baseline_output: str | None,
    stats: PipelineStats,
    intervention: str,
) -> str:
    """Stage 6: Produce the final ranked report."""
    system = load_prompt("synthesizer.md")

    # Build the full input for the Synthesizer
    critiques_text = []
    for d in debated:
        c = d.critique.critique.original
        critiques_text.append(
            f"### {c.title}\n"
            f"- **Thread:** {c.thread_name}\n"
            f"- **Hypothesis:** {d.critique.critique.revised_hypothesis or c.hypothesis}\n"
            f"- **Mechanism:** {c.mechanism}\n"
            f"- **Evidence:** {'; '.join(d.critique.critique.evidence_found)}\n"
            f"- **Evidence Strength:** {d.critique.critique.evidence_strength}\n"
            f"- **Sensitivity Results:** {json.dumps(d.critique.sensitivity_results, indent=2)}\n"
            f"- **Materiality:** {d.critique.materiality}\n"
            f"- **Surviving Strength:** {d.surviving_strength}\n"
            f"- **Advocate Defense:** {d.advocate_defense[:500]}...\n"
            f"- **Challenger Rebuttal:** {d.challenger_rebuttal[:500]}...\n"
            f"- **Key Unresolved:** {'; '.join(d.key_unresolved)}\n"
            f"- **Recommended Action:** {d.recommended_action}\n"
        )

    user_message = (
        f"## Pipeline Statistics\n"
        f"- Total candidate critiques generated: {all_critiques_count}\n"
        f"- Verified critiques: {verified_count}\n"
        f"- Critiques surviving adversarial review: {len(debated)}\n\n"
        f"## Surviving Critiques\n\n{''.join(critiques_text)}\n"
    )

    if baseline_output:
        user_message += f"\n\n## GiveWell's Previous AI Red Teaming Output\n\n{baseline_output[:5000]}\n"

    raw = call_api(OPUS_MODEL, system, user_message, stats, "synthesizer", MAX_TOKENS_SYNTHESIZER)

    save_stage_output(intervention, 6, "synthesizer", None, raw)
    return raw
```

- [ ] **Step 2: Verify no import errors**

Run: `cd /home/tsondo/projects/givewell_redteam && python -c "from pipeline.agents import run_adversarial, run_synthesizer; print('OK')"`

Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add pipeline/agents.py
git commit -m "feat: add adversarial pair and synthesizer agent callers"
```

---

## Task 8: Pipeline Orchestrator

**Files:**
- Create: `pipeline/run_pipeline.py`

- [ ] **Step 1: Implement the orchestrator**

```python
"""Main pipeline orchestrator. Run with: python -m pipeline.run_pipeline water-chlorination"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

from pipeline.config import RESULTS_DIR, DATA_DIR, INTERVENTION_URLS, ANTHROPIC_API_KEY
from pipeline.schemas import (
    DecomposerOutput,
    CandidateCritique,
    VerifiedCritique,
    QuantifiedCritique,
    DebatedCritique,
    PipelineStats,
)
from pipeline.agents import (
    run_decomposer,
    run_investigators,
    run_verifier,
    run_quantifier,
    run_adversarial,
    run_synthesizer,
    call_api,
)
from pipeline.spreadsheet import WaterCEA

STAGES = ["decomposer", "investigators", "verifier", "quantifier", "adversarial", "synthesizer"]


def setup_logging(intervention: str) -> None:
    """Configure logging to both console and file."""
    output_dir = RESULTS_DIR / intervention
    output_dir.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("pipeline")
    logger.setLevel(logging.INFO)

    # Console handler
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s", datefmt="%H:%M:%S"))
    logger.addHandler(ch)

    # File handler
    fh = logging.FileHandler(output_dir / "pipeline.log")
    fh.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(fh)


def fetch_web_content(url: str, stats: PipelineStats) -> str:
    """Fetch content from a URL using the Anthropic API with web search.

    Uses a simple prompt to retrieve and summarize the page content.
    """
    logger = logging.getLogger("pipeline")
    logger.info(f"Fetching: {url}")

    from pipeline.config import SONNET_MODEL
    text = call_api(
        model=SONNET_MODEL,
        system="You are a research assistant. Retrieve and return the full content of the requested URL. Preserve all substantive content, data, and arguments. Do not summarize — return as much of the original text as possible.",
        user_message=f"Please retrieve and return the full content from this URL: {url}",
        stats=stats,
        stage="fetch",
        max_tokens=8192,
        tools=[{"type": "web_search_20250305", "name": "web_search"}],
    )
    return text


def load_stage_json(intervention: str, stage_num: int, stage_name: str) -> dict | list:
    """Load a stage's JSON output from disk."""
    path = RESULTS_DIR / intervention / f"{stage_num:02d}-{stage_name}.json"
    if not path.exists():
        raise FileNotFoundError(f"Cannot resume: {path} not found. Run earlier stages first.")
    return json.loads(path.read_text())


def run_pipeline(intervention: str, resume_from: str | None = None) -> None:
    """Run the full pipeline for an intervention."""
    logger = logging.getLogger("pipeline")
    stats = PipelineStats()

    # Determine which stages to run
    start_idx = 0
    if resume_from:
        if resume_from not in STAGES:
            print(f"Error: Unknown stage '{resume_from}'. Valid stages: {', '.join(STAGES)}")
            sys.exit(1)
        start_idx = STAGES.index(resume_from)
        logger.info(f"Resuming from stage: {resume_from} (stage {start_idx + 1})")

    # Validate intervention
    if intervention not in INTERVENTION_URLS:
        print(f"Error: Unknown intervention '{intervention}'. Valid: {', '.join(INTERVENTION_URLS.keys())}")
        sys.exit(1)

    urls = INTERVENTION_URLS[intervention]

    # Load CEA spreadsheet
    spreadsheet_path = DATA_DIR / urls["spreadsheet"]
    if not spreadsheet_path.exists():
        print(f"Error: CEA spreadsheet not found at {spreadsheet_path}")
        sys.exit(1)
    cea = WaterCEA(spreadsheet_path)
    cea_summary = cea.get_parameter_summary()

    # Fetch source materials (or use cached if resuming past decomposer)
    intervention_report = ""
    baseline_output = ""
    if start_idx <= 0:
        logger.info("=== Fetching source materials ===")
        intervention_report = fetch_web_content(urls["report"], stats)
        if urls.get("baseline"):
            baseline_output = fetch_web_content(urls["baseline"], stats)

    # --- Stage 1: Decomposer ---
    decomposed: DecomposerOutput | None = None
    if start_idx <= 0:
        logger.info("=== Stage 1: Decomposer ===")
        decomposed, _ = run_decomposer(intervention_report, cea_summary, baseline_output or None, stats, intervention)
        logger.info(f"Decomposer produced {len(decomposed.threads)} threads")
    elif start_idx > 0:
        data = load_stage_json(intervention, 1, "decomposer")
        decomposed = DecomposerOutput.from_dict(data)
        logger.info(f"Loaded decomposer output: {len(decomposed.threads)} threads")

    assert decomposed is not None

    # --- Stage 2: Investigators ---
    candidates: list[CandidateCritique] = []
    if start_idx <= 1:
        logger.info("=== Stage 2: Investigators ===")
        candidates, _ = run_investigators(decomposed.threads, decomposed.exclusion_list, stats, intervention)
        logger.info(f"Investigators produced {len(candidates)} candidate critiques")
    elif start_idx > 1:
        data = load_stage_json(intervention, 2, "investigators")
        candidates = [CandidateCritique.from_dict(d) for d in data]
        logger.info(f"Loaded {len(candidates)} candidate critiques")

    # --- Stage 3: Verifier ---
    verified: list[VerifiedCritique] = []
    if start_idx <= 2:
        logger.info("=== Stage 3: Verifier ===")
        verified, _ = run_verifier(candidates, stats, intervention)
        logger.info(f"Verifier passed {len(verified)} critiques")
    elif start_idx > 2:
        data = load_stage_json(intervention, 3, "verifier")
        all_verified = [VerifiedCritique.from_dict(d) for d in data]
        verified = [v for v in all_verified if v.verdict in ("verified", "partially_verified")]
        logger.info(f"Loaded {len(verified)} verified critiques")

    # --- Stage 4: Quantifier ---
    quantified: list[QuantifiedCritique] = []
    if start_idx <= 3:
        logger.info("=== Stage 4: Quantifier ===")
        quantified, _ = run_quantifier(verified, cea, decomposed.cea_parameter_map, stats, intervention)
        logger.info(f"Quantifier produced {len(quantified)} quantified critiques")
    elif start_idx > 3:
        data = load_stage_json(intervention, 4, "quantifier")
        quantified = [QuantifiedCritique.from_dict(d) for d in data]
        logger.info(f"Loaded {len(quantified)} quantified critiques")

    # --- Stage 5: Adversarial ---
    debated: list[DebatedCritique] = []
    if start_idx <= 4:
        logger.info("=== Stage 5: Adversarial Pair ===")
        # Refetch report if we're resuming and don't have it
        if not intervention_report:
            intervention_report = fetch_web_content(urls["report"], stats)
        debated, _ = run_adversarial(quantified, intervention_report, decomposed.cea_parameter_map, stats, intervention)
        logger.info(f"Adversarial pair produced {len(debated)} debated critiques")
    elif start_idx > 4:
        data = load_stage_json(intervention, 5, "adversarial")
        debated = [DebatedCritique.from_dict(d) for d in data]
        logger.info(f"Loaded {len(debated)} debated critiques")

    # --- Stage 6: Synthesizer ---
    if start_idx <= 5:
        logger.info("=== Stage 6: Synthesizer ===")
        if not baseline_output and urls.get("baseline"):
            baseline_output = fetch_web_content(urls["baseline"], stats)
        final = run_synthesizer(
            debated, len(candidates), len(verified),
            baseline_output or None, stats, intervention,
        )
        logger.info("Synthesizer complete — final report written")

    # --- Summary ---
    logger.info("=== Pipeline Complete ===")
    logger.info(f"Total input tokens: {stats.total_input_tokens:,}")
    logger.info(f"Total output tokens: {stats.total_output_tokens:,}")
    logger.info(f"Total cost: ${stats.total_cost:.4f}")
    for stage, cost in stats.stage_costs.items():
        logger.info(f"  {stage}: ${cost:.4f}")

    # Save stats
    stats_path = RESULTS_DIR / intervention / "pipeline-stats.json"
    stats_path.write_text(json.dumps(stats.to_dict(), indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the red teaming pipeline")
    parser.add_argument("intervention", choices=list(INTERVENTION_URLS.keys()),
                       help="Which intervention to analyze")
    parser.add_argument("--resume-from", choices=STAGES, default=None,
                       help="Resume from a specific stage (loads earlier stages from disk)")
    args = parser.parse_args()

    setup_logging(args.intervention)
    run_pipeline(args.intervention, args.resume_from)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Verify it parses args correctly**

Run: `cd /home/tsondo/projects/givewell_redteam && python -m pipeline.run_pipeline --help`

Expected: Usage message with `water-chlorination`, `itns`, `smc` choices and `--resume-from` flag.

- [ ] **Step 3: Commit**

```bash
git add pipeline/run_pipeline.py
git commit -m "feat: add pipeline orchestrator with --resume-from support"
```

---

## Task 9: Integration Test — Dry Run

**Files:**
- No new files — this is a manual verification step.

- [ ] **Step 1: Run the full test suite**

Run: `cd /home/tsondo/projects/givewell_redteam && python -m pytest tests/ -v`

Expected: All tests pass.

- [ ] **Step 2: Do a dry run of Stage 1 only**

Run: `cd /home/tsondo/projects/givewell_redteam && python -m pipeline.run_pipeline water-chlorination`

Observe:
- Source materials are fetched
- Decomposer runs and produces threads
- Output files appear in `results/water-chlorination/`
- Cost is logged
- Then let it continue (or Ctrl-C after Stage 1 to review)

- [ ] **Step 3: Review Decomposer output**

Read: `results/water-chlorination/01-decomposer.md` and `01-decomposer.json`

Verify:
- 5-8 investigation threads produced
- Each thread has a scope, parameters, and exclusions
- The exclusion list is non-empty
- The CEA parameter map is populated

- [ ] **Step 4: Resume from Stage 2 if needed**

Run: `cd /home/tsondo/projects/givewell_redteam && python -m pipeline.run_pipeline water-chlorination --resume-from investigators`

This loads the decomposer output from disk and continues.

- [ ] **Step 5: Review full pipeline output after completion**

Check `results/water-chlorination/06-synthesizer.md` — this is the final report. Verify it contains ranked critiques with evidence, quantification, and debate summaries.

- [ ] **Step 6: Commit any fixes**

```bash
git add -A
git commit -m "fix: integration fixes from dry run"
```

---

## Execution Order Summary

| Task | Component | Risk | Dependencies |
|------|-----------|------|-------------|
| 1 | Config + scaffolding | Low | None |
| 2 | Schemas | Low | Task 1 |
| 3 | Spreadsheet reader | **High** | Task 1 |
| 4 | Sensitivity analysis | **High** | Task 3 |
| 5 | API utility + Decomposer | Medium | Tasks 1, 2 |
| 6 | Investigators + Verifier + Quantifier | Medium | Tasks 2, 3, 4, 5 |
| 7 | Adversarial + Synthesizer | Low | Task 6 |
| 8 | Orchestrator | Medium | All above |
| 9 | Integration test | N/A | Task 8 |

Tasks 3-4 (spreadsheet) and Task 5 (API utility) can be developed in parallel since they have no code dependencies on each other.
