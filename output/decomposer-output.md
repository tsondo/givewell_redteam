# DECOMPOSER OUTPUT: Water Chlorination

*Generated against: GiveWell Water Quality Interventions report (April 2022) + Water Quality CEA (ILC and DSW)*

---

## OUTPUT 1: INVESTIGATION THREADS

---

### THREAD 1: Mortality Effect Size — Meta-Analytic Foundations

**SCOPE:** Investigate whether GiveWell's internal meta-analysis of 5 RCTs (subset of Kremer et al. 2022) produces a reliable base mortality effect size estimate (~12% reduction in under-5 all-cause mortality). Focus on statistical methodology, study selection, and whether the pooled estimate is appropriate for predicting effects in new implementation contexts.

**KEY QUESTIONS:**
- Is the Peto odds ratio method appropriate for this data (rare events, imbalanced treatment/control sizes, heterogeneous follow-up lengths)?
- Does GiveWell's selection of 5 studies from Kremer's 15 introduce its own selection effects? What happens to the estimate if the inclusion criteria change slightly?
- How does the estimate change under alternative pooling methods (Bayesian random effects, inverse-variance weighting, the MRPRP approach proposed by Więcek on the Columbia statistics blog)?
- Is the confidence interval (31% reduction to 13% increase) too wide to be decision-relevant, and does GiveWell adequately account for this uncertainty in their cost-effectiveness estimate?

**CEA PARAMETERS AFFECTED:**
- Base mortality effect size (~12% pre-adjustment) — this is the single highest-sensitivity parameter. Everything downstream scales with it.
- Plausibility cap (derived from indirect estimate) — acts as a ceiling that can bind in some country contexts.

**RELEVANT SOURCES:**
- Intervention report: "Randomized controlled trials" section, all footnotes on individual studies
- Kremer et al. 2022 working paper (the meta-analysis itself)
- Higgs external review (statistical methods concerns)
- Clasen external review (intervention heterogeneity concerns)
- EA Forum analysis by GiveWell Change Our Mind contest entrants
- Więcek/Gelman discussion on Columbia statistics blog

**OUT OF SCOPE:** External validity adjustments (Thread 2), implementation and adherence (Thread 4), non-mortality benefits (Thread 5). This thread examines the raw evidence base only.

---

### THREAD 2: Internal and External Validity Adjustments

**SCOPE:** Investigate whether GiveWell's adjustments from the base mortality estimate to the final program-specific estimates are correctly calibrated. The base estimate is ~12%; after adjustments, ILC Kenya = ~11% and DSW Kenya = ~6%. The adjustments include: bundled treatment adjustment (-25% internal validity), adherence-based external validity, and the share-of-deaths-from-enteric-infection adjustment.

**KEY QUESTIONS:**
- Is the -25% internal validity adjustment for bundled treatments sufficient? Trials included flocculation, safe storage vessels, and hygiene education. What is the independent contribution of flocculation (which removes Cryptosporidium, a pathogen chlorine cannot eliminate)?
- The adherence adjustment uses Pickering et al. 2019 as the basis for ILC and program monitoring data for DSW. Are these adherence measures reliable? Do they capture the right thing (chlorine residual at point of consumption vs. self-reported use)?
- The external validity adjustment uses national-level enteric infection mortality shares. Do these accurately represent the specific sub-national areas where programs operate (which likely have worse water quality and higher enteric mortality than national averages)?
- The counterfactual chlorination rate (what fraction of people would treat water without the program) was updated from 22% to 10% in Kenya. How sensitive is the result to this parameter?

**CEA PARAMETERS AFFECTED:**
- Internal validity adjustment (-25%) — "Adjustment for bundled treatments" row
- External validity adjustment (adherence component) — varies by program and country
- External validity adjustment (enteric infection share component)
- Counterfactual water treatment rates (Kenya, Uganda, Malawi)

**RELEVANT SOURCES:**
- CEA spreadsheet: "Internal validity adjustment" tab, "External validity" tabs
- Pickering et al. 2019 (ILC adherence)
- DSW monitoring data (program-specific adherence)
- GBD data on enteric infection mortality shares
- GiveWell DSW lookback (2025) — documents updated adjustment values

**OUT OF SCOPE:** The base meta-analytic estimate (Thread 1), cost parameters (Thread 4), mechanism questions (Thread 3).

---

### THREAD 3: The Unexplained Mortality Gap

**SCOPE:** GiveWell's report highlights that the observed mortality reduction (~12-14%) is roughly 4x larger than what would be predicted from chlorine's effect on diarrhea alone (~3.3%, based on 23% diarrhea reduction × 14.5% share of mortality from enteric infections). The report suggests water quality interventions may reduce mortality from non-waterborne diseases, possibly through reduced immune burden or improved nutritional absorption. Investigate whether this gap is real and what mechanisms could explain it.

**KEY QUESTIONS:**
- Is the 4x gap a genuine signal or an artifact of imprecise mortality measurement in underpowered trials?
- What is the evidence for "environmental enteric dysfunction" (EED) — subclinical gut inflammation from contaminated water that impairs nutrient absorption and immune function without causing clinical diarrhea?
- Could the mortality reduction include deaths from conditions exacerbated by diarrhea (e.g., malaria mortality in children weakened by dehydration, pneumonia in malnourished children)?
- Does the plausibility cap methodology adequately capture these indirect pathways? GiveWell's cap uses "all infectious diseases" under generous assumptions, but is this generous enough?
- Historical water improvement studies (e.g., Cutler & Miller on US municipal chlorination) show mortality reductions from non-waterborne diseases. How applicable are these to current low-income settings?

**CEA PARAMETERS AFFECTED:**
- Plausibility cap — if the indirect pathways are real and larger than assumed, the cap may be too low, binding the estimate below its true value
- Base mortality effect interpretation — if the gap is noise rather than signal, the true effect is closer to 3.3% than 12%

**RELEVANT SOURCES:**
- Intervention report: "Studies of historical water quality improvements" section
- Intervention report: discussion of the mortality-diarrhea discrepancy
- Cutler & Miller 2005 (historical US chlorination)
- Kotloff et al. 2013 (GEMS study — pathogen-specific mortality)
- Literature on environmental enteric dysfunction

**OUT OF SCOPE:** Statistical methodology of the meta-analysis (Thread 1), cost and implementation (Thread 4).

---

### THREAD 4: Implementation Fidelity and Cost Parameters

**SCOPE:** Investigate whether the CEA's assumptions about program costs, coverage, adherence in the field, and operational sustainability match reality. The CEA models ILC at ~$1.68/person and DSW at $1.22-$1.87/person. It assumes certain coverage rates and adherence levels. Examine whether these hold under real implementation conditions.

**KEY QUESTIONS:**
- Are cost-per-person estimates stable over time, or do they increase as programs expand to harder-to-reach areas?
- How does chlorine dosing work in practice? The CEA treats chlorine residual as binary (present/absent), but efficacy depends on concentration-time relationships. Are programs achieving adequate chlorine residual at the point of consumption?
- What is the maintenance and replacement cycle for chlorine dispensers and ILC systems? Does the model account for downtime?
- What fraction of the population in targeted areas actually collects water from treated sources (for ILC) or uses dispensers (for DSW)? Are there systematic non-users?
- How do seasonal factors (rainfall, turbidity, temperature) affect chlorine efficacy and dosing requirements?
- What is the supply chain reliability for chlorine? How often do stockouts occur?

**CEA PARAMETERS AFFECTED:**
- Cost per person served (both ILC and DSW)
- Adherence/usage rates (feed into external validity adjustment)
- Effective coverage (fraction of target population actually reached)

**RELEVANT SOURCES:**
- CEA spreadsheet: cost tabs for ILC and DSW
- Evidence Action program monitoring reports
- Pickering et al. 2019 (ILC field performance)
- WHO guidance on chlorine dosing and residual monitoring
- GiveWell DSW lookback (2025)

**OUT OF SCOPE:** Mortality effect size evidence (Threads 1-3), non-mortality benefits (Thread 5).

---

### THREAD 5: Non-Mortality Benefits and Omitted Harms

**SCOPE:** The CEA includes four benefit categories beyond under-5 mortality: over-5 mortality, diarrhea morbidity reduction, development effects (income), and medical costs averted. Investigate whether these are correctly estimated and whether the model omits material benefits or harms.

**KEY QUESTIONS:**
- The over-5 mortality estimate is extrapolated from under-5 data with limited direct evidence. How reliable is this extrapolation?
- Development effects (income benefits) are modeled based on childhood health → adult income literature. Is the causal chain from reduced diarrhea → better nutrition → higher income well-supported?
- Medical costs averted: what healthcare utilization data underpins this estimate? Does it account for the fact that many children in target areas have limited access to formal healthcare?
- **Omitted harms:** Disinfection byproducts (trihalomethanes) from chlorinating water with high organic matter — what is the cancer/reproductive risk at realistic exposure levels? Does this offset mortality benefits?
- **Omitted harms:** Does free chlorination crowd out investment in piped water infrastructure? If so, the long-term welfare cost could be substantial.
- **Omitted benefits:** Reduced school absenteeism, reduced caregiver time burden, reduced waterborne disease in pregnant women (birth outcomes).

**CEA PARAMETERS AFFECTED:**
- Over-5 mortality effect size and adjustment
- Development effects estimate
- Medical costs averted estimate
- No current parameter for DBP harms or infrastructure crowd-out (these would be new)

**RELEVANT SOURCES:**
- CEA spreadsheet: tabs for each benefit category
- WHO guidelines on trihalomethanes in drinking water
- Literature on diarrhea → child development → income pathway
- GiveWell AI red teaming output (flagged turbidity and DBPs as concerns)

**OUT OF SCOPE:** Under-5 mortality evidence (Threads 1-3), program costs (Thread 4).

---

### THREAD 6: Comparative Effectiveness and Intervention Choice

**SCOPE:** GiveWell evaluates ILC and DSW as separate programs but both use chlorination as the mechanism. Investigate whether the choice between intervention types (and the decision not to fund alternatives like household filtration, UV treatment, or piped water) is justified, and whether the CEA framework handles the comparison correctly.

**KEY QUESTIONS:**
- ILC achieves higher effective chlorination rates than DSW because it's automatic. But ILC only works at shared water points — what fraction of target populations use shared points vs. private sources?
- Are there contexts where filtration (which removes Cryptosporidium) would be more cost-effective than chlorination, particularly in areas with high Cryptosporidium burden?
- GiveWell recently added chlorine vouchers as a third modality. How does the voucher CEA compare, and does it suggest the per-modality adjustments are consistent?
- As countries develop, will the target population shift from shared water points to private connections, making ILC obsolete faster than the model assumes?

**CEA PARAMETERS AFFECTED:**
- Adherence rates (differ between ILC and DSW)
- Cost per person (differ between ILC and DSW)
- Room for more funding estimates
- Implicit parameter: what share of waterborne disease burden is addressable by chlorination vs. requiring filtration

**RELEVANT SOURCES:**
- CEA spreadsheet: compare ILC and DSW tabs
- GiveWell chlorine vouchers page
- Clasen review (questioning treatment of heterogeneous interventions as homogeneous)
- Evidence on Cryptosporidium burden in target countries

**OUT OF SCOPE:** Mortality effect size (Threads 1-3), non-mortality benefits (Thread 5).

---

## OUTPUT 2: EXCLUSION LIST

The following concerns are ALREADY ADDRESSED in GiveWell's intervention report or CEA. Investigators must NOT raise these as novel critiques.

```
ALREADY ADDRESSED:

1. Bundled treatments in RCTs inflating effect size
   Addressed in: CEA "Internal validity adjustment" tab; report "Bundled treatments" section
   Summary: GiveWell applies a -25% internal validity adjustment to account for trials
   including flocculation, safe storage, and hygiene components beyond chlorination alone.

2. Publication bias in the Kremer et al. meta-analysis
   Addressed in: Report "Possible publication bias" section
   Summary: GiveWell acknowledges this concern. Kremer et al. ran two tests (Begg's, Andrews-Kasy)
   finding no significant bias, but power was limited. Adjusted estimate under assumed bias = 17%
   reduction. GiveWell uses its own 5-study subset partly to mitigate this.

3. Wide confidence intervals on mortality estimate
   Addressed in: Report "Quantified uncertainty" section
   Summary: 95% CI is 31% reduction to 13% increase. GiveWell acknowledges this and notes
   it does not stand out relative to uncertainty in their other CEAs.

4. Unquantified uncertainty beyond the CI
   Addressed in: Report "Unquantified uncertainty" section (Higgs review)
   Summary: Higgs raised concerns about prediction vs. estimation uncertainty and
   heterogeneity. GiveWell acknowledges uncertainty is likely greater than the CI suggests.

5. Chlorination's limited effectiveness against Cryptosporidium
   Addressed in: Report "Mechanism of action" section
   Summary: Report explicitly notes chlorine has limited effectiveness against protozoan
   parasites including Cryptosporidium. This is a known limitation.

6. Trials not designed to measure mortality as primary outcome
   Addressed in: Report "Mortality assessment methods" section (Clasen review)
   Summary: Clasen flagged that mortality ascertainment methods were likely informal
   (household reports, not death certificates). GiveWell acknowledges this limitation.

7. Heterogeneity of interventions in the meta-analysis
   Addressed in: Report "External validity" section (Clasen review)
   Summary: Clasen criticized pooling chlorination with filtration and spring protection.
   GiveWell's 5-study subset excludes non-chlorination interventions to address this.

8. Preregistration concerns about Kremer et al.
   Addressed in: Report "Limitations of preregistration" section
   Summary: Registry created July 2020 after initial analyses began. GiveWell acknowledges
   this increases risk of specification searching.

9. Mortality-diarrhea discrepancy (observed effect ~4x predicted)
   Addressed in: Report "Conversations with researchers" and "Historical studies" sections
   Summary: GiveWell acknowledges the discrepancy and uses a plausibility cap to bound the
   estimate. They also explore non-diarrheal pathways as potential explanations.

10. Recontamination after chlorination
    Addressed in: Report "Mechanism of action" section (chlorine residual discussion)
    Summary: Report discusses residual chlorine and the importance of storage conditions.
    Some trials included safe storage vessels to address this.

11. Difference in effectiveness between ILC and DSW
    Addressed in: CEA models these separately with different adherence rates and costs
    Summary: DSW has lower effective chlorination increase than ILC because it requires
    active user behavior. This is reflected in different final mortality estimates.

12. Counterfactual water treatment rates
    Addressed in: CEA external validity adjustments; updated in 2024 lookback
    Summary: GiveWell models what fraction of people would treat water without the program
    (Kenya revised from 22% to 10%). Explicitly accounted for.

13. Follow-up length heterogeneity in trials
    Addressed in: Report and Kremer et al. supplementary materials
    Summary: Sensitivity analysis shows short studies have negligible impact on precision.
    GiveWell's 5-study subset requires ≥1 year follow-up.

14. Passive control group concern (Null et al. 2018)
    Addressed in: 2024 DSW lookback
    Summary: GiveWell dropped the Null et al. passive control group from their meta-analysis,
    reducing the base estimate from 14% to 12%.
```

---

## OUTPUT 3: CEA PARAMETER MAP

```
CEA PARAMETER MAP: Water Quality CEA (ILC and DSW)

MODEL STRUCTURE:
- Calculates: Units of value per dollar (expressed as multiples of GiveDirectly
  unconditional cash transfers, "Nx cash")
- Final result: Sum of five benefit categories, each converted to value units
- Programs modeled separately: In-line chlorination (ILC) and Dispensers for Safe Water (DSW),
  each in multiple country contexts (Kenya, Uganda, Malawi, India)

BENEFIT CATEGORIES (approximate share of total value for ILC Kenya):
1. Under-5 mortality reduction: ~45% of total value
2. Over-5 mortality reduction: ~small share
3. Diarrhea morbidity reduction: ~small share
4. Development effects (income): ~35% of total value
5. Medical costs averted: ~19% of total value

KEY PARAMETERS:

1. Base mortality effect size (under-5, pre-adjustment)
   - Current value: ~12% reduction in all-cause mortality (updated from 14% after
     dropping Null et al. passive control)
   - Source: GiveWell's internal meta-analysis of 5 RCTs from Kremer et al. subset
   - Sensitivity: HIGH — this is the single largest driver. A 1pp change here moves
     the bottom line by ~3-4%
   - Adjustments: Internal validity (-25%), external validity (varies by context)

2. Internal validity adjustment
   - Current value: -25% (i.e., multiply base effect by 0.75)
   - Source: GiveWell judgment based on bundled treatments in trial
   - Sensitivity: HIGH — directly scales the mortality benefit
   - Components: Adjustment for flocculation, safe storage, hygiene education in trials

3. External validity adjustment (adherence component)
   - Current value: Varies. For ILC, based on Pickering et al. 2019 chlorine residual data.
     For DSW, based on program monitoring surveys.
   - Source: Ratio of program-achieved chlorination increase to trial-achieved increase
   - Sensitivity: MEDIUM-HIGH — differs substantially between ILC and DSW

4. External validity adjustment (enteric infection share)
   - Current value: Based on GBD national estimates of share of under-5 deaths from
     enteric infections, compared to trial settings
   - Source: GBD Results Tool
   - Sensitivity: MEDIUM — adjusts upward in countries with higher enteric mortality burden

5. Counterfactual water treatment rate
   - Current value: Kenya 10%, Uganda 9%, Malawi 9% (updated 2024)
   - Source: DHS and program monitoring data
   - Sensitivity: MEDIUM — affects the denominator of the adherence adjustment

6. Plausibility cap
   - Current value: Derived from diarrhea morbidity reduction (23%, Clasen et al. 2015)
     × share of mortality from conditions plausibly affected by chlorination
   - Source: Indirect estimate methodology
   - Sensitivity: CONTEXT-DEPENDENT — binds in some country contexts (e.g., DSW Kenya
     where direct estimate was 6.1% but cap was 5.6%)

7. Cost per person served
   - Current value: ILC ~$1.68/person; DSW $1.22-$1.87/person (varies by country)
   - Source: Program cost data from Evidence Action
   - Sensitivity: MEDIUM — linear relationship with cost-effectiveness

8. Diarrhea morbidity reduction
   - Current value: ~23% (from Clasen et al. 2015 Cochrane review)
   - Source: Meta-analysis of chlorination trials with diarrhea outcomes
   - Sensitivity: LOW for overall result (morbidity is small share of total value),
     but HIGH for plausibility cap calculation

9. Development effects (income increase)
   - Current value: Based on childhood health → adult income literature
   - Source: Various (likely Baird et al. deworming extrapolation framework)
   - Sensitivity: MEDIUM — ~35% of total value for ILC

10. Medical costs averted
    - Current value: Based on healthcare utilization estimates
    - Source: Country-specific health expenditure data
    - Sensitivity: MEDIUM — ~19% of total value for ILC

ADJUSTMENT CHAIN (for under-5 mortality):

Base meta-analytic estimate (~12%)
  → Apply internal validity adjustment (×0.75) = ~9%
    → Apply external validity adjustment:
       - Adherence ratio (program vs. trial chlorination increase)
       - Enteric infection share ratio (program setting vs. trial setting)
       = ~6-11% depending on program and country
        → Check against plausibility cap
           - If adjusted estimate > cap: use cap
           - If adjusted estimate < cap: use adjusted estimate
             → Final under-5 mortality reduction used in CEA

LARGEST DRIVERS (parameters that most affect bottom-line cost-effectiveness):
1. Base mortality effect size — highest sensitivity by far
2. Internal validity adjustment — directly scales the largest benefit category
3. External validity adjustment (adherence) — explains most of the ILC vs. DSW gap
4. Cost per person served — linear relationship
5. Development effects estimate — second-largest benefit category for ILC
```

---

## NOTES FOR DOWNSTREAM AGENTS

**Priority ordering:** Thread 1 (mortality effect size) and Thread 2 (adjustments) target the highest-sensitivity parameters and should be investigated first. Thread 3 (mortality gap) is conceptually important but may be hard to resolve with available evidence. Thread 4 (implementation) and Thread 5 (non-mortality) are important but target lower-sensitivity parameters. Thread 6 (comparative effectiveness) is lowest priority for the CEA but relevant for GiveWell's portfolio decisions.

**Key tension in the CEA:** The direct mortality evidence suggests a ~12% effect. The indirect evidence (diarrhea → mortality) suggests ~3.3%. GiveWell uses the direct evidence but caps it with a plausibility estimate derived from the indirect pathway under generous assumptions. Whether this cap is too high, too low, or correctly calibrated is probably the single most consequential question for this CEA.

**Thread 3 investigates in both directions.** Most red teaming assumes the goal is to find overestimates — reasons the intervention is less effective than claimed. Thread 3 is deliberately designed to also investigate whether GiveWell may be *underestimating* the effect. The plausibility cap constrains the direct evidence downward based on an indirect model of how chlorination should affect mortality. If the environmental enteric dysfunction pathway is real, the cap may be too conservative. This could reflect a deliberate methodological choice toward conservatism, or it could reflect an unexamined assumption about mechanism. Either way, it's worth surfacing — GiveWell should know whether their cap is a considered judgment or an inherited default, and if it's binding in program contexts, the stakes are high.

**What GiveWell's own AI red teaming found:** The water chlorination AI output surfaced 4 critiques worth investigating: water turbidity (novel), infrastructure crowd-out (valid but hallucinated evidence), chlorine dosing optimization (known), and disinfection byproducts (known). All four fall within our thread structure. Thread 4 covers turbidity and dosing; Thread 5 covers crowd-out and byproducts. Our pipeline should aim to find these AND additional critiques their single-pass approach missed.
