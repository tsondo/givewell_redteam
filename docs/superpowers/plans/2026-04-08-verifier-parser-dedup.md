# Verifier Batch Parser Deduplication — Implementation Plan

> **For Claude Code:** Diagnosis is complete and documented in the Background section below. No further investigation needed before fixing. Use targeted `str_replace` edits, not full file rewrites. No API access required for any task in this plan.

**Goal:** Fix a parser bug in `_parse_batched_verifier_output` that double-counts critiques when the verifier model produces a summary restatement section. Add a regression test. De-duplicate the existing affected result JSONs.

**Architecture:** Minimum-change fix to the parser's match iteration — track seen `critique_idx` values and skip duplicates, keeping the first match (which is the detailed analysis section). Add a regression test against an actual problematic raw response. Apply a one-time data fix to the affected result JSONs without re-running the pipeline.

---

## Background — Diagnosis Already Confirmed

**The bug:** `_parse_batched_verifier_output` in `pipeline/agents.py` (around lines 1017–1035) iterates all regex matches of `## Critique N:` without deduplicating by `critique_idx`. The verifier model produces a structured response shaped like:

```
## Critique 1: <title>
<detailed analysis>

## Critique 2: <title>
<detailed analysis>

## Critique 3: <title>
<detailed analysis>

---

## Critique 1: <title>
<summary restatement with abbreviated verdict>

## Critique 2: <title>
<summary restatement>

## Critique 3: <title>
<summary restatement>
```

The regex `r"(?:^|\n)\s*#{1,3}\s*Critique\s+(\d+)\s*[:\-]"` (`agents.py:1017–1018`) matches all six headers. The loop processes all six matches and produces six `VerifiedCritique` objects from a batch of three originals. Each `original` critique gets paired with both its detailed analysis section and its summary restatement section, both appended to `results`.

**Confirmed by examining raw responses in:**
- `results/vas/03-verifier.md`
- `results/itns/03-verifier.md`

Both show the detailed-analysis-then-summary-restatement structure with the `---` separator.

**Confirmed scope of impact:**
- VAS run: 3 duplicates (Cold Chain Failures, Record-Keeping Inflation, Marginal Supplements)
- ITN run: 2 duplicates (Spatial Clustering, SMC-ITN Interaction)
- Water chlorination: clean (model didn't produce summary restatement)
- SMC: clean (same)

**Why the fix is "first match wins":** The first match per `critique_idx` is the detailed analysis section. The second match is the summary restatement, which by definition contains no information beyond what's already in the detailed section. Taking the first match preserves all evidence and discards only the duplicate.

**Constants confirmed:**
- `VERIFIER_BATCH_SIZE = 3` (`config.py:33`)
- Regex location: `agents.py:1017–1018`
- Match iteration: `agents.py:1027–1035`

---

## File Map

| Action | File | Responsibility |
|--------|------|----------------|
| Modify | `pipeline/agents.py` | Add critique_idx deduplication to `_parse_batched_verifier_output` |
| Create | `tests/fixtures/verifier_batch_with_summary_restatement.txt` | Real problematic raw response, extracted from VAS run |
| Create or Modify | `tests/test_agents.py` | Regression test that loads the fixture and asserts entry count |
| Modify | `results/vas/03-verifier.json` | De-duplicate (backup original first) |
| Modify | `results/vas/04-quantifier.json` | De-duplicate (backup original first) |
| Modify | `results/vas/05-adversarial.json` | De-duplicate (backup original first) |
| Modify | `results/itns/03-verifier.json` | De-duplicate (backup original first) |
| Modify | `results/itns/04-quantifier.json` | De-duplicate (backup original first) |
| Modify | `results/itns/05-adversarial.json` | De-duplicate (backup original first) |

**Files explicitly NOT modified:**
- `results/vas/06-synthesizer.json` and `results/itns/06-synthesizer.json` — narrative format, not entry list
- `results/vas/pipeline-stats.json` and `results/itns/pipeline-stats.json` — must preserve truthful spending record
- `results/water-chlorination/*` and `results/smc/*` — these runs are clean
- `docs/conclusions.md` — separate decision after Tsondo sees corrected numbers

---

### Task 1: Fix the parser

**Files:**
- Modify: `pipeline/agents.py`

- [ ] **Step 1: View the current `_parse_batched_verifier_output` function**

```bash
cd /home/tsondo/projects/givewell_redteam
```

`view` `pipeline/agents.py` lines 1010–1050 to confirm the current state matches the diagnosis. The regex should be at line 1017–1018 and the match iteration loop at 1027–1035.

If line numbers have shifted (e.g., due to recent edits), find the function by name and re-confirm before editing.

- [ ] **Step 2: Add critique_idx deduplication**

Use `str_replace` to modify the loop that processes `matches`. The minimum change tracks seen indices and skips duplicates:

```python
    if len(matches) >= 2 and len(batch) > 1:
        # Multiple sections found — parse each
        seen_indices: set[int] = set()
        for i, m in enumerate(matches):
            critique_idx = int(m.group(1)) - 1
            if critique_idx in seen_indices:
                # Model restated the header in a summary section; skip duplicate
                continue
            seen_indices.add(critique_idx)
            start = m.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(raw)
            section = raw[start:end].strip()

            if 0 <= critique_idx < len(batch):
                result = parse_verifier_output(section, batch[critique_idx])
                results.append(result)
```

The exact `str_replace` should target the existing iteration block. Do not change the regex. Do not refactor anything else in the function. The only additions are the `seen_indices` set declaration and the two-line guard inside the loop.

**Important nuance about `end = matches[i + 1].start()`:** When skipping a duplicate match, the next match's start position is still the boundary for the *previous* (kept) section. But since we've already processed the kept section in an earlier iteration, this is fine — we're discarding the section between the duplicate and the next match anyway. Verify by tracing through the logic mentally before committing.

- [ ] **Step 3: Verify the function still imports and runs**

```bash
python -c "
from pipeline.agents import _parse_batched_verifier_output
print('Import OK')
"
```

---

### Task 2: Create a regression test fixture

**Files:**
- Create: `tests/fixtures/verifier_batch_with_summary_restatement.txt`

- [ ] **Step 1: Locate the problematic batch in the VAS raw output**

`view` `results/vas/03-verifier.md` and find the section containing the Cold Chain Failures / Record-Keeping Inflation / Marginal Supplements batch. The batch should contain a detailed analysis section with three `## Critique N:` headers, a `---` separator, and a summary restatement section with three more `## Critique N:` headers.

Note: `results/vas/03-verifier.md` is a concatenation of all batches, separated by `--- Critique: <title> ---` delimiters. The single batch raw response is the text between two such delimiters that contains all three of Cold Chain, Record-Keeping, and Marginal as `## Critique N:` headers within it.

- [ ] **Step 2: Extract and save the fixture**

Create `tests/fixtures/verifier_batch_with_summary_restatement.txt` containing exactly one batch's raw API response. The fixture should:

- Begin at the first `## Critique 1:` header
- End at the end of the summary restatement (after the `## Critique 3:` summary)
- NOT include the surrounding `--- Critique: <title> ---` delimiters from the concatenated `.md` file
- Preserve all whitespace and formatting exactly as it appeared in the raw response

Verify the fixture by counting `## Critique` matches in it:

```bash
grep -c "^## Critique" tests/fixtures/verifier_batch_with_summary_restatement.txt
```

Expected: 6 (three from the detailed analysis, three from the summary restatement). If you get fewer than 6, the fixture is incomplete or wasn't extracted correctly. **Stop and report.**

- [ ] **Step 3: Create the fixtures directory if needed**

```bash
mkdir -p tests/fixtures
```

---

### Task 3: Add the regression test

**Files:**
- Create or Modify: `tests/test_agents.py`

- [ ] **Step 1: Check if `tests/test_agents.py` exists**

```bash
ls tests/test_agents.py 2>&1
```

If it exists, append the test below. If not, create it with a standard pytest module header.

- [ ] **Step 2: Write the test**

```python
"""Tests for pipeline.agents."""
from pathlib import Path

import pytest

from pipeline.agents import _parse_batched_verifier_output
from pipeline.schemas import CandidateCritique


FIXTURES = Path(__file__).parent / "fixtures"


def _make_critique(title: str) -> CandidateCritique:
    """Construct a minimal CandidateCritique for parser testing."""
    return CandidateCritique(
        thread_name="test_thread",
        title=title,
        hypothesis="test hypothesis",
        mechanism="test mechanism",
        parameters_affected=["test_param"],
        suggested_evidence=["test evidence"],
        estimated_direction="uncertain",
        estimated_magnitude="unknown",
    )


class TestVerifierBatchParserDeduplication:
    """Regression test for the verifier batch parser duplicate bug.

    The verifier model sometimes produces a detailed analysis section
    followed by a "---" separator and a summary restatement that repeats
    each "## Critique N:" header. Without deduplication, the parser
    counts each critique twice. This was discovered in the VAS run
    (3 duplicates) and the ITN run (2 duplicates).
    """

    def test_summary_restatement_not_double_counted(self):
        fixture_path = FIXTURES / "verifier_batch_with_summary_restatement.txt"
        raw_text = fixture_path.read_text()

        # Sanity check: the fixture should contain 6 critique headers
        # (3 detailed + 3 restated). If this fails, the fixture is wrong.
        assert raw_text.count("## Critique") == 6, (
            "Fixture should contain 6 '## Critique' headers "
            "(3 detailed analysis + 3 summary restatement)"
        )

        batch = [
            _make_critique("Cold Chain Failures During Distribution Creating Spotty Potency"),
            _make_critique("Record-Keeping Inflation Due to Performance Incentives"),
            _make_critique("Marginal Supplements Target Higher-Cost Remote Populations"),
        ]

        results = _parse_batched_verifier_output(raw_text, batch)

        assert len(results) == 3, (
            f"Expected 3 parsed entries (one per batch critique), got {len(results)}. "
            f"The parser is double-counting the summary restatement section."
        )

        result_titles = [r.original.title for r in results]
        assert result_titles == [c.title for c in batch], (
            f"Expected results in batch order, got {result_titles}"
        )
```

- [ ] **Step 3: Verify the test passes against the fixed parser**

```bash
python -m pytest tests/test_agents.py::TestVerifierBatchParserDeduplication -v
```

Expected: passes.

- [ ] **Step 4: Verify the test would have caught the bug**

Temporarily revert the parser fix (just the `seen_indices` lines, in memory — do not commit) and re-run the test. It should fail with `Expected 3 parsed entries, got 6`. Then restore the fix.

If the test passes against the unfixed parser, **stop and report** — the fixture isn't triggering the bug correctly and we need to look at it again.

If you don't want to do the temporary revert, you can verify equivalently by adding a one-shot manual check: load the fixture, run the regex against it, count matches, confirm there are 6 — if there are 6 matches in the fixture and the parser returns 3 results, the deduplication is working.

---

### Task 4: De-duplicate the existing result JSONs

**Files:**
- Modify (with backup): `results/vas/03-verifier.json`, `results/vas/04-quantifier.json`, `results/vas/05-adversarial.json`
- Modify (with backup): `results/itns/03-verifier.json`, `results/itns/04-quantifier.json`, `results/itns/05-adversarial.json`

This is a one-time data fix. **Do not re-run the pipeline.**

- [ ] **Step 1: Determine the title field path for each stage**

The verifier output has titles at `entry["original"]["title"]`. The quantifier and adversarial outputs may use different paths. Inspect one entry from each before writing the de-dup script:

```bash
python3 -c "
import json
for run in ['vas', 'itns']:
    for stage in ['03-verifier', '04-quantifier', '05-adversarial']:
        with open(f'results/{run}/{stage}.json') as f:
            data = json.load(f)
        print(f'=== {run}/{stage} ===')
        print(f'  Total entries: {len(data)}')
        print(f'  First entry top-level keys: {list(data[0].keys())[:8]}')
"
```

For the adversarial stage specifically, the title is nested deeper — recall from prior analysis that it lives at `entry["critique"]["critique"]["original"]["title"]`. Verify before writing the de-dup script.

If any stage has a structure that doesn't fit "list of entries with extractable title," **stop and report**.

- [ ] **Step 2: Write and run the de-duplication script**

```python
# Run as a one-shot script, do not save
import json
import shutil
from pathlib import Path

def get_title(entry, stage):
    """Extract the critique title for de-duplication, depending on stage."""
    if stage == "03-verifier":
        return entry["original"]["title"]
    elif stage == "04-quantifier":
        # Verify path against the actual structure inspected in Step 1
        return entry["original"]["title"]  # adjust if needed
    elif stage == "05-adversarial":
        return entry["critique"]["critique"]["original"]["title"]
    raise ValueError(f"Unknown stage: {stage}")

for run in ["vas", "itns"]:
    for stage in ["03-verifier", "04-quantifier", "05-adversarial"]:
        path = Path(f"results/{run}/{stage}.json")
        backup = path.with_suffix(".with-duplicates.json")

        if backup.exists():
            print(f"SKIP {path}: backup already exists at {backup}")
            continue

        shutil.copy(path, backup)

        with open(path) as f:
            data = json.load(f)

        seen = set()
        deduped = []
        for entry in data:
            title = get_title(entry, stage)
            if title in seen:
                continue
            seen.add(title)
            deduped.append(entry)

        with open(path, "w") as f:
            json.dump(deduped, f, indent=2)

        print(f"{run}/{stage}: {len(data)} -> {len(deduped)} entries")
```

Expected output:
```
vas/03-verifier: 31 -> 28 entries
vas/04-quantifier: 31 -> 28 entries
vas/05-adversarial: 31 -> 28 entries
itns/03-verifier: 30 -> 28 entries
itns/04-quantifier: 30 -> 28 entries
itns/05-adversarial: 30 -> 28 entries
```

If any count comes out differently, **stop and report** — something is wrong with the title extraction or the data structure.

- [ ] **Step 3: Verify the de-duplication is consistent across stages**

```bash
python3 -c "
import json
for run in ['vas', 'itns']:
    counts = []
    for stage in ['03-verifier', '04-quantifier', '05-adversarial']:
        with open(f'results/{run}/{stage}.json') as f:
            counts.append(len(json.load(f)))
    print(f'{run}: {counts}')
    assert len(set(counts)) == 1, f'{run}: stage counts differ: {counts}'
print('All stages consistent.')
"
```

Expected: VAS shows `[28, 28, 28]`, ITN shows `[28, 28, 28]`, and prints `All stages consistent.`

---

### Task 5: Run the full test suite

- [ ] **Step 1: Confirm no regressions**

```bash
python -m pytest tests/ -v
```

Expected: all prior tests still pass plus the new `TestVerifierBatchParserDeduplication` test. If anything fails, **stop and report** — do not attempt fixes that go beyond this plan.

---

### Task 6: Commit in three logical steps

- [ ] **Commit 1: Parser fix**

```bash
git add pipeline/agents.py
git commit -m "fix: deduplicate verifier batch parser matches by critique_idx

The verifier model produces detailed analysis followed by a summary
restatement after a '---' separator. The regex matched each
'## Critique N:' header twice, producing 2N parsed entries from a
batch of N critiques.

Discovered during VAS run analysis. Affected VAS (3 duplicates) and
ITN (2 duplicates); water chlorination and SMC runs were clean
because their model responses didn't include the summary section.

Fix takes the first match per critique_idx, which is the detailed
analysis section. The summary restatement contains no new information."
```

- [ ] **Commit 2: Regression test**

```bash
git add tests/fixtures/verifier_batch_with_summary_restatement.txt tests/test_agents.py
git commit -m "test: add regression test for verifier batch parser duplicate bug

Replays an actual problematic raw response from results/vas/03-verifier.md
and asserts the parser produces 3 entries, not 6."
```

- [ ] **Commit 3: De-duplicated result JSONs**

```bash
git add results/vas/03-verifier.json results/vas/04-quantifier.json results/vas/05-adversarial.json
git add results/vas/03-verifier.with-duplicates.json results/vas/04-quantifier.with-duplicates.json results/vas/05-adversarial.with-duplicates.json
git add results/itns/03-verifier.json results/itns/04-quantifier.json results/itns/05-adversarial.json
git add results/itns/03-verifier.with-duplicates.json results/itns/04-quantifier.with-duplicates.json results/itns/05-adversarial.with-duplicates.json
git status  # confirm pipeline-stats.json files are NOT staged
git commit -m "data: deduplicate VAS and ITN result JSONs after parser fix

Removes duplicate entries from the verifier, quantifier, and adversarial
result files for VAS and ITN runs. Originals saved as *.with-duplicates.json
for audit. Pipeline-stats.json files left unchanged to preserve the
truthful spending record. Synthesizer reports left unchanged because
they are narrative, not entry-list, format.

VAS corrected counts: 28 unique critiques across all stages (was 31).
ITN corrected counts: 28 unique critiques across all stages (was 30)."
```

- [ ] **Step 4: Verify the commit history**

```bash
git log --oneline -6
```

Expected: three new commits on top of the prior history, in order: parser fix, regression test, data dedup.

---

## Stop Conditions Requiring Tsondo Input

- Parser line numbers don't match the diagnosis (function may have moved)
- Fixture extraction produces fewer than 6 `## Critique` headers
- Regression test passes against the unfixed parser (means the fixture isn't triggering the bug)
- De-duplication produces unexpected counts (anything other than 28 for VAS or 28 for ITN)
- Any stage's JSON has a structure incompatible with the title extraction approach
- The full test suite has any new failures after the fix

## Things You Should NOT Do

- Re-run any pipeline stages
- Modify `pipeline-stats.json` for either run
- Modify `results/water-chlorination/*` or `results/smc/*` (these runs are clean)
- Modify `results/vas/06-synthesizer.json` or `results/itns/06-synthesizer.json` (narrative format)
- Modify `docs/conclusions.md` (separate decision after Tsondo sees corrected numbers)
- Refactor `_parse_batched_verifier_output` beyond the minimum deduplication fix
- Change the verifier regex
- Change `VERIFIER_BATCH_SIZE` or any other config constant
- Activate the API key (no API access required for any task in this plan)
