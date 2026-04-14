# How to Use extract.py

## What It Is

`extract.py` converts pipeline stage JSON outputs into a single `graph.json`
conforming to the `red_team_explorer` schema v0.2. The explorer renders this
file — it is the only interface between the pipeline and the explorer.

The extractor is deterministic (no LLM calls). It reads structured JSON from
stages 03-06, maps fields to schema nodes/edges, computes confidence priors,
and writes one self-contained graph file.

## Where It Is

```
givewell_redteam/extract.py
```

No additional dependencies beyond the Python standard library.

## Prerequisites

The input directory must contain these pipeline stage outputs:

| File | Required | Source stage |
|------|----------|-------------|
| `05-adversarial.json` | Yes | Adversarial debate with judge audit |
| `03-verifier-rejected.json` | Yes | Rejected/unverified critiques |
| `06-synthesizer.json` | Yes | Synthesizer report (markdown in JSON) |
| `05b-linker.json` | No | Critique dependency links |

**The adversarial JSON must include `judge_audit` and
`advocate_self_assessment` fields** (added by the judge stage). Runs produced
before the judge stage was introduced will fail with a clear error:

```
ERROR: 05-adversarial.json lacks judge_audit fields.
This run was produced by a pipeline version before the judge stage.
Re-run the pipeline through the judge stage before extracting.
```

If `05b-linker.json` is absent, the graph is produced without
`critique_dependency` edges. This is valid — the schema allows an empty array.

## Usage

### Basic — write graph.json to current directory

```bash
python extract.py --input-dir results/vas --run-id vas-2026-04-13
```

Writes `./graph.json`.

### With output directory — write to explorer's runs folder

```bash
python extract.py \
    --input-dir results/vas \
    --run-id vas-2026-04-13 \
    --output-dir ../red_team_explorer/static/runs
```

Writes `../red_team_explorer/static/runs/vas-2026-04-13/graph.json`
(creates the directory if needed).

### Override the topic string

The topic is auto-detected from the synthesizer report title
(`# Red Team Report: <topic>` becomes `GiveWell <topic>`). Override it if
the report title is missing or wrong:

```bash
python extract.py \
    --input-dir results/itns \
    --run-id itns-2026-04-14 \
    --topic "GiveWell Insecticide-Treated Nets" \
    --output-dir ../red_team_explorer/static/runs
```

## Options Reference

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--input-dir` | Yes | — | Path to pipeline results directory (e.g. `results/vas`) |
| `--run-id` | Yes | — | Run identifier used in the output path and `graph.json` metadata |
| `--output-dir` | No | `.` (cwd) | Parent directory; output goes to `<output-dir>/<run-id>/graph.json` |
| `--topic` | No | Auto-detected | Override the topic string in graph metadata |

## What It Produces

A single `graph.json` containing:

- **Claims** — extracted from verifier caveats (one per caveat entry)
- **Arguments** — advocate + challenger pair per critique, with judge verdict,
  rationale, debate resolved/unresolved, recommended action
- **Surviving critiques** — title, hypothesis, mechanism, materiality,
  judge surviving strength
- **Rejected critiques** — title, hypothesis, verdict, verifier reasoning
- **Findings** — parsed from the synthesizer markdown report (structured
  fields for strong/moderate; text-only for weak)
- **Edges** — all five types: claim-to-argument, rebuttal, containment,
  dependency, roll-up
- **Failure flags** — from judge audit (advocate and challenger failures)
- **Pipeline summary** — computed from data counts (threads, critiques,
  signal rate)
- **Aggregation config** — default config for the propagation engine (M3)

## After Extracting

Regenerate the explorer's run index so the new run appears in the dropdown:

```bash
cd ../red_team_explorer
node scripts/build-index.js
```

Then load the explorer with `?run=<run-id>` or select the run from the
dropdown.

## Confidence Calibration

The extractor assigns default confidence priors — these are starting points
for the propagation engine, not ground truth.

| Node type | Condition | Confidence |
|-----------|-----------|------------|
| Claim | verified | 0.9 |
| Claim | partially_verified | 0.7 |
| Claim | unverified | 0.4 |
| Argument | base = strength prior, minus 0.1 per failure flag (capped at 0.5) | varies |
| Surviving critique | average of verifier prior and judge strength prior | varies |
| Rejected critique (unverified) | — | 0.4 |
| Rejected critique (rejected) | — | 0.1 |
| Finding (strong) | — | 0.75 |
| Finding (moderate) | — | 0.55 |
| Finding (weak) | — | 0.25 |

Strength priors: strong = 0.75, moderate = 0.55, weak = 0.35.

## Troubleshooting

**"Required file not found"** — The input directory is missing a stage JSON.
Check that the pipeline ran to completion.

**"lacks judge_audit fields"** — The run predates the judge stage. Re-run the
pipeline to add judge verdicts and failure flags.

**"WARNING: No finding matched for critique"** — The synthesizer report
doesn't contain a finding whose title matches a surviving critique. Check
the synthesizer markdown for title mismatches.

**"WARNING: Unknown materiality"** — The pipeline emitted a materiality value
outside the schema enum (`material`, `marginal`, `immaterial`). The extractor
defaults to `marginal` and logs a warning. If the pipeline consistently emits
a new value, the schema may need updating.
