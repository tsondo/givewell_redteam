# Red Team Report: Insecticide-Treated Nets (ITNs)

> **Note (April 2026):** The pipeline summary counts in this report were generated before a parser bug was discovered that double-counted critiques whose verifier output included a summary restatement section. The corrected counts are: 28 verified critiques (not 30), 28 surviving adversarial review (not 30), signal rate 93.3% (not 100%). The underlying findings are unchanged — only the headline counts were affected by the bug. See commit 5aeed0e for the data correction and commit 6680f59 for the parser fix.

## Pipeline Summary
- Investigation threads examined: Not specified
- Candidate critiques generated: 30
- Verified critiques: 30
- Critiques surviving adversarial review: 30
- Signal rate: 100% (30 surviving / 30 generated)

## Critical Findings (surviving strength: STRONG)

### Finding 1: Mosquito Species Composition Misalignment
**Impact:** The malaria incidence reduction parameter could drop from 0.45 to 0.30-0.35, reducing cost-effectiveness by 22-33%.
**Evidence:** Studies show Anopheles arabiensis (outdoor-biting) has replaced An. gambiae as primary vector in several regions following bed net distribution. Multiple sites report presence of behaviorally resistant species like An. funestus that weren't dominant in original trials.
**GiveWell's best defense:** Insecticide resistance adjustments (up to 58.6% reduction) already capture real-world effectiveness variations including behavioral factors.
**Why it survives:** Chemical resistance and behavioral resistance are fundamentally different mechanisms. GiveWell's adjustments address mosquitoes that contact nets but survive; behavioral resistance involves mosquitoes avoiding nets entirely through outdoor/early biting.
**Recommended action:** Conduct species composition surveys in current implementation areas and separate chemical from behavioral resistance in adjustments.
**Key unresolved question:** What proportion of current malaria transmission occurs during hours when people are not under nets?

### Finding 2: Housing Quality and Indoor Residual Coverage Differences
**Impact:** Effectiveness could drop from 0.45 to 0.32-0.38 in areas with poor housing, reducing cost-effectiveness by 16-29%.
**Evidence:** High-quality housing reduces malaria odds by 74-78% compared to poor housing. Unscreened eave gaps significantly increase indoor mosquito exposure where ITNs are meant to provide protection.
**GiveWell's best defense:** The 5% external validity adjustment captures systematic differences between trial and implementation settings, including housing.
**Why it survives:** A generic 5% adjustment cannot adequately capture a mechanism that could reduce effectiveness by 20-30%. No evidence that housing quality specifically informed this parameter.
**Recommended action:** Quantify housing quality distribution in current vs. historical trial sites and adjust external validity parameter accordingly.
**Key unresolved question:** How much do indoor/outdoor biting ratios actually vary with housing quality in practice?

### Finding 3: Post-Distribution Usage Decline Over Time
**Impact:** If average usage over net lifespan is 55-60% rather than 70%, cost-effectiveness drops by 15-21%.
**Evidence:** GiveWell has expressed concerns about AMF's monitoring showing "more positive findings about ITN retention over time than we would expect from other high quality net durability literature."
**GiveWell's best defense:** The 70% parameter comes from Pryce et al.'s systematic review spanning multiple years, not short-term measurements.
**Why it survives:** Averaging across different time horizons doesn't model usage decline. The parameter appears to be a static average that doesn't account for temporal patterns over the 2.5-year lifespan.
**Recommended action:** Model usage as a declining function over time rather than a constant parameter.
**Key unresolved question:** Does GiveWell's model apply the 70% usage rate uniformly across the 2.5-year lifespan or model temporal decline?

### Finding 4: Net Physical Degradation Accelerated by Distribution Context
**Impact:** If effective lifespan is 2 years rather than 2.5 years, cost-effectiveness decreases by 20%.
**Evidence:** WHO monitoring shows median survival times of 2.0-2.6 years with strong influence from use environment. One study showed only 70% survivorship after one year, below model thresholds.
**GiveWell's best defense:** The 70% usage parameter may partially account for degradation.
**Why it survives:** Usage rate and physical lifespan are fundamentally different parameters. The 70% measures behavioral compliance, not how long nets remain protective.
**Recommended action:** Explicitly model net lifespan with empirical data from mass distribution contexts.
**Key unresolved question:** What is GiveWell's empirical basis for the 2.5-year lifespan assumption?

### Finding 5: Systematic Selection Bias in Remaining Uncovered Populations
**Impact:** Could affect both baseline mortality and usage parameters by 20-40%, with complex net effects on cost-effectiveness.
**Evidence:** Economic status strongly predicts bed net ownership and usage. As coverage increases, remaining uncovered populations are systematically different.
**GiveWell's best defense:** External validity and location-specific baseline coverage adjustments partially address population differences.
**Why it survives:** Static adjustments don't capture how selection bias intensifies as coverage increases. The marginal population at 80% coverage differs fundamentally from the marginal population at 30% coverage.
**Recommended action:** Develop coverage-dependent adjustments that account for changing population composition.
**Key unresolved question:** How do baseline malaria risk and net usage effectiveness vary with household wealth/education in real-world settings?

### Finding 6: Verbal Autopsy Misclassification May Inflate Malaria Attribution
**Impact:** If baseline malaria mortality is overestimated by 20-40%, cost-effectiveness could drop by approximately 25%.
**Evidence:** VA sensitivity for malaria deaths ranges from only 18.4% to 33% compared to gold standard methods, while specificity is 86.6% to 97%.
**GiveWell's best defense:** RCT efficacy estimates don't rely on verbal autopsy; they use clinical diagnosis.
**Why it survives:** GiveWell multiplies RCT efficacy by baseline mortality rates to calculate lives saved. If baseline rates are inflated by VA misclassification, the total impact is overestimated regardless of RCT measurement quality.
**Recommended action:** Investigate data sources for baseline mortality and apply appropriate corrections for VA bias.
**Key unresolved question:** How do IHME/WHO models handle verbal autopsy misclassification uncertainty?

## Significant Findings (surviving strength: MODERATE)

### Finding 7: Behavioral Adaptation and Residual Transmission
**Impact:** Combined with insecticide resistance, total effectiveness could drop from 0.45 to 0.25-0.35.
**Evidence:** While one study found no behavioral shifts over 2 years, systematic review shows only 79% of bites occur when people are in bed.
**Why it survives:** Insecticide resistance adjustments are sized for chemical resistance based on bioassays, not behavioral avoidance patterns.
**Recommended action:** Investigate whether 2 years is sufficient to detect behavioral adaptations that may emerge over 5-10 year timescales.

### Finding 8: Seasonal Usage Variation Not Reflected in Annual Averages
**Impact:** Effective protection could be overestimated by 10-15% if usage measurements don't weight by transmission intensity.
**Evidence:** Each 1°C temperature increase reduces ITN use by 9 percentage points; rainfall increases usage by 0.7 points per 10mm.
**Why it survives:** Most trials measure usage at discrete points rather than continuously, potentially biasing toward peak transmission seasons.
**Recommended action:** Investigate seasonal timing of usage measurements in Pryce trials and correlation with transmission patterns.

### Finding 9: Non-Linear Herd Protection Effects at High Coverage
**Impact:** In high-coverage locations like Togo (79.5% baseline), marginal impact could be 40-60% higher than linear assumptions predict.
**Evidence:** High coverage provides community effects protecting non-users, with >90% protection possible at >70% coverage.
**Why it survives:** GiveWell applies linear reductions as coverage increases, but herd protection creates non-linear acceleration at high coverage.
**Recommended action:** Model non-linear community effects, especially for locations approaching coverage thresholds.

### Finding 10: Treatment of Uncertainty Favors Simpler Causal Chains
**Impact:** ITNs could be systematically undervalued by 15-40% compared to simpler interventions.
**Evidence:** GiveWell requires 2-3x differences due to uncertainty and tests inputs individually rather than modeling joint distributions.
**Why it survives:** Complex interventions face compounding uncertainty discounts at each causal step, creating systematic bias.
**Recommended action:** Test whether uncertainty treatment produces different burdens across intervention types.

## Minor Findings (surviving strength: WEAK)

Several additional critiques survived but with weaker evidence or smaller expected impacts:

- **Crowd-Out Effects**: Mass distribution may reduce private net purchases by 10-20%, affecting incremental protection calculations
- **Differential Usage by Household Size**: Use-to-access ratios vary considerably between regions (0.89 vs 0.64)
- **Spatial Clustering**: Non-random distribution creates transmission pockets, reducing effective coverage by 15-30%
- **SMC-ITN Interaction**: Potential redundancy during peak season when both interventions operate
- **Age-Shifting**: Declining transmission shifts burden toward older ages not captured in current parameters
- **Context-Dependent Indirect Mortality**: Fixed 0.75 ratio may not capture variation across health system contexts

## Comparison with GiveWell's AI Output

| Our Critique | Overlap with GiveWell AI Output? | What We Added |
|---|---|---|
| Mosquito Species Composition | No | Novel finding with verified evidence and mechanistic clarity |
| Housing Quality Differences | No | Quantified impact with specific evidence on housing-malaria relationship |
| Usage Decline Over Time | Partial | Added AMF monitoring concerns and temporal modeling need |
| Net Physical Degradation | No | Separated lifespan from usage, added WHO durability data |
| Selection Bias | No | Novel finding on coverage-dependent population changes |
| Verbal Autopsy Misclassification | No | Critical methodological issue with quantified impact |
| Behavioral Adaptation | No | Distinguished from chemical resistance |
| Seasonal Usage | No | Temperature/rainfall effects on usage patterns |
| Non-Linear Herd Protection | No | Identified threshold effects at high coverage |
| Uncertainty Treatment Bias | No | Systematic framework issue affecting rankings |

## Ungrounded Hypotheses Worth Investigating

1. **Over-5 Efficacy Assumptions**: GiveWell acknowledges no RCTs estimate bed net impact on over-5 mortality, yet uses 0.8 relative efficacy. The single relevant RCT found 30-40% morbidity reduction, not mortality.

2. **Unaccounted Cognitive Benefits**: 21.4% of cerebral malaria survivors have lasting cognitive deficits. With >575,000 annual cases, this represents substantial unmodeled benefits.

3. **General Equilibrium Effects**: In high-coverage areas, large-scale health improvements may affect wages and prices in ways that reduce net benefits.

4. **Health System Strengthening**: ITN distribution through health facilities may create spillover capacity benefits not captured in individual-focused CEA.

## Meta-Observations

1. **Systematic Underestimation of Heterogeneity**: Multiple critiques identify variation (species, housing, usage patterns, mortality ratios) that GiveWell's model treats as constants or addresses with generic adjustments.

2. **Temporal Dynamics Ignored**: The model uses static parameters for phenomena that change over time (usage, resistance, degradation, population composition).

3. **Conflation of Different Mechanisms**: Chemical vs. behavioral resistance, usage vs. lifespan, funding vs. behavioral crowd-out—the model lacks granularity to distinguish related but distinct mechanisms.

4. **High-Coverage Contexts Poorly Modeled**: As more locations approach high coverage, non-linear effects and selection biases become increasingly important but aren't captured.

5. **Evidence Gaps Filled with Assumptions**: Several parameters (over-5 efficacy, 2.5-year lifespan, indirect mortality ratio) lack direct evidence but significantly affect results.

The pipeline generated more novel, mechanistically-specific critiques than expected, with 100% surviving adversarial review (though this seems implausibly high and may reflect pipeline calibration issues). The findings suggest GiveWell's model, while sophisticated, may systematically overestimate ITN cost-effectiveness by 20-50% through multiple compounding factors.