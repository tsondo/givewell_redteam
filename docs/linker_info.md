# Linker Stage — Sample Output and Sanity Checks

This document captures what a realistic Linker stage (5b) output looks like,
for reference when reviewing a real run. The sample below is **hand-constructed**
from real VAS critique titles and hypothesis text — it is NOT the output of an
actual API call. When the pipeline is re-run, use it as a template for sanity
checks, not as ground truth.

## Where the linker sits

```
adversarial (stage 5) -> linker (stage 5b) -> synthesizer (stage 6)
```

The linker takes two inputs:

1. **Surviving critiques** — the list output by `run_adversarial` (passed both
   verification and judge debate).
2. **Rejected critiques** — the list written to `03-verifier-rejected.json`,
   split by verdict into `unverified` and `rejected`.

It emits a `LinkerOutput` containing a list of `CritiqueDependency` records
plus three summary counts (`n_surviving_critiques_examined`,
`n_rejected_critiques_available`, `n_dependencies_found`).

Artifacts are written to `results/{intervention}/05b-linker.{json,md}`. The
non-standard `05b` prefix exists to keep `06-synthesizer.*` stable across
historical runs.

## Short-circuit case

If either input is empty, the linker makes NO API call and writes a zero-state
artifact:

```json
{
  "dependencies": [],
  "n_surviving_critiques_examined": 0,
  "n_rejected_critiques_available": 3,
  "n_dependencies_found": 0
}
```

The `.md` sibling starts with `# Linker — zero-state (short-circuit)` and
explains the reason. **Sanity check: if you see a populated upstream run but
zero-state linker output, something is wrong** — likely the upstream files
loaded empty or the dataclass round-trip dropped records.

## Raw model output format

The linker prompt requires a single `## DEPENDENCIES` section. Each dependency
is a `### Dependency N` block with six key:value lines. This is what the model
produces and what `parse_linker_output` consumes directly:

```
## DEPENDENCIES

### Dependency 1
surviving: Threshold Effects Below Critical VAD Prevalence Levels
rejected: Threshold Effects for Herd Protection in High-Mortality Settings
verdict: unverified
relationship: depends_on
confidence: high
justification: The surviving critique's argument that VAS benefits exhibit
non-linear threshold behavior below a critical VAD prevalence level directly
presupposes the epidemiological tipping-point mechanism described in the
rejected critique. If the herd-protection threshold does not exist, the
surviving finding's linearity concern loses its mechanistic basis.

### Dependency 2
surviving: Differential Effectiveness by Cause-Specific Mortality Patterns
rejected: Accelerating Benefits from Immunological Priming Effects
verdict: rejected
relationship: contradicts
confidence: medium
justification: The surviving critique argues VAS effectiveness varies with
the local cause-of-death mix (measles, diarrhea, respiratory), which
undercuts the rejected hypothesis that priming effects would amplify benefit
uniformly across mortality causes. The two are actively at odds.

### Dependency 3
surviving: Seasonal Variation in Historical VAD Surveys Not Reflected in Proxy Extrapolation
rejected: Seasonal and Campaign-Timing Cost Variations Not Reflected
verdict: unverified
relationship: engages_with
confidence: medium
justification: Both critiques invoke seasonality of the same underlying VAD
pattern but on different CEA dimensions — the surviving finding targets
effectiveness estimates, the rejected one targets cost. The surviving
critique does not need the cost claim to be true for its own argument to
hold.
```

An empty result is the literal text `(none found)`:

```
## DEPENDENCIES

(none found)
```

## Parsed `05b-linker.json` shape

After parsing + count hydration by `run_linker`, the JSON artifact looks like:

```json
{
  "dependencies": [
    {
      "surviving_critique_title": "Threshold Effects Below Critical VAD Prevalence Levels",
      "rejected_critique_title": "Threshold Effects for Herd Protection in High-Mortality Settings",
      "rejected_critique_verdict": "unverified",
      "relationship": "depends_on",
      "justification": "The surviving critique's argument that VAS benefits exhibit non-linear threshold behavior below a critical VAD prevalence level directly presupposes the epidemiological tipping-point mechanism described in the rejected critique. If the herd-protection threshold does not exist, the surviving finding's linearity concern loses its mechanistic basis.",
      "confidence": "high"
    },
    {
      "surviving_critique_title": "Differential Effectiveness by Cause-Specific Mortality Patterns",
      "rejected_critique_title": "Accelerating Benefits from Immunological Priming Effects",
      "rejected_critique_verdict": "rejected",
      "relationship": "contradicts",
      "justification": "The surviving critique argues VAS effectiveness varies with the local cause-of-death mix (measles, diarrhea, respiratory), which undercuts the rejected hypothesis that priming effects would amplify benefit uniformly across mortality causes. The two are actively at odds.",
      "confidence": "medium"
    },
    {
      "surviving_critique_title": "Seasonal Variation in Historical VAD Surveys Not Reflected in Proxy Extrapolation",
      "rejected_critique_title": "Seasonal and Campaign-Timing Cost Variations Not Reflected",
      "rejected_critique_verdict": "unverified",
      "relationship": "engages_with",
      "justification": "Both critiques invoke seasonality of the same underlying VAD pattern but on different CEA dimensions — the surviving finding targets effectiveness estimates, the rejected one targets cost. The surviving critique does not need the cost claim to be true for its own argument to hold.",
      "confidence": "medium"
    }
  ],
  "n_surviving_critiques_examined": 8,
  "n_rejected_critiques_available": 4,
  "n_dependencies_found": 3
}
```

Notes on the sample:

- The three entries exercise each of the three relationship types
  (`depends_on`, `engages_with`, `contradicts`) and both verdict values
  (`unverified`, `rejected`).
- All six surviving/rejected titles come from the real VAS run on disk
  (`results/vas/05-adversarial.json`,
  `results/vas/03-verifier-rejected.json`). The justifications are invented
  plausibly but were NOT produced by a model.
- The terminology distinction holds: `rejected_critique_verdict` stores
  `"unverified"` (schema value), while prompts render this as `UNVERIFIABLE`
  for readers.

## Sanity checks for a real re-run

When you run `python -m pipeline.run_pipeline {intervention} --resume-from linker`
against real data, verify the following against the resulting
`05b-linker.json`. These catch the plausible failure modes without needing
ground truth.

### Structural checks

1. **Both `.json` and `.md` artifacts exist** at `results/{intervention}/05b-linker.{json,md}`.
2. **`n_surviving_critiques_examined` matches** the length of the adversarial stage output loaded into the linker.
3. **`n_rejected_critiques_available` matches** `len(03-verifier-rejected.json)`.
4. **`n_dependencies_found == len(dependencies)`** (counts hydrated correctly by `run_linker`, not left at zero from `parse_linker_output`).
5. **Every dependency's `relationship` is one of** `{depends_on, engages_with, contradicts}`. The parser drops invalid ones with a warning — so if the model emits something unexpected, you won't see it in the JSON but you WILL see warnings in `pipeline.log`.
6. **Every dependency's `rejected_critique_verdict` is** `"unverified"` or `"rejected"` (lowercase literal, not `"UNVERIFIABLE"`).
7. **Every dependency's `confidence` is** `{high, medium, low}`. The parser defaults invalid values to `medium` and logs a warning.

### Semantic checks (spot-check a sample of dependencies)

8. **Titles match verbatim.** `surviving_critique_title` should appear in `05-adversarial.json` as `critique.critique.original.title`. `rejected_critique_title` should appear in `03-verifier-rejected.json` as `original.title`. Any mismatch means the synthesizer will silently fail to tag that finding as CONDITIONAL.
9. **No duplicate `(surviving, rejected)` pairs.** The parser deduplicates on the pair as a safety net, but if the model emits duplicates the log will show it.
10. **Justification fields are non-empty and reference both sides of the relationship.** A justification that only describes the surviving critique (or only the rejected one) is a red flag — it suggests the model hallucinated the connection.
11. **`depends_on` dependencies should plausibly weaken the surviving finding if the rejected claim is wrong.** Read the surviving critique's hypothesis and the rejected critique's hypothesis and ask: "if the rejected one turned out to be false, would I still believe the surviving recommendation as strongly?" If yes, the relationship should probably be `engages_with`, not `depends_on`.
12. **`contradicts` is the rarest relationship.** In practice we'd expect 0–2 per run. If you see more, the model may be conflating `engages_with` with `contradicts`.

### Cross-stage checks (after synthesizer runs)

13. **Every `depends_on` entry in the linker output corresponds to a `CONDITIONAL` tag in the synthesizer report.** Grep the synthesizer markdown for `[CONDITIONAL — see dependencies]` and verify the finding titles match the linker's `surviving_critique_title` values.
14. **`engages_with` and `contradicts` entries do NOT produce CONDITIONAL tags.** Only `depends_on` propagates. This is by design — see `prompts/synthesizer.md` for the rule.
15. **Conditional Findings section in the synthesizer report references the rejected critique title verbatim** as the "Depends on" line, and the verdict label shown is `UNVERIFIABLE` or `REJECTED` (the human-facing label, not the `unverified`/`rejected` schema value).

### Cost / volume sanity

16. **Linker cost in `pipeline-stats.json` is small** — expect ~$0.05–0.30 for a Sonnet call with the current `MAX_TOKENS_LINKER = 4096`. A linker cost above $1 suggests the input construction (surviving + rejected blocks) is bloated; check `run_linker` in `pipeline/agents.py`.
17. **Dependency count is plausible vs. input sizes.** With, say, 8 surviving and 4 rejected critiques, expect 0–5 dependencies typically. Zero is valid (`(none found)`). Double-digit counts on small inputs suggest the model is being non-conservative — re-read the output and delete weak links, or tighten the "be conservative" rule in `prompts/linker.md`.

## What's NOT in the sample

Two things deliberately not illustrated here that you may see in a real run:

- **Low-confidence links.** The prompt explicitly invites `low` confidence entries for reviewer attention. A real run may include 1–2 such entries.
- **Justification spanning multiple lines with continuation wrapping.** The parser's `_extract_linker_field(..., multiline=True)` handles this, but the hand-constructed sample keeps justifications on a single logical line for clarity.
