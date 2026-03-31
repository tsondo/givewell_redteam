Based on the intervention report and CEA parameters provided, I'll decompose GiveWell's insecticide-treated nets (ITNs) analysis into investigation threads. Since the baseline AI output wasn't accessible, I'll proceed without that exclusion list.

## Investigation Thread Decomposition

### THREAD 1: External Validity of the Pryce et al. Meta-Analysis to Current Program Settings

**SCOPE:** This thread investigates whether the 45% malaria incidence reduction from Pryce et al.'s meta-analysis validly applies to the specific contexts where GiveWell funds ITN distributions, given differences in mosquito species, resistance patterns, housing structures, and baseline malaria endemicity between trial settings and current program locations.

**KEY PARAMETERS:** 
- Malaria incidence reduction (Pryce et al.): 0.45
- External validity adjustment: -0.05
- Location-specific insecticide resistance adjustments (ranging from -0.0377 to -0.5860)

**WHAT GIVEWELL ALREADY ACCOUNTS FOR:** GiveWell applies a 5% external validity discount and location-specific insecticide resistance adjustments. They differentiate between trial settings and program settings by adjusting for net usage differences.

**WHAT GIVEWELL DOES NOT ACCOUNT FOR:** Potential interactions between insecticide resistance and behavioral adaptation by mosquito populations, differences in housing quality that affect indoor/outdoor biting ratios, variation in mosquito species composition between trials and current settings, and temporal changes in resistance patterns since the studies in Pryce et al.

**DATA SOURCES TO EXAMINE:**
- Pryce et al. 2018 meta-analysis (full text and supplementary materials)
- WHO Malaria Threat Maps for resistance data
- National malaria control program reports from Chad, DRC, Guinea, Nigeria, South Sudan, Togo, and Uganda
- Recent entomological surveillance data from program areas

**MATERIALITY THRESHOLD:** A reduction in the base efficacy parameter from 0.45 to 0.35 would reduce cost-effectiveness by approximately 22%, potentially moving several programs below funding thresholds. Location-specific findings that increase resistance adjustments by >0.15 would be material.

**KNOWN CONCERNS ALREADY SURFACED:** GiveWell acknowledges uncertainty about insecticide resistance through location-specific adjustments and notes the age of some studies in the meta-analysis.

### THREAD 2: Actual Net Usage and Retention in Mass Distribution Campaigns

**SCOPE:** This thread examines whether the assumed 70% net usage rate and the implicit retention/replacement cycle accurately reflect real-world usage patterns in AMF-supported mass distribution campaigns, particularly focusing on post-distribution monitoring data and behavioral factors affecting usage.

**KEY PARAMETERS:**
- Net usage in trials: 0.7
- Person-years of protection (implicitly affected by retention assumptions)
- Baseline net coverage (location-specific, ranging from 0.313 to 0.795)

**WHAT GIVEWELL ALREADY ACCOUNTS FOR:** GiveWell uses a 70% usage rate based on trial data and accounts for baseline coverage to avoid double-counting protection.

**WHAT GIVEWELL DOES NOT ACCOUNT FOR:** Seasonal variation in usage, differential usage by age group, net quality degradation in different climates, sharing of nets beyond intended recipients, and potential crowd-out effects where free distribution reduces future net purchases.

**DATA SOURCES TO EXAMINE:**
- AMF post-distribution monitoring reports
- DHS and MIS surveys from program countries
- Behavioral studies on ITN usage patterns
- Net durability monitoring studies from similar contexts

**MATERIALITY THRESHOLD:** A reduction in effective usage from 70% to 55% would reduce cost-effectiveness by approximately 21%. Evidence of faster degradation reducing average net lifespan from 2.5 to 2 years would reduce cost-effectiveness by approximately 20%.

**KNOWN CONCERNS ALREADY SURFACED:** GiveWell acknowledges uncertainty about distribution and usage rates in their report.

### THREAD 3: Marginal Impact Given Existing Coverage and Seasonal Malaria Chemoprevention

**SCOPE:** This thread investigates whether GiveWell's methodology appropriately accounts for diminishing marginal returns as baseline coverage increases and the interaction effects between ITNs and seasonal malaria chemoprevention (SMC) programs.

**KEY PARAMETERS:**
- Baseline net coverage (location-specific)
- SMC reduction factors (location-specific)
- The implicit assumption of linear impact reduction with coverage

**WHAT GIVEWELL ALREADY ACCOUNTS FOR:** GiveWell adjusts for baseline coverage and includes SMC reduction factors for each location.

**WHAT GIVEWELL DOES NOT ACCOUNT FOR:** Non-linear coverage effects (e.g., herd immunity at high coverage), synergistic or antagonistic interactions between ITNs and SMC, spatial clustering of coverage gaps, and potential selection effects where remaining uncovered populations are systematically different.

**DATA SOURCES TO EXAMINE:**
- Studies on ITN coverage and community-level protection
- SMC and ITN interaction studies
- Spatial analysis of coverage patterns
- Mathematical modeling studies of malaria transmission dynamics

**MATERIALITY THRESHOLD:** Evidence that marginal impact decreases non-linearly above 60% coverage, reducing effectiveness by >30% in high-coverage areas like Togo (79.5% baseline), would materially affect program prioritization.

**KNOWN CONCERNS ALREADY SURFACED:** GiveWell notes uncertainty about interaction effects but treats them additively.

### THREAD 4: Mortality Estimation Methodology and Age-Specific Effects

**SCOPE:** This thread examines whether GiveWell's method for estimating direct malaria mortality rates and the assumed 80% relative efficacy for over-5 populations accurately captures the mortality burden and intervention effect across age groups.

**KEY PARAMETERS:**
- Direct malaria mortality (u5) - location specific
- Over-5 relative efficacy: 0.8
- Indirect deaths per direct death: 0.75
- Age-specific moral weights

**WHAT GIVEWELL ALREADY ACCOUNTS FOR:** GiveWell uses location-specific mortality estimates, applies an 80% efficacy discount for over-5 populations, and includes indirect mortality effects.

**WHAT GIVEWELL DOES NOT ACCOUNT FOR:** Uncertainty in cause-of-death attribution in weak surveillance systems, changing age patterns of malaria mortality with declining transmission, potential protective effects beyond mortality (severe anemia, neurological sequelae), and variation in indirect mortality ratios by context.

**DATA SOURCES TO EXAMINE:**
- Verbal autopsy studies from program countries
- WHO Global Health Observatory malaria mortality data
- Studies on age-shifting of malaria burden
- Recent burden of disease estimates for malaria

**MATERIALITY THRESHOLD:** A 30% systematic overestimate of under-5 malaria mortality across locations would reduce cost-effectiveness by approximately 25%. Evidence that over-5 efficacy is 60% rather than 80% would reduce cost-effectiveness by 10-15%.

**KNOWN CONCERNS ALREADY SURFACED:** GiveWell acknowledges uncertainty in mortality estimates and the evidence base for over-5 effects.

### THREAD 5: Implementation Quality and Supply Chain Losses

**SCOPE:** This thread investigates whether the program as implemented matches the program as modeled, focusing on supply chain efficiency, distribution quality, correct net sizing, and potential diversion or misuse of nets.

**KEY PARAMETERS:**
- Implicitly affects all efficacy parameters if implementation differs from trials
- Leverage and funging adjustments (partially capture this)

**WHAT GIVEWELL ALREADY ACCOUNTS FOR:** GiveWell includes leverage and funging adjustments that partially account for implementation inefficiencies.

**WHAT GIVEWELL DOES NOT ACCOUNT FOR:** Physical net losses in supply chain, systematic under-sizing leading to reduced protection, quality issues with nets procured at scale, distribution inequities within targeted areas, and potential resale or alternative use of nets.

**DATA SOURCES TO EXAMINE:**
- AMF distribution reports and audits
- Supply chain assessments from program countries
- Independent monitoring reports
- Studies on ITN misuse and resale markets

**MATERIALITY THRESHOLD:** Evidence of >15% net loss or misuse in the supply chain would reduce cost-effectiveness proportionally. Systematic quality issues reducing net efficacy by 20% would be material.

**KNOWN CONCERNS ALREADY SURFACED:** GiveWell mentions distribution uncertainties but doesn't quantify supply chain losses explicitly.

### THREAD 6: Long-term Economic Benefits and Development Effects

**SCOPE:** This thread examines whether GiveWell's income effect estimates adequately capture the long-term economic benefits of malaria prevention, including educational attainment, cognitive development, and labor productivity effects.

**KEY PARAMETERS:**
- Income per case averted: 0.0058088
- Additional benefits adjustment (location-specific, ranging from 0.379 to 0.529)
- Discount rate: 0.04

**WHAT GIVEWELL ALREADY ACCOUNTS FOR:** GiveWell includes income effects and additional benefits adjustments, with a 4% discount rate for future benefits.

**WHAT GIVEWELL DOES NOT ACCOUNT FOR:** Heterogeneity in economic returns by severity of averted cases, potential threshold effects in cognitive development, general equilibrium effects of large-scale health improvements, and uncertainty in the persistence of economic benefits over decades.

**DATA SOURCES TO EXAMINE:**
- Long-term follow-up studies of malaria prevention programs
- Recent literature on early-life health shocks and human capital
- Studies on malaria's economic burden in African contexts
- Evidence on complementarities between health and other investments

**MATERIALITY THRESHOLD:** Evidence that income effects are 50% smaller than estimated would reduce the additional benefits component by approximately 20%, with varying impacts by location based on their additional benefits adjustments.

**KNOWN CONCERNS ALREADY SURFACED:** GiveWell acknowledges uncertainty in long-term effect estimates and uses conservative assumptions.

### THREAD 7: Structural Biases in the Cost-Effectiveness Framework

**SCOPE:** This thread investigates whether GiveWell's analytical framework contains systematic biases that favor or disfavor ITNs relative to other interventions, including the choice of moral weights, the handling of uncertainty, and the decision to exclude certain benefit categories.

**KEY PARAMETERS:**
- Moral weights (116.25 for under-5, 73.19 for over-5)
- Benchmark value: 0.00333
- The structure of the CEA model itself

**WHAT GIVEWELL ALREADY ACCOUNTS FOR:** GiveWell uses explicit moral weights and benchmarks for comparison across interventions.

**WHAT GIVEWELL DOES NOT ACCOUNT FOR:** Potential double-counting when comparing to cash transfers, exclusion of health system strengthening effects, distributional concerns within recipient populations, and option value of maintaining elimination potential.

**DATA SOURCES TO EXAMINE:**
- GiveWell's moral weights methodology documents
- Literature on cost-effectiveness analysis in global health
- Critiques of DALY-based frameworks
- Alternative frameworks for valuing health interventions

**MATERIALITY THRESHOLD:** Structural changes that alter relative cost-effectiveness by >30% compared to other GiveWell interventions would affect funding allocation decisions.

**KNOWN CONCERNS ALREADY SURFACED:** GiveWell acknowledges moral weight uncertainty and regularly reviews their framework.

## DEPENDENCY MAP

- **Thread 1 ↔ Thread 3:** External validity findings affect how marginal impact should be calculated
- **Thread 2 → Thread 5:** Usage patterns inform what implementation quality means in practice
- **Thread 4 → Thread 6:** Mortality methodology affects the denominators for economic benefit calculations
- **Thread 3 → Thread 7:** Coverage interactions raise questions about the linear modeling framework
- **Thread 5 → All threads:** Implementation quality affects the real-world applicability of all parameters

## RECOMMENDED SEQUENCING

1. **First:** Thread 5 (Implementation) - Establishes whether the modeled intervention matches reality
2. **Second:** Thread 1 (External Validity) and Thread 4 (Mortality) - Core parameters affecting all calculations
3. **Third:** Thread 2 (Usage) and Thread 3 (Marginal Impact) - Build on base parameters
4. **Fourth:** Thread 6 (Long-term Benefits) - Requires clarity on immediate effects
5. **Last:** Thread 7 (Structural) - Best assessed after understanding all parameter-level issues