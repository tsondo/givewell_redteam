# Blind validation: Coefficient Giving TB statins BOTEC

*Written 2026-11-07, after run #02. Kept deliberately plain so we cannot talk ourselves into a better result than we got.*

## Why this test

Our earlier runs on GiveWell CEAs could be compared only with GiveWell's single-pass AI output. That shows the pipeline produces more, better-grounded critiques. It does not show the critiques are *right*.

Coefficient Giving (CG, formerly Open Philanthropy) published four sample back-of-the-envelope calculations (BOTECs) in May 2025, in "How we use back-of-the-envelope calculations in our grantmaking". For one of them, a grant to trial atorvastatin as an adjunct treatment for drug-susceptible TB, the same post also lists CG's own limitations and the revisions CG made after the grant. That gives an answer key written by the analysts themselves, before we ran anything.

The BOTEC is a sample written to show CG's method, not a full analysis. Gaps in it are expected and say nothing about CG's research quality. The question is only whether the pipeline finds what CG's own analysts later found.

## Design

- **Input:** the BOTEC text only (`data/cg-tb-statins/report.md`), captured as a close paraphrase with every published number. CG's "limitations" and "updates since making the grant" sections were removed. A short header maps GiveWell terms to CG's units ($OP, SROI) and its ~2,000x funding bar. Prompts were not changed.
- **Model:** `pipeline/botec.py` replicates the formula chain and reproduces CG's bottom line (3,055x vs. "about 3,000x").
- **Blinding:** the verifier's web search was limited to medical and health-data domains (`INTERVENTION_VERIFIER_OVERRIDES["cg-tb-statins"]`). CG's site, Open Philanthropy's and the EA Forum, which host the answer key, were excluded.
- **Scoring rule, fixed before the run:** *caught* = the pipeline raises the same issue with the same direction of effect; *partial* = right issue but wrong direction or mechanism, or only a vague mention; *missed* = not raised. The net-direction item is scored on whether the pipeline's verdict points the same way.

## Answer key (CG's own follow-ups)

**Limitations CG listed**
- L1. Omits the value of the sweat-based TB diagnostic funded by the same grant.
- L2. Omits quality-of-life gains beyond deaths averted.
- L3. Costs of later trials are only rough estimates.
- L4. Ignores that newer TB treatments could lower the disease burden beyond the existing trend.

**Updates CG made after the grant**
- U1. Probability of success should be ~30%, not 40%.
- U2. Speedup should be ~3 years, not 1: few funding options existed, and the grant backed the lead researcher early.
- U3. Model a longer period: widespread adoption may take ~18 years, not 8, and falling TB prevalence over that extra decade lowers ROI.
- U4. Net: the larger speedup outweighs U1 and U3, so the corrected SROI is *higher* than 3,000x.

## Result (run #02)

Run #02: 2026-11-07, `claude-opus-5-5` and `claude-sonnet-5-5`, $22.23, no truncated calls. 8 threads, 41 candidate critiques, 39 debated (2 judged immaterial), 39 surviving.

| CG item | Score | What the pipeline said |
|---|---|---|
| L1 diagnostic | Caught (weak) | Finding 32: the sweat-based diagnostic carries real option value but is speculative. |
| L2 quality of life | Caught (moderate) | Finding 21: post-TB lung disease morbidity is likely the largest unvalued channel. |
| L3 later trial costs | Caught (strong) | Finding 1: a $7M programme cannot fund a mortality-powered Phase III; also Findings 19 and 29. |
| L4 newer treatments | Caught (moderate) | Finding 14: shorter and new regimens erode the eligible population and the incremental benefit; Finding 36 on the M72 vaccine. |
| U1 success ~30% | Caught | Findings 4 and 18: base rates put "Phase II and III both succeed" at 15–25%. Same direction as CG, more pessimistic. |
| U2 speedup ~3 years | Caught (moderate) | Findings 2 and 20: a generic statin has no natural funder, so "never adopted" is a live counterfactual and SROI rises. This is CG's own reasoning. Findings 24 and 35 argue the opposite. |
| U3 longer horizon | Partial | Finding 5: a slower S-curve adoption ramp lowers SROI 20–31%, matching the direction. But Finding 13 disputes CG's falling-prevalence premise because notified cases rose from 7.5M (2022) to 8.3M (2024). That reasoning is weak: notifications rose mostly because detection improved (8.3M is about 78% of estimated incidence), and TB deaths fell in 2024. |
| U4 net higher | Partial | The report names the counterfactual framing, which pushes SROI up, "the single most decision-relevant question" and warns the downward adjustments double-count. It gives no net estimate. |

**6 caught, 2 partial, 0 missed.**

The pipeline also raised points CG did not list. The strongest: Phase III "success" will likely be judged on a surrogate or composite endpoint, while the BOTEC values only mortality (Findings 16, 17, 27). Rifampicin interactions may reduce atorvastatin exposure in routine care (Finding 30). The eligible population lacks label filters (Finding 6). Whether these are right is not tested here.

Run #01 (same day) failed for mechanical reasons: silent output truncation on the new models and a parser bug that dropped a decomposer thread. It is archived in `results/cg-tb-statins-run01/` and gives no evidence either way about the pipeline's reasoning.

## Caveats

- **Possible recall.** Both models' training data extends past May 2025, so they may have seen CG's post. Web blinding cannot prevent recall. We searched every stage output: none cites CG's or the EA Forum's pages, and none uses CG's distinctive revised figures (18 years, a 3-year speedup). The only mention of the post's title comes from the source line in our own input. Recall cannot be ruled out, but nothing points to it.
- **Coverage is cheap when output is large.** 39 findings on a 700-word BOTEC will touch most issues. A fair reading: the pipeline found everything CG later found, but a grantmaker would need the synthesizer's grouping (four undocumented parameters) to use it.
- **Most impact numbers are not executed.** The quantifier ran real sensitivity analysis for only 2 of 41 critiques. Other SROI figures in the report are the model's own arithmetic.
- **The verifier rejected nothing** (0 of 41), so it did not act as a filter on this input.
- **Different models from the April runs.** Results are not directly comparable with the GiveWell runs.
- **Single run.** No repeat yet to test stability.

## Process issues found in run #02, and the fixes

| Issue in run #02 | Fix (commits b577583 to dc6c88e) |
|---|---|
| Verifier rejected 0 of 41 | Verifier names each critique's core claim and rates it SUPPORTED, LOGIC ONLY or CONTRADICTED; contradicted means rejected |
| Sensitivity executed for 2 of 41 | Quantifier ends with plain-text `RANGE:` lines in the model's parameter names; the code runs those |
| 39 findings, overlapping haircuts | New "Findings by Parameter" table with a do-not-stack note |
| Opposing findings not reconciled | New "Conflicting Findings" section, each with what would decide it |
| Immaterial critiques not reported | Listed and counted in the report |
| Extractor missed weak findings | Fixed for both header and bold-paragraph formats |

These changed the verifier, quantifier and synthesizer prompts, so run #03 is not directly comparable with run #02 on those stages.

## Run #03: same critiques, fixed pipeline

Run #03 resumed from the verifier on run #02's exact 41 critiques, so differences come only from the fixes. Cost $17.49 for the resumed stages, no truncated calls.

| Measure | Run #02 | Run #03 |
|---|---|---|
| Verifier rejections | 0 of 41 | 5 of 41 (2 contradicted, 3 unverifiable) |
| Critiques with executed sensitivity | 2 of 41 | 35 of 36 |
| Surviving findings | 39 (some strong) | 35 (27 moderate, 8 weak, none strong) |
| Score against CG's follow-ups | 6 caught, 2 partial | 6 caught, 2 partial |

**What changed:** the report is far more usable. Every finding carries an executed range; 35 findings collapse into 10 parameter rows; the speedup disagreement appears as an explicit conflict whose decider ("has any funder committed to a statin-TB Phase III independently?") is essentially CG's own reason for revising the speedup. The upward counterfactual argument is now Finding 1. No finding reached STRONG: with the core-claim rating visible, the judge capped findings whose load-bearing claim could not be checked. The report attributes this to the BOTEC leaving p_success, adult_uptake, the 10% effect and the 6% mortality undefined, and recommends one document request to CG as the highest-value next step.

**What did not change:** the same 6 caught and 2 partial. U4 is still partial, and the report now leans the other way from CG: it says most adjustments point down and a joint downside "would likely fall below 2,000x", while CG concluded the corrected SROI is higher.

**New issues found in run #03:**
1. The verifier rated 34 of 36 surviving core claims LOGIC ONLY, so the Open Questions note has 33 entries. On a BOTEC whose inputs are undocumented, almost every load-bearing claim is about CG's own definitions. Most "what would settle it" lines are the same few document requests.
2. The verifier over-uses CONTRADICTED: it rejected "Phase IIc success is a weak gate" as contradicted while its own reason says whether this trial matches the design standard "is unchecked".
3. Debate failure modes were dominated by false_definitiveness (47) and call_to_ignorance (40), both sides asserting what undefined parameters "already" include.

Issues 1 and 2 are fixed in commit 275c389 and not yet tested in a run. The verifier now rates a claim CONTRADICTED only when evidence refutes it as it applies to this case. Open Questions is now a short checklist of the distinct questions, split into questions for the CEA's authors and questions needing new evidence, each listing the findings it settles. Issue 3 is open.

## Spot check of findings after run #03

- **TB case counts (run #03 Finding 21).** WHO does report a record 8.3M people newly diagnosed in 2024, up from 7.5M in 2022. But that is about 78% of estimated incidence, the rise mostly reflects better detection, and TB deaths fell (1.25M to 1.23M). It does not undercut a falling-burden assumption. Run #03 treated it as a stale starting figure and marked it not assessable, which is reasonable.
- **Rifampicin interaction.** Real: rifampicin sharply lowers atorvastatin levels (Backman et al., 2005). But the trials give atorvastatin alongside rifampicin-based treatment, so the trial effect already includes the interaction. It matters only if routine-care dosing differs.

## Comparison: a single-session skill on the same test

The pipeline costs about $20 a run and needs a local setup. To see how much of its value survives in
something a researcher could use in their own chat with no setup, we wrote
[botec-review](../botec-review/), a Claude skill that reviews a BOTEC in one session. It rebuilds
the arithmetic, finds the inputs that decide whether the estimate clears the bar, checks those inputs
against public evidence, and lists questions for the author. A small script does all the arithmetic.
Output is capped at five findings.

A fresh agent with no other context ran the skill on the same BOTEC text, with the same web
blocking, and was scored against the same answer key with the same rule, written down before its
output was read. [Full review](../botec-review/validation/tb-statins/review.md) and
[scoring](../botec-review/validation/README.md).

| CG item | Pipeline (run #03) | Skill |
|---|---|---|
| L1 diagnostic | Caught | Caught |
| L2 quality of life | Caught | Caught |
| L3 later trial costs | Caught | Caught |
| L4 newer treatments | Caught | Missed |
| U1 success ~30% | Caught | Partial: a decision driver, no direction argued |
| U2 speedup ~3 years | Caught | Caught, as a question for the author |
| U3 longer horizon | Partial | Partial |
| U4 net higher | Partial | Missed: leans downward |
| **Total** | **6 caught, 2 partial, 0 missed** | **4 caught, 2 partial, 2 missed** |
| Cost | ~$17–22 | A few dollars (11 searches, ~128k tokens) |
| Output | 35 findings plus a checklist | 2 findings, a decision table, 7 questions |

Both found the most decision-relevant gap: the trials measure sputum and X-ray results, while the
estimate values deaths. The skill made it concrete with a sample-size calculation (about 23,000
patients per arm for a mortality-powered Phase III), and showed that at a published Phase III cost
the estimate falls to 959x, below the bar. Neither reproduced CG's net upward correction, which came
from CG's knowledge of the funding landscape.

**Reading.** The pipeline catches more, and its debate stage argues directions the skill leaves as
questions. The skill gets most of the decision-relevant content at a fraction of the cost, in a form
a grantmaker can read in a few minutes. Which is better depends on the stakes of the decision.

**Same caveats as above, plus two.** It is one case with one run of each approach. The skill's
instructions were revised after this test, to fix clarity problems the test agent reported, not
the items it missed, so the score describes the version that was tested.

## Files

- Run #02 outputs: `results/cg-tb-statins-run02/` (graph: `cg-tb-statins-run02-2026-11-07/graph.json`)
- Run #03 outputs: `results/cg-tb-statins/` (graph: `cg-tb-statins-run03-2026-11-07/graph.json`)
- Input and model: `data/cg-tb-statins/`, `pipeline/botec.py`
- Single-session skill, its review and scoring: `botec-review/`
- Source: Coefficient Giving, "How we use back-of-the-envelope calculations in our grantmaking", May 2025 (also on the EA Forum).
