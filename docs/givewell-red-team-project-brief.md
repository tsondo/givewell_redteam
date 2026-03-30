# Project: GiveWell AI Red Teaming — Methodology Upgrade

## Origin

GiveWell published a detailed report (January 2026) on their experiment using AI to red team their charitable intervention research. They used ChatGPT 5 Pro with structured prompts across six intervention areas. Their results: ~15-30% of AI critiques were useful, with persistent hallucination, lost context, and unreliable quantitative estimates. They acknowledge multi-agent workflows and better tooling as future possibilities but haven't pursued them.

Source: https://www.givewell.org/how-we-work/our-criteria/cost-effectiveness/ai-red-teaming-12-25

## Thesis

GiveWell's limitations aren't model limitations — they're architecture limitations. Decomposition, verification pipelines, adversarial agent structure, scoped context documents, and tool-augmented quantitative reasoning would each independently improve results, and they compound. We demonstrate this with a proof-of-concept that uses only GiveWell's own public materials.

## Deliverables

### 1. Analysis + Architecture Write-up
- Critique of GiveWell's current approach (prompt-based, single-pass, monolithic context)
- Proposed multi-agent pipeline architecture with spec
- Dual framing: portfolio piece for tsondo.com AND outreach piece for GiveWell

### 2. Proof-of-Concept Runs
- **Phase 1:** Water chlorination (primary test case — hallucinated citations in their output, quantitative gaps, good public data)
- **Phase 2:** ITNs / bed nets (most thoroughly researched by GiveWell — strongest baseline to beat)
- **Phase 3:** SMC / seasonal malaria chemoprevention (they ran 3 AI variations — most comparison data)
- Each phase: run our pipeline, compare results side-by-side with their published AI output

### 3. Implementation Artifacts
- **Accessible version:** Claude Project with sequential manual prompts GiveWell could adopt directly
- **Automated version:** Scripted API pipeline (Python) for reproducibility and scale

## Proposed Agent Pipeline (draft — to be refined against actual source materials)

```
1. DECOMPOSER
   Input: Intervention report + cost-effectiveness model
   Output: Investigation threads with scoped specs
   (e.g., "external validity of trial evidence," "causal model assumptions,"
   "parameter sensitivity," "implementation fidelity," "literature gaps")

2. INVESTIGATORS (one per thread)
   Input: Scoped spec + relevant subset of source materials + search tools
   Output: Candidate critiques with cited evidence
   Each has: focused context doc, explicit definition of "material critique,"
   quantitative threshold for "bottom-line relevant"

3. VERIFIER
   Input: Each candidate critique
   Output: Verified critique (citations checked, claims grounded) or rejection
   Separates hypothesis generation from evidence retrieval

4. QUANTIFIER
   Input: Verified critiques + cost-effectiveness spreadsheet
   Output: Sensitivity analysis — which parameters matter, estimated impact magnitude
   Uses code execution to programmatically interrogate the CEA model

5. ADVERSARIAL PAIR (Advocate + Challenger)
   Input: Verified, quantified critiques
   Output: Stress-tested critiques that survive defense of GiveWell's current position

6. SYNTHESIZER
   Input: Surviving critiques
   Output: Ranked final critique set with evidence, quantified impact, confidence levels
```

## Key Design Principles

- **Only public materials as inputs.** Proves improvement comes from methodology, not privileged access.
- **Scoped context per agent.** No agent gets the whole filing cabinet. Each gets a CONTEXT.md defining what's in scope, what data sources GiveWell actually uses, what adjustments are already made.
- **Verification is first-class.** Every factual claim and citation is independently checked before reaching a human.
- **Quantitative grounding.** No "could reduce cost-effectiveness by 15-25%" without showing the math. Code execution against actual spreadsheet models.
- **Comparative evaluation.** Every output is measured against GiveWell's published baseline: signal rate, hallucination rate, novel findings, quantitative specificity.

## Source Materials to Collect

### Water Chlorination (Phase 1)
- [ ] GiveWell intervention report: https://www.givewell.org/international/technical/programs/water-quality-interventions
- [ ] GiveWell AI output doc: https://docs.google.com/document/d/1l8baZ_9zQ3FDmmEI50L0T2KqzoEhow6lNXjgLKUhGUg/
- [ ] Cost-effectiveness model (find in GiveWell CEA framework)
- [ ] Key cited papers: Si et al. 2022, LeChevallier et al. 1981, Crider et al. 2018, EPA disinfection manual, WHO water quality guidelines

### ITNs (Phase 2)
- [ ] GiveWell intervention report: https://www.givewell.org/international/technical/programs/insecticide-treated-nets
- [ ] GiveWell AI output doc: https://docs.google.com/document/d/16iIzH_KneLjlRSAc-2ZLO4aWdNB48CZ0LWH7sRe8yFo/
- [ ] CEA spreadsheet: https://docs.google.com/spreadsheets/d/1VEtie59TgRvZSEVjfG7qcKBKcQyJn8zO91Lau9YNqXc/
- [ ] Key papers: Pryce et al. 2018, Skovmand et al. 2021, WHO prequalification 2023

### SMC (Phase 3)
- [ ] GiveWell intervention report: https://www.givewell.org/international/technical/programs/seasonal-malaria-chemoprevention
- [ ] GiveWell AI output doc: https://docs.google.com/document/d/1562HtXfGOQ3EYOWgDnCAV_s6uF2zbPmRAqZ817_lNpA/
- [ ] CEA spreadsheet: https://docs.google.com/spreadsheets/d/1qazIM1BVb3Iyyz4Yjt9k39gu1ylQactDT95laEhoTdM/
- [ ] Key papers: Diawara et al. 2025

## Evaluation Criteria (how we measure success)

For each phase, compare our pipeline output against GiveWell's published AI output on:

| Metric | GiveWell Baseline | Our Target |
|--------|-------------------|------------|
| Signal rate (% of critiques worth investigating) | ~15-30% | >60% |
| Hallucination rate (fabricated citations/claims) | Multiple per run | Zero (verification layer) |
| Novel findings (not in source materials) | 1-2 per intervention | ≥3 per intervention |
| Quantitative specificity | Ungrounded estimates | Parameter-linked sensitivity ranges |
| Time investment (human) | ~75 min | Comparable or less |

## Competencies Demonstrated (portfolio framing)

- **Evaluation design:** Defining metrics, building comparative baselines
- **Task decomposition:** Breaking monolithic prompts into scoped agent specs
- **Context architecture:** Designing per-agent context documents, managing information flow
- **Multi-agent orchestration:** Pipeline design with verification, adversarial, and synthesis stages
- **Tool augmentation:** Code execution against real spreadsheet models
- **Prompt engineering:** Structured specs with explicit criteria vs. open-ended prompting

## Repository Structure (proposed)

```
givewell-red-team/
├── README.md                     # This brief, expanded
├── docs/
│   ├── architecture.md           # Pipeline design document
│   ├── analysis-givewell.md      # Critique of their current approach
│   └── writeup-tsondo.md         # Blog post draft for tsondo.com
├── source-materials/
│   ├── water-chlorination/
│   ├── itns/
│   └── smc/
├── prompts/
│   ├── decomposer.md
│   ├── investigator-template.md
│   ├── verifier.md
│   ├── quantifier.md
│   ├── adversarial-advocate.md
│   ├── adversarial-challenger.md
│   └── synthesizer.md
├── pipeline/
│   ├── run_pipeline.py           # Automated API version
│   └── manual-workflow.md        # Claude Project sequential version
├── results/
│   ├── water-chlorination/
│   ├── itns/
│   └── smc/
└── evaluation/
    └── comparison-template.md    # Side-by-side scoring framework
```
