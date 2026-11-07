--- Critique: Selection-on-success makes the "conditional 10%" an upward-biased estimate (winner's curse), and it is not shrunk ---

## Critique 1: Selection-on-success / winner's curse on the 10% effect

**CLAIM CHECK**
- **Selection on a significance or efficacy bar inflates the observed effect estimate, especially in small or underpowered trials.** Status: PLAUSIBLE. This is standard statistical reasoning. My search on empirical evidence (for example, truncated-trial literature) hit the tool limit, so I did not confirm it with a source. I am relying on general knowledge here.
- **The Phase IIa/b trial is "a few hundred participants at most" and powered for surrogates.** Status: UNVERIFIABLE. I don't have the grant or the trial's identity. I can't confirm the sample size, CIs or powering. The Investigator marked this as UNGROUNDED and it remains so.
- **The 10% figure was derived from the surrogate-endpoint trial.** Status: UNVERIFIABLE. This is stated only as a conditional ("if they drove the 10% figure"). I can't check where the 10% came from.
- **A shrinkage factor of 0.5–0.8 gives rr of 0.05–0.08 and SROI of about 1,500–2,400x.** Status: arithmetic PLAUSIBLE. It implies a base SROI of about 3,000x (0.5×3,000 and 0.8×3,000), and SROI scales linearly with rr. I can't verify the base SROI. The Investigator correctly labels the 0.5–0.8 range as their own inference, with no TB-specific source.

**Logic problems**
- Winner's curse biases the observed estimate. It biases the true effect only if the model treats the observed effect as the truth. The hypothesis blurs this. In its words, the 10% "should be treated as the *true* mortality effect," and the same passage says there is no basis for assuming that.
- The critique only bites if the 10% is a point estimate from a trial or surrogate. If the 10% is a prior or expert assumption, the argument shifts to a surrogate-to-mortality translation problem. That is a different and weaker bias argument.
- Conditioning on success does raise the posterior mean of the true effect relative to the unconditional mean. So the CEA's conditional-on-success 10% is not automatically biased. The question is whether 10% is the posterior mean given success, or the observed effect in a successful trial.

**EVIDENCE FOUND**
- Nothing TB-specific on shrinkage.
- Related background: in trials of adjuncts such as corticosteroids in TB meningitis, a pooled estimate gave RR 0.84 (95% CI 0.76–0.94) for mortality. 
Corticosteroids significantly reduced all-cause mortality (RR = 0.84, 95% CI: 0.76–0.94, p = 0.002) with low heterogeneity.
 That is a roughly 16% relative reduction in a very high-mortality condition. It is a useful reference point for the plausible size of an adjunct mortality effect, but it is not evidence of winner's curse.
- Cochrane found an older, smaller pooled estimate of RR 0.79 in 
six trials of 595 patients
, versus 0.84 in the later, larger pooled analysis. That is mildly consistent with small-sample inflation, though it is not a clean test.

**OVERALL VERDICT: PARTIALLY VERIFIED (hypothesis sound but UNGROUNDED)**
The logic is valid. The empirical specifics (trial size, source of the 10%, shrinkage factor) are unverifiable.

**REVISED CRITIQUE**
If the CEA's 10% mortality reduction is taken from a small surrogate-powered trial, or from the observed effect in a trial that cleared a significance bar, it is likely an overestimate of the true effect. Treat this as an UNGROUNDED but plausible hypothesis. Recommend a sensitivity analysis on `relative_reduction`, for example 5–10%, with no claim about the specific shrinkage factor. The 0.5–0.8 factor is an illustrative assumption. Strength: **low–medium**. It is conditional on how the 10% was derived, which is not established.

---

## Critique 2: A mortality-powered Phase III costs several multiples of $7M

**CITATION / CLAIM CHECK**
- **n ≈ 23,400 per arm (about 47,000 total) at 6.0% vs 5.4%.** VERIFIED by my recomputation. The variance term is 0.0564 + 0.051084 = 0.107484. Multiplied by 7.84 and divided by 0.006², it gives about 23,400.
- **n ≈ 48,000 per arm (about 96,000 total) at 3.0% vs 2.7%.** VERIFIED. Variance term 0.055371 × 7.84 / 0.003² ≈ 48,200.
- **Cost arithmetic.** VERIFIED. 47,000 × $500 ≈ $23.5M, 47,000 × $1,000 ≈ $47M, and 96,000 × $500 ≈ $48M.
- **"SROI would fall roughly in proportion, by about 70% or more."** PLAUSIBLE. Going from $7M to $24M is about 3.4×, which is about a 71% fall. This holds only if all-in cost is the SROI denominator and the trial replaces the $7M rather than adding to it.
- **Study 31/A5349 enrolled about 2,500.** VERIFIED. 
Among 2516 participants who had undergone randomization
. It was a noninferiority design. 
An international randomized open-label phase 3 noninferiority trial.
 The primary outcome was 
survival free of tuberculosis at 12 months.

- **REMoxTB about 1,900.** NOT CHECKED in my searches. From memory it is about 1,931, which matches. Treat as plausible.
- **TRUNCATE-TB "several hundred."** VERIFIED. 
675 participants (674 in the intention-to-treat population) were enrolled.

- **RIFASHORT "several hundred."** VERIFIED. 
A total of 672 participants were randomly assigned.

- **SimpliciTB several hundred.** NOT CHECKED. It is listed as a completed Phase 3 trial, but I did not retrieve its enrollment (about 455 from memory).
- **These trials were powered for non-inferiority on unfavourable outcome, not mortality.** VERIFIED for Study 31. TRUNCATE-TB's primary outcome was also an unfavourable-outcome measure. 
A primary-outcome event occurred in 7 of the 181 participants (3.9%) in the standard-treatment group.
 I did not verify the design details for RIFASHORT and SimpliciTB.
- **Trial-arm mortality is lower than community case-fatality, which raises N.** PLAUSIBLE. This is a general trial-design principle. I found no specific data in this search. The 3% figure is an assumption.
- **$500–$1,000 per participant.** UNGROUNDED, and the evidence suggests it is probably too low (see below).

**EVIDENCE FOUND**
- The cost data supports the direction of the critique. 
Total costs for TB-PRACTECAL were €33.9 million and the average cost per patient was €61,460.
 That is a drug-resistant TB trial with hospital-level care, so it is not comparable on a per-patient basis.
- A systematic review in the same paper found a wide range: 
reported costs per trial ranged US$7–221 million.
 Notably, $7M is the very bottom of that range.
- A modelling study of a TB vaccine trial estimated 
a total cost of $120 million, including $30 million in start-up/infrastructure costs, and $90 million for recruitment and follow-up ($7,500 per subject)
, for 12,000 infants. This is a different setting and indication, and an older estimate.
- Together these suggest $500–$1,000 per participant is a low bound and the real cost could be higher. That strengthens the critique.
- **Counter-considerations the Investigator omitted:**
  - Mortality-powered trials in high-mortality populations need far fewer participants. In TB meningitis, case fatality can reach about 50% in resource-limited settings, per 
a case fatality rate of up to 50%
. N is much smaller there than at 6% baseline mortality.
  - Trials are usually powered for larger hypothesized effects than 10%. IMPI hypothesised 
a 30% reduction in mortality
. That requires a much smaller N, but a true 10% effect would then be underpowered.
  - IMPI enrolled 1,400 participants, and 
did not show a mortality benefit
. Even 1,400-person mortality-focused trials are difficult.
  - Large events-driven or pragmatic registry-embedded trials can cost far less per participant.

**OVERALL VERDICT: PARTIALLY VERIFIED**
The arithmetic and the trial-size comparison hold. The cost per participant is ungrounded, and what the $7M covers is unknown. The critique also assumes the Phase III must be powered for a 10% effect on all-cause mortality, which is a design choice, not a given.

**REVISED CRITIQUE**
Detecting a 10% relative reduction from 6.0% baseline mortality needs about 47,000 participants (about 23,400 per arm) at α=0.05 and 80% power. At 3% baseline it needs about 96,000. This is 20–40 times the size of recent pivotal TB regimen trials (about 450–2,500 participants). That makes a $7M all-in budget implausible for a mortality-powered Phase III, unless the design is enriched for high-mortality populations or powered for a larger effect. The $500–$1,000 per participant cost is ungrounded. Available TB-trial cost evidence is consistent with it being a lower bound. The "70% or more" SROI fall is illustrative. It holds only if the trial cost replaces the budgeted amount and dominates all-in cost. Strength: **large if the CEA assumes a mortality-powered Phase III, otherwise conditional.** This should be paired with Critique 3 as an either/or.

---

## Critique 3: If Phase III is surrogate-powered, costs and benefits describe different interventions

**CITATION / CLAIM CHECK**
- **GRADE rates certainty down for indirectness when the outcome is a surrogate.** VERIFIED in the GRADE methodology. 
Authors should rate the importance of the patient-important outcome for which the surrogate is a substitute and subsequently rate down the quality of evidence for indirectness of outcome.
 WHO guidance for vaccine recommendations says the same. 
If important outcomes are represented by a surrogate, they will frequently require down-rating of the quality of evidence for indirectness.
 The downgrade is 
by one or two levels
.
- **WHO uses GRADE.** VERIFIED. WHO TB guidelines follow the Handbook with GRADE, for example 
the WHO Handbook for guideline development, 2014
. I did not retrieve the Handbook text itself.
- **Corticosteroid recommendations for TB meningitis rested on mortality or clinical-outcome trials.** VERIFIED for TBM. 
Randomized controlled trials ... included death or disability as outcome measures.
 Cochrane graded the mortality benefit as 
high quality evidence of the benefit of corticosteroids in preventing death.

- **The same for pericarditis.** PARTIALLY VERIFIED. IMPI (1,400 participants) used clinical outcomes (death, tamponade, constriction). 
Prednisolone did not significantly affect mortality, cardiac tamponade necessitating pericardiocentesis, or constrictive pericarditis.
 The pericarditis example therefore doesn't show that mortality evidence led to a recommendation. It shows a large clinical-outcome trial that was null on mortality. Cochrane found 
corticosteroids probably reduce deaths from pericarditis
 (moderate certainty) with broader all-cause mortality evidence of low certainty.
- **"The only way to keep a Phase III near $7M is to power it on a surrogate or composite."** PLAUSIBLE but not shown. It follows from Critique 2's arithmetic, but a high-mortality enrichment is a counter-example.
- **Whether this grant's Phase III is surrogate-powered.** UNVERIFIABLE. The Investigator flags this as UNGROUNDED.

**Conceptual issues**
- Unfavourable outcome and relapse are not necessarily "surrogates" in the GRADE sense. They are often treated as patient-important outcomes. Only culture conversion and CXR or lung function are clearly surrogates. WHO's TB regimen recommendations have been based on noninferiority trials for unfavourable outcome. For example, 
Study 31 was a randomized, multi-national, open-label, controlled phase 3 trial
 that informed a WHO rapid communication. So a regimen could be recommended without mortality-powered evidence. Adjuncts (host-directed therapies) are a harder case, because the mortality benefit is the whole claim.
- "If WHO requires mortality evidence, the scenario collapses into Critique 1" refers to the cost critique, which is Critique 2 in this batch. The cross-reference is wrong.
- The downgrade for indirectness reduces certainty. It does not prevent a recommendation. The critique acknowledges this, noting conditional adoption.
- This critique overlaps heavily with Critique 2. They are two branches of the same dilemma and should be merged.

**OVERALL VERDICT: PARTIALLY VERIFIED**
The GRADE mechanism is correct. The dilemma structure is logically sound. The magnitude is unquantified and the key premise (the grant's trial design) is unknown.

**REVISED CRITIQUE**
There is a possible inconsistency between cost and benefit. If the budgeted Phase III is powered on a surrogate (for example culture conversion) rather than mortality, the CEA credits a 10% mortality benefit that the trial would not test. Under GRADE, WHO typically rates down certainty for indirectness when evidence relies on surrogates. That is likely to make recommendations conditional and slow adoption (`speedup_years`, coverage), or require a follow-on mortality trial. If the trial is mortality-powered, the cost problem in Critique 2 applies instead. This dilemma should be merged with Critique 2 into a single "cost–benefit design consistency" critique. Corticosteroids for TB meningitis are a supporting precedent, because the recommendation rests on mortality trials. Strength: **medium–large, conditional.** The grant's actual Phase III endpoint must be confirmed. The claim that surrogate-only evidence would block or delay a WHO recommendation is not established for regimen-type trials. Unfavourable outcome is a patient-important composite, not a pure surrogate.

--- Critique: A mortality-powered Phase III costs several multiples of $7M, and trial-population mortality makes it worse ---

## Critique 1: Selection-on-success / winner's curse on the 10% effect

**CLAIM CHECK**
- **Selection on a significance or efficacy bar inflates the observed effect estimate, especially in small or underpowered trials.** Status: PLAUSIBLE. This is standard statistical reasoning. My search on empirical evidence (for example, truncated-trial literature) hit the tool limit, so I did not confirm it with a source. I am relying on general knowledge here.
- **The Phase IIa/b trial is "a few hundred participants at most" and powered for surrogates.** Status: UNVERIFIABLE. I don't have the grant or the trial's identity. I can't confirm the sample size, CIs or powering. The Investigator marked this as UNGROUNDED and it remains so.
- **The 10% figure was derived from the surrogate-endpoint trial.** Status: UNVERIFIABLE. This is stated only as a conditional ("if they drove the 10% figure"). I can't check where the 10% came from.
- **A shrinkage factor of 0.5–0.8 gives rr of 0.05–0.08 and SROI of about 1,500–2,400x.** Status: arithmetic PLAUSIBLE. It implies a base SROI of about 3,000x (0.5×3,000 and 0.8×3,000), and SROI scales linearly with rr. I can't verify the base SROI. The Investigator correctly labels the 0.5–0.8 range as their own inference, with no TB-specific source.

**Logic problems**
- Winner's curse biases the observed estimate. It biases the true effect only if the model treats the observed effect as the truth. The hypothesis blurs this. In its words, the 10% "should be treated as the *true* mortality effect," and the same passage says there is no basis for assuming that.
- The critique only bites if the 10% is a point estimate from a trial or surrogate. If the 10% is a prior or expert assumption, the argument shifts to a surrogate-to-mortality translation problem. That is a different and weaker bias argument.
- Conditioning on success does raise the posterior mean of the true effect relative to the unconditional mean. So the CEA's conditional-on-success 10% is not automatically biased. The question is whether 10% is the posterior mean given success, or the observed effect in a successful trial.

**EVIDENCE FOUND**
- Nothing TB-specific on shrinkage.
- Related background: in trials of adjuncts such as corticosteroids in TB meningitis, a pooled estimate gave RR 0.84 (95% CI 0.76–0.94) for mortality. 
Corticosteroids significantly reduced all-cause mortality (RR = 0.84, 95% CI: 0.76–0.94, p = 0.002) with low heterogeneity.
 That is a roughly 16% relative reduction in a very high-mortality condition. It is a useful reference point for the plausible size of an adjunct mortality effect, but it is not evidence of winner's curse.
- Cochrane found an older, smaller pooled estimate of RR 0.79 in 
six trials of 595 patients
, versus 0.84 in the later, larger pooled analysis. That is mildly consistent with small-sample inflation, though it is not a clean test.

**OVERALL VERDICT: PARTIALLY VERIFIED (hypothesis sound but UNGROUNDED)**
The logic is valid. The empirical specifics (trial size, source of the 10%, shrinkage factor) are unverifiable.

**REVISED CRITIQUE**
If the CEA's 10% mortality reduction is taken from a small surrogate-powered trial, or from the observed effect in a trial that cleared a significance bar, it is likely an overestimate of the true effect. Treat this as an UNGROUNDED but plausible hypothesis. Recommend a sensitivity analysis on `relative_reduction`, for example 5–10%, with no claim about the specific shrinkage factor. The 0.5–0.8 factor is an illustrative assumption. Strength: **low–medium**. It is conditional on how the 10% was derived, which is not established.

---

## Critique 2: A mortality-powered Phase III costs several multiples of $7M

**CITATION / CLAIM CHECK**
- **n ≈ 23,400 per arm (about 47,000 total) at 6.0% vs 5.4%.** VERIFIED by my recomputation. The variance term is 0.0564 + 0.051084 = 0.107484. Multiplied by 7.84 and divided by 0.006², it gives about 23,400.
- **n ≈ 48,000 per arm (about 96,000 total) at 3.0% vs 2.7%.** VERIFIED. Variance term 0.055371 × 7.84 / 0.003² ≈ 48,200.
- **Cost arithmetic.** VERIFIED. 47,000 × $500 ≈ $23.5M, 47,000 × $1,000 ≈ $47M, and 96,000 × $500 ≈ $48M.
- **"SROI would fall roughly in proportion, by about 70% or more."** PLAUSIBLE. Going from $7M to $24M is about 3.4×, which is about a 71% fall. This holds only if all-in cost is the SROI denominator and the trial replaces the $7M rather than adding to it.
- **Study 31/A5349 enrolled about 2,500.** VERIFIED. 
Among 2516 participants who had undergone randomization
. It was a noninferiority design. 
An international randomized open-label phase 3 noninferiority trial.
 The primary outcome was 
survival free of tuberculosis at 12 months.

- **REMoxTB about 1,900.** NOT CHECKED in my searches. From memory it is about 1,931, which matches. Treat as plausible.
- **TRUNCATE-TB "several hundred."** VERIFIED. 
675 participants (674 in the intention-to-treat population) were enrolled.

- **RIFASHORT "several hundred."** VERIFIED. 
A total of 672 participants were randomly assigned.

- **SimpliciTB several hundred.** NOT CHECKED. It is listed as a completed Phase 3 trial, but I did not retrieve its enrollment (about 455 from memory).
- **These trials were powered for non-inferiority on unfavourable outcome, not mortality.** VERIFIED for Study 31. TRUNCATE-TB's primary outcome was also an unfavourable-outcome measure. 
A primary-outcome event occurred in 7 of the 181 participants (3.9%) in the standard-treatment group.
 I did not verify the design details for RIFASHORT and SimpliciTB.
- **Trial-arm mortality is lower than community case-fatality, which raises N.** PLAUSIBLE. This is a general trial-design principle. I found no specific data in this search. The 3% figure is an assumption.
- **$500–$1,000 per participant.** UNGROUNDED, and the evidence suggests it is probably too low (see below).

**EVIDENCE FOUND**
- The cost data supports the direction of the critique. 
Total costs for TB-PRACTECAL were €33.9 million and the average cost per patient was €61,460.
 That is a drug-resistant TB trial with hospital-level care, so it is not comparable on a per-patient basis.
- A systematic review in the same paper found a wide range: 
reported costs per trial ranged US$7–221 million.
 Notably, $7M is the very bottom of that range.
- A modelling study of a TB vaccine trial estimated 
a total cost of $120 million, including $30 million in start-up/infrastructure costs, and $90 million for recruitment and follow-up ($7,500 per subject)
, for 12,000 infants. This is a different setting and indication, and an older estimate.
- Together these suggest $500–$1,000 per participant is a low bound and the real cost could be higher. That strengthens the critique.
- **Counter-considerations the Investigator omitted:**
  - Mortality-powered trials in high-mortality populations need far fewer participants. In TB meningitis, case fatality can reach about 50% in resource-limited settings, per 
a case fatality rate of up to 50%
. N is much smaller there than at 6% baseline mortality.
  - Trials are usually powered for larger hypothesized effects than 10%. IMPI hypothesised 
a 30% reduction in mortality
. That requires a much smaller N, but a true 10% effect would then be underpowered.
  - IMPI enrolled 1,400 participants, and 
did not show a mortality benefit
. Even 1,400-person mortality-focused trials are difficult.
  - Large events-driven or pragmatic registry-embedded trials can cost far less per participant.

**OVERALL VERDICT: PARTIALLY VERIFIED**
The arithmetic and the trial-size comparison hold. The cost per participant is ungrounded, and what the $7M covers is unknown. The critique also assumes the Phase III must be powered for a 10% effect on all-cause mortality, which is a design choice, not a given.

**REVISED CRITIQUE**
Detecting a 10% relative reduction from 6.0% baseline mortality needs about 47,000 participants (about 23,400 per arm) at α=0.05 and 80% power. At 3% baseline it needs about 96,000. This is 20–40 times the size of recent pivotal TB regimen trials (about 450–2,500 participants). That makes a $7M all-in budget implausible for a mortality-powered Phase III, unless the design is enriched for high-mortality populations or powered for a larger effect. The $500–$1,000 per participant cost is ungrounded. Available TB-trial cost evidence is consistent with it being a lower bound. The "70% or more" SROI fall is illustrative. It holds only if the trial cost replaces the budgeted amount and dominates all-in cost. Strength: **large if the CEA assumes a mortality-powered Phase III, otherwise conditional.** This should be paired with Critique 3 as an either/or.

---

## Critique 3: If Phase III is surrogate-powered, costs and benefits describe different interventions

**CITATION / CLAIM CHECK**
- **GRADE rates certainty down for indirectness when the outcome is a surrogate.** VERIFIED in the GRADE methodology. 
Authors should rate the importance of the patient-important outcome for which the surrogate is a substitute and subsequently rate down the quality of evidence for indirectness of outcome.
 WHO guidance for vaccine recommendations says the same. 
If important outcomes are represented by a surrogate, they will frequently require down-rating of the quality of evidence for indirectness.
 The downgrade is 
by one or two levels
.
- **WHO uses GRADE.** VERIFIED. WHO TB guidelines follow the Handbook with GRADE, for example 
the WHO Handbook for guideline development, 2014
. I did not retrieve the Handbook text itself.
- **Corticosteroid recommendations for TB meningitis rested on mortality or clinical-outcome trials.** VERIFIED for TBM. 
Randomized controlled trials ... included death or disability as outcome measures.
 Cochrane graded the mortality benefit as 
high quality evidence of the benefit of corticosteroids in preventing death.

- **The same for pericarditis.** PARTIALLY VERIFIED. IMPI (1,400 participants) used clinical outcomes (death, tamponade, constriction). 
Prednisolone did not significantly affect mortality, cardiac tamponade necessitating pericardiocentesis, or constrictive pericarditis.
 The pericarditis example therefore doesn't show that mortality evidence led to a recommendation. It shows a large clinical-outcome trial that was null on mortality. Cochrane found 
corticosteroids probably reduce deaths from pericarditis
 (moderate certainty) with broader all-cause mortality evidence of low certainty.
- **"The only way to keep a Phase III near $7M is to power it on a surrogate or composite."** PLAUSIBLE but not shown. It follows from Critique 2's arithmetic, but a high-mortality enrichment is a counter-example.
- **Whether this grant's Phase III is surrogate-powered.** UNVERIFIABLE. The Investigator flags this as UNGROUNDED.

**Conceptual issues**
- Unfavourable outcome and relapse are not necessarily "surrogates" in the GRADE sense. They are often treated as patient-important outcomes. Only culture conversion and CXR or lung function are clearly surrogates. WHO's TB regimen recommendations have been based on noninferiority trials for unfavourable outcome. For example, 
Study 31 was a randomized, multi-national, open-label, controlled phase 3 trial
 that informed a WHO rapid communication. So a regimen could be recommended without mortality-powered evidence. Adjuncts (host-directed therapies) are a harder case, because the mortality benefit is the whole claim.
- "If WHO requires mortality evidence, the scenario collapses into Critique 1" refers to the cost critique, which is Critique 2 in this batch. The cross-reference is wrong.
- The downgrade for indirectness reduces certainty. It does not prevent a recommendation. The critique acknowledges this, noting conditional adoption.
- This critique overlaps heavily with Critique 2. They are two branches of the same dilemma and should be merged.

**OVERALL VERDICT: PARTIALLY VERIFIED**
The GRADE mechanism is correct. The dilemma structure is logically sound. The magnitude is unquantified and the key premise (the grant's trial design) is unknown.

**REVISED CRITIQUE**
There is a possible inconsistency between cost and benefit. If the budgeted Phase III is powered on a surrogate (for example culture conversion) rather than mortality, the CEA credits a 10% mortality benefit that the trial would not test. Under GRADE, WHO typically rates down certainty for indirectness when evidence relies on surrogates. That is likely to make recommendations conditional and slow adoption (`speedup_years`, coverage), or require a follow-on mortality trial. If the trial is mortality-powered, the cost problem in Critique 2 applies instead. This dilemma should be merged with Critique 2 into a single "cost–benefit design consistency" critique. Corticosteroids for TB meningitis are a supporting precedent, because the recommendation rests on mortality trials. Strength: **medium–large, conditional.** The grant's actual Phase III endpoint must be confirmed. The claim that surrogate-only evidence would block or delay a WHO recommendation is not established for regimen-type trials. Unfavourable outcome is a patient-important composite, not a pure surrogate.

--- Critique: If Phase III is surrogate-powered, costs and benefits describe different interventions ---

## Critique 1: Selection-on-success / winner's curse on the 10% effect

**CLAIM CHECK**
- **Selection on a significance or efficacy bar inflates the observed effect estimate, especially in small or underpowered trials.** Status: PLAUSIBLE. This is standard statistical reasoning. My search on empirical evidence (for example, truncated-trial literature) hit the tool limit, so I did not confirm it with a source. I am relying on general knowledge here.
- **The Phase IIa/b trial is "a few hundred participants at most" and powered for surrogates.** Status: UNVERIFIABLE. I don't have the grant or the trial's identity. I can't confirm the sample size, CIs or powering. The Investigator marked this as UNGROUNDED and it remains so.
- **The 10% figure was derived from the surrogate-endpoint trial.** Status: UNVERIFIABLE. This is stated only as a conditional ("if they drove the 10% figure"). I can't check where the 10% came from.
- **A shrinkage factor of 0.5–0.8 gives rr of 0.05–0.08 and SROI of about 1,500–2,400x.** Status: arithmetic PLAUSIBLE. It implies a base SROI of about 3,000x (0.5×3,000 and 0.8×3,000), and SROI scales linearly with rr. I can't verify the base SROI. The Investigator correctly labels the 0.5–0.8 range as their own inference, with no TB-specific source.

**Logic problems**
- Winner's curse biases the observed estimate. It biases the true effect only if the model treats the observed effect as the truth. The hypothesis blurs this. In its words, the 10% "should be treated as the *true* mortality effect," and the same passage says there is no basis for assuming that.
- The critique only bites if the 10% is a point estimate from a trial or surrogate. If the 10% is a prior or expert assumption, the argument shifts to a surrogate-to-mortality translation problem. That is a different and weaker bias argument.
- Conditioning on success does raise the posterior mean of the true effect relative to the unconditional mean. So the CEA's conditional-on-success 10% is not automatically biased. The question is whether 10% is the posterior mean given success, or the observed effect in a successful trial.

**EVIDENCE FOUND**
- Nothing TB-specific on shrinkage.
- Related background: in trials of adjuncts such as corticosteroids in TB meningitis, a pooled estimate gave RR 0.84 (95% CI 0.76–0.94) for mortality. 
Corticosteroids significantly reduced all-cause mortality (RR = 0.84, 95% CI: 0.76–0.94, p = 0.002) with low heterogeneity.
 That is a roughly 16% relative reduction in a very high-mortality condition. It is a useful reference point for the plausible size of an adjunct mortality effect, but it is not evidence of winner's curse.
- Cochrane found an older, smaller pooled estimate of RR 0.79 in 
six trials of 595 patients
, versus 0.84 in the later, larger pooled analysis. That is mildly consistent with small-sample inflation, though it is not a clean test.

**OVERALL VERDICT: PARTIALLY VERIFIED (hypothesis sound but UNGROUNDED)**
The logic is valid. The empirical specifics (trial size, source of the 10%, shrinkage factor) are unverifiable.

**REVISED CRITIQUE**
If the CEA's 10% mortality reduction is taken from a small surrogate-powered trial, or from the observed effect in a trial that cleared a significance bar, it is likely an overestimate of the true effect. Treat this as an UNGROUNDED but plausible hypothesis. Recommend a sensitivity analysis on `relative_reduction`, for example 5–10%, with no claim about the specific shrinkage factor. The 0.5–0.8 factor is an illustrative assumption. Strength: **low–medium**. It is conditional on how the 10% was derived, which is not established.

---

## Critique 2: A mortality-powered Phase III costs several multiples of $7M

**CITATION / CLAIM CHECK**
- **n ≈ 23,400 per arm (about 47,000 total) at 6.0% vs 5.4%.** VERIFIED by my recomputation. The variance term is 0.0564 + 0.051084 = 0.107484. Multiplied by 7.84 and divided by 0.006², it gives about 23,400.
- **n ≈ 48,000 per arm (about 96,000 total) at 3.0% vs 2.7%.** VERIFIED. Variance term 0.055371 × 7.84 / 0.003² ≈ 48,200.
- **Cost arithmetic.** VERIFIED. 47,000 × $500 ≈ $23.5M, 47,000 × $1,000 ≈ $47M, and 96,000 × $500 ≈ $48M.
- **"SROI would fall roughly in proportion, by about 70% or more."** PLAUSIBLE. Going from $7M to $24M is about 3.4×, which is about a 71% fall. This holds only if all-in cost is the SROI denominator and the trial replaces the $7M rather than adding to it.
- **Study 31/A5349 enrolled about 2,500.** VERIFIED. 
Among 2516 participants who had undergone randomization
. It was a noninferiority design. 
An international randomized open-label phase 3 noninferiority trial.
 The primary outcome was 
survival free of tuberculosis at 12 months.

- **REMoxTB about 1,900.** NOT CHECKED in my searches. From memory it is about 1,931, which matches. Treat as plausible.
- **TRUNCATE-TB "several hundred."** VERIFIED. 
675 participants (674 in the intention-to-treat population) were enrolled.

- **RIFASHORT "several hundred."** VERIFIED. 
A total of 672 participants were randomly assigned.

- **SimpliciTB several hundred.** NOT CHECKED. It is listed as a completed Phase 3 trial, but I did not retrieve its enrollment (about 455 from memory).
- **These trials were powered for non-inferiority on unfavourable outcome, not mortality.** VERIFIED for Study 31. TRUNCATE-TB's primary outcome was also an unfavourable-outcome measure. 
A primary-outcome event occurred in 7 of the 181 participants (3.9%) in the standard-treatment group.
 I did not verify the design details for RIFASHORT and SimpliciTB.
- **Trial-arm mortality is lower than community case-fatality, which raises N.** PLAUSIBLE. This is a general trial-design principle. I found no specific data in this search. The 3% figure is an assumption.
- **$500–$1,000 per participant.** UNGROUNDED, and the evidence suggests it is probably too low (see below).

**EVIDENCE FOUND**
- The cost data supports the direction of the critique. 
Total costs for TB-PRACTECAL were €33.9 million and the average cost per patient was €61,460.
 That is a drug-resistant TB trial with hospital-level care, so it is not comparable on a per-patient basis.
- A systematic review in the same paper found a wide range: 
reported costs per trial ranged US$7–221 million.
 Notably, $7M is the very bottom of that range.
- A modelling study of a TB vaccine trial estimated 
a total cost of $120 million, including $30 million in start-up/infrastructure costs, and $90 million for recruitment and follow-up ($7,500 per subject)
, for 12,000 infants. This is a different setting and indication, and an older estimate.
- Together these suggest $500–$1,000 per participant is a low bound and the real cost could be higher. That strengthens the critique.
- **Counter-considerations the Investigator omitted:**
  - Mortality-powered trials in high-mortality populations need far fewer participants. In TB meningitis, case fatality can reach about 50% in resource-limited settings, per 
a case fatality rate of up to 50%
. N is much smaller there than at 6% baseline mortality.
  - Trials are usually powered for larger hypothesized effects than 10%. IMPI hypothesised 
a 30% reduction in mortality
. That requires a much smaller N, but a true 10% effect would then be underpowered.
  - IMPI enrolled 1,400 participants, and 
did not show a mortality benefit
. Even 1,400-person mortality-focused trials are difficult.
  - Large events-driven or pragmatic registry-embedded trials can cost far less per participant.

**OVERALL VERDICT: PARTIALLY VERIFIED**
The arithmetic and the trial-size comparison hold. The cost per participant is ungrounded, and what the $7M covers is unknown. The critique also assumes the Phase III must be powered for a 10% effect on all-cause mortality, which is a design choice, not a given.

**REVISED CRITIQUE**
Detecting a 10% relative reduction from 6.0% baseline mortality needs about 47,000 participants (about 23,400 per arm) at α=0.05 and 80% power. At 3% baseline it needs about 96,000. This is 20–40 times the size of recent pivotal TB regimen trials (about 450–2,500 participants). That makes a $7M all-in budget implausible for a mortality-powered Phase III, unless the design is enriched for high-mortality populations or powered for a larger effect. The $500–$1,000 per participant cost is ungrounded. Available TB-trial cost evidence is consistent with it being a lower bound. The "70% or more" SROI fall is illustrative. It holds only if the trial cost replaces the budgeted amount and dominates all-in cost. Strength: **large if the CEA assumes a mortality-powered Phase III, otherwise conditional.** This should be paired with Critique 3 as an either/or.

---

## Critique 3: If Phase III is surrogate-powered, costs and benefits describe different interventions

**CITATION / CLAIM CHECK**
- **GRADE rates certainty down for indirectness when the outcome is a surrogate.** VERIFIED in the GRADE methodology. 
Authors should rate the importance of the patient-important outcome for which the surrogate is a substitute and subsequently rate down the quality of evidence for indirectness of outcome.
 WHO guidance for vaccine recommendations says the same. 
If important outcomes are represented by a surrogate, they will frequently require down-rating of the quality of evidence for indirectness.
 The downgrade is 
by one or two levels
.
- **WHO uses GRADE.** VERIFIED. WHO TB guidelines follow the Handbook with GRADE, for example 
the WHO Handbook for guideline development, 2014
. I did not retrieve the Handbook text itself.
- **Corticosteroid recommendations for TB meningitis rested on mortality or clinical-outcome trials.** VERIFIED for TBM. 
Randomized controlled trials ... included death or disability as outcome measures.
 Cochrane graded the mortality benefit as 
high quality evidence of the benefit of corticosteroids in preventing death.

- **The same for pericarditis.** PARTIALLY VERIFIED. IMPI (1,400 participants) used clinical outcomes (death, tamponade, constriction). 
Prednisolone did not significantly affect mortality, cardiac tamponade necessitating pericardiocentesis, or constrictive pericarditis.
 The pericarditis example therefore doesn't show that mortality evidence led to a recommendation. It shows a large clinical-outcome trial that was null on mortality. Cochrane found 
corticosteroids probably reduce deaths from pericarditis
 (moderate certainty) with broader all-cause mortality evidence of low certainty.
- **"The only way to keep a Phase III near $7M is to power it on a surrogate or composite."** PLAUSIBLE but not shown. It follows from Critique 2's arithmetic, but a high-mortality enrichment is a counter-example.
- **Whether this grant's Phase III is surrogate-powered.** UNVERIFIABLE. The Investigator flags this as UNGROUNDED.

**Conceptual issues**
- Unfavourable outcome and relapse are not necessarily "surrogates" in the GRADE sense. They are often treated as patient-important outcomes. Only culture conversion and CXR or lung function are clearly surrogates. WHO's TB regimen recommendations have been based on noninferiority trials for unfavourable outcome. For example, 
Study 31 was a randomized, multi-national, open-label, controlled phase 3 trial
 that informed a WHO rapid communication. So a regimen could be recommended without mortality-powered evidence. Adjuncts (host-directed therapies) are a harder case, because the mortality benefit is the whole claim.
- "If WHO requires mortality evidence, the scenario collapses into Critique 1" refers to the cost critique, which is Critique 2 in this batch. The cross-reference is wrong.
- The downgrade for indirectness reduces certainty. It does not prevent a recommendation. The critique acknowledges this, noting conditional adoption.
- This critique overlaps heavily with Critique 2. They are two branches of the same dilemma and should be merged.

**OVERALL VERDICT: PARTIALLY VERIFIED**
The GRADE mechanism is correct. The dilemma structure is logically sound. The magnitude is unquantified and the key premise (the grant's trial design) is unknown.

**REVISED CRITIQUE**
There is a possible inconsistency between cost and benefit. If the budgeted Phase III is powered on a surrogate (for example culture conversion) rather than mortality, the CEA credits a 10% mortality benefit that the trial would not test. Under GRADE, WHO typically rates down certainty for indirectness when evidence relies on surrogates. That is likely to make recommendations conditional and slow adoption (`speedup_years`, coverage), or require a follow-on mortality trial. If the trial is mortality-powered, the cost problem in Critique 2 applies instead. This dilemma should be merged with Critique 2 into a single "cost–benefit design consistency" critique. Corticosteroids for TB meningitis are a supporting precedent, because the recommendation rests on mortality trials. Strength: **medium–large, conditional.** The grant's actual Phase III endpoint must be confirmed. The claim that surrogate-only evidence would block or delay a WHO recommendation is not established for regimen-type trials. Unfavourable outcome is a patient-important composite, not a pure surrogate.

--- Critique: WHO is unlikely to rely on a single trial ---

**CRITIQUE:** WHO is unlikely to rely on a single trial
**Thread:** Realism of the $7M all-in cost, given what a Phase III would need to show

**CITATION CHECK**
- The critique cites nothing. The Hypothesis, Mechanism, and Suggested Evidence fields are blank. No source materials were attached, so I could not identify the product, indication, or trial design the "$7M all-in cost" refers to.

**CLAIM CHECK**
- **"WHO is unlikely to rely on a single trial" (title, the only claim).** I rate it **PLAUSIBLE but OVERBROAD / context-dependent**. It is neither verified nor false as a general statement.
  - **Supporting evidence.** A WHO draft guidance on TB preventive treatment says 
a single trial often does not provide sufficient evidence required for a strong recommendation
. It also says that 
downgrading of evidence due to imprecision has been by far the greatest hurdle to achieving moderate or high certainty evidence based on single trials
. WHO guideline development uses GRADE, which 
explicitly considers certainty of evidence, values and preferences, balance of benefits and harms, and resource implications
. Because these are separate domains from efficacy, a single trial may not cover all of them.
  - **Contradicting evidence.** WHO has acted on a single Phase III trial.
    - The R21/Matrix-M malaria vaccine recommendation was 
informed by evidence from an ongoing R21 vaccine clinical trial and other studies
. A meta-analysis notes that 
R21 demonstrated 68% efficacy against first episodes in a single phase 3 trial
. The Lancet publication says the vaccine 
recently received a WHO policy recommendation and prequalification
.
    - The AMBITION trial authors argue that 
a single large and well done trial can rapidly and credibly translate research evidence to international clinical practice
.
    - The same WHO TB draft says the regulatory "two-trial rule" 
has not been applied in TB in the way it has in some other therapeutic areas
, because multiple trials can be infeasible.
  - **Regulatory context.** Single pivotal trial approvals are increasingly common at the FDA. 
185 (42%) were based on a single pivotal trial
 in one analysis of 2015–2023 approvals. That is the FDA, not WHO, so it is only indirectly relevant.

**EVIDENCE FOUND**
- WHO's stance depends on the type of product and the type of recommendation.
  - For vaccines, WHO prequalification and SAGE recommendations have rested on one large Phase III trial plus supportive data. R21 is the clearest example.
  - For treatment guidelines, such as TB regimens, WHO is more likely to want several trials, or a single large multi-site trial with a high certainty rating under GRADE.
- A single trial is more likely to be enough if it is large, multi-country, and has a hard clinical endpoint. It is also more likely to be enough if it is supported by other evidence such as immunogenicity, safety, and modelling data.
- I found nothing on the $7M cost figure. I can't say whether it is realistic without knowing the product and trial. A single Phase III of any real size in a low- or middle-income setting could plausibly cost more or less than that, depending on size and endpoint. That is an assumption, not a finding.

**OVERALL VERDICT: UNVERIFIABLE (as stated); the title claim is only partially supportable**
- The critique has no hypothesis, mechanism, or evidence to check. Its only content is the title, which is directionally reasonable as a heuristic but not a safe general claim.
- **Recommendation:** Do not retain it as written. Retain it only as a flagged hypothesis if the Investigator rewrites it with specifics.

**REVISED CRITIQUE**
- **Hypothesis (UNGROUNDED, needs product-specific support):** The proposed $7M all-in budget may be unrealistic if it funds only one Phase III trial. WHO guideline bodies may want evidence beyond a single trial, such as a second trial, additional settings or populations, or extra safety and acceptability data. That could raise the true cost.
- **Needed to make this critique usable:**
  1. Identify the product type. Vaccines and treatments face different WHO evidence expectations, as the R21 and TB examples show.
  2. Say whether the plan has a hard clinical endpoint and a multi-site design. If it does, one trial is more likely to suffice.
  3. Cite the actual WHO pathway the plan relies on (prequalification, SAGE, or a guideline development group), plus a benchmark cost for comparable Phase III trials.
- **Strength:** Downgrade to **weak/uncertain**. The R21 precedent directly undercuts the strong form of the claim ("unlikely to rely on a single trial").