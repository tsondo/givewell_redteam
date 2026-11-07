---
name: botec-review
description: Review a draft back-of-the-envelope calculation (BOTEC) or cost-effectiveness estimate before a funding decision. Rebuilds the arithmetic, finds which inputs decide whether it clears the bar, checks key numbers against public evidence, and lists questions for the author. Use when someone shares a BOTEC, CEA, SROI or cost-per-outcome estimate and asks for a review, sanity check, critique or red team.
---

# BOTEC review

A fast, structured second look at a cost-effectiveness estimate, done in one session. The reader
is a busy grantmaker deciding whether to trust the number. Lead with what decides the result,
keep every claim checkable, and keep the review short.

This is a checklist, not a verdict. It does not replace the author's judgment or an independent
review. Say so once, at the end.

## Before you start

1. **What you need.** The estimate itself (prose, a pasted table, or a spreadsheet), its unit of
   value, and the funding bar it is compared against. If the bar or unit is missing, ask once. If
   the person doesn't know, continue without a bar and skip the break-even column.
2. **Search queries leave the workspace.** Search only for general facts (for example "TB
   treatment mortality drug-susceptible adults"). Never put the grantee's name, the grant amount,
   internal project names, or anything else from the draft into a query. Don't open links in the
   draft that point to internal systems.
3. **Keep the author's framing.** Review the estimate on its own terms first. Do not swap in your
   preferred method; if you think the method is wrong, that is one finding, not a rewrite.

## Step 1: Rebuild the model

- List every parameter: a short snake_case name, value, unit, and basis: `cited` (the draft gives
  a source), `stated` (a number with no source), or `implicit` (an assumption the formula makes
  without saying so, such as no discounting).
- Write the formula chain as ordered steps, then write a spec file and run
  `scripts/botec_check.py spec.json`. The docstring at the top of the script shows the format.
- Compare the rebuilt result with the draft's stated result. A gap over 5% is the first finding:
  an arithmetic slip or a hidden step.
- List the **structural choices** the formula makes: what it counts (deaths only? income?), what
  it leaves out, the time horizon, discounting, and whose costs are in the denominator.

## Step 2: Ranges and what decides the result

- Give each parameter a low and high that a careful reviewer could defend: roughly an 80%
  interval, so you would be surprised, but not shocked, if the true value fell outside it. One
  line of basis each, marked `evidence` or `judgment`. Fixed conventions (such as the funder's
  value per DALY) get no range; the script lists them as fixed.
- Rerun the script. It sorts parameters by how much they move the result and gives each one's
  **break-even**: the value at which the estimate would exactly meet the bar.
- The **decision drivers** are the parameters whose break-even falls inside their plausible
  range, plus the two largest swings. When the result sits close to the bar, many parameters
  qualify. List them all in the output table, but check evidence (Step 3) for the five with the
  largest swing, and mark the rest "not checked".

## Step 3: Check the decision drivers against evidence

For each decision driver (at most five), search for public evidence on its value.

- Cite only pages you actually opened and read, with the number they give. Never cite from memory.
- If you rely on general knowledge without a source, label it "unsourced".
- "Not checkable from public sources" is a normal and useful result. Many BOTEC inputs are the
  author's own judgment or internal data; say so and move the question to Step 6.
- If evidence shifts a range, update the spec and rerun.
- A public record, such as a trial registry entry, may appear to describe the very project
  under review. You may cite it, but say it may or may not be the same project. Find it by
  searching for the intervention, never for the grantee.
- An input with no evidence either way has no direction, so it is not a finding. It stays in
  the decision table, and if it decides the result, name it in the bottom line and add it as a
  question.

## Step 4: Structural issues

Check each item. Keep an issue only if you can express it as a parameter change or a new factor,
compute its effect with the script (use `scenarios`), and it moves the result by more than 10% or
changes which side of the bar it lands on.

- To add a factor the draft leaves out, add it as a parameter at its neutral value (1 for a
  multiplier, 0 for a rate) with a range, and use it in a scenario.
- If the size rests on a figure you chose rather than found, say so and call it illustrative, for
  example "+25% if morbidity adds a quarter to the death DALYs (illustrative)".
- Put supporting calculations that don't feed the result, such as a trial sample size or a
  population rebuilt from public data, in the spec's `checks` list, so their numbers also come
  from the script.
- An issue that turns on the author's own convention or data (whether the framework discounts,
  what the budget covers) is a question for Step 6, not a finding.

- **Missing channels:** benefits or costs the formula leaves out, such as morbidity, spillovers,
  other outputs funded by the same grant, or downstream costs.
- **Double counting** between parameters, for example a success probability and an effect size
  that both discount the same risk.
- **Counterfactual:** what happens without this grant. Is the speedup, share of credit, or
  "would happen anyway" assumption defensible? This often moves the result *up*.
- **Timing:** adoption ramp, time horizon, discounting, and trends in the problem's size.
- **Does success establish what is valued?** For R&D: would the trial's endpoint, if met,
  actually demonstrate the effect the estimate puts a value on?
- **Cost scope matches benefit scope:** all-in costs against all-in benefits, or the funder's
  share against its share.
- **Population:** whether eligibility, uptake and coverage filters are all applied, and only once.

## Step 5: Challenge your own findings

For every finding from Steps 1 to 4, write the best one-sentence reply the author could give.

- If the reply settles it, drop the finding.
- If only the author's information could settle it, move it to Step 6 as a question.
- Check the balance: list which findings raise the estimate and which lower it. If they all point
  one way, look again specifically for the other direction. The goal is an accurate estimate, not a
  case against the grant.
- Mark findings that overlap (two haircuts on the same risk). Never present them as additive.

Keep at most five findings.

## Step 6: Questions for the author

Write the distinct questions that would settle what remains open. Merge questions that one
document or one conversation would answer. For each, say which parameter it affects and how far
the answer could move the result (computed, from the script).

## Output

Write the review in this order. Aim for one to two pages before the appendix; the appendix
doesn't count. Plain language; define any term the author didn't use. If the rebuilt result
matches the stated one, say so in the bottom line.

```
# BOTEC review: [title]

**Bottom line.** [Rebuilt result vs stated. Clears the bar robustly / clears it but depends
on X / does not clear it. The one to three inputs that decide it, each with its break-even.]

## What decides the result
| Parameter | Value | Plausible range | Result at low / high | Break-even | Evidence |
[decision drivers only; Evidence = cited page, "unsourced", or "not checkable publicly"]

## Findings
### 1. [Short title] ([raises / lowers] the estimate, [computed size])
[What and why, in 2-4 sentences, with sources.]
*Likely reply from the author:* [one sentence, and why the finding still stands]

**Balance.** [Which findings and open questions raise the estimate, which lower it, and which
overlap. One or two sentences.]

## Questions for the author
- [ ] [Question] (affects [parameter]; could move the result [range])

## What this review did not check
[Anything outside a single-session review: internal data, the author's sources that weren't
public, independent replication. One line noting this is a structured checklist, not an
independent review.]

## Appendix: model as rebuilt
[Parameter table with basis, formula steps, and the script's output]
```

Rules for the whole review:
- Every number in the findings comes from the script or a cited source. No mental arithmetic.
- No finding without a direction and a size.
- Don't pad. Three solid findings beat eight speculative ones. Zero findings is acceptable if
  the estimate holds up; say so.
