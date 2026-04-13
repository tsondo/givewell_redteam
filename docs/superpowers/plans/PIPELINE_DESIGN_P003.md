# Pipeline Design P-003: Intra-Critique Conditional Representation

**Status:** Draft — design question, not yet a commitment to build
**Prompted by:** P-002 investigation (synthesizer CONDITIONAL tag on
Finding 5 with no linker backing)
**Affected stages:** Potentially 05b-linker, 06-synthesizer, schema,
extractor
**Scope:** Should the pipeline model conditionals embedded within a
single critique's mechanism, not just dependencies between two
distinct critiques?

## The problem

The pipeline currently represents one kind of conditional structure:
inter-critique dependencies via the linker's `depends_on` relationship.
When Surviving Critique A's argument requires Rejected Critique B's
claim to be true, the linker produces a `depends_on` edge and the
synthesizer tags the finding CONDITIONAL.

But critiques can also contain *intra-critique* conditionals: IF
clauses in their own mechanism text that are load-bearing for the
finding's conclusion but whose truth status hasn't been independently
established. The pipeline has no way to express these.

## The VAS example

Finding 5 ("Proxy Weight Distribution Invalidated by Micronutrient
Program Rollouts") has this mechanism:

> "If micronutrient programs have reduced VAD prevalence beyond what
> the proxy indicators suggest, GiveWell would overestimate current
> VAD rates."

The verifier confirmed that micronutrient programs *exist* in the
relevant countries (Mali, DRC). But it did not verify that these
programs have *actually reduced VAD prevalence beyond what proxy
indicators suggest*. That IF clause is unverified and load-bearing:
if it's false, the finding's quantified impact (9x inflation for DRC)
doesn't hold.

The synthesizer (Opus) noticed this and tried to tag it CONDITIONAL,
violating its prompt rules in the process (P-002). The instinct was
correct — the conditional structure is real — but the pipeline gave
it no legitimate way to express it.

## What "intra-critique conditional" means precisely

A critique has an intra-critique conditional when:
1. Its mechanism contains an IF/THEN structure
2. The IF clause is an empirical claim (not a tautology or definition)
3. The verifier's evidence addresses the THEN clause or surrounding
   context but does not directly verify the IF clause itself
4. The finding's quantified impact or recommendation depends on the
   IF clause being true

This is distinct from:
- **Inter-critique dependency** (linker `depends_on`): the unverified
  claim exists as a separate, named rejected critique
- **General uncertainty**: every critique has uncertainty; an
  intra-critique conditional is specifically about an identifiable,
  falsifiable claim embedded in the mechanism that wasn't tested

## Design options

### Option A: Linker expansion — detect intra-critique conditionals

Expand the linker's scope to detect IF clauses in surviving critique
mechanisms that aren't backed by verifier evidence. Emit a new
relationship type (e.g., `self_conditional`) with the unverified
clause as a field.

**Schema addition:**
```json
{
  "surviving_critique_title": "Proxy Weight Distribution...",
  "conditional_clause": "micronutrient programs have reduced VAD prevalence beyond what proxy indicators suggest",
  "clause_verified": false,
  "relationship": "self_conditional",
  "confidence": "high",
  "justification": "The mechanism's IF clause was not directly tested by the verifier..."
}
```

**Pros:**
- Keeps the synthesizer's CONDITIONAL tagging rule simple: any
  `depends_on` OR `self_conditional` entry triggers the tag
- The linker already reads both surviving mechanisms and verifier
  evidence, so it has the data needed
- Auditable: the extracted clause appears in the linker output

**Cons:**
- Significant scope expansion for the linker. Currently it matches
  titles across two lists; this requires parsing mechanism text for
  conditional structures and cross-referencing verifier evidence
- Prompt complexity increases substantially
- Higher risk of false positives (the linker may flag hedging
  language as conditionals)

### Option B: Verifier annotation — flag unverified mechanism clauses

Add a field to the verifier output: `unverified_mechanism_clauses`,
listing IF clauses in the mechanism that the verifier found evidence
*around* but not *for*. The linker then doesn't need to do
mechanism parsing — it just forwards verifier annotations.

**Schema addition to VerifiedCritique:**
```json
{
  "unverified_mechanism_clauses": [
    {
      "clause": "micronutrient programs have reduced VAD prevalence beyond what proxy indicators suggest",
      "related_evidence": "Verifier confirmed programs exist but not their effect on VAD vs proxies"
    }
  ]
}
```

**Pros:**
- The verifier is already reading mechanisms and evaluating evidence;
  this is a natural extension of its role
- The linker stays focused on inter-critique relationships
- Lower risk of false positives because the verifier has domain
  context

**Cons:**
- Requires prompt changes to the verifier (more invalidation risk
  than changing only the linker)
- The verifier is already the longest and most complex prompt
- Adds a new output field that all downstream stages must handle

### Option C: Synthesizer-side heuristic — controlled over-reach

Instead of preventing the synthesizer from noticing intra-critique
conditionals, give it explicit rules for when and how to surface them.
Add a new tag (e.g., `[MECHANISM ASSUMPTION — see note]`) distinct
from `[CONDITIONAL — see dependencies]`, with its own section.

**Pros:**
- No upstream changes. Only the synthesizer prompt and schema change
- The synthesizer is already the stage that reads mechanism text in
  full context
- Cheapest to implement and test

**Cons:**
- This asks the same model that already failed at this task to do
  more of it, with more elaborate rules. The failure mode in VAS
  wasn't insufficient instruction — the existing CONDITIONAL rule
  was clear and unambiguous. The failure was the model acting on
  rich contextual information (the IF clause in the mechanism text)
  against a structured constraint (the linker's dependency list).
  Adding rules doesn't change which signal the model attends to;
  it just adds more rules for it to violate when the rich context
  pulls harder than the structured constraint
- No auditability: the conditional extraction happens inside the
  synthesizer's reasoning, not as a separate stage output
- Conflates two functions in one stage (synthesis + conditional
  detection)

### Option D: Do nothing — document the gap

Accept that intra-critique conditionals are a known limitation.
Document it in the report methodology section. Let readers notice
IF clauses in mechanism text on their own.

**Pros:**
- Zero implementation cost
- The extractor already captures the discrepancy
  (`synthesizer_conditional_tag` vs `conditional_on`) as a data
  quality signal

**Cons:**
- The whole point of the pipeline is to surface epistemic structure
  that single-pass approaches miss. Leaving a known structural gap
  undocumented in the output is a missed opportunity
- Future synthesizer runs may produce the same over-reach as VAS
  Finding 5, with or without the P-002 prompt fix, because the
  underlying pressure to surface real conditional structure remains

## Prevalence estimate

Before committing to any option, measure how common intra-critique
conditionals are:

1. **VAS run:** Scan all 28 surviving critique mechanisms for IF/THEN
   structures where the IF clause wasn't directly verified. Finding 5
   is the known case; are there others?
2. **Other runs:** Same scan for water-chlorination (if mechanism text
   is available), itns, smc.
3. **Judgment call:** If only 1-2 findings per typical run are
   affected, the extractor's data-quality flag is sufficient (Option
   D). If more than that, verifier annotation (Option B) is worth
   the prompt complexity. See Decision Criteria below.

## Recommendation

Pending prevalence measurement; do not commit to any option until the
scan is complete.

If the scan justifies action, **Option B** (verifier annotation) is
the strongest candidate. The verifier is the right stage to flag
unverified mechanism clauses because it's already evaluating what
evidence supports and what it doesn't. But this is a non-trivial
prompt change to the most complex stage in the pipeline, so prevalence
must justify the complexity.

Option C is ruled out. The VAS Finding 5 incident is direct evidence
against synthesizer-side conditional detection. The failure mode
wasn't insufficient instruction — the existing CONDITIONAL rule was
clear and unambiguous. The model acted on rich contextual information
(the IF clause in the mechanism text) against a structured constraint
(the linker's empty dependency list). Adding a second tag with
different rules doesn't change which signal the model attends to
when rich context and structured constraints conflict. This is the
same model, with the same context window, facing the same tension.

## Decision criteria

- **Rare** (1-2 findings per typical run): Option D. The extractor's
  data-quality flag (`synthesizer_conditional_tag` vs `conditional_on`
  mismatch) is sufficient. Document the limitation in the report
  methodology.
- **Common** (more than a handful per run): Option B. Verifier
  annotation. The prompt complexity is justified by the
  interpretability gain.
- **Majority** (most critique mechanisms contain unverified IF
  clauses): Option B still applies, but the more interesting
  question shifts upstream. If the majority of mechanisms have
  load-bearing unverified IF clauses, the investigators may be
  producing weaker mechanisms than necessary — hedging with "if X"
  rather than committing to testable claims. In that case the right
  fix is tighter investigator prompts that force mechanisms to be
  grounded, not downstream annotation of the hedging. The prevalence
  scan would then also serve as a diagnostic for investigator prompt
  quality.

## Cross-reference

- **P-002**: The bug that prompted this design question. Synthesizer
  tagged Finding 5 CONDITIONAL without linker backing because it
  noticed an intra-critique conditional the pipeline couldn't
  represent.
