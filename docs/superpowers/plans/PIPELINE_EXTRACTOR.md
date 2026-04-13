# Pipeline Extractor: Implementation Guide

Target repo: `givewell_redteam`
Deliverable: new `07-extractor/` stage that reads pipeline outputs from
stages 01-06 and emits `results/<topic>/graph.json` conforming to the
schema defined in the `red_team_explorer` repo at `docs/SCHEMA.md`.

**The schema is the contract.** It lives in `red_team_explorer/docs/SCHEMA.md`
and is maintained there. This repo consumes it. Before implementing, ensure
you have access to the current schema — either via a pinned copy committed
to `docs/SCHEMA.md` in this repo, a git submodule of `red_team_explorer`,
or by reading directly from the `red_team_explorer` repo. All subsequent
references to "the schema" or "SCHEMA.md" in this document mean that file.

## Context

The red-team pipeline produces markdown artifacts at each stage
(decomposer, investigators, verifier, quantifier, adversarial, linker,
synthesizer). Downstream consumers (notably the `red_team_explorer`)
need this information as a structured graph. The extractor stage
converts markdown to `graph.json`.

The schema is versioned (`schema_version: "0.1"`). The extractor emits
this version string; the explorer refuses mismatches. Do not change the
version string without coordinating a schema update.

## Where the data lives in existing pipeline outputs

| Schema element       | Source stage(s)                      |
|---------------------|--------------------------------------|
| Sources              | 02-investigators, 03-verifier        |
| Claims               | 03-verifier                          |
| SurvivingCritique    | 04-quantifier, 05-adversarial        |
| RejectedCritique     | 03-verifier                          |
| Arguments            | 05-adversarial (advocate, challenger, judge) |
| failure_flags        | 05-adversarial-judge                 |
| quality_flags        | 05-adversarial-judge                 |
| critique_dependency  | 05b-linker                           |
| Findings             | 06-synthesizer                       |
| pipeline_summary     | 06-synthesizer (pipeline summary section) |

## Extractor structure

Six extraction prompts, one per logical slice. Each prompt reads one or
two stage files and emits a slice of the schema. A Python orchestrator
stitches the slices into a single `graph.json`, validates against a
pydantic model, and writes the output file.

```
07-extractor/
├── README.md                    # links to red_team_explorer/docs/SCHEMA.md
├── prompts/
│   ├── 01_sources.md            # reads 02-investigators, 03-verifier
│   ├── 02_claims.md             # reads 03-verifier
│   ├── 03_critiques.md          # reads 04-quantifier, 03-verifier (rejected)
│   ├── 04_arguments_flags.md    # reads 05-adversarial-*
│   ├── 05_dependencies.md       # reads 05b-linker
│   └── 06_findings_summary.md   # reads 06-synthesizer
├── models.py                    # pydantic schemas mirroring SCHEMA.md
├── extractor.py                 # orchestrator
└── validate.py                  # standalone validator for CI
```

## Prompt design

Each extraction prompt must:

1. Emit **only** its slice of the graph JSON. No prose, no markdown,
   no code fences unless the runner strips them.
2. Preserve titles verbatim. The synthesizer uses critique titles as
   join keys; the linker references them exactly. Any paraphrasing
   breaks cross-references.
3. Produce a `confidence` and `confidence_justification` for every node,
   and a `weight` + `weight_justification` for every edge. These are
   non-optional.
4. Use source-derived confidence. For Source nodes, the extractor LLM
   reads the verifier's status (VERIFIED/EXTRAPOLATED/UNVERIFIABLE/
   DISPUTED) and any notes, and assigns a calibrated confidence. The
   justification must reference the verifier's reasoning, not invent
   new grounds.
5. Produce stable IDs. IDs should be content-derived slugs (e.g.
   `src_devta_mortality_ratio`, `arg_adv_devta_outlier_r1`) so that
   re-extraction on the same pipeline output produces the same IDs.
   Don't use random UUIDs.

## Confidence calibration rules for the extractor LLM

For **Source** nodes:
- VERIFIED, strong methodology, major journal → 0.9-1.0
- VERIFIED, minor methodology concerns → 0.75-0.9
- EXTRAPOLATED from verified components → 0.6-0.75
- UNVERIFIABLE but plausible → 0.4-0.6
- DISPUTED or contradicted → 0.1-0.3

For **RejectedCritique** nodes:
- UNVERIFIABLE verdict → default 0.4 (neither confirmed nor denied)
- REJECTED verdict → default 0.1 (contradicting evidence found)

Justifications for Source confidences must cite the verifier's reasoning
(e.g. "verifier marked VERIFIED; Lancet publication, n=1M, CI crosses
unity but central finding robust"). The extractor is not allowed to
invent new grounds for a confidence value beyond what the upstream
stages documented.

## Validation

`models.py` uses pydantic to mirror the schema exactly. Unknown fields
fail validation (strict mode). Missing required fields fail validation.
The orchestrator runs validation after merging the six slices and aborts
with a clear error if anything fails.

A standalone `validate.py` runs the same check on any `graph.json` file,
suitable for CI. When schema v0.2 lands, pydantic models get regenerated
and both producer and consumer update in lockstep.

## ID conventions

Short prefixes, content-derived slugs, lowercase snake_case. Examples:

- `src_devta_mortality_ratio`
- `clm_devta_no_mortality_benefit`
- `arg_adv_devta_outlier_r1`  (advocate, critique devta_outlier, round 1)
- `arg_chl_devta_valid_r1`    (challenger)
- `crt_devta_mortality_signal`
- `rcrt_vad_threshold_effect`
- `fnd_publication_bias_material`
- `fflag_001`, `qflag_001`    (numbered; scope is the whole run)
- `e_001`, `e_dep_001`        (edges; `e_dep_*` for dependency edges)

Edge IDs are sequential within the run; node IDs are content-derived.

## Orchestrator outline

```python
def extract(topic_dir: Path) -> Graph:
    slices = [
        extract_sources(topic_dir / "02-investigators.md", topic_dir / "03-verifier.md"),
        extract_claims(topic_dir / "03-verifier.md"),
        extract_critiques(topic_dir / "04-quantifier.md", topic_dir / "03-verifier.md"),
        extract_arguments_and_flags(topic_dir / "05-adversarial-*.md"),
        extract_dependencies(topic_dir / "05b-linker.md"),
        extract_findings_and_summary(topic_dir / "06-synthesizer.md"),
    ]
    graph = merge_slices(slices)
    validate(graph)  # pydantic, strict
    return graph
```

Each `extract_*` function calls Claude with the corresponding prompt and
the relevant source file(s), parses the JSON response, and returns a
typed slice object. `merge_slices` combines them into the top-level
document shape.

## Edge construction

Most edges are constructed by the extractor rather than emitted by the
LLM directly, because edges depend on ID consistency across slices. The
LLM emits node lists with their "supports" / "used-by" / "rebuts"
references by title or natural key; the orchestrator resolves these to
IDs and emits edges.

Exception: `argument_rebuts_argument` edges with `relation` = `reframes`
require LLM judgment (did this argument actually engage the opponent's
point?), so the adversarial extraction prompt emits them with relation
classifications. The orchestrator resolves IDs but preserves the
relation.

## What NOT to do

- Do not compute `pipeline_summary` counts. Read them from the
  synthesizer's pipeline summary section verbatim. If a count is
  missing, write 0 and log a warning; do not estimate.
- Do not paraphrase titles. The synthesizer and linker already treat
  them as join keys.
- Do not invent confidence justifications. They must reference
  upstream reasoning.
- Do not add fields not in `SCHEMA.md` (the canonical version in
  `red_team_explorer/docs/`). If you find you need one, raise it against
  `red_team_explorer` — the schema is the contract shared across
  pipelines and the explorer, and unilateral extensions break every
  consumer. Schema changes require a version bump coordinated across
  all repos.

## Testing

Two levels:

1. **Schema validation.** Run `validate.py` on every produced
   `graph.json`. Must pass before the file is written.
2. **Round-trip smoke test.** Load `graph.json`, walk every node's
   referenced edges, confirm all referenced IDs exist. Catches orphan
   references the schema itself can't catch.

Eventual: golden-file tests using a saved VAS pipeline run as input and
a committed `graph.json` as expected output. Deferred until the
extractor prompts stabilize.

## Future: native structured output

The current design retrofits structured output from existing markdown.
Longer-term, pipeline stages should emit structured JSON natively
alongside their markdown, and the extractor becomes a thin merger rather
than an LLM pass. Not required now; flagged for when the schema
stabilizes and the extractor's LLM cost becomes annoying.
