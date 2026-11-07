# Validation

## TB statins BOTEC (blind)

Written before the skill's output was read, so the scoring rule can't drift toward the result.

**Why this case.** Coefficient Giving (CG) published this sample BOTEC in May 2025 and later published
its own limitations and revisions for it. That gives an answer key written by the analysts, against
which a blind review can be scored. The same answer key was used to test the full multi-agent
pipeline in this repository ([write-up](../../docs/cg-tb-statins-validation.md)),
which caught 6 of 8 items and partly caught 2.

**Setup.** A fresh agent with no other context ran the skill exactly as written on the BOTEC text
only (`tb-statins/input.md`). Its web searches excluded CG's site, Open Philanthropy's, Good
Ventures', and the EA Forum and its mirrors. It was told not to use any knowledge of CG's later
revisions. Possible recall from training data can't be ruled out.

**Answer key.**
- L1. Omits the value of the sweat-based TB diagnostic funded by the same grant.
- L2. Omits quality-of-life gains beyond deaths averted.
- L3. Costs of later trials are only rough estimates.
- L4. Ignores that newer TB treatments could lower the disease burden beyond the existing trend.
- U1. Probability of success should be ~30%, not 40%.
- U2. Speedup should be ~3 years, not 1 (few funding options; the grant backed the lead researcher early).
- U3. Model a longer adoption period (~18 years, not 8); falling prevalence over that extra decade lowers ROI.
- U4. Net: the larger speedup outweighs U1 and U3, so the corrected SROI is higher than 3,000x.

**Scoring rule.** *Caught*: the review raises the issue with the same direction, as a finding, a
decision driver, or a question for the author. *Partial*: right issue, wrong direction or only a
passing mention. *Missed*: not raised. U4 is scored on whether the review's overall lean matches.

**Expected handicap.** The skill keeps at most five findings and checks at most five decision
drivers, on purpose: it is meant to be read in two minutes. It should score lower than the
pipeline. The question is whether it catches the items that decide the result (U1, U2, U4) at a
small fraction of the cost.

### Result (2026-11-07)

The skill ran with 11 web searches and about 128k tokens, a few dollars at most at API prices (no exact meter for a single session); the
pipeline's comparable runs cost $17–22. Review: [`tb-statins/review.md`](tb-statins/review.md).

| CG item | Score | What the review did |
|---|---|---|
| L1 diagnostic | Caught | Finding 2: the diagnostic funded by the same grant is valued at zero (raises) |
| L2 quality of life | Caught | Finding 2: post-TB lung damage and illness are left out (raises) |
| L3 later trial costs | Caught | Finding 1: a Phase III able to show fewer deaths would need ~23,000 patients per arm; at a published Phase III cost the SROI is 959x, below the bar |
| L4 newer treatments | Missed | Not raised |
| U1 success ~30% | Partial | A decision driver with break-even 26% and a question about what "success" means; no direction argued, evidence not checked (it fell outside the five-driver limit) |
| U2 speedup ~3 years | Caught | Raised as a question ("who else would run this trial without the grant?"), with evidence that no other group is racing to run it and a 3-year scenario at 9,165x |
| U3 longer horizon | Partial | Timing raised through discounting (lowers), not through a slower adoption ramp |
| U4 net higher | Missed | The review leans downward: "clears the bar only narrowly" |

**4 caught, 2 partial, 2 missed** (pipeline: 6 caught, 2 partial, 0 missed).

**Reading.** The skill finds the issue that matters most for a decision, the gap between what
the trials measure and what the estimate values, and makes it concrete with a sample-size
calculation. It flags each other driver of the result, but turns most into questions rather
than arguing a direction. That is the intended design for inputs that rest on the author's judgment, but it is why
U1 and U4 are not caught: the net upward correction came from CG's own knowledge of the funding
landscape, which a single session working from public sources mostly lacks.

**Changes after this test.** The test agent reported eight places where the instructions were
unclear. The fixes address those clarity problems only, not the items the review missed, so as
not to tune the skill to this answer key:
- what to do when more than five inputs qualify as decision drivers;
- an anchor for ranges (roughly an 80% interval);
- how to handle factors of unknown size (label them illustrative) and the author's own conventions (they become questions);
- an input with no evidence either way is not a finding;
- a `checks` section in the script for side calculations, and fixed parameters left out of the sensitivity table;
- a balance line in the output, and the appendix not counting toward length;
- how to cite a public record that may describe the project under review.

Because the skill changed after this run, this result describes the version at the time of the
test. The three other sample BOTECs are run with the revised version.
