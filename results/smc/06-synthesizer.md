# Red Team Report: Seasonal Malaria Chemoprevention (SMC)

## Pipeline Summary
- Investigation threads examined: 6
- Candidate critiques generated: 34
- Verified critiques: 29
- Critiques surviving adversarial review: 28
- Signal rate: 82% (28 surviving / 34 generated)

## Critical Findings (surviving strength: STRONG)

### Finding 1: Rapid dhfr/dhps Mutation Selection Under SMC Pressure
**Impact:** Resistance mutations increased from 18.6% to 58.3% in Burkina Faso after SMC adoption (2010-2020). If efficacy drops from 75% to 50% due to resistance, cost-effectiveness worsens by approximately 50%.
**Evidence:** Post-SMC surveillance data from Burkina Faso demonstrates significant increases in resistance markers. The IRN haplotype of dhfr appeared higher in most countries after SMC scale-up. However, recent studies show SMC remains effective in areas with high quintuple mutant prevalence when amodiaquine sensitivity is maintained.
**GiveWell's best defense:** Real-world effectiveness data would inherently capture any resistance effects, and the amodiaquine component maintains effectiveness even in high-resistance areas.
**Why it survives:** GiveWell's efficacy estimates are based on studies from SMC's early rollout phase (2012-2018), while resistance markers have continued evolving post-study periods. The model contains no explicit resistance adjustment factor despite modeling efficacy decay for other interventions like bed nets.
**Recommended action:** Add explicit resistance evolution parameters to the model, with sensitivity analysis on efficacy decay rates.
**Key unresolved question:** What resistance threshold renders SMC ineffective, and how quickly will resistance spread from current hotspots?

### Finding 2: Climate Change Extending Transmission Seasons Beyond Historical SMC Windows
**Impact:** If historical SMC months captured 90% of transmission but now capture only 80% due to extended seasons, cost-effectiveness drops by roughly 10%, compounding over time.
**Evidence:** Strong evidence shows malaria transmission peaks shifting (e.g., to week 40 in some areas due to flooding). In semi-arid regions like Agadez, Niger, adults and adolescents are increasingly affected by malaria, with similar trends in Mali, Burkina Faso, Togo, and Chad.
**GiveWell's best defense:** Malaria Consortium conducts ongoing monitoring and can adjust campaign timing based on observed epidemiological patterns.
**Why it survives:** SMC requires massive logistical coordination planned 6-12 months in advance. Programs cannot simply adjust timing based on real-time observations. The evidence directly contradicts claims of flexible adaptation.
**Recommended action:** Investigate the proportion of annual burden current campaigns actually capture and adjust the "proportion of annual burden during SMC months" parameter accordingly.
**Key unresolved question:** How many SMC-implementing countries have adjusted their campaign calendars in response to epidemiological evidence of seasonal shifts?

### Finding 3: Concurrent Scale-Up of Complementary Child Health Interventions
**Impact:** If 20-40% of observed mortality reduction stems from concurrent interventions, SMC's true effect would be lower, increasing cost per death averted by 25-67%.
**Evidence:** Gavi Alliance allocated $178 million to health system strengthening in 2015 alone, with documented impacts on child mortality in the same countries implementing SMC. Multiple child health interventions scaled up simultaneously during the SMC implementation period.
**GiveWell's best defense:** SMC cost-effectiveness is based on RCT evidence that isolates the intervention effect.
**Why it survives:** While RCTs provide biological proof-of-concept, GiveWell's cost-effectiveness model relies heavily on real-world effectiveness data from scale-up programs. GiveWell explicitly adjusts RCT results for "real-world effectiveness," but this data comes from areas with concurrent health system improvements.
**Recommended action:** Disaggregate mortality effects of SMC from concurrent health systems strengthening in the model.
**Key unresolved question:** What proportion of GiveWell's SMC effectiveness estimates derives from real-world observational data versus controlled trials?

### Finding 4: Seasonal vs. Year-Round Exposure Developmental Impact Differential
**Impact:** Long-term income benefits may be overstated by 30-60% if seasonal prevention provides proportionally less developmental protection than year-round prevention studied in foundational research.
**Evidence:** Research confirms prenatal period and infancy are critical for brain development. The foundational Bleakley studies examined year-round elimination campaigns, while SMC only prevents seasonal transmission. Children in SMC areas still experience malaria during non-peak seasons.
**GiveWell's best defense:** GiveWell calibrates mortality/morbidity to seasonal patterns.
**Why it survives:** The defense misses the developmental critique entirely. Preventing cases only during peak season may not provide the same cumulative developmental benefits as year-round protection during critical early brain development periods.
**Recommended action:** Apply different developmental benefit estimates based on seasonal versus year-round protection patterns.
**Key unresolved question:** What is the actual developmental benefit differential between 60-80% seasonal malaria prevention vs. 95%+ year-round prevention in ages 3-59 months?

## Significant Findings (surviving strength: MODERATE)

### Finding 5: Geographic Resistance Heterogeneity Not Captured
**Impact:** In high-resistance areas, SMC may provide <30% efficacy rather than modeled ~75%, making cost per death averted 2-3x higher.
**Evidence:** Prevalence of dhps mutations varies dramatically by region. Only 7 countries remain fully eligible for IPTp by 2020 (including several SMC targets), while resistance levels within "eligible" regions show substantial variation.
**Why it survives:** Country-level cost variations don't prove resistance heterogeneity is captured—they could reflect mortality, costs, or coverage differences. GiveWell provides no evidence that efficacy parameters vary by resistance levels.
**Recommended action:** Include explicit resistance parameters by geographic region rather than relying on WHO eligibility as a proxy.

### Finding 6: Sub-National Heterogeneity Creates Mistimed Campaigns
**Impact:** If 40% of target districts have suboptimal timing reducing protection by 20-30%, country-level effectiveness drops by 8-12%.
**Evidence:** Climate drivers of malaria transmission vary significantly within regions. Researchers are developing sub-national approaches showing predicted onset of high transmission season varies by district within countries.
**Why it survives:** The 4-5 month campaign window addresses duration, not timing. A campaign running June-October is still mistimed if peak transmission is April-August in the north and August-December in the south.
**Recommended action:** Investigate what fraction of SMC districts receive optimally-timed campaigns versus nationally-standardized timing.

### Finding 7: Community Health Worker Wage Inflation
**Impact:** CHW wages could double from ~$50 to ~$100 per campaign cycle, increasing total program costs by 20-30% and pushing cost per child from $5.62-$8.37 to approximately $6.75-$10.88.
**Evidence:** Recent SMC costing studies explicitly state that "studies did not cost mature programmes, but pilots or relatively new campaigns." Funding barriers and time-limited compensation pose substantial risks to CHW workforce retention.
**Why it survives:** Current estimates are based on immature programs. The evidence directly contradicts claims that costs reflect "mature programs."
**Recommended action:** Investigate actual labor cost trajectories in mature programs and adjust cost projections accordingly.

## Minor Findings (surviving strength: WEAK to MODERATE)

- **Socioeconomic stratification in adherence**: Lower-income households show reduced adherence rates, but GiveWell's 28% adjustment may not capture SES-specific variation
- **Rainfall anomalies shifting peak transmission**: Fixed SMC windows miss climate-driven timing variations affecting 30-40% of years
- **Migration patterns**: Seasonal agricultural migration exposes children to transmission outside SMC periods
- **Cold chain failures**: Temperature exposure could reduce drug efficacy by 3-6 percentage points in 20-30% of doses
- **Community distributor skill dilution**: Rapid scale-up may lead to 10-15% reduction in effective coverage due to dosing errors
- **Supply chain stockouts**: Remote areas may experience 8-12% coverage gaps due to logistics challenges
- **Quality assurance gaps in mega-scale programs**: Programs treating 20+ million children face supervision intensity challenges
- **Distributor retention crisis**: High turnover (30-50% annually) reduces implementation quality

## Comparison with GiveWell's AI Output

| Our Critique | Overlap with GiveWell AI Output? | What We Added |
|---|---|---|
| Resistance evolution | Unknown* | Quantified impact (50% efficacy loss), verified evidence from Burkina Faso |
| Climate change impacts | Unknown* | Specific evidence of seasonal shifts, quantified coverage loss |
| Concurrent interventions | Unknown* | Identified $178M Gavi investment, quantified attribution bias |
| Developmental impact differential | Unknown* | Novel framing comparing seasonal vs year-round protection |
| Geographic heterogeneity | Unknown* | Specific resistance prevalence data by country |
| Wage inflation | Unknown* | Evidence that current costs based on immature programs |

*Unable to access GiveWell's baseline AI output document for comparison

## Ungrounded Hypotheses Worth Investigating

1. **Accelerated evolution under mass administration**: Resistance may evolve 2-3x faster under mass drug administration versus individual treatment
2. **"Dry season" malaria burden**: Areas with permanent water bodies may have 20-25% transmission outside SMC months versus assumed 5-10%
3. **Diminishing returns in high-burden areas**: Critical period damage before SMC begins may reduce marginal developmental benefits
4. **School attendance pathway weakness**: Agricultural labor demands during peak malaria season may limit educational benefits

## Meta-Observations

**Temporal blindness**: GiveWell's model appears static, missing dynamic factors like resistance evolution, climate change, and program maturation that compound over time.

**Scale effects**: Multiple critiques suggest diseconomies of scale (wage inflation, supervision challenges, distributor retention) not captured in current modeling.

**Attribution complexity**: The model may overattribute benefits to SMC when multiple interventions operate simultaneously in target areas.

**Methodological gaps**: Despite modeling detailed parameters for other interventions (e.g., bed net decay), SMC lacks similar dynamic adjustments for resistance, climate adaptation, or program lifecycle effects.