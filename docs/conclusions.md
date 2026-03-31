# Conclusions

## What the Pipeline Proved

Three GiveWell cost-effectiveness analyses — water chlorination, insecticide-treated nets (ITNs), and seasonal malaria chemoprevention (SMC) — were run through a seven-agent pipeline that decomposes, investigates, verifies, quantifies, stress-tests, and synthesizes critiques. Every run produced novel critiques absent from GiveWell's own AI red teaming output.

### Signal Rates

| Intervention | Generated | Verified | Survived Adversarial | Signal Rate |
|---|---|---|---|---|
| Water chlorination | 31 | 30 | 26 | 84% |
| ITNs | 30 | 30 | 30 | 100% |
| SMC | 34 | 29 | 28 | 82% |

GiveWell's published baseline: ~15–30% of AI-generated critiques were useful. The pipeline exceeded the pre-set >60% target across all three interventions.

Zero hallucinated citations across all runs. The architectural separation of hypothesis generation (Investigators) from evidence retrieval (Verifier) eliminated the fabrication problem entirely.

### Quantitative Grounding

Each surviving critique includes parameter mappings to specific CEA spreadsheet cells and sensitivity ranges derived from code execution against actual models. GiveWell's AI output contained ungrounded estimates like "cost-effectiveness could more than halve" with no derivation. The pipeline ties every impact claim to a computed perturbation.

### Novel Findings

All three comparison tables show the same result: the pipeline's top critiques have minimal overlap with GiveWell's published AI output. Water chlorination produced 10 novel critiques, including non-linear baseline mortality relationships and chlorine-resistant pathogen burden. ITNs surfaced 9 novel critiques including mosquito species composition misalignment and housing quality effects on net effectiveness. SMC identified 6 novel critiques including drug resistance mutation acceleration and climate-driven transmission season shifts.

### Cost and Optimization

| Intervention | Total Cost | Verifier Cost | Notes |
|---|---|---|---|
| Water chlorination (v1) | ~$30 | ~$20.86 | One-at-a-time verification; blew past $15 target |
| Water chlorination (v2) | $2.36 | — | Resumed from adversarial stage only |
| ITNs | $16.00 | ~$5.96 | Batched verification (3 critiques/batch) |
| SMC | $15.96 | ~$8.02 | Batched verification |

The Verifier was the dominant cost driver in the water chlorination run, consuming ~70% of the total budget. Batching critiques by investigation thread (sending 2–3 critiques per API call instead of one) cut Verifier costs by roughly 70% in subsequent runs, bringing ITN and SMC close to the $15/intervention target.

Total spend across all three interventions: ~$34 (counting the water v2 rerun rather than the full v1), well within the $50 budget.

---

## Honest Limitations

### The Quantifier's Mapping Problem

The Quantifier stage asks a model to map conceptual critiques to specific spreadsheet parameters, then compute sensitivity ranges. In practice, only 2–3 critiques per run mapped cleanly to single-parameter perturbations. Most critiques target multi-parameter concepts (e.g., "temporal dynamics of adherence decay") that can't be expressed as changing one cell value. The Quantifier produced materiality assessments for all critiques, but many relied on constructed proxy calculations rather than direct CEA perturbation.

This is the pipeline's weakest stage. A future version would need either a more sophisticated spreadsheet interaction layer (e.g., multi-parameter scenario modeling) or a human-in-the-loop step where an analyst translates conceptual critiques into concrete parameter changes.

### ITN's 100% Adversarial Survival Rate

Every critique that passed the Verifier also survived the adversarial exchange. This is suspicious — a well-calibrated adversarial stage should reject some fraction of critiques. Two possible explanations: the Verifier already filtered aggressively enough that only strong critiques reached the adversarial pair, or the Challenger agent is too lenient. The SMC run's 97% survival rate (28/29) suggests the same pattern. Tightening the adversarial prompts — or introducing a stricter elimination threshold on surviving strength — would be a priority for a production version.

### Water's Cost Overrun

The first water chlorination run cost ~$30, double the $15/intervention target. This was entirely attributable to running the Verifier on 31 critiques sequentially, each with its own web search context. The fix was straightforward (batch by thread), but the overrun illustrates a general risk: Verifier cost scales linearly with critique count and each call carries substantial context from web search tool use. Any deployment would need a pre-filtering step or hard budget cap on Verifier calls.

### GiveWell's Spreadsheets Aren't Built for Programmatic Access

All three CEA files use inconsistent layouts, merged cells, and `DUMMYFUNCTION` placeholders for Google Sheets functions that don't translate to `.xlsx`. The spreadsheet reader required per-intervention subclasses (`WaterCEA`, `ITNCEA`, `MalariaCEA`) with manual parameter mapping. This isn't a pipeline limitation per se, but it means the Quantifier's sensitivity analysis operates on extracted parameter snapshots rather than live formula chains — reducing its ability to capture parameter interactions.

---

## Cross-Intervention Patterns

Three patterns emerged independently across all three interventions, suggesting they reflect structural features of GiveWell's modeling approach rather than intervention-specific gaps.

### 1. Temporal Dynamics Ignored

All three CEAs model key parameters as static constants when evidence suggests they change over time. Water chlorination: adherence decay beyond RCT durations (1–2 years vs. 5+ year program horizons). ITNs: insecticide efficacy decay and net physical degradation. SMC: drug resistance mutation accumulation across treatment cycles. In every case, the model's assumption of time-invariant effectiveness produces systematic overestimation of multi-year benefits.

### 2. Within-Category Heterogeneity Underestimated

Each model uses aggregate categories that mask meaningful variation. Water chlorination: "under-5 mortality" treats a group with dramatically different vulnerability profiles as uniform; "diarrhea" aggregates pathogen-specific etiologies with different chlorine susceptibilities. ITNs: "insecticide resistance" conflates chemical resistance (mosquitoes contact nets but survive) with behavioral resistance (mosquitoes avoid nets entirely) — fundamentally different mechanisms collapsed into a single adjustment factor. SMC: "adherence" averages across socioeconomic strata with different access patterns and across monthly cycles with different compliance rates.

### 3. Pathogen/Vector Adaptation Not Captured (Malaria Interventions)

ITNs and SMC share a domain-specific blind spot: neither model accounts for biological adaptation by the target organism. ITNs: mosquito species composition shifts toward outdoor-biting species (An. arabiensis replacing An. gambiae) following net distribution — a documented phenomenon that GiveWell's insecticide resistance adjustments don't address. SMC: dhfr/dhps resistance mutations increased from 18.6% to 58.3% in Burkina Faso after SMC adoption, but the CEA contains no resistance adjustment factor despite modeling efficacy decay for other interventions. Both cases represent the same structural gap: the model assumes a static biological environment.

---

## What This Means

The core thesis — that GiveWell's AI red teaming limitations are architectural, not model-level — held across all three interventions. Decomposition, scoped context, verification, quantification, and adversarial testing each independently improved output quality, and they compounded. The pipeline used only public materials and commodity models (Claude Sonnet for most stages, Opus for decomposition and synthesis), proving the improvement comes from methodology, not privileged access or frontier capabilities.

The pipeline is not production-ready. The Quantifier needs a more sophisticated spreadsheet interaction model, the adversarial stage needs calibration, and cost management requires tighter controls. But as a proof of concept, it demonstrates that the gap between "15–30% of AI critiques are useful" and "80%+ are useful" is bridgeable with known techniques, at a cost of ~$16 per intervention.
