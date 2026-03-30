# Critique of GiveWell's AI Red Teaming Approach

*Analysis prepared for the GiveWell AI Red Teaming Methodology Upgrade project*

---

## Executive Summary

In January 2026, GiveWell published a detailed account of their experiment using AI to red team charitable intervention research across six grantmaking areas. Their approach produced moderately useful results — roughly 15–30% of AI-generated critiques were deemed worth investigating — at low human time cost (~75 minutes per intervention).

This analysis argues that GiveWell's observed limitations are not primarily model limitations. They are **architecture limitations**. The specific failure modes GiveWell reports — hallucinated citations, lost context, unreliable quantitative estimates, and high noise-to-signal ratio — are predictable consequences of their single-pass, monolithic-context, prompt-only approach. Each failure mode maps to a known architectural solution that GiveWell acknowledges but has not yet pursued.

This matters because GiveWell directs hundreds of millions of dollars annually based on cost-effectiveness analyses that contain uncertain parameters and structural assumptions. Better AI red teaming doesn't just produce more critiques — it produces *more reliable* critiques with *verifiable* evidence and *quantified* impact on bottom-line cost-effectiveness estimates.

---

## 1. What GiveWell Did

GiveWell's pipeline had three steps:

1. **Background compilation.** ChatGPT 5 Pro's Deep Research feature produced a 15–20 page literature summary per intervention.
2. **Red teaming prompt.** A structured prompt instructed the model to generate 20–30 critiques, verify novelty, assess impact, and select the top 15. The prompt specified critique categories (evidence quality, methodology, external validity, etc.) and required novelty rationale and confidence levels.
3. **Human review.** Grantmaking teams spent ~60 minutes reviewing AI output and identifying critiques worth investigating.

They tested across Claude Opus 4.1, Gemini 2.5 Pro, and ChatGPT 5 Pro, settling on ChatGPT 5 Pro as producing the most consistently useful output. They applied this to six interventions: water chlorination, CMAM, syphilis screening, malaria vaccines, SMC, and ITNs.

### What They Got Right

GiveWell's approach reflects genuine thought about prompt design. Several features are well-conceived:

- **Explicit novelty checking.** The prompt instructs the model to verify each critique isn't already in the source materials before including it.
- **Structured categories.** Requiring critiques across evidence quality, methodology, implementation, external validity, and overlooked factors forces breadth.
- **Calibrated expectations.** GiveWell correctly frames AI output as brainstorming input, not finished analysis, requiring human review.
- **Comparative testing.** They tested multiple models rather than assuming one would dominate.

The 75-minute total time investment is genuinely low, making even a 15% signal rate potentially worthwhile on a cost basis.

---

## 2. Diagnosing the Failure Modes

GiveWell identified five recurring problems. Each maps to a structural cause in their architecture.

### 2.1 Hallucinated Citations and Claims

**GiveWell's observation:** The AI frequently fabricated specific details even when raising valid concerns. Examples include nonexistent "Kenya and Malawi focus groups from 2024" cited in the water chlorination output and fabricated WHO procurement alerts for benzathine-penicillin G in the syphilis output.

**Structural cause:** GiveWell's pipeline asks a single model to *simultaneously* generate hypotheses and provide supporting evidence. This conflates two cognitively distinct tasks. Language models are strong hypothesis generators — they can identify plausible concerns by pattern-matching across training data. But when forced to also produce citations in the same pass, they confabulate evidence that *would* support the hypothesis if it existed. This is a well-documented failure mode of autoregressive generation under pressure to produce specific factual details.

**Architectural solution:** Separate hypothesis generation from evidence retrieval. An investigator agent generates candidate critiques *without* being asked to cite evidence. A separate verifier agent then attempts to ground each critique in real sources using retrieval tools. Critiques that survive verification proceed; those that don't are flagged as ungrounded hypotheses rather than presented as supported claims.

Examining the water chlorination AI output confirms this pattern clearly. The "strategic crowd-out of piped-water investment" critique is a legitimate concern — GiveWell themselves acknowledge this — but the AI fabricated specific focus group evidence to support it. A verification layer would have flagged the citation as unverifiable while preserving the underlying hypothesis for human investigation.

### 2.2 Lost Context and Misunderstanding of GiveWell's Methods

**GiveWell's observation:** The AI frequently raised concerns about data or methods GiveWell doesn't actually use, critiquing data sources not in their models or misunderstanding their adjustment methodology.

**Structural cause:** GiveWell fed the model their intervention report, internal research materials, and the Deep Research literature summary simultaneously. In a monolithic context window, the model cannot reliably distinguish between: (a) what GiveWell's model *actually does*, (b) what the academic literature *generally discusses*, and (c) what the Deep Research output *speculates about*. The result is critiques aimed at a phantom version of GiveWell's analysis that blends all three.

The water chlorination output illustrates this. Critique #3 ("Behavioral Hawthorne bias in dispenser trials") states "GiveWell adjusts for bundled hardware but not for 'bundled behavior.'" This may or may not be true — but the critique's framing reveals the model isn't clearly distinguishing what adjustments GiveWell's CEA *actually makes* from what the literature *generally discusses*.

**Architectural solution:** Scoped context documents per agent. Instead of giving a single model everything, create a CONTEXT.md for each investigation thread that specifies: what data sources GiveWell's model uses, what adjustments are already made, what parameters drive cost-effectiveness, and what the model *doesn't* account for. An investigator focused on "external validity of trial evidence" gets the relevant trial descriptions and GiveWell's external validity adjustments — not the entire filing cabinet.

### 2.3 Low Signal Rate (~15–30% Useful)

**GiveWell's observation:** Most critiques (~85% initially, improving to ~70% by December 2025) were unlikely to affect bottom-line cost-effectiveness, represented misunderstandings, or were issues already addressed.

**Structural cause:** A single model producing 15 critiques in one pass has no mechanism for filtering by *materiality*. It cannot distinguish between a critique that might shift cost-effectiveness by 50% and one that might shift it by 0.5%. The prompt instructs it to assess "potential impact on cost-effectiveness," but without access to the actual spreadsheet model, this assessment is purely speculative.

The water chlorination output exemplifies this. It lists 20 critiques with impact estimates like "5–10% reduction in effect size" or "Could cut projected mortality benefit by 10–20%." These numbers are ungrounded — the model has no way to trace a parameter change through GiveWell's multi-sheet CEA to a bottom-line result. Some critiques with modest-sounding estimates might actually be devastating; others with alarming-sounding estimates might be irrelevant because the parameter in question has low sensitivity.

**Architectural solution:** A quantifier agent with code execution access to the actual CEA spreadsheet. Before a critique reaches a human, the pipeline should answer: "If this critique is valid, which parameters in the CEA change, and by how much does the bottom-line cost-effectiveness estimate move?" This transforms vague "could reduce effectiveness by 15–25%" claims into concrete sensitivity analyses.

### 2.4 Unreliable Quantitative Estimates

**GiveWell's observation:** The AI often suggested specific impact magnitudes ("could reduce cost-effectiveness by 15–25%") without solid basis, partly because it couldn't work with their complex multi-sheet spreadsheets.

**Structural cause:** This is the same issue as 2.3, stated from the quantitative side. The model is asked to estimate impact magnitude but has no computational access to the model where magnitude is determined. It's doing arithmetic by analogy rather than by calculation.

**Architectural solution:** Same as 2.3 — code execution against the actual CEA. GiveWell's spreadsheets are public Google Sheets. A quantifier agent can programmatically read parameter values, perturb them based on a critique's implications, and report the resulting change in cost per DALY or cost per life saved.

### 2.5 Repetition of Known Concerns

**GiveWell's observation:** Many AI critiques flagged issues already explicitly discussed in their research. The novelty-checking instruction in the prompt was insufficient.

**Structural cause:** Novelty checking within a single prompt is unreliable because the model's "memory" of what's in the source documents degrades as the context window fills and as attention is split between generating and checking. The instruction "Is this already in the report?" requires the model to simultaneously hold the full report in working memory while generating new content — exactly the scenario where attention-based architectures lose fidelity.

**Architectural solution:** An explicit decomposition step where a first agent reads the source materials and produces: (a) a list of concerns GiveWell already addresses, (b) a list of adjustments already in the CEA, and (c) a list of acknowledged limitations. Downstream investigator agents receive this "already known" list as part of their scoped context and are instructed to not duplicate it. This turns an unreliable in-context novelty check into a structured exclusion list.

---

## 3. The Compound Problem

GiveWell's five failure modes don't just coexist — they compound. A hallucinated citation supporting a non-novel critique with an ungrounded quantitative estimate about a method GiveWell doesn't use represents a quadruple failure. Yet in a single-pass architecture, each critique has roughly independent probability of exhibiting each failure mode.

If we estimate (conservatively) a 30% chance of hallucination, 40% chance of context confusion, 70% chance of immateriality, and 30% chance of non-novelty, the probability that a given critique is *fully clean* across all dimensions is roughly 0.7 × 0.6 × 0.3 × 0.7 ≈ **9%**. This is consistent with GiveWell's observed ~15% useful rate (accounting for some critiques being partially useful).

A pipeline architecture attacks each failure mode independently:

| Failure Mode | Single-Pass Fix | Pipeline Fix |
|---|---|---|
| Hallucinated citations | Prompt instruction (unreliable) | Verification agent with retrieval tools |
| Lost context | More source materials (makes it worse) | Scoped context docs per agent |
| Low signal rate | "Focus on impact" instruction | Quantifier with CEA code execution |
| Ungrounded estimates | "Be specific" instruction | Programmatic sensitivity analysis |
| Non-novelty | "Check the report" instruction | Structured exclusion list from decomposer |

Because each fix operates on a different failure mode, the improvements compound. If verification eliminates 90% of hallucinations, scoped context eliminates 60% of confusion, and quantification eliminates 80% of immaterial critiques, the combined signal rate jumps dramatically — even before adversarial stress-testing.

---

## 4. What GiveWell Acknowledges but Hasn't Pursued

GiveWell's "Next Steps" section explicitly mentions three improvements they considered but deprioritized:

1. **Making research more AI-accessible.** They note that AI output quality depends on context quality, but say "meaningful improvements likely require AI advances in handling complex spreadsheets and large document volumes."
2. **Multi-agent workflows.** They've "considered using multiple AI agents in sequence" but say their "current approach appears sufficient" and they "don't know whether added complexity would yield proportional benefits."
3. **Specialized research tools.** They haven't identified tools that "would meaningfully improve on our current approach."

These positions are understandable given GiveWell's resource constraints and core competencies, but each one is more tractable than they suggest:

- **AI-accessible research:** This doesn't require waiting for model advances. It requires authoring scoped context documents — summaries of what the CEA does, what parameters matter, what adjustments exist — written for AI consumption. This is a one-time investment per intervention that improves all downstream AI analysis.
- **Multi-agent workflows:** The question isn't whether "added complexity yields proportional benefits." It's whether *decomposition* yields benefits. The answer from the AI engineering literature is unambiguously yes for tasks that combine hypothesis generation, evidence retrieval, quantitative reasoning, and adversarial evaluation. These are qualitatively different cognitive tasks that benefit from separation.
- **Specialized tools:** Code execution against spreadsheets is not a "specialized research tool" — it's a standard capability of current AI systems. GiveWell's CEA spreadsheets are publicly available Google Sheets. Programmatic access is straightforward.

---

## 5. Evidence from Their Own Output

The water chlorination AI output document provides a detailed case study of how these failures manifest in practice.

### Hallucination Examples

- **"Kenya and Malawi focus groups, 2024"** cited as evidence for infrastructure crowd-out. GiveWell confirmed this was fabricated.
- **"A 2023 Uganda port delay paused dispenser refills for eight weeks"** (Critique #9, supply chain fragility). Unverified and likely fabricated — presented with false specificity.
- **"Field audits indicate dispenser taps have a mean-time-to-failure of 26 months vs. modelled 60 months"** (Critique #10). Presented as fact with no source; "field audits" is a classic hallucination pattern.

### Context Confusion Examples

- The Sonnet 4.5 output (included as a secondary run) critiques "Evidence Action's organizational survival" incentives — but this is a critique of a specific implementing organization, not of GiveWell's analytical methodology. The model conflated the research question with the implementation question.
- Multiple critiques reference "GiveWell's models assume..." followed by claims about what the models assume that may or may not be accurate. Without scoped context specifying actual model parameters, the AI is guessing.

### Ungrounded Quantitative Claims

The output is filled with specific-sounding but baseless numbers:

- "Cost-effectiveness could more than halve" (turbidity critique)
- "15% cheaper, equally effective programs" (dose-response critique)
- "Effect size erosion by 5 pp over five years" (pathogen substitution)
- "30% O&M costs up, lowering CE by ~15%" (mechanical failure)

None of these are derived from GiveWell's actual CEA. They're the model's intuitive estimates dressed up in quantitative language.

### What Worked

Despite these problems, the output did surface genuinely useful concerns:

- **Water turbidity and flood-season efficacy** — a legitimate critique GiveWell hadn't considered, connecting seasonal flooding to reduced chlorine effectiveness.
- **Disinfection byproducts** — a real concern about trihalomethane generation in high-organic-matter water sources.
- **Chlorine dosing optimization** — a legitimate question about whether binary (present/absent) modeling of chlorine residual misses the dose-response relationship.

These successes share a pattern: they're *conceptual* insights about mechanisms the CEA doesn't model, rather than evidence-dependent claims. The model excels at "have you thought about X?" and fails at "here's the evidence for X."

---

## 6. Proposed Alternative: Multi-Agent Pipeline

Based on this analysis, we propose the following pipeline architecture. The full specification is in the companion document (`architecture.md`); here we summarize the design rationale.

```
DECOMPOSER → INVESTIGATORS → VERIFIER → QUANTIFIER → ADVERSARIAL PAIR → SYNTHESIZER
```

**Decomposer.** Reads the intervention report and CEA, produces scoped investigation threads (e.g., "external validity of trial evidence," "parameter sensitivity," "implementation fidelity"). Each thread gets a CONTEXT.md specifying what's in scope and what GiveWell already accounts for.

**Investigators** (one per thread). Generate candidate critiques within their scoped domain. They don't cite evidence — they identify *hypotheses worth checking*.

**Verifier.** Takes each candidate critique and attempts to ground it: checks cited papers, searches for supporting evidence, confirms factual claims. Outputs verified critiques or flags unverifiable ones.

**Quantifier.** Takes verified critiques and the CEA spreadsheet. Uses code execution to determine which parameters each critique affects and runs sensitivity analysis to estimate bottom-line impact.

**Adversarial Pair.** An Advocate defends GiveWell's current position; a Challenger argues for the critique. Critiques that survive this exchange are more likely to represent genuine issues rather than superficial concerns.

**Synthesizer.** Ranks surviving critiques by quantified impact, evidence strength, and novelty. Produces a final output comparable to GiveWell's current format but with verification status, parameter linkage, and sensitivity ranges.

---

## 7. Evaluation Framework

To demonstrate improvement, we will run this pipeline against GiveWell's own published AI output for each intervention, measuring:

| Metric | GiveWell Baseline | Target |
|---|---|---|
| Signal rate (% worth investigating) | ~15–30% | >60% |
| Hallucination rate | Multiple per run | Zero (verification layer) |
| Novel findings | 1–2 per intervention | ≥3 per intervention |
| Quantitative specificity | Ungrounded estimates | Parameter-linked sensitivity ranges |
| Human review time | ~60 min | Comparable or less |

The key constraint: we use only GiveWell's own public materials as inputs. Any improvement comes from methodology, not privileged access.

---

## 8. Implications for GiveWell

This analysis is not a criticism of GiveWell's decision to experiment with AI red teaming — it was a well-designed pilot that produced genuinely useful results. The critique is narrower: having identified that AI red teaming is worth doing, GiveWell should invest in doing it well rather than waiting for models to improve.

The specific failure modes they observe are solvable with current tools. The ~15% signal rate is not a ceiling imposed by AI capability; it's a floor set by architectural choices. A multi-agent pipeline with verification, scoped context, and quantitative grounding should substantially improve both the reliability and the specificity of AI-generated critiques — making them more useful inputs to the human review process that GiveWell correctly insists on retaining.
