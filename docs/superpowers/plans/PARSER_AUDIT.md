# Parser Audit: Stage Output Parsers

**Date:** 2026-04-13
**Scope:** All stage output parsers in `pipeline/agents.py`
**Prompted by:** P-004 fix revealing a pattern of naive line splitting
across parsers

## Audit Table

| Stage | Parser | Assumption | Continuation? | Vulnerability | Code Location | Recommendation |
|-------|--------|-----------|---------------|---------------|---------------|----------------|
| 01 Decomposer | `parse_decomposer_output` | Line-per-item (3 list fields) | NO → **YES** (fixed) | ~~High~~ Low | `agents.py:284-298` | **Fixed** — switched to `_parse_bullet_list` |
| 02 Investigator | `parse_investigator_output` | Line-per-item (evidence) | NO → **YES** (fixed) | ~~High~~ Low | `agents.py:375` | **Fixed** — switched to `_parse_bullet_list` |
| 03 Verifier | `parse_verifier_output` | `_parse_bullet_list` | YES | Low | `agents.py:551,569` | Already fixed (P-004) |
| 04 Quantifier | `parse_quantifier_output` | Regex blocks + `re.DOTALL` | YES | Low | `agents.py:655-773` | Leave alone — robust multi-strategy extraction |
| 05 Challenger | `parse_challenger_output` | Line-per-item (questions) | NO → **YES** (fixed) | ~~Medium~~ Low | `agents.py:990` | **Fixed** — switched to `_parse_bullet_list` (parser is deprecated/advisory; judge is authoritative) |
| 05 Advocate | `parse_advocate_self_assessment` | Keyword in full text | YES (inherent) | Low | `agents.py:1029` | Leave alone — no list parsing |
| 05 Judge | `parse_judge_output` | Structured field pairing | YES | Low | `agents.py:1090-1132` | Leave alone — `failure_type:`/`evidence:` pairing is robust |
| 05b Linker | `parse_linker_output` | Block headers + field extraction | YES (multiline flag) | Low | `agents.py:1259-1343` | Leave alone — `_extract_linker_field` handles continuations |
| 06 Synthesizer | (none) | N/A — raw text output | N/A | N/A | `agents.py:2257` | No parser to audit |

## Fixes Applied in This Audit

Three parsers used the identical naive line-per-item pattern as the
pre-fix verifier:

```python
items = [
    line.strip().lstrip("-•* ").strip()
    for line in raw.splitlines()
    if line.strip() and line.strip().lstrip("-•* ").strip()
]
```

All three were replaced with `_parse_bullet_list(raw)`, which joins
continuation lines and filters trivial fragments. 163/163 tests pass
after the changes.

### Observed fragments eliminated

| Stage | Run | Fragment count | Fragment types |
|-------|-----|---------------|----------------|
| Investigator | VAS | 6 | `':'` (×6) — from `_extract_section` header pattern issue (P-005) |
| Investigator | water-chlorination | 3 | `'Some'` (×2), `'The biological'` (×1) |
| Investigator | SMC | 5 | `':'` (×5) — same root cause as VAS |
| Decomposer | VAS | 1 | `'##'` (×1) |
| Challenger | all | 0 | None observed (but latent vulnerability existed) |

### Lowercase heuristic verification

The `_parse_bullet_list` function treats lowercase-starting lines as
continuations. This is safe for prose (evidence, caveats) but could
misfire on lists where items legitimately start lowercase (code
terms, parameter names).

**Verified per-stage:**
- **Decomposer** (`key_params`, `data_sources`, `exclusion_list`):
  Scanned all VAS items — zero start with lowercase. Safe.
- **Investigator** (`suggested_evidence`): Evidence items start with
  "UNGROUNDED", "Logical argument:", or similar uppercase phrases.
  Safe.
- **Challenger** (`key_unresolved`): Questions start with "What",
  "How", "Has". Safe.
- **Verifier** (already validated in P-004): Evidence and caveats
  start with "Claim", "Mali", "DRC", etc. Safe.

## New Bug Found: `_extract_section` Header Pattern (P-005)

The `':'` fragments in the investigator (11 of 14 total fragments)
have a different root cause than P-004's line-splitting issue. See
P-005 for details.

**Summary:** `_extract_section`'s header pattern `^[\s#*]*HEADER\s*:?\s*`
consumes leading `**` but not trailing `**:`, leaving `:` as content.
`_parse_bullet_list` filters this as a trivial fragment, so the
symptom is fixed, but the root cause in `_extract_section` persists.

## Structural Observation: Markdown → JSON Parsing

Every stage except the synthesizer emits markdown that gets parsed
back into Python dataclasses via regex/string operations. Each parser
is a failure point that wouldn't exist if the LLM emitted JSON
directly.

| Stage | LLM emits | Parsed via | Could emit JSON? |
|-------|-----------|-----------|-----------------|
| 01 Decomposer | Markdown sections | `_extract_section` + list splits | Yes, with prompt change |
| 02 Investigator | Markdown sections | `_extract_section` + list splits | Yes, with prompt change |
| 03 Verifier | Markdown sections | `_extract_section` + `_parse_bullet_list` | Yes, with prompt change |
| 04 Quantifier | Markdown with numbers | Multi-strategy regex | Partially — numbers in prose are hard to template |
| 05 Challenger | Markdown sections | `_extract_section` + keyword mapping | Yes, with prompt change |
| 05 Judge | Markdown with typed fields | `_extract_section` + field pairing | Yes, and would benefit most (complex field structure) |
| 05b Linker | Markdown with typed fields | Block split + field extraction | Yes, and already closest to structured output |

**Directional note:** Every prompt revision is an opportunity to
replace prose output with structured output. The judge and linker
parsers would benefit most — their output is already quasi-structured
(typed fields, paired key-value lines) but expressed in markdown that
requires fragile parsing. The quantifier would benefit least — its
output involves numbers embedded in reasoning prose that's hard to
template.

This is not a bug to fix now. It's a design direction for the next
prompt revision cycle.
