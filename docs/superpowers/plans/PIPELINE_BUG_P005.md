# Pipeline Bug P-005: `_extract_section` Header Pattern Leaves Trailing Bold+Colon as Content

**Status:** Open — symptom masked by `_parse_bullet_list` filter, root cause unfixed
**Severity:** Low (all downstream parsers now filter the artifact; no user-visible impact)
**Target repo:** `givewell_redteam`
**Affected stages:** All stages using `_extract_section` with bold-wrapped headers
**Discovered in:** Parser audit (2026-04-13), prompted by P-004 investigation

## Observation

When the LLM emits a section header in bold markdown format:

```
**EVIDENCE**:
- First item
- Second item
```

`_extract_section` extracts the content starting after the header
match but leaves `**:` as leading content. After `_strip_orphan_bold`
removes the `**`, a bare `:` remains as the first line of the
extracted text.

In parsers that use `_parse_bullet_list` (verifier, investigator,
decomposer, challenger — all post-P-004), the `:` is filtered as a
trivial fragment. The symptom is masked. But the root cause persists
in `_extract_section` and could surface in any future parser that
doesn't use `_parse_bullet_list`.

## Root Cause

`_extract_section` at `agents.py:209` builds this pattern:

```python
pattern = r"^[\s#*]*" + re.escape(header) + r"\s*:?\s*"
```

For header `"EVIDENCE"` against text `**EVIDENCE**:`:

1. `[\s#*]*` matches `**` (consuming the leading bold markers)
2. `EVIDENCE` matches `EVIDENCE`
3. `\s*:?\s*` tries to match `**:` — but `\s*` can't match `*`,
   so the optional `:?` and trailing `\s*` match nothing

The match covers `**EVIDENCE` (10 chars). Content starts at `**:`,
which after `_strip_orphan_bold` becomes `:`.

## Proposed Fix

Add `\**` after the header word to consume trailing bold markers:

**Current** (`agents.py:209`):
```python
pattern = r"^[\s#*]*" + re.escape(header) + r"\s*:?\s*"
```

**Proposed:**
```python
pattern = r"^[\s#*]*" + re.escape(header) + r"\s*\**\s*:?\s*"
```

The `\**` matches zero or more trailing asterisks between the header
word and the optional colon. This handles all observed formats:

| Format | Match | Remainder |
|--------|-------|-----------|
| `**EVIDENCE**:` | `**EVIDENCE**:` | (clean) |
| `**EVIDENCE**: ` | `**EVIDENCE**: ` | (clean) |
| `**EVIDENCE**` | `**EVIDENCE**` | (clean) |
| `EVIDENCE:` | `EVIDENCE:` | (clean, unchanged) |
| `## EVIDENCE` | `## EVIDENCE` | (clean, unchanged) |

## Risk Assessment

Low risk. The change adds a zero-or-more match for `*` after the
header word, which is already consumed in the leading `[\s#*]*`
prefix for the input side. No existing format would match differently
in a breaking way because:

- Headers without bold markers: `\**` matches zero chars (no change)
- Headers with `#` markers: `\**` matches zero chars (no change)
- Headers with bold: `\**` now correctly consumes trailing `**`

## When to Fix

Can be applied independently of any prompt revision — this is a
parser-only change that doesn't affect LLM output. Safe to apply
at any time. Currently low priority because all downstream parsers
filter the artifact via `_parse_bullet_list`.

## Cross-reference

- **P-004**: Verifier parser fragment fix. Introduced `_parse_bullet_list`
  which masks this bug's symptom.
- **P-001**: Orphan `**` markers in investigator output. Same family
  of bold-marker handling issue.
- **Parser Audit** (`PARSER_AUDIT.md`): Full audit that discovered
  this bug.
