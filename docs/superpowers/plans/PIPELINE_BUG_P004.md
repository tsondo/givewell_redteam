# Pipeline Bug P-004: Parser Fragments in Verifier `caveats` and `evidence_found` Arrays

**Status:** Fixed — root cause and filter both applied; 21/21 tests pass
**Severity:** Medium (polluted evidence extraction; affected 13/28 critiques in VAS run)
**Target repo:** `givewell_redteam`
**Affected stage:** 03-verifier (output parser)
**Cross-reference:** P-001 (similar parser issue, already fixed). Same family of bug.

## Observation

The verifier's `caveats` and `evidence_found` arrays contain bullets
that are not evidence atoms but fragments of broken sentences. From
the VAS run's `03-verifier.json`:

```
'.', '. However,', 'Evidence:', 'Claim:', 'and', 'where data exist.'
```

These appeared 28 times across 13 of the 28 critiques. Examples:

| Critique idx | Field | Bullet |
|---|---|---|
| 3 | caveats | `'Claim:'` |
| 3 | evidence_found | `'. However,'` |
| 4 | evidence_found | `'.'` (×3) |
| 4 | evidence_found | `'. However,'` |
| 17 | caveats | `'and'` |
| 19 | caveats | `'Evidence:'` (×2) |
| 23 | evidence_found | `'where data exist.'` |

Source: results from `scan_classified.py` in the source-extraction
prevalence scan session.

## Root cause hypothesis

The verifier LLM emits prose with inline structural markers like:

```
[Claim X]: VERIFIED - [reasoning]. However, [caveat]. Evidence:
[bulleted content].
```

A parser is splitting this prose into bullet arrays at the wrong
boundaries, capturing structural fragments (`. However,`, `Evidence:`,
sentence-terminating periods) as if they were standalone evidence
items.

Likely culprits:
- A regex that splits on bullet-marker characters (`-`, `•`, `*`,
  numbered lists) without checking that the resulting fragments are
  substantive
- A line-by-line splitter that treats every newline as a bullet
  boundary
- An overly-permissive sentence splitter combined with bullet
  reconstruction

Without seeing the parser code, the spec describes what the fix
needs to accomplish rather than where to apply it. Investigation
should locate the exact function in the 03-verifier output handling.

## Impact

**Direct:** Evidence extraction (current and future) needs to filter
parser fragments. The graph.json extractor in `red_team_explorer`
already has implicit handling because it ignores anything below a
length/word threshold, but this is compensation for an upstream bug
that should be fixed at the source.

**Downstream:** Source extraction (planned for v0.3 of the schema)
will be more reliable if it doesn't have to defensively skip 13% of
input atoms. Per the prevalence scan: 28 of 221 atoms (13%) are
parser fragments.

**Pattern continuation risk:** P-001 was the same family of bug
(orphan `**` markers in investigator output). If parser hygiene is
weak across multiple stages, more bugs of this shape are likely
elsewhere. P-004 is an opportunity to audit parsing across stages
generally, not just patch this one.

## Affected critiques in VAS run

Critiques with at least one parser fragment in their evidence:

```
3, 4, 5, 6, 7, 8, 17, 19, 20, 21, 22, 23, 24
```

Critique 19 has the most fragments (5 — including 2 instances of
`'Evidence:'` and several bare periods).

## Fix applied (2026-04-13)

### Root cause

`parse_verifier_output()` at `agents.py:476-502` used a naive
newline splitter for both `evidence_found` and `caveats`:

```python
evidence_items = [
    line.strip().lstrip("-•* ").strip()
    for line in evidence_raw.splitlines()
    if line.strip() and line.strip().lstrip("-•* ").strip()
]
```

The verifier LLM writes evidence as quoted text with periods and
transitions on separate lines:

```
Mali is specifically listed among 12 countries...
.
DRC is among 15 countries...
.
Mali implemented voluntary vitamin A oil fortification...
. However,
the actual coverage may be limited...
.
```

The naive splitter treats every non-empty line as a separate item,
creating standalone fragment items from sentence-ending punctuation
and transition phrases.

### What changed

Replaced the naive splitter with `_parse_bullet_list()` (new function
at `agents.py:445`). The function:

1. **Recognizes bullet markers** (`-`, `•`, `*`, `1.`) as new-item
   boundaries — same as before.
2. **Joins continuation lines** to the previous item. A line is a
   continuation if it:
   - Matches the fragment regex (bare punctuation, structural markers
     like `Evidence:` / `Claim:`, bare conjunctions)
   - Is very short (<15 chars) with no substantive word
   - Starts with punctuation (`.`, `,`, `;`) — sentence continuation
   - Starts with lowercase — wrapped text after a line break
3. **Filters remaining trivial items** in a final pass after joining.

Helper `_is_continuation()` encapsulates the continuation detection
logic.

### Verification

- 163/163 tests pass (21 parser tests, 142 others).
- 3 new regression tests added to `tests/test_parsing.py`:
  - `test_parse_bullet_list_joins_fragments` — reproduces VAS Critique
    4 evidence pattern; asserts 3 items with no standalone fragments
  - `test_parse_bullet_list_filters_structural_markers` — asserts
    `Evidence:` and `Claim:` bullet content is filtered
  - `test_parse_bullet_list_preserves_normal_bullets` — asserts clean
    bulleted lists pass through unchanged
- Tested against actual VAS Critique 4 raw text: old parser produced
  8 items (4 fragments); new parser produces 3 clean items with
  continuations properly joined.

## Note on run comparability

This fix changes the parser, not a prompt, so it does **not**
invalidate prior run comparability. Existing `03-verifier.json` files
are already written; the parser only runs at pipeline execution time.
Future runs will produce cleaner evidence arrays, but the raw LLM
output (preserved in `03-verifier.md`) is unchanged.

## Cross-references

- **P-001** (orphan `**` markers): same family — parser hygiene
  issue in a stage's output processing. Already fixed.
- **P-002** (synthesizer CONDITIONAL fabrication): unrelated, but
  bundled into the same coordinated revision.
- **P-003** (intra-critique conditionals): unrelated; design question.
- **SOURCE_SCAN_RESULTS.md**: this spec was produced from data in
  the prevalence scan; reference for affected-critique list and
  fragment examples.
