# Adding First-Class Source Extraction to the Pipeline

**Status:** Planning document — not implemented
**Target repo:** `givewell_redteam`
**Schema change:** Requires schema v0.3+ (reintroduces Source nodes and `source_supports_claim` edges dropped in v0.2)
**Related:** Future pipeline improvement P1 in `SCHEMA.md`

## Why this matters

The explorer's most valuable feature — the one Mikyo explicitly asked for
— is the "what if this source turns out to be wrong" interaction: drag a
source's confidence down and watch which findings weaken. This is the
single-point-of-failure lens on the reasoning structure.

Without structured sources, this interaction is impossible at the right
granularity. Users can toggle UNVERIFIED rejected critiques (via the
linker dependency edges), but they can't ask "what if DEVTA's mortality
ratio turns out to be compromised?" because DEVTA is not a node — it's a
phrase embedded in verifier evidence prose. There's nothing to slide.

For the red-team methodology to be trustworthy to domain experts, the
ability to trace findings to their evidence atoms and stress-test them
individually is not optional. It's what makes the reasoning auditable
rather than just plausible.

## What "full functionality" requires

The explorer needs Source objects with these properties:

1. **Atomic.** DEVTA's mortality ratio, DEVTA's sample size, and DEVTA's
   CI bounds are three separate sources if three separate arguments can
   cite one without the others. Granularity rule: if two arguments can
   cite one aspect of a paper without the other, they are two sources.

2. **Typed.** `study_finding | statement | dataset | meta_analysis |
   expert_opinion` at minimum. Lets the UI color-code and filter.

3. **Traceable.** Each source carries a citation string and, where
   possible, a URL. Users clicking a source should see where the claim
   came from, not just the extractor's paraphrase.

4. **Status-marked.** Verifier's verdict on the source attaches to the
   Source node: `verified` (source exists and says what the critique
   claims), `partially_verified` (source exists but says something
   narrower or broader), `unverifiable` (could not confirm or deny),
   `disputed` (other sources contradict).

5. **Linked to claims.** Each Claim node has one or more incoming
   `source_supports_claim` edges, with edge weights representing how
   much the claim depends on that specific source.

## Where to extract sources from

Three places in the current pipeline output contain citation-like
content:

### 1. Investigator `suggested_evidence` arrays

Each investigator critique produces a `suggested_evidence` list, e.g.:

```json
"suggested_evidence": [
  "The DEVTA trial in India (2013) found no mortality benefit...",
  "Biological mechanism: VAS primarily prevents deaths through...",
  "UNGROUNDED — needs verification: I believe there are recent WHO..."
]
```

These are the investigator's initial citations *before* verification.
Useful as a starting inventory, but not authoritative — the verifier
checks them and marks some as unverifiable.

### 2. Verifier `evidence_found` and `caveats` arrays

The verifier emits structured arrays of verified claims:

```json
"evidence_found": [
  "Additional evidence from Indian context supports the critique..."
],
"caveats": [
  "DEVTA showed no mortality benefit: VERIFIED - mortality ratio 0.96 (95% CI 0.89-1.03, p=0.22)",
  "Contrast with earlier trials: VERIFIED - Meta-analysis including DEVTA showed 11% mortality reduction..."
]
```

These are the authoritative grounding for claims. Each bullet typically
corresponds to one source (or a small cluster). The `VERIFIED` /
`UNVERIFIABLE` prefix is the verifier's status assessment.

### 3. Adversarial advocate/challenger defenses

The advocate and challenger also cite sources in their arguments. These
should generally already appear in the verifier evidence package — if a
debater cites something novel, that's a separate concern (see "What
could go wrong" below).

## Two approaches

### Approach A: Verifier emits structured sources directly

**Modify the verifier prompt.** Instead of (or in addition to) producing
prose `evidence_found` / `caveats` arrays, the verifier emits a
structured `sources` array:

```json
"sources": [
  {
    "id": "src_devta_mortality_ratio",
    "citation": "Awasthi et al. 2013, Lancet",
    "kind": "study_finding",
    "content": "DEVTA mortality ratio 0.96 (95% CI 0.89-1.03, p=0.22)",
    "status": "verified",
    "notes": "Large sample, Lancet publication"
  },
  ...
]
```

And the existing `caveats` array optionally retained for human
readability, or replaced entirely by the structured form plus a
derived markdown rendering.

**Pros:**
- Cleanest long-term solution.
- Source granularity is determined by the verifier, which has full
  context on each citation.
- No post-hoc extraction, no risk of misreading prose into wrong
  structure.
- Sets precedent for future pipeline stages to emit structured outputs
  as first-class.

**Cons:**
- Prompt change invalidates run comparability (the "prompts are
  experimental treatment" rule from CLAUDE.md).
- Adds verifier output token cost.
- If the prompt is poorly designed, granularity judgment by the LLM
  could be inconsistent across runs.

### Approach B: Post-hoc extraction pass

**Add a new pipeline stage** (`07-source-extractor/` or similar) that
reads the verifier output and produces structured sources, keeping the
verifier unchanged.

```
verifier.md/.json → source_extractor → sources.json
```

The source extractor is a Sonnet call per critique with a prompt that
reads `caveats` and `evidence_found`, identifies atomic evidence units,
assigns status, and produces citations.

**Pros:**
- Doesn't modify the verifier prompt; preserves run comparability.
- Can be iterated independently without rerunning expensive stages.
- Cheaper to improve — prompt changes only affect extraction, not
  verification quality.

**Cons:**
- Extra pipeline stage, extra cost per run.
- Extractor is doing interpretive work on prose, which is where
  misreadings creep in.
- Two sources of truth (verifier prose + extracted structure) can
  diverge.

**Recommendation: Approach A.** The prompt-change cost is one-time; the
post-hoc extraction cost is forever. The comparability concern is real
but can be managed by versioning the verifier prompt and noting which
runs used which version.

## Schema additions required

When sources become first-class, the schema needs to add:

```json
"nodes": {
  "sources": [
    {
      "id": "src_devta_mortality_ratio",
      "kind": "study_finding" | "statement" | "dataset" | "meta_analysis" | "expert_opinion",
      "title": "DEVTA mortality ratio",
      "content": "Mortality ratio 0.96 (95% CI 0.89-1.03, p=0.22)",
      "origin": {
        "citation": "Awasthi et al. 2013, Lancet",
        "url": "https://...",
        "verifier_status": "verified" | "partially_verified" | "unverifiable" | "disputed"
      },
      "confidence": 0.9,
      "confidence_justification": "Verifier marked VERIFIED; Lancet publication, n=1M"
    }
  ],
  ...
}

"edges": {
  "source_supports_claim": [
    {
      "id": "e_001",
      "source_node_id": "src_devta_mortality_ratio",
      "target_node_id": "clm_devta_no_mortality_benefit",
      "weight": 1.0,
      "weight_justification": "Claim is a direct restatement of source finding"
    }
  ],
  ...
}

"aggregation_config": {
  "claim_from_sources": "noisy_or",  // replaces "claim_from_grounding: direct"
  ...
}
```

Claim nodes keep their `grounding` and `grounding_citations` fields as
human-readable context, but confidence now propagates from Source nodes
through `source_supports_claim` edges using noisy-OR aggregation by
default. The "SPOF lens" toggle (switch to `min` aggregation) becomes
meaningful.

## Extractor changes required

When schema v0.3 lands with Sources:

1. The extractor reads `sources` arrays from the verifier JSON (if
   Approach A) or calls the source-extractor stage (Approach B).
2. Each source becomes a node with the structure above.
3. For each claim, the extractor identifies which sources support it
   and emits `source_supports_claim` edges with weights reflecting how
   central the source is to the claim.
4. The existing Claim structure is retained but `claim.grounding` and
   `claim.grounding_citations` become supplementary — confidence
   propagates from Sources, not from extractor-assigned values.

## Granularity calibration

The extractor (or verifier, under Approach A) needs a rule for when to
split one paper into multiple sources. Default rule:

> If two arguments in the adversarial stage can cite one aspect of a
> paper without citing the other, they are separate sources.

In practice, this typically means:

- A study's main finding is usually one source.
- The study's confidence interval or effect size is a separate source
  if arguments cite it independently (e.g. debating whether the CI
  crossing unity is significant).
- The study's sample size or setting is a separate source if arguments
  cite it to establish external validity.
- A meta-analysis is usually one source, unless arguments debate
  individual studies within it (in which case those studies become
  their own sources).

Conservative default: when in doubt, keep at coarser granularity. A
single source per paper is fine for v1; the SPOF-lens lets users see
where the coarseness is hiding dependencies, and granularity can
refine over time.

## What could go wrong

1. **Sources cited in debates but not in verifier evidence.** An
   advocate or challenger might cite a source the verifier didn't
   process. The extractor needs to decide: treat as a new Source node
   (with reduced confidence because the verifier never checked it), or
   flag as an ungrounded citation. Probably the latter, with a clear
   visual indicator.

2. **Granularity drift across runs.** Different verifier runs might
   split DEVTA differently (one source vs. three). The explorer needs
   to handle this gracefully — it means SPOF-lens comparisons across
   runs are not apples-to-apples until granularity stabilizes.

3. **Prompt cost inflation.** Asking the verifier to emit structured
   sources adds output tokens. Mitigation: make the `caveats` /
   `evidence_found` arrays optional (derivable from sources) rather
   than both being required.

4. **Source deduplication.** The same source (e.g. DEVTA) will be
   referenced by multiple critiques. The extractor needs to dedupe by
   citation string or content similarity, producing one Source node
   with edges to multiple Claims rather than N duplicate nodes. This
   is a judgment call the extractor makes; wrong answers are either
   over-consolidation (losing granularity) or under-consolidation
   (same source appears as multiple nodes, confusing the graph).

## Testing

Before shipping, the sources-enabled pipeline should produce a run
where:

1. Dragging DEVTA's confidence to 0 visibly weakens the
   "Threshold Effects Below Critical VAD Prevalence Levels" finding.
2. Dragging a source no finding depends on (if any exist) does not
   change any finding confidence.
3. The SPOF-lens (min aggregation) and default (noisy-OR) views show
   different results for claims with multiple supporting sources,
   and identical results for claims with single sources.

All three tests are visual / interactive in the explorer; they need a
real run to verify.

## When to do this

After the current VAS run's graph.json is validated end-to-end in the
explorer at v0.2. At that point:

1. The explorer has proven it can render what the schema specifies.
2. Mikyo (or equivalent domain reviewer) has stress-tested the v0.2
   views and identified what's missing.
3. The verifier prompt modification can be designed with clarity about
   what the downstream consumer actually needs.

Rushing this now — before v0.2 is proven — means designing source
extraction against assumptions rather than observed usage. The right
sequence is: ship v0.2, use it, then scope v0.3 with evidence.
