# Amendment: Increase MAX_TOKENS_SYNTHESIZER and complete VAS re-run

> Amendment to `2026-04-13-synthesizer-rubric-and-patterns-fix.md`. The 8192 max_tokens limit truncated the regenerated VAS synthesizer output mid-Resolved Negatives, omitting Meta-Observations entirely. The "How to Read This Report" addition pushed output past the previous ceiling. The original plan's "no code changes" constraint was a simplifying assumption, not a principle — it only held while the prompt-only change fit the existing token budget. A one-line config change is the correct path. This project commits directly to main; do not create branches.

## Context

The prior run completed at $1.06 cost but produced a truncated artifact (missing Meta-Observations section, incomplete Resolved Negatives). The runner correctly stopped before committing. Pre-rubric backups are intact at `results/vas/06-synthesizer.pre-rubric.{json,md}`.

Sizing: 8192 was adequate before. The rubric explainer adds ~200 tokens. A bump to 12288 provides ~50% headroom and prevents recurrence as the report naturally grows. Cost impact: Opus output at $75/million tokens → ~$0.31 worst case additional per run. Negligible.

## File Map

| Action | File | Change |
|--------|------|------|
| Modify | `pipeline/config.py` | `MAX_TOKENS_SYNTHESIZER` from 8192 to 12288 |
| Re-run | `results/vas/06-synthesizer.{json,md}` | Regenerated complete artifact |

---

## Task 4: Raise the synthesizer token limit

**Files:**
- Modify: `pipeline/config.py`

- [ ] **Step 1: Update the constant**

Find `MAX_TOKENS_SYNTHESIZER: int = 8192` and change to `MAX_TOKENS_SYNTHESIZER: int = 12288`.

- [ ] **Step 2: Verify no other callers assume the old value**

Run `grep -r MAX_TOKENS_SYNTHESIZER pipeline/ tests/` and confirm only the synthesizer call site uses it. If tests reference the value directly, update them to match.

- [ ] **Step 3: Commit the config change**

```
chore: increase MAX_TOKENS_SYNTHESIZER from 8192 to 12288

The 8192 limit truncated the VAS synthesizer output mid-Resolved
Negatives after the "How to Read This Report" section addition. 12288
provides ~50% headroom while staying well within Opus's output capacity.

Cost impact: ~$0.31/run worst case (4096 extra output tokens at Opus
pricing). Negligible relative to the ~$0.50 baseline synthesizer call.
```

Use Co-Authored-By trailers as standard.

---

## Task 5: Re-run VAS synthesizer and verify full completion

This task involves ~$0.50–0.80 of API spend. API key should still be active from the prior run.

- [ ] **Step 1: State of disk before re-running**

The partial output currently at `results/vas/06-synthesizer.{json,md}` is truncated and should NOT be committed. Either overwrite it with the pre-rubric backup temporarily OR proceed directly to re-running (which will overwrite). Either is fine — the re-run will replace whatever's there.

- [ ] **Step 2: Invoke the resume**

```
python -m pipeline.run_pipeline vas --resume-from synthesizer
```

Expected runtime: ~45-90 seconds. Expected cost: ~$0.50–0.80 with the higher token limit. Hard stop: $2 total cost.

- [ ] **Step 3: Verify full completion**

Load the new `results/vas/06-synthesizer.md` and confirm ALL of the following:

**From the original plan (still required):**
1. The "How to Read This Report" section is present and matches the verbatim text from the prompt (no paraphrasing)
2. The section appears after "Pipeline Summary" and before "Critical Findings"
3. The Debate Quality Audit's Patterns subsection labels combined vs per-side counts (spot-check: any specific failure mode count referenced in the prose should be explicitly tagged as either combined or per-side)

**New completeness checks for this re-run:**
4. `## Meta-Observations` section is present at the end of the document
5. Resolved Negatives section is complete (all expected entries present, none cut off mid-sentence)
6. The raw markdown ends cleanly (the file does not terminate mid-sentence or mid-section)
7. All structural sections accounted for: Pipeline Summary, How to Read This Report, Critical Findings, Significant Findings, Minor Findings, Comparison with GiveWell's AI Output, Debate Quality Audit, Conditional Findings, Open Questions, Resolved Negatives, Meta-Observations

If the output is still truncated at 12288 tokens, **stop and report** — the problem is larger than the token limit and needs investigation (possibly the synthesizer generating unnecessarily verbose content, or the prompt needing tightening rather than more budget).

- [ ] **Step 4: Commit the regenerated artifact**

If all checks pass, commit the regenerated files:

```
data: regenerate VAS synthesizer with rubric explainer and complete output

Re-run after raising MAX_TOKENS_SYNTHESIZER to 12288. The previous
attempt at 8192 truncated mid-Resolved Negatives. This run completes
all sections including Meta-Observations.

Cost: ~$0.XX. Upstream stages 1-5b unchanged.

Pre-rubric backup retained locally as *.pre-rubric.* for comparison.
```

Replace `$0.XX` with the actual cost from `pipeline-stats.json`.

---

## Stop Conditions Requiring Tsondo Input

- Any existing test fails after the config update (unlikely — tests rarely assert on this constant)
- The verbatim rubric text appears paraphrased in the regenerated output
- The Patterns subsection still conflates combined vs per-side counts
- Output still truncates at 12288 tokens (investigate content bloat, not budget)
- Cost exceeds $2 (well above the $0.80 upper expectation)

## Things You Should NOT Do

- Re-run any upstream stages (adversarial, linker) — they're unchanged
- Modify the judge prompt — that's a separate plan awaiting Mikyo's taxonomy response
- Modify `pipeline/agents.py` or `pipeline/run_pipeline.py` — only `pipeline/config.py`
- Touch artifacts for water-chlorination, ITN, or SMC
- Commit the `*.pre-rubric.*` backup files
- Create branches — commit directly to main as before
