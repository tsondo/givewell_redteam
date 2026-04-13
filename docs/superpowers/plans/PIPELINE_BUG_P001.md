# Pipeline Bug P-001: Orphan `**` Markers in Investigator Output

**Status:** Open
**Severity:** Low (cosmetic; downstream consumers compensate defensively)
**Target repo:** `givewell_redteam`
**Affected file:** investigator output parser (location TBD during fix)

## Observation

In `results/vas/02-investigators.json`, every entry has `hypothesis` and
`mechanism` fields starting with `"** "`. Four entries also have `title`
fields ending with `**`:

- `"Frailty Selection and Competing Mortality Risks**"`
- `"Short-Term Protection Window Creating Mortality Displacement**"`
- `"Survivor Bias in Long-Term Benefit Calculations**"`
- `"Clustering of Prevented Deaths in Households with Multiple Risk Factors**"`

All 32 entries show the pattern on hypothesis and mechanism. The four
title cases appear to be where the investigator LLM varied the
formatting slightly and escaped the parser's cleanup.

## Root cause

The investigator prompt produces markdown-formatted output like:

```
**Title:** Frailty Selection and Competing Mortality Risks
**Hypothesis:** ** VAS mortality benefits may exhibit...
**Mechanism:** ** This would affect...
```

The parser that converts this to JSON strips the leading `**Label:**`
prefix but does not strip the trailing `**` that closes the bold
marker on the same line. For `hypothesis` and `mechanism`, the LLM
consistently writes a leading `** ` inside the field value (bold-closing
artifact), leaving it in the parsed output.

For four titles, the LLM wrote the title with trailing `**` instead of
letting the parser handle the closing marker, so stripping the prefix
leaves the suffix intact.

## Impact

Every downstream consumer (verifier, quantifier, adversarial, linker,
synthesizer, and now the extractor building graph.json) has to
defensively strip the artifact. The synthesizer already strips trailing
`**` from titles when producing findings — that's why the synthesizer's
output doesn't show the bug while the intermediate files do.

The extractor also strips the artifact. This is the compensation
pattern that a proper fix would remove.

## Proposed fix

One of:

1. **Parser-side (preferred).** Fix the investigator output parser to
   strip trailing `**` from all extracted field values, not just the
   leading `**Label:**` prefix. Single-line change most likely.
2. **Prompt-side.** Instruct the investigator to emit plain text for
   field values, not bolded text. Higher-risk — changes prompt behavior
   which is under the "prompts are read-only" rule.

The parser-side fix is better because:

- It respects the "prompts are experimental treatment" principle from
  CLAUDE.md. The prompt is doing what it was designed to do; the parser
  has a bug.
- Parser changes don't invalidate comparability across runs. Old runs
  stay analyzable; new runs produce cleaner output.
- Single fix vs. prompt tuning across seven agent prompts.

## Verification

After the fix, re-run the investigator on any test input and confirm:

- No hypothesis or mechanism starts with `"** "`.
- No title ends with `**`.
- Content is otherwise identical to pre-fix output (only the orphan
  markers change).

A simple regression check: compare pre-fix and post-fix JSON and assert
that `.strip('*').strip()` of every string field yields identical
output, and that no post-fix string starts or ends with `*`.

## When to fix

Next pipeline patch. Safe, self-contained, removes a defensive burden
from every downstream consumer.
