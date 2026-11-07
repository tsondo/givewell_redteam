--- Thread: Mortality effect of adjunctive atorvastatin (relative_reduction) — ---

CRITIQUE 1: "Success" in Phase III is unlikely to be a mortality result, so the 10% mortality effect is not what a "success" would establish

HYPOTHESIS: The prior evidence is on surrogates (culture conversion, radiographic damage). A mortality-powered Phase III in DS-TB is probably infeasible. If Phase III is designed on a composite "unfavourable outcome" (failure, relapse, death) or on culture conversion, passing it says little about on-treatment death. CG's model multiplies p_success = 0.40 by a 10% mortality effect as if "success" meant "a 10% mortality reduction was demonstrated." A large share of the success probability mass probably carries a mortality effect near zero, or an effect never measured.

MECHANISM: SROI is linear in relative_reduction × p_success. Suppose a fraction f of "success" worlds are surrogate-only successes with a true mortality effect of about r_s. Then E[r | success] = (1−f)(0.10) + f·r_s. With f = 0.5 and r_s = 0.03 (my assumption, not sourced), E[r | success] = 0.065. That is exactly at the threshold that pushes SROI below 2,000x. With f = 0.5 and r_s = 0, it is 0.05, a 50% cut.

Sample-size check (my own arithmetic, standard two-proportion formula, 80% power, α = 0.05 two-sided):
- At 4% baseline on-treatment mortality and a 10% relative reduction (4.0% → 3.6%), about 36,000 per arm, roughly 72,000 total.
- At 8% baseline mortality (an HIV-enriched population) and a 10% reduction, about 17,000 per arm.
- At 2% baseline mortality (typical of trial-selected HIV-negative cohorts, as I recall), the requirement is larger still.
No TB drug trial approaches this scale. A trial powered for a 10% mortality effect is therefore implausible, and any realistic Phase III is powered on something else.

EVIDENCE: The sample-size arithmetic is a logical argument. The 4% and 8% baseline mortality figures are illustrative assumptions; the Verifier should check actual on-treatment mortality in DS-TB programs (WHO Global TB Report cohorts) and in trials. On surrogate validity, I believe Phillips et al. and Wallis et al. found 2-month culture conversion to be a weak individual-level predictor of relapse. I cannot supply exact citations or numbers. I know of no evidence that culture-conversion speed predicts mortality. UNGROUNDED pending verification of the Phase IIc/III registry design.

STRENGTH: HIGH. It affects the primary parameter, rests on arithmetic anyone can check, and the plausible magnitude (0.03–0.05 vs 0.10) crosses the threshold.

NOVELTY CHECK: Not on the exclusion list. "Might not replicate" is already priced into p_success. This critique is different. It argues that even a "success" does not imply a mortality effect, so r and p_success are conceptually mismatched. The materiality note's "success defined on surrogates" case supports exactly this framing.

---

CRITIQUE 2: A large share of on-treatment deaths is unreachable by a weeks-scale host-directed adjunct, and shorter regimens shrink the headroom further

HYPOTHESIS: Deaths during DS-TB treatment are concentrated early and in people with advanced HIV, severe malnutrition, old age, or late presentation. Many die before an adjunct that modifies inflammation and lung damage over weeks could act. Others die from non-TB causes or from comorbidity (HIV-related disease, cardiovascular and renal disease, diabetes complications). A "10% relative reduction in mortality" applies the effect to all deaths, whereas only a subset of deaths is plausibly modifiable.

MECHANISM: Write r_eff = (fraction reachable) × (effect among reachable deaths). If 25–35% of deaths are unreachable and the effect among reachable deaths is 10%, r falls to 0.065–0.075. That is at or near the materiality line. A weaker effect among reachable deaths pushes it lower. The 4-month HPMZ regimen is a further issue. It shortens the treatment window and likely lowers the on-treatment lung-damage burden that statins are meant to reduce. Only the share of deaths attributable to slow bacterial clearance or immunopathology is left for the adjunct to address, and the absolute effect shrinks if the baseline mortality rate is lower.

EVIDENCE: Waitt & Squire 2011 (systematic review of deaths during TB treatment, mainly in Africa) is the obvious source for timing and causes. I believe it reports that deaths cluster early and in HIV-positive patients, but I cannot recall the exact fractions. Verify. Precedent from other adjuncts: corticosteroids reduced mortality in TB meningitis (Thwaites 2004), a specific anatomical form, but there is no analogous result for pulmonary DS-TB overall. The HPMZ-headroom point is my own inference. UNGROUNDED on exact figures.

STRENGTH: MEDIUM. The logic is sound and the direction is clear, but the unreachable fraction needs data. By itself it is "near-material" per the thread's own threshold.

NOVELTY CHECK: Not on the exclusion list. The thread lists "no adjustment for unreachable deaths" as an unaccounted item, and this critique operationalizes it.

---

CRITIQUE 3: Rifampicin induction structurally limits atorvastatin exposure in routine programs, and the trial exposure does not transfer

HYPOTHESIS: Atorvastatin is a CYP3A4 and OATP1B1 substrate. Rifampicin is a potent CYP3A4 inducer that also inhibits OATP1B1 acutely. The atorvastatin label (as I recall) says concomitant rifampicin should be co-administered simultaneously, because delayed administration after rifampicin gave significantly lower atorvastatin plasma concentrations. That is the OATP-inhibition-versus-induction trade-off. Simultaneous dosing temporarily raises exposure through OATP inhibition, but under chronic daily rifampicin the net steady-state exposure is uncertain and plausibly lower. Programs cannot guarantee simultaneous dosing, and the trial may have been run under supervised, optimized dosing that routine DOT or self-administration does not replicate. Interactions with ART add another layer. Protease inhibitors (ritonavir-boosted) raise atorvastatin exposure and myopathy risk. Efavirenz lowers it. Dolutegravir with doubled-dose-under-rifampicin is less relevant.

MECHANISM: If the statin effect is exposure-dependent, realized relative_reduction scales with achievable AUC or lipophilic tissue concentration in lung lesions. Halving effective exposure could plausibly lower the effect by more than half if the dose-response is steep (unknown). An illustrative range for the multiplier is 0.5–0.8 on r. That is my guess, not derived from data. Magnitude uncertain; it requires a PK/PD model.

Transferability across statins is a related problem. If the prior positive human data are from pravastatin (hydrophilic, not CYP3A4-metabolized, so largely unaffected by rifampicin) or rosuvastatin (minimal CYP metabolism), they do not demonstrate atorvastatin efficacy under rifampicin. The Phase IIc is then testing an exposure-limited drug with a different PK profile from the one that produced the signal.

EVIDENCE: The atorvastatin label statement on rifampicin (verify wording). Kyrklund et al. 2004 reported a large reduction in simvastatin exposure with rifampicin, as I recall, but I cannot confirm the numbers, and simvastatin is not atorvastatin. I believe a Johns Hopkins group (Karakousis) ran pravastatin Phase IIa work and that StAT-TB used a different statin, but I cannot confirm which. The Verifier must identify the exact statin in the prior trial. UNGROUNDED on specific PK reductions for atorvastatin under chronic rifampicin.

STRENGTH: MEDIUM-HIGH. The mechanism is well established pharmacologically, but the quantitative translation into mortality effect is uncertain.

NOVELTY CHECK: Related to the excluded "need for dose-finding," but distinct. The exclusion list explicitly says that showing the rifampicin interaction structurally limits programmatic exposure is new. This critique argues that dose-finding in trials may not translate into delivered exposure in programs, so the Phase IIc result can overstate scale-up performance.

---

CRITIQUE 4: Winner's-curse and reference-class patterns imply the conditional effect should sit well below the surrogate-implied one, and r and p_success should not be independent

HYPOTHESIS: A 10% conditional effect is probably anchored on promising early signals. Effect sizes that clear a statistical filter in small, early trials are systematically overestimated. In TB host-directed therapy, the track record is of surrogate or early-phase positives that fail to translate into outcome benefit. Examples: vitamin D (the Martineau 2011 culture-conversion signal in a genotype subgroup, with no robust outcome benefit in later trials as I recall), CC-11050, metformin and everolimus (the latter two I believe produced mixed or no clear clinical benefit). The Verifier should check each.

The independence assumption also fails. Draws where Phase II/III "pass" are exactly those with large estimated effects, so the posterior mean of the true effect, conditional on passing a surrogate threshold, is shrunk relative to the point estimate. Where trials are powered on surrogates, "passing" selects on surrogate noise as well as true effect.

MECHANISM: With a Bayesian shrinkage factor of 0.7–0.9 (an illustrative assumption), r falls to 0.07–0.09 from this effect alone. Modeling the joint distribution, i.e. a mixture of "real effect" and "surrogate-only or null" worlds, would give E[r × p_success] below the product of means if surrogate-only wins are common.

EVIDENCE: Winner's curse in selected small trials is a general statistical result (logical argument). The HDT reference class is partly recalled and needs verification of each trial's actual endpoints and results. Observational statin cohorts (Taiwan, Korea) suggesting lower TB risk or mortality are exposed to healthy-user and indication bias. I cannot cite specific papers confidently. UNGROUNDED on specifics.

STRENGTH: MEDIUM. It is mainly a general argument and its size depends on how the 10% was derived; CG states no derivation, which weakens the ability to check.

NOVELTY CHECK: Adjacent to the excluded "might not replicate," which is the probability of failure. This critique concerns the conditional effect size given success (shrinkage) and the independence modeling, which the exclusion list does not cover.

---

CRITIQUE 5: Hepatotoxicity and myopathy add a negative tail, and the combined attenuations compound

HYPOTHESIS: Adding atorvastatin to rifampicin, isoniazid and pyrazinamide stacks hepatotoxic risk, and statins carry myopathy risk, higher when co-administered with some ART. In a population where fatal drug-induced liver injury is a recognized cause of treatment death, even a small excess hepatotoxicity-related mortality could offset part of the benefit. Small phase II trials cannot detect this.

MECHANISM: CG models only a non-negative effect. If the true distribution includes a harm tail, E[r] decreases. For example, 10% probability of net-zero or small negative effect contributes about −0.01 on a base of 0.10, which is a modest and not threshold-crossing effect alone. The bigger issue is compounding with Critiques 1–4. Using my illustrative ranges (all assumptions, and they overlap): reachable fraction 0.65–0.75, PK attenuation 0.5–0.8, shrinkage 0.7–0.9. Product 0.23–0.54, so r ≈ 0.023–0.054 vs 0.10. Treat this as an upper-bound illustration, since CG's 10% may already partly embed some attenuation and the factors are correlated.

EVIDENCE: Hepatotoxicity of first-line TB drugs and statin liver and muscle warnings are well established in labeling. I cannot cite a study quantifying excess hepatotoxicity from statin plus HRZ co-treatment. The compounding calculation is my inference. UNGROUNDED on magnitude.

STRENGTH: LOW-MEDIUM individually (the harm tail), but useful as the aggregation argument.

NOVELTY CHECK: Not on the exclusion list. The "no possibility of zero or negative effect" item in the unaccounted list is the basis, and this adds the compounding calculation.

---

SUMMARY: The most important finding is that a mortality-powered Phase III is almost certainly infeasible (roughly 36,000 per arm at 4% baseline mortality), so "success" probably means a surrogate or composite win. That makes the 10% conditional mortality effect much weaker than a straight multiplication by p_success implies. Combined with unreachable deaths, rifampicin-limited statin exposure and winner's-curse shrinkage, a plausible conditional r is 0.03–0.065 vs 0.10, at or below the materiality threshold.

RECOMMENDED VERIFICATION PRIORITIES:
1. Identify the exact prior Phase IIa/b trial, statin, endpoints and effect sizes, and confirm Phase IIc/III primary endpoints in the registry (Critiques 1, 3). This determines whether the core assumption of the thread holds.
2. Check actual on-treatment mortality rates in DS-TB programs and trials, to validate the sample-size arithmetic (Critique 1).
3. Check the atorvastatin label wording and any rifampicin–atorvastatin PK studies under chronic dosing, and which statin the positive human data used (Critique 3).
4. Check the timing and causes of death in Waitt & Squire 2011 to size the unreachable fraction (Critique 2).
5. Check the HDT reference-class outcomes (vitamin D, metformin, CC-11050, everolimus) as recalled in Critique 4.

OUT OF SCOPE OBSERVATIONS: Because the model values only mortality, an adjunct whose real benefit is less lung damage and fewer relapses would be undervalued by the model; this is already on the exclusion list, so I do not develop it. The 10% effect also interacts with the HIV share of the treated population. If HIV-positive patients carry a disproportionate share of deaths and the benefit is attenuated there (via ART interactions), country-level weighting would matter. That belongs to a different thread.

--- Thread: Realism of all-in cost (all_in_cost) — Phase III trial size, ---

# Thread: all_in_cost realism: investigator output

**Baseline inference (my own, not from CG).** The materiality figures imply a baseline SROI of about 2,000 × 10.7 / 7 ≈ 3,000x at $7M. I use this baseline to convert cost changes into SROI multipliers. The Verifier should check it against the CEA.

---

CRITIQUE 1: A $7M Phase III cannot be powered on mortality, and the CEA's benefit is mortality only

HYPOTHESIS: The CEA's benefit stream is mortality reduction, assumed at 10%, and the model credits only mortality. A Phase III that produces guideline-grade evidence of a mortality effect of this size is a very large trial. Even a pragmatic, low-cost one is likely to cost several times $7M for the Phase III alone. If $7M instead buys a surrogate-endpoint trial (culture conversion, unfavourable composite outcome, relapse), the cost is plausible but the evidence does not support the mortality benefit being claimed. CG would then be either understating cost or overstating p_success. The two cannot both be right.

MECHANISM: all_in_cost rises, and SROI falls in proportion to 1/cost.
- Own sample-size calculation (standard two-proportion formula, 80% power, α = 0.05, two-sided). Assume 5% baseline mortality and a 10% relative reduction, from 5.0% to 4.5%. That needs about 28,000 per arm, roughly 57,000 in total.
- With 8% baseline mortality, as in higher-risk or HIV-heavy cohorts, it is still about 17,000 per arm, roughly 35,000 in total.
- At a pragmatic cost of $500–$1,000 per participant, the trial costs about $17M–$57M. At conventional TB-trial per-participant costs, which I believe are in the thousands of dollars (UNGROUNDED), it costs more.
- Enriching for high-mortality groups (TB meningitis, advanced HIV) shrinks N. But it makes the evidence non-generalisable to the drug-susceptible (DS) majority that drives the 3.3M-patient benefit base.
- Central estimate for the Phase III alone is about $25–40M, with a range of $15–100M. Total all-in cost is then about $30–45M. SROI is about 3,000 × 7/37 ≈ 570x, with a plausible range of roughly 300–1,000x. That is a 3–10× reduction, far above the 25% materiality bar.

EVIDENCE:
- Logical and arithmetic argument, labelled as my own inference. The sample-size numbers depend on the baseline mortality and effect size, which the Verifier should recompute.
- The cost-per-participant figures are UNGROUNDED. I believe the RECOVERY trial showed that very low per-patient costs are possible in a streamlined pragmatic design, but I cannot cite a specific figure.
- I cannot cite a specific source stating what endpoint WHO's Guideline Development Group (GDG) would require for an adjunctive host-directed therapy. UNGROUNDED, though the thread lists WHO GDG requirements as a source to check.

STRENGTH: HIGH. The arithmetic is direct, the parameter is high-sensitivity, and the magnitude is a multiple rather than a percentage.

NOVELTY CHECK: Not on the exclusion list. The excluded item is "later trials cost more than $320k, and CG includes them in $7M." This critique does not say later trials are omitted. It says the $7M envelope is internally inconsistent with the endpoint needed to justify the benefit CG credits.

---

CRITIQUE 2: The all-in framing counts benefits for every treated patient but not the cost of treating them

HYPOTHESIS: CG's logic is that the SROI should compare all-in benefits (all patients receiving the sped-up adoption) against all-in costs. Consistency then requires including the cost of the intervention delivered to those patients. The $7M is R&D and adoption cost only. It omits drug procurement, liver-function and safety monitoring, and health-worker time for about 3.3M patients in the credited year. The omission is asymmetric: the benefits of delivery are counted and the costs are not.

MECHANISM: Add delivery cost D to all_in_cost.
- Break-even: SROI stays above 2,000x only if D < $3.7M, which is about $1.10 per patient across 3.3M patients.
- Generic atorvastatin plus monitoring plausibly costs $1–10 per course in procurement. This is the thread's range, and I could not verify prices. Including monitoring and clinic time, it is plausibly higher. That gives D of about $3–33M, or more.
- At a central D of about $10M, before any counterfactual-value discount: total about $17M, SROI ≈ 3,000 × 7/17 ≈ 1,250x.
- If governments and the Global Fund pay and CG values their money at, say, 20–30% of face value (my assumption), D_effective is about $2–3M and the effect is small.
- So the result depends on the counterfactual-value convention, which CG does not state. The unstated convention is itself the finding. The conclusion is anywhere from roughly no change to a 2–3× reduction.

EVIDENCE:
- Logical consistency argument.
- Unit prices: UNGROUNDED here. The thread points to the Stop TB GDF catalog and the MSH price guide, and the Verifier should pull atorvastatin 20–40 mg prices.
- I cannot cite a specific CG or Open Philanthropy statement on how it values third-party government spending. UNGROUNDED.

STRENGTH: MEDIUM-HIGH. The structural omission is clear. The magnitude depends on an unstated discount convention.

NOVELTY CHECK: Not on the exclusion list. The excluded "CG funds only 4.5%" concern is about the funding share. This critique is about cost categories that are missing from the numerator-versus-denominator comparison entirely.

---

CRITIQUE 3: Regulatory, pharmacovigilance and dissemination costs for an off-patent drug have no obvious payer, and the $7M likely under-budgets them

HYPOTHESIS: Atorvastatin is generic, so no sponsor has a commercial incentive to file a label extension, run pharmacovigilance, or fund country-level uptake. "Guideline change, dissemination and validation" must cover WHO guideline development, national guideline updates across the high-burden countries, training, supply-chain integration, and post-adoption safety surveillance. Statins can cause hepatotoxicity and myopathy, and these overlap with the hepatotoxicity of rifampicin, isoniazid and pyrazinamide. Safety monitoring and adverse-event management are therefore a real cost, and a regulatory-credibility cost, for an adjunct given to nearly all patients. Adverse-event harms are also not netted against the mortality benefit. That is outside this thread's cost scope, but I note it.

MECHANISM: all_in_cost rises by the unfunded adoption infrastructure.
- No component is quantifiable from sources I can cite. As an illustration only, with no empirical basis (UNGROUNDED): a multi-country guideline and rollout programme of $5–20M would add 70–300% to the $7M.
- Even a $4M add-on pushes the total past the $10.7M threshold.
- The point is that the $7M leaves little headroom. A Phase IIc of $320k plus any plausible Phase III already uses most of it.

EVIDENCE:
- Logical argument about the incentive structure of generic repurposing.
- The hepatotoxicity overlap between statins and first-line TB drugs is a pharmacological argument I believe is sound. I cannot cite a specific paper.
- I cannot identify a reliable source for rollout costs of comparable TB regimen changes. UNGROUNDED. Candidates for the Verifier are Unitaid and Global Fund transition-grant documentation.

STRENGTH: MEDIUM. The mechanism is plausible but the magnitude is speculative.

NOVELTY CHECK: Partly adjacent to "CG includes guideline change and dissemination in the $7M." The new point is that these categories have no breakdown, no payer, and a specific safety-monitoring component that is not obviously covered.

---

CRITIQUE 4: Unclear scope boundary for the sweat-diagnostic workstream

HYPOTHESIS: The thread notes a sweat-diagnostic workstream. If the diagnostic work is part of the same program, its costs are either inside the $7M, which leaves less for statin Phase III and adoption, or outside it. If outside, the all-in cost is understated. If the diagnostic's benefits are included in the credited benefits but its costs are not, that is a mismatch. If it is a separate program, shared trial infrastructure could be double-counted or free-ridden in either direction.

MECHANISM: Ambiguous in sign.
- If diagnostic costs are excluded but diagnostic-linked benefits are counted, cost is understated by the diagnostic budget.
- That budget is unknown. Any budget above about $3.7M would breach the 2,000x threshold.
- If it is separate and its benefits are not counted, there is no effect.
- Magnitude uncertain; this requires clarification of the grant structure.

EVIDENCE: UNGROUNDED. I have no source on the structure of the workstream beyond the thread description. This is a clarification question for CG, not an established flaw.

STRENGTH: LOW. It is plausible and cheap to check, but I cannot establish that the problem exists.

NOVELTY CHECK: Not on the exclusion list.

---

CRITIQUE 5: Reference-class check: TB Phase III trials, and the evidence package WHO may require, point to more than one trial

HYPOTHESIS: Published Phase III TB trials (Study 31/A5349, STREAM, endTB, TRUNCATE-TB, SimpliciTB) enrolled hundreds to thousands of participants. I believe their budgets were generally in the tens of millions of dollars, though I cannot cite specific figures. A $7M all-in budget would sit well below that reference class. A WHO guideline change for an adjunctive therapy given to all DS-TB patients might also require evidence across subgroups (HIV co-infection, children, pregnancy, drug-resistant TB) or more than one trial or an individual patient data meta-analysis. That multiplies Phase III cost.

MECHANISM: all_in_cost scales with the number and size of trials.
- If the reference class is $20–60M for a single Phase III, all-in cost is 3–9× the CG figure and SROI falls to roughly 350–1,000x.
- The reference class might overstate the cost for a cheap oral adjunct using routine-care endpoints. This is the main counterargument.
- If it holds, a central total of $30M, SROI of about 700x, is reasonable.

EVIDENCE:
- The thread lists NIH RePORTER, EDCTP, Unitaid, Gates and Treatment Action Group (TAG) reports as sources. The Verifier should use them to establish actual budgets.
- The figures above are from my recollection and UNGROUNDED.
- I cannot cite a specific WHO document establishing the number-of-trials requirement.

STRENGTH: MEDIUM. The reference-class approach is standard, and the verification path is clear. I am uncertain about the figures.

NOVELTY CHECK: Related to the excluded "later trials cost more," but different. This asks whether the $7M is realistic against a benchmark, and CG provides no reconciliation with one.

---

**SUMMARY:** The most important finding is that $7M is hard to reconcile with a mortality-powered Phase III, which the 10% mortality benefit requires. The omission of delivery costs from an all-in comparison that counts all patients' benefits is also a structural inconsistency. A central all-in cost of about $30–45M implies SROI of roughly 400–700x, versus about 3,000x at $7M.

**RECOMMENDED VERIFICATION PRIORITIES:**
1. **Critique 1.** Recompute the sample size from CG's own baseline mortality and effect size, and establish what endpoint WHO would require. This is the highest-leverage check, and it also bears on Thread 1 (p_success).
2. **Critique 5.** Get actual budgets for Study 31, TRUNCATE-TB, STREAM and endTB from NIH RePORTER, Unitaid, EDCTP and TAG, to ground the reference class.
3. **Critique 2.** Pull generic atorvastatin unit prices from GDF and MSH, and find whether CG states a convention for third-party spending, since the magnitude turns on it.
4. **Critiques 3 and 4.** Lower priority. Critique 4 needs a clarification from CG and not a literature search.

**OUT OF SCOPE OBSERVATIONS:**
- If all-in cost is treated as certain while benefits are multiplied by p_success, the model may overstate expected cost. Later-stage spend only occurs if earlier stages succeed. This works in CG's favour and should be checked for symmetry.
- The rifampicin–atorvastatin pharmacokinetic interaction and adverse-event netting against benefits belong to other threads.

--- Thread: Structural — counterfactual definition of "speedup," attribution ---

# Candidate Critiques: Counterfactual Framing, Attribution, Discounting

**Note on inputs.** I was not given the CEA spreadsheet. From the materiality thresholds I infer a base SROI of about 3,050x and a $7M all-in cost, of which CG pays about $320k (about 4.5%). All derived numbers below are my own calculations. Parameters I had to assume are labeled as such.

---

CRITIQUE 1: The speedup benefit and the all-in cost come from different counterfactuals. Every coherent framing gives roughly 10–20x higher SROI.

HYPOTHESIS: The BOTEC counts benefit as one year of plateau-level deaths averted. That is the value of shifting the whole pathway one year earlier, so the counterfactual is "the same pathway happens later." It then charges the full $7M pathway as cost. That is the cost of the world where the pathway never happens otherwise. The numerator comes from the "delay" world and the denominator from the "never" world. No single counterfactual yields this ratio.

I derived the ratio under each coherent framing. Let PV_B be the present value of the whole program's benefits (including p_success), and PV_C the PV of its costs.

- **Pure delay (others would fund it D years later).** Delaying the whole program by D years loses (1−e^(−rD))·PV_B in benefits. It also defers (1−e^(−rD))·PV_C in costs. The real cost of acceleration is therefore only the interest on moving ~$7M forward, about r·D·PV_C. The ratio of benefit to cost is **PV_B/PV_C, independent of D**. The $6.7M downstream spend is not a cost of the grant. It is only the time value of money pulled forward.
- **Never (no one else would run it).** Benefits are PV_B over all future years. The cost is PV_C. The ratio is again **PV_B/PV_C**.
- **Mixture with probability q of "never."** Numerator and denominator both scale by the same factor, so the ratio is again PV_B/PV_C.

The BOTEC's ratio is instead roughly (one year of plateau benefit)/(full cost), which is far smaller than PV_B/PV_C whenever benefits last many years.

MECHANISM: PV_B/PV_C is approximately (BOTEC SROI) × (effective benefit-years in PV terms) × (a cost-discount adjustment).

- Under illustrative assumptions of r = 4% plus the model's 2% annual decline in cases, the effective benefit-years are about 1/(0.06) ≈ 17, times a delay factor of about 0.6–0.7. That gives about 10–11 benefit-years.
- Adjusting for discounted costs (÷ ~0.85) gives about 12–13x.
- Without the 2% decline and with r = 4%, it is about 18x.
- This implies a coherent SROI on the order of **30,000–55,000x versus ~3,050x**.
- The result is bounded by a finite adoption horizon, drug or regimen obsolescence, and the fact that other funders' dollars are not free.
- The ranking (coherent framing ≥ BOTEC) holds under any horizon longer than about 1.5–2 years of effective benefit.
- The number to report is the coherent ratio, not the 10–20x multiple itself. The multiple depends on horizon assumptions that I had to assume.

A separate but related issue is whose dollars count. The all-in ratio treats other funders' money as equal in value to CG's. If that money would otherwise fund TB research at similar cost-effectiveness, displacement should be charged. That would reduce the delay-branch benefit and is not captured in either framing.

EVIDENCE: Logical and algebraic argument (my own derivation). It requires no external source. It does require the CEA to confirm that the benefit really is "1 year × plateau annual deaths averted." UNGROUNDED as to whether CG has an internal rationale for the hybrid framing, for example deliberate conservatism. If CG describes the choice as deliberately conservative, the finding becomes "the framing is knowingly biased low by roughly an order of magnitude" rather than an error.

STRENGTH: HIGH. The mechanism is algebraic, and the magnitude is well above the materiality threshold. The direction is upward, which is useful for decisions near the bar and for rank-ordering grants. If CG intends SROI as a consistent cross-grant metric, the hybrid framing will mis-rank this grant against grants evaluated under a different counterfactual.

NOVELTY CHECK: This is the exact new item the exclusion list asks for: it shows that the speedup and all-in framings are mutually inconsistent, and it derives the coherent estimate. It does not simply restate the 4.5% share (CG's all-in approach is retained), the 1-year assumption, or the no-discounting note.

---

CRITIQUE 2: The funding landscape for a generic-statin TB program makes "never" a live branch. The speedup is a poor proxy for the grant's real counterfactual.

HYPOTHESIS: Statins are off-patent and cheap. The Phase III-scale trial needed for a WHO recommendation has no commercial sponsor. The plausible funders are NIH (Johns Hopkins and related groups have published preclinical and early clinical work, which I recall but cannot cite precisely), EDCTP, Unitaid, Gates, MRC, and national agencies. Public-health funders have so far favored novel regimens, shortened regimens, and vaccines over host-directed therapies. If so, the realistic counterfactual for a CG-funded Phase IIc is not "same trial in one year" but a long, uncertain delay, or never. That is a distribution, not a point value.

If the grant is the gating event for this pathway (dose-finding precedes Phase III), the speedup has a structure the BOTEC does not model:

- With probability q, a gap of 3+ years, or never.
- With probability 1−q, a delay of 0.5–2 years.
- The expected effective speedup is q·H_eff + (1−q)·D, where H_eff is the effective horizon of benefits (about 10+ years by my Critique 1 calculation).
- Even for modest q (say 0.1–0.2), this exceeds 1 year.
- The break-even is q ≈ 0 (see Critique 1). With the all-in cost counted in the "never" branch, the ratio improves in every branch.

MECHANISM: This critique concerns which branch is realistic. It affects `speedup_years` (should be an expected value, plausibly >1) and whether benefits should be credited for all future years. Because the SROI ratio is robust to q (Critique 1), the main effect is on the **total value created per CG dollar**. This matters if CG's all-in framing is replaced by crediting the grant with its own marginal impact on a $320k cost. In that case the SROI could be roughly 20× higher than the current figure, and the grant would look like a high-leverage seed funder rather than a marginal accelerator. The direction is up. It could be down if there is an existing, adequately funded statin-TB trial that makes the CG grant redundant (q ≈ 0 and D ≈ 0).

EVIDENCE: UNGROUNDED for the specific funder landscape. The following need verification:

- ClinicalTrials.gov and WHO ICTRP search for statin / pravastatin / atorvastatin / rosuvastatin + tuberculosis, with sponsor, phase, status, and start date.
- The TAG pipeline report and the Working Group on New TB Drugs pipeline, to see whether host-directed therapies or statins appear and with which funders.
- EDCTP and Unitaid portfolio pages.
- NIH RePORTER for statin-TB awards.

I believe this is a concern but cannot identify a specific source. The logical argument is that generic drugs lack a sponsor, which is a standard finding in the repurposing literature. I cannot give a specific citation.

STRENGTH: MEDIUM. The logic is sound and the potential magnitude is large, but it hinges on registry facts I cannot confirm. A registry finding of an already-funded Phase II/III statin-TB trial would invert the conclusion.

NOVELTY CHECK: Related to the excluded "speedup is an assumption" and "CG funds small share" items, but distinct. Those are about whether the numbers are stated as assumptions. This is about which counterfactual world is plausible given the funders, and the implication of that world for expected speedup.

---

CRITIQUE 3: Discounting quantified properly with an S-curve ramp and discounted costs. The net effect is about −20% to −31%, not the benefit-only −21% to −35%.

HYPOTHESIS: The thread's materiality figures discount a flat benefit stream at 8–9 years (×0.64–0.79 for 3–5%). Two refinements move the answer in opposite directions.

(i) **Adoption ramp pushes benefit later.** A one-year shift of an adoption curve gains, in discounted terms, about r·Δ·PV(benefit stream). For a ramp of length L starting at T0, the factor relative to the BOTEC's undiscounted "1 year × plateau" is approximately e^(−rT0)·(1−e^(−rL))/(rL). I assumed T0 = 8.5 years and a linear ramp of L = 6 years; the true uptake curve in the model is unknown.

| Discount rate | Benefit factor |
|---|---|
| 3% | ≈ 0.71 |
| 4% | ≈ 0.63 (about 0.62 with the exact 1−e^(−rΔ)) |
| 5% | ≈ 0.57 |

These are slightly lower than the flat-8.5-year factors (0.77 / 0.71 / 0.65).

(ii) **Costs are also discounted.** The $6.7M downstream spend is incurred during years ~1–8, before benefits. Spreading it uniformly over years 1–8, the all-in cost PV is ≈ 0.88 / 0.85 / 0.82 of nominal at 3% / 4% / 5%.

Net SROI factor (benefit factor ÷ cost factor):

| Discount rate | Net factor | Approximate SROI |
|---|---|---|
| 3% | ≈ 0.80 | ≈ 2,440x |
| 4% | ≈ 0.73 | ≈ 2,230x |
| 5% | ≈ 0.69 | ≈ 2,100x |

MECHANISM: A benefit-only discount overstates the penalty. A consistent discounting of benefits and costs gives roughly −20% / −27% / −31% for 3% / 4% / 5%. That is near the 25% materiality line at 4% and above it at 5%. If costs are probability-weighted by stage (Critique 4), expected spend falls and weights toward the near term, so the cost-side offset changes only modestly. If the S-curve ramp is longer (L = 10), the benefit factor falls further, to roughly 0.57 (4%) and 0.51 (5%).

The more important structural point is a conflict with Critique 1. Under any coherent counterfactual framing, discounting has a smaller effect than in the speedup framing. In the PV_B/PV_C framing the discount factor still applies, but it is dwarfed by the framing effect. The decision-relevant question is therefore which framing CG adopts. Discounting is a second-order refinement.

EVIDENCE: Algebraic derivation (mine). The assumptions about uniform spending, T0 = 8.5, and ramp length are illustrative and should be replaced with the CEA's actual timeline.

On CG's convention: I believe GiveWell has used roughly 4% for discounting consumption benefits in some CEAs, and that CG's GHW BOTECs sometimes apply and sometimes omit discounting. I cannot identify a specific CG source stating a rate or a rule for R&D BOTECs. The Verifier should check "How we use BOTECs" (May 2025) and the GHW cause-prioritization posts for discounting guidance. The materiality text implies the bar is roughly 2,000x, but I cannot confirm that value.

STRENGTH: MEDIUM. The magnitude is near the threshold only at ≥4–5%, and it depends on the convention CG actually applies. The refinement of the benefit and cost sides is a real contribution, but the ordering matters less than Critique 1.

NOVELTY CHECK: "No time discounting" is in the exclusion list, and I do not raise it as an omission. This quantifies it under assumed CG conventions and adds two points the thread framing did not give: the S-curve ramp effect, and the offsetting discounting of costs.

---

CRITIQUE 4: Probability weighting is asymmetric between benefit and cost.

HYPOTHESIS: Benefits are multiplied by p_success = 0.40. If the $7M cost is a nominal sum of all stages, the denominator ignores that later-stage spend only occurs if earlier stages succeed. Under a sequential, gated pathway (Phase IIc, then Phase III, then implementation or demonstration studies), expected spend is lower than nominal spend. The benefit is discounted for failure while the cost is not. This is a double penalty.

MECHANISM: Expected all-in cost = $0.32M + s × $6.7M, where s is the probability that downstream spending actually occurs. With s = 0.6 (illustrative), expected cost is about $4.3M, which raises SROI by about 1.6x. With s = 0.4 it is about $3.0M (about 2.3x). If the $7M already reflects expected values, the critique does not apply. The direction is up.

There is a subtle counterpoint. If p_success = 0.40 is the probability of the whole pathway succeeding, the probability that spending reaches Phase III may be higher than 0.40, since failure can occur late. Late failure still incurs most of the cost. The correct s therefore lies between 0.4 and 1, and the effect might be small. I cannot determine this without the CEA.

EVIDENCE: Logical argument. UNGROUNDED as to how CG built the $7M and whether it weights costs by stage. This requires inspecting the CEA cells.

STRENGTH: LOW–MEDIUM. The mechanism is sound and could exceed the threshold, but it depends on a spreadsheet detail I cannot see.

NOVELTY CHECK: Not on the exclusion list. The excluded item "later trials are in the $7M" concerns whether later costs are included. This concerns whether they are weighted by probability.

---

CRITIQUE 5: A 1-year speedup of trial results does not necessarily become a 1-year speedup of adoption, in either direction.

HYPOTHESIS: The model assumes a pure translation of the adoption curve by one year. That holds only if the trial is the binding constraint on adoption. For a generic adjunct drug, adoption requires a WHO guideline (via a Guideline Development Group cycle), national policy updates, and procurement or training. Each step has its own lags and queue. If some steps are slack-bound (for example, WHO guideline updates occur on a roughly fixed schedule), earlier trial results may be absorbed into waiting time, giving a speedup of less than one year. The effect could be asymmetric: trial results arriving just after a guideline window close could cost a full cycle (2+ years) for a short delay. In that case the speedup is more than a year.

The speedup is therefore a random variable with a lumpy distribution. The expected value could differ from the point estimate in either direction, and 1 year may be a reasonable central value but not a defensible point value.

MECHANISM: `speedup_years` is linear in SROI. The materiality threshold is a speedup of about 0.65 years. A loss of one guideline cycle on a short delay would push the effective speedup well above 1. Slack absorption would push it below 0.65 only if the guideline pipeline were slack-bound for more than a third of the year. I cannot estimate the probabilities. Magnitude is uncertain and requires sensitivity analysis.

EVIDENCE: UNGROUNDED. The WHO guideline process for TB (Guideline Development Groups, a public call for data) is institutional, and I do not have a source on cycle lengths. The Verifier should check historical lags between pivotal trial publication and WHO guideline changes for TB regimens (for example, the 4-month rifapentine-moxifloxacin regimen of Study 31/A5349 and the shift to BPaLM). I believe this is a concern but cannot cite specific lags.

STRENGTH: LOW–MEDIUM. It is plausible and the effect is symmetric in direction, so it does not provide a clear case for revising the point estimate. It supports modeling speedup as a distribution.

NOVELTY CHECK: Not on the exclusion list. "Speedup is an assumption" concerns the existence of the assumption, not its transmission through the adoption pipeline.

---

## OUT OF SCOPE OBSERVATIONS

- If CG's SROI uses a fixed horizon for plateau benefits, the 2% annual decline in cases (an explicit assumption) interacts with the horizon in Critique 1. The Verifier should check whether the decline is applied.
- The displacement of other funders' dollars (Critique 1) is a general leverage-accounting question that reaches beyond this thread.

---

**SUMMARY:** The BOTEC mixes the benefit of a one-year delay counterfactual with the cost of a never-happens counterfactual. Any coherent single framing (delay, never, or a mixture) gives a ratio of about PV_B/PV_C, which I estimate is roughly an order of magnitude higher than the BOTEC's ~3,050x. Discounting benefits and costs consistently has a smaller effect (−20% to −31%, near the materiality threshold at 4–5%).

**RECOMMENDED VERIFICATION PRIORITIES:**

1. **Critique 1.** Confirm from the CEA that benefit = 1 year × plateau annual deaths averted and cost = full $7M. Check for any CG text defending the hybrid as deliberately conservative. This is the highest-leverage finding, and the Verifier can check it algebraically.
2. **Critique 2.** Run the registry and funder searches (ClinicalTrials.gov, TAG pipeline, NIH RePORTER, EDCTP, Unitaid) for statin-TB trials. A found, funded, adequately resourced trial would reverse the direction of the finding.
3. **Critique 3.** Find CG's stated discount-rate convention in "How we use BOTECs" and the GHW framework posts, and replace my assumed ramp length and spending timeline with the model's real values.
4. **Critique 4.** Inspect how the $7M was built, to see whether costs are weighted by stage probabilities.

--- Thread: Unvalued benefits — post-TB lung disease, long-term post-treatment ---

# Thread: Unvalued benefits (post-TB lung disease, post-treatment mortality, transmission, diagnostic)

**Conventions used throughout.**
- I treat the ~535k DALY figure as already weighted by p_success = 0.40. "Pre-p" numbers are per adoption-year before that weighting.
- Where I give a number, the inputs are labelled as my own inference. I have not verified them against the sources.
- Exact figures from Menzies 2021 and Romanowski 2019 are flagged for the Verifier. I recall the direction of both findings but not the precise values.

---

## CRITIQUE 1: Post-TB lung disease morbidity is likely the largest unvalued channel (~50–60k central, wide range)

**HYPOTHESIS:** The trial's strongest signal was reduced lung damage, and the BOTEC gives it zero value. Post-TB lung disease (airflow obstruction, restrictive impairment, bronchiectasis, and chronic breathlessness) affects a large share of survivors for decades. Even a modest proportional reduction in that burden, applied to 3.3M patients, is not trivial relative to a 535k base.

**MECHANISM:** This adds a new term: patients × baseline post-TB morbidity DALYs × relative reduction × probability weight.
- Baseline per patient (inference): about 30% have clinically meaningful impairment. Average disability weight is ~0.1–0.2 (GBD chronic respiratory states, which I'd verify) over ~15–25 years. That gives ~2.5 DALYs per affected patient, or ~0.75 DALYs per treated patient. The pool is then 3.3M × 0.75 ≈ 2.5M DALYs per adoption-year.
- Reduction attributable to the intervention: 5% central. This is deliberately lower than the trial's lung-damage signal, to allow for surrogate attenuation. The range is 2–15%.
- Pre-p: 2.5M × 0.05 ≈ 124k.
- Probability weight: ~0.45. This is p_success = 0.4, plus a small contribution from the branch where the mortality endpoint fails but the lung benefit is real and still leads to adoption (see Critique 4).
- Result: ~55k central. The range is ~10k (2% reduction, lower baseline) to ~300k (15% reduction, ~1.5 DALYs per patient baseline).
- By itself this is below the 134k threshold. It reaches the threshold only in the upper half of the range.

Under CG's no-discounting convention these decades-long DALYs count in full. That inflates this channel relative to a discounted calculation, so it is partly an artifact of the convention. I would report both versions.

**EVIDENCE:**
- Menzies et al. 2021 (Lancet Glob Health, systematic review and meta-analysis of lifetime TB burden) reportedly attributes a substantial share of lifetime DALYs per incident case to post-TB sequelae. I believe the share is large but cannot confirm the exact proportion. The Verifier should check it, since it anchors my baseline (0.75 DALYs per patient).
- The International Post-TB Symposium consensus and Allwood et al. document the high prevalence of post-TB lung disease. The prevalence and disability-weight inputs above are my own inference from that literature, not quoted values.
- The link between reduced early lung damage and long-term function is not established in an RCT with long follow-up. That is UNGROUNDED for the specific statin effect size, and the 5% figure is my assumption.

**STRENGTH:** MEDIUM. The channel is real and the direction is clear. The magnitude depends on a surrogate-to-outcome translation with no direct evidence.

**NOVELTY CHECK:** The exclusion list says noting the omission is not a finding and quantifying it is. This critique quantifies it with explicit assumptions.

---

## CRITIQUE 2: Post-treatment excess mortality (~40–50k central) and a related sign-reversing adjustment

**HYPOTHESIS:** TB survivors have a substantially elevated long-term all-cause mortality rate compared with matched controls. Part of that is respiratory and plausibly linked to residual lung damage. A lung-sparing adjunct could avert some of these deaths, in addition to the on-treatment deaths CG values. There is also a counterweight. CG's DALYs per on-treatment death averted presumably assume near-normal remaining life expectancy, but the patients rescued from death are those with advanced disease, who are likely to have a worse post-TB prognosis.

**MECHANISM:** There are two opposite-signed adjustments.

**(a) Upside, excess-death channel** (inference-based arithmetic):
- Cumulative excess mortality over ~10 years: ~10% of survivors. Romanowski 2019 reports elevated post-treatment mortality, but the specific values here are my illustrative assumption.
- Share attributable to lung and respiratory sequelae: ~40%. This is UNGROUNDED.
- Reduction attributable to the intervention: 5%.
- Deaths averted: 0.10 × 0.4 × 0.05 = 0.002 per patient.
- DALYs per death averted at the typical age of death: ~15.
- Result: 0.03 DALYs per patient × 3.3M ≈ 100k pre-p, or ~45k after weighting.
- The statin's own cardiovascular benefit over a ~6-month course is negligible. I'd treat it as zero.

**(b) Downside, life-expectancy adjustment:**
- If on-treatment deaths averted are valued at standard life expectancy, the benefit is overstated by roughly 5–10%. This applies to a subpopulation with higher baseline mortality (HIV, malnutrition, advanced disease).
- Applied to 535k, that is about −25k to −55k.
- The two adjustments could nearly cancel. A net-zero effect is possible.

**EVIDENCE:**
- Romanowski et al. 2019 (Lancet Infect Dis) is the primary source for elevated post-treatment mortality. I recall the pooled all-cause mortality being a multiple of the general population's, but I have not confirmed the number.
- The respiratory attribution share and the "advanced disease lowers residual life expectancy" argument are my own inference. UNGROUNDED pending verification.

**STRENGTH:** MEDIUM for (a), LOW-MEDIUM for (b). Both are logically sound but rest on assumed parameters.

**NOVELTY CHECK:** Distinct from the excluded "mortality only" note. Part (b) is new because it reduces the valued benefit rather than adding to it, which is relevant to "upside findings are as decision-relevant as downside ones."

---

## CRITIQUE 3: Transmission benefit is small, with a bounded calculation (~10–30k central)

**HYPOTHESIS:** Faster culture conversion could shorten infectiousness. Because most transmission occurs before diagnosis, and infectiousness falls quickly after effective therapy starts, the incremental effect is small. But the benefit chains through to secondary cases, so a tiny fractional change is not negligible.

**MECHANISM:**
- Direct secondary disease cases per index case: ~0.3–1 (inference).
- Share of an index case's lifetime transmission occurring after treatment start: ~1–5% (inference, UNGROUNDED).
- Fractional reduction in that post-start transmission from a faster conversion: ~10–20%.
- Net transmission reduction: ~0.1–1%, with 0.3% as central.
- DALYs per secondary case (including its mortality and morbidity): ~10.
- Calculation: 3.3M × 0.5 secondary cases × 0.003 × 10 ≈ 50k pre-p, or ~20k after weighting.
- The range is ~3k to ~150k, with a heavy upper tail.
- Two further adjustments push the estimate down:
  - Sputum culture conversion at 8 weeks does not map one-to-one to infectiousness reduction.
  - Fewer secondary cases are averted if the incidence trend and treated-share assumptions are already near saturation.

**EVIDENCE:**
- The literature on rapid infectiousness decline after starting effective therapy and on pre-diagnosis transmission supports the logic. I cannot name specific studies with confidence. UNGROUNDED, and the Verifier should find the most relevant modelling studies.
- All numerical inputs are my own inference.

**STRENGTH:** LOW-MEDIUM. The channel is real, but I expect it to be well below the materiality threshold on its own.

**NOVELTY CHECK:** Not on the exclusion list. The thread spec already guesses it is small, and the value added here is a bounded calculation with an upper tail.

---

## CRITIQUE 4: The "lung benefit without mortality benefit" scenario is structurally less valuable than a simple p_success weighting implies

**HYPOTHESIS:** The thread's framing suggests the unvalued channels might make the estimate "robust even if the on-treatment mortality effect is small." That holds only if a surrogate-only result still leads to adoption at similar scale. The Phase III endpoint, and what WHO guideline bodies require, determines this.
- If the trial's primary endpoint is something like unfavorable outcome or relapse rather than lung function, a lung-only benefit would not obviously earn a recommendation.
- Adoption would also require willingness to pay for an additional drug for 3.3M patients.
- This gives an adoption probability in the "mortality fails, lung holds" branch well below the 60% uptake CG assumes. I'd guess ≤10–20%, but this is UNGROUNDED.

**MECHANISM:** This is a correction to how Critiques 1–3 are weighted, not a separate value term.
- Simple weighting: p_success × full uptake. If I naively applied the same 60% uptake in the lung-only branch, the lung channel would be up to ~2× higher (a probability of roughly 0.4 + 0.6 × P(lung holds | mortality fails) instead of 0.45).
- Realistic weighting, with P(lung holds | mortality fails) at 0.3–0.5 and conditional adoption of 10–20%, adds only ~0.02–0.06 to the 0.4 base. That supports the ~0.45 figure I used.
- Net effect: the lung channel is closer to 1× than 2× its p_success-weighted value, which limits the upside. Anyone who weights it by a "surrogate holds" probability alone without discounting for adoption will overstate it.

**EVIDENCE:**
- Logical and structural argument about regulatory and guideline pathways. I cannot identify a specific source for this trial's registered endpoints. UNGROUNDED.
- The Verifier should check the Phase IIc and planned Phase III endpoints, and how WHO guideline development weighs lung-function surrogates.

**STRENGTH:** MEDIUM. It affects how the probability weight is applied across several channels, and it is a methodological check on the thread's own logic.

**NOVELTY CHECK:** Distinct from the "might not replicate" item, which p_success already covers. This concerns the conditional adoption probability in the branch where p_success fails but a surrogate holds.

---

## CRITIQUE 5: The sweat-based diagnostic carries real option value but is speculative (~10–30k central)

**HYPOTHESIS:** CG assigns zero value to the sweat-based TB diagnostic funded alongside the trial. A non-sputum, point-of-care test could reach people who cannot produce sputum (children, people with HIV, those without access to labs). Roughly 2–3M TB cases per year are undiagnosed or unreported. A successful test could therefore add value on a scale comparable to the main intervention, but the probability of success is low and counterfactual diagnostics (tongue swabs and others) are advancing.

**MECHANISM:**
- P(reaches adoption): ~5%. This is UNGROUNDED; it is a typical early-stage-diagnostic base rate, not a figure from a source.
- Incremental cases detected beyond what alternative tests would detect (e.g., tongue-swab PCR): ~1–3% of incidence of ~10M, so ~100–300k cases per year.
- DALYs averted per additional case treated: ~5, assuming ~20% case fatality untreated × ~25 DALYs.
- Calculation: 0.05 × 200k × 5 ≈ 50k DALYs per year. Allowing for a delay before adoption and for counterfactual displacement, I discount this to ~10–30k. The range is 0 to ~100k.
- One consistency point for the Verifier: if the $7M all-in cost already includes the diagnostic's funding while the benefit is zero, the omission biases against the intervention. If it excludes the diagnostic funding, treating it as separate is defensible.

**EVIDENCE:**
- I cannot cite a specific source for the sweat-based test's development stage, accuracy, or regulatory path. UNGROUNDED.
- The existence of competing non-sputum diagnostics (tongue swab, urine LAM) is an inference from the broader field. I have not checked current WHO endorsements.

**STRENGTH:** LOW. The expected value is plausible but rests almost entirely on an unverified success probability and on the counterfactual.

**NOVELTY CHECK:** Item (d) in the thread scope, not previously on the exclusion list. The new element is the cost-consistency question and a bounded estimate.

---

## SUMMARY

Quantified with explicit assumptions, the four unvalued channels sum to a central estimate near ~130–150k DALYs per adoption-year (lung morbidity ~55k, excess mortality ~45k, transmission ~20k, diagnostic ~15k). That is essentially at the 134k materiality threshold, with a range of roughly 40k to 400k+ that is skewed upward by the lung-disease and transmission channels. Offsets (the life-expectancy adjustment, conditional adoption in the surrogate-only branch, the no-discounting inflation of decades-long DALYs) could reduce it by 25–50k. The honest conclusion is that this is a borderline-material upside with large uncertainty, not a clear 25%+ correction.

## RECOMMENDED VERIFICATION PRIORITIES

1. **Menzies 2021 (Critique 1).** Check the exact share of lifetime TB DALYs attributed to post-TB sequelae and the per-case DALY total. This anchors the largest channel, and my 0.75 DALYs per patient baseline is the most consequential assumption.
2. **Romanowski 2019 and the respiratory share of post-TB deaths (Critique 2).** Check the pooled mortality figures and cause-of-death attribution. Both the 10% cumulative excess and the 40% respiratory share are my own placeholders.
3. **The trial's registered Phase III endpoint and WHO adoption criteria (Critique 4).** This determines whether the surrogate-only branch has any value, and it affects how every channel should be weighted.
4. **The prior trial's lung outcomes.** Check effect sizes and whether any longer follow-up exists. This tests whether 5% is reasonable, too conservative, or too optimistic.
5. **The $7M composition (Critique 5).** Check whether it includes the diagnostic work. If it does, the zero benefit is an inconsistency worth flagging.

**OUT OF SCOPE OBSERVATIONS:** The DALY value assigned to each on-treatment death averted (life-expectancy and age-at-death assumptions) sits in the core mortality calculation, not in this thread. It interacts with Critique 2(b) and should be checked there.

--- Thread: Implementation — trial execution, guideline adoption pathway, ---

```
CRITIQUE 1: 60% steady-state uptake has no precedent among comparable TB program additions

HYPOTHESIS: CG's 60% is justified as "generic and cheap." Cost is only one of several determinants of uptake in TB programs. Comparable additions have often taken many years to reach even moderate coverage, and some stall below 50%. These include Xpert MTB/RIF (WHO endorsement 2010), the 4-month rifapentine-moxifloxacin regimen (WHO 2022), and adjunctive dexamethasone for TB meningitis (evidence 2004, widely recommended afterward). Adjunctive pyridoxine with isoniazid has also been recommended for years but is inconsistently supplied. An adjunct with no direct patient-visible benefit (it does not shorten treatment) and a separate pill is, if anything, a harder sell than diagnostics or regimens that simplify care. 60% is therefore plausibly an upper-bound or optimistic-case value, not a central one.

MECHANISM: adult_uptake enters roughly linearly. Reducing the long-run ceiling to 0.30–0.40 (the materiality line is 0.39) cuts SROI by 33–50%. Ramp shape matters little for a one-year speedup over an infinite horizon, because shifting any ramp by one year gains about (ceiling × one year of cases). So the ceiling matters much more than the ramp. The ramp only matters through a finite horizon, incidence decline and discounting (Thread 3).

EVIDENCE: Logical argument plus my recollection of precedents. I believe WHO Global TB Reports show that well over a decade after endorsement, Xpert/WRD was still the initial test for well under 100% of notified cases (roughly 40–50% in recent reports), but I cannot give an exact figure or citation, so this is UNGROUNDED as to numbers. I believe the dexamethasone-for-TBM and pyridoxine examples are real, but I cannot cite specific coverage data. Type of evidence: inference from precedents, not a direct study. The Verifier should pull WHO Global TB Report WRD-testing percentages by year and the HPMZ rollout data (GDF orders, number of countries adopting).

STRENGTH: MEDIUM-HIGH. It hits the primary parameter and a plausible downward revision of 0.15–0.25 crosses materiality. The evidence is analogical, not direct.

NOVELTY CHECK: The exclusion list says "60% is assumed." This critique does not restate that. It argues that the cited justification (generic, cheap) is insufficient given empirical uptake curves for TB program additions, and that the ceiling rather than the ramp is what drives value under CG's speedup framing.
```

```
CRITIQUE 2: A Phase III cannot be powered on mortality, so the WHO GDG would be recommending on surrogate or composite endpoints

HYPOTHESIS: CG's value is entirely mortality-based. If the modeled relative reduction (~10%) refers to mortality in DS-TB, a Phase III cannot feasibly detect it. On-treatment mortality in DS-TB is perhaps 3–6% in many settings, though higher with HIV or in severe disease. Detecting a 10% relative reduction from a 5% baseline (absolute 0.5 pp; alpha 0.05, power 80%) needs roughly 2 × (2.8)² × 0.0475 / 0.005² ≈ 30,000 per arm. That is my own calculation and rests on the assumed baseline. The realistic Phase III will therefore use relapse-free cure, unfavorable outcome, culture conversion or lung function. The GDG (GRADE) would then rate certainty down for indirectness on the mortality benefit. A recommendation could be delayed, made conditional, or made only for subgroups (e.g., high-risk, HIV-negative, severe disease). The adoption probability and uptake given a "positive" trial are therefore lower than CG's "if it works → 60%."

MECHANISM: This lowers adult_uptake (conditional recommendations produce lower uptake). It may also lengthen years_to_adoption if the GDG requests additional evidence. It also means the mortality effect that drives all benefits is never directly verified, which raises the variance of the realized relative_reduction (Thread 1). The direction is downward on uptake. Quantification is uncertain: a conditional recommendation limited to a subgroup (e.g., a third of patients) would cut effective uptake by about half or more, but that scenario is speculative.

EVIDENCE: Logical and statistical argument (sample size calculation above, which depends on the 5% and 10% inputs). On GRADE, I believe indirectness from surrogate outcomes is a standard downgrading criterion in the WHO handbook for guideline development, but the Verifier should check the handbook text. The baseline mortality figure is UNGROUNDED and needs a source (WHO Global TB Report treatment-outcome data).

STRENGTH: MEDIUM. The logic is sound, but it depends on what the 10% parameter actually measures and what endpoints the planned Phase III uses.

NOVELTY CHECK: Not on the exclusion list. p_success = 0.40 captures "might not work." This critique is about a positive trial's evidence type being insufficient for a mortality-based recommendation and uptake, which is distinct from the effect failing to replicate.
```

```
CRITIQUE 3: Clinical eligibility and monitoring barriers cap the achievable prescribing share below the "generic and cheap" logic

HYPOTHESIS: TB treatment (isoniazid, rifampicin, pyrazinamide) is itself hepatotoxic, and anti-TB drug-induced liver injury occurs in a non-trivial minority of patients (commonly cited in the low single digits to ~10%, depending on setting and definition). Statins carry label warnings for active liver disease and transaminase elevation, and are historically avoided in pregnancy. Clinicians managing a TB patient with rising ALT will plausibly not want an additional agent that confounds attribution of DILI, and may stop it. Programs would likely require baseline and follow-up LFTs, which many NTP settings do not routinely perform for DS-TB. Also relevant are drug–drug interactions (rifampicin induction of CYP3A4; some protease-inhibitor-based ART raises atorvastatin exposure, while efavirenz lowers it) and pill-burden aversion. FDC regimens are valued precisely because they avoid extra pills.

MECHANISM: This reduces adult_uptake through (a) a smaller eligible population, (b) program reluctance, and (c) discontinuation. Inference-based illustrative arithmetic: excluding ~10–20% of adults for liver disease, DILI, pregnancy or women of reproductive age, polypharmacy and age, then applying a program-adoption factor, could move 0.60 to roughly 0.45–0.50 before adherence. This is my own illustrative scenario, not a sourced estimate. If LFT monitoring is mandated and not available, uptake could fall further, or monitoring costs (not in CG's cost) would be added.

EVIDENCE: Mixed. Statin labeling and CYP3A4 pharmacology are well-established. The Liverpool HIV/TB drug interaction resource is the right place to check specific ART interactions. Anti-TB DILI incidence ranges are in the literature but I cannot cite a specific paper. The specific exclusion shares are UNGROUNDED.

STRENGTH: MEDIUM. The mechanism is credible and the direction is clear. The magnitude is individually below materiality but is additive with Critiques 1 and 4.

NOVELTY CHECK: Not on the exclusion list. CG's "No monitoring requirements" is listed as a non-accounted item, and this critique quantifies its effect on the uptake ceiling.
```

```
CRITIQUE 4: Effective delivered dose and adherence diverge from trial conditions, and programmatic dose may be lower than the trial dose, notably with rifapentine regimens

HYPOTHESIS: The model applies a trial-derived effect to 60% of patients as if "prescribed" equals "treated at effective dose for the effective window." In programs, adjunct pills outside the FDC are self-administered and often unsupervised, and are less likely to be taken than anti-TB drugs, which are the patient's focus and may have DOT or digital adherence support. Statin adherence in general populations is known to be poor (a large fraction discontinue within a year in observational cohorts, though TB treatment is only 6 months and the motivating context differs). Trials measure adherence under research conditions with pill counts and supervision, so the real-world delivered dose and duration will be lower. In addition, the shift toward the 4-month rifapentine-containing regimen (HPMZ) matters because rifapentine is generally considered a strong CYP3A4 inducer, comparable to or stronger than rifampicin in some dosing contexts. That would further lower atorvastatin exposure in the very regimens programs are shifting toward, and shorten the treatment window over which a statin could be co-administered. Dose-finding in a Phase IIc is performed on one regimen (presumably rifampicin-based HRZE), so the dose selected may not carry over.

MECHANISM: Effective uptake equals prescribed share × adherence × the fraction achieving effective exposure. At 70% adherence, 0.60 becomes 0.42, about a 30% reduction. This is near the materiality threshold alone, and it compounds with Critiques 1 and 3. It also reduces relative_reduction in effectiveness (Thread 1) if there is a dose-response relationship. The rifapentine concern affects only the share of patients on HPMZ, which is currently small but growing. The direction is downward and the magnitude uncertain.

EVIDENCE: Logical argument plus general pharmacology (rifamycin induction of CYP3A4). I cannot identify a specific source on adherence to adjunctive non-TB drugs during TB treatment. The rifapentine/atorvastatin interaction magnitude is UNGROUNDED and needs checking (Liverpool interaction database, rifapentine label). The "70% adherence" figure is from the thread's materiality framing, not an empirical estimate.

STRENGTH: MEDIUM. The adherence-attenuation logic is general and strong; the specific numbers are uncertain.

NOVELTY CHECK: CG's lack of adherence modeling is listed as unaccounted for, not on the exclusion list. The dose-finding and rifampicin-limits-exposure points are on the exclusion list as stated. This critique does not re-argue them. What is new here is the mismatch between trial and programmatic delivery, and the rifapentine/HPMZ-regimen specifics.
```

```
CRITIQUE 5: Private-sector treatment share and the reach of national guidelines are not modeled

HYPOTHESIS: A large fraction of DS-TB treatment, especially in India, Indonesia, Pakistan and the Philippines, occurs in the private sector. Private providers frequently deviate from national standard treatment guidelines and may not use FDCs. Whether a WHO recommendation changes behavior there depends on professional societies, pharma marketing and mandatory notification, not on NTP procurement. Also, unnotified patients ("missing" cases, a large share in the same countries) never see the guideline. The relevant denominator for "60% of adult patients" is therefore a mix of settings with very different uptake dynamics.

MECHANISM: The effect on adult_uptake is ambiguous in sign. Private providers readily prescribe adjuncts and may adopt a cheap generic faster than NTPs, or even before guidelines (which would also reduce the counterfactual value of the trial). But dosing and duration there are unsupervised and non-standard, so effective exposure and benefit are lower. Net effect on the global average: probably a modest downward adjustment to effective uptake in the highest-burden countries, plausibly ~5–15% of the benefit. This is inference, not sourced. The sign could flip in specific countries.

EVIDENCE: WHO Global TB Reports contain country-level notification data and, I believe, India's Ni-kshay data show private-sector notifications of roughly a third of the total in recent years, but I cannot give exact figures. UNGROUNDED as to numbers. The claim that private-sector prescribing deviates from guidelines is widely discussed in the TB literature, but I cannot cite a specific paper.

STRENGTH: LOW-MEDIUM. The sign is ambiguous and the magnitude is probably below materiality alone.

NOVELTY CHECK: Not on the exclusion list. The constant treated-share assumption is excluded. This concerns the heterogeneity of adoption among treated patients by sector, not the share treated.
```

```
CRITIQUE 6: Zero modeled lag between Phase III completion and adoption, and a speedup that assumes trial timing is the binding constraint

HYPOTHESIS: The model treats years_to_adoption as equal to Phase III completion (8 years). Real-world chains include publication, WHO GDG convening and guideline development, national guideline revision, training, and GDF/Global Fund procurement cycles. For the 4-month HPMZ regimen, my recollection is that Study 31/A5349 published in 2021 and WHO guidance followed in 2022. The WHO step can therefore be short when a rapid-communication path is used. National adoption and procurement then took additional years. Separately, the 8-year timeline itself is exposed to execution risk. TB trials, particularly those run at multiple high-burden sites with a relapse endpoint requiring 12–24 months of follow-up, routinely slip. A generic drug also has no commercial sponsor, so Phase III funding could be a gating constraint, not the Phase IIc result. If so, a 1-year acceleration of the Phase IIc does not translate one-for-one into a 1-year earlier adoption.

MECHANISM: A longer years_to_adoption lowers eligible cases by ~2% per year under the current formula, which is not material alone (adding 3–5 years of lag lowers benefits by roughly 6–10%, more with discounting; see Thread 3). The larger concern is that expected speedup_years may be below 1 if the trial is not on the critical path. I note that lumpy decision cycles by themselves do not lower the expected speedup (if the timing is uniformly random, the expected shift equals the trial shift), so the case for a lower speedup rests on the trial not being the binding constraint, not on lumpiness.

EVIDENCE: Partly my recollection of the HPMZ timeline (verify). For Xpert, WHO endorsement was in 2010, and implementation took many years afterward (Albert et al., Cazabon et al. are the sources the thread names; I have not confirmed their specific findings). The Phase III funding-gap argument is a logical inference. Phase IIc registry timelines are not something I can cite.

STRENGTH: LOW-MEDIUM. The lag effect is individually immaterial; the possibility that the trial is not binding is more important but speculative.

NOVELTY CHECK: The 8-year assumption and the speedup assumption are both excluded as stated assumptions. This critique does not restate that they are assumptions. It points to the omitted downstream lag (adoption chain) and to the conditions under which the speedup would not transmit to adoption timing. If the Verifier judges the second point too close to the excluded speedup concern, treat only the lag point as in scope.
```

SUMMARY: The most important finding is that CG's 60% uptake is applied as a constant steady-state ceiling with no empirical support. Several independent haircuts compound: the precedent-based ceiling, clinical eligibility, adherence and delivered dose, and the endpoint problem for the GDG. Together they could plausibly bring effective uptake to ~0.30–0.40, at or below the materiality threshold of 0.39.

RECOMMENDED VERIFICATION PRIORITIES:
1. Critique 1 (precedents): get actual WHO and GDF coverage and uptake curves for Xpert, HPMZ and TBM dexamethasone, since they directly test the 60% ceiling.
2. Critique 4 (adherence and rifapentine induction): the 0.70 factor is close to material alone, and the CYP3A4 and rifapentine interaction magnitude should be checked.
3. Critique 2 (endpoint and GRADE): confirm what the 10% parameter refers to and what primary endpoint the planned Phase III would use. If it is mortality, the feasibility argument is strong.
4. Critiques 3, 5 and 6 are lower priority because they are individually sub-material, but the exclusion shares and private-sector shares need sourcing if they are carried forward.

**OUT OF SCOPE OBSERVATIONS**
- Pre-guideline off-label atorvastatin use in private sectors, driven by Phase II evidence, would erode the counterfactual value of the trial. This belongs with the counterfactual and speedup threads.
- Participation of lower-risk strata (HIV-negative, low baseline mortality) in the Phase III population may reduce the generalizability of the effect size to high-mortality programmatic populations. This belongs in Thread 1.

--- Thread: Who dies and how many healthy years are lost — ---

CRITIQUE 1: Survivors' excess mortality and comorbidity shrink the 27 DALYs per death

HYPOTHESIS: CG describes 27 as the "remaining healthy life expectancy" of a person who dies of TB. A person whose death is averted is not an average member of the population. TB patients carry high rates of smoking, alcohol use, diabetes, undernutrition, HIV and post-TB lung damage. Their expected remaining life after cure is therefore shorter than a general-population life table implies. If 27 comes from general-population or GBD-style life tables, it overstates the years gained per death averted.

MECHANISM: dalys_per_death falls. Illustrative calculation (my own inference, not from a source):
- Under Gompertz mortality, multiplying the hazard by a factor k is roughly equivalent to ageing by ln(k)/b years. For b ≈ 0.09–0.10 per year and an SMR of about 3, that is ln(3)/0.09 ≈ 11–12 years of effective ageing.
- For a patient aged about 40, remaining life expectancy in an LMIC life table is roughly low-to-mid 30s. For an effective age of about 52 it is mid-20s.
- That is a 20–30% reduction in remaining life expectancy. 27 would fall to roughly 19–22, which is near or below the 17.7 threshold once combined with any other downward adjustment.
- The shift is partly offset if 27 is already a healthy-life measure built from a TB-specific population. It is amplified if CG took general-population HALE and then applied it unadjusted.

EVIDENCE:
- Romanowski et al. 2019 (Lancet Infect Dis), a systematic review of long-term all-cause mortality after TB treatment. I recall a pooled SMR of roughly 3–4 versus general populations, but the exact figure needs verification.
- Gompertz scaling is a standard demographic approximation.
- The SMR is partly confounded by shared risk factors. That is exactly why the counterfactual years of an averted-death patient are lower than the population average.
- I cannot identify a source for how CG derived 27.

STRENGTH: MEDIUM-HIGH. It is a high-sensitivity parameter, and the logic is sound and probably crosses materiality. The size depends on how 27 was built, which is unknown.

NOVELTY CHECK: The thread lists "no adjustment for survivors' excess mortality" as something CG does not do. This critique goes beyond restating that. It gives a quantified mechanism and shows that the adjustment alone can take the parameter toward the threshold.

---

CRITIQUE 2: The 6% is a mix of deaths, and only a fraction is reachable and modifiable by atorvastatin

HYPOTHESIS: On-treatment deaths are concentrated early. Many occur in the first weeks, often in patients who are very sick, severely malnourished, or have advanced HIV, and some occur before or just after treatment initiation. A host-directed adjunct that takes time to reach effective exposure, and is further limited by rifampicin induction, cannot avert deaths that occur within days. Some deaths are also non-TB causes (HIV-related, cardiovascular, hepatic, or other). The "addressable" share of the 6% is therefore smaller than 6%.

MECHANISM: This is a decomposition of baseline_mortality into an effective baseline, addressable_mortality = 6% × (share of deaths occurring after statin could plausibly act) × (share TB-attributable and statin-responsive) × (share of the population eligible for statin).
- Illustrative only: if 30% of deaths are very early or in contraindicated or sicker-than-eligible groups, and 15% are non-TB causes, effective baseline is 6% × 0.7 × 0.85 ≈ 3.6%. That is below the 3.9% threshold.
- These shares are placeholders. I do not have verified values.

EVIDENCE:
- Waitt & Squire 2011 (IJTLD), a systematic review of risk factors for death during and after TB treatment. I believe it reports HIV, older age, and malnutrition as risk factors and that many deaths occur early, but details need verification.
- Country cohort studies (India, South Africa, Indonesia, Nigeria) on timing of death. I cannot cite specific ones.
- The rifampicin–atorvastatin interaction is pharmacologically established. Its effect on onset of benefit is an inference.

STRENGTH: MEDIUM. The logic is strong and the direction is clear. The magnitude depends on unsourced cohort timing data.

NOVELTY CHECK: This is adjacent to the "subgroups excluded or contraindicated" line in the thread. What is new here is the timing and cause-of-death filter, and its use to define an addressable baseline.

---

CRITIQUE 3: Under-ascertained deaths push true mortality up, and the direction is the opposite of Critiques 1–2

HYPOTHESIS: The 6% appears to come from the "died" category of WHO notified-cohort outcomes. That category excludes deaths among patients lost to follow-up (typically ~3–4% of the cohort), those "not evaluated" (a few percent), and deaths before treatment start or among transferred-out patients. It also excludes deaths among untreated or un-notified cases, who are unreachable for statin delivery but not for the all-in cost-effectiveness logic. If a meaningful share of LTFU and not-evaluated patients die, true on-treatment mortality among treated patients is above 6%.

MECHANISM: baseline_mortality rises.
- Illustrative arithmetic: if LTFU plus not-evaluated is about 6–7% of the cohort and 10–20% of them die, that adds roughly 0.6–1.4 percentage points. True mortality is then about 6.6–7.4%, which raises SROI by roughly 10–23% (proportional to mortality).
- The caveat is that the statin effect on those patients is uncertain, because they may not complete treatment.

EVIDENCE:
- The WHO Global TB Report outcome tables define treatment outcomes this way. I recall about 5–6% died, ~3–4% LTFU, and a few percent not evaluated, but the figures need checking.
- I believe tracing studies of patients lost to follow-up show materially elevated mortality, but I cannot identify a specific study. UNGROUNDED on magnitude.

STRENGTH: MEDIUM. The direction is well-founded, but the magnitude is unsourced and the reachability caveat is real.

NOVELTY CHECK: The thread lists this as something CG does not account for. This critique quantifies it and flags the interaction with reachability.

---

CRITIQUE 4: Covariance between mortality and DALYs per death means the product of means is not the mean of the product

HYPOTHESIS: baseline_mortality and dalys_per_death are applied as independent averages. In reality the subgroups with the highest mortality (older, comorbid, advanced disease) tend to have fewer remaining years. Groups with lower mortality are younger, with more years lost per death. The relevant quantity is the death-weighted mean DALYs, not the population mean. If 27 was derived without that weighting, the product 6% × 27 is biased. HIV-positive deaths push the other way, since they occur at younger ages and carry more DALYs per death.

MECHANISM: Illustrative arithmetic (my own, assumed numbers):
- Group A is 70% of patients, with 4% mortality and 35 DALYs per death. Group B is 30% of patients, with 12% mortality and 15 DALYs per death.
- Mean mortality is 6.4%. Death-weighted DALYs are (0.028×35 + 0.036×15)/0.064 ≈ 23.8, not 27.
- Expected DALYs per treated patient is 1.52, versus 6.4% × 27 = 1.73 if the population-average 27 is used. That is about 12% lower.
- The effect could be near zero or reversed if HIV+ deaths dominate in high-HIV deployment settings.
- Conclusion: the net effect on SROI is uncertain in sign but plausibly −10 to −15% in low-HIV settings.

EVIDENCE:
- GBD 2021 TB deaths and YLLs by age, country and HIV status could be used to compute death-weighted YLL per death. I have not run this, and it needs verification.
- The structure of the bias is a logical argument.
- The group numbers above are illustrative, not sourced.

STRENGTH: MEDIUM-LOW. The mechanism is valid, but it depends on how 27 was derived and on unsourced subgroup values.

NOVELTY CHECK: This is not on the exclusion list. The thread's "no age weighting" point is about averages. This critique is about the interaction between the two parameters.

---

CRITIQUE 5: A global-average mortality may not match the countries where an atorvastatin adjunct would actually be deployed

HYPOTHESIS: baseline_mortality is a single global figure, but on-treatment mortality varies a lot by country, mainly through HIV prevalence, age mix, and diagnostic delay. The Phase III trials and eventual uptake would concentrate in a handful of high-burden countries (e.g., India, South Africa, Indonesia, Nigeria, Philippines). If deployment is weighted toward lower-mortality settings, the 6% overstates. If weighted toward high-HIV settings, it understates and the DALYs per death shift too.

MECHANISM: baseline_mortality becomes a case-weighted average over deployment countries rather than the global figure. If India (a large share of cases) has on-treatment death near 4–5% and South Africa near 8–10% (both from memory, UNVERIFIED), the weighted mean depends heavily on the deployment mix. A mix dominated by India could bring the figure to about 4.5%, still above the 3.9% threshold. A mix dominated by high-HIV countries would exceed 6%. This is a sensitivity issue rather than a clear bias.

EVIDENCE:
- WHO Global TB Report country-level outcome data for the 2021 or 2022 cohorts.
- GBD country-level TB deaths and YLLs.
- I cannot cite country-specific figures with confidence. UNGROUNDED.

STRENGTH: LOW-MEDIUM. It is a plausible heterogeneity concern, but the direction is ambiguous and I have no verified numbers.

NOVELTY CHECK: This is not on the exclusion list. It is distinct from the "constant treated share" and "96% DS share" assumptions, which concern the case base rather than the mortality rate.

---

OUT OF SCOPE OBSERVATIONS: Whether the statin mortality effect applies uniformly across the mortality categories is a clinical-effect question and belongs to another thread. The rifampicin–atorvastatin pharmacokinetic interaction is on the exclusion list in its dose-finding form.

SUMMARY: The most important finding is that the 27 DALYs per death is likely overstated for the actual statin-eligible, comorbid population. An SMR-based adjustment alone could plausibly take it to about 19–22, near the 17.7 threshold. The 6% baseline has offsetting biases: addressable mortality is likely lower, while true mortality including unascertained deaths is likely higher.

RECOMMENDED VERIFICATION PRIORITIES:
1. Critique 1. Verify the Romanowski SMR value and, critically, how CG derived 27 (general life table vs HALE vs TB-specific). This is the highest-leverage, materiality-crossing item.
2. Critique 2. Source the timing-of-death distribution and cause-of-death split from published cohorts.
3. Critique 3. Verify the WHO outcome percentages and find a tracing-study estimate of mortality among LTFU.
4. Critiques 4 and 5 can be tested by computing death-weighted YLL per death from GBD by age, HIV status and country.

--- Thread: Probability of success (p_success) — base rates and the ---

# Thread: p_success, base rates and the definition of "success"

These critiques stay within the thread scope. I do not re-raise "40% is subjective" or "effects might not replicate" in general terms. Figures from memory are labelled as such. The Verifier should check them before they count.

---

## CRITIQUE 1: Industry phase-transition base rates put "II and III both succeed" at roughly 15–25%, so 40% requires an unstated premium of about 1.6–2.7×

**HYPOTHESIS:** CG names no reference class for 40%. The best-known class is industry phase-transition data. From memory, BIO/Informa/QLS (2021, covering 2011–2020) report about 29% for Phase II→III, about 58% for Phase III→NDA/BLA, and about 91% for filing→approval. Wong, Siah & Lo (2019, *Biostatistics*) give similar overall figures, with infectious-disease or anti-infective programs doing better than average. On these numbers, P(II and III both succeed) is about 0.29 × 0.58 ≈ 17%, and P(II→approval) is about 15%. Even generously uplifted for infectious disease (say Phase II ~37–40% and Phase III ~65%), the product is about 24–26%. That is at or below the 0.26 break-even. To justify 40%, CG needs a premium of roughly 1.6× over the infectious-disease-adjusted rate, or about 2.4× over the all-indication rate. The model never states or defends that premium.

**MECHANISM:** p_success enters linearly. A move from 0.40 to 0.20–0.25 cuts expected cost-effectiveness by 37–50%. This crosses the 0.26 threshold, below which SROI falls under the bar. A proposed decomposition, with the reasoning shown:
- P(IIc success) ≈ 0.5. This is higher than the 29–40% industry Phase II rate because a PK/dose-selection Phase IIc is easier to "pass".
- P(III | IIc) ≈ 0.40–0.55, adjusted for infectious disease and repurposing but not for the TB-specific track record (Critique 2).
- P(adopted | III) ≈ 0.7–0.85 (Critique 4).
- Product ≈ 0.14–0.30, with a central value of about 0.20.

This decomposition is my own inference, not from a source.

**EVIDENCE:** Published industry datasets (BIO/Informa/QLS 2021; Wong, Siah & Lo 2019). Figures are from memory and should be verified, especially the infectious-disease-specific rates. A counter-argument CG could make is that repurposed or generic drugs have known safety, which lifts Phase I and II transition rates. I believe the literature supports some premium, but I cannot cite a specific source for the size of a repurposing premium. That is UNGROUNDED. The premium mostly applies to safety attrition, whereas the dominant failure mode in Phase II/III is lack of efficacy, which repurposing does not help.

**STRENGTH:** HIGH. The dataset is published and the parameter is high-sensitivity. The ±0.10 move is above the materiality threshold, and the central estimate sits at the break-even point.

**NOVELTY CHECK:** Not on the exclusion list. "40% is subjective" is excluded. This critique is about the numeric mismatch with a specific reference class and the missing decomposition.

---

## CRITIQUE 2: The TB-specific reference classes (host-directed therapy, adjunctives, regimen-shortening) have a much worse record than 40%

**HYPOTHESIS:** The relevant class is not "drugs" but "TB host-directed or adjunctive therapies, and TB treatment-shortening strategies promoted on animal or early-phase surrogate data". To my knowledge this class has a poor Phase III record.
- **Vitamin D.** Trials in Guinea-Bissau (Wejse et al., 2009) and London (Martineau et al., 2011) showed no mortality or overall culture-conversion benefit. I am fairly confident of this but have not checked details.
- **Fluoroquinolone 4-month regimens.** REMoxTB, OFLOTUB and RIFAQUIN failed non-inferiority in Phase III despite encouraging mouse and Phase II (culture-conversion) data. This is the closest analogue to "promising preclinical plus Phase II surrogate → Phase III".
- **Dexamethasone in HIV-associated TB meningitis.** The ACT HIV trial (2023) was, as I recall, null on survival. This is a case where an adjunctive anti-inflammatory looked effective in an earlier trial population and did not generalize.
- **Corticosteroids.** These are the counter-example: benefit in TB meningitis (Thwaites 2004) and pericarditis, and they were adopted. They are the one clear success of the class.
- **Other HDTs.** Statins, metformin and others have mostly mouse and observational support. To my knowledge no HDT is WHO-recommended for drug-sensitive pulmonary TB. Reviews such as Wallis & Hafner and Kolloli & Subbian describe a pipeline that is mostly preclinical or small Phase II.
- **Statin preclinical data.** Mouse data for pravastatin (Parihar and colleagues, Karakousis group) are promising. Observational human data (statin use and lower TB risk) are subject to healthy-user bias.

A success rate for this class of well under 40% from Phase II onward looks plausible, perhaps 10–20%. However, Study 31/A5349 (rifapentine-moxifloxacin 4-month regimen) succeeded and was adopted, so the class is not zero.

**MECHANISM:** Using the TB-class prior in place of the generic one gives p_success of roughly 0.10–0.25 (my inference). At 0.15, cost-effectiveness is about 38% of the CG base case, well below the bar. Even a blend of the TB-class and industry priors gives p_success ≈ 0.2–0.3.

**EVIDENCE:** The cited trials are real as far as I recall, but exact results and endpoints need Verifier checking. The class-level success rate is my inference, not a published number. I cannot cite a systematic review giving a "HDT success rate for TB". UNGROUNDED as a quantitative rate.

**STRENGTH:** MEDIUM-HIGH. The qualitative record is well known, but the reference-class membership and the quantitative base rate are arguable. A proponent would say a statin is a different mechanism (pharmacokinetically more tractable, with a human safety record) and that the fluoroquinolone failures are mismatched analogues.

**NOVELTY CHECK:** Distinct from the excluded "might not replicate". This identifies a specific reference class with a specific track record and asks whether 40% sits above or below it. It does not argue about replicability in the abstract.

---

## CRITIQUE 3: "Success" probably means a surrogate or composite endpoint, but the model needs a 10% mortality reduction, so P(adopted AND 10% mortality benefit) < P(trials succeed)

**HYPOTHESIS:** CG's p_success is defined as "Phase II and III both succeed", and the benefit is a 10% relative mortality reduction. A Phase III TB trial cannot realistically be powered to show a 10% relative mortality reduction.

A power calculation with reasoning shown (my own arithmetic):
- Assume baseline trial-population mortality of about 4% (programmatic mortality in DS-TB is of similar order, maybe 4–6%).
- A 10% relative reduction is 0.4 percentage points (4.0% → 3.6%).
- Using n ≈ (1.96 + 0.84)² × [p₁q₁ + p₂q₂] / d², n ≈ 7.84 × 0.0731 / (0.004)² ≈ 36,000 per arm, about 70,000 in total.
- Even at 6% baseline mortality, this is still tens of thousands per arm.

Standard TB Phase III trials enroll hundreds to a few thousand and use composite "unfavorable outcome", relapse or culture-conversion endpoints. So "Phase III success" will almost certainly be declared on a surrogate or composite endpoint. The 10% mortality figure is then an extrapolation never directly tested. P(trials succeed) overstates P(adopted AND mortality benefit ≥ 10%). The mortality benefit conditional on surrogate success is uncertain and could be much smaller.

**MECHANISM:** The model effectively computes p_success × uptake × 10% × deaths. The coherent quantity is P(trials succeed on surrogate) × P(adopted | success) × E[mortality reduction | surrogate success, adoption]. If E[RR | surrogate success] is 5–7% rather than 10%, benefit falls 30–50%, compounding with any p_success revision. The magnitude depends on the surrogate-to-mortality relationship, which is uncertain, so it needs a sensitivity analysis. Also note that if success needs a 10% mortality effect to be real, the true probability is lower still. Unless the success definition is aligned with the 10%, the two parameters cannot both be right.

**EVIDENCE:** Logical and arithmetic argument, based on standard sample-size mathematics. The baseline mortality is an assumption, so the Verifier should check typical DS-TB trial mortality rates and the primary endpoints of recent Phase III trials such as Study 31, REMoxTB and TRUNCATE-TB. The surrogate-to-mortality relationship for TB adjuncts is UNGROUNDED here.

**STRENGTH:** HIGH on the logical structure. MEDIUM on magnitude, because the mechanism by which the statin yields 10% mortality is not specified in the material I was given. If CG's 10% comes from a treatment-shortening or anti-inflammatory mechanism, the surrogate link may be reasonably good.

**NOVELTY CHECK:** "10% is an assumption" is excluded. This critique is about the incoherence between the definition of success and the benefit parameter, not the assumption itself. It is the Thread 1 coordination point and should be reconciled there.

---

## CRITIQUE 4: P(adoption | Phase III success) and P(Phase III gets funded and run | Phase IIc success) are missing, and the 60% uptake factor may not cover them

**HYPOTHESIS:** CG's chain has no explicit step for (a) WHO guideline adoption after a positive Phase III, or (b) securing the Phase III itself. Both are especially fragile for a generic repurposed drug.

On (a), WHO recommendations require a GRADE evidence review. A surrogate-based trial with low-certainty mortality evidence might yield a conditional recommendation or none. Guideline timing also adds delay, and the model already assumes 8 years to Phase III completion. The 60% uptake figure appears to be about country-level implementation after adoption. If so, adoption is still not captured. If instead 60% blends adoption and uptake, it should be disclosed.

On (b), a generic has no commercial sponsor with a registration incentive. In industry data, many Phase II→III failures are strategic or funding exits, but for generics the funding risk is arguably greater. CG's $7M includes later trials, which assumes funding is secured with certainty. Yet p_success only covers scientific success, not the probability that someone pays for Phase III. If CG itself would fund Phase III, that is a commitment that needs to be modeled as cost conditional on IIc success. If CG would not, then another funder must be found with some probability below 1.

**MECHANISM:** If P(adopted | III success) is 0.75–0.85, p_success_effective falls from 0.40 to 0.30–0.34, reducing cost-effectiveness by 15–25% (simple multiplication). If P(Phase III funded | IIc success) is also below 1 (say 0.8), the combined reduction is larger and takes the base case close to the 0.26 threshold. This depends on how CG's 60% was derived. If the 60% already embeds adoption, this critique mostly collapses to a documentation concern.

**EVIDENCE:** Logical argument. The GRADE and WHO guideline process is institutional knowledge. I cannot cite a specific source for adoption probabilities after positive trials, and the numbers above are inference. UNGROUNDED quantitatively. The Verifier should check how CG derived the 60% and what it covers.

**STRENGTH:** MEDIUM. The structural gap is real, but the size depends on what CG's uptake figure encodes.

**NOVELTY CHECK:** "60% uptake is assumed" is excluded. This critique is not about whether 60% is reasonable. It is about a separate, unmodeled probability factor, adoption given success, and the funding probability for later trials.

---

## CRITIQUE 5: Phase IIc "success" is a weak gate. If it is defined by PK or dose selection, it passes easily and transmits little information, so the probability of the whole chain should be weighted toward Phase III

**HYPOTHESIS:** The one-stage framing "40% that II and III both succeed" masks that the two stages carry very different risk. If the Phase IIc is chiefly dose-finding or PK/safety, as the exclusion list implies, then P(IIc success) is high (0.6–0.8). This is not strictly a probability of efficacy, and "success" at this stage may only mean "a tolerable dose with acceptable exposure was found". Industry Phase II rates of ~29% reflect proof-of-efficacy trials. A dose-finding IIc therefore does not de-risk Phase III the way a proof-of-concept Phase II would, and it may even produce an optimistic dose or a surrogate signal that Phase III later fails to confirm. REMoxTB-type experience, where Phase II culture-conversion signals did not translate, is relevant here (see Critique 2).

Implication: the 40% cannot be sanity-checked against Phase II→approval statistics without first defining the IIc endpoint. If IIc is easy and Phase III is the real hurdle, the realistic product is P(IIc) ≈ 0.7 × P(III | weak signal) ≈ 0.3 ≈ 0.21 (illustrative inference), again at or below the break-even.

**MECHANISM:** The same linear effect on p_success as in Critique 1, but with a different decomposition: the Phase III failure rate becomes the focus and the Phase IIc contributes little. This also affects the joint distribution of p_success and relative_reduction. A weak gate lets through a dose that may be too low for efficacy, which correlates a lower effect size with Phase III failure. If the true effect is below 10%, Phase III is also less likely to succeed. So modelling p_success and RR as independent point values can mislead. The expected value of the product E[p × RR] is not p × E[RR] when both depend on the true effect. The direction is ambiguous. Conditional on Phase III success, winner's curse suggests the realized effect on the endpoint is smaller than the 10% planning value. Conversely, successful trials select for larger true effects. A simple scenario analysis with a prior over true effect sizes would show which dominates.

**EVIDENCE:** Logical and theoretical argument, plus general knowledge about Phase IIc design. Direct evidence on how this specific Phase IIc defines success is UNGROUNDED here. The Verifier should check the trial protocol and the CG grant rationale.

**STRENGTH:** LOW-MEDIUM. This is a structural point whose numerical impact depends on details of the trial design I do not have.

**NOVELTY CHECK:** The excluded "need for dose-finding" concerns the purpose of IIc. This critique is about its implication for the probability model: a dose-finding trial is a weak filter on p_success and induces dependence between p_success and effect size. It does not re-raise the dose-finding need itself. It is adjacent to the rifampicin interaction point (which is new but belongs to another thread), and I do not develop that here.

---

**OUT OF SCOPE OBSERVATIONS:**
- The rifampicin-statin pharmacokinetic interaction may structurally cap programmatic exposure. This affects relative_reduction, not p_success.
- The 10% effect applied to all TB deaths (including HIV-TB and DR-TB, which are not in the DS-TB 96% share) may overstate coverage. This is another thread's concern.

---

**SUMMARY:** CG's 40% for "Phase II and III both succeed" sits well above the generic industry rate (~15–17%), above an infectious-disease-adjusted rate (~24–26%), and above any reasonable TB host-directed-therapy class estimate. The mortality-definition problem (Critique 3) and the missing adoption and funding steps (Critique 4) pull the effective probability of "adopted AND 10% mortality benefit" lower still. A decomposed central estimate of about 0.20 (range 0.14–0.30) is at or below the 0.26 threshold.

**RECOMMENDED VERIFICATION PRIORITIES:**
1. **Critique 1.** Verify the exact BIO/Informa/QLS 2021 and Wong et al. 2019 transition rates, particularly the infectious-disease-specific rates. This is the quantitative anchor for the whole thread and is easy to verify.
2. **Critique 3.** Verify typical primary endpoints and mortality rates in recent TB Phase III trials, and what CG's "success" means. The sample-size argument is strong if baseline mortality is as assumed. Coordinate with Thread 1.
3. **Critique 2.** Verify the specific trial outcomes (vitamin D, REMoxTB/OFLOTUB/RIFAQUIN, ACT HIV, Study 31) and whether any HDT has been WHO-adopted for DS-TB. The reference-class claim fails if analogues are mismatched.
4. **Critique 4.** Check what CG's 60% uptake covers. If it includes adoption, this critique mostly drops out.

--- Thread: Eligible population and the future TB landscape ---

# Candidate critiques: eligible population and the future TB landscape

**Reconstruction check (part a).** I could not identify CG's actual inputs, so this is my inference.
- 7.5M (2022 notifications) × 0.96 (DS) × 0.98^8 (0.851) × ~0.90 (adult) ≈ 5.5M. This reproduces the figure cleanly.
- 8.0M × 0.96 × 0.851 × 0.90 ≈ 5.9M. An adult share of ~0.84 would be needed to get 5.5M from an 8.0M baseline, which looks too low.
- So CG most likely used ~7.5M as the baseline, with a ~90% adult share. The Verifier should confirm this against the CEA.
- I believe WHO reported ~7.5M notifications for 2022 and ~8.2M for 2023, but I cannot cite exact figures.

---

CRITIQUE 1: Baseline year is stale and the 5.5M figure is sensitive to it

HYPOTHESIS: If CG anchored on 2022 notifications (~7.5M), that was a post-COVID recovery year. WHO's later reports show notifications continuing to rise (~8.2M in 2023). The "8 years of decline" is then applied from a baseline that is already out of date. The thread notes there is no sensitivity analysis on baseline year.

MECHANISM: Moving the baseline from 7.5M to ~8.2–8.3M raises eligible_people_at_8y by ~9–11%, from ~5.5M to ~6.0–6.1M. Taken alone this is below the ±25% materiality bar. It is an upward, non-material correction. It matters mainly because it stacks with Critique 2.

EVIDENCE: Logical argument plus my recollection of WHO Global TB Reports (2023 and 2024 editions). I cannot give exact figures. This is a reconstruction concern and would need verification against the WHO reports.

STRENGTH: LOW (real but not material alone).

NOVELTY CHECK: The exclusion list covers the 2% decline and the constant treated share as assumptions. This concerns the choice of anchor year, which the thread lists as unaccounted for. It does not restate those assumptions.

---

CRITIQUE 2: A 2%/yr decline in notified case counts probably contradicts the observed trend; incidence rates fall slowly while counts do not

HYPOTHESIS: WHO's headline declines are in incidence *rates* per 100,000 (about 1–2%/yr in good pre-COVID years). Absolute case counts depend on population growth, which is large in the highest-burden countries (India, Nigeria, DRC, Pakistan, Philippines, Indonesia). Notified cases also reflect closing detection gaps (roughly 25% of incident cases are not notified), and WHO and national programmes are pushing active case-finding. If rate declines are roughly offset by population growth, absolute incident cases are roughly flat. If detection keeps improving, notifications could rise. CG applies a 2% annual decline to the count of cases. That is plausibly a different quantity from the one WHO reports as declining.

MECHANISM: Scenario using my own arithmetic:
- Baseline 8.2M, flat for 8 years, × 0.96 × 0.90 → ~7.1M, about +29% versus 5.5M.
- A mild rise (+1%/yr) would give ~7.7M.
- A downside shock, such as the 2025 funding disruptions to TB programmes, could cut notifications. I cannot ground the size of that effect.

The 2%/yr figure therefore looks conservative for counts, and the error is probably in the upward direction (eligible ≈ 6.5–7.7M). Combined with Critique 1, this likely crosses the >25% threshold, but in the direction that improves cost-effectiveness.

EVIDENCE: WHO Global TB Report trends, which I recall showing global incident cases of ~10–11M and roughly flat in absolute terms since ~2015, with the rate falling ~8% over 2015–2023. I cannot cite exact values. Population growth is a logical argument. UNGROUNDED on specific numbers; needs verification.

STRENGTH: MEDIUM. The direction is plausible and the magnitude may exceed the bar, but the numbers need verification.

NOVELTY CHECK: The exclusion list says the 2% decline and the constant treated share are explicit assumptions and that restating them is not a finding. This critique argues something different: the decline is applied to notification counts, whereas the evidence concerns rates. It also argues that the empirical sign of the error is an *understatement* of eligible population.

---

CRITIQUE 3: "Adult DS notified" is not "eligible for the trial label": missing applicability filters

HYPOTHESIS: The 5.5M appears to be adults with drug-susceptible TB, but a statin adjunct would likely be indicated only for a subset.
- **Extrapulmonary TB** is ~15% of notified cases. If the proposed mechanism and outcomes (culture conversion, relapse, lung pathology) are pulmonary, these patients are outside the evidence.
- **Clinically diagnosed (not bacteriologically confirmed) cases** are ~35–40% of notifications globally. These patients lack culture endpoints, and some may not have TB.
- **Exclusions typical of a statin trial:** HIV coinfection (~6–8% of cases; ART interactions), pregnancy, hepatic disease, existing statin use, and drug-interaction contraindications.
- **Isoniazid-resistant, rifampicin-susceptible TB** (Hr-TB, ~7% of cases) is classified as "DS" in some schemas but is treated with a different regimen. The 96% share may overstate trial-regimen-eligible patients.

MECHANISM: Illustrative stack from my own multiplication:
- Pulmonary only: ×0.85 → ~4.7M.
- Add other filters (HIV, pregnancy, hepatic, Hr-TB), ×~0.85 → ~4.0M.
- Restrict to bacteriologically confirmed cases (×~0.62): ~2.5M.

Stacked with an overly conservative decline (Critique 2), this could net out to roughly the current figure. The filters should be modelled explicitly rather than implicitly. Applied alone and fully, they could push eligible below the 3.6M bar.

EVIDENCE: WHO Global TB Report for extrapulmonary share (~15–16%), bacteriological confirmation (~60–65%), and TB-HIV share. These are my recollections and should be verified. The statin exclusion list is my own inference from standard trial design and statin labelling, not from any specific protocol. Which filters apply depends on the trial design, which I have not seen.

STRENGTH: MEDIUM. The magnitude could be material, but the filters are my inference about trial eligibility rather than documented parameters.

NOVELTY CHECK: The exclusion list covers DS share and the adult assumption only as stated assumptions. This concerns additional, unmodelled eligibility filters. The thread notes the adult definition, and my pediatric point is subsumed here.

---

CRITIQUE 4: Shorter and new regimens erode both the eligible population and the incremental benefit

HYPOTHESIS: By ~2033, a meaningful share of DS-TB patients may be on regimens other than the 6-month HRZE the trial tests.
- WHO (2022) recommended a 4-month rifapentine–moxifloxacin regimen (HPMZ, from Study 31/A5349, Dorman et al., NEJM 2021) for people aged 12 and over.
- Other pipeline options include TRUNCATE-TB-type strategies (Paton et al., NEJM 2023, from my recollection) and bedaquiline-containing short regimens.

Consequences:
1. **Applicability:** a statin trial on HRZE does not establish efficacy on a rifapentine- or moxifloxacin-based backbone. Rifapentine is a stronger CYP3A4 inducer than rifampicin, so the interaction problem may worsen. Re-trialing on new backbones would add cost and time that the model may not count.
2. **Incremental value:** shorter, more potent regimens may lower baseline relapse and mortality. This leaves less room for an adjunct to add benefit, if the benefit is defined relative to standard-regimen outcomes.
3. **Mechanism:** if the statin's value is in shortening treatment, a 4-month regimen leaves less to shorten.

MECHANISM: If 20–40% of eligible patients are on non-trial regimens at the benefit horizon, effective eligible falls ~20–40%, from 5.5M to ~3.3–4.4M. That is at or near the 3.6M bar. If the effect size also shrinks on newer backbones, the effect compounds. The 20–40% adoption range is my own scenario and is not grounded in published projections. Programme uptake of HPMZ has so far been slow because of rifapentine supply and cost, so the low end is more likely than the high end.

EVIDENCE: Dorman et al. (NEJM 2021) and WHO 2022 guidance exist. The adoption forecast is UNGROUNDED, so this is an inference. The interaction claim for rifapentine and atorvastatin is pharmacological reasoning, not a cited study.

STRENGTH: MEDIUM. It is plausible and potentially at the materiality bar, but the key quantity (regimen share in 2033) is speculative.

NOVELTY CHECK: The exclusion list covers rifampicin-limited exposure and dose-finding. This critique is about regimen *change* narrowing applicability and diluting incremental value, which is not on the list.

---

CRITIQUE 5: M72/AS01E and other incidence shocks are likely not large enough by year 8–10, but should be modelled

HYPOTHESIS: The Phase III of M72/AS01E (started 2024, ~20,000 participants, results expected late 2020s from my recollection of Gates MRI materials) follows a Phase IIb (Tait et al., NEJM 2019) that reported ~50% efficacy against progression to pulmonary TB in already-infected adults. If Phase III succeeds, licensure could come ~2028–30, with rollout starting thereafter.

The 30–50% incidence reduction that would be material is unlikely by 2033–35:
- Rollout is slow. Adolescent and adult programmes need Gavi financing and new delivery platforms.
- Vaccine impact accrues gradually, mostly by preventing progression in already-infected people.

My own estimate is a 5–15% reduction in incidence by 2033–35, which on its own would not cross the threshold. LSHTM-type models (e.g. Harris et al.) project larger impacts mostly in the 2040s. I cannot cite a specific figure from them.

The vaccine effect matters more over the *benefit horizon*. If atorvastatin benefit accrues across many years after adoption, a vaccine could reduce the eligible pool by 30–50% in the later years. CG's constant 5.5M "eligible at 8y" ignores the downward trajectory after that point.

MECHANISM: Effect on eligible at year 8: –5 to –15%, i.e. ~4.7–5.2M. If the benefit horizon extends beyond ~15 years, average eligible over that horizon could be ~20–35% lower, depending on how the horizon is modelled. I cannot determine this without seeing how the CEA treats post-adoption years (**magnitude uncertain, requires CEA sensitivity analysis**). The probability of vaccine success should be weighted separately (the Phase IIb efficacy estimate was in a small, selected population).

EVIDENCE: Tait et al. (NEJM 2019) for the Phase IIb. The Phase III timeline is from my recollection of Gates MRI. The modelling is a general recollection that I cannot cite precisely. UNGROUNDED on the specific impact numbers.

STRENGTH: LOW–MEDIUM. It is directionally sound, but its materiality depends on how the model treats years after adoption. It is not material for the year-8 snapshot alone.

NOVELTY CHECK: The thread already lists the vaccine as an unmodelled factor. The new element is the argument that the timing lag likely keeps the year-8 effect below the bar, and that the real exposure is the post-adoption horizon.

---

SUMMARY: The 5.5M figure reproduces (likely 7.5M × 0.96 × 0.98⁸ × ~0.90), but it mixes two errors that push in opposite directions. The 2% decline on case counts probably understates future eligible cases (Critiques 1–2, up to ~+30%), while omitted applicability filters and regimen change could lower effective eligible by a similar or larger amount (Critiques 3–4). The net effect is uncertain and may cross ±25% either way. A vaccine is unlikely to be material at year 8 but matters for the post-adoption horizon.

RECOMMENDED VERIFICATION PRIORITIES:
1. **Critique 2.** Check WHO trend data on absolute incident cases and notifications against the rate decline. This is the highest-leverage empirical check, and it decides the sign.
2. **Critique 3.** Verify the extrapulmonary, bacteriological-confirmation, and HIV shares in WHO reports. Check the trial's eligibility criteria to see which filters actually apply.
3. **Critique 4.** Verify the status of HPMZ and other short-regimen adoption, and check whether any WHO or industry forecast of regimen share exists.
4. **Critique 5.** Confirm the Phase III timeline and find published model-based vaccine impact projections for 2033–35, then check how the CEA treats the post-adoption horizon.

**OUT OF SCOPE OBSERVATIONS:** The CEA applies the eligible population at a single point (year 8) but benefits accrue over the following years. How the model treats that horizon is a structural question for another thread. Note also that effects of new regimens on the 10% effect size and p_success belong with the efficacy thread.