# Synthesizer prompt fixes + VAS re-run from synthesizer

> Two targeted prompt updates to `prompts/synthesizer.md`, followed by a single-stage re-run (`--resume-from synthesizer`) to regenerate `results/vas/06-synthesizer.{json,md}` with the improvements. No API spend until the prompt changes are committed and tested. This project commits directly to main; do not create branches.

## Context

Mikyo's 11 April review surfaced two synthesizer output issues that don't block correctness but do block clarity for external readers:

1. **Label opacity.** The "strong / moderate / weak" labels in the report are meaningful internally (see `prompts/adversarial-judge.md` for the rubric) but the synthesizer never tells the reader what they mean. For a domain-sophisticated reader encountering the report for the first time, this creates unnecessary friction.

2. **Patterns narrative conflation.** The Debate Quality Audit's "Patterns" subsection interprets the combined-failure-mode table as if the numbers were per-side. E.g., the current VAS report says "Advocate side most frequently failed by strawmanning (27 instances)" where 27 is combined across both sides; the advocate-only count is 18. Table counts are correct; prose misattribution is the bug.

Both are prompt-level fixes, no code changes. After the prompt update, a single synthesizer-only re-run against the current VAS adversarial + linker outputs regenerates the report. Expected cost: ~$0.50. Stages 1–5b are unchanged and not re-run.

## File Map

| Action | File | Change |
|--------|------|------|
| Modify | `prompts/synthesizer.md` | Add label rubric explainer section + tighten Patterns instruction |
| No change | `pipeline/agents.py`, `pipeline/run_pipeline.py` | No code changes required |
| Re-run | `results/vas/06-synthesizer.{json,md}` | Regenerated via `--resume-from synthesizer` |
| No change | `results/vas/05-adversarial.*`, `05b-linker.*` | Unchanged inputs |

---

## Task 1: Update the synthesizer prompt

**Files:**
- Modify: `prompts/synthesizer.md`

- [ ] **Step 1: Read the current prompt**

`view prompts/synthesizer.md` and locate two insertion points:
- Top of the output format template (before "Pipeline Summary")
- The Debate Quality Audit section's "Patterns" subsection

- [ ] **Step 2: Add a label rubric explainer section**

Insert this as a new top-level section in the output format, AFTER the "Pipeline Summary" section and BEFORE "Critical Findings". Use exactly the section header `## How to Read This Report` so it's findable and consistent.

```markdown
## How to Read This Report

This report classifies findings by the surviving strength a neutral judge
assigned after reviewing each Advocate/Challenger debate. The three levels
mean:

- **STRONG** — The Challenger made grounded arguments the Advocate could
  not adequately defend. The critique identifies a real gap in the CEA
  that warrants direct attention.

- **MODERATE** — Both sides made some grounded arguments, and the
  substantive question remains open. The critique identifies a real
  concern but the evidence doesn't yet settle how to adjust.

- **WEAK** — The debate was dominated by reasoning failures (unsupported
  estimates, strawmanning, whataboutism, or similar) on one or both
  sides. The critique may still be valid, but this particular debate
  did not establish it. Weak findings are preserved in this report
  because the underlying claim may deserve a better-argued examination
  later.

The Debate Quality Audit section further below quantifies the reasoning
failure modes detected across all debates. Readers who want to assess
the calibration of these labels should start there.
```

The prompt instruction should make clear this section is ALWAYS included, with the text above used verbatim. The synthesizer should not rewrite or paraphrase it — this is reader-facing documentation of the system, not a content section.

- [ ] **Step 3: Tighten the Patterns subsection instruction**

In the current Debate Quality Audit section's Patterns subsection, the instruction gives the synthesizer latitude to interpret the failure mode table. This is where the conflation bug originates. Replace the current Patterns instruction with the following stricter version:

```markdown
**Patterns (1-3 sentences):** Interpret what these numbers mean. When
referring to a specific failure type's count, you MUST specify whether
the number is combined across both sides or is the per-side count. The
input provides:

- The combined table (totals across Advocate + Challenger)
- "Most common Advocate failure: [type]" — per-side top for Advocate
- "Most common Challenger failure: [type]" — per-side top for Challenger

If you cite a number from the combined table, label it as such:
"strawmanning appeared 27 times across both sides combined." Do not
write "the Advocate side most frequently failed by strawmanning (27
instances)" if 27 is the combined total — that conflates combined with
per-side.

If you want to comment on per-side patterns, use the "Most common X
failure" lines and their underlying counts, not the combined table.

Acceptable example: "The Advocate's most common failure was strawmanning
(18 instances), while the Challenger's most common was
unsupported_estimate_counter (14 instances). Across both sides combined,
strawmanning (27) was the most frequent failure mode overall."

Unacceptable example: "The Advocate side most frequently failed by
strawmanning (27 instances)."

If the numbers don't support a clear interpretation, write "No clear
pattern across this run."
```

- [ ] **Step 4: Verify the prompt file is well-formed**

Read the file back. Confirm the new section is in the right position (after Pipeline Summary, before Critical Findings), the markdown structure is intact, and the Patterns instruction replacement didn't leave orphan text.

- [ ] **Step 5: Run existing tests**

Run the full test suite. The synthesizer prompt construction test should still pass (it tests the message-building contract, not the prompt content itself). If any test fails, **stop and report**.

---

## Task 2: Commit the prompt update

- [ ] **Step 1: Commit**

Single commit.

```
feat: synthesizer prompt — label rubric explainer + tightened patterns instruction

Addresses two readability issues surfaced by domain expert review:

1. The strong/moderate/weak labels in the report were opaque to readers
   even though the judge prompt defines them clearly. Adds a verbatim
   "How to Read This Report" section explaining the rubric.

2. The Patterns subsection conflated combined-failure-mode table totals
   with per-side counts ("Advocate side most frequently failed by X
   (27 instances)" where 27 is combined). Tightens the instruction to
   require explicit combined-vs-per-side labeling.

No code changes. Pipeline behavior unchanged. Next synthesizer run
will reflect the new prompt.
```

Use Co-Authored-By trailers as standard.

---

## Task 3: VAS synthesizer re-run

This task involves ~$0.50 of API spend. Verify API key is active before starting.

- [ ] **Step 1: Back up the current VAS synthesizer output locally**

Copy `results/vas/06-synthesizer.{json,md}` to `results/vas/06-synthesizer.pre-rubric.{json,md}`. These are local-only — gitignore should already cover them via the existing `*.pre-judge.*` / `*.pre-dedup.*` patterns, but verify and extend if needed.

- [ ] **Step 2: Invoke the resume**

```
python -m pipeline.run_pipeline vas --resume-from synthesizer
```

Expected runtime: ~30-60 seconds. Expected cost: ~$0.50 (Opus synthesizer call). Hard stop: $2 total cost.

- [ ] **Step 3: Verify the new output**

Load the new `results/vas/06-synthesizer.md` and confirm:

1. The "How to Read This Report" section is present and matches the verbatim text from the prompt (no paraphrasing)
2. The section appears after "Pipeline Summary" and before "Critical Findings"
3. The Debate Quality Audit's Patterns subsection now labels combined vs per-side counts (spot-check: any specific failure mode count referenced in the prose should be explicitly tagged as either combined or per-side)
4. All other sections present and accounted for (Critical Findings, Significant, Minor, Conditional Findings, Open Questions, Resolved Negatives, Meta-Observations) — no regression in structure

If any check fails, **stop and report** before committing. Revert to the pre-rubric backup if the new output is worse.

- [ ] **Step 4: Commit the regenerated artifact**

If all checks pass, commit the regenerated files:

```
data: regenerate VAS synthesizer with label rubric + patterns fix

Re-runs synthesizer only against unchanged adversarial + linker outputs.
Applies the prompt updates from the prior commit: adds "How to Read This
Report" section and fixes the combined-vs-per-side conflation in the
Debate Quality Audit patterns subsection.

Cost: ~$0.50. Upstream stages 1-5b unchanged.

Pre-rubric backup saved locally as *.pre-rubric.* for comparison.
```

---

## Stop Conditions Requiring Tsondo Input

- Any existing test fails after the prompt update
- The verbatim rubric text appears to be paraphrased by the synthesizer in the regenerated output
- The Patterns subsection still conflates combined vs per-side counts after the prompt tightening
- Cost exceeds $2 (far above the $0.50 expectation)
- Structural regression in the regenerated report (missing sections that were present before)

## Things You Should NOT Do

- Re-run any upstream stages (adversarial, linker) — they're unchanged
- Modify the judge prompt — that's a separate plan awaiting Mikyo's taxonomy response
- Modify `pipeline/agents.py` or any Python code — this is prompt-only
- Touch artifacts for water-chlorination, ITN, or SMC
- Commit the `*.pre-rubric.*` backup files
- Create branches — commit directly to main as before
