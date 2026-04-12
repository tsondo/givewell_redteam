# Persist Rejected Critiques and Surface Them Honestly in the Synthesizer

> **For Claude Code:** Use targeted `str_replace` edits, not full file rewrites. No API access required for any task in this plan unless backfill is opted into (Task 5).

**Goal:** Make the verifier's rejected critiques first-class artifacts in two ways: (a) persist them to disk with full reasoning so future analysis has visibility into rejection rates and patterns, and (b) feed them to the synthesizer so the report's "Ungrounded Hypotheses" section reflects what the pipeline actually rejected rather than what the synthesizer creatively generated at write time.

**Architecture:** Three coupled changes. The verifier writes a new `03-verifier-rejected.json` alongside the existing filtered file. The orchestrator loads both and passes them to the synthesizer as separate inputs. The synthesizer prompt is rewritten to populate two new sections (Open Questions, Resolved Negatives) *only* from the rejected_critiques input, with explicit prohibition on creative generation.

---

## Background

An investigation today (`docs/superpowers/plans/2026-04-09-dropped-critiques-investigation.md` if saved, otherwise see chat history) confirmed:

- The verifier issues explicit verdicts including UNVERIFIABLE and REJECTED, with substantive reasoning.
- The verdict filter at `pipeline/agents.py:1128` correctly drops these from `03-verifier.json` so downstream stages (quantifier, adversarial) don't process them.
- The rejected critiques are visible only in `03-verifier.md` (the raw API response file) and have no structured representation anywhere.
- The synthesizer's "Ungrounded Hypotheses Worth Investigating" section is generated creatively at synthesis time, with **zero exact-title overlap** with actually-rejected critiques across all four runs (water-chlorination, ITN, SMC, VAS).
- The verifier rejection mechanism is calibrated and working — the visibility problem is downstream, not upstream.

This plan does NOT change the verifier's rejection logic. It changes only what gets persisted and how the synthesizer consumes it.

## Epistemic categories

The two verdict types map to two different epistemic states and deserve separate sections in the synthesizer report:

- **UNVERIFIABLE** → "Open Questions" — the pipeline couldn't find evidence either way. These are legitimately worth further investigation because the question is open.
- **REJECTED** → "Resolved Negatives" — the pipeline found contradicting evidence. These are NOT worth further investigation because the verifier already answered the question; they're useful as a record of "your AI flagged this but the evidence shows it's wrong."

Conflating these is the kind of failure mode the multi-agent architecture exists to prevent.

---

## File Map

| Action | File | Responsibility |
|--------|------|----------------|
| Modify | `pipeline/agents.py` | Persist rejected critiques in `run_verifier`; update return signature |
| Modify | `pipeline/run_pipeline.py` | Load `03-verifier-rejected.json` and pass to synthesizer |
| Modify | `pipeline/agents.py` | Update `run_synthesizer` signature to accept rejected critiques |
| Modify | `prompts/synthesizer.md` | Replace "Ungrounded Hypotheses" section with two sections; forbid creative generation |
| Modify | `tests/test_agents.py` | Add tests for verifier persistence and synthesizer input handling |

---

### Task 1: Persist rejected critiques in `run_verifier`

**Files:**
- Modify: `pipeline/agents.py`

- [ ] **Step 1: Locate the verdict filter**

`view` `pipeline/agents.py` and find the section in `run_verifier` (around line 1128 per the investigation findings) that filters by verdict. Confirm the exact filter logic — it should be checking `verdict in ("verified", "partially_verified")` or equivalent.

If the line number has shifted or the filter logic looks different, **stop and report** before continuing.

- [ ] **Step 2: Capture the rejected critiques separately**

Modify the filter loop to collect both kept and rejected critiques. The rejected list should preserve the full `VerifiedCritique` (or whatever schema is in use) including the verdict, evidence found, evidence strength, counter-evidence, and any reasoning fields the parser already extracts. Do NOT strip any fields — the whole point is to make these auditable.

The minimum-change pattern is something like:

```python
verified: list[VerifiedCritique] = []
rejected: list[VerifiedCritique] = []
# ... inside the existing loop that processes parsed results ...
for result in parsed_results:
    if result.verdict in ("verified", "partially_verified"):
        verified.append(result)
    else:
        rejected.append(result)
```

- [ ] **Step 3: Save the rejected critiques to disk**

The verifier currently saves `03-verifier.json` and `03-verifier.md` to `RESULTS_DIR / intervention /`. Add a parallel save for `03-verifier-rejected.json` containing the rejected list. Use the same JSON serialization the existing save uses (likely `dataclasses.asdict` or a similar pattern).

Do NOT add a `.md` version of the rejected file. The JSON is sufficient; the raw text is already in `03-verifier.md`.

- [ ] **Step 4: Update the function return**

`run_verifier` currently returns `(verified, raw)` per the project knowledge I saw earlier. Change it to return `(verified, rejected, raw)` so the orchestrator can pass the rejected list to the synthesizer without re-reading the JSON file.

This is a breaking signature change. The only caller is `run_pipeline.py`, which Task 2 updates.

- [ ] **Step 5: Verify the verifier still imports and the existing tests still pass**

Run the test suite. Existing tests should continue to pass. If any test breaks because it called `run_verifier` and expected a 2-tuple, **stop and report** — there may be a caller I didn't anticipate.

---

### Task 2: Load and pass rejected critiques in the orchestrator

**Files:**
- Modify: `pipeline/run_pipeline.py`

- [ ] **Step 1: Update the verifier call site**

Find where `run_pipeline.py` calls `run_verifier` and unpacks its return value. Update to unpack three values instead of two:

```python
verified, rejected, raw = run_verifier(...)
```

- [ ] **Step 2: Update the synthesizer call site**

Find where the orchestrator calls `run_synthesizer` (or whatever the actual function name is). The synthesizer currently receives the surviving critiques from stage 5 (adversarial). Add the rejected critiques as a new parameter.

If the orchestrator currently re-reads files between stages rather than passing return values directly, then the cleanest path is to read `03-verifier-rejected.json` from disk at synthesizer-call time, the same way it reads other intermediate stage outputs. Match the existing pattern in the file rather than introducing a new one.

- [ ] **Step 3: Verify the orchestrator still imports**

Confirm `pipeline.run_pipeline` imports without error. Don't run the pipeline.

---

### Task 3: Update the synthesizer function and prompt

**Files:**
- Modify: `pipeline/agents.py` (the `run_synthesizer` function)
- Modify: `prompts/synthesizer.md`

- [ ] **Step 1: Update `run_synthesizer` signature**

The function should accept `rejected_critiques` as a new parameter alongside its existing inputs. Inside the function, the user message construction needs to include the rejected critiques as a clearly-labeled separate section. Suggested format:

```
## Surviving Critiques (from adversarial stage)
[existing format unchanged]

## Rejected Critiques (from verifier — DO NOT generate new entries)

### Verdict: UNVERIFIABLE (no evidence found either way)
[for each rejected critique with verdict=UNVERIFIABLE, include:
 - title
 - hypothesis
 - mechanism
 - what the verifier searched for
 - the verifier's reasoning for marking it unverifiable]

### Verdict: REJECTED (contradicted by evidence)
[for each rejected critique with verdict=REJECTED, include:
 - title
 - hypothesis
 - mechanism
 - the contradicting evidence the verifier found
 - the verifier's reasoning]
```

If there are zero rejected critiques in either category, write `(none)` rather than omitting the section.

- [ ] **Step 2: Rewrite the synthesizer prompt**

Find the current "Ungrounded Hypotheses Worth Investigating" section in `prompts/synthesizer.md` and replace it with the following:

```markdown
## Open Questions (from rejected_critiques input only)

For each critique in the input section "Verdict: UNVERIFIABLE", produce
one entry in this format:

### [Title from input]
**Hypothesis:** [hypothesis from input]
**Why the verifier couldn't ground it:** [verifier's reasoning from input]
**Why it's still worth investigating:** [one sentence on what makes this
an open question rather than a closed one]

CRITICAL RULES FOR THIS SECTION:
- ONLY use entries from the "Verdict: UNVERIFIABLE" input section.
- DO NOT generate new entries from your own reading of the surviving
  critiques.
- DO NOT combine, summarize, or paraphrase across multiple input entries.
- If the input section is empty, write "(none — all hypotheses were
  either grounded or contradicted)" and move on.

## Resolved Negatives (from rejected_critiques input only)

For each critique in the input section "Verdict: REJECTED", produce one
entry in this format:

### [Title from input]
**Hypothesis:** [hypothesis from input]
**Contradicting evidence:** [verifier's evidence from input]
**Why this matters for GiveWell:** [one sentence on the value of knowing
this hypothesis was tested and found wanting]

CRITICAL RULES FOR THIS SECTION:
- ONLY use entries from the "Verdict: REJECTED" input section.
- DO NOT generate new entries.
- If the input section is empty, write "(none)".
```

The CRITICAL RULES blocks are deliberately verbose because the prior synthesizer behavior was to generate creatively. The prompt needs to be unambiguous that this is forbidden.

- [ ] **Step 3: Verify the prompt file is well-formed**

Read it back and confirm the markdown structure is intact (no broken headers, no orphaned sections).

---

### Task 4: Add tests

**Files:**
- Modify: `tests/test_agents.py`

- [ ] **Step 1: Test that `run_verifier` separates verdicts correctly**

Construct a test that calls `_parse_batched_verifier_output` (or whichever function does the parsing) with a stub raw response containing four critiques: one verified, one partially_verified, one unverifiable, one rejected. Assert that after the verdict filter, the verified list has 2 entries and the rejected list has 2 entries.

Use a real raw response format — base it on the actual structure in `results/vas/03-verifier.md` rather than inventing a format.

If the parser/filter logic is currently entangled with API calls and can't be tested in isolation, **stop and report**. The fix in that case is to extract a pure function for the filter logic, but that's out of scope for this plan and Tsondo should decide.

- [ ] **Step 2: Test that the synthesizer prompt construction includes rejected critiques**

Construct a test that calls the synthesizer's user-message-building code (likely a helper function within `run_synthesizer` — extract it if needed for testability) with a fake list of surviving critiques and a fake list of rejected critiques. Assert that the resulting message string contains:

- A section header matching "Rejected Critiques"
- A subheader matching "Verdict: UNVERIFIABLE"
- A subheader matching "Verdict: REJECTED"
- The titles of the rejected critiques

This is a contract test, not a behavior test — we're not calling the API. We're confirming that the rejected data flows into the prompt at all.

- [ ] **Step 3: Run the full test suite**

All prior tests should still pass. New tests should pass. If anything fails, **stop and report**.

---

### Task 5: Backfill prior runs (separate decision — DO NOT START without confirming with Tsondo)

This task is OPTIONAL and bounded. Do not begin until Tsondo has explicitly said "yes, do the backfill."

The four prior runs (water-chlorination, ITN, SMC, VAS) all have rejected critiques in their `03-verifier.md` files but no structured `03-verifier-rejected.json`. A backfill script could parse the raw .md files and reconstruct the rejected lists.

**Reasons to do it:**
- The conclusions doc could then report accurate per-run rejection counts (currently it can only report post-filter survival rates).
- The VAS synthesizer report could be regenerated yet again with the correct Open Questions / Resolved Negatives sections (currently it has the fabricated three).
- It would let you compute the actual verdict distribution across the project: "across 4 runs and 122 candidate critiques, the verifier produced X verified, Y partially_verified, Z unverifiable, W rejected" — which is the kind of number that strengthens the writeup to Brendan.

**Reasons NOT to do it:**
- Re-parsing `.md` files is fragile and may produce slightly different structure than a fresh run would.
- Regenerating the VAS synthesizer report a second time means the canonical report has shifted twice in two days, which is awkward.
- The chlorination report is already distributed; backfilling won't change it.

**My recommendation if asked:** Do the backfill for visibility (so the conclusions doc has accurate numbers), but do NOT regenerate any synthesizer reports. The structured rejected data is useful for analysis and writeups even without re-running synthesis.

If Tsondo says yes, the work is:

1. Write a one-shot script that parses each `results/<run>/03-verifier.md`, extracts rejected critique entries with their verdicts and reasoning, and writes `results/<run>/03-verifier-rejected.json`.
2. Verify the counts are sensible (rejected count + verified count = total in `02-investigators.json` minus any drops from earlier stages).
3. Commit as a one-time data fix with a clear message explaining the source.

**Stop and ask Tsondo before starting Task 5.**

---

### Task 6: Commit

Three logical commits, in order:

- [ ] **Commit 1: Verifier persistence**

Stages: `pipeline/agents.py` (verifier changes only — not the synthesizer changes), `tests/test_agents.py` (verifier persistence test only).

Commit message should explain: the verifier already issues UNVERIFIABLE and REJECTED verdicts with reasoning, but they were only visible in raw .md files. This persists them to a structured `03-verifier-rejected.json` so future analysis has visibility into pipeline calibration. Downstream stages still consume only the filtered `03-verifier.json` — no behavior change for quantifier or adversarial. Note that this is the first half of a two-commit fix.

- [ ] **Commit 2: Synthesizer consumption**

Stages: `pipeline/agents.py` (synthesizer changes), `pipeline/run_pipeline.py`, `prompts/synthesizer.md`, `tests/test_agents.py` (synthesizer test).

Commit message should explain: investigation revealed the synthesizer was generating "Ungrounded Hypotheses" entries creatively at write time, with zero overlap with actually-rejected critiques across all four prior runs. This fixes that by passing the rejected critiques as explicit input and rewriting the prompt to populate two new sections (Open Questions for UNVERIFIABLE, Resolved Negatives for REJECTED) only from input data. References the investigation findings.

- [ ] **Commit 3: Backfill data (only if Task 5 was approved and executed)**

Stages: the new `03-verifier-rejected.json` files for each prior run, plus the one-shot script if it's worth keeping.

---

## Stop Conditions Requiring Tsondo Input

- Verifier filter line numbers don't match the investigation findings (function may have moved)
- Filter logic in `run_verifier` is more complex than a simple verdict check
- A test breaks because of an unexpected caller of `run_verifier`
- The parser/filter logic can't be tested in isolation (would require extracting a pure function)
- Backfill (Task 5) — explicitly waits for go-ahead

## Things You Should NOT Do

- Change the verifier's rejection criteria or verdict logic — only change what gets persisted
- Modify the quantifier or adversarial stages — they still consume only `03-verifier.json`
- Modify the existing `03-verifier.json` schema or contents
- Modify any existing synthesizer report files (`results/*/06-synthesizer.{md,json}`)
- Re-run any pipeline stages
- Start Task 5 without explicit approval
- Activate the API key (no API access required for Tasks 1–4)
