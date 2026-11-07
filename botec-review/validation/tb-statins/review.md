# BOTEC review: Trialing statins for treating tuberculosis

**Bottom line.** The arithmetic holds: the rebuilt SROI is 3,055x against a stated ~3,000x (+2%), so there is no arithmetic slip. It clears the ~2,000x bar, but only narrowly, and it depends on inputs that are mostly the author's judgment. Six inputs would each, on their own, push the estimate below the bar somewhere inside a range a careful reviewer could defend. The three that matter most:
- the relative cut in deaths from adding atorvastatin (break-even 6.5% vs 10% assumed);
- the speedup the grant buys (break-even 0.65 years vs 1 year assumed);
- all-in cost (break-even $10.7M vs $7M assumed).

The cost line is the most exposed. A Phase III trial that could show a mortality benefit does not fit in $7M (Finding 1).

("Break-even" means the value at which the estimate exactly meets the 2,000x bar, with all other inputs held at the draft's values.)

## What decides the result

| Parameter | Value | Plausible range | Result at low / high | Break-even | Evidence |
|---|---|---|---|---|---|
| speedup_years | 1 yr | 0.5–3 yr | 1,527 / 9,165 | 0.655 yr | Not checkable publicly. Context: a separate rosuvastatin Phase 2b trial (n=137) found no significant speedup in culture conversion (HR 1.30, 95% CI 0.88–1.91), so other groups may not be racing to test statins ([abstract](https://pesquisa.bvsalud.org/bvsecuador/resource/pt/mdl-36966799)) |
| relative_reduction (deaths) | 10% | 3%–20% | 916 / 6,110 | 6.55% | Not checkable publicly; no mortality data found. The atorvastatin Phase IIb (n=150, open-label, 40 mg for 2 months) reported culture-negative sputum in 97% vs 85.1% (P=0.02) and chest X-ray score falls of 37% vs 22% ([abstract](https://pesquisa.bvsalud.org/portal/resource/es/mdl-38042968)). A meta-analysis of statins and TB covers only TB incidence, not deaths on treatment ([review](https://www.infezmed.it/media/articoli-html/Vol_30_2_2022_4.html)) |
| all_in_cost | $7M | $5M–$30M | 4,277 / 713 | $10.7M | A published costing of one Phase III pulmonary TB drug trial (850–1,000 patients) gives $22.3–22.6M in 2000 USD ([ISPOR 2001](https://www.ispor.org/heor-resources/presentations-database/presentation/ispor-fourth-annual-european-congress/estimated-costs-to-conduct-a-phase-iii-clinical-trial-of-a-new-pulmonary-tuberculosis-drug)) |
| baseline_mortality (on treatment) | 6% | 3%–8% | 1,527 / 4,073 | 3.93% | Partly checked. WHO reports 88% treatment success for the 2022 first-line cohort, but the death share is only in a figure I could not read ([WHO 2024](https://www.who.int/teams/global-programme-on-tuberculosis-and-lung-health/tb-reports/global-tuberculosis-report-2024/tb-diagnosis-and-treatment/2-3-tb-treatment--coverage-and-outcomes)). The 6% itself is unsourced |
| uptake | 60% | 30%–80% | 1,527 / 4,073 | 39.3% | Not checkable publicly. Context: muscle pain was 16% vs 5% in the Phase IIb, which bears on adherence ([abstract](https://pesquisa.bvsalud.org/portal/resource/es/mdl-38042968)) |
| p_success | 40% | 20%–50% | 1,527 / 3,819 | 26.2% | Not checked (the review checks at most five drivers); see Questions |

Each row changes one input with the rest held at the draft's values. The swings do not add up.

## Findings

### 1. A Phase III that could show fewer deaths is not costed (lowers the estimate; at $22.3M all-in, SROI falls to 959x, below the bar)
All of the value comes from deaths prevented, but the trials measure something else. The completed Phase IIb measured sputum culture conversion (whether TB bacteria are still found in sputum) and chest X-ray. The public registration of an atorvastatin Phase IIC trial in pulmonary TB has 440 participants in 4 arms and describes itself as a pilot for Phase III ([registry](https://ctv.veeva.com/study/atorvastatin-in-pulmonary-tuberculosis)). It lists sputum, X-ray, lung function and safety outcomes, not death. Detecting the assumed drop in deaths from 6% to 5.4% would take about 23,434 patients per arm (script: 80% power, two-sided 5% test). That is far larger than the 850–1,000-patient Phase III that was costed at $22.3–22.6M in 2000 dollars ([ISPOR 2001](https://www.ispor.org/heor-resources/presentations-database/presentation/ispor-fourth-annual-european-congress/estimated-costs-to-conduct-a-phase-iii-clinical-trial-of-a-new-pulmonary-tuberculosis-drug)). Either the all-in cost is too low for a trial that shows the valued effect, or the 10% cut in deaths is never directly tested and rests on surrogate endpoints (outcomes like culture conversion that stand in for survival). With $22.3M as the all-in cost, the script gives 959x. The break-even all-in cost is $10.7M.
*Likely reply from the author:* "Phase III would use culture and lung-damage endpoints, and a cheap generic needs no costly registration package, so $7M is realistic." That may make $7M feasible, but then a successful trial does not show the mortality effect the estimate values. The 10% cut stays an untested assumption, so this finding still stands. It overlaps with `p_success` and `relative_reduction` (the same risk, seen from the cost side); do not add it to haircuts on those inputs.

### 2. Benefits beyond deaths during treatment are left out (raises the estimate; +25% at a 1.25x factor, to 3,819x; +50% at 1.5x, to 4,582x)
The formula counts only deaths during treatment. It leaves out the lung damage the Phase IIb suggests statins reduce (X-ray score down 37% vs 22%), along with any illness it causes after treatment, and it gives no value to the sweat-based diagnostic the same grant funds. Post-TB harm is not small: one modelling study of TB survivors assumes they die at 2.91 times (2.21–3.84) the rate of people who never had TB, citing a systematic review ([Post-TB paper](https://eprints.whiterose.ac.uk/168718/1/PostTB_authorAccepted.pdf)). How large the factor is remains judgment. I could not find a public estimate linking X-ray improvement to later deaths or disability.
*Likely reply from the author:* "We left these out on purpose to be conservative." That is reasonable. The finding stands only as a note that the stated figure is a floor on this channel, which partly offsets Finding 1.

**Balance check.** Finding 1 lowers the estimate; Finding 2 raises it. The population base is also probably conservative (raises; see Questions). Discounting, if the framework uses it, lowers it. Finding 1 overlaps with the `p_success` and `relative_reduction` ranges.

## Questions for the author
- [ ] What is the Phase III plan: primary endpoint (deaths or surrogate), sample size, budget inside the $7M, and what counts as "success" in the 40%? (affects `all_in_cost`, `p_success`; across $5M–$30M the result runs 4,277x to 713x; at $22.3M, 959x; across 20%–50% success, 1,527x to 3,819x)
- [ ] What is the basis for a 10% relative cut in deaths, given the trial evidence is on sputum and X-ray only? Does the Phase IIc actually record survival? (affects `relative_reduction`; 3%–20% gives 916x to 6,110x)
- [ ] Why 1 year of speedup? Who else would run this trial without the grant, and when? (affects `speedup_years`; 0.5–3 years gives 1,527x to 9,165x)
- [ ] What supports 60% uptake of an add-on pill in national TB programmes, given side effects such as muscle pain? (affects `uptake`; 30%–80% gives 1,527x to 4,073x)
- [ ] Spreadsheet details, all answerable from the working file:
  - (a) Where does the 6% on-treatment death rate come from? (`baseline_mortality`; 3%–8% gives 1,527x to 4,073x)
  - (b) How was 5.5M derived? Applying the draft's own adjustments (2%/yr decline for 8 years, 96% drug-susceptible) to WHO's 8.3M notified cases in 2024 gives 6.78M, or 6.02M without children ([WHO factsheet](https://cdn.who.int/media/docs/default-source/global-tuberculosis-report-2025/global-tb-report-2025_factsheet.pdf?sfvrsn=cd5722e6_5)). Does 5.5M already exclude children, given uptake is "60% of adult patients"? (`people_eligible`; 6.02M gives 3,344x, +9%; 6.78M gives 3,766x, +23%)
  - (c) Are benefits that start about 9+ years out discounted anywhere in the framework? (`discount_rate`; 3%/yr gives 2,341x over 9 years and 2,143x over 12)

## What this review did not check
I did not check the author's internal sources, the grantee's trial protocol or budget, base rates for Phase II-to-III success of repurposed drugs, or the drug-interaction question (rifampicin lowering atorvastatin levels; unsourced, and the Phase IIc's dose arms may address it). Nothing here was independently replicated. This is a structured checklist, not an independent review, and it does not replace the author's judgment.

## Appendix: model as rebuilt

**Parameters**

| Name | Value | Unit | Basis | Range | Range basis |
|---|---|---|---|---|---|
| people_eligible | 5,500,000 | DS-TB patients/yr at adoption | stated | 4.5M–7M | evidence: WHO 8.3M notified 2024; 1.2M of 10.7M incident cases are children |
| speedup_years | 1 | years | stated | 0.5–3 | judgment |
| baseline_mortality | 0.06 | probability | stated | 0.03–0.08 | judgment (WHO death share not readable) |
| relative_reduction | 0.10 | relative | stated | 0.03–0.20 | judgment (no mortality data) |
| uptake | 0.6 | share | stated | 0.3–0.8 | judgment |
| dalys_per_death | 27 | DALYs | stated | 20–32 | judgment |
| op_per_daly | 100,000 | $OP/DALY | stated (funder convention) | none | fixed by framework |
| all_in_cost | 7,000,000 | USD | stated | 5M–30M | evidence (high end): ISPOR 2001 |
| p_success | 0.4 | probability | stated | 0.2–0.5 | judgment |
| uncounted_benefit_factor | 1 | multiplier | implicit (deaths only) | 1–1.5 | judgment |
| discount_rate | 0 | per year | implicit (no discounting) | 0–0.04 | judgment; 3% is a common convention (unsourced) |
| years_to_benefit | 9 | years | implicit | none | 8 yr to Phase III end (stated) + ~1 yr (judgment) |

The $320,000 trial cost and the 4.5% funder share do not enter the formula. The draft credits 4.5% of benefits against 4.5% of costs, so the share cancels.

**Structural choices.** The formula counts deaths during treatment only. It leaves out morbidity, post-TB disease and the diagnostic. Benefit is one year of full-scale deaths prevented per year of speedup, with no ramp; a shifted adoption curve gives the same total over a long horizon, but the timing is undiscounted. Costs and benefits are both all-in. Drug-susceptible cases only, with the treated share held constant.

**Formula steps**
1. treated_users = people_eligible × uptake
2. deaths_averted_per_year = treated_users × baseline_mortality × relative_reduction
3. deaths_averted = deaths_averted_per_year × speedup_years
4. dalys_averted = deaths_averted × dalys_per_death × uncounted_benefit_factor
5. discount = 1 / (1 + discount_rate)^years_to_benefit
6. benefit_op = dalys_averted × op_per_daly × discount
7. sroi = benefit_op / all_in_cost × p_success
8. Side checks, which do not feed sroi: n per arm for a mortality trial; population rebuilt from WHO 2024 notifications

**Script output** (`botec_check.py spec.json`)

Rebuilt sroi: **3,055** (stated: 3,000, +2%). Bar: 2,000; passes.

Intermediate steps: treated_users = 3.3M; deaths_averted_per_year = 19,800; deaths_averted = 19,800; dalys_averted = 534,600; discount = 1; benefit_op = 53.5B; sroi = 3,055; mortality_treated_arm = 0.054; n_per_arm_mortality_trial = 23,434; people_from_who_2024_notified = 6.78M; people_from_who_excl_children = 6.02M

| Parameter | Value | Range | Result at low / high | Change | Break-even | Break-even in range? |
|---|---|---|---|---|---|---|
| speedup_years | 1 years | 0.5–3 | 1,527 / 9,165 | -50% / +200% | 0.655 | **yes** |
| relative_reduction | 0.1 relative | 0.03–0.2 | 916 / 6,110 | -70% / +100% | 0.0655 | **yes** |
| all_in_cost | 7M USD | 5M–30M | 4,277 / 713 | +40% / -77% | 10.7M | **yes** |
| baseline_mortality | 0.06 probability | 0.03–0.08 | 1,527 / 4,073 | -50% / +33% | 0.0393 | **yes** |
| uptake | 0.6 share | 0.3–0.8 | 1,527 / 4,073 | -50% / +33% | 0.393 | **yes** |
| p_success | 0.4 probability | 0.2–0.5 | 1,527 / 3,819 | -50% / +25% | 0.262 | **yes** |
| uncounted_benefit_factor | 1 multiplier on death DALYs | 1–1.5 | 3,055 / 4,582 | +0% / +50% | 0.655 | no |
| people_eligible | 5.5M DS-TB patients/yr at adoption | 4.5M–7M | 2,499 / 3,888 | -18% / +27% | 3.6M | no |
| dalys_per_death | 27 DALYs | 20–32 | 2,263 / 3,621 | -26% / +19% | 17.7 | no |
| discount_rate | 0 per year | 0–0.04 | 3,055 / 2,146 | +0% / -30% | 0.0482 | no |
| op_per_daly | 100,000 $OP/DALY | – | – / – | – / – | 65,470 | no |
| years_to_benefit | 9 years | – | – / – | – / – | none within 1000x | no |

| Scenario | Overrides | Result | Change | Passes bar |
|---|---|---|---|---|
| phase3_at_ispor_cost | all_in_cost=22.3M | 959 | -69% | no |
| uncounted_benefits_x1.25 | uncounted_benefit_factor=1.25 | 3,819 | +25% | yes |
| discount_3pct_9yr | discount_rate=0.03 | 2,341 | -23% | yes |
| discount_3pct_12yr | discount_rate=0.03, years_to_benefit=12 | 2,143 | -30% | yes |
| speedup_3yr | speedup_years=3 | 9,165 | +200% | yes |
| population_who_adults | people_eligible=6.02M | 3,344 | +9% | yes |
| population_who_all_ages | people_eligible=6.78M | 3,766 | +23% | yes |
