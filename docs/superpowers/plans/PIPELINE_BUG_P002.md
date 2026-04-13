# Pipeline Investigation P-002: Synthesizer Tags Finding as CONDITIONAL Without Linker Support

**Status:** Investigated — Cause A confirmed (synthesizer prompt-following failure); Cause C confirmed as underlying design gap (see P-003)
**Severity:** Low (cosmetic in current VAS output; prompt fixes prevent recurrence)
**Target repo:** `givewell_redteam`
**Affected stages:** 06-synthesizer (prompt-following failure). 05b-linker is NOT at fault. Schema/architecture gap documented in P-003.

## Observation

In the VAS run, the synthesizer marked Finding 5 as `[CONDITIONAL — see
dependencies]` and wrote a "Conditional on:" field referencing an
unverified claim:

```
### Finding 5: Proxy Weight Distribution Invalidated by Micronutrient
Program Rollouts [CONDITIONAL — see dependencies]
**Impact:** Even a 30% overestimate in VAD prevalence would inflate
cost-effectiveness by ~9x for high-rated locations like DRC.
**Evidence:** Mali and DRC implement VAS alongside other vitamin A
programs but lack recent nationally-representative VAD data...
**Conditional on:** the unverified claim that micronutrient programs
systematically reduce VAD prevalence beyond what proxy indicators
suggest (rejected critique title).
```

But:

1. The linker output (`05b-linker.json`) contains **no `depends_on`
   relationship** for "Proxy Weight Distribution Invalidated by
   Micronutrient Program Rollouts."
2. The synthesizer's own "Conditional Findings" section, further down
   in the same report, states "(no findings depend on unverified
   claims in this run)" — directly contradicting its own CONDITIONAL
   tag on Finding 5.
3. **However**, the conditional claim the synthesizer references is
   not entirely absent from upstream data. The investigator's mechanism
   for this same critique reads:

   > "If micronutrient programs have reduced VAD prevalence beyond
   > what the proxy indicators suggest, GiveWell would overestimate
   > current VAD rates."

   And the verifier marked this critique as VERIFIED with reasoning
   that includes: "Both DRC and Mali have implemented micronutrient
   interventions... which **could** reduce VAD prevalence
   independently of changes in stunting, wasting, or poverty."

   So the conditional structure exists in the upstream data. It's just
   embedded in the surviving critique's own mechanism, not represented
   as a separate dependency edge.

This is what makes the diagnosis ambiguous and worth investigating
before writing prompt fixes.

## Three plausible root causes

In rough order of likelihood, but the real distribution is unknown
without investigation:

### Cause A: Synthesizer over-reach (categorization error)

The synthesizer correctly noticed that Finding 5 rests on a
conditional ("IF micronutrient programs reduce VAD beyond proxies"),
but mis-categorized this as a dependency on a separately-investigated
rejected critique rather than recognizing it as the surviving
critique's own internal IF/THEN structure.

Symptoms consistent with this:
- The conditional content is real and grounded in the critique's
  mechanism.
- The literal placeholder text `(rejected critique title)` was
  emitted, suggesting the synthesizer tried to fill in a citation
  slot it couldn't satisfy.
- The synthesizer's later "Conditional Findings" section correctly
  reflects the linker's empty depends_on output.

### Cause B: Linker omission

The linker should have detected that the surviving critique's
mechanism contains an unverified conditional, and emitted a
self-referential or special-form dependency, but didn't. The
synthesizer correctly noticed the gap and tried to compensate.

Symptoms consistent with this:
- The conditional structure in the critique's mechanism is real and
  load-bearing for the finding.
- The linker prompt only describes linking surviving critiques to
  separately-investigated rejected critiques. There is no provision
  for representing conditionals embedded in a critique's own mechanism.

### Cause C: Architectural gap (neither stage's fault)

The pipeline does not currently model intra-critique conditionals at
all. The linker's `depends_on` relationship is between two distinct
critiques. A critique whose own IF/THEN mechanism contains an
unverified clause has no place to express that. The synthesizer is
trying to surface a real epistemic structure that the schema doesn't
support, and necessarily fails at it.

Symptoms consistent with this:
- Same observable symptoms as A and B.
- This is the case where the fix is at the schema/architecture level,
  not in any single prompt.

## Investigation results (2026-04-13)

Investigation performed by reconstructing stage inputs from the
orchestrator code (`pipeline/agents.py`), since `pipeline.log` records
metadata (token counts, costs, stage transitions) but not full input
payloads.

### Task 1: Linker's input — what it received and what it had to work with

Source: `run_linker()` at `agents.py:1895-1951`.

**The linker received Finding 5's full mechanism**, including the IF
clause: "If micronutrient programs have reduced VAD prevalence beyond
what the proxy indicators suggest, GiveWell would overestimate current
VAD rates."

**The 4 rejected critiques the linker received:**

| # | Title | Verdict |
|---|-------|---------|
| 1 | Seasonal and Campaign-Timing Cost Variations Not Reflected | unverified |
| 2 | Short-Term Protection Window Creating Mortality Displacement | rejected |
| 3 | Threshold Effects for Herd Protection in High-Mortality Settings | unverified |
| 4 | Accelerating Benefits from Immunological Priming Effects | rejected |

**None of these match "micronutrient programs systematically reduce
VAD prevalence beyond what proxy indicators suggest."** The closest
is #3 (Threshold Effects for Herd Protection), which concerns
community-level herd protection thresholds — a different mechanism
entirely.

**Conclusion:** The linker had no rejected critique to link to for
Finding 5's conditional claim. A `depends_on` edge was structurally
impossible. **This rules out Cause B** (linker omission) and confirms
the gap is upstream of the linker.

### Task 2: Synthesizer's input — what it saw

Source: `_build_synthesizer_user_message()` at `agents.py:2090-2187`.

The synthesizer received both:
- The full surviving critique data including mechanism text with its
  IF clause (in the "Surviving Critiques" section)
- The linker's dependency block (in the "Critique Dependencies" section)

The dependency block the synthesizer received contained 3 entries:

```
- surviving: Threshold Effects Below Critical VAD Prevalence Levels
  rejected: Threshold Effects for Herd Protection... (verdict: UNVERIFIABLE)
  relationship: engages_with (confidence: medium)
- surviving: Meta-Analysis Publication Bias in Historical Evidence Base
  rejected: Short-Term Protection Window... (verdict: REJECTED)
  relationship: contradicts (confidence: high)
- surviving: Systematic Timing Delays Between Supplementation Rounds
  rejected: Seasonal and Campaign-Timing Cost Variations... (verdict: UNVERIFIABLE)
  relationship: engages_with (confidence: medium)
```

**"Proxy Weight Distribution" does not appear in this block at all** —
not as `depends_on`, not as `engages_with`, not in any form. And
critically, **none of the 3 dependencies use the `depends_on`
relationship type** — they are all `engages_with` or `contradicts`.

The synthesizer had unambiguous evidence that Finding 5 had no
dependency. The runtime input matches the prompt's expected sections.

### Task 3: Synthesizer prompt rules — unambiguous

Two rules in `prompts/synthesizer.md` govern CONDITIONAL tagging:

> **Line 112-114:** "The `[CONDITIONAL — see dependencies]` tag in the
> Finding header is only added if at least one `depends_on` dependency
> for this title exists in the Critique Dependencies input. Otherwise
> omit the tag entirely."

> **Lines 206-209:** "`engages_with` and `contradicts` relationships
> do NOT make a finding conditional — they are informational only and
> should not trigger this section."

These rules are clear, explicit, and leave no room for a broader
reading of "dependency." **The synthesizer violated a clear rule.**
This is Cause A strong form — a prompt-following failure.

The self-contradiction is revealing:
1. The synthesizer **correctly** applied the rule in the "Conditional
   Findings" section → "(no findings depend on unverified claims in
   this run)"
2. The synthesizer **incorrectly** ignored the rule when producing
   Finding 5's header tag earlier in the document

The failure is positional: the header was generated first, before the
model reached the section where it cross-checked against the linker's
structured output. By then, the CONDITIONAL tag was already committed.

### Task 4: Placeholder text in other findings

- `(rejected critique title)` appears **only once** across all runs:
  VAS Finding 5.
- The other three runs (water-chlorination, itns, smc) **predate the
  linker stage** — none have `05b-linker.json` or any CONDITIONAL
  tagging mechanism.
- VAS is the only run where this failure could have occurred. Sample
  size is n=1; cannot determine whether recurring or isolated.
- The placeholder leak is consistent with the synthesizer trying to
  fill a citation slot it couldn't satisfy — it noticed the IF clause
  in the mechanism, tagged it CONDITIONAL, then couldn't find a
  rejected critique title to substitute.

### Task 5: Assessment — intra-critique conditionals

**Cause A (synthesizer over-reach) is the proximate cause.** The
synthesizer violated an unambiguous rule.

**Cause C (architectural gap) is the underlying reason the over-reach
was tempting.** The conditional structure in Finding 5's mechanism is
real and load-bearing:

- The mechanism literally starts with "If micronutrient programs have
  reduced VAD prevalence beyond what the proxy indicators suggest"
- The finding's strength genuinely depends on whether this IF clause
  holds
- The verifier marked this critique as VERIFIED with reasoning that
  includes: "Both DRC and Mali have implemented micronutrient
  interventions... which could reduce VAD prevalence independently of
  changes in stunting, wasting, or poverty"
- But nobody verified the IF clause itself — the verifier confirmed
  that programs exist, not that they've actually reduced VAD beyond
  proxies

The pipeline has no way to express this. The linker's `depends_on`
relationship is strictly inter-critique (surviving → rejected). An
intra-critique conditional ("this critique's own IF clause is
unverified") has no representation in the schema.

**This gap is documented in P-003** as a design question separate from
this bug fix.

## Proposed prompt changes (draft — do not apply yet)

Per CLAUDE.md, prompt changes invalidate run comparability. These are
specifications for the next coordinated revision, not immediate edits.
Both are confirmed necessary by the investigation.

### Fix 1: Prevent placeholder text leakage

The synthesizer emitted the literal format-example phrase `(rejected
critique title)` as content. This happened because it tagged a finding
CONDITIONAL but couldn't find a rejected critique title to substitute.

**Current text** (synthesizer.md lines 102-106):
```
**Conditional on:** [If this finding's title appears in the Critique
Dependencies input as the `surviving` side of a `depends_on` relationship,
list each one here in the format: "the unverified claim that X (rejected
critique title)". If multiple, list all. If none, OMIT this subsection
entirely — do NOT write "Conditional on: none".]
```

**Proposed replacement:**
```
**Conditional on:** [Before producing this subsection, look up this
Finding's title in the Critique Dependencies input. If it appears as
the `surviving` side of a `depends_on` edge, emit "Conditional on:"
followed by the rejected critique's **actual title** from the dependency
entry (not the literal phrase "rejected critique title", which is a
format example). If multiple `depends_on` edges exist for this title,
list all. If this Finding's title does NOT appear as the `surviving`
side of any `depends_on` edge, OMIT this entire subsection — do NOT
write "Conditional on: none" and do NOT infer conditionals from the
critique's own mechanism text.]
```

The key addition is the final clause: "do NOT infer conditionals from
the critique's own mechanism text." This directly addresses the failure
mode observed in the VAS run.

### Fix 2: Pre-computed conditional list + self-consistency check

The synthesizer produced a CONDITIONAL header tag on Finding 5 but then
wrote "(no findings depend on unverified claims in this run)" in the
dedicated section — a self-contradiction. The failure is positional:
the tag was generated before the model reached the cross-check.

Asking the model to retroactively correct earlier output is unreliable —
models tend to re-emit text rather than surgically revise. The more
robust approach: force the model to compute the conditional list
*before* it produces any Finding headers, so the constraint is
upstream of the failure point.

**Proposed addition** (insert in the Output Format, immediately before
`## Critical Findings`):
```
## Pre-Computation (emit before producing any Finding sections)

Before writing any Finding headers, extract the list of surviving
critique titles that appear in `depends_on` entries in the Critique
Dependencies input. Emit this list as a hidden comment at the top of
your output:

<!-- conditional_titles: ["Title A", "Title B"] -->
<!-- conditional_count: 2 -->

If no `depends_on` entries exist, emit:

<!-- conditional_titles: [] -->
<!-- conditional_count: 0 -->

When producing each Finding header below, apply the [CONDITIONAL —
see dependencies] tag ONLY if the Finding's title appears in this
pre-computed list.
```

**Proposed addition** (append after `## Meta-Observations`, before
`## Rules`):
```
## Self-Consistency Check (perform before finalizing)

After producing all sections, verify:
1. Count the Findings tagged `[CONDITIONAL — see dependencies]` in
   the Critical/Significant/Minor Findings sections.
2. This count must equal the `conditional_count` value you emitted
   above in the Pre-Computation comment.
3. The number of entries in the Conditional Findings section must
   also equal this count.
4. If any count disagrees, you have a tagging error. Re-check each
   Finding header against your pre-computed `conditional_titles` list.
```

The two additions are complementary: the pre-computation puts the
constraint before the failure point; the self-consistency check
catches any remaining drift. Either one alone is an improvement;
together they make the failure mode from VAS Finding 5 structurally
difficult to reproduce.

## How the extractor handles this in the meantime

The extractor (`extract.py`) currently captures both signals
separately on each Finding node:
- `synthesizer_conditional_tag: true | false` — whether the synthesizer
  emitted the CONDITIONAL header tag
- `synthesizer_conditional_note: string | null` — the "Conditional on:"
  text the synthesizer wrote, if any
- `conditional_on: [...]` — the authoritative list derived from linker
  `depends_on` edges

For Finding 5 in the VAS run, this gives:
- `synthesizer_conditional_tag: true`
- `synthesizer_conditional_note: "the unverified claim that micronutrient
  programs systematically reduce VAD prevalence beyond what proxy
  indicators suggest (rejected critique title)."`
- `conditional_on: []`

The explorer can render this discrepancy as data-quality information
("synthesizer claimed CONDITIONAL but linker did not substantiate;
investigate"). This is the right thing to do even after the upstream
fix lands, because it preserves the audit trail.

## Cross-reference

- **P-001** (orphan `**` markers): a separate parser bug, already fixed.
- **P-003** (intra-critique conditionals): architectural design question
  prompted by this investigation. The pipeline currently cannot
  represent conditionals embedded in a critique's own mechanism — only
  inter-critique dependencies via the linker. P-003 explores whether
  this deserves schema-level support.

## Resolution

This bug closes when Fix 1 and Fix 2 are applied to
`prompts/synthesizer.md` in the next coordinated prompt revision. The
underlying design gap (intra-critique conditionals) is tracked
separately in P-003 and does not block closing P-002.
