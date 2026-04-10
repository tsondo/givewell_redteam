# Synthesizer Update + Linker Stage — Implementation Plan

> **For Claude Code:** Use targeted `str_replace` edits, not full file rewrites. No API access required for any task in this plan. The re-run of VAS happens in a separate later plan after this also lands. This project commits directly to main; do not create branches.

**Goal:** Update the synthesizer to consume the new judge audit data from Plan 1, fix the thread count hallucination, surface debate quality statistics as a first-class section in the report, and add structured handling of UNVERIFIABLE claims as conditional assumptions that propagate through to findings. The conditional-reasoning fix introduces a new Linker stage between adversarial and synthesizer that identifies dependencies between surviving critiques and rejected critiques as a first-class artifact.

**Architecture:** New Linker stage (Sonnet) reads surviving critiques + rejected critiques, produces `05b-linker.json` with structured dependency records. Synthesizer (Opus) consumes the existing inputs plus the linker output plus the decomposer output (for the thread count fix). Synthesizer prompt is rewritten to: (a) read counts from upstream data instead of guessing, (b) populate a new "Debate Quality Audit" section from judge audit data, (c) populate a new "Conditional Findings" section from linker output, (d) tag findings with their dependency status when applicable.

---

## Background

**Plan 1 landed three commits worth of changes.** The judge agent now produces structured `JudgeAudit` data on every adversarial entry, the debaters have updated prompts that prevent the failure modes the domain expert flagged, and the schema supports both old (no judge audit) and new (with judge audit) `DebatedCritique` records.

**The synthesizer has not yet been updated to consume this.** Right now the synthesizer reads `05-adversarial.json` and produces a report using only the surviving critique data — it ignores judge audits entirely, including failure mode lists, verdict justifications, and the per-debate resolved/unresolved summaries. This is the next thing to fix.

**Three additional issues bundle naturally with the synthesizer update:**

1. **Thread count hallucination.** The synthesizer fabricates the "Investigation threads examined" number rather than reading it from the decomposer's actual output. Fix: pass `01-decomposer.json` to the synthesizer and have it read the count from there.

2. **Conditional reasoning.** Mikyo's epistemological point: an UNVERIFIABLE verdict means "the verifier could not assess this directly" — it does not mean the claim is false. When a surviving finding's argument depends on an unverified claim, the finding should propagate that dependency explicitly. Currently the synthesizer treats surviving findings and rejected claims as completely separate inputs with no awareness of dependencies between them.

3. **Debate quality visibility.** The judge agent now produces failure mode flags and `sound_synthesis_noted` markers on every debate. None of this currently surfaces in the report. The aggregate distribution is exactly the calibration metric the project has been missing.

**The conditional reasoning fix requires structural support, not just a prompt change.** Computing dependencies between surviving and rejected critiques is a separate cognitive task from synthesizing the final report. Bundling both into the synthesizer prompt would either produce unreliable LLM-inference dependencies or force the synthesizer to do two unrelated jobs in one pass. Cleaner: a new Linker stage that does the dependency identification as its own structured task with its own auditable artifact.

---

## File Map

| Action | File | Responsibility |
|--------|------|----------------|
| Modify | `pipeline/schemas.py` | Add `CritiqueDependency` and `LinkerOutput` dataclasses |
| Create | `prompts/linker.md` | Linker agent prompt |
| Modify | `pipeline/agents.py` | Add `run_linker` and `parse_linker_output`; update `run_synthesizer` signature and user message construction |
| Modify | `pipeline/run_pipeline.py` | Add linker stage between adversarial and synthesizer; load decomposer output for synthesizer |
| Modify | `pipeline/config.py` | Add `MAX_TOKENS_LINKER` constant |
| Modify | `prompts/synthesizer.md` | Read counts from data; new Debate Quality Audit section; new Conditional Findings section; consume linker output |
| Modify | `tests/test_agents.py` | Linker parser tests, synthesizer prompt construction tests |
| Modify | `tests/test_schemas.py` | New schema round-trip tests |

---

## Task 1: Schema additions

**Files:**
- Modify: `pipeline/schemas.py`

- [ ] **Step 1: Add `CritiqueDependency` dataclass**

```python
@dataclass
class CritiqueDependency:
    """A dependency relationship between a surviving critique and a rejected
    critique, identified by the Linker stage.

    The relationship type captures whether the surviving critique's argument
    requires the unverified claim to be true, merely engages with it, or
    actively contradicts it. This distinction matters because findings that
    depend on unverified claims must be tagged as conditional, while findings
    that merely engage with them can stand on their own.
    """

    surviving_critique_title: str
    rejected_critique_title: str
    rejected_critique_verdict: str  # "unverifiable" | "rejected"
    relationship: str  # "depends_on" | "engages_with" | "contradicts"
    justification: str  # 1-2 sentences citing where in the surviving critique
                        # the dependency appears
    confidence: str  # "high" | "medium" | "low" — Linker's confidence in the link

    def to_dict(self) -> dict[str, Any]:
        return dataclasses.asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> CritiqueDependency:
        return cls(**d)
```

- [ ] **Step 2: Add `LinkerOutput` dataclass**

```python
@dataclass
class LinkerOutput:
    """Output of the Linker stage. Top-level artifact written to 05b-linker.json.

    Contains the full list of dependencies identified across all surviving
    critiques. May be empty (no dependencies found) — that is a valid result.
    """

    dependencies: list[CritiqueDependency]
    # Optional summary stats for downstream consumers
    n_surviving_critiques_examined: int
    n_rejected_critiques_available: int
    n_dependencies_found: int

    def to_dict(self) -> dict[str, Any]:
        return {
            "dependencies": [d.to_dict() for d in self.dependencies],
            "n_surviving_critiques_examined": self.n_surviving_critiques_examined,
            "n_rejected_critiques_available": self.n_rejected_critiques_available,
            "n_dependencies_found": self.n_dependencies_found,
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> LinkerOutput:
        return cls(
            dependencies=[
                CritiqueDependency.from_dict(dep) for dep in d.get("dependencies", [])
            ],
            n_surviving_critiques_examined=d.get("n_surviving_critiques_examined", 0),
            n_rejected_critiques_available=d.get("n_rejected_critiques_available", 0),
            n_dependencies_found=d.get("n_dependencies_found", 0),
        )
```

- [ ] **Step 3: Verify schemas import and round-trip**

Construct a `LinkerOutput` with at least one `CritiqueDependency`, serialize to dict, parse back, confirm equality. Also verify that an empty `LinkerOutput` (no dependencies) round-trips correctly — that's the expected case when a run has no dependencies, and it must not crash.

---

## Task 2: Add Linker config

**Files:**
- Modify: `pipeline/config.py`

- [ ] **Step 1: Add token limit constant**

```python
MAX_TOKENS_LINKER: int = 4096  # linker output is structured, not narrative
```

The linker uses Sonnet (cheaper than Opus, adequate for structured matching). No new model constant needed — use the existing `SONNET_MODEL`.

---

## Task 3: Create the Linker prompt

**Files:**
- Create: `prompts/linker.md`

- [ ] **Step 1: Write the prompt**

```markdown
# Critique Dependency Linker

## Role

You identify dependency relationships between surviving critiques and rejected
critiques in a multi-agent red-teaming pipeline for cost-effectiveness analyses.

A "surviving critique" is one that passed verification and adversarial review.
A "rejected critique" is one the verifier marked as either UNVERIFIABLE (no
direct evidence found) or REJECTED (contradicting evidence found).

Your job: for each surviving critique, identify whether it argues from, engages
with, or contradicts any of the rejected critiques. Output a structured list of
dependencies.

## Why this matters

An UNVERIFIABLE verdict does NOT mean a claim is false. It means the verifier
could not directly assess it from available evidence. When a surviving critique's
argument depends on an unverified claim, the surviving finding is *conditional*
on that assumption — and downstream readers need to know this so they can
correctly evaluate how robust the finding is.

Treating unverified claims as if they were discardable produces biased reasoning
("we can't measure X, therefore X doesn't matter"). The correct treatment is to
carry the assumption forward as an explicit tag: "this finding holds CONDITIONAL
ON assumption A; if A is wrong, the finding's recommendation changes."

Your output enables the synthesizer to produce conditional-tagged findings.

## Inputs

You will receive:

1. **Surviving critiques**: Each with title, hypothesis, mechanism, verifier
   evidence summary, and the judge's debate audit.
2. **Rejected critiques**: Each with title, hypothesis, mechanism, verdict
   (UNVERIFIABLE or REJECTED), and the verifier's reasoning for the verdict.

## Task

For each surviving critique, scan all rejected critiques and identify any that
have one of three relationships:

### depends_on
The surviving critique's argument requires the rejected claim to be true (or at
least plausible). If the rejected claim is wrong, the surviving critique's
recommendation changes or weakens.

Example: A surviving critique argues "VAS effectiveness depends on baseline VAD
prevalence; in low-VAD locations, the program may not be cost-effective." A
rejected critique was "Threshold effects in VAD prevalence" (UNVERIFIABLE). The
surviving critique *depends_on* the threshold mechanism even though it wasn't
directly verified.

### engages_with
The surviving critique addresses or references the rejected claim but doesn't
require it to be true. The surviving critique would still hold even if the
rejected claim turned out to be false.

Example: A surviving critique argues "Even granting the strongest plausible VAS
mortality effect, cost-effectiveness varies by 5x across countries due to delivery
costs." This *engages_with* a rejected critique about mortality effect magnitude
without depending on it.

### contradicts
The surviving critique actively contradicts the rejected claim. The surviving
critique's validity is *strengthened* by the rejected claim being wrong.

Example: A surviving critique argues "Administrative coverage is inflated by
double-counting." A rejected critique argued "Coverage rates are accurate because
they're based on multiple data sources" (REJECTED with contradicting evidence
found). These *contradict* each other.

## Output format

Use exactly the following format. The parser depends on it.

```
## DEPENDENCIES

[For each dependency found, produce one block. If none found, write "(none found)"
and stop.]

### Dependency 1
surviving: [exact title of surviving critique]
rejected: [exact title of rejected critique]
verdict: [unverifiable | rejected]
relationship: [depends_on | engages_with | contradicts]
confidence: [high | medium | low]
justification: [1-2 sentences citing where in the surviving critique the
dependency appears]

### Dependency 2
[same format]
```

## Critical rules

1. **Use exact titles.** The parser matches on title strings. If you paraphrase
   or abbreviate, the link won't be made.
2. **Be conservative.** When in doubt, do not link. A false positive (claiming
   a dependency that isn't really there) is worse than a false negative
   (missing a dependency). The synthesizer will tag findings as conditional
   based on your output, and incorrect tags create confusion.
3. **Confidence calibration.**
   - **high**: the surviving critique explicitly references the rejected claim's
     subject matter and the dependency is unmistakable
   - **medium**: the dependency is implicit but clear from reading both
   - **low**: the connection is plausible but uncertain — include it for
     reviewer attention but flag the uncertainty
4. **Empty output is acceptable.** If no dependencies exist across all surviving
   and rejected critiques, write "(none found)" and stop. This is a valid result
   and the synthesizer handles it correctly.
5. **One pair, one entry.** Don't list the same surviving/rejected pair twice
   even if they have multiple connection points. Pick the strongest relationship
   type and the most representative justification.
```

- [ ] **Step 2: Verify the prompt file is well-formed**

Read it back, confirm markdown structure is intact.

---

## Task 4: Implement `run_linker` and parser

**Files:**
- Modify: `pipeline/agents.py`

- [ ] **Step 1: Add `parse_linker_output` function**

The linker produces structured output with `### Dependency N` sections. Parse them into a list of `CritiqueDependency` objects, then wrap in a `LinkerOutput` with the summary stats.

Apply the lessons from prior parser work:
- Deduplicate matches by section header (in case of restated headers)
- Handle the `(none found)` case explicitly — return an empty `LinkerOutput` with stats but no dependencies
- For each parsed entry, validate that `relationship` is one of the three allowed values; skip and log invalid entries rather than crashing

- [ ] **Step 2: Add `run_linker` function**

Signature:

```python
def run_linker(
    surviving_critiques: list[DebatedCritique],
    rejected_critiques: list[VerifiedCritique],
    stats: PipelineStats,
    intervention: str,
) -> LinkerOutput:
```

Inside:
- Load `prompts/linker.md` as system prompt
- Construct user message with two clearly labeled sections: "## Surviving Critiques" (with title, hypothesis, mechanism, judge audit summary for each) and "## Rejected Critiques" (with title, hypothesis, verdict, verifier reasoning for each)
- If `len(rejected_critiques) == 0`, skip the API call entirely and return `LinkerOutput(dependencies=[], n_surviving_critiques_examined=len(surviving_critiques), n_rejected_critiques_available=0, n_dependencies_found=0)`. No work to do.
- If `len(surviving_critiques) == 0`, same — empty result.
- Otherwise, call the API with `SONNET_MODEL`, `MAX_TOKENS_LINKER`, stage name `"linker"`
- Parse with `parse_linker_output`
- Populate the summary stats from the inputs
- Save to `RESULTS_DIR / intervention / "05b-linker.json"` and `.md`
- Return the `LinkerOutput`

- [ ] **Step 3: Verify the function imports and the existing tests still pass**

---

## Task 5: Wire the linker into the orchestrator

**Files:**
- Modify: `pipeline/run_pipeline.py`

- [ ] **Step 1: Add the linker call between adversarial and synthesizer**

Find where `run_adversarial` is called and where `run_synthesizer` is called. Insert a `run_linker` call between them. The linker takes:
- Surviving critiques: from `run_adversarial`'s output
- Rejected critiques: from `run_verifier`'s third return value (the rejected list, already loaded by the orchestrator per the persistence fix)

- [ ] **Step 2: Update the synthesizer call**

The synthesizer now needs three additional inputs that the orchestrator must load and pass:
- The linker output (from step 1 above)
- The decomposer output (`01-decomposer.json`) for the thread count fix
- The full set of judge audits (already on the surviving critiques as `debated.judge_audit`)

If the orchestrator currently re-reads stage outputs from disk between stages, follow that pattern. If it passes return values directly, follow that pattern. Match existing convention.

- [ ] **Step 3: Update the resume logic**

The pipeline has a `--resume-from` mechanism. When resuming from `synthesizer`, the orchestrator should now also load `05b-linker.json`. When resuming from `linker`, it should load adversarial output and rejected critiques. Add `linker` as a valid resume target if it isn't already.

If the resume logic doesn't currently support this kind of dependency loading, **stop and report**. We may need a small refactor.

- [ ] **Step 4: Verify the orchestrator imports cleanly**

---

## Task 6: Update the synthesizer

**Files:**
- Modify: `pipeline/agents.py` (the `run_synthesizer` function)
- Modify: `prompts/synthesizer.md`

- [ ] **Step 1: Update `run_synthesizer` signature**

Add three new parameters:
- `linker_output: LinkerOutput`
- `decomposer_output: DecomposerOutput` (or whatever the existing dataclass is called — find by inspection)
- The judge audits are already on the `DebatedCritique` objects, no new parameter needed

The user message construction needs to include these as clearly labeled sections.

Suggested format for the new user message:

```
## Decomposer Output (for accurate counts)
Investigation threads examined: [N]
[Brief thread titles list]

## Surviving Critiques
[existing format unchanged]

## Rejected Critiques (from verifier — DO NOT generate new entries)
[existing persistence-fix format unchanged]

## Critique Dependencies (from linker)
[For each dependency in linker_output.dependencies, formatted as:
  - surviving: [title]
    rejected: [title] (verdict: unverifiable | rejected)
    relationship: [type] (confidence: [level])
    justification: [text]
If linker_output.dependencies is empty, write "(no dependencies identified)".]

## Judge Audit Aggregate (computed from surviving critiques)
[Code in run_synthesizer should compute the aggregate failure mode counts
from all judge audits and pass them in. Format as:
  - Total critiques debated: N
  - Sound syntheses noted: M
  - Failure mode counts:
    - unsupported_estimate_fabricated: K
    - unsupported_estimate_pseudo: L
    - unsupported_estimate_counter: ...
    - whataboutism: ...
    - call_to_ignorance: ...
    - strawmanning: ...
    - false_definitiveness: ...
    - generic_recommendation: ...
    - misrepresenting_evidence_status: ...
  - Most common Advocate failure: [type]
  - Most common Challenger failure: [type]]
```

The aggregation logic should be computed in Python before constructing the message — don't ask the LLM to count things. The LLM will use the pre-computed numbers.

- [ ] **Step 2: Rewrite the synthesizer prompt**

`view` `prompts/synthesizer.md` and identify the sections that need to change. The goal is to:

1. Replace any creative count generation with explicit "read this from the Decomposer Output section"
2. Add a new "Debate Quality Audit" section in the report output format
3. Add a new "Conditional Findings" treatment for findings that have linker dependencies
4. Forbid creative content in the existing sections that already have data sources (Open Questions, Resolved Negatives — these came from the persistence fix and should already be input-bound, but verify)

Suggested additions to the prompt's output format section:

```markdown
## Pipeline Summary

Read these counts from the input data sections, do not generate them:
- Investigation threads examined: [from Decomposer Output]
- Candidate critiques generated: [from Surviving + Rejected counts]
- Surviving critiques: [count from Surviving Critiques input]
- Rejected critiques: [count from Rejected Critiques input]
- Dependencies identified: [count from Critique Dependencies input]

CRITICAL: If you cannot find a count in the input data, write "(not available)"
rather than estimating. Estimating counts is forbidden.

## Critical Findings (surviving strength: STRONG)

[Existing format. New requirement: if a finding's title appears in the Critique
Dependencies input as the surviving side of a "depends_on" relationship, mark
the finding as CONDITIONAL and add a "Conditional on:" subsection.]

### Finding 1: [Title] [CONDITIONAL — see dependencies]
**Impact:** ...
**Evidence:** ...
**Conditional on:** [If this finding has any depends_on dependencies in the
linker input, list each one here in the format: "the unverified claim that X
(rejected critique title)". If multiple, list all. If none, OMIT this subsection
entirely — do not write "Conditional on: none".]
**GiveWell's best defense:** ...
[...rest of existing format]

## Significant Findings (surviving strength: MODERATE)
[Same format, briefer. Apply CONDITIONAL tagging the same way.]

## Debate Quality Audit (from judge agent data)

This section reports the calibration of the adversarial stage based on the
judge agent's per-debate audit. Read all numbers from the Judge Audit
Aggregate input section — do not estimate or generate.

**Total debates audited:** [N]
**Sound analytical moves noted:** [M] across all debates

**Failure modes detected:**
[Format as a table or list, copying counts directly from the input.]

**Patterns:**
[1-3 sentences interpreting the patterns. Acceptable interpretations:
- "The Advocate side most frequently failed by [type], suggesting [observation]"
- "Sound syntheses outnumbered failure modes by [ratio], indicating substantive
  analytical engagement"
- "[type] failures clustered in [thread name] critiques, suggesting the prompts
  may need [specific tuning]"
DO NOT make up patterns that aren't supported by the numbers. If the numbers
don't support a clear interpretation, write "No clear pattern across this run."]

## Conditional Findings (from linker output)

This section consolidates the findings that have explicit dependencies on
unverified claims. It does NOT introduce new findings — it cross-references
findings already listed above.

For each finding above marked CONDITIONAL, include here:

### [Finding title]
**Depends on:** [the rejected critique title] ([unverifiable | rejected])
**Verifier's reasoning for marking it [verdict]:** [from rejected critique input]
**If the assumption holds:** [the finding's recommendation, restated briefly]
**If the assumption is wrong:** [how the recommendation changes — derive this
from the finding's logic, do not speculate]

If no findings are CONDITIONAL, write "(no findings depend on unverified claims
in this run)" and move on. This is a valid result.

## Open Questions (from Rejected Critiques input — verdict: UNVERIFIABLE)
[Existing format from persistence fix, unchanged. CRITICAL RULES blocks remain
in place forbidding creative generation.]

## Resolved Negatives (from Rejected Critiques input — verdict: REJECTED)
[Existing format from persistence fix, unchanged.]

## Meta-Observations

[Existing format. New requirement: at least one meta-observation should
reference the Debate Quality Audit data — for example, "the prevalence of
[failure mode] across debates suggests [structural finding about the
critiques themselves, not the pipeline]."]
```

- [ ] **Step 3: Verify the prompt file is well-formed**

---

## Task 7: Tests

**Files:**
- Modify: `tests/test_agents.py`
- Modify: `tests/test_schemas.py`

- [ ] **Step 1: Schema round-trip tests**

- `CritiqueDependency` round-trips via `to_dict` / `from_dict`
- `LinkerOutput` with multiple dependencies round-trips
- `LinkerOutput` with empty dependencies list round-trips and doesn't crash
- `LinkerOutput.from_dict` handles missing optional fields gracefully (the same backward-compatibility pattern as `JudgeAudit.from_dict`)

- [ ] **Step 2: Linker parser tests**

Hand-craft a fake linker response containing:
- One `depends_on` dependency with high confidence
- One `engages_with` dependency with medium confidence
- One `contradicts` dependency with low confidence

Call `parse_linker_output` and assert all three are extracted with correct field values.

Add a second test for the `(none found)` case: a linker response that contains the section header but no dependency blocks. Assert `parse_linker_output` returns an empty `LinkerOutput`.

Add a third test for malformed entries: an entry with `relationship: invalid_value` should be skipped, not crash the parser.

- [ ] **Step 3: Synthesizer prompt construction test**

This is a contract test similar to the one in Plan 1 for the judge. Construct fake `surviving_critiques`, `rejected_critiques`, `linker_output`, and `decomposer_output`. Call the user-message-building helper inside `run_synthesizer` (extract it if needed for testability). Assert that the resulting message contains:

- A "Decomposer Output" section with the thread count
- A "Critique Dependencies" section
- A "Judge Audit Aggregate" section with the failure mode counts
- A "Surviving Critiques" section
- A "Rejected Critiques" section split by verdict

Also test the empty-dependencies case: when `linker_output.dependencies` is empty, the message should still have the Critique Dependencies section but say "(no dependencies identified)".

- [ ] **Step 4: Linker short-circuit tests**

Test that `run_linker` returns an empty `LinkerOutput` without making an API call when:
- `surviving_critiques` is empty
- `rejected_critiques` is empty
- Both are empty

These edge cases must not crash and must not waste API spend.

- [ ] **Step 5: Run the full test suite**

All prior tests + new tests pass. If any prior test breaks, **stop and report**.

---

## Task 8: Commit

Three logical commits, in order:

1. **Schema additions** (`schemas.py` + schema tests)

   Commit message: explain the new dataclasses, motivate the structural choice (separate stage rather than inline LLM inference), reference the conditional reasoning principle from the domain expert review.

2. **Linker stage** (`prompts/linker.md` + `agents.py` linker functions + `config.py` constant + `run_pipeline.py` orchestration + linker parser tests)

   Commit message: explain that the linker identifies dependencies between surviving critiques and rejected/unverifiable critiques, motivate the Sonnet-not-Opus model choice (structured matching task), reference the empty-input short-circuit behavior.

3. **Synthesizer update** (`prompts/synthesizer.md` + `agents.py` synthesizer changes + `run_pipeline.py` updates + synthesizer prompt construction test)

   Commit message: explain the four changes — count reading from upstream data (thread count fix), Debate Quality Audit section, Conditional Findings section, conditional tagging on individual findings. Reference Plan 1 (judge audit data is now consumed) and the persistence fix (rejected critiques input format unchanged from prior synthesizer prompt).

Use Co-Authored-By trailers as standard.

---

## Stop Conditions Requiring Tsondo Input

- The orchestrator's resume logic doesn't currently support loading multiple intermediate stage outputs cleanly (Task 5 Step 3)
- A test fails for reasons not addressed by Task 7
- The existing synthesizer prompt has structural elements not anticipated by this plan that conflict with the rewrite (in which case, propose minimal-change alternatives rather than ripping out existing structure)
- The decomposer output schema doesn't have a clean way to extract the thread count (in which case, report what fields are available and we'll decide how to compute it)

## Things You Should NOT Do

- Re-run any pipeline stages — the re-run is the next plan after this lands
- Modify the conclusions doc — that's after the re-run
- Modify any existing report files in `results/*/06-synthesizer.{md,json}`
- Touch the verifier or quantifier or adversarial stages — only the linker (new) and synthesizer are in scope
- Activate the API key — no task in this plan requires it
- Create branches — commit directly to main as before
