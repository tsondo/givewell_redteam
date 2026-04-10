# VAS Re-Run Verification Report

## Run summary

- **Total cost:** $6.3616
  - Per the plan clarification, `pipeline-stats.json` is per-run (not cumulative), so this is the absolute cost of re-running stages 5, 5b, and 6 plus the unavoidable `fetch_web` retrieval of the intervention report.
  - The prior `pipeline-stats.json` (covering only an earlier synthesizer-only run) is preserved locally at `results/vas/pipeline-stats.pre-judge.json` for comparison if needed.
- **Per-stage costs:**
  - `fetch_web`: $0.0831 (intervention report re-fetch + empty-URL baseline attempt)
  - Adversarial total: **$5.2828**
    - advocate (28 calls, Sonnet): $0.7128 ($0.0255 avg)
    - challenger (28 calls, Sonnet): $0.8620 ($0.0308 avg)
    - judge (28 calls, Opus): $3.7081 ($0.1324 avg)
  - Linker: **$0.0536**
  - Synthesizer: **$0.9421**
- **Wall-clock time:** 44 min 53 sec (13:48:57 → 14:33:50)
- **Warnings during run:** None. Zero parser warnings, zero API retries, zero exceptions. The log is clean apart from the first launch, which was aborted by a 401 invalid-API-key error before any work was done (new key was provided and the re-launch succeeded).
- **Real-time cost monitoring:** Available (outcome 1). `call_api` logs per-call cost and cumulative via `agents.py:93-101`. Monitoring tracked each critique in real time and no cost/wall-clock threshold was breached.
- **Plan/reality delta on the 30-min wall-clock hard stop:** The plan projected 12–20 min total runtime based on the prior (no-judge) adversarial stage. The Opus judge tripled per-critique wall time (~85s/critique × 28 = ~40 min). The 30-min hard stop would have killed a perfectly healthy run at ~critique 18. Tsondo approved lifting the wall-clock hard stop for this run while keeping the $25 cost hard stop (total stayed at $6.36, far below $25).

## Structural checks (Task 3)

| # | Check | Result |
|---|---|---|
| 1 | Adversarial output integrity (5 sub-checks: judge_audit populated, advocate_self_assessment valid, surviving_strength valid, recommended_action non-empty, action_feasibility valid) | **PASS** (all 28/28) |
| 2 | Verdict distribution vs pre-judge baseline | **PASS with flag** — see below |
| 3 | Failure mode aggregation | **PASS** — judge detecting failures in 28/28 entries on both sides |
| 4 | Linker output integrity (structural) | **PASS** — 3 deps, all counts match, all enums valid |
| 5 | Linker semantic checks | **FLAG** — title mismatch on Dep 2; `contradicts` classification also questionable. Mitigated: 0 `depends_on`. |
| 6 | Synthesizer section headers (all 10) | **PASS** |
| 7 | Pipeline Summary count verification | **PASS** — all 5 counts match upstream data exactly |
| 8 | Debate Quality Audit verification | **PASS on counts, FLAG on patterns narrative** |
| 9 | Conditional Findings cross-reference | **PASS** — 0 `depends_on` → 0 CONDITIONAL tags → zero-state text present |
| 10 | Open Questions / Resolved Negatives cross-reference | **PASS** — all 4 rejected critiques in correct section, no fabrications |

### Step 2 detail (verdict distribution)

Distribution shift:

| Strength | Pre-judge (actual) | New | Change |
|---|---|---|---|
| strong | 17 | 0 | -17 |
| moderate | 11 | 27 | +16 |
| weak | 0 | 1 | +1 |

**Movement breakdown across the 28 shared titles:**
- strong → moderate: 16
- strong → weak: 1
- (unchanged moderate → moderate: 11)
- upgrades: 0
- new/dropped titles: 0

**Plan documentation error (non-blocking flag):** The plan's Task 3 Step 2 stated "Pre-judge baseline (from prior dedup work): 28/28 surviving as 'strong' (100%)." The actual pre-judge distribution on disk (backed up to `results/vas/05-adversarial.pre-judge.json`) was 17 strong / 11 moderate. The plan's claim was wrong, likely from stale memory during plan authoring. This doesn't affect the verification conclusion — the calibration check ("if new distribution is still 100% strong AND failure mode lists are mostly empty → stop") was not triggered under either the documented or actual baseline, because the new distribution shows clear downgrades and substantive failure detection. Worth correcting in the plan file for future reference.

### Step 5 detail (linker semantic)

Linker output has 3 dependencies:

1. `Threshold Effects Below Critical VAD Prevalence Levels` ↔ `Threshold Effects for Herd Protection in High-Mortality Settings` — `engages_with` / unverified. Titles match ✓.
2. `Meta-Analysis Publication Bias in Historical Evidence Base` ↔ `Short-Term Protection Window Creating Mortality Displacement` — `contradicts` / rejected. **Title mismatch:** the rejected file actually stores the title with a trailing `**` (stray markdown bold markers that leaked into the title field during an earlier stage). The linker stripped it when emitting its JSON, so verbatim matching fails.
3. `Systematic Timing Delays Between Supplementation Rounds` ↔ `Seasonal and Campaign-Timing Cost Variations Not Reflected` — `engages_with` / unverified. Titles match ✓.

**Why this is a flag not a stop, despite the plan saying title mismatches are stop-and-report:** The plan's reasoning for stopping on title mismatches is that they cause silent failure in CONDITIONAL tagging. But CONDITIONAL only propagates for `depends_on` relationships (per `docs/linker_info.md` rule 14 and `prompts/synthesizer.md`), and this run has zero `depends_on` dependencies. All 3 deps are `engages_with` or `contradicts`, which do not trigger CONDITIONAL. So the mismatch has no practical impact on the synthesizer output for this run. The root cause (trailing `**` in the source data) still needs fixing so future runs with `depends_on` don't silently fail.

**Additional semantic concern on Dep 2:** Both the surviving critique (publication bias) and the rejected critique (mortality displacement) argue that VAS effects are overstated, just from different causes. They are independent hypotheses, not actively at odds. `engages_with` would be a better classification than `contradicts`. The linker's justification tries to thread the needle by arguing that "the rejection of displacement ... strengthens the publication bias concern," but that logic is strained. Not a stop condition — flagging for review only.

### Step 8 detail (Debate Quality Audit)

**Counts match perfectly** (combined advocate + challenger table in the synthesizer report vs. independent aggregation from `05-adversarial.json`):

| Type | Synth report | Independent (adv+ch) |
|---|---|---|
| unsupported_estimate_fabricated | 14 | 10+4=14 ✓ |
| unsupported_estimate_pseudo | 20 | 9+11=20 ✓ |
| unsupported_estimate_counter | 30 | 16+14=30 ✓ |
| whataboutism | 2 | 1+1=2 ✓ |
| call_to_ignorance | 17 | 11+6=17 ✓ |
| strawmanning | 27 | 18+9=27 ✓ |
| false_definitiveness | 24 | 11+13=24 ✓ |
| generic_recommendation | 2 | 2+0=2 ✓ |
| misrepresenting_evidence_status | 20 | 6+14=20 ✓ |
| **Total** | **156** | **156** ✓ |

"Most common Advocate failure: strawmanning" ✓ (advocate-only top at 18)
"Most common Challenger failure: unsupported_estimate_counter" ✓ (tied-top at 14 with misrepresenting_evidence_status)
"Sound analytical moves noted: 0" ✓ (matches independent count)

**Patterns narrative flag:** The patterns paragraph conflates combined table counts with per-side counts:

> "The Advocate side most frequently failed by strawmanning (**27 instances**)"

27 is the combined total (18 advocate + 9 challenger). The advocate-only count is 18. Similarly, "Challenger's predominant failure was unsupported counterfactual estimates (30 instances)" — 30 is combined (16+14), not challenger-only (14). The combined-table counts are correct; the narrative sentences misattribute them. This is a prose-level issue that a Plan-2 refinement could tighten (e.g., by having the synthesizer emit per-side counts or by tightening the prompt on how to reference the combined table). Not blocking.

## Substantive checks (Task 4)

- **Verdict distribution:** new 0/27/1 (strong/moderate/weak) vs old 17/11/0. 17 downgraded, 0 upgrades, 0 dropped/added titles. Judge is doing real work.
- **Failure mode aggregate:** 156 real failures across 28 debates (84 advocate + 72 challenger). Top types: `unsupported_estimate_counter` (30), `strawmanning` (27), `false_definitiveness` (24), `misrepresenting_evidence_status` (20), `unsupported_estimate_pseudo` (20).
- **Sound syntheses noted:** 0. No debates were judged as reaching sound resolution. This is internally consistent with 0 `surviving_strength = strong`.
- **Linker dependency count:** 3 (2 `engages_with` + 1 `contradicts` + 0 `depends_on`).
- **Findings continuity:** 9 shared titles / 0 old-only / 19 new-only. **All 9 pre-judge headline titles are still present in the new report** (full-text search confirms). The new synthesizer surfaces all 28 surviving critiques as distinct findings rather than editing down to ~9 headlines. This is a major behavioral shift vs the pre-judge run, but nothing was dropped — 19 previously-hidden findings are now surfaced.
- **Finding 1 status:**
  - "15-20% threshold" claim still present, but hedged with `~` and softened verbs ("may drop", "potentially eliminating")
  - Demoted from Critical (pre-judge) to Significant (new, surviving_strength `moderate`)
  - Not marked CONDITIONAL (expected: 0 `depends_on` in linker output)
  - Explicit "Key unresolved question" acknowledges the specific threshold uncertainty
  - Net: partial but not full resolution of the overconfident-threshold concern

### Judge quality spot-checks (Task 4 Step 2)

- **Downgraded pick (strong→weak):** *Systematic Timing Delays Between Supplementation Rounds.* `verdict_justification` cites specific debate moves, `recommended_action` uses SPECIFIC INVESTIGATION format with concrete partner contacts (Helen Keller International, Nutrition International), failure entries quote the actual unsupported calculations (`8-17%`, `14%/25%`). Substantive, not boilerplate.
- **Highest-failure-count pick (8 total):** *Government Health Worker Time Opportunity Costs Not Captured.* Judge effectively distinguishes what the debate resolved vs what it couldn't (both sides unsupported on magnitude), action has concrete next step. Substantive.
- **sound_synthesis_noted pick:** None exist in the dataset (structurally consistent with 0 strong verdicts). Nothing to spot-check.

## Anomalies and flags

These are the items requiring your judgment before a commit decision:

1. **Plan documentation error:** Plan stated pre-judge baseline was 28/28 strong; actual was 17 strong / 11 moderate (Task 3 Step 2 flag). Doesn't affect the verification outcome, but the plan file should be corrected for future reference.

2. **Linker Dep 2 title mismatch:** Source data (`03-verifier-rejected.json`) has `"Short-Term Protection Window Creating Mortality Displacement**"` with trailing bold markers. Linker stripped them, defeating verbatim match. **Mitigated this run** by all 3 deps being `engages_with`/`contradicts` (no `depends_on` → no CONDITIONAL propagation). **Future runs with `depends_on` on this same rejected critique would silently fail CONDITIONAL tagging.** Root fix: clean up the stray `**` in the source data (requires running the data through a sanitizer or re-running verifier/investigator with a prompt tweak to prevent the leak).

3. **Linker Dep 2 `contradicts` classification questionable:** Both critiques argue effects are overstated, just via different mechanisms. `engages_with` would fit better than `contradicts`. A prompt tightening for the linker could help. Not blocking.

4. **Synthesizer Debate Quality Audit patterns narrative:** Conflates combined-table counts with per-side counts ("Advocate side most frequently failed by strawmanning (27 instances)" where 27 is combined; actual advocate-only is 18). The table itself is correct; the prose summary is sloppy. Not blocking. Plan-2 refinement candidate.

5. **Synthesizer behavior shift — surfacing all 28 findings:** The new synthesizer presents all 28 surviving critiques as distinct findings (0 Critical + 28 Significant + 0 Minor) rather than curating ~9 headlines. Nothing dropped; 19 previously-hidden findings are now visible. Needs your decision on whether this is the intended behavior or whether you want the new synthesizer to restore curation. (Arguably healthier: lets readers see the full set and sort for themselves. Arguably noisier: dilutes the top-tier signal.)

6. **VAS baseline URL is intentionally empty in `pipeline/config.py`** (`INTERVENTION_URLS['vas']['baseline'] = ""`). The synthesizer's `Comparison with GiveWell's AI Output` section received whatever the web_search tool returned for an empty URL (2071 input / 65 output tokens — essentially an error response). I did not spot-check that section's content beyond verifying its header is present. If VAS comparison-to-baseline matters for the Mikyo/Brendan share, that section may be degraded. Not flagged in the plan as a check, so surfacing here as an FYI.

7. **Plan's wall-clock estimate was off by ~2x:** The 12–20 min / 30 min hard-stop estimate was based on the pre-judge flow. The Opus judge tripled per-critique time to ~85s (not cost — cost is well under). You approved lifting the wall-clock hard stop during the run. Future plans that introduce Opus judge-agent calls should base wall-clock estimates on ~2.5 min/critique including all three calls.

8. **Pre-flight API-key check is insufficient:** The plan's Task 1 Step 5 verifies the env var is set but doesn't make an API call. The first run failed on a 401 because the key in `.env` at that time was invalid. A zero-token ping (e.g., an intentionally malformed request that fails with 400 instead of 401) in pre-flight would catch this earlier. Plan refinement candidate, not a finding against this run.

## Recommended next step

**Verification complete with concerns, see flags.** All structural and substantive checks either passed or flagged for review. No hard stops triggered. The regenerated artifacts are internally consistent and substantively reasonable:

- Judge is doing real work (17 of 28 downgraded, 156 real failures detected, 0 sound syntheses).
- Linker found a conservative 3 dependencies with no `depends_on`, so no CONDITIONAL chains need to be validated.
- Synthesizer is reading upstream counts correctly, not fabricating. No rejected critiques were dropped.
- Finding 1 has been partially softened (hedged language, Critical → Significant demotion, explicit open question).

The items under "Anomalies and flags" are mostly data-hygiene, prose-quality, and plan-refinement issues rather than correctness problems. The only item that genuinely needs your judgment before deciding on Task 6 is **#5 (the synthesizer behavior shift to surfacing all 28 findings)**, because it materially changes what the report looks like compared to the pre-judge baseline — that one is a product decision, not a verification issue.

Artifacts ready for commit (pending your approval of Task 6):
- `results/vas/05-adversarial.json`
- `results/vas/05-adversarial.md`
- `results/vas/05b-linker.json`
- `results/vas/05b-linker.md`
- `results/vas/06-synthesizer.json`
- `results/vas/06-synthesizer.md`
- `results/vas/pipeline-stats.json`

Pre-judge backups remain gitignored at `results/vas/{05-adversarial,06-synthesizer,pipeline-stats}.pre-judge.*` for local comparison.
