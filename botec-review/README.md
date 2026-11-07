# botec-review

A Claude skill that gives a draft back-of-the-envelope calculation (BOTEC) or cost-effectiveness
estimate a fast, structured second look before a funding decision. It runs inside your own Claude
workspace: nothing to install on your computer, no data sent anywhere new.

What you get, in one or two pages:

- **The arithmetic, rebuilt and run.** A gap between the rebuilt and stated result is flagged.
- **What decides the result.** Each input gets a plausible range and a break-even value: the value
  at which the estimate would just meet your bar. Inputs whose break-even falls inside their
  plausible range are the ones to scrutinize.
- **Evidence on those inputs**, from pages actually opened and cited, or an explicit "not checkable
  from public sources".
- **At most five findings**, each with a direction, a computed size, and the author's likely reply.
- **A checklist of questions for the author** that would settle what's still open.

It is a checklist, not a verdict.

## Install

**Claude (Team or Enterprise).** An admin can add the skill for the whole organization, or each person
can add it themselves, from the skills settings: zip the `botec-review/` folder (the one containing `SKILL.md`) and
upload the zip. It needs code execution turned
on, and web search for the evidence step.

**Use it.** Paste or attach a BOTEC and ask for a review: "Can you review this BOTEC before
Thursday's meeting? Our bar is 2,000x." Claude loads the skill when the request fits.

**Without skills (ChatGPT or a Claude project).** Paste `botec-review/SKILL.md` into the project's
or custom GPT's instructions and upload `scripts/botec_check.py` as a file. The steps work the
same way; the model runs the script with its code tool.

## Data handling

- The review runs in whatever workspace you use it in; the skill adds no service or vendor.
- Web searches leave the workspace. The skill tells the model to search only for general facts
  (an epidemiological rate, a drug interaction) and never to put the grantee, amounts, or internal
  names into a query. Turn web search off for anything too sensitive even for that; the review
  then marks inputs as unchecked.
- The helper script uses the Python standard library only and evaluates formulas with a restricted
  arithmetic parser, not `eval`.

## Limits

- One session, one model. The full multi-agent pipeline this comes from
  (the pipeline in [this repository](../README.md)) separates critique generation,
  evidence checking, quantification and debate into separate agents, and catches more. This skill
  trades some of that for speed and zero setup.
- Inputs that rest on the author's judgment or internal data can't be checked from public sources.
  The review says so and turns them into questions.

## Validation

Tested blind on a published Coefficient Giving sample BOTEC that has a public answer key: the
analysts' own later limitations and revisions. See [validation/](validation/).

## Development

```bash
cd botec-review
python3 -m pytest tests -q     # helper script tests, no API calls
python3 botec-review/scripts/botec_check.py tests/fixtures/tb-statins.json
```
