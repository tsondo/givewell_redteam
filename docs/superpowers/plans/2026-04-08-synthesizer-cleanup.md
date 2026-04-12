# Synthesizer Report Cleanup — VAS Regenerate, ITN Footnote

> **For Claude Code:** Two tasks, one session, two commits. API key is active for Task A. No API access needed for Task B.

**Goal:** Bring the VAS and ITN synthesizer reports into alignment with the de-duplicated underlying data from commit 5aeed0e. VAS is regenerated cleanly (the report hasn't been distributed yet); ITN is footnoted in place (the original artifact has already been shared and shouldn't diverge).

---

## Background

Commit 5aeed0e de-duplicated the verifier, quantifier, and adversarial JSONs for the VAS and ITN runs after a parser bug was found that double-counted critiques whose verifier output included a summary restatement section. The fix landed in commit 6680f59 with a regression test in 7b67999.

The synthesizer reports (`results/vas/06-synthesizer.md` and `results/itns/06-synthesizer.md`) were generated against the pre-dedup data and still show inflated counts:

- **VAS:** says 31 verified / 31 surviving / 97% signal rate. Correct: 28 / 28 / 88%.
- **ITN:** says 30 verified / 30 surviving / 100% signal rate. Correct: 28 / 28 / 93.3%.

---

## Task A: Regenerate VAS synthesizer

The VAS report has not been distributed. Regenerating produces a clean canonical artifact.

- [ ] **Step 1: Confirm the resume mechanism**

`pipeline/run_pipeline.py` should support resuming from a specific stage (this came up during the live VAS quantifier crash). Confirm it exists, accepts `synthesizer` as a target, loads the existing `05-adversarial.json` rather than re-running prior stages, and overwrites the stage 6 outputs.

If the resume mechanism doesn't exist or doesn't work this way, **stop and report**. We'll need a different approach (probably a small script that imports `run_synthesizer` directly and feeds it the loaded stage 5 data).

- [ ] **Step 2: Back up the original VAS synthesizer outputs locally**

Save the existing `06-synthesizer.json` and `06-synthesizer.md` as `*.pre-dedup.*` for sanity-checking. These are local-only — make sure the `*.with-duplicates.*` gitignore rule from commit 5aeed0e covers them, or extend it if not.

- [ ] **Step 3: Run the synthesizer stage**

Expected: a single Opus call, ~$0.50, ~30 seconds.

**Stop condition:** If the cost exceeds $2, something is re-running stages it shouldn't. Stop and report.

- [ ] **Step 4: Verify the new report has correct counts**

The pipeline summary section should reference 28, not 31. Specifically, "Verified critiques: 28", "Critiques surviving adversarial review: 28", and a signal rate around 88% (28/32).

**Stop condition:** If the new report still says 31, the synthesizer may have its own count source that wasn't de-duplicated. Stop and report.

- [ ] **Step 5: Sanity-check the findings haven't shifted substantively**

Diff the new report against the pre-dedup backup. Expected differences: count numbers, possibly minor wording or reordering of findings. **Not expected:** entirely different findings, missing critical findings, or new critical findings that weren't there before.

**Stop condition:** If the new synthesizer output looks substantively different from the original (e.g., Finding 1 is now about something completely different), stop and report. That would suggest the synthesizer is more non-deterministic than acceptable and we should think about whether to keep the original wording instead.

- [ ] **Step 6: Commit**

One commit covering the regenerated `06-synthesizer.json`, `06-synthesizer.md`, and the updated `pipeline-stats.json` (the rerun will naturally add the additional ~$0.50 to it; that's fine and expected).

Commit message should explain: this is a stage-6 rerun against deduplicated stage 5 data, the prior report was generated before commit 5aeed0e, the underlying findings are substantively unchanged, only headline counts needed correction. Reference 5aeed0e in the message.

---

## Task B: Footnote the ITN synthesizer report

The ITN report has been distributed. Footnoting preserves the original artifact and creates an audit trail without divergence.

- [ ] **Step 1: Insert this exact footnote at the top of `results/itns/06-synthesizer.md`**

Place it immediately after the first `# Red Team Report:` title line. Use `str_replace`. The exact text:

```markdown

> **Note (April 2026):** The pipeline summary counts in this report were generated before a parser bug was discovered that double-counted critiques whose verifier output included a summary restatement section. The corrected counts are: 28 verified critiques (not 30), 28 surviving adversarial review (not 30), signal rate 93.3% (not 100%). The underlying findings are unchanged — only the headline counts were affected by the bug. See commit 5aeed0e for the data correction and commit 6680f59 for the parser fix.

```

The exact wording matters here — it's the audit trail that future readers (including Tsondo, Brendan, or anyone reviewing the work) will use to understand what happened. Don't paraphrase.

- [ ] **Step 2: Commit**

A single commit modifying only `results/itns/06-synthesizer.md`. Commit message should explain: footnote-only change, body of the report unchanged because the original has been distributed, references 5aeed0e and 6680f59.

---

## Stop Conditions Summary

- VAS resume mechanism doesn't exist or doesn't work as described
- VAS synthesizer rerun costs more than $1
- New VAS report still shows count of 31
- New VAS findings are substantively different from the original
- Any test suite failure after either task

## Don't

- Re-run any stage other than the VAS synthesizer
- Modify the body of the ITN report — only the footnote addition
- Touch anything in `results/water-chlorination/` or `results/smc/` — those runs are clean and unaffected
- Modify `pipeline-stats.json` by hand for either run (VAS gets updated naturally by the rerun; ITN doesn't change at all)
- Commit the `*.pre-dedup.*` backup files
