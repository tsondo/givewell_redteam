# Conclusions

## What the Pipeline Proved

Four GiveWell cost-effectiveness analyses — water chlorination, insecticide-treated nets (ITNs), seasonal malaria chemoprevention (SMC), and vitamin A supplementation (VAS) — were run through a multi-agent pipeline that decomposes, investigates, verifies, quantifies, stress-tests, audits, and synthesizes critiques. Every run produced novel critiques absent from GiveWell's own AI red teaming output, where such output was available for comparison.

### Signal Rates

| Intervention | Generated | Verified | Survived Adversarial | Signal Rate |
|---|---|---|---|---|
| Water chlorination | 31 | 30 | 26 | 84% |
| ITNs | 30 | 30 | 30 | 100% |
| SMC | 34 | 29 | 28 | 82% |
| VAS | 32 | 28 | 28 | 87.5% |

These signal rates are compared against GiveWell's publicly documented AI red teaming output, which reported a useful-critique rate of ~15–30%. GiveWell has since moved past that approach and built their own agentic pipeline, with reported improvements; however, their newer pipeline's output is not publicly published, so direct comparison against their current state is not possible. The comparison in this project is against the published baseline — not against GiveWell's current capability, which has almost certainly advanced beyond what they first published. The pipeline exceeded the pre-set 60% target against the published baseline across all four interventions.

Zero hallucinated citations across all runs. The architectural separation of hypothesis generation (Investigators) from evidence retrieval (Verifier) eliminated the fabrication problem entirely. This is the single clearest architectural lesson from the project: decomposing one agent's job into two agents with distinct roles prevents an entire category of failure.

### Quantitative Grounding

Each surviving critique includes parameter mappings to specific CEA spreadsheet cells and sensitivity ranges derived from code execution against actual models, wherever the underlying model structure supports such mapping (water chlorination, ITN, SMC). GiveWell's published AI output contained ungrounded estimates like "cost-effectiveness could more than halve" with no derivation. The pipeline ties every impact claim to a computed perturbation or explicit derivation chain from verified evidence.

VAS is a partial exception. The VAS CEA exposes aggregate cost-effectiveness multiples per country rather than the parameter formula chain the earlier interventions used, so Quantifier sensitivity analysis for VAS operated on abstracted inputs rather than direct spreadsheet perturbation. The critique evidence remains grounded; the parameter-level quantification is weaker.

### Novel Findings

Across the three interventions where GiveWell published comparable AI output, the pipeline's top critiques have minimal overlap with GiveWell's published comparison set. Water chlorination produced 10 novel critiques, including non-linear baseline mortality relationships and chlorine-resistant pathogen burden. ITNs surfaced 9 novel critiques including mosquito species composition misalignment and housing quality effects on net effectiveness. SMC identified 6 novel critiques including drug resistance mutation acceleration and climate-driven transmission season shifts.

The comparison set here is GiveWell's initial publicly documented AI output, not their current internal pipeline's output. GiveWell's agentic pipeline may have independently surfaced overlapping critiques; the comparison in this project simply cannot speak to that.

VAS did not have a comparable GiveWell AI output in the published baseline. The 28 surviving VAS critiques stand as pipeline output without a direct comparison, though they align directionally with revisions GiveWell has been making to its own VAS estimates over 2025–2026.

### Cost and Optimization

| Intervention | Total Cost | Notes |
|---|---|---|
| Water chlorination (v1) | ~$30 | One-at-a-time verification; blew past $15 target |
| Water chlorination (v2) | $2.36 | Resumed from adversarial stage only |
| ITNs | $16.00 | Batched verification (3 critiques/batch) |
| SMC | $15.96 | Batched verification |
| VAS (pre-judge) | $20.14 | Includes wasted $10.14 on a crashed run |
| VAS (post-judge re-run) | $6.36 | Adversarial + new judge + linker + synthesizer |

Total spend across all four interventions and their re-runs: approximately $90. The Verifier was the dominant cost driver in the early water chlorination run at ~70% of total budget. Batching critiques by investigation thread cut Verifier costs by roughly 70% in subsequent runs, bringing per-intervention cost below the $16 target. The VAS re-run, which added a judge agent call per critique, stayed well under budget because Opus judge calls averaged $0.13 rather than the $0.30–0.50 projected.

---

## The Adversarial Stage Rebuild

The original pipeline architecture had the Challenger — the agent whose prompted role was to argue for the critique — also assign the surviving strength verdict. This produced suspiciously high survival rates (100% ITN, 97% SMC, 87.5% pre-judge VAS) that reflected a structural conflict of interest rather than calibrated debate outcomes. The party arguing for the critique was also deciding whether the critique survived.

A domain expert reviewer (Denis Wallez) surfaced this indirectly through a move-level review of adversarial transcripts. He identified six recurring failure modes in the debates: unsupported numerical estimates traded without sourcing, whataboutism (deflecting to the opponent's separate weaknesses), calls to ignorance (asserting X might be true because we don't know it isn't), strawmanning (rebutting claims the opponent didn't make), equivocal conclusions delivered in confident language, and generic "investigate further" recommendations without specifying what would settle the question.

The pipeline was rebuilt in two stages:

**Judge agent.** A neutral Opus-based judge now reads both sides' outputs after the debate and produces a structured audit naming detected failure modes, verdict justification citing specific debate moves, and recommended actions with feasibility tagged. The Challenger no longer assigns verdicts. The judge's failure mode taxonomy extends Mikyo's original six to nine categories (splitting "unsupported estimate" into fabricated, pseudo-derivation, and counter-estimate subtypes; adding "misrepresenting evidence status" to distinguish unverified from disproven claims). A positive marker, `sound_synthesis_noted`, tracks grounded syntheses that survive scrutiny.

**Linker stage.** A separate Sonnet-based stage identifies dependency relationships between surviving critiques and rejected critiques (unverifiable or contradicted). Where a surviving finding's argument depends on an unverified claim, the synthesizer now tags the finding as CONDITIONAL and propagates the dependency explicitly. This addresses a deeper epistemological point from the same review: unverified claims should propagate as tagged conditional assumptions, not be discarded — "unverified" is not equivalent to "false."

**VAS re-run results.** Applying the rebuilt architecture to VAS produced a meaningfully different verdict distribution: 0 strong / 27 moderate / 1 weak, with 156 failure modes detected across the 28 debates and zero sound syntheses noted. The prior pre-judge VAS distribution showed 17 strong / 11 moderate with no failure mode tracking. The new distribution reflects honest calibration — debates full of unsupported estimates and strawmanning now resolve to "moderate" rather than "strong." An independent LLM review (Grok in Expert mode) read both the pre-judge and post-judge versions and substantively validated the shift as an improvement in rigor and intellectual honesty, though LLM-evaluating-LLM is not a substitute for domain expert validation.

The rebuild took roughly two weeks of work across three plans (judge agent and debater prompt updates, linker stage and synthesizer rewrite, VAS re-run and verification). The architectural lesson: the original adversarial design had a real structural bias, and fixing it required separating role from judgment.

---

## Honest Limitations

### The Quantifier's Mapping Problem

The Quantifier stage asks a model to map conceptual critiques to specific spreadsheet parameters, then compute sensitivity ranges. In practice, only 2–3 critiques per run mapped cleanly to single-parameter perturbations. Most critiques target multi-parameter concepts (e.g., "temporal dynamics of adherence decay") that can't be expressed as changing one cell value. The Quantifier produces materiality assessments for all critiques, but many rely on constructed proxy calculations rather than direct CEA perturbation.

This remains the pipeline's weakest stage. A future version would need either a more sophisticated spreadsheet interaction layer (multi-parameter scenario modeling) or a human-in-the-loop step where an analyst translates conceptual critiques into concrete parameter changes.

### The Moderate-Verdict-Bucket Collapse

The post-judge VAS run produced 96% of critiques at "moderate" surviving strength (27 of 28, plus one weak, zero strong). The distribution is likely correct — debates with substantive failure modes on both sides appropriately resolve to moderate rather than strong — but the three-bucket granularity (strong / moderate / weak) may be too coarse to capture meaningful differentiation when most debates have similar failure profiles. A future version might weight surviving strength by failure-mode count or introduce a finer granularity for findings at the failure-heavy end of the distribution.

### Finding-Title Matching Fragility

The linker stage identifies dependencies by matching surviving-critique titles and rejected-critique titles as exact strings. The synthesizer then propagates CONDITIONAL tags by matching the same titles. String matching is brittle — any paraphrase or whitespace difference silently breaks the link. The synthesizer prompt explicitly instructs verbatim title use, and the current VAS run's three dependencies all matched correctly, but the architecture is one prompt-drift away from silent failure. A future version should use explicit IDs rather than title strings for cross-stage reference.

### GiveWell's Spreadsheets Aren't Built for Programmatic Access

All four CEA files use inconsistent layouts, merged cells, and `DUMMYFUNCTION` placeholders for Google Sheets functions that don't translate to `.xlsx`. The spreadsheet reader required per-intervention subclasses (`WaterCEA`, `ITNCEA`, `MalariaCEA`, `VASCEA`) with manual parameter mapping. This isn't a pipeline limitation per se, but it means the Quantifier's sensitivity analysis operates on extracted parameter snapshots rather than live formula chains, reducing its ability to capture parameter interactions.

### The UNVERIFIABLE Category Is Still Coarse

The verifier produces three verdicts: verified, unverifiable, rejected. The unverifiable category bundles at least four epistemically distinct states: evidence searched and not found, claims that are interpolations from grounded components without direct attestation, claims unfalsifiable in principle, and claims where relevant literature exists but isn't accessible to the verifier's search. Each has different epistemic weight. The current pipeline doesn't distinguish these, and the adversarial stage's debaters occasionally conflate "unverified" with "false" — a failure mode the judge now catches (`misrepresenting_evidence_status`) but doesn't prevent upstream. Splitting the unverifiable category is future work.

---

## Cross-Intervention Patterns

Three patterns emerged independently across all four interventions, suggesting they reflect structural features of GiveWell's modeling approach rather than intervention-specific gaps.

### 1. Temporal Dynamics Not Incorporated

All four CEAs model key parameters as static constants when evidence suggests they change over time. Water chlorination: adherence decay beyond RCT durations (1–2 years vs. 5+ year program horizons). ITNs: insecticide efficacy decay and net physical degradation. SMC: drug resistance mutation accumulation across treatment cycles. VAS: VAD prevalence changes driven by fortification programs, urbanization, and shifting disease burden since the 1990s baseline surveys that populate the CEA. In every case, the model's assumption of time-invariant parameters produces systematic overestimation of multi-year benefits.

### 2. Within-Category Heterogeneity Underestimated

Each model uses aggregate categories that mask meaningful variation. Water chlorination: "under-5 mortality" treats a group with dramatically different vulnerability profiles as uniform. ITNs: "insecticide resistance" conflates chemical resistance with behavioral resistance — fundamentally different mechanisms collapsed into a single adjustment factor. SMC: "adherence" averages across socioeconomic strata with different access patterns. VAS: "external validity" uses broad nutritional proxies (stunting, wasting, poverty) as multiplicative adjustments on mortality effect size, scaling a linear baseline rather than modeling threshold or cause-specific relationships. In each case, the aggregation obscures the specific mechanism the intervention targets.

### 3. Biological and Contextual Adaptation Not Captured

Three of the four CEAs share a structural blind spot around target-system adaptation. ITNs: mosquito species composition shifts toward outdoor-biting species following net distribution — documented, unmodeled. SMC: dhfr/dhps resistance mutations rose from 18.6% to 58.3% in Burkina Faso post-SMC adoption, with no resistance adjustment factor despite the CEA modeling efficacy decay for other interventions. VAS: micronutrient fortification programs, measles vaccination coverage increases, and improved case management have changed the disease environment VAS operates in, yet the CEA extrapolates from 1990s trials using proxy adjustments that treat the current environment as a scaled version of the original rather than a structurally different one. Water chlorination shows a milder version: chlorine-resistant pathogen burden changes with chlorination uptake.

---

## What This Means

The core thesis — that architectural choices (decomposition, scoped context, verification, quantification, adversarial testing, judge audit, dependency linking) drive output quality as much as model capability — held across all four interventions. Each stage independently improved output quality, and they compounded. The pipeline used only public materials and commodity models (Claude Sonnet for most stages, Opus for decomposition, judge, synthesis), suggesting the improvement comes from methodology, not privileged access or frontier capabilities.

The pipeline is not production-ready. The Quantifier needs a more sophisticated spreadsheet interaction model. The verdict bucket granularity could be refined. Cross-stage references should move from string matching to explicit IDs. The verifier's UNVERIFIABLE category should be split. Cost management needs tighter controls for runs approaching the materiality threshold count.

But as a proof of concept, it demonstrates that the gap between the published baseline (15–30% of AI critiques useful) and "80%+ useful, zero hallucinated citations, honest failure-mode tracking" is bridgeable with known techniques, at a cost under $20 per intervention. This is a comparison against the published baseline, not GiveWell's current agentic pipeline; GiveWell has independently moved past their initial approach and their current capability is not publicly benchmarked. What this project contributes is not a claim of superiority over GiveWell's current work, but a public demonstration that specific architectural moves — separating hypothesis from evidence, separating argument from judgment, propagating unverified claims as conditional rather than discarding them — reliably improve AI-assisted critique in the cost-effectiveness analysis domain. These moves are portable beyond this domain. Any context where AI-assisted critique would benefit from structural rigor can adopt them.

The single most valuable input to the project was domain expert review that operated at the move level rather than the narrative level. An AI pipeline can be internally consistent, produce fluent output, and pass its own self-evaluation while still containing specific reasoning failures that only a human reader catches. The architectural improvements in this project — the judge agent, the failure mode taxonomy, the conditional-reasoning treatment of unverified claims — are all downstream of review that saw what the pipeline couldn't see about itself. Interpretability isn't cosmetic. It's what makes the work correctable, and therefore trustworthy.
