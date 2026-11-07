# Investigation Threads: Coefficient Giving TB Statins BOTEC

## Preliminary Notes for All Investigators

**Model arithmetic.** SROI = 5.5M × 0.60 × 0.06 × 0.10 × 1 yr × 27 × $OP 100,000 ÷ $7M × 0.40 ≈ 3,055x.

Every parameter except `all_in_cost` enters multiplicatively and linearly. So:

- A single multiplicative parameter must fall about 34.5% (to 0.655× baseline) to push SROI below the 2,000x bar.
- A ±25% change in any single multiplicative parameter is the materiality threshold.
- `all_in_cost` enters inversely. SROI falls 25% (to about 2,290x) if costs reach about $9.3M. SROI crosses the bar at about $10.7M.
- Additive benefits that are not modeled, such as morbidity, are material if they add or subtract at least 25% of the $OP 53.5B benefit, which is about $OP 13B.

**Formula quirk.** `years_to_adoption` enters only through the exponent (years − 8), and the model has no discounting. Changing the adoption date therefore changes only the population, not the value of time. This is relevant to Thread 3.

**Exclusion baseline.** CG publishes no prior AI red teaming. CG's text states its assumptions openly: 2% decline, constant treatment share, 96% drug-susceptible (DS), 60% uptake, 40% joint success, 4.5% funder share, no discounting, and only mortality valued. Investigators must not simply restate that these are assumptions or that the BOTEC is rough. A finding must bring evidence that a value is wrong and quantify the effect on SROI.

---

## THREAD 1: Translating surrogate endpoints into a 10% mortality reduction, and coherence with p_success

**SCOPE:** The Phase IIa/b trial CG cites measured culture clearance and chest X-ray lung damage, not mortality. This thread asks four questions:
1. Is a 10% relative reduction in on-treatment mortality a defensible expectation, given the surrogate results and what host-directed therapies (HDTs) have historically shown?
2. Is the 10% conditional on "success", or unconditional? If the 40% `p_success` already encodes "the effect is real," then 10% may be an inflated conditional estimate, or an expected value has been double-applied.
3. Is atorvastatin likely to affect the kinds of TB deaths that occur? Many on-treatment deaths happen early, in advanced, HIV-coinfected, or late-presenting patients, before an anti-inflammatory or bacterial-clearance adjunct could plausibly act.
4. Does rifampicin, a strong CYP3A4/OATP inducer, materially cut atorvastatin exposure in a way that weakens real-world effect? The IIc dosing work exists partly for this reason.

**KEY PARAMETERS:** `relative_reduction` (0.10), `p_success` (0.40), and secondarily `baseline_mortality` (0.06), which is the portion of mortality that is modifiable.

**WHAT CG ALREADY ACCOUNTS FOR:**
- A 40% joint probability that Phase II and III succeed.
- An effect size framed as an assumption conditional on a positive result ("a positive result is assumed to cut that by 10%").
- Dosing optimization is part of the funded trial's purpose.

**WHAT CG DOES NOT ACCOUNT FOR:**
- No explicit link from surrogate to mortality.
- No winner's-curse shrinkage from the IIa/b effect.
- No breakdown of deaths by timing or cause, to identify which are modifiable.
- No distinction between "success on surrogate/efficacy endpoints" and "demonstrated mortality benefit". This distinction matters for what guideline bodies will accept.
- No modeling of the drug–drug interaction with rifampicin.
- No modeling of the HIV/ART interactions that apply to a large share of deaths, particularly with boosted protease inhibitors. Interactions with dolutegravir regimens are minimal.

**DATA SOURCES TO EXAMINE:**
- The Phase IIa/b atorvastatin–TB trial CG references. Identify it exactly; likely the StAT-TB program, South Africa. Examine effect sizes, confidence intervals, sample size, and whether the trial was powered for its endpoints.
- Observational statin–TB cohorts, such as Taiwanese and Korean claims data and diabetic cohorts. These suggest lower TB incidence or mortality among statin users but are prone to healthy-user bias.
- Meta-analyses of host-directed therapies (e.g., Wallis & Hafner, *Nat Rev Immunol*), plus corticosteroid trials in TB meningitis and pericarditis, as precedents for how often adjunct effects on surrogates translate into effects on mortality.
- Pharmacokinetic studies of rifampicin–atorvastatin interaction (e.g., Backman et al. 2005, which found large AUC reductions with co-administration).
- WHO Global TB Report treatment-outcome data, and cohort studies on the timing of on-treatment deaths (for example, the share occurring in the first 2 months).
- Base rates of Phase II→III success for repurposed or adjunctive drugs in infectious disease (e.g., BIO/Informa clinical success-rate reports).

**MATERIALITY THRESHOLD:**
- `relative_reduction` below 0.0655 pushes SROI below 2,000x.
- ±0.025 (to 0.075 or 0.125) is a ±25% change.
- `p_success` below 0.262 crosses the bar.
- If only about 50% of on-treatment deaths are plausibly modifiable, and the effect on those is 10%, the effective reduction is 0.05. That alone gives about 1,530x.

**KNOWN CONCERNS ALREADY SURFACED (exclude):**
- That the trial may fail. This is already priced in at 60%.
- That 10% is "an assumption". CG says so. The investigator must provide an evidence-based alternative value.

---

## THREAD 2: Realism of the $7M all-in cost, given what a Phase III would need to show

**SCOPE:** This thread tests whether $7M can plausibly cover Phase III trials, guideline change, dissemination, and validation.

A rough power calculation shows the problem. Detecting a reduction from 6.0% to 5.4% mortality (α = 0.05, 80% power) needs about 23,000 participants per arm, roughly 47,000 in total. At typical TB trial costs per participant, that is far above $7M.

This leaves two possibilities:
- **(a)** Phase III is powered on surrogate or composite endpoints. Mortality benefit would then remain unproven at guideline time, which affects whether WHO adopts and, if so, how fast (links to Threads 1 and 5).
- **(b)** The all-in cost is understated by a large multiple.

The thread should also check whether the $7M includes the sweat-diagnostic workstream (which would mean cost is counted with no matching benefit). It should also ask how many Phase III trials, sites, and populations (HIV+ and HIV−, multiple regions) WHO would want.

**KEY PARAMETERS:** `all_in_cost` ($7M), `p_success` (whether the endpoint is powerable at all), and `speedup_years` (trial duration).

**WHAT CG ALREADY ACCOUNTS FOR:**
- All-in costs are included through Phase III, guideline change, dissemination, and validation.
- SROI is computed on all-in costs and all-in benefits, with CG's 4.5% share noted.

**WHAT CG DOES NOT ACCOUNT FOR:**
- No line-item breakdown.
- No statement of the Phase III sample size, endpoint, or cost per participant.
- No allowance for cost overruns or extra confirmatory trials.
- Health-system costs of delivering the drug are not counted. Atorvastatin for 6 months × 3.3M patients is likely small but should be confirmed.

**DATA SOURCES TO EXAMINE:**
- Published costs and sample sizes of recent TB Phase III trials: Study 31/A5349 (rifapentine–moxifloxacin, about 2,500 participants), TRUNCATE-TB, SimpliciTB, REMoxTB, and the RIFASHORT trial.
- Cost per participant estimates for TB trials (e.g., TAG pipeline reports, Treatment Action Group R&D funding reports).
- Trial registries (ClinicalTrials.gov, PACTR) for the Phase IIc design and any planned Phase III.
- WHO guideline-development handbooks on the evidence certainty needed for adjunctive therapy recommendations.

**MATERIALITY THRESHOLD:**
- All-in cost ≥ $9.3M is a −25% change.
- All-in cost ≥ $10.7M falls below the bar.
- A mortality-powered Phase III at even $500 per participant (about $24M) would give SROI ≤ about 900x.

**KNOWN CONCERNS ALREADY SURFACED (exclude):**
- CG's 4.5% attribution share. The method already scales correctly by using all-in figures, so the investigator should not re-argue the attribution logic itself.

---

## THREAD 3 (Structural/Methodological): The counterfactual speedup framework, benefit horizon, and time treatment

**SCOPE:** The entire benefit equals one year of full-scale benefit, credited 8+ years in the future, with no discounting. This thread examines whether that framework is systematically biased. Bias could run either way.

**Downward pressures:**
- Real adoption ramps up over time. A one-year shift of an S-curve equals one plateau-year of benefit only over an infinite, undisturbed horizon.
- Competing developments could shrink or end the benefit window before then:
  - the M72/AS01E vaccine, with Phase III results expected around 2028, which could cut incidence;
  - shorter regimens;
  - other HDTs;
  - faster decline in TB incidence.
- CG's own frameworks elsewhere apply some discount for "things changing".
- There is a question of whether a $320k trial (4.5% of costs) causes a full year's acceleration of the whole pathway, or whether others would fund it anyway.

**Upward pressures:**
- If no one else would test atorvastatin, the counterfactual may be "never adopted" or "much later". The benefit would then be several years of benefit, not one.

The thread should also flag the `years_to_adoption` quirk noted in the preliminary notes, and check whether the formula chain treats correlated uncertainties as a product of point estimates. For example, effect size and p_success are plausibly correlated.

**KEY PARAMETERS:** `speedup_years` (1), `years_to_adoption` (8), `decline_per_year` (0.02), and the implicit discount rate (0).

**WHAT CG ALREADY ACCOUNTS FOR:**
- Explicit 1-year speedup.
- Population decline of 2% per year until adoption.
- The formula notes state that no time discounting is used.

**WHAT CG DOES NOT ACCOUNT FOR:**
- No adoption ramp.
- No finite horizon and no risk that a competing technology arrives.
- No justification for the 1-year figure, such as a funding-landscape analysis.
- No discounting, whether for pure time or for "civilizational change".
- No uncertainty distribution; the estimate is a point estimate only.

**DATA SOURCES TO EXAMINE:**
- CG/Open Philanthropy's published guidance on discounting in GHW (e.g., the "technical updates to our global health and wellbeing cause prioritization framework" posts), to see whether this BOTEC departs from house methodology.
- TB pipeline reports from the Stop TB Working Group on New