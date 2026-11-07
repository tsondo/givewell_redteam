--- Critique: "Success" in Phase III is unlikely to be a mortality result, so the 10% mortality effect is not what a "success" would establish ---

## Critique 1: "Success" in Phase III is unlikely to be a mortality result

**OVERALL VERDICT: PARTIALLY VERIFIED.** The sample-size arithmetic and the surrogate-validity background check out. The claim that the model treats "success" as a demonstrated 10% mortality reduction, and the SROI threshold, could not be checked because I don't have the model or the Phase IIc/III registry design. Flag it as UNGROUNDED on model interpretation.

**CLAIM CHECK**
- **Sample sizes of about 36,000, 17,000 and "larger still" per arm: VERIFIED.** I recomputed with the standard two-proportion formula (80% power, two-sided α = 0.05).
  - 4.0% → 3.6% gives about 35,800 per arm.
  - 8% → 7.2% gives about 17,200 per arm.
  - 2% → 1.8% gives about 73,000 per arm.
- **Mixture arithmetic (0.5 × 0.10 + 0.5 × 0.03 = 0.065, and 0.05 when r_s = 0): VERIFIED.** This is a calculation only. Whether 0.065 pushes SROI below 2,000x depends on the model, which I could not see.
- **Baseline on-treatment mortality of 4–8%: PLAUSIBLE.**
  - 
A systematic review found case fatality during TB treatment ranged from 1.8 to 33.3%.

  - 
In a five-country adherence cohort of 23,799 participants, 6% died during treatment.

  - I did not retrieve the WHO cohort figures or the trial-cohort figure of about 2%, so the 2% claim is UNVERIFIABLE here.
- **"No TB drug trial approaches this scale": UNVERIFIED.** I did not search trial sizes. It is very likely true for DS-TB regimen trials, but I have no source.
- **Phillips et al. and Wallis et al. on 2-month culture as a weak predictor: PARTIALLY VERIFIED.**
  - Both papers exist: Phillips, Fielding & Nunn, PLoS ONE 2013, and Wallis et al. 2013 and 2015.
  - 
Wallis 2015 itself states that month 2 culture status remains a relatively weak predictor of outcomes for individual patients.

  - 
Phillips cites a systematic review finding the 2-month culture had modest specificity but low sensitivity for predicting failure and relapse.

  - Wallis is better characterised as promoting a trial-level model that combines culture status with treatment duration. 
Wallis et al. claim 2-month culture status is a good predictor in DS-TB when combined with treatment duration.

  - The critique's lumping of the two authors is therefore slightly inaccurate.
- **"No evidence that culture-conversion speed predicts mortality": UNVERIFIABLE.** I found none, but I did not search for it directly.

**EVIDENCE FOUND**
- 
A review argues that 2- or 3-month culture positivity on LJ is not an acceptable surrogate for long-term clinical outcome.
 This supports the point that surrogate success does not imply a mortality effect.
- The prior human atorvastatin data are on surrogates. 
A Phase IIA atorvastatin study showed reduced sputum mycobacterial load, while a rosuvastatin trial did not affect sputum culture conversion.
 This is consistent with the critique's premise.

**CORE CLAIM**
- **Claim:** A "success" in the Phase III used by the model would not be a demonstrated 10% mortality reduction, so a large share of success worlds carry a mortality effect well below 10%.
- **Support: LOGIC ONLY.**
- **Why:** The sample-size arithmetic is correct and the prior evidence is surrogate-based. How the model defines "success" was not available to me.

**REVISED CRITIQUE**
- **Keep:** The sample-size arithmetic. A mortality-powered trial at a 10% relative reduction needs tens of thousands of participants per arm at plausible baselines. The existing atorvastatin signals are on bacterial-load and culture endpoints, which are imperfect individual-level surrogates.
- **Remove or flag:**
  - The model-interpretation claim and the SROI threshold, which are UNGROUNDED.
  - The r_s = 0.03 value, which is an assumption.
  - The "no TB trial approaches this scale" claim, which is unsourced.
- **Strength:** Medium to large, conditional on how the model defines "success."

---

## Critique 2: Much on-treatment mortality is unreachable by a weeks-scale adjunct

**OVERALL VERDICT: PARTIALLY VERIFIED.** The qualitative premise (early, HIV-associated, comorbidity-driven deaths) is supported. The 25–35% unreachable fraction and the HPMZ headroom point are unsourced inferences.

**CLAIM CHECK**
- **Waitt & Squire 2011 exists: VERIFIED.** It is Int J Tuberc Lung Dis 2011;15(7):871–885, "A systematic review of risk factors for death in adults during and after tuberculosis treatment." 
Waitt and Squire hypothesised that associations between comorbidities, social isolation and TB death may reflect delays in presenting to a provider.
 I could not retrieve its own timing or cause fractions, so those remain UNVERIFIED.
- **Deaths cluster early: VERIFIED by other sources.**
  - 
In US data, 47% of those who died during treatment died within 30 days of diagnosis.

  - 
In a Taiwanese review of culture-proven TB deaths, most TB-related deaths occurred early (median survival 20 days), typically from septic shock.

  - 
In a Taiwanese cohort, underweight was associated with elevated mortality only within the first 8 weeks.

- **Non-TB and comorbid causes: VERIFIED.** 
Malignancy, liver cirrhosis and renal failure were independent predictors of all TB deaths.

- **HIV and advanced disease as drivers: PLAUSIBLE.** 
A systematic review showed a 44–71% mortality reduction with ART among HIV-positive TB patients.
 That indicates a large HIV-attributable mortality share.
- **Thwaites 2004 (corticosteroids in TB meningitis): not re-checked in this session.** I recall it as a real NEJM 2004 trial. The framing, that there is no analogous result in pulmonary DS-TB, is a reasonable inference.
- **25–35% unreachable, and the HPMZ headroom point: UNVERIFIABLE.** The critique labels these as its own inference. I did not verify the HPMZ regimen definition or its effect on lung-damage burden.

**EVIDENCE FOUND**
- Early deaths are typically from fulminant septic shock, which supports "die before the adjunct could act." But that same shock is inflammatory, so a host-directed drug is not obviously irrelevant to it. This weakens the "unreachable" framing for some early deaths.
- I found no data showing statins reduce early TB mortality.

**CORE CLAIM**
- **Claim:** A material share (25–35%) of on-treatment deaths is not modifiable by a weeks-scale adjunct, so the effective r is below 10%.
- **Support: LOGIC ONLY.**
- **Why:** The direction is supported by early-death and comorbidity data, but the fraction is not quantified in any source I found.

**REVISED CRITIQUE**
- **Keep:** A 10% reduction applied to all-cause on-treatment deaths overstates the reachable pool, because many deaths are early, HIV-driven or non-TB.
- **Remove or flag:** The 25–35% unreachable figure and the HPMZ headroom claim, both UNGROUNDED.
- **Strength:** Medium, with direction supported and magnitude unknown.

---

## Critique 3: Rifampicin induction limits atorvastatin exposure

**OVERALL VERDICT: PARTIALLY VERIFIED.** The label wording and the dual-mechanism interaction are verified. Several secondary claims are wrong, and the magnitude multiplier is unsupported.

**CITATION CHECK**
- **Atorvastatin label statement: VERIFIED.**
  - 
The label says rifampin or other CYP3A4 inducers can lead to variable reductions in atorvastatin. It recommends simultaneous co-administration because delayed administration after rifampin is associated with a significant reduction in plasma concentrations.

  - The label table gives the numbers. 
Rifampin co-administered (600 mg for 7 days) raised AUC by 30% and Cmax 2.7-fold, while separated doses lowered AUC by 80% and Cmax by 40%.

- **Atorvastatin-specific rifampin study: VERIFIED (a different study from the one the critique cited).** 
Backman et al. found rifampin reduced atorvastatin acid AUC by 80%.
 This was in healthy volunteers after 5 days of pretreatment.
- **Kyrklund 2004 as a simvastatin study: LIKELY MISATTRIBUTED, not confirmed by search.**
  - From my background knowledge, Kyrklund 2004 is a pravastatin–rifampicin study. The simvastatin paper is Kyrklund 2000.
  - 
The StAT-TB protocol states that pravastatin exposures are reduced by 30–50% with rifampin.
 This is consistent with that attribution.
- **Karakousis and pravastatin: VERIFIED.**
  - 
StAT-TB was led by Petros Karakousis at Johns Hopkins.

  - 
Its title describes it as a Phase 2b dose-finding study of pravastatin.

  - It is therefore not "Phase IIa," and the registered study is a dose-finding safety and PK study. 
Participants received standard anti-TB therapy (Rifafour) plus pravastatin for 14 days.


**CLAIM CHECK**
- **Atorvastatin is a CYP3A4 and OATP1B1 substrate, and rifampicin both induces and inhibits: VERIFIED.** This follows from the label's "dual interaction mechanism" wording.
- **Net steady-state exposure under chronic daily rifampicin is uncertain: VERIFIED as uncertain.** 
A review notes that the consequences of prolonged simultaneous statin–rifampin administration have never been investigated.
 The label also says the effect on hepatocyte concentrations is unknown.
- **Pravastatin is "largely unaffected by rifampicin": FALSE.** The 30–50% exposure reduction cited above contradicts it.
- **"The prior positive human data are from pravastatin or rosuvastatin": CONTRADICTED for atorvastatin.**
  - 
The positive human signal comes from a randomised Phase IIA trial of atorvastatin in Nigeria (Adewole et al., IJTLD 2023), which found significantly reduced mycobacterial load in sputum.

  - Rosuvastatin (ROSETTA) was the null trial.
  - Pravastatin has so far only a PK and safety study that I could find. So the transferability concern is mostly moot if the model's evidence is the atorvastatin trial. That trial was run under rifampicin-based therapy.
- **Rifampicin is the relevant inducer: UNVERIFIED for this regimen.** If the Phase III regimen is rifapentine-based (HPMZ), the label data are by analogy only, since rifapentine is a somewhat weaker but still real CYP3A4 inducer.
- **ART interactions (ritonavir-boosted PIs raise atorvastatin, efavirenz lowers it): VERIFIED.**
  - 
The label table shows tipranavir/ritonavir raising atorvastatin AUC 9.4-fold.

  - 
The label lists efavirenz among the inducers that can reduce plasma concentrations.

- **"Programs cannot guarantee simultaneous dosing": PLAUSIBLE but unsupported.** Daily fixed-dose-combination dosing makes co-administration straightforward.
- **Multiplier of 0.5–0.8 on r, and a steep dose-response: UNVERIFIABLE.** The critique itself calls this a guess.

**EVIDENCE FOUND**
- Preclinical rationale favours other statins. 
At non-toxic doses atorvastatin was unable to inhibit Mtb growth in THP-1 cells, while simvastatin, fluvastatin and pravastatin showed the most favourable therapeutic index and enhanced first-line drug activity.
 This independently raises doubt that atorvastatin's effect is exposure-limited rather than mechanism-limited.
- The atorvastatin interaction has a large asymmetry. Co-administered dosing gives a modest AUC rise, whereas separated dosing gives an 80% AUC fall. Dosing-time adherence therefore matters, which supports the critique's concern in principle.

**CORE CLAIM**
- **Claim:** Under routine chronic rifampicin therapy, achieved atorvastatin exposure is low enough to reduce the realised mortality effect by about 20–50%.
- **Support: LOGIC ONLY.**
- **Why:** The interaction is real and the label confirms variable reductions. Chronic co-administered exposure is uninvestigated, and no data link exposure to a mortality effect.

**REVISED CRITIQUE**
- **Keep:**
  - Rifampicin has a dual interaction with atorvastatin.
  - Separated dosing lowers AUC by about 80%.
  - Chronic co-administered exposure is unknown.
  - ART interactions run in both directions.
  - Real-world dosing adherence matters.
- **Remove:**
  - The claim that prior positive data are pravastatin-based, since the atorvastatin signal is from atorvastatin itself.
  - The claim that pravastatin is unaffected by rifampicin.
  - The Kyrklund simvastatin attribution.
- **Flag as UNGROUNDED:**
  - The 0.5–0.8 multiplier.
  - The steep dose-response assumption.
  - Applicability to rifapentine-based HPMZ.
- **Strength:** Medium rather than large, since the direction is plausible but the magnitude has no empirical basis.

--- Critique: A large share of on-treatment deaths is unreachable by a weeks-scale host-directed adjunct, and shorter regimens shrink the headroom further ---

## Critique 1: "Success" in Phase III is unlikely to be a mortality result

**OVERALL VERDICT: PARTIALLY VERIFIED.** The sample-size arithmetic and the surrogate-validity background check out. The claim that the model treats "success" as a demonstrated 10% mortality reduction, and the SROI threshold, could not be checked because I don't have the model or the Phase IIc/III registry design. Flag it as UNGROUNDED on model interpretation.

**CLAIM CHECK**
- **Sample sizes of about 36,000, 17,000 and "larger still" per arm: VERIFIED.** I recomputed with the standard two-proportion formula (80% power, two-sided α = 0.05).
  - 4.0% → 3.6% gives about 35,800 per arm.
  - 8% → 7.2% gives about 17,200 per arm.
  - 2% → 1.8% gives about 73,000 per arm.
- **Mixture arithmetic (0.5 × 0.10 + 0.5 × 0.03 = 0.065, and 0.05 when r_s = 0): VERIFIED.** This is a calculation only. Whether 0.065 pushes SROI below 2,000x depends on the model, which I could not see.
- **Baseline on-treatment mortality of 4–8%: PLAUSIBLE.**
  - 
A systematic review found case fatality during TB treatment ranged from 1.8 to 33.3%.

  - 
In a five-country adherence cohort of 23,799 participants, 6% died during treatment.

  - I did not retrieve the WHO cohort figures or the trial-cohort figure of about 2%, so the 2% claim is UNVERIFIABLE here.
- **"No TB drug trial approaches this scale": UNVERIFIED.** I did not search trial sizes. It is very likely true for DS-TB regimen trials, but I have no source.
- **Phillips et al. and Wallis et al. on 2-month culture as a weak predictor: PARTIALLY VERIFIED.**
  - Both papers exist: Phillips, Fielding & Nunn, PLoS ONE 2013, and Wallis et al. 2013 and 2015.
  - 
Wallis 2015 itself states that month 2 culture status remains a relatively weak predictor of outcomes for individual patients.

  - 
Phillips cites a systematic review finding the 2-month culture had modest specificity but low sensitivity for predicting failure and relapse.

  - Wallis is better characterised as promoting a trial-level model that combines culture status with treatment duration. 
Wallis et al. claim 2-month culture status is a good predictor in DS-TB when combined with treatment duration.

  - The critique's lumping of the two authors is therefore slightly inaccurate.
- **"No evidence that culture-conversion speed predicts mortality": UNVERIFIABLE.** I found none, but I did not search for it directly.

**EVIDENCE FOUND**
- 
A review argues that 2- or 3-month culture positivity on LJ is not an acceptable surrogate for long-term clinical outcome.
 This supports the point that surrogate success does not imply a mortality effect.
- The prior human atorvastatin data are on surrogates. 
A Phase IIA atorvastatin study showed reduced sputum mycobacterial load, while a rosuvastatin trial did not affect sputum culture conversion.
 This is consistent with the critique's premise.

**CORE CLAIM**
- **Claim:** A "success" in the Phase III used by the model would not be a demonstrated 10% mortality reduction, so a large share of success worlds carry a mortality effect well below 10%.
- **Support: LOGIC ONLY.**
- **Why:** The sample-size arithmetic is correct and the prior evidence is surrogate-based. How the model defines "success" was not available to me.

**REVISED CRITIQUE**
- **Keep:** The sample-size arithmetic. A mortality-powered trial at a 10% relative reduction needs tens of thousands of participants per arm at plausible baselines. The existing atorvastatin signals are on bacterial-load and culture endpoints, which are imperfect individual-level surrogates.
- **Remove or flag:**
  - The model-interpretation claim and the SROI threshold, which are UNGROUNDED.
  - The r_s = 0.03 value, which is an assumption.
  - The "no TB trial approaches this scale" claim, which is unsourced.
- **Strength:** Medium to large, conditional on how the model defines "success."

---

## Critique 2: Much on-treatment mortality is unreachable by a weeks-scale adjunct

**OVERALL VERDICT: PARTIALLY VERIFIED.** The qualitative premise (early, HIV-associated, comorbidity-driven deaths) is supported. The 25–35% unreachable fraction and the HPMZ headroom point are unsourced inferences.

**CLAIM CHECK**
- **Waitt & Squire 2011 exists: VERIFIED.** It is Int J Tuberc Lung Dis 2011;15(7):871–885, "A systematic review of risk factors for death in adults during and after tuberculosis treatment." 
Waitt and Squire hypothesised that associations between comorbidities, social isolation and TB death may reflect delays in presenting to a provider.
 I could not retrieve its own timing or cause fractions, so those remain UNVERIFIED.
- **Deaths cluster early: VERIFIED by other sources.**
  - 
In US data, 47% of those who died during treatment died within 30 days of diagnosis.

  - 
In a Taiwanese review of culture-proven TB deaths, most TB-related deaths occurred early (median survival 20 days), typically from septic shock.

  - 
In a Taiwanese cohort, underweight was associated with elevated mortality only within the first 8 weeks.

- **Non-TB and comorbid causes: VERIFIED.** 
Malignancy, liver cirrhosis and renal failure were independent predictors of all TB deaths.

- **HIV and advanced disease as drivers: PLAUSIBLE.** 
A systematic review showed a 44–71% mortality reduction with ART among HIV-positive TB patients.
 That indicates a large HIV-attributable mortality share.
- **Thwaites 2004 (corticosteroids in TB meningitis): not re-checked in this session.** I recall it as a real NEJM 2004 trial. The framing, that there is no analogous result in pulmonary DS-TB, is a reasonable inference.
- **25–35% unreachable, and the HPMZ headroom point: UNVERIFIABLE.** The critique labels these as its own inference. I did not verify the HPMZ regimen definition or its effect on lung-damage burden.

**EVIDENCE FOUND**
- Early deaths are typically from fulminant septic shock, which supports "die before the adjunct could act." But that same shock is inflammatory, so a host-directed drug is not obviously irrelevant to it. This weakens the "unreachable" framing for some early deaths.
- I found no data showing statins reduce early TB mortality.

**CORE CLAIM**
- **Claim:** A material share (25–35%) of on-treatment deaths is not modifiable by a weeks-scale adjunct, so the effective r is below 10%.
- **Support: LOGIC ONLY.**
- **Why:** The direction is supported by early-death and comorbidity data, but the fraction is not quantified in any source I found.

**REVISED CRITIQUE**
- **Keep:** A 10% reduction applied to all-cause on-treatment deaths overstates the reachable pool, because many deaths are early, HIV-driven or non-TB.
- **Remove or flag:** The 25–35% unreachable figure and the HPMZ headroom claim, both UNGROUNDED.
- **Strength:** Medium, with direction supported and magnitude unknown.

---

## Critique 3: Rifampicin induction limits atorvastatin exposure

**OVERALL VERDICT: PARTIALLY VERIFIED.** The label wording and the dual-mechanism interaction are verified. Several secondary claims are wrong, and the magnitude multiplier is unsupported.

**CITATION CHECK**
- **Atorvastatin label statement: VERIFIED.**
  - 
The label says rifampin or other CYP3A4 inducers can lead to variable reductions in atorvastatin. It recommends simultaneous co-administration because delayed administration after rifampin is associated with a significant reduction in plasma concentrations.

  - The label table gives the numbers. 
Rifampin co-administered (600 mg for 7 days) raised AUC by 30% and Cmax 2.7-fold, while separated doses lowered AUC by 80% and Cmax by 40%.

- **Atorvastatin-specific rifampin study: VERIFIED (a different study from the one the critique cited).** 
Backman et al. found rifampin reduced atorvastatin acid AUC by 80%.
 This was in healthy volunteers after 5 days of pretreatment.
- **Kyrklund 2004 as a simvastatin study: LIKELY MISATTRIBUTED, not confirmed by search.**
  - From my background knowledge, Kyrklund 2004 is a pravastatin–rifampicin study. The simvastatin paper is Kyrklund 2000.
  - 
The StAT-TB protocol states that pravastatin exposures are reduced by 30–50% with rifampin.
 This is consistent with that attribution.
- **Karakousis and pravastatin: VERIFIED.**
  - 
StAT-TB was led by Petros Karakousis at Johns Hopkins.

  - 
Its title describes it as a Phase 2b dose-finding study of pravastatin.

  - It is therefore not "Phase IIa," and the registered study is a dose-finding safety and PK study. 
Participants received standard anti-TB therapy (Rifafour) plus pravastatin for 14 days.


**CLAIM CHECK**
- **Atorvastatin is a CYP3A4 and OATP1B1 substrate, and rifampicin both induces and inhibits: VERIFIED.** This follows from the label's "dual interaction mechanism" wording.
- **Net steady-state exposure under chronic daily rifampicin is uncertain: VERIFIED as uncertain.** 
A review notes that the consequences of prolonged simultaneous statin–rifampin administration have never been investigated.
 The label also says the effect on hepatocyte concentrations is unknown.
- **Pravastatin is "largely unaffected by rifampicin": FALSE.** The 30–50% exposure reduction cited above contradicts it.
- **"The prior positive human data are from pravastatin or rosuvastatin": CONTRADICTED for atorvastatin.**
  - 
The positive human signal comes from a randomised Phase IIA trial of atorvastatin in Nigeria (Adewole et al., IJTLD 2023), which found significantly reduced mycobacterial load in sputum.

  - Rosuvastatin (ROSETTA) was the null trial.
  - Pravastatin has so far only a PK and safety study that I could find. So the transferability concern is mostly moot if the model's evidence is the atorvastatin trial. That trial was run under rifampicin-based therapy.
- **Rifampicin is the relevant inducer: UNVERIFIED for this regimen.** If the Phase III regimen is rifapentine-based (HPMZ), the label data are by analogy only, since rifapentine is a somewhat weaker but still real CYP3A4 inducer.
- **ART interactions (ritonavir-boosted PIs raise atorvastatin, efavirenz lowers it): VERIFIED.**
  - 
The label table shows tipranavir/ritonavir raising atorvastatin AUC 9.4-fold.

  - 
The label lists efavirenz among the inducers that can reduce plasma concentrations.

- **"Programs cannot guarantee simultaneous dosing": PLAUSIBLE but unsupported.** Daily fixed-dose-combination dosing makes co-administration straightforward.
- **Multiplier of 0.5–0.8 on r, and a steep dose-response: UNVERIFIABLE.** The critique itself calls this a guess.

**EVIDENCE FOUND**
- Preclinical rationale favours other statins. 
At non-toxic doses atorvastatin was unable to inhibit Mtb growth in THP-1 cells, while simvastatin, fluvastatin and pravastatin showed the most favourable therapeutic index and enhanced first-line drug activity.
 This independently raises doubt that atorvastatin's effect is exposure-limited rather than mechanism-limited.
- The atorvastatin interaction has a large asymmetry. Co-administered dosing gives a modest AUC rise, whereas separated dosing gives an 80% AUC fall. Dosing-time adherence therefore matters, which supports the critique's concern in principle.

**CORE CLAIM**
- **Claim:** Under routine chronic rifampicin therapy, achieved atorvastatin exposure is low enough to reduce the realised mortality effect by about 20–50%.
- **Support: LOGIC ONLY.**
- **Why:** The interaction is real and the label confirms variable reductions. Chronic co-administered exposure is uninvestigated, and no data link exposure to a mortality effect.

**REVISED CRITIQUE**
- **Keep:**
  - Rifampicin has a dual interaction with atorvastatin.
  - Separated dosing lowers AUC by about 80%.
  - Chronic co-administered exposure is unknown.
  - ART interactions run in both directions.
  - Real-world dosing adherence matters.
- **Remove:**
  - The claim that prior positive data are pravastatin-based, since the atorvastatin signal is from atorvastatin itself.
  - The claim that pravastatin is unaffected by rifampicin.
  - The Kyrklund simvastatin attribution.
- **Flag as UNGROUNDED:**
  - The 0.5–0.8 multiplier.
  - The steep dose-response assumption.
  - Applicability to rifapentine-based HPMZ.
- **Strength:** Medium rather than large, since the direction is plausible but the magnitude has no empirical basis.

--- Critique: Rifampicin induction structurally limits atorvastatin exposure in routine programs, and the trial exposure does not transfer ---

## Critique 1: "Success" in Phase III is unlikely to be a mortality result

**OVERALL VERDICT: PARTIALLY VERIFIED.** The sample-size arithmetic and the surrogate-validity background check out. The claim that the model treats "success" as a demonstrated 10% mortality reduction, and the SROI threshold, could not be checked because I don't have the model or the Phase IIc/III registry design. Flag it as UNGROUNDED on model interpretation.

**CLAIM CHECK**
- **Sample sizes of about 36,000, 17,000 and "larger still" per arm: VERIFIED.** I recomputed with the standard two-proportion formula (80% power, two-sided α = 0.05).
  - 4.0% → 3.6% gives about 35,800 per arm.
  - 8% → 7.2% gives about 17,200 per arm.
  - 2% → 1.8% gives about 73,000 per arm.
- **Mixture arithmetic (0.5 × 0.10 + 0.5 × 0.03 = 0.065, and 0.05 when r_s = 0): VERIFIED.** This is a calculation only. Whether 0.065 pushes SROI below 2,000x depends on the model, which I could not see.
- **Baseline on-treatment mortality of 4–8%: PLAUSIBLE.**
  - 
A systematic review found case fatality during TB treatment ranged from 1.8 to 33.3%.

  - 
In a five-country adherence cohort of 23,799 participants, 6% died during treatment.

  - I did not retrieve the WHO cohort figures or the trial-cohort figure of about 2%, so the 2% claim is UNVERIFIABLE here.
- **"No TB drug trial approaches this scale": UNVERIFIED.** I did not search trial sizes. It is very likely true for DS-TB regimen trials, but I have no source.
- **Phillips et al. and Wallis et al. on 2-month culture as a weak predictor: PARTIALLY VERIFIED.**
  - Both papers exist: Phillips, Fielding & Nunn, PLoS ONE 2013, and Wallis et al. 2013 and 2015.
  - 
Wallis 2015 itself states that month 2 culture status remains a relatively weak predictor of outcomes for individual patients.

  - 
Phillips cites a systematic review finding the 2-month culture had modest specificity but low sensitivity for predicting failure and relapse.

  - Wallis is better characterised as promoting a trial-level model that combines culture status with treatment duration. 
Wallis et al. claim 2-month culture status is a good predictor in DS-TB when combined with treatment duration.

  - The critique's lumping of the two authors is therefore slightly inaccurate.
- **"No evidence that culture-conversion speed predicts mortality": UNVERIFIABLE.** I found none, but I did not search for it directly.

**EVIDENCE FOUND**
- 
A review argues that 2- or 3-month culture positivity on LJ is not an acceptable surrogate for long-term clinical outcome.
 This supports the point that surrogate success does not imply a mortality effect.
- The prior human atorvastatin data are on surrogates. 
A Phase IIA atorvastatin study showed reduced sputum mycobacterial load, while a rosuvastatin trial did not affect sputum culture conversion.
 This is consistent with the critique's premise.

**CORE CLAIM**
- **Claim:** A "success" in the Phase III used by the model would not be a demonstrated 10% mortality reduction, so a large share of success worlds carry a mortality effect well below 10%.
- **Support: LOGIC ONLY.**
- **Why:** The sample-size arithmetic is correct and the prior evidence is surrogate-based. How the model defines "success" was not available to me.

**REVISED CRITIQUE**
- **Keep:** The sample-size arithmetic. A mortality-powered trial at a 10% relative reduction needs tens of thousands of participants per arm at plausible baselines. The existing atorvastatin signals are on bacterial-load and culture endpoints, which are imperfect individual-level surrogates.
- **Remove or flag:**
  - The model-interpretation claim and the SROI threshold, which are UNGROUNDED.
  - The r_s = 0.03 value, which is an assumption.
  - The "no TB trial approaches this scale" claim, which is unsourced.
- **Strength:** Medium to large, conditional on how the model defines "success."

---

## Critique 2: Much on-treatment mortality is unreachable by a weeks-scale adjunct

**OVERALL VERDICT: PARTIALLY VERIFIED.** The qualitative premise (early, HIV-associated, comorbidity-driven deaths) is supported. The 25–35% unreachable fraction and the HPMZ headroom point are unsourced inferences.

**CLAIM CHECK**
- **Waitt & Squire 2011 exists: VERIFIED.** It is Int J Tuberc Lung Dis 2011;15(7):871–885, "A systematic review of risk factors for death in adults during and after tuberculosis treatment." 
Waitt and Squire hypothesised that associations between comorbidities, social isolation and TB death may reflect delays in presenting to a provider.
 I could not retrieve its own timing or cause fractions, so those remain UNVERIFIED.
- **Deaths cluster early: VERIFIED by other sources.**
  - 
In US data, 47% of those who died during treatment died within 30 days of diagnosis.

  - 
In a Taiwanese review of culture-proven TB deaths, most TB-related deaths occurred early (median survival 20 days), typically from septic shock.

  - 
In a Taiwanese cohort, underweight was associated with elevated mortality only within the first 8 weeks.

- **Non-TB and comorbid causes: VERIFIED.** 
Malignancy, liver cirrhosis and renal failure were independent predictors of all TB deaths.

- **HIV and advanced disease as drivers: PLAUSIBLE.** 
A systematic review showed a 44–71% mortality reduction with ART among HIV-positive TB patients.
 That indicates a large HIV-attributable mortality share.
- **Thwaites 2004 (corticosteroids in TB meningitis): not re-checked in this session.** I recall it as a real NEJM 2004 trial. The framing, that there is no analogous result in pulmonary DS-TB, is a reasonable inference.
- **25–35% unreachable, and the HPMZ headroom point: UNVERIFIABLE.** The critique labels these as its own inference. I did not verify the HPMZ regimen definition or its effect on lung-damage burden.

**EVIDENCE FOUND**
- Early deaths are typically from fulminant septic shock, which supports "die before the adjunct could act." But that same shock is inflammatory, so a host-directed drug is not obviously irrelevant to it. This weakens the "unreachable" framing for some early deaths.
- I found no data showing statins reduce early TB mortality.

**CORE CLAIM**
- **Claim:** A material share (25–35%) of on-treatment deaths is not modifiable by a weeks-scale adjunct, so the effective r is below 10%.
- **Support: LOGIC ONLY.**
- **Why:** The direction is supported by early-death and comorbidity data, but the fraction is not quantified in any source I found.

**REVISED CRITIQUE**
- **Keep:** A 10% reduction applied to all-cause on-treatment deaths overstates the reachable pool, because many deaths are early, HIV-driven or non-TB.
- **Remove or flag:** The 25–35% unreachable figure and the HPMZ headroom claim, both UNGROUNDED.
- **Strength:** Medium, with direction supported and magnitude unknown.

---

## Critique 3: Rifampicin induction limits atorvastatin exposure

**OVERALL VERDICT: PARTIALLY VERIFIED.** The label wording and the dual-mechanism interaction are verified. Several secondary claims are wrong, and the magnitude multiplier is unsupported.

**CITATION CHECK**
- **Atorvastatin label statement: VERIFIED.**
  - 
The label says rifampin or other CYP3A4 inducers can lead to variable reductions in atorvastatin. It recommends simultaneous co-administration because delayed administration after rifampin is associated with a significant reduction in plasma concentrations.

  - The label table gives the numbers. 
Rifampin co-administered (600 mg for 7 days) raised AUC by 30% and Cmax 2.7-fold, while separated doses lowered AUC by 80% and Cmax by 40%.

- **Atorvastatin-specific rifampin study: VERIFIED (a different study from the one the critique cited).** 
Backman et al. found rifampin reduced atorvastatin acid AUC by 80%.
 This was in healthy volunteers after 5 days of pretreatment.
- **Kyrklund 2004 as a simvastatin study: LIKELY MISATTRIBUTED, not confirmed by search.**
  - From my background knowledge, Kyrklund 2004 is a pravastatin–rifampicin study. The simvastatin paper is Kyrklund 2000.
  - 
The StAT-TB protocol states that pravastatin exposures are reduced by 30–50% with rifampin.
 This is consistent with that attribution.
- **Karakousis and pravastatin: VERIFIED.**
  - 
StAT-TB was led by Petros Karakousis at Johns Hopkins.

  - 
Its title describes it as a Phase 2b dose-finding study of pravastatin.

  - It is therefore not "Phase IIa," and the registered study is a dose-finding safety and PK study. 
Participants received standard anti-TB therapy (Rifafour) plus pravastatin for 14 days.


**CLAIM CHECK**
- **Atorvastatin is a CYP3A4 and OATP1B1 substrate, and rifampicin both induces and inhibits: VERIFIED.** This follows from the label's "dual interaction mechanism" wording.
- **Net steady-state exposure under chronic daily rifampicin is uncertain: VERIFIED as uncertain.** 
A review notes that the consequences of prolonged simultaneous statin–rifampin administration have never been investigated.
 The label also says the effect on hepatocyte concentrations is unknown.
- **Pravastatin is "largely unaffected by rifampicin": FALSE.** The 30–50% exposure reduction cited above contradicts it.
- **"The prior positive human data are from pravastatin or rosuvastatin": CONTRADICTED for atorvastatin.**
  - 
The positive human signal comes from a randomised Phase IIA trial of atorvastatin in Nigeria (Adewole et al., IJTLD 2023), which found significantly reduced mycobacterial load in sputum.

  - Rosuvastatin (ROSETTA) was the null trial.
  - Pravastatin has so far only a PK and safety study that I could find. So the transferability concern is mostly moot if the model's evidence is the atorvastatin trial. That trial was run under rifampicin-based therapy.
- **Rifampicin is the relevant inducer: UNVERIFIED for this regimen.** If the Phase III regimen is rifapentine-based (HPMZ), the label data are by analogy only, since rifapentine is a somewhat weaker but still real CYP3A4 inducer.
- **ART interactions (ritonavir-boosted PIs raise atorvastatin, efavirenz lowers it): VERIFIED.**
  - 
The label table shows tipranavir/ritonavir raising atorvastatin AUC 9.4-fold.

  - 
The label lists efavirenz among the inducers that can reduce plasma concentrations.

- **"Programs cannot guarantee simultaneous dosing": PLAUSIBLE but unsupported.** Daily fixed-dose-combination dosing makes co-administration straightforward.
- **Multiplier of 0.5–0.8 on r, and a steep dose-response: UNVERIFIABLE.** The critique itself calls this a guess.

**EVIDENCE FOUND**
- Preclinical rationale favours other statins. 
At non-toxic doses atorvastatin was unable to inhibit Mtb growth in THP-1 cells, while simvastatin, fluvastatin and pravastatin showed the most favourable therapeutic index and enhanced first-line drug activity.
 This independently raises doubt that atorvastatin's effect is exposure-limited rather than mechanism-limited.
- The atorvastatin interaction has a large asymmetry. Co-administered dosing gives a modest AUC rise, whereas separated dosing gives an 80% AUC fall. Dosing-time adherence therefore matters, which supports the critique's concern in principle.

**CORE CLAIM**
- **Claim:** Under routine chronic rifampicin therapy, achieved atorvastatin exposure is low enough to reduce the realised mortality effect by about 20–50%.
- **Support: LOGIC ONLY.**
- **Why:** The interaction is real and the label confirms variable reductions. Chronic co-administered exposure is uninvestigated, and no data link exposure to a mortality effect.

**REVISED CRITIQUE**
- **Keep:**
  - Rifampicin has a dual interaction with atorvastatin.
  - Separated dosing lowers AUC by about 80%.
  - Chronic co-administered exposure is unknown.
  - ART interactions run in both directions.
  - Real-world dosing adherence matters.
- **Remove:**
  - The claim that prior positive data are pravastatin-based, since the atorvastatin signal is from atorvastatin itself.
  - The claim that pravastatin is unaffected by rifampicin.
  - The Kyrklund simvastatin attribution.
- **Flag as UNGROUNDED:**
  - The 0.5–0.8 multiplier.
  - The steep dose-response assumption.
  - Applicability to rifapentine-based HPMZ.
- **Strength:** Medium rather than large, since the direction is plausible but the magnitude has no empirical basis.

--- Critique: Winner's-curse and reference-class patterns imply the conditional effect should sit well below the surrogate-implied one, and r and p_success should not be independent ---

## Critique 1: Winner's-curse and reference-class patterns, and r and p_success not independent

**OVERALL VERDICT: PARTIALLY VERIFIED.** The winner's-curse logic is sound, and the HDT reference class is partly real. But the Investigator overstates it as a track record of failure to translate. The covariance argument is also shakier than presented.

**CLAIM CHECK**
- **Martineau 2011 vitamin D signal:** VERIFIED.
  - 
Overall, the adjusted HR for time to culture conversion was 1.39 (95% CI 0.90–2.16, p=0.14).

  - 
TaqI genotype modified the effect (p-interaction=0.03), with benefit seen only in tt patients (HR 8.09, 95% CI 1.36–48.01).

  - The tt subgroup was tiny: 
12 subjects.
 This is a textbook winner's-curse case.
  - Later evidence: a meta-analysis found 
no shortening of time to culture conversion overall, with the tt subgroup effect still reported.

  - The endpoint was culture conversion, not mortality. That fits "surrogate positive, no outcome benefit." But no mortality trial was run, so "no robust outcome benefit" is better stated as "no benefit on the surrogate in the full population."
- **CC-11050 and everolimus:** PARTIALLY VERIFIED, and MISCHARACTERISED as failures.
  - The Phase 2 TB-HDT trial found 
improved FEV1 recovery at day 180 for CC-11050 and everolimus (6.30% and 6.56% differences).
 The lower confidence limits were near zero, and the p-values were 0.048 and 0.044.
  - 
None of the arms showed accelerated eradication of MTB infection.

  - I found no Phase 3 or mortality trial. So these are marginal, unreplicated early signals, which fits the winner's-curse argument. They are not documented "failures to translate."
  - A Lancet Respiratory Medicine paper reported 
two control-group patients with life-threatening, treatment-attributable liver injury.

- **Metformin:** PARTIALLY VERIFIED.
  - One RCT concluded that 
adding metformin to anti-TB therapy does not affect sputum conversion.
 The same paper notes that 
other studies (Abinaya, Marupuru) had found additional benefit.
 Early positives that later fail to replicate are supported.
  - A different source claims 
a randomized trial showed faster conversion and better clinical outcomes.
 The evidence is mixed, and I found no mortality data.
- **Everolimus:** see the CC-11050 entry above. The only evidence is the Phase 2 trial.
- **Observational statin cohorts exist:** VERIFIED in outline. 
Several population-based studies found statin use associated with lower TB incidence.
 I did not verify the healthy-user bias claim, but it is a standard and plausible concern.
- **"Bayesian shrinkage 0.7–0.9 gives r = 0.07–0.09":** the arithmetic is correct. The shrinkage factor is an assumption with no empirical anchor.
- **"E[r × p_success] below the product of means":** LOGIC ONLY, and it depends on how p_success is defined.
  - Winner's curse shows that the true effect, given a pass, is below the estimate. It does not by itself create negative covariance between r and p_success.
  - If p_success is the chance of true mortality benefit, r and p_success are positively correlated, and E[rp] would exceed the product of means.
  - Negative covariance arises only if p_success is the chance of passing on a surrogate, because surrogate-only worlds then pass with r≈0.
  - I could not see how the CG model defines p_success or where its 10% comes from. The "anchored on promising early signals" premise is therefore unverified.

**EVIDENCE FOUND (additional)**
- **Atorvastatin itself has only a surrogate signal.**
  - A Phase II atorvastatin trial in Nigeria reported 
a significant reduction in sputum mycobacterial load.

  - It was a Phase II trial using a bacteriological surrogate, with no mortality data. This is the strongest on-point support for the critique.
- **Rosuvastatin Phase 2b was null.**
  - 
Median time to culture conversion was 42 days in both arms (HR 1.30, 95% CI 0.88–1.91, p=0.19).

  - 
The authors concluded it was safe but gave no substantive benefit on culture conversion overall.

  - This is a class-adjacent datapoint against optimism, though rosuvastatin is not atorvastatin.

**CORE CLAIM**
- Claim: the CG's 10% conditional mortality effect is inflated relative to the true effect because it is anchored on selected early or surrogate signals, so r should be shrunk.
- Support: **LOGIC ONLY.** The reference class (vitamin D, metformin, CC-11050, everolimus, rosuvastatin, atorvastatin Phase IIa) shows that surrogate signals are mixed or unreplicated. I found no evidence on how CG derived 10%, and no mortality data for these agents.

**REVISED CRITIQUE**
The effect size is probably better treated as a prior with downward-skewed uncertainty than as a point estimate of 0.10. The supporting reference class is:
- vitamin D: a subgroup-only conversion signal, with null results overall;
- metformin: mixed on sputum conversion;
- CC-11050 and everolimus: marginal FEV1 signals with no conversion benefit;
- rosuvastatin: a null Phase 2b;
- atorvastatin: only a Phase IIa bacillary-load signal.

The shrinkage factor of 0.7–0.9 is UNGROUNDED, and the sign of the r–p_success covariance depends on how p_success is defined. Drop the claim that these agents "failed to translate to outcome benefit." They were never tested on mortality. Strength: medium, direction: decreases (probably).

---

## Critique 2: Hepatotoxicity and myopathy tail, and compounding attenuations

**OVERALL VERDICT: PARTIALLY VERIFIED.** The qualitative harm-tail hypothesis is plausible and UNGROUNDED on magnitude. The arithmetic is correct. The compounding ranges are assumptions drawn from critiques I was not given.

**CLAIM CHECK**
- **Statins and first-line TB drugs add hepatic risk, and statins carry myopathy risk:** PLAUSIBLE. This is standard labeling knowledge, and I did not search for it.
- **Higher myopathy risk with some ART:** PLAUSIBLE, from background pharmacology (boosted protease inhibitors raise atorvastatin levels). I did not verify it in this session. One COVID trial lists 
protease inhibitors among drugs with significant atorvastatin interactions.

- **Small Phase II trials cannot detect excess hepatotoxicity:** LOGIC, and correct. The available trials are small and show no signal:
  - Rosuvastatin Phase 2b: 
grade 3–5 adverse events in 9% of the rosuvastatin arm and 6% of controls, none judged related.

  - Atorvastatin Phase II (Nigeria): reported as 
a safe additive to standard anti-TB treatment.

  - Absence of a signal in these trials is weak evidence either way, as the Investigator says.
- **"10% probability of null or negative contributes about −0.01":** the arithmetic is correct (0.10 × 0.10). The loss may be double-counted if p_success already prices in a null world.
- **Compounding:**
  - 0.65 × 0.5 × 0.7 = 0.2275, and 0.75 × 0.8 × 0.9 = 0.54. So r ≈ 0.023–0.054, which matches the critique.
  - All three factors are assumptions. The "reachable fraction" and "PK attenuation" come from other critiques I cannot see.
  - The Investigator itself flags that the factors overlap and are correlated.

**EVIDENCE FOUND (additional)**
- Drug-interaction concerns with rifampicin are recognised in the statin-TB literature. The StAT-TB protocol cites 
known drug interactions between pravastatin and rifampin in humans.
 That supports the existence of PK attenuation, though not the 0.5–0.8 range, and it concerns pravastatin rather than atorvastatin.
- Metformin shows the same pattern. A PK substudy found 
metformin reduced rifampicin bioavailability by 24%.
 This shows that adjunctive HDTs can erode first-line drug exposure, which is a reference-class point.
- I could not complete my planned check of rifampicin's effect on atorvastatin exposure. From background knowledge, rifampicin induces CYP3A4 and lowers atorvastatin exposure, but this is not verified here.

**CORE CLAIM**
- Claim: the independent attenuation factors (reachable fraction, PK attenuation, shrinkage) multiply to cut r to about 0.023–0.054.
- Support: **LOGIC ONLY.** The multiplication is correct, but each input is an unsourced assumption, and the factors are likely correlated and overlap with Critique 1.

**REVISED CRITIQUE**
A small harm tail is plausible. Existing small trials show no hepatic signal but cannot rule one out. The first-order effect on E[r] from a net-zero or harm world is modest, about −0.01 under the stated assumption. The compounded 0.023–0.054 range is an illustrative upper bound on attenuation, not an estimate. It is UNGROUNDED, "plausible but needs empirical support," and should not be added to Critique 1 without removing overlap. Strength: low to medium for the harm tail alone. The compounding claim stays flagged as hypothetical.

---

## Critique 3: A $7M Phase III cannot be powered on mortality

**OVERALL VERDICT: PARTIALLY VERIFIED.** The sample-size arithmetic checks out. The cost-per-participant figures and the WHO endpoint requirement are unverified. The SROI scaling appears internally inconsistent.

**CLAIM CHECK**
- **5% → 4.5% mortality (80% power, two-sided α=0.05):** VERIFIED.
  - My recomputation: n per arm = (1.96 + 0.8416)² × (0.0475 + 0.042975) / 0.005² ≈ 28,400, so about 56,800 in total.
- **8% → 7.2%:** VERIFIED.
  - n per arm ≈ 7.849 × 0.1404 / 0.008² ≈ 17,200, so about 34,400 in total.
- **Cost of $17M–$57M at $500–$1,000 per participant:** arithmetic correct (34k × $500 ≈ $17M; 57k × $1,000 ≈ $57M). The per-participant figures themselves are UNVERIFIABLE.
  - My RECOVERY cost search returned nothing relevant, so I could not confirm the claim about RECOVERY.
  - An unrelated cost source shows per-participant costs for conventional rehabilitation trials of order $16k–$36k. That is a different trial type and not informative here.
  - For $7M to fund 35–57k participants, total cost per participant would have to be about $120–$200. Whether that is achievable in a streamlined TB trial is unknown.
- **WHO GDG would require a mortality endpoint for adjunctive HDT:** UNVERIFIABLE. I found no source. WHO may accept a composite unfavourable outcome, which would change N.
- **Enrichment (TB meningitis, advanced HIV) reduces N but limits generalisability:** LOGIC, sound.
- **SROI ≈ 3,000 × 7/37 ≈ 570x:** the arithmetic is right (567). But the scaling uses $7M as the baseline all-in cost, while the title says $7M is the Phase III alone. If the baseline all-in cost is larger than $7M, the proportional drop is smaller than 3–10×. I could not see the CG model to resolve this.
- **Baseline mortality of 5–8%:** PLAUSIBLE but unverified. Mortality in DS-TB trial populations is often lower than this (my recollection, not checked). That would raise N further, so this assumption is probably conservative for the critique.
- **Not checked:** the 3.3M-patient benefit base and the "25% materiality bar." They come from the model, which I could not see.

**EVIDENCE FOUND (additional)**
- The Phase II HDT trials I found used surrogate or physiological endpoints, not mortality:
  - the TB-HDT trial used FEV1 and culture conversion;
  - the rosuvastatin trial used 
time to culture conversion by week 8.

- The critique's fork is therefore real: either the Phase III is surrogate-based, or it is far costlier than $7M. This is consistent with how this field has run trials, but it does not prove what CG assumed.

**CORE CLAIM**
- Claim: a Phase III powered to detect a 10% relative mortality reduction needs about 35,000–57,000 participants and therefore costs well above $7M.
- Support: **LOGIC ONLY.** The sample-size half is verified by my recomputation. The cost half depends on a per-participant cost that I could not verify, so the conclusion rests on reasoning and not on direct evidence.

**REVISED CRITIQUE**
Powering a Phase III on mortality at a 10% relative reduction needs about 34,000–57,000 participants (5–8% baseline mortality, 80% power). If CG's $7M budget is for that design, it implies about $120–$200 per participant, which looks implausibly low but is not shown to be impossible. If the trial instead uses a surrogate or composite endpoint, the cost may be reasonable but the model's mortality-only benefit stream is then unsupported. The $25–40M central estimate and the 3–10× SROI reduction are UNGROUNDED because they depend on unverified per-participant costs and an unclear baseline for the 7/37 scaling. Strength: medium to high on the internal-consistency point (cost versus endpoint), low to medium on the specific SROI magnitude. The direction (cost up, SROI down, or p_success overstated) is well supported by logic.

**Search limitations:** I ran out of searches before checking the RECOVERY per-participant cost, the rifampicin–atorvastatin PK effect, and the WHO GDG endpoint requirement. Those items remain unverified.

--- Critique: Hepatotoxicity and myopathy add a negative tail, and the combined attenuations compound ---

## Critique 1: Winner's-curse and reference-class patterns, and r and p_success not independent

**OVERALL VERDICT: PARTIALLY VERIFIED.** The winner's-curse logic is sound, and the HDT reference class is partly real. But the Investigator overstates it as a track record of failure to translate. The covariance argument is also shakier than presented.

**CLAIM CHECK**
- **Martineau 2011 vitamin D signal:** VERIFIED.
  - 
Overall, the adjusted HR for time to culture conversion was 1.39 (95% CI 0.90–2.16, p=0.14).

  - 
TaqI genotype modified the effect (p-interaction=0.03), with benefit seen only in tt patients (HR 8.09, 95% CI 1.36–48.01).

  - The tt subgroup was tiny: 
12 subjects.
 This is a textbook winner's-curse case.
  - Later evidence: a meta-analysis found 
no shortening of time to culture conversion overall, with the tt subgroup effect still reported.

  - The endpoint was culture conversion, not mortality. That fits "surrogate positive, no outcome benefit." But no mortality trial was run, so "no robust outcome benefit" is better stated as "no benefit on the surrogate in the full population."
- **CC-11050 and everolimus:** PARTIALLY VERIFIED, and MISCHARACTERISED as failures.
  - The Phase 2 TB-HDT trial found 
improved FEV1 recovery at day 180 for CC-11050 and everolimus (6.30% and 6.56% differences).
 The lower confidence limits were near zero, and the p-values were 0.048 and 0.044.
  - 
None of the arms showed accelerated eradication of MTB infection.

  - I found no Phase 3 or mortality trial. So these are marginal, unreplicated early signals, which fits the winner's-curse argument. They are not documented "failures to translate."
  - A Lancet Respiratory Medicine paper reported 
two control-group patients with life-threatening, treatment-attributable liver injury.

- **Metformin:** PARTIALLY VERIFIED.
  - One RCT concluded that 
adding metformin to anti-TB therapy does not affect sputum conversion.
 The same paper notes that 
other studies (Abinaya, Marupuru) had found additional benefit.
 Early positives that later fail to replicate are supported.
  - A different source claims 
a randomized trial showed faster conversion and better clinical outcomes.
 The evidence is mixed, and I found no mortality data.
- **Everolimus:** see the CC-11050 entry above. The only evidence is the Phase 2 trial.
- **Observational statin cohorts exist:** VERIFIED in outline. 
Several population-based studies found statin use associated with lower TB incidence.
 I did not verify the healthy-user bias claim, but it is a standard and plausible concern.
- **"Bayesian shrinkage 0.7–0.9 gives r = 0.07–0.09":** the arithmetic is correct. The shrinkage factor is an assumption with no empirical anchor.
- **"E[r × p_success] below the product of means":** LOGIC ONLY, and it depends on how p_success is defined.
  - Winner's curse shows that the true effect, given a pass, is below the estimate. It does not by itself create negative covariance between r and p_success.
  - If p_success is the chance of true mortality benefit, r and p_success are positively correlated, and E[rp] would exceed the product of means.
  - Negative covariance arises only if p_success is the chance of passing on a surrogate, because surrogate-only worlds then pass with r≈0.
  - I could not see how the CG model defines p_success or where its 10% comes from. The "anchored on promising early signals" premise is therefore unverified.

**EVIDENCE FOUND (additional)**
- **Atorvastatin itself has only a surrogate signal.**
  - A Phase II atorvastatin trial in Nigeria reported 
a significant reduction in sputum mycobacterial load.

  - It was a Phase II trial using a bacteriological surrogate, with no mortality data. This is the strongest on-point support for the critique.
- **Rosuvastatin Phase 2b was null.**
  - 
Median time to culture conversion was 42 days in both arms (HR 1.30, 95% CI 0.88–1.91, p=0.19).

  - 
The authors concluded it was safe but gave no substantive benefit on culture conversion overall.

  - This is a class-adjacent datapoint against optimism, though rosuvastatin is not atorvastatin.

**CORE CLAIM**
- Claim: the CG's 10% conditional mortality effect is inflated relative to the true effect because it is anchored on selected early or surrogate signals, so r should be shrunk.
- Support: **LOGIC ONLY.** The reference class (vitamin D, metformin, CC-11050, everolimus, rosuvastatin, atorvastatin Phase IIa) shows that surrogate signals are mixed or unreplicated. I found no evidence on how CG derived 10%, and no mortality data for these agents.

**REVISED CRITIQUE**
The effect size is probably better treated as a prior with downward-skewed uncertainty than as a point estimate of 0.10. The supporting reference class is:
- vitamin D: a subgroup-only conversion signal, with null results overall;
- metformin: mixed on sputum conversion;
- CC-11050 and everolimus: marginal FEV1 signals with no conversion benefit;
- rosuvastatin: a null Phase 2b;
- atorvastatin: only a Phase IIa bacillary-load signal.

The shrinkage factor of 0.7–0.9 is UNGROUNDED, and the sign of the r–p_success covariance depends on how p_success is defined. Drop the claim that these agents "failed to translate to outcome benefit." They were never tested on mortality. Strength: medium, direction: decreases (probably).

---

## Critique 2: Hepatotoxicity and myopathy tail, and compounding attenuations

**OVERALL VERDICT: PARTIALLY VERIFIED.** The qualitative harm-tail hypothesis is plausible and UNGROUNDED on magnitude. The arithmetic is correct. The compounding ranges are assumptions drawn from critiques I was not given.

**CLAIM CHECK**
- **Statins and first-line TB drugs add hepatic risk, and statins carry myopathy risk:** PLAUSIBLE. This is standard labeling knowledge, and I did not search for it.
- **Higher myopathy risk with some ART:** PLAUSIBLE, from background pharmacology (boosted protease inhibitors raise atorvastatin levels). I did not verify it in this session. One COVID trial lists 
protease inhibitors among drugs with significant atorvastatin interactions.

- **Small Phase II trials cannot detect excess hepatotoxicity:** LOGIC, and correct. The available trials are small and show no signal:
  - Rosuvastatin Phase 2b: 
grade 3–5 adverse events in 9% of the rosuvastatin arm and 6% of controls, none judged related.

  - Atorvastatin Phase II (Nigeria): reported as 
a safe additive to standard anti-TB treatment.

  - Absence of a signal in these trials is weak evidence either way, as the Investigator says.
- **"10% probability of null or negative contributes about −0.01":** the arithmetic is correct (0.10 × 0.10). The loss may be double-counted if p_success already prices in a null world.
- **Compounding:**
  - 0.65 × 0.5 × 0.7 = 0.2275, and 0.75 × 0.8 × 0.9 = 0.54. So r ≈ 0.023–0.054, which matches the critique.
  - All three factors are assumptions. The "reachable fraction" and "PK attenuation" come from other critiques I cannot see.
  - The Investigator itself flags that the factors overlap and are correlated.

**EVIDENCE FOUND (additional)**
- Drug-interaction concerns with rifampicin are recognised in the statin-TB literature. The StAT-TB protocol cites 
known drug interactions between pravastatin and rifampin in humans.
 That supports the existence of PK attenuation, though not the 0.5–0.8 range, and it concerns pravastatin rather than atorvastatin.
- Metformin shows the same pattern. A PK substudy found 
metformin reduced rifampicin bioavailability by 24%.
 This shows that adjunctive HDTs can erode first-line drug exposure, which is a reference-class point.
- I could not complete my planned check of rifampicin's effect on atorvastatin exposure. From background knowledge, rifampicin induces CYP3A4 and lowers atorvastatin exposure, but this is not verified here.

**CORE CLAIM**
- Claim: the independent attenuation factors (reachable fraction, PK attenuation, shrinkage) multiply to cut r to about 0.023–0.054.
- Support: **LOGIC ONLY.** The multiplication is correct, but each input is an unsourced assumption, and the factors are likely correlated and overlap with Critique 1.

**REVISED CRITIQUE**
A small harm tail is plausible. Existing small trials show no hepatic signal but cannot rule one out. The first-order effect on E[r] from a net-zero or harm world is modest, about −0.01 under the stated assumption. The compounded 0.023–0.054 range is an illustrative upper bound on attenuation, not an estimate. It is UNGROUNDED, "plausible but needs empirical support," and should not be added to Critique 1 without removing overlap. Strength: low to medium for the harm tail alone. The compounding claim stays flagged as hypothetical.

---

## Critique 3: A $7M Phase III cannot be powered on mortality

**OVERALL VERDICT: PARTIALLY VERIFIED.** The sample-size arithmetic checks out. The cost-per-participant figures and the WHO endpoint requirement are unverified. The SROI scaling appears internally inconsistent.

**CLAIM CHECK**
- **5% → 4.5% mortality (80% power, two-sided α=0.05):** VERIFIED.
  - My recomputation: n per arm = (1.96 + 0.8416)² × (0.0475 + 0.042975) / 0.005² ≈ 28,400, so about 56,800 in total.
- **8% → 7.2%:** VERIFIED.
  - n per arm ≈ 7.849 × 0.1404 / 0.008² ≈ 17,200, so about 34,400 in total.
- **Cost of $17M–$57M at $500–$1,000 per participant:** arithmetic correct (34k × $500 ≈ $17M; 57k × $1,000 ≈ $57M). The per-participant figures themselves are UNVERIFIABLE.
  - My RECOVERY cost search returned nothing relevant, so I could not confirm the claim about RECOVERY.
  - An unrelated cost source shows per-participant costs for conventional rehabilitation trials of order $16k–$36k. That is a different trial type and not informative here.
  - For $7M to fund 35–57k participants, total cost per participant would have to be about $120–$200. Whether that is achievable in a streamlined TB trial is unknown.
- **WHO GDG would require a mortality endpoint for adjunctive HDT:** UNVERIFIABLE. I found no source. WHO may accept a composite unfavourable outcome, which would change N.
- **Enrichment (TB meningitis, advanced HIV) reduces N but limits generalisability:** LOGIC, sound.
- **SROI ≈ 3,000 × 7/37 ≈ 570x:** the arithmetic is right (567). But the scaling uses $7M as the baseline all-in cost, while the title says $7M is the Phase III alone. If the baseline all-in cost is larger than $7M, the proportional drop is smaller than 3–10×. I could not see the CG model to resolve this.
- **Baseline mortality of 5–8%:** PLAUSIBLE but unverified. Mortality in DS-TB trial populations is often lower than this (my recollection, not checked). That would raise N further, so this assumption is probably conservative for the critique.
- **Not checked:** the 3.3M-patient benefit base and the "25% materiality bar." They come from the model, which I could not see.

**EVIDENCE FOUND (additional)**
- The Phase II HDT trials I found used surrogate or physiological endpoints, not mortality:
  - the TB-HDT trial used FEV1 and culture conversion;
  - the rosuvastatin trial used 
time to culture conversion by week 8.

- The critique's fork is therefore real: either the Phase III is surrogate-based, or it is far costlier than $7M. This is consistent with how this field has run trials, but it does not prove what CG assumed.

**CORE CLAIM**
- Claim: a Phase III powered to detect a 10% relative mortality reduction needs about 35,000–57,000 participants and therefore costs well above $7M.
- Support: **LOGIC ONLY.** The sample-size half is verified by my recomputation. The cost half depends on a per-participant cost that I could not verify, so the conclusion rests on reasoning and not on direct evidence.

**REVISED CRITIQUE**
Powering a Phase III on mortality at a 10% relative reduction needs about 34,000–57,000 participants (5–8% baseline mortality, 80% power). If CG's $7M budget is for that design, it implies about $120–$200 per participant, which looks implausibly low but is not shown to be impossible. If the trial instead uses a surrogate or composite endpoint, the cost may be reasonable but the model's mortality-only benefit stream is then unsupported. The $25–40M central estimate and the 3–10× SROI reduction are UNGROUNDED because they depend on unverified per-participant costs and an unclear baseline for the 7/37 scaling. Strength: medium to high on the internal-consistency point (cost versus endpoint), low to medium on the specific SROI magnitude. The direction (cost up, SROI down, or p_success overstated) is well supported by logic.

**Search limitations:** I ran out of searches before checking the RECOVERY per-participant cost, the rifampicin–atorvastatin PK effect, and the WHO GDG endpoint requirement. Those items remain unverified.

--- Critique: A $7M Phase III cannot be powered on mortality, and the CEA's benefit is mortality only ---

## Critique 1: Winner's-curse and reference-class patterns, and r and p_success not independent

**OVERALL VERDICT: PARTIALLY VERIFIED.** The winner's-curse logic is sound, and the HDT reference class is partly real. But the Investigator overstates it as a track record of failure to translate. The covariance argument is also shakier than presented.

**CLAIM CHECK**
- **Martineau 2011 vitamin D signal:** VERIFIED.
  - 
Overall, the adjusted HR for time to culture conversion was 1.39 (95% CI 0.90–2.16, p=0.14).

  - 
TaqI genotype modified the effect (p-interaction=0.03), with benefit seen only in tt patients (HR 8.09, 95% CI 1.36–48.01).

  - The tt subgroup was tiny: 
12 subjects.
 This is a textbook winner's-curse case.
  - Later evidence: a meta-analysis found 
no shortening of time to culture conversion overall, with the tt subgroup effect still reported.

  - The endpoint was culture conversion, not mortality. That fits "surrogate positive, no outcome benefit." But no mortality trial was run, so "no robust outcome benefit" is better stated as "no benefit on the surrogate in the full population."
- **CC-11050 and everolimus:** PARTIALLY VERIFIED, and MISCHARACTERISED as failures.
  - The Phase 2 TB-HDT trial found 
improved FEV1 recovery at day 180 for CC-11050 and everolimus (6.30% and 6.56% differences).
 The lower confidence limits were near zero, and the p-values were 0.048 and 0.044.
  - 
None of the arms showed accelerated eradication of MTB infection.

  - I found no Phase 3 or mortality trial. So these are marginal, unreplicated early signals, which fits the winner's-curse argument. They are not documented "failures to translate."
  - A Lancet Respiratory Medicine paper reported 
two control-group patients with life-threatening, treatment-attributable liver injury.

- **Metformin:** PARTIALLY VERIFIED.
  - One RCT concluded that 
adding metformin to anti-TB therapy does not affect sputum conversion.
 The same paper notes that 
other studies (Abinaya, Marupuru) had found additional benefit.
 Early positives that later fail to replicate are supported.
  - A different source claims 
a randomized trial showed faster conversion and better clinical outcomes.
 The evidence is mixed, and I found no mortality data.
- **Everolimus:** see the CC-11050 entry above. The only evidence is the Phase 2 trial.
- **Observational statin cohorts exist:** VERIFIED in outline. 
Several population-based studies found statin use associated with lower TB incidence.
 I did not verify the healthy-user bias claim, but it is a standard and plausible concern.
- **"Bayesian shrinkage 0.7–0.9 gives r = 0.07–0.09":** the arithmetic is correct. The shrinkage factor is an assumption with no empirical anchor.
- **"E[r × p_success] below the product of means":** LOGIC ONLY, and it depends on how p_success is defined.
  - Winner's curse shows that the true effect, given a pass, is below the estimate. It does not by itself create negative covariance between r and p_success.
  - If p_success is the chance of true mortality benefit, r and p_success are positively correlated, and E[rp] would exceed the product of means.
  - Negative covariance arises only if p_success is the chance of passing on a surrogate, because surrogate-only worlds then pass with r≈0.
  - I could not see how the CG model defines p_success or where its 10% comes from. The "anchored on promising early signals" premise is therefore unverified.

**EVIDENCE FOUND (additional)**
- **Atorvastatin itself has only a surrogate signal.**
  - A Phase II atorvastatin trial in Nigeria reported 
a significant reduction in sputum mycobacterial load.

  - It was a Phase II trial using a bacteriological surrogate, with no mortality data. This is the strongest on-point support for the critique.
- **Rosuvastatin Phase 2b was null.**
  - 
Median time to culture conversion was 42 days in both arms (HR 1.30, 95% CI 0.88–1.91, p=0.19).

  - 
The authors concluded it was safe but gave no substantive benefit on culture conversion overall.

  - This is a class-adjacent datapoint against optimism, though rosuvastatin is not atorvastatin.

**CORE CLAIM**
- Claim: the CG's 10% conditional mortality effect is inflated relative to the true effect because it is anchored on selected early or surrogate signals, so r should be shrunk.
- Support: **LOGIC ONLY.** The reference class (vitamin D, metformin, CC-11050, everolimus, rosuvastatin, atorvastatin Phase IIa) shows that surrogate signals are mixed or unreplicated. I found no evidence on how CG derived 10%, and no mortality data for these agents.

**REVISED CRITIQUE**
The effect size is probably better treated as a prior with downward-skewed uncertainty than as a point estimate of 0.10. The supporting reference class is:
- vitamin D: a subgroup-only conversion signal, with null results overall;
- metformin: mixed on sputum conversion;
- CC-11050 and everolimus: marginal FEV1 signals with no conversion benefit;
- rosuvastatin: a null Phase 2b;
- atorvastatin: only a Phase IIa bacillary-load signal.

The shrinkage factor of 0.7–0.9 is UNGROUNDED, and the sign of the r–p_success covariance depends on how p_success is defined. Drop the claim that these agents "failed to translate to outcome benefit." They were never tested on mortality. Strength: medium, direction: decreases (probably).

---

## Critique 2: Hepatotoxicity and myopathy tail, and compounding attenuations

**OVERALL VERDICT: PARTIALLY VERIFIED.** The qualitative harm-tail hypothesis is plausible and UNGROUNDED on magnitude. The arithmetic is correct. The compounding ranges are assumptions drawn from critiques I was not given.

**CLAIM CHECK**
- **Statins and first-line TB drugs add hepatic risk, and statins carry myopathy risk:** PLAUSIBLE. This is standard labeling knowledge, and I did not search for it.
- **Higher myopathy risk with some ART:** PLAUSIBLE, from background pharmacology (boosted protease inhibitors raise atorvastatin levels). I did not verify it in this session. One COVID trial lists 
protease inhibitors among drugs with significant atorvastatin interactions.

- **Small Phase II trials cannot detect excess hepatotoxicity:** LOGIC, and correct. The available trials are small and show no signal:
  - Rosuvastatin Phase 2b: 
grade 3–5 adverse events in 9% of the rosuvastatin arm and 6% of controls, none judged related.

  - Atorvastatin Phase II (Nigeria): reported as 
a safe additive to standard anti-TB treatment.

  - Absence of a signal in these trials is weak evidence either way, as the Investigator says.
- **"10% probability of null or negative contributes about −0.01":** the arithmetic is correct (0.10 × 0.10). The loss may be double-counted if p_success already prices in a null world.
- **Compounding:**
  - 0.65 × 0.5 × 0.7 = 0.2275, and 0.75 × 0.8 × 0.9 = 0.54. So r ≈ 0.023–0.054, which matches the critique.
  - All three factors are assumptions. The "reachable fraction" and "PK attenuation" come from other critiques I cannot see.
  - The Investigator itself flags that the factors overlap and are correlated.

**EVIDENCE FOUND (additional)**
- Drug-interaction concerns with rifampicin are recognised in the statin-TB literature. The StAT-TB protocol cites 
known drug interactions between pravastatin and rifampin in humans.
 That supports the existence of PK attenuation, though not the 0.5–0.8 range, and it concerns pravastatin rather than atorvastatin.
- Metformin shows the same pattern. A PK substudy found 
metformin reduced rifampicin bioavailability by 24%.
 This shows that adjunctive HDTs can erode first-line drug exposure, which is a reference-class point.
- I could not complete my planned check of rifampicin's effect on atorvastatin exposure. From background knowledge, rifampicin induces CYP3A4 and lowers atorvastatin exposure, but this is not verified here.

**CORE CLAIM**
- Claim: the independent attenuation factors (reachable fraction, PK attenuation, shrinkage) multiply to cut r to about 0.023–0.054.
- Support: **LOGIC ONLY.** The multiplication is correct, but each input is an unsourced assumption, and the factors are likely correlated and overlap with Critique 1.

**REVISED CRITIQUE**
A small harm tail is plausible. Existing small trials show no hepatic signal but cannot rule one out. The first-order effect on E[r] from a net-zero or harm world is modest, about −0.01 under the stated assumption. The compounded 0.023–0.054 range is an illustrative upper bound on attenuation, not an estimate. It is UNGROUNDED, "plausible but needs empirical support," and should not be added to Critique 1 without removing overlap. Strength: low to medium for the harm tail alone. The compounding claim stays flagged as hypothetical.

---

## Critique 3: A $7M Phase III cannot be powered on mortality

**OVERALL VERDICT: PARTIALLY VERIFIED.** The sample-size arithmetic checks out. The cost-per-participant figures and the WHO endpoint requirement are unverified. The SROI scaling appears internally inconsistent.

**CLAIM CHECK**
- **5% → 4.5% mortality (80% power, two-sided α=0.05):** VERIFIED.
  - My recomputation: n per arm = (1.96 + 0.8416)² × (0.0475 + 0.042975) / 0.005² ≈ 28,400, so about 56,800 in total.
- **8% → 7.2%:** VERIFIED.
  - n per arm ≈ 7.849 × 0.1404 / 0.008² ≈ 17,200, so about 34,400 in total.
- **Cost of $17M–$57M at $500–$1,000 per participant:** arithmetic correct (34k × $500 ≈ $17M; 57k × $1,000 ≈ $57M). The per-participant figures themselves are UNVERIFIABLE.
  - My RECOVERY cost search returned nothing relevant, so I could not confirm the claim about RECOVERY.
  - An unrelated cost source shows per-participant costs for conventional rehabilitation trials of order $16k–$36k. That is a different trial type and not informative here.
  - For $7M to fund 35–57k participants, total cost per participant would have to be about $120–$200. Whether that is achievable in a streamlined TB trial is unknown.
- **WHO GDG would require a mortality endpoint for adjunctive HDT:** UNVERIFIABLE. I found no source. WHO may accept a composite unfavourable outcome, which would change N.
- **Enrichment (TB meningitis, advanced HIV) reduces N but limits generalisability:** LOGIC, sound.
- **SROI ≈ 3,000 × 7/37 ≈ 570x:** the arithmetic is right (567). But the scaling uses $7M as the baseline all-in cost, while the title says $7M is the Phase III alone. If the baseline all-in cost is larger than $7M, the proportional drop is smaller than 3–10×. I could not see the CG model to resolve this.
- **Baseline mortality of 5–8%:** PLAUSIBLE but unverified. Mortality in DS-TB trial populations is often lower than this (my recollection, not checked). That would raise N further, so this assumption is probably conservative for the critique.
- **Not checked:** the 3.3M-patient benefit base and the "25% materiality bar." They come from the model, which I could not see.

**EVIDENCE FOUND (additional)**
- The Phase II HDT trials I found used surrogate or physiological endpoints, not mortality:
  - the TB-HDT trial used FEV1 and culture conversion;
  - the rosuvastatin trial used 
time to culture conversion by week 8.

- The critique's fork is therefore real: either the Phase III is surrogate-based, or it is far costlier than $7M. This is consistent with how this field has run trials, but it does not prove what CG assumed.

**CORE CLAIM**
- Claim: a Phase III powered to detect a 10% relative mortality reduction needs about 35,000–57,000 participants and therefore costs well above $7M.
- Support: **LOGIC ONLY.** The sample-size half is verified by my recomputation. The cost half depends on a per-participant cost that I could not verify, so the conclusion rests on reasoning and not on direct evidence.

**REVISED CRITIQUE**
Powering a Phase III on mortality at a 10% relative reduction needs about 34,000–57,000 participants (5–8% baseline mortality, 80% power). If CG's $7M budget is for that design, it implies about $120–$200 per participant, which looks implausibly low but is not shown to be impossible. If the trial instead uses a surrogate or composite endpoint, the cost may be reasonable but the model's mortality-only benefit stream is then unsupported. The $25–40M central estimate and the 3–10× SROI reduction are UNGROUNDED because they depend on unverified per-participant costs and an unclear baseline for the 7/37 scaling. Strength: medium to high on the internal-consistency point (cost versus endpoint), low to medium on the specific SROI magnitude. The direction (cost up, SROI down, or p_success overstated) is well supported by logic.

**Search limitations:** I ran out of searches before checking the RECOVERY per-participant cost, the rifampicin–atorvastatin PK effect, and the WHO GDG endpoint requirement. Those items remain unverified.

--- Critique: The all-in framing counts benefits for every treated patient but not the cost of treating them ---

## Critique 1: The all-in framing counts benefits for every treated patient but not the cost of treating them

**CITATION CHECK:** The critique cites no papers. It points to the Stop TB GDF catalog and the MSH price guide as places to look for prices.
- Stop TB GDF catalog: it exists, and 
its prices are ex-works (EXW)
. I did not find atorvastatin in the retrieved portion. It is a TB-medicines catalog and probably doesn't stock a statin, so it may not be the right source.
- MSH International Drug Price Indicator Guide: it exists. It is 
published by Management Sciences for Health
 and 
lists package price and unit price in USD
. I could not retrieve the atorvastatin line itself.

**CLAIM CHECK:**
- **"$1–10 per course in procurement": PLAUSIBLE.**
  - Canadian generic atorvastatin is listed at 
about $0.17–0.23 per tablet
.
  - UK generic packs of 28 tablets 
cost about £1 in 2014
.
  - The ATORTUB phase IIB gave 
40 mg for 2 months
. A related popPK sub-study uses 
16 weeks of 20, 40 or 60 mg
.
  - That is roughly 56–112 tablets. At LMIC tender prices of a few cents each, this gives about $1–6. At rich-country list prices it is $10–25.
  - So $1–10 is a reasonable range, and the low end is close to the critique's break-even of $1.10 per patient.
- **"$3.7M break-even = $1.10 × 3.3M": VERIFIED arithmetic.** If $10.7M is the 2,000x threshold, then $10.7M − $7M = $3.7M, and $3.7M ÷ 3.3M patients ≈ $1.12.
- **"D = $10M gives about 1,250x": VERIFIED arithmetic.** 3,000 × 7/17 ≈ 1,235.
- **The $7M figure, 3.3M patients, ~3,000x SROI and 2,000x threshold: UNVERIFIABLE.** I found no public Coefficient Giving (CG) write-up of this grant or its model. I take these as given inputs.
- **"The $7M excludes delivery costs": UNVERIFIABLE.** I can't see CG's model. It may already net out delivery costs or treat them as a separate counterfactual. The critique itself concedes it can't cite CG's convention for third-party spending.

**EVIDENCE FOUND:**
- ATORTUB phase IIC (NCT06199921) lists Open Philanthropy as a collaborator and plans 
440 patients
. This suggests the program is real and in the right area, though I can't confirm it is the grant in question.
- The registry notes that 
phase III is "more expensive"
 than phase IIB. That supports the idea that the $7M leaves little headroom.
- Procurement alone is cheap, so the critique's result depends mostly on monitoring and clinic costs and on the counterfactual-value convention. The critique already says this.

**CORE CLAIM:**
- Claim: CG's all-in cost omits delivery cost for the ~3.3M treated patients while counting their benefits. Including it would push SROI materially below the threshold unless third-party money is heavily discounted.
- Support: **LOGIC ONLY.**
- Why: The arithmetic and plausible prices hold, but I found no evidence on how CG's model treats delivery costs or third-party spending.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The consistency argument and the arithmetic are sound, and the price range is plausible. The factual premise that CG excludes delivery costs is unverified, and the critique correctly flags it as ungrounded.

**REVISED CRITIQUE:** If CG credits benefits to all treated patients but counts only R&D and adoption costs, the framing is asymmetric.
- Generic atorvastatin costs roughly $1–10 per course, plausibly more once monitoring is included. That is $3–33M across 3.3M patients.
- This could take SROI from above 2,000x to roughly 1,000–1,250x at $10M. It could have little effect if government and Global Fund money is heavily discounted.
- Status: UNGROUNDED on CG's actual convention. Direction: decreases. Magnitude: **medium**, downgraded from large because it depends on an unverified convention and on procurement being cheap.

---

## Critique 2: Regulatory, pharmacovigilance and dissemination costs have no obvious payer, and the $7M likely under-budgets them

**CITATION CHECK:** No papers are cited. The critique says it cannot cite a source for the hepatotoxicity overlap. It names Unitaid and Global Fund transition grants as candidate sources for rollout costs, and I did not check those.

**CLAIM CHECK:**
- **"Statins cause hepatotoxicity and myopathy": VERIFIED.**
  - Atorvastatin is the statin most often reported in statin liver-injury cases: 
53.48% of FAERS statin DILI reports
.
  - Case reports also describe 
liver injury with rhabdomyolysis
.
  - Serious cases are rare. 
Statin liver injury is described as frequent but usually not severe
, and 
idiosyncratic injury as "very rare"
.
- **"This overlaps with first-line TB drug hepatotoxicity": VERIFIED (pharmacological argument).** Anti-TB drug-induced liver injury 
occurs in 2–28% of patients
, and 
it can reduce treatment effectiveness and cause treatment failure
.
- **"Safety monitoring and adverse-event management are a real cost": PLAUSIBLE.** The phase II ATORTUB reports describe atorvastatin as 
generally safe and well tolerated
. Those are small trials (40 and 150 patients) run by the sponsors. They do not show that no monitoring is needed at scale.
- **"No sponsor has a commercial incentive for a generic": PLAUSIBLE (logic).** It is not contradicted. Other statin-TB trials are publicly funded, for example StatinTB under 
EDCTP2
. That shows academic and public funders can pay for generic repurposing trials, but not for guideline rollout.
- **"$5–20M rollout programme, or a $4M add-on, pushes the total past $10.7M": the arithmetic is correct ($7M + $4M = $11M), but the magnitude is UNGROUNDED.** I found no rollout-cost benchmark.
- **"A Phase IIc of $320k plus any plausible Phase III already uses most of the $7M": UNVERIFIABLE.** I found no budget figures.
- **"Adverse-event harms are not netted against the mortality benefit": UNVERIFIABLE.** It depends on CG's model.

**EVIDENCE FOUND:**
- The ATORTUB phase IIC registry entry describes it as 
a pilot phase III
 and notes that 
the phase III will be fully international and multicenter
. A multi-country phase III is likely to take a large share of $7M before any adoption work.
- This critique overlaps with Critique 1, because both include monitoring and delivery costs. Adding both would double-count them.
- Sources for the rollout-cost gap are still missing. I did not pull Unitaid or Global Fund documents.

**CORE CLAIM:**
- Claim: The $7M is too small to cover the unfunded adoption infrastructure (guidelines, training, supply chain, pharmacovigilance) on top of the trials.
- Support: **LOGIC ONLY.**
- Why: The incentive argument and the hepatotoxicity concern hold, but I found no budget data or comparable rollout costs.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The qualitative hypothesis survives. The cost magnitudes are ungrounded.

**REVISED CRITIQUE:** Atorvastatin is generic, so the costs of guideline change, dissemination and pharmacovigilance have no obvious commercial payer. There is a verified safety concern: atorvastatin is the statin most often linked to liver injury, and anti-TB drugs are also hepatotoxic.
- The size of any shortfall in the $7M is **UNGROUNDED — plausible but needs empirical support.** Drop the $5–20M illustration, or keep it flagged as illustrative only.
- The direction is uncertain and should not be stated as "likely under-budgets" without evidence. Magnitude: medium to small. Merge the monitoring-cost part with Critique 1 to avoid double counting.

---

## Critique 3: Unclear scope boundary for the sweat-diagnostic workstream

**CITATION CHECK:** No citations. The critique itself says it has no source on the workstream's structure.

**CLAIM CHECK:**
- **"A sweat-diagnostic workstream exists in this program": UNVERIFIABLE.** I found no public link between the statin program and a sweat-based diagnostic. Sweat as a TB diagnostic matrix is a real research area: a proof-of-concept study found 
26 proteins detected only in the sweat of active TB patients
. That study says nothing about this program.
- **"Any diagnostic budget above ~$3.7M breaches 2,000x": VERIFIED arithmetic, conditional on the other numbers.** It uses the same $10.7M threshold as Critique 1.
- **Cost and benefit mismatch scenarios: logically coherent but hypothetical.** Only one of the four branches has any effect: costs excluded while diagnostic-linked benefits are counted. There is no evidence that this branch applies.

**EVIDENCE FOUND:** Nothing on the grant structure. I did not find the CG grant page.

**CORE CLAIM:**
- Claim: Diagnostic costs sit outside the $7M while diagnostic-linked benefits are counted in the credited benefits.
- Support: **LOGIC ONLY.**
- Why: The critique presents it as a scenario, and I found no evidence for or against it.

**OVERALL VERDICT: UNVERIFIABLE.** Keep it only as a low-priority clarification question for CG about grant structure and whether diagnostic benefits are credited. It is not an established flaw. I recommend dropping it from any list of substantive critiques unless the thread text shows that diagnostic benefits are actually counted.

--- Critique: Regulatory, pharmacovigilance and dissemination costs for an off-patent drug have no obvious payer, and the $7M likely under-budgets them ---

## Critique 1: The all-in framing counts benefits for every treated patient but not the cost of treating them

**CITATION CHECK:** The critique cites no papers. It points to the Stop TB GDF catalog and the MSH price guide as places to look for prices.
- Stop TB GDF catalog: it exists, and 
its prices are ex-works (EXW)
. I did not find atorvastatin in the retrieved portion. It is a TB-medicines catalog and probably doesn't stock a statin, so it may not be the right source.
- MSH International Drug Price Indicator Guide: it exists. It is 
published by Management Sciences for Health
 and 
lists package price and unit price in USD
. I could not retrieve the atorvastatin line itself.

**CLAIM CHECK:**
- **"$1–10 per course in procurement": PLAUSIBLE.**
  - Canadian generic atorvastatin is listed at 
about $0.17–0.23 per tablet
.
  - UK generic packs of 28 tablets 
cost about £1 in 2014
.
  - The ATORTUB phase IIB gave 
40 mg for 2 months
. A related popPK sub-study uses 
16 weeks of 20, 40 or 60 mg
.
  - That is roughly 56–112 tablets. At LMIC tender prices of a few cents each, this gives about $1–6. At rich-country list prices it is $10–25.
  - So $1–10 is a reasonable range, and the low end is close to the critique's break-even of $1.10 per patient.
- **"$3.7M break-even = $1.10 × 3.3M": VERIFIED arithmetic.** If $10.7M is the 2,000x threshold, then $10.7M − $7M = $3.7M, and $3.7M ÷ 3.3M patients ≈ $1.12.
- **"D = $10M gives about 1,250x": VERIFIED arithmetic.** 3,000 × 7/17 ≈ 1,235.
- **The $7M figure, 3.3M patients, ~3,000x SROI and 2,000x threshold: UNVERIFIABLE.** I found no public Coefficient Giving (CG) write-up of this grant or its model. I take these as given inputs.
- **"The $7M excludes delivery costs": UNVERIFIABLE.** I can't see CG's model. It may already net out delivery costs or treat them as a separate counterfactual. The critique itself concedes it can't cite CG's convention for third-party spending.

**EVIDENCE FOUND:**
- ATORTUB phase IIC (NCT06199921) lists Open Philanthropy as a collaborator and plans 
440 patients
. This suggests the program is real and in the right area, though I can't confirm it is the grant in question.
- The registry notes that 
phase III is "more expensive"
 than phase IIB. That supports the idea that the $7M leaves little headroom.
- Procurement alone is cheap, so the critique's result depends mostly on monitoring and clinic costs and on the counterfactual-value convention. The critique already says this.

**CORE CLAIM:**
- Claim: CG's all-in cost omits delivery cost for the ~3.3M treated patients while counting their benefits. Including it would push SROI materially below the threshold unless third-party money is heavily discounted.
- Support: **LOGIC ONLY.**
- Why: The arithmetic and plausible prices hold, but I found no evidence on how CG's model treats delivery costs or third-party spending.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The consistency argument and the arithmetic are sound, and the price range is plausible. The factual premise that CG excludes delivery costs is unverified, and the critique correctly flags it as ungrounded.

**REVISED CRITIQUE:** If CG credits benefits to all treated patients but counts only R&D and adoption costs, the framing is asymmetric.
- Generic atorvastatin costs roughly $1–10 per course, plausibly more once monitoring is included. That is $3–33M across 3.3M patients.
- This could take SROI from above 2,000x to roughly 1,000–1,250x at $10M. It could have little effect if government and Global Fund money is heavily discounted.
- Status: UNGROUNDED on CG's actual convention. Direction: decreases. Magnitude: **medium**, downgraded from large because it depends on an unverified convention and on procurement being cheap.

---

## Critique 2: Regulatory, pharmacovigilance and dissemination costs have no obvious payer, and the $7M likely under-budgets them

**CITATION CHECK:** No papers are cited. The critique says it cannot cite a source for the hepatotoxicity overlap. It names Unitaid and Global Fund transition grants as candidate sources for rollout costs, and I did not check those.

**CLAIM CHECK:**
- **"Statins cause hepatotoxicity and myopathy": VERIFIED.**
  - Atorvastatin is the statin most often reported in statin liver-injury cases: 
53.48% of FAERS statin DILI reports
.
  - Case reports also describe 
liver injury with rhabdomyolysis
.
  - Serious cases are rare. 
Statin liver injury is described as frequent but usually not severe
, and 
idiosyncratic injury as "very rare"
.
- **"This overlaps with first-line TB drug hepatotoxicity": VERIFIED (pharmacological argument).** Anti-TB drug-induced liver injury 
occurs in 2–28% of patients
, and 
it can reduce treatment effectiveness and cause treatment failure
.
- **"Safety monitoring and adverse-event management are a real cost": PLAUSIBLE.** The phase II ATORTUB reports describe atorvastatin as 
generally safe and well tolerated
. Those are small trials (40 and 150 patients) run by the sponsors. They do not show that no monitoring is needed at scale.
- **"No sponsor has a commercial incentive for a generic": PLAUSIBLE (logic).** It is not contradicted. Other statin-TB trials are publicly funded, for example StatinTB under 
EDCTP2
. That shows academic and public funders can pay for generic repurposing trials, but not for guideline rollout.
- **"$5–20M rollout programme, or a $4M add-on, pushes the total past $10.7M": the arithmetic is correct ($7M + $4M = $11M), but the magnitude is UNGROUNDED.** I found no rollout-cost benchmark.
- **"A Phase IIc of $320k plus any plausible Phase III already uses most of the $7M": UNVERIFIABLE.** I found no budget figures.
- **"Adverse-event harms are not netted against the mortality benefit": UNVERIFIABLE.** It depends on CG's model.

**EVIDENCE FOUND:**
- The ATORTUB phase IIC registry entry describes it as 
a pilot phase III
 and notes that 
the phase III will be fully international and multicenter
. A multi-country phase III is likely to take a large share of $7M before any adoption work.
- This critique overlaps with Critique 1, because both include monitoring and delivery costs. Adding both would double-count them.
- Sources for the rollout-cost gap are still missing. I did not pull Unitaid or Global Fund documents.

**CORE CLAIM:**
- Claim: The $7M is too small to cover the unfunded adoption infrastructure (guidelines, training, supply chain, pharmacovigilance) on top of the trials.
- Support: **LOGIC ONLY.**
- Why: The incentive argument and the hepatotoxicity concern hold, but I found no budget data or comparable rollout costs.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The qualitative hypothesis survives. The cost magnitudes are ungrounded.

**REVISED CRITIQUE:** Atorvastatin is generic, so the costs of guideline change, dissemination and pharmacovigilance have no obvious commercial payer. There is a verified safety concern: atorvastatin is the statin most often linked to liver injury, and anti-TB drugs are also hepatotoxic.
- The size of any shortfall in the $7M is **UNGROUNDED — plausible but needs empirical support.** Drop the $5–20M illustration, or keep it flagged as illustrative only.
- The direction is uncertain and should not be stated as "likely under-budgets" without evidence. Magnitude: medium to small. Merge the monitoring-cost part with Critique 1 to avoid double counting.

---

## Critique 3: Unclear scope boundary for the sweat-diagnostic workstream

**CITATION CHECK:** No citations. The critique itself says it has no source on the workstream's structure.

**CLAIM CHECK:**
- **"A sweat-diagnostic workstream exists in this program": UNVERIFIABLE.** I found no public link between the statin program and a sweat-based diagnostic. Sweat as a TB diagnostic matrix is a real research area: a proof-of-concept study found 
26 proteins detected only in the sweat of active TB patients
. That study says nothing about this program.
- **"Any diagnostic budget above ~$3.7M breaches 2,000x": VERIFIED arithmetic, conditional on the other numbers.** It uses the same $10.7M threshold as Critique 1.
- **Cost and benefit mismatch scenarios: logically coherent but hypothetical.** Only one of the four branches has any effect: costs excluded while diagnostic-linked benefits are counted. There is no evidence that this branch applies.

**EVIDENCE FOUND:** Nothing on the grant structure. I did not find the CG grant page.

**CORE CLAIM:**
- Claim: Diagnostic costs sit outside the $7M while diagnostic-linked benefits are counted in the credited benefits.
- Support: **LOGIC ONLY.**
- Why: The critique presents it as a scenario, and I found no evidence for or against it.

**OVERALL VERDICT: UNVERIFIABLE.** Keep it only as a low-priority clarification question for CG about grant structure and whether diagnostic benefits are credited. It is not an established flaw. I recommend dropping it from any list of substantive critiques unless the thread text shows that diagnostic benefits are actually counted.

--- Critique: Unclear scope boundary for the sweat-diagnostic workstream ---

## Critique 1: The all-in framing counts benefits for every treated patient but not the cost of treating them

**CITATION CHECK:** The critique cites no papers. It points to the Stop TB GDF catalog and the MSH price guide as places to look for prices.
- Stop TB GDF catalog: it exists, and 
its prices are ex-works (EXW)
. I did not find atorvastatin in the retrieved portion. It is a TB-medicines catalog and probably doesn't stock a statin, so it may not be the right source.
- MSH International Drug Price Indicator Guide: it exists. It is 
published by Management Sciences for Health
 and 
lists package price and unit price in USD
. I could not retrieve the atorvastatin line itself.

**CLAIM CHECK:**
- **"$1–10 per course in procurement": PLAUSIBLE.**
  - Canadian generic atorvastatin is listed at 
about $0.17–0.23 per tablet
.
  - UK generic packs of 28 tablets 
cost about £1 in 2014
.
  - The ATORTUB phase IIB gave 
40 mg for 2 months
. A related popPK sub-study uses 
16 weeks of 20, 40 or 60 mg
.
  - That is roughly 56–112 tablets. At LMIC tender prices of a few cents each, this gives about $1–6. At rich-country list prices it is $10–25.
  - So $1–10 is a reasonable range, and the low end is close to the critique's break-even of $1.10 per patient.
- **"$3.7M break-even = $1.10 × 3.3M": VERIFIED arithmetic.** If $10.7M is the 2,000x threshold, then $10.7M − $7M = $3.7M, and $3.7M ÷ 3.3M patients ≈ $1.12.
- **"D = $10M gives about 1,250x": VERIFIED arithmetic.** 3,000 × 7/17 ≈ 1,235.
- **The $7M figure, 3.3M patients, ~3,000x SROI and 2,000x threshold: UNVERIFIABLE.** I found no public Coefficient Giving (CG) write-up of this grant or its model. I take these as given inputs.
- **"The $7M excludes delivery costs": UNVERIFIABLE.** I can't see CG's model. It may already net out delivery costs or treat them as a separate counterfactual. The critique itself concedes it can't cite CG's convention for third-party spending.

**EVIDENCE FOUND:**
- ATORTUB phase IIC (NCT06199921) lists Open Philanthropy as a collaborator and plans 
440 patients
. This suggests the program is real and in the right area, though I can't confirm it is the grant in question.
- The registry notes that 
phase III is "more expensive"
 than phase IIB. That supports the idea that the $7M leaves little headroom.
- Procurement alone is cheap, so the critique's result depends mostly on monitoring and clinic costs and on the counterfactual-value convention. The critique already says this.

**CORE CLAIM:**
- Claim: CG's all-in cost omits delivery cost for the ~3.3M treated patients while counting their benefits. Including it would push SROI materially below the threshold unless third-party money is heavily discounted.
- Support: **LOGIC ONLY.**
- Why: The arithmetic and plausible prices hold, but I found no evidence on how CG's model treats delivery costs or third-party spending.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The consistency argument and the arithmetic are sound, and the price range is plausible. The factual premise that CG excludes delivery costs is unverified, and the critique correctly flags it as ungrounded.

**REVISED CRITIQUE:** If CG credits benefits to all treated patients but counts only R&D and adoption costs, the framing is asymmetric.
- Generic atorvastatin costs roughly $1–10 per course, plausibly more once monitoring is included. That is $3–33M across 3.3M patients.
- This could take SROI from above 2,000x to roughly 1,000–1,250x at $10M. It could have little effect if government and Global Fund money is heavily discounted.
- Status: UNGROUNDED on CG's actual convention. Direction: decreases. Magnitude: **medium**, downgraded from large because it depends on an unverified convention and on procurement being cheap.

---

## Critique 2: Regulatory, pharmacovigilance and dissemination costs have no obvious payer, and the $7M likely under-budgets them

**CITATION CHECK:** No papers are cited. The critique says it cannot cite a source for the hepatotoxicity overlap. It names Unitaid and Global Fund transition grants as candidate sources for rollout costs, and I did not check those.

**CLAIM CHECK:**
- **"Statins cause hepatotoxicity and myopathy": VERIFIED.**
  - Atorvastatin is the statin most often reported in statin liver-injury cases: 
53.48% of FAERS statin DILI reports
.
  - Case reports also describe 
liver injury with rhabdomyolysis
.
  - Serious cases are rare. 
Statin liver injury is described as frequent but usually not severe
, and 
idiosyncratic injury as "very rare"
.
- **"This overlaps with first-line TB drug hepatotoxicity": VERIFIED (pharmacological argument).** Anti-TB drug-induced liver injury 
occurs in 2–28% of patients
, and 
it can reduce treatment effectiveness and cause treatment failure
.
- **"Safety monitoring and adverse-event management are a real cost": PLAUSIBLE.** The phase II ATORTUB reports describe atorvastatin as 
generally safe and well tolerated
. Those are small trials (40 and 150 patients) run by the sponsors. They do not show that no monitoring is needed at scale.
- **"No sponsor has a commercial incentive for a generic": PLAUSIBLE (logic).** It is not contradicted. Other statin-TB trials are publicly funded, for example StatinTB under 
EDCTP2
. That shows academic and public funders can pay for generic repurposing trials, but not for guideline rollout.
- **"$5–20M rollout programme, or a $4M add-on, pushes the total past $10.7M": the arithmetic is correct ($7M + $4M = $11M), but the magnitude is UNGROUNDED.** I found no rollout-cost benchmark.
- **"A Phase IIc of $320k plus any plausible Phase III already uses most of the $7M": UNVERIFIABLE.** I found no budget figures.
- **"Adverse-event harms are not netted against the mortality benefit": UNVERIFIABLE.** It depends on CG's model.

**EVIDENCE FOUND:**
- The ATORTUB phase IIC registry entry describes it as 
a pilot phase III
 and notes that 
the phase III will be fully international and multicenter
. A multi-country phase III is likely to take a large share of $7M before any adoption work.
- This critique overlaps with Critique 1, because both include monitoring and delivery costs. Adding both would double-count them.
- Sources for the rollout-cost gap are still missing. I did not pull Unitaid or Global Fund documents.

**CORE CLAIM:**
- Claim: The $7M is too small to cover the unfunded adoption infrastructure (guidelines, training, supply chain, pharmacovigilance) on top of the trials.
- Support: **LOGIC ONLY.**
- Why: The incentive argument and the hepatotoxicity concern hold, but I found no budget data or comparable rollout costs.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The qualitative hypothesis survives. The cost magnitudes are ungrounded.

**REVISED CRITIQUE:** Atorvastatin is generic, so the costs of guideline change, dissemination and pharmacovigilance have no obvious commercial payer. There is a verified safety concern: atorvastatin is the statin most often linked to liver injury, and anti-TB drugs are also hepatotoxic.
- The size of any shortfall in the $7M is **UNGROUNDED — plausible but needs empirical support.** Drop the $5–20M illustration, or keep it flagged as illustrative only.
- The direction is uncertain and should not be stated as "likely under-budgets" without evidence. Magnitude: medium to small. Merge the monitoring-cost part with Critique 1 to avoid double counting.

---

## Critique 3: Unclear scope boundary for the sweat-diagnostic workstream

**CITATION CHECK:** No citations. The critique itself says it has no source on the workstream's structure.

**CLAIM CHECK:**
- **"A sweat-diagnostic workstream exists in this program": UNVERIFIABLE.** I found no public link between the statin program and a sweat-based diagnostic. Sweat as a TB diagnostic matrix is a real research area: a proof-of-concept study found 
26 proteins detected only in the sweat of active TB patients
. That study says nothing about this program.
- **"Any diagnostic budget above ~$3.7M breaches 2,000x": VERIFIED arithmetic, conditional on the other numbers.** It uses the same $10.7M threshold as Critique 1.
- **Cost and benefit mismatch scenarios: logically coherent but hypothetical.** Only one of the four branches has any effect: costs excluded while diagnostic-linked benefits are counted. There is no evidence that this branch applies.

**EVIDENCE FOUND:** Nothing on the grant structure. I did not find the CG grant page.

**CORE CLAIM:**
- Claim: Diagnostic costs sit outside the $7M while diagnostic-linked benefits are counted in the credited benefits.
- Support: **LOGIC ONLY.**
- Why: The critique presents it as a scenario, and I found no evidence for or against it.

**OVERALL VERDICT: UNVERIFIABLE.** Keep it only as a low-priority clarification question for CG about grant structure and whether diagnostic benefits are credited. It is not an established flaw. I recommend dropping it from any list of substantive critiques unless the thread text shows that diagnostic benefits are actually counted.

--- Critique: Reference-class check: TB Phase III trials, and the evidence package WHO may require, point to more than one trial ---

## Critique 1: Reference-class check for TB Phase III trial cost

**CITATION CHECK**
- The critique cites no papers. It names five trials: Study 31/A5349, STREAM, endTB, TRUNCATE-TB and SimpliciTB.
- **Study 31/A5349: VERIFIED.** 
Target enrollment is 2500 participants.
 The record also lists 
TBTC Study 31, ACTG Study A5349
 as the same trial.
- **STREAM: VERIFIED as a Phase III TB trial.** 
The first participant was enrolled in July 2012.
 I did not retrieve its enrollment number.
- **endTB: VERIFIED as a Phase III trial.** 
It is funded by a Unitaid grant.
 I did not retrieve enrollment.
- **TRUNCATE-TB and SimpliciTB: NOT CHECKED.** I found no source for their sizes.
- The "hundreds to thousands" range is plausible but only partly confirmed.

**CLAIM CHECK**
- **TB Phase III budgets are "generally in the tens of millions": PLAUSIBLE, with one direct TB data point.**
  - TB-PRACTECAL is a Phase 2b-3 drug-resistant TB trial. 
Its total cost was €33.9 million, or €61,460 per patient.

  - A TB-specific cost model gives 
a mean of $48.9 million for trials with an active-drug control arm.

  - A systematic review found 
a range of US$7–221 million per Phase 2/3 trial.

  - The general median is 
$19 million for a single Phase III trial, from 138 FDA pivotal trials (2015–16).

  - TAG's bedaquiline analysis used 
Sertkaya (2016) estimates, with a Phase III upper bound of US$26.6 million,
 then adjusted downward for lower trial costs in LMICs.
- **I found no actual budgets for Study 31, STREAM, endTB, TRUNCATE-TB or SimpliciTB. UNVERIFIABLE.** The critique already flags its figures as recalled and ungrounded.
- **The counterargument about cheap trials with routine-care endpoints: PLAUSIBLE, with some support.**
  - An EDCTP-funded pragmatic DS-TB trial protocol (NCT05575518) lists 
a grand total of £226,734 in its per-site budget table.

  - The document is ambiguous. The budget is stated for 
a minimal number of 436 patients per site.

  - Pragmatic DS-TB trials can therefore be much cheaper per patient than TB-PRACTECAL. The $20–60M range is probably the upper part of the plausible distribution for this design.
- **Arithmetic: VERIFIED.** $20–60M against $7M is about 2.9–8.6×. 3,050 divided by that gives about 355–1,050. $30M gives about 710.
- **WHO may require subgroup evidence, multiple trials or an IPD meta-analysis: UNVERIFIABLE.** I found no WHO document setting a number-of-trials requirement. The critique concedes this. A 2026 review of host-directed therapy (HDT) says 
moving these agents into standard practice requires large-scale, stratified Phase III trials.
 That loosely supports the stratification point.

**EVIDENCE FOUND**
- TB-PRACTECAL's cost per patient, €61,460, is high because it ran in hospital-based drug-resistant TB settings. Using it for a DS-TB adjunct probably overstates cost.
- The Mullard/JAMA median of $19M comes from FDA-approved pivotal trials, so it is not TB-specific.

**CORE CLAIM**
- **Claim:** A Phase III trial for this intervention would plausibly cost well above $7M, in the range $20–60M.
- **Support: SUPPORTED for the reference class, not for this trial design.**
- **Why:** TB-PRACTECAL and the JAMA/TAG estimates directly show tens of millions per TB Phase III. I found no cost for a cheap DS-TB adjunct trial, and one pragmatic protocol hints at a much lower cost.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The direction (a $7M all-in cost looks low) survives. The specific trial budgets and the WHO multi-trial requirement are unverified.

**REVISED CRITIQUE**
- Documented TB Phase III costs include €33.9M for TB-PRACTECAL (drug-resistant TB) and a general pivotal-trial median of about $19M.
- A $7M all-in budget is below that reference class unless the trial is a cheap pragmatic design with routine-care endpoints.
- A central all-in cost of $15–30M gives SROI of roughly 700–1,400x. This range is my adjustment, wider than the original "about 700x."
- Mark as UNGROUNDED: the claim that WHO requires multiple trials or an IPD meta-analysis, and the budgets of the five named trials.
- Strength: **medium**. Direction: SROI down.

---

## Critique 2: Benefit and cost come from different counterfactuals

**CITATION CHECK**
- The critique cites no external sources. It is an algebraic argument.
- I could not see the CEA or BOTEC, so I cannot confirm the "1 year × plateau deaths" benefit, the 3,050x SROI, the $7M or $6.7M figures, or the 2% case decline. These are **UNVERIFIABLE** from what I was given.

**CLAIM CHECK**
- **Pure delay gives PV_B/PV_C, independent of D: PLAUSIBLE, with a hidden assumption.** I re-derived it. Shifting the whole stream by D scales both PVs by e^(−rD), so the ratio of differences is PV_B/PV_C. For a perpetuity, the benefit lost is about D × one plateau year. That matches the BOTEC's benefit term, so the critique correctly isolates the denominator as the inconsistent part.
- **The assumption: other funders' $6.7M costs the grant only the time value of money, r·D·PV_C.**
  - This holds only if money is valued at the discount rate r.
  - If displaced dollars would fund other TB work at a high cost-effectiveness bar, the cost is not just interest.
  - By my rough calculation, the ratio is then about (1−e^(−rD))·PV_B/PV_C + CE_other·e^(−rD).
  - With D=1 and r=4%, that is about 0.4–0.5× the BOTEC plus CE_other. It could fall at or below the BOTEC unless CE_other is very high.
  - The critique mentions displacement only as a separate issue. It is actually load-bearing for the delay branch.
- **Never branch gives PV_B/PV_C: VERIFIED algebraically.** This depends on the grant being truly decisive and on attributing the whole program's benefit to it.
- **Mixture is the same: VERIFIED algebraically.**
- **Multiplier arithmetic: VERIFIED.** 1/0.06 ≈ 16.7. Times 0.6–0.7 is about 10–11.7. Dividing by 0.85 gives about 12–14. Without the decline, 1/0.04 = 25, which gives about 18–20. 3,050 × 10–18 gives about 30,500–55,000.
- **The 0.6–0.7 "delay factor" and 0.85 "cost-discount adjustment": UNGROUNDED.** They are not derived or sourced. They probably reflect lag before benefits start, but that is not stated.
- **Internal inconsistency:** Estimated Direction is "decreases," yet the critique argues SROI is 10–20× higher. It presumably means "the BOTEC understates SROI," but the label is confusing.

**EVIDENCE FOUND**
- None external. Nothing I found speaks to whether CG's framing was deliberately conservative.

**CORE CLAIM**
- **Claim:** Under every coherent counterfactual the ratio equals PV_B/PV_C, so the BOTEC understates SROI by roughly 10–20×.
- **Support: LOGIC ONLY.**
- **Why:** The algebra holds when other funders' money is valued at the discount rate. It fails if displacement is priced at the funder's opportunity cost, and the multiplier rests on assumed horizon and delay parameters.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The hybrid-counterfactual diagnosis is sound. "Every coherent framing" and the 10–20× multiple are overstated.

**REVISED CRITIQUE**
- The BOTEC pairs a delay-world benefit (one year of plateau deaths averted) with a never-world cost (the full pathway). That is internally inconsistent.
- If other funders' dollars are treated as costing only time value, a consistent framing gives PV_B/PV_C. That is higher than the BOTEC by roughly the number of discounted benefit-years, which is **UNGROUNDED but plausibly about 5–20×** under a finite horizon.
- If displaced funding is valued at CG's own bar, the delay branch could be near or below the BOTEC. Only the never branch reliably raises the ratio.
- Do not report 30,000–55,000x. Report it as a conditional upper scenario.
- Strength: **medium**, not large. Direction: SROI up in the never branch, ambiguous in the delay branch.

---

## Critique 3: "Never" is a live branch for a generic-statin TB program

**CITATION CHECK**
- The critique cites no papers and flags the funder landscape as ungrounded.
- **NIH and Johns Hopkins preclinical and early clinical work: PARTIALLY VERIFIED.**
  - StAT-TB is 
a Phase 2b dose-finding study of pravastatin in adults with TB, sponsored by NIAID. It started in February 2020 and completed in 2022.

  - Preclinical statin mouse work acknowledges 
NIH grant R00 AI114952 and a Bill & Melinda Gates Foundation grant (OPP 1066499).

  - Hopkins affiliation did not appear in the retrieved text.
- **Searches of ClinicalTrials.gov, ICTRP, TAG, EDCTP, Unitaid and RePORTER were not possible with my tools.** The absence of a Phase III statin-TB trial in my results is therefore only weak evidence.

**CLAIM CHECK**
- **Statins are off-patent and have no commercial sponsor: PLAUSIBLE.** This is a general repurposing argument. I did not locate a source for it.
- **Public-health funders have favored novel regimens, shortened regimens and vaccines over HDTs: UNVERIFIABLE.**
  - Gates did fund a four-arm HDT Phase 2 trial. 
It "provided funding for this trial and contributed to the selection of host-directed therapy candidates."
 Statins were not among its four arms.
  - Statins also drew NIH and Gates support at the preclinical stage and NIAID at Phase 2b. Funders have not ignored statins.
- **The grant is the gating event, with dose-finding preceding Phase III: QUESTIONABLE.**
  - StAT-TB, a Phase 2b dose-finding trial, is already completed.
  - A separate rosuvastatin Phase 2b trial reported: 
median time to culture conversion was 42 days in both arms (HR 1.30, 0.88–1.91, p=0.19).
 The authors concluded that 
rosuvastatin 10 mg was safe but did not produce substantive benefits on culture conversion overall.

  - A PET-CT sub-study found 
no impact on PET-CT changes.

  - The critique does not mention this null result. It lowers p_success. It also makes a "never" outcome more likely, but through low prior efficacy rather than lack of funding.
  - Whether the CG Phase IIc is gating depends on the grant's design, which I could not see.
- **Observational support exists.** 
A meta-analysis found statins associated with reduced active TB risk (OR 0.66; 95% CI 0.54–0.81).
 This is observational and confounded.
- **Expected speedup q·H_eff + (1−q)·D exceeds 1 year for q = 0.1–0.2: VERIFIED arithmetically.** For example, 0.1×10 + 0.9×1 = 1.9. The "break-even at q ≈ 0" is loose, because at q=0 with D=0.5 the speedup is below 1.
- **"About 20× higher" SROI: arithmetic VERIFIED, framing problematic.** $7M / $0.32M ≈ 22. But crediting the whole downstream benefit while charging only the grant's cost ignores that the never branch needs the other funders' $6.7M. This contradicts Critique 2, which charges the full cost in that branch.
- **Cross-references to "Critique 1" appear to refer to the speedup critique (Critique 2 here).** The numbering is mismatched.

**EVIDENCE FOUND**
- The negative rosuvastatin Phase 2b is the main added evidence. It weakens efficacy priors and the case for a Phase III.
- A 2026 review says HDT candidates, including statins, still need 
large-scale, stratified Phase III trials.
 That is consistent with the gap the critique describes.
- I found no registered statin-TB Phase III trial in these searches. This is not exhaustive.

**CORE CLAIM**
- **Claim:** The realistic counterfactual for a CG-funded statin Phase IIc has a substantial probability (q about 0.1–0.2 or more) of long delay or never, so expected speedup is above 1 year.
- **Support: LOGIC ONLY.**
- **Why:** The reasoning is coherent and consistent with no Phase III being found. I found no direct evidence on q, and existing NIH, Gates and other Phase 2b statin trials show funding has occurred.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The hypothesis stays as UNGROUNDED but plausible. The gating-event premise and the "20× higher" figure are weakened.

**REVISED CRITIQUE**
- Statin-TB trials have been funded at Phase 2b by NIAID, and a rosuvastatin Phase 2b exists. A Phase III sponsor is plausibly still lacking, but I could not confirm that.
- The speedup is better modeled as a distribution than as a fixed 1 year. This is logic-only and depends on an unestimated q.
- The null rosuvastatin result should lower p_success. That partly offsets any gain from a longer speedup.
- Drop the "SROI about 20× higher" claim. It credits the full downstream benefit against only the grant cost, which conflicts with Critique 2's accounting.
- Strength: **low to medium**. Direction: ambiguous, with up in the never branch and down if p_success falls or the grant is redundant.

--- Critique: The speedup benefit and the all-in cost come from different counterfactuals. Every coherent framing gives roughly 10–20x higher SROI. ---

## Critique 1: Reference-class check for TB Phase III trial cost

**CITATION CHECK**
- The critique cites no papers. It names five trials: Study 31/A5349, STREAM, endTB, TRUNCATE-TB and SimpliciTB.
- **Study 31/A5349: VERIFIED.** 
Target enrollment is 2500 participants.
 The record also lists 
TBTC Study 31, ACTG Study A5349
 as the same trial.
- **STREAM: VERIFIED as a Phase III TB trial.** 
The first participant was enrolled in July 2012.
 I did not retrieve its enrollment number.
- **endTB: VERIFIED as a Phase III trial.** 
It is funded by a Unitaid grant.
 I did not retrieve enrollment.
- **TRUNCATE-TB and SimpliciTB: NOT CHECKED.** I found no source for their sizes.
- The "hundreds to thousands" range is plausible but only partly confirmed.

**CLAIM CHECK**
- **TB Phase III budgets are "generally in the tens of millions": PLAUSIBLE, with one direct TB data point.**
  - TB-PRACTECAL is a Phase 2b-3 drug-resistant TB trial. 
Its total cost was €33.9 million, or €61,460 per patient.

  - A TB-specific cost model gives 
a mean of $48.9 million for trials with an active-drug control arm.

  - A systematic review found 
a range of US$7–221 million per Phase 2/3 trial.

  - The general median is 
$19 million for a single Phase III trial, from 138 FDA pivotal trials (2015–16).

  - TAG's bedaquiline analysis used 
Sertkaya (2016) estimates, with a Phase III upper bound of US$26.6 million,
 then adjusted downward for lower trial costs in LMICs.
- **I found no actual budgets for Study 31, STREAM, endTB, TRUNCATE-TB or SimpliciTB. UNVERIFIABLE.** The critique already flags its figures as recalled and ungrounded.
- **The counterargument about cheap trials with routine-care endpoints: PLAUSIBLE, with some support.**
  - An EDCTP-funded pragmatic DS-TB trial protocol (NCT05575518) lists 
a grand total of £226,734 in its per-site budget table.

  - The document is ambiguous. The budget is stated for 
a minimal number of 436 patients per site.

  - Pragmatic DS-TB trials can therefore be much cheaper per patient than TB-PRACTECAL. The $20–60M range is probably the upper part of the plausible distribution for this design.
- **Arithmetic: VERIFIED.** $20–60M against $7M is about 2.9–8.6×. 3,050 divided by that gives about 355–1,050. $30M gives about 710.
- **WHO may require subgroup evidence, multiple trials or an IPD meta-analysis: UNVERIFIABLE.** I found no WHO document setting a number-of-trials requirement. The critique concedes this. A 2026 review of host-directed therapy (HDT) says 
moving these agents into standard practice requires large-scale, stratified Phase III trials.
 That loosely supports the stratification point.

**EVIDENCE FOUND**
- TB-PRACTECAL's cost per patient, €61,460, is high because it ran in hospital-based drug-resistant TB settings. Using it for a DS-TB adjunct probably overstates cost.
- The Mullard/JAMA median of $19M comes from FDA-approved pivotal trials, so it is not TB-specific.

**CORE CLAIM**
- **Claim:** A Phase III trial for this intervention would plausibly cost well above $7M, in the range $20–60M.
- **Support: SUPPORTED for the reference class, not for this trial design.**
- **Why:** TB-PRACTECAL and the JAMA/TAG estimates directly show tens of millions per TB Phase III. I found no cost for a cheap DS-TB adjunct trial, and one pragmatic protocol hints at a much lower cost.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The direction (a $7M all-in cost looks low) survives. The specific trial budgets and the WHO multi-trial requirement are unverified.

**REVISED CRITIQUE**
- Documented TB Phase III costs include €33.9M for TB-PRACTECAL (drug-resistant TB) and a general pivotal-trial median of about $19M.
- A $7M all-in budget is below that reference class unless the trial is a cheap pragmatic design with routine-care endpoints.
- A central all-in cost of $15–30M gives SROI of roughly 700–1,400x. This range is my adjustment, wider than the original "about 700x."
- Mark as UNGROUNDED: the claim that WHO requires multiple trials or an IPD meta-analysis, and the budgets of the five named trials.
- Strength: **medium**. Direction: SROI down.

---

## Critique 2: Benefit and cost come from different counterfactuals

**CITATION CHECK**
- The critique cites no external sources. It is an algebraic argument.
- I could not see the CEA or BOTEC, so I cannot confirm the "1 year × plateau deaths" benefit, the 3,050x SROI, the $7M or $6.7M figures, or the 2% case decline. These are **UNVERIFIABLE** from what I was given.

**CLAIM CHECK**
- **Pure delay gives PV_B/PV_C, independent of D: PLAUSIBLE, with a hidden assumption.** I re-derived it. Shifting the whole stream by D scales both PVs by e^(−rD), so the ratio of differences is PV_B/PV_C. For a perpetuity, the benefit lost is about D × one plateau year. That matches the BOTEC's benefit term, so the critique correctly isolates the denominator as the inconsistent part.
- **The assumption: other funders' $6.7M costs the grant only the time value of money, r·D·PV_C.**
  - This holds only if money is valued at the discount rate r.
  - If displaced dollars would fund other TB work at a high cost-effectiveness bar, the cost is not just interest.
  - By my rough calculation, the ratio is then about (1−e^(−rD))·PV_B/PV_C + CE_other·e^(−rD).
  - With D=1 and r=4%, that is about 0.4–0.5× the BOTEC plus CE_other. It could fall at or below the BOTEC unless CE_other is very high.
  - The critique mentions displacement only as a separate issue. It is actually load-bearing for the delay branch.
- **Never branch gives PV_B/PV_C: VERIFIED algebraically.** This depends on the grant being truly decisive and on attributing the whole program's benefit to it.
- **Mixture is the same: VERIFIED algebraically.**
- **Multiplier arithmetic: VERIFIED.** 1/0.06 ≈ 16.7. Times 0.6–0.7 is about 10–11.7. Dividing by 0.85 gives about 12–14. Without the decline, 1/0.04 = 25, which gives about 18–20. 3,050 × 10–18 gives about 30,500–55,000.
- **The 0.6–0.7 "delay factor" and 0.85 "cost-discount adjustment": UNGROUNDED.** They are not derived or sourced. They probably reflect lag before benefits start, but that is not stated.
- **Internal inconsistency:** Estimated Direction is "decreases," yet the critique argues SROI is 10–20× higher. It presumably means "the BOTEC understates SROI," but the label is confusing.

**EVIDENCE FOUND**
- None external. Nothing I found speaks to whether CG's framing was deliberately conservative.

**CORE CLAIM**
- **Claim:** Under every coherent counterfactual the ratio equals PV_B/PV_C, so the BOTEC understates SROI by roughly 10–20×.
- **Support: LOGIC ONLY.**
- **Why:** The algebra holds when other funders' money is valued at the discount rate. It fails if displacement is priced at the funder's opportunity cost, and the multiplier rests on assumed horizon and delay parameters.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The hybrid-counterfactual diagnosis is sound. "Every coherent framing" and the 10–20× multiple are overstated.

**REVISED CRITIQUE**
- The BOTEC pairs a delay-world benefit (one year of plateau deaths averted) with a never-world cost (the full pathway). That is internally inconsistent.
- If other funders' dollars are treated as costing only time value, a consistent framing gives PV_B/PV_C. That is higher than the BOTEC by roughly the number of discounted benefit-years, which is **UNGROUNDED but plausibly about 5–20×** under a finite horizon.
- If displaced funding is valued at CG's own bar, the delay branch could be near or below the BOTEC. Only the never branch reliably raises the ratio.
- Do not report 30,000–55,000x. Report it as a conditional upper scenario.
- Strength: **medium**, not large. Direction: SROI up in the never branch, ambiguous in the delay branch.

---

## Critique 3: "Never" is a live branch for a generic-statin TB program

**CITATION CHECK**
- The critique cites no papers and flags the funder landscape as ungrounded.
- **NIH and Johns Hopkins preclinical and early clinical work: PARTIALLY VERIFIED.**
  - StAT-TB is 
a Phase 2b dose-finding study of pravastatin in adults with TB, sponsored by NIAID. It started in February 2020 and completed in 2022.

  - Preclinical statin mouse work acknowledges 
NIH grant R00 AI114952 and a Bill & Melinda Gates Foundation grant (OPP 1066499).

  - Hopkins affiliation did not appear in the retrieved text.
- **Searches of ClinicalTrials.gov, ICTRP, TAG, EDCTP, Unitaid and RePORTER were not possible with my tools.** The absence of a Phase III statin-TB trial in my results is therefore only weak evidence.

**CLAIM CHECK**
- **Statins are off-patent and have no commercial sponsor: PLAUSIBLE.** This is a general repurposing argument. I did not locate a source for it.
- **Public-health funders have favored novel regimens, shortened regimens and vaccines over HDTs: UNVERIFIABLE.**
  - Gates did fund a four-arm HDT Phase 2 trial. 
It "provided funding for this trial and contributed to the selection of host-directed therapy candidates."
 Statins were not among its four arms.
  - Statins also drew NIH and Gates support at the preclinical stage and NIAID at Phase 2b. Funders have not ignored statins.
- **The grant is the gating event, with dose-finding preceding Phase III: QUESTIONABLE.**
  - StAT-TB, a Phase 2b dose-finding trial, is already completed.
  - A separate rosuvastatin Phase 2b trial reported: 
median time to culture conversion was 42 days in both arms (HR 1.30, 0.88–1.91, p=0.19).
 The authors concluded that 
rosuvastatin 10 mg was safe but did not produce substantive benefits on culture conversion overall.

  - A PET-CT sub-study found 
no impact on PET-CT changes.

  - The critique does not mention this null result. It lowers p_success. It also makes a "never" outcome more likely, but through low prior efficacy rather than lack of funding.
  - Whether the CG Phase IIc is gating depends on the grant's design, which I could not see.
- **Observational support exists.** 
A meta-analysis found statins associated with reduced active TB risk (OR 0.66; 95% CI 0.54–0.81).
 This is observational and confounded.
- **Expected speedup q·H_eff + (1−q)·D exceeds 1 year for q = 0.1–0.2: VERIFIED arithmetically.** For example, 0.1×10 + 0.9×1 = 1.9. The "break-even at q ≈ 0" is loose, because at q=0 with D=0.5 the speedup is below 1.
- **"About 20× higher" SROI: arithmetic VERIFIED, framing problematic.** $7M / $0.32M ≈ 22. But crediting the whole downstream benefit while charging only the grant's cost ignores that the never branch needs the other funders' $6.7M. This contradicts Critique 2, which charges the full cost in that branch.
- **Cross-references to "Critique 1" appear to refer to the speedup critique (Critique 2 here).** The numbering is mismatched.

**EVIDENCE FOUND**
- The negative rosuvastatin Phase 2b is the main added evidence. It weakens efficacy priors and the case for a Phase III.
- A 2026 review says HDT candidates, including statins, still need 
large-scale, stratified Phase III trials.
 That is consistent with the gap the critique describes.
- I found no registered statin-TB Phase III trial in these searches. This is not exhaustive.

**CORE CLAIM**
- **Claim:** The realistic counterfactual for a CG-funded statin Phase IIc has a substantial probability (q about 0.1–0.2 or more) of long delay or never, so expected speedup is above 1 year.
- **Support: LOGIC ONLY.**
- **Why:** The reasoning is coherent and consistent with no Phase III being found. I found no direct evidence on q, and existing NIH, Gates and other Phase 2b statin trials show funding has occurred.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The hypothesis stays as UNGROUNDED but plausible. The gating-event premise and the "20× higher" figure are weakened.

**REVISED CRITIQUE**
- Statin-TB trials have been funded at Phase 2b by NIAID, and a rosuvastatin Phase 2b exists. A Phase III sponsor is plausibly still lacking, but I could not confirm that.
- The speedup is better modeled as a distribution than as a fixed 1 year. This is logic-only and depends on an unestimated q.
- The null rosuvastatin result should lower p_success. That partly offsets any gain from a longer speedup.
- Drop the "SROI about 20× higher" claim. It credits the full downstream benefit against only the grant cost, which conflicts with Critique 2's accounting.
- Strength: **low to medium**. Direction: ambiguous, with up in the never branch and down if p_success falls or the grant is redundant.

--- Critique: The funding landscape for a generic-statin TB program makes "never" a live branch. The speedup is a poor proxy for the grant's real counterfactual. ---

## Critique 1: Reference-class check for TB Phase III trial cost

**CITATION CHECK**
- The critique cites no papers. It names five trials: Study 31/A5349, STREAM, endTB, TRUNCATE-TB and SimpliciTB.
- **Study 31/A5349: VERIFIED.** 
Target enrollment is 2500 participants.
 The record also lists 
TBTC Study 31, ACTG Study A5349
 as the same trial.
- **STREAM: VERIFIED as a Phase III TB trial.** 
The first participant was enrolled in July 2012.
 I did not retrieve its enrollment number.
- **endTB: VERIFIED as a Phase III trial.** 
It is funded by a Unitaid grant.
 I did not retrieve enrollment.
- **TRUNCATE-TB and SimpliciTB: NOT CHECKED.** I found no source for their sizes.
- The "hundreds to thousands" range is plausible but only partly confirmed.

**CLAIM CHECK**
- **TB Phase III budgets are "generally in the tens of millions": PLAUSIBLE, with one direct TB data point.**
  - TB-PRACTECAL is a Phase 2b-3 drug-resistant TB trial. 
Its total cost was €33.9 million, or €61,460 per patient.

  - A TB-specific cost model gives 
a mean of $48.9 million for trials with an active-drug control arm.

  - A systematic review found 
a range of US$7–221 million per Phase 2/3 trial.

  - The general median is 
$19 million for a single Phase III trial, from 138 FDA pivotal trials (2015–16).

  - TAG's bedaquiline analysis used 
Sertkaya (2016) estimates, with a Phase III upper bound of US$26.6 million,
 then adjusted downward for lower trial costs in LMICs.
- **I found no actual budgets for Study 31, STREAM, endTB, TRUNCATE-TB or SimpliciTB. UNVERIFIABLE.** The critique already flags its figures as recalled and ungrounded.
- **The counterargument about cheap trials with routine-care endpoints: PLAUSIBLE, with some support.**
  - An EDCTP-funded pragmatic DS-TB trial protocol (NCT05575518) lists 
a grand total of £226,734 in its per-site budget table.

  - The document is ambiguous. The budget is stated for 
a minimal number of 436 patients per site.

  - Pragmatic DS-TB trials can therefore be much cheaper per patient than TB-PRACTECAL. The $20–60M range is probably the upper part of the plausible distribution for this design.
- **Arithmetic: VERIFIED.** $20–60M against $7M is about 2.9–8.6×. 3,050 divided by that gives about 355–1,050. $30M gives about 710.
- **WHO may require subgroup evidence, multiple trials or an IPD meta-analysis: UNVERIFIABLE.** I found no WHO document setting a number-of-trials requirement. The critique concedes this. A 2026 review of host-directed therapy (HDT) says 
moving these agents into standard practice requires large-scale, stratified Phase III trials.
 That loosely supports the stratification point.

**EVIDENCE FOUND**
- TB-PRACTECAL's cost per patient, €61,460, is high because it ran in hospital-based drug-resistant TB settings. Using it for a DS-TB adjunct probably overstates cost.
- The Mullard/JAMA median of $19M comes from FDA-approved pivotal trials, so it is not TB-specific.

**CORE CLAIM**
- **Claim:** A Phase III trial for this intervention would plausibly cost well above $7M, in the range $20–60M.
- **Support: SUPPORTED for the reference class, not for this trial design.**
- **Why:** TB-PRACTECAL and the JAMA/TAG estimates directly show tens of millions per TB Phase III. I found no cost for a cheap DS-TB adjunct trial, and one pragmatic protocol hints at a much lower cost.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The direction (a $7M all-in cost looks low) survives. The specific trial budgets and the WHO multi-trial requirement are unverified.

**REVISED CRITIQUE**
- Documented TB Phase III costs include €33.9M for TB-PRACTECAL (drug-resistant TB) and a general pivotal-trial median of about $19M.
- A $7M all-in budget is below that reference class unless the trial is a cheap pragmatic design with routine-care endpoints.
- A central all-in cost of $15–30M gives SROI of roughly 700–1,400x. This range is my adjustment, wider than the original "about 700x."
- Mark as UNGROUNDED: the claim that WHO requires multiple trials or an IPD meta-analysis, and the budgets of the five named trials.
- Strength: **medium**. Direction: SROI down.

---

## Critique 2: Benefit and cost come from different counterfactuals

**CITATION CHECK**
- The critique cites no external sources. It is an algebraic argument.
- I could not see the CEA or BOTEC, so I cannot confirm the "1 year × plateau deaths" benefit, the 3,050x SROI, the $7M or $6.7M figures, or the 2% case decline. These are **UNVERIFIABLE** from what I was given.

**CLAIM CHECK**
- **Pure delay gives PV_B/PV_C, independent of D: PLAUSIBLE, with a hidden assumption.** I re-derived it. Shifting the whole stream by D scales both PVs by e^(−rD), so the ratio of differences is PV_B/PV_C. For a perpetuity, the benefit lost is about D × one plateau year. That matches the BOTEC's benefit term, so the critique correctly isolates the denominator as the inconsistent part.
- **The assumption: other funders' $6.7M costs the grant only the time value of money, r·D·PV_C.**
  - This holds only if money is valued at the discount rate r.
  - If displaced dollars would fund other TB work at a high cost-effectiveness bar, the cost is not just interest.
  - By my rough calculation, the ratio is then about (1−e^(−rD))·PV_B/PV_C + CE_other·e^(−rD).
  - With D=1 and r=4%, that is about 0.4–0.5× the BOTEC plus CE_other. It could fall at or below the BOTEC unless CE_other is very high.
  - The critique mentions displacement only as a separate issue. It is actually load-bearing for the delay branch.
- **Never branch gives PV_B/PV_C: VERIFIED algebraically.** This depends on the grant being truly decisive and on attributing the whole program's benefit to it.
- **Mixture is the same: VERIFIED algebraically.**
- **Multiplier arithmetic: VERIFIED.** 1/0.06 ≈ 16.7. Times 0.6–0.7 is about 10–11.7. Dividing by 0.85 gives about 12–14. Without the decline, 1/0.04 = 25, which gives about 18–20. 3,050 × 10–18 gives about 30,500–55,000.
- **The 0.6–0.7 "delay factor" and 0.85 "cost-discount adjustment": UNGROUNDED.** They are not derived or sourced. They probably reflect lag before benefits start, but that is not stated.
- **Internal inconsistency:** Estimated Direction is "decreases," yet the critique argues SROI is 10–20× higher. It presumably means "the BOTEC understates SROI," but the label is confusing.

**EVIDENCE FOUND**
- None external. Nothing I found speaks to whether CG's framing was deliberately conservative.

**CORE CLAIM**
- **Claim:** Under every coherent counterfactual the ratio equals PV_B/PV_C, so the BOTEC understates SROI by roughly 10–20×.
- **Support: LOGIC ONLY.**
- **Why:** The algebra holds when other funders' money is valued at the discount rate. It fails if displacement is priced at the funder's opportunity cost, and the multiplier rests on assumed horizon and delay parameters.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The hybrid-counterfactual diagnosis is sound. "Every coherent framing" and the 10–20× multiple are overstated.

**REVISED CRITIQUE**
- The BOTEC pairs a delay-world benefit (one year of plateau deaths averted) with a never-world cost (the full pathway). That is internally inconsistent.
- If other funders' dollars are treated as costing only time value, a consistent framing gives PV_B/PV_C. That is higher than the BOTEC by roughly the number of discounted benefit-years, which is **UNGROUNDED but plausibly about 5–20×** under a finite horizon.
- If displaced funding is valued at CG's own bar, the delay branch could be near or below the BOTEC. Only the never branch reliably raises the ratio.
- Do not report 30,000–55,000x. Report it as a conditional upper scenario.
- Strength: **medium**, not large. Direction: SROI up in the never branch, ambiguous in the delay branch.

---

## Critique 3: "Never" is a live branch for a generic-statin TB program

**CITATION CHECK**
- The critique cites no papers and flags the funder landscape as ungrounded.
- **NIH and Johns Hopkins preclinical and early clinical work: PARTIALLY VERIFIED.**
  - StAT-TB is 
a Phase 2b dose-finding study of pravastatin in adults with TB, sponsored by NIAID. It started in February 2020 and completed in 2022.

  - Preclinical statin mouse work acknowledges 
NIH grant R00 AI114952 and a Bill & Melinda Gates Foundation grant (OPP 1066499).

  - Hopkins affiliation did not appear in the retrieved text.
- **Searches of ClinicalTrials.gov, ICTRP, TAG, EDCTP, Unitaid and RePORTER were not possible with my tools.** The absence of a Phase III statin-TB trial in my results is therefore only weak evidence.

**CLAIM CHECK**
- **Statins are off-patent and have no commercial sponsor: PLAUSIBLE.** This is a general repurposing argument. I did not locate a source for it.
- **Public-health funders have favored novel regimens, shortened regimens and vaccines over HDTs: UNVERIFIABLE.**
  - Gates did fund a four-arm HDT Phase 2 trial. 
It "provided funding for this trial and contributed to the selection of host-directed therapy candidates."
 Statins were not among its four arms.
  - Statins also drew NIH and Gates support at the preclinical stage and NIAID at Phase 2b. Funders have not ignored statins.
- **The grant is the gating event, with dose-finding preceding Phase III: QUESTIONABLE.**
  - StAT-TB, a Phase 2b dose-finding trial, is already completed.
  - A separate rosuvastatin Phase 2b trial reported: 
median time to culture conversion was 42 days in both arms (HR 1.30, 0.88–1.91, p=0.19).
 The authors concluded that 
rosuvastatin 10 mg was safe but did not produce substantive benefits on culture conversion overall.

  - A PET-CT sub-study found 
no impact on PET-CT changes.

  - The critique does not mention this null result. It lowers p_success. It also makes a "never" outcome more likely, but through low prior efficacy rather than lack of funding.
  - Whether the CG Phase IIc is gating depends on the grant's design, which I could not see.
- **Observational support exists.** 
A meta-analysis found statins associated with reduced active TB risk (OR 0.66; 95% CI 0.54–0.81).
 This is observational and confounded.
- **Expected speedup q·H_eff + (1−q)·D exceeds 1 year for q = 0.1–0.2: VERIFIED arithmetically.** For example, 0.1×10 + 0.9×1 = 1.9. The "break-even at q ≈ 0" is loose, because at q=0 with D=0.5 the speedup is below 1.
- **"About 20× higher" SROI: arithmetic VERIFIED, framing problematic.** $7M / $0.32M ≈ 22. But crediting the whole downstream benefit while charging only the grant's cost ignores that the never branch needs the other funders' $6.7M. This contradicts Critique 2, which charges the full cost in that branch.
- **Cross-references to "Critique 1" appear to refer to the speedup critique (Critique 2 here).** The numbering is mismatched.

**EVIDENCE FOUND**
- The negative rosuvastatin Phase 2b is the main added evidence. It weakens efficacy priors and the case for a Phase III.
- A 2026 review says HDT candidates, including statins, still need 
large-scale, stratified Phase III trials.
 That is consistent with the gap the critique describes.
- I found no registered statin-TB Phase III trial in these searches. This is not exhaustive.

**CORE CLAIM**
- **Claim:** The realistic counterfactual for a CG-funded statin Phase IIc has a substantial probability (q about 0.1–0.2 or more) of long delay or never, so expected speedup is above 1 year.
- **Support: LOGIC ONLY.**
- **Why:** The reasoning is coherent and consistent with no Phase III being found. I found no direct evidence on q, and existing NIH, Gates and other Phase 2b statin trials show funding has occurred.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The hypothesis stays as UNGROUNDED but plausible. The gating-event premise and the "20× higher" figure are weakened.

**REVISED CRITIQUE**
- Statin-TB trials have been funded at Phase 2b by NIAID, and a rosuvastatin Phase 2b exists. A Phase III sponsor is plausibly still lacking, but I could not confirm that.
- The speedup is better modeled as a distribution than as a fixed 1 year. This is logic-only and depends on an unestimated q.
- The null rosuvastatin result should lower p_success. That partly offsets any gain from a longer speedup.
- Drop the "SROI about 20× higher" claim. It credits the full downstream benefit against only the grant cost, which conflicts with Critique 2's accounting.
- Strength: **low to medium**. Direction: ambiguous, with up in the never branch and down if p_success falls or the grant is redundant.

--- Critique: Discounting quantified properly with an S-curve ramp and discounted costs. The net effect is about −20% to −31%, not the benefit-only −21% to −35%. ---

## Critique 1: Discounting with an S-curve ramp and discounted costs (net about −20% to −31%)

**CITATION CHECK**
- No papers are cited. The Investigator names "How we use BOTECs" (May 2025) and GiveWell's 4% rate as things to check.
  - "How we use BOTECs": NOT FOUND. My search returned only irrelevant results.
  - GiveWell's ~4% rate: UNVERIFIABLE. My searches returned no GiveWell or Coefficient Giving (CG) source. The general literature does not settle the question. 
Global health evaluations typically apply a 3% discount rate to health outcomes and costs.
 
One paper argues for at least 5% in low- and lower-middle-income countries.
 The 3–5% range is therefore reasonable, but it is not tied to CG.

**CLAIM CHECK**
- Benefit factors of 0.71 / 0.63 / 0.57 (T0 = 8.5, L = 6, linear ramp): **VERIFIED**.
  - I recomputed the formula e^(−rT0)(1−e^(−rL))/(rL) and got 0.709, 0.633 and 0.565.
- Flat 8.5-year factors of 0.77 / 0.71 / 0.65: **VERIFIED** (0.775, 0.712, 0.654).
- All-in cost factors of 0.88 / 0.85 / 0.82: **VERIFIED**.
  - This assumes $0.32M at t=0 and $6.7M spread uniformly over years 1–8.
  - I got 0.881, 0.845 and 0.812, so the 5% figure is closer to 0.81.
- Net factors of 0.80 / 0.73 / 0.69, i.e. −20% / −27% / −31%: **MOSTLY VERIFIED**.
  - The 4% figure mixes two benefit factors. It uses 0.62 (the "exact" version) rather than the 0.633 from the stated formula.
  - With 0.633 the 4% net factor is about 0.75, which is −25%.
  - The cleaner statement is "about −20% / −25 to −27% / −31%".
- The back-calculated base SROI of about 3,050x is consistent across the three rows (2,440/0.80, 2,230/0.73, 2,100/0.69). That at least makes the table internally coherent.
- The "one-year shift" approximation is **PLAUSIBLE but approximate**.
  - Shifting a ramp-to-plateau curve earlier by one year yields a bump of the difference B(t)−B(t−1). That bump spans [T0, T0+L+1] with mass 1.
  - The formula uses support [T0, T0+L] instead. The exact 4% factor is about 0.62, so the error is small.
- Directional logic (a benefit-only discount overstates the penalty when costs also fall earlier): **VERIFIED**, and standard. 
Health effects valued in monetary terms, as in cost-benefit analysis, should be discounted at the same rate as costs.

- "Conflict with Critique 1": **ERROR**. This is Critique 1, so the cross-reference is wrong or garbled. The "(Critique 4)" reference points to a critique I wasn't given.
- A 25% materiality line and a ~2,000x bar: **UNVERIFIABLE**. The Investigator said so too.
- The claim that the ramp and cost timing are illustrative: honest. T0 = 8.5, L = 6, and costs uniform over years 1–8 are all assumed.

**EVIDENCE FOUND**
- I found no CG or GiveWell rule on discounting R&D BOTECs.
- Sensitivity to ramp length is mathematically correct. For L = 10 at 4%, the formula gives e^(−0.34)·(1−e^(−0.4))/0.4 ≈ 0.712 × 0.824 ≈ 0.59. The Investigator said ~0.57, which is close.

**CORE CLAIM**
- Claim: Consistent discounting of costs and benefits gives a net penalty of about 20–31%, smaller than the benefit-only penalty of 21–35%.
- Support: **LOGIC ONLY**
- Why: The arithmetic checks out and the principle is standard, but the inputs (T0, L, cost timing) are unsourced assumptions and CG's actual convention is unknown.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The arithmetic and the "discount costs too" logic survive. The specific percentages depend on assumed timing. The cross-reference to "Critique 1" is erroneous. Whether CG discounts at all is unverified.

**REVISED CRITIQUE**
- If benefits are discounted, costs should be discounted consistently.
- Under illustrative timing (ramp starting at about year 8.5, 6-year linear ramp, costs spread over years 1–8), the net discount penalty is about −20% at 3%, −25 to −27% at 4%, and −31% at 5%.
- This is smaller than the benefit-only penalty.
- Flag these as sensitive to the CEA's real timeline.
- Remove the claim about CG/GiveWell conventions and the "conflict with Critique 1" sentence.
- Strength: **medium-low**. It is a second-order refinement, and the Investigator concedes this.

---

## Critique 2: Asymmetric probability weighting of benefit and cost

**CITATION CHECK**
- No citations. The critique is explicitly "UNGROUNDED" and "logical argument."

**CLAIM CHECK**
- Expected cost = $0.32M + s × $6.7M: **VERIFIED as arithmetic**.
  - s = 0.6 gives $4.34M, so SROI rises by about 1.62x (7.02/4.34).
  - s = 0.4 gives $3.0M, so SROI rises by about 2.34x.
  - These match the stated 1.6x and 2.3x.
- "The $7M is a nominal sum of all stages": **UNVERIFIABLE**. I don't have the CEA cells, and the critique itself says the point fails if the $7M is already an expected value.
- Counterpoint that s lies between p_success and 1 because late-stage failures still incur most of the cost: **LOGICALLY CORRECT**. If p_success is the product of per-stage probabilities, s for Phase III spend equals the probability of passing the earlier stage, which is at least 0.40. Whether s is closer to 0.4 or 1 depends on where the attrition occurs.
- A "double penalty": **PLAUSIBLE**. It is a real methodological inconsistency if costs are unweighted. Matching expected benefits to expected costs is standard. It is only a "penalty" in the sense of an understated SROI.

**EVIDENCE FOUND**
- I searched for nothing specific on how CG built the $7M, and no result addressed it.
- Context: other parties often fund the downstream spend (Phase III, implementation). Whether that spend belongs in CG's cost denominator at all is a separate counterfactual-attribution question. That could shrink the denominator further, or make the whole gating argument moot.

**CORE CLAIM**
- Claim: The $7M denominator is a nominal, unweighted sum of gated stage costs, while the benefit carries p = 0.40.
- Support: **LOGIC ONLY**
- Why: The mechanism is sound, but I found no evidence on how the CEA constructed the cost, and the critique is conditional on it.

**OVERALL VERDICT: UNVERIFIABLE.** The hypothesis is logically sound, with correct arithmetic and no fabricated evidence. Retain it as a flagged hypothesis marked "UNGROUNDED — plausible but needs empirical support." It should be checked against the CEA's cost cells before use. If the $7M is nominal, the direction is up, with a magnitude of roughly 1.2–2.3x depending on s.

---

## Critique 3: A 1-year trial speedup is not necessarily a 1-year adoption speedup

**CITATION CHECK**
- Study 31/A5349 and BPaLM were named only as case studies. Both exist and the Investigator's characterisation is generally fair.
  - Study 31 is VERIFIED. It was a 
randomized, multi-national, open-label, controlled phase 3 trial comparing two 4-month rifapentine-containing regimens to the standard 6-month control.

  - BPaLM was based on TB-PRACTECAL and ZeNix. VERIFIED.

**CLAIM CHECK**
- WHO uses a GDG process to change TB guidelines: **VERIFIED**. 
In 2021, the WHO Global TB Programme received data from the Study 31 investigators and convened a Guideline Development Group to review results.

- "WHO guideline updates occur on a roughly fixed schedule": **NOT SUPPORTED, and partly CONTRADICTED by these two cases**. GDGs appear to be convened ad hoc when data arrive.
  - Study 31: 
results were presented at the 51st virtual Union World Conference in October 2020
. 
The GDG met virtually from 27–30 April 2021.
 
Detailed results were published on 6 May 2021.
 
WHO then issued a rapid communication in June 2021
. The lag from conference presentation to rapid communication was about 8 months, and from the NEJM paper about 5–6 weeks.
  - BPaLM: 
WHO convened a GDG in February–March 2022 after the TB-PRACTECAL and ZeNix results.
 
A rapid communication followed in May 2022.
 The full guideline update was published later in the year (the Lancet Respiratory Medicine page lists Dec 15, 2022).
  - A WHO "rapid communication" route exists, which weakens the idea of a fixed window with a 2+ year miss penalty. I found no evidence supporting the "2+ years" cycle claim.
- Trial results are not the only binding constraint on uptake: **SUPPORTED**. WHO said 
implementation and uptake of the new regimen in the short to medium term will be more feasible if the cost of rifapentine is reduced and availability improved.
 The same communication flagged 
a need for rigorous antibacterial stewardship because the regimen contains moxifloxacin.
 This supports the "speedup less than one year" direction through downstream bottlenecks (price, supply, national adoption). It does not support the lumpy "WHO-window" mechanism.
- A public call for data and national policy/procurement lags: **PLAUSIBLE, not checked**.
- "Materiality threshold of about 0.65 years" and "speedup_years linear in SROI": **UNVERIFIABLE** without the CEA. Linearity follows from the stated structure.

**EVIDENCE FOUND**
- Both case studies show a short gap between pivotal data and WHO guidance (months, not years). Real WHO timing therefore looks more responsive than the critique assumes.
- I did not find data on national adoption lags, which is where slack-absorption would most plausibly occur.
- Direction: the evidence points more toward "less than one year" through downstream bottlenecks than toward "more than one year" through missed guideline windows.

**CORE CLAIM**
- Claim: The trial is not the sole binding constraint, so a 1-year trial speedup need not translate into a 1-year adoption speedup, and the effective speedup is a lumpy random variable.
- Support: **LOGIC ONLY** for the general point, with partial direct support for non-trial bottlenecks (price, availability).
- Why: Downstream constraints are documented, but the specific "fixed WHO schedule, missed-window" mechanism is not supported by the two cases I checked.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The core concern, that speedup is not a pure translation of the adoption curve, is sound and partly supported. The "roughly fixed WHO guideline schedule" and "lose a full 2+ year cycle" mechanisms are unsupported, and the TB cases lean against them.

**REVISED CRITIQUE**
- The model's assumption that a 1-year trial speedup gives a 1-year adoption speedup is untested.
- Adoption also depends on national policy change, procurement and drug price/availability (documented for rifapentine), so the effective speedup could be below 1 year.
- WHO's guideline step in recent TB cases (Study 31, BPaLM) was ad hoc and fast (months), so the upside "missed window" scenario is weakly supported.
- Direction: **leaning down or uncertain**, rather than symmetric.
- Magnitude: medium, and sensitivity analysis is needed.
- Flag as UNGROUNDED for national-level lags.
- Remove the "fixed schedule" and "2+ year cycle" claims.

--- Critique: Probability weighting is asymmetric between benefit and cost. ---

## Critique 1: Discounting with an S-curve ramp and discounted costs (net about −20% to −31%)

**CITATION CHECK**
- No papers are cited. The Investigator names "How we use BOTECs" (May 2025) and GiveWell's 4% rate as things to check.
  - "How we use BOTECs": NOT FOUND. My search returned only irrelevant results.
  - GiveWell's ~4% rate: UNVERIFIABLE. My searches returned no GiveWell or Coefficient Giving (CG) source. The general literature does not settle the question. 
Global health evaluations typically apply a 3% discount rate to health outcomes and costs.
 
One paper argues for at least 5% in low- and lower-middle-income countries.
 The 3–5% range is therefore reasonable, but it is not tied to CG.

**CLAIM CHECK**
- Benefit factors of 0.71 / 0.63 / 0.57 (T0 = 8.5, L = 6, linear ramp): **VERIFIED**.
  - I recomputed the formula e^(−rT0)(1−e^(−rL))/(rL) and got 0.709, 0.633 and 0.565.
- Flat 8.5-year factors of 0.77 / 0.71 / 0.65: **VERIFIED** (0.775, 0.712, 0.654).
- All-in cost factors of 0.88 / 0.85 / 0.82: **VERIFIED**.
  - This assumes $0.32M at t=0 and $6.7M spread uniformly over years 1–8.
  - I got 0.881, 0.845 and 0.812, so the 5% figure is closer to 0.81.
- Net factors of 0.80 / 0.73 / 0.69, i.e. −20% / −27% / −31%: **MOSTLY VERIFIED**.
  - The 4% figure mixes two benefit factors. It uses 0.62 (the "exact" version) rather than the 0.633 from the stated formula.
  - With 0.633 the 4% net factor is about 0.75, which is −25%.
  - The cleaner statement is "about −20% / −25 to −27% / −31%".
- The back-calculated base SROI of about 3,050x is consistent across the three rows (2,440/0.80, 2,230/0.73, 2,100/0.69). That at least makes the table internally coherent.
- The "one-year shift" approximation is **PLAUSIBLE but approximate**.
  - Shifting a ramp-to-plateau curve earlier by one year yields a bump of the difference B(t)−B(t−1). That bump spans [T0, T0+L+1] with mass 1.
  - The formula uses support [T0, T0+L] instead. The exact 4% factor is about 0.62, so the error is small.
- Directional logic (a benefit-only discount overstates the penalty when costs also fall earlier): **VERIFIED**, and standard. 
Health effects valued in monetary terms, as in cost-benefit analysis, should be discounted at the same rate as costs.

- "Conflict with Critique 1": **ERROR**. This is Critique 1, so the cross-reference is wrong or garbled. The "(Critique 4)" reference points to a critique I wasn't given.
- A 25% materiality line and a ~2,000x bar: **UNVERIFIABLE**. The Investigator said so too.
- The claim that the ramp and cost timing are illustrative: honest. T0 = 8.5, L = 6, and costs uniform over years 1–8 are all assumed.

**EVIDENCE FOUND**
- I found no CG or GiveWell rule on discounting R&D BOTECs.
- Sensitivity to ramp length is mathematically correct. For L = 10 at 4%, the formula gives e^(−0.34)·(1−e^(−0.4))/0.4 ≈ 0.712 × 0.824 ≈ 0.59. The Investigator said ~0.57, which is close.

**CORE CLAIM**
- Claim: Consistent discounting of costs and benefits gives a net penalty of about 20–31%, smaller than the benefit-only penalty of 21–35%.
- Support: **LOGIC ONLY**
- Why: The arithmetic checks out and the principle is standard, but the inputs (T0, L, cost timing) are unsourced assumptions and CG's actual convention is unknown.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The arithmetic and the "discount costs too" logic survive. The specific percentages depend on assumed timing. The cross-reference to "Critique 1" is erroneous. Whether CG discounts at all is unverified.

**REVISED CRITIQUE**
- If benefits are discounted, costs should be discounted consistently.
- Under illustrative timing (ramp starting at about year 8.5, 6-year linear ramp, costs spread over years 1–8), the net discount penalty is about −20% at 3%, −25 to −27% at 4%, and −31% at 5%.
- This is smaller than the benefit-only penalty.
- Flag these as sensitive to the CEA's real timeline.
- Remove the claim about CG/GiveWell conventions and the "conflict with Critique 1" sentence.
- Strength: **medium-low**. It is a second-order refinement, and the Investigator concedes this.

---

## Critique 2: Asymmetric probability weighting of benefit and cost

**CITATION CHECK**
- No citations. The critique is explicitly "UNGROUNDED" and "logical argument."

**CLAIM CHECK**
- Expected cost = $0.32M + s × $6.7M: **VERIFIED as arithmetic**.
  - s = 0.6 gives $4.34M, so SROI rises by about 1.62x (7.02/4.34).
  - s = 0.4 gives $3.0M, so SROI rises by about 2.34x.
  - These match the stated 1.6x and 2.3x.
- "The $7M is a nominal sum of all stages": **UNVERIFIABLE**. I don't have the CEA cells, and the critique itself says the point fails if the $7M is already an expected value.
- Counterpoint that s lies between p_success and 1 because late-stage failures still incur most of the cost: **LOGICALLY CORRECT**. If p_success is the product of per-stage probabilities, s for Phase III spend equals the probability of passing the earlier stage, which is at least 0.40. Whether s is closer to 0.4 or 1 depends on where the attrition occurs.
- A "double penalty": **PLAUSIBLE**. It is a real methodological inconsistency if costs are unweighted. Matching expected benefits to expected costs is standard. It is only a "penalty" in the sense of an understated SROI.

**EVIDENCE FOUND**
- I searched for nothing specific on how CG built the $7M, and no result addressed it.
- Context: other parties often fund the downstream spend (Phase III, implementation). Whether that spend belongs in CG's cost denominator at all is a separate counterfactual-attribution question. That could shrink the denominator further, or make the whole gating argument moot.

**CORE CLAIM**
- Claim: The $7M denominator is a nominal, unweighted sum of gated stage costs, while the benefit carries p = 0.40.
- Support: **LOGIC ONLY**
- Why: The mechanism is sound, but I found no evidence on how the CEA constructed the cost, and the critique is conditional on it.

**OVERALL VERDICT: UNVERIFIABLE.** The hypothesis is logically sound, with correct arithmetic and no fabricated evidence. Retain it as a flagged hypothesis marked "UNGROUNDED — plausible but needs empirical support." It should be checked against the CEA's cost cells before use. If the $7M is nominal, the direction is up, with a magnitude of roughly 1.2–2.3x depending on s.

---

## Critique 3: A 1-year trial speedup is not necessarily a 1-year adoption speedup

**CITATION CHECK**
- Study 31/A5349 and BPaLM were named only as case studies. Both exist and the Investigator's characterisation is generally fair.
  - Study 31 is VERIFIED. It was a 
randomized, multi-national, open-label, controlled phase 3 trial comparing two 4-month rifapentine-containing regimens to the standard 6-month control.

  - BPaLM was based on TB-PRACTECAL and ZeNix. VERIFIED.

**CLAIM CHECK**
- WHO uses a GDG process to change TB guidelines: **VERIFIED**. 
In 2021, the WHO Global TB Programme received data from the Study 31 investigators and convened a Guideline Development Group to review results.

- "WHO guideline updates occur on a roughly fixed schedule": **NOT SUPPORTED, and partly CONTRADICTED by these two cases**. GDGs appear to be convened ad hoc when data arrive.
  - Study 31: 
results were presented at the 51st virtual Union World Conference in October 2020
. 
The GDG met virtually from 27–30 April 2021.
 
Detailed results were published on 6 May 2021.
 
WHO then issued a rapid communication in June 2021
. The lag from conference presentation to rapid communication was about 8 months, and from the NEJM paper about 5–6 weeks.
  - BPaLM: 
WHO convened a GDG in February–March 2022 after the TB-PRACTECAL and ZeNix results.
 
A rapid communication followed in May 2022.
 The full guideline update was published later in the year (the Lancet Respiratory Medicine page lists Dec 15, 2022).
  - A WHO "rapid communication" route exists, which weakens the idea of a fixed window with a 2+ year miss penalty. I found no evidence supporting the "2+ years" cycle claim.
- Trial results are not the only binding constraint on uptake: **SUPPORTED**. WHO said 
implementation and uptake of the new regimen in the short to medium term will be more feasible if the cost of rifapentine is reduced and availability improved.
 The same communication flagged 
a need for rigorous antibacterial stewardship because the regimen contains moxifloxacin.
 This supports the "speedup less than one year" direction through downstream bottlenecks (price, supply, national adoption). It does not support the lumpy "WHO-window" mechanism.
- A public call for data and national policy/procurement lags: **PLAUSIBLE, not checked**.
- "Materiality threshold of about 0.65 years" and "speedup_years linear in SROI": **UNVERIFIABLE** without the CEA. Linearity follows from the stated structure.

**EVIDENCE FOUND**
- Both case studies show a short gap between pivotal data and WHO guidance (months, not years). Real WHO timing therefore looks more responsive than the critique assumes.
- I did not find data on national adoption lags, which is where slack-absorption would most plausibly occur.
- Direction: the evidence points more toward "less than one year" through downstream bottlenecks than toward "more than one year" through missed guideline windows.

**CORE CLAIM**
- Claim: The trial is not the sole binding constraint, so a 1-year trial speedup need not translate into a 1-year adoption speedup, and the effective speedup is a lumpy random variable.
- Support: **LOGIC ONLY** for the general point, with partial direct support for non-trial bottlenecks (price, availability).
- Why: Downstream constraints are documented, but the specific "fixed WHO schedule, missed-window" mechanism is not supported by the two cases I checked.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The core concern, that speedup is not a pure translation of the adoption curve, is sound and partly supported. The "roughly fixed WHO guideline schedule" and "lose a full 2+ year cycle" mechanisms are unsupported, and the TB cases lean against them.

**REVISED CRITIQUE**
- The model's assumption that a 1-year trial speedup gives a 1-year adoption speedup is untested.
- Adoption also depends on national policy change, procurement and drug price/availability (documented for rifapentine), so the effective speedup could be below 1 year.
- WHO's guideline step in recent TB cases (Study 31, BPaLM) was ad hoc and fast (months), so the upside "missed window" scenario is weakly supported.
- Direction: **leaning down or uncertain**, rather than symmetric.
- Magnitude: medium, and sensitivity analysis is needed.
- Flag as UNGROUNDED for national-level lags.
- Remove the "fixed schedule" and "2+ year cycle" claims.

--- Critique: A 1-year speedup of trial results does not necessarily become a 1-year speedup of adoption, in either direction. ---

## Critique 1: Discounting with an S-curve ramp and discounted costs (net about −20% to −31%)

**CITATION CHECK**
- No papers are cited. The Investigator names "How we use BOTECs" (May 2025) and GiveWell's 4% rate as things to check.
  - "How we use BOTECs": NOT FOUND. My search returned only irrelevant results.
  - GiveWell's ~4% rate: UNVERIFIABLE. My searches returned no GiveWell or Coefficient Giving (CG) source. The general literature does not settle the question. 
Global health evaluations typically apply a 3% discount rate to health outcomes and costs.
 
One paper argues for at least 5% in low- and lower-middle-income countries.
 The 3–5% range is therefore reasonable, but it is not tied to CG.

**CLAIM CHECK**
- Benefit factors of 0.71 / 0.63 / 0.57 (T0 = 8.5, L = 6, linear ramp): **VERIFIED**.
  - I recomputed the formula e^(−rT0)(1−e^(−rL))/(rL) and got 0.709, 0.633 and 0.565.
- Flat 8.5-year factors of 0.77 / 0.71 / 0.65: **VERIFIED** (0.775, 0.712, 0.654).
- All-in cost factors of 0.88 / 0.85 / 0.82: **VERIFIED**.
  - This assumes $0.32M at t=0 and $6.7M spread uniformly over years 1–8.
  - I got 0.881, 0.845 and 0.812, so the 5% figure is closer to 0.81.
- Net factors of 0.80 / 0.73 / 0.69, i.e. −20% / −27% / −31%: **MOSTLY VERIFIED**.
  - The 4% figure mixes two benefit factors. It uses 0.62 (the "exact" version) rather than the 0.633 from the stated formula.
  - With 0.633 the 4% net factor is about 0.75, which is −25%.
  - The cleaner statement is "about −20% / −25 to −27% / −31%".
- The back-calculated base SROI of about 3,050x is consistent across the three rows (2,440/0.80, 2,230/0.73, 2,100/0.69). That at least makes the table internally coherent.
- The "one-year shift" approximation is **PLAUSIBLE but approximate**.
  - Shifting a ramp-to-plateau curve earlier by one year yields a bump of the difference B(t)−B(t−1). That bump spans [T0, T0+L+1] with mass 1.
  - The formula uses support [T0, T0+L] instead. The exact 4% factor is about 0.62, so the error is small.
- Directional logic (a benefit-only discount overstates the penalty when costs also fall earlier): **VERIFIED**, and standard. 
Health effects valued in monetary terms, as in cost-benefit analysis, should be discounted at the same rate as costs.

- "Conflict with Critique 1": **ERROR**. This is Critique 1, so the cross-reference is wrong or garbled. The "(Critique 4)" reference points to a critique I wasn't given.
- A 25% materiality line and a ~2,000x bar: **UNVERIFIABLE**. The Investigator said so too.
- The claim that the ramp and cost timing are illustrative: honest. T0 = 8.5, L = 6, and costs uniform over years 1–8 are all assumed.

**EVIDENCE FOUND**
- I found no CG or GiveWell rule on discounting R&D BOTECs.
- Sensitivity to ramp length is mathematically correct. For L = 10 at 4%, the formula gives e^(−0.34)·(1−e^(−0.4))/0.4 ≈ 0.712 × 0.824 ≈ 0.59. The Investigator said ~0.57, which is close.

**CORE CLAIM**
- Claim: Consistent discounting of costs and benefits gives a net penalty of about 20–31%, smaller than the benefit-only penalty of 21–35%.
- Support: **LOGIC ONLY**
- Why: The arithmetic checks out and the principle is standard, but the inputs (T0, L, cost timing) are unsourced assumptions and CG's actual convention is unknown.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The arithmetic and the "discount costs too" logic survive. The specific percentages depend on assumed timing. The cross-reference to "Critique 1" is erroneous. Whether CG discounts at all is unverified.

**REVISED CRITIQUE**
- If benefits are discounted, costs should be discounted consistently.
- Under illustrative timing (ramp starting at about year 8.5, 6-year linear ramp, costs spread over years 1–8), the net discount penalty is about −20% at 3%, −25 to −27% at 4%, and −31% at 5%.
- This is smaller than the benefit-only penalty.
- Flag these as sensitive to the CEA's real timeline.
- Remove the claim about CG/GiveWell conventions and the "conflict with Critique 1" sentence.
- Strength: **medium-low**. It is a second-order refinement, and the Investigator concedes this.

---

## Critique 2: Asymmetric probability weighting of benefit and cost

**CITATION CHECK**
- No citations. The critique is explicitly "UNGROUNDED" and "logical argument."

**CLAIM CHECK**
- Expected cost = $0.32M + s × $6.7M: **VERIFIED as arithmetic**.
  - s = 0.6 gives $4.34M, so SROI rises by about 1.62x (7.02/4.34).
  - s = 0.4 gives $3.0M, so SROI rises by about 2.34x.
  - These match the stated 1.6x and 2.3x.
- "The $7M is a nominal sum of all stages": **UNVERIFIABLE**. I don't have the CEA cells, and the critique itself says the point fails if the $7M is already an expected value.
- Counterpoint that s lies between p_success and 1 because late-stage failures still incur most of the cost: **LOGICALLY CORRECT**. If p_success is the product of per-stage probabilities, s for Phase III spend equals the probability of passing the earlier stage, which is at least 0.40. Whether s is closer to 0.4 or 1 depends on where the attrition occurs.
- A "double penalty": **PLAUSIBLE**. It is a real methodological inconsistency if costs are unweighted. Matching expected benefits to expected costs is standard. It is only a "penalty" in the sense of an understated SROI.

**EVIDENCE FOUND**
- I searched for nothing specific on how CG built the $7M, and no result addressed it.
- Context: other parties often fund the downstream spend (Phase III, implementation). Whether that spend belongs in CG's cost denominator at all is a separate counterfactual-attribution question. That could shrink the denominator further, or make the whole gating argument moot.

**CORE CLAIM**
- Claim: The $7M denominator is a nominal, unweighted sum of gated stage costs, while the benefit carries p = 0.40.
- Support: **LOGIC ONLY**
- Why: The mechanism is sound, but I found no evidence on how the CEA constructed the cost, and the critique is conditional on it.

**OVERALL VERDICT: UNVERIFIABLE.** The hypothesis is logically sound, with correct arithmetic and no fabricated evidence. Retain it as a flagged hypothesis marked "UNGROUNDED — plausible but needs empirical support." It should be checked against the CEA's cost cells before use. If the $7M is nominal, the direction is up, with a magnitude of roughly 1.2–2.3x depending on s.

---

## Critique 3: A 1-year trial speedup is not necessarily a 1-year adoption speedup

**CITATION CHECK**
- Study 31/A5349 and BPaLM were named only as case studies. Both exist and the Investigator's characterisation is generally fair.
  - Study 31 is VERIFIED. It was a 
randomized, multi-national, open-label, controlled phase 3 trial comparing two 4-month rifapentine-containing regimens to the standard 6-month control.

  - BPaLM was based on TB-PRACTECAL and ZeNix. VERIFIED.

**CLAIM CHECK**
- WHO uses a GDG process to change TB guidelines: **VERIFIED**. 
In 2021, the WHO Global TB Programme received data from the Study 31 investigators and convened a Guideline Development Group to review results.

- "WHO guideline updates occur on a roughly fixed schedule": **NOT SUPPORTED, and partly CONTRADICTED by these two cases**. GDGs appear to be convened ad hoc when data arrive.
  - Study 31: 
results were presented at the 51st virtual Union World Conference in October 2020
. 
The GDG met virtually from 27–30 April 2021.
 
Detailed results were published on 6 May 2021.
 
WHO then issued a rapid communication in June 2021
. The lag from conference presentation to rapid communication was about 8 months, and from the NEJM paper about 5–6 weeks.
  - BPaLM: 
WHO convened a GDG in February–March 2022 after the TB-PRACTECAL and ZeNix results.
 
A rapid communication followed in May 2022.
 The full guideline update was published later in the year (the Lancet Respiratory Medicine page lists Dec 15, 2022).
  - A WHO "rapid communication" route exists, which weakens the idea of a fixed window with a 2+ year miss penalty. I found no evidence supporting the "2+ years" cycle claim.
- Trial results are not the only binding constraint on uptake: **SUPPORTED**. WHO said 
implementation and uptake of the new regimen in the short to medium term will be more feasible if the cost of rifapentine is reduced and availability improved.
 The same communication flagged 
a need for rigorous antibacterial stewardship because the regimen contains moxifloxacin.
 This supports the "speedup less than one year" direction through downstream bottlenecks (price, supply, national adoption). It does not support the lumpy "WHO-window" mechanism.
- A public call for data and national policy/procurement lags: **PLAUSIBLE, not checked**.
- "Materiality threshold of about 0.65 years" and "speedup_years linear in SROI": **UNVERIFIABLE** without the CEA. Linearity follows from the stated structure.

**EVIDENCE FOUND**
- Both case studies show a short gap between pivotal data and WHO guidance (months, not years). Real WHO timing therefore looks more responsive than the critique assumes.
- I did not find data on national adoption lags, which is where slack-absorption would most plausibly occur.
- Direction: the evidence points more toward "less than one year" through downstream bottlenecks than toward "more than one year" through missed guideline windows.

**CORE CLAIM**
- Claim: The trial is not the sole binding constraint, so a 1-year trial speedup need not translate into a 1-year adoption speedup, and the effective speedup is a lumpy random variable.
- Support: **LOGIC ONLY** for the general point, with partial direct support for non-trial bottlenecks (price, availability).
- Why: Downstream constraints are documented, but the specific "fixed WHO schedule, missed-window" mechanism is not supported by the two cases I checked.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The core concern, that speedup is not a pure translation of the adoption curve, is sound and partly supported. The "roughly fixed WHO guideline schedule" and "lose a full 2+ year cycle" mechanisms are unsupported, and the TB cases lean against them.

**REVISED CRITIQUE**
- The model's assumption that a 1-year trial speedup gives a 1-year adoption speedup is untested.
- Adoption also depends on national policy change, procurement and drug price/availability (documented for rifapentine), so the effective speedup could be below 1 year.
- WHO's guideline step in recent TB cases (Study 31, BPaLM) was ad hoc and fast (months), so the upside "missed window" scenario is weakly supported.
- Direction: **leaning down or uncertain**, rather than symmetric.
- Magnitude: medium, and sensitivity analysis is needed.
- Flag as UNGROUNDED for national-level lags.
- Remove the "fixed schedule" and "2+ year cycle" claims.

--- Critique: Post-TB lung disease morbidity is likely the largest unvalued channel (~50–60k central, wide range) ---

## Critique 1: Post-TB lung disease morbidity (~50–60k central)

**CITATION CHECK**
- Menzies et al. 2021 (Lancet Glob Health): **VERIFIED**, and the exact share can now be filled in. The paper exists. 
It estimates 12.1 DALYs per incident TB case, of which 6.3 come from the disease episode and 5.8 from post-TB.
 
Globally, 58 million of 122 million DALYs (47%) are attributed to post-TB sequelae.
 
The post-TB estimates are based on decreased lung function caused by pulmonary TB.
 The Investigator's "substantial share" is correct.
- International Post-TB Symposium consensus and Allwood et al.: **NOT CHECKED.** The Investigator gave no specific citation. 
Allwood et al.'s 2019 Lancet Infect Dis correspondence ("The long shadow post-tuberculosis") does highlight the hidden epidemic of chronic disease and impairment after microbiological cure.
 That fits the general claim.

**CLAIM CHECK**
- "Post-TB lung disease affects a large share of survivors": **VERIFIED** qualitatively. 
One source says pulmonary TB causes structural lung changes in more than two-thirds of patients that persist after cure.
 
Another study found 31% of survivors reported respiratory symptoms 1 year after treatment.
 The "~30% clinically meaningful impairment" input is plausible.
- Disability weight of 0.1–0.2 over 15–25 years, giving ~0.75 DALYs per treated patient: **UNVERIFIABLE.** These are the Investigator's own inputs. They sit well below Menzies' post-TB total of 5.8 per case. Menzies includes post-TB mortality, and I could not confirm the morbidity/mortality split.
- Arithmetic (3.3M × 0.75 × 5% × 0.45 ≈ 55k, range 10k–300k): **VERIFIED.** It reproduces correctly.
- "Trial's strongest signal was reduced lung damage": **UNVERIFIABLE.** The trial is not identified in what I was given. For context, in the ROSETTA rosuvastatin trial 
10 mg rosuvastatin for the first eight weeks did not produce substantive benefit on culture conversion, chest x-ray lung involvement, or spirometry.
 Whether the source trial differs from ROSETTA should be checked.
- "Link between early lung damage and long-term function is not established in a long-follow-up RCT": **PLAUSIBLE.** I found no counter-evidence.
- "No-discounting inflates this channel": **PLAUSIBLE.** 
Menzies found 28% of total DALYs accrue 15 or more years after incident TB.
 That supports the point that a large share of the burden is very long-dated.

**EVIDENCE FOUND**
- The Investigator's baseline looks too low relative to Menzies. 
Menzies puts post-TB burden at 5.8 DALYs per case.
 For 3.3M patients that is ~19M DALYs, versus the Investigator's ~2.5M for lung morbidity alone. This is a different scope (mortality included, extrapulmonary cases included), so it isn't a direct contradiction. It does suggest the 5% × baseline term could be understated if the lung-damage-to-long-term-outcome link holds.
- 
A 2025 Lancet Glob Health modelling paper on progressive lung damage found post-TB DALYs were 52.5% of total DALYs with prompt treatment.
 This supports a large post-TB share.
- Overlap with Critique 2: both apply the same 5% reduction to the same lung-damage pathway. Menzies models post-TB mortality and morbidity jointly from lung function, so these two channels should be combined rather than added as independent terms.

**CORE CLAIM**
- Claim: A ~5% proportional reduction in long-term post-TB lung burden follows from the trial's early lung-damage signal.
- Support: **LOGIC ONLY**
- Why: The baseline burden is well supported, but I found no evidence on surrogate-to-long-term transfer, and the 5% is admitted to be an assumption.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The channel exists and is large. The 5% effect size and the 0.45 probability weight are ungrounded.

**REVISED CRITIQUE**
- Post-TB sequelae account for about 5.8 of 12.1 lifetime DALYs per incident case (Menzies 2021). The BOTEC assigns this channel zero value.
- The Investigator's baseline of 0.75 DALYs per patient is probably conservative for morbidity alone, and could be much larger if mortality is included.
- The 5% reduction attributable to the intervention is UNGROUNDED, as is the claim that early lung-damage reductions persist. Treat the central estimate (~55k) as illustrative.
- Combine with Critique 2 to avoid double counting.
- Strength: medium, with higher upside uncertainty than stated.
- Report both discounted and undiscounted versions, as the Investigator suggested.

---

## Critique 2: Post-treatment excess mortality and life-expectancy adjustment

**CITATION CHECK**
- Romanowski et al. 2019 (Lancet Infect Dis 19:1129–37): **VERIFIED.** 
It found the force of mortality in TB survivors to be 2.91 (95% CI 2.21–3.84) times that of people who never had TB.
 
A commentary describes it as roughly three to four times greater mortality than local populations.
 The "multiple of the general population" recollection is correct. The Investigator's cumulative 10% excess over 10 years is flagged as illustrative and is not from the paper.

**CLAIM CHECK**
- Elevated long-term all-cause mortality after TB: **VERIFIED.**
- ~40% of excess deaths attributable to respiratory sequelae: **PLAUSIBLE, UNGROUNDED.**
  - 
Romanowski attributed 20% (95% CI 15–26) of the excess to cardiovascular disease.
 That leaves room for a respiratory share.
  - 
A 2025 lung-function meta-analysis says respiratory diseases remain the leading cause of excess deaths in people who recover from TB.
 This is a secondary claim, so I can't pin the share at 40%.
- ~10% cumulative excess mortality over 10 years: **PLAUSIBLE.** With an SMR of ~2.9 the figure depends on background mortality, so 10% is within a reasonable range. It is not directly verified.
- Arithmetic: **VERIFIED.** 0.1 × 0.4 × 0.05 = 0.002; × 15 DALYs × 3.3M ≈ 99k; × 0.45 ≈ 45k. The (b) range of 25–55k also reproduces from 5–10% of 535k.
- (b) The 5–10% overstatement from the life-expectancy adjustment: **UNVERIFIABLE.**
  - 
Menzies finds young age, HIV and living in a high-incidence country associated with higher DALYs per incident case.
 That is about post-TB burden, not remaining life expectancy of those rescued from death.
  - The direction of the Investigator's argument is plausible, but the magnitude is invented.
- Statin's own cardiovascular benefit over ~6 months is negligible: **PLAUSIBLE.** I did not search for this.

**EVIDENCE FOUND**
- Post-TB mortality is already modelled in Menzies' per-case DALYs, so channel (a) overlaps Critique 1 and the Menzies framework.
- The "Estimated Direction: decreases" label is ambiguous. (a) adds benefit and (b) subtracts it, so the net sign is genuinely unclear, as the Investigator says.

**CORE CLAIM**
- Claim: About 40% of post-treatment excess deaths are lung-related and reducible by ~5% via the intervention, roughly offset by a 5–10% overstatement of on-treatment benefit.
- Support: **LOGIC ONLY**
- Why: The excess mortality is verified, but I found no evidence on the respiratory share, the 5% reduction, or the life-expectancy adjustment.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The elevated mortality is real. The magnitudes are all assumptions.

**REVISED CRITIQUE**
- TB survivors have about 2.9× background mortality (Romanowski 2019). Some of it is respiratory, and CVD accounts for ~20%.
- A lung-sparing adjunct could avert some post-treatment deaths, but the respiratory share, the 5% reduction, and the 10% cumulative excess are UNGROUNDED.
- The sign-reversing life-expectancy adjustment is a logically coherent hypothesis. It is flagged UNGROUNDED, and the 5–10% is unsupported.
- The net could be anywhere between about −25k and +45k. Because it overlaps with Critique 1, merge the two.
- Strength: low–medium.

---

## Critique 3: Transmission benefit (~10–30k central)

**CITATION CHECK**
- No specific studies were cited, so there is nothing to check. Supporting literature I found is listed below.

**CLAIM CHECK**
- "Infectiousness falls quickly after effective therapy starts": **VERIFIED.**
  - 
In early guinea-pig experiments, animals exposed to patients on effective treatment were only 2% as likely to be infected as those exposed to untreated patients.

  - 
A systematic review says data from diverse experimental studies suggest infectiousness declines rapidly after effective treatment starts, before smear and culture conversion.

  - 
A 2025 review says the exact duration remains uncertain.

- "Most transmission occurs before diagnosis": **PLAUSIBLE, partly supported.**
  - 
A Valencia whole-genome-sequencing study found 5 of 14 cases (35.7%) likely transmitted well before symptom onset.

  - 
In rural China (Songjiang), 40.6% of determinate transmission events occurred before the index case's symptom onset.

  - These figures are for before symptom onset, not before diagnosis. Diagnostic delay would push the pre-diagnosis share higher.
  - 
A modelling study estimated roughly 68% of global transmission came from asymptomatic TB.
 The range is wide (27–92%).
- Post-start share of lifetime transmission is 1–5%: **UNVERIFIABLE, plausible.** The guinea-pig 2% figure and the pre-diagnosis shares are consistent with a small number. I found no direct estimate of this parameter.
- "Culture conversion at 8 weeks does not map to infectiousness one-to-one": **VERIFIED.**
  - 
A WHO-commissioned meta-analysis found most patients remained culture positive at 2 weeks. It notes culture positivity is only one component of infectiousness, with cough frequency and aerosol generation also important.

  - 
It also states there are no data describing how infectiousness changed over time after treatment initiation.

  - This supports the Investigator's downward adjustment, and also means the 10–20% fractional reduction is poorly anchored.
- Arithmetic: **VERIFIED.** 3.3M × 0.5 × 0.003 × 10 ≈ 50k, and ~20k after weighting.
- 10 DALYs per secondary case: **PLAUSIBLE.** It is consistent with Menzies' 12.1 DALYs per incident case.

**EVIDENCE FOUND**
- The guinea-pig data show infectiousness drops sharply with effective therapy regardless of culture status, which weakens the case that a faster culture conversion adds much extra transmission reduction.
- 
In one MDR-TB guinea-pig experiment, patients infected 26.7% of animals before treatment and 27.8% at 72 hours after drug initiation.
 Early post-start infectiousness is therefore not always near zero, which keeps some upper tail alive.
- 
The ROSETTA trial found no substantive benefit of rosuvastatin on culture conversion.
 If the trial under evaluation has a similarly weak conversion signal, this channel shrinks further. I can't confirm this for the actual trial.

**CORE CLAIM**
- Claim: The net reduction in total transmission from faster conversion is ~0.3% (range 0.1–1%).
- Support: **LOGIC ONLY**
- Why: Qualitative literature supports "small", but the 1–5% post-start share and the 10–20% fractional reduction are unsupported, and the evidence cuts toward a smaller effect.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The direction and the logic that the benefit is small are supported. The numbers are unanchored.

**REVISED CRITIQUE**
- Most transmission occurs before treatment starts, and effective therapy rapidly reduces infectiousness. Culture conversion is an imperfect proxy for infectiousness, so the incremental transmission benefit is small.
- The specific figures (0.3% net reduction, 1–5% post-start share, 10–20% fractional reduction) are UNGROUNDED.
- Treat ~10–30k as an order-of-magnitude placeholder. The true value is probably at or below the low end if the trial's culture-conversion effect is weak.
- Strength: low. This is the least material of the three channels.

--- Critique: Post-treatment excess mortality (~40–50k central) and a related sign-reversing adjustment ---

## Critique 1: Post-TB lung disease morbidity (~50–60k central)

**CITATION CHECK**
- Menzies et al. 2021 (Lancet Glob Health): **VERIFIED**, and the exact share can now be filled in. The paper exists. 
It estimates 12.1 DALYs per incident TB case, of which 6.3 come from the disease episode and 5.8 from post-TB.
 
Globally, 58 million of 122 million DALYs (47%) are attributed to post-TB sequelae.
 
The post-TB estimates are based on decreased lung function caused by pulmonary TB.
 The Investigator's "substantial share" is correct.
- International Post-TB Symposium consensus and Allwood et al.: **NOT CHECKED.** The Investigator gave no specific citation. 
Allwood et al.'s 2019 Lancet Infect Dis correspondence ("The long shadow post-tuberculosis") does highlight the hidden epidemic of chronic disease and impairment after microbiological cure.
 That fits the general claim.

**CLAIM CHECK**
- "Post-TB lung disease affects a large share of survivors": **VERIFIED** qualitatively. 
One source says pulmonary TB causes structural lung changes in more than two-thirds of patients that persist after cure.
 
Another study found 31% of survivors reported respiratory symptoms 1 year after treatment.
 The "~30% clinically meaningful impairment" input is plausible.
- Disability weight of 0.1–0.2 over 15–25 years, giving ~0.75 DALYs per treated patient: **UNVERIFIABLE.** These are the Investigator's own inputs. They sit well below Menzies' post-TB total of 5.8 per case. Menzies includes post-TB mortality, and I could not confirm the morbidity/mortality split.
- Arithmetic (3.3M × 0.75 × 5% × 0.45 ≈ 55k, range 10k–300k): **VERIFIED.** It reproduces correctly.
- "Trial's strongest signal was reduced lung damage": **UNVERIFIABLE.** The trial is not identified in what I was given. For context, in the ROSETTA rosuvastatin trial 
10 mg rosuvastatin for the first eight weeks did not produce substantive benefit on culture conversion, chest x-ray lung involvement, or spirometry.
 Whether the source trial differs from ROSETTA should be checked.
- "Link between early lung damage and long-term function is not established in a long-follow-up RCT": **PLAUSIBLE.** I found no counter-evidence.
- "No-discounting inflates this channel": **PLAUSIBLE.** 
Menzies found 28% of total DALYs accrue 15 or more years after incident TB.
 That supports the point that a large share of the burden is very long-dated.

**EVIDENCE FOUND**
- The Investigator's baseline looks too low relative to Menzies. 
Menzies puts post-TB burden at 5.8 DALYs per case.
 For 3.3M patients that is ~19M DALYs, versus the Investigator's ~2.5M for lung morbidity alone. This is a different scope (mortality included, extrapulmonary cases included), so it isn't a direct contradiction. It does suggest the 5% × baseline term could be understated if the lung-damage-to-long-term-outcome link holds.
- 
A 2025 Lancet Glob Health modelling paper on progressive lung damage found post-TB DALYs were 52.5% of total DALYs with prompt treatment.
 This supports a large post-TB share.
- Overlap with Critique 2: both apply the same 5% reduction to the same lung-damage pathway. Menzies models post-TB mortality and morbidity jointly from lung function, so these two channels should be combined rather than added as independent terms.

**CORE CLAIM**
- Claim: A ~5% proportional reduction in long-term post-TB lung burden follows from the trial's early lung-damage signal.
- Support: **LOGIC ONLY**
- Why: The baseline burden is well supported, but I found no evidence on surrogate-to-long-term transfer, and the 5% is admitted to be an assumption.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The channel exists and is large. The 5% effect size and the 0.45 probability weight are ungrounded.

**REVISED CRITIQUE**
- Post-TB sequelae account for about 5.8 of 12.1 lifetime DALYs per incident case (Menzies 2021). The BOTEC assigns this channel zero value.
- The Investigator's baseline of 0.75 DALYs per patient is probably conservative for morbidity alone, and could be much larger if mortality is included.
- The 5% reduction attributable to the intervention is UNGROUNDED, as is the claim that early lung-damage reductions persist. Treat the central estimate (~55k) as illustrative.
- Combine with Critique 2 to avoid double counting.
- Strength: medium, with higher upside uncertainty than stated.
- Report both discounted and undiscounted versions, as the Investigator suggested.

---

## Critique 2: Post-treatment excess mortality and life-expectancy adjustment

**CITATION CHECK**
- Romanowski et al. 2019 (Lancet Infect Dis 19:1129–37): **VERIFIED.** 
It found the force of mortality in TB survivors to be 2.91 (95% CI 2.21–3.84) times that of people who never had TB.
 
A commentary describes it as roughly three to four times greater mortality than local populations.
 The "multiple of the general population" recollection is correct. The Investigator's cumulative 10% excess over 10 years is flagged as illustrative and is not from the paper.

**CLAIM CHECK**
- Elevated long-term all-cause mortality after TB: **VERIFIED.**
- ~40% of excess deaths attributable to respiratory sequelae: **PLAUSIBLE, UNGROUNDED.**
  - 
Romanowski attributed 20% (95% CI 15–26) of the excess to cardiovascular disease.
 That leaves room for a respiratory share.
  - 
A 2025 lung-function meta-analysis says respiratory diseases remain the leading cause of excess deaths in people who recover from TB.
 This is a secondary claim, so I can't pin the share at 40%.
- ~10% cumulative excess mortality over 10 years: **PLAUSIBLE.** With an SMR of ~2.9 the figure depends on background mortality, so 10% is within a reasonable range. It is not directly verified.
- Arithmetic: **VERIFIED.** 0.1 × 0.4 × 0.05 = 0.002; × 15 DALYs × 3.3M ≈ 99k; × 0.45 ≈ 45k. The (b) range of 25–55k also reproduces from 5–10% of 535k.
- (b) The 5–10% overstatement from the life-expectancy adjustment: **UNVERIFIABLE.**
  - 
Menzies finds young age, HIV and living in a high-incidence country associated with higher DALYs per incident case.
 That is about post-TB burden, not remaining life expectancy of those rescued from death.
  - The direction of the Investigator's argument is plausible, but the magnitude is invented.
- Statin's own cardiovascular benefit over ~6 months is negligible: **PLAUSIBLE.** I did not search for this.

**EVIDENCE FOUND**
- Post-TB mortality is already modelled in Menzies' per-case DALYs, so channel (a) overlaps Critique 1 and the Menzies framework.
- The "Estimated Direction: decreases" label is ambiguous. (a) adds benefit and (b) subtracts it, so the net sign is genuinely unclear, as the Investigator says.

**CORE CLAIM**
- Claim: About 40% of post-treatment excess deaths are lung-related and reducible by ~5% via the intervention, roughly offset by a 5–10% overstatement of on-treatment benefit.
- Support: **LOGIC ONLY**
- Why: The excess mortality is verified, but I found no evidence on the respiratory share, the 5% reduction, or the life-expectancy adjustment.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The elevated mortality is real. The magnitudes are all assumptions.

**REVISED CRITIQUE**
- TB survivors have about 2.9× background mortality (Romanowski 2019). Some of it is respiratory, and CVD accounts for ~20%.
- A lung-sparing adjunct could avert some post-treatment deaths, but the respiratory share, the 5% reduction, and the 10% cumulative excess are UNGROUNDED.
- The sign-reversing life-expectancy adjustment is a logically coherent hypothesis. It is flagged UNGROUNDED, and the 5–10% is unsupported.
- The net could be anywhere between about −25k and +45k. Because it overlaps with Critique 1, merge the two.
- Strength: low–medium.

---

## Critique 3: Transmission benefit (~10–30k central)

**CITATION CHECK**
- No specific studies were cited, so there is nothing to check. Supporting literature I found is listed below.

**CLAIM CHECK**
- "Infectiousness falls quickly after effective therapy starts": **VERIFIED.**
  - 
In early guinea-pig experiments, animals exposed to patients on effective treatment were only 2% as likely to be infected as those exposed to untreated patients.

  - 
A systematic review says data from diverse experimental studies suggest infectiousness declines rapidly after effective treatment starts, before smear and culture conversion.

  - 
A 2025 review says the exact duration remains uncertain.

- "Most transmission occurs before diagnosis": **PLAUSIBLE, partly supported.**
  - 
A Valencia whole-genome-sequencing study found 5 of 14 cases (35.7%) likely transmitted well before symptom onset.

  - 
In rural China (Songjiang), 40.6% of determinate transmission events occurred before the index case's symptom onset.

  - These figures are for before symptom onset, not before diagnosis. Diagnostic delay would push the pre-diagnosis share higher.
  - 
A modelling study estimated roughly 68% of global transmission came from asymptomatic TB.
 The range is wide (27–92%).
- Post-start share of lifetime transmission is 1–5%: **UNVERIFIABLE, plausible.** The guinea-pig 2% figure and the pre-diagnosis shares are consistent with a small number. I found no direct estimate of this parameter.
- "Culture conversion at 8 weeks does not map to infectiousness one-to-one": **VERIFIED.**
  - 
A WHO-commissioned meta-analysis found most patients remained culture positive at 2 weeks. It notes culture positivity is only one component of infectiousness, with cough frequency and aerosol generation also important.

  - 
It also states there are no data describing how infectiousness changed over time after treatment initiation.

  - This supports the Investigator's downward adjustment, and also means the 10–20% fractional reduction is poorly anchored.
- Arithmetic: **VERIFIED.** 3.3M × 0.5 × 0.003 × 10 ≈ 50k, and ~20k after weighting.
- 10 DALYs per secondary case: **PLAUSIBLE.** It is consistent with Menzies' 12.1 DALYs per incident case.

**EVIDENCE FOUND**
- The guinea-pig data show infectiousness drops sharply with effective therapy regardless of culture status, which weakens the case that a faster culture conversion adds much extra transmission reduction.
- 
In one MDR-TB guinea-pig experiment, patients infected 26.7% of animals before treatment and 27.8% at 72 hours after drug initiation.
 Early post-start infectiousness is therefore not always near zero, which keeps some upper tail alive.
- 
The ROSETTA trial found no substantive benefit of rosuvastatin on culture conversion.
 If the trial under evaluation has a similarly weak conversion signal, this channel shrinks further. I can't confirm this for the actual trial.

**CORE CLAIM**
- Claim: The net reduction in total transmission from faster conversion is ~0.3% (range 0.1–1%).
- Support: **LOGIC ONLY**
- Why: Qualitative literature supports "small", but the 1–5% post-start share and the 10–20% fractional reduction are unsupported, and the evidence cuts toward a smaller effect.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The direction and the logic that the benefit is small are supported. The numbers are unanchored.

**REVISED CRITIQUE**
- Most transmission occurs before treatment starts, and effective therapy rapidly reduces infectiousness. Culture conversion is an imperfect proxy for infectiousness, so the incremental transmission benefit is small.
- The specific figures (0.3% net reduction, 1–5% post-start share, 10–20% fractional reduction) are UNGROUNDED.
- Treat ~10–30k as an order-of-magnitude placeholder. The true value is probably at or below the low end if the trial's culture-conversion effect is weak.
- Strength: low. This is the least material of the three channels.

--- Critique: Transmission benefit is small, with a bounded calculation (~10–30k central) ---

## Critique 1: Post-TB lung disease morbidity (~50–60k central)

**CITATION CHECK**
- Menzies et al. 2021 (Lancet Glob Health): **VERIFIED**, and the exact share can now be filled in. The paper exists. 
It estimates 12.1 DALYs per incident TB case, of which 6.3 come from the disease episode and 5.8 from post-TB.
 
Globally, 58 million of 122 million DALYs (47%) are attributed to post-TB sequelae.
 
The post-TB estimates are based on decreased lung function caused by pulmonary TB.
 The Investigator's "substantial share" is correct.
- International Post-TB Symposium consensus and Allwood et al.: **NOT CHECKED.** The Investigator gave no specific citation. 
Allwood et al.'s 2019 Lancet Infect Dis correspondence ("The long shadow post-tuberculosis") does highlight the hidden epidemic of chronic disease and impairment after microbiological cure.
 That fits the general claim.

**CLAIM CHECK**
- "Post-TB lung disease affects a large share of survivors": **VERIFIED** qualitatively. 
One source says pulmonary TB causes structural lung changes in more than two-thirds of patients that persist after cure.
 
Another study found 31% of survivors reported respiratory symptoms 1 year after treatment.
 The "~30% clinically meaningful impairment" input is plausible.
- Disability weight of 0.1–0.2 over 15–25 years, giving ~0.75 DALYs per treated patient: **UNVERIFIABLE.** These are the Investigator's own inputs. They sit well below Menzies' post-TB total of 5.8 per case. Menzies includes post-TB mortality, and I could not confirm the morbidity/mortality split.
- Arithmetic (3.3M × 0.75 × 5% × 0.45 ≈ 55k, range 10k–300k): **VERIFIED.** It reproduces correctly.
- "Trial's strongest signal was reduced lung damage": **UNVERIFIABLE.** The trial is not identified in what I was given. For context, in the ROSETTA rosuvastatin trial 
10 mg rosuvastatin for the first eight weeks did not produce substantive benefit on culture conversion, chest x-ray lung involvement, or spirometry.
 Whether the source trial differs from ROSETTA should be checked.
- "Link between early lung damage and long-term function is not established in a long-follow-up RCT": **PLAUSIBLE.** I found no counter-evidence.
- "No-discounting inflates this channel": **PLAUSIBLE.** 
Menzies found 28% of total DALYs accrue 15 or more years after incident TB.
 That supports the point that a large share of the burden is very long-dated.

**EVIDENCE FOUND**
- The Investigator's baseline looks too low relative to Menzies. 
Menzies puts post-TB burden at 5.8 DALYs per case.
 For 3.3M patients that is ~19M DALYs, versus the Investigator's ~2.5M for lung morbidity alone. This is a different scope (mortality included, extrapulmonary cases included), so it isn't a direct contradiction. It does suggest the 5% × baseline term could be understated if the lung-damage-to-long-term-outcome link holds.
- 
A 2025 Lancet Glob Health modelling paper on progressive lung damage found post-TB DALYs were 52.5% of total DALYs with prompt treatment.
 This supports a large post-TB share.
- Overlap with Critique 2: both apply the same 5% reduction to the same lung-damage pathway. Menzies models post-TB mortality and morbidity jointly from lung function, so these two channels should be combined rather than added as independent terms.

**CORE CLAIM**
- Claim: A ~5% proportional reduction in long-term post-TB lung burden follows from the trial's early lung-damage signal.
- Support: **LOGIC ONLY**
- Why: The baseline burden is well supported, but I found no evidence on surrogate-to-long-term transfer, and the 5% is admitted to be an assumption.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The channel exists and is large. The 5% effect size and the 0.45 probability weight are ungrounded.

**REVISED CRITIQUE**
- Post-TB sequelae account for about 5.8 of 12.1 lifetime DALYs per incident case (Menzies 2021). The BOTEC assigns this channel zero value.
- The Investigator's baseline of 0.75 DALYs per patient is probably conservative for morbidity alone, and could be much larger if mortality is included.
- The 5% reduction attributable to the intervention is UNGROUNDED, as is the claim that early lung-damage reductions persist. Treat the central estimate (~55k) as illustrative.
- Combine with Critique 2 to avoid double counting.
- Strength: medium, with higher upside uncertainty than stated.
- Report both discounted and undiscounted versions, as the Investigator suggested.

---

## Critique 2: Post-treatment excess mortality and life-expectancy adjustment

**CITATION CHECK**
- Romanowski et al. 2019 (Lancet Infect Dis 19:1129–37): **VERIFIED.** 
It found the force of mortality in TB survivors to be 2.91 (95% CI 2.21–3.84) times that of people who never had TB.
 
A commentary describes it as roughly three to four times greater mortality than local populations.
 The "multiple of the general population" recollection is correct. The Investigator's cumulative 10% excess over 10 years is flagged as illustrative and is not from the paper.

**CLAIM CHECK**
- Elevated long-term all-cause mortality after TB: **VERIFIED.**
- ~40% of excess deaths attributable to respiratory sequelae: **PLAUSIBLE, UNGROUNDED.**
  - 
Romanowski attributed 20% (95% CI 15–26) of the excess to cardiovascular disease.
 That leaves room for a respiratory share.
  - 
A 2025 lung-function meta-analysis says respiratory diseases remain the leading cause of excess deaths in people who recover from TB.
 This is a secondary claim, so I can't pin the share at 40%.
- ~10% cumulative excess mortality over 10 years: **PLAUSIBLE.** With an SMR of ~2.9 the figure depends on background mortality, so 10% is within a reasonable range. It is not directly verified.
- Arithmetic: **VERIFIED.** 0.1 × 0.4 × 0.05 = 0.002; × 15 DALYs × 3.3M ≈ 99k; × 0.45 ≈ 45k. The (b) range of 25–55k also reproduces from 5–10% of 535k.
- (b) The 5–10% overstatement from the life-expectancy adjustment: **UNVERIFIABLE.**
  - 
Menzies finds young age, HIV and living in a high-incidence country associated with higher DALYs per incident case.
 That is about post-TB burden, not remaining life expectancy of those rescued from death.
  - The direction of the Investigator's argument is plausible, but the magnitude is invented.
- Statin's own cardiovascular benefit over ~6 months is negligible: **PLAUSIBLE.** I did not search for this.

**EVIDENCE FOUND**
- Post-TB mortality is already modelled in Menzies' per-case DALYs, so channel (a) overlaps Critique 1 and the Menzies framework.
- The "Estimated Direction: decreases" label is ambiguous. (a) adds benefit and (b) subtracts it, so the net sign is genuinely unclear, as the Investigator says.

**CORE CLAIM**
- Claim: About 40% of post-treatment excess deaths are lung-related and reducible by ~5% via the intervention, roughly offset by a 5–10% overstatement of on-treatment benefit.
- Support: **LOGIC ONLY**
- Why: The excess mortality is verified, but I found no evidence on the respiratory share, the 5% reduction, or the life-expectancy adjustment.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The elevated mortality is real. The magnitudes are all assumptions.

**REVISED CRITIQUE**
- TB survivors have about 2.9× background mortality (Romanowski 2019). Some of it is respiratory, and CVD accounts for ~20%.
- A lung-sparing adjunct could avert some post-treatment deaths, but the respiratory share, the 5% reduction, and the 10% cumulative excess are UNGROUNDED.
- The sign-reversing life-expectancy adjustment is a logically coherent hypothesis. It is flagged UNGROUNDED, and the 5–10% is unsupported.
- The net could be anywhere between about −25k and +45k. Because it overlaps with Critique 1, merge the two.
- Strength: low–medium.

---

## Critique 3: Transmission benefit (~10–30k central)

**CITATION CHECK**
- No specific studies were cited, so there is nothing to check. Supporting literature I found is listed below.

**CLAIM CHECK**
- "Infectiousness falls quickly after effective therapy starts": **VERIFIED.**
  - 
In early guinea-pig experiments, animals exposed to patients on effective treatment were only 2% as likely to be infected as those exposed to untreated patients.

  - 
A systematic review says data from diverse experimental studies suggest infectiousness declines rapidly after effective treatment starts, before smear and culture conversion.

  - 
A 2025 review says the exact duration remains uncertain.

- "Most transmission occurs before diagnosis": **PLAUSIBLE, partly supported.**
  - 
A Valencia whole-genome-sequencing study found 5 of 14 cases (35.7%) likely transmitted well before symptom onset.

  - 
In rural China (Songjiang), 40.6% of determinate transmission events occurred before the index case's symptom onset.

  - These figures are for before symptom onset, not before diagnosis. Diagnostic delay would push the pre-diagnosis share higher.
  - 
A modelling study estimated roughly 68% of global transmission came from asymptomatic TB.
 The range is wide (27–92%).
- Post-start share of lifetime transmission is 1–5%: **UNVERIFIABLE, plausible.** The guinea-pig 2% figure and the pre-diagnosis shares are consistent with a small number. I found no direct estimate of this parameter.
- "Culture conversion at 8 weeks does not map to infectiousness one-to-one": **VERIFIED.**
  - 
A WHO-commissioned meta-analysis found most patients remained culture positive at 2 weeks. It notes culture positivity is only one component of infectiousness, with cough frequency and aerosol generation also important.

  - 
It also states there are no data describing how infectiousness changed over time after treatment initiation.

  - This supports the Investigator's downward adjustment, and also means the 10–20% fractional reduction is poorly anchored.
- Arithmetic: **VERIFIED.** 3.3M × 0.5 × 0.003 × 10 ≈ 50k, and ~20k after weighting.
- 10 DALYs per secondary case: **PLAUSIBLE.** It is consistent with Menzies' 12.1 DALYs per incident case.

**EVIDENCE FOUND**
- The guinea-pig data show infectiousness drops sharply with effective therapy regardless of culture status, which weakens the case that a faster culture conversion adds much extra transmission reduction.
- 
In one MDR-TB guinea-pig experiment, patients infected 26.7% of animals before treatment and 27.8% at 72 hours after drug initiation.
 Early post-start infectiousness is therefore not always near zero, which keeps some upper tail alive.
- 
The ROSETTA trial found no substantive benefit of rosuvastatin on culture conversion.
 If the trial under evaluation has a similarly weak conversion signal, this channel shrinks further. I can't confirm this for the actual trial.

**CORE CLAIM**
- Claim: The net reduction in total transmission from faster conversion is ~0.3% (range 0.1–1%).
- Support: **LOGIC ONLY**
- Why: Qualitative literature supports "small", but the 1–5% post-start share and the 10–20% fractional reduction are unsupported, and the evidence cuts toward a smaller effect.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The direction and the logic that the benefit is small are supported. The numbers are unanchored.

**REVISED CRITIQUE**
- Most transmission occurs before treatment starts, and effective therapy rapidly reduces infectiousness. Culture conversion is an imperfect proxy for infectiousness, so the incremental transmission benefit is small.
- The specific figures (0.3% net reduction, 1–5% post-start share, 10–20% fractional reduction) are UNGROUNDED.
- Treat ~10–30k as an order-of-magnitude placeholder. The true value is probably at or below the low end if the trial's culture-conversion effect is weak.
- Strength: low. This is the least material of the three channels.

--- Critique: The "lung benefit without mortality benefit" scenario is structurally less valuable than a simple p_success weighting implies ---

## Critique 1: Lung benefit without mortality benefit is worth less than a simple p_success weighting implies

**OVERALL VERDICT: PARTIALLY VERIFIED.** The logic holds, but it is ungrounded. Its inputs are unverified and its labelled direction is inconsistent.

**CLAIM CHECK**
- *"A surrogate-only (lung) result would not obviously lead to adoption at 60% scale."* **PLAUSIBLE, no direct evidence.** I found no WHO guideline text on how lung-function surrogates are weighed. I did not find the CG model, the specific trial, or its registered Phase IIc and Phase III endpoints, so these remain **UNVERIFIABLE**.
- *Conditional adoption of 10–20% in the "mortality fails, lung holds" branch.* **UNVERIFIABLE.** The Investigator already labels it UNGROUNDED.
- *The 0.45, 0.4 base and 60% uptake figures, and the 3.3M patients.* **UNVERIFIABLE.** These come from the CG model, which I could not access.
- *Arithmetic.*
  - The "realistic" range checks out: 0.6 × (0.3–0.5) × (0.1–0.2) ≈ 0.018–0.06.
  - The "naive" bound is overstated. 0.4 + 0.6 × (0.3–0.5) gives about 0.58–0.70, which is roughly 1.3–1.6× of 0.45, not "up to ~2×". A 2× result would need P(lung holds | mortality fails) near 1.
- *Direction label.* The critique argues that the 0.45 figure is about right and that the upside is limited. It is labelled "increases", which does not match that argument. Its net effect is closer to neutral. It is a caution against over-crediting the lung channel.

**EVIDENCE FOUND**
- 
Few tuberculosis treatment trials have included lung function as a primary efficacy outcome
, although 
FEV1 correlates with long-term mortality
. This supports the premise that lung function is a non-standard endpoint, so a lung-only win may not translate cleanly into guidelines.
- The phase 2 trial by Wallis et al. found that 
CC-11050 and everolimus might enhance the recovery of FEV1
. FEV1 was therefore used as a preliminary efficacy signal, not as an established registrational endpoint.
- Phase IIc in TB normally means the STEP design. 
CRUSH-TB, for example, uses time to sputum culture negativity as its primary intermediate endpoint
. A trial in this style would not natively produce a lung-function primary endpoint. This is circumstantial, because I could not identify the CG-funded trial.

**CORE CLAIM**
- Claim: conditional adoption in the lung-only branch is far below 60% (about 10–20%).
- Support: **LOGIC ONLY.**
- Why: the reasoning is plausible, and lung function is a non-standard TB endpoint, but I found no direct evidence on WHO or adoption behaviour for this branch.

**REVISED CRITIQUE**
- Retain this as a **weighting caution, flagged UNGROUNDED**. Do not apply the full uptake to the lung-only branch without a separate adoption discount.
- The effect is modest: roughly +0.02–0.06 on a 0.4 base.
- Fix the "up to 2×" figure to about 1.3–1.6×. Treat the direction as neutral to slightly decreasing, with small magnitude.

---

## Critique 2: Sweat-based diagnostic option value (~10–30k central)

**OVERALL VERDICT: UNVERIFIABLE for the specific test. The background facts are verified.** Retain it as a flagged, low-confidence hypothesis.

**CLAIM CHECK**
- *CG funds a sweat-based TB diagnostic alongside the trial.* **UNVERIFIABLE.** I found nothing on this test's development stage, accuracy or regulatory path, or on the funding link.
- *Roughly 2–3M TB cases per year are undiagnosed or unreported.* **VERIFIED.** 
8.3 million people were newly diagnosed with TB in 2024, which is 78% of the estimated incident cases
. 
Estimated incidence was 10.7 million
, so the gap is about 2.4M.
- *Non-sputum competitors are advancing (tongue swab).* **VERIFIED, and ahead of the Investigator's expectation.** 
WHO has issued its first recommendations on near-point-of-care molecular tests and easy-to-collect tongue swab samples
, in February 2026. The Investigator had not checked WHO endorsements. The accuracy evidence is 
tongue-swab performance meeting the minimum WHO non-sputum target (>75% sensitivity, >98% specificity)
.
- *Urine LAM as a competitor.* **PLAUSIBLE.** The LF-LAM assays are named in the WHO report as a bacteriological confirmation method.
- *Arithmetic.* 0.05 × 200k × 5 = 50k DALYs per year, which is correct. The 20% untreated case fatality and 25 DALYs per death are unverified assumptions. Widely cited untreated-TB fatality figures are higher than 20%, so these are not clearly inflated.
- *Whether the $7M all-in cost includes the diagnostic.* **UNVERIFIABLE.** I could not see the model. The Investigator correctly flags this as a consistency check for the CG model owner.

**EVIDENCE FOUND**
- WHO's tongue-swab recommendation has a limited scope. 
Programmes may use tongue swabs from adults and adolescents when sputum cannot be obtained
. Children and others who cannot give sputum are therefore not covered by that recommendation. This leaves some room for a different non-sputum test, which mildly supports the critique's option-value logic.
- Against that, 
tongue swabs are less sensitive than sputum
. The counterfactual is also moving fast. The base case for "incremental cases beyond alternatives" at 1–3% of incidence is therefore uncertain. Counterfactual displacement could push the value toward the low end.
- The tongue-swab and NPOC tests are PCR-based. A sweat-based test would need its own evidence pathway and WHO policy review, which supports the low adoption probability.

**CORE CLAIM**
- Claim: P(adoption) ≈ 5% with an incremental yield of 1–3% of incidence, giving about 10–30k DALYs per year.
- Support: **LOGIC ONLY.**
- Why: the arithmetic is internally consistent, but the probability and yield inputs are an assumed base rate with no source, and the test itself could not be found.

**REVISED CRITIQUE**
- CG assigns zero value to the sweat test. This may understate value, but the amount is speculative, and the range of 0 to ~100k DALYs per year is wide.
- The tongue-swab and NPOC WHO endorsement (Feb 2026) lowers the counterfactual incremental value relative to what the Investigator assumed. The paediatric and no-sputum gap remains.
- Mark it **UNGROUNDED, small magnitude, direction uncertain**.
- The cost-attribution question should be resolved from the model, not from this critique.

---

## Critique 3: 60% steady-state uptake has no precedent among comparable additions

**OVERALL VERDICT: PARTIALLY VERIFIED.** Slow ramps are well supported. The claim that the ceiling is below 60% is not. The title's "no precedent" is overstated.

**CITATION CHECK**
- *Xpert MTB/RIF, WHO endorsement 2010.* **VERIFIED in outline.** 
Since 2011, rapid molecular tests have transformed the TB diagnostic landscape
.
- *WRD coverage "roughly 40–50% in recent reports".* **PARTIALLY VERIFIED.** The global figure was 
54% in 2024, up from 47% in 2022
, and 48% in 2023. The Investigator's range is slightly low. The WRD indicator also covers all WHO-recommended rapid tests, not just Xpert.
- *4-month rifapentine-moxifloxacin, WHO 2022.* **VERIFIED, with strong support for slow uptake.** 
Only 4,154 people were reported started on 4-month HPMZ in 2024, up from 1,271 in 2023
. That is about 0.05% of the 8.3M notified. 
Uptake has been slow, largely because of limited rifapentine availability
. The WHO page also says 
15 countries and areas reported using the regimen by end-2024
. A second list on the same page gives 26.
- *Dexamethasone for TBM (evidence 2004).* **UNVERIFIED.** I did not retrieve coverage data. The 2004 trial is real from background knowledge, but its uptake history needs checking.
- *Pyridoxine with isoniazid recommended but inconsistently supplied.* **UNVERIFIED.** No coverage data retrieved.

**CLAIM CHECK**
- *Reducing the ceiling to 0.30–0.40 cuts SROI by 33–50%.* **VERIFIED as arithmetic.** 0.40/0.60 is a 33% cut and 0.30/0.60 is a 50% cut, assuming linear dependence. The model structure and the "0.39 materiality line" are unverifiable.
- *Comparable additions "often" stall below 50%.* **PARTIALLY CONTRADICTED.** Global WRD coverage is 54% after about 14 years and still rising, not stalled below 50%. WHO also reports that 
37 of 49 high-burden countries used a WRD as the initial test for more than half of notified cases in 2024, up from 31 in 2023
. This is evidence of a slow ramp, not a ceiling.
- *An adjunct with no visible patient benefit is a harder sell.* **PLAUSIBLE, no direct evidence.** It is a reasonable argument.
- *The ramp matters little over an infinite horizon.* **LOGICALLY VALID**, with the discounting caveat the Investigator notes.

**EVIDENCE FOUND**
- The analogs have key differences from a cheap generic oral adjunct. Xpert needs capital equipment and labs. HPMZ is supply-limited by rifapentine, and the NYC experience showed tolerability problems: 
only 14% of eligible patients were prescribed it, and 64% of those who started discontinued
. Neither is a clean analog for generic-drug supply, so they bear on the ramp more than on the ceiling.
- The global target is 100% WRD coverage by 2027 (
set at the 2023 UN high-level meeting
). A system target is not the same as steady-state achieved coverage, but it suggests over 50% is feasible with sustained push.
- Equating adult_uptake with a coverage fraction among all patients may be a different construct from "percent of notified cases tested". I could not check how the CG model defines it.

**CORE CLAIM**
- Claim: the long-run uptake ceiling is plausibly 0.30–0.40, not 0.60.
- Support: **LOGIC ONLY.**
- Why: the precedents show slow ramps (HPMZ about 0.05% after three years, WRD 54% after about 14 years). None shows a stalled ceiling below 60% for a cheap, generic, oral co-administered drug.

**REVISED CRITIQUE**
- Evidence supports the view that new TB tools take about 10 or more years to reach about 50% coverage, and that guideline endorsement does not guarantee uptake.
- This is a stronger argument against the ramp (timing) than against the ceiling. Its main effect is through discounting and finite horizons.
- Retain the ceiling concern as **UNGROUNDED**. Downgrade the magnitude from **large to medium**, with direction **decreases**.
- Do not use "stall below 50%" as support for the 0.30–0.40 ceiling. The WRD data point to 54% and rising.
- Dexamethasone and pyridoxine remain unverified. The pull the Investigator requested has been done for WRD and HPMZ. The GDF order data were not found.

--- Critique: The sweat-based diagnostic carries real option value but is speculative (~10–30k central) ---

## Critique 1: Lung benefit without mortality benefit is worth less than a simple p_success weighting implies

**OVERALL VERDICT: PARTIALLY VERIFIED.** The logic holds, but it is ungrounded. Its inputs are unverified and its labelled direction is inconsistent.

**CLAIM CHECK**
- *"A surrogate-only (lung) result would not obviously lead to adoption at 60% scale."* **PLAUSIBLE, no direct evidence.** I found no WHO guideline text on how lung-function surrogates are weighed. I did not find the CG model, the specific trial, or its registered Phase IIc and Phase III endpoints, so these remain **UNVERIFIABLE**.
- *Conditional adoption of 10–20% in the "mortality fails, lung holds" branch.* **UNVERIFIABLE.** The Investigator already labels it UNGROUNDED.
- *The 0.45, 0.4 base and 60% uptake figures, and the 3.3M patients.* **UNVERIFIABLE.** These come from the CG model, which I could not access.
- *Arithmetic.*
  - The "realistic" range checks out: 0.6 × (0.3–0.5) × (0.1–0.2) ≈ 0.018–0.06.
  - The "naive" bound is overstated. 0.4 + 0.6 × (0.3–0.5) gives about 0.58–0.70, which is roughly 1.3–1.6× of 0.45, not "up to ~2×". A 2× result would need P(lung holds | mortality fails) near 1.
- *Direction label.* The critique argues that the 0.45 figure is about right and that the upside is limited. It is labelled "increases", which does not match that argument. Its net effect is closer to neutral. It is a caution against over-crediting the lung channel.

**EVIDENCE FOUND**
- 
Few tuberculosis treatment trials have included lung function as a primary efficacy outcome
, although 
FEV1 correlates with long-term mortality
. This supports the premise that lung function is a non-standard endpoint, so a lung-only win may not translate cleanly into guidelines.
- The phase 2 trial by Wallis et al. found that 
CC-11050 and everolimus might enhance the recovery of FEV1
. FEV1 was therefore used as a preliminary efficacy signal, not as an established registrational endpoint.
- Phase IIc in TB normally means the STEP design. 
CRUSH-TB, for example, uses time to sputum culture negativity as its primary intermediate endpoint
. A trial in this style would not natively produce a lung-function primary endpoint. This is circumstantial, because I could not identify the CG-funded trial.

**CORE CLAIM**
- Claim: conditional adoption in the lung-only branch is far below 60% (about 10–20%).
- Support: **LOGIC ONLY.**
- Why: the reasoning is plausible, and lung function is a non-standard TB endpoint, but I found no direct evidence on WHO or adoption behaviour for this branch.

**REVISED CRITIQUE**
- Retain this as a **weighting caution, flagged UNGROUNDED**. Do not apply the full uptake to the lung-only branch without a separate adoption discount.
- The effect is modest: roughly +0.02–0.06 on a 0.4 base.
- Fix the "up to 2×" figure to about 1.3–1.6×. Treat the direction as neutral to slightly decreasing, with small magnitude.

---

## Critique 2: Sweat-based diagnostic option value (~10–30k central)

**OVERALL VERDICT: UNVERIFIABLE for the specific test. The background facts are verified.** Retain it as a flagged, low-confidence hypothesis.

**CLAIM CHECK**
- *CG funds a sweat-based TB diagnostic alongside the trial.* **UNVERIFIABLE.** I found nothing on this test's development stage, accuracy or regulatory path, or on the funding link.
- *Roughly 2–3M TB cases per year are undiagnosed or unreported.* **VERIFIED.** 
8.3 million people were newly diagnosed with TB in 2024, which is 78% of the estimated incident cases
. 
Estimated incidence was 10.7 million
, so the gap is about 2.4M.
- *Non-sputum competitors are advancing (tongue swab).* **VERIFIED, and ahead of the Investigator's expectation.** 
WHO has issued its first recommendations on near-point-of-care molecular tests and easy-to-collect tongue swab samples
, in February 2026. The Investigator had not checked WHO endorsements. The accuracy evidence is 
tongue-swab performance meeting the minimum WHO non-sputum target (>75% sensitivity, >98% specificity)
.
- *Urine LAM as a competitor.* **PLAUSIBLE.** The LF-LAM assays are named in the WHO report as a bacteriological confirmation method.
- *Arithmetic.* 0.05 × 200k × 5 = 50k DALYs per year, which is correct. The 20% untreated case fatality and 25 DALYs per death are unverified assumptions. Widely cited untreated-TB fatality figures are higher than 20%, so these are not clearly inflated.
- *Whether the $7M all-in cost includes the diagnostic.* **UNVERIFIABLE.** I could not see the model. The Investigator correctly flags this as a consistency check for the CG model owner.

**EVIDENCE FOUND**
- WHO's tongue-swab recommendation has a limited scope. 
Programmes may use tongue swabs from adults and adolescents when sputum cannot be obtained
. Children and others who cannot give sputum are therefore not covered by that recommendation. This leaves some room for a different non-sputum test, which mildly supports the critique's option-value logic.
- Against that, 
tongue swabs are less sensitive than sputum
. The counterfactual is also moving fast. The base case for "incremental cases beyond alternatives" at 1–3% of incidence is therefore uncertain. Counterfactual displacement could push the value toward the low end.
- The tongue-swab and NPOC tests are PCR-based. A sweat-based test would need its own evidence pathway and WHO policy review, which supports the low adoption probability.

**CORE CLAIM**
- Claim: P(adoption) ≈ 5% with an incremental yield of 1–3% of incidence, giving about 10–30k DALYs per year.
- Support: **LOGIC ONLY.**
- Why: the arithmetic is internally consistent, but the probability and yield inputs are an assumed base rate with no source, and the test itself could not be found.

**REVISED CRITIQUE**
- CG assigns zero value to the sweat test. This may understate value, but the amount is speculative, and the range of 0 to ~100k DALYs per year is wide.
- The tongue-swab and NPOC WHO endorsement (Feb 2026) lowers the counterfactual incremental value relative to what the Investigator assumed. The paediatric and no-sputum gap remains.
- Mark it **UNGROUNDED, small magnitude, direction uncertain**.
- The cost-attribution question should be resolved from the model, not from this critique.

---

## Critique 3: 60% steady-state uptake has no precedent among comparable additions

**OVERALL VERDICT: PARTIALLY VERIFIED.** Slow ramps are well supported. The claim that the ceiling is below 60% is not. The title's "no precedent" is overstated.

**CITATION CHECK**
- *Xpert MTB/RIF, WHO endorsement 2010.* **VERIFIED in outline.** 
Since 2011, rapid molecular tests have transformed the TB diagnostic landscape
.
- *WRD coverage "roughly 40–50% in recent reports".* **PARTIALLY VERIFIED.** The global figure was 
54% in 2024, up from 47% in 2022
, and 48% in 2023. The Investigator's range is slightly low. The WRD indicator also covers all WHO-recommended rapid tests, not just Xpert.
- *4-month rifapentine-moxifloxacin, WHO 2022.* **VERIFIED, with strong support for slow uptake.** 
Only 4,154 people were reported started on 4-month HPMZ in 2024, up from 1,271 in 2023
. That is about 0.05% of the 8.3M notified. 
Uptake has been slow, largely because of limited rifapentine availability
. The WHO page also says 
15 countries and areas reported using the regimen by end-2024
. A second list on the same page gives 26.
- *Dexamethasone for TBM (evidence 2004).* **UNVERIFIED.** I did not retrieve coverage data. The 2004 trial is real from background knowledge, but its uptake history needs checking.
- *Pyridoxine with isoniazid recommended but inconsistently supplied.* **UNVERIFIED.** No coverage data retrieved.

**CLAIM CHECK**
- *Reducing the ceiling to 0.30–0.40 cuts SROI by 33–50%.* **VERIFIED as arithmetic.** 0.40/0.60 is a 33% cut and 0.30/0.60 is a 50% cut, assuming linear dependence. The model structure and the "0.39 materiality line" are unverifiable.
- *Comparable additions "often" stall below 50%.* **PARTIALLY CONTRADICTED.** Global WRD coverage is 54% after about 14 years and still rising, not stalled below 50%. WHO also reports that 
37 of 49 high-burden countries used a WRD as the initial test for more than half of notified cases in 2024, up from 31 in 2023
. This is evidence of a slow ramp, not a ceiling.
- *An adjunct with no visible patient benefit is a harder sell.* **PLAUSIBLE, no direct evidence.** It is a reasonable argument.
- *The ramp matters little over an infinite horizon.* **LOGICALLY VALID**, with the discounting caveat the Investigator notes.

**EVIDENCE FOUND**
- The analogs have key differences from a cheap generic oral adjunct. Xpert needs capital equipment and labs. HPMZ is supply-limited by rifapentine, and the NYC experience showed tolerability problems: 
only 14% of eligible patients were prescribed it, and 64% of those who started discontinued
. Neither is a clean analog for generic-drug supply, so they bear on the ramp more than on the ceiling.
- The global target is 100% WRD coverage by 2027 (
set at the 2023 UN high-level meeting
). A system target is not the same as steady-state achieved coverage, but it suggests over 50% is feasible with sustained push.
- Equating adult_uptake with a coverage fraction among all patients may be a different construct from "percent of notified cases tested". I could not check how the CG model defines it.

**CORE CLAIM**
- Claim: the long-run uptake ceiling is plausibly 0.30–0.40, not 0.60.
- Support: **LOGIC ONLY.**
- Why: the precedents show slow ramps (HPMZ about 0.05% after three years, WRD 54% after about 14 years). None shows a stalled ceiling below 60% for a cheap, generic, oral co-administered drug.

**REVISED CRITIQUE**
- Evidence supports the view that new TB tools take about 10 or more years to reach about 50% coverage, and that guideline endorsement does not guarantee uptake.
- This is a stronger argument against the ramp (timing) than against the ceiling. Its main effect is through discounting and finite horizons.
- Retain the ceiling concern as **UNGROUNDED**. Downgrade the magnitude from **large to medium**, with direction **decreases**.
- Do not use "stall below 50%" as support for the 0.30–0.40 ceiling. The WRD data point to 54% and rising.
- Dexamethasone and pyridoxine remain unverified. The pull the Investigator requested has been done for WRD and HPMZ. The GDF order data were not found.

--- Critique: 60% steady-state uptake has no precedent among comparable TB program additions ---

## Critique 1: Lung benefit without mortality benefit is worth less than a simple p_success weighting implies

**OVERALL VERDICT: PARTIALLY VERIFIED.** The logic holds, but it is ungrounded. Its inputs are unverified and its labelled direction is inconsistent.

**CLAIM CHECK**
- *"A surrogate-only (lung) result would not obviously lead to adoption at 60% scale."* **PLAUSIBLE, no direct evidence.** I found no WHO guideline text on how lung-function surrogates are weighed. I did not find the CG model, the specific trial, or its registered Phase IIc and Phase III endpoints, so these remain **UNVERIFIABLE**.
- *Conditional adoption of 10–20% in the "mortality fails, lung holds" branch.* **UNVERIFIABLE.** The Investigator already labels it UNGROUNDED.
- *The 0.45, 0.4 base and 60% uptake figures, and the 3.3M patients.* **UNVERIFIABLE.** These come from the CG model, which I could not access.
- *Arithmetic.*
  - The "realistic" range checks out: 0.6 × (0.3–0.5) × (0.1–0.2) ≈ 0.018–0.06.
  - The "naive" bound is overstated. 0.4 + 0.6 × (0.3–0.5) gives about 0.58–0.70, which is roughly 1.3–1.6× of 0.45, not "up to ~2×". A 2× result would need P(lung holds | mortality fails) near 1.
- *Direction label.* The critique argues that the 0.45 figure is about right and that the upside is limited. It is labelled "increases", which does not match that argument. Its net effect is closer to neutral. It is a caution against over-crediting the lung channel.

**EVIDENCE FOUND**
- 
Few tuberculosis treatment trials have included lung function as a primary efficacy outcome
, although 
FEV1 correlates with long-term mortality
. This supports the premise that lung function is a non-standard endpoint, so a lung-only win may not translate cleanly into guidelines.
- The phase 2 trial by Wallis et al. found that 
CC-11050 and everolimus might enhance the recovery of FEV1
. FEV1 was therefore used as a preliminary efficacy signal, not as an established registrational endpoint.
- Phase IIc in TB normally means the STEP design. 
CRUSH-TB, for example, uses time to sputum culture negativity as its primary intermediate endpoint
. A trial in this style would not natively produce a lung-function primary endpoint. This is circumstantial, because I could not identify the CG-funded trial.

**CORE CLAIM**
- Claim: conditional adoption in the lung-only branch is far below 60% (about 10–20%).
- Support: **LOGIC ONLY.**
- Why: the reasoning is plausible, and lung function is a non-standard TB endpoint, but I found no direct evidence on WHO or adoption behaviour for this branch.

**REVISED CRITIQUE**
- Retain this as a **weighting caution, flagged UNGROUNDED**. Do not apply the full uptake to the lung-only branch without a separate adoption discount.
- The effect is modest: roughly +0.02–0.06 on a 0.4 base.
- Fix the "up to 2×" figure to about 1.3–1.6×. Treat the direction as neutral to slightly decreasing, with small magnitude.

---

## Critique 2: Sweat-based diagnostic option value (~10–30k central)

**OVERALL VERDICT: UNVERIFIABLE for the specific test. The background facts are verified.** Retain it as a flagged, low-confidence hypothesis.

**CLAIM CHECK**
- *CG funds a sweat-based TB diagnostic alongside the trial.* **UNVERIFIABLE.** I found nothing on this test's development stage, accuracy or regulatory path, or on the funding link.
- *Roughly 2–3M TB cases per year are undiagnosed or unreported.* **VERIFIED.** 
8.3 million people were newly diagnosed with TB in 2024, which is 78% of the estimated incident cases
. 
Estimated incidence was 10.7 million
, so the gap is about 2.4M.
- *Non-sputum competitors are advancing (tongue swab).* **VERIFIED, and ahead of the Investigator's expectation.** 
WHO has issued its first recommendations on near-point-of-care molecular tests and easy-to-collect tongue swab samples
, in February 2026. The Investigator had not checked WHO endorsements. The accuracy evidence is 
tongue-swab performance meeting the minimum WHO non-sputum target (>75% sensitivity, >98% specificity)
.
- *Urine LAM as a competitor.* **PLAUSIBLE.** The LF-LAM assays are named in the WHO report as a bacteriological confirmation method.
- *Arithmetic.* 0.05 × 200k × 5 = 50k DALYs per year, which is correct. The 20% untreated case fatality and 25 DALYs per death are unverified assumptions. Widely cited untreated-TB fatality figures are higher than 20%, so these are not clearly inflated.
- *Whether the $7M all-in cost includes the diagnostic.* **UNVERIFIABLE.** I could not see the model. The Investigator correctly flags this as a consistency check for the CG model owner.

**EVIDENCE FOUND**
- WHO's tongue-swab recommendation has a limited scope. 
Programmes may use tongue swabs from adults and adolescents when sputum cannot be obtained
. Children and others who cannot give sputum are therefore not covered by that recommendation. This leaves some room for a different non-sputum test, which mildly supports the critique's option-value logic.
- Against that, 
tongue swabs are less sensitive than sputum
. The counterfactual is also moving fast. The base case for "incremental cases beyond alternatives" at 1–3% of incidence is therefore uncertain. Counterfactual displacement could push the value toward the low end.
- The tongue-swab and NPOC tests are PCR-based. A sweat-based test would need its own evidence pathway and WHO policy review, which supports the low adoption probability.

**CORE CLAIM**
- Claim: P(adoption) ≈ 5% with an incremental yield of 1–3% of incidence, giving about 10–30k DALYs per year.
- Support: **LOGIC ONLY.**
- Why: the arithmetic is internally consistent, but the probability and yield inputs are an assumed base rate with no source, and the test itself could not be found.

**REVISED CRITIQUE**
- CG assigns zero value to the sweat test. This may understate value, but the amount is speculative, and the range of 0 to ~100k DALYs per year is wide.
- The tongue-swab and NPOC WHO endorsement (Feb 2026) lowers the counterfactual incremental value relative to what the Investigator assumed. The paediatric and no-sputum gap remains.
- Mark it **UNGROUNDED, small magnitude, direction uncertain**.
- The cost-attribution question should be resolved from the model, not from this critique.

---

## Critique 3: 60% steady-state uptake has no precedent among comparable additions

**OVERALL VERDICT: PARTIALLY VERIFIED.** Slow ramps are well supported. The claim that the ceiling is below 60% is not. The title's "no precedent" is overstated.

**CITATION CHECK**
- *Xpert MTB/RIF, WHO endorsement 2010.* **VERIFIED in outline.** 
Since 2011, rapid molecular tests have transformed the TB diagnostic landscape
.
- *WRD coverage "roughly 40–50% in recent reports".* **PARTIALLY VERIFIED.** The global figure was 
54% in 2024, up from 47% in 2022
, and 48% in 2023. The Investigator's range is slightly low. The WRD indicator also covers all WHO-recommended rapid tests, not just Xpert.
- *4-month rifapentine-moxifloxacin, WHO 2022.* **VERIFIED, with strong support for slow uptake.** 
Only 4,154 people were reported started on 4-month HPMZ in 2024, up from 1,271 in 2023
. That is about 0.05% of the 8.3M notified. 
Uptake has been slow, largely because of limited rifapentine availability
. The WHO page also says 
15 countries and areas reported using the regimen by end-2024
. A second list on the same page gives 26.
- *Dexamethasone for TBM (evidence 2004).* **UNVERIFIED.** I did not retrieve coverage data. The 2004 trial is real from background knowledge, but its uptake history needs checking.
- *Pyridoxine with isoniazid recommended but inconsistently supplied.* **UNVERIFIED.** No coverage data retrieved.

**CLAIM CHECK**
- *Reducing the ceiling to 0.30–0.40 cuts SROI by 33–50%.* **VERIFIED as arithmetic.** 0.40/0.60 is a 33% cut and 0.30/0.60 is a 50% cut, assuming linear dependence. The model structure and the "0.39 materiality line" are unverifiable.
- *Comparable additions "often" stall below 50%.* **PARTIALLY CONTRADICTED.** Global WRD coverage is 54% after about 14 years and still rising, not stalled below 50%. WHO also reports that 
37 of 49 high-burden countries used a WRD as the initial test for more than half of notified cases in 2024, up from 31 in 2023
. This is evidence of a slow ramp, not a ceiling.
- *An adjunct with no visible patient benefit is a harder sell.* **PLAUSIBLE, no direct evidence.** It is a reasonable argument.
- *The ramp matters little over an infinite horizon.* **LOGICALLY VALID**, with the discounting caveat the Investigator notes.

**EVIDENCE FOUND**
- The analogs have key differences from a cheap generic oral adjunct. Xpert needs capital equipment and labs. HPMZ is supply-limited by rifapentine, and the NYC experience showed tolerability problems: 
only 14% of eligible patients were prescribed it, and 64% of those who started discontinued
. Neither is a clean analog for generic-drug supply, so they bear on the ramp more than on the ceiling.
- The global target is 100% WRD coverage by 2027 (
set at the 2023 UN high-level meeting
). A system target is not the same as steady-state achieved coverage, but it suggests over 50% is feasible with sustained push.
- Equating adult_uptake with a coverage fraction among all patients may be a different construct from "percent of notified cases tested". I could not check how the CG model defines it.

**CORE CLAIM**
- Claim: the long-run uptake ceiling is plausibly 0.30–0.40, not 0.60.
- Support: **LOGIC ONLY.**
- Why: the precedents show slow ramps (HPMZ about 0.05% after three years, WRD 54% after about 14 years). None shows a stalled ceiling below 60% for a cheap, generic, oral co-administered drug.

**REVISED CRITIQUE**
- Evidence supports the view that new TB tools take about 10 or more years to reach about 50% coverage, and that guideline endorsement does not guarantee uptake.
- This is a stronger argument against the ramp (timing) than against the ceiling. Its main effect is through discounting and finite horizons.
- Retain the ceiling concern as **UNGROUNDED**. Downgrade the magnitude from **large to medium**, with direction **decreases**.
- Do not use "stall below 50%" as support for the 0.30–0.40 ceiling. The WRD data point to 54% and rising.
- Dexamethasone and pyridoxine remain unverified. The pull the Investigator requested has been done for WRD and HPMZ. The GDF order data were not found.

--- Critique: A Phase III cannot be powered on mortality, so the WHO GDG would be recommending on surrogate or composite endpoints ---

## Critique 1: Phase III cannot be powered on mortality, so the WHO GDG would recommend on surrogate or composite endpoints

**OVERALL VERDICT: PARTIALLY VERIFIED.** The sample-size arithmetic and the GRADE indirectness logic hold. The baseline mortality is now grounded. The link from this to lower uptake is logic only, and the critique overstates how much a lack of mortality data would hurt in TB guidelines.

**CLAIM CHECK**
- **Sample size of about 30,000 per arm (5% baseline, 10% relative reduction, α 0.05, 80% power): VERIFIED (arithmetic).**
  - I recomputed it with the standard two-proportion formula: 7.84 × (0.0475 + 0.0430) / 0.005² ≈ 28,400 per arm. The Investigator's shortcut gives about 29,800. Both round to roughly 28–30k per arm.
  - The result depends entirely on the 5% baseline and the 10% effect, as the Investigator said.
- **On-treatment DS-TB mortality of about 3–6% (previously UNGROUNDED): PLAUSIBLE, now sourced.**
  - 
A program-setting cohort of drug-susceptible pulmonary TB found 37 of 565 patients (6.6%) died during the study period.

  - 
In Kenya, about 6% of drug-susceptible TB cases died.

  - 
A multi-country study reported mortality of 6.0% in adequately treated patients with pan-susceptible strains.

  - 
WHO reports DS-TB treatment success of 88% (2023 data).
 That is consistent with deaths of roughly 4–6%, but I did not retrieve the exact WHO death proportion.
  - The "3–6%" range is therefore reasonable. Cohorts with HIV or severe disease run higher, so the range sits at the low-to-mid end of what is reported.
- **GRADE downgrades for indirectness when surrogate outcomes are used: VERIFIED.**
  - 
WHO SAGE guidance says that when important outcomes are represented by a surrogate, the evidence quality frequently needs down-rating for indirectness.

  - 
A WHO guideline applying the Handbook (2nd edition) downgrades for indirectness when the evidence differs from the target context in populations, interventions, comparisons or outcomes.

  - I did not retrieve the Handbook text itself. The two sources above are WHO documents applying it.
- **Recommendation delayed, conditional or subgroup-only: PLAUSIBLE.** This is a reasonable inference. It is not a documented outcome for any specific TB adjunct.
- **Effective uptake would fall by about half or more under a subgroup recommendation: UNVERIFIABLE.** The Investigator already flagged this as speculative.

**EVIDENCE FOUND**
- **Weakens the critique.** WHO TB guideline groups routinely treat composite patient-important outcomes (treatment success, unfavourable outcome including death, relapse) as critical outcomes.
  - The critique treats a composite as a weak substitute. In TB, a composite that includes death is often a direct outcome. That reduces the expected indirectness penalty.
  - This is from my background knowledge. I did not search for it.
- **Supports the critique.** The only statin RCT I found, StAT-TB, is a Phase 2b dose-finding trial. 
Its endpoints are time to sputum-culture negativity and lung function.
 
Mortality is assessed as a tolerability measure.
 Mortality is not the primary efficacy endpoint.
- Observational data link statin use to lower all-cause mortality in TB patients with ASCVD. 
The authors say RCTs are needed.
 That is a narrow subgroup, and it supports the case for a subgroup-limited recommendation.

**CORE CLAIM**
- **Claim:** A Phase III cannot be powered on a roughly 10% relative mortality reduction (about 30k per arm), so the recommendation would rest on surrogate or composite endpoints that GRADE treats as indirect.
- **Support:** SUPPORTED, for the feasibility and GRADE-mechanism part. The effect on uptake is LOGIC ONLY.
- **Why:** The arithmetic reproduces, baseline mortality sits in the claimed range, and WHO guidance confirms the downgrading mechanism. No evidence ties this to a specific uptake reduction.

**REVISED CRITIQUE**
A mortality-powered Phase III would need about 28–30k patients per arm at a 5–6% baseline. A mortality-driven benefit would therefore probably be inferred from composite or surrogate endpoints. That invites an indirectness downgrade. It could make the recommendation conditional, delayed or subgroup-limited, and it raises variance on the realized relative reduction. Counterweight: TB GDGs usually accept unfavourable-outcome composites that include death as direct. The uptake and timing effects are UNGROUNDED. **Magnitude: low-to-medium** (downgraded from medium). Direction: decreases.

---

## Critique 2: Clinical eligibility and monitoring barriers cap the prescribing share

**OVERALL VERDICT: PARTIALLY VERIFIED.** The hepatotoxicity premise is verified. The numeric uptake cap is ungrounded. Several pharmacology points are likely mismatched to the statin actually under study.

**CLAIM CHECK**
- **Anti-TB DILI is common, "low single digits to ~10%": PARTIALLY VERIFIED.**
  - 
A recent meta-analysis reported a global incidence of 11.5%, with rates varying from 2% to 28%.

  - 
Another source cites 3–36% for drug-susceptible TB.

  - 
Incidence varies with the cohort, regimen, DILI threshold and monitoring.

  - The Investigator's range is directionally right but understates the upper end. If anything, DILI is more common than stated, which strengthens the premise. The Investigator said they could not cite a paper. Wang et al. (2022), a meta-analysis of 160 studies, is the relevant one.
- **Rifampicin is a strong CYP3A4 inducer: VERIFIED.** 
Rifampin is a strong inducer of CYP3A4 and 2C19.

- **Specific ART interactions (PI-boosted raises atorvastatin, efavirenz lowers it): UNVERIFIED.** I did not check the Liverpool database. This is standard pharmacology and plausible.
- **Statin label warnings for liver disease and pregnancy: PLAUSIBLE but possibly outdated.** I did not search this. From background knowledge, FDA labelling was revised after 2012 to drop routine periodic LFT monitoring. The pregnancy contraindication was also relaxed in 2021. The "mandated LFT monitoring" scenario is therefore weaker than the critique implies.
- **Exclusion of 10–20% of adults, bringing 0.60 to 0.45–0.50: UNVERIFIABLE.** The Investigator labelled it illustrative and ungrounded. I found no data.
- **Many NTPs do not routinely perform LFTs in DS-TB: PLAUSIBLE.** I found no direct source. WHO guidance recommends symptom-based monitoring for most patients, which is consistent with it.

**EVIDENCE FOUND**
- **Statin identity matters.** The Phase 2b trial (StAT-TB) tests pravastatin. 
It asks whether pravastatin adjunctive therapy shortens time to sputum-culture negativity and improves lung function.

  - 
In preclinical work, atorvastatin and mevastatin did not inhibit Mtb growth in THP-1 cells at nontoxic doses.
 
Pravastatin showed the least toxicity in that study.

  - From background knowledge, pravastatin is not substantially CYP3A4-metabolised. If CG's candidate is pravastatin, the CYP3A4 and PI-boosted ART interaction arguments largely fall away. The hepatotoxicity-attribution and pill-burden arguments remain.
  - I do not know which statin CG assumes. The Investigator should have flagged that dependence.
- 
The DILI meta-analysis authors say regular liver function monitoring is imperative during anti-TB treatment.
 This supports the premise that monitoring is a live issue, though it is not specific to statins.

**CORE CLAIM**
- **Claim:** Eligibility exclusions, DILI-attribution concerns and monitoring requirements would cut adult uptake from about 0.60 to about 0.45–0.50.
- **Support:** LOGIC ONLY.
- **Why:** The mechanisms are plausible and the DILI base rate is verified, but I found no evidence for the size of the exclusion or program-reluctance effect.

**REVISED CRITIQUE**
Anti-TB DILI is common, with a pooled incidence of about 11.5% and a range of roughly 2–28% or more. Clinicians may be reluctant to add a hepatically relevant agent that confounds attribution. Some eligibility exclusion (liver disease, pregnancy, polypharmacy) is therefore plausible. The cited drug-interaction concerns apply to CYP3A4-metabolised statins such as atorvastatin, not necessarily to pravastatin, which is the statin in the Phase 2b trial. The specific 0.45–0.50 figure is **UNGROUNDED — plausible but needs empirical support.** **Magnitude: low-to-medium.** Direction: decreases.

---

## Critique 3: Delivered dose and adherence diverge from trial conditions, especially with rifapentine regimens

**OVERALL VERDICT: PARTIALLY VERIFIED.** The general adherence and effectiveness-gap logic is sound. The rifapentine claim is overstated relative to the sources. The adherence factor risks double-counting.

**CLAIM CHECK**
- **Rifapentine is a strong CYP3A4 inducer, "comparable to or stronger than rifampicin in some dosing contexts": PARTIALLY VERIFIED, mostly contradicted on direction.**
  - 
One review ranks relative inductive potency as rifampin > rifapentine > rifabutin. It says rifapentine's CYP3A4 induction approaches rifampin's (85–100%) with daily dosing and is more moderate with once- or twice-weekly dosing.

  - 
The WHO prequalification document says rifapentine's induction potential may be less than rifampicin's but more potent than rifabutin's.

  - 
A clinical protocol gives relative potency as rifampin 100%, rifapentine 85% and rifabutin 40%.

  - There is supporting evidence for "stronger in some contexts." 
In one study, oral midazolam AUC fell 75% with rifampin versus 92% with rifapentine, each at 10 mg/kg daily.

  - 
One in vitro hepatocyte study found rifapentine to be the weakest of the three inducers.

  - The evidence is mixed. It does not support the stronger claim that HPMZ regimens would lower statin exposure "further" than rifampicin regimens. Daily rifapentine dosing, as in HPMZ, is the condition where induction is closest to rifampicin's. A modest difference in either direction is the best-supported reading.
- **HPMZ is a 4-month rifapentine-containing regimen that programs are moving toward, with a currently small but growing share: PLAUSIBLE.** I did not search this. From background knowledge, WHO recommended it in 2022. I have no uptake share data.
- **Statin non-adherence is high in general populations: PLAUSIBLE, not searched.** It is a well-known finding, but it was not checked for the TB context.
- **Adjunct pills outside an FDC are less likely to be taken than anti-TB drugs: PLAUSIBLE.** The Investigator admitted there is no specific source, and I found none.
- **0.60 × 0.70 = 0.42, about a 30% reduction: VERIFIED (arithmetic).** The 70% adherence figure is an assumption.
- **Dose-finding on one regimen may not carry over: PLAUSIBLE.** StAT-TB tests statins with first-line HRZE. 
The protocol describes testing statins in combination with first-line TB drugs.


**EVIDENCE FOUND**
- **Possible double-counting.** If the Phase III is pragmatic or intention-to-treat, the effect size already embeds trial-level non-adherence. Applying an adherence haircut again to uptake would then overstate the downward adjustment. The Investigator did not address this.
- **Statin identity again.** If pravastatin is the candidate, rifamycin CYP3A4 induction is a minor concern. The rifapentine-specific argument then largely falls away.
- The critique says it "compounds with Critiques 1 and 3". That appears to be a self-reference error and should probably read 1 and 2.

**CORE CLAIM**
- **Claim:** Real-world delivered dose and adherence (about 70%) would reduce effective uptake by about 30%, and rifapentine regimens would further lower statin exposure.
- **Support:** LOGIC ONLY for the adherence factor. The rifapentine "further lower" claim is weakly supported to partly contradicted.
- **Why:** The effectiveness-gap mechanism is generic and plausible. The 70% is assumed, and most pharmacology sources rank rifapentine at or below rifampicin for CYP3A4 induction.

**REVISED CRITIQUE**
Programmatic adherence to an unsupervised adjunct pill is likely below trial adherence, and this lowers realized benefit. The size of the effect is **UNGROUNDED — plausible but needs empirical support.** The 70% figure is an assumption, and it risks double-counting if the trial effect is already pragmatic or intention-to-treat. The rifapentine point is weaker than stated. Daily rifapentine induces CYP3A4 at roughly 85–100% of rifampicin's level. That is similar to the interaction already present in HRZE-based trials, not clearly worse, and it matters only for CYP3A4-metabolised statins. **Magnitude: low-to-medium** (downgraded from medium). Direction: decreases.

--- Critique: Clinical eligibility and monitoring barriers cap the achievable prescribing share below the "generic and cheap" logic ---

## Critique 1: Phase III cannot be powered on mortality, so the WHO GDG would recommend on surrogate or composite endpoints

**OVERALL VERDICT: PARTIALLY VERIFIED.** The sample-size arithmetic and the GRADE indirectness logic hold. The baseline mortality is now grounded. The link from this to lower uptake is logic only, and the critique overstates how much a lack of mortality data would hurt in TB guidelines.

**CLAIM CHECK**
- **Sample size of about 30,000 per arm (5% baseline, 10% relative reduction, α 0.05, 80% power): VERIFIED (arithmetic).**
  - I recomputed it with the standard two-proportion formula: 7.84 × (0.0475 + 0.0430) / 0.005² ≈ 28,400 per arm. The Investigator's shortcut gives about 29,800. Both round to roughly 28–30k per arm.
  - The result depends entirely on the 5% baseline and the 10% effect, as the Investigator said.
- **On-treatment DS-TB mortality of about 3–6% (previously UNGROUNDED): PLAUSIBLE, now sourced.**
  - 
A program-setting cohort of drug-susceptible pulmonary TB found 37 of 565 patients (6.6%) died during the study period.

  - 
In Kenya, about 6% of drug-susceptible TB cases died.

  - 
A multi-country study reported mortality of 6.0% in adequately treated patients with pan-susceptible strains.

  - 
WHO reports DS-TB treatment success of 88% (2023 data).
 That is consistent with deaths of roughly 4–6%, but I did not retrieve the exact WHO death proportion.
  - The "3–6%" range is therefore reasonable. Cohorts with HIV or severe disease run higher, so the range sits at the low-to-mid end of what is reported.
- **GRADE downgrades for indirectness when surrogate outcomes are used: VERIFIED.**
  - 
WHO SAGE guidance says that when important outcomes are represented by a surrogate, the evidence quality frequently needs down-rating for indirectness.

  - 
A WHO guideline applying the Handbook (2nd edition) downgrades for indirectness when the evidence differs from the target context in populations, interventions, comparisons or outcomes.

  - I did not retrieve the Handbook text itself. The two sources above are WHO documents applying it.
- **Recommendation delayed, conditional or subgroup-only: PLAUSIBLE.** This is a reasonable inference. It is not a documented outcome for any specific TB adjunct.
- **Effective uptake would fall by about half or more under a subgroup recommendation: UNVERIFIABLE.** The Investigator already flagged this as speculative.

**EVIDENCE FOUND**
- **Weakens the critique.** WHO TB guideline groups routinely treat composite patient-important outcomes (treatment success, unfavourable outcome including death, relapse) as critical outcomes.
  - The critique treats a composite as a weak substitute. In TB, a composite that includes death is often a direct outcome. That reduces the expected indirectness penalty.
  - This is from my background knowledge. I did not search for it.
- **Supports the critique.** The only statin RCT I found, StAT-TB, is a Phase 2b dose-finding trial. 
Its endpoints are time to sputum-culture negativity and lung function.
 
Mortality is assessed as a tolerability measure.
 Mortality is not the primary efficacy endpoint.
- Observational data link statin use to lower all-cause mortality in TB patients with ASCVD. 
The authors say RCTs are needed.
 That is a narrow subgroup, and it supports the case for a subgroup-limited recommendation.

**CORE CLAIM**
- **Claim:** A Phase III cannot be powered on a roughly 10% relative mortality reduction (about 30k per arm), so the recommendation would rest on surrogate or composite endpoints that GRADE treats as indirect.
- **Support:** SUPPORTED, for the feasibility and GRADE-mechanism part. The effect on uptake is LOGIC ONLY.
- **Why:** The arithmetic reproduces, baseline mortality sits in the claimed range, and WHO guidance confirms the downgrading mechanism. No evidence ties this to a specific uptake reduction.

**REVISED CRITIQUE**
A mortality-powered Phase III would need about 28–30k patients per arm at a 5–6% baseline. A mortality-driven benefit would therefore probably be inferred from composite or surrogate endpoints. That invites an indirectness downgrade. It could make the recommendation conditional, delayed or subgroup-limited, and it raises variance on the realized relative reduction. Counterweight: TB GDGs usually accept unfavourable-outcome composites that include death as direct. The uptake and timing effects are UNGROUNDED. **Magnitude: low-to-medium** (downgraded from medium). Direction: decreases.

---

## Critique 2: Clinical eligibility and monitoring barriers cap the prescribing share

**OVERALL VERDICT: PARTIALLY VERIFIED.** The hepatotoxicity premise is verified. The numeric uptake cap is ungrounded. Several pharmacology points are likely mismatched to the statin actually under study.

**CLAIM CHECK**
- **Anti-TB DILI is common, "low single digits to ~10%": PARTIALLY VERIFIED.**
  - 
A recent meta-analysis reported a global incidence of 11.5%, with rates varying from 2% to 28%.

  - 
Another source cites 3–36% for drug-susceptible TB.

  - 
Incidence varies with the cohort, regimen, DILI threshold and monitoring.

  - The Investigator's range is directionally right but understates the upper end. If anything, DILI is more common than stated, which strengthens the premise. The Investigator said they could not cite a paper. Wang et al. (2022), a meta-analysis of 160 studies, is the relevant one.
- **Rifampicin is a strong CYP3A4 inducer: VERIFIED.** 
Rifampin is a strong inducer of CYP3A4 and 2C19.

- **Specific ART interactions (PI-boosted raises atorvastatin, efavirenz lowers it): UNVERIFIED.** I did not check the Liverpool database. This is standard pharmacology and plausible.
- **Statin label warnings for liver disease and pregnancy: PLAUSIBLE but possibly outdated.** I did not search this. From background knowledge, FDA labelling was revised after 2012 to drop routine periodic LFT monitoring. The pregnancy contraindication was also relaxed in 2021. The "mandated LFT monitoring" scenario is therefore weaker than the critique implies.
- **Exclusion of 10–20% of adults, bringing 0.60 to 0.45–0.50: UNVERIFIABLE.** The Investigator labelled it illustrative and ungrounded. I found no data.
- **Many NTPs do not routinely perform LFTs in DS-TB: PLAUSIBLE.** I found no direct source. WHO guidance recommends symptom-based monitoring for most patients, which is consistent with it.

**EVIDENCE FOUND**
- **Statin identity matters.** The Phase 2b trial (StAT-TB) tests pravastatin. 
It asks whether pravastatin adjunctive therapy shortens time to sputum-culture negativity and improves lung function.

  - 
In preclinical work, atorvastatin and mevastatin did not inhibit Mtb growth in THP-1 cells at nontoxic doses.
 
Pravastatin showed the least toxicity in that study.

  - From background knowledge, pravastatin is not substantially CYP3A4-metabolised. If CG's candidate is pravastatin, the CYP3A4 and PI-boosted ART interaction arguments largely fall away. The hepatotoxicity-attribution and pill-burden arguments remain.
  - I do not know which statin CG assumes. The Investigator should have flagged that dependence.
- 
The DILI meta-analysis authors say regular liver function monitoring is imperative during anti-TB treatment.
 This supports the premise that monitoring is a live issue, though it is not specific to statins.

**CORE CLAIM**
- **Claim:** Eligibility exclusions, DILI-attribution concerns and monitoring requirements would cut adult uptake from about 0.60 to about 0.45–0.50.
- **Support:** LOGIC ONLY.
- **Why:** The mechanisms are plausible and the DILI base rate is verified, but I found no evidence for the size of the exclusion or program-reluctance effect.

**REVISED CRITIQUE**
Anti-TB DILI is common, with a pooled incidence of about 11.5% and a range of roughly 2–28% or more. Clinicians may be reluctant to add a hepatically relevant agent that confounds attribution. Some eligibility exclusion (liver disease, pregnancy, polypharmacy) is therefore plausible. The cited drug-interaction concerns apply to CYP3A4-metabolised statins such as atorvastatin, not necessarily to pravastatin, which is the statin in the Phase 2b trial. The specific 0.45–0.50 figure is **UNGROUNDED — plausible but needs empirical support.** **Magnitude: low-to-medium.** Direction: decreases.

---

## Critique 3: Delivered dose and adherence diverge from trial conditions, especially with rifapentine regimens

**OVERALL VERDICT: PARTIALLY VERIFIED.** The general adherence and effectiveness-gap logic is sound. The rifapentine claim is overstated relative to the sources. The adherence factor risks double-counting.

**CLAIM CHECK**
- **Rifapentine is a strong CYP3A4 inducer, "comparable to or stronger than rifampicin in some dosing contexts": PARTIALLY VERIFIED, mostly contradicted on direction.**
  - 
One review ranks relative inductive potency as rifampin > rifapentine > rifabutin. It says rifapentine's CYP3A4 induction approaches rifampin's (85–100%) with daily dosing and is more moderate with once- or twice-weekly dosing.

  - 
The WHO prequalification document says rifapentine's induction potential may be less than rifampicin's but more potent than rifabutin's.

  - 
A clinical protocol gives relative potency as rifampin 100%, rifapentine 85% and rifabutin 40%.

  - There is supporting evidence for "stronger in some contexts." 
In one study, oral midazolam AUC fell 75% with rifampin versus 92% with rifapentine, each at 10 mg/kg daily.

  - 
One in vitro hepatocyte study found rifapentine to be the weakest of the three inducers.

  - The evidence is mixed. It does not support the stronger claim that HPMZ regimens would lower statin exposure "further" than rifampicin regimens. Daily rifapentine dosing, as in HPMZ, is the condition where induction is closest to rifampicin's. A modest difference in either direction is the best-supported reading.
- **HPMZ is a 4-month rifapentine-containing regimen that programs are moving toward, with a currently small but growing share: PLAUSIBLE.** I did not search this. From background knowledge, WHO recommended it in 2022. I have no uptake share data.
- **Statin non-adherence is high in general populations: PLAUSIBLE, not searched.** It is a well-known finding, but it was not checked for the TB context.
- **Adjunct pills outside an FDC are less likely to be taken than anti-TB drugs: PLAUSIBLE.** The Investigator admitted there is no specific source, and I found none.
- **0.60 × 0.70 = 0.42, about a 30% reduction: VERIFIED (arithmetic).** The 70% adherence figure is an assumption.
- **Dose-finding on one regimen may not carry over: PLAUSIBLE.** StAT-TB tests statins with first-line HRZE. 
The protocol describes testing statins in combination with first-line TB drugs.


**EVIDENCE FOUND**
- **Possible double-counting.** If the Phase III is pragmatic or intention-to-treat, the effect size already embeds trial-level non-adherence. Applying an adherence haircut again to uptake would then overstate the downward adjustment. The Investigator did not address this.
- **Statin identity again.** If pravastatin is the candidate, rifamycin CYP3A4 induction is a minor concern. The rifapentine-specific argument then largely falls away.
- The critique says it "compounds with Critiques 1 and 3". That appears to be a self-reference error and should probably read 1 and 2.

**CORE CLAIM**
- **Claim:** Real-world delivered dose and adherence (about 70%) would reduce effective uptake by about 30%, and rifapentine regimens would further lower statin exposure.
- **Support:** LOGIC ONLY for the adherence factor. The rifapentine "further lower" claim is weakly supported to partly contradicted.
- **Why:** The effectiveness-gap mechanism is generic and plausible. The 70% is assumed, and most pharmacology sources rank rifapentine at or below rifampicin for CYP3A4 induction.

**REVISED CRITIQUE**
Programmatic adherence to an unsupervised adjunct pill is likely below trial adherence, and this lowers realized benefit. The size of the effect is **UNGROUNDED — plausible but needs empirical support.** The 70% figure is an assumption, and it risks double-counting if the trial effect is already pragmatic or intention-to-treat. The rifapentine point is weaker than stated. Daily rifapentine induces CYP3A4 at roughly 85–100% of rifampicin's level. That is similar to the interaction already present in HRZE-based trials, not clearly worse, and it matters only for CYP3A4-metabolised statins. **Magnitude: low-to-medium** (downgraded from medium). Direction: decreases.

--- Critique: Effective delivered dose and adherence diverge from trial conditions, and programmatic dose may be lower than the trial dose, notably with rifapentine regimens ---

## Critique 1: Phase III cannot be powered on mortality, so the WHO GDG would recommend on surrogate or composite endpoints

**OVERALL VERDICT: PARTIALLY VERIFIED.** The sample-size arithmetic and the GRADE indirectness logic hold. The baseline mortality is now grounded. The link from this to lower uptake is logic only, and the critique overstates how much a lack of mortality data would hurt in TB guidelines.

**CLAIM CHECK**
- **Sample size of about 30,000 per arm (5% baseline, 10% relative reduction, α 0.05, 80% power): VERIFIED (arithmetic).**
  - I recomputed it with the standard two-proportion formula: 7.84 × (0.0475 + 0.0430) / 0.005² ≈ 28,400 per arm. The Investigator's shortcut gives about 29,800. Both round to roughly 28–30k per arm.
  - The result depends entirely on the 5% baseline and the 10% effect, as the Investigator said.
- **On-treatment DS-TB mortality of about 3–6% (previously UNGROUNDED): PLAUSIBLE, now sourced.**
  - 
A program-setting cohort of drug-susceptible pulmonary TB found 37 of 565 patients (6.6%) died during the study period.

  - 
In Kenya, about 6% of drug-susceptible TB cases died.

  - 
A multi-country study reported mortality of 6.0% in adequately treated patients with pan-susceptible strains.

  - 
WHO reports DS-TB treatment success of 88% (2023 data).
 That is consistent with deaths of roughly 4–6%, but I did not retrieve the exact WHO death proportion.
  - The "3–6%" range is therefore reasonable. Cohorts with HIV or severe disease run higher, so the range sits at the low-to-mid end of what is reported.
- **GRADE downgrades for indirectness when surrogate outcomes are used: VERIFIED.**
  - 
WHO SAGE guidance says that when important outcomes are represented by a surrogate, the evidence quality frequently needs down-rating for indirectness.

  - 
A WHO guideline applying the Handbook (2nd edition) downgrades for indirectness when the evidence differs from the target context in populations, interventions, comparisons or outcomes.

  - I did not retrieve the Handbook text itself. The two sources above are WHO documents applying it.
- **Recommendation delayed, conditional or subgroup-only: PLAUSIBLE.** This is a reasonable inference. It is not a documented outcome for any specific TB adjunct.
- **Effective uptake would fall by about half or more under a subgroup recommendation: UNVERIFIABLE.** The Investigator already flagged this as speculative.

**EVIDENCE FOUND**
- **Weakens the critique.** WHO TB guideline groups routinely treat composite patient-important outcomes (treatment success, unfavourable outcome including death, relapse) as critical outcomes.
  - The critique treats a composite as a weak substitute. In TB, a composite that includes death is often a direct outcome. That reduces the expected indirectness penalty.
  - This is from my background knowledge. I did not search for it.
- **Supports the critique.** The only statin RCT I found, StAT-TB, is a Phase 2b dose-finding trial. 
Its endpoints are time to sputum-culture negativity and lung function.
 
Mortality is assessed as a tolerability measure.
 Mortality is not the primary efficacy endpoint.
- Observational data link statin use to lower all-cause mortality in TB patients with ASCVD. 
The authors say RCTs are needed.
 That is a narrow subgroup, and it supports the case for a subgroup-limited recommendation.

**CORE CLAIM**
- **Claim:** A Phase III cannot be powered on a roughly 10% relative mortality reduction (about 30k per arm), so the recommendation would rest on surrogate or composite endpoints that GRADE treats as indirect.
- **Support:** SUPPORTED, for the feasibility and GRADE-mechanism part. The effect on uptake is LOGIC ONLY.
- **Why:** The arithmetic reproduces, baseline mortality sits in the claimed range, and WHO guidance confirms the downgrading mechanism. No evidence ties this to a specific uptake reduction.

**REVISED CRITIQUE**
A mortality-powered Phase III would need about 28–30k patients per arm at a 5–6% baseline. A mortality-driven benefit would therefore probably be inferred from composite or surrogate endpoints. That invites an indirectness downgrade. It could make the recommendation conditional, delayed or subgroup-limited, and it raises variance on the realized relative reduction. Counterweight: TB GDGs usually accept unfavourable-outcome composites that include death as direct. The uptake and timing effects are UNGROUNDED. **Magnitude: low-to-medium** (downgraded from medium). Direction: decreases.

---

## Critique 2: Clinical eligibility and monitoring barriers cap the prescribing share

**OVERALL VERDICT: PARTIALLY VERIFIED.** The hepatotoxicity premise is verified. The numeric uptake cap is ungrounded. Several pharmacology points are likely mismatched to the statin actually under study.

**CLAIM CHECK**
- **Anti-TB DILI is common, "low single digits to ~10%": PARTIALLY VERIFIED.**
  - 
A recent meta-analysis reported a global incidence of 11.5%, with rates varying from 2% to 28%.

  - 
Another source cites 3–36% for drug-susceptible TB.

  - 
Incidence varies with the cohort, regimen, DILI threshold and monitoring.

  - The Investigator's range is directionally right but understates the upper end. If anything, DILI is more common than stated, which strengthens the premise. The Investigator said they could not cite a paper. Wang et al. (2022), a meta-analysis of 160 studies, is the relevant one.
- **Rifampicin is a strong CYP3A4 inducer: VERIFIED.** 
Rifampin is a strong inducer of CYP3A4 and 2C19.

- **Specific ART interactions (PI-boosted raises atorvastatin, efavirenz lowers it): UNVERIFIED.** I did not check the Liverpool database. This is standard pharmacology and plausible.
- **Statin label warnings for liver disease and pregnancy: PLAUSIBLE but possibly outdated.** I did not search this. From background knowledge, FDA labelling was revised after 2012 to drop routine periodic LFT monitoring. The pregnancy contraindication was also relaxed in 2021. The "mandated LFT monitoring" scenario is therefore weaker than the critique implies.
- **Exclusion of 10–20% of adults, bringing 0.60 to 0.45–0.50: UNVERIFIABLE.** The Investigator labelled it illustrative and ungrounded. I found no data.
- **Many NTPs do not routinely perform LFTs in DS-TB: PLAUSIBLE.** I found no direct source. WHO guidance recommends symptom-based monitoring for most patients, which is consistent with it.

**EVIDENCE FOUND**
- **Statin identity matters.** The Phase 2b trial (StAT-TB) tests pravastatin. 
It asks whether pravastatin adjunctive therapy shortens time to sputum-culture negativity and improves lung function.

  - 
In preclinical work, atorvastatin and mevastatin did not inhibit Mtb growth in THP-1 cells at nontoxic doses.
 
Pravastatin showed the least toxicity in that study.

  - From background knowledge, pravastatin is not substantially CYP3A4-metabolised. If CG's candidate is pravastatin, the CYP3A4 and PI-boosted ART interaction arguments largely fall away. The hepatotoxicity-attribution and pill-burden arguments remain.
  - I do not know which statin CG assumes. The Investigator should have flagged that dependence.
- 
The DILI meta-analysis authors say regular liver function monitoring is imperative during anti-TB treatment.
 This supports the premise that monitoring is a live issue, though it is not specific to statins.

**CORE CLAIM**
- **Claim:** Eligibility exclusions, DILI-attribution concerns and monitoring requirements would cut adult uptake from about 0.60 to about 0.45–0.50.
- **Support:** LOGIC ONLY.
- **Why:** The mechanisms are plausible and the DILI base rate is verified, but I found no evidence for the size of the exclusion or program-reluctance effect.

**REVISED CRITIQUE**
Anti-TB DILI is common, with a pooled incidence of about 11.5% and a range of roughly 2–28% or more. Clinicians may be reluctant to add a hepatically relevant agent that confounds attribution. Some eligibility exclusion (liver disease, pregnancy, polypharmacy) is therefore plausible. The cited drug-interaction concerns apply to CYP3A4-metabolised statins such as atorvastatin, not necessarily to pravastatin, which is the statin in the Phase 2b trial. The specific 0.45–0.50 figure is **UNGROUNDED — plausible but needs empirical support.** **Magnitude: low-to-medium.** Direction: decreases.

---

## Critique 3: Delivered dose and adherence diverge from trial conditions, especially with rifapentine regimens

**OVERALL VERDICT: PARTIALLY VERIFIED.** The general adherence and effectiveness-gap logic is sound. The rifapentine claim is overstated relative to the sources. The adherence factor risks double-counting.

**CLAIM CHECK**
- **Rifapentine is a strong CYP3A4 inducer, "comparable to or stronger than rifampicin in some dosing contexts": PARTIALLY VERIFIED, mostly contradicted on direction.**
  - 
One review ranks relative inductive potency as rifampin > rifapentine > rifabutin. It says rifapentine's CYP3A4 induction approaches rifampin's (85–100%) with daily dosing and is more moderate with once- or twice-weekly dosing.

  - 
The WHO prequalification document says rifapentine's induction potential may be less than rifampicin's but more potent than rifabutin's.

  - 
A clinical protocol gives relative potency as rifampin 100%, rifapentine 85% and rifabutin 40%.

  - There is supporting evidence for "stronger in some contexts." 
In one study, oral midazolam AUC fell 75% with rifampin versus 92% with rifapentine, each at 10 mg/kg daily.

  - 
One in vitro hepatocyte study found rifapentine to be the weakest of the three inducers.

  - The evidence is mixed. It does not support the stronger claim that HPMZ regimens would lower statin exposure "further" than rifampicin regimens. Daily rifapentine dosing, as in HPMZ, is the condition where induction is closest to rifampicin's. A modest difference in either direction is the best-supported reading.
- **HPMZ is a 4-month rifapentine-containing regimen that programs are moving toward, with a currently small but growing share: PLAUSIBLE.** I did not search this. From background knowledge, WHO recommended it in 2022. I have no uptake share data.
- **Statin non-adherence is high in general populations: PLAUSIBLE, not searched.** It is a well-known finding, but it was not checked for the TB context.
- **Adjunct pills outside an FDC are less likely to be taken than anti-TB drugs: PLAUSIBLE.** The Investigator admitted there is no specific source, and I found none.
- **0.60 × 0.70 = 0.42, about a 30% reduction: VERIFIED (arithmetic).** The 70% adherence figure is an assumption.
- **Dose-finding on one regimen may not carry over: PLAUSIBLE.** StAT-TB tests statins with first-line HRZE. 
The protocol describes testing statins in combination with first-line TB drugs.


**EVIDENCE FOUND**
- **Possible double-counting.** If the Phase III is pragmatic or intention-to-treat, the effect size already embeds trial-level non-adherence. Applying an adherence haircut again to uptake would then overstate the downward adjustment. The Investigator did not address this.
- **Statin identity again.** If pravastatin is the candidate, rifamycin CYP3A4 induction is a minor concern. The rifapentine-specific argument then largely falls away.
- The critique says it "compounds with Critiques 1 and 3". That appears to be a self-reference error and should probably read 1 and 2.

**CORE CLAIM**
- **Claim:** Real-world delivered dose and adherence (about 70%) would reduce effective uptake by about 30%, and rifapentine regimens would further lower statin exposure.
- **Support:** LOGIC ONLY for the adherence factor. The rifapentine "further lower" claim is weakly supported to partly contradicted.
- **Why:** The effectiveness-gap mechanism is generic and plausible. The 70% is assumed, and most pharmacology sources rank rifapentine at or below rifampicin for CYP3A4 induction.

**REVISED CRITIQUE**
Programmatic adherence to an unsupervised adjunct pill is likely below trial adherence, and this lowers realized benefit. The size of the effect is **UNGROUNDED — plausible but needs empirical support.** The 70% figure is an assumption, and it risks double-counting if the trial effect is already pragmatic or intention-to-treat. The rifapentine point is weaker than stated. Daily rifapentine induces CYP3A4 at roughly 85–100% of rifampicin's level. That is similar to the interaction already present in HRZE-based trials, not clearly worse, and it matters only for CYP3A4-metabolised statins. **Magnitude: low-to-medium** (downgraded from medium). Direction: decreases.

--- Critique: Private-sector treatment share and the reach of national guidelines are not modeled ---

## Critique 1: Private-sector treatment share and the reach of national guidelines are not modeled

**OVERALL VERDICT: PARTIALLY VERIFIED.** The India notification share checks out. The sign of the effect, the 5–15% magnitude and the guideline-deviation claim are unsourced. Some evidence also cuts against the "not on NTP procurement" framing.

**CITATION CHECK:** The critique cites no specific papers. It names WHO Global TB Reports and Ni-kshay generally, and it says it cannot cite a paper for guideline deviation.

**CLAIM CHECK:**
- *India's private-sector notifications are roughly a third of the total.* **VERIFIED.**
  - 
India's Ministry of Health reports 0.73 million private notifications in 2022 (30% of the total) and 0.83 million in 2023 (32%).

  - Other sources give 
33% (0.84 million) in 2023
.
- *A large share of TB care is in the private sector in India, Indonesia, Pakistan and the Philippines.* **PARTIALLY VERIFIED.**
  - For India, 
a prevalence survey found about 50% of people with TB symptoms consult private facilities
. This is much larger than the one-third notified share.
  - 
India, Indonesia, the Philippines and Pakistan are among the five countries with the most cases
.
  - I found no data on private-sector share for Indonesia, Pakistan or the Philippines.
- *Private providers deviate from guidelines.* **PLAUSIBLE.** 
Reports describe persistent underreporting, delays in diagnosis and treatment initiation, and weak adherence to standards of care in the Indian private sector.
 I found no direct evidence on FDC use or dosing.
- *Unnotified ("missing") cases are a large share in the same countries.* **PARTIALLY CONTRADICTED for India.**
  - 
India cut missed notifications from 1.2 million in 2015 to 0.3 million in 2023.

  - Globally, 
notifications reached 78% of estimated incident cases
.
  - The "large share missing" claim is therefore weaker for India than the critique implies. I did not check the other three countries.
- *Uptake depends on professional societies, pharma marketing and notification, not on NTP procurement.* **PARTIALLY CONTRADICTED.** India's programme is actively routing private patients to government supply.
  - 
Private-sector engagement agencies (PPSAs) link private patients to free public drugs and diagnostics.

  - 
The programme also works with professional bodies such as the Indian Medical Association.

  - Private-sector uptake therefore runs partly through NTP channels.
- *Net effect is a downward adjustment of about 5–15% of benefit.* **UNVERIFIABLE.** The critique itself labels this inference.

**EVIDENCE FOUND:**
- 
Private practitioners in India have had to notify every TB case since a 2012 Gazette notification.
 The mandatory-notification lever the critique mentions exists, but enforcement is weak.
- 
Notification and public-health actions in the private sector have not really become routine practice.

- The direction is ambiguous, as the critique admits. Rising private-sector linkage to NTP drugs argues against a net downward adjustment in India.

**CORE CLAIM:**
- Claim: Effective uptake of a new regimen in the private sector is materially lower than the model assumes, giving a net downward adjustment to benefit.
- Support: **LOGIC ONLY.**
- Why: The private share is real, but I found no evidence on private-sector uptake of new regimens, and the sign is admittedly ambiguous.

**REVISED CRITIQUE:** The private sector handles about one-third of notified cases in India. The share of all care-seeking is higher, with roughly half of symptomatic people consulting private providers. A guideline's reach into the private sector depends partly on notification mandates and PPSA-mediated access to free drugs. The model's single uptake figure does not capture this. The direction and size of the effect are **UNGROUNDED, plausible but needing empirical support**. Do not assert the 5–15% figure. Strength: **low–medium**, and the direction is uncertain, not "decreases".

---

## Critique 2: Zero modeled lag between Phase III completion and adoption

**OVERALL VERDICT: PARTIALLY VERIFIED.** The HPMZ timeline is slightly wrong in a way that supports the critique's own "WHO step can be short" point. The Xpert example is real. The funding-gating argument is logic only.

**CITATION CHECK:**
- Study 31/A5349, published 2021: **VERIFIED.** 
WHO notes that detailed results were published on 6 May 2021.
 The NEJM citation is 
n engl j med 384;18, May 6, 2021
.
- WHO guidance in 2022: **PARTIALLY VERIFIED, with a correction.**
  - 
WHO convened its guideline group on 27–30 April 2021, before publication.
 A rapid communication followed in June 2021.
  - The 2022 date matches the consolidated Module 4 guidelines, 
which list the HPMZ regimen as conditionally recommended
.
  - The WHO step was therefore faster than the critique recalls, at about a month from publication and months from topline data. 
WHO posted a news item on the findings in October 2020.

- Xpert endorsement in 2010: **VERIFIED.** 
WHO endorsed it in December 2010 and recommended phased implementation from 2011.

- Cazabon et al.: **VERIFIED as existing.** 
Cazabon D, et al., "Implementation of Xpert MTB/RIF in 22 high tuberculosis burden countries: are we making progress?", Eur Respir J 2017.
 I did not retrieve its findings. Another paper on market penetration states that 
previous studies showed low market penetration
.
- Albert et al.: **NOT CHECKED.** The search budget ran out before I could look it up.

**CLAIM CHECK:**
- *Real-world chains include long national adoption and procurement lags.* **PLAUSIBLE.** Xpert supports it. Early WHO endorsement was followed by 
a trial (registered 2013) describing Xpert as not yet integrated into national programmes
.
- *A generic drug has no sponsor, so Phase III funding could gate the timeline.* **UNVERIFIABLE (logic).**
- *Phase III trials routinely slip.* **PLAUSIBLE.** No source was retrieved.
- *The model sets years_to_adoption equal to Phase III completion and loses about 2% of benefit per year of delay.* **UNVERIFIABLE.** I have no access to the model.

**EVIDENCE FOUND:**
- The HPMZ case shows the WHO step can be very short once data exist. The critique's central point is that country adoption and the trial's place on the critical path matter more, which this case does not contradict. I found no HPMZ country-uptake data.

**CORE CLAIM:**
- Claim: A 1-year acceleration of Phase IIc does not give a 1-year earlier adoption, because the trial is not the binding constraint.
- Support: **LOGIC ONLY.**
- Why: Plausible, since sponsorship and funding could gate Phase III, but I found no evidence on this regimen's funding path or timeline.

**REVISED CRITIQUE:** Correct the HPMZ chronology: WHO acted within weeks of publication in 2021, with consolidated guidelines in 2022. Retain the argument that post-guideline national adoption and procurement add lag, with Xpert as a qualitative analogy. Flag the Phase III funding gate and the claim that speedup is below 1 year as **UNGROUNDED**. The critique's own admission that lumpiness does not lower expected speedup should stay. Strength: **low–medium**.

---

## Critique 3: Survivors' excess mortality and comorbidity shrink the 27 DALYs per death

**OVERALL VERDICT: PARTIALLY VERIFIED.** The Romanowski citation is real and the SMR is close, though slightly lower than recalled. The Gompertz arithmetic is sound. The load-bearing claim about how 27 was derived cannot be checked.

**CITATION CHECK:**
- Romanowski et al. 2019, Lancet Infect Dis: **VERIFIED, with a number correction.**
  - It is published as 
Lancet Infect Dis 2019;19:1129–1137.

  - 
It found the force of mortality in TB survivors was 2.91 (95% CI 2.21–3.84) times that of people who never had TB.

  - The critique recalled a pooled SMR of 3–4. The point estimate is about 2.9, and 3–4 is the upper part of the CI.
  - Another source summarizes it as 
2 to 5 times more likely to die versus the general population or matched controls
.

**CLAIM CHECK:**
- *The Gompertz shift is ln(k)/b, which is about 11–12 years for k = 3 and b = 0.09.* **VERIFIED (arithmetic).** With the real estimate of 2.91, ln(2.91)/0.09 ≈ 11.9 years.
- *Remaining life expectancy at 40 is low-to-mid 30s, and in the mid-20s at effective age 52.* **PLAUSIBLE.** I did not retrieve a life table.
- *That implies a 20–30% reduction, so 27 falls to about 19–22.* **PLAUSIBLE but conditional.**
  - It holds only if 27 came from an unadjusted general-population table.
  - The SMR is also confounded, as the critique notes. For a counterfactual averted-death patient, shared risk factors still apply.
  - A first-year or on-treatment death averted differs from a post-treatment survivor, so applying the post-treatment SMR to the whole remaining lifespan is a modelling choice.
- *The 17.7 threshold.* **UNVERIFIABLE.** It comes from the model I cannot see.
- *CG's derivation of 27.* **UNVERIFIABLE.**

**EVIDENCE FOUND:**
- Independent support: 
A lifetime-burden analysis estimated 12.1 DALYs per incident TB case, 5.8 of them from post-TB sequelae
. 
Per-case post-TB burden was greater for younger people and in high-incidence countries.
 This confirms that post-TB morbidity and mortality are material. It also shows that burden estimates can include post-TB effects, which could offset the critique if CG's figure already includes them.
- A large 2026 cohort comparison found 
elevated natural-cause mortality in the treated cohort (RR = 1.77)
. This is lower than Romanowski's pooled estimate, which suggests k = 3 may be on the high side.
- Using k ≈ 1.8 instead of 2.9 gives an effective ageing of about 6.5 years, which roughly halves the reduction the critique computes.

**CORE CLAIM:**
- Claim: The 27 DALYs per death derives from general-population or GBD-style life tables and is therefore overstated for the people whose deaths are actually averted.
- Support: **LOGIC ONLY.**
- Why: Excess post-TB mortality is well documented, but I could not find how CG built 27. It may already be a TB-specific or healthy-life figure, which would offset the adjustment.

**REVISED CRITIQUE:** Survivors of TB have roughly 1.8–2.9 times the all-cause mortality of the general population, per Romanowski 2019 (2.91, 95% CI 2.21–3.84) and a recent cohort study (RR 1.77). Applying general-population life expectancy to averted deaths probably overstates years gained. Using Gompertz scaling, the plausible reduction is about 10–25%, not a flat 20–30%, and it is **conditional on the provenance of 27**, which is **UNGROUNDED**. The claim that 27 falls "near or below 17.7" is a model-specific inference. Strength: **medium**, down from large, until the source of 27 is known.

--- Critique: Zero modeled lag between Phase III completion and adoption, and a speedup that assumes trial timing is the binding constraint ---

## Critique 1: Private-sector treatment share and the reach of national guidelines are not modeled

**OVERALL VERDICT: PARTIALLY VERIFIED.** The India notification share checks out. The sign of the effect, the 5–15% magnitude and the guideline-deviation claim are unsourced. Some evidence also cuts against the "not on NTP procurement" framing.

**CITATION CHECK:** The critique cites no specific papers. It names WHO Global TB Reports and Ni-kshay generally, and it says it cannot cite a paper for guideline deviation.

**CLAIM CHECK:**
- *India's private-sector notifications are roughly a third of the total.* **VERIFIED.**
  - 
India's Ministry of Health reports 0.73 million private notifications in 2022 (30% of the total) and 0.83 million in 2023 (32%).

  - Other sources give 
33% (0.84 million) in 2023
.
- *A large share of TB care is in the private sector in India, Indonesia, Pakistan and the Philippines.* **PARTIALLY VERIFIED.**
  - For India, 
a prevalence survey found about 50% of people with TB symptoms consult private facilities
. This is much larger than the one-third notified share.
  - 
India, Indonesia, the Philippines and Pakistan are among the five countries with the most cases
.
  - I found no data on private-sector share for Indonesia, Pakistan or the Philippines.
- *Private providers deviate from guidelines.* **PLAUSIBLE.** 
Reports describe persistent underreporting, delays in diagnosis and treatment initiation, and weak adherence to standards of care in the Indian private sector.
 I found no direct evidence on FDC use or dosing.
- *Unnotified ("missing") cases are a large share in the same countries.* **PARTIALLY CONTRADICTED for India.**
  - 
India cut missed notifications from 1.2 million in 2015 to 0.3 million in 2023.

  - Globally, 
notifications reached 78% of estimated incident cases
.
  - The "large share missing" claim is therefore weaker for India than the critique implies. I did not check the other three countries.
- *Uptake depends on professional societies, pharma marketing and notification, not on NTP procurement.* **PARTIALLY CONTRADICTED.** India's programme is actively routing private patients to government supply.
  - 
Private-sector engagement agencies (PPSAs) link private patients to free public drugs and diagnostics.

  - 
The programme also works with professional bodies such as the Indian Medical Association.

  - Private-sector uptake therefore runs partly through NTP channels.
- *Net effect is a downward adjustment of about 5–15% of benefit.* **UNVERIFIABLE.** The critique itself labels this inference.

**EVIDENCE FOUND:**
- 
Private practitioners in India have had to notify every TB case since a 2012 Gazette notification.
 The mandatory-notification lever the critique mentions exists, but enforcement is weak.
- 
Notification and public-health actions in the private sector have not really become routine practice.

- The direction is ambiguous, as the critique admits. Rising private-sector linkage to NTP drugs argues against a net downward adjustment in India.

**CORE CLAIM:**
- Claim: Effective uptake of a new regimen in the private sector is materially lower than the model assumes, giving a net downward adjustment to benefit.
- Support: **LOGIC ONLY.**
- Why: The private share is real, but I found no evidence on private-sector uptake of new regimens, and the sign is admittedly ambiguous.

**REVISED CRITIQUE:** The private sector handles about one-third of notified cases in India. The share of all care-seeking is higher, with roughly half of symptomatic people consulting private providers. A guideline's reach into the private sector depends partly on notification mandates and PPSA-mediated access to free drugs. The model's single uptake figure does not capture this. The direction and size of the effect are **UNGROUNDED, plausible but needing empirical support**. Do not assert the 5–15% figure. Strength: **low–medium**, and the direction is uncertain, not "decreases".

---

## Critique 2: Zero modeled lag between Phase III completion and adoption

**OVERALL VERDICT: PARTIALLY VERIFIED.** The HPMZ timeline is slightly wrong in a way that supports the critique's own "WHO step can be short" point. The Xpert example is real. The funding-gating argument is logic only.

**CITATION CHECK:**
- Study 31/A5349, published 2021: **VERIFIED.** 
WHO notes that detailed results were published on 6 May 2021.
 The NEJM citation is 
n engl j med 384;18, May 6, 2021
.
- WHO guidance in 2022: **PARTIALLY VERIFIED, with a correction.**
  - 
WHO convened its guideline group on 27–30 April 2021, before publication.
 A rapid communication followed in June 2021.
  - The 2022 date matches the consolidated Module 4 guidelines, 
which list the HPMZ regimen as conditionally recommended
.
  - The WHO step was therefore faster than the critique recalls, at about a month from publication and months from topline data. 
WHO posted a news item on the findings in October 2020.

- Xpert endorsement in 2010: **VERIFIED.** 
WHO endorsed it in December 2010 and recommended phased implementation from 2011.

- Cazabon et al.: **VERIFIED as existing.** 
Cazabon D, et al., "Implementation of Xpert MTB/RIF in 22 high tuberculosis burden countries: are we making progress?", Eur Respir J 2017.
 I did not retrieve its findings. Another paper on market penetration states that 
previous studies showed low market penetration
.
- Albert et al.: **NOT CHECKED.** The search budget ran out before I could look it up.

**CLAIM CHECK:**
- *Real-world chains include long national adoption and procurement lags.* **PLAUSIBLE.** Xpert supports it. Early WHO endorsement was followed by 
a trial (registered 2013) describing Xpert as not yet integrated into national programmes
.
- *A generic drug has no sponsor, so Phase III funding could gate the timeline.* **UNVERIFIABLE (logic).**
- *Phase III trials routinely slip.* **PLAUSIBLE.** No source was retrieved.
- *The model sets years_to_adoption equal to Phase III completion and loses about 2% of benefit per year of delay.* **UNVERIFIABLE.** I have no access to the model.

**EVIDENCE FOUND:**
- The HPMZ case shows the WHO step can be very short once data exist. The critique's central point is that country adoption and the trial's place on the critical path matter more, which this case does not contradict. I found no HPMZ country-uptake data.

**CORE CLAIM:**
- Claim: A 1-year acceleration of Phase IIc does not give a 1-year earlier adoption, because the trial is not the binding constraint.
- Support: **LOGIC ONLY.**
- Why: Plausible, since sponsorship and funding could gate Phase III, but I found no evidence on this regimen's funding path or timeline.

**REVISED CRITIQUE:** Correct the HPMZ chronology: WHO acted within weeks of publication in 2021, with consolidated guidelines in 2022. Retain the argument that post-guideline national adoption and procurement add lag, with Xpert as a qualitative analogy. Flag the Phase III funding gate and the claim that speedup is below 1 year as **UNGROUNDED**. The critique's own admission that lumpiness does not lower expected speedup should stay. Strength: **low–medium**.

---

## Critique 3: Survivors' excess mortality and comorbidity shrink the 27 DALYs per death

**OVERALL VERDICT: PARTIALLY VERIFIED.** The Romanowski citation is real and the SMR is close, though slightly lower than recalled. The Gompertz arithmetic is sound. The load-bearing claim about how 27 was derived cannot be checked.

**CITATION CHECK:**
- Romanowski et al. 2019, Lancet Infect Dis: **VERIFIED, with a number correction.**
  - It is published as 
Lancet Infect Dis 2019;19:1129–1137.

  - 
It found the force of mortality in TB survivors was 2.91 (95% CI 2.21–3.84) times that of people who never had TB.

  - The critique recalled a pooled SMR of 3–4. The point estimate is about 2.9, and 3–4 is the upper part of the CI.
  - Another source summarizes it as 
2 to 5 times more likely to die versus the general population or matched controls
.

**CLAIM CHECK:**
- *The Gompertz shift is ln(k)/b, which is about 11–12 years for k = 3 and b = 0.09.* **VERIFIED (arithmetic).** With the real estimate of 2.91, ln(2.91)/0.09 ≈ 11.9 years.
- *Remaining life expectancy at 40 is low-to-mid 30s, and in the mid-20s at effective age 52.* **PLAUSIBLE.** I did not retrieve a life table.
- *That implies a 20–30% reduction, so 27 falls to about 19–22.* **PLAUSIBLE but conditional.**
  - It holds only if 27 came from an unadjusted general-population table.
  - The SMR is also confounded, as the critique notes. For a counterfactual averted-death patient, shared risk factors still apply.
  - A first-year or on-treatment death averted differs from a post-treatment survivor, so applying the post-treatment SMR to the whole remaining lifespan is a modelling choice.
- *The 17.7 threshold.* **UNVERIFIABLE.** It comes from the model I cannot see.
- *CG's derivation of 27.* **UNVERIFIABLE.**

**EVIDENCE FOUND:**
- Independent support: 
A lifetime-burden analysis estimated 12.1 DALYs per incident TB case, 5.8 of them from post-TB sequelae
. 
Per-case post-TB burden was greater for younger people and in high-incidence countries.
 This confirms that post-TB morbidity and mortality are material. It also shows that burden estimates can include post-TB effects, which could offset the critique if CG's figure already includes them.
- A large 2026 cohort comparison found 
elevated natural-cause mortality in the treated cohort (RR = 1.77)
. This is lower than Romanowski's pooled estimate, which suggests k = 3 may be on the high side.
- Using k ≈ 1.8 instead of 2.9 gives an effective ageing of about 6.5 years, which roughly halves the reduction the critique computes.

**CORE CLAIM:**
- Claim: The 27 DALYs per death derives from general-population or GBD-style life tables and is therefore overstated for the people whose deaths are actually averted.
- Support: **LOGIC ONLY.**
- Why: Excess post-TB mortality is well documented, but I could not find how CG built 27. It may already be a TB-specific or healthy-life figure, which would offset the adjustment.

**REVISED CRITIQUE:** Survivors of TB have roughly 1.8–2.9 times the all-cause mortality of the general population, per Romanowski 2019 (2.91, 95% CI 2.21–3.84) and a recent cohort study (RR 1.77). Applying general-population life expectancy to averted deaths probably overstates years gained. Using Gompertz scaling, the plausible reduction is about 10–25%, not a flat 20–30%, and it is **conditional on the provenance of 27**, which is **UNGROUNDED**. The claim that 27 falls "near or below 17.7" is a model-specific inference. Strength: **medium**, down from large, until the source of 27 is known.

--- Critique: Survivors' excess mortality and comorbidity shrink the 27 DALYs per death ---

## Critique 1: Private-sector treatment share and the reach of national guidelines are not modeled

**OVERALL VERDICT: PARTIALLY VERIFIED.** The India notification share checks out. The sign of the effect, the 5–15% magnitude and the guideline-deviation claim are unsourced. Some evidence also cuts against the "not on NTP procurement" framing.

**CITATION CHECK:** The critique cites no specific papers. It names WHO Global TB Reports and Ni-kshay generally, and it says it cannot cite a paper for guideline deviation.

**CLAIM CHECK:**
- *India's private-sector notifications are roughly a third of the total.* **VERIFIED.**
  - 
India's Ministry of Health reports 0.73 million private notifications in 2022 (30% of the total) and 0.83 million in 2023 (32%).

  - Other sources give 
33% (0.84 million) in 2023
.
- *A large share of TB care is in the private sector in India, Indonesia, Pakistan and the Philippines.* **PARTIALLY VERIFIED.**
  - For India, 
a prevalence survey found about 50% of people with TB symptoms consult private facilities
. This is much larger than the one-third notified share.
  - 
India, Indonesia, the Philippines and Pakistan are among the five countries with the most cases
.
  - I found no data on private-sector share for Indonesia, Pakistan or the Philippines.
- *Private providers deviate from guidelines.* **PLAUSIBLE.** 
Reports describe persistent underreporting, delays in diagnosis and treatment initiation, and weak adherence to standards of care in the Indian private sector.
 I found no direct evidence on FDC use or dosing.
- *Unnotified ("missing") cases are a large share in the same countries.* **PARTIALLY CONTRADICTED for India.**
  - 
India cut missed notifications from 1.2 million in 2015 to 0.3 million in 2023.

  - Globally, 
notifications reached 78% of estimated incident cases
.
  - The "large share missing" claim is therefore weaker for India than the critique implies. I did not check the other three countries.
- *Uptake depends on professional societies, pharma marketing and notification, not on NTP procurement.* **PARTIALLY CONTRADICTED.** India's programme is actively routing private patients to government supply.
  - 
Private-sector engagement agencies (PPSAs) link private patients to free public drugs and diagnostics.

  - 
The programme also works with professional bodies such as the Indian Medical Association.

  - Private-sector uptake therefore runs partly through NTP channels.
- *Net effect is a downward adjustment of about 5–15% of benefit.* **UNVERIFIABLE.** The critique itself labels this inference.

**EVIDENCE FOUND:**
- 
Private practitioners in India have had to notify every TB case since a 2012 Gazette notification.
 The mandatory-notification lever the critique mentions exists, but enforcement is weak.
- 
Notification and public-health actions in the private sector have not really become routine practice.

- The direction is ambiguous, as the critique admits. Rising private-sector linkage to NTP drugs argues against a net downward adjustment in India.

**CORE CLAIM:**
- Claim: Effective uptake of a new regimen in the private sector is materially lower than the model assumes, giving a net downward adjustment to benefit.
- Support: **LOGIC ONLY.**
- Why: The private share is real, but I found no evidence on private-sector uptake of new regimens, and the sign is admittedly ambiguous.

**REVISED CRITIQUE:** The private sector handles about one-third of notified cases in India. The share of all care-seeking is higher, with roughly half of symptomatic people consulting private providers. A guideline's reach into the private sector depends partly on notification mandates and PPSA-mediated access to free drugs. The model's single uptake figure does not capture this. The direction and size of the effect are **UNGROUNDED, plausible but needing empirical support**. Do not assert the 5–15% figure. Strength: **low–medium**, and the direction is uncertain, not "decreases".

---

## Critique 2: Zero modeled lag between Phase III completion and adoption

**OVERALL VERDICT: PARTIALLY VERIFIED.** The HPMZ timeline is slightly wrong in a way that supports the critique's own "WHO step can be short" point. The Xpert example is real. The funding-gating argument is logic only.

**CITATION CHECK:**
- Study 31/A5349, published 2021: **VERIFIED.** 
WHO notes that detailed results were published on 6 May 2021.
 The NEJM citation is 
n engl j med 384;18, May 6, 2021
.
- WHO guidance in 2022: **PARTIALLY VERIFIED, with a correction.**
  - 
WHO convened its guideline group on 27–30 April 2021, before publication.
 A rapid communication followed in June 2021.
  - The 2022 date matches the consolidated Module 4 guidelines, 
which list the HPMZ regimen as conditionally recommended
.
  - The WHO step was therefore faster than the critique recalls, at about a month from publication and months from topline data. 
WHO posted a news item on the findings in October 2020.

- Xpert endorsement in 2010: **VERIFIED.** 
WHO endorsed it in December 2010 and recommended phased implementation from 2011.

- Cazabon et al.: **VERIFIED as existing.** 
Cazabon D, et al., "Implementation of Xpert MTB/RIF in 22 high tuberculosis burden countries: are we making progress?", Eur Respir J 2017.
 I did not retrieve its findings. Another paper on market penetration states that 
previous studies showed low market penetration
.
- Albert et al.: **NOT CHECKED.** The search budget ran out before I could look it up.

**CLAIM CHECK:**
- *Real-world chains include long national adoption and procurement lags.* **PLAUSIBLE.** Xpert supports it. Early WHO endorsement was followed by 
a trial (registered 2013) describing Xpert as not yet integrated into national programmes
.
- *A generic drug has no sponsor, so Phase III funding could gate the timeline.* **UNVERIFIABLE (logic).**
- *Phase III trials routinely slip.* **PLAUSIBLE.** No source was retrieved.
- *The model sets years_to_adoption equal to Phase III completion and loses about 2% of benefit per year of delay.* **UNVERIFIABLE.** I have no access to the model.

**EVIDENCE FOUND:**
- The HPMZ case shows the WHO step can be very short once data exist. The critique's central point is that country adoption and the trial's place on the critical path matter more, which this case does not contradict. I found no HPMZ country-uptake data.

**CORE CLAIM:**
- Claim: A 1-year acceleration of Phase IIc does not give a 1-year earlier adoption, because the trial is not the binding constraint.
- Support: **LOGIC ONLY.**
- Why: Plausible, since sponsorship and funding could gate Phase III, but I found no evidence on this regimen's funding path or timeline.

**REVISED CRITIQUE:** Correct the HPMZ chronology: WHO acted within weeks of publication in 2021, with consolidated guidelines in 2022. Retain the argument that post-guideline national adoption and procurement add lag, with Xpert as a qualitative analogy. Flag the Phase III funding gate and the claim that speedup is below 1 year as **UNGROUNDED**. The critique's own admission that lumpiness does not lower expected speedup should stay. Strength: **low–medium**.

---

## Critique 3: Survivors' excess mortality and comorbidity shrink the 27 DALYs per death

**OVERALL VERDICT: PARTIALLY VERIFIED.** The Romanowski citation is real and the SMR is close, though slightly lower than recalled. The Gompertz arithmetic is sound. The load-bearing claim about how 27 was derived cannot be checked.

**CITATION CHECK:**
- Romanowski et al. 2019, Lancet Infect Dis: **VERIFIED, with a number correction.**
  - It is published as 
Lancet Infect Dis 2019;19:1129–1137.

  - 
It found the force of mortality in TB survivors was 2.91 (95% CI 2.21–3.84) times that of people who never had TB.

  - The critique recalled a pooled SMR of 3–4. The point estimate is about 2.9, and 3–4 is the upper part of the CI.
  - Another source summarizes it as 
2 to 5 times more likely to die versus the general population or matched controls
.

**CLAIM CHECK:**
- *The Gompertz shift is ln(k)/b, which is about 11–12 years for k = 3 and b = 0.09.* **VERIFIED (arithmetic).** With the real estimate of 2.91, ln(2.91)/0.09 ≈ 11.9 years.
- *Remaining life expectancy at 40 is low-to-mid 30s, and in the mid-20s at effective age 52.* **PLAUSIBLE.** I did not retrieve a life table.
- *That implies a 20–30% reduction, so 27 falls to about 19–22.* **PLAUSIBLE but conditional.**
  - It holds only if 27 came from an unadjusted general-population table.
  - The SMR is also confounded, as the critique notes. For a counterfactual averted-death patient, shared risk factors still apply.
  - A first-year or on-treatment death averted differs from a post-treatment survivor, so applying the post-treatment SMR to the whole remaining lifespan is a modelling choice.
- *The 17.7 threshold.* **UNVERIFIABLE.** It comes from the model I cannot see.
- *CG's derivation of 27.* **UNVERIFIABLE.**

**EVIDENCE FOUND:**
- Independent support: 
A lifetime-burden analysis estimated 12.1 DALYs per incident TB case, 5.8 of them from post-TB sequelae
. 
Per-case post-TB burden was greater for younger people and in high-incidence countries.
 This confirms that post-TB morbidity and mortality are material. It also shows that burden estimates can include post-TB effects, which could offset the critique if CG's figure already includes them.
- A large 2026 cohort comparison found 
elevated natural-cause mortality in the treated cohort (RR = 1.77)
. This is lower than Romanowski's pooled estimate, which suggests k = 3 may be on the high side.
- Using k ≈ 1.8 instead of 2.9 gives an effective ageing of about 6.5 years, which roughly halves the reduction the critique computes.

**CORE CLAIM:**
- Claim: The 27 DALYs per death derives from general-population or GBD-style life tables and is therefore overstated for the people whose deaths are actually averted.
- Support: **LOGIC ONLY.**
- Why: Excess post-TB mortality is well documented, but I could not find how CG built 27. It may already be a TB-specific or healthy-life figure, which would offset the adjustment.

**REVISED CRITIQUE:** Survivors of TB have roughly 1.8–2.9 times the all-cause mortality of the general population, per Romanowski 2019 (2.91, 95% CI 2.21–3.84) and a recent cohort study (RR 1.77). Applying general-population life expectancy to averted deaths probably overstates years gained. Using Gompertz scaling, the plausible reduction is about 10–25%, not a flat 20–30%, and it is **conditional on the provenance of 27**, which is **UNGROUNDED**. The claim that 27 falls "near or below 17.7" is a model-specific inference. Strength: **medium**, down from large, until the source of 27 is known.

--- Critique: The 6% is a mix of deaths, and only a fraction is reachable and modifiable by atorvastatin ---

## Critique 1: The 6% is a mix of deaths, and only a fraction is reachable and modifiable by atorvastatin

**CITATION CHECK**
- Waitt & Squire 2011, IJTLD: **VERIFIED as existing, only partly verified on content.**
  - It is a real paper: Int J Tuberc Lung Dis 2011;15(7):871–85. 
It identified 62 studies on risk factors for death in patients started on TB treatment.

  - 
The review found two distinct epidemics with separate risk factors for death.

  - Other papers cite it as showing that 
comorbidities were risk factors in high-incidence, high-HIV settings rather than low-incidence, low-HIV settings.

  - I could not retrieve the review itself. The critique's "many deaths occur early" attribution to it is unconfirmed, though other sources support the point.
- "Country cohort studies": the Investigator named none. I found several (see Evidence Found).
- Rifampicin–atorvastatin interaction: **VERIFIED.** 
Rifampin shortened atorvastatin's half-life by 74%.
 Prescribing guidance also notes 
CYP3A inducers such as rifampin can cause variable reductions in atorvastatin plasma concentrations.


**CLAIM CHECK**
- Deaths are concentrated early, in the first weeks: **VERIFIED.**
  - Zambia, 1,063 deaths: 
58.1% occurred in the first month and 75.1% in the first two months.
 
The median time to death was 21 days.

  - Kenya, Meru County: 
76% of deaths occurred within three months of starting treatment.

  - Ethiopia: 
More than 70% of deaths occur in the first two months.

  - Taiwan: 
Underweight was associated with higher mortality only in the first 8 weeks.

- Very sick, malnourished or advanced-HIV patients dominate early deaths: **VERIFIED.** 
The major risk factors for early death are HIV positivity, old age, being underweight and retreatment.

- Some deaths are non-TB causes: **VERIFIED.** A Taiwanese review classified deaths as TB-related or non-TB-related. 
Most TB-related deaths occurred early, with a median survival of 20 days.
 The non-TB share varies by setting, and I did not find a pooled figure.
- Some deaths occur before treatment starts: **VERIFIED, but outside the treated cohort.** In a US study, 
TB-related death occurred during treatment for 75% of decedents and before treatment began for 25%.
 These deaths would not be in an on-treatment 6%.
- Rifampicin induction delays onset of statin benefit: **PLAUSIBLE.** The interaction is real. The timing of induction relative to benefit is an inference, and the Investigator labels it as one.
- The arithmetic 6% × 0.7 × 0.85 = 3.57%: **VERIFIED** (≈3.6%). I could not verify the 3.9% threshold. It comes from the source model.
- The 30% and 15% shares are placeholders, as the Investigator says. The 30% is plausible for deaths within about 2 weeks, given the Zambian median of 21 days. The 15% non-TB share is unsupported.

**EVIDENCE FOUND**
- The timing evidence above comes from Zambia, Kenya, Ethiopia, Turkey, Cameroon and India. It supports the early-death premise strongly.
- Caveat the Investigator did not raise: if the model's statin effect size comes from a trial population, it already excludes very early or ineligible deaths. Applying the "addressable share" haircut on top would double-count.
- The eligibility factor appears in the mechanism formula but not in the worked example.
- Early deaths may be partly reversible with timely care. 
Deaths within 14 days of anti-TB treatment suggest some mortality may have been reversible with earlier therapy.
 That cuts against treating all very early deaths as unreachable.

**CORE CLAIM**
- Claim: A large enough share of the 6% is unreachable or non-TB (about 35–40% combined) to push the effective baseline below 3.9%.
- Support: **LOGIC ONLY**
- Why: Early concentration of deaths is directly supported, but the specific shares are acknowledged placeholders, and I found no evidence on the statin onset-time or non-TB share needed to reach the threshold.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The direction (the addressable share is below 6%) is well supported. The magnitude, and the claim that the threshold is crossed, are ungrounded.

**REVISED CRITIQUE**
- Deaths during TB treatment are heavily front-loaded. In several African cohorts, roughly 55–75% occur within 1–2 months, and the median is about 3 weeks in Zambia.
- Early deaths are concentrated in HIV-positive, underweight and older patients. Rifampicin cuts atorvastatin exposure substantially.
- Applying the 6% to all patients probably overstates the share a statin could avert.
- **UNGROUNDED:** the size of the haircut. Needed evidence: statin time-to-effect, the TB-attributable share of deaths, and whether the model's effect size already reflects an enrolled trial population.
- Strength: medium, direction decreases, with a caution against double-counting.

---

## Critique 2: Under-ascertained deaths push true mortality up

**CITATION CHECK**
- WHO Global TB Report outcome categories: **VERIFIED for definitions.** WHO data lists 
treatment success (cured or completed), failed, died, lost to follow-up, or not evaluated
 as the outcome categories.
- WHO figures of "~5–6% died, ~3–4% LTFU, a few % not evaluated": **UNVERIFIED.** I could not retrieve the global outcome table. 
Global treatment success was 88% in 2023 and 2022.
 That leaves about 12% across all other outcomes, which is consistent with the Investigator's recall but does not confirm it.
- The tracing studies the Investigator "believed" existed: **found, see below.**

**CLAIM CHECK**
- The 6% comes from the "died" category and excludes LTFU and not-evaluated patients: **PLAUSIBLE.** WHO's definition supports the structure. I cannot confirm how the source model derived its 6%.
- LTFU is about 3–4% and not-evaluated a few percent: **PLAUSIBLE.**
  - Uganda/Kenya-type cohort: 
5.5% died and 2.6% were LTFU
, and 618/10,717 (5.8%) were not evaluated.
  - Kenya, Meru County: 
6.3% were LTFU and 5.1% died.

  - Ranges vary widely by country, and Zimbabwe has very high not-evaluated shares.
- A meaningful share of LTFU patients die: **SUPPORTED for TB, at the low end of the Investigator's 10–20%.**
  - Kenya CHP tracing: 
of 140 patients identified for tracing, 36 (25.7%) were traced, 90 had relocated and 14 (10.0%) had died.

  - A medRxiv cohort found that 
LTFU raised standardized five-year mortality by 2.23 percentage points.
 It noted that 
SMRs after LTFU are two to seven times higher than after cure.

  - Cape Town tracing: a small share died among true LTFU (1/30 and 3/12 in two subgroups). That is a low and noisy signal.
  - The HIV ART LTFU meta-analysis (20–60% of traced patients dead) is about ART programmes, not TB, so it should not be used for the TB range.
- Pre-treatment deaths and untreated cases are excluded: **VERIFIED, but not statin-reachable.** In Zimbabwe, 
49.6% (252/508) of pre-treatment lost-to-follow-up TB patients died.
 In Cape Town, 
2% died before starting treatment.

- Arithmetic: 6–7% × 10–20% = 0.6–1.4 pp. 6.6–7.4% / 6% = +10% to +23%. **VERIFIED.**
- The title says "opposite of Critiques 1–2", but this is Critique 2. It is probably a labelling slip and should say "opposite of Critique 1".

**EVIDENCE FOUND**
- Mortality in some settings is already above 6%, for example 
8.6% among South African adults on treatment.
 This shows that 6% is a global average, not a floor.
- A conceptual weakness: many LTFU deaths happen after treatment stops. They are not on-treatment deaths, so a statin taken during treatment may not be able to avert them. The Investigator mentions this caveat but still applies the full proportional uplift to SROI.
- "Not evaluated" includes transfers and missing records, and most of these patients are probably alive. A 10–20% death rate for that group is unsupported. The 10–20% range fits LTFU better than the not-evaluated group.
- This critique and Critique 1 pull in opposite directions. Both are plausible, and the net effect is undetermined.

**CORE CLAIM**
- Claim: A meaningful share of LTFU and not-evaluated patients die, so true mortality among treated patients exceeds 6%, and the excess is relevant to statin benefit.
- Support: **SUPPORTED for direction.** Several studies show excess mortality after LTFU, but the 10–20% magnitude and the statin relevance are only logic.
- Why: Tracing and cohort data show elevated post-LTFU mortality (about 10% in Kenya, SMR 2–7×), but no source shows these deaths are modifiable by an adjunct taken during treatment.

**OVERALL VERDICT: PARTIALLY VERIFIED.**

**REVISED CRITIQUE**
- WHO outcome categories exclude post-LTFU and pre-treatment deaths. TB-specific evidence shows elevated mortality among LTFU patients, with about 10% found dead in one Kenyan tracing study and SMRs 2–7× higher than after cure.
- True all-cause mortality among everyone who starts treatment is therefore probably somewhat above the "died" category.
- The SROI uplift is smaller than 10–23% if the statin cannot affect deaths after treatment interruption.
- **UNGROUNDED:** the exact WHO shares and the 10–20% death rate for not-evaluated patients.
- Strength: low-to-medium, direction increases. Reduce the weight because of the addressability caveat.

---

## Critique 3: Covariance between mortality and DALYs per death

**CITATION CHECK**
- GBD 2021 TB deaths and YLLs by age, country and HIV status: **NOT CHECKED.** The Investigator proposes this as an analysis and has not run it. The critique cites no paper, and the group numbers are labelled illustrative.

**CLAIM CHECK**
- The arithmetic is **VERIFIED:**
  - Mean mortality = 0.7×4% + 0.3×12% = 6.4%.
  - Death-weighted DALYs = (0.028×35 + 0.036×15)/0.064 = 23.75.
  - Expected DALYs per patient = 1.52, versus 6.4%×27 = 1.73, which is −12%.
- The illustrative inputs are internally inconsistent with the "27" baseline. The case-weighted mean of 35 and 15 is 0.7×35 + 0.3×15 = 29, not 27. If 29 were the population-average comparator, the bias would be −18%, not −12%.
- Higher mortality in older or comorbid patients: **VERIFIED.** 
Advanced age raised the risk of death during treatment in Turkey.
 
Old age, TB/HIV co-infection and baseline body weight under 35 kg increased mortality in Ethiopia.

- HIV deaths push the other way: **PLAUSIBLE and consistent with the evidence.** In Cape Town, 
the main risk factor was HIV status at treatment start.
 HIV-associated deaths tend to be in younger adults. I did not retrieve an age-specific YLL figure.
- "27 was derived without death-weighting": **UNVERIFIABLE.** I do not know how 27 was derived. If it came from GBD YLL ÷ deaths, it is already death-weighted by construction, and the critique's concern would not apply. The critique matters only if 27 came from a population or case-weighted age-at-diagnosis calculation.

**EVIDENCE FOUND**
- Two points weaken the critique:
  - Statin benefit may not be proportional across subgroups, so the right weight is deaths averted, not deaths.
  - The Investigator concedes the sign is uncertain, particularly in high-HIV settings. The stated direction "decreases" with a −10 to −15% range is therefore stronger than the evidence allows.
- The critique's structural point (E[m·d] ≠ E[m]·E[d] when the two covary) is mathematically correct.

**CORE CLAIM**
- Claim: The 27 DALYs/death input is not death-weighted, and the covariance is negative enough to bias the product upward by about 10–15%.
- Support: **LOGIC ONLY**
- Why: The covariance logic is sound, but I found no evidence on how 27 was derived or on the actual size of the covariance.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The mathematical structure is verified, and the empirical claim is **UNGROUNDED**.

**REVISED CRITIQUE**
- If dalys_per_death is a case-weighted or population-average figure rather than a death-weighted one, multiplying it by mean mortality can misstate expected DALYs averted.
- Age is a known mortality risk factor, which supports a negative covariance in low-HIV settings. HIV-associated deaths in younger adults push the other way, so the net sign is uncertain.
- **UNGROUNDED:** the −10 to −15% magnitude. It depends on how 27 was derived and on GBD age- and HIV-stratified YLL data.
- Check first whether 27 is already GBD YLL ÷ deaths. If so, drop this critique.
- Strength: low-to-medium, direction uncertain (lean decreases in low-HIV settings only).

--- Critique: Under-ascertained deaths push true mortality up, and the direction is the opposite of Critiques 1–2 ---

## Critique 1: The 6% is a mix of deaths, and only a fraction is reachable and modifiable by atorvastatin

**CITATION CHECK**
- Waitt & Squire 2011, IJTLD: **VERIFIED as existing, only partly verified on content.**
  - It is a real paper: Int J Tuberc Lung Dis 2011;15(7):871–85. 
It identified 62 studies on risk factors for death in patients started on TB treatment.

  - 
The review found two distinct epidemics with separate risk factors for death.

  - Other papers cite it as showing that 
comorbidities were risk factors in high-incidence, high-HIV settings rather than low-incidence, low-HIV settings.

  - I could not retrieve the review itself. The critique's "many deaths occur early" attribution to it is unconfirmed, though other sources support the point.
- "Country cohort studies": the Investigator named none. I found several (see Evidence Found).
- Rifampicin–atorvastatin interaction: **VERIFIED.** 
Rifampin shortened atorvastatin's half-life by 74%.
 Prescribing guidance also notes 
CYP3A inducers such as rifampin can cause variable reductions in atorvastatin plasma concentrations.


**CLAIM CHECK**
- Deaths are concentrated early, in the first weeks: **VERIFIED.**
  - Zambia, 1,063 deaths: 
58.1% occurred in the first month and 75.1% in the first two months.
 
The median time to death was 21 days.

  - Kenya, Meru County: 
76% of deaths occurred within three months of starting treatment.

  - Ethiopia: 
More than 70% of deaths occur in the first two months.

  - Taiwan: 
Underweight was associated with higher mortality only in the first 8 weeks.

- Very sick, malnourished or advanced-HIV patients dominate early deaths: **VERIFIED.** 
The major risk factors for early death are HIV positivity, old age, being underweight and retreatment.

- Some deaths are non-TB causes: **VERIFIED.** A Taiwanese review classified deaths as TB-related or non-TB-related. 
Most TB-related deaths occurred early, with a median survival of 20 days.
 The non-TB share varies by setting, and I did not find a pooled figure.
- Some deaths occur before treatment starts: **VERIFIED, but outside the treated cohort.** In a US study, 
TB-related death occurred during treatment for 75% of decedents and before treatment began for 25%.
 These deaths would not be in an on-treatment 6%.
- Rifampicin induction delays onset of statin benefit: **PLAUSIBLE.** The interaction is real. The timing of induction relative to benefit is an inference, and the Investigator labels it as one.
- The arithmetic 6% × 0.7 × 0.85 = 3.57%: **VERIFIED** (≈3.6%). I could not verify the 3.9% threshold. It comes from the source model.
- The 30% and 15% shares are placeholders, as the Investigator says. The 30% is plausible for deaths within about 2 weeks, given the Zambian median of 21 days. The 15% non-TB share is unsupported.

**EVIDENCE FOUND**
- The timing evidence above comes from Zambia, Kenya, Ethiopia, Turkey, Cameroon and India. It supports the early-death premise strongly.
- Caveat the Investigator did not raise: if the model's statin effect size comes from a trial population, it already excludes very early or ineligible deaths. Applying the "addressable share" haircut on top would double-count.
- The eligibility factor appears in the mechanism formula but not in the worked example.
- Early deaths may be partly reversible with timely care. 
Deaths within 14 days of anti-TB treatment suggest some mortality may have been reversible with earlier therapy.
 That cuts against treating all very early deaths as unreachable.

**CORE CLAIM**
- Claim: A large enough share of the 6% is unreachable or non-TB (about 35–40% combined) to push the effective baseline below 3.9%.
- Support: **LOGIC ONLY**
- Why: Early concentration of deaths is directly supported, but the specific shares are acknowledged placeholders, and I found no evidence on the statin onset-time or non-TB share needed to reach the threshold.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The direction (the addressable share is below 6%) is well supported. The magnitude, and the claim that the threshold is crossed, are ungrounded.

**REVISED CRITIQUE**
- Deaths during TB treatment are heavily front-loaded. In several African cohorts, roughly 55–75% occur within 1–2 months, and the median is about 3 weeks in Zambia.
- Early deaths are concentrated in HIV-positive, underweight and older patients. Rifampicin cuts atorvastatin exposure substantially.
- Applying the 6% to all patients probably overstates the share a statin could avert.
- **UNGROUNDED:** the size of the haircut. Needed evidence: statin time-to-effect, the TB-attributable share of deaths, and whether the model's effect size already reflects an enrolled trial population.
- Strength: medium, direction decreases, with a caution against double-counting.

---

## Critique 2: Under-ascertained deaths push true mortality up

**CITATION CHECK**
- WHO Global TB Report outcome categories: **VERIFIED for definitions.** WHO data lists 
treatment success (cured or completed), failed, died, lost to follow-up, or not evaluated
 as the outcome categories.
- WHO figures of "~5–6% died, ~3–4% LTFU, a few % not evaluated": **UNVERIFIED.** I could not retrieve the global outcome table. 
Global treatment success was 88% in 2023 and 2022.
 That leaves about 12% across all other outcomes, which is consistent with the Investigator's recall but does not confirm it.
- The tracing studies the Investigator "believed" existed: **found, see below.**

**CLAIM CHECK**
- The 6% comes from the "died" category and excludes LTFU and not-evaluated patients: **PLAUSIBLE.** WHO's definition supports the structure. I cannot confirm how the source model derived its 6%.
- LTFU is about 3–4% and not-evaluated a few percent: **PLAUSIBLE.**
  - Uganda/Kenya-type cohort: 
5.5% died and 2.6% were LTFU
, and 618/10,717 (5.8%) were not evaluated.
  - Kenya, Meru County: 
6.3% were LTFU and 5.1% died.

  - Ranges vary widely by country, and Zimbabwe has very high not-evaluated shares.
- A meaningful share of LTFU patients die: **SUPPORTED for TB, at the low end of the Investigator's 10–20%.**
  - Kenya CHP tracing: 
of 140 patients identified for tracing, 36 (25.7%) were traced, 90 had relocated and 14 (10.0%) had died.

  - A medRxiv cohort found that 
LTFU raised standardized five-year mortality by 2.23 percentage points.
 It noted that 
SMRs after LTFU are two to seven times higher than after cure.

  - Cape Town tracing: a small share died among true LTFU (1/30 and 3/12 in two subgroups). That is a low and noisy signal.
  - The HIV ART LTFU meta-analysis (20–60% of traced patients dead) is about ART programmes, not TB, so it should not be used for the TB range.
- Pre-treatment deaths and untreated cases are excluded: **VERIFIED, but not statin-reachable.** In Zimbabwe, 
49.6% (252/508) of pre-treatment lost-to-follow-up TB patients died.
 In Cape Town, 
2% died before starting treatment.

- Arithmetic: 6–7% × 10–20% = 0.6–1.4 pp. 6.6–7.4% / 6% = +10% to +23%. **VERIFIED.**
- The title says "opposite of Critiques 1–2", but this is Critique 2. It is probably a labelling slip and should say "opposite of Critique 1".

**EVIDENCE FOUND**
- Mortality in some settings is already above 6%, for example 
8.6% among South African adults on treatment.
 This shows that 6% is a global average, not a floor.
- A conceptual weakness: many LTFU deaths happen after treatment stops. They are not on-treatment deaths, so a statin taken during treatment may not be able to avert them. The Investigator mentions this caveat but still applies the full proportional uplift to SROI.
- "Not evaluated" includes transfers and missing records, and most of these patients are probably alive. A 10–20% death rate for that group is unsupported. The 10–20% range fits LTFU better than the not-evaluated group.
- This critique and Critique 1 pull in opposite directions. Both are plausible, and the net effect is undetermined.

**CORE CLAIM**
- Claim: A meaningful share of LTFU and not-evaluated patients die, so true mortality among treated patients exceeds 6%, and the excess is relevant to statin benefit.
- Support: **SUPPORTED for direction.** Several studies show excess mortality after LTFU, but the 10–20% magnitude and the statin relevance are only logic.
- Why: Tracing and cohort data show elevated post-LTFU mortality (about 10% in Kenya, SMR 2–7×), but no source shows these deaths are modifiable by an adjunct taken during treatment.

**OVERALL VERDICT: PARTIALLY VERIFIED.**

**REVISED CRITIQUE**
- WHO outcome categories exclude post-LTFU and pre-treatment deaths. TB-specific evidence shows elevated mortality among LTFU patients, with about 10% found dead in one Kenyan tracing study and SMRs 2–7× higher than after cure.
- True all-cause mortality among everyone who starts treatment is therefore probably somewhat above the "died" category.
- The SROI uplift is smaller than 10–23% if the statin cannot affect deaths after treatment interruption.
- **UNGROUNDED:** the exact WHO shares and the 10–20% death rate for not-evaluated patients.
- Strength: low-to-medium, direction increases. Reduce the weight because of the addressability caveat.

---

## Critique 3: Covariance between mortality and DALYs per death

**CITATION CHECK**
- GBD 2021 TB deaths and YLLs by age, country and HIV status: **NOT CHECKED.** The Investigator proposes this as an analysis and has not run it. The critique cites no paper, and the group numbers are labelled illustrative.

**CLAIM CHECK**
- The arithmetic is **VERIFIED:**
  - Mean mortality = 0.7×4% + 0.3×12% = 6.4%.
  - Death-weighted DALYs = (0.028×35 + 0.036×15)/0.064 = 23.75.
  - Expected DALYs per patient = 1.52, versus 6.4%×27 = 1.73, which is −12%.
- The illustrative inputs are internally inconsistent with the "27" baseline. The case-weighted mean of 35 and 15 is 0.7×35 + 0.3×15 = 29, not 27. If 29 were the population-average comparator, the bias would be −18%, not −12%.
- Higher mortality in older or comorbid patients: **VERIFIED.** 
Advanced age raised the risk of death during treatment in Turkey.
 
Old age, TB/HIV co-infection and baseline body weight under 35 kg increased mortality in Ethiopia.

- HIV deaths push the other way: **PLAUSIBLE and consistent with the evidence.** In Cape Town, 
the main risk factor was HIV status at treatment start.
 HIV-associated deaths tend to be in younger adults. I did not retrieve an age-specific YLL figure.
- "27 was derived without death-weighting": **UNVERIFIABLE.** I do not know how 27 was derived. If it came from GBD YLL ÷ deaths, it is already death-weighted by construction, and the critique's concern would not apply. The critique matters only if 27 came from a population or case-weighted age-at-diagnosis calculation.

**EVIDENCE FOUND**
- Two points weaken the critique:
  - Statin benefit may not be proportional across subgroups, so the right weight is deaths averted, not deaths.
  - The Investigator concedes the sign is uncertain, particularly in high-HIV settings. The stated direction "decreases" with a −10 to −15% range is therefore stronger than the evidence allows.
- The critique's structural point (E[m·d] ≠ E[m]·E[d] when the two covary) is mathematically correct.

**CORE CLAIM**
- Claim: The 27 DALYs/death input is not death-weighted, and the covariance is negative enough to bias the product upward by about 10–15%.
- Support: **LOGIC ONLY**
- Why: The covariance logic is sound, but I found no evidence on how 27 was derived or on the actual size of the covariance.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The mathematical structure is verified, and the empirical claim is **UNGROUNDED**.

**REVISED CRITIQUE**
- If dalys_per_death is a case-weighted or population-average figure rather than a death-weighted one, multiplying it by mean mortality can misstate expected DALYs averted.
- Age is a known mortality risk factor, which supports a negative covariance in low-HIV settings. HIV-associated deaths in younger adults push the other way, so the net sign is uncertain.
- **UNGROUNDED:** the −10 to −15% magnitude. It depends on how 27 was derived and on GBD age- and HIV-stratified YLL data.
- Check first whether 27 is already GBD YLL ÷ deaths. If so, drop this critique.
- Strength: low-to-medium, direction uncertain (lean decreases in low-HIV settings only).

--- Critique: Covariance between mortality and DALYs per death means the product of means is not the mean of the product ---

## Critique 1: The 6% is a mix of deaths, and only a fraction is reachable and modifiable by atorvastatin

**CITATION CHECK**
- Waitt & Squire 2011, IJTLD: **VERIFIED as existing, only partly verified on content.**
  - It is a real paper: Int J Tuberc Lung Dis 2011;15(7):871–85. 
It identified 62 studies on risk factors for death in patients started on TB treatment.

  - 
The review found two distinct epidemics with separate risk factors for death.

  - Other papers cite it as showing that 
comorbidities were risk factors in high-incidence, high-HIV settings rather than low-incidence, low-HIV settings.

  - I could not retrieve the review itself. The critique's "many deaths occur early" attribution to it is unconfirmed, though other sources support the point.
- "Country cohort studies": the Investigator named none. I found several (see Evidence Found).
- Rifampicin–atorvastatin interaction: **VERIFIED.** 
Rifampin shortened atorvastatin's half-life by 74%.
 Prescribing guidance also notes 
CYP3A inducers such as rifampin can cause variable reductions in atorvastatin plasma concentrations.


**CLAIM CHECK**
- Deaths are concentrated early, in the first weeks: **VERIFIED.**
  - Zambia, 1,063 deaths: 
58.1% occurred in the first month and 75.1% in the first two months.
 
The median time to death was 21 days.

  - Kenya, Meru County: 
76% of deaths occurred within three months of starting treatment.

  - Ethiopia: 
More than 70% of deaths occur in the first two months.

  - Taiwan: 
Underweight was associated with higher mortality only in the first 8 weeks.

- Very sick, malnourished or advanced-HIV patients dominate early deaths: **VERIFIED.** 
The major risk factors for early death are HIV positivity, old age, being underweight and retreatment.

- Some deaths are non-TB causes: **VERIFIED.** A Taiwanese review classified deaths as TB-related or non-TB-related. 
Most TB-related deaths occurred early, with a median survival of 20 days.
 The non-TB share varies by setting, and I did not find a pooled figure.
- Some deaths occur before treatment starts: **VERIFIED, but outside the treated cohort.** In a US study, 
TB-related death occurred during treatment for 75% of decedents and before treatment began for 25%.
 These deaths would not be in an on-treatment 6%.
- Rifampicin induction delays onset of statin benefit: **PLAUSIBLE.** The interaction is real. The timing of induction relative to benefit is an inference, and the Investigator labels it as one.
- The arithmetic 6% × 0.7 × 0.85 = 3.57%: **VERIFIED** (≈3.6%). I could not verify the 3.9% threshold. It comes from the source model.
- The 30% and 15% shares are placeholders, as the Investigator says. The 30% is plausible for deaths within about 2 weeks, given the Zambian median of 21 days. The 15% non-TB share is unsupported.

**EVIDENCE FOUND**
- The timing evidence above comes from Zambia, Kenya, Ethiopia, Turkey, Cameroon and India. It supports the early-death premise strongly.
- Caveat the Investigator did not raise: if the model's statin effect size comes from a trial population, it already excludes very early or ineligible deaths. Applying the "addressable share" haircut on top would double-count.
- The eligibility factor appears in the mechanism formula but not in the worked example.
- Early deaths may be partly reversible with timely care. 
Deaths within 14 days of anti-TB treatment suggest some mortality may have been reversible with earlier therapy.
 That cuts against treating all very early deaths as unreachable.

**CORE CLAIM**
- Claim: A large enough share of the 6% is unreachable or non-TB (about 35–40% combined) to push the effective baseline below 3.9%.
- Support: **LOGIC ONLY**
- Why: Early concentration of deaths is directly supported, but the specific shares are acknowledged placeholders, and I found no evidence on the statin onset-time or non-TB share needed to reach the threshold.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The direction (the addressable share is below 6%) is well supported. The magnitude, and the claim that the threshold is crossed, are ungrounded.

**REVISED CRITIQUE**
- Deaths during TB treatment are heavily front-loaded. In several African cohorts, roughly 55–75% occur within 1–2 months, and the median is about 3 weeks in Zambia.
- Early deaths are concentrated in HIV-positive, underweight and older patients. Rifampicin cuts atorvastatin exposure substantially.
- Applying the 6% to all patients probably overstates the share a statin could avert.
- **UNGROUNDED:** the size of the haircut. Needed evidence: statin time-to-effect, the TB-attributable share of deaths, and whether the model's effect size already reflects an enrolled trial population.
- Strength: medium, direction decreases, with a caution against double-counting.

---

## Critique 2: Under-ascertained deaths push true mortality up

**CITATION CHECK**
- WHO Global TB Report outcome categories: **VERIFIED for definitions.** WHO data lists 
treatment success (cured or completed), failed, died, lost to follow-up, or not evaluated
 as the outcome categories.
- WHO figures of "~5–6% died, ~3–4% LTFU, a few % not evaluated": **UNVERIFIED.** I could not retrieve the global outcome table. 
Global treatment success was 88% in 2023 and 2022.
 That leaves about 12% across all other outcomes, which is consistent with the Investigator's recall but does not confirm it.
- The tracing studies the Investigator "believed" existed: **found, see below.**

**CLAIM CHECK**
- The 6% comes from the "died" category and excludes LTFU and not-evaluated patients: **PLAUSIBLE.** WHO's definition supports the structure. I cannot confirm how the source model derived its 6%.
- LTFU is about 3–4% and not-evaluated a few percent: **PLAUSIBLE.**
  - Uganda/Kenya-type cohort: 
5.5% died and 2.6% were LTFU
, and 618/10,717 (5.8%) were not evaluated.
  - Kenya, Meru County: 
6.3% were LTFU and 5.1% died.

  - Ranges vary widely by country, and Zimbabwe has very high not-evaluated shares.
- A meaningful share of LTFU patients die: **SUPPORTED for TB, at the low end of the Investigator's 10–20%.**
  - Kenya CHP tracing: 
of 140 patients identified for tracing, 36 (25.7%) were traced, 90 had relocated and 14 (10.0%) had died.

  - A medRxiv cohort found that 
LTFU raised standardized five-year mortality by 2.23 percentage points.
 It noted that 
SMRs after LTFU are two to seven times higher than after cure.

  - Cape Town tracing: a small share died among true LTFU (1/30 and 3/12 in two subgroups). That is a low and noisy signal.
  - The HIV ART LTFU meta-analysis (20–60% of traced patients dead) is about ART programmes, not TB, so it should not be used for the TB range.
- Pre-treatment deaths and untreated cases are excluded: **VERIFIED, but not statin-reachable.** In Zimbabwe, 
49.6% (252/508) of pre-treatment lost-to-follow-up TB patients died.
 In Cape Town, 
2% died before starting treatment.

- Arithmetic: 6–7% × 10–20% = 0.6–1.4 pp. 6.6–7.4% / 6% = +10% to +23%. **VERIFIED.**
- The title says "opposite of Critiques 1–2", but this is Critique 2. It is probably a labelling slip and should say "opposite of Critique 1".

**EVIDENCE FOUND**
- Mortality in some settings is already above 6%, for example 
8.6% among South African adults on treatment.
 This shows that 6% is a global average, not a floor.
- A conceptual weakness: many LTFU deaths happen after treatment stops. They are not on-treatment deaths, so a statin taken during treatment may not be able to avert them. The Investigator mentions this caveat but still applies the full proportional uplift to SROI.
- "Not evaluated" includes transfers and missing records, and most of these patients are probably alive. A 10–20% death rate for that group is unsupported. The 10–20% range fits LTFU better than the not-evaluated group.
- This critique and Critique 1 pull in opposite directions. Both are plausible, and the net effect is undetermined.

**CORE CLAIM**
- Claim: A meaningful share of LTFU and not-evaluated patients die, so true mortality among treated patients exceeds 6%, and the excess is relevant to statin benefit.
- Support: **SUPPORTED for direction.** Several studies show excess mortality after LTFU, but the 10–20% magnitude and the statin relevance are only logic.
- Why: Tracing and cohort data show elevated post-LTFU mortality (about 10% in Kenya, SMR 2–7×), but no source shows these deaths are modifiable by an adjunct taken during treatment.

**OVERALL VERDICT: PARTIALLY VERIFIED.**

**REVISED CRITIQUE**
- WHO outcome categories exclude post-LTFU and pre-treatment deaths. TB-specific evidence shows elevated mortality among LTFU patients, with about 10% found dead in one Kenyan tracing study and SMRs 2–7× higher than after cure.
- True all-cause mortality among everyone who starts treatment is therefore probably somewhat above the "died" category.
- The SROI uplift is smaller than 10–23% if the statin cannot affect deaths after treatment interruption.
- **UNGROUNDED:** the exact WHO shares and the 10–20% death rate for not-evaluated patients.
- Strength: low-to-medium, direction increases. Reduce the weight because of the addressability caveat.

---

## Critique 3: Covariance between mortality and DALYs per death

**CITATION CHECK**
- GBD 2021 TB deaths and YLLs by age, country and HIV status: **NOT CHECKED.** The Investigator proposes this as an analysis and has not run it. The critique cites no paper, and the group numbers are labelled illustrative.

**CLAIM CHECK**
- The arithmetic is **VERIFIED:**
  - Mean mortality = 0.7×4% + 0.3×12% = 6.4%.
  - Death-weighted DALYs = (0.028×35 + 0.036×15)/0.064 = 23.75.
  - Expected DALYs per patient = 1.52, versus 6.4%×27 = 1.73, which is −12%.
- The illustrative inputs are internally inconsistent with the "27" baseline. The case-weighted mean of 35 and 15 is 0.7×35 + 0.3×15 = 29, not 27. If 29 were the population-average comparator, the bias would be −18%, not −12%.
- Higher mortality in older or comorbid patients: **VERIFIED.** 
Advanced age raised the risk of death during treatment in Turkey.
 
Old age, TB/HIV co-infection and baseline body weight under 35 kg increased mortality in Ethiopia.

- HIV deaths push the other way: **PLAUSIBLE and consistent with the evidence.** In Cape Town, 
the main risk factor was HIV status at treatment start.
 HIV-associated deaths tend to be in younger adults. I did not retrieve an age-specific YLL figure.
- "27 was derived without death-weighting": **UNVERIFIABLE.** I do not know how 27 was derived. If it came from GBD YLL ÷ deaths, it is already death-weighted by construction, and the critique's concern would not apply. The critique matters only if 27 came from a population or case-weighted age-at-diagnosis calculation.

**EVIDENCE FOUND**
- Two points weaken the critique:
  - Statin benefit may not be proportional across subgroups, so the right weight is deaths averted, not deaths.
  - The Investigator concedes the sign is uncertain, particularly in high-HIV settings. The stated direction "decreases" with a −10 to −15% range is therefore stronger than the evidence allows.
- The critique's structural point (E[m·d] ≠ E[m]·E[d] when the two covary) is mathematically correct.

**CORE CLAIM**
- Claim: The 27 DALYs/death input is not death-weighted, and the covariance is negative enough to bias the product upward by about 10–15%.
- Support: **LOGIC ONLY**
- Why: The covariance logic is sound, but I found no evidence on how 27 was derived or on the actual size of the covariance.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The mathematical structure is verified, and the empirical claim is **UNGROUNDED**.

**REVISED CRITIQUE**
- If dalys_per_death is a case-weighted or population-average figure rather than a death-weighted one, multiplying it by mean mortality can misstate expected DALYs averted.
- Age is a known mortality risk factor, which supports a negative covariance in low-HIV settings. HIV-associated deaths in younger adults push the other way, so the net sign is uncertain.
- **UNGROUNDED:** the −10 to −15% magnitude. It depends on how 27 was derived and on GBD age- and HIV-stratified YLL data.
- Check first whether 27 is already GBD YLL ÷ deaths. If so, drop this critique.
- Strength: low-to-medium, direction uncertain (lean decreases in low-HIV settings only).

--- Critique: A global-average mortality may not match the countries where an atorvastatin adjunct would actually be deployed ---

## Critique 1: Global-average mortality vs. deployment countries

**CITATION CHECK:** The critique cites no papers. It names the WHO Global TB Report and GBD as suggested evidence only.

**CLAIM CHECK**
- **TB burden is concentrated in India, Indonesia, the Philippines, Nigeria and South Africa: VERIFIED.** The CDC/WHO 2019 summary lists 
India (26%), Indonesia (8.5%), China (8.4%), the Philippines (6.0%), Pakistan (5.7%), Nigeria (4.4%), Bangladesh (3.6%), and South Africa (3.6%)
 as the eight countries with two thirds of global cases.
- **On-treatment mortality differs by country: PLAUSIBLE.** A model-based analysis of Brazil, India and South Africa reports different deviations in deaths during treatment in each country (
13.7% higher than predicted in Brazil, 1.7% in India and 21.8% in South Africa
). That shows heterogeneity in how deaths changed, not baseline levels.
- **India about 4–5% and South Africa about 8–10%: UNVERIFIABLE.** The critique itself flags these as from memory. My searches did not return the WHO country-level cohort tables. An Indian systematic review of treatment-phase case fatality exists (
India accounts for a third of global TB deaths; the review covers cohort studies and trial control arms
). I did not retrieve its pooled estimate.
- **The global 6% figure, the 3.9% threshold and the "Phase III and uptake concentrate in a handful of countries" claim: UNVERIFIABLE.** These are properties of the model or its deployment plan, which I could not check.

**EVIDENCE FOUND**
- WHO reports 
a sustained high treatment success rate for drug-susceptible TB, 88% globally in 2023 and 2022
. The residual 12% (deaths, loss to follow-up, failure) leaves room for substantial country spread.
- One caveat the critique misses: trial-enrolled patients usually have lower on-treatment mortality than programmatic cohorts. The relevant baseline for a Phase III-based effect may be below WHO country figures. That would push the number down in every country.

**CORE CLAIM**
- Claim: Country-weighted on-treatment mortality could differ materially from the single global 6% figure, depending on deployment mix.
- Support: **LOGIC ONLY.**
- Why: Heterogeneity is plausible and directionally supported, but I found no country-specific on-treatment death percentages to size it.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The structural point is sound: a global average is a proxy for a deployment-weighted one. The country mortality numbers remain UNGROUNDED. The critique correctly labels itself a sensitivity issue with uncertain direction.

**REVISED CRITIQUE:** Baseline mortality is a global figure, but TB burden is concentrated in a few countries whose on-treatment mortality probably differs (HIV, age mix, delay to diagnosis). The model should show a case-weighted sensitivity range. Remove the specific India and South Africa percentages until sourced from WHO country cohort tables. Also consider trial-versus-programme mortality differences. Direction: uncertain. Magnitude: medium-low. Strength: moderate-weak.

---

## Critique 2: Industry base rates imply about 15–25%, not 40%

**CITATION CHECK**
- **BIO/Informa/QLS 2021 (2011–2020): VERIFIED.** It is cited in multiple papers as 
"Clinical Development Success Rates and Contributing Factors 2011–2020" (2021)
.
- **Wong, Siah & Lo 2019, *Biostatistics*: VERIFIED (exists).** It is 
Biostatistics 2019 Apr 1;20(2):273-286
.
  - There is a corrigendum. 
The original Tables 1 and 2 had errors in the Phase 2→3 and Phase 3→approval columns.
 The critique's "similar overall figures" from memory may come from the uncorrected numbers, so they need checking against the corrected tables.

**CLAIM CHECK**
- **Phase II→III about 29%: VERIFIED.** BIO's figure is 
28.9%
.
- **Phase III→NDA/BLA about 58%: VERIFIED.** The BIO table gives 
57.8%
 for Phase III.
- **Filing→approval about 91%: UNVERIFIABLE** in my results, though plausible.
- **Arithmetic: VERIFIED.** 0.289 × 0.578 ≈ 16.7%. The 1.6×–2.7× premium and the 37–50% cut from moving 0.40 to 0.20–0.25 are correct.
- **Infectious-disease uplift gives Phase III about 65% and a product of 24–26%: PARTIALLY CONTRADICTED.**
  - One analysis of a different dataset finds infectious diseases have 
the highest unconditional success rate at 14.0%, with a Phase III success rate of 80.9% and application success of 95.6%
.
  - This is a different methodology from BIO and probably uses different phase definitions. Still, it suggests the critique's assumed 65% Phase III rate for infectious disease may be too low.
  - With Phase II at about 37–40% and Phase III at about 80%, the product is roughly 30%, not 24–26%.
  - It would still be below 40%, but near the 0.26 break-even. The critique's central 0.20 looks somewhat pessimistic.
- **Anti-infective overall rates are not dramatically above average: VERIFIED.** Anti-infective Phase I→approval is 
fairly stable around 10.6%
. Wong et al. report that 
only 6.8% of non-industry-sponsored vaccine and 8.2% of non-vaccine infectious-disease programs transition from phase 1 to approval
. This mildly supports the critique's skepticism.
- **Repurposing premium applies mostly to safety attrition, not efficacy: LOGIC ONLY.** The critique flags this as UNGROUNDED, which is accurate.
- **The PIIc success estimate of 0.5 and the decomposition: UNVERIFIABLE** (own inference, as stated).
- **The 0.26 break-even and CG's 40%: UNVERIFIABLE.** They come from the model.

**EVIDENCE FOUND**
- Hay et al. 2014 (via a secondary source) put the non-oncology Phase II→III rate at 
34.8%
 and Phase III success at 
54%
. This corroborates the general range.
- Industry transition rates measure drug progression, which includes business-driven terminations. They may understate the scientific probability of success for a well-funded academic or public-health program. They are also not defined identically to CG's p_success, which may start at Phase IIc and end at adoption. The critique doesn't discuss this definitional mismatch.
- The critique's internal cross-references ("Critique 2", "Critique 4") do not match this batch's numbering.

**CORE CLAIM**
- Claim: Industry reference-class rates imply P(II and III succeed) of roughly 15–25%, so CG's 40% needs an unstated premium of about 1.6× or more.
- Support: **SUPPORTED** for the base-rate numbers (BIO's 28.9% and 57.8%). The conclusion that 40% is unjustified is LOGIC ONLY, because the definitional match is untested.
- Why: The BIO rates were directly confirmed, but the infectious-disease uplift could be larger than assumed and CG's endpoint definition is unknown.

**OVERALL VERDICT: PARTIALLY VERIFIED.**

**REVISED CRITIQUE:** CG gives no reference class for 40%. BIO 2011–2020 rates (Phase II→III 28.9%, Phase III→filing 57.8%) imply about 17% for both phases. Infectious-disease-specific data (one analysis: Phase III about 81%) lift this to roughly 25–32%, which is still below 40% and close to the 0.26 break-even. Remove the claim that the infectious-disease-adjusted product is 24–26%. Replace it with a range of about 25–32%, and state that the Wong 2019 figures need checking against the corrected tables. The own-inference decomposition is UNGROUNDED. The repurposing-premium argument is plausible but unsourced. Strength: moderate-to-strong on direction, with the size of the gap uncertain. Magnitude: medium-large.

---

## Critique 3: TB host-directed and adjunctive therapy record is poor

**CITATION CHECK**
- **Wejse et al. 2009 (Guinea-Bissau): VERIFIED.** It is 
Wejse C, et al., Am J Respir Crit Care Med 2009;179:843–50
. A review summarises it as showing 
no difference in TB score, 12-month mortality, or sputum smear conversion times between arms
.
- **Martineau et al. 2011 (London): VERIFIED, with nuance.** The trial found 
median time to culture conversion of 36.0 vs 43.5 days (adjusted HR 1.39, 95% CI 0.90–2.16; p=0.14)
. It also found 
a significant effect in participants with the tt genotype of the TaqI polymorphism
. "No overall benefit" is accurate. The genotype signal is omitted.
- **ACT HIV 2023: VERIFIED.** Deaths were 
116/263 (44.1%) with dexamethasone vs 126/257 (49.0%) with placebo (HR 0.85, 95% CI 0.66–1.10; P=0.22)
. The trial 
did not confer a benefit on survival or any secondary end point
.
- **Thwaites 2004: VERIFIED.** The trial showed 
improved survival in patients over 14 years of age with tuberculous meningitis
. The 
benefit was uncertain in the 98 HIV-positive participants
. That fits the critique's "didn't generalise" framing.
- **REMoxTB, OFLOTUB, RIFAQUIN (all NEJM 2014) failing non-inferiority for 4-month regimens, and Study 31/A5349 succeeding: NOT CHECKED.** My final search was rejected. They match my background knowledge, but they are not verified in this session.
- **Parihar and colleagues, "Karakousis group": PARTIALLY MISATTRIBUTED (from background knowledge, unchecked).** I believe the 2014 Parihar statin–macrophage–mouse paper came from Reto Guler's group in Cape Town. The Karakousis group published separate pravastatin mouse work. The critique conflates the two.
- **Wallis & Hafner; Kolloli & Subbian reviews: NOT CHECKED.**

**CLAIM CHECK**
- **"No HDT is WHO-recommended for drug-sensitive pulmonary TB": PLAUSIBLE, unchecked.**
- **Class success rate of 10–20%: UNVERIFIABLE** (own inference, as stated).
- **At p=0.15, cost-effectiveness is about 38% of CG's base case: VERIFIED arithmetically** (0.15/0.40 = 0.375).

**EVIDENCE FOUND**
- A vitamin D meta-analysis found 
a significantly higher proportion of sputum culture conversion overall (OR 1.22, 1.04–1.43), but no shortening of time to conversion
. This is a mild counterweight to "null."
- The 2025 LAST ACT trial in HIV-negative adults, stratified by LTA4H genotype, found 
neither non-inferiority nor superiority of placebo established in CC/CT-genotype adults
. A combined analysis 
supports dexamethasone's modest survival benefit in all HIV-negative adults
. This reinforces that even the one adopted class member has a modest, heterogeneous effect.
- **Reference-class weakness:**
  - The list is a hand-picked set of failures, so it is vulnerable to selection bias.
  - Several trials were themselves Phase II/III, not Phase II→III transitions.
  - The ACT HIV trial concerned TB meningitis mortality, a very different setting from pulmonary TB with a culture-conversion or relapse endpoint.
  - Most statin evidence is preclinical, so a 10–20% rate from this class has no denominator.

**CORE CLAIM**
- Claim: The appropriate TB-specific reference class has a success rate well under 40% from Phase II onward (about 10–20%).
- Support: **LOGIC ONLY.**
- Why: The individual trial facts check out, but the class rate is an unpublished inference built from a non-systematic, selected list.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The vitamin D, dexamethasone and Thwaites facts are real and accurately characterised. The quantitative class rate stays UNGROUNDED, and the statin attribution is dubious.

**REVISED CRITIQUE:** TB adjunctive and host-directed trials have a mixed record. Vitamin D showed no overall benefit on culture conversion (Wejse 2009, Martineau 2011). Dexamethasone in HIV-associated TB meningitis was null (ACT HIV, HR 0.85, 0.66–1.10). Dexamethasone in HIV-negative TB meningitis showed benefit (Thwaites 2004), though it is modest and heterogeneous. The fluoroquinolone 4-month failures and the Study 31 success are from the critique's memory and need a check. Remove the Parihar/Karakousis attribution until verified. The 10–20% class rate and the blended p_success of 0.2–0.3 are UNGROUNDED inferences. They are plausible, but the reference class is selective and the endpoint context differs from pulmonary TB. Direction: lowers p_success. Magnitude: medium-large. Strength: moderate, as a qualitative prior shift rather than a quantified one.

--- Critique: Industry phase-transition base rates put "II and III both succeed" at roughly 15–25%, so 40% requires an unstated premium of about 1.6–2.7× ---

## Critique 1: Global-average mortality vs. deployment countries

**CITATION CHECK:** The critique cites no papers. It names the WHO Global TB Report and GBD as suggested evidence only.

**CLAIM CHECK**
- **TB burden is concentrated in India, Indonesia, the Philippines, Nigeria and South Africa: VERIFIED.** The CDC/WHO 2019 summary lists 
India (26%), Indonesia (8.5%), China (8.4%), the Philippines (6.0%), Pakistan (5.7%), Nigeria (4.4%), Bangladesh (3.6%), and South Africa (3.6%)
 as the eight countries with two thirds of global cases.
- **On-treatment mortality differs by country: PLAUSIBLE.** A model-based analysis of Brazil, India and South Africa reports different deviations in deaths during treatment in each country (
13.7% higher than predicted in Brazil, 1.7% in India and 21.8% in South Africa
). That shows heterogeneity in how deaths changed, not baseline levels.
- **India about 4–5% and South Africa about 8–10%: UNVERIFIABLE.** The critique itself flags these as from memory. My searches did not return the WHO country-level cohort tables. An Indian systematic review of treatment-phase case fatality exists (
India accounts for a third of global TB deaths; the review covers cohort studies and trial control arms
). I did not retrieve its pooled estimate.
- **The global 6% figure, the 3.9% threshold and the "Phase III and uptake concentrate in a handful of countries" claim: UNVERIFIABLE.** These are properties of the model or its deployment plan, which I could not check.

**EVIDENCE FOUND**
- WHO reports 
a sustained high treatment success rate for drug-susceptible TB, 88% globally in 2023 and 2022
. The residual 12% (deaths, loss to follow-up, failure) leaves room for substantial country spread.
- One caveat the critique misses: trial-enrolled patients usually have lower on-treatment mortality than programmatic cohorts. The relevant baseline for a Phase III-based effect may be below WHO country figures. That would push the number down in every country.

**CORE CLAIM**
- Claim: Country-weighted on-treatment mortality could differ materially from the single global 6% figure, depending on deployment mix.
- Support: **LOGIC ONLY.**
- Why: Heterogeneity is plausible and directionally supported, but I found no country-specific on-treatment death percentages to size it.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The structural point is sound: a global average is a proxy for a deployment-weighted one. The country mortality numbers remain UNGROUNDED. The critique correctly labels itself a sensitivity issue with uncertain direction.

**REVISED CRITIQUE:** Baseline mortality is a global figure, but TB burden is concentrated in a few countries whose on-treatment mortality probably differs (HIV, age mix, delay to diagnosis). The model should show a case-weighted sensitivity range. Remove the specific India and South Africa percentages until sourced from WHO country cohort tables. Also consider trial-versus-programme mortality differences. Direction: uncertain. Magnitude: medium-low. Strength: moderate-weak.

---

## Critique 2: Industry base rates imply about 15–25%, not 40%

**CITATION CHECK**
- **BIO/Informa/QLS 2021 (2011–2020): VERIFIED.** It is cited in multiple papers as 
"Clinical Development Success Rates and Contributing Factors 2011–2020" (2021)
.
- **Wong, Siah & Lo 2019, *Biostatistics*: VERIFIED (exists).** It is 
Biostatistics 2019 Apr 1;20(2):273-286
.
  - There is a corrigendum. 
The original Tables 1 and 2 had errors in the Phase 2→3 and Phase 3→approval columns.
 The critique's "similar overall figures" from memory may come from the uncorrected numbers, so they need checking against the corrected tables.

**CLAIM CHECK**
- **Phase II→III about 29%: VERIFIED.** BIO's figure is 
28.9%
.
- **Phase III→NDA/BLA about 58%: VERIFIED.** The BIO table gives 
57.8%
 for Phase III.
- **Filing→approval about 91%: UNVERIFIABLE** in my results, though plausible.
- **Arithmetic: VERIFIED.** 0.289 × 0.578 ≈ 16.7%. The 1.6×–2.7× premium and the 37–50% cut from moving 0.40 to 0.20–0.25 are correct.
- **Infectious-disease uplift gives Phase III about 65% and a product of 24–26%: PARTIALLY CONTRADICTED.**
  - One analysis of a different dataset finds infectious diseases have 
the highest unconditional success rate at 14.0%, with a Phase III success rate of 80.9% and application success of 95.6%
.
  - This is a different methodology from BIO and probably uses different phase definitions. Still, it suggests the critique's assumed 65% Phase III rate for infectious disease may be too low.
  - With Phase II at about 37–40% and Phase III at about 80%, the product is roughly 30%, not 24–26%.
  - It would still be below 40%, but near the 0.26 break-even. The critique's central 0.20 looks somewhat pessimistic.
- **Anti-infective overall rates are not dramatically above average: VERIFIED.** Anti-infective Phase I→approval is 
fairly stable around 10.6%
. Wong et al. report that 
only 6.8% of non-industry-sponsored vaccine and 8.2% of non-vaccine infectious-disease programs transition from phase 1 to approval
. This mildly supports the critique's skepticism.
- **Repurposing premium applies mostly to safety attrition, not efficacy: LOGIC ONLY.** The critique flags this as UNGROUNDED, which is accurate.
- **The PIIc success estimate of 0.5 and the decomposition: UNVERIFIABLE** (own inference, as stated).
- **The 0.26 break-even and CG's 40%: UNVERIFIABLE.** They come from the model.

**EVIDENCE FOUND**
- Hay et al. 2014 (via a secondary source) put the non-oncology Phase II→III rate at 
34.8%
 and Phase III success at 
54%
. This corroborates the general range.
- Industry transition rates measure drug progression, which includes business-driven terminations. They may understate the scientific probability of success for a well-funded academic or public-health program. They are also not defined identically to CG's p_success, which may start at Phase IIc and end at adoption. The critique doesn't discuss this definitional mismatch.
- The critique's internal cross-references ("Critique 2", "Critique 4") do not match this batch's numbering.

**CORE CLAIM**
- Claim: Industry reference-class rates imply P(II and III succeed) of roughly 15–25%, so CG's 40% needs an unstated premium of about 1.6× or more.
- Support: **SUPPORTED** for the base-rate numbers (BIO's 28.9% and 57.8%). The conclusion that 40% is unjustified is LOGIC ONLY, because the definitional match is untested.
- Why: The BIO rates were directly confirmed, but the infectious-disease uplift could be larger than assumed and CG's endpoint definition is unknown.

**OVERALL VERDICT: PARTIALLY VERIFIED.**

**REVISED CRITIQUE:** CG gives no reference class for 40%. BIO 2011–2020 rates (Phase II→III 28.9%, Phase III→filing 57.8%) imply about 17% for both phases. Infectious-disease-specific data (one analysis: Phase III about 81%) lift this to roughly 25–32%, which is still below 40% and close to the 0.26 break-even. Remove the claim that the infectious-disease-adjusted product is 24–26%. Replace it with a range of about 25–32%, and state that the Wong 2019 figures need checking against the corrected tables. The own-inference decomposition is UNGROUNDED. The repurposing-premium argument is plausible but unsourced. Strength: moderate-to-strong on direction, with the size of the gap uncertain. Magnitude: medium-large.

---

## Critique 3: TB host-directed and adjunctive therapy record is poor

**CITATION CHECK**
- **Wejse et al. 2009 (Guinea-Bissau): VERIFIED.** It is 
Wejse C, et al., Am J Respir Crit Care Med 2009;179:843–50
. A review summarises it as showing 
no difference in TB score, 12-month mortality, or sputum smear conversion times between arms
.
- **Martineau et al. 2011 (London): VERIFIED, with nuance.** The trial found 
median time to culture conversion of 36.0 vs 43.5 days (adjusted HR 1.39, 95% CI 0.90–2.16; p=0.14)
. It also found 
a significant effect in participants with the tt genotype of the TaqI polymorphism
. "No overall benefit" is accurate. The genotype signal is omitted.
- **ACT HIV 2023: VERIFIED.** Deaths were 
116/263 (44.1%) with dexamethasone vs 126/257 (49.0%) with placebo (HR 0.85, 95% CI 0.66–1.10; P=0.22)
. The trial 
did not confer a benefit on survival or any secondary end point
.
- **Thwaites 2004: VERIFIED.** The trial showed 
improved survival in patients over 14 years of age with tuberculous meningitis
. The 
benefit was uncertain in the 98 HIV-positive participants
. That fits the critique's "didn't generalise" framing.
- **REMoxTB, OFLOTUB, RIFAQUIN (all NEJM 2014) failing non-inferiority for 4-month regimens, and Study 31/A5349 succeeding: NOT CHECKED.** My final search was rejected. They match my background knowledge, but they are not verified in this session.
- **Parihar and colleagues, "Karakousis group": PARTIALLY MISATTRIBUTED (from background knowledge, unchecked).** I believe the 2014 Parihar statin–macrophage–mouse paper came from Reto Guler's group in Cape Town. The Karakousis group published separate pravastatin mouse work. The critique conflates the two.
- **Wallis & Hafner; Kolloli & Subbian reviews: NOT CHECKED.**

**CLAIM CHECK**
- **"No HDT is WHO-recommended for drug-sensitive pulmonary TB": PLAUSIBLE, unchecked.**
- **Class success rate of 10–20%: UNVERIFIABLE** (own inference, as stated).
- **At p=0.15, cost-effectiveness is about 38% of CG's base case: VERIFIED arithmetically** (0.15/0.40 = 0.375).

**EVIDENCE FOUND**
- A vitamin D meta-analysis found 
a significantly higher proportion of sputum culture conversion overall (OR 1.22, 1.04–1.43), but no shortening of time to conversion
. This is a mild counterweight to "null."
- The 2025 LAST ACT trial in HIV-negative adults, stratified by LTA4H genotype, found 
neither non-inferiority nor superiority of placebo established in CC/CT-genotype adults
. A combined analysis 
supports dexamethasone's modest survival benefit in all HIV-negative adults
. This reinforces that even the one adopted class member has a modest, heterogeneous effect.
- **Reference-class weakness:**
  - The list is a hand-picked set of failures, so it is vulnerable to selection bias.
  - Several trials were themselves Phase II/III, not Phase II→III transitions.
  - The ACT HIV trial concerned TB meningitis mortality, a very different setting from pulmonary TB with a culture-conversion or relapse endpoint.
  - Most statin evidence is preclinical, so a 10–20% rate from this class has no denominator.

**CORE CLAIM**
- Claim: The appropriate TB-specific reference class has a success rate well under 40% from Phase II onward (about 10–20%).
- Support: **LOGIC ONLY.**
- Why: The individual trial facts check out, but the class rate is an unpublished inference built from a non-systematic, selected list.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The vitamin D, dexamethasone and Thwaites facts are real and accurately characterised. The quantitative class rate stays UNGROUNDED, and the statin attribution is dubious.

**REVISED CRITIQUE:** TB adjunctive and host-directed trials have a mixed record. Vitamin D showed no overall benefit on culture conversion (Wejse 2009, Martineau 2011). Dexamethasone in HIV-associated TB meningitis was null (ACT HIV, HR 0.85, 0.66–1.10). Dexamethasone in HIV-negative TB meningitis showed benefit (Thwaites 2004), though it is modest and heterogeneous. The fluoroquinolone 4-month failures and the Study 31 success are from the critique's memory and need a check. Remove the Parihar/Karakousis attribution until verified. The 10–20% class rate and the blended p_success of 0.2–0.3 are UNGROUNDED inferences. They are plausible, but the reference class is selective and the endpoint context differs from pulmonary TB. Direction: lowers p_success. Magnitude: medium-large. Strength: moderate, as a qualitative prior shift rather than a quantified one.

--- Critique: The TB-specific reference classes (host-directed therapy, adjunctives, regimen-shortening) have a much worse record than 40% ---

## Critique 1: Global-average mortality vs. deployment countries

**CITATION CHECK:** The critique cites no papers. It names the WHO Global TB Report and GBD as suggested evidence only.

**CLAIM CHECK**
- **TB burden is concentrated in India, Indonesia, the Philippines, Nigeria and South Africa: VERIFIED.** The CDC/WHO 2019 summary lists 
India (26%), Indonesia (8.5%), China (8.4%), the Philippines (6.0%), Pakistan (5.7%), Nigeria (4.4%), Bangladesh (3.6%), and South Africa (3.6%)
 as the eight countries with two thirds of global cases.
- **On-treatment mortality differs by country: PLAUSIBLE.** A model-based analysis of Brazil, India and South Africa reports different deviations in deaths during treatment in each country (
13.7% higher than predicted in Brazil, 1.7% in India and 21.8% in South Africa
). That shows heterogeneity in how deaths changed, not baseline levels.
- **India about 4–5% and South Africa about 8–10%: UNVERIFIABLE.** The critique itself flags these as from memory. My searches did not return the WHO country-level cohort tables. An Indian systematic review of treatment-phase case fatality exists (
India accounts for a third of global TB deaths; the review covers cohort studies and trial control arms
). I did not retrieve its pooled estimate.
- **The global 6% figure, the 3.9% threshold and the "Phase III and uptake concentrate in a handful of countries" claim: UNVERIFIABLE.** These are properties of the model or its deployment plan, which I could not check.

**EVIDENCE FOUND**
- WHO reports 
a sustained high treatment success rate for drug-susceptible TB, 88% globally in 2023 and 2022
. The residual 12% (deaths, loss to follow-up, failure) leaves room for substantial country spread.
- One caveat the critique misses: trial-enrolled patients usually have lower on-treatment mortality than programmatic cohorts. The relevant baseline for a Phase III-based effect may be below WHO country figures. That would push the number down in every country.

**CORE CLAIM**
- Claim: Country-weighted on-treatment mortality could differ materially from the single global 6% figure, depending on deployment mix.
- Support: **LOGIC ONLY.**
- Why: Heterogeneity is plausible and directionally supported, but I found no country-specific on-treatment death percentages to size it.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The structural point is sound: a global average is a proxy for a deployment-weighted one. The country mortality numbers remain UNGROUNDED. The critique correctly labels itself a sensitivity issue with uncertain direction.

**REVISED CRITIQUE:** Baseline mortality is a global figure, but TB burden is concentrated in a few countries whose on-treatment mortality probably differs (HIV, age mix, delay to diagnosis). The model should show a case-weighted sensitivity range. Remove the specific India and South Africa percentages until sourced from WHO country cohort tables. Also consider trial-versus-programme mortality differences. Direction: uncertain. Magnitude: medium-low. Strength: moderate-weak.

---

## Critique 2: Industry base rates imply about 15–25%, not 40%

**CITATION CHECK**
- **BIO/Informa/QLS 2021 (2011–2020): VERIFIED.** It is cited in multiple papers as 
"Clinical Development Success Rates and Contributing Factors 2011–2020" (2021)
.
- **Wong, Siah & Lo 2019, *Biostatistics*: VERIFIED (exists).** It is 
Biostatistics 2019 Apr 1;20(2):273-286
.
  - There is a corrigendum. 
The original Tables 1 and 2 had errors in the Phase 2→3 and Phase 3→approval columns.
 The critique's "similar overall figures" from memory may come from the uncorrected numbers, so they need checking against the corrected tables.

**CLAIM CHECK**
- **Phase II→III about 29%: VERIFIED.** BIO's figure is 
28.9%
.
- **Phase III→NDA/BLA about 58%: VERIFIED.** The BIO table gives 
57.8%
 for Phase III.
- **Filing→approval about 91%: UNVERIFIABLE** in my results, though plausible.
- **Arithmetic: VERIFIED.** 0.289 × 0.578 ≈ 16.7%. The 1.6×–2.7× premium and the 37–50% cut from moving 0.40 to 0.20–0.25 are correct.
- **Infectious-disease uplift gives Phase III about 65% and a product of 24–26%: PARTIALLY CONTRADICTED.**
  - One analysis of a different dataset finds infectious diseases have 
the highest unconditional success rate at 14.0%, with a Phase III success rate of 80.9% and application success of 95.6%
.
  - This is a different methodology from BIO and probably uses different phase definitions. Still, it suggests the critique's assumed 65% Phase III rate for infectious disease may be too low.
  - With Phase II at about 37–40% and Phase III at about 80%, the product is roughly 30%, not 24–26%.
  - It would still be below 40%, but near the 0.26 break-even. The critique's central 0.20 looks somewhat pessimistic.
- **Anti-infective overall rates are not dramatically above average: VERIFIED.** Anti-infective Phase I→approval is 
fairly stable around 10.6%
. Wong et al. report that 
only 6.8% of non-industry-sponsored vaccine and 8.2% of non-vaccine infectious-disease programs transition from phase 1 to approval
. This mildly supports the critique's skepticism.
- **Repurposing premium applies mostly to safety attrition, not efficacy: LOGIC ONLY.** The critique flags this as UNGROUNDED, which is accurate.
- **The PIIc success estimate of 0.5 and the decomposition: UNVERIFIABLE** (own inference, as stated).
- **The 0.26 break-even and CG's 40%: UNVERIFIABLE.** They come from the model.

**EVIDENCE FOUND**
- Hay et al. 2014 (via a secondary source) put the non-oncology Phase II→III rate at 
34.8%
 and Phase III success at 
54%
. This corroborates the general range.
- Industry transition rates measure drug progression, which includes business-driven terminations. They may understate the scientific probability of success for a well-funded academic or public-health program. They are also not defined identically to CG's p_success, which may start at Phase IIc and end at adoption. The critique doesn't discuss this definitional mismatch.
- The critique's internal cross-references ("Critique 2", "Critique 4") do not match this batch's numbering.

**CORE CLAIM**
- Claim: Industry reference-class rates imply P(II and III succeed) of roughly 15–25%, so CG's 40% needs an unstated premium of about 1.6× or more.
- Support: **SUPPORTED** for the base-rate numbers (BIO's 28.9% and 57.8%). The conclusion that 40% is unjustified is LOGIC ONLY, because the definitional match is untested.
- Why: The BIO rates were directly confirmed, but the infectious-disease uplift could be larger than assumed and CG's endpoint definition is unknown.

**OVERALL VERDICT: PARTIALLY VERIFIED.**

**REVISED CRITIQUE:** CG gives no reference class for 40%. BIO 2011–2020 rates (Phase II→III 28.9%, Phase III→filing 57.8%) imply about 17% for both phases. Infectious-disease-specific data (one analysis: Phase III about 81%) lift this to roughly 25–32%, which is still below 40% and close to the 0.26 break-even. Remove the claim that the infectious-disease-adjusted product is 24–26%. Replace it with a range of about 25–32%, and state that the Wong 2019 figures need checking against the corrected tables. The own-inference decomposition is UNGROUNDED. The repurposing-premium argument is plausible but unsourced. Strength: moderate-to-strong on direction, with the size of the gap uncertain. Magnitude: medium-large.

---

## Critique 3: TB host-directed and adjunctive therapy record is poor

**CITATION CHECK**
- **Wejse et al. 2009 (Guinea-Bissau): VERIFIED.** It is 
Wejse C, et al., Am J Respir Crit Care Med 2009;179:843–50
. A review summarises it as showing 
no difference in TB score, 12-month mortality, or sputum smear conversion times between arms
.
- **Martineau et al. 2011 (London): VERIFIED, with nuance.** The trial found 
median time to culture conversion of 36.0 vs 43.5 days (adjusted HR 1.39, 95% CI 0.90–2.16; p=0.14)
. It also found 
a significant effect in participants with the tt genotype of the TaqI polymorphism
. "No overall benefit" is accurate. The genotype signal is omitted.
- **ACT HIV 2023: VERIFIED.** Deaths were 
116/263 (44.1%) with dexamethasone vs 126/257 (49.0%) with placebo (HR 0.85, 95% CI 0.66–1.10; P=0.22)
. The trial 
did not confer a benefit on survival or any secondary end point
.
- **Thwaites 2004: VERIFIED.** The trial showed 
improved survival in patients over 14 years of age with tuberculous meningitis
. The 
benefit was uncertain in the 98 HIV-positive participants
. That fits the critique's "didn't generalise" framing.
- **REMoxTB, OFLOTUB, RIFAQUIN (all NEJM 2014) failing non-inferiority for 4-month regimens, and Study 31/A5349 succeeding: NOT CHECKED.** My final search was rejected. They match my background knowledge, but they are not verified in this session.
- **Parihar and colleagues, "Karakousis group": PARTIALLY MISATTRIBUTED (from background knowledge, unchecked).** I believe the 2014 Parihar statin–macrophage–mouse paper came from Reto Guler's group in Cape Town. The Karakousis group published separate pravastatin mouse work. The critique conflates the two.
- **Wallis & Hafner; Kolloli & Subbian reviews: NOT CHECKED.**

**CLAIM CHECK**
- **"No HDT is WHO-recommended for drug-sensitive pulmonary TB": PLAUSIBLE, unchecked.**
- **Class success rate of 10–20%: UNVERIFIABLE** (own inference, as stated).
- **At p=0.15, cost-effectiveness is about 38% of CG's base case: VERIFIED arithmetically** (0.15/0.40 = 0.375).

**EVIDENCE FOUND**
- A vitamin D meta-analysis found 
a significantly higher proportion of sputum culture conversion overall (OR 1.22, 1.04–1.43), but no shortening of time to conversion
. This is a mild counterweight to "null."
- The 2025 LAST ACT trial in HIV-negative adults, stratified by LTA4H genotype, found 
neither non-inferiority nor superiority of placebo established in CC/CT-genotype adults
. A combined analysis 
supports dexamethasone's modest survival benefit in all HIV-negative adults
. This reinforces that even the one adopted class member has a modest, heterogeneous effect.
- **Reference-class weakness:**
  - The list is a hand-picked set of failures, so it is vulnerable to selection bias.
  - Several trials were themselves Phase II/III, not Phase II→III transitions.
  - The ACT HIV trial concerned TB meningitis mortality, a very different setting from pulmonary TB with a culture-conversion or relapse endpoint.
  - Most statin evidence is preclinical, so a 10–20% rate from this class has no denominator.

**CORE CLAIM**
- Claim: The appropriate TB-specific reference class has a success rate well under 40% from Phase II onward (about 10–20%).
- Support: **LOGIC ONLY.**
- Why: The individual trial facts check out, but the class rate is an unpublished inference built from a non-systematic, selected list.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The vitamin D, dexamethasone and Thwaites facts are real and accurately characterised. The quantitative class rate stays UNGROUNDED, and the statin attribution is dubious.

**REVISED CRITIQUE:** TB adjunctive and host-directed trials have a mixed record. Vitamin D showed no overall benefit on culture conversion (Wejse 2009, Martineau 2011). Dexamethasone in HIV-associated TB meningitis was null (ACT HIV, HR 0.85, 0.66–1.10). Dexamethasone in HIV-negative TB meningitis showed benefit (Thwaites 2004), though it is modest and heterogeneous. The fluoroquinolone 4-month failures and the Study 31 success are from the critique's memory and need a check. Remove the Parihar/Karakousis attribution until verified. The 10–20% class rate and the blended p_success of 0.2–0.3 are UNGROUNDED inferences. They are plausible, but the reference class is selective and the endpoint context differs from pulmonary TB. Direction: lowers p_success. Magnitude: medium-large. Strength: moderate, as a qualitative prior shift rather than a quantified one.

--- Critique: "Success" probably means a surrogate or composite endpoint, but the model needs a 10% mortality reduction, so P(adopted AND 10% mortality benefit) < P(trials succeed) ---

## Critique 1: "Success" is probably a surrogate or composite endpoint, but the model needs a 10% mortality reduction

**OVERALL VERDICT: PARTIALLY VERIFIED.** The arithmetic and the claim about standard TB Phase III endpoints check out. The specific baseline mortality and the effect-size discount are ungrounded. The critique also assumes a DS-TB population, which I could not confirm.

**CLAIM CHECK**
- **Power calculation (~36,000 per arm at 4% → 3.6%): VERIFIED (arithmetic).** I recomputed it. The variance term is 0.0384 + 0.0347 = 0.0731. Then 7.84 × 0.0731 / 0.004² ≈ 35,800 per arm.
- **Baseline mortality of ~4% in trial populations: FALSE or overstated for trials, and the error makes the critique stronger.**
  - 
Study 31 on-treatment all-cause mortality was 0.8% (control), 0.4% (rifapentine–moxifloxacin) and 0.5% (rifapentine).

  - 
Overall mortality in Study 31 was 0.6%.

  - 
Among people with HIV it was 1.5%.

  - In TRUNCATE-TB, 
deaths before week 96 were 2 (1.1%) in the control arm and 5 (2.7%) in one experimental arm.

  - At about 1% baseline, my calculation gives roughly 148,000 per arm. The 4–6% figure is closer to programmatic cohorts, which I did not verify.
- **Standard Phase III TB trials use composite endpoints, not mortality: VERIFIED.**
  - Study 31's 
primary efficacy endpoint was TB disease-free survival at 12 months.

  - REMoxTB's 
primary endpoint was a composite unfavorable outcome (failure or relapse within 18 months).

  - TRUNCATE-TB's 
primary outcome was a composite of death before week 96, or ongoing treatment or active TB at week 96.

  - Another source says 
the accepted primary efficacy endpoint is a composite of mainly bacteriological failure and relapse.

- **Enrolment of "hundreds to a few thousand": VERIFIED.** Study 31 randomized about 2,500 and TRUNCATE-TB about 675 across its arms.
- **The surrogate-to-mortality link is uncertain: PLAUSIBLE.** Culture-conversion surrogates are known to be weak. 
Culture conversion has only a limited role in advancing regimens to phase III or predicting outcomes.
 That evidence concerns culture conversion and relapse, not mortality for adjunct drugs.
- **"E[RR | surrogate success] is 5–7%": UNGROUNDED.** It is an illustrative number with no source.

**EVIDENCE FOUND**
- **Counter-consideration.** The critique's DS-TB framing may not match the model. In high-mortality populations such as TB meningitis or advanced HIV, mortality-powered trials are feasible. One review notes 
dexamethasone significantly reduces mortality in tuberculous meningitis and pericarditis.
 If CG targets those populations, the power argument weakens.
- **Possible misreading of the 10%.** The model's 10% may be a population-level or assumed effect, not the trial's powered effect size. I could not see CG's model, so I could not check this.

**CORE CLAIM**
- **Claim:** CG's "Phase III success" is declared on a surrogate or composite endpoint that does not directly test a 10% mortality reduction, so P(success) overstates P(adopted AND ≥10% mortality benefit).
- **Support: LOGIC ONLY.**
- **Why:** The arithmetic and TB endpoint conventions are verified, but I found no evidence on how CG defines success or on the actual mortality-conditional effect.

**REVISED CRITIQUE**
- **Verified:** A mortality-powered Phase III in a typical drug-susceptible TB population needs about 36,000 per arm at 4% baseline mortality. It would need far more at the 0.5–2% mortality seen in Study 31 and TRUNCATE-TB. Standard TB Phase III trials use composite unfavorable-outcome endpoints.
- **Implication:** If CG's population is DS-TB or similarly low-mortality, the 10% mortality effect is an extrapolation, and the model should state it separately from P(trial success).
- **Flagged:** The 5–7% discount is UNGROUNDED. The critique does not apply in high-mortality populations. CG's definition of success needs checking.
- **Strength:** Large if the population is low-mortality, but conditional on that. The direction is correct.

---

## Critique 2: P(adoption | Phase III success) and P(Phase III funded | IIc success) are missing

**OVERALL VERDICT: UNVERIFIABLE (retain as a flagged, UNGROUNDED hypothesis).** The arithmetic is correct. Everything else depends on CG's model structure, which I could not access.

**CLAIM CHECK**
- **0.40 × 0.75–0.85 = 0.30–0.34, a 15–25% reduction: VERIFIED (arithmetic).**
- **Combined with funding at 0.8, the result is "close to the 0.26 threshold": UNVERIFIABLE.** The 0.26 break-even is internal to CG's model. Note that 0.40 × 0.8 × 0.8 ≈ 0.256, which is consistent with the claim.
- **WHO recommendations require a GRADE review and low-certainty evidence may give a conditional or no recommendation: PLAUSIBLE.** This is general institutional knowledge. My searches did not retrieve WHO guideline-methodology documents.
- **The 60% uptake figure covers only country-level implementation, or blends adoption and uptake: UNVERIFIABLE.** I could not find CG's model or grant documents.
- **"$7M includes later trials": UNVERIFIABLE.**
- **"Many Phase II→III failures are strategic or funding exits": UNVERIFIED.** I did not search for it. It is a reasonable industry-data claim but needs a source.
- **"8 years to Phase III completion": UNVERIFIABLE.**

**EVIDENCE FOUND**
- Nothing directly confirms or contradicts the critique. Generic repurposed drugs lack a commercial sponsor, which is plausible. I found no data on adoption or funding probabilities for repurposed TB adjuncts.
- There may be a double-counting issue. If the 40% came from industry base rates for reaching approval, it may already include some funding and strategic attrition. That would cut against this critique, but I could not check it.

**CORE CLAIM**
- **Claim:** The model has no separate factor for WHO adoption or Phase III funding, and the 60% uptake does not already cover them.
- **Support: LOGIC ONLY.**
- **Why:** This depends on how CG derived the 60% and what it includes, which I could not check.

**REVISED CRITIQUE**
- **Hypothesis (UNGROUNDED):** Separate adoption and funding steps may be missing from the p_success chain. If they are absent and each is below 1, cost-effectiveness falls roughly proportionally.
- **Arithmetic:** 0.40 × 0.75–0.85 gives 0.30–0.34, a 15–25% reduction.
- **Action:** The first step is to check how the 60% was derived. If it embeds adoption, this becomes a documentation point only. Medium strength at most, conditional on that check.

---

## Critique 3: Phase IIc "success" is a weak gate

**OVERALL VERDICT: REJECTED as stated.** The key premise, that Phase IIc is chiefly PK or dose-finding, conflicts with how Phase IIc is defined in TB. A conditional version of the hypothesis survives. It depends on how CG defines its IIc, which I could not see.

**CLAIM CHECK**
- **Phase IIc is chiefly dose-finding or PK/safety: CONTRADICTED under standard TB usage.**
  - The Phase IIC STEP design is 
a hybrid in which the experimental regimen is given for its planned Phase III duration, with patients followed for failure and relapse for 12 months from randomisation.

  - The authors say their 
intention was to set a high bar for moving regimens forward, to reduce the risk of costly phase III failures.

  - A review describes 
the hybrid Phase IIC design as permitting earlier identification of candidate regimens likely to succeed in Phase III.

  - An ongoing Phase IIc protocol uses unfavorable outcome status as its efficacy endpoint. It uses 
Stage 1 unfavorable outcome status to inform the decision to proceed to Stage 2.

  - The critique infers "dose-finding" from an exclusion list I cannot see. CG could be using "IIc" loosely, which I could not check.
- **"Phase II culture-conversion signals did not translate in REMoxTB": PARTIALLY VERIFIED.**
  - REMoxTB was itself a Phase III trial. It 
showed a faster initial decline in bacterial burden but was not sufficiently sterilizing to shorten treatment from six to four months.

  - 
Earlier time to culture conversion failed to predict successful 4-month fluoroquinolone regimens and had limited surrogate use in REMoxTB.

  - The analogy supports the point that early-phase surrogates mislead. It concerns Phase IIb culture-conversion endpoints, not Phase IIc dose-finding.
  - "See Critique 2" appears to be a wrong cross-reference. The surrogate point belongs to Critique 1.
- **"Industry Phase II rate ~29%": UNVERIFIED.** I did not search for it. It is plausible from general knowledge.
- **0.7 × 0.3 = 0.21: VERIFIED (arithmetic).** The inputs are illustrative.
- **E[p·RR] ≠ p·E[RR] when both depend on the true effect: VERIFIED (statistical logic).** The critique itself says the direction is ambiguous.

**EVIDENCE FOUND**
- The STEP design was created precisely because Phase II endpoints at 14 days and 8 weeks were over-relied on. That runs against the "weak gate" framing for TB Phase IIc in general.
- Phase IIc in TB can still be underpowered. In STEP's own simulation, 
80 patients per arm with 2.5% unfavourable outcomes gives a probability of 0.99 that Phase III unfavourable outcomes would be below 12%.
 That is a Bayesian prediction, not a guarantee, so some uncertainty remains.

**CORE CLAIM**
- **Claim:** The Phase IIc success criterion is PK or dose selection, so P(IIc) is about 0.6–0.8 and transmits little information about Phase III.
- **Support: CONTRADICTED** under the standard TB definition of Phase IIc, which is an efficacy-based selection trial.
- **Why:** Phase IIc is designed to be a high-bar efficacy gate. Whether CG's IIc matches that design is unchecked.

**REVISED CRITIQUE (conditional, not a finding)**
- **Retain only this conditional hypothesis.** If CG's Phase IIc is defined by PK or dose rather than clinical outcomes, the 40% should be decomposed into P(IIc) × P(III | weak signal) before it is compared with Phase II→approval base rates.
- **Generic point that survives:** Modelling p_success and RR as independent point values is a modelling simplification. It can be tested by a scenario analysis over a prior on the true effect size.
- **Flagged UNGROUNDED:** The 0.6–0.8 IIc pass rate, the 0.21 product, and the direction of the joint-distribution effect.
- **Strength:** Downgrade from medium to low-to-medium, pending the check of CG's IIc definition.

--- Critique: P(adoption | Phase III success) and P(Phase III gets funded and run | Phase IIc success) are missing, and the 60% uptake factor may not cover them ---

## Critique 1: "Success" is probably a surrogate or composite endpoint, but the model needs a 10% mortality reduction

**OVERALL VERDICT: PARTIALLY VERIFIED.** The arithmetic and the claim about standard TB Phase III endpoints check out. The specific baseline mortality and the effect-size discount are ungrounded. The critique also assumes a DS-TB population, which I could not confirm.

**CLAIM CHECK**
- **Power calculation (~36,000 per arm at 4% → 3.6%): VERIFIED (arithmetic).** I recomputed it. The variance term is 0.0384 + 0.0347 = 0.0731. Then 7.84 × 0.0731 / 0.004² ≈ 35,800 per arm.
- **Baseline mortality of ~4% in trial populations: FALSE or overstated for trials, and the error makes the critique stronger.**
  - 
Study 31 on-treatment all-cause mortality was 0.8% (control), 0.4% (rifapentine–moxifloxacin) and 0.5% (rifapentine).

  - 
Overall mortality in Study 31 was 0.6%.

  - 
Among people with HIV it was 1.5%.

  - In TRUNCATE-TB, 
deaths before week 96 were 2 (1.1%) in the control arm and 5 (2.7%) in one experimental arm.

  - At about 1% baseline, my calculation gives roughly 148,000 per arm. The 4–6% figure is closer to programmatic cohorts, which I did not verify.
- **Standard Phase III TB trials use composite endpoints, not mortality: VERIFIED.**
  - Study 31's 
primary efficacy endpoint was TB disease-free survival at 12 months.

  - REMoxTB's 
primary endpoint was a composite unfavorable outcome (failure or relapse within 18 months).

  - TRUNCATE-TB's 
primary outcome was a composite of death before week 96, or ongoing treatment or active TB at week 96.

  - Another source says 
the accepted primary efficacy endpoint is a composite of mainly bacteriological failure and relapse.

- **Enrolment of "hundreds to a few thousand": VERIFIED.** Study 31 randomized about 2,500 and TRUNCATE-TB about 675 across its arms.
- **The surrogate-to-mortality link is uncertain: PLAUSIBLE.** Culture-conversion surrogates are known to be weak. 
Culture conversion has only a limited role in advancing regimens to phase III or predicting outcomes.
 That evidence concerns culture conversion and relapse, not mortality for adjunct drugs.
- **"E[RR | surrogate success] is 5–7%": UNGROUNDED.** It is an illustrative number with no source.

**EVIDENCE FOUND**
- **Counter-consideration.** The critique's DS-TB framing may not match the model. In high-mortality populations such as TB meningitis or advanced HIV, mortality-powered trials are feasible. One review notes 
dexamethasone significantly reduces mortality in tuberculous meningitis and pericarditis.
 If CG targets those populations, the power argument weakens.
- **Possible misreading of the 10%.** The model's 10% may be a population-level or assumed effect, not the trial's powered effect size. I could not see CG's model, so I could not check this.

**CORE CLAIM**
- **Claim:** CG's "Phase III success" is declared on a surrogate or composite endpoint that does not directly test a 10% mortality reduction, so P(success) overstates P(adopted AND ≥10% mortality benefit).
- **Support: LOGIC ONLY.**
- **Why:** The arithmetic and TB endpoint conventions are verified, but I found no evidence on how CG defines success or on the actual mortality-conditional effect.

**REVISED CRITIQUE**
- **Verified:** A mortality-powered Phase III in a typical drug-susceptible TB population needs about 36,000 per arm at 4% baseline mortality. It would need far more at the 0.5–2% mortality seen in Study 31 and TRUNCATE-TB. Standard TB Phase III trials use composite unfavorable-outcome endpoints.
- **Implication:** If CG's population is DS-TB or similarly low-mortality, the 10% mortality effect is an extrapolation, and the model should state it separately from P(trial success).
- **Flagged:** The 5–7% discount is UNGROUNDED. The critique does not apply in high-mortality populations. CG's definition of success needs checking.
- **Strength:** Large if the population is low-mortality, but conditional on that. The direction is correct.

---

## Critique 2: P(adoption | Phase III success) and P(Phase III funded | IIc success) are missing

**OVERALL VERDICT: UNVERIFIABLE (retain as a flagged, UNGROUNDED hypothesis).** The arithmetic is correct. Everything else depends on CG's model structure, which I could not access.

**CLAIM CHECK**
- **0.40 × 0.75–0.85 = 0.30–0.34, a 15–25% reduction: VERIFIED (arithmetic).**
- **Combined with funding at 0.8, the result is "close to the 0.26 threshold": UNVERIFIABLE.** The 0.26 break-even is internal to CG's model. Note that 0.40 × 0.8 × 0.8 ≈ 0.256, which is consistent with the claim.
- **WHO recommendations require a GRADE review and low-certainty evidence may give a conditional or no recommendation: PLAUSIBLE.** This is general institutional knowledge. My searches did not retrieve WHO guideline-methodology documents.
- **The 60% uptake figure covers only country-level implementation, or blends adoption and uptake: UNVERIFIABLE.** I could not find CG's model or grant documents.
- **"$7M includes later trials": UNVERIFIABLE.**
- **"Many Phase II→III failures are strategic or funding exits": UNVERIFIED.** I did not search for it. It is a reasonable industry-data claim but needs a source.
- **"8 years to Phase III completion": UNVERIFIABLE.**

**EVIDENCE FOUND**
- Nothing directly confirms or contradicts the critique. Generic repurposed drugs lack a commercial sponsor, which is plausible. I found no data on adoption or funding probabilities for repurposed TB adjuncts.
- There may be a double-counting issue. If the 40% came from industry base rates for reaching approval, it may already include some funding and strategic attrition. That would cut against this critique, but I could not check it.

**CORE CLAIM**
- **Claim:** The model has no separate factor for WHO adoption or Phase III funding, and the 60% uptake does not already cover them.
- **Support: LOGIC ONLY.**
- **Why:** This depends on how CG derived the 60% and what it includes, which I could not check.

**REVISED CRITIQUE**
- **Hypothesis (UNGROUNDED):** Separate adoption and funding steps may be missing from the p_success chain. If they are absent and each is below 1, cost-effectiveness falls roughly proportionally.
- **Arithmetic:** 0.40 × 0.75–0.85 gives 0.30–0.34, a 15–25% reduction.
- **Action:** The first step is to check how the 60% was derived. If it embeds adoption, this becomes a documentation point only. Medium strength at most, conditional on that check.

---

## Critique 3: Phase IIc "success" is a weak gate

**OVERALL VERDICT: REJECTED as stated.** The key premise, that Phase IIc is chiefly PK or dose-finding, conflicts with how Phase IIc is defined in TB. A conditional version of the hypothesis survives. It depends on how CG defines its IIc, which I could not see.

**CLAIM CHECK**
- **Phase IIc is chiefly dose-finding or PK/safety: CONTRADICTED under standard TB usage.**
  - The Phase IIC STEP design is 
a hybrid in which the experimental regimen is given for its planned Phase III duration, with patients followed for failure and relapse for 12 months from randomisation.

  - The authors say their 
intention was to set a high bar for moving regimens forward, to reduce the risk of costly phase III failures.

  - A review describes 
the hybrid Phase IIC design as permitting earlier identification of candidate regimens likely to succeed in Phase III.

  - An ongoing Phase IIc protocol uses unfavorable outcome status as its efficacy endpoint. It uses 
Stage 1 unfavorable outcome status to inform the decision to proceed to Stage 2.

  - The critique infers "dose-finding" from an exclusion list I cannot see. CG could be using "IIc" loosely, which I could not check.
- **"Phase II culture-conversion signals did not translate in REMoxTB": PARTIALLY VERIFIED.**
  - REMoxTB was itself a Phase III trial. It 
showed a faster initial decline in bacterial burden but was not sufficiently sterilizing to shorten treatment from six to four months.

  - 
Earlier time to culture conversion failed to predict successful 4-month fluoroquinolone regimens and had limited surrogate use in REMoxTB.

  - The analogy supports the point that early-phase surrogates mislead. It concerns Phase IIb culture-conversion endpoints, not Phase IIc dose-finding.
  - "See Critique 2" appears to be a wrong cross-reference. The surrogate point belongs to Critique 1.
- **"Industry Phase II rate ~29%": UNVERIFIED.** I did not search for it. It is plausible from general knowledge.
- **0.7 × 0.3 = 0.21: VERIFIED (arithmetic).** The inputs are illustrative.
- **E[p·RR] ≠ p·E[RR] when both depend on the true effect: VERIFIED (statistical logic).** The critique itself says the direction is ambiguous.

**EVIDENCE FOUND**
- The STEP design was created precisely because Phase II endpoints at 14 days and 8 weeks were over-relied on. That runs against the "weak gate" framing for TB Phase IIc in general.
- Phase IIc in TB can still be underpowered. In STEP's own simulation, 
80 patients per arm with 2.5% unfavourable outcomes gives a probability of 0.99 that Phase III unfavourable outcomes would be below 12%.
 That is a Bayesian prediction, not a guarantee, so some uncertainty remains.

**CORE CLAIM**
- **Claim:** The Phase IIc success criterion is PK or dose selection, so P(IIc) is about 0.6–0.8 and transmits little information about Phase III.
- **Support: CONTRADICTED** under the standard TB definition of Phase IIc, which is an efficacy-based selection trial.
- **Why:** Phase IIc is designed to be a high-bar efficacy gate. Whether CG's IIc matches that design is unchecked.

**REVISED CRITIQUE (conditional, not a finding)**
- **Retain only this conditional hypothesis.** If CG's Phase IIc is defined by PK or dose rather than clinical outcomes, the 40% should be decomposed into P(IIc) × P(III | weak signal) before it is compared with Phase II→approval base rates.
- **Generic point that survives:** Modelling p_success and RR as independent point values is a modelling simplification. It can be tested by a scenario analysis over a prior on the true effect size.
- **Flagged UNGROUNDED:** The 0.6–0.8 IIc pass rate, the 0.21 product, and the direction of the joint-distribution effect.
- **Strength:** Downgrade from medium to low-to-medium, pending the check of CG's IIc definition.

--- Critique: Phase IIc "success" is a weak gate. If it is defined by PK or dose selection, it passes easily and transmits little information, so the probability of the whole chain should be weighted toward Phase III ---

## Critique 1: "Success" is probably a surrogate or composite endpoint, but the model needs a 10% mortality reduction

**OVERALL VERDICT: PARTIALLY VERIFIED.** The arithmetic and the claim about standard TB Phase III endpoints check out. The specific baseline mortality and the effect-size discount are ungrounded. The critique also assumes a DS-TB population, which I could not confirm.

**CLAIM CHECK**
- **Power calculation (~36,000 per arm at 4% → 3.6%): VERIFIED (arithmetic).** I recomputed it. The variance term is 0.0384 + 0.0347 = 0.0731. Then 7.84 × 0.0731 / 0.004² ≈ 35,800 per arm.
- **Baseline mortality of ~4% in trial populations: FALSE or overstated for trials, and the error makes the critique stronger.**
  - 
Study 31 on-treatment all-cause mortality was 0.8% (control), 0.4% (rifapentine–moxifloxacin) and 0.5% (rifapentine).

  - 
Overall mortality in Study 31 was 0.6%.

  - 
Among people with HIV it was 1.5%.

  - In TRUNCATE-TB, 
deaths before week 96 were 2 (1.1%) in the control arm and 5 (2.7%) in one experimental arm.

  - At about 1% baseline, my calculation gives roughly 148,000 per arm. The 4–6% figure is closer to programmatic cohorts, which I did not verify.
- **Standard Phase III TB trials use composite endpoints, not mortality: VERIFIED.**
  - Study 31's 
primary efficacy endpoint was TB disease-free survival at 12 months.

  - REMoxTB's 
primary endpoint was a composite unfavorable outcome (failure or relapse within 18 months).

  - TRUNCATE-TB's 
primary outcome was a composite of death before week 96, or ongoing treatment or active TB at week 96.

  - Another source says 
the accepted primary efficacy endpoint is a composite of mainly bacteriological failure and relapse.

- **Enrolment of "hundreds to a few thousand": VERIFIED.** Study 31 randomized about 2,500 and TRUNCATE-TB about 675 across its arms.
- **The surrogate-to-mortality link is uncertain: PLAUSIBLE.** Culture-conversion surrogates are known to be weak. 
Culture conversion has only a limited role in advancing regimens to phase III or predicting outcomes.
 That evidence concerns culture conversion and relapse, not mortality for adjunct drugs.
- **"E[RR | surrogate success] is 5–7%": UNGROUNDED.** It is an illustrative number with no source.

**EVIDENCE FOUND**
- **Counter-consideration.** The critique's DS-TB framing may not match the model. In high-mortality populations such as TB meningitis or advanced HIV, mortality-powered trials are feasible. One review notes 
dexamethasone significantly reduces mortality in tuberculous meningitis and pericarditis.
 If CG targets those populations, the power argument weakens.
- **Possible misreading of the 10%.** The model's 10% may be a population-level or assumed effect, not the trial's powered effect size. I could not see CG's model, so I could not check this.

**CORE CLAIM**
- **Claim:** CG's "Phase III success" is declared on a surrogate or composite endpoint that does not directly test a 10% mortality reduction, so P(success) overstates P(adopted AND ≥10% mortality benefit).
- **Support: LOGIC ONLY.**
- **Why:** The arithmetic and TB endpoint conventions are verified, but I found no evidence on how CG defines success or on the actual mortality-conditional effect.

**REVISED CRITIQUE**
- **Verified:** A mortality-powered Phase III in a typical drug-susceptible TB population needs about 36,000 per arm at 4% baseline mortality. It would need far more at the 0.5–2% mortality seen in Study 31 and TRUNCATE-TB. Standard TB Phase III trials use composite unfavorable-outcome endpoints.
- **Implication:** If CG's population is DS-TB or similarly low-mortality, the 10% mortality effect is an extrapolation, and the model should state it separately from P(trial success).
- **Flagged:** The 5–7% discount is UNGROUNDED. The critique does not apply in high-mortality populations. CG's definition of success needs checking.
- **Strength:** Large if the population is low-mortality, but conditional on that. The direction is correct.

---

## Critique 2: P(adoption | Phase III success) and P(Phase III funded | IIc success) are missing

**OVERALL VERDICT: UNVERIFIABLE (retain as a flagged, UNGROUNDED hypothesis).** The arithmetic is correct. Everything else depends on CG's model structure, which I could not access.

**CLAIM CHECK**
- **0.40 × 0.75–0.85 = 0.30–0.34, a 15–25% reduction: VERIFIED (arithmetic).**
- **Combined with funding at 0.8, the result is "close to the 0.26 threshold": UNVERIFIABLE.** The 0.26 break-even is internal to CG's model. Note that 0.40 × 0.8 × 0.8 ≈ 0.256, which is consistent with the claim.
- **WHO recommendations require a GRADE review and low-certainty evidence may give a conditional or no recommendation: PLAUSIBLE.** This is general institutional knowledge. My searches did not retrieve WHO guideline-methodology documents.
- **The 60% uptake figure covers only country-level implementation, or blends adoption and uptake: UNVERIFIABLE.** I could not find CG's model or grant documents.
- **"$7M includes later trials": UNVERIFIABLE.**
- **"Many Phase II→III failures are strategic or funding exits": UNVERIFIED.** I did not search for it. It is a reasonable industry-data claim but needs a source.
- **"8 years to Phase III completion": UNVERIFIABLE.**

**EVIDENCE FOUND**
- Nothing directly confirms or contradicts the critique. Generic repurposed drugs lack a commercial sponsor, which is plausible. I found no data on adoption or funding probabilities for repurposed TB adjuncts.
- There may be a double-counting issue. If the 40% came from industry base rates for reaching approval, it may already include some funding and strategic attrition. That would cut against this critique, but I could not check it.

**CORE CLAIM**
- **Claim:** The model has no separate factor for WHO adoption or Phase III funding, and the 60% uptake does not already cover them.
- **Support: LOGIC ONLY.**
- **Why:** This depends on how CG derived the 60% and what it includes, which I could not check.

**REVISED CRITIQUE**
- **Hypothesis (UNGROUNDED):** Separate adoption and funding steps may be missing from the p_success chain. If they are absent and each is below 1, cost-effectiveness falls roughly proportionally.
- **Arithmetic:** 0.40 × 0.75–0.85 gives 0.30–0.34, a 15–25% reduction.
- **Action:** The first step is to check how the 60% was derived. If it embeds adoption, this becomes a documentation point only. Medium strength at most, conditional on that check.

---

## Critique 3: Phase IIc "success" is a weak gate

**OVERALL VERDICT: REJECTED as stated.** The key premise, that Phase IIc is chiefly PK or dose-finding, conflicts with how Phase IIc is defined in TB. A conditional version of the hypothesis survives. It depends on how CG defines its IIc, which I could not see.

**CLAIM CHECK**
- **Phase IIc is chiefly dose-finding or PK/safety: CONTRADICTED under standard TB usage.**
  - The Phase IIC STEP design is 
a hybrid in which the experimental regimen is given for its planned Phase III duration, with patients followed for failure and relapse for 12 months from randomisation.

  - The authors say their 
intention was to set a high bar for moving regimens forward, to reduce the risk of costly phase III failures.

  - A review describes 
the hybrid Phase IIC design as permitting earlier identification of candidate regimens likely to succeed in Phase III.

  - An ongoing Phase IIc protocol uses unfavorable outcome status as its efficacy endpoint. It uses 
Stage 1 unfavorable outcome status to inform the decision to proceed to Stage 2.

  - The critique infers "dose-finding" from an exclusion list I cannot see. CG could be using "IIc" loosely, which I could not check.
- **"Phase II culture-conversion signals did not translate in REMoxTB": PARTIALLY VERIFIED.**
  - REMoxTB was itself a Phase III trial. It 
showed a faster initial decline in bacterial burden but was not sufficiently sterilizing to shorten treatment from six to four months.

  - 
Earlier time to culture conversion failed to predict successful 4-month fluoroquinolone regimens and had limited surrogate use in REMoxTB.

  - The analogy supports the point that early-phase surrogates mislead. It concerns Phase IIb culture-conversion endpoints, not Phase IIc dose-finding.
  - "See Critique 2" appears to be a wrong cross-reference. The surrogate point belongs to Critique 1.
- **"Industry Phase II rate ~29%": UNVERIFIED.** I did not search for it. It is plausible from general knowledge.
- **0.7 × 0.3 = 0.21: VERIFIED (arithmetic).** The inputs are illustrative.
- **E[p·RR] ≠ p·E[RR] when both depend on the true effect: VERIFIED (statistical logic).** The critique itself says the direction is ambiguous.

**EVIDENCE FOUND**
- The STEP design was created precisely because Phase II endpoints at 14 days and 8 weeks were over-relied on. That runs against the "weak gate" framing for TB Phase IIc in general.
- Phase IIc in TB can still be underpowered. In STEP's own simulation, 
80 patients per arm with 2.5% unfavourable outcomes gives a probability of 0.99 that Phase III unfavourable outcomes would be below 12%.
 That is a Bayesian prediction, not a guarantee, so some uncertainty remains.

**CORE CLAIM**
- **Claim:** The Phase IIc success criterion is PK or dose selection, so P(IIc) is about 0.6–0.8 and transmits little information about Phase III.
- **Support: CONTRADICTED** under the standard TB definition of Phase IIc, which is an efficacy-based selection trial.
- **Why:** Phase IIc is designed to be a high-bar efficacy gate. Whether CG's IIc matches that design is unchecked.

**REVISED CRITIQUE (conditional, not a finding)**
- **Retain only this conditional hypothesis.** If CG's Phase IIc is defined by PK or dose rather than clinical outcomes, the 40% should be decomposed into P(IIc) × P(III | weak signal) before it is compared with Phase II→approval base rates.
- **Generic point that survives:** Modelling p_success and RR as independent point values is a modelling simplification. It can be tested by a scenario analysis over a prior on the true effect size.
- **Flagged UNGROUNDED:** The 0.6–0.8 IIc pass rate, the 0.21 product, and the direction of the joint-distribution effect.
- **Strength:** Downgrade from medium to low-to-medium, pending the check of CG's IIc definition.

--- Critique: Baseline year is stale and the 5.5M figure is sensitive to it ---

## Critique 1: Baseline year is stale and the 5.5M figure is sensitive to it

**OVERALL VERDICT: VERIFIED (conditional).** The WHO numbers are right and the arithmetic holds. I could not see CG's model, so whether CG actually anchored on 2022 is unverified. The critique is worded conditionally ("If CG anchored on 2022"), so that is acceptable.

**CLAIM CHECK**
- **2022 notifications ≈ 7.5M:** VERIFIED. 
WHO reported about 8.2 million newly diagnosed in 2023, up from 7.5 million in 2022.

- **2023 ≈ 8.2M:** VERIFIED. 
Globally in 2023, 8.2 million people with a new episode of TB were diagnosed and notified.

- **"Later reports show notifications continuing to rise" (8.3M for 2024):** VERIFIED, but the rise has flattened. 
In 2024, 8.3 million were notified, similar to the 8.2 million in 2023 and 17% above the pre-pandemic 7.1 million in 2019.
 The critique's "~8.2–8.3M" range is therefore accurate.
- **"2022 was a post-COVID recovery year":** VERIFIED. 
WHO says those diagnosed in 2022 and 2023 probably included a sizeable backlog of people whose diagnosis was delayed by COVID.
 The critique does not note that 2023 shares this backlog caveat. 2024 held at 8.3M, though, so the higher level looks persistent.
- **Uplift of 9–11% (5.5M → 6.0–6.1M):** VERIFIED arithmetic. 8.2/7.5 = +9.3% and 8.3/7.5 = +10.7%. The 5.5M figure also reconciles with 7.5M × 0.98⁸ × 0.96 × ~0.90, which suggests the model is built the way the critique assumes.
- **"Below ±25% materiality bar":** correct.
- **"No sensitivity analysis on baseline year":** UNVERIFIABLE. It comes from the thread, not from external evidence.

**EVIDENCE FOUND**
- The 2025 WHO report is already out. It gives 2024 notifications as 8.3M, and 
notifications were 78% of estimated incidence
. A baseline of 2023 or 2024 is therefore clearly available.
- Notifications rose even though incidence was flat to slightly down, which is the detection-gap mechanism behind Critique 2.

**CORE CLAIM**
- Claim: Notified cases are ~8.2–8.3M, not ~7.5M, so a 7.5M baseline understates the starting point by ~9–11%.
- Support: **SUPPORTED**
- Why: Two successive WHO reports give 8.2M (2023) and 8.3M (2024) against 7.5M (2022).

**REVISED CRITIQUE:** Stands as written. Add that the latest figure is 8.3M for 2024. Flag that the CG anchor year is an assumption. Strength: low-to-moderate, upward, non-material alone (+9–11%).

---

## Critique 2: A 2%/yr decline in notified case counts probably contradicts the observed trend

**OVERALL VERDICT: PARTIALLY VERIFIED.** The core observation survives: counts are not falling at 2%/yr. Several details need correction, and the "UNGROUNDED" numbers can now be grounded. Whether CG applies the 2% to counts rather than rates is unverified.

**CLAIM CHECK**
- **WHO headline declines are in incidence rates:** VERIFIED. 
The rate fell 1.7% between 2023 and 2024, and the net reduction from 2015 to 2024 was 12.3%.

- **Rate fell ~8% over 2015–2023:** VERIFIED. 
The net reduction in the incidence rate between 2015 and 2023 was 8.3%.

- **Absolute incident cases roughly flat, ~10–11M:** VERIFIED for 2020–2024. 
The total was 10.8M in 2023, up from 10.7M in 2022, 10.4M in 2021 and 10.1M in 2020.
 
The 2024 figure of 10.7M was a ~1% reduction from 2023.
 I did not verify the "flat since ~2015" claim directly.
- **Population growth offsets rate declines:** VERIFIED. 
Most of the increase in incident cases between 2022 and 2023 reflects population growth.

- **"~1–2%/yr in good pre-COVID years":** PARTLY WRONG, understated. The 2024 report slide says 
the 2015–2020 reduction was 12%
, about 2.5%/yr. This weakens the "2% is clearly too fast" framing only for rates, not for counts.
- **~25% of incident cases not notified:** approximately right but slightly stale. The 2024 figure is 22% (78% notified). The gap was 
2.7M in 2023, down from about 4M in 2020–21 and below the pre-pandemic 3.2M
.
- **Notifications can rise as the detection gap closes:** VERIFIED. Notifications went from 7.1M (2019) to 8.3M (2024) while incident cases were flat.
- **Scenario arithmetic:** correct. 8.2 × 0.96 × 0.90 ≈ 7.1M (+29% vs 5.5M), and +1%/yr gives ≈ 7.7M.
- **2025 funding disruption could cut notifications:** PLAUSIBLE and now partly grounded. 
WHO's provisional data for the first half of 2025 show a mixed picture, with reductions beyond trend in Cambodia, Kenya, Mozambique and Uganda.
 
WHO says impacts could worsen over time.
 Modelling studies project 
excess TB deaths from USAID termination (420,500 by 2035)
. The effect on global notified counts is not established. The critique's "cannot ground the size" is fair.

**EVIDENCE FOUND**
- Modelling of US funding cuts projects 
a 12–41% increase in TB episodes among people living with HIV in South Africa over 2025–2035.
 If cuts persist, true incidence could rise, which pushes the same way as the critique.
- The notification-versus-incidence distinction matters. A drug given at treatment start is exposed to notified/treated counts, which track detection, not the incidence-rate trend.
- The critique's "direction: uncertain" label conflicts with its own conclusion ("probably upward"). Net direction is upward, with downside risk from funding.
- Critique 2's scenario starts from the 8.2M baseline, so it already includes Critique 1. The two should not be added together.

**CORE CLAIM**
- Claim: Notified case counts have not been declining ~2%/yr and are more likely flat or rising over the next 8 years, so applying 2%/yr to counts understates eligible volume.
- Support: **SUPPORTED** for the historical trend (counts flat or rising 2020–2024). The 8-year forward projection is **LOGIC ONLY**.
- Why: WHO data show incident counts flat and notifications up while rates fell only 1.7% in 2024.

**REVISED CRITIQUE**
- Replace "roughly flat since ~2015" with "roughly flat 2020–2024".
- Correct pre-COVID rate declines to ~2.5%/yr, and the gap to ~22%.
- The conclusion is upward, not "uncertain": eligible ≈ 6.5–7.7M under flat-to-mild-growth scenarios, with a flagged downside from funding cuts.
- Flag that CG's use of 2% on counts is unverified.
- Strength: moderate-to-high, **upward**. It is likely material (>25%) when combined with the baseline correction, which is already inside its own scenario.

---

## Critique 3: "Adult DS notified" is not "eligible for the trial label"

**OVERALL VERDICT: PARTIALLY VERIFIED.** The epidemiological shares are essentially correct and the arithmetic holds. The hypothesis that applicability filters are missing is logically sound but depends on trial design and on CG's actual model, neither of which I could see. The statin-specific exclusions are the investigator's own inference, as the investigator admits.

**CLAIM CHECK**
- **Extrapulmonary ≈ 15%:** VERIFIED, slightly low. 
In 2024, 8.3 million were notified: 84% pulmonary and 16% extrapulmonary.
 Regional variation is large. 
Extrapulmonary share is 25% in South-East Asia and 8% in the Western Pacific.
 
It exceeds 20% in India, Bangladesh and Ethiopia.
 India is the largest contributor, so the real filter loss is likely larger than 15%.
- **Clinically diagnosed ~35–40% of notifications:** MOSTLY CORRECT, but mislabelled. 
64% of the 6.9M pulmonary cases were bacteriologically confirmed in 2024, up from 62% in 2023.
 That is a share of pulmonary cases, so it is ~36% clinically diagnosed among pulmonary cases. The critique's own stack applies ×0.62 after the pulmonary filter, which is correct sequencing. Confirmed pulmonary cases are ~54% of all notifications (0.84 × 0.64).
- **HIV coinfection ~6–8%:** ROUGHLY CORRECT. 
413,516 notified TB cases were in people with HIV in 2024, equal to 6.2% of the 6.7M with an HIV test result.
 That is about 5% of all notifications. 
In 2023 the figure was 6.8%.
 The range is fine for tested cases but slightly high for all notifications.
- **Hr-TB ~7%:** VERIFIED. 
Data reported to WHO from 156 countries (2002–2018) gave 7.4% of new patients and 11.4% of previously treated patients.
 Other sources say 
about 8% (range 5–11%)
. The treatment difference is verified. 
WHO recommended a distinct 6-month regimen for Hr-TB containing rifampicin, pyrazinamide, ethambutol and levofloxacin.
 The claim that Hr-TB is classified as "DS" in some schemas is UNVERIFIABLE. It depends on CG's schema, and Hr-TB patients are usually not detected without isoniazid testing.
- **Stack arithmetic:** correct. 5.5 × 0.85 = 4.7M; × 0.85 = 4.0M; × 0.62 = 2.5M.
- **Statin exclusion list (pregnancy, hepatic disease, ART interaction, existing statin use):** UNVERIFIABLE as a trial design. This is the investigator's inference, which the investigator discloses. It is plausible. Rifampicin–statin interactions are real, and I did not check them against a protocol.
- **Pregnancy filter:** The size is not grounded in any search result.

**EVIDENCE FOUND**
- WHO data confirm that the extrapulmonary share and the confirmation share vary a lot by region, so a global average could misstate a model weighted toward India, Nigeria and Indonesia.
- The bacteriological-confirmation filter is design-dependent and probably the weakest link. A label or real-world adoption model would apply to all treated pulmonary DS-TB, not only culture-confirmed cases. WHO notes that 
a proportion of clinically diagnosed cases may be incorrect diagnoses of TB
, which supports some downward adjustment but not a full ×0.62.
- The critique's "could push eligible below the 3.6M bar" only occurs with the full confirmation filter. Without it, ~4.0M stays above the bar.
- The filters partly overlap. HIV-positive and extrapulmonary cases are correlated, so multiplying them overstates the combined loss.

**CORE CLAIM**
- Claim: CG's 5.5M includes cases outside the likely trial or label population (extrapulmonary, HIV, pregnancy, hepatic disease, Hr-TB, clinically diagnosed), and these should be modelled explicitly.
- Support: **LOGIC ONLY**
- Why: The WHO shares are verified, but whether CG's 5.5M already excludes them, and which filters a trial or label would apply, are not visible or verifiable.

**REVISED CRITIQUE**
- Keep the verified shares: extrapulmonary 16% (up to 25% in SE Asia), pulmonary bacteriological confirmation 64%, HIV ~5–6%, Hr-TB ~7–8%.
- Flag the statin-specific exclusions and the pregnancy and hepatic filters as **UNGROUNDED — plausible but needs a trial protocol**.
- Treat the bacteriological-confirmation filter as scenario-dependent rather than a base-case reduction.
- Account for filter overlap.
- Realistic range: ~3.5–4.7M before any confirmation restriction; ~2.5M only under a culture-confirmed-only design.
- Direction: **downward** if filters are not already in the model. The "uncertain" label arises only from Critique 2 offsetting it.
- Strength: moderate. It is conditional on CG's model structure and on trial design.

--- Critique: A 2%/yr decline in notified case counts probably contradicts the observed trend; incidence rates fall slowly while counts do not ---

## Critique 1: Baseline year is stale and the 5.5M figure is sensitive to it

**OVERALL VERDICT: VERIFIED (conditional).** The WHO numbers are right and the arithmetic holds. I could not see CG's model, so whether CG actually anchored on 2022 is unverified. The critique is worded conditionally ("If CG anchored on 2022"), so that is acceptable.

**CLAIM CHECK**
- **2022 notifications ≈ 7.5M:** VERIFIED. 
WHO reported about 8.2 million newly diagnosed in 2023, up from 7.5 million in 2022.

- **2023 ≈ 8.2M:** VERIFIED. 
Globally in 2023, 8.2 million people with a new episode of TB were diagnosed and notified.

- **"Later reports show notifications continuing to rise" (8.3M for 2024):** VERIFIED, but the rise has flattened. 
In 2024, 8.3 million were notified, similar to the 8.2 million in 2023 and 17% above the pre-pandemic 7.1 million in 2019.
 The critique's "~8.2–8.3M" range is therefore accurate.
- **"2022 was a post-COVID recovery year":** VERIFIED. 
WHO says those diagnosed in 2022 and 2023 probably included a sizeable backlog of people whose diagnosis was delayed by COVID.
 The critique does not note that 2023 shares this backlog caveat. 2024 held at 8.3M, though, so the higher level looks persistent.
- **Uplift of 9–11% (5.5M → 6.0–6.1M):** VERIFIED arithmetic. 8.2/7.5 = +9.3% and 8.3/7.5 = +10.7%. The 5.5M figure also reconciles with 7.5M × 0.98⁸ × 0.96 × ~0.90, which suggests the model is built the way the critique assumes.
- **"Below ±25% materiality bar":** correct.
- **"No sensitivity analysis on baseline year":** UNVERIFIABLE. It comes from the thread, not from external evidence.

**EVIDENCE FOUND**
- The 2025 WHO report is already out. It gives 2024 notifications as 8.3M, and 
notifications were 78% of estimated incidence
. A baseline of 2023 or 2024 is therefore clearly available.
- Notifications rose even though incidence was flat to slightly down, which is the detection-gap mechanism behind Critique 2.

**CORE CLAIM**
- Claim: Notified cases are ~8.2–8.3M, not ~7.5M, so a 7.5M baseline understates the starting point by ~9–11%.
- Support: **SUPPORTED**
- Why: Two successive WHO reports give 8.2M (2023) and 8.3M (2024) against 7.5M (2022).

**REVISED CRITIQUE:** Stands as written. Add that the latest figure is 8.3M for 2024. Flag that the CG anchor year is an assumption. Strength: low-to-moderate, upward, non-material alone (+9–11%).

---

## Critique 2: A 2%/yr decline in notified case counts probably contradicts the observed trend

**OVERALL VERDICT: PARTIALLY VERIFIED.** The core observation survives: counts are not falling at 2%/yr. Several details need correction, and the "UNGROUNDED" numbers can now be grounded. Whether CG applies the 2% to counts rather than rates is unverified.

**CLAIM CHECK**
- **WHO headline declines are in incidence rates:** VERIFIED. 
The rate fell 1.7% between 2023 and 2024, and the net reduction from 2015 to 2024 was 12.3%.

- **Rate fell ~8% over 2015–2023:** VERIFIED. 
The net reduction in the incidence rate between 2015 and 2023 was 8.3%.

- **Absolute incident cases roughly flat, ~10–11M:** VERIFIED for 2020–2024. 
The total was 10.8M in 2023, up from 10.7M in 2022, 10.4M in 2021 and 10.1M in 2020.
 
The 2024 figure of 10.7M was a ~1% reduction from 2023.
 I did not verify the "flat since ~2015" claim directly.
- **Population growth offsets rate declines:** VERIFIED. 
Most of the increase in incident cases between 2022 and 2023 reflects population growth.

- **"~1–2%/yr in good pre-COVID years":** PARTLY WRONG, understated. The 2024 report slide says 
the 2015–2020 reduction was 12%
, about 2.5%/yr. This weakens the "2% is clearly too fast" framing only for rates, not for counts.
- **~25% of incident cases not notified:** approximately right but slightly stale. The 2024 figure is 22% (78% notified). The gap was 
2.7M in 2023, down from about 4M in 2020–21 and below the pre-pandemic 3.2M
.
- **Notifications can rise as the detection gap closes:** VERIFIED. Notifications went from 7.1M (2019) to 8.3M (2024) while incident cases were flat.
- **Scenario arithmetic:** correct. 8.2 × 0.96 × 0.90 ≈ 7.1M (+29% vs 5.5M), and +1%/yr gives ≈ 7.7M.
- **2025 funding disruption could cut notifications:** PLAUSIBLE and now partly grounded. 
WHO's provisional data for the first half of 2025 show a mixed picture, with reductions beyond trend in Cambodia, Kenya, Mozambique and Uganda.
 
WHO says impacts could worsen over time.
 Modelling studies project 
excess TB deaths from USAID termination (420,500 by 2035)
. The effect on global notified counts is not established. The critique's "cannot ground the size" is fair.

**EVIDENCE FOUND**
- Modelling of US funding cuts projects 
a 12–41% increase in TB episodes among people living with HIV in South Africa over 2025–2035.
 If cuts persist, true incidence could rise, which pushes the same way as the critique.
- The notification-versus-incidence distinction matters. A drug given at treatment start is exposed to notified/treated counts, which track detection, not the incidence-rate trend.
- The critique's "direction: uncertain" label conflicts with its own conclusion ("probably upward"). Net direction is upward, with downside risk from funding.
- Critique 2's scenario starts from the 8.2M baseline, so it already includes Critique 1. The two should not be added together.

**CORE CLAIM**
- Claim: Notified case counts have not been declining ~2%/yr and are more likely flat or rising over the next 8 years, so applying 2%/yr to counts understates eligible volume.
- Support: **SUPPORTED** for the historical trend (counts flat or rising 2020–2024). The 8-year forward projection is **LOGIC ONLY**.
- Why: WHO data show incident counts flat and notifications up while rates fell only 1.7% in 2024.

**REVISED CRITIQUE**
- Replace "roughly flat since ~2015" with "roughly flat 2020–2024".
- Correct pre-COVID rate declines to ~2.5%/yr, and the gap to ~22%.
- The conclusion is upward, not "uncertain": eligible ≈ 6.5–7.7M under flat-to-mild-growth scenarios, with a flagged downside from funding cuts.
- Flag that CG's use of 2% on counts is unverified.
- Strength: moderate-to-high, **upward**. It is likely material (>25%) when combined with the baseline correction, which is already inside its own scenario.

---

## Critique 3: "Adult DS notified" is not "eligible for the trial label"

**OVERALL VERDICT: PARTIALLY VERIFIED.** The epidemiological shares are essentially correct and the arithmetic holds. The hypothesis that applicability filters are missing is logically sound but depends on trial design and on CG's actual model, neither of which I could see. The statin-specific exclusions are the investigator's own inference, as the investigator admits.

**CLAIM CHECK**
- **Extrapulmonary ≈ 15%:** VERIFIED, slightly low. 
In 2024, 8.3 million were notified: 84% pulmonary and 16% extrapulmonary.
 Regional variation is large. 
Extrapulmonary share is 25% in South-East Asia and 8% in the Western Pacific.
 
It exceeds 20% in India, Bangladesh and Ethiopia.
 India is the largest contributor, so the real filter loss is likely larger than 15%.
- **Clinically diagnosed ~35–40% of notifications:** MOSTLY CORRECT, but mislabelled. 
64% of the 6.9M pulmonary cases were bacteriologically confirmed in 2024, up from 62% in 2023.
 That is a share of pulmonary cases, so it is ~36% clinically diagnosed among pulmonary cases. The critique's own stack applies ×0.62 after the pulmonary filter, which is correct sequencing. Confirmed pulmonary cases are ~54% of all notifications (0.84 × 0.64).
- **HIV coinfection ~6–8%:** ROUGHLY CORRECT. 
413,516 notified TB cases were in people with HIV in 2024, equal to 6.2% of the 6.7M with an HIV test result.
 That is about 5% of all notifications. 
In 2023 the figure was 6.8%.
 The range is fine for tested cases but slightly high for all notifications.
- **Hr-TB ~7%:** VERIFIED. 
Data reported to WHO from 156 countries (2002–2018) gave 7.4% of new patients and 11.4% of previously treated patients.
 Other sources say 
about 8% (range 5–11%)
. The treatment difference is verified. 
WHO recommended a distinct 6-month regimen for Hr-TB containing rifampicin, pyrazinamide, ethambutol and levofloxacin.
 The claim that Hr-TB is classified as "DS" in some schemas is UNVERIFIABLE. It depends on CG's schema, and Hr-TB patients are usually not detected without isoniazid testing.
- **Stack arithmetic:** correct. 5.5 × 0.85 = 4.7M; × 0.85 = 4.0M; × 0.62 = 2.5M.
- **Statin exclusion list (pregnancy, hepatic disease, ART interaction, existing statin use):** UNVERIFIABLE as a trial design. This is the investigator's inference, which the investigator discloses. It is plausible. Rifampicin–statin interactions are real, and I did not check them against a protocol.
- **Pregnancy filter:** The size is not grounded in any search result.

**EVIDENCE FOUND**
- WHO data confirm that the extrapulmonary share and the confirmation share vary a lot by region, so a global average could misstate a model weighted toward India, Nigeria and Indonesia.
- The bacteriological-confirmation filter is design-dependent and probably the weakest link. A label or real-world adoption model would apply to all treated pulmonary DS-TB, not only culture-confirmed cases. WHO notes that 
a proportion of clinically diagnosed cases may be incorrect diagnoses of TB
, which supports some downward adjustment but not a full ×0.62.
- The critique's "could push eligible below the 3.6M bar" only occurs with the full confirmation filter. Without it, ~4.0M stays above the bar.
- The filters partly overlap. HIV-positive and extrapulmonary cases are correlated, so multiplying them overstates the combined loss.

**CORE CLAIM**
- Claim: CG's 5.5M includes cases outside the likely trial or label population (extrapulmonary, HIV, pregnancy, hepatic disease, Hr-TB, clinically diagnosed), and these should be modelled explicitly.
- Support: **LOGIC ONLY**
- Why: The WHO shares are verified, but whether CG's 5.5M already excludes them, and which filters a trial or label would apply, are not visible or verifiable.

**REVISED CRITIQUE**
- Keep the verified shares: extrapulmonary 16% (up to 25% in SE Asia), pulmonary bacteriological confirmation 64%, HIV ~5–6%, Hr-TB ~7–8%.
- Flag the statin-specific exclusions and the pregnancy and hepatic filters as **UNGROUNDED — plausible but needs a trial protocol**.
- Treat the bacteriological-confirmation filter as scenario-dependent rather than a base-case reduction.
- Account for filter overlap.
- Realistic range: ~3.5–4.7M before any confirmation restriction; ~2.5M only under a culture-confirmed-only design.
- Direction: **downward** if filters are not already in the model. The "uncertain" label arises only from Critique 2 offsetting it.
- Strength: moderate. It is conditional on CG's model structure and on trial design.

--- Critique: "Adult DS notified" is not "eligible for the trial label": missing applicability filters ---

## Critique 1: Baseline year is stale and the 5.5M figure is sensitive to it

**OVERALL VERDICT: VERIFIED (conditional).** The WHO numbers are right and the arithmetic holds. I could not see CG's model, so whether CG actually anchored on 2022 is unverified. The critique is worded conditionally ("If CG anchored on 2022"), so that is acceptable.

**CLAIM CHECK**
- **2022 notifications ≈ 7.5M:** VERIFIED. 
WHO reported about 8.2 million newly diagnosed in 2023, up from 7.5 million in 2022.

- **2023 ≈ 8.2M:** VERIFIED. 
Globally in 2023, 8.2 million people with a new episode of TB were diagnosed and notified.

- **"Later reports show notifications continuing to rise" (8.3M for 2024):** VERIFIED, but the rise has flattened. 
In 2024, 8.3 million were notified, similar to the 8.2 million in 2023 and 17% above the pre-pandemic 7.1 million in 2019.
 The critique's "~8.2–8.3M" range is therefore accurate.
- **"2022 was a post-COVID recovery year":** VERIFIED. 
WHO says those diagnosed in 2022 and 2023 probably included a sizeable backlog of people whose diagnosis was delayed by COVID.
 The critique does not note that 2023 shares this backlog caveat. 2024 held at 8.3M, though, so the higher level looks persistent.
- **Uplift of 9–11% (5.5M → 6.0–6.1M):** VERIFIED arithmetic. 8.2/7.5 = +9.3% and 8.3/7.5 = +10.7%. The 5.5M figure also reconciles with 7.5M × 0.98⁸ × 0.96 × ~0.90, which suggests the model is built the way the critique assumes.
- **"Below ±25% materiality bar":** correct.
- **"No sensitivity analysis on baseline year":** UNVERIFIABLE. It comes from the thread, not from external evidence.

**EVIDENCE FOUND**
- The 2025 WHO report is already out. It gives 2024 notifications as 8.3M, and 
notifications were 78% of estimated incidence
. A baseline of 2023 or 2024 is therefore clearly available.
- Notifications rose even though incidence was flat to slightly down, which is the detection-gap mechanism behind Critique 2.

**CORE CLAIM**
- Claim: Notified cases are ~8.2–8.3M, not ~7.5M, so a 7.5M baseline understates the starting point by ~9–11%.
- Support: **SUPPORTED**
- Why: Two successive WHO reports give 8.2M (2023) and 8.3M (2024) against 7.5M (2022).

**REVISED CRITIQUE:** Stands as written. Add that the latest figure is 8.3M for 2024. Flag that the CG anchor year is an assumption. Strength: low-to-moderate, upward, non-material alone (+9–11%).

---

## Critique 2: A 2%/yr decline in notified case counts probably contradicts the observed trend

**OVERALL VERDICT: PARTIALLY VERIFIED.** The core observation survives: counts are not falling at 2%/yr. Several details need correction, and the "UNGROUNDED" numbers can now be grounded. Whether CG applies the 2% to counts rather than rates is unverified.

**CLAIM CHECK**
- **WHO headline declines are in incidence rates:** VERIFIED. 
The rate fell 1.7% between 2023 and 2024, and the net reduction from 2015 to 2024 was 12.3%.

- **Rate fell ~8% over 2015–2023:** VERIFIED. 
The net reduction in the incidence rate between 2015 and 2023 was 8.3%.

- **Absolute incident cases roughly flat, ~10–11M:** VERIFIED for 2020–2024. 
The total was 10.8M in 2023, up from 10.7M in 2022, 10.4M in 2021 and 10.1M in 2020.
 
The 2024 figure of 10.7M was a ~1% reduction from 2023.
 I did not verify the "flat since ~2015" claim directly.
- **Population growth offsets rate declines:** VERIFIED. 
Most of the increase in incident cases between 2022 and 2023 reflects population growth.

- **"~1–2%/yr in good pre-COVID years":** PARTLY WRONG, understated. The 2024 report slide says 
the 2015–2020 reduction was 12%
, about 2.5%/yr. This weakens the "2% is clearly too fast" framing only for rates, not for counts.
- **~25% of incident cases not notified:** approximately right but slightly stale. The 2024 figure is 22% (78% notified). The gap was 
2.7M in 2023, down from about 4M in 2020–21 and below the pre-pandemic 3.2M
.
- **Notifications can rise as the detection gap closes:** VERIFIED. Notifications went from 7.1M (2019) to 8.3M (2024) while incident cases were flat.
- **Scenario arithmetic:** correct. 8.2 × 0.96 × 0.90 ≈ 7.1M (+29% vs 5.5M), and +1%/yr gives ≈ 7.7M.
- **2025 funding disruption could cut notifications:** PLAUSIBLE and now partly grounded. 
WHO's provisional data for the first half of 2025 show a mixed picture, with reductions beyond trend in Cambodia, Kenya, Mozambique and Uganda.
 
WHO says impacts could worsen over time.
 Modelling studies project 
excess TB deaths from USAID termination (420,500 by 2035)
. The effect on global notified counts is not established. The critique's "cannot ground the size" is fair.

**EVIDENCE FOUND**
- Modelling of US funding cuts projects 
a 12–41% increase in TB episodes among people living with HIV in South Africa over 2025–2035.
 If cuts persist, true incidence could rise, which pushes the same way as the critique.
- The notification-versus-incidence distinction matters. A drug given at treatment start is exposed to notified/treated counts, which track detection, not the incidence-rate trend.
- The critique's "direction: uncertain" label conflicts with its own conclusion ("probably upward"). Net direction is upward, with downside risk from funding.
- Critique 2's scenario starts from the 8.2M baseline, so it already includes Critique 1. The two should not be added together.

**CORE CLAIM**
- Claim: Notified case counts have not been declining ~2%/yr and are more likely flat or rising over the next 8 years, so applying 2%/yr to counts understates eligible volume.
- Support: **SUPPORTED** for the historical trend (counts flat or rising 2020–2024). The 8-year forward projection is **LOGIC ONLY**.
- Why: WHO data show incident counts flat and notifications up while rates fell only 1.7% in 2024.

**REVISED CRITIQUE**
- Replace "roughly flat since ~2015" with "roughly flat 2020–2024".
- Correct pre-COVID rate declines to ~2.5%/yr, and the gap to ~22%.
- The conclusion is upward, not "uncertain": eligible ≈ 6.5–7.7M under flat-to-mild-growth scenarios, with a flagged downside from funding cuts.
- Flag that CG's use of 2% on counts is unverified.
- Strength: moderate-to-high, **upward**. It is likely material (>25%) when combined with the baseline correction, which is already inside its own scenario.

---

## Critique 3: "Adult DS notified" is not "eligible for the trial label"

**OVERALL VERDICT: PARTIALLY VERIFIED.** The epidemiological shares are essentially correct and the arithmetic holds. The hypothesis that applicability filters are missing is logically sound but depends on trial design and on CG's actual model, neither of which I could see. The statin-specific exclusions are the investigator's own inference, as the investigator admits.

**CLAIM CHECK**
- **Extrapulmonary ≈ 15%:** VERIFIED, slightly low. 
In 2024, 8.3 million were notified: 84% pulmonary and 16% extrapulmonary.
 Regional variation is large. 
Extrapulmonary share is 25% in South-East Asia and 8% in the Western Pacific.
 
It exceeds 20% in India, Bangladesh and Ethiopia.
 India is the largest contributor, so the real filter loss is likely larger than 15%.
- **Clinically diagnosed ~35–40% of notifications:** MOSTLY CORRECT, but mislabelled. 
64% of the 6.9M pulmonary cases were bacteriologically confirmed in 2024, up from 62% in 2023.
 That is a share of pulmonary cases, so it is ~36% clinically diagnosed among pulmonary cases. The critique's own stack applies ×0.62 after the pulmonary filter, which is correct sequencing. Confirmed pulmonary cases are ~54% of all notifications (0.84 × 0.64).
- **HIV coinfection ~6–8%:** ROUGHLY CORRECT. 
413,516 notified TB cases were in people with HIV in 2024, equal to 6.2% of the 6.7M with an HIV test result.
 That is about 5% of all notifications. 
In 2023 the figure was 6.8%.
 The range is fine for tested cases but slightly high for all notifications.
- **Hr-TB ~7%:** VERIFIED. 
Data reported to WHO from 156 countries (2002–2018) gave 7.4% of new patients and 11.4% of previously treated patients.
 Other sources say 
about 8% (range 5–11%)
. The treatment difference is verified. 
WHO recommended a distinct 6-month regimen for Hr-TB containing rifampicin, pyrazinamide, ethambutol and levofloxacin.
 The claim that Hr-TB is classified as "DS" in some schemas is UNVERIFIABLE. It depends on CG's schema, and Hr-TB patients are usually not detected without isoniazid testing.
- **Stack arithmetic:** correct. 5.5 × 0.85 = 4.7M; × 0.85 = 4.0M; × 0.62 = 2.5M.
- **Statin exclusion list (pregnancy, hepatic disease, ART interaction, existing statin use):** UNVERIFIABLE as a trial design. This is the investigator's inference, which the investigator discloses. It is plausible. Rifampicin–statin interactions are real, and I did not check them against a protocol.
- **Pregnancy filter:** The size is not grounded in any search result.

**EVIDENCE FOUND**
- WHO data confirm that the extrapulmonary share and the confirmation share vary a lot by region, so a global average could misstate a model weighted toward India, Nigeria and Indonesia.
- The bacteriological-confirmation filter is design-dependent and probably the weakest link. A label or real-world adoption model would apply to all treated pulmonary DS-TB, not only culture-confirmed cases. WHO notes that 
a proportion of clinically diagnosed cases may be incorrect diagnoses of TB
, which supports some downward adjustment but not a full ×0.62.
- The critique's "could push eligible below the 3.6M bar" only occurs with the full confirmation filter. Without it, ~4.0M stays above the bar.
- The filters partly overlap. HIV-positive and extrapulmonary cases are correlated, so multiplying them overstates the combined loss.

**CORE CLAIM**
- Claim: CG's 5.5M includes cases outside the likely trial or label population (extrapulmonary, HIV, pregnancy, hepatic disease, Hr-TB, clinically diagnosed), and these should be modelled explicitly.
- Support: **LOGIC ONLY**
- Why: The WHO shares are verified, but whether CG's 5.5M already excludes them, and which filters a trial or label would apply, are not visible or verifiable.

**REVISED CRITIQUE**
- Keep the verified shares: extrapulmonary 16% (up to 25% in SE Asia), pulmonary bacteriological confirmation 64%, HIV ~5–6%, Hr-TB ~7–8%.
- Flag the statin-specific exclusions and the pregnancy and hepatic filters as **UNGROUNDED — plausible but needs a trial protocol**.
- Treat the bacteriological-confirmation filter as scenario-dependent rather than a base-case reduction.
- Account for filter overlap.
- Realistic range: ~3.5–4.7M before any confirmation restriction; ~2.5M only under a culture-confirmed-only design.
- Direction: **downward** if filters are not already in the model. The "uncertain" label arises only from Critique 2 offsetting it.
- Strength: moderate. It is conditional on CG's model structure and on trial design.

--- Critique: Shorter and new regimens erode both the eligible population and the incremental benefit ---

## Critique 1: Shorter and new regimens erode both the eligible population and the incremental benefit

**CITATION CHECK**
- WHO 2022, 4-month HPMZ for age ≥12: **VERIFIED**. 
WHO's 2022 Module 4 conditionally recommends the 4-month isoniazid–rifapentine–moxifloxacin–pyrazinamide regimen for people aged 12 or older with drug-susceptible pulmonary TB (moderate certainty).

- Dorman et al., NEJM 2021 (Study 31/A5349): **VERIFIED in substance, but not directly retrieved.** 
TBTC Study 31/ACTG A5349 is a phase 3 trial that found the 4-month rifapentine-moxifloxacin regimen safe and effective.
 I did not pull the NEJM 2021 record itself. The authorship and year match my own knowledge.
- Paton et al., NEJM 2023 (TRUNCATE-TB): **VERIFIED.** 
It was published in N Engl J Med 2023;388:873-887.
 The Investigator's "from my recollection" hedge is unnecessary.
- "Bedaquiline-containing short regimens": **PARTIALLY VERIFIED, with a correction.** 
TRUNCATE-TB found that a strategy starting with an 8-week regimen of bedaquiline and linezolid was noninferior to standard treatment at week 96.
 This is a trial strategy that includes retreatment, not a WHO-recommended DS-TB regimen. The Investigator should not group it with HPMZ as an "adopted" regimen.

**CLAIM CHECK**
- WHO recommended the 4-month HPMZ regimen in 2022 for age ≥12: **VERIFIED** (see above).
- A statin trial on HRZE does not establish efficacy on a rifapentine/moxifloxacin backbone: **PLAUSIBLE.** This is sound reasoning, and I found no direct evidence either way.
- "Rifapentine is a stronger CYP3A4 inducer than rifampicin": **UNVERIFIABLE and probably overstated.** I ran out of searches before checking it. From general pharmacology, rifampicin is usually described as the most potent inducer, and rifapentine is comparable or somewhat weaker depending on dose. Both are inducers, so the broader worry about interactions with atorvastatin survives. The comparative "stronger" claim should be dropped or checked.
- "Programme uptake of HPMZ has been slow because of rifapentine supply and cost": **UNVERIFIABLE.** I found no direct source. One adjacent source says 
use of the regimen in clinical practice may be limited by the high rifapentine dose, particularly in patients with comorbidities.
 This partly supports the idea that uptake is constrained, though for a different reason than the Investigator gives.
- 20–40% of eligible patients on non-trial regimens by ~2033: **UNGROUNDED.** The Investigator says so too. I found no projection.
- Shorter regimens reduce room for an adjunct to add benefit: **PLAUSIBLE.** This is logic only.

**EVIDENCE FOUND**
- HPMZ is restricted to age ≥12, and it is conditional. Rifapentine exposure has been shown to drive outcomes: 
low rifapentine exposure is the strongest driver of TB-related unfavorable outcomes in the rifapentine-moxifloxacin arm.
 That limits how fast HPMZ can displace HRZE, because dosing and supply constraints apply. It weakly favours the low end of the Investigator's range.
- Under the WHO guidance, 
adolescents aged 12–16 have three options: 4-month HPMZ, 4-month 2HRZ(E)/2HR, or standard 6-month 2HRZ(E)/4HR.
 The 4-month HRZ(E) regimen for children with non-severe TB still contains rifampicin. The rifamycin-induction problem would therefore remain on that backbone, which weakens the "non-trial backbone" argument for that group.
- Most 2022 TRUNCATE-type and bedaquiline-linezolid strategies remain trial-stage. They are unlikely to reach 20–40% of patients by 2033.

**CORE CLAIM**
- Claim: 20–40% of eligible patients will be on non-HRZE regimens at the benefit horizon, which pushes effective eligibility down to about the 3.6M threshold.
- Support: **LOGIC ONLY**
- Why: No adoption projection exists, and the Investigator admits it is a self-chosen scenario. The slow-uptake evidence points to the low end of the range or below it.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The regimen facts and the direction of the concern are real. The adoption range, the "stronger inducer" claim, and the "uptake slow" claim are ungrounded or unverifiable. The 3.3–4.4M figure depends on a source model (5.5M eligible, 3.6M bar) that I could not see.

**REVISED CRITIQUE**
The 6-month HRZE regimen is no longer the only standard of care. 
WHO conditionally recommends a 4-month HPMZ regimen for people aged 12 or older
, and Paton et al. (NEJM 2023) showed that an 8-week bedaquiline-linezolid strategy was noninferior to standard treatment in a trial. Three things follow:
- Efficacy shown on an HRZE backbone may not transfer to rifapentine/moxifloxacin regimens. Rifapentine is a CYP3A4 inducer, so the atorvastatin interaction question carries over. Whether it is stronger than rifampicin is unverified.
- Shorter regimens may leave less baseline relapse or mortality for an adjunct to improve.
- Any statin benefit that works through shortening treatment would be reduced.

The share of patients moved off HRZE by ~2033 is **UNGROUNDED, plausible but needs empirical support**. Evidence of dosing and supply limits suggests the share may be modest. Direction: uncertain, magnitude: low-to-medium (down from medium), because the displacement estimate has no support and the evidence points to slow uptake.

---

## Critique 2: M72/AS01E and other incidence shocks are likely not large enough by year 8–10, but should be modelled

**CITATION CHECK**
- Tait et al., NEJM 2019, Phase IIb, ~50% efficacy: **VERIFIED.** 
Vaccine efficacy at month 36 was 49.7% (95% CI, 2.1 to 74.2).
 The earlier primary analysis (a separate NEJM 2018 paper) reported 
54.0% (95% CI, 2.9 to 78.2).
 The "Tait 2019" citation correctly points to the final analysis.
- Harris et al. (LSHTM-type models): **PARTIALLY VERIFIED.** Harris et al. exist: 
New tuberculosis vaccines in India: modelling the potential health and economic impacts, with projections to 2050
 (BMC Med 2023). The Investigator said they cannot cite a figure, and I could not extract a 2033–35 incidence figure either. The models report cumulative impact and 2050 outcomes, which is consistent with the "impact in the 2040s" framing but does not prove it.
- Gates MRI Phase III, started 2024, ~20,000 participants: **PARTIALLY VERIFIED, with a discrepancy.** 
Nature reports that M72 entered phase 3 in March 2024, targeting around 26,000 participants across seven countries.
 
The Phase III (Gates MRI; NCT06062238) is described as ongoing.
 A design paper modelled 
18,000 IGRA-positive participants, with 110 events accruing in 3.5–4 years
. So "~20,000" is in the right range, but the current target is higher (~26,000, including the larger HIV cohort).

**CLAIM CHECK**
- Phase IIb efficacy applied to an already-infected population: **VERIFIED.** 
The trial enrolled 3,573 HIV-negative adults aged 18–50 in Southern Africa with evidence of M.tb infection (IGRA+).

- Phase IIb evidence is "small, selected": **VERIFIED.** 
Only 39 participants contributed to the primary efficacy analysis: 13 vaccinated and 26 placebo.
 The confidence interval is very wide.
- Results are expected in the late 2020s and licensure around 2028–30: **PLAUSIBLE, not directly confirmed.** The event-driven design implies several years of accrual after a ~2-year enrolment period. I found no official timeline.
- Incidence reduction of 5–15% by 2033–35: **UNVERIFIABLE.** This is the Investigator's own estimate.
- Vaccine impact accrues gradually, mostly via already-infected people: **PARTIALLY CONTRADICTED / nuanced.** Harris et al. conclude M72 would 
be effective in a larger proportion of the population than BCG-revaccination and have a more rapid impact on tuberculosis incidence.
 Post-infection vaccines act on the prevalent latent pool, so they are faster than infection-blocking vaccines. They are still limited by coverage ramp-up and duration of protection. Separately, 
a vaccine with pre- and post-infection efficacy had a much greater 2050 incidence impact than a post-infection-only vaccine.
 That supports a modest impact from a post-infection-only M72.
- Average eligible pool 20–35% lower over a >15-year horizon: **UNVERIFIABLE.** The Investigator says so. It depends on assumptions about vaccine uptake, duration and coverage.

**EVIDENCE FOUND**
- Models assume ~10-year duration of protection, 50% efficacy and staggered introduction. For example, 
the India model assumed introduction in 2025 with repeat campaigns in 2035 and 2045.
 Vaccine timing therefore matters a great deal. With later introduction, around 2030, impact by 2033–35 is likely small. This supports the Investigator's claim of a small effect at year 8 and a larger one later.
- A baseline assumption matters here. The India model assumed 
scale-up of non-vaccine interventions to meet a 50% reduction in incidence by 2035 versus 2015.
 The CEA's eligible-population baseline should be checked for the same kind of decline.
- A South Africa model found M72 could 
avert between 0.86 and 2.55 million TB cases by 2050
. That is large cumulatively but consistent with back-loaded impact.
- A demand-forecast paper exists (
"Preparing for Tuberculosis Vaccine M72/AS01E Implementation"
). It could inform uptake assumptions but I did not extract numbers from it.

**CORE CLAIM**
- Claim: M72-driven incidence reduction by year 8–10 is small (5–15%). It becomes large (30–50%) only later, so a constant eligible-population assumption overstates the pool in the later years of the benefit horizon.
- Support: **LOGIC ONLY**
- Why: The model literature points to impact building toward 2050 and a modest effect from a post-infection-only vaccine, but no source gives 2033–35 incidence figures, and the 30–50% later-year reduction is not sourced.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The citations are real. The trial size is slightly off (~26,000 target versus ~20,000). The Phase IIb limitations are verified. All the quantitative impact estimates are ungrounded.

**REVISED CRITIQUE**
Tait et al. (NEJM 2019) reported a vaccine efficacy of 49.7% (95% CI 2.1–74.2) against pulmonary TB in about 3,500 HIV-negative, IGRA-positive adults. The primary analysis rested on only 39 cases, so the point estimate is imprecise. The Phase III, which started in March 2024, is ongoing with a target of about 26,000 participants. Licensure and rollout timing are uncertain but unlikely to produce a large incidence effect by 2033–35. Published models (Harris et al. and related work) project cumulative impact toward 2050 and a smaller effect from post-infection-only vaccines. The CEA should therefore be checked for whether it holds the eligible pool constant after year 8. Any later-year reduction in eligibility (30–50%) and the 20–35% averaged reduction are **UNGROUNDED, plausible but needing empirical support** via CEA sensitivity analysis. Vaccine success probability should be weighted separately. Direction: decreases, magnitude: low-to-medium and horizon-dependent, with the "5–15% at year 8" figure marked as the Investigator's own estimate.

--- Critique: M72/AS01E and other incidence shocks are likely not large enough by year 8–10, but should be modelled ---

## Critique 1: Shorter and new regimens erode both the eligible population and the incremental benefit

**CITATION CHECK**
- WHO 2022, 4-month HPMZ for age ≥12: **VERIFIED**. 
WHO's 2022 Module 4 conditionally recommends the 4-month isoniazid–rifapentine–moxifloxacin–pyrazinamide regimen for people aged 12 or older with drug-susceptible pulmonary TB (moderate certainty).

- Dorman et al., NEJM 2021 (Study 31/A5349): **VERIFIED in substance, but not directly retrieved.** 
TBTC Study 31/ACTG A5349 is a phase 3 trial that found the 4-month rifapentine-moxifloxacin regimen safe and effective.
 I did not pull the NEJM 2021 record itself. The authorship and year match my own knowledge.
- Paton et al., NEJM 2023 (TRUNCATE-TB): **VERIFIED.** 
It was published in N Engl J Med 2023;388:873-887.
 The Investigator's "from my recollection" hedge is unnecessary.
- "Bedaquiline-containing short regimens": **PARTIALLY VERIFIED, with a correction.** 
TRUNCATE-TB found that a strategy starting with an 8-week regimen of bedaquiline and linezolid was noninferior to standard treatment at week 96.
 This is a trial strategy that includes retreatment, not a WHO-recommended DS-TB regimen. The Investigator should not group it with HPMZ as an "adopted" regimen.

**CLAIM CHECK**
- WHO recommended the 4-month HPMZ regimen in 2022 for age ≥12: **VERIFIED** (see above).
- A statin trial on HRZE does not establish efficacy on a rifapentine/moxifloxacin backbone: **PLAUSIBLE.** This is sound reasoning, and I found no direct evidence either way.
- "Rifapentine is a stronger CYP3A4 inducer than rifampicin": **UNVERIFIABLE and probably overstated.** I ran out of searches before checking it. From general pharmacology, rifampicin is usually described as the most potent inducer, and rifapentine is comparable or somewhat weaker depending on dose. Both are inducers, so the broader worry about interactions with atorvastatin survives. The comparative "stronger" claim should be dropped or checked.
- "Programme uptake of HPMZ has been slow because of rifapentine supply and cost": **UNVERIFIABLE.** I found no direct source. One adjacent source says 
use of the regimen in clinical practice may be limited by the high rifapentine dose, particularly in patients with comorbidities.
 This partly supports the idea that uptake is constrained, though for a different reason than the Investigator gives.
- 20–40% of eligible patients on non-trial regimens by ~2033: **UNGROUNDED.** The Investigator says so too. I found no projection.
- Shorter regimens reduce room for an adjunct to add benefit: **PLAUSIBLE.** This is logic only.

**EVIDENCE FOUND**
- HPMZ is restricted to age ≥12, and it is conditional. Rifapentine exposure has been shown to drive outcomes: 
low rifapentine exposure is the strongest driver of TB-related unfavorable outcomes in the rifapentine-moxifloxacin arm.
 That limits how fast HPMZ can displace HRZE, because dosing and supply constraints apply. It weakly favours the low end of the Investigator's range.
- Under the WHO guidance, 
adolescents aged 12–16 have three options: 4-month HPMZ, 4-month 2HRZ(E)/2HR, or standard 6-month 2HRZ(E)/4HR.
 The 4-month HRZ(E) regimen for children with non-severe TB still contains rifampicin. The rifamycin-induction problem would therefore remain on that backbone, which weakens the "non-trial backbone" argument for that group.
- Most 2022 TRUNCATE-type and bedaquiline-linezolid strategies remain trial-stage. They are unlikely to reach 20–40% of patients by 2033.

**CORE CLAIM**
- Claim: 20–40% of eligible patients will be on non-HRZE regimens at the benefit horizon, which pushes effective eligibility down to about the 3.6M threshold.
- Support: **LOGIC ONLY**
- Why: No adoption projection exists, and the Investigator admits it is a self-chosen scenario. The slow-uptake evidence points to the low end of the range or below it.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The regimen facts and the direction of the concern are real. The adoption range, the "stronger inducer" claim, and the "uptake slow" claim are ungrounded or unverifiable. The 3.3–4.4M figure depends on a source model (5.5M eligible, 3.6M bar) that I could not see.

**REVISED CRITIQUE**
The 6-month HRZE regimen is no longer the only standard of care. 
WHO conditionally recommends a 4-month HPMZ regimen for people aged 12 or older
, and Paton et al. (NEJM 2023) showed that an 8-week bedaquiline-linezolid strategy was noninferior to standard treatment in a trial. Three things follow:
- Efficacy shown on an HRZE backbone may not transfer to rifapentine/moxifloxacin regimens. Rifapentine is a CYP3A4 inducer, so the atorvastatin interaction question carries over. Whether it is stronger than rifampicin is unverified.
- Shorter regimens may leave less baseline relapse or mortality for an adjunct to improve.
- Any statin benefit that works through shortening treatment would be reduced.

The share of patients moved off HRZE by ~2033 is **UNGROUNDED, plausible but needs empirical support**. Evidence of dosing and supply limits suggests the share may be modest. Direction: uncertain, magnitude: low-to-medium (down from medium), because the displacement estimate has no support and the evidence points to slow uptake.

---

## Critique 2: M72/AS01E and other incidence shocks are likely not large enough by year 8–10, but should be modelled

**CITATION CHECK**
- Tait et al., NEJM 2019, Phase IIb, ~50% efficacy: **VERIFIED.** 
Vaccine efficacy at month 36 was 49.7% (95% CI, 2.1 to 74.2).
 The earlier primary analysis (a separate NEJM 2018 paper) reported 
54.0% (95% CI, 2.9 to 78.2).
 The "Tait 2019" citation correctly points to the final analysis.
- Harris et al. (LSHTM-type models): **PARTIALLY VERIFIED.** Harris et al. exist: 
New tuberculosis vaccines in India: modelling the potential health and economic impacts, with projections to 2050
 (BMC Med 2023). The Investigator said they cannot cite a figure, and I could not extract a 2033–35 incidence figure either. The models report cumulative impact and 2050 outcomes, which is consistent with the "impact in the 2040s" framing but does not prove it.
- Gates MRI Phase III, started 2024, ~20,000 participants: **PARTIALLY VERIFIED, with a discrepancy.** 
Nature reports that M72 entered phase 3 in March 2024, targeting around 26,000 participants across seven countries.
 
The Phase III (Gates MRI; NCT06062238) is described as ongoing.
 A design paper modelled 
18,000 IGRA-positive participants, with 110 events accruing in 3.5–4 years
. So "~20,000" is in the right range, but the current target is higher (~26,000, including the larger HIV cohort).

**CLAIM CHECK**
- Phase IIb efficacy applied to an already-infected population: **VERIFIED.** 
The trial enrolled 3,573 HIV-negative adults aged 18–50 in Southern Africa with evidence of M.tb infection (IGRA+).

- Phase IIb evidence is "small, selected": **VERIFIED.** 
Only 39 participants contributed to the primary efficacy analysis: 13 vaccinated and 26 placebo.
 The confidence interval is very wide.
- Results are expected in the late 2020s and licensure around 2028–30: **PLAUSIBLE, not directly confirmed.** The event-driven design implies several years of accrual after a ~2-year enrolment period. I found no official timeline.
- Incidence reduction of 5–15% by 2033–35: **UNVERIFIABLE.** This is the Investigator's own estimate.
- Vaccine impact accrues gradually, mostly via already-infected people: **PARTIALLY CONTRADICTED / nuanced.** Harris et al. conclude M72 would 
be effective in a larger proportion of the population than BCG-revaccination and have a more rapid impact on tuberculosis incidence.
 Post-infection vaccines act on the prevalent latent pool, so they are faster than infection-blocking vaccines. They are still limited by coverage ramp-up and duration of protection. Separately, 
a vaccine with pre- and post-infection efficacy had a much greater 2050 incidence impact than a post-infection-only vaccine.
 That supports a modest impact from a post-infection-only M72.
- Average eligible pool 20–35% lower over a >15-year horizon: **UNVERIFIABLE.** The Investigator says so. It depends on assumptions about vaccine uptake, duration and coverage.

**EVIDENCE FOUND**
- Models assume ~10-year duration of protection, 50% efficacy and staggered introduction. For example, 
the India model assumed introduction in 2025 with repeat campaigns in 2035 and 2045.
 Vaccine timing therefore matters a great deal. With later introduction, around 2030, impact by 2033–35 is likely small. This supports the Investigator's claim of a small effect at year 8 and a larger one later.
- A baseline assumption matters here. The India model assumed 
scale-up of non-vaccine interventions to meet a 50% reduction in incidence by 2035 versus 2015.
 The CEA's eligible-population baseline should be checked for the same kind of decline.
- A South Africa model found M72 could 
avert between 0.86 and 2.55 million TB cases by 2050
. That is large cumulatively but consistent with back-loaded impact.
- A demand-forecast paper exists (
"Preparing for Tuberculosis Vaccine M72/AS01E Implementation"
). It could inform uptake assumptions but I did not extract numbers from it.

**CORE CLAIM**
- Claim: M72-driven incidence reduction by year 8–10 is small (5–15%). It becomes large (30–50%) only later, so a constant eligible-population assumption overstates the pool in the later years of the benefit horizon.
- Support: **LOGIC ONLY**
- Why: The model literature points to impact building toward 2050 and a modest effect from a post-infection-only vaccine, but no source gives 2033–35 incidence figures, and the 30–50% later-year reduction is not sourced.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The citations are real. The trial size is slightly off (~26,000 target versus ~20,000). The Phase IIb limitations are verified. All the quantitative impact estimates are ungrounded.

**REVISED CRITIQUE**
Tait et al. (NEJM 2019) reported a vaccine efficacy of 49.7% (95% CI 2.1–74.2) against pulmonary TB in about 3,500 HIV-negative, IGRA-positive adults. The primary analysis rested on only 39 cases, so the point estimate is imprecise. The Phase III, which started in March 2024, is ongoing with a target of about 26,000 participants. Licensure and rollout timing are uncertain but unlikely to produce a large incidence effect by 2033–35. Published models (Harris et al. and related work) project cumulative impact toward 2050 and a smaller effect from post-infection-only vaccines. The CEA should therefore be checked for whether it holds the eligible pool constant after year 8. Any later-year reduction in eligibility (30–50%) and the 20–35% averaged reduction are **UNGROUNDED, plausible but needing empirical support** via CEA sensitivity analysis. Vaccine success probability should be weighted separately. Direction: decreases, magnitude: low-to-medium and horizon-dependent, with the "5–15% at year 8" figure marked as the Investigator's own estimate.