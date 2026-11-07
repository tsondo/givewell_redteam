# Red Team Report: Adjunctive Atorvastatin (Host-Directed Therapy) for Drug-Susceptible TB, Phase IIc Grant BOTEC

## Pipeline Summary

- Investigation threads examined: 8
- Candidate critiques generated: 41
- Verified critiques: 41
- Rejected by verifier: 0
- Critiques surviving adversarial review: 39
- Dependencies identified: 0
- Signal rate: 39/41

**Note on these counts.** The verifier rejected 0 of 41 candidates, yet 39 critiques survived adversarial review. The inputs do not account for the other 2: they appear in neither the surviving nor the rejected lists. The high signal rate shows that the verification stage filtered almost nothing. It is not evidence that 95% of candidates were high quality.

The verifier did flag many claims *within* critiques as UNGROUNDED. However, it never assigned a critique-level UNVERIFIABLE or REJECTED verdict. That is why the Open Questions, Resolved Negatives and Conditional Findings sections below are empty.

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

---

## Critical Findings (surviving strength: STRONG)

### Finding 1: A $7M Phase III cannot be powered on mortality, and the CEA's benefit is mortality only

**Impact:** Suppose the $7M all-in budget must fund a Phase III capable of supporting the mortality-only benefit. All-in cost then plausibly rises to ~$30–45M, and SROI falls from ~3,050x to ~570x at the central case (plausible range ~300–1,000x).
- The judge endorses only the narrower claim: SROI is overstated by at least ~1.3×.
- The overstatement shrinks toward ~1× only if an ultra-lean embedded design under ~$200/participant is feasible.

**Evidence:**
- Sample size (two-proportion formula, 80% power, α = 0.05): a 10% relative mortality reduction needs ~28,000 per arm at 5% baseline mortality and ~17,000 per arm at 8% (~34,000–57,000 total).
- Per-participant costs span ~$100 for routine-care-embedded trials to tens of thousands of dollars (TB-PRACTECAL). The pragmatic-trial literature the verifier retrieved supports a lean lower bound near $5M.
- An editorial notes there is no consensus on endpoints for host-directed therapy (HDT) trials.
- The verifier rated evidence strength **weak**. The STRONG label reflects the Advocate's failure to escape the argument's structure, not a dense evidence base.

**GiveWell's best defense:** The $7M is explicitly all-in ("later Phase III trials, guideline changes, dissemination and validation"). The 40% p_success is where any surrogate-to-mortality gap is priced. Under the speedup framing, attributable cost scales less than 1:1.

**Why it survives:** The defense cannot escape a dilemma:
- If the Phase III is mortality-powered, $7M is far too small.
- If it is surrogate-powered, "success" does not establish the 10% mortality effect that drives all modeled benefit.

The cost figure and the p_success/relative_reduction pair cannot both be right as currently specified.

**Recommended action:**
1. Ask CG to state the Phase III primary endpoint, target sample size and power assumption behind "success."
2. Have the verifier retrieve published per-participant costs for large pragmatic DS-TB or HIV-TB trials in LMICs, especially trials with vital-status endpoints.

**Key unresolved question:** What is the per-participant cost of the cheapest Phase III design credible enough to drive a WHO recommendation, and does that design measure mortality?

---

## Significant Findings (surviving strength: MODERATE)

These are ordered by the magnitude of the SROI shift the judge was willing to endorse. Findings with no endorsed magnitude come last. Many share upstream unknowns, so their adjustments **cannot be summed** (see Meta-Observations).

### Finding 2: The speedup benefit and the all-in cost come from different counterfactuals. Every coherent framing gives roughly 10–20x higher SROI.

**Impact:** The BOTEC pairs a one-year benefit pulse with the full program cost. Any branch-matched framing raises SROI, by an amount that depends on the effective benefit horizon:

| Effective horizon | SROI uplift |
|---|---|
| ~5 years | ~4–5× |
| ~17 years | ~11× |
| Pure-delay corner | up to ~20× (likely overstated) |

The title's "10–20x" is the critique's original range. The judge endorses the horizon-conditional range in this table. Direction: **increases** SROI.

**Evidence:** The argument is structural, and the verifier found nothing contradicting it. The result is highly horizon-sensitive. The null ROSETTA (rosuvastatin) results and statin class/dose uncertainty argue for a bounded horizon.

**GiveWell's best defense:** The pairing is deliberate and visible. "1 year" may be a blended expected acceleration, which is consistent with the BOTEC only at a pivotal probability q ≈ 5–9%. At realistic q (25–50%), the uplift is ~3.5–6×.

**Why it survives:** The Advocate's reading blends the benefit but not the cost. The direction (coherent framing ≥ BOTEC) holds for any effective horizon longer than ~1.5–2 years.

**Recommended action:**
1. Confirm whether "1 year" is a pure delay or a mixture.
2. Rebuild a q × horizon table (q ∈ {0, 0.25, 0.5, 1}; horizon ∈ {5, 10, 17+} years) with branch-matched costs. Include the discounted time cost of accelerating other funders' ~$6.7M.

**Key unresolved question:** What is the effective benefit horizon, given regimen obsolescence, and is the 1-year speedup a pure delay?

### Finding 3: The all-in framing counts benefits for every treated patient but not the cost of treating them

**Impact:** At ~$3 per patient across ~3.3M patients, delivery cost moves SROI from ~3,086x to ~1,960x (~−35%, roughly at the bar).
- The reduction is larger if delivery approaches ~$10 per course.
- It is immaterial if third-party money is heavily discounted.
- The judge's break-even is ~$2.9 per patient. The critique's own mechanism used ~$1.10 per patient (D < $3.7M). These differ and should be reconciled.

**Evidence:**
- The Phase IIC trial (NCT06199921, Open Philanthropy listed as collaborator) tests multiple atorvastatin doses in 440 patients, so delivery cost depends on which dose is adopted.
- Retail drug prices are low-to-tens of dollars per course. Tender prices were not retrieved.
- First-line TB treatment already carries liver-monitoring needs.

**GiveWell's best defense:** The 60% uptake is justified as "generic and cheap." Excluded benefit channels offset the omitted cost.

**Why it survives:** Uptake is a patient count and puts no dollars in the denominator. CG's convention for third-party implementation costs is unstated, and that gap is itself the finding.

**Recommended action:**
1. Retrieve MSH International Drug Price Indicator and GDF catalog prices for atorvastatin 20/40 mg and multiply by the 112-tablet course.
2. Check how CG/Open Philanthropy SROI methodology treats third-party delivery costs.

**Key unresolved question:** Does CG's SROI convention count third-party delivery costs, and at what fraction of face value?

### Finding 4: Industry phase-transition base rates put "II and III both succeed" at roughly 15–25%, so 40% requires an unstated premium of about 1.6–2.7×

**Impact:** The judge's working range for p_success is ~0.25–0.35 (central ~0.30). This implies SROI of ~1,875–2,625x, which straddles the 2,000x bar. The critique's 0.20 central estimate and 1.6–2.7× premium were **not** adopted.

**Evidence:**
- BIO 2011–2020 gives ~29% (Phase II→III) × ~58% (Phase III→filing) ≈ 17%.
- Anti-infective programs perform above average, and one dataset shows Phase III success above 80%. This pulls the defensible range up.
- Regulatory approval is not the same as LMIC adoption at scale.

**GiveWell's best defense:** The 60% uptake already haircuts adoption, so multiplying by P(adopted | III) double-counts.

**Why it survives:** The parameter map says adoption is "may be partly captured" in uptake, which is a hedge. CG provides no reference class or decomposition for 40%.

**Recommended action:** Confirm from CG's model notes:
- whether the 60% uptake is conditional on WHO adoption;
- how Phase IIc "success" is defined.

**Key unresolved question:** What reference class and success definition underlie the 0.40?

### Finding 5: Discounting quantified properly with an S-curve ramp and discounted costs. The net effect is about −20% to −31%, not the benefit-only −21% to −35%.

**Impact:** With costs and benefits both discounted, SROI falls ~20%, 27% and 31% at 3%, 4% and 5% discount rates.
- This is material at 4–5% but not at 3%.
- Only the long-ramp scenario (L = 10, 5% rate, ~1,900x) crosses the bar.

**Evidence:**
- Global health evaluations typically use 3% for both costs and outcomes. One review argues for ≥5% in low- and lower-middle-income countries.
- The inferred bar (~2,000x against a ~3,050x baseline) is crossed at about −34%, not at the 25% materiality line.

**GiveWell's best defense:** The ~1.5× gap between ~3,000x and the 2,000x bar provides informal headroom for second-order terms.

**Why it survives:** Zero discounting is conceded, and the headroom claim has no source.

**Recommended action:**
1. Extract the CEA's benefit-onset timing (ramp from year ~8 versus a one-year pulse).
2. Report a discounted SROI alongside the undiscounted figure.

**Key unresolved question:** What benefit-onset profile does the CEA assume?

### Finding 6: "Adult DS notified" is not "eligible for the trial label": missing applicability filters

**Impact:**
- Non-confirmation filters (pulmonary-only, HIV, pregnancy, hepatic impairment, Hr-TB) give roughly ×0.74–0.78 on the eligible population (~−22 to −26%).
- Restricting to bacteriologically confirmed cases (×~0.62) takes eligible to ~2.5M, below the 3.6M bar.
- Combined with Finding 13's count correction, the result is ~5.1M (~−7%) without the confirmation restriction and ~3.2M with it.

**Evidence:** Verified WHO figures:
- extrapulmonary share: 16% globally, ~25% in South-East Asia;
- bacteriological confirmation: 64% of pulmonary cases;
- HIV: ~5–6%;
- Hr-TB: ~7%.

**GiveWell's best defense:** The 40% non-uptake plausibly already absorbs these exclusions.

**Why it survives:** The 60% is justified as "generic and cheap," and nothing ties it to label eligibility. The Advocate concedes the overlap is inference.

**Recommended action:**
1. Retrieve the registered inclusion and exclusion criteria of the trials CG relies on.
2. Check whether prior WHO TB recommendations (e.g., HPMZ) mirrored their trial populations.

**Key unresolved question:** Would a recommendation be restricted to bacteriologically confirmed pulmonary TB?

### Finding 7: Probability weighting is asymmetric between benefit and cost.

**Impact:** If the $7M is a nominal full-pathway sum while benefits are gated by 0.40, SROI is understated. The critique's bound is up to 1.6–2.3×. The judge's realistic range is 1.0–1.7×, and the low end may be immaterial. Direction: **increases** SROI.

**Evidence:**
- No external evidence exists on how the $7M was built.
- Late-stage failure still incurs most costs, which pushes the effective spend probability toward 1.

**GiveWell's best defense:** The BOTEC does not say whether the $7M is nominal or expected, and the critique concedes it fails if the $7M is expected.

**Why it survives:** Gating the benefit by a joint probability does nothing to the cost side.

**Recommended action:** Obtain the cost build-up:
- whether the $7M is nominal or expected spend;
- its split across Phase II, Phase III and guideline/dissemination;
- whether CG's $0.32M share is an early, certain stage.

**Key unresolved question:** Is the $7M a full-pathway budget or a probability-weighted spend?

### Finding 8: Survivors' excess mortality and comorbidity shrink the 27 DALYs per death

**Impact:** If 27 is a general-population figure, dalys_per_death is overstated by ~10–30%, giving SROI of ~2,100–2,700x. This is material but does not cross the bar alone.

**Evidence:**
- Romanowski 2019 reports a pooled SMR of 2.91 (95% CI 2.21–3.84) for TB survivors.
- A Gompertz illustration (unsourced) implies ~11–12 years of effective ageing and a 20–30% cut in remaining life expectancy at age ~40.
- No source for the derivation of 27 was found.

**GiveWell's best defense:** 27 is "remaining *healthy* life expectancy," so a morbidity discount is already built in.

**Why it survives:** A HALE-type discount scales years by general-population morbidity. It does not capture the elevated mortality hazard of TB survivors, which is a separate channel.

**Recommended action:** Locate the derivation of 27: its source (HALE or life table), the evaluation age, and any TB adjustment. If it is general-population, re-run with setting-specific SMRs.

**Key unresolved question:** Is 27 a general-population HALE value, and at what age?

### Finding 9: 60% steady-state uptake has no precedent among comparable TB program additions

**Impact:** The judge supports at most a 0.45–0.50 alternative case (~−17 to −25%). The pipeline sensitivity run gives:
- low case: ~1,527x (−50%), which crosses the bar;
- high case: ~3,819x (+25%).

**Evidence:**
- WHO-recommended rapid diagnostic (WRD) coverage reached 54% globally after ~14 years.
- In 24 African countries, WRD coverage rose from 37% (2018) to 58% (2023), ~4 percentage points per year.
- WHO's GDG anticipated gradual uptake of the 4-month regimen.
- Neither analog is a clean comparator for a cheap generic adjunct.

**GiveWell's best defense:** The 60% is a long-run ceiling conditional on success, already discounted by the 40% p_success.

**Why it survives:** p_success multiplies the whole benefit stream and does not discount the ceiling. Still, the debate supports "uncertain," not "demonstrably too high."

**Recommended action:** Check whether "uptake" means prescribing and whether the efficacy estimate is intention-to-treat. If efficacy is ITT, the adherence haircut largely collapses.

**Key unresolved question:** Has any comparable TB adjunct reached ~60% steady-state use?

### Finding 10: P(adoption | Phase III success) and P(Phase III gets funded and run | Phase IIc success) are missing, and the 60% uptake factor may not cover them

**Impact:** If the 60% excludes adoption, a 0.75–0.85 adoption factor gives SROI of ~2,300–2,600x. This does not breach the bar alone. The funding factor was dropped as a quantitative adjustment.

**Evidence:**
- No source gives P(adoption | positive Phase III) for TB adjuncts.
- Study 31 was adopted within months, which argues against a heavy discount in the best case.
- An adjunct with low-certainty mortality evidence is the harder case.

**GiveWell's best defense:** Phase III funding sits inside the 40%, and the $7M already charges for Phase III.

**Why it survives:** The funding point is conceded in part, but the adoption gap remains undocumented.

**Recommended action:** Confirm how the 60% was derived and how the $7M splits between Phase IIc and Phase III.

**Key unresolved question:** What is P(WHO/national adoption) given a surrogate-positive Phase III?

### Finding 11: Clinical eligibility and monitoring barriers cap the achievable prescribing share below the "generic and cheap" logic

**Impact:** A valid downward adjustment to adult_uptake of ~15–25% (moderate confidence in direction, low in magnitude). It does not cross the bar alone, may overlap the existing 40-point haircut, and should not be stacked with adherence.

**Evidence:**
- Anti-TB drug-induced liver injury (DILI) has a pooled incidence of ~11.5%, higher with HIV.
- Rifamycin, protease inhibitor and efavirenz interactions with atorvastatin are documented.
- Existing statin-TB trials are small and short (e.g., rosuvastatin 10 mg for 8 weeks), and their exclusions would be inherited by any recommendation.

**GiveWell's best defense:** The 40% non-uptake plausibly contains these frictions.

**Why it survives:** The Advocate cannot show that CG intended this, so the conditional cuts both ways.

**Recommended action:**
1. Retrieve CG's rationale for the 60% and the named statin candidate.
2. Retrieve on-treatment mortality for HIV and liver-disease subgroups.

**Key unresolved question:** What share of adult DS-TB patients would be excluded or need monitoring the system cannot provide?

### Finding 12: Winner's-curse and reference-class patterns imply the conditional effect should sit well below the surrogate-implied one, and r and p_success should not be independent

**Impact:** A shrinkage factor of 0.7–0.9 gives r ≈ 0.07–0.09 (−10 to −30%). This is not decisive alone: SROI stays above 2,000x unless r < ~6.5%.

**Evidence:**
- Rosuvastatin Phase 2b was null on culture conversion (42 vs 42 days; HR 1.30, 95% CI 0.88–1.91, p = 0.19) and on PET-CT.
- StAT-TB (pravastatin) is registered as completed, but no results were found.
- Atorvastatin evidence in the verifier's results is largely preclinical (synergy in guinea pigs).
- The verifier argues this is translation and confounding risk rather than winner's curse, and arguably supports a *larger* downward adjustment.

**GiveWell's best defense:** p × E[r | success] is already the joint expectation, so no independence assumption is made.

**Why it survives:** The independence point is conceded, but the level of r remains unsupported by human mortality data.

**Recommended action:**
1. Retrieve the atorvastatin Phase IIa/b sample size, prespecified versus post-hoc endpoints, and confidence intervals.
2. Retrieve StAT-TB results.
3. Confirm the success definition.

**Key unresolved question:** How large and how prespecified was the atorvastatin signal CG relies on?

### Finding 13: A 2%/yr decline in notified case counts probably contradicts the observed trend; incidence rates fall slowly while counts do not

**Impact:** If CG applies 2%/yr to counts, eligible population is understated by ~8–17.5% (central ~+12%). Direction: **increases** SROI. This premise is unverified.

**Evidence:**
- Notifications rose from 7.5M (2022) to 8.3M (2024).
- Incident counts have been roughly flat at 10.3–10.8M since 2020, with a ~−1% change in 2024 and a ~1.4%/yr rate decline.
- The 2.4M detection gap caps detection-driven growth.

**GiveWell's best defense:** The model holds treated share constant, so the pool tracks incidence, not notifications.

**Why it survives:** Incidence counts are also flat, so the comparator switch does not rescue a 2%/yr count decline.

**Recommended action:** Confirm in the BOTEC whether the decline applies to counts or rates. Note the 2025 funding-disruption downside as an unquantified caveat.

**Key unresolved question:** Does CG apply the decline to counts or to rates?

### Finding 14: Shorter and new regimens erode both the eligible population and the incremental benefit

**Impact:** A modest 10–20% displacement scenario leaves SROI at ~2,400x at the low end. The bar is crossed at ~33–35% displacement.

**Evidence:**
- WHO's conditional HPMZ recommendation explicitly references rifapentine availability, consistent with slow uptake.
- 2HRZ(E)/2HR is for non-severe paediatric TB only.
- TRUNCATE-TB is a strategy trial, not a standard regimen.
- Bedaquiline-based DS-TB regimens remain in Phase 2/2c.
- No evidence was found on statin effects on shorter backbones.

**GiveWell's best defense:** Patients on non-HRZE regimens may sit inside the 40% non-uptake.

**Why it survives:** CG does not state this, and the 60% is not tied to regimen composition.

**Recommended action:**
1. Add an explicit displacement parameter.
2. Flag effect transfer to HPMZ as untested.
3. Optionally, pull GDF rifapentine procurement volumes.

**Key unresolved question:** Does the atorvastatin effect transfer to a rifapentine–moxifloxacin backbone?

### Finding 15: A large share of on-treatment deaths is unreachable by a weeks-scale host-directed adjunct, and shorter regimens shrink the headroom further

**Impact:** A reachability sensitivity of 0–35% unreachable gives SROI of ~3,000x→~1,950x. Only a haircut of ~33% or more flips the decision.

**Evidence:**
- Atorvastatin was given for 2 months (Phase IIB) and 16 weeks (planned sub-study), so it only partly overlaps the early-death window.
- A 1.8–33.3% range shows the reachable share is strongly setting- and HIV-dependent.

**GiveWell's best defense:** The 10% is a net population-level figure that could already embed reachability (e.g., 14% × 70%).

**Why it survives:** The embedding is hypothetical, because CG gives no derivation for 10%.

**Recommended action:**
1. Flag the 10% as underived and add the reachability sensitivity row.
2. Drop the HPMZ headroom claim.
3. Ask CG whether the 10% came from a mortality signal, a surrogate or judgment.

**Key unresolved question:** How was the 10% derived?

### Finding 16: "Success" in Phase III is unlikely to be a mortality result, so the 10% mortality effect is not what a "success" would establish

**Impact:**
- With half of success worlds surrogate-only at r_s = 0.03, E[r | success] = 0.065, which is at the threshold.
- With r_s = 0, it falls to 0.05 (−50%).
- The share f is ungrounded, so the bar-crossing claim does not survive.
- The judge recommends reporting SROI as conditional on f·(0.10 − r_s) < 0.033.

**Evidence:**
- The Phase IIB was open-label, with muscle pain 16% vs 5% and a 97% vs 85% surrogate result. Reduced peripheral neuropathy was also reported.
- No human mortality data support 10%.
- ~36,000 per arm are needed at 4% baseline mortality.

**GiveWell's best defense:** The 10% is conditional on a positive result, and the 40% absorbs failure worlds, so expected r is 4%.

**Why it survives:** p_success cannot absorb a discount on the effect size *within* success worlds.

**Recommended action:**
1. Ask CG whether the 10% is the mortality effect expected given surrogate or composite success.
2. Drop the Phillips/Wallis claim unless verified.

**Key unresolved question:** Is the 10% meant as the mortality effect conditional on a surrogate success?

### Finding 17: "Success" probably means a surrogate or composite endpoint, but the model needs a 10% mortality reduction, so P(adopted AND 10% mortality benefit) < P(trials succeed)

**Impact:** Break-even is at E[RR | success] ≈ 6.7%. The critique's 30–50% benefit cut is not established. This overlaps heavily with Findings 1 and 16.

**Evidence:**
- TB Fast Track (advanced HIV, all-cause mortality) was null: 19.0 vs 21.6 deaths per 100 person-years, HR 0.92.
- At 20% baseline mortality, ~6,000 per arm are still needed.
- DS-TB trial-population mortality is closer to 0.4–1.5%.
- An HDT Phase 2 trial "succeeded" on FEV₁, a surrogate.

**GiveWell's best defense:** 10% is an assumed true effect given success, not a trial-powered effect size.

**Why it survives:** The 10% is unanchored to any defined success criterion.

**Recommended action:**
1. Add a 5–10% sensitivity analysis on E[RR | success].
2. State the success endpoint.
3. Look up the Phase IIc/III primary endpoint.

**Key unresolved question:** What endpoint defines "success," and what mortality effect does it imply?

### Finding 18: The TB-specific reference classes (host-directed therapy, adjunctives, regimen-shortening) have a much worse record than 40%

**Impact:** No grounded change to the central estimate. The judge advises against lowering p_success below the 0.26 break-even on current evidence. The pipeline sensitivity low case (~1,527x, −50%) crosses the bar.

**Evidence:**
- REMoxTB, OFLOTUB and RIFAQUIN failed non-inferiority. Study 31 and SHINE succeeded.
- Dexamethasone showed RR 0.69 in TB meningitis (TBM), but ACT HIV was null (HR 0.85, P = 0.22).
- No sourced HDT class rate exists.

**GiveWell's best defense:** The 40% is a joint probability already conditioned on a positive Phase IIa/b signal.

**Why it survives:** A surrogate-positive Phase II is exactly what preceded the TB failures.

**Recommended action:**
1. Confirm CG's success definition and planned Phase III population.
2. Run targeted searches for systematic reviews of TB HDT Phase II→III outcomes.

**Key unresolved question:** What is the sourced Phase II→III→adoption rate for TB adjuncts and HDT?

### Finding 19: Reference-class check: TB Phase III trials, and the evidence package WHO may require, point to more than one trial

**Impact:** SROI exceeds 2,000x only if all-in cost stays below ~$10.8M. The critique's $30M / ~700x central estimate is discarded. Overlaps Finding 1.

**Evidence:**
- Phase III cost benchmarks: median ~$19M, ~$23M for anti-infectives, €33.9M for TB-PRACTECAL (whose cost included atypical infrastructure).
- The full range is $7–221M, so $7M is at the bottom but not impossible.

**GiveWell's best defense:** The $7M is explicitly all-in, and all-in SROI already penalizes the estimate.

**Why it survives:** The credibility of ~$6.7M for Phase III plus rollout is undemonstrated.

**Recommended action:**
1. Obtain CG's $7M breakdown and the planned Phase III design (start with the StAT-TB protocol).
2. Search for costs of pragmatic adjunct RCTs.

**Key unresolved question:** What Phase III design and budget does CG assume?

### Finding 20: The funding landscape for a generic-statin TB program makes "never" a live branch. The speedup is a poor proxy for the grant's real counterfactual.

**Impact:** Sign uncertain.
- The judge drops the critique's 20× figure.
- The judge recommends replacing the fixed 1-year speedup with E[s] = 1 − r + q(H_eff − 1).
- CG's estimate is likely understated if q ≥ ~5% and the grant's trial is not redundant.

**Evidence:**
- An active Phase II pipeline exists: StAT-TB (NIAID), StatinTB (EDCTP/NIAID), ROSETTA and ATORTUB.
- The ROSETTA null lowers class appetite.
- TAG, Unitaid and NIH RePORTER were not searched.

**GiveWell's best defense:** The 20× figure is a cost-ratio artifact, and the all-in denominator handles attribution.

**Why it survives:** The 20× figure is conceded, but neither the "never" branch nor the redundancy branch is represented in the BOTEC.

**Recommended action:**
1. Compare ATORTUB's sponsors with the CG grant. The pipeline's own evidence (Finding 3) shows NCT06199921, the registry number this critique gives for ATORTUB, lists Open Philanthropy as collaborator. This suggests ATORTUB *is* the grant's trial rather than a competitor, which should be confirmed before applying the judge's redundancy rule.
2. Search for a Phase III funding pathway.

**Key unresolved question:** Absent this grant, would a statin-TB Phase III ever be funded?

### Finding 21: Post-TB lung disease morbidity is likely the largest unvalued channel (~50–60k central, wide range)

**Impact:** ~+10% central (~55k vs ~539.5k DALY-equivalents), with a range of ~10k–300k. This is a conservative omission and does not move the headline estimate.

**Evidence:**
- Menzies 2021 puts ~5.8 of 12.1 lifetime DALYs per case in the post-TB phase.
- ROSETTA found no lung benefit on x-ray, spirometry or PET-CT, which contradicts the "lung signal" premise.
- Discounting would cut this long-tail channel materially.
- The channel overlaps with post-treatment mortality.

**GiveWell's best defense:** This is a deliberate, stated conservative simplification, and a ~10% uplift does not change the decision.

**Why it survives:** It is a real but sub-decisive omission that should be documented.

**Recommended action:**
1. Extract the Menzies YLD/YLL decomposition.
2. Identify the trial behind CG's chest X-ray lung signal.
3. Net the channel against post-treatment mortality.

**Key unresolved question:** Does atorvastatin reduce post-TB lung impairment, given the rosuvastatin null?

### Finding 22: Under-ascertained deaths push true mortality up, and the direction is the opposite of Critiques 1–2

**Impact:** About +4–8% on SROI. The +14–23% upper figures do not survive.

**Evidence:**
- Kenyan surveillance could not ascertain vital status for the 8.4% who were lost to follow-up (LTFU) or not evaluated.
- Kilifi tracing found ~10% mortality among LTFU patients. Drug-resistant TB figures (23–30%) are less applicable.
- Kenya's national "died" share is ~6%.

**GiveWell's best defense:** The 6% has no stated provenance.

**Why it survives:** Missing provenance cuts both ways: there is also no evidence that LTFU deaths are included.

**Recommended action:**
1. Confirm the citation for the 6%.
2. Check whether the Kilifi "relocated" patients had known vital status.

**Key unresolved question:** Is CG's 6% a WHO-cohort "died" share that excludes LTFU deaths?

### Finding 23: Hepatotoxicity and myopathy add a negative tail, and the combined attenuations compound

**Impact:**
- The harm tail is at most ~−0.01 on r and mostly overlaps p_success.
- Compounding reachability × shrinkage (~0.46–0.68) is bar-crossing only if the 10% applies to all on-treatment deaths with no existing discount.

**Evidence:**
- StAT-TB chose pravastatin partly for lower toxicity, and pravastatin was least toxic in THP-1/Vero cells.
- The rosuvastatin safety data are mildly reassuring but underpowered.

**GiveWell's best defense:** A drug with a visible harm signal would fail Phase II/III, so the harm tail sits in the 60% failure mass.

**Why it survives:** The harm-tail point is conceded, but the compounding question stands.

**Recommended action:**
1. Inspect whether the 10% applies to all deaths and whether it was haircut from surrogates.
2. Evaluate compounding at the portfolio level.

**Key unresolved question:** Is the 10% applied to all on-treatment deaths?

### Finding 24: Zero modeled lag between Phase III completion and adoption, and a speedup that assumes trial timing is the binding constraint

**Impact:**
- The lag alone is under 10% (3–5 years of lag → ~−6 to −10%).
- Break-even speedup is ~0.67 years in isolation, or ~0.86–0.94 years with 3–5% discounting and a 5-year lag.

**Evidence:** HPMZ was published in NEJM in May 2021 and received a WHO rapid communication in June 2021. Uptake was then constrained by cost and availability, not by WHO.

**GiveWell's best defense:** Zero lag is a stated simplification, and the 60% addresses access.

**Why it survives:** The 60% sets a level, not a timing. Whether the trial is on the critical path is unresolved.

**Recommended action:**
1. Check registries and funders for a planned or funded statin-TB Phase III.
2. Ask CG whether 1 year is an expected value or a best case.

**Key unresolved question:** Is the Phase IIc trial on the critical path to adoption?

### Finding 25: Effective delivered dose and adherence diverge from trial conditions, and programmatic dose may be lower than the trial dose, notably with rifapentine regimens

**Impact:** Unknown. The illustrative 70% adherence would cut effective uptake from 0.60 to 0.42 (−30%), but the true gap (programmatic versus trial adherence) is likely smaller. The rifapentine-specific claim was downgraded to low strength.

**Evidence:**
- The rifamycin–statin interaction is large and variable even on HRZE.
- Pravastatin AUC fell to ≤50% in 5 of 10 subjects.
- Daily rifapentine induces CYP3A4 at ~85–100% of rifampicin's level.

**GiveWell's best defense:** Dose selection under rifamycin co-treatment is the stated purpose of the grant.

**Why it survives:** That argument defends the trial, not programme delivery.

**Recommended action:**
1. Pull the Phase IIc protocol: backbone, statin duration, DOT, and adherence measurement.
2. Add an explicit relative-adherence parameter.

**Key unresolved question:** What is the ratio of programmatic to trial adherence for an out-of-FDC adjunct?

### Finding 26: The 6% is a mix of deaths, and only a fraction is reachable and modifiable by atorvastatin

**Impact:** No decomposition is applied. The judge recommends flagging that SROI falls below 2,000x if the effective addressable baseline drops by more than ~35%. Overlaps Finding 15.

**Evidence:**
- Early-death concentration: ~75% of deaths within months 1–2 in Zambia, with similar patterns in Ethiopia and Cameroon.
- In Taiwan, malnutrition-related excess mortality is confined to the first 8 weeks.
- There is double-counting risk if the 10% is a trial-derived all-cause effect.

**GiveWell's best defense:** The 10% is all-cause and already nets out unreachable deaths.

**Why it survives:** The logic is conceded only conditionally. The derivation is unknown, and trial populations exclude the sickest patients.

**Recommended action:**
1. Determine whether the 10% is surrogate-derived or an unselected all-cause assumption.
2. Then search time-to-death distributions.

**Key unresolved question:** Was the 10% derived in an unselected population?

### Finding 27: A Phase III cannot be powered on mortality, so the WHO GDG would be recommending on surrogate or composite endpoints

**Impact:** The uptake channel is unquantified. It becomes decision-relevant only if conditional WHO recommendations show a ≥1/3 uptake shortfall. The years_to_adoption and variance-only pathways were dropped.

**Evidence:**
- GRADE supports downgrading mortality evidence for indirectness.
- WHO treats unfavorable outcome (including death) as a critical outcome, so a recommendation need not stall.
- The baseline was corrected to CG's 6% (~23,400 per arm).

**GiveWell's best defense:** The BOTEC already conditions on success, and the 60% is a haircut.

**Why it survives:** "Success" is undefined, and p_success and uptake are not linked.

**Recommended action:**
1. Check CG's conditioning of the 60% and 40%.
2. Compare national uptake after conditional versus strong WHO TB recommendations.
3. Retrieve WHO "died" proportions.

**Key unresolved question:** Do conditional WHO TB recommendations produce materially lower national uptake?

### Finding 28: A global-average mortality may not match the countries where an atorvastatin adjunct would actually be deployed

**Impact:** No magnitude established. On the critique's own figures, an India-weighted mix (~4.5%) still exceeds the 3.9% break-even.

**Evidence:**
- The country figures are recalled from memory and unverified.
- Trial sites (often South Africa) may not match deployment, which is India-heavy by case share.

**GiveWell's best defense:** A global numerator matches CG's global denominator.

**Why it survives:** That argument assumes the 6% is a case-weighted global mean, which is unconfirmed.

**Recommended action:** Pull the WHO data portal "died" share for the global aggregate, the top 8 countries and South Africa, then compute the case-weighted mean.
- Close the critique if the mean is 5–7.5%.
- Escalate if it is below 4.5%.

**Key unresolved question:** What is the case-weighted on-treatment death share across deployment countries?

### Finding 29: Regulatory, pharmacovigilance and dissemination costs for an off-patent drug have no obvious payer, and the $7M likely under-budgets them

**Impact:** No adjustment. The relevant break-even lies between ~$3.8M and ~$9.5M, depending on whether the $7M is nominal or probability-weighted.

**Evidence:**
- The Phase IIC record says important questions must be answered "before a more expensive Phase III study."
- Early-phase safety data are favourable, so monitoring cost may be a guideline-driven choice.

**GiveWell's best defense:** The $7M explicitly covers guidelines and dissemination and is ~22× the $320k Phase IIc.

**Why it survives:** This is a magnitude question with thin headroom and no natural payer.

**Recommended action:**
1. Obtain the $7M derivation.
2. Search for rollout costs of BPaL/BPaLM and HPMZ.

**Key unresolved question:** What did comparable TB regimen rollouts cost, and who paid?

### Finding 30: Rifampicin induction structurally limits atorvastatin exposure in routine programs, and the trial exposure does not transfer

**Impact:** No haircut to r. Dosing-timing dependence and ART interactions are recorded as unmodeled risks.

**Evidence:**
- Separated rifampicin dosing cuts atorvastatin AUC by ~80%. Simultaneous dosing preserves or raises AUC at 7 days.
- Tipranavir/ritonavir raises atorvastatin AUC 9.4-fold.
- A popPK-PD sub-study (20/40/60 mg for 16 weeks) is registered.
- The rifapentine interaction is unverified.

**GiveWell's best defense:** The signal was generated with atorvastatin under rifampicin, so the statin-transfer worry is moot.

**Why it survives:** The statin-transfer point is conceded. Routine-program dosing timing and ART co-administration may still not reproduce trial conditions.

**Recommended action:**
1. Retrieve the ATORTUB dosing schedule relative to rifampicin.
2. Search for chronic co-administration PK data.
3. Flag the popPK-PD sub-study as the decisive input.

**Key unresolved question:** Were trial doses given simultaneously with rifampicin, and under DOT?

---

## Minor Findings (surviving strength: WEAK)

### Finding 31: Covariance between mortality and DALYs per death means the product of means is not the mean of the product

The judge declined any signed adjustment. The sign depends on how 27 was derived and how the effect distributes across strata; for example, a death-weighted GBD figure with a uniform absolute effect reverses it. Even the largest illustrative magnitude (~18%) does not cross the bar. Recommended action: state the source of 27 and whether it is death-weighted, and compare it with GBD TB YLLs divided by deaths for the deployment countries.

### Finding 32: The sweat-based diagnostic carries real option value but is speculative (~10–30k central)

The 10–30k figure is UNGROUNDED, and even at face value it moves SROI by only ~+5–14%. The verified evidence points down:
- WHO tongue-swab and near-point-of-care NAAT recommendations came in early 2026, followed by a May 2026 toolkit.
- ~100 diagnostic products are in the pipeline.

Recommended action: state the zero valuation explicitly, and confirm whether any diagnostic funding sits inside the $7M.

### Finding 33: Transmission benefit is small, with a bounded calculation (~10–30k central)

Both sides agree the channel is small (0 to ~20k weighted, roughly 0–10% of benefit). It is contingent on a culture-conversion effect that ROSETTA did not find, because most transmission precedes diagnosis. Keep it at zero with a documented note. If it is ever modelled, use ~10–12 DALYs per secondary case, consistent with Menzies, not the Advocate's 1.6.

### Finding 34: Private-sector treatment share and the reach of national guidelines are not modeled

India's private notifications are ~30–33% of the total, and more than half of patients first seek care privately. However, the critique's upper bound (15%) is below materiality and its sign is ambiguous. Over three-quarters of private providers prescribe ISTC-consistent regimens, which weakens the dosing-fidelity mechanism.
- Record this as a qualitative caveat.
- Separately flag private adoption before guidelines as an unquantified downside to speedup_years.
- Check whether the 5.5M base derives from notified or estimated treated cases.

### Finding 35: A 1-year speedup of trial results does not necessarily become a 1-year speedup of adoption, in either direction.

The BPaLM and Study 31 precedents show the WHO GDG responding within ~1–2 months of data, which supports ~1 year at the WHO stage. Retain 1 year as the central value, define the trial-result date as "available to WHO GDG," and report a 0.5–1.25 year band. The bar is crossed only below ~0.67 years. Post-WHO national and procurement lags remain untested.

### Finding 36: M72/AS01E and other incidence shocks are likely not large enough by year 8–10, but should be modelled

The context: M72's Phase IIb efficacy was 49.7% (95% CI 2.1–74.2), and its Phase III began in March 2024. Under the CEA's single-cohort year-8 structure, even the conditional −15% upper bound is sub-material, and the probability-weighted effect is likely in the low single digits. Recommended action:
1. Confirm whether 5.5M is computed after the 2%/yr decline.
2. Run a one-way sensitivity on decline_per_year over ~1–5%/yr. Open a new critique on the secular decline only if this crosses the threshold.

### Finding 37: Post-treatment excess mortality (~40–50k central) and a related sign-reversing adjustment

TB survivors have elevated long-term mortality (pooled SMR ~2.9). However, the upside (~45k) rests on three ungrounded inputs, and the downside life-expectancy adjustment is unquantified, so the net is approximately zero with uncertain sign. Make no separate adjustment. Route the upside through Finding 21 to avoid double-counting, and record the downside as a caveat on the 27 DALYs per death.

### Finding 38: The "lung benefit without mortality benefit" scenario is structurally less valuable than a simple p_success weighting implies

Under the critique's own inputs, the lung-only branch adds only ~+0.02–0.06 probability weight, which leaves ~0.45 unchanged. Record it as a structural caveat. Separately, look up the Phase IIc registered primary endpoint, which bears on what the 40% means.

### Finding 39: Unclear scope boundary for the sweat-diagnostic workstream

The sweat test appears to be an exploratory outcome inside the ATORTUB trial infrastructure, which suggests low cost. Make no adjustment. Add two yes/no clarification questions for CG:
- (a) Does the $7M include diagnostic costs?
- (b) Does the Phase III use the sweat test?

Only a "no" to (a) combined with a "yes" to (b), plus a diagnostic budget above ~$3.7M, would reopen the question.

---

## Comparison with GiveWell's AI Output

**The Baseline AI Output section of the input is empty.** Overlap therefore cannot be assessed, and the "Overlap" column is marked accordingly rather than guessed. The "What We Added" column describes what this pipeline contributed relative to a single-pass critique.

| Our Critique | Overlap with GiveWell AI Output? | What We Added |
|---|---|---|
| F1: $7M Phase III cannot be mortality-powered | Cannot assess (baseline not provided) | Own sample-size calculation; per-participant cost range; judge-bounded ≥1.3× overstatement |
| F2: Speedup vs all-in counterfactual mismatch | Cannot assess | Horizon-conditional uplift (4–20×); q × horizon design |
| F3: Delivery costs omitted from denominator | Cannot assess | Break-even per patient; convention dependence identified |
| F4: Industry base rates for p_success | Cannot assess | BIO figures verified; anti-infective uplift; judge range 0.25–0.35 |
| F5: Discounting with consistent costs | Cannot assess | Net −20/−27/−31%; bar-crossing scenario isolated |
| F6: Applicability filters on eligible pool | Cannot assess | WHO filter figures verified; confirmation restriction identified as pivotal |
| F7: Asymmetric probability weighting | Cannot assess | Bounded 1.0–1.7×; late-failure correction |
| F8: Survivor SMR shrinks 27 DALYs | Cannot assess | Romanowski SMR verified; 10–30% conditional range |
| F9: 60% uptake precedent | Cannot assess | WRD ramp data; sensitivity run (±) |
| F10: Missing adoption/funding factors | Cannot assess | Funding factor netted out; adoption bounded |
| F11: Eligibility and monitoring barriers | Cannot assess | DILI and interaction evidence; overlap warning |
| F12: Winner's curse / reference class for r | Cannot assess | Rosuvastatin null data; re-diagnosis as translation risk |
| F13: Case-count trend | Cannot assess | Notification/incidence data; corrected direction (up) |
| F14: Shorter regimens displacement | Cannot assess | Regimen landscape corrections; break-even 33–35% |
| F15: Unreachable deaths | Cannot assess | Sensitivity row; HPMZ claim removed |
| F16: Phase III success ≠ mortality result | Cannot assess | f-mixture crossing condition |
| F17: Surrogate success vs 10% mortality | Cannot assess | TB Fast Track, TBM evidence; break-even 6.7% |
| F18: TB-specific reference classes | Cannot assess | Verified TB trial history; ungrounded class rate flagged |
| F19: Phase III cost reference class | Cannot assess | Cost benchmarks; $10.8M break-even |
| F20: Funding landscape / "never" branch | Cannot assess | Pipeline map; E[s] formula; ATORTUB identity issue |
| F21: Post-TB lung disease | Cannot assess | Menzies figures; ROSETTA contradiction |
| F22: Under-ascertained deaths | Cannot assess | Kenyan LTFU data; +4–8% bound |
| F23: Harm tail and compounding | Cannot assess | Harm tail bounded to ≤−0.01; compounding isolated |
| F24: Zero lag / critical path | Cannot assess | HPMZ timeline; adjusted break-even |
| F25: Adherence and dose transfer | Cannot assess | Rifapentine claim downgraded; PK evidence |
| F26: 6% decomposition | Cannot assess | Early-death evidence; double-count condition |
| F27: WHO GDG on surrogates | Cannot assess | GRADE/WHO critical-outcome nuance; decision rule |
| F28: Deployment-weighted mortality | Cannot assess | Concrete data pull and decision rule |
| F29: Regulatory/PV costs | Cannot assess | Nominal vs expected break-even range |
| F30: Rifampicin–atorvastatin exposure | Cannot assess | Citation corrections; statin-transfer claim retracted |
| F31–F39 (weak) | Cannot assess | Mostly bounded to immaterial; converted to documentation items |

---

## Debate Quality Audit (from judge agent data)

**Total debates audited:** 39
**Sound analytical moves noted:** 101

**Failure modes detected (combined across both sides):**

| Failure type | Count |
|---|---|
| unsupported_estimate_fabricated | 16 |
| unsupported_estimate_pseudo | 33 |
| unsupported_estimate_counter | 8 |
| whataboutism | 12 |
| call_to_ignorance | 49 |
| strawmanning | 30 |
| false_definitiveness | 51 |
| generic_recommendation | 1 |
| misrepresenting_evidence_status | 32 |

**Most common Advocate failure:** false_definitiveness
**Most common Challenger failure:** call_to_ignorance

**Patterns:**
- Across both sides combined, false_definitiveness (51) and call_to_ignorance (49) were the most frequent failure modes.
- Per side, the Advocate's most common failure was false_definitiveness and the Challenger's was call_to_ignorance. The input does not provide per-side counts, so none are cited here.
- The three unsupported-estimate subtypes total 57 instances across both sides combined, and misrepresenting_evidence_status appeared 32 times combined. Together these indicate that many debates turned on numbers neither side could source.

---

## Conditional Findings (from linker output)

(no findings depend on unverified claims in this run)

## Open Questions (from Rejected Critiques input — verdict: UNVERIFIABLE)

(none — all hypotheses were either grounded or contradicted)

## Resolved Negatives (from Rejected Critiques input — verdict: REJECTED)

(none)

---

## Meta-Observations

1. **Most findings reduce to four undocumented CEA parameters.** Roughly 30 of the 39 surviving critiques hinge on the provenance of one of these:
   - **The 10% relative mortality reduction and the definition of "success":** Findings 1, 12, 15, 16, 17, 18, 23, 26, 27.
   - **The 60% uptake:** Findings 4, 6, 9, 10, 11, 14, 25, 34.
   - **The $7M all-in cost:** Findings 1, 3, 7, 19, 29, 39.
   - **The 6% baseline and 27 DALYs per death:** Findings 8, 22, 28, 31.

   A single document request to CG covering these four derivations would resolve or collapse more findings than any further red-teaming. The judge repeatedly recommended exactly such lookups.

2. **Adjustments cannot be stacked.** Many downward findings target the same slack. For example, Findings 6, 11, 14 and 34 all compete to occupy the same 40% non-uptake. Findings 15, 16, 17 and 26 all discount the same 10%. Multiplying them would heavily double-count. Conversely, Finding 2 (counterfactual framing) and Finding 7 (cost-side probability weighting) push **upward**, potentially by multiples. The single most decision-relevant structural question is therefore which counterfactual framing CG adopts, not any individual parameter haircut.

3. **One strong finding rests on weak evidence.** The only STRONG finding (Finding 1) has verifier evidence strength rated "weak." Its strength comes from a logical dilemma (a mortality-powered trial versus a surrogate-only success), not from data. This is defensible, but readers should not read STRONG as "well-evidenced."

4. **The debate audit shows the critiques are mostly about missing documentation, not demonstrated error.** The Advocate's most common failure (false_definitiveness) and the Challenger's (call_to_ignorance) are mirror images. Advocates asserted that an undocumented parameter "plausibly already absorbs" a concern. Challengers argued that the absence of documentation implies omission. Combined, these two modes account for 100 of the logged failures. This suggests the underlying critiques are structurally about undocumented CEA inputs, where neither side can win on evidence. That is consistent with Observation 1.

5. **The pipeline itself under-filtered.** The verifier rejected zero critiques. As a result, the linker had nothing to link, and the Open Questions and Resolved Negatives sections are empty. This happened even though the verifier flagged many internal claims as UNGROUNDED or retracted them (e.g., Phillips/Wallis, the HPMZ headroom claim, the "different statin" premise, Harris 2019).

   Two pipeline data issues also need attention:
   - Two candidates disappear between verification (41) and adversarial survival (39) with no record.
   - The pipeline's own evidence suggests ATORTUB (NCT06199921) is the Open Philanthropy-linked grant trial. Finding 20's redundancy test should be reconsidered in that light.

6. **No baseline comparison was possible.** Without the baseline output, this report cannot claim novelty over GiveWell's prior AI red teaming. Several critiques (p_success reference classes, surrogate endpoints, uptake optimism, discounting) are standard CEA concerns. The pipeline's clearest contributions are:
   - verified sample-size and cost arithmetic (Finding 1);
   - the counterfactual-mismatch framing with an upward direction (Finding 2);
   - explicit break-even values that let each concern be checked against the 2,000x bar.