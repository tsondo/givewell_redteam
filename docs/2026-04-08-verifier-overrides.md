# Per-Intervention Verifier Overrides — Implementation Plan

> **For Claude Code:** Use targeted `str_replace` edits, not full file rewrites. No API access required for any task in this plan; the API key can stay deactivated throughout.

**Goal:** Add a per-intervention override mechanism for Verifier settings (allowed domains, max searches, max tokens, cost warning threshold), and configure VAS-specific overrides that prioritize evidence quality over cost.

**Architecture:** A new `INTERVENTION_VERIFIER_OVERRIDES` dict in `config.py` plus a `get_verifier_settings(intervention)` helper that merges overrides with module-level defaults. `run_verifier` in `agents.py` calls the helper instead of reading the module constants directly. The cost-warning threshold is set on `PipelineStats` at run start so `call_api` reads it from the stats object (already in scope at every call site) rather than from a module constant. Defaults remain unchanged, so water/itns/smc behavior is identical.

---

## File Map

| Action | File | Responsibility |
|--------|------|----------------|
| Modify | `pipeline/config.py` | Add override dict, helper function |
| Modify | `pipeline/schemas.py` | Add `cost_warning_threshold` field to `PipelineStats` |
| Modify | `pipeline/agents.py` | Replace direct constant reads in `run_verifier` with helper; update `call_api` cost check to use `stats.cost_warning_threshold` |
| Modify | `pipeline/run_pipeline.py` | Set `stats.cost_warning_threshold` from intervention settings at run start |
| Create | `tests/test_config.py` | Test defaults, VAS overrides, and PipelineStats threshold wiring |

---

### Task 1: Add override dict and helper to config.py

**Files:**
- Modify: `pipeline/config.py`

- [ ] **Step 1: Add the override dict and helper function**

Use `str_replace` to insert the following block immediately after the `VERIFIER_ALLOWED_DOMAINS` list definition (before the `# Cost thresholds` section):

```python

# ---------------------------------------------------------------------------
# Per-intervention verifier overrides
# ---------------------------------------------------------------------------
# Each intervention may override any of: allowed_domains, max_searches,
# max_tokens, cost_warning. Keys not present fall back to the module-level
# defaults above. This exists because different interventions need different
# evidence-quality / cost trade-offs (e.g., VAS depends on DHS prevalence
# data and grantee implementation reports that aren't on the default list).

INTERVENTION_VERIFIER_OVERRIDES: dict[str, dict[str, Any]] = {
    "vas": {
        "allowed_domains": [
            # Defaults retained
            "givewell.org",
            "who.int",
            "ncbi.nlm.nih.gov",
            "pubmed.ncbi.nlm.nih.gov",
            "scholar.google.com",
            "thelancet.com",
            "bmj.com",
            "nature.com",
            "cochranelibrary.com",
            "worldbank.org",
            "unicef.org",
            # Tier 1 — prevalence and implementation data
            "dhsprogram.com",
            "childmortality.org",
            "healthdata.org",
            "ghdx.healthdata.org",
            "helenkellerintl.org",
            "nutritionintl.org",
            # Tier 2 — expanded biomedical access
            "europepmc.org",
            "nejm.org",
            "ajcn.nutrition.org",
            "journals.plos.org",
            "micronutrient.org",
            "micronutrientforum.org",
            # Tier 3 — structural debate sources
            "lshtm.ac.uk",
            "jhsph.edu",
            "gainhealth.org",
            "advancingnutrition.org",
        ],
        "max_searches": 8,
        "max_tokens": 6144,
        "cost_warning": 40.0,
    },
}


def get_verifier_settings(intervention: str) -> dict[str, Any]:
    """Return verifier settings for an intervention, merging overrides with defaults.

    Always returns a dict with all four keys populated. Interventions without
    an override entry receive the module-level defaults unchanged.
    """
    overrides = INTERVENTION_VERIFIER_OVERRIDES.get(intervention, {})
    return {
        "allowed_domains": overrides.get("allowed_domains", VERIFIER_ALLOWED_DOMAINS),
        "max_searches": overrides.get("max_searches", VERIFIER_MAX_SEARCHES),
        "max_tokens": overrides.get("max_tokens", MAX_TOKENS_VERIFIER),
        "cost_warning": overrides.get("cost_warning", COST_WARNING_PER_INTERVENTION),
    }
```

- [ ] **Step 2: Add `Any` import if needed**

```bash
grep -n "from typing" pipeline/config.py
```

If `Any` is not already imported, add it. If there is no typing import at all, add `from typing import Any` after the existing `from pathlib import Path` line.

- [ ] **Step 3: Verify config still imports cleanly**

```bash
python -c "
from pipeline.config import get_verifier_settings, INTERVENTION_VERIFIER_OVERRIDES
defaults = get_verifier_settings('itns')
vas = get_verifier_settings('vas')
print('itns max_searches:', defaults['max_searches'])
print('vas max_searches:', vas['max_searches'])
print('vas allowed domains count:', len(vas['allowed_domains']))
print('vas cost_warning:', vas['cost_warning'])
assert defaults['max_searches'] == 5
assert vas['max_searches'] == 8
assert vas['cost_warning'] == 40.0
assert 'dhsprogram.com' in vas['allowed_domains']
assert 'dhsprogram.com' not in defaults['allowed_domains']
print('OK')
"
```

Expected: prints values and `OK`. If anything fails, fix before continuing.

---

### Task 2: Add `cost_warning_threshold` to PipelineStats

**Files:**
- Modify: `pipeline/schemas.py`

- [ ] **Step 1: Add the field to PipelineStats**

In `pipeline/schemas.py`, add a `cost_warning_threshold` field to the `PipelineStats` dataclass. Insert it after the `stage_costs` field (line 185):

```python
    cost_warning_threshold: float = 15.0  # default; overridden per-intervention at run start
```

The default value `15.0` matches `COST_WARNING_PER_INTERVENTION` in config.py. We hardcode it here rather than importing from config to avoid a circular dependency (schemas should not depend on config).

- [ ] **Step 2: Verify schemas still import cleanly**

```bash
python -c "
from pipeline.schemas import PipelineStats
s = PipelineStats()
assert s.cost_warning_threshold == 15.0
print('OK')
"
```

---

### Task 3: Wire helper into `run_verifier` and update `call_api` cost check

**Files:**
- Modify: `pipeline/agents.py`

- [ ] **Step 1: Update the import block**

Add `get_verifier_settings` to the existing `from pipeline.config import (...)` block. Add it alphabetically — between `COST_WARNING_PER_INTERVENTION` and `MAX_RETRIES`. (Keep `COST_WARNING_PER_INTERVENTION` in the import — it may still be referenced elsewhere, and the import is harmless.)

- [ ] **Step 2: Replace the web_search_tool construction in `run_verifier`**

Replace lines 1067-1072:

```python
    web_search_tool: dict[str, Any] = {
        "type": "web_search_20250305",
        "name": "web_search",
        "max_uses": VERIFIER_MAX_SEARCHES,
        "allowed_domains": VERIFIER_ALLOWED_DOMAINS,
    }
```

with:

```python
    settings = get_verifier_settings(intervention)
    web_search_tool: dict[str, Any] = {
        "type": "web_search_20250305",
        "name": "web_search",
        "max_uses": settings["max_searches"],
        "allowed_domains": settings["allowed_domains"],
    }
```

- [ ] **Step 3: Replace `MAX_TOKENS_VERIFIER` in the verifier call_api invocation**

Replace line 1106:

```python
            max_tokens=MAX_TOKENS_VERIFIER * len(batch),
```

with:

```python
            max_tokens=settings["max_tokens"] * len(batch),
```

The `* len(batch)` scaling is intentional — 6144 is the per-critique unit, same as 4096 was before.

- [ ] **Step 4: Update the cost-warning check in `call_api` to use `stats.cost_warning_threshold`**

Replace lines 99-104:

```python
            if stats.total_cost > COST_WARNING_PER_INTERVENTION:
                logger.warning(
                    "Cumulative cost $%.2f exceeds warning threshold $%.2f",
                    stats.total_cost,
                    COST_WARNING_PER_INTERVENTION,
                )
```

with:

```python
            if stats.total_cost > stats.cost_warning_threshold:
                logger.warning(
                    "Cumulative cost $%.2f exceeds warning threshold $%.2f",
                    stats.total_cost,
                    stats.cost_warning_threshold,
                )
```

This is a single-line semantic change. No signature change to `call_api`, no caller changes. Every stage now reads the threshold from the stats object that's already in scope.

- [ ] **Step 5: Verify agents.py still imports cleanly**

```bash
python -c "from pipeline.agents import run_verifier; print('OK')"
```

---

### Task 4: Set threshold at run start in run_pipeline.py

**Files:**
- Modify: `pipeline/run_pipeline.py`

- [ ] **Step 1: Add import**

Add `get_verifier_settings` to the imports from `pipeline.config`. The existing import block (lines 10-16) becomes:

```python
from pipeline.config import (
    COST_WARNING_PER_INTERVENTION,
    DATA_DIR,
    INTERVENTION_URLS,
    RESULTS_DIR,
    get_verifier_settings,
)
```

- [ ] **Step 2: Set the threshold after stats is created**

After line 110 (`stats = PipelineStats()`), add:

```python
    stats.cost_warning_threshold = get_verifier_settings(intervention)["cost_warning"]
```

- [ ] **Step 3: Verify the wiring**

```bash
python -c "
from pipeline.config import get_verifier_settings
from pipeline.schemas import PipelineStats
stats = PipelineStats()
stats.cost_warning_threshold = get_verifier_settings('vas')['cost_warning']
assert stats.cost_warning_threshold == 40.0
stats2 = PipelineStats()
stats2.cost_warning_threshold = get_verifier_settings('itns')['cost_warning']
assert stats2.cost_warning_threshold == 15.0
print('OK')
"
```

---

### Task 5: Add tests for the override mechanism

**Files:**
- Create: `tests/test_config.py`

- [ ] **Step 1: Create the test file**

```python
"""Tests for per-intervention verifier overrides."""
from __future__ import annotations

from pipeline.config import (
    COST_WARNING_PER_INTERVENTION,
    MAX_TOKENS_VERIFIER,
    VERIFIER_ALLOWED_DOMAINS,
    VERIFIER_MAX_SEARCHES,
    get_verifier_settings,
)
from pipeline.schemas import PipelineStats


class TestVerifierSettingsDefaults:
    """Interventions without overrides receive module-level defaults."""

    def test_water_chlorination_uses_defaults(self):
        s = get_verifier_settings("water-chlorination")
        assert s["max_searches"] == VERIFIER_MAX_SEARCHES
        assert s["max_tokens"] == MAX_TOKENS_VERIFIER
        assert s["cost_warning"] == COST_WARNING_PER_INTERVENTION
        assert s["allowed_domains"] == VERIFIER_ALLOWED_DOMAINS

    def test_itns_uses_defaults(self):
        s = get_verifier_settings("itns")
        assert s["max_searches"] == VERIFIER_MAX_SEARCHES
        assert s["allowed_domains"] == VERIFIER_ALLOWED_DOMAINS

    def test_smc_uses_defaults(self):
        s = get_verifier_settings("smc")
        assert s["max_searches"] == VERIFIER_MAX_SEARCHES

    def test_unknown_intervention_uses_defaults(self):
        s = get_verifier_settings("nonexistent")
        assert s["max_searches"] == VERIFIER_MAX_SEARCHES
        assert s["cost_warning"] == COST_WARNING_PER_INTERVENTION


class TestVerifierSettingsVAS:
    """VAS overrides apply correctly."""

    def test_vas_max_searches_raised(self):
        assert get_verifier_settings("vas")["max_searches"] == 8

    def test_vas_max_tokens_raised(self):
        assert get_verifier_settings("vas")["max_tokens"] == 6144

    def test_vas_cost_warning_raised(self):
        assert get_verifier_settings("vas")["cost_warning"] == 40.0

    def test_vas_includes_dhs(self):
        assert "dhsprogram.com" in get_verifier_settings("vas")["allowed_domains"]

    def test_vas_includes_grantees(self):
        domains = get_verifier_settings("vas")["allowed_domains"]
        assert "helenkellerintl.org" in domains
        assert "nutritionintl.org" in domains

    def test_vas_includes_ihme(self):
        domains = get_verifier_settings("vas")["allowed_domains"]
        assert "healthdata.org" in domains

    def test_vas_retains_default_domains(self):
        """Override should be additive, not replacement."""
        domains = get_verifier_settings("vas")["allowed_domains"]
        for default_domain in VERIFIER_ALLOWED_DOMAINS:
            assert default_domain in domains, f"Lost default: {default_domain}"


class TestPipelineStatsCostThreshold:
    """Cost warning threshold is set per-intervention via PipelineStats."""

    def test_default_threshold(self):
        stats = PipelineStats()
        assert stats.cost_warning_threshold == 15.0

    def test_vas_threshold_from_settings(self):
        stats = PipelineStats()
        stats.cost_warning_threshold = get_verifier_settings("vas")["cost_warning"]
        assert stats.cost_warning_threshold == 40.0

    def test_itns_threshold_unchanged(self):
        stats = PipelineStats()
        stats.cost_warning_threshold = get_verifier_settings("itns")["cost_warning"]
        assert stats.cost_warning_threshold == COST_WARNING_PER_INTERVENTION
```

- [ ] **Step 2: Run the new tests**

```bash
python -m pytest tests/test_config.py -v
```

Expected: all tests pass.

---

### Task 6: Run the full test suite to check no regressions

- [ ] **Step 1: Run everything**

```bash
python -m pytest tests/ -v
```

Expected: all existing tests still pass plus the new config tests. If anything fails, stop and report the failure — do not attempt fixes that go beyond this plan.

- [ ] **Step 2: Spot-check that the verifier wiring works end-to-end (no API call)**

```bash
python -c "
from pipeline.agents import run_verifier
from pipeline.config import get_verifier_settings
import inspect
src = inspect.getsource(run_verifier)
assert 'get_verifier_settings(intervention)' in src
assert 'settings[\"max_searches\"]' in src or \"settings['max_searches']\" in src
assert 'settings[\"allowed_domains\"]' in src or \"settings['allowed_domains']\" in src
print('run_verifier wiring confirmed')

from pipeline.agents import call_api
src2 = inspect.getsource(call_api)
assert 'stats.cost_warning_threshold' in src2
assert 'COST_WARNING_PER_INTERVENTION' not in src2
print('call_api cost-check wiring confirmed')
"
```

---

### Task 7: Commit

- [ ] **Step 1: Stage and commit**

```bash
git add pipeline/config.py pipeline/schemas.py pipeline/agents.py pipeline/run_pipeline.py tests/test_config.py
git status  # confirm only these five files are staged
git commit -m "feat: per-intervention verifier overrides; VAS quality config

Adds INTERVENTION_VERIFIER_OVERRIDES + get_verifier_settings() helper.
run_verifier now reads allowed_domains, max_searches, and max_tokens
per intervention rather than from module constants directly.

Cost-warning threshold moves from module constant to PipelineStats field,
set per-intervention at run start. call_api reads stats.cost_warning_threshold
instead of COST_WARNING_PER_INTERVENTION directly. Zero signature changes.

VAS overrides expand the allowlist to cover DHS prevalence data, IHME
mortality estimates, HKI/NI grantee reports, and the structural-debate
literature (Tier 1 + 2 + 3). max_searches raised 5 -> 8, max_tokens
raised 4096 -> 6144, cost_warning raised 15 -> 40 to reflect the
quality-over-cost trade-off for this intervention.

Defaults unchanged for water-chlorination, itns, smc."
```

---

## Notes for Claude Code

- The `COST_WARNING_PER_INTERVENTION = 15.0` constant must remain in `config.py` — it's the default value used by `get_verifier_settings` for interventions without overrides.
- Do NOT import `COST_WARNING_PER_INTERVENTION` in `schemas.py` — use the hardcoded `15.0` default to avoid a circular dependency.
- All edits should be `str_replace`, not file rewrites.
- No `.env` activation needed at any point in this plan.
