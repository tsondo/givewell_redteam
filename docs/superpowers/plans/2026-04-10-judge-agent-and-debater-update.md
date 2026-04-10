# Judge Agent + Debater Prompt Update — Implementation Plan

> **Post-implementation notes (2026-04-10):** The plan body below is left intact as a historical artifact. The following annotations bridge it to what actually shipped:
>
> 1. **Shipped as three commits on `main`:**
>    - `b8a1c61` — schema additions (JudgeAudit dataclass, judge_audit + advocate_self_assessment fields on DebatedCritique, backward-compatible from_dict)
>    - `5632fc2` — Advocate + Challenger prompt updates
>    - `14b5f4f` — Judge prompt + `run_judge` + updated `run_adversarial` + parsers + tests
>
> 2. **Background was inaccurate about the Advocate self-assessment.** The plan says the OVERALL ASSESSMENT field "is parsed by the parser currently but not stored anywhere" and later that the parser "discards it entirely." In fact there was no Advocate parser at all — `run_adversarial` held the Advocate response as a raw string (`advocate_raw`) and passed it verbatim to the Challenger's user message. A `parse_advocate_self_assessment(text) -> str` helper was added as part of Commit 3.
>
> 3. **Task 1 Step 3's stop condition was hit and resolved with option (A).** Because the Advocate output was a raw string (per note 2), the plan's "stop and report" instruction fired. The resolution: add a minimal parser for just the OVERALL ASSESSMENT section (no new `AdvocateOutput` dataclass), store the normalized `"strong" | "partial" | "weak"` string on a new `DebatedCritique.advocate_self_assessment` field, and pass it to `run_judge` as a plain string alongside `advocate_raw`. This preserves the calibration metric (Advocate self-rating vs. Judge rating) while staying within the spirit of the stop condition.
>
> 4. **Task 3 also deleted the existing "asymmetric skepticism" instructions in the Challenger prompt.** The plan's Task 3 specified adding the new anti-whataboutism section but did not explicitly call out that the Challenger prompt already instructed the Challenger to *look for* asymmetric skepticism (in the Principles section AND in "Your Task" step 2). Both were deleted because they directly contradict the new section. No parallel instruction existed in the Advocate prompt.
>
> ---

> **For Claude Code:** Use targeted `str_replace` edits, not full file rewrites. No API access required for any task in this plan. The re-run of VAS happens in a separate later plan after the synthesizer fix also lands — this plan only implements and tests the judge agent and debater prompt changes. This project commits directly to main; do not create branches.

**Goal:** Replace the structurally biased "Challenger assigns verdict" pattern with a neutral judge agent, AND update the Advocate and Challenger prompts to prevent the specific failure modes identified by domain expert review (unsupported numerical estimates, whataboutism, calls to ignorance, strawmanning, generic recommendations). The judge produces an explicit audit of debate quality alongside the verdict, giving you a structured calibration metric for the first time.

**Architecture:** Three API calls per critique instead of two: Advocate (Sonnet) → Challenger (Sonnet) → Judge (Opus). The Challenger no longer assigns `surviving_strength` or `recommended_action` — the Judge does both, with explicit justification tied to specific debate moves. The Advocate's existing self-assessment field (currently parsed but discarded) becomes input to the Judge as context. Schema gains a new `judge_audit` field on `DebatedCritique` with backward-compatible default for loading old runs.

---

## Background

**The structural finding (yesterday):** The current adversarial stage has the Challenger — the agent whose prompted role is to *argue for the critique* — also assign the `surviving_strength` verdict. This is not adversarial; it's one party arguing both sides while wearing a neutral hat for the verdict. Across four runs the survival rates are 87% / 100% / 97% / 100%. The Advocate also produces a self-assessment of its own defense quality that the parser currently discards entirely.

**The substantive findings (domain expert review of VAS adversarial transcripts):** A research-experienced reviewer identified six recurring failure modes in the debates:

1. **Unsupported numerical estimates traded as substantive.** Both sides invent numbers and trade them. Each correctly identifies the opponent's number as unsupported, then offers an equally unsupported counter. The dialogue flags the problem ("pure assertion without supporting analysis") without solving it.
2. **Whataboutism.** "The Advocate employs asymmetric skepticism here. They demand strong evidence for X while GiveWell's own Y rests on untested Z." This is true but irrelevant — asymmetry is structurally guaranteed by the prompts. Pointing to a separate weakness in the opponent's position is not engaging with the argument at hand.
3. **Calls to ignorance.** "This could be rapid degradation once the threshold is crossed." We don't know X, therefore X might be Y. Not an argument.
4. **Strawmanning by misreading.** Worked example: Advocate said vitamin A *stores* decline gradually; Challenger demanded evidence for the claim that *protection* declines gradually — a claim the Advocate never made. The Challenger then mixed this misreading with valid arguments, making the response look substantive while containing a category swap at its core.
5. **Equivocal conclusions delivered in definitive tone.** "The magnitude remains uncertain, but even conservative estimates suggest material impact." Hedges and asserts simultaneously.
6. **Generic "investigate further" recommendations.** Every critique gets one because each is reasoned about in isolation. The reviewer's framing: *the game is what we can conclude from what we currently have*, not what could in principle be investigated.

The reviewer also flagged a substantive misreading in one debate (the 9-59x cost-effectiveness exchange — Advocate argued residual effectiveness still justifies funding even at 40% reduction; Challenger responded "wide range shows high sensitivity," which is both irrelevant to the Advocate's point AND technically wrong because range alone doesn't measure sensitivity).

**Out of scope for this plan:**
- Synthesizer changes (separate plan, will follow this one)
- Conclusions doc update (separate task, after this lands)
- The "investigate further" trap at the synthesizer level (also next plan — that's a portfolio-selection problem the synthesizer should solve, not the per-critique judge)

---

## File Map

| Action | File | Responsibility |
|--------|------|----------------|
| Modify | `pipeline/schemas.py` | Add `judge_audit` field to `DebatedCritique`; add `JudgeAudit` dataclass; add `advocate_self_assessment` field |
| Modify | `prompts/adversarial-advocate.md` | Sourcing requirements, derivation requirements, anti-whataboutism, structured format |
| Modify | `prompts/adversarial-challenger.md` | Same, plus require restating opponent's claim before responding, REMOVE verdict assignment instructions |
| Create | `prompts/adversarial-judge.md` | Full judge agent prompt |
| Modify | `pipeline/agents.py` | Add `run_judge` function; modify `run_adversarial` to call judge; update parsers |
| Modify | `pipeline/run_pipeline.py` | No changes expected (run_adversarial encapsulates the new flow), but verify |
| Modify | `tests/test_agents.py` | Tests for judge parser, schema backward compatibility, debater prompt loading |

---

## Task 1: Schema updates

**Files:**
- Modify: `pipeline/schemas.py`

- [ ] **Step 1: Add the `JudgeAudit` dataclass**

The judge produces a structured audit of failure modes detected on each side, plus the verdict and recommended action. Define a dataclass that captures all of this.

```python
@dataclass
class JudgeAudit:
    """Structured audit of an adversarial debate by the neutral judge agent.

    Produced by run_judge after Advocate and Challenger have completed their
    exchange. The verdict and recommended_action fields supersede any values
    the Challenger may have produced in its own output.
    """
    # Failure modes detected, by side
    advocate_failures: list[str]  # e.g., ["unsupported_estimate_counter: 10-25% offered without derivation"]
    challenger_failures: list[str]
    # Verdict with explicit justification
    surviving_strength: str  # "strong" | "moderate" | "weak"
    verdict_justification: str  # 2-4 sentences citing specific debate moves
    # Recommended action with feasibility
    recommended_action: str  # concrete, NOT "investigate further" alone
    action_feasibility: str  # "actionable_now" | "requires_specified_evidence" | "open_question"
    # Honest summary of what the debate established
    debate_resolved: str  # 1-2 sentences on what (if anything) the debate settled
    debate_unresolved: str  # 1-2 sentences on what remains contested
```

- [ ] **Step 2: Add `judge_audit` field to `DebatedCritique`**

The existing `DebatedCritique` class has `surviving_strength`, `key_unresolved`, `recommended_action` fields populated by the Challenger. Keep those fields for backward compatibility with old run JSONs, but add a new `judge_audit` field of type `JudgeAudit | None`. When the judge produces a verdict, the `surviving_strength` and `recommended_action` fields on `DebatedCritique` should be populated *from* the judge audit, not from the Challenger.

```python
# In DebatedCritique:
judge_audit: JudgeAudit | None = None  # None for old runs without judge
```

The default of `None` makes loading old `05-adversarial.json` files backward-compatible — they simply won't have the field.

- [ ] **Step 3: Add `advocate_self_assessment` field to whatever schema holds the parsed Advocate output**

Currently the Advocate's "OVERALL ASSESSMENT: Strong/Partial/Weak defense" line is parsed by the parser but not stored anywhere. Find where Advocate output is held (likely a dataclass or dict in `agents.py`) and add a field for `advocate_self_assessment: str`. This field will be passed to the judge as context.

If the Advocate output is currently held as a raw string and not parsed at all, **stop and report** — that's a bigger refactor than this plan accommodates and we should discuss.

- [ ] **Step 4: Verify schemas import cleanly and serialize/deserialize**

Run a quick round-trip test: construct a `JudgeAudit`, wrap it in a `DebatedCritique`, serialize to JSON, parse back, confirm equality. Also verify that loading an *existing* `results/vas/05-adversarial.json` (which has no `judge_audit` field) still works without error.

---

## Task 2: Update the Advocate prompt

**Files:**
- Modify: `prompts/adversarial-advocate.md`

- [ ] **Step 1: Read the current prompt**

Understand what's there before editing. Note any sections that need to remain (the role definition, the input format description) and what needs to change.

- [ ] **Step 2: Add a "Sourcing requirements" section**

Insert this section near the top of the rules, before any output format instructions:

```markdown
## Sourcing requirements (these are non-negotiable)

When you make any factual claim about evidence, literature, or empirical
findings, you MUST do one of the following:

1. **Cite a specific source** — paper, study, report, or dataset by name
   and year if known. The Verifier has already grounded much of the relevant
   evidence base for this critique; draw from that evidence package.

2. **Show your derivation** — when you produce a numerical estimate that
   isn't directly attested by a single source, show the synthesis chain
   explicitly. The chain must trace from grounded components (cited sources
   or items in the verifier evidence package) to your number, with each
   step inspectable.

   Acceptable: "The Cochrane meta-analysis shows 11% mortality reduction
   post-DEVTA, down from ~24% in pre-DEVTA meta-analyses (verifier evidence
   item N). The effective range is therefore approximately 11-24%. My
   midpoint estimate of ~18% is the average of the bounds, appropriate
   when I don't have a principled reason to weight one over the other."

   Unacceptable: "I estimate 10-25%" with no chain shown. Also unacceptable:
   "Studies suggest 10-25%" with no specific studies cited. Also
   unacceptable: a chain that mentions sources but doesn't actually follow
   from them ("the meta-analysis shows X, therefore the threshold is Y"
   when X doesn't entail Y).

3. **Explicitly disclaim** — if you cannot ground a claim and cannot show
   a derivation, say "I cannot ground this; treat as uninformed prior"
   rather than asserting it.

Producing a confident-sounding number without grounding it OR without
showing a sound derivation chain is the single most common failure mode
in this stage. The Judge will flag three distinct sub-cases: fabricated
numbers (no components, no chain), pseudo-derivations (components cited
but chain doesn't follow), and unsupported counter-estimates offered to
neutralize the opponent's number. Synthesized estimates with sound chains
are NOT failures — but the synthesis quality becomes a legitimate target
of substantive debate.
```

- [ ] **Step 3: Add an "Anti-whataboutism" section**

```markdown
## Engage with the argument, not the opponent's overall position

Your job is to defend GiveWell's position on the specific critique in
front of you. When the Challenger raises a point, address that point
directly. Do not respond by pointing out separate weaknesses elsewhere in
the Challenger's overall argument or in critiques of GiveWell more broadly.

Specifically forbidden moves:
- "The Challenger demands evidence for X but ignores that GiveWell's Y
  also lacks rigorous testing." This is whataboutism even if true.
- "While the Challenger raises a valid concern about A, they should also
  consider B." If B isn't part of your defense of the specific point,
  it's deflection.
- Any sentence of the form "the Challenger employs [asymmetric skepticism /
  selective rigor / inconsistent standards]." Asymmetry is structurally
  guaranteed by your roles. Pointing it out is true but useless.

When you cannot defend against a specific point, the correct move is to
concede that specific point and pivot to whether the conceded weakness is
material to the overall cost-effectiveness conclusion. Concession on a
specific point is not concession on the critique.

## Engage with unverified claims as conditional arguments

When the Challenger raises a claim that the Verifier did not directly
verify, that does NOT make the claim false or empty. UNVERIFIABLE means
"the verifier could not find direct evidence either way" — it does not
mean "no underlying data exists" or "the claim has been disproven."

When responding to such a claim, engage with it conditionally: "If the
Challenger's claim about X is correct, does it follow that Y?" The
Challenger's argument may still be sound or unsound under that conditional
structure, and that is the substantive question.

Specifically forbidden moves:
- "The Challenger's claim has no data" when the verifier evidence package
  contains components that could support the claim through synthesis
- "There is no evidence for X" when the verifier marked X as UNVERIFIABLE
  (which means "could not find direct evidence," not "the claim is false")
- Treating absence of direct attestation as positive evidence of falsity

The Judge will flag these moves as misrepresentation of evidence status.
The correct move when facing an unverified opposing claim is to engage
with the conditional structure or to explicitly note that you accept it
arguendo and respond to its implications.
```

- [ ] **Step 4: Add structured format guidance**

```markdown
## Format

Use discrete numbered or bulleted points wherever possible. A single
discrete claim per bullet is easier to evaluate (and harder to hide
weak reasoning inside) than a long compound sentence with multiple
hedges. Reserve prose for connecting tissue between claims, not for
the claims themselves.

When you must hedge (because evidence is genuinely mixed), state the
hedge explicitly: "Evidence is mixed: [study A] found X, [study B]
found ¬X. I lean toward X because [specific reason]." Do not produce
hedges of the form "the magnitude remains uncertain, but even conservative
estimates suggest material impact" — this hedges and asserts in the same
breath, and the Judge will flag it as false definitiveness.
```

- [ ] **Step 5: Update the OVERALL ASSESSMENT instructions**

The Advocate currently produces an "OVERALL ASSESSMENT: Strong/Partial/Weak defense" field. Keep this — it now becomes input to the Judge. But add an instruction: the assessment must be honest, not strategic. If your defense is weak, say weak. The Judge sees both your assessment and your actual defense; producing a confident self-assessment of a weak defense will be flagged as a calibration failure, not rewarded.

---

## Task 3: Update the Challenger prompt

**Files:**
- Modify: `prompts/adversarial-challenger.md`

- [ ] **Step 1: Read the current prompt**

- [ ] **Step 2: Add the same Sourcing requirements section as the Advocate**

Identical content. Both sides are subject to the same standards. Adapt only the role-specific framing if needed.

- [ ] **Step 3: Add the same Anti-whataboutism and unverified-claims sections**

Identical content to the Advocate version, adapted to the Challenger's role: when the Advocate raises a defense, address that defense directly. Don't deflect to separate weaknesses in GiveWell's broader methodology. Same for unverified claims — when the Advocate dismisses something with "no data," check whether the verifier actually marked it UNVERIFIABLE versus REJECTED, and if UNVERIFIABLE, point out that the dismissal misrepresents the evidence status.

- [ ] **Step 4: Add a "Restate before responding" requirement**

This is the fix for the strawmanning failure mode. Add:

```markdown
## Restate the Advocate's claim before responding to it

For each Advocate claim you intend to rebut, BEGIN your response to that
claim by restating the Advocate's claim in your own words. Then respond.

This is not a stylistic preference. It is required to prevent the failure
mode of rebutting a claim the Advocate didn't actually make. In one
documented case from a prior run, the Advocate stated that vitamin A
*stores* decline gradually; the Challenger demanded evidence for the claim
that *protection* declines gradually — a claim the Advocate never made.
Restating the Advocate's actual claim before responding would have
surfaced the category swap before it became a rebuttal.

Format:
> The Advocate claims: [their claim, in your own words]
>
> Response: [your rebuttal]

If, in the act of restating, you realize you misread the Advocate, fix
your understanding before responding. Do not produce a rebuttal to a
claim you cannot accurately restate.
```

- [ ] **Step 5: REMOVE the verdict assignment section**

The Challenger currently produces "SURVIVING STRENGTH: Strong/Moderate/Weak" and "RECOMMENDED ACTION: ..." sections. Remove these instructions entirely. The Judge agent now produces both.

Replace with a brief explanation:

```markdown
## You do not assign the verdict

A neutral Judge agent will read your rebuttal alongside the Advocate's
defense and determine the surviving strength of the critique and the
recommended action. Do not produce SURVIVING STRENGTH or RECOMMENDED
ACTION sections. Focus entirely on the substance of your rebuttal.
```

- [ ] **Step 6: Add the same Format section as the Advocate**

Bullet-point preference, explicit hedging requirement.

---

## Task 4: Create the Judge prompt

**Files:**
- Create: `prompts/adversarial-judge.md`

- [ ] **Step 1: Write the prompt**

```markdown
# Adversarial Debate Judge

## Role

You are a neutral judge evaluating the quality of a structured debate
about a methodological critique of a cost-effectiveness analysis. You
did not participate in the debate. Your job has two parts:

1. **Audit the debate quality.** Identify specific reasoning failures
   on both sides using the failure mode definitions below. Be willing
   to flag failures even when the overall side made some valid points.
2. **Assess what the debate established.** Based on the substance of
   the exchange (not the rhetorical confidence of either side), what
   has the debate resolved, what remains contested, and what is the
   appropriate verdict on the critique's surviving strength?

You read both sides with equal skepticism. The Advocate and Challenger
are advocates for opposing positions by design; you are not.

## Inputs

You will receive:

1. The original critique (title, hypothesis, mechanism)
2. The verifier's evidence package (what was checked, what was found,
   what was contradicted)
3. The Advocate's defense, including their own self-assessment of
   defense quality
4. The Challenger's rebuttal

## Failure modes to detect

For each failure mode below, scan both the Advocate's and Challenger's
output. Report each detected instance in the audit. A side can have zero,
one, or multiple instances of each.

### 1. Unsupported numerical estimate

A specific number (percentage, magnitude, range, multiplier) that lacks
sound grounding. This category has three sub-cases that should be
distinguished in your audit:

**1a. Fabricated number.** No source cited and no derivation shown. The
number appears as if from nowhere. Worst form. "I estimate 10-25%" with
nothing else.

**1b. Pseudo-derivation.** Sources are cited or referenced but the
synthesis chain doesn't actually follow from them. Looks grounded but
isn't. Also a clear failure. "The Cochrane meta-analysis shows X, therefore
the threshold is Y" when X does not entail Y.

**1c. Unsupported counter-estimate.** A number offered specifically to
counter the opponent's number, but with the same grounding deficiencies
as 1a or 1b. Common in this stage because each side tries to neutralize
the other's number with a competing one. Flag both numbers, not just one.

NOT a failure mode: synthesized estimates with sound derivation chains.
If a debater takes grounded components from the verifier evidence package
and synthesizes them into a number with each step shown, that's
legitimate analysis. The synthesis quality is then a legitimate target of
substantive debate (does the chain actually follow? are the components
weighted appropriately?), but it is NOT a failure mode in itself. In your
audit, when you encounter a sound synthesis, note it explicitly so the
verdict reflects that the debate engaged with substantive analysis rather
than guess-trading.

When in doubt between 1b (pseudo-derivation) and a substantive synthesis
disagreement, default to flagging it as 1b only when the chain has a
clear logical gap. If the chain is debatable but defensible, treat it as
substantive analysis and let the verdict reflect whether the opposing
side engaged with the substance.

Both sides are equally subject to this — flag the Advocate's unsupported
numbers and the Challenger's unsupported counter-numbers.

### 2. Whataboutism
Deflecting from the opponent's specific argument by pointing to a
separate weakness in their broader position. "They demand strong evidence
for X while their own Y rests on untested Z." This is true-but-irrelevant
and does not address the argument at hand. Asymmetric skepticism is
structurally guaranteed by the debater roles; pointing it out is not
engagement.

### 3. Call to ignorance
Arguing X might be true because we don't know it isn't. "This could be
rapid degradation once the threshold is crossed." Absence of evidence
treated as evidence of presence. The correct move when evidence is absent
is to acknowledge the gap, not to fill it with speculation.

### 4. Strawmanning / category swap
Rebutting a claim the opponent didn't make. The most common form is a
category swap: opponent said X about A, response treats it as a claim
about B. Worked example from a prior run: Advocate said vitamin A *stores*
decline gradually; Challenger demanded evidence for the claim that
*protection* declines gradually. The Challenger response was a rebuttal
to a claim that was never made.

### 5. False definitiveness
An equivocal conclusion delivered in confident language. "The magnitude
remains uncertain, but even conservative estimates suggest material
impact." This hedges and asserts simultaneously. Either commit to an
estimate with a derivation, or acknowledge that the magnitude is genuinely
unknown — but do not do both in one breath while sounding decisive.

### 6. Generic recommendation
A "needs further investigation" or "more research required" recommendation
without specifying what investigation, what evidence would settle the
question, or whether collecting that evidence is feasible. The default
recommendation should be "based on this debate, here is what we can
conclude now"; investigation recommendations are acceptable only when
specific and feasible.

### 7. Misrepresenting evidence status

Treating an unverified claim as if it were a disproven claim. The verifier's
UNVERIFIABLE verdict means "we could not find direct evidence either way" —
it does NOT mean "the claim is false" or "there is no underlying data."

Common forms:
- "The opponent's number has no data" when the verifier evidence package
  contains components from which the number can be synthesized (often
  pairs with failure mode 1c — both flag at once)
- "There is no evidence for X" when the verifier marked X as UNVERIFIABLE
  rather than REJECTED
- Treating absence of direct attestation as positive evidence of falsity

The correct move when facing an unverified claim is to engage with it as
a conditional argument: "If we accept the claim that X (which the verifier
could not directly verify), does it follow that Y?" The argument may still
be sound or unsound under that conditional structure, and that is the
substantive question worth debating.

Do not flag this when:
- A debater explicitly notes "this is unverified, but conditional on it..."
  and then engages with the conditional argument
- A debater correctly distinguishes UNVERIFIABLE from REJECTED
- A debater states they accept the claim arguendo and engages with its
  implications

## Output format

Produce your audit in the following structure. Use exactly these section
headers so the parser can extract them.

```
## ADVOCATE FAILURES

[List each detected failure mode with a brief quote or paraphrase showing
where it appeared. If none, write "(none detected)". Be willing to find
zero failures if the side reasoned cleanly.]

- failure_type: [one of: unsupported_estimate_fabricated,
  unsupported_estimate_pseudo, unsupported_estimate_counter, whataboutism,
  call_to_ignorance, strawmanning, false_definitiveness, generic_recommendation,
  misrepresenting_evidence_status, sound_synthesis_noted]
  evidence: [brief quote or paraphrase]

## CHALLENGER FAILURES

[Same format]

## DEBATE RESOLVED

[1-2 sentences on what, if anything, this debate has actually established.
Resist the temptation to say nothing was established. Often a debate does
narrow the question even when it doesn't settle it. If the debate truly
established nothing, say so plainly.]

## DEBATE UNRESOLVED

[1-2 sentences on what remains genuinely contested after this exchange.
This is different from "what could in principle be investigated" — only
include items where the exchange itself surfaced an unresolved question.]

## SURVIVING STRENGTH

[One of: strong, moderate, weak]

Justification: [2-4 sentences citing specific moves from the debate.
"Strong" requires the Challenger to have made grounded arguments the
Advocate could not adequately defend. "Weak" means the critique mostly
survived because the debate was unproductive (heavy use of unsupported
estimates, whataboutism, or strawmanning), not because the critique itself
was strong. "Moderate" is the appropriate middle when both sides made
some grounded arguments and the substantive question remains open.]

Important: A debate full of failure modes on both sides should usually
produce a "weak" verdict, not a "moderate" one, because the debate didn't
do the work of testing the critique. The verdict reflects what the *debate*
established, not what *might be true*.

## RECOMMENDED ACTION

[Concrete and feasible. NOT "investigate further" alone. The format is one
of:]

1. CONCLUDE NOW: [Specific conclusion the debate supports, with confidence
   level. "Based on this exchange, the critique appears to overstate the
   magnitude; the underlying concern remains valid but the quantitative
   claim does not survive."]

2. SPECIFIC INVESTIGATION: [Exactly what evidence would change the answer,
   and whether collecting it is realistic. "Re-run the verifier with
   targeted searches for serum retinol studies in [specific countries];
   this is feasible within existing tooling."]

3. OPEN QUESTION: [Acknowledge that the debate did not resolve the question
   and the path to resolution is not clear. Use this only when neither of
   the above applies.]

action_feasibility: [one of: actionable_now, requires_specified_evidence,
open_question]
```

## Critical reminders

- You are not running the debate. You are evaluating it.
- Penalize critiques where the Challenger's strongest moves relied on the
  failure modes above, even if the underlying critique might be true.
  The verdict reflects the quality of *this debate*, not the quality of
  the underlying claim.
- Penalize critiques where the Advocate had valid moves available that
  they didn't make. (When you can identify a missed defense, name it
  briefly in the audit — this is high-value calibration data.)
- Consider the Advocate's self-assessment as one input among many. You
  may use it as a signal but you are not bound by it. If the Advocate
  rated their own defense "Strong" but you assess it as weak, say so.
- Your verdict and recommended action SUPERSEDE any verdict-like content
  the Challenger may have produced. Ignore the Challenger's self-assessment
  entirely if present.
```

- [ ] **Step 2: Verify the prompt file is well-formed**

Read it back, confirm markdown headers are intact, no orphaned sections.

---

## Task 5: Add `run_judge` function and update `run_adversarial`

**Files:**
- Modify: `pipeline/agents.py`

- [ ] **Step 1: Add a `parse_judge_output` function**

The judge produces a structured response with section headers (`## ADVOCATE FAILURES`, `## CHALLENGER FAILURES`, etc.). Parse these into a `JudgeAudit` dataclass. Use the same regex-on-section-headers pattern that other parsers in the file use.

For the failure lists, parse the per-bullet format (`failure_type: ...` / `evidence: ...`) into a list of strings or a list of dicts — whichever matches the schema field type.

Apply the lesson from the verifier batch parser bug: dedupe matches on section header, take the first occurrence.

- [ ] **Step 2: Add a `run_judge` function**

Signature roughly:

```python
def run_judge(
    critique: VerifiedCritique,  # original + verifier evidence
    advocate_output: AdvocateOutput,  # parsed advocate response
    challenger_output: ChallengerOutput,  # parsed challenger response
    stats: PipelineStats,
    intervention: str,
) -> JudgeAudit:
```

Inside:
- Load `prompts/adversarial-judge.md` as system prompt
- Construct the user message with all four input sections clearly labeled
- Call the API with `OPUS_MODEL` and a reasonable max_tokens (suggest 4096 — the audit is structured but not huge)
- Parse the response with `parse_judge_output`
- Return the `JudgeAudit`

Use the same `call_api` helper that other stages use, with stage name like `judge-N` so it appears in `pipeline-stats.json`.

- [ ] **Step 3: Modify `run_adversarial` to call the judge**

The current flow per critique is:
1. Call Advocate
2. Call Challenger
3. Build `DebatedCritique` from Challenger's parsed output

The new flow is:
1. Call Advocate (parse including the previously-discarded self-assessment field)
2. Call Challenger (no longer parses surviving_strength or recommended_action — those parsing calls should be removed or commented as unused)
3. Call Judge with all of the above as inputs
4. Build `DebatedCritique` with `judge_audit` populated AND with `surviving_strength` / `recommended_action` set from the judge audit, NOT from the Challenger

Be careful: the existing `parse_challenger_output` function may be called in places other than `run_adversarial`. Check before removing the surviving_strength parsing — if it's used elsewhere, leave it in place but mark it as advisory and add a comment that the value is no longer used downstream.

- [ ] **Step 4: Verify the new flow imports and the existing tests still pass**

This is a structural change. Some tests may fail because they expected the old behavior. Document any test failures explicitly — do NOT modify tests yet, that's Task 7. Just confirm what breaks and why.

---

## Task 6: Update `run_pipeline.py`

**Files:**
- Modify: `pipeline/run_pipeline.py` (probably)

- [ ] **Step 1: Verify whether changes are needed**

`run_adversarial` is supposed to encapsulate the new flow internally. If the orchestrator just calls `run_adversarial(...)` and saves the result, there should be no changes needed at the orchestrator level. Confirm this by reading the relevant section.

If the orchestrator does anything stage-specific (e.g., logs a stage count, expects two API calls per critique), update accordingly.

- [ ] **Step 2: Verify the pipeline imports cleanly**

---

## Task 7: Tests

**Files:**
- Modify: `tests/test_agents.py`
- Modify: `tests/test_schemas.py` if it exists

- [ ] **Step 1: Schema backward compatibility test**

Construct a `DebatedCritique` JSON the way an old run would have produced it (no `judge_audit` field). Confirm it loads without error. Then construct one with a `judge_audit` and confirm it round-trips correctly.

- [ ] **Step 2: Judge parser test**

Hand-craft a fake judge response that contains all six output sections in the expected format. Call `parse_judge_output`. Assert the resulting `JudgeAudit` has the expected fields populated with the expected values.

Include at least one test case with multiple failure modes detected on each side, and one with `(none detected)` on both sides, to exercise the parser's empty-list handling.

- [ ] **Step 3: Update or replace tests that assumed the old Challenger-assigns-verdict flow**

Some tests probably assert that `surviving_strength` came from a Challenger output. These need to be updated to assert it comes from a judge audit. Where the old test was structurally sound, modify it. Where the old test no longer makes sense (e.g., asserted the Challenger parser populated `surviving_strength`), delete it and add a comment in the commit message explaining what was removed.

- [ ] **Step 4: Run the full test suite**

All tests should pass. If anything fails after Tasks 1-7 are complete, **stop and report**.

---

## Task 8: Commit

The plan should produce roughly 3 commits, in this order:

1. **Schema additions** (`schemas.py` + tests for backward compat)
2. **Debater prompt updates** (`adversarial-advocate.md` + `adversarial-challenger.md`)
3. **Judge agent implementation** (`adversarial-judge.md` + `agents.py` changes + judge parser test)

Each commit message should reference the domain expert review that motivated the change (the teacher's feedback) and the structural finding that the Challenger was assigning its own verdict. Use Co-Authored-By trailers as standard.

---

## Stop Conditions Requiring Tsondo Input

- Advocate output is currently held as a raw string and not parsed at all (Task 1 Step 3)
- A test fails for reasons not addressed by Task 7
- Removing the Challenger's verdict-assignment parsing breaks code in places other than `run_adversarial`
- Any concrete CEA class or downstream stage turns out to depend on the old `surviving_strength`-from-Challenger flow in a non-obvious way

## Things You Should NOT Do

- Modify the synthesizer prompt (separate plan, follows this one)
- Modify the conclusions doc (separate task, after the synthesizer plan and re-run land)
- Re-run any pipeline stages — the re-run happens in a later plan after the synthesizer fix is also in place, so a single re-run captures both fixes at once
- Activate the API key — no task in this plan requires it
