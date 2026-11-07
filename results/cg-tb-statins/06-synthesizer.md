# Red Team Report: Adjunctive Atorvastatin for Drug-Susceptible TB (CG R&D Grant: Phase IIc → Phase III → Adoption)

## Pipeline Summary

- Investigation threads examined: 8
- Candidate critiques generated: 41
- Verified critiques: 36
- Rejected by verifier: 5
- Judged immaterial by quantifier (not debated): 1
- Critiques surviving adversarial review: 35
- Dependencies identified: 10
- Signal rate: 35/41

## How to Read This Report

This report classifies findings by the surviving strength a neutral judge
assigned after reviewing each Advocate/Challenger debate. The three levels
mean:

- **STRONG** — The Challenger made grounded arguments the Advocate could
  not adequately defend. The critique identifies a real gap in the CEA
  that warrants direct attention.

- **MODERATE** — Both sides made some grounded arguments, and the
  substantive question remains open. The critique identifies a real
  concern but the evidence doesn't yet settle how to adjust.

- **WEAK** — The debate was dominated by reasoning failures (unsupported
  estimates, strawmanning, whataboutism, or similar) on one or both
  sides. The critique may still be valid, but this particular debate
  did not establish it. Weak findings are preserved in this report
  because the underlying claim may deserve a better-argued examination
  later.

The Debate Quality Audit section further below quantifies the reasoning
failure modes detected across all debates. Readers who want to assess
the calibration of these labels should start there.

*Context for all impact figures:* the executed baseline is about 3,055x SROI, and the decision bar is about 2,000x. A finding therefore crosses the bar on its own only if it cuts SROI by about 35% or more. All percentages below come from the pipeline's executed sensitivity runs on the CG BOTEC.

## Critical Findings (surviving strength: STRONG)

(none: no finding reached STRONG in this run)

## Significant Findings (surviving strength: MODERATE)

Findings are ranked by the magnitude of the executed central-case change in SROI.

### Finding 1: The speedup benefit and the all-in cost come from different counterfactuals. Every coherent framing gives roughly 10–20x higher SROI.
**Impact:** This finding raises SROI. At the quantifier's central speedup-equivalent of 5 years, SROI rises to about 15,300x (+400%), with an executed range of −50% to +1,400%. The judge would report only about a 3–5× uplift, conditional on a 5–10 year horizon and low delivery costs.
**Evidence:** There is no external evidence. The finding is an internal-consistency argument: the BOTEC pairs one year of plateau benefit (a delay-world numerator) with the full ~$7M pathway cost (a never-world denominator).
**Core claim:** Under every coherent counterfactual the ratio equals PV_B/PV_C, so the BOTEC understates SROI by roughly 10–20×. (LOGIC ONLY)
**GiveWell's best defense:** All-in benefit against all-in cost is a deliberate shared-credit convention. CG takes about 4.5% of the benefit against about 4.5% of the cost, which keeps funders' credit claims from summing to more than 100%.
**Why it survives:** Shared credit only works if the numerator is the whole pathway's benefit, and here it is one year of acceleration. The judge noted that if displaced funding is valued at CG's own bar, the delay branch could fall to or below the BOTEC figure. The direction is therefore branch-dependent rather than settled.
**Recommended action:** Present SROI conditionally. The delay branch should be one year of benefit against the incremental cost. The never branch should be the full discounted stream against the full pathway cost plus delivery. Drop the 30,000–55,000x figure. Check generic atorvastatin and monitoring prices against the ~$3.3 per-patient never-branch breakeven.
**Key unresolved question:** Is the realistic counterfactual for this pathway "delayed" or "never", and at what rate should other funders' displaced dollars be charged?

### Finding 2: Reference-class check: TB Phase III trials, and the evidence package WHO may require, point to more than one trial
**Impact:** Raising all_in_cost to a central $20M cuts SROI to about 1,069x (−65%). At $40M the cut is −82%.
**Evidence:** TB-PRACTECAL cost €33.9M (€61,460 per patient, hospital-based DR-TB), and the median pivotal trial costs about $19M (not TB-specific). Both probably overstate cost for an oral DS-TB adjunct. The NCT05575518 per-site figure implies roughly $660 per patient. At that rate a ~47,000-person mortality-powered trial would cost about $31M, while a surrogate-powered trial of a few thousand would cost well under $7M.
**Core claim:** A Phase III trial for this intervention would plausibly cost well above $7M, in the range $20–60M. (SUPPORTED)
**GiveWell's best defense:** The $7M is explicitly all-in. The 40% p_success also partly prices in cost risk, because failed programs stop before the full Phase III spend.
**Why it survives:** The Advocate concedes that the components are included. The dispute is whether the amount is adequate, and the early-stopping offset does not apply to the success worlds that generate all the benefit.
**Recommended action:** Extract per-participant cost from NCT05575518 and confirm whether £226,734 covers all 436 patients. Then obtain CG's intended Phase III endpoint. The judge's interim view, at moderate confidence, is that $7M is consistent only with a pragmatic or surrogate design.
**Key unresolved question:** Is the Phase III powered on mortality or on a surrogate/composite endpoint? This determines which horn of the cost-versus-effect dilemma applies (see Meta-Observations).

### Finding 3: A $7M Phase III cannot be powered on mortality, and the CEA's benefit is mortality only
**Impact:** Raising all_in_cost to a central $16M cuts SROI to about 1,337x (−56%). At $50M the cut is −86%. The decision-relevant threshold is an all-in cost of about $9.3M.
**Evidence:** Phase II host-directed-therapy trials used surrogate or physiological endpoints (TB-HDT: FEV1 and culture conversion; rosuvastatin: culture conversion at week 8). This confirms the fork: either the Phase III is surrogate-based, or it costs far more than $7M.
**Core claim:** a Phase III powered to detect a 10% relative mortality reduction needs about 35,000–57,000 participants and therefore costs well above $7M. (LOGIC ONLY)
**GiveWell's best defense:** The $7M explicitly includes the Phase III, and the 40% p_success is where endpoint risk is absorbed.
**Why it survives:** The Challenger showed that "the Phase III is included" restates the question. The issue is whether $7M can plausibly fund the design implied by the mortality-only benefit stream.
**Recommended action:** Run the verifier on per-participant costs for large simple trials (RECOVERY, Study 31/A5349, TRUNCATE-TB, SimpliciTB) and on the endpoints WHO accepted for recent DS-TB guideline changes. Ask CG for the $7M breakdown and the Phase III endpoint. Do not adopt the 3–10× SROI reduction as stated.
**Key unresolved question:** What is the per-participant cost and primary endpoint of the planned Phase III?

### Finding 4: The TB-specific reference classes (host-directed therapy, adjunctives, regimen-shortening) have a much worse record than 40%
**Impact:** Lowering p_success to a central 0.25 cuts SROI to about 1,909x (−38%), which is below the bar. The executed range is −63% to −13%.
**Evidence:** The individual data points check out. Vitamin D had no overall effect on time to conversion. Dexamethasone in HIV-associated TB meningitis was null (HR 0.85), and its benefit in HIV-negative meningitis is modest and genotype-heterogeneous (LAST ACT 2025). The list is selective, several trials were Phase II/III hybrids, and the settings differ from pulmonary TB.
**Core claim:** The appropriate TB-specific reference class has a success rate well under 40% from Phase II onward (about 10–20%). (LOGIC ONLY)
**GiveWell's best defense:** The 40% is already a 60% haircut. It is also conditioned on a positive Phase IIa/b human signal, which the critique's examples were not.
**Why it survives:** "Already discounted" defends the existence of a haircut, not its size, and CG documents no derivation of 0.40. The judge dropped the 0.15 point estimate but kept the concern that a revision to about 0.25 puts SROI at the bar.
**Recommended action:** Verify the BIO/Informa/QLS 2011–2020 infectious-disease and repurposed-drug transition rates. Obtain CG's derivation of 0.40. Check whether REMoxTB, RIFAQUIN, OFLOTUB and Study 31 were preceded by positive Phase IIb signals. Treat this finding as overlapping with Finding 5, not as an additional adjustment.
**Key unresolved question:** What is CG's basis for 0.40, and what does "success" mean in it?

### Finding 5: Industry phase-transition base rates put "II and III both succeed" at roughly 15–25%, so 40% requires an unstated premium of about 1.6–2.7× [CONDITIONAL — see dependencies]
**Impact:** Lowering p_success to a central 0.27 gives about 2,062x (−33%), just above the bar. At 0.17 SROI is about 1,298x (−58%).
**Evidence:** BIO 2011–2020 rates (Phase II→III 28.9%, Phase III→filing 57.8%) imply about 17% for both phases. Hay 2014 non-oncology rates corroborate this. An infectious-disease uplift (Phase III about 81%) gives roughly 25–32%. Industry rates include business-driven terminations and may understate scientific success for an academic program.
**Core claim:** Industry reference-class rates imply P(II and III succeed) of roughly 15–25%, so CG's 40% needs an unstated premium of about 1.6× or more. (LOGIC ONLY)
**Conditional on:** the unverified claim that the model has no separate factor for WHO adoption or Phase III funding, and that the 60% uptake does not already cover them (P(adoption | Phase III success) and P(Phase III gets funded and run | Phase IIc success) are missing, and the 60% uptake factor may not cover them).
**GiveWell's best defense:** The 40% is conditioned on a prior positive IIa/b signal and a known safety record, so it is not a naive industry draw.
**Why it survives:** A haircut is not a calibration. Even the judge's best-grounded adjusted range (0.25–0.32) sits well below 0.40 and close to the ~0.26 break-even.
**Recommended action:** Replace the critique's 0.20 central and its 0.14–0.30 decomposition with 0.25–0.32. Pull the corrected Wong 2019 infectious-disease rates. Ask CG to state its reference class and whether "success" includes adoption.
**Key unresolved question:** Do non-industry infectious-disease programs with a positive Phase IIa/b signal clear Phase II and III at nearer 25% or 40%?

### Finding 6: "Success" in Phase III is unlikely to be a mortality result, so the 10% mortality effect is not what a "success" would establish
**Impact:** Lowering relative_reduction to a central 0.07 gives about 2,138x (−30%). At 0.05 SROI is about 1,527x (−50%). The bar is crossed if the effective conditional effect falls below about 0.065.
**Evidence:** A review argues that 2–3-month culture positivity is not an acceptable surrogate for long-term outcome. The atorvastatin signal is a Phase IIa bacillary-load result, and rosuvastatin did not affect culture conversion. The sample-size arithmetic (about 72,000 participants at 4% baseline mortality) was reproduced.
**Core claim:** A "success" in the Phase III used by the model would not be a demonstrated 10% mortality reduction, so a large share of success worlds carry a mortality effect well below 10%. (LOGIC ONLY)
**GiveWell's best defense:** The BOTEC never assumes a mortality-powered Phase III. The Phase IIc names survival as an endpoint. Surrogate-only worlds also carry unvalued benefits (morbidity, lung damage, transmission).
**Why it survives:** Silence about the definition of success is not coverage. The 10% is applied as if it were a demonstrated mortality effect.
**Recommended action:** Present a sensitivity table over surrogate-only fraction f ∈ {0.2, 0.35, 0.5} and r_s ∈ {0, 0.03} rather than a point haircut. Ask CG what endpoint "success" refers to. The claim that SROI falls below 2,000x requires f ≥ 0.35–0.49, and nothing anchors f at that level.
**Key unresolved question:** What fraction of "success" worlds would rest on surrogate-only evidence?

### Finding 7: "Success" probably means a surrogate or composite endpoint, but the model needs a 10% mortality reduction, so P(adopted AND 10% mortality benefit) < P(trials succeed)
**Impact:** Lowering relative_reduction to a central 0.07 gives about 2,138x (−30%), with a range of −50% to 0%. This overlaps heavily with Finding 6.
**Evidence:** A mortality-powered DS-TB Phase III needs about 36,000 per arm at 4% mortality, and far more at the 0.5–2% seen in Study 31 and TRUNCATE-TB. Standard TB Phase IIIs use composite unfavourable-outcome endpoints. Counterweight: in high-mortality populations (TB meningitis, advanced HIV), mortality-powered trials are feasible.
**Core claim:** CG's "Phase III success" is declared on a surrogate or composite endpoint that does not directly test a 10% mortality reduction, so P(success) overstates P(adopted AND ≥10% mortality benefit). (LOGIC ONLY)
**GiveWell's best defense:** The BOTEC already contains P(success), P(adoption | success) and E[RR | success] under other labels.
**Why it survives:** Three multiplied terms are only coherent if they share an endpoint definition, and CG does not state one.
**Recommended action:** Report P(trial success) and E[mortality RR | success] under one explicit endpoint definition, and flag the 6.5% crossing point. Obtain the planned endpoint, the target population and the cost breakdown from CG.
**Key unresolved question:** In TB adjunct trials, how well does surrogate or composite success predict a mortality reduction?

### Finding 8: "Adult DS notified" is not "eligible for the trial label": missing applicability filters
**Impact:** Lowering eligible_people_at_8y to a central 4.0M gives about 2,222x (−27%). At 3.5M SROI is about 1,944x (−36%). The grounded extrapulmonary-only filter (×0.84 → about 4.6M) gives roughly −15%.
**Evidence:** WHO shares are verified: extrapulmonary 16% (up to 25% in SE Asia), bacteriological confirmation 64%, HIV about 5–6%, Hr-TB about 7–8%. The filters overlap (HIV and extrapulmonary disease are correlated). The bacteriological-confirmation filter depends on trial design and is probably not appropriate for a real-world label.
**Core claim:** CG's 5.5M includes cases outside the likely trial or label population (extrapulmonary, HIV, pregnancy, hepatic disease, Hr-TB, clinically diagnosed), and these should be modelled explicitly. (LOGIC ONLY)
**GiveWell's best defense:** The 60% uptake parameter plausibly already nets out contraindications and non-pulmonary disease.
**Why it survives:** The 60% is undecomposed and described as a behavioural estimate, so it cannot be shown to embed label filters.
**Recommended action:** Apply at least the ×0.84 extrapulmonary adjustment now. Check CG's source for the 5.5M, the registered trial's exclusion criteria, and whether the 60% is conditional on eligibility.
**Key unresolved question:** What are the trial's exclusion criteria, and is the 5.5M already pulmonary-only?

### Finding 9: Discounting quantified properly with an S-curve ramp and discounted costs. The net effect is about −20% to −31%, not the benefit-only −21% to −35%.
**Impact:** A speedup-equivalent of 0.74 gives about 2,261x (−26%). The range is −20% at a 3% discount rate to −38% under the jointly pessimistic case (10-year ramp and 5% rate), which crosses the bar.
**Evidence:** The verifier confirmed the ramp arithmetic (L=10, 4% → about 0.59). No CG or GiveWell rule on discounting R&D BOTECs was found.
**Core claim:** Consistent discounting of costs and benefits gives a net penalty of about 20–31%, smaller than the benefit-only penalty of 21–35%. (LOGIC ONLY)
**GiveWell's best defense:** The zero discount rate is disclosed ("No time discounting"), and timing is partly handled through the 8-year delay and the case decline.
**Why it survives:** Disclosure is not justification. The Advocate conceded that CG offers no rationale for a zero rate.
**Recommended action:** Add a discount-rate sensitivity row (central about 2,100–2,450x). Ask CG whether the ~2,000x bar is expressed in discounted terms and what time to scale-up it expects.
**Key unresolved question:** Is the ~2,000x bar itself a discounted or undiscounted quantity?

### Finding 10: Post-TB lung disease morbidity is likely the largest unvalued channel (~50–60k central, wide range)
**Impact:** This finding raises SROI. Using dalys_per_death of 34 as a proxy gives about 3,847x (+26%), with a range of +5% to +140%.
**Evidence:** Menzies 2021 puts post-TB sequelae at 5.8 of 12.1 lifetime DALYs per case. A 2025 Lancet Global Health model puts post-TB DALYs at 52.5% of the total. The baseline burden is well supported, but the 5% reduction and its persistence are not, and ROSETTA's null rosuvastatin result on lung involvement cuts against a robust class signal.
**Core claim:** A ~5% proportional reduction in long-term post-TB lung burden follows from the trial's early lung-damage signal. (LOGIC ONLY)
**GiveWell's best defense:** The channel is omitted by design, which makes the BOTEC conservative. If sequelae are large, the 27 DALYs per averted death is overstated, which partly cancels the gain.
**Why it survives:** "Conservative by construction" does not defend a value of zero. The offset (about 6–20k DALYs) is smaller than the central gain.
**Recommended action:** Confirm the size of the atorvastatin lung-damage effect against ROSETTA. Run one merged post-TB morbidity and mortality sensitivity (merging with Finding 34) at p = 0.40, with back-loaded accrual, both discounted and undiscounted.
**Key unresolved question:** Do early radiographic lung-damage reductions persist into long-term lung function?

### Finding 11: The 6% is a mix of deaths, and only a fraction is reachable and modifiable by atorvastatin
**Impact:** Lowering effective baseline_mortality to a central 0.045 gives about 2,291x (−25%). At 0.03 SROI is about 1,527x (−50%).
**Evidence:** On-treatment deaths are front-loaded: about 55–75% occur within 1–2 months across African cohorts, and the median is about 3 weeks in Zambia. Two caveats apply. If the effect size comes from a trial population, a haircut on top double-counts. And some very early deaths may be reversible.
**Core claim:** A large enough share of the 6% is unreachable or non-TB (about 35–40% combined) to push the effective baseline below 3.9%. (LOGIC ONLY)
**GiveWell's best defense:** The 10% is a population-average effect, so an addressable-share haircut double-counts.
**Why it survives:** The Advocate's own point that the observed signal was on lung damage undercuts the claim that 10% is an empirically embedded intention-to-treat mortality effect.
**Recommended action:** Trace the provenance of the 10%. Retrieve the day-7/14/28 cumulative death proportions from the Zambia cohort and data on statin onset timing. Add a flag that SROI falls below the bar if more than about 35% of deaths are unaddressable. This finding overlaps with Finding 17.
**Key unresolved question:** Is the 10% an ITT mortality figure, a surrogate extrapolation, or a judgment call?

### Finding 12: The funding landscape for a generic-statin TB program makes "never" a live branch. The speedup is a poor proxy for the grant's real counterfactual.
**Impact:** The effect is mixed. A speedup of 1.25 years gives about 3,819x (+25%), while p_success of 0.3 gives about 2,291x (−25%). A redundancy branch (speedup 0.5) gives −50%.
**Evidence:** No registered statin-TB Phase III was found (the search was not exhaustive). A 2026 review says HDTs still need Phase III trials. The null rosuvastatin Phase 2b lowers efficacy priors, and NIH-funded Phase 2b trials show that funding does occur.
**Core claim:** The realistic counterfactual for a CG-funded statin Phase IIc has a substantial probability (q about 0.1–0.2 or more) of long delay or never, so expected speedup is above 1 year. (LOGIC ONLY)
**GiveWell's best defense:** "Never funded" plausibly already sits inside the 60% failure mass.
**Why it survives:** That conflates a with-grant failure world with a without-grant counterfactual world.
**Recommended action:** Keep the central SROI and drop the "~20× higher" claim. Use a two-sided speedup range that includes both a redundancy branch and a q-weighted never branch. Check whether CG's Phase IIc is gating relative to the completed StAT-TB and rosuvastatin trials.
**Key unresolved question:** Would anyone fund a statin-TB Phase III absent CG's Phase IIc?

### Finding 13: The all-in framing counts benefits for every treated patient but not the cost of treating them
**Impact:** Adding delivery cost (central all_in_cost of $8.98M) gives about 2,381x (−22%). At $20.2M SROI is about 1,059x (−65%). The breakeven is delivery cost below about $3.7M (about $1.10 per patient).
**Evidence:** ATORTUB (NCT06199921, 440 patients, with Open Philanthropy as collaborator) confirms the program. Procurement alone is cheap, so the result turns on monitoring costs and on how third-party health spending is valued.
**Core claim:** CG's all-in cost omits delivery cost for the ~3.3M treated patients while counting their benefits. Including it would push SROI materially below the threshold unless third-party money is heavily discounted. (LOGIC ONLY)
**GiveWell's best defense:** There is no delivery-cost line, but unvalued benefits and the conservative 4% expected effect partly offset this.
**Why it survives:** The Advocate conceded that no existing adjustment addresses delivery cost. The structural asymmetry was judged valid with high confidence.
**Recommended action:** Re-run with delivery cost weighted by 0.4, a 56–112-tablet course at $1–6, and face-value versus 25% valuation of third-party money. In any case, state the convention for third-party spending.
**Key unresolved question:** What per-patient monitoring cost would programs actually incur, and how does CG value government and Global Fund money?

### Finding 14: Winner's-curse and reference-class patterns imply the conditional effect should sit well below the surrogate-implied one, and r and p_success should not be independent
**Impact:** Lowering relative_reduction to a central 0.08 gives about 2,444x (−20%). At 0.05 SROI falls by 50%.
**Evidence:** Atorvastatin has only a Phase II bacillary-load signal (Nigeria). The rosuvastatin Phase 2b was null (HR 1.30, p=0.19). The broader reference class (vitamin D, metformin, CC-11050, everolimus) shows surrogate-only or null signals.
**Core claim:** the CG's 10% conditional mortality effect is inflated relative to the true effect because it is anchored on selected early or surrogate signals, so r should be shrunk. (LOGIC ONLY)
**GiveWell's best defense:** Null and surrogate-only worlds sit inside the 60% failure mass, so E[r×p] = E[r]×E[p].
**Why it survives:** The Advocate's own argument that the trial targets lung damage implies that success can be surrogate-defined, which reopens the covariance between r and p_success.
**Recommended action:** Look up the funded trials' primary endpoints and the provenance of the 10%. If success is surrogate-defined, add a single surrogate-only fraction f rather than stacking it on a shrinkage factor. Otherwise treat r as downward-skewed with a central value of about 0.08–0.09.
**Key unresolved question:** Is the 10% an observed-effect planning value or a true-effect prior?

### Finding 15: A 2%/yr decline in notified case counts probably contradicts the observed trend; incidence rates fall slowly while counts do not
**Impact:** This finding raises SROI. A flat-count central of 6.46M eligible gives about 3,588x (+17%), with a range of −5% to +27%. It already includes Finding 21's baseline correction and must not be added to it.
**Evidence:** WHO data show notifications rising while incidence rates fall about 1.7% per year. Funding-cut modelling projects 12–41% more TB among people living with HIV in South Africa. Provisional 2025 notification declines in several countries support some downside.
**Core claim:** Notified case counts have not been declining ~2%/yr and are more likely flat or rising over the next 8 years, so applying 2%/yr to counts understates eligible volume. (LOGIC ONLY)
**GiveWell's best defense:** The 2% is a forward-looking, conservative planning assumption that 2020–2024 data cannot refute.
**Why it survives:** The 2% has no stated basis and is applied to counts, which track detection rather than incidence.
**Recommended action:** Use 0%/yr as the central value, with a sensitivity range of −1% to +1%/yr (about 5.9–7.0M). Check WHO notification counts for 2015–2018.
**Key unresolved question:** Were pre-COVID notification counts rising?

### Finding 16: 60% steady-state uptake has no precedent among comparable TB program additions
**Impact:** Lowering adult_uptake to a central 0.5 gives about 2,546x (−17%). At 0.35 SROI is about 1,782x (−42%). Lengthening years_to_adoption to 10 adds −4%.
**Evidence:** WRD coverage reached 54% after about 14 years and is still rising. HPMZ uptake was about 0.05% after 3 years (supply-limited). In NYC, 14% of eligible patients were prescribed HPMZ and 64% of those discontinued. Neither is a clean analog for a cheap generic oral drug, and the analogs bear more on the ramp than on the ceiling.
**Core claim:** the long-run uptake ceiling is plausibly 0.30–0.40, not 0.60. (LOGIC ONLY)
**GiveWell's best defense:** Any uptake ceiling scales both the accelerated and counterfactual worlds equally.
**Why it survives:** The grant's value is the difference between the two worlds, and that difference is proportional to the ceiling. The sensitivity run contradicts the cancellation claim.
**Recommended action:** Retrieve CG's definition of adult_uptake. Search for cheap-adjunct analogs (pyridoxine co-prescription, dexamethasone in TB meningitis, GDF order volumes). Interim: a ceiling of about 0.5 gives about 2,450x.
**Key unresolved question:** What sustained coverage do cheap TB adjuncts achieve in high-burden national programs?

### Finding 17: A large share of on-treatment deaths is unreachable by a weeks-scale host-directed adjunct, and shorter regimens shrink the headroom further
**Impact:** Lowering relative_reduction to a central 0.085 gives about 2,597x (−15%). At 0.065 SROI is about 1,986x (−35%).
**Evidence:** Early deaths are typically from fulminant septic shock. That shock is inflammatory, however, so a host-directed drug is not obviously irrelevant to it. No data show statins reduce early TB mortality.
**Core claim:** A material share (25–35%) of on-treatment deaths is not modifiable by a weeks-scale adjunct, so the effective r is below 10%. (LOGIC ONLY)
**GiveWell's best defense:** The 10% is a success-conditional population-level effect, so the unreachable share is already inside it.
**Why it survives:** That is true only if 10% is a realized trial effect. Its provenance is unknown.
**Recommended action:** Keep this as a directional flag and drop the 25–35% figure as a quantitative input. Ask CG whether 10% is the trial's powered minimum detectable effect. Do not stack with Finding 11.
**Key unresolved question:** Is 10% the powered target of the trial or an extrapolation from a surrogate?

### Finding 18: A 1-year speedup of trial results does not necessarily become a 1-year speedup of adoption, in either direction.
**Impact:** A speedup of 0.85 years gives about 2,597x (−15%), with a range of −50% to +20%. The bar is crossed below about 0.65 years.
**Evidence:** WHO acted within months of pivotal data for Study 31 and BPaLM, so the "missed guideline window" upside is weakly supported. No data were found on national adoption lags, which is where slack is most plausible.
**Core claim:** The trial is not the sole binding constraint, so a 1-year trial speedup need not translate into a 1-year adoption speedup, and the effective speedup is a lumpy random variable. (LOGIC ONLY)
**GiveWell's best defense:** The 1 year is an adoption speedup, and a pure time translation gives (shift) × (steady-state benefit) whatever the ramp shape.
**Why it survives:** The translation derivation assumes that adoption shifts one-for-one, which is the very point in dispute.
**Recommended action:** Report a range of 0.5–1.2 years and the 0.65 break-even, optionally with a central value of 0.85–0.95. Search MSF/Stop TB "Step Up for TB" data on national adoption lags.
**Key unresolved question:** How long after WHO guidance do high-burden countries adopt new TB regimens?

### Finding 19: Clinical eligibility and monitoring barriers cap the achievable prescribing share below the "generic and cheap" logic
**Impact:** Lowering adult_uptake to a central 0.51 gives about 2,597x (−15%). At 0.42 SROI is about 2,138x (−30%), which does not cross the bar.
**Evidence:** Pooled anti-TB drug-induced liver injury is about 11.5%, and its authors say liver monitoring is imperative. StAT-TB tests pravastatin, and atorvastatin was inactive at non-toxic doses in THP-1 cells. This raises a statin-identity question that may matter more than uptake.
**Core claim:** Eligibility exclusions, DILI-attribution concerns and monitoring requirements would cut adult uptake from about 0.60 to about 0.45–0.50. (LOGIC ONLY)
**GiveWell's best defense:** 60% is already a 40-point haircut with room for exclusions.
**Why it survives:** A haircut with no derivation cannot be shown to absorb specific exclusions.
**Recommended action:** Confirm which statin CG assumes and whether the 60% is defined over all adults. Note monitoring and adverse-event costs as an omission under all_in_cost (see Finding 13).
**Key unresolved question:** Is the CG candidate atorvastatin or pravastatin, and over what population is the 60% defined?

### Finding 20: Survivors' excess mortality and comorbidity shrink the 27 DALYs per death
**Impact:** Lowering dalys_per_death to a central 24 gives about 2,715x (−11%). At 20 SROI is about 2,263x (−26%).
**Evidence:** Romanowski 2019 gives an SMR of 2.91 (2.21–3.84). A 2026 cohort gives an RR of 1.77, which roughly halves the computed reduction. Menzies shows burden estimates can include post-TB effects.
**Core claim:** The 27 DALYs per death derives from general-population or GBD-style life tables and is therefore overstated for the people whose deaths are actually averted. (LOGIC ONLY)
**GiveWell's best defense:** 27 is "remaining healthy life expectancy" and so already reflects morbidity.
**Why it survives:** The healthy-versus-total life expectancy gap does not show that TB-survivor excess mortality is embedded.
**Recommended action:** Apply a downward adjustment of about 10–20% (central about 23). Determine CG's source for 27, and retrieve Romanowski's SMR by time since treatment completion.
**Key unresolved question:** Was 27 built from a general-population or a TB-specific life table?

### Finding 21: Baseline year is stale and the 5.5M figure is sensitive to it
**Impact:** This finding raises SROI. Eligible people of 6.05M gives about 3,360x (+10%). It is subsumed by Finding 15 and should not be added to it.
**Evidence:** WHO 2025 reports 8.3M notifications in 2024, 78% of estimated incidence.
**Core claim:** Notified cases are ~8.2–8.3M, not ~7.5M, so a 7.5M baseline understates the starting point by ~9–11%. (SUPPORTED)
**GiveWell's best defense:** This is a rounded BOTEC designed for re-anchoring, and the effect is bounded at about +10%.
**Why it survives:** Re-anchoring being cheap does not make the current input right.
**Recommended action:** Re-anchor on 8.2M (+9%). Correct the "material" label. Confirm CG's anchor year and the ~0.90 factor.
**Key unresolved question:** What year and figure does CG's 5.5M rest on?

### Finding 22: Zero modeled lag between Phase III completion and adoption, and a speedup that assumes trial timing is the binding constraint
**Impact:** A speedup of 0.9 years gives about 2,749x (−10%), and years_to_adoption of 10 gives −4%. The speedup range is −50% to +25%.
**Evidence:** WHO acted within weeks for HPMZ. The concern is about country adoption and the critical path, for which no HPMZ data were found.
**Core claim:** A 1-year acceleration of Phase IIc does not give a 1-year earlier adoption, because the trial is not the binding constraint. (LOGIC ONLY)
**GiveWell's best defense:** Post-Phase III lag is common to both timelines and costs only the 2%/yr case decline.
**Why it survives:** "Common to both timelines" assumes the trial is on the critical path, which is the open question.
**Recommended action:** Flag the 1-year speedup as unjustified, with a 0.5–1.25 band. Inspect the model's time horizon. Search registries and funders for an existing Phase III commitment. This finding overlaps with Finding 18.
**Key unresolved question:** Is a Phase III already funded independent of the Phase IIc timing?

### Finding 23: A Phase III cannot be powered on mortality, so the WHO GDG would be recommending on surrogate or composite endpoints
**Impact:** Lowering adult_uptake to a central 0.55 gives about 2,800x (−8%). At 0.45 SROI falls by 25%. The years_to_adoption effect is about −1%.
**Evidence:** WHO TB GDGs usually treat composites that include death as critical outcomes, which reduces the expected indirectness penalty. StAT-TB treats mortality only as a tolerability measure. Observational statin benefit is shown only in the ASCVD subgroup.
**Core claim:** A Phase III cannot be powered on a roughly 10% relative mortality reduction (about 30k per arm), so the recommendation would rest on surrogate or composite endpoints that GRADE treats as indirect. (LOGIC ONLY)
**GiveWell's best defense:** The 40% p_success already absorbs equivocal surrogate evidence.
**Why it survives:** p_success is undefined, so it cannot be shown to cover a "positive trial, narrowed recommendation" outcome.
**Recommended action:** Keep only the uptake channel (−5% to −15%). Note in the model that p_success is undefined. Check WHO's handling of corticosteroids in TB meningitis and pericarditis as a precedent.
**Key unresolved question:** Have WHO TB recommendations for host-directed adjuncts been population-restricted?

### Finding 24: A global-average mortality may not match the countries where an atorvastatin adjunct would actually be deployed
**Impact:** baseline_mortality of 0.055 gives about 2,800x (−8%), with a range of −33% to +25%. The low end (0.04) gives 2,037x, just above the bar.
**Evidence:** WHO reports 88% global treatment success for DS-TB, leaving room for country spread. Trial-enrolled patients usually have lower mortality than programmatic cohorts.
**Core claim:** Country-weighted on-treatment mortality could differ materially from the single global 6% figure, depending on deployment mix. (LOGIC ONLY)
**GiveWell's best defense:** With uniform uptake, the case-weighted global mean is the correct quantity.
**Why it survives:** The Challenger conceded the algebra. What survives is that the 6% is unsourced and may not match the case-count population.
**Recommended action:** Compute the case-weighted "% died" for the eight high-burden countries from WHO cohort tables. Close the critique if the result is 5–7%, and escalate if it is at or below 4.5%.
**Key unresolved question:** What is the case-weighted on-treatment death rate in the deployment countries?

### Finding 25: Shorter and new regimens erode both the eligible population and the incremental benefit
**Impact:** Eligible people of 5.09M gives about 2,826x (−8%). At 4.125M SROI falls by 25%.
**Evidence:** HPMZ is conditional, restricted to age 12 and over, and constrained by rifapentine supply and exposure. The 4-month HRZ(E) regimen for children retains rifampicin. Bedaquiline-linezolid strategies remain at trial stage.
**Core claim:** 20–40% of eligible patients will be on non-HRZE regimens at the benefit horizon, which pushes effective eligibility down to about the 3.6M threshold. (LOGIC ONLY)
**GiveWell's best defense:** Existing parameters partly absorb this, and shortening cannot matter in a model without a duration term.
**Why it survives:** The Advocate conceded that regimen change is unmodeled.
**Recommended action:** Add a displacement × (1 − transfer) adjustment as a −5% to −25% band. Drop the "compounding" and "stronger inducer" strands. Optionally pull data on GDF rifapentine uptake.
**Key unresolved question:** What share of DS-TB patients will be on non-HRZE backbones by about 2033?

### Finding 26: Hepatotoxicity and myopathy add a negative tail, and the combined attenuations compound
**Impact:** relative_reduction of 0.095 gives about 2,902x (−5%). The compounded 0.023–0.054 range double-counts overlapping factors and was rejected as an estimate.
**Evidence:** The StAT-TB protocol cites pravastatin–rifampin interactions. Metformin reduced rifampicin bioavailability by 24%, a reference-class point. The atorvastatin–rifampicin exposure check was not completed.
**Core claim:** the independent attenuation factors (reachable fraction, PK attenuation, shrinkage) multiply to cut r to about 0.023–0.054. (LOGIC ONLY)
**GiveWell's best defense:** Detectable harm sits inside the 40% failure mass.
**Why it survives:** The narrow point was conceded. What survives is the need for a single de-duplicated attenuation in place of separate multipliers.
**Recommended action:** Drop the harm tail as a standalone adjustment. Add a sensitivity case at relative_reduction = 0.065 and one de-duplicated net multiplier once the endpoint and drug-interaction evidence is in.
**Key unresolved question:** What is the measured atorvastatin exposure under co-administered rifampicin?

### Finding 27: Transmission benefit is small, with a bounded calculation (~10–30k central)
**Impact:** This finding raises SROI slightly. A dalys_per_death proxy of 28.26 gives about 3,197x (+5%), with a range of +1% to +19%. It is not decision-relevant.
**Evidence:** Guinea-pig data show infectiousness drops sharply with effective therapy regardless of culture status. One MDR-TB experiment showed infectiousness unchanged at 72 hours, which keeps some upper tail. ROSETTA found no rosuvastatin effect on culture conversion.
**Core claim:** The net reduction in total transmission from faster conversion is ~0.3% (range 0.1–1%). (LOGIC ONLY)
**GiveWell's best defense:** Omitting transmission is conservative and does not move the decision.
**Why it survives:** Both sides agree it is small. What survives is the documentation gap and a correction to the materiality label.
**Recommended action:** Document the omission. Confirm how the 40% enters the formula and source the 19,900 deaths-averted base. Relabel the critique as not material.
**Key unresolved question:** Does the trial show any culture-conversion acceleration at all?

## Minor Findings (surviving strength: WEAK)

**Finding 28: Regulatory, pharmacovigilance and dissemination costs for an off-patent drug have no obvious payer, and the $7M likely under-budgets them.** An all_in_cost of $8.5M gives about 2,516x (−18%), with a range of +8% to −42%. The headroom is thin: the bar is crossed above about $10.7M. The ATORTUB registry describes an international multicenter Phase III, which plausibly consumes much of the $7M. No rollout-cost data were found, and the $5–20M illustration is ungrounded (core claim: LOGIC ONLY). The judge recommends no cost adjustment, a request to CG for the line items of the $7M, and folding monitoring cost into Finding 13. Benchmarking against EDCTP/CORDIS awards would revive the critique only if the trial alone exceeds about $6M.

**Finding 29: Rifampicin induction structurally limits atorvastatin exposure in routine programs, and the trial exposure does not transfer.** relative_reduction of 0.085 gives −15%. The interaction is real (separated dosing cuts AUC by about 80%; co-administration modestly raises it), and atorvastatin had a poor in vitro therapeutic index. However, the debate established that, under regimen-matched co-administration, the interaction is a p_success consideration rather than an r haircut, because the positive signal was obtained on rifampicin backgrounds (core claim: LOGIC ONLY). Do not apply the 0.5–0.8 multiplier. Record a qualitative flag on p_success, and read the Phase IIc/III protocol for the background regimen and dosing timing.

**Finding 30: The sweat-based diagnostic carries real option value but is speculative (~10–30k central).** The executed run at relative_reduction 0.1094 gives +9%, but the judge notes the stated 10–30k central corresponds to only 0.102–0.106 (about +1–6%). WHO's 2026 tongue-swab recommendation lowers incremental value, though paediatric and no-sputum gaps remain (core claim: LOGIC ONLY). Add a one-line exclusion note and confirm whether any diagnostic spend sits in the cost base. This finding engages with, but does not depend on, the unverifiable scope-boundary critique (see Open Questions).

**Finding 31: Private-sector treatment share and the reach of national guidelines are not modeled.** adult_uptake of 0.57 gives −5%, with a range of −15% to +5%. The private sector handles about one-third of notified cases in India, and the notification mandate exists but is weakly enforced. The sign is ambiguous, since private providers may adopt a cheap generic faster (core claim: LOGIC ONLY). Make no adjustment, and record that the 60% has no stated channel decomposition.

**Finding 32: Under-ascertained deaths push true mortality up, and the direction is the opposite of Critiques 1–2.** This finding raises SROI. baseline_mortality of 0.0625 gives +4%, with a range of 0 to +13%. Post-LTFU mortality is elevated (about 10% dead in Kenyan tracing, SMR 2–7×), but most such deaths occur after treatment stops and are unreachable by an on-treatment adjunct (core claim: LOGIC ONLY). The critique is moot if CG's 6% is all-cause cohort mortality, which is a single document check.

**Finding 33: M72/AS01E and other incidence shocks are likely not large enough by year 8–10, but should be modelled.** Eligible people of 5.3M gives −4%. Even a 15% shock leaves SROI at about 2,600x. M72 Phase IIb efficacy was 49.7% (CI 2.1–74.2, 39 cases), and modelled impact builds toward 2050 (core claim: LOGIC ONLY). Add a joint sensitivity row varying secular decline (2% vs 4%/yr) with a 0/5/15% vaccine shock. The worst combination gives about 2,200x.

**Finding 34: Post-treatment excess mortality (~40–50k central) and a related sign-reversing adjustment.** dalys_per_death of 27.5 gives +2%, with a range of −10% to +19%, and the sign is ambiguous. Channel (a), post-treatment deaths, overlaps with Menzies' framework and Finding 10. Channel (b), a life-expectancy overstatement, overlaps with Finding 20 (core claim: LOGIC ONLY). Merge (a) into Finding 10. Check whether 27 uses a general-population or TB-adjusted life table.

**Finding 35: Covariance between mortality and DALYs per death means the product of means is not the mean of the product.** The executed central is 0%, with a range of −11% to +7%. The mathematics is correct, but the sign is uncertain (high-HIV settings reverse it), and the effect is zero if 27 is already death-weighted (core claim: LOGIC ONLY). Compare 27 to GBD TB YLL ÷ TB deaths for the deployment countries, and drop the critique if the ratio is about 24–30.

## Findings by Parameter

| Parameter | Findings (by number) | Direction | Executed range of the bottom line |
|---|---|---|---|
| relative_reduction | 4, 5, 6, 7, 11, 14, 17, 23, 26, 29, 30, 35 | mixed (all lower except 30) | −50% to +14% (runs from 6, 7, 14, 17, 26, 29, 30) |
| p_success | 2, 4, 5, 6, 12, 14, 26, 29, 33 | lowers | −63% to +0% (runs from 4, 5, 12) |
| all_in_cost | 2, 3, 6, 13, 28 | lowers | −86% to +8% (runs from 2, 3, 13, 28) |
| speedup_years | 1, 9, 12, 18, 22, 31 | mixed (1, 12 raise; 9, 18, 22 lower) | −50% to +1,400% (runs from 1, 9, 12, 18, 22) |
| dalys_per_death | 10, 20, 27, 34, 35 | mixed (10, 27 raise; 20 lowers) | −26% to +140% (runs from 10, 20, 27, 34, 35) |
| baseline_mortality | 8, 11, 17, 24, 32, 35 | mixed (32 raises; 11, 17 lower) | −50% to +25% (runs from 11, 24, 32) |
| adult_uptake | 8, 16, 18, 19, 23, 29, 31 | lowers | −42% to +17% (runs from 16, 19, 23, 31) |
| eligible_people_at_8y | 6, 8, 15, 21, 25, 31, 33 | mixed (15, 21 raise; 8, 25, 33 lower) | −36% to +27% (runs from 8, 15, 21, 25, 33) |
| years_to_adoption | 15, 16, 18, 21, 22, 23, 33 | lowers | −11% to +0% (runs from 16, 22, 23) |
| decline_per_year | 15, 21, 22 | raises (15) | not executed (expressed via eligible_people_at_8y) |
| (structural) | (none: every surviving finding mapped to at least one parameter) | — | — |

Findings in the same row describe overlapping concerns about one number. Take the most credible one per row rather than stacking them.

## Conflicting Findings

**speedup_years:** Findings 1, 12 vs 9, 18, 22. Findings 1 and 12 argue the effective counterfactual benefit window is much larger than one year (never-branch, coherent PV framing). Findings 9, 18 and 22 argue discounting and downstream adoption friction shrink it below one year. *What would decide it:* evidence on whether any funder has committed to a statin-TB Phase III independent of CG's Phase IIc, combined with observed national adoption lags after WHO TB guidance.

**eligible_people_at_8y:** Findings 15, 21 vs 8, 25, 33. Findings 15 and 21 show notified counts are higher and flatter than the model assumes. Findings 8, 25 and 33 argue that label filters, regimen displacement and incidence shocks shrink the eligible pool. *What would decide it:* CG's source for the 5.5M (anchor year, adults-only, pulmonary-only) together with the trial's registered exclusion criteria.

**baseline_mortality (and effective mortality reached):** Finding 32 vs 11, 17, 24. Finding 32 argues true mortality exceeds 6% through under-ascertainment. Findings 11, 17 and 24 argue the reachable or deployment-weighted mortality is lower. *What would decide it:* CG's definition of the 6% (WHO "died" share or all-cause cohort mortality) and day-by-day timing of deaths from cohort data.

**dalys_per_death:** Findings 10, 27 vs 20, 35. Findings 10 and 27 add unvalued long-term and transmission DALYs. Findings 20 and 35 argue the 27 DALYs per averted death is overstated for TB survivors. *What would decide it:* the provenance of the 27 figure (life table, age, and whether it is death-weighted) and long-term lung-function follow-up from the atorvastatin trial.

## Comparison with GiveWell's AI Output

**The Baseline AI Output section of the input was empty, so overlap cannot be assessed.** The table below records what the pipeline contributed to each finding. The "Overlap" column is marked "Not assessable" rather than guessed. Until the baseline is supplied, this report cannot demonstrate improvement over it.

| Our Critique | Overlap with GiveWell AI Output? | What We Added |
|---|---|---|
| 1. Speedup/all-in counterfactual mismatch | Not assessable | Novel structural framing; executed speedup sensitivity; debate cut the claim from 10–20× to 3–5× conditional |
| 2. Reference-class TB Phase III cost | Not assessable | Verified cost anchors (TB-PRACTECAL, pivotal median); per-patient check route via NCT05575518 |
| 3. $7M cannot fund mortality-powered Phase III | Not assessable | Sample-size arithmetic; $9.3M threshold; verified that HDT Phase IIs used surrogates |
| 4. TB-specific reference class for p_success | Not assessable | Verified individual trial outcomes; flagged selection bias |
| 5. Industry base rates for p_success | Not assessable | Verified BIO rates; grounded 0.25–0.32 range; dependency on adoption-gate claim tracked |
| 6. Phase III "success" not a mortality result | Not assessable | f/r_s sensitivity structure; surrogate-validity evidence |
| 7. Surrogate success vs 10% mortality effect | Not assessable | Verified TB endpoint conventions; 6.5% crossing point |
| 8. Missing label-applicability filters | Not assessable | Verified WHO shares; filter-overlap correction |
| 9. Consistent discounting | Not assessable | Verified ramp arithmetic; net vs benefit-only penalty |
| 10. Post-TB lung morbidity | Not assessable | Menzies and Lancet Global Health anchors; merge rule with Finding 34 |
| 11. Reachable share of the 6% | Not assessable | Verified multi-country early-death timing |
| 12. "Never" branch and funding landscape | Not assessable | Registry check; two-sided speedup band |
| 13. Delivery cost omitted | Not assessable | ATORTUB registry; $3.7M breakeven |
| 14. Winner's curse / r–p covariance | Not assessable | Verified atorvastatin and rosuvastatin data |
| 15. 2%/yr decline on counts | Not assessable | WHO 2025 notification data; non-additivity with Finding 21 |
| 16. 60% uptake precedent | Not assessable | WRD/HPMZ uptake data |
| 17. Unreachable deaths | Not assessable | Septic-shock counterpoint; overlap with Finding 11 |
| 18. Trial vs adoption speedup | Not assessable | Study 31 and BPaLM timing; 0.65-year break-even |
| 19. Eligibility and monitoring barriers | Not assessable | DILI base rate; statin-identity flag |
| 20. Survivor excess mortality vs 27 DALYs | Not assessable | Romanowski and 2026 cohort SMRs |
| 21. Stale baseline year | Not assessable | WHO 2024 figure (8.3M) |
| 22. Zero adoption lag | Not assessable | HPMZ chronology correction |
| 23. WHO GDG indirectness | Not assessable | GRADE composite-outcome counterweight |
| 24. Global vs deployment-country mortality | Not assessable | Trial-vs-programme mortality caveat |
| 25. Regimen displacement | Not assessable | HPMZ restrictions; rifampicin in paediatric 4-month regimen |
| 26. Harm tail / compounding | Not assessable | Identified double-counting in compounded attenuations |
| 27. Transmission | Not assessable | Guinea-pig infectiousness data |
| 28. Adoption-infrastructure budget | Not assessable | Registry description of Phase III scope |
| 29. Rifampicin–atorvastatin PK | Not assessable | AUC asymmetry; reframed as a p_success issue |
| 30. Sweat diagnostic | Not assessable | WHO tongue-swab scope check |
| 31. Private-sector reach | Not assessable | India notification mandate evidence |
| 32. Under-ascertained deaths | Not assessable | LTFU mortality data; addressability caveat |
| 33. M72 incidence shock | Not assessable | Vaccine model timelines |
| 34. Post-treatment excess mortality | Not assessable | Overlap identification |
| 35. Mortality × DALY covariance | Not assessable | GBD cross-check route |

## Debate Quality Audit (from judge agent data)

**Total debates audited:** 35
**Sound analytical moves noted:** 89

**Failure modes detected (combined across both sides):**

| Failure type | Count |
|---|---|
| unsupported_estimate_fabricated | 12 |
| unsupported_estimate_pseudo | 33 |
| unsupported_estimate_counter | 8 |
| whataboutism | 5 |
| call_to_ignorance | 40 |
| strawmanning | 33 |
| false_definitiveness | 47 |
| generic_recommendation | 0 |
| misrepresenting_evidence_status | 19 |

**Most common Advocate failure:** false_definitiveness
**Most common Challenger failure:** false_definitiveness

**Patterns:** Across both sides combined, false_definitiveness (47) was the most frequent failure mode. It was followed by call_to_ignorance (40, combined) and by strawmanning and unsupported_estimate_pseudo (33 each, combined). The input identifies false_definitiveness as the single most common failure for the Advocate and for the Challenger separately, but gives no per-side counts, so we cannot say how the combined 47 splits between them. generic_recommendation was zero across both sides combined.

## Conditional Findings (from linker output)

### Industry phase-transition base rates put "II and III both succeed" at roughly 15–25%, so 40% requires an unstated premium of about 1.6–2.7×
**Depends on:** P(adoption | Phase III success) and P(Phase III gets funded and run | Phase IIc success) are missing, and the 60% uptake factor may not cover them (UNVERIFIABLE)
**Verifier's reasoning for marking it UNVERIFIABLE:** "This depends on how CG derived the 60% and what it includes, which I could not check." The verifier found nothing that directly confirms or contradicts the critique. It noted a possible double-count: if the 40% came from industry base rates for reaching approval, it may already include some funding and strategic attrition.
**If the assumption holds:** The critique's decomposition, which includes P(adopted | III) ≈ 0.7–0.85, supports a p_success central near 0.20. That is below the ~0.26 break-even, so SROI falls under the bar. Revise p_success downward and ask CG to state its reference class.
**If the assumption is wrong:** If adoption is already embedded in the 60% uptake (or is near-certain), the adoption factor drops out of the decomposition and the sub-0.26 central is no longer supported. The judge's adjusted range of 0.25–0.32, built from infectious-disease Phase II × Phase III transition rates alone, does not use the adoption gate and still stands. It implies a 20–37% SROI reduction (about 1,900–2,450x) that may or may not breach the bar. The recommendation then softens from "below the bar" to "40% is unsupported and should be revised to about 0.25–0.32."

## Open Questions (from Rejected Critiques input — verdict: UNVERIFIABLE)

### Unclear scope boundary for the sweat-diagnostic workstream
**Hypothesis:** The thread notes a sweat-diagnostic workstream. If the diagnostic work is part of the same program, its costs are either inside the $7M, which leaves less for statin Phase III and adoption, or outside it. If outside, the all-in cost is understated. If the diagnostic's benefits are included in the credited benefits but its costs are not, that is a mismatch. If it is a separate program, shared trial infrastructure could be double-counted or free-ridden in either direction.
**Why the verifier couldn't ground it:** The critique presents it as a scenario, and the verifier found no evidence for or against it. No public link between the statin program and a sweat-based diagnostic was found, nor the CG grant page.
**Why it's still worth investigating:** A diagnostic budget above about $3.7M would breach the bar if its costs and benefits are booked asymmetrically, and one look at the grant structure resolves it.

### Probability weighting is asymmetric between benefit and cost.
**Hypothesis:** Benefits are multiplied by p_success = 0.40. If the $7M cost is a nominal sum of all stages, the denominator ignores that later-stage spend only occurs if earlier stages succeed. Under a sequential, gated pathway, expected spend is lower than nominal spend. The benefit is discounted for failure while the cost is not. This is a double penalty.
**Why the verifier couldn't ground it:** The mechanism is sound, but the verifier found no evidence on how the CEA constructed the cost, and the critique is conditional on it.
**Why it's still worth investigating:** It is one of the few upward cost-side adjustments (potentially 1.6–2.3× SROI, though plausibly smaller because late failures still incur cost), and it interacts directly with Findings 2, 3 and 13.

### P(adoption | Phase III success) and P(Phase III gets funded and run | Phase IIc success) are missing, and the 60% uptake factor may not cover them
**Hypothesis:** Separate adoption and funding steps may be missing from the p_success chain. If they are absent and each is below 1, cost-effectiveness falls roughly proportionally. 0.40 × 0.75–0.85 gives 0.30–0.34, a 15–25% reduction. If the 60% embeds adoption, this becomes a documentation point only.
**Why the verifier couldn't ground it:** This depends on how CG derived the 60% and what it includes, which the verifier could not check.
**Why it's still worth investigating:** Finding 5's sub-threshold conclusion explicitly depends on it, and with a funding gate of about 0.8 the base case approaches the 0.26 break-even.

### Findings that rest on unverified claims

**"Success" in Phase III is unlikely to be a mortality result, so the 10% mortality effect is not what a "success" would establish** rests on: A "success" in the Phase III used by the model would not be a demonstrated 10% mortality reduction, so a large share of success worlds carry a mortality effect well below 10%.
*Why it could not be checked:* The sample-size arithmetic is correct and the prior evidence is surrogate-based, but how the model defines "success" was not available.
*What would settle it:* CG's stated Phase III primary endpoint behind the 40% and the 10%.

**A large share of on-treatment deaths is unreachable by a weeks-scale host-directed adjunct, and shorter regimens shrink the headroom further** rests on: A material share (25–35%) of on-treatment deaths is not modifiable by a weeks-scale adjunct, so the effective r is below 10%.
*Why it could not be checked:* The direction is supported by early-death and comorbidity data, but the fraction is not quantified in any source found.
*What would settle it:* Cumulative time-to-death distributions from cohorts such as Zambia's, combined with data on the onset of statin anti-inflammatory effects.

**Rifampicin induction structurally limits atorvastatin exposure in routine programs, and the trial exposure does not transfer** rests on: Under routine chronic rifampicin therapy, achieved atorvastatin exposure is low enough to reduce the realised mortality effect by about 20–50%.
*Why it could not be checked:* The interaction is real and the label confirms variable reductions, but chronic co-administered exposure is uninvestigated and no data link exposure to a mortality effect.
*What would settle it:* A PK substudy of chronic co-administered atorvastatin under rifampicin, plus the Phase IIc/III protocol's background regimen and dosing timing.

**Winner's-curse and reference-class patterns imply the conditional effect should sit well below the surrogate-implied one, and r and p_success should not be independent** rests on: the CG's 10% conditional mortality effect is inflated relative to the true effect because it is anchored on selected early or surrogate signals, so r should be shrunk.
*Why it could not be checked:* (not given in input)
*What would settle it:* CG's documentation of where the 10% comes from (an observed trial effect or a true-effect prior).

**Hepatotoxicity and myopathy add a negative tail, and the combined attenuations compound** rests on: the independent attenuation factors (reachable fraction, PK attenuation, shrinkage) multiply to cut r to about 0.023–0.054.
*Why it could not be checked:* (not given in input)
*What would settle it:* Measured rifampicin–atorvastatin exposure data and CG's definition of "success", which together determine which factors are distinct.

**A $7M Phase III cannot be powered on mortality, and the CEA's benefit is mortality only** rests on: a Phase III powered to detect a 10% relative mortality reduction needs about 35,000–57,000 participants and therefore costs well above $7M.
*Why it could not be checked:* (not given in input)
*What would settle it:* Per-participant costs from large pragmatic TB trials (e.g., Study 31/A5349, TRUNCATE-TB) and CG's $7M line-item breakdown.

**The all-in framing counts benefits for every treated patient but not the cost of treating them** rests on: CG's all-in cost omits delivery cost for the ~3.3M treated patients while counting their benefits. Including it would push SROI materially below the threshold unless third-party money is heavily discounted.
*Why it could not be checked:* The arithmetic and plausible prices hold, but there was no evidence on how CG's model treats delivery costs or third-party spending.
*What would settle it:* CG's stated convention for valuing government and Global Fund delivery spending, plus programme-level monitoring cost data.

**Regulatory, pharmacovigilance and dissemination costs for an off-patent drug have no obvious payer, and the $7M likely under-budgets them** rests on: The $7M is too small to cover the unfunded adoption infrastructure (guidelines, training, supply chain, pharmacovigilance) on top of the trials.
*Why it could not be checked:* The incentive argument and the hepatotoxicity concern hold, but no budget data or comparable rollout costs were found.
*What would settle it:* Public award amounts for comparable multi-country TB repurposing Phase IIIs (e.g., EDCTP StatinTB on CORDIS).

**The speedup benefit and the all-in cost come from different counterfactuals. Every coherent framing gives roughly 10–20x higher SROI.** rests on: Under every coherent counterfactual the ratio equals PV_B/PV_C, so the BOTEC understates SROI by roughly 10–20×.
*Why it could not be checked:* The algebra holds when other funders' money is valued at the discount rate. It fails if displacement is priced at the funder's opportunity cost, and the multiplier rests on assumed horizon and delay parameters.
*What would settle it:* A CG decision on how displaced co-funder dollars are valued, plus a documented benefit horizon.

**The funding landscape for a generic-statin TB program makes "never" a live branch. The speedup is a poor proxy for the grant's real counterfactual.** rests on: The realistic counterfactual for a CG-funded statin Phase IIc has a substantial probability (q about 0.1–0.2 or more) of long delay or never, so expected speedup is above 1 year.
*Why it could not be checked:* The reasoning is coherent and consistent with no Phase III being found, but there is no direct evidence on q, and existing NIH, Gates and other Phase 2b statin trials show funding has occurred.
*What would settle it:* Registry and funder searches (Unitaid, EDCTP, NIH/ACTG) for any committed statin-TB Phase III, and CG's own assessment of whether its Phase IIc is gating.

**Discounting quantified properly with an S-curve ramp and discounted costs. The net effect is about −20% to −31%, not the benefit-only −21% to −35%.** rests on: Consistent discounting of costs and benefits gives a net penalty of about 20–31%, smaller than the benefit-only penalty of 21–35%.
*Why it could not be checked:* The arithmetic checks out and the principle is standard, but the inputs (T0, L, cost timing) are unsourced assumptions and CG's actual convention is unknown.
*What would settle it:* CG confirmation of whether its ~2,000x bar is discounted, and its expected scale-up timeline.

**A 1-year speedup of trial results does not necessarily become a 1-year speedup of adoption, in either direction.** rests on: The trial is not the sole binding constraint, so a 1-year trial speedup need not translate into a 1-year adoption speedup, and the effective speedup is a lumpy random variable.
*Why it could not be checked:* Downstream constraints are documented, but the specific "fixed WHO schedule, missed-window" mechanism is not supported by the two cases checked.
*What would settle it:* National adoption-lag data after WHO rapid communications for 4-month HPMZ and BPaLM (e.g., Step Up for TB surveys).

**Post-TB lung disease morbidity is likely the largest unvalued channel (~50–60k central, wide range)** rests on: A ~5% proportional reduction in long-term post-TB lung burden follows from the trial's early lung-damage signal.
*Why it could not be checked:* The baseline burden is well supported, but there is no evidence on surrogate-to-long-term transfer, and the 5% is admitted to be an assumption.
*What would settle it:* Long-term spirometry follow-up from the atorvastatin trial, compared against ROSETTA's lung outcomes.

**Post-treatment excess mortality (~40–50k central) and a related sign-reversing adjustment** rests on: About 40% of post-treatment excess deaths are lung-related and reducible by ~5% via the intervention, roughly offset by a 5–10% overstatement of on-treatment benefit.
*Why it could not be checked:* The excess mortality is verified, but there is no evidence on the respiratory share, the 5% reduction, or the life-expectancy adjustment.
*What would settle it:* Cause-specific post-TB mortality breakdowns (e.g., from Romanowski-type cohorts) and the provenance of the 27-DALY figure.

**Transmission benefit is small, with a bounded calculation (~10–30k central)** rests on: The net reduction in total transmission from faster conversion is ~0.3% (range 0.1–1%).
*Why it could not be checked:* Qualitative literature supports "small", but the 1–5% post-start share and the 10–20% fractional reduction are unsupported, and the evidence cuts toward a smaller effect.
*What would settle it:* The trial's culture-conversion effect size, combined with household-contact transmission studies by treatment phase.

**The sweat-based diagnostic carries real option value but is speculative (~10–30k central)** rests on: P(adoption) ≈ 5% with an incremental yield of 1–3% of incidence, giving about 10–30k DALYs per year.
*Why it could not be checked:* The arithmetic is internally consistent, but the probability and yield inputs are an assumed base rate with no source, and the test itself could not be found.
*What would settle it:* CG's grant documentation describing the diagnostic's development stage and its comparator performance against tongue-swab PCR.

**60% steady-state uptake has no precedent among comparable TB program additions** rests on: the long-run uptake ceiling is plausibly 0.30–0.40, not 0.60.
*Why it could not be checked:* The precedents show slow ramps (HPMZ about 0.05% after three years, WRD 54% after about 14 years), but none shows a stalled ceiling below 60% for a cheap, generic, oral co-administered drug.
*What would settle it:* National-programme coverage data for cheap adjuncts such as pyridoxine co-prescription and dexamethasone in TB meningitis.

**A Phase III cannot be powered on mortality, so the WHO GDG would be recommending on surrogate or composite endpoints** rests on: A Phase III cannot be powered on a roughly 10% relative mortality reduction (about 30k per arm), so the recommendation would rest on surrogate or composite endpoints that GRADE treats as indirect.
*Why it could not be checked:* The arithmetic reproduces, baseline mortality sits in the claimed range, and WHO guidance confirms the downgrading mechanism, but no evidence ties this to a specific uptake reduction.
*What would settle it:* WHO's GRADE evidence profiles for corticosteroid recommendations in TB meningitis and pericarditis, showing endpoint basis and population scope.

**Clinical eligibility and monitoring barriers cap the achievable prescribing share below the "generic and cheap" logic** rests on: Eligibility exclusions, DILI-attribution concerns and monitoring requirements would cut adult uptake from about 0.60 to about 0.45–0.50.
*Why it could not be checked:* The mechanisms are plausible and the DILI base rate is verified, but there is no evidence for the size of the exclusion or program-reluctance effect.
*What would settle it:* The trial protocol's exclusion criteria and CG's statement of which statin and which population the 60% refers to.

**Private-sector treatment share and the reach of national guidelines are not modeled** rests on: Effective uptake of a new regimen in the private sector is materially lower than the model assumes, giving a net downward adjustment to benefit.
*Why it could not be checked:* The private share is real, but there is no evidence on private-sector uptake of new regimens, and the sign is admittedly ambiguous.
*What would settle it:* Private-sector prescription audits in India (e.g., via PPSA data) for a recently recommended TB regimen.

**Zero modeled lag between Phase III completion and adoption, and a speedup that assumes trial timing is the binding constraint** rests on: A 1-year acceleration of Phase IIc does not give a 1-year earlier adoption, because the trial is not the binding constraint.
*Why it could not be checked:* The claim is plausible, since sponsorship and funding could gate Phase III, but there is no evidence on this regimen's funding path or timeline.
*What would settle it:* Evidence of whether a Phase III sponsor is already committed, from registries and funder announcements.

**Survivors' excess mortality and comorbidity shrink the 27 DALYs per death** rests on: The 27 DALYs per death derives from general-population or GBD-style life tables and is therefore overstated for the people whose deaths are actually averted.
*Why it could not be checked:* Excess post-TB mortality is well documented, but how CG built 27 could not be found. It may already be a TB-specific or healthy-life figure, which would offset the adjustment.
*What would settle it:* CG's source table for 27 (country, age and life-table type).

**The 6% is a mix of deaths, and only a fraction is reachable and modifiable by atorvastatin** rests on: A large enough share of the 6% is unreachable or non-TB (about 35–40% combined) to push the effective baseline below 3.9%.
*Why it could not be checked:* Early concentration of deaths is directly supported, but the specific shares are acknowledged placeholders, and there is no evidence on statin onset time or the non-TB share needed to reach the threshold.
*What would settle it:* Cause-of-death and timing data from on-treatment cohorts, combined with CRP-onset timing data for statins.

**Under-ascertained deaths push true mortality up, and the direction is the opposite of Critiques 1–2** rests on: A meaningful share of LTFU and not-evaluated patients die, so true mortality among treated patients exceeds 6%, and the excess is relevant to statin benefit.
*Why it could not be checked:* Tracing and cohort data show elevated post-LTFU mortality (about 10% in Kenya, SMR 2–7×), but no source shows these deaths are modifiable by an adjunct taken during treatment.
*What would settle it:* CG's definition of the 6% (WHO "died" category or all-cause cohort mortality).

**Covariance between mortality and DALYs per death means the product of means is not the mean of the product** rests on: The 27 DALYs/death input is not death-weighted, and the covariance is negative enough to bias the product upward by about 10–15%.
*Why it could not be checked:* The covariance logic is sound, but there is no evidence on how 27 was derived or on the actual size of the covariance.
*What would settle it:* GBD TB YLL ÷ TB deaths for the main deployment countries, compared to 27.

**A global-average mortality may not match the countries where an atorvastatin adjunct would actually be deployed** rests on: Country-weighted on-treatment mortality could differ materially from the single global 6% figure, depending on deployment mix.
*Why it could not be checked:* Heterogeneity is plausible and directionally supported, but no country-specific on-treatment death percentages were found to size it.
*What would settle it:* WHO Global TB Report country "% died" for the new-and-relapse cohort in the eight high-burden countries.

**Industry phase-transition base rates put "II and III both succeed" at roughly 15–25%, so 40% requires an unstated premium of about 1.6–2.7×** rests on: Industry reference-class rates imply P(II and III succeed) of roughly 15–25%, so CG's 40% needs an unstated premium of about 1.6× or more.
*Why it could not be checked:* The BIO rates were directly confirmed, but the infectious-disease uplift could be larger than assumed and CG's endpoint definition is unknown.
*What would settle it:* The corrected Wong 2019 infectious-disease Phase II/III rates with a non-industry breakdown, plus CG's definition of success.

**The TB-specific reference classes (host-directed therapy, adjunctives, regimen-shortening) have a much worse record than 40%** rests on: The appropriate TB-specific reference class has a success rate well under 40% from Phase II onward (about 10–20%).
*Why it could not be checked:* The individual trial facts check out, but the class rate is an unpublished inference built from a non-systematic, selected list.
*What would settle it:* A systematic enumeration of TB adjunct and HDT programs that had a positive Phase IIa/b signal, with their subsequent outcomes.

**"Success" probably means a surrogate or composite endpoint, but the model needs a 10% mortality reduction, so P(adopted AND 10% mortality benefit) < P(trials succeed)** rests on: CG's "Phase III success" is declared on a surrogate or composite endpoint that does not directly test a 10% mortality reduction, so P(success) overstates P(adopted AND ≥10% mortality benefit).
*Why it could not be checked:* The arithmetic and TB endpoint conventions are verified, but there is no evidence on how CG defines success or on the actual mortality-conditional effect.
*What would settle it:* CG's planned Phase III primary endpoint and target population.

**A 2%/yr decline in notified case counts probably contradicts the observed trend; incidence rates fall slowly while counts do not** rests on: Notified case counts have not been declining ~2%/yr and are more likely flat or rising over the next 8 years, so applying 2%/yr to counts understates eligible volume.
*Why it could not be checked:* WHO data show incident counts flat and notifications up while rates fell only 1.7% in 2024.
*What would settle it:* WHO notification count series for 2015–2018 and early 2025–2026 provisional counts.

**"Adult DS notified" is not "eligible for the trial label": missing applicability filters** rests on: CG's 5.5M includes cases outside the likely trial or label population (extrapulmonary, HIV, pregnancy, hepatic disease, Hr-TB, clinically diagnosed), and these should be modelled explicitly.
*Why it could not be checked:* The WHO shares are verified, but whether CG's 5.5M already excludes them, and which filters a trial or label would apply, are not visible or verifiable.
*What would settle it:* CG's derivation of the 5.5M together with the registered trial's exclusion criteria.

**Shorter and new regimens erode both the eligible population and the incremental benefit** rests on: 20–40% of eligible patients will be on non-HRZE regimens at the benefit horizon, which pushes effective eligibility down to about the 3.6M threshold.
*Why it could not be checked:* No adoption projection exists, and the Investigator admits it is a self-chosen scenario. The slow-uptake evidence points to the low end of the range or below it.
*What would settle it:* GDF rifapentine procurement trends and WHO Global TB Report data on HPMZ uptake.

**M72/AS01E and other incidence shocks are likely not large enough by year 8–10, but should be modelled** rests on: M72-driven incidence reduction by year 8–10 is small (5–15%). It becomes large (30–50%) only later, so a constant eligible-population assumption overstates the pool in the later years of the benefit horizon.
*Why it could not be checked:* The model literature points to impact building toward 2050 and a modest effect from a post-infection-only vaccine, but no source gives 2033–35 incidence figures, and the 30–50% later-year reduction is not sourced.
*What would settle it:* The M72 Phase III readout timeline and published country models reporting incidence reductions at 2033–35.

## Resolved Negatives (from Rejected Critiques input — verdict: REJECTED)

### Effective delivered dose and adherence diverge from trial conditions, and programmatic dose may be lower than the trial dose, notably with rifapentine regimens
**Hypothesis:** Programmatic adherence to an unsupervised adjunct pill is likely below trial adherence, and this lowers realized benefit. The size of the effect is ungrounded. The 70% figure is an assumption, and it risks double-counting if the trial effect is already pragmatic or intention-to-treat. Daily rifapentine induces CYP3A4 at roughly 85–100% of rifampicin's level, similar to the interaction already present in HRZE-based trials and not clearly worse.
**Contradicting evidence:** Multiple pharmacology sources rank inductive potency as rifampin > rifapentine > rifabutin (relative potency 100% / 85% / 40%), and the WHO prequalification document says rifapentine's induction may be less than rifampicin's. One midazolam study showed a larger AUC fall with rifapentine, and one hepatocyte study found it the weakest inducer, so the best-supported reading is a modest difference in either direction. The 70% adherence figure is assumed, and if the Phase III is ITT the haircut double-counts.
**Why this matters for GiveWell:** It rules out treating HPMZ's growing share as an additional exposure penalty beyond the rifampicin interaction already present in the trial setting, and it confirms an ITT effect size should not be further haircut for adherence.

### Phase IIc "success" is a weak gate. If it is defined by PK or dose selection, it passes easily and transmits little information, so the probability of the whole chain should be weighted toward Phase III
**Hypothesis:** If CG's Phase IIc is defined by PK or dose rather than clinical outcomes, the 40% should be decomposed into P(IIc) × P(III | weak signal) before comparison with Phase II→approval base rates. Modelling p_success and RR as independent point values is a simplification.
**Contradicting evidence:** Under standard TB usage, Phase IIc (the STEP design) is a hybrid efficacy gate. The experimental regimen is given for its planned Phase III duration with 12-month failure and relapse follow-up, explicitly to "set a high bar" and reduce the risk of costly Phase III failure. Ongoing Phase IIc protocols use unfavourable outcome status as the efficacy endpoint. Whether CG uses "IIc" in this sense is unchecked.
**Why this matters for GiveWell:** If CG's IIc follows the standard design, a IIc pass is informative about Phase III. That supports a p_success above naive industry Phase II rates, and it undercuts the 0.5 IIc assumption that Finding 5's decomposition borrowed.

## Judged Immaterial (not debated)

**The "lung benefit without mortality benefit" scenario is structurally less valuable than a simple p_success weighting implies**: (none mapped); not executed. These were not debated because the quantifier found their effect on the bottom line too small.

## Meta-Observations

1. **No finding reached STRONG.** All 35 survivors are MODERATE (27) or WEAK (8), and 33 of 35 rest on a LOGIC ONLY core claim. Only Findings 2 and 21 have a SUPPORTED core claim. The high signal rate (35/41) reflects that most critiques are plausible directional points. It does not mean that most were established quantitatively. Many are variants of well-known BOTEC concerns (an undocumented p_success, zero discounting, an unanchored uptake share).

2. **One undefined term drives a large share of the downside.** The definition of Phase III "success" and its endpoint underlies Findings 3, 6, 7, 14, 23 and 26, and bears on 2, 4 and 5. These findings form a fork. If the Phase III is mortality-powered, the $7M is too low (Findings 2 and 3: −56% to −65%). If it is surrogate- or composite-powered, the $7M may be adequate but the 10% mortality effect is overstated (Findings 6 and 7: about −30%). Both cannot apply at once, so stacking the cost and effect-size findings double-counts. A single document request to CG (the Phase III endpoint, population and $7M breakdown) is the highest-value next step in this report.

3. **The headroom is thin and most adjustments point down.** The baseline clears the bar by about 35%. Five rows of the parameter table (p_success, all_in_cost, relative_reduction, adult_uptake and, net, eligible_people_at_8y) each contain a finding that, at its own central value, uses up half or more of that headroom. These rows are not fully independent, but they are not identical either. A joint downside scenario (for example p_success of 0.3 combined with r of 0.085) would likely fall below 2,000x and should be run explicitly. The main offsets are the case-count corrections (Findings 15 and 21, about +17%), post-TB morbidity (Finding 10, about +26%) and the counterfactual-framing argument (Finding 1). The last is large but highly conditional.

4. **The debates' failure profile mirrors the model's documentation gaps.** false_definitiveness (47 combined) and call_to_ignorance (40 combined) were the two most frequent failure modes. Many Advocate defenses took the form "the 40% / 60% / 10% already absorbs this," and many Challenger rebuttals took the form "CG doesn't define it, so it can't cover it." Both assert a definite answer about parameters that the BOTEC leaves undefined. This is a property of the critiques' subject matter, not merely of debate quality: until CG documents what p_success, adult_uptake, the 10% and the 6% mean, these questions cannot be argued to resolution, and the MODERATE ceiling is likely to persist.

5. **Data gaps that recur across threads:** the provenance of the 27 DALYs per death (Findings 20, 34, 35); the definition of the 6% (Findings 11, 24, 32); which statin is assumed and its rifamycin interaction (Findings 19, 26, 29); and whether a Phase III sponsor exists (Findings 12, 22). Each is a desk check.

6. **Comparison caveat:** the baseline AI output was not supplied in this run, so this report cannot demonstrate improvement over GiveWell's single-pass output. The pipeline's identifiable contributions are executed sensitivities for every finding, verifier-corrected evidence (for example the HPMZ chronology, the rifapentine induction ranking and the Phase IIc design standard), explicit non-additivity rules within parameter rows, and one tracked conditional dependency.