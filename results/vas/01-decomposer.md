# DECOMPOSITION OF GIVEWELL'S VITAMIN A SUPPLEMENTATION ANALYSIS

Based on my analysis of GiveWell's vitamin A supplementation (VAS) intervention report and cost-effectiveness model, I've identified 7 investigation threads that represent distinct areas where material findings could alter the bottom-line cost-effectiveness estimates.

## THREAD 1: External Validity of Mortality Effect Across Heterogeneous Modern Contexts

SCOPE: This thread investigates whether the ~4-12% mortality reduction from VAS (derived primarily from trials conducted 1980s-1990s) validly applies across the 37 diverse implementation locations in GiveWell's model, given substantial changes in disease burden, health systems, and nutritional status over the past 30-40 years.

KEY PARAMETERS: 
- "Effect of VAS on mortality" (single scalar applied across all locations)
- External validity adjustment factors (based on stunting, wasting, poverty proxies)

WHAT GIVEWELL ALREADY ACCOUNTS FOR: GiveWell acknowledges this uncertainty as their primary concern, stating they have "more uncertainty about its effect on mortality compared to GiveWell's other top recommended programs." They apply an external validity adjustment using proxy indicators (stunting, wasting, poverty rates) to estimate how VAD prevalence has changed since the original trials.

WHAT GIVEWELL DOES NOT ACCOUNT FOR: 
- Heterogeneity in cause-specific mortality patterns across locations (VAS may differentially affect deaths from measles vs. diarrhea vs. malaria)
- Potential threshold effects where VAS becomes ineffective below certain VAD prevalence levels
- Interactions with improved vaccination coverage and treatment access since the 1980s-1990s trials

DATA SOURCES TO EXAMINE:
- Imdad et al. 2022 Cochrane review (update to 2017 version GiveWell cites)
- Country-specific Demographic and Health Surveys showing cause-of-death patterns
- WHO Global Health Observatory data on vaccination coverage trends
- Recent VAS trials in low-VAD settings (e.g., DEVTA trial in India)

MATERIALITY THRESHOLD: A reduction in the mortality effect from 4-12% to 2-6% would reduce cost-effectiveness by 50%, potentially dropping several locations below GiveWell's funding bar. The sensitivity analysis shows this parameter alone can change CE by -80% to +75%.

KNOWN CONCERNS ALREADY SURFACED: GiveWell explicitly notes that "some experts argue that vitamin A supplementation is no longer effective in modern contexts and should be discontinued." They've already incorporated external validity adjustments.

## THREAD 2: Systematic Bias in VAD Prevalence Estimates from Decades-Old Survey Data

SCOPE: This thread examines whether VAD prevalence estimates based on surveys from 1997-2011 (with 8 locations having data >15 years old) systematically over or understate current VAD levels, given that these estimates directly scale the mortality effect in the model.

KEY PARAMETERS:
- VAD prevalence estimates (especially for DRC, Mali, Angola, Madagascar with 1997-2000 surveys)
- External validity adjustment methodology (1/3 weight each to stunting, wasting, poverty)

WHAT GIVEWELL ALREADY ACCOUNTS FOR: GiveWell extrapolates current VAD prevalence using proxy indicators (stunting, wasting, poverty rates) weighted equally at 1/3 each, acknowledging the age of direct survey data.

WHAT GIVEWELL DOES NOT ACCOUNT FOR:
- Whether the proxy weighting scheme (1/3, 1/3, 1/3) accurately captures VAD trends
- Potential non-linear relationships between proxies and VAD
- Country-specific factors that might invalidate the proxy approach (e.g., targeted micronutrient programs)

DATA SOURCES TO EXAMINE:
- More recent serum retinol or retinol-binding protein surveys from any of the 8 countries with stale data
- Validation studies comparing proxy-based estimates to actual VAD measurements
- National micronutrient survey reports
- Food fortification program coverage data that might reduce VAD independent of the proxies

MATERIALITY THRESHOLD: For high-CE locations like DRC (29.88x) and Mali (16.93x) with 25+ year old VAD data, a 50% error in current VAD prevalence would change CE by approximately 35-40%, potentially affecting funding decisions.

KNOWN CONCERNS ALREADY SURFACED: GiveWell acknowledges using proxy indicators due to lack of recent direct VAD measurements.

## THREAD 3: Implementation Fidelity Gap Between Mass Campaigns and Steady-State Delivery

SCOPE: This thread investigates whether the actual implementation of VAS campaigns achieves the coverage, dosing schedule, and quality assumed in the CEA, particularly examining the gap between reported administrative coverage and effective biological coverage.

KEY PARAMETERS:
- Counterfactual coverage rates
- Number of supplementation rounds per year (fixed at 2)
- Cost per supplement delivered

WHAT GIVEWELL ALREADY ACCOUNTS FOR: The model includes counterfactual coverage estimates and assumes 2 rounds per year. Costs include implementation expenses.

WHAT GIVEWELL DOES NOT ACCOUNT FOR:
- Coverage validation studies showing gaps between reported and actual coverage
- Vitamin A potency degradation in supply chains
- Inconsistent timing between rounds affecting biological efficacy
- Geographic clustering of missed children (same children repeatedly missed)

DATA SOURCES TO EXAMINE:
- Post-campaign coverage evaluation surveys (PCCEs) for GiveWell-funded locations
- Supply chain assessment reports from Helen Keller International and Nutrition International
- Vitamin A stability studies under field storage conditions
- Administrative vs. survey coverage validation studies

MATERIALITY THRESHOLD: A 20% systematic overstatement of effective coverage (e.g., 80% reported but 60% biological coverage) would reduce cost-effectiveness by approximately 25%, sufficient to change funding allocations.

KNOWN CONCERNS ALREADY SURFACED: None explicitly mentioned beyond basic counterfactual coverage adjustments.

## THREAD 4: Cost Attribution and Marginal vs. Average Cost Conflation

SCOPE: This thread examines whether the cost-per-supplement estimates accurately reflect the marginal cost of GiveWell-funded supplements versus the average cost of the entire campaign, particularly in contexts where government and other funders provide substantial co-funding.

KEY PARAMETERS:
- Cost per supplement ($0.49-$1.54 range)
- Leverage adjustments (-0.4% to -6.7%)
- Funging adjustments (-14% to -69%)

WHAT GIVEWELL ALREADY ACCOUNTS FOR: The model includes both leverage (additional funding crowded in) and funging (resources freed up) adjustments by location.

WHAT GIVEWELL DOES NOT ACCOUNT FOR:
- Whether marginal supplements are more expensive than average (reaching remote populations)
- Hidden government costs not captured in budget analyses
- Opportunity costs of health worker time during campaigns
- Economics of scale that might be lost if programs contract

DATA SOURCES TO EXAMINE:
- Detailed campaign budgets showing cost breakdowns by geography
- Government health budget analyses for VAS campaign contributions
- Cost studies comparing first vs. last quintile of coverage
- Time-motion studies of health worker allocation during campaigns

MATERIALITY THRESHOLD: A 50% underestimate of true marginal cost (e.g., $1.50 vs $1.00) would reduce cost-effectiveness by approximately 33%, affecting funding decisions for marginal locations.

KNOWN CONCERNS ALREADY SURFACED: GiveWell includes leverage and funging adjustments but doesn't explicitly address marginal vs. average cost distinctions.

## THREAD 5: Mortality Displacement vs. Mortality Reduction

SCOPE: This thread investigates whether VAS primarily prevents deaths (assumed in the model) or merely delays them by weeks or months (mortality displacement), particularly for the frailest children who might die from other causes shortly after being saved from VAD-related mortality.

KEY PARAMETERS:
- Moral value of averting an under-5 death (118.73 UoV)
- Long-term benefits calculations
- Developmental effects adjustments

WHAT GIVEWELL ALREADY ACCOUNTS FOR: The model assigns full moral weight to each death averted and includes developmental benefits for survivors.

WHAT GIVEWELL DOES NOT ACCOUNT FOR:
- Competing risks of mortality in high-mortality settings
- Whether VAS-prevented deaths cluster among children with multiple vulnerabilities
- Time horizon of mortality benefits (immediate vs. sustained protection)
- Differential life expectancy of marginal survivors

DATA SOURCES TO EXAMINE:
- Long-term follow-up studies of VAS trial participants
- Analyses of cause-specific mortality in VAS trials
- Studies on competing mortality risks in high-burden settings
- Child cohort studies examining survival trajectories post-VAS

MATERIALITY THRESHOLD: If 30% of "prevented" deaths are merely displaced by 6-12 months, the effective moral value per death averted would decrease by ~25%, reducing cost-effectiveness proportionally.

KNOWN CONCERNS ALREADY SURFACED: Not explicitly mentioned in the provided materials.

## THREAD 6: Interaction Effects with Concurrent Health Interventions

SCOPE: This thread examines whether the mortality reduction attributed to VAS in the CEA double-counts benefits that actually arise from synergies with other child health interventions (vaccines, malaria prevention, nutrition programs) that have scaled up since the original VAS trials.

KEY PARAMETERS:
- Effect of VAS on mortality (main effect)
- Additional benefits/downsides adjustments

WHAT GIVEWELL ALREADY ACCOUNTS FOR: The model includes an "additional benefits downsides" adjustment factor, though its specific components aren't detailed in the parameter summary.

WHAT GIVEWELL DOES NOT ACCOUNT FOR:
- Explicit modeling of VAS-vaccine interaction effects
- Synergies with malaria control programs (bed nets, SMC)
- Overlap with other micronutrient supplementation programs
- Whether base mortality rates already reflect these other interventions

DATA SOURCES TO EXAMINE:
- Studies on VAS-vaccine interaction effects (particularly measles, DPT)
- Integrated child health program evaluations
- Timeline analyses of child health intervention scale-up by country
- Factorial trials examining VAS with and without other interventions

MATERIALITY THRESHOLD: If 40% of the mortality reduction attributed to VAS actually requires co-delivery with vaccines or other programs already in place, the incremental effect of VAS would be overstated by ~40%, substantially affecting cost-effectiveness.

KNOWN CONCERNS ALREADY SURFACED: Additional benefits are modeled but interaction effects aren't explicitly discussed.

## THREAD 7: Structural Model Assumptions About Linear Dose-Response

SCOPE: This thread investigates whether the CEA's implicit assumption of linear relationships (double the coverage = double the impact) holds across the full range of implementation contexts, or whether there are threshold effects, diminishing returns, or accelerating benefits at different coverage levels.

KEY PARAMETERS:
- The mathematical structure linking coverage to mortality reduction
- Cost-per-supplement at different coverage levels
- Counterfactual coverage estimates

WHAT GIVEWELL ALREADY ACCOUNTS FOR: The model appears to use linear scaling of effects with coverage, with adjustments for counterfactual coverage.

WHAT GIVEWELL DOES NOT ACCOUNT FOR:
- Threshold effects (minimum effective coverage for herd protection)
- Diminishing returns (hardest-to-reach children may benefit most)
- Non-linear cost curves at high coverage levels
- Community-level vs. individual-level benefits

DATA SOURCES TO EXAMINE:
- Dose-response analyses from VAS trials with varying coverage
- Economic evaluations showing cost curves at different coverage levels
- Ecological studies comparing mortality at different VAS coverage levels
- Mathematical models of indirect protection effects

MATERIALITY THRESHOLD: If the true dose-response curve shows 50% diminishing returns above 60% coverage, high-coverage locations would see 20-30% reductions in cost-effectiveness, affecting several funding decisions.

KNOWN CONCERNS ALREADY SURFACED: Not explicitly mentioned; the model appears to assume linear relationships throughout.

## DEPENDENCY MAP

- **Thread 1 (External Validity) ↔ Thread 2 (VAD Prevalence)**: Updated VAD prevalence estimates would directly inform external validity adjustments
- **Thread 3 (Implementation) ↔ Thread 4 (Costs)**: True coverage levels affect the real cost per effectively covered child
- **Thread 5 (Mortality Displacement) ↔ Thread 6 (Interaction Effects)**: Both address whether the measured mortality benefit is fully attributable to VAS
- **Thread 7 (Structural Assumptions) → All threads**: Non-linear effects would modify how all other findings translate to CE changes

## RECOMMENDED SEQUENCING

1. **First: Thread 2 (VAD Prevalence)** — Most concrete and measurable; findings would inform multiple other threads
2. **Second: Thread 3 (Implementation Fidelity)** — Establishes what intervention is actually being delivered
3. **Third: Thread 1 (External Validity)** — Can incorporate findings from Threads 2 and 3
4. **Fourth: Thread 7 (Structural Assumptions)** — Determines how to interpret all parameter-level findings
5. **Parallel: Threads 4, 5, 6** — These can run independently once the above context is established