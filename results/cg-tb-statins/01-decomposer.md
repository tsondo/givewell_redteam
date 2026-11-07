# Investigation Threads: Coefficient Giving TB Statins BOTEC

## Preliminary: Model Arithmetic for Materiality

SROI = eligible × adult_uptake × baseline_mortality × relative_reduction × dalys_per_death × op_per_daly × speedup_years × p_success / all_in_cost. The baseline replica gives **3,055x**.

The model is purely multiplicative, so every parameter except `all_in_cost` scales SROI proportionally. A 25% change in any one parameter moves SROI by 25%.

- **Falling below the 2,000x bar** requires the product of all changes to reach ×0.655. That means a 34.5% cut in any single numerator parameter, or a 52.7% increase in `all_in_cost`.
- **Single-parameter break-even values:**

| Parameter | Base | Break-even |
|---|---|---|
| relative_reduction | 0.10 | 0.065 |
| p_success | 0.40 | 0.26 |
| adult_uptake | 0.60 | 0.39 |
| speedup_years | 1.0 | 0.65 |
| baseline_mortality | 0.06 | 0.039 |
| dalys_per_death | 27 | 17.7 |
| eligible | 5.5M | 3.6M |
| all_in_cost | $7.0M | $10.7M |

- **Compounding:** moderate cuts in two parameters, for example −20% each, give ×0.64 and drop SROI below the bar. Investigators should report findings as multipliers so they can be combined.
- **No prior CG red teaming exists.** The exclusion lists below therefore contain only the assumptions and caveats CG states explicitly. Restating that an explicit assumption is "uncertain" is not a finding. A finding must say which direction the parameter moves, by how much, and on what evidence.

---

```
THREAD 1: Mortality effect of adjunctive atorvastatin (relative_reduction) —
surrogate-to-mortality translation, pharmacology under rifampicin, and
effect size conditional on "success"

SCOPE: The prior Phase IIa/b evidence concerns infection clearance (sputum
culture conversion) and radiographic lung damage. It does not concern
mortality. This thread asks whether a 10% relative reduction in mortality
during treatment is a credible expected effect, conditional on the trials
"succeeding." It covers four questions:
(a) What the prior trial actually measured and found, including which
    statin was tested. Verify whether it was atorvastatin or another statin
    (e.g., the StAT-TB rosuvastatin trial or pravastatin Phase 2a work).
    Assess whether the result transfers across statins.
(b) Whether faster culture conversion or less CXR damage plausibly lowers
    on-treatment death. Most deaths among treated DS-TB patients occur
    early, in HIV-positive, elderly, malnourished, or late-presenting
    patients. Many are driven by comorbidity or advanced disease, which a
    host-directed therapy acting over weeks may not touch.
(c) Pharmacokinetics. Rifampicin is a strong CYP3A4/OATP1B1 inducer and
    substantially reduces atorvastatin exposure, especially when dosing is
    staggered. Achievable exposure in routine programs may be well below
    trial exposure. Conversely, interactions with some ART regimens may
    raise toxicity risk.
(d) Winner's curse. Assess the effect size expected conditional on passing
    Phase III, especially if Phase III is powered on a surrogate endpoint.

KEY PARAMETERS: relative_reduction (primary). Secondary: the joint
distribution of relative_reduction and p_success, which is currently
modeled as independent.

WHAT GIVEWELL (CG) ALREADY ACCOUNTS FOR: CG assumes a 10% relative
mortality reduction conditional on a positive result. It discounts by a 40%
probability that Phase II and III both succeed, so the expected relative
reduction is 4%. The Phase IIc trial is described as testing "dosing
strategies for survival, infection clearance and lung damage." This
implicitly acknowledges that dosing and the mortality endpoint are
unresolved.

WHAT GIVEWELL (CG) DOES NOT ACCOUNT FOR:
- No stated derivation of the 10% figure from the prior trial's effect on
  surrogates.
- No adjustment for the share of deaths plausibly unreachable by
  adjunctive therapy (e.g., deaths in the first 2–4 weeks, or deaths from
  HIV/other comorbidity).
- No consideration of rifampicin-induced reduction in statin exposure.
- No consideration of whether newer/shorter regimens (4-month HPMZ)
  change the room for adjunctive benefit.
- No possibility of zero or negative effect, e.g., added hepatotoxicity
  alongside isoniazid/rifampicin/pyrazinamide, or myopathy.
- No discussion of whether "success" means a mortality benefit or a
  surrogate benefit.

DATA SOURCES TO EXAMINE:
- The specific Phase IIa/b trial CG references. Identify it, record its
  primary endpoint, effect size, CI, sample size, population, and statin.
- Phase IIc protocol/registry entry: ClinicalTrials.gov / PACTR / ISRCTN.
- FDA/EMA atorvastatin label and PK studies of rifampicin–atorvastatin
  co-administration.
- Observational cohorts on statin use and TB outcomes/mortality (e.g.,
  Taiwanese and Korean national insurance cohorts) and meta-analyses
  thereof. Note healthy-user bias.
- Literature on surrogate validity in TB, i.e., how well 2-month culture
  conversion predicts relapse and mortality (e.g., Phillips et al.;
  Wallis et al.).
- Systematic reviews on the timing and causes of death during TB
  treatment (e.g., Waitt & Squire 2011 on early deaths).
- Results of other host-directed therapy trials in TB (metformin, CC-11050,
  everolimus, vitamin D) as a reference class for surrogate-positive /
  outcome-null patterns.

MATERIALITY THRESHOLD: SROI is linear in relative_reduction.
- A conditional effect below 0.065 (vs 0.10) pushes SROI below 2,000x.
- Any change beyond ±0.025 (to <0.075 or >0.125) is a >25% move.
- If the investigator concludes that roughly a third or more of on-treatment
  deaths are unreachable, and the effect among reachable deaths is ~10%,
  that alone is near-material.
- If the conditional mortality effect is plausibly zero in a substantial
  probability mass (e.g., success is defined on surrogates), express this
  as an expected-value multiplier on relative_reduction × p_success.

KNOWN CONCERNS ALREADY SURFACED (exclusion list):
- That the effect "might not replicate" in general terms. This is already
  captured by p_success = 0.40.
- That the 10% figure is an assumption. CG states it as one.
- The need for dose-finding, which is the stated purpose of the Phase IIc
  trial. Raising it is not new. Showing that rifampicin interaction
  structurally limits achievable exposure in programmatic use is new.
```

```
THREAD 2: Realism of all-in cost (all_in_cost) — Phase III trial size,
downstream drug and delivery costs, and costs excluded from the denominator

SCOPE: CG puts the all-in cost of reaching adoption at ~$7M, covering
Phase IIc, Phase III, guideline change, dissemination, and validation. This
thread tests that figure against three things:
(a) The size and cost of a Phase III trial capable of supporting WHO
    guideline adoption. A trial powered to detect 6.0% → 5.4% mortality
    (80% power, α=0.05, two-sided) needs roughly 23,000 per arm, about
    47,000 patients. Even a trial powered on a surrogate or composite
    unfavorable-outcome endpoint typically costs tens of millions of
    dollars in TB (benchmarks: TBTC Study 31/A5349, TRUNCATE-TB, SimpliciTB,
    RIFASHORT).
(b) The incremental cost of actually delivering atorvastatin to ~3.3M
    patients in the speedup year. This includes drug procurement for
    ~4–6 months at generic prices, liver-function or safety monitoring if
    required by guidelines, and program delivery costs. CG's framework
    usually weighs other actors' spending at its counterfactual value.
(c) Other costs: WHO Guideline Development Group processes, national
    guideline revisions, and training.
The thread should also ask whether CG's choice of a $7M denominator is
internally consistent with its 4.5% credit share, which is ~$315k, roughly
the current trial cost.

KEY PARAMETERS: all_in_cost (primary). Interacts with p_success, since a
cheap Phase III implies a surrogate endpoint and weaker mortality evidence
(Thread 1).

WHAT GIVEWELL (CG) ALREADY ACCOUNTS FOR: The $7M figure explicitly
includes "later Phase III trials, guideline changes, dissemination and
validation." CG computes SROI on all-in costs and all-in benefits rather
than its own share.

WHAT GIVEWELL (CG) DOES NOT ACCOUNT FOR:
- No breakdown of the $7M.
- No reconciliation with typical TB Phase III costs.
- No discussion of what endpoint a $7M-budget Phase III could be powered
  on.
- No costs of delivering the drug: procurement, monitoring, health-worker
  time.
- No costs of managing adverse events.
- No account of who bears delivery costs (governments, Global Fund) and at
  what counterfactual value.
- Sweat-diagnostic workstream costs: it is unclear whether these sit
  inside the $7M.

DATA SOURCES TO EXAMINE:
- Published or reported budgets for TB Phase III trials (TBTC/ACTG Study
  31, TRUNCATE-TB, STREAM, endTB, SimpliciTB). Use funder disclosures from
  NIH RePORTER, EDCTP, Unitaid, and the Gates Foundation.
- Treatment Action Group annual TB R&D funding reports, for trial-level
  cost benchmarks.
- Stop TB Partnership Global Drug Facility catalog and MSH International
  Medical Products Price Guide for generic atorvastatin unit prices.
- WHO consolidated TB treatment guidelines and GDG evidence requirements.
- CG/Open Philanthropy statements on how they weight other actors'
  spending (leverage/funging conventions).

MATERIALITY THRESHOLD:
- SROI ∝ 1/all_in_cost. All-in cost above ~$10.7M (+53%) drops SROI below
  2,000x. Cost above $9.3M (+33%) is a >25% decline.
- A realistic mortality-powered Phase III would likely raise costs by a
  multiple, not a percentage.
- Drug delivery alone at ~$1–10 per course × 3.3M patients is ~$3–33M for
  the credited speedup year. Even after a substantial counterfactual-value
  discount on government spending, this could exceed the bar threshold.
- Report a central cost estimate and the implied SROI multiplier.

KNOWN CONCERNS ALREADY SURFACED (exclusion list):
- That the current trial is only $320k and that later trials cost more.
  CG already includes later trials in the $7M.
- That CG funds only ~4.5% of costs. CG explicitly addresses this by
  using all-in cost and benefit.
```

```
THREAD 3: Structural — counterfactual definition of "speedup," attribution
consistency, and absence of time discounting

SCOPE: This thread examines whether the BOTEC's framework is internally
coherent. It has three parts.

(a) Counterfactual inconsistency. Benefit equals ONE year of deaths averted
    (speedup_years = 1), which implies the counterfactual is "the same
    pathway happens one year later." Cost equals the entire $7M pathway,
    which implies the counterfactual is "none of this spending happens."
    Under the first framing, the grant's counterfactual cost is roughly
    $320k plus the time value of pulling ~$6.7M of downstream spending
    forward a year. SROI would then be far higher. Under the second
    framing, the benefit is all future years of adoption, also far higher,
    but the counterfactual must then justify why no one else would ever
    run the trial. A consistent framing could move SROI substantially in
    either direction. The investigator should derive the coherent
    estimate(s) and say which framing best fits the actual funding
    landscape.
(b) Plausibility of a 1-year speedup from a $320k Phase IIc. The question
    is whether other funders (NIH, EDCTP, Unitaid, Gates, national
    agencies) would have funded the same or an equivalent study, and how
    quickly.
(c) Time discounting. The formula applies none. Benefits begin ~8–9 years
    after the grant. CG has published discounting conventions for GHW
    work; check whether they apply. Also consider whether a 1-year shift
    of an adoption S-curve credits the full plateau-level benefit only
    under no discounting. With discounting, the benefit of shifting is
    concentrated on the early, low-uptake portion.

KEY PARAMETERS: speedup_years, all_in_cost (as a counterfactual
denominator), years_to_adoption (timing of benefits), and the implicit
discount rate (currently 0).

WHAT GIVEWELL (CG) ALREADY ACCOUNTS FOR: CG credits a 1-year acceleration
and computes SROI on all-in benefits and costs. It states its share is
~4.5% and credits itself with ~4.5% of benefits. The formula notes "No
time discounting."

WHAT GIVEWELL (CG) DOES NOT ACCOUNT FOR:
- No justification for 1 year rather than some other speedup.
- No reconciliation of the speedup framing with the all-in cost framing.
- No discounting.
- No treatment of the adoption-curve shape and how it interacts with
  discounting.
- No consideration of whether the counterfactual pathway would be faster
  or slower with other funders.

DATA SOURCES TO EXAMINE:
- Coefficient Giving / Open Philanthropy published methodology: "How we
  use BOTECs" (May 2025), GHW cause-prioritization framework posts, and
  any statements on discount rates and on R&D speedup valuation.
- Treatment Action Group pipeline reports and the Working Group on New TB
  Drugs pipeline, to assess whether competing funders are pursuing
  statin/host-directed therapy trials.
- Literature on R&D acceleration valuation, e.g., health-economics
  treatments of "bringing forward" an innovation; GiveWell's and Founders
  Pledge's approaches to R&D BOTECs.
- Trial registries for other planned or ongoing statin-TB trials.

MATERIALITY THRESHOLD:
- Discounting benefits arriving ~8–9 years out:
  - 3%/yr gives ×0.77–0.79, about 2,350–2,410x (−21% to −23%).
  - 4% gives ×0.70–0.73, about 2,150–2,230x.
  - 5% gives ×0.64–0.68, about 1,970–2,070x. This crosses or approaches
    the bar.
- Speedup below 0.65 years is below the bar.
- A coherent counterfactual reframing could change SROI by an order of
  magnitude in either direction. Any well-supported reframing that changes
  the effective cost or benefit attributed by >25% is material.

KNOWN CONCERNS ALREADY SURFACED (exclusion list):
- That the speedup is an assumption. CG states it as one.
- That CG funds a small share of total costs. CG explicitly handles this
  via the all-in approach. Raising the share alone is not new. Showing the
  speedup and all-in framings are mutually inconsistent is new.
- "No time discounting" is stated in the formula notes. Merely noting the
  absence is not a finding. Quantifying the effect under CG's own
  conventions is.
```

```
THREAD 4: Unvalued benefits — post-TB lung disease, long-term post-treatment
mortality, transmission, and the diagnostic workstream (upside thread)

SCOPE: The BOTEC values only on-treatment mortality reduction. The prior
trial's most direct signals, however, were reduced lung damage and faster
clearance. This thread estimates value from four channels CG does not
model:
(a) Post-TB lung disease morbidity. Reduced cavitation and fibrosis could
    lower the burden of chronic obstructive or restrictive lung disease,
    bronchiectasis, and disability in TB survivors.
(b) Post-treatment excess mortality. TB survivors have elevated long-term
    all-cause mortality, much of it respiratory or cardiovascular. Statins
    also carry their own cardiovascular benefit during the course, though
    a ~6-month course limits this.
(c) Transmission. Faster culture conversion may shorten infectious
    periods. The effect is likely small, since most transmission occurs
    before diagnosis.
(d) The sweat-based TB diagnostic work funded alongside the trial, which
    the BOTEC assigns zero value.
These are probability-weighted by the same p_success, and by the
probability that the surrogate benefits hold even if the mortality benefit
does not.

KEY PARAMETERS: Adds new benefit terms to the formula chain. Currently
implicit zeros: morbidity DALYs, post-treatment mortality DALYs,
transmission-averted cases, and diagnostic value. Interacts with
relative_reduction and p_success.

WHAT GIVEWELL (CG) ALREADY ACCOUNTS FOR: The formula notes "only
mortality is valued." The context mentions reduced lung damage on chest
X-ray and the sweat-based diagnostic, but neither enters the calculation.

WHAT GIVEWELL (CG) DOES NOT ACCOUNT FOR: All four channels above. In
particular, the possibility that the intervention's main value is in
morbidity and long-term survival rather than on-treatment deaths. This
could make the estimate robust even if Thread 1 finds a small on-treatment
mortality effect.

DATA SOURCES TO EXAMINE:
- Menzies et al. 2021 (Lancet Global Health), lifetime burden of incident
  TB including post-TB disease. Their estimate attributes a large share
  of lifetime TB DALYs to post-TB sequelae; verify the exact proportion.
- Romanowski et al. 2019 (Lancet Infectious Diseases), long-term all-cause
  mortality after TB treatment.
- Allwood et al. and the International Post-TB Symposium consensus on
  post-TB lung disease prevalence and disability weights.
- GBD disability weights for chronic respiratory conditions.
- The prior trial's CXR/lung-function outcomes and any follow-up data.
- Transmission modeling literature on the infectious period after
  treatment start (e.g., studies of rapid infectiousness decline on
  effective therapy).
- Any public description of the sweat-based diagnostic's development
  stage.

MATERIALITY THRESHOLD: Current benefit is ~535k DALYs. Unvalued benefits
are material (>25% upside) if they add ≥~134k DALYs per adoption-year,
probability-weighted on the same basis. For example, averting ~0.3
DALYs of post-TB morbidity and excess mortality per treated patient across
3.3M patients × 10% of patients experiencing a meaningful benefit gives
~100k DALYs. The investigator should report a central estimate with
explicit assumptions. Upside findings are as decision-relevant as downside
ones.

KNOWN CONCERNS ALREADY SURFACED (exclusion list):
- That the model values only mortality. This is stated in the formula
  notes. Noting the omission is not a finding. Quantifying the omitted
  value is.
```

```
THREAD 5: Implementation — trial execution, guideline adoption pathway,
and real-world uptake (adult_uptake, years_to_adoption)

SCOPE: This thread asks whether the program as it would actually unfold
matches the program as modeled. It covers:
(a) Trial execution risk for the Phase IIc: recruitment, sites, and
    follow-up in high-burden settings.
(b) The adoption pathway. What evidence the WHO GDG needs to recommend an
    adjunctive host-directed therapy, typical lags from Phase III
    publication to WHO recommendation to national guideline adoption to
    procurement, and whether 8 years from grant to adoption is realistic.
(c) Uptake. Whether 60% of adult DS-TB patients would actually receive
    atorvastatin. Relevant precedents include uptake curves for comparable
    TB program additions: the 4-month HPMZ regimen, Xpert rollout, and
    adjunctive pyridoxine or nutritional support. Relevant barriers
    include pill burden, liver-function monitoring requirements,
    treatment of patients in the private sector (large in India, Indonesia,
    Pakistan, Philippines), contraindications, and drug–drug interactions
    with ART. Also consider whether uptake would be faster or slower than
    assumed, given that atorvastatin is already on essential medicines
    lists.
(d) Adherence. Whether patients who are prescribed atorvastatin take it
    at the effective dose and duration.

KEY PARAMETERS: adult_uptake (primary), years_to_adoption, speedup_years
(via how the adoption curve shape interacts with a 1-year shift; coordinate
with Thread 3 on discounting), and the effective dose actually delivered
(interacts with relative_reduction in Thread 1).

WHAT GIVEWELL (CG) ALREADY ACCOUNTS FOR: CG assumes 60% of adult
patients would add atorvastatin "if it works," justified by it being
"generic and cheap." It assumes a Phase III finishes 8 years after the
grant and that the share of cases being treated stays constant.

WHAT GIVEWELL (CG) DOES NOT ACCOUNT FOR:
- No adoption-lag modeling after Phase III.
- No private-sector treatment share.
- No monitoring requirements.
- No adherence.
- No empirical precedent for 60% uptake.
- No account that uptake ramps over years rather than jumping to 60%.

DATA SOURCES TO EXAMINE:
- WHO Global TB Report: notifications, and public vs private sector
  shares by country.
- Documented rollout timelines for the WHO 2022 4-month HPMZ regimen and
  for Xpert MTB/RIF (Albert et al.; Cazabon et al.).
- WHO GDG methodology and handbook (GRADE requirements).
- India's Ni-kshay data on private-sector notification and adherence.
- Evidence on adherence to adjunctive or non-TB medications during TB
  treatment.
- Statin-safety guidance on co-administration with TB drugs and ART
  (Liverpool HIV/TB drug interaction database).
- Trial registry entry and timelines for the Phase IIc.

MATERIALITY THRESHOLD:
- adult_uptake below 0.39 drops SROI below 2,000x. A ±0.15 change is a
  >25% move.
- Adherence-adjusted effective uptake: 60% prescribed × 70% adherent at an
  effective dose gives 0.42, roughly ×0.70. That is near-material alone
  and material when combined.
- A longer years_to_adoption mainly matters through discounting (Thread 3)
  and incidence decline. Each extra year changes eligible by ~2% under
  the current formula, which is not material alone.

KNOWN CONCERNS ALREADY SURFACED (exclusion list):
- That 60% uptake is assumed. CG states this with its justification.
- That 8 years to Phase III completion is assumed.
- That the share of cases treated is held constant. This is an explicit
  assumption.
```

```
THREAD 6: Who dies and how many healthy years are lost —
baseline_mortality and dalys_per_death among eligible adult DS-TB patients

SCOPE: This thread tests the 6% on-treatment mortality figure and the 27
DALYs per death against the population that would actually receive
atorvastatin. It covers:
(a) Whether 6% refers to deaths among all notified DS-TB patients, among
    adults only, or includes deaths before treatment start. Also how
    WHO-reported "died" outcomes compare with deaths among patients
    lost to follow-up or not evaluated, which are under-ascertained.
(b) The composition of deaths by HIV status, age, and timing, and how
    this compares with the subpopulation that would actually be
    prescribed atorvastatin. Coordinate with Thread 1 on reachability; this
    thread owns the descriptive epidemiology.
(c) DALYs per death. Assess the age distribution of on-treatment TB deaths
    in high-burden countries, remaining healthy life expectancy at those
    ages, and the adjustment for TB survivors' elevated subsequent
    mortality (lower residual life expectancy), and for HIV and other
    comorbidities among those who die.

KEY PARAMETERS: baseline_mortality, dalys_per_death.

WHAT GIVEWELL (CG) ALREADY ACCOUNTS FOR: CG uses ~6% mortality among
treated drug-susceptible patients and 27 DALYs per TB death, described as
remaining healthy life expectancy.

WHAT GIVEWELL (CG) DOES NOT ACCOUNT FOR:
- No adjustment for survivors' excess mortality reducing the years gained
  per death averted.
- No age or comorbidity weighting.
- No distinction between notified-cohort mortality and true mortality,
  including unascertained deaths. These could raise baseline_mortality.
- No decomposition of how much of the 6% sits in subgroups excluded from
  or contraindicated for statin use.

DATA SOURCES TO EXAMINE:
- WHO Global TB Report treatment outcome tables for new and relapse DS-TB
  cohorts, by region and HIV status.
- GBD 2021 TB deaths and YLLs by age and country. Compute YLL per death
  for HIV-negative and HIV-positive TB.
- Romanowski et al. 2019 for survivor mortality SMRs.
- Country cohort studies (India, South Africa, Indonesia, Nigeria) on
  timing and predictors of on-treatment death.
- Studies on deaths among patients lost to follow-up, to gauge
  under-ascertainment.

MATERIALITY THRESHOLD:
- baseline_mortality below 0.039 or dalys_per_death below 17.7 each alone
  drop SROI below the bar.
- A combined downward adjustment of ~20% to each is ×0.64, below the bar.
- Upward revisions are equally relevant. For example, true mortality of
  8% would raise SROI by 33%.

KNOWN CONCERNS ALREADY SURFACED (exclusion list):
- None beyond the stated parameter values themselves.
```

```
THREAD 7: Probability of success (p_success) — base rates and the
definition of "success"

SCOPE: This thread examines whether 40% for "Phase II and Phase III both
succeed" is consistent with reference classes. These include clinical
development phase-transition rates (overall, infectious disease, and
repurposed or generic drugs), the track record of host-directed therapies
for TB, and the track record of TB adjunctive therapies. It also examines
what "success" must mean for the model to be coherent: success must lead
to guideline adoption at 60% uptake AND deliver the 10% mortality benefit.
If success can be declared on surrogate endpoints, then P(adopted AND
effective on mortality) may be lower than P(trials succeed). That
reconciliation is coordinated with Thread 1.

KEY PARAMETERS: p_success (primary), and the joint distribution of
p_success and relative_reduction.

WHAT GIVEWELL (CG) ALREADY ACCOUNTS FOR: CG uses a 40% probability that
both Phase II and Phase III succeed.

WHAT GIVEWELL (CG) DOES NOT ACCOUNT FOR:
- No stated reference class.
- No separation of probabilities for Phase IIc success, Phase III
  success, and adoption given success.
- No definition of success.
- No probability that a successful Phase III still fails to produce WHO
  adoption. Adoption may be partly captured in uptake, but this is not
  explicit.

DATA SOURCES TO EXAMINE:
- BIO/Informa/QLS 2021 "Clinical Development Success Rates" (phase
  transitions by therapeutic area).
- Wong, Siah & Lo 2019 (Biostatistics) on phase success probabilities.
- Repurposed-drug success-rate literature.
- Reviews of TB host-directed therapy trials (e.g., Wallis & Hafner;
  Kolloli & Subbian), and the outcomes of completed HDT trials.
- Prior statin-TB trial results, including any null results.

MATERIALITY THRESHOLD:
- p_success below 0.26 drops SROI below the bar. A change of ±0.10 is a
  >25% move.
- Reference-class rates for Phase II→approval are commonly ~15–30%. This
  would place p_success near or below the break-even value unless
  repurposing or generic status justifies a premium.
- Report the decomposition P(IIc) × P(III | IIc) × P(adoption | III).

KNOWN CONCERNS ALREADY SURFACED (exclusion list):
- That 40% is a subjective estimate. CG states it as one.
```

```
THREAD 8: Eligible population and the future TB landscape
(eligible_people_at_8y, decline_per_year)

SCOPE: This thread reconstructs the 5.5M figure and asks how the
treatment and epidemiological landscape ~8–10 years out affects it.
(a) Reconstruction. Start from current notifications (~8M in recent WHO
    reports). Apply the 96% DS share, the 2%/yr decline over 8 years, and
    the adult share. Check that the arithmetic reproduces ~5.5M and
    identify which baseline CG used.
(b) Incidence trajectory. Assess whether a 2%/yr decline is realistic.
    Consider post-COVID rebound, notification gains from case-finding,
    and possible incidence reductions from new vaccines. The M72/AS01E
    Phase III is expected to read out in the late 2020s; a successful
    vaccine could substantially lower incidence in the 2030s, when the
    speedup benefit accrues.
(c) Treatment landscape. Assess whether shorter regimens, new drugs, or
    other host-directed therapies would reduce the incremental value of
    atorvastatin or require re-trialing alongside new regimens. This
    effectively truncates or reduces the eligible population.

KEY PARAMETERS: eligible_people_at_8y, decline_per_year,
years_to_adoption (via the decline exponent).

WHAT GIVEWELL (CG) ALREADY ACCOUNTS FOR: CG assumes a 2% annual decline
in new cases until Phase III finishes (8 years), a constant treated share,
and 96% drug-susceptible.

WHAT GIVEWELL (CG) DOES NOT ACCOUNT FOR:
- No vaccine or other major incidence shock.
- No regimen changes affecting the applicability of the trial results.
- No sensitivity to the baseline year of notifications.
- No account of whether "adult" excludes ~10–12% pediatric cases
  consistently.

DATA SOURCES TO EXAMINE:
- WHO Global TB Report 2023/2024 (notifications, incidence trends, DR-TB
  share).
- M72/AS01E Phase IIb (Tait et al. 2019, NEJM) and Phase III timelines
  (Gates MRI).
- Modeling of vaccine impact on incidence (e.g., Harris et al. / LSHTM
  TB vaccine impact models).
- WHO 2022 regimen guidance and the new-drug pipeline (Working Group on
  New TB Drugs).

MATERIALITY THRESHOLD:
- eligible below ~3.6M is below the bar. A change of more than ±1.4M is
  a >25% move.
- A faster decline of 4%/yr instead of 2% over 8 years lowers eligible by
  ~15%, which is not material alone.
- A vaccine-driven ~30–50% incidence reduction by the adoption year would
  be material.
- An error in reconstruction of more than ~25% would be material.

KNOWN CONCERNS ALREADY SURFACED (exclusion list):
- The 2% decline, constant treated share, and 96% DS share are explicit
  assumptions. Restating them is not a finding.
```

---

## DEPENDENCY MAP

**Effect size and success (Threads 1 and 7).** Thread 1 owns the effect conditional on success. Thread 7 owns the probability of success. Both must agree on a single definition of "success." If success is defined on surrogate endpoints, the expected mortality benefit is P(success) × E[effect | success] and may be much lower than 0.40 × 0.10.

**Phase III design links cost, evidence, and probability (Threads 1, 2, 7).**
- A cheap Phase III implies a surrogate endpoint. That weakens the mortality evidence (Thread 1) and changes the meaning of p_success (Thread 7).
- A mortality-powered Phase III implies much higher cost (Thread 2) but strengthens the evidence. This is a tension between Thread 2 and Thread 1.
- These threads must reconcile so the analysis does not double-penalize or double-credit.

**The counterfactual framing sets the denominator (Threads 3 and 2).** Thread 3's resolution determines whether Thread 2's cost findings even enter the denominator. Under a "1-year delay" counterfactual, most downstream costs are shifted rather than caused, so drug delivery costs in the speedup year become the relevant incremental cost.

**Discounting and adoption timing (Threads 3 and 5).** The discounting impact depends on the adoption timing and uptake ramp from Thread 5. A slow ramp means the shifted year falls in a low-uptake period, which lowers the discounted benefit.

**Delivered dose (Threads 5 and 1).** Adherence and rifampicin interactions in real-world use from Thread 5 modify the delivered dose that Thread 1 depends on. Avoid counting the same exposure reduction in both.

**Who dies versus who can be helped (Threads 6 and 1).** Thread 6 supplies the descriptive epidemiology of deaths. Thread 1 uses it to judge which deaths are reachable. Do not apply a reachability discount in both threads.

**Long-term survival versus residual life expectancy (Threads 4 and 6).** Thread 4's post-treatment excess mortality finding raises benefits through survival gains. Thread 6's survivor-SMR finding lowers DALYs per death averted. Both use the same data (Romanowski et al.) and must be internally consistent.

**Robustness from unvalued benefits (Threads 4 and 1).** Thread 4 may make the estimate robust to a weak Thread 1 finding, since lung damage and morbidity benefits may survive even if the on-treatment mortality effect is small.

**Landscape and effect size (Threads 8 and 1).** Regimen changes found in Thread 8 may reduce the applicability of Thread 1's effect estimate.

## RECOMMENDED SEQUENCING

1. **Run first, in parallel: Thread 1 (effect size) and Thread 3 (structural counterfactual and discounting).**
   - Thread 1 determines the central parameter and the definition of success.
   - Thread 3 determines how costs and benefits should be framed at all.
   - Both have the largest potential swings, and other threads depend on their resolutions.
2. **Run second: Thread 2 (costs) and Thread 7 (p_success).** Both need Thread 1's answer on Phase III endpoints. Thread 2 also needs Thread 3's counterfactual framing.
3. **Run third: Thread 5 (implementation) and Thread 6 (who dies).** Thread 5 feeds adoption timing back into Thread 3's discounting estimate. Thread 6 feeds the death composition into Thread 1's reachability estimate. A brief second pass on Threads 1 and 3 may be needed.
4. **Run last: Thread 4 (unvalued benefits) and Thread 8 (landscape).**
   - Thread 4 is best estimated once Threads 1 and 7 settle how to probability-weight surrogate benefits.
   - Thread 8 has the lowest expected single-parameter impact, except in the vaccine scenario.
5. **Final integration.** Combine findings as multipliers on the 3,055x baseline. Check for double-counting across the dependency pairs above. Report the combined central estimate and its range relative to the 2,000x bar.