# Multi-Agent Red Teaming Pipeline: Architecture Specification

---

## Overview

This document specifies a six-stage pipeline for AI red teaming of GiveWell's cost-effectiveness analyses. Each stage is a separate agent with scoped context, explicit inputs/outputs, and a defined role. The pipeline separates hypothesis generation from evidence retrieval, quantitative reasoning from qualitative judgment, and critique from defense.

The pipeline exists in two forms:

- **Manual version:** Sequential prompts run in a Claude Project. A human copies outputs between stages. GiveWell could adopt this directly.
- **Automated version:** A Python script (`run_pipeline.py`) that orchestrates API calls, passes outputs between stages, and executes code against CEA spreadsheets.

Both versions use identical prompts and produce identical output structure.

---

## Pipeline Flow

```
┌─────────────┐
│  DECOMPOSER  │  Reads: intervention report + CEA summary
│              │  Produces: investigation threads + CONTEXT.md per thread + exclusion list
└──────┬───────┘
       │  (one thread per Investigator)
       ▼
┌─────────────┐
│ INVESTIGATOR │  ×N (one per thread)
│              │  Reads: scoped CONTEXT.md + relevant source subset
│              │  Produces: candidate critiques (hypotheses, no citations required)
└──────┬───────┘
       │  (all candidate critiques)
       ▼
┌─────────────┐
│   VERIFIER   │  Reads: each candidate critique + retrieval tools
│              │  Produces: verified critiques (grounded) OR flagged hypotheses (ungrounded)
└──────┬───────┘
       │  (verified + flagged critiques)
       ▼
┌─────────────┐
│  QUANTIFIER  │  Reads: verified critiques + CEA spreadsheet (code execution)
│              │  Produces: parameter mapping + sensitivity analysis per critique
└──────┬───────┘
       │  (quantified critiques)
       ▼
┌─────────────────────┐
│  ADVERSARIAL PAIR    │  Advocate defends GiveWell's position
│  (Advocate+Challenger)│  Challenger argues for the critique
│                      │  Produces: stress-tested critiques with defense/attack summaries
└──────┬───────────────┘
       │  (surviving critiques)
       ▼
┌─────────────┐
│ SYNTHESIZER  │  Reads: all surviving critiques with verification, quantification, and debate records
│              │  Produces: ranked final output with evidence, impact estimates, confidence levels
└─────────────┘
```

---

## Stage Specifications

### Stage 1: Decomposer

**Purpose:** Read the intervention report and CEA, then produce scoped investigation threads. This replaces GiveWell's approach of giving a single model everything and asking for 20–30 critiques.

**Inputs:**
- GiveWell intervention report (full text)
- CEA spreadsheet summary (key parameters, structure, adjustments)
- GiveWell's published AI red teaming output for this intervention (if available, for baseline comparison)

**Outputs:**
1. **Investigation threads** (5–8). Each thread is a scoped area of inquiry with:
   - Thread name (e.g., "External Validity of Trial Evidence")
   - Scope definition: what questions this thread investigates
   - Key parameters in the CEA that this thread could affect
   - Relevant source materials for this thread
2. **Exclusion list.** Concerns GiveWell already addresses in their report or CEA adjustments. Investigators must not duplicate these.
3. **CEA parameter map.** A structured summary of the CEA's key parameters, their current values, and which adjustments are applied. Used by the Quantifier downstream.

**Design rationale:** The Decomposer sees the full picture but doesn't generate critiques. Its job is strategic: identify where to look and what not to repeat. This prevents the "lost context" failure mode by ensuring downstream agents get focused, relevant subsets of information.

---

### Stage 2: Investigators (×N)

**Purpose:** Generate candidate critiques within a single scoped investigation thread. Investigators are hypothesis generators — they identify concerns worth checking, not proven claims.

**Inputs:**
- CONTEXT.md for this thread (from Decomposer)
- Relevant subset of source materials
- Exclusion list (from Decomposer)

**Outputs:**
- 3–6 candidate critiques per thread, each containing:
  - **Hypothesis:** A clear statement of what might be wrong or missing
  - **Mechanism:** How this would affect cost-effectiveness if true
  - **Parameters affected:** Which CEA parameters would change
  - **Suggested evidence:** What data or sources would confirm or refute this (but the Investigator does NOT claim to have found this evidence)
  - **Estimated direction:** Would this increase or decrease cost-effectiveness?

**Critical constraint:** Investigators do NOT cite evidence. They do NOT claim papers say things. They identify hypotheses and suggest where to look. This is the key architectural separation that prevents hallucinated citations.

**Design rationale:** By scoping each Investigator to a single thread, we prevent attention dilution across the full report. By prohibiting citation, we eliminate the single largest source of hallucination in GiveWell's current output.

---

### Stage 3: Verifier

**Purpose:** Take each candidate critique and attempt to ground it in real evidence. The Verifier is the fact-checker — it searches for supporting or refuting evidence and confirms or denies factual claims.

**Inputs:**
- Each candidate critique from Investigators
- Access to web search and document retrieval tools
- The original intervention report (for cross-reference)

**Outputs:**
For each critique, one of:
- **VERIFIED:** The critique is grounded in real evidence. Output includes:
  - Actual citations with quotes or specific findings
  - Assessment of evidence strength (strong / moderate / weak)
  - Any caveats or limitations of the supporting evidence
- **PARTIALLY VERIFIED:** The hypothesis is plausible but evidence is incomplete. Output includes:
  - What was found and what wasn't
  - Assessment of plausibility given available evidence
  - Specific gaps that would need to be filled
- **UNVERIFIED:** No supporting evidence found. Output includes:
  - What searches were conducted
  - Whether absence of evidence is informative (i.e., if evidence should exist but doesn't, that's different from a topic with sparse literature)
  - Recommendation: discard or flag for human investigation

**Design rationale:** Verification as a separate stage means the pipeline never presents a hallucinated citation to the human reviewer. Unverified critiques are transparently labeled, not silently mixed with grounded ones. This directly addresses GiveWell's observation that "AI works best as a brainstorming tool, not a fact-checker" — we agree, so we don't ask the same agent to do both.

---

### Stage 4: Quantifier

**Purpose:** Take verified critiques and determine their impact on GiveWell's bottom-line cost-effectiveness estimate by programmatically interrogating the CEA spreadsheet.

**Inputs:**
- Verified and partially verified critiques (from Verifier)
- CEA spreadsheet (local .xlsx file)
- CEA parameter map (from Decomposer)

**Outputs:**
For each critique:
- **Parameters affected:** Which specific cells/parameters in the CEA this critique targets
- **Current values:** What GiveWell currently assumes for these parameters
- **Plausible alternative range:** What the parameter values would be if the critique is valid (with justification)
- **Sensitivity result:** The change in final cost-effectiveness (units of value per dollar) when the parameter is moved across the alternative range
- **Materiality assessment:** Whether the critique changes cost-effectiveness by more than 10% (material), 1–10% (notable), or <1% (immaterial)

**Implementation note:** This stage requires code execution. The automated version uses Python (openpyxl or pandas) to read the spreadsheet, identify parameter cells, perturb them, and trace through formulas to the result. The manual version provides the human with specific cells to change and instructions for reading the result.

**Design rationale:** This is the single biggest improvement over GiveWell's current approach. Their AI output is filled with ungrounded claims like "could reduce cost-effectiveness by 15–25%." The Quantifier replaces these with actual calculations. A critique that sounds devastating but only moves the needle by 0.3% can be deprioritized; a critique that sounds minor but affects a high-sensitivity parameter gets escalated.

---

### Stage 5: Adversarial Pair (Advocate + Challenger)

**Purpose:** Stress-test each quantified critique through structured debate. The Advocate defends GiveWell's current position; the Challenger argues for the critique.

**Inputs:**
- Quantified critiques (from Quantifier)
- GiveWell's intervention report (for the Advocate to draw on)
- Verification evidence (for the Challenger to draw on)

**Process:**
1. **Challenger** presents the critique with evidence and quantified impact.
2. **Advocate** responds: defends GiveWell's current approach, identifies weaknesses in the critique, suggests why it may not matter.
3. **Challenger** rebuts: addresses the Advocate's defenses, identifies what the Advocate couldn't answer.
4. **Judgment:** A summary of which points survived the exchange and which didn't.

**Outputs:**
For each critique:
- Surviving strength: Strong / Moderate / Weak (post-debate)
- Key unresolved questions
- Strongest argument for the critique
- Strongest defense against it
- Recommended action: Investigate further / Monitor / Dismiss

**Design rationale:** GiveWell noted that "the process works best as a dialogue." The Adversarial Pair formalizes this. It prevents the pipeline from surfacing critiques that sound compelling in isolation but collapse under pushback. It also prevents the opposite failure: dismissing valid critiques because of superficial defenses.

---

### Stage 6: Synthesizer

**Purpose:** Produce the final ranked output, comparable in format to GiveWell's current AI red teaming output but with verification status, parameter linkage, sensitivity ranges, and debate summaries.

**Inputs:**
- All surviving critiques with full metadata from all previous stages

**Outputs:**
A structured report containing:
1. **Executive summary:** Top 3–5 critiques by impact, one paragraph each
2. **Ranked critique list:** Each critique includes:
   - Hypothesis (from Investigator)
   - Verification status and evidence summary (from Verifier)
   - Parameters affected and sensitivity result (from Quantifier)
   - Debate outcome and surviving strength (from Adversarial Pair)
   - Recommended action and confidence level
3. **Comparison with baseline:** Side-by-side scoring against GiveWell's published AI output on signal rate, hallucination rate, novel findings, and quantitative specificity
4. **Methodological notes:** What the pipeline found that a single-pass approach would likely miss, and what it might miss that a human investigator would catch

---

## Context Architecture

Each agent operates on a scoped context document. These documents control information flow and prevent the "lost context" failure mode.

### CONTEXT.md Structure (per investigation thread)

```markdown
# Investigation Thread: [Thread Name]

## Scope
What this thread investigates. What questions to answer.

## Out of Scope
What this thread does NOT investigate (handled by other threads).

## CEA Parameters in Play
Which parameters in GiveWell's model could be affected by findings in this thread.
Current values and where they come from.

## What GiveWell Already Accounts For
Adjustments and considerations already in the report or CEA.
DO NOT re-raise these as critiques.

## Key Source Materials
Which documents/papers are relevant to this thread.

## Definition of "Material Critique"
A critique is material if it could change the bottom-line cost-effectiveness
estimate by more than 10%, OR if it identifies a structural assumption
that lacks empirical grounding.
```

### Information Flow Rules

1. **Only the Decomposer sees the full intervention report and CEA.** Investigators see their scoped CONTEXT.md plus relevant excerpts.
2. **Investigators never see other Investigators' output.** This prevents anchoring and ensures independent hypothesis generation.
3. **The Verifier sees one critique at a time.** This prevents the Verifier from batch-confirming based on pattern rather than evidence.
4. **The Quantifier sees all verified critiques together** (to identify interactions between parameters).
5. **The Adversarial Pair sees one critique at a time** with its full evidence and quantification package.
6. **The Synthesizer sees everything** and produces the final ranking.

---

## Evaluation Protocol

For each intervention, we score our pipeline output against GiveWell's published AI output:

| Metric | How Measured |
|---|---|
| Signal rate | % of final critiques rated "worth investigating" by a domain expert (or by us, applying GiveWell's own standards) |
| Hallucination rate | Count of fabricated citations or factual claims in final output |
| Novel findings | Count of critiques not present in GiveWell's report, CEA, or published AI output |
| Quantitative specificity | % of critiques with parameter-linked sensitivity ranges vs. ungrounded estimates |
| Human review time | Time for a reviewer to process our output vs. GiveWell's format |

---

## Implementation Notes

### Manual Version (Claude Project)

A human runs each prompt sequentially in a Claude Project:

1. Paste Decomposer prompt + intervention report → receive threads + exclusion list
2. For each thread: paste Investigator prompt + CONTEXT.md → receive candidate critiques
3. Paste all candidates into Verifier prompt → receive verified/flagged critiques
4. Hand verified critiques + CEA parameter info to human for manual spreadsheet checks (or use Claude's code execution)
5. Paste quantified critiques into Adversarial prompts → receive debate output
6. Paste everything into Synthesizer → receive final report

Total: ~7 prompt executions per intervention (1 Decomposer + ~5 Investigators + 1 Verifier + Quantifier is manual/code + 1 Adversarial round + 1 Synthesizer).

### Automated Version (run_pipeline.py)

Python script that:
1. Calls the Anthropic API for each stage
2. Parses structured output (JSON/XML) between stages
3. Executes Quantifier code against local .xlsx files
4. Produces a final report in markdown
5. Generates the comparison scorecard

This is where Claude Code comes in. The spec for `run_pipeline.py` will be handed off separately.
