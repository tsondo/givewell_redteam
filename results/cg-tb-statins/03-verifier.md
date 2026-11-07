--- Critique: "Success" in Phase III is unlikely to be a mortality result, so the 10% mortality effect is not what a "success" would establish ---

Note: my search budget ran out during this pass. I could not check the Phillips/Wallis surrogate papers, Thwaites 2004, or the HPMZ regimen definition. They are flagged below as unverified. I also could not see the CG model, so any claim about "the SROI threshold" is unverifiable.

---

## Critique 1: "Success" in Phase III is unlikely to be a mortality result

**OVERALL VERDICT: PARTIALLY VERIFIED.** The sample-size arithmetic is correct and the logical point stands. The claim that prior evidence is surrogate-only is supported. The claims about surrogate validity and about the Phase III design are not verified. The size of the effect depends on CG's model structure, which I could not inspect.

**CLAIM CHECK**
- **Sample size of about 36,000 per arm at 4% baseline and a 10% relative reduction:** VERIFIED. I recomputed it with the standard formula (80% power, two-sided α = 0.05) and got about 35,900 per arm.
- **About 17,000 per arm at 8% baseline:** VERIFIED. I get about 17,200.
- **"Larger still" at 2% baseline:** VERIFIED. I get about 73,000 per arm.
- **Baseline mortality assumptions (4%, 8%, 2%):** PLAUSIBLE. These are illustrative, as the Investigator said.
  - A five-country cohort of 23,799 adults on DS-TB treatment found 
6% died during treatment
.
  - A systematic review reported 
case fatality during TB treatment ranging from 1.8 to 33.3%
.
  - I did not find a source for the 2% trial-cohort figure.
- **Prior human evidence is on surrogates:** VERIFIED. The atorvastatin Phase IIB (n=150) reported 
culture-negative results in 97% vs 85.1% and a larger reduction in chest X-ray severity score
. The Phase IIC (STEP) lists 
time to sputum culture conversion, decline in chest X-ray severity score and lung function
 as outcomes in 440 patients. Mortality is not a primary outcome.
- **No mortality-powered trial is planned:** PLAUSIBLE. The registry describes Phase IIC as 
a pilot Phase III
 and says the Phase III 
will be fully international and multicenter
. I found no Phase III endpoint definition.
- **Phillips/Wallis found 2-month culture conversion to be a weak individual-level predictor of relapse:** UNVERIFIABLE in this session. I recall Phillips et al. (AJRCCM, ~2013) making this argument, but I did not confirm it.
- **No evidence that conversion speed predicts mortality:** UNVERIFIABLE. This is an absence claim and I found nothing either way.
- **f = 0.5, r_s = 0.03, and "exactly at the threshold that pushes SROI below 2,000x":** UNVERIFIABLE. These are assumptions and depend on CG's model.

**EVIDENCE FOUND**
- The Phase IIB was open-label, and 
muscle pain was more frequent with atorvastatin (16% vs 5%)
. This affects how much the 97% vs 85% result can be trusted, but it is not mortality evidence.
- The registry notes the Phase IIB also showed 
reduced incidence of peripheral neuropathy
. This is another non-mortality signal.
- Nothing I found supports a 10% mortality reduction from human data. The Investigator's central point is therefore consistent with the registry record.

**REVISED CRITIQUE**
The prior atorvastatin evidence is surrogate-only (culture conversion, chest X-ray score). A mortality-powered DS-TB trial needs roughly 17,000–73,000+ per arm, depending on baseline mortality and assuming a 10% relative effect. A "Phase III success" is therefore most likely a composite-unfavourable-outcome or surrogate success. The mortality effect conditional on success should be discounted toward the surrogate-only value r_s, which is unknown. Keep the f and r_s numbers as flagged assumptions, and drop the Phillips/Wallis claim unless it is separately checked. Strength: **large in direction, with unknown magnitude**. It is conditional on how CG's model defines "success."

---

## Critique 2: A large share of on-treatment deaths is unreachable by a weeks-scale adjunct

**OVERALL VERDICT: PARTIALLY VERIFIED.** The qualitative hypothesis is supported by other studies. The numeric fractions and the HPMZ point are ungrounded. Waitt & Squire exists, but I could not confirm the details the Investigator attributes to it.

**CLAIM CHECK**
- **Waitt & Squire 2011, systematic review of death risk factors:** VERIFIED as a citation. It is Int J Tuberc Lung Dis 2011;15(7):871–885, 
"A systematic review of risk factors for death in adults during and after tuberculosis treatment"
. It is cited as reporting 
comorbidities as risk factors for TB deaths in areas with high TB incidence and HIV prevalence
. Its early-clustering and "mainly Africa" details are UNVERIFIED.
- **Deaths cluster early:** VERIFIED from other sources.
  - In a US study, 
48% of patients who died during treatment died within 30 days
.
  - In a Taiwan series, 
most TB-related deaths occurred early (median survival 20 days)
.
  - In another Taiwan cohort, 
underweight was associated with higher mortality only in the first 8 weeks
.
- **Many deaths are non-TB or comorbidity-driven:** VERIFIED. In the Taiwan series, 
malignancy, liver cirrhosis and renal failure were independent predictors of all TB deaths
, and deaths were classified as TB-related or non-TB-related.
- **HIV is a major driver:** SUPPORTED indirectly. ART 
cut mortality by 44–71% among HIV-positive TB patients
.
- **"25–35% unreachable":** UNVERIFIABLE. This is an illustrative number, and I found no source for the share of deaths that is modifiable.
- **Thwaites 2004 (corticosteroids in TB meningitis):** NOT CHECKED. I recall it as a real NEJM trial showing a mortality benefit, but I did not verify it here.
- **"4-month HPMZ shrinks headroom":** UNVERIFIABLE. The registered ATORTUB regimens use the standard six-month course, and the popPK sub-study lists 
2RHZE/4RH plus 16 weeks of atorvastatin
. I found no HPMZ arm. If CG's model assumes HPMZ, that is an external premise I could not check.

**EVIDENCE FOUND**
- Because early deaths dominate, the adjunct's window matters. Atorvastatin was given for 2 months in the Phase IIB and 16 weeks in the planned sub-study, so it overlaps the early-death period only partly, depending on onset of effect.
- The 1.8–33.3% range shows that the reachable share depends strongly on setting and HIV prevalence. Any single 25–35% figure is therefore weakly grounded.

**REVISED CRITIQUE**
On-treatment deaths are early-clustered and often tied to advanced HIV, comorbidity and non-TB causes. A uniform 10% relative reduction across all deaths likely overstates the modifiable share. The decomposition r_eff = reachable fraction × effect among reachable deaths is logically sound. The 25–35% figure is **UNGROUNDED** and should be presented as a placeholder. Remove the HPMZ headroom claim, or flag it as UNGROUNDED, unless CG's model actually uses a 4-month regimen. Strength: **small-to-medium**, because the direction is well supported but the magnitude is not.

---

## Critique 3: Rifampicin induction limits atorvastatin exposure and trial exposure doesn't transfer

**OVERALL VERDICT: PARTIALLY VERIFIED.** The label and interaction mechanism are verified. One citation is misattributed. The "different statin" premise is largely contradicted by the registry record. The exposure-limitation concern has real support, but the evidence conflicts on steady-state net exposure.

**CITATION CHECK**
- **Atorvastatin label statement on rifampicin:** VERIFIED. The label says 
rifampin can lead to variable reductions in plasma atorvastatin, and simultaneous co-administration is recommended because delayed administration was associated with a significant reduction
. It also states that 
the effect of rifampin on atorvastatin concentrations in hepatocytes is unknown
.
- **Kyrklund et al. 2004, reduced simvastatin exposure:** MISREPRESENTED. The 2004 Kyrklund paper is about **pravastatin**: 
mean AUC was 69% of the placebo phase (range 24–220%)
. The simvastatin paper is Kyrklund et al. **2000**: 
rifampin decreased the AUC of simvastatin and simvastatin acid by 87% and 93%
.
- **Johns Hopkins (Karakousis) pravastatin work:** PARTIALLY VERIFIED. StAT-TB is a Phase **IIb** two-week dose-finding PK/safety study of 
pravastatin, with Karakousis as PI at Johns Hopkins
, not Phase IIa. It is a safety/PK study, not an efficacy trial.

**CLAIM CHECK**
- **CYP3A4 induction plus OATP1B1 inhibition by rifampicin, with a timing trade-off:** VERIFIED. The label cites 
the dual mechanism (CYP3A induction and OATP1B1 inhibition)
.
- **Atorvastatin-specific PK:** VERIFIED. The label table shows that with rifampin and atorvastatin 
co-administered (7 days), AUC rose 30% and Cmax rose 2.7-fold; with doses separated (5 days), AUC fell 80% and Cmax fell 40%
. Backman 2005 confirms the 80% fall: 
rifampin reduced atorvastatin acid AUC by 80%
.
- **"Net steady-state exposure uncertain, plausibly lower":** CONFLICTING.
  - The label's 7-day co-administration data show plasma AUC maintained or increased, not decreased.
  - A review notes that 
the consequences of prolonged simultaneous statin–rifampin administration have never been investigated
.
  - Another review says that 
after multiple doses, induction can overcome the OATP effect and AUC decreases
.
  - Net: uncertain, which matches the Investigator's wording, but "plausibly lower" is not established.
- **Protease inhibitors raise atorvastatin exposure:** VERIFIED. 
Tipranavir/ritonavir raised AUC 9.4-fold
. The efavirenz-lowers claim is supported by the label's inducer wording: 
efavirenz and rifampin can lead to variable reductions
.
- **"Prior positive human data may be from pravastatin or rosuvastatin":** LARGELY FALSE for the likely source.
  - The positive human data are atorvastatin. The ATORTUB Phase IIA/IIB used 
atorvastatin 40 mg daily for 2 months with standard of care
.
  - A reviewer notes that 
rosuvastatin did not affect sputum culture conversion
, so rosuvastatin is a null result, not a positive signal.
  - The pravastatin work is PK-only.
- **Trial exposure doesn't transfer to routine programs:** WEAKENED. ATORTUB was run with rifampicin-containing standard therapy, so any rifampicin-induced exposure loss is already embedded in the observed signal. The remaining issue is whether dosing timing and adherence differ in routine care. I found no evidence on that.
- **Multiplier 0.5–0.8 on r:** UNVERIFIABLE. It is a guess, as the Investigator said.
- **Dolutegravir comment:** NOT CHECKED.

**EVIDENCE FOUND**
- A population PK–PD sub-study is registered. It covers atorvastatin 20/40/60 mg with 2RHZE/4RH: 
16 weeks of daily atorvastatin at each dose
. The Phase IIC registry says 
PK-PD evaluation at different doses, correlated with outcomes, will be essential
. The investigators themselves treat exposure as an open question, which supports the Investigator's concern. The sub-study could also provide the missing data.
- If a Phase III used a rifapentine-based regimen (as "HPMZ" suggests), the rifampicin-specific label guidance would not map directly. Rifapentine is also a CYP3A4 inducer, but I did not verify its atorvastatin interaction.

**REVISED CRITIQUE**
Atorvastatin exposure under rifampicin depends on dosing timing: separated dosing cuts AUC by about 80%, while simultaneous dosing preserves or raises plasma AUC at 7 days. Net chronic-dosing exposure at the site of action (lung, hepatocyte) is **UNGROUNDED**. The atorvastatin label itself says the hepatocyte effect is unknown. Replace "Kyrklund 2004 (simvastatin)" with Kyrklund 2000 (simvastatin) and Backman 2005 (atorvastatin). Drop the premise that the positive human signal came from a different statin, because the Phase IIA/IIB was atorvastatin, so the signal was generated under rifampicin. The surviving concern is that routine-program dosing may not reproduce trial-condition timing and adherence, plus the ART interactions. Strength: **medium** (reduced from large), with magnitude unknown. A PK/PD model or the ATORTUB popPK-PD sub-study is needed.

--- Critique: A large share of on-treatment deaths is unreachable by a weeks-scale host-directed adjunct, and shorter regimens shrink the headroom further ---

Note: my search budget ran out during this pass. I could not check the Phillips/Wallis surrogate papers, Thwaites 2004, or the HPMZ regimen definition. They are flagged below as unverified. I also could not see the CG model, so any claim about "the SROI threshold" is unverifiable.

---

## Critique 1: "Success" in Phase III is unlikely to be a mortality result

**OVERALL VERDICT: PARTIALLY VERIFIED.** The sample-size arithmetic is correct and the logical point stands. The claim that prior evidence is surrogate-only is supported. The claims about surrogate validity and about the Phase III design are not verified. The size of the effect depends on CG's model structure, which I could not inspect.

**CLAIM CHECK**
- **Sample size of about 36,000 per arm at 4% baseline and a 10% relative reduction:** VERIFIED. I recomputed it with the standard formula (80% power, two-sided α = 0.05) and got about 35,900 per arm.
- **About 17,000 per arm at 8% baseline:** VERIFIED. I get about 17,200.
- **"Larger still" at 2% baseline:** VERIFIED. I get about 73,000 per arm.
- **Baseline mortality assumptions (4%, 8%, 2%):** PLAUSIBLE. These are illustrative, as the Investigator said.
  - A five-country cohort of 23,799 adults on DS-TB treatment found 
6% died during treatment
.
  - A systematic review reported 
case fatality during TB treatment ranging from 1.8 to 33.3%
.
  - I did not find a source for the 2% trial-cohort figure.
- **Prior human evidence is on surrogates:** VERIFIED. The atorvastatin Phase IIB (n=150) reported 
culture-negative results in 97% vs 85.1% and a larger reduction in chest X-ray severity score
. The Phase IIC (STEP) lists 
time to sputum culture conversion, decline in chest X-ray severity score and lung function
 as outcomes in 440 patients. Mortality is not a primary outcome.
- **No mortality-powered trial is planned:** PLAUSIBLE. The registry describes Phase IIC as 
a pilot Phase III
 and says the Phase III 
will be fully international and multicenter
. I found no Phase III endpoint definition.
- **Phillips/Wallis found 2-month culture conversion to be a weak individual-level predictor of relapse:** UNVERIFIABLE in this session. I recall Phillips et al. (AJRCCM, ~2013) making this argument, but I did not confirm it.
- **No evidence that conversion speed predicts mortality:** UNVERIFIABLE. This is an absence claim and I found nothing either way.
- **f = 0.5, r_s = 0.03, and "exactly at the threshold that pushes SROI below 2,000x":** UNVERIFIABLE. These are assumptions and depend on CG's model.

**EVIDENCE FOUND**
- The Phase IIB was open-label, and 
muscle pain was more frequent with atorvastatin (16% vs 5%)
. This affects how much the 97% vs 85% result can be trusted, but it is not mortality evidence.
- The registry notes the Phase IIB also showed 
reduced incidence of peripheral neuropathy
. This is another non-mortality signal.
- Nothing I found supports a 10% mortality reduction from human data. The Investigator's central point is therefore consistent with the registry record.

**REVISED CRITIQUE**
The prior atorvastatin evidence is surrogate-only (culture conversion, chest X-ray score). A mortality-powered DS-TB trial needs roughly 17,000–73,000+ per arm, depending on baseline mortality and assuming a 10% relative effect. A "Phase III success" is therefore most likely a composite-unfavourable-outcome or surrogate success. The mortality effect conditional on success should be discounted toward the surrogate-only value r_s, which is unknown. Keep the f and r_s numbers as flagged assumptions, and drop the Phillips/Wallis claim unless it is separately checked. Strength: **large in direction, with unknown magnitude**. It is conditional on how CG's model defines "success."

---

## Critique 2: A large share of on-treatment deaths is unreachable by a weeks-scale adjunct

**OVERALL VERDICT: PARTIALLY VERIFIED.** The qualitative hypothesis is supported by other studies. The numeric fractions and the HPMZ point are ungrounded. Waitt & Squire exists, but I could not confirm the details the Investigator attributes to it.

**CLAIM CHECK**
- **Waitt & Squire 2011, systematic review of death risk factors:** VERIFIED as a citation. It is Int J Tuberc Lung Dis 2011;15(7):871–885, 
"A systematic review of risk factors for death in adults during and after tuberculosis treatment"
. It is cited as reporting 
comorbidities as risk factors for TB deaths in areas with high TB incidence and HIV prevalence
. Its early-clustering and "mainly Africa" details are UNVERIFIED.
- **Deaths cluster early:** VERIFIED from other sources.
  - In a US study, 
48% of patients who died during treatment died within 30 days
.
  - In a Taiwan series, 
most TB-related deaths occurred early (median survival 20 days)
.
  - In another Taiwan cohort, 
underweight was associated with higher mortality only in the first 8 weeks
.
- **Many deaths are non-TB or comorbidity-driven:** VERIFIED. In the Taiwan series, 
malignancy, liver cirrhosis and renal failure were independent predictors of all TB deaths
, and deaths were classified as TB-related or non-TB-related.
- **HIV is a major driver:** SUPPORTED indirectly. ART 
cut mortality by 44–71% among HIV-positive TB patients
.
- **"25–35% unreachable":** UNVERIFIABLE. This is an illustrative number, and I found no source for the share of deaths that is modifiable.
- **Thwaites 2004 (corticosteroids in TB meningitis):** NOT CHECKED. I recall it as a real NEJM trial showing a mortality benefit, but I did not verify it here.
- **"4-month HPMZ shrinks headroom":** UNVERIFIABLE. The registered ATORTUB regimens use the standard six-month course, and the popPK sub-study lists 
2RHZE/4RH plus 16 weeks of atorvastatin
. I found no HPMZ arm. If CG's model assumes HPMZ, that is an external premise I could not check.

**EVIDENCE FOUND**
- Because early deaths dominate, the adjunct's window matters. Atorvastatin was given for 2 months in the Phase IIB and 16 weeks in the planned sub-study, so it overlaps the early-death period only partly, depending on onset of effect.
- The 1.8–33.3% range shows that the reachable share depends strongly on setting and HIV prevalence. Any single 25–35% figure is therefore weakly grounded.

**REVISED CRITIQUE**
On-treatment deaths are early-clustered and often tied to advanced HIV, comorbidity and non-TB causes. A uniform 10% relative reduction across all deaths likely overstates the modifiable share. The decomposition r_eff = reachable fraction × effect among reachable deaths is logically sound. The 25–35% figure is **UNGROUNDED** and should be presented as a placeholder. Remove the HPMZ headroom claim, or flag it as UNGROUNDED, unless CG's model actually uses a 4-month regimen. Strength: **small-to-medium**, because the direction is well supported but the magnitude is not.

---

## Critique 3: Rifampicin induction limits atorvastatin exposure and trial exposure doesn't transfer

**OVERALL VERDICT: PARTIALLY VERIFIED.** The label and interaction mechanism are verified. One citation is misattributed. The "different statin" premise is largely contradicted by the registry record. The exposure-limitation concern has real support, but the evidence conflicts on steady-state net exposure.

**CITATION CHECK**
- **Atorvastatin label statement on rifampicin:** VERIFIED. The label says 
rifampin can lead to variable reductions in plasma atorvastatin, and simultaneous co-administration is recommended because delayed administration was associated with a significant reduction
. It also states that 
the effect of rifampin on atorvastatin concentrations in hepatocytes is unknown
.
- **Kyrklund et al. 2004, reduced simvastatin exposure:** MISREPRESENTED. The 2004 Kyrklund paper is about **pravastatin**: 
mean AUC was 69% of the placebo phase (range 24–220%)
. The simvastatin paper is Kyrklund et al. **2000**: 
rifampin decreased the AUC of simvastatin and simvastatin acid by 87% and 93%
.
- **Johns Hopkins (Karakousis) pravastatin work:** PARTIALLY VERIFIED. StAT-TB is a Phase **IIb** two-week dose-finding PK/safety study of 
pravastatin, with Karakousis as PI at Johns Hopkins
, not Phase IIa. It is a safety/PK study, not an efficacy trial.

**CLAIM CHECK**
- **CYP3A4 induction plus OATP1B1 inhibition by rifampicin, with a timing trade-off:** VERIFIED. The label cites 
the dual mechanism (CYP3A induction and OATP1B1 inhibition)
.
- **Atorvastatin-specific PK:** VERIFIED. The label table shows that with rifampin and atorvastatin 
co-administered (7 days), AUC rose 30% and Cmax rose 2.7-fold; with doses separated (5 days), AUC fell 80% and Cmax fell 40%
. Backman 2005 confirms the 80% fall: 
rifampin reduced atorvastatin acid AUC by 80%
.
- **"Net steady-state exposure uncertain, plausibly lower":** CONFLICTING.
  - The label's 7-day co-administration data show plasma AUC maintained or increased, not decreased.
  - A review notes that 
the consequences of prolonged simultaneous statin–rifampin administration have never been investigated
.
  - Another review says that 
after multiple doses, induction can overcome the OATP effect and AUC decreases
.
  - Net: uncertain, which matches the Investigator's wording, but "plausibly lower" is not established.
- **Protease inhibitors raise atorvastatin exposure:** VERIFIED. 
Tipranavir/ritonavir raised AUC 9.4-fold
. The efavirenz-lowers claim is supported by the label's inducer wording: 
efavirenz and rifampin can lead to variable reductions
.
- **"Prior positive human data may be from pravastatin or rosuvastatin":** LARGELY FALSE for the likely source.
  - The positive human data are atorvastatin. The ATORTUB Phase IIA/IIB used 
atorvastatin 40 mg daily for 2 months with standard of care
.
  - A reviewer notes that 
rosuvastatin did not affect sputum culture conversion
, so rosuvastatin is a null result, not a positive signal.
  - The pravastatin work is PK-only.
- **Trial exposure doesn't transfer to routine programs:** WEAKENED. ATORTUB was run with rifampicin-containing standard therapy, so any rifampicin-induced exposure loss is already embedded in the observed signal. The remaining issue is whether dosing timing and adherence differ in routine care. I found no evidence on that.
- **Multiplier 0.5–0.8 on r:** UNVERIFIABLE. It is a guess, as the Investigator said.
- **Dolutegravir comment:** NOT CHECKED.

**EVIDENCE FOUND**
- A population PK–PD sub-study is registered. It covers atorvastatin 20/40/60 mg with 2RHZE/4RH: 
16 weeks of daily atorvastatin at each dose
. The Phase IIC registry says 
PK-PD evaluation at different doses, correlated with outcomes, will be essential
. The investigators themselves treat exposure as an open question, which supports the Investigator's concern. The sub-study could also provide the missing data.
- If a Phase III used a rifapentine-based regimen (as "HPMZ" suggests), the rifampicin-specific label guidance would not map directly. Rifapentine is also a CYP3A4 inducer, but I did not verify its atorvastatin interaction.

**REVISED CRITIQUE**
Atorvastatin exposure under rifampicin depends on dosing timing: separated dosing cuts AUC by about 80%, while simultaneous dosing preserves or raises plasma AUC at 7 days. Net chronic-dosing exposure at the site of action (lung, hepatocyte) is **UNGROUNDED**. The atorvastatin label itself says the hepatocyte effect is unknown. Replace "Kyrklund 2004 (simvastatin)" with Kyrklund 2000 (simvastatin) and Backman 2005 (atorvastatin). Drop the premise that the positive human signal came from a different statin, because the Phase IIA/IIB was atorvastatin, so the signal was generated under rifampicin. The surviving concern is that routine-program dosing may not reproduce trial-condition timing and adherence, plus the ART interactions. Strength: **medium** (reduced from large), with magnitude unknown. A PK/PD model or the ATORTUB popPK-PD sub-study is needed.

--- Critique: Rifampicin induction structurally limits atorvastatin exposure in routine programs, and the trial exposure does not transfer ---

Note: my search budget ran out during this pass. I could not check the Phillips/Wallis surrogate papers, Thwaites 2004, or the HPMZ regimen definition. They are flagged below as unverified. I also could not see the CG model, so any claim about "the SROI threshold" is unverifiable.

---

## Critique 1: "Success" in Phase III is unlikely to be a mortality result

**OVERALL VERDICT: PARTIALLY VERIFIED.** The sample-size arithmetic is correct and the logical point stands. The claim that prior evidence is surrogate-only is supported. The claims about surrogate validity and about the Phase III design are not verified. The size of the effect depends on CG's model structure, which I could not inspect.

**CLAIM CHECK**
- **Sample size of about 36,000 per arm at 4% baseline and a 10% relative reduction:** VERIFIED. I recomputed it with the standard formula (80% power, two-sided α = 0.05) and got about 35,900 per arm.
- **About 17,000 per arm at 8% baseline:** VERIFIED. I get about 17,200.
- **"Larger still" at 2% baseline:** VERIFIED. I get about 73,000 per arm.
- **Baseline mortality assumptions (4%, 8%, 2%):** PLAUSIBLE. These are illustrative, as the Investigator said.
  - A five-country cohort of 23,799 adults on DS-TB treatment found 
6% died during treatment
.
  - A systematic review reported 
case fatality during TB treatment ranging from 1.8 to 33.3%
.
  - I did not find a source for the 2% trial-cohort figure.
- **Prior human evidence is on surrogates:** VERIFIED. The atorvastatin Phase IIB (n=150) reported 
culture-negative results in 97% vs 85.1% and a larger reduction in chest X-ray severity score
. The Phase IIC (STEP) lists 
time to sputum culture conversion, decline in chest X-ray severity score and lung function
 as outcomes in 440 patients. Mortality is not a primary outcome.
- **No mortality-powered trial is planned:** PLAUSIBLE. The registry describes Phase IIC as 
a pilot Phase III
 and says the Phase III 
will be fully international and multicenter
. I found no Phase III endpoint definition.
- **Phillips/Wallis found 2-month culture conversion to be a weak individual-level predictor of relapse:** UNVERIFIABLE in this session. I recall Phillips et al. (AJRCCM, ~2013) making this argument, but I did not confirm it.
- **No evidence that conversion speed predicts mortality:** UNVERIFIABLE. This is an absence claim and I found nothing either way.
- **f = 0.5, r_s = 0.03, and "exactly at the threshold that pushes SROI below 2,000x":** UNVERIFIABLE. These are assumptions and depend on CG's model.

**EVIDENCE FOUND**
- The Phase IIB was open-label, and 
muscle pain was more frequent with atorvastatin (16% vs 5%)
. This affects how much the 97% vs 85% result can be trusted, but it is not mortality evidence.
- The registry notes the Phase IIB also showed 
reduced incidence of peripheral neuropathy
. This is another non-mortality signal.
- Nothing I found supports a 10% mortality reduction from human data. The Investigator's central point is therefore consistent with the registry record.

**REVISED CRITIQUE**
The prior atorvastatin evidence is surrogate-only (culture conversion, chest X-ray score). A mortality-powered DS-TB trial needs roughly 17,000–73,000+ per arm, depending on baseline mortality and assuming a 10% relative effect. A "Phase III success" is therefore most likely a composite-unfavourable-outcome or surrogate success. The mortality effect conditional on success should be discounted toward the surrogate-only value r_s, which is unknown. Keep the f and r_s numbers as flagged assumptions, and drop the Phillips/Wallis claim unless it is separately checked. Strength: **large in direction, with unknown magnitude**. It is conditional on how CG's model defines "success."

---

## Critique 2: A large share of on-treatment deaths is unreachable by a weeks-scale adjunct

**OVERALL VERDICT: PARTIALLY VERIFIED.** The qualitative hypothesis is supported by other studies. The numeric fractions and the HPMZ point are ungrounded. Waitt & Squire exists, but I could not confirm the details the Investigator attributes to it.

**CLAIM CHECK**
- **Waitt & Squire 2011, systematic review of death risk factors:** VERIFIED as a citation. It is Int J Tuberc Lung Dis 2011;15(7):871–885, 
"A systematic review of risk factors for death in adults during and after tuberculosis treatment"
. It is cited as reporting 
comorbidities as risk factors for TB deaths in areas with high TB incidence and HIV prevalence
. Its early-clustering and "mainly Africa" details are UNVERIFIED.
- **Deaths cluster early:** VERIFIED from other sources.
  - In a US study, 
48% of patients who died during treatment died within 30 days
.
  - In a Taiwan series, 
most TB-related deaths occurred early (median survival 20 days)
.
  - In another Taiwan cohort, 
underweight was associated with higher mortality only in the first 8 weeks
.
- **Many deaths are non-TB or comorbidity-driven:** VERIFIED. In the Taiwan series, 
malignancy, liver cirrhosis and renal failure were independent predictors of all TB deaths
, and deaths were classified as TB-related or non-TB-related.
- **HIV is a major driver:** SUPPORTED indirectly. ART 
cut mortality by 44–71% among HIV-positive TB patients
.
- **"25–35% unreachable":** UNVERIFIABLE. This is an illustrative number, and I found no source for the share of deaths that is modifiable.
- **Thwaites 2004 (corticosteroids in TB meningitis):** NOT CHECKED. I recall it as a real NEJM trial showing a mortality benefit, but I did not verify it here.
- **"4-month HPMZ shrinks headroom":** UNVERIFIABLE. The registered ATORTUB regimens use the standard six-month course, and the popPK sub-study lists 
2RHZE/4RH plus 16 weeks of atorvastatin
. I found no HPMZ arm. If CG's model assumes HPMZ, that is an external premise I could not check.

**EVIDENCE FOUND**
- Because early deaths dominate, the adjunct's window matters. Atorvastatin was given for 2 months in the Phase IIB and 16 weeks in the planned sub-study, so it overlaps the early-death period only partly, depending on onset of effect.
- The 1.8–33.3% range shows that the reachable share depends strongly on setting and HIV prevalence. Any single 25–35% figure is therefore weakly grounded.

**REVISED CRITIQUE**
On-treatment deaths are early-clustered and often tied to advanced HIV, comorbidity and non-TB causes. A uniform 10% relative reduction across all deaths likely overstates the modifiable share. The decomposition r_eff = reachable fraction × effect among reachable deaths is logically sound. The 25–35% figure is **UNGROUNDED** and should be presented as a placeholder. Remove the HPMZ headroom claim, or flag it as UNGROUNDED, unless CG's model actually uses a 4-month regimen. Strength: **small-to-medium**, because the direction is well supported but the magnitude is not.

---

## Critique 3: Rifampicin induction limits atorvastatin exposure and trial exposure doesn't transfer

**OVERALL VERDICT: PARTIALLY VERIFIED.** The label and interaction mechanism are verified. One citation is misattributed. The "different statin" premise is largely contradicted by the registry record. The exposure-limitation concern has real support, but the evidence conflicts on steady-state net exposure.

**CITATION CHECK**
- **Atorvastatin label statement on rifampicin:** VERIFIED. The label says 
rifampin can lead to variable reductions in plasma atorvastatin, and simultaneous co-administration is recommended because delayed administration was associated with a significant reduction
. It also states that 
the effect of rifampin on atorvastatin concentrations in hepatocytes is unknown
.
- **Kyrklund et al. 2004, reduced simvastatin exposure:** MISREPRESENTED. The 2004 Kyrklund paper is about **pravastatin**: 
mean AUC was 69% of the placebo phase (range 24–220%)
. The simvastatin paper is Kyrklund et al. **2000**: 
rifampin decreased the AUC of simvastatin and simvastatin acid by 87% and 93%
.
- **Johns Hopkins (Karakousis) pravastatin work:** PARTIALLY VERIFIED. StAT-TB is a Phase **IIb** two-week dose-finding PK/safety study of 
pravastatin, with Karakousis as PI at Johns Hopkins
, not Phase IIa. It is a safety/PK study, not an efficacy trial.

**CLAIM CHECK**
- **CYP3A4 induction plus OATP1B1 inhibition by rifampicin, with a timing trade-off:** VERIFIED. The label cites 
the dual mechanism (CYP3A induction and OATP1B1 inhibition)
.
- **Atorvastatin-specific PK:** VERIFIED. The label table shows that with rifampin and atorvastatin 
co-administered (7 days), AUC rose 30% and Cmax rose 2.7-fold; with doses separated (5 days), AUC fell 80% and Cmax fell 40%
. Backman 2005 confirms the 80% fall: 
rifampin reduced atorvastatin acid AUC by 80%
.
- **"Net steady-state exposure uncertain, plausibly lower":** CONFLICTING.
  - The label's 7-day co-administration data show plasma AUC maintained or increased, not decreased.
  - A review notes that 
the consequences of prolonged simultaneous statin–rifampin administration have never been investigated
.
  - Another review says that 
after multiple doses, induction can overcome the OATP effect and AUC decreases
.
  - Net: uncertain, which matches the Investigator's wording, but "plausibly lower" is not established.
- **Protease inhibitors raise atorvastatin exposure:** VERIFIED. 
Tipranavir/ritonavir raised AUC 9.4-fold
. The efavirenz-lowers claim is supported by the label's inducer wording: 
efavirenz and rifampin can lead to variable reductions
.
- **"Prior positive human data may be from pravastatin or rosuvastatin":** LARGELY FALSE for the likely source.
  - The positive human data are atorvastatin. The ATORTUB Phase IIA/IIB used 
atorvastatin 40 mg daily for 2 months with standard of care
.
  - A reviewer notes that 
rosuvastatin did not affect sputum culture conversion
, so rosuvastatin is a null result, not a positive signal.
  - The pravastatin work is PK-only.
- **Trial exposure doesn't transfer to routine programs:** WEAKENED. ATORTUB was run with rifampicin-containing standard therapy, so any rifampicin-induced exposure loss is already embedded in the observed signal. The remaining issue is whether dosing timing and adherence differ in routine care. I found no evidence on that.
- **Multiplier 0.5–0.8 on r:** UNVERIFIABLE. It is a guess, as the Investigator said.
- **Dolutegravir comment:** NOT CHECKED.

**EVIDENCE FOUND**
- A population PK–PD sub-study is registered. It covers atorvastatin 20/40/60 mg with 2RHZE/4RH: 
16 weeks of daily atorvastatin at each dose
. The Phase IIC registry says 
PK-PD evaluation at different doses, correlated with outcomes, will be essential
. The investigators themselves treat exposure as an open question, which supports the Investigator's concern. The sub-study could also provide the missing data.
- If a Phase III used a rifapentine-based regimen (as "HPMZ" suggests), the rifampicin-specific label guidance would not map directly. Rifapentine is also a CYP3A4 inducer, but I did not verify its atorvastatin interaction.

**REVISED CRITIQUE**
Atorvastatin exposure under rifampicin depends on dosing timing: separated dosing cuts AUC by about 80%, while simultaneous dosing preserves or raises plasma AUC at 7 days. Net chronic-dosing exposure at the site of action (lung, hepatocyte) is **UNGROUNDED**. The atorvastatin label itself says the hepatocyte effect is unknown. Replace "Kyrklund 2004 (simvastatin)" with Kyrklund 2000 (simvastatin) and Backman 2005 (atorvastatin). Drop the premise that the positive human signal came from a different statin, because the Phase IIA/IIB was atorvastatin, so the signal was generated under rifampicin. The surviving concern is that routine-program dosing may not reproduce trial-condition timing and adherence, plus the ART interactions. Strength: **medium** (reduced from large), with magnitude unknown. A PK/PD model or the ATORTUB popPK-PD sub-study is needed.

--- Critique: Winner's-curse and reference-class patterns imply the conditional effect should sit well below the surrogate-implied one, and r and p_success should not be independent ---

## Critique 1: Winner's curse and reference-class patterns

**CLAIM CHECK**

- **Martineau 2011 vitamin D trial, culture-conversion signal in a genotype subgroup:** VERIFIED, but the framing needs correcting.
  - 
Median time to sputum culture conversion was 36.0 days with vitamin D and 43.5 days with placebo (adjusted HR 1.39, 95% CI 0.90–2.16, p=0.14).
 The primary endpoint was therefore null.
  - 
TaqI genotype modified the effect (p-interaction 0.03), with a response only in tt-genotype patients (HR 8.09, 95% CI 1.36–48.01).
 The tt subgroup estimate is very wide and imprecise, which is a textbook winner's-curse profile.
  - This was a post-hoc subgroup signal, not a Phase II trial that "passed" a filter.
- **No robust later benefit:** VERIFIED. 
A meta-analysis found no shortening of time to sputum culture conversion overall (HR 1.04, 0.89–1.23).
 A later trial also 
found that the tt genotype did not influence conversion, in contrast with the earlier report.
 The subgroup effect was not replicated in that trial.
- **CC-11050 and everolimus "surrogate positives that fail to translate":** MISREPRESENTED.
  - The relevant trial is Wallis et al. 2021, a phase 2 trial in South Africa (NCT02968927).
  - 
It found both drugs safe and well tolerated, and they might have improved FEV1 recovery.
 
FEV1 was significantly higher than control at day 180 (CC-11050 6.30%, p=0.048; everolimus 6.56%, p=0.044).

  - 
There was no effect of CC-11050 on stable culture conversion, which the authors attributed to small sample size.

  - 
The authors called for further definitive studies.
 I found no Phase III, so these drugs have not "failed to translate". They are untested at Phase III.
  - Safety and FEV1 were the endpoints, not mortality.
- **Metformin "mixed or no clear clinical benefit":** NOT SUPPORTED as stated.
  - What exists is mostly observational or preclinical work. 
A scoping review describes pilot preclinical and observational research recommending metformin as an adjunct.

  - 
The impact of combining metformin with RHZE is described as still under investigation.

  - Metformin is therefore unproven, not a documented translation failure. I found no completed outcome RCT in these results.
- **Observational statin cohorts exposed to healthy-user and indication bias:** PLAUSIBLE (logical argument).
  - 
Population-based studies found statin use related to lower TB incidence.

  - I did not locate the specific Taiwan or Korea statin cohorts, so I could not verify them. A comparable Taiwan metformin cohort did find an association with lower TB risk. 
The HR was 0.84 (0.74–0.96).

- **Winner's curse as a general statistical result:** VERIFIED as standard theory (no search needed).
- **Joint-distribution claim, "E[r × p_success] below the product of means":** LOGICALLY CONDITIONAL.
  - The sign of the covariance depends on how p_success is defined.
  - If success is defined on a surrogate and surrogate-only wins exist, high p_success pairs with r≈0. That gives a negative covariance, so E[rp] is below E[r]E[p], as the critique says.
  - If p_success means success on a mortality-powered endpoint, real-effect worlds have both high p and high r. That gives a positive covariance and the effect reverses.
  - I could not inspect the CG model to see which applies.
- **Shrinkage arithmetic:** the 0.7–0.9 factor is explicitly an assumption, and 0.10 × 0.7–0.9 = 0.07–0.09 is arithmetically correct.

**EVIDENCE FOUND (additional)**

- The directly relevant statin reference class contradicts the "early positive signal" premise. Human surrogate data for statins in TB are null so far.
  - 
Rosuvastatin phase 2b: median time to culture conversion was 42 days in both arms (HR 1.30, 0.88–1.91, p=0.19).

  - 
Rosuvastatin had no impact on PET-CT changes.

  - 
StAT-TB (pravastatin, phase 2b) is registered as completed.
 I found no results in this search.
  - Atorvastatin evidence in these results is preclinical. 
In guinea pigs, atorvastatin and anti-TB drugs showed a synergistic bactericidal action.

- So the 10% likely rests on preclinical and observational anchoring, not a winner's-curse-selected human trial. That is a different mechanism (translation risk and confounding) and arguably points to a larger downward adjustment than shrinkage alone.
- 
An editorial notes there is no clear consensus on appropriate biomarkers or study endpoints for HDT trials.
 This supports the surrogate-to-outcome concern in general terms.

**OVERALL VERDICT: PARTIALLY VERIFIED.**

**REVISED CRITIQUE**

- **Survives:** The 10% conditional effect is probably over-optimistic.
  - Early or subgroup estimates are upwardly biased.
  - Martineau 2011 is a valid example, but of a post-hoc subgroup signal that did not replicate.
  - Observational statin data are confounded.
  - r and p_success are unlikely to be independent, though the sign of the effect on E[rp] depends on how success is defined.
- **Removed:** The claims that CC-11050, everolimus and metformin are failed-translation examples. They are unproven, not refuted.
- **Added:** Human statin-in-TB surrogate trials (rosuvastatin) are null. None of them used atorvastatin.
- **Status:** The shrinkage factor is UNGROUNDED, an illustrative assumption. Direction: decreases. Magnitude: medium.

---

## Critique 2: Hepatotoxicity, myopathy, and compounding

**CLAIM CHECK**

- **HRZ hepatotoxicity and statin liver/muscle warnings are well established:** PLAUSIBLE from standard labeling and general knowledge. I did not retrieve labels in this session.
  - Supportive data point: in the Wallis HDT trial, 
two control-group patients had life-threatening, treatment-attributable liver injury
 on standard therapy.
- **Small phase II trials cannot detect excess mortality from hepatotoxicity:** PLAUSIBLE (statistical).
  - The rosuvastatin trial is a data point. 
Grade 3–5 adverse events occurred in 9% (6/70) with rosuvastatin versus 6% (4/67) in controls (p=0.75), none considered related to rosuvastatin.

  - There was no signal, but the trial is too small to exclude a rare harm. Rosuvastatin also has less CYP3A4 involvement than atorvastatin, so it does not transfer directly.
- **Myopathy risk higher with "some ART":** PLAUSIBLE but of limited relevance.
  - From my own knowledge (not searched here), the main statin interaction is with boosted protease inhibitors and cobicistat. Those are generally avoided with rifampicin, and efavirenz or dolutegravir regimens are the usual choice.
  - The ART argument is therefore weaker for rifampicin-based TB treatment.
- **"CG models only a non-negative effect":** UNVERIFIABLE. The CG model is not available to me.
- **−0.01 contribution:** arithmetic is correct (10% × 0.10 = 0.01).
  - A "net-zero" outcome is already what a failed Phase III in p_success represents. Counting it again as a harm tail risks double-counting.
  - Only the genuinely negative portion is incremental.
- **Compounding product:** arithmetic VERIFIED. 0.65×0.5×0.7 = 0.23 and 0.75×0.8×0.9 = 0.54, so r ≈ 0.023–0.054. The inputs come from other critiques that I cannot see. The Investigator itself flags that the factors overlap and are correlated.
- **PK attenuation (0.5–0.8):** this concerns rifampicin induction of atorvastatin metabolism.
  - I did not search this specifically. I know from general pharmacology that rifampicin lowers atorvastatin exposure, but I did not verify the magnitude here.
  - Supportive indirect evidence: the Wallis trial 
substituted rifabutin for rifampin because of potentially deleterious pharmacokinetic interactions with the HDT drugs.
 The StAT-TB protocol 
cites known pravastatin–rifampin interactions in humans.

  - Interaction-driven dosing problems are a recognized concern in this field.

**EVIDENCE FOUND (additional)**

- StAT-TB chose pravastatin partly for lower toxicity. 
Pravastatin showed the least toxicity in THP-1 and Vero cells.
 The programme's own choice of statin was driven by interaction and toxicity concerns.
- The rosuvastatin trial's safety result is mildly reassuring but underpowered for mortality.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The hypothesis is sound but largely ungrounded on magnitude, and the compounding is an upper bound.

**REVISED CRITIQUE**

- **Survives:** A harm tail for hepatotoxicity or myopathy is plausible and not testable in small trials. Adding hepatotoxic risk on top of HRZ is biologically coherent. Compounding of attenuations is a reasonable concern.
- **Corrections:**
  - The harm-tail adjustment is small (≈ −0.01 at most) and may double-count p_success.
  - The ART-myopathy point is weak for rifampicin-based regimens.
  - The 0.023–0.054 range is an upper-bound illustration. It uses correlated inputs from other critiques that could not be checked.
- **Flag:** "UNGROUNDED – plausible but needs empirical support" on magnitude. Direction: decreases. Magnitude: small for the harm tail itself, medium for the compounding.

---

## Critique 3: A $7M Phase III cannot be powered on mortality

**CLAIM CHECK**

I recomputed the sample sizes with the standard two-proportion formula, α=0.05 two-sided, 80% power (z-sum² = 7.849).

- **5.0% → 4.5% mortality:** VERIFIED. n per arm = 7.849 × (0.0475 + 0.042975) / 0.000025 ≈ 28,400, so about 56,800 in total. The critique says about 28,000 per arm and 57,000 in total.
- **8.0% → 7.2% mortality:** VERIFIED. n per arm = 7.849 × (0.0736 + 0.066816) / 0.000064 ≈ 17,200, so about 34,400 in total. The critique says about 17,000 per arm and 35,000 in total.
- **Cost at $500–$1,000 per participant:** arithmetic is roughly right. The two scenarios give about $17M–$57M across the two enrolment sizes (35,000 and 57,000), so the quoted range is correct as a union.
- **Cost-per-participant realism:** PARTIALLY SUPPORTED. The range is too narrow at the low end and too low for TB specifically.
  - Embedded pragmatic trials have cost far less. 
Across 64 such trials, mean cost per patient randomized was $478 and median $97 (2015 dollars).
 
Ten trials cost over $1,000 per patient.

  - At the $97 median, 35,000–57,000 patients would cost only about $3.4M–$5.5M, which would fit inside $7M. These are mostly EHR- or registry-embedded trials in high-income settings, not 6-month TB trials with clinical follow-up in LMICs.
  - At the other extreme, 
TB-PRACTECAL cost €33.9M in total, an average of €61,460 per patient.
 That is an MDR-TB trial with hospital-based visits, but it shows TB-trial costs can be orders of magnitude above $1,000.
  - 
Standard trials are typically estimated at $2,000–$40,000 per subject.

  - So the true cost range is wide, and "$500–$1,000" is a central pragmatic guess, not a verified figure.
- **RECOVERY showed very low per-patient costs:** UNVERIFIED. I did not find a RECOVERY per-patient cost in my search. The embedded-trial review is the best support I found for low-cost designs.
- **WHO GDG would require mortality for adjunctive HDT:** UNVERIFIABLE (I did not retrieve WHO GDG requirements). It is overstated as stated, since WHO can consider other patient-important outcomes. The critique's logic is still valid if the CEA's benefit is mortality-only: whatever evidence supports p_success has to support a mortality effect.
- **SROI arithmetic:** 3,000 × 7/37 ≈ 568, which is correct. The 3–10× reduction is consistent (3,000 → ~1,000 to ~300). One ambiguity: the hypothesis calls the $7M a "Phase III" cost, but the SROI formula uses 7 as the base all-in cost. I cannot check this against the CG source model.
- **The 3,000× baseline SROI, the 3.3M-patient base and the 25% materiality bar:** UNVERIFIABLE from my materials (CG model details).
- **"Enriching for high-mortality groups shrinks N but loses generalisability":** logically sound. Absolute risk differences matter more than relative ones here.

**EVIDENCE FOUND (additional)**

- The pragmatic cost literature suggests the cost range should include a lower bound near $5M for a very lean design. The critique's central estimate of $25–40M therefore depends on assuming TB-trial costs of several hundred dollars or more per participant.
- 
No clear consensus exists on appropriate endpoints for HDT trials.
 This supports the open question about what evidence would be needed.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The sample-size core is solid and the cost estimate is plausible but uncertain.

**REVISED CRITIQUE**

- **Verified:**
  - A mortality-powered Phase III of a 10% relative reduction needs about 17,000–28,000 per arm (about 34,000–57,000 total) at 8% and 5% baseline mortality.
  - A $7M budget is very unlikely to fund that at conventional TB-trial per-patient costs.
  - If the $7M funds a surrogate-endpoint trial, the mortality benefit in the CEA is not supported by the evidence that trial would produce.
  - CG's cost and p_success are in tension.
- **Revised:**
  - Per-participant cost is UNGROUNDED but has a wide range. It runs from about $100 (embedded trials) to tens of thousands of dollars (TB-PRACTECAL).
  - Phase III cost is better stated as roughly $5M–$100M+, with a central case of about $20–40M if sites are LMIC pragmatic TB sites.
  - The 3–10× SROI reduction holds at the central case. It narrows toward about 1× if an ultra-lean embedded design is feasible.
  - The RECOVERY comparison and the WHO GDG endpoint claim stay flagged as unverified.
- **Direction:** decreases. **Magnitude:** large, with a wider uncertainty band than stated.

--- Critique: Hepatotoxicity and myopathy add a negative tail, and the combined attenuations compound ---

## Critique 1: Winner's curse and reference-class patterns

**CLAIM CHECK**

- **Martineau 2011 vitamin D trial, culture-conversion signal in a genotype subgroup:** VERIFIED, but the framing needs correcting.
  - 
Median time to sputum culture conversion was 36.0 days with vitamin D and 43.5 days with placebo (adjusted HR 1.39, 95% CI 0.90–2.16, p=0.14).
 The primary endpoint was therefore null.
  - 
TaqI genotype modified the effect (p-interaction 0.03), with a response only in tt-genotype patients (HR 8.09, 95% CI 1.36–48.01).
 The tt subgroup estimate is very wide and imprecise, which is a textbook winner's-curse profile.
  - This was a post-hoc subgroup signal, not a Phase II trial that "passed" a filter.
- **No robust later benefit:** VERIFIED. 
A meta-analysis found no shortening of time to sputum culture conversion overall (HR 1.04, 0.89–1.23).
 A later trial also 
found that the tt genotype did not influence conversion, in contrast with the earlier report.
 The subgroup effect was not replicated in that trial.
- **CC-11050 and everolimus "surrogate positives that fail to translate":** MISREPRESENTED.
  - The relevant trial is Wallis et al. 2021, a phase 2 trial in South Africa (NCT02968927).
  - 
It found both drugs safe and well tolerated, and they might have improved FEV1 recovery.
 
FEV1 was significantly higher than control at day 180 (CC-11050 6.30%, p=0.048; everolimus 6.56%, p=0.044).

  - 
There was no effect of CC-11050 on stable culture conversion, which the authors attributed to small sample size.

  - 
The authors called for further definitive studies.
 I found no Phase III, so these drugs have not "failed to translate". They are untested at Phase III.
  - Safety and FEV1 were the endpoints, not mortality.
- **Metformin "mixed or no clear clinical benefit":** NOT SUPPORTED as stated.
  - What exists is mostly observational or preclinical work. 
A scoping review describes pilot preclinical and observational research recommending metformin as an adjunct.

  - 
The impact of combining metformin with RHZE is described as still under investigation.

  - Metformin is therefore unproven, not a documented translation failure. I found no completed outcome RCT in these results.
- **Observational statin cohorts exposed to healthy-user and indication bias:** PLAUSIBLE (logical argument).
  - 
Population-based studies found statin use related to lower TB incidence.

  - I did not locate the specific Taiwan or Korea statin cohorts, so I could not verify them. A comparable Taiwan metformin cohort did find an association with lower TB risk. 
The HR was 0.84 (0.74–0.96).

- **Winner's curse as a general statistical result:** VERIFIED as standard theory (no search needed).
- **Joint-distribution claim, "E[r × p_success] below the product of means":** LOGICALLY CONDITIONAL.
  - The sign of the covariance depends on how p_success is defined.
  - If success is defined on a surrogate and surrogate-only wins exist, high p_success pairs with r≈0. That gives a negative covariance, so E[rp] is below E[r]E[p], as the critique says.
  - If p_success means success on a mortality-powered endpoint, real-effect worlds have both high p and high r. That gives a positive covariance and the effect reverses.
  - I could not inspect the CG model to see which applies.
- **Shrinkage arithmetic:** the 0.7–0.9 factor is explicitly an assumption, and 0.10 × 0.7–0.9 = 0.07–0.09 is arithmetically correct.

**EVIDENCE FOUND (additional)**

- The directly relevant statin reference class contradicts the "early positive signal" premise. Human surrogate data for statins in TB are null so far.
  - 
Rosuvastatin phase 2b: median time to culture conversion was 42 days in both arms (HR 1.30, 0.88–1.91, p=0.19).

  - 
Rosuvastatin had no impact on PET-CT changes.

  - 
StAT-TB (pravastatin, phase 2b) is registered as completed.
 I found no results in this search.
  - Atorvastatin evidence in these results is preclinical. 
In guinea pigs, atorvastatin and anti-TB drugs showed a synergistic bactericidal action.

- So the 10% likely rests on preclinical and observational anchoring, not a winner's-curse-selected human trial. That is a different mechanism (translation risk and confounding) and arguably points to a larger downward adjustment than shrinkage alone.
- 
An editorial notes there is no clear consensus on appropriate biomarkers or study endpoints for HDT trials.
 This supports the surrogate-to-outcome concern in general terms.

**OVERALL VERDICT: PARTIALLY VERIFIED.**

**REVISED CRITIQUE**

- **Survives:** The 10% conditional effect is probably over-optimistic.
  - Early or subgroup estimates are upwardly biased.
  - Martineau 2011 is a valid example, but of a post-hoc subgroup signal that did not replicate.
  - Observational statin data are confounded.
  - r and p_success are unlikely to be independent, though the sign of the effect on E[rp] depends on how success is defined.
- **Removed:** The claims that CC-11050, everolimus and metformin are failed-translation examples. They are unproven, not refuted.
- **Added:** Human statin-in-TB surrogate trials (rosuvastatin) are null. None of them used atorvastatin.
- **Status:** The shrinkage factor is UNGROUNDED, an illustrative assumption. Direction: decreases. Magnitude: medium.

---

## Critique 2: Hepatotoxicity, myopathy, and compounding

**CLAIM CHECK**

- **HRZ hepatotoxicity and statin liver/muscle warnings are well established:** PLAUSIBLE from standard labeling and general knowledge. I did not retrieve labels in this session.
  - Supportive data point: in the Wallis HDT trial, 
two control-group patients had life-threatening, treatment-attributable liver injury
 on standard therapy.
- **Small phase II trials cannot detect excess mortality from hepatotoxicity:** PLAUSIBLE (statistical).
  - The rosuvastatin trial is a data point. 
Grade 3–5 adverse events occurred in 9% (6/70) with rosuvastatin versus 6% (4/67) in controls (p=0.75), none considered related to rosuvastatin.

  - There was no signal, but the trial is too small to exclude a rare harm. Rosuvastatin also has less CYP3A4 involvement than atorvastatin, so it does not transfer directly.
- **Myopathy risk higher with "some ART":** PLAUSIBLE but of limited relevance.
  - From my own knowledge (not searched here), the main statin interaction is with boosted protease inhibitors and cobicistat. Those are generally avoided with rifampicin, and efavirenz or dolutegravir regimens are the usual choice.
  - The ART argument is therefore weaker for rifampicin-based TB treatment.
- **"CG models only a non-negative effect":** UNVERIFIABLE. The CG model is not available to me.
- **−0.01 contribution:** arithmetic is correct (10% × 0.10 = 0.01).
  - A "net-zero" outcome is already what a failed Phase III in p_success represents. Counting it again as a harm tail risks double-counting.
  - Only the genuinely negative portion is incremental.
- **Compounding product:** arithmetic VERIFIED. 0.65×0.5×0.7 = 0.23 and 0.75×0.8×0.9 = 0.54, so r ≈ 0.023–0.054. The inputs come from other critiques that I cannot see. The Investigator itself flags that the factors overlap and are correlated.
- **PK attenuation (0.5–0.8):** this concerns rifampicin induction of atorvastatin metabolism.
  - I did not search this specifically. I know from general pharmacology that rifampicin lowers atorvastatin exposure, but I did not verify the magnitude here.
  - Supportive indirect evidence: the Wallis trial 
substituted rifabutin for rifampin because of potentially deleterious pharmacokinetic interactions with the HDT drugs.
 The StAT-TB protocol 
cites known pravastatin–rifampin interactions in humans.

  - Interaction-driven dosing problems are a recognized concern in this field.

**EVIDENCE FOUND (additional)**

- StAT-TB chose pravastatin partly for lower toxicity. 
Pravastatin showed the least toxicity in THP-1 and Vero cells.
 The programme's own choice of statin was driven by interaction and toxicity concerns.
- The rosuvastatin trial's safety result is mildly reassuring but underpowered for mortality.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The hypothesis is sound but largely ungrounded on magnitude, and the compounding is an upper bound.

**REVISED CRITIQUE**

- **Survives:** A harm tail for hepatotoxicity or myopathy is plausible and not testable in small trials. Adding hepatotoxic risk on top of HRZ is biologically coherent. Compounding of attenuations is a reasonable concern.
- **Corrections:**
  - The harm-tail adjustment is small (≈ −0.01 at most) and may double-count p_success.
  - The ART-myopathy point is weak for rifampicin-based regimens.
  - The 0.023–0.054 range is an upper-bound illustration. It uses correlated inputs from other critiques that could not be checked.
- **Flag:** "UNGROUNDED – plausible but needs empirical support" on magnitude. Direction: decreases. Magnitude: small for the harm tail itself, medium for the compounding.

---

## Critique 3: A $7M Phase III cannot be powered on mortality

**CLAIM CHECK**

I recomputed the sample sizes with the standard two-proportion formula, α=0.05 two-sided, 80% power (z-sum² = 7.849).

- **5.0% → 4.5% mortality:** VERIFIED. n per arm = 7.849 × (0.0475 + 0.042975) / 0.000025 ≈ 28,400, so about 56,800 in total. The critique says about 28,000 per arm and 57,000 in total.
- **8.0% → 7.2% mortality:** VERIFIED. n per arm = 7.849 × (0.0736 + 0.066816) / 0.000064 ≈ 17,200, so about 34,400 in total. The critique says about 17,000 per arm and 35,000 in total.
- **Cost at $500–$1,000 per participant:** arithmetic is roughly right. The two scenarios give about $17M–$57M across the two enrolment sizes (35,000 and 57,000), so the quoted range is correct as a union.
- **Cost-per-participant realism:** PARTIALLY SUPPORTED. The range is too narrow at the low end and too low for TB specifically.
  - Embedded pragmatic trials have cost far less. 
Across 64 such trials, mean cost per patient randomized was $478 and median $97 (2015 dollars).
 
Ten trials cost over $1,000 per patient.

  - At the $97 median, 35,000–57,000 patients would cost only about $3.4M–$5.5M, which would fit inside $7M. These are mostly EHR- or registry-embedded trials in high-income settings, not 6-month TB trials with clinical follow-up in LMICs.
  - At the other extreme, 
TB-PRACTECAL cost €33.9M in total, an average of €61,460 per patient.
 That is an MDR-TB trial with hospital-based visits, but it shows TB-trial costs can be orders of magnitude above $1,000.
  - 
Standard trials are typically estimated at $2,000–$40,000 per subject.

  - So the true cost range is wide, and "$500–$1,000" is a central pragmatic guess, not a verified figure.
- **RECOVERY showed very low per-patient costs:** UNVERIFIED. I did not find a RECOVERY per-patient cost in my search. The embedded-trial review is the best support I found for low-cost designs.
- **WHO GDG would require mortality for adjunctive HDT:** UNVERIFIABLE (I did not retrieve WHO GDG requirements). It is overstated as stated, since WHO can consider other patient-important outcomes. The critique's logic is still valid if the CEA's benefit is mortality-only: whatever evidence supports p_success has to support a mortality effect.
- **SROI arithmetic:** 3,000 × 7/37 ≈ 568, which is correct. The 3–10× reduction is consistent (3,000 → ~1,000 to ~300). One ambiguity: the hypothesis calls the $7M a "Phase III" cost, but the SROI formula uses 7 as the base all-in cost. I cannot check this against the CG source model.
- **The 3,000× baseline SROI, the 3.3M-patient base and the 25% materiality bar:** UNVERIFIABLE from my materials (CG model details).
- **"Enriching for high-mortality groups shrinks N but loses generalisability":** logically sound. Absolute risk differences matter more than relative ones here.

**EVIDENCE FOUND (additional)**

- The pragmatic cost literature suggests the cost range should include a lower bound near $5M for a very lean design. The critique's central estimate of $25–40M therefore depends on assuming TB-trial costs of several hundred dollars or more per participant.
- 
No clear consensus exists on appropriate endpoints for HDT trials.
 This supports the open question about what evidence would be needed.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The sample-size core is solid and the cost estimate is plausible but uncertain.

**REVISED CRITIQUE**

- **Verified:**
  - A mortality-powered Phase III of a 10% relative reduction needs about 17,000–28,000 per arm (about 34,000–57,000 total) at 8% and 5% baseline mortality.
  - A $7M budget is very unlikely to fund that at conventional TB-trial per-patient costs.
  - If the $7M funds a surrogate-endpoint trial, the mortality benefit in the CEA is not supported by the evidence that trial would produce.
  - CG's cost and p_success are in tension.
- **Revised:**
  - Per-participant cost is UNGROUNDED but has a wide range. It runs from about $100 (embedded trials) to tens of thousands of dollars (TB-PRACTECAL).
  - Phase III cost is better stated as roughly $5M–$100M+, with a central case of about $20–40M if sites are LMIC pragmatic TB sites.
  - The 3–10× SROI reduction holds at the central case. It narrows toward about 1× if an ultra-lean embedded design is feasible.
  - The RECOVERY comparison and the WHO GDG endpoint claim stay flagged as unverified.
- **Direction:** decreases. **Magnitude:** large, with a wider uncertainty band than stated.

--- Critique: A $7M Phase III cannot be powered on mortality, and the CEA's benefit is mortality only ---

## Critique 1: Winner's curse and reference-class patterns

**CLAIM CHECK**

- **Martineau 2011 vitamin D trial, culture-conversion signal in a genotype subgroup:** VERIFIED, but the framing needs correcting.
  - 
Median time to sputum culture conversion was 36.0 days with vitamin D and 43.5 days with placebo (adjusted HR 1.39, 95% CI 0.90–2.16, p=0.14).
 The primary endpoint was therefore null.
  - 
TaqI genotype modified the effect (p-interaction 0.03), with a response only in tt-genotype patients (HR 8.09, 95% CI 1.36–48.01).
 The tt subgroup estimate is very wide and imprecise, which is a textbook winner's-curse profile.
  - This was a post-hoc subgroup signal, not a Phase II trial that "passed" a filter.
- **No robust later benefit:** VERIFIED. 
A meta-analysis found no shortening of time to sputum culture conversion overall (HR 1.04, 0.89–1.23).
 A later trial also 
found that the tt genotype did not influence conversion, in contrast with the earlier report.
 The subgroup effect was not replicated in that trial.
- **CC-11050 and everolimus "surrogate positives that fail to translate":** MISREPRESENTED.
  - The relevant trial is Wallis et al. 2021, a phase 2 trial in South Africa (NCT02968927).
  - 
It found both drugs safe and well tolerated, and they might have improved FEV1 recovery.
 
FEV1 was significantly higher than control at day 180 (CC-11050 6.30%, p=0.048; everolimus 6.56%, p=0.044).

  - 
There was no effect of CC-11050 on stable culture conversion, which the authors attributed to small sample size.

  - 
The authors called for further definitive studies.
 I found no Phase III, so these drugs have not "failed to translate". They are untested at Phase III.
  - Safety and FEV1 were the endpoints, not mortality.
- **Metformin "mixed or no clear clinical benefit":** NOT SUPPORTED as stated.
  - What exists is mostly observational or preclinical work. 
A scoping review describes pilot preclinical and observational research recommending metformin as an adjunct.

  - 
The impact of combining metformin with RHZE is described as still under investigation.

  - Metformin is therefore unproven, not a documented translation failure. I found no completed outcome RCT in these results.
- **Observational statin cohorts exposed to healthy-user and indication bias:** PLAUSIBLE (logical argument).
  - 
Population-based studies found statin use related to lower TB incidence.

  - I did not locate the specific Taiwan or Korea statin cohorts, so I could not verify them. A comparable Taiwan metformin cohort did find an association with lower TB risk. 
The HR was 0.84 (0.74–0.96).

- **Winner's curse as a general statistical result:** VERIFIED as standard theory (no search needed).
- **Joint-distribution claim, "E[r × p_success] below the product of means":** LOGICALLY CONDITIONAL.
  - The sign of the covariance depends on how p_success is defined.
  - If success is defined on a surrogate and surrogate-only wins exist, high p_success pairs with r≈0. That gives a negative covariance, so E[rp] is below E[r]E[p], as the critique says.
  - If p_success means success on a mortality-powered endpoint, real-effect worlds have both high p and high r. That gives a positive covariance and the effect reverses.
  - I could not inspect the CG model to see which applies.
- **Shrinkage arithmetic:** the 0.7–0.9 factor is explicitly an assumption, and 0.10 × 0.7–0.9 = 0.07–0.09 is arithmetically correct.

**EVIDENCE FOUND (additional)**

- The directly relevant statin reference class contradicts the "early positive signal" premise. Human surrogate data for statins in TB are null so far.
  - 
Rosuvastatin phase 2b: median time to culture conversion was 42 days in both arms (HR 1.30, 0.88–1.91, p=0.19).

  - 
Rosuvastatin had no impact on PET-CT changes.

  - 
StAT-TB (pravastatin, phase 2b) is registered as completed.
 I found no results in this search.
  - Atorvastatin evidence in these results is preclinical. 
In guinea pigs, atorvastatin and anti-TB drugs showed a synergistic bactericidal action.

- So the 10% likely rests on preclinical and observational anchoring, not a winner's-curse-selected human trial. That is a different mechanism (translation risk and confounding) and arguably points to a larger downward adjustment than shrinkage alone.
- 
An editorial notes there is no clear consensus on appropriate biomarkers or study endpoints for HDT trials.
 This supports the surrogate-to-outcome concern in general terms.

**OVERALL VERDICT: PARTIALLY VERIFIED.**

**REVISED CRITIQUE**

- **Survives:** The 10% conditional effect is probably over-optimistic.
  - Early or subgroup estimates are upwardly biased.
  - Martineau 2011 is a valid example, but of a post-hoc subgroup signal that did not replicate.
  - Observational statin data are confounded.
  - r and p_success are unlikely to be independent, though the sign of the effect on E[rp] depends on how success is defined.
- **Removed:** The claims that CC-11050, everolimus and metformin are failed-translation examples. They are unproven, not refuted.
- **Added:** Human statin-in-TB surrogate trials (rosuvastatin) are null. None of them used atorvastatin.
- **Status:** The shrinkage factor is UNGROUNDED, an illustrative assumption. Direction: decreases. Magnitude: medium.

---

## Critique 2: Hepatotoxicity, myopathy, and compounding

**CLAIM CHECK**

- **HRZ hepatotoxicity and statin liver/muscle warnings are well established:** PLAUSIBLE from standard labeling and general knowledge. I did not retrieve labels in this session.
  - Supportive data point: in the Wallis HDT trial, 
two control-group patients had life-threatening, treatment-attributable liver injury
 on standard therapy.
- **Small phase II trials cannot detect excess mortality from hepatotoxicity:** PLAUSIBLE (statistical).
  - The rosuvastatin trial is a data point. 
Grade 3–5 adverse events occurred in 9% (6/70) with rosuvastatin versus 6% (4/67) in controls (p=0.75), none considered related to rosuvastatin.

  - There was no signal, but the trial is too small to exclude a rare harm. Rosuvastatin also has less CYP3A4 involvement than atorvastatin, so it does not transfer directly.
- **Myopathy risk higher with "some ART":** PLAUSIBLE but of limited relevance.
  - From my own knowledge (not searched here), the main statin interaction is with boosted protease inhibitors and cobicistat. Those are generally avoided with rifampicin, and efavirenz or dolutegravir regimens are the usual choice.
  - The ART argument is therefore weaker for rifampicin-based TB treatment.
- **"CG models only a non-negative effect":** UNVERIFIABLE. The CG model is not available to me.
- **−0.01 contribution:** arithmetic is correct (10% × 0.10 = 0.01).
  - A "net-zero" outcome is already what a failed Phase III in p_success represents. Counting it again as a harm tail risks double-counting.
  - Only the genuinely negative portion is incremental.
- **Compounding product:** arithmetic VERIFIED. 0.65×0.5×0.7 = 0.23 and 0.75×0.8×0.9 = 0.54, so r ≈ 0.023–0.054. The inputs come from other critiques that I cannot see. The Investigator itself flags that the factors overlap and are correlated.
- **PK attenuation (0.5–0.8):** this concerns rifampicin induction of atorvastatin metabolism.
  - I did not search this specifically. I know from general pharmacology that rifampicin lowers atorvastatin exposure, but I did not verify the magnitude here.
  - Supportive indirect evidence: the Wallis trial 
substituted rifabutin for rifampin because of potentially deleterious pharmacokinetic interactions with the HDT drugs.
 The StAT-TB protocol 
cites known pravastatin–rifampin interactions in humans.

  - Interaction-driven dosing problems are a recognized concern in this field.

**EVIDENCE FOUND (additional)**

- StAT-TB chose pravastatin partly for lower toxicity. 
Pravastatin showed the least toxicity in THP-1 and Vero cells.
 The programme's own choice of statin was driven by interaction and toxicity concerns.
- The rosuvastatin trial's safety result is mildly reassuring but underpowered for mortality.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The hypothesis is sound but largely ungrounded on magnitude, and the compounding is an upper bound.

**REVISED CRITIQUE**

- **Survives:** A harm tail for hepatotoxicity or myopathy is plausible and not testable in small trials. Adding hepatotoxic risk on top of HRZ is biologically coherent. Compounding of attenuations is a reasonable concern.
- **Corrections:**
  - The harm-tail adjustment is small (≈ −0.01 at most) and may double-count p_success.
  - The ART-myopathy point is weak for rifampicin-based regimens.
  - The 0.023–0.054 range is an upper-bound illustration. It uses correlated inputs from other critiques that could not be checked.
- **Flag:** "UNGROUNDED – plausible but needs empirical support" on magnitude. Direction: decreases. Magnitude: small for the harm tail itself, medium for the compounding.

---

## Critique 3: A $7M Phase III cannot be powered on mortality

**CLAIM CHECK**

I recomputed the sample sizes with the standard two-proportion formula, α=0.05 two-sided, 80% power (z-sum² = 7.849).

- **5.0% → 4.5% mortality:** VERIFIED. n per arm = 7.849 × (0.0475 + 0.042975) / 0.000025 ≈ 28,400, so about 56,800 in total. The critique says about 28,000 per arm and 57,000 in total.
- **8.0% → 7.2% mortality:** VERIFIED. n per arm = 7.849 × (0.0736 + 0.066816) / 0.000064 ≈ 17,200, so about 34,400 in total. The critique says about 17,000 per arm and 35,000 in total.
- **Cost at $500–$1,000 per participant:** arithmetic is roughly right. The two scenarios give about $17M–$57M across the two enrolment sizes (35,000 and 57,000), so the quoted range is correct as a union.
- **Cost-per-participant realism:** PARTIALLY SUPPORTED. The range is too narrow at the low end and too low for TB specifically.
  - Embedded pragmatic trials have cost far less. 
Across 64 such trials, mean cost per patient randomized was $478 and median $97 (2015 dollars).
 
Ten trials cost over $1,000 per patient.

  - At the $97 median, 35,000–57,000 patients would cost only about $3.4M–$5.5M, which would fit inside $7M. These are mostly EHR- or registry-embedded trials in high-income settings, not 6-month TB trials with clinical follow-up in LMICs.
  - At the other extreme, 
TB-PRACTECAL cost €33.9M in total, an average of €61,460 per patient.
 That is an MDR-TB trial with hospital-based visits, but it shows TB-trial costs can be orders of magnitude above $1,000.
  - 
Standard trials are typically estimated at $2,000–$40,000 per subject.

  - So the true cost range is wide, and "$500–$1,000" is a central pragmatic guess, not a verified figure.
- **RECOVERY showed very low per-patient costs:** UNVERIFIED. I did not find a RECOVERY per-patient cost in my search. The embedded-trial review is the best support I found for low-cost designs.
- **WHO GDG would require mortality for adjunctive HDT:** UNVERIFIABLE (I did not retrieve WHO GDG requirements). It is overstated as stated, since WHO can consider other patient-important outcomes. The critique's logic is still valid if the CEA's benefit is mortality-only: whatever evidence supports p_success has to support a mortality effect.
- **SROI arithmetic:** 3,000 × 7/37 ≈ 568, which is correct. The 3–10× reduction is consistent (3,000 → ~1,000 to ~300). One ambiguity: the hypothesis calls the $7M a "Phase III" cost, but the SROI formula uses 7 as the base all-in cost. I cannot check this against the CG source model.
- **The 3,000× baseline SROI, the 3.3M-patient base and the 25% materiality bar:** UNVERIFIABLE from my materials (CG model details).
- **"Enriching for high-mortality groups shrinks N but loses generalisability":** logically sound. Absolute risk differences matter more than relative ones here.

**EVIDENCE FOUND (additional)**

- The pragmatic cost literature suggests the cost range should include a lower bound near $5M for a very lean design. The critique's central estimate of $25–40M therefore depends on assuming TB-trial costs of several hundred dollars or more per participant.
- 
No clear consensus exists on appropriate endpoints for HDT trials.
 This supports the open question about what evidence would be needed.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The sample-size core is solid and the cost estimate is plausible but uncertain.

**REVISED CRITIQUE**

- **Verified:**
  - A mortality-powered Phase III of a 10% relative reduction needs about 17,000–28,000 per arm (about 34,000–57,000 total) at 8% and 5% baseline mortality.
  - A $7M budget is very unlikely to fund that at conventional TB-trial per-patient costs.
  - If the $7M funds a surrogate-endpoint trial, the mortality benefit in the CEA is not supported by the evidence that trial would produce.
  - CG's cost and p_success are in tension.
- **Revised:**
  - Per-participant cost is UNGROUNDED but has a wide range. It runs from about $100 (embedded trials) to tens of thousands of dollars (TB-PRACTECAL).
  - Phase III cost is better stated as roughly $5M–$100M+, with a central case of about $20–40M if sites are LMIC pragmatic TB sites.
  - The 3–10× SROI reduction holds at the central case. It narrows toward about 1× if an ultra-lean embedded design is feasible.
  - The RECOVERY comparison and the WHO GDG endpoint claim stay flagged as unverified.
- **Direction:** decreases. **Magnitude:** large, with a wider uncertainty band than stated.

--- Critique: The all-in framing counts benefits for every treated patient but not the cost of treating them ---

## Critique 1: The all-in framing counts benefits for every treated patient but not the cost of treating them

**OVERALL VERDICT: PARTIALLY VERIFIED.** The logical-consistency argument is sound. The numbers are illustrative and unsourced, and the decisive input (how CG values third-party spending) is unverified.

**CLAIM CHECK**
- **Arithmetic: VERIFIED, with one small inconsistency.**
  - $3.7M ÷ 3.3M patients ≈ $1.12 per patient. 3,000 × 7/17 ≈ 1,235x. $1–10 × 3.3M = $3.3–33M.
  - The break-even is derived from the $10.7M threshold used in Critique 2. A flat 3,000x on $7M gives about $21B in benefits, and $21B ÷ 2,000 is $10.5M, not $10.7M. The difference is small, but the 3,000x figure is evidently rounded.
- **"About 3.3M patients in the credited year": UNVERIFIABLE.** I found no source for this number.
- **"Generic atorvastatin costs $1–10 per course": PLAUSIBLE, with caveats.**
  - The trial regimens are 16 weeks of 20, 40 or 60 mg daily, which is about 112 tablets. 
The ATORTUB sub-study arms are 20, 40 and 60 mg atorvastatin, each given for 16 weeks.

  - Canadian public-formulary prices are about $0.17–0.23 per tablet, which gives roughly $19–26 per course. 
One CADTH table lists 20 mg and 40 mg atorvastatin tablets at 0.1743 to 0.2342 per tablet for the generic strengths.
 Another CADTH table lists $0.39–0.42 per tablet. 
Daily drug cost there is $0.31–0.42.

  - UK generics were under £2 per 28-tablet pack. 
The generic 10, 20 and 40 mg doses are priced below £2 per pack.
 That is about £8 for 112 tablets.
  - Tender prices in LMICs would be lower than any of these. So $1–10 is plausible at tender prices and may be low at retail.
  - I could not retrieve the MSH International Drug Price Indicator Guide or the GDF catalog entries for atorvastatin. The MSH guide is a real source: 
it is published by Management Sciences for Health and provides medicine price information.

- **"CG values government and Global Fund money at 20–30% of face value": UNGROUNDED.** The Investigator flags this as an assumption. I found no CG or Open Philanthropy statement on how it values third-party spending.
- **Asymmetry claim (benefits counted, delivery cost not): UNVERIFIABLE.** I could not retrieve the CG SROI documentation. The claim depends on how CG defined "all-in" and on the $7M scope.

**EVIDENCE FOUND**
- The Phase IIC trial is real and Open Philanthropy-linked. 
The ClinicalTrials.gov record for NCT06199921 lists Open Philanthropy as a collaborator.

- Dosing matters for D. 
Phase IIC tests different atorvastatin doses in 440 patients.
 The cost of delivery therefore depends on which dose is eventually adopted.
- Monitoring costs are plausibly material. First-line TB drugs already carry liver-monitoring needs (see Critique 2).

**REVISED CRITIQUE**
Retain the hypothesis: if benefits are counted for all treated patients, then the cost of delivering the intervention to them, or an explicit convention for excluding it, belongs in the denominator.
- Drug procurement alone is likely in the low-to-tens of dollars per course (verified at retail and plausible at tender prices). This puts D anywhere from a few million dollars to tens of millions across 3.3M patients. The 3.3M figure is unverified.
- Flag the "counterfactual-value convention" point as UNGROUNDED but logically sound.
- Strength: medium to large, and conditional on CG's convention. The Investigator's "large" is defensible only if third-party funds are valued near face value.

---

## Critique 2: Regulatory, pharmacovigilance and dissemination costs for an off-patent drug have no obvious payer

**OVERALL VERDICT: PARTIALLY VERIFIED.** The pharmacological and incentive arguments hold. The cost magnitudes are admitted illustrations with no empirical basis.

**CLAIM CHECK**
- **Rifampicin, isoniazid and pyrazinamide are hepatotoxic: VERIFIED.**
  - 
First-line anti-TB drugs associated with hepatotoxicity include isoniazid, rifampicin and pyrazinamide, and their patterns of liver injury overlap.

  - 
Rifampicin enhances the hepatotoxicity of other antitubercular drugs.

- **Statins cause hepatotoxicity and myopathy: PLAUSIBLE.** This is well-established pharmacology, but I did not retrieve a source in this session. I also found no retrospective data on statin-plus-TB-drug liver injury. 
One review notes that no retrospective studies were found evaluating statins during TB treatment.

- **Overlap means safety monitoring is a real cost: PLAUSIBLE.** The trials treat this as a primary safety endpoint. 
The ATORTUB protocol measures treatment-emergent adverse events through lab abnormalities, ECGs and physical exams.

- **Existing safety signal is favourable, which cuts against the severity of the concern:**
  - 
ATORTUB Phase IIB found atorvastatin generally safe, with reduced peripheral neuropathy in that group.

  - 
Rosuvastatin was also safe in a separate trial but did not improve sputum culture conversion.

- **No sponsor has a commercial incentive: PLAUSIBLE, logical.** I found nothing contradicting it.
- **"A Phase IIc of $320k": UNVERIFIABLE.** The trial design is real, but I found no budget figure.
- **"$5–20M adds 70–300%": arithmetic VERIFIED** (71–286%). **"$4M add-on exceeds $10.7M": VERIFIED** ($11M).
- **"Adverse-event harms are not netted against the mortality benefit": UNVERIFIABLE.** I could not see the CG model.
- **Rollout costs for comparable TB regimen changes (Unitaid, Global Fund): not found in this session.**

**EVIDENCE FOUND**
- The Phase IIC is explicitly a stepping stone to a more expensive trial. 
The record says important questions need answering before a more expensive Phase III study.
 This supports the point that the $7M leaves little headroom, but it is not a budget figure.
- The efficacy evidence is mixed across statins. The rosuvastatin result above is relevant to benefit magnitude, which is outside this critique's cost scope.

**REVISED CRITIQUE**
- Keep: no natural payer exists for post-adoption pharmacovigilance and dissemination of a generic adjunct. The TB-drug hepatotoxicity overlap is real, so monitoring is a genuine cost item.
- Flag as UNGROUNDED: all dollar magnitudes ($5–20M, $4M, $320k).
- Add the countervailing evidence: early-phase safety data are favourable, so the cost of monitoring is likely a guideline-driven choice rather than a demonstrated necessity.
- Direction: uncertain, leaning up. Magnitude: medium, but wholly unquantified.

---

## Critique 3: Unclear scope boundary for the sweat-diagnostic workstream

**OVERALL VERDICT: PARTIALLY VERIFIED.** This is a legitimate clarification question rather than an established flaw, and the Investigator frames it that way. The search provided some grounding for it.

**CLAIM CHECK**
- **A sweat-diagnostic component exists alongside the statin work: VERIFIED in a related form.** 
The ATORTUB Phase IIA/B record lists an exploratory outcome, the diagnostic utility of a sweat TB test, measured by sensitivity, specificity, PPV and agreement.
 This shows the sweat test is run within the same trial infrastructure. That makes the shared-infrastructure and double-counting concerns real rather than hypothetical.
- **It is not clear whether the Phase IIC record includes the sweat test.** I did not confirm this.
- **Separate sweat-protein research exists.** 
A German study (SwEaTB, NCT03667742) collects sweat samples with the Macroduct system in patients with suspected TB.
 It is unrelated to the statin program, which shows "sweat diagnostic" can refer to different efforts. The Investigator's "if it is a separate program" branch is therefore live.
- **"Any budget above about $3.7M would breach 2,000x": arithmetic VERIFIED** (same $10.7M threshold). Note the internal tension with "magnitude small". A sweat test embedded as an exploratory outcome in a 150-patient trial would likely cost far less than $3.7M, which supports "small". But the Investigator's stated magnitude rests on an unknown budget.
- **Whether diagnostic-linked benefits are counted in the credited benefits: UNVERIFIABLE.** I could not see the CG model.

**EVIDENCE FOUND**
- The exploratory sweat-test outcome in ATORTUB is the main new evidence. It suggests the diagnostic is a low-cost add-on to the trial rather than a standalone large program. This favours "small magnitude" and weakens the "breaches threshold" scenario.
- Funding links: 
the Phase IIC record lists Open Philanthropy as a collaborator.


**REVISED CRITIQUE**
- Keep as a clarification question for CG. The diagnostic appears to have been an exploratory outcome inside the ATORTUB trial infrastructure, so cost sharing with the statin trials is plausible.
- Direction: uncertain, leaning toward no material effect. Magnitude: small. The scope boundary is still unconfirmed. This item should rank below Critiques 1 and 2 in priority.

--- Critique: Regulatory, pharmacovigilance and dissemination costs for an off-patent drug have no obvious payer, and the $7M likely under-budgets them ---

## Critique 1: The all-in framing counts benefits for every treated patient but not the cost of treating them

**OVERALL VERDICT: PARTIALLY VERIFIED.** The logical-consistency argument is sound. The numbers are illustrative and unsourced, and the decisive input (how CG values third-party spending) is unverified.

**CLAIM CHECK**
- **Arithmetic: VERIFIED, with one small inconsistency.**
  - $3.7M ÷ 3.3M patients ≈ $1.12 per patient. 3,000 × 7/17 ≈ 1,235x. $1–10 × 3.3M = $3.3–33M.
  - The break-even is derived from the $10.7M threshold used in Critique 2. A flat 3,000x on $7M gives about $21B in benefits, and $21B ÷ 2,000 is $10.5M, not $10.7M. The difference is small, but the 3,000x figure is evidently rounded.
- **"About 3.3M patients in the credited year": UNVERIFIABLE.** I found no source for this number.
- **"Generic atorvastatin costs $1–10 per course": PLAUSIBLE, with caveats.**
  - The trial regimens are 16 weeks of 20, 40 or 60 mg daily, which is about 112 tablets. 
The ATORTUB sub-study arms are 20, 40 and 60 mg atorvastatin, each given for 16 weeks.

  - Canadian public-formulary prices are about $0.17–0.23 per tablet, which gives roughly $19–26 per course. 
One CADTH table lists 20 mg and 40 mg atorvastatin tablets at 0.1743 to 0.2342 per tablet for the generic strengths.
 Another CADTH table lists $0.39–0.42 per tablet. 
Daily drug cost there is $0.31–0.42.

  - UK generics were under £2 per 28-tablet pack. 
The generic 10, 20 and 40 mg doses are priced below £2 per pack.
 That is about £8 for 112 tablets.
  - Tender prices in LMICs would be lower than any of these. So $1–10 is plausible at tender prices and may be low at retail.
  - I could not retrieve the MSH International Drug Price Indicator Guide or the GDF catalog entries for atorvastatin. The MSH guide is a real source: 
it is published by Management Sciences for Health and provides medicine price information.

- **"CG values government and Global Fund money at 20–30% of face value": UNGROUNDED.** The Investigator flags this as an assumption. I found no CG or Open Philanthropy statement on how it values third-party spending.
- **Asymmetry claim (benefits counted, delivery cost not): UNVERIFIABLE.** I could not retrieve the CG SROI documentation. The claim depends on how CG defined "all-in" and on the $7M scope.

**EVIDENCE FOUND**
- The Phase IIC trial is real and Open Philanthropy-linked. 
The ClinicalTrials.gov record for NCT06199921 lists Open Philanthropy as a collaborator.

- Dosing matters for D. 
Phase IIC tests different atorvastatin doses in 440 patients.
 The cost of delivery therefore depends on which dose is eventually adopted.
- Monitoring costs are plausibly material. First-line TB drugs already carry liver-monitoring needs (see Critique 2).

**REVISED CRITIQUE**
Retain the hypothesis: if benefits are counted for all treated patients, then the cost of delivering the intervention to them, or an explicit convention for excluding it, belongs in the denominator.
- Drug procurement alone is likely in the low-to-tens of dollars per course (verified at retail and plausible at tender prices). This puts D anywhere from a few million dollars to tens of millions across 3.3M patients. The 3.3M figure is unverified.
- Flag the "counterfactual-value convention" point as UNGROUNDED but logically sound.
- Strength: medium to large, and conditional on CG's convention. The Investigator's "large" is defensible only if third-party funds are valued near face value.

---

## Critique 2: Regulatory, pharmacovigilance and dissemination costs for an off-patent drug have no obvious payer

**OVERALL VERDICT: PARTIALLY VERIFIED.** The pharmacological and incentive arguments hold. The cost magnitudes are admitted illustrations with no empirical basis.

**CLAIM CHECK**
- **Rifampicin, isoniazid and pyrazinamide are hepatotoxic: VERIFIED.**
  - 
First-line anti-TB drugs associated with hepatotoxicity include isoniazid, rifampicin and pyrazinamide, and their patterns of liver injury overlap.

  - 
Rifampicin enhances the hepatotoxicity of other antitubercular drugs.

- **Statins cause hepatotoxicity and myopathy: PLAUSIBLE.** This is well-established pharmacology, but I did not retrieve a source in this session. I also found no retrospective data on statin-plus-TB-drug liver injury. 
One review notes that no retrospective studies were found evaluating statins during TB treatment.

- **Overlap means safety monitoring is a real cost: PLAUSIBLE.** The trials treat this as a primary safety endpoint. 
The ATORTUB protocol measures treatment-emergent adverse events through lab abnormalities, ECGs and physical exams.

- **Existing safety signal is favourable, which cuts against the severity of the concern:**
  - 
ATORTUB Phase IIB found atorvastatin generally safe, with reduced peripheral neuropathy in that group.

  - 
Rosuvastatin was also safe in a separate trial but did not improve sputum culture conversion.

- **No sponsor has a commercial incentive: PLAUSIBLE, logical.** I found nothing contradicting it.
- **"A Phase IIc of $320k": UNVERIFIABLE.** The trial design is real, but I found no budget figure.
- **"$5–20M adds 70–300%": arithmetic VERIFIED** (71–286%). **"$4M add-on exceeds $10.7M": VERIFIED** ($11M).
- **"Adverse-event harms are not netted against the mortality benefit": UNVERIFIABLE.** I could not see the CG model.
- **Rollout costs for comparable TB regimen changes (Unitaid, Global Fund): not found in this session.**

**EVIDENCE FOUND**
- The Phase IIC is explicitly a stepping stone to a more expensive trial. 
The record says important questions need answering before a more expensive Phase III study.
 This supports the point that the $7M leaves little headroom, but it is not a budget figure.
- The efficacy evidence is mixed across statins. The rosuvastatin result above is relevant to benefit magnitude, which is outside this critique's cost scope.

**REVISED CRITIQUE**
- Keep: no natural payer exists for post-adoption pharmacovigilance and dissemination of a generic adjunct. The TB-drug hepatotoxicity overlap is real, so monitoring is a genuine cost item.
- Flag as UNGROUNDED: all dollar magnitudes ($5–20M, $4M, $320k).
- Add the countervailing evidence: early-phase safety data are favourable, so the cost of monitoring is likely a guideline-driven choice rather than a demonstrated necessity.
- Direction: uncertain, leaning up. Magnitude: medium, but wholly unquantified.

---

## Critique 3: Unclear scope boundary for the sweat-diagnostic workstream

**OVERALL VERDICT: PARTIALLY VERIFIED.** This is a legitimate clarification question rather than an established flaw, and the Investigator frames it that way. The search provided some grounding for it.

**CLAIM CHECK**
- **A sweat-diagnostic component exists alongside the statin work: VERIFIED in a related form.** 
The ATORTUB Phase IIA/B record lists an exploratory outcome, the diagnostic utility of a sweat TB test, measured by sensitivity, specificity, PPV and agreement.
 This shows the sweat test is run within the same trial infrastructure. That makes the shared-infrastructure and double-counting concerns real rather than hypothetical.
- **It is not clear whether the Phase IIC record includes the sweat test.** I did not confirm this.
- **Separate sweat-protein research exists.** 
A German study (SwEaTB, NCT03667742) collects sweat samples with the Macroduct system in patients with suspected TB.
 It is unrelated to the statin program, which shows "sweat diagnostic" can refer to different efforts. The Investigator's "if it is a separate program" branch is therefore live.
- **"Any budget above about $3.7M would breach 2,000x": arithmetic VERIFIED** (same $10.7M threshold). Note the internal tension with "magnitude small". A sweat test embedded as an exploratory outcome in a 150-patient trial would likely cost far less than $3.7M, which supports "small". But the Investigator's stated magnitude rests on an unknown budget.
- **Whether diagnostic-linked benefits are counted in the credited benefits: UNVERIFIABLE.** I could not see the CG model.

**EVIDENCE FOUND**
- The exploratory sweat-test outcome in ATORTUB is the main new evidence. It suggests the diagnostic is a low-cost add-on to the trial rather than a standalone large program. This favours "small magnitude" and weakens the "breaches threshold" scenario.
- Funding links: 
the Phase IIC record lists Open Philanthropy as a collaborator.


**REVISED CRITIQUE**
- Keep as a clarification question for CG. The diagnostic appears to have been an exploratory outcome inside the ATORTUB trial infrastructure, so cost sharing with the statin trials is plausible.
- Direction: uncertain, leaning toward no material effect. Magnitude: small. The scope boundary is still unconfirmed. This item should rank below Critiques 1 and 2 in priority.

--- Critique: Unclear scope boundary for the sweat-diagnostic workstream ---

## Critique 1: The all-in framing counts benefits for every treated patient but not the cost of treating them

**OVERALL VERDICT: PARTIALLY VERIFIED.** The logical-consistency argument is sound. The numbers are illustrative and unsourced, and the decisive input (how CG values third-party spending) is unverified.

**CLAIM CHECK**
- **Arithmetic: VERIFIED, with one small inconsistency.**
  - $3.7M ÷ 3.3M patients ≈ $1.12 per patient. 3,000 × 7/17 ≈ 1,235x. $1–10 × 3.3M = $3.3–33M.
  - The break-even is derived from the $10.7M threshold used in Critique 2. A flat 3,000x on $7M gives about $21B in benefits, and $21B ÷ 2,000 is $10.5M, not $10.7M. The difference is small, but the 3,000x figure is evidently rounded.
- **"About 3.3M patients in the credited year": UNVERIFIABLE.** I found no source for this number.
- **"Generic atorvastatin costs $1–10 per course": PLAUSIBLE, with caveats.**
  - The trial regimens are 16 weeks of 20, 40 or 60 mg daily, which is about 112 tablets. 
The ATORTUB sub-study arms are 20, 40 and 60 mg atorvastatin, each given for 16 weeks.

  - Canadian public-formulary prices are about $0.17–0.23 per tablet, which gives roughly $19–26 per course. 
One CADTH table lists 20 mg and 40 mg atorvastatin tablets at 0.1743 to 0.2342 per tablet for the generic strengths.
 Another CADTH table lists $0.39–0.42 per tablet. 
Daily drug cost there is $0.31–0.42.

  - UK generics were under £2 per 28-tablet pack. 
The generic 10, 20 and 40 mg doses are priced below £2 per pack.
 That is about £8 for 112 tablets.
  - Tender prices in LMICs would be lower than any of these. So $1–10 is plausible at tender prices and may be low at retail.
  - I could not retrieve the MSH International Drug Price Indicator Guide or the GDF catalog entries for atorvastatin. The MSH guide is a real source: 
it is published by Management Sciences for Health and provides medicine price information.

- **"CG values government and Global Fund money at 20–30% of face value": UNGROUNDED.** The Investigator flags this as an assumption. I found no CG or Open Philanthropy statement on how it values third-party spending.
- **Asymmetry claim (benefits counted, delivery cost not): UNVERIFIABLE.** I could not retrieve the CG SROI documentation. The claim depends on how CG defined "all-in" and on the $7M scope.

**EVIDENCE FOUND**
- The Phase IIC trial is real and Open Philanthropy-linked. 
The ClinicalTrials.gov record for NCT06199921 lists Open Philanthropy as a collaborator.

- Dosing matters for D. 
Phase IIC tests different atorvastatin doses in 440 patients.
 The cost of delivery therefore depends on which dose is eventually adopted.
- Monitoring costs are plausibly material. First-line TB drugs already carry liver-monitoring needs (see Critique 2).

**REVISED CRITIQUE**
Retain the hypothesis: if benefits are counted for all treated patients, then the cost of delivering the intervention to them, or an explicit convention for excluding it, belongs in the denominator.
- Drug procurement alone is likely in the low-to-tens of dollars per course (verified at retail and plausible at tender prices). This puts D anywhere from a few million dollars to tens of millions across 3.3M patients. The 3.3M figure is unverified.
- Flag the "counterfactual-value convention" point as UNGROUNDED but logically sound.
- Strength: medium to large, and conditional on CG's convention. The Investigator's "large" is defensible only if third-party funds are valued near face value.

---

## Critique 2: Regulatory, pharmacovigilance and dissemination costs for an off-patent drug have no obvious payer

**OVERALL VERDICT: PARTIALLY VERIFIED.** The pharmacological and incentive arguments hold. The cost magnitudes are admitted illustrations with no empirical basis.

**CLAIM CHECK**
- **Rifampicin, isoniazid and pyrazinamide are hepatotoxic: VERIFIED.**
  - 
First-line anti-TB drugs associated with hepatotoxicity include isoniazid, rifampicin and pyrazinamide, and their patterns of liver injury overlap.

  - 
Rifampicin enhances the hepatotoxicity of other antitubercular drugs.

- **Statins cause hepatotoxicity and myopathy: PLAUSIBLE.** This is well-established pharmacology, but I did not retrieve a source in this session. I also found no retrospective data on statin-plus-TB-drug liver injury. 
One review notes that no retrospective studies were found evaluating statins during TB treatment.

- **Overlap means safety monitoring is a real cost: PLAUSIBLE.** The trials treat this as a primary safety endpoint. 
The ATORTUB protocol measures treatment-emergent adverse events through lab abnormalities, ECGs and physical exams.

- **Existing safety signal is favourable, which cuts against the severity of the concern:**
  - 
ATORTUB Phase IIB found atorvastatin generally safe, with reduced peripheral neuropathy in that group.

  - 
Rosuvastatin was also safe in a separate trial but did not improve sputum culture conversion.

- **No sponsor has a commercial incentive: PLAUSIBLE, logical.** I found nothing contradicting it.
- **"A Phase IIc of $320k": UNVERIFIABLE.** The trial design is real, but I found no budget figure.
- **"$5–20M adds 70–300%": arithmetic VERIFIED** (71–286%). **"$4M add-on exceeds $10.7M": VERIFIED** ($11M).
- **"Adverse-event harms are not netted against the mortality benefit": UNVERIFIABLE.** I could not see the CG model.
- **Rollout costs for comparable TB regimen changes (Unitaid, Global Fund): not found in this session.**

**EVIDENCE FOUND**
- The Phase IIC is explicitly a stepping stone to a more expensive trial. 
The record says important questions need answering before a more expensive Phase III study.
 This supports the point that the $7M leaves little headroom, but it is not a budget figure.
- The efficacy evidence is mixed across statins. The rosuvastatin result above is relevant to benefit magnitude, which is outside this critique's cost scope.

**REVISED CRITIQUE**
- Keep: no natural payer exists for post-adoption pharmacovigilance and dissemination of a generic adjunct. The TB-drug hepatotoxicity overlap is real, so monitoring is a genuine cost item.
- Flag as UNGROUNDED: all dollar magnitudes ($5–20M, $4M, $320k).
- Add the countervailing evidence: early-phase safety data are favourable, so the cost of monitoring is likely a guideline-driven choice rather than a demonstrated necessity.
- Direction: uncertain, leaning up. Magnitude: medium, but wholly unquantified.

---

## Critique 3: Unclear scope boundary for the sweat-diagnostic workstream

**OVERALL VERDICT: PARTIALLY VERIFIED.** This is a legitimate clarification question rather than an established flaw, and the Investigator frames it that way. The search provided some grounding for it.

**CLAIM CHECK**
- **A sweat-diagnostic component exists alongside the statin work: VERIFIED in a related form.** 
The ATORTUB Phase IIA/B record lists an exploratory outcome, the diagnostic utility of a sweat TB test, measured by sensitivity, specificity, PPV and agreement.
 This shows the sweat test is run within the same trial infrastructure. That makes the shared-infrastructure and double-counting concerns real rather than hypothetical.
- **It is not clear whether the Phase IIC record includes the sweat test.** I did not confirm this.
- **Separate sweat-protein research exists.** 
A German study (SwEaTB, NCT03667742) collects sweat samples with the Macroduct system in patients with suspected TB.
 It is unrelated to the statin program, which shows "sweat diagnostic" can refer to different efforts. The Investigator's "if it is a separate program" branch is therefore live.
- **"Any budget above about $3.7M would breach 2,000x": arithmetic VERIFIED** (same $10.7M threshold). Note the internal tension with "magnitude small". A sweat test embedded as an exploratory outcome in a 150-patient trial would likely cost far less than $3.7M, which supports "small". But the Investigator's stated magnitude rests on an unknown budget.
- **Whether diagnostic-linked benefits are counted in the credited benefits: UNVERIFIABLE.** I could not see the CG model.

**EVIDENCE FOUND**
- The exploratory sweat-test outcome in ATORTUB is the main new evidence. It suggests the diagnostic is a low-cost add-on to the trial rather than a standalone large program. This favours "small magnitude" and weakens the "breaches threshold" scenario.
- Funding links: 
the Phase IIC record lists Open Philanthropy as a collaborator.


**REVISED CRITIQUE**
- Keep as a clarification question for CG. The diagnostic appears to have been an exploratory outcome inside the ATORTUB trial infrastructure, so cost sharing with the statin trials is plausible.
- Direction: uncertain, leaning toward no material effect. Magnitude: small. The scope boundary is still unconfirmed. This item should rank below Critiques 1 and 2 in priority.

--- Critique: Reference-class check: TB Phase III trials, and the evidence package WHO may require, point to more than one trial ---

## Critique 1: TB Phase III reference class and WHO evidence package

**CLAIM CHECK**
- **"Phase III TB trials (Study 31/A5349, STREAM, endTB, TRUNCATE-TB, SimpliciTB) enrolled hundreds to thousands of participants": PLAUSIBLE, only partly verified.**
  - The trials are real. I confirmed that 
endTB is a Phase III, randomized, open-label, non-inferiority, multi-country trial of five shortened all-oral MDR-TB regimens
. I also confirmed that 
STREAM was a phase-III non-inferiority RCT.

  - The endTB launch statement said 
750 patients would take part in the clinical trial across six countries.

  - I did not retrieve enrollment figures for Study 31, TRUNCATE-TB or SimpliciTB, so those remain from memory. SimpliciTB may be registered as a Phase 2 or 2/3 trial rather than Phase III, so the label needs a check.
- **"Budgets were generally in the tens of millions of dollars": PLAUSIBLE, with partial support.**
  - TB-PRACTECAL was an MSF-sponsored phase 2b-3 trial. Its 
total cost was €33.9 million, an average of €61,460 per patient.

  - The same paper reports a literature range of 
US$7–221 million per trial for pharmaceutical phase 2 and 3 trials.

  - It also cites an 
average of US$23 million for anti-infective and respiratory phase 3 trials.

  - Outside TB, 
the median cost of a single phase III trial was $19 million
 in a JAMA IM analysis of 138 pivotal trials for FDA-approved drugs.
  - The endTB "US$60M" figure is not a trial budget. 
It is a four-year Unitaid project that also covers an estimated 2,600-patient treatment cohort.
 Do not use it as a single-trial cost.
  - I found no budgets for Study 31, STREAM or TRUNCATE-TB. Those would need NIH RePORTER, EDCTP and Unitaid lookups.
- **"WHO may require more than one trial or an IPD meta-analysis": UNVERIFIABLE.**
  - I found no WHO requirement of this kind. The WHO Global TB Report 2025 says its drug-resistant TB update drew on 
two clinical trials, BEAT-TB and endTB.
 That shows WHO sometimes relies on more than one trial. It is a drug-resistant TB example, and it does not show a requirement.
  - Subgroup evidence looks less likely to multiply costs for statins. A preprint notes 
pregnant women are unlikely to be on statins because of teratogenicity concerns.
 That suggests a pregnancy subgroup would probably be excluded, and the recommendation would likely carry a caveat instead. This is a weak source.
  - The StAT-TB protocol notes that 
statins and antiretrovirals can be co-administered with drug and dose selection.
 The HIV subgroup is therefore a real design question.
- **Arithmetic: VERIFIED.**
  - $20–60M divided by $7M is 2.9–8.6×.
  - $3,050 divided by 3–9 is about 340–1,020×.
  - $30M gives about 710×.

**EVIDENCE FOUND**
- The reference class is supported, but it mixes novel-drug registrational trials with different cost drivers. The TB-PRACTECAL paper says its cost 
included investment in trial infrastructure and medical expenditures not typical of standard clinical trials.
 A cheap oral adjunct with a routine-care endpoint could cost well below $20M. The Investigator's counterargument stands.
- Cost scales with per-patient cost and sample size. The review's lower bound of $7M overlaps the BOTEC figure. The $7M budget is therefore at the very bottom of the range and is not impossible.

**OVERALL VERDICT: PARTIALLY VERIFIED**

**REVISED CRITIQUE**
- Published cost data support a reference class of roughly $19–34M for a single Phase III trial, with a very wide range ($7–221M). Examples are the $19M Phase III median, $23M for anti-infective trials and €33.9M for TB-PRACTECAL.
- A $7M all-in budget sits at the low end of that range. It is not clearly implausible for a low-cost adjunct trial.
- The "multiple trials or IPD meta-analysis" requirement is UNGROUNDED. The pregnancy subgroup would probably be excluded for statins, so the multiplier is probably smaller than implied.
- Drop endTB's $60M as a trial cost.
- The 350–1,000× SROI range is correct arithmetic, but only if a $20–60M cost is accepted.
- Strength: medium, direction: uncertain, with a downward lean on SROI.

---

## Critique 2: Mismatched counterfactuals (speedup benefit vs. all-in cost)

**CLAIM CHECK**
- **Pure-delay algebra: VERIFIED as a derivation, with one caveat.**
  - If the whole program shifts by D years, benefits and costs both scale by e^(−rD). The net effect is (1−e^(−rD))·PV_B against (1−e^(−rD))·PV_C. The ratio is PV_B/PV_C, independent of D.
  - This is a standard result for pure time-shifts under a constant discount rate. It holds only if the benefit stream and cost stream shift by the same D. If the benefit lag is longer than the cost lag, the ratio changes.
- **"Never" and mixture branches: VERIFIED.** Both numerator and denominator scale by the same factor, so the ratio is PV_B/PV_C.
- **Numbers: VERIFIED as arithmetic, with one undocumented input.**
  - 1/0.06 ≈ 16.7. Multiplying by 0.6–0.7 gives about 10–11.7. Dividing by 0.85 gives about 12–13.8.
  - With r = 4% only, 25 × 0.6–0.7 ÷ 0.85 is about 17.6–20.6, so "about 18x" holds.
  - 3,050 × 12.5 ≈ 38,000 and 3,050 × 18 ≈ 55,000. The "30,000–55,000x" range is consistent.
  - The 0.6–0.7 delay factor is unexplained. It presumably reflects benefit onset after trial, WHO review and rollout. It should be stated explicitly because it drives the result.
- **"The BOTEC counts one year of plateau deaths averted and charges the full $7M": UNVERIFIABLE.** I do not have the CEA, so the diagnosis that the numerator and denominator come from different counterfactuals rests on the Investigator's reading.
- **Hybrid framing may be deliberate conservatism: UNGROUNDED, as the Investigator says.**
- **Displacement of other funders' money: a valid conceptual point.** The delay-branch ratio is PV_B/PV_C only if the other funders' dollars are valued at zero opportunity cost. The Investigator flags this but does not quantify it. If the displaced money would fund equally cost-effective research, the delay benefit shrinks toward zero and the 10–20× uplift would not hold.

**EVIDENCE FOUND**
- No external empirical evidence is needed for the core argument. I found nothing that contradicts it.
- The result is highly sensitive to the benefit horizon. The Investigator notes this but then states a 30,000–55,000× headline. That headline should be treated as an upper-bound illustration only.
- Real-world constraints on the horizon are visible in the statin evidence. ROSETTA found 
rosuvastatin 10 mg was safe but did not produce substantive benefits on culture conversion overall.
 Its PET-CT analysis showed 
no effect on microbiological or radiological outcomes.
 A 
phase IIA atorvastatin study showed a significant reduction in sputum mycobacterial load.
 Statin class and dose effects are uncertain, and p_success should be modest. The Investigator says p_success is included in PV_B, so this lowers the level but not the ratio logic.

**OVERALL VERDICT: PARTIALLY VERIFIED**

**REVISED CRITIQUE**
- Under a pure time-shift, "never", or a mixture of the two, the benefit-to-cost ratio is PV_B/PV_C. The BOTEC's "one year of benefit against full cost" is internally inconsistent if that is what the BOTEC does. That last point needs confirmation against the CEA.
- The uplift is plausibly about 10–20× under the stated horizon and discount assumptions. It depends heavily on the unexplained delay factor, the horizon, and treating other funders' dollars as free.
- Report the uplift as an illustrative range, not as "30,000–55,000×".
- Direction: the ratio rises, but displacement and horizon limits could pull it back down. Strength: large conceptually, medium once displacement is applied.

---

## Critique 3: Funding landscape and the "never" branch

**CLAIM CHECK**
- **"NIH and Johns Hopkins have published preclinical and early clinical work": VERIFIED.**
  - StAT-TB (NCT03882177) is a 
NIAID-sponsored Phase 2b dose-finding pravastatin study.
 It is 
completed.

  - The protocol lists 
Petros Karakousis of Johns Hopkins as US Principal Investigator.

  - It states the findings will 
inform dose selection for an anticipated larger follow-up study testing treatment-shortening potential.
 This supports the "dose-finding precedes Phase III" structure.
- **"Public-health funders have so far favored novel regimens and vaccines over host-directed therapies": UNVERIFIED, and partly contradicted.**
  - EDCTP funded StatinTB, a 
proof-of-concept Phase IIB placebo-controlled trial in Khayelitsha
 under grant RIA2017T-2004.
  - NIAID also funded it, through 
R01AI160501.

  - Wellcome has co-funded related work.
  - ROSETTA was a 
phase 2b trial run in the Philippines, Viet Nam and Uganda.
 I did not identify its funder.
  - Public funders have clearly supported Phase II statin-TB work. The open question is Phase III, where I found no funded trial.
- **"No commercial sponsor for generic statins": PLAUSIBLE.** The StAT-TB protocol itself says 
statins are attractive because of the widespread availability of less costly generics.
 That is the flip side of weak commercial incentive. I found no repurposing-literature source for the sponsor gap.
- **"Phase IIc" competitor: NOTABLE.**
  - ATORTUB has a registered 
Phase IIC selection trial with extended follow-up, designed as a pilot Phase III.
 (NCT06199921).
  - The ATORTUB group 
recently completed Phase IIA and IIB studies.

  - I cannot say whether this is the CG-funded trial. If the grant funds this trial, it is not a new gating step. If it funds a different trial, ATORTUB is an existing parallel pipeline, which lowers q. Check this first.
- **Expected speedup formula: VERIFIED.** q·H_eff + (1−q)·D with H_eff ≈ 10 and q = 0.1–0.2 gives about 1.9–3 years, assuming D ≈ 1.
- **"SROI roughly 20× higher": ARITHMETICALLY EXPLAINED, but conceptually weak.**
  - 7 ÷ 0.32 ≈ 22, so the 20× is just the ratio of the all-in cost to CG's own cost.
  - It credits CG with all benefits while charging only CG's $320k. If the counterfactual is "never", the other funders' $6.7M is a real cost that exists only because of the grant (see Critique 2). Under a delay counterfactual it is displaced spending.
  - Either way the 20× needs a justified attribution rule, such as a leverage or fractional-credit approach, before it can be reported.
- **Cross-reference error.** The text says the ratio is robust to q "(see Critique 1)", and uses H_eff from "my Critique 1 calculation". In this set that derivation is in Critique 2, not Critique 1. The finding also conflicts with the claim that SROI could be 20× higher: robustness to q means the all-in ratio does not change, so the uplift comes only from the change of cost basis.

**EVIDENCE FOUND**
- There is a real pipeline: StAT-TB (NIAID), StatinTB (EDCTP/NIAID), ROSETTA, and ATORTUB. A review noted 
four ongoing statin-TB clinical trials, calling statins one of the most promising HDT drugs in the pipeline.

- The ROSETTA null result reduces expected Phase III appetite for the whole class. That raises q for "never" for rosuvastatin-like approaches, and it reduces p_success.
- I did not search the TAG pipeline, Working Group on New TB Drugs, Unitaid portfolio, or NIH RePORTER directly. Those remain open.

**OVERALL VERDICT: PARTIALLY VERIFIED**

**REVISED CRITIQUE**
- Verified facts: the Phase II statin-TB landscape is populated by NIH, EDCTP and Wellcome-funded work; dose-finding explicitly precedes a larger follow-up trial; generics have no obvious commercial sponsor.
- The claim that funders disfavor HDT is UNGROUNDED, and Phase II funding evidence cuts against it. No Phase III statin-TB trial funder was found, so the "never" branch remains plausible but unquantified.
- A competing registered Phase IIC trial (ATORTUB) must be checked against the CG grant. If it is the same trial, the redundancy case in the critique's last sentence applies, not the leverage case.
- The "20× higher SROI" should be dropped or re-derived with an explicit attribution rule. Fix the cross-reference to Critique 2.
- Direction: uncertain rather than clearly up. Strength: medium.

--- Critique: The speedup benefit and the all-in cost come from different counterfactuals. Every coherent framing gives roughly 10–20x higher SROI. ---

## Critique 1: TB Phase III reference class and WHO evidence package

**CLAIM CHECK**
- **"Phase III TB trials (Study 31/A5349, STREAM, endTB, TRUNCATE-TB, SimpliciTB) enrolled hundreds to thousands of participants": PLAUSIBLE, only partly verified.**
  - The trials are real. I confirmed that 
endTB is a Phase III, randomized, open-label, non-inferiority, multi-country trial of five shortened all-oral MDR-TB regimens
. I also confirmed that 
STREAM was a phase-III non-inferiority RCT.

  - The endTB launch statement said 
750 patients would take part in the clinical trial across six countries.

  - I did not retrieve enrollment figures for Study 31, TRUNCATE-TB or SimpliciTB, so those remain from memory. SimpliciTB may be registered as a Phase 2 or 2/3 trial rather than Phase III, so the label needs a check.
- **"Budgets were generally in the tens of millions of dollars": PLAUSIBLE, with partial support.**
  - TB-PRACTECAL was an MSF-sponsored phase 2b-3 trial. Its 
total cost was €33.9 million, an average of €61,460 per patient.

  - The same paper reports a literature range of 
US$7–221 million per trial for pharmaceutical phase 2 and 3 trials.

  - It also cites an 
average of US$23 million for anti-infective and respiratory phase 3 trials.

  - Outside TB, 
the median cost of a single phase III trial was $19 million
 in a JAMA IM analysis of 138 pivotal trials for FDA-approved drugs.
  - The endTB "US$60M" figure is not a trial budget. 
It is a four-year Unitaid project that also covers an estimated 2,600-patient treatment cohort.
 Do not use it as a single-trial cost.
  - I found no budgets for Study 31, STREAM or TRUNCATE-TB. Those would need NIH RePORTER, EDCTP and Unitaid lookups.
- **"WHO may require more than one trial or an IPD meta-analysis": UNVERIFIABLE.**
  - I found no WHO requirement of this kind. The WHO Global TB Report 2025 says its drug-resistant TB update drew on 
two clinical trials, BEAT-TB and endTB.
 That shows WHO sometimes relies on more than one trial. It is a drug-resistant TB example, and it does not show a requirement.
  - Subgroup evidence looks less likely to multiply costs for statins. A preprint notes 
pregnant women are unlikely to be on statins because of teratogenicity concerns.
 That suggests a pregnancy subgroup would probably be excluded, and the recommendation would likely carry a caveat instead. This is a weak source.
  - The StAT-TB protocol notes that 
statins and antiretrovirals can be co-administered with drug and dose selection.
 The HIV subgroup is therefore a real design question.
- **Arithmetic: VERIFIED.**
  - $20–60M divided by $7M is 2.9–8.6×.
  - $3,050 divided by 3–9 is about 340–1,020×.
  - $30M gives about 710×.

**EVIDENCE FOUND**
- The reference class is supported, but it mixes novel-drug registrational trials with different cost drivers. The TB-PRACTECAL paper says its cost 
included investment in trial infrastructure and medical expenditures not typical of standard clinical trials.
 A cheap oral adjunct with a routine-care endpoint could cost well below $20M. The Investigator's counterargument stands.
- Cost scales with per-patient cost and sample size. The review's lower bound of $7M overlaps the BOTEC figure. The $7M budget is therefore at the very bottom of the range and is not impossible.

**OVERALL VERDICT: PARTIALLY VERIFIED**

**REVISED CRITIQUE**
- Published cost data support a reference class of roughly $19–34M for a single Phase III trial, with a very wide range ($7–221M). Examples are the $19M Phase III median, $23M for anti-infective trials and €33.9M for TB-PRACTECAL.
- A $7M all-in budget sits at the low end of that range. It is not clearly implausible for a low-cost adjunct trial.
- The "multiple trials or IPD meta-analysis" requirement is UNGROUNDED. The pregnancy subgroup would probably be excluded for statins, so the multiplier is probably smaller than implied.
- Drop endTB's $60M as a trial cost.
- The 350–1,000× SROI range is correct arithmetic, but only if a $20–60M cost is accepted.
- Strength: medium, direction: uncertain, with a downward lean on SROI.

---

## Critique 2: Mismatched counterfactuals (speedup benefit vs. all-in cost)

**CLAIM CHECK**
- **Pure-delay algebra: VERIFIED as a derivation, with one caveat.**
  - If the whole program shifts by D years, benefits and costs both scale by e^(−rD). The net effect is (1−e^(−rD))·PV_B against (1−e^(−rD))·PV_C. The ratio is PV_B/PV_C, independent of D.
  - This is a standard result for pure time-shifts under a constant discount rate. It holds only if the benefit stream and cost stream shift by the same D. If the benefit lag is longer than the cost lag, the ratio changes.
- **"Never" and mixture branches: VERIFIED.** Both numerator and denominator scale by the same factor, so the ratio is PV_B/PV_C.
- **Numbers: VERIFIED as arithmetic, with one undocumented input.**
  - 1/0.06 ≈ 16.7. Multiplying by 0.6–0.7 gives about 10–11.7. Dividing by 0.85 gives about 12–13.8.
  - With r = 4% only, 25 × 0.6–0.7 ÷ 0.85 is about 17.6–20.6, so "about 18x" holds.
  - 3,050 × 12.5 ≈ 38,000 and 3,050 × 18 ≈ 55,000. The "30,000–55,000x" range is consistent.
  - The 0.6–0.7 delay factor is unexplained. It presumably reflects benefit onset after trial, WHO review and rollout. It should be stated explicitly because it drives the result.
- **"The BOTEC counts one year of plateau deaths averted and charges the full $7M": UNVERIFIABLE.** I do not have the CEA, so the diagnosis that the numerator and denominator come from different counterfactuals rests on the Investigator's reading.
- **Hybrid framing may be deliberate conservatism: UNGROUNDED, as the Investigator says.**
- **Displacement of other funders' money: a valid conceptual point.** The delay-branch ratio is PV_B/PV_C only if the other funders' dollars are valued at zero opportunity cost. The Investigator flags this but does not quantify it. If the displaced money would fund equally cost-effective research, the delay benefit shrinks toward zero and the 10–20× uplift would not hold.

**EVIDENCE FOUND**
- No external empirical evidence is needed for the core argument. I found nothing that contradicts it.
- The result is highly sensitive to the benefit horizon. The Investigator notes this but then states a 30,000–55,000× headline. That headline should be treated as an upper-bound illustration only.
- Real-world constraints on the horizon are visible in the statin evidence. ROSETTA found 
rosuvastatin 10 mg was safe but did not produce substantive benefits on culture conversion overall.
 Its PET-CT analysis showed 
no effect on microbiological or radiological outcomes.
 A 
phase IIA atorvastatin study showed a significant reduction in sputum mycobacterial load.
 Statin class and dose effects are uncertain, and p_success should be modest. The Investigator says p_success is included in PV_B, so this lowers the level but not the ratio logic.

**OVERALL VERDICT: PARTIALLY VERIFIED**

**REVISED CRITIQUE**
- Under a pure time-shift, "never", or a mixture of the two, the benefit-to-cost ratio is PV_B/PV_C. The BOTEC's "one year of benefit against full cost" is internally inconsistent if that is what the BOTEC does. That last point needs confirmation against the CEA.
- The uplift is plausibly about 10–20× under the stated horizon and discount assumptions. It depends heavily on the unexplained delay factor, the horizon, and treating other funders' dollars as free.
- Report the uplift as an illustrative range, not as "30,000–55,000×".
- Direction: the ratio rises, but displacement and horizon limits could pull it back down. Strength: large conceptually, medium once displacement is applied.

---

## Critique 3: Funding landscape and the "never" branch

**CLAIM CHECK**
- **"NIH and Johns Hopkins have published preclinical and early clinical work": VERIFIED.**
  - StAT-TB (NCT03882177) is a 
NIAID-sponsored Phase 2b dose-finding pravastatin study.
 It is 
completed.

  - The protocol lists 
Petros Karakousis of Johns Hopkins as US Principal Investigator.

  - It states the findings will 
inform dose selection for an anticipated larger follow-up study testing treatment-shortening potential.
 This supports the "dose-finding precedes Phase III" structure.
- **"Public-health funders have so far favored novel regimens and vaccines over host-directed therapies": UNVERIFIED, and partly contradicted.**
  - EDCTP funded StatinTB, a 
proof-of-concept Phase IIB placebo-controlled trial in Khayelitsha
 under grant RIA2017T-2004.
  - NIAID also funded it, through 
R01AI160501.

  - Wellcome has co-funded related work.
  - ROSETTA was a 
phase 2b trial run in the Philippines, Viet Nam and Uganda.
 I did not identify its funder.
  - Public funders have clearly supported Phase II statin-TB work. The open question is Phase III, where I found no funded trial.
- **"No commercial sponsor for generic statins": PLAUSIBLE.** The StAT-TB protocol itself says 
statins are attractive because of the widespread availability of less costly generics.
 That is the flip side of weak commercial incentive. I found no repurposing-literature source for the sponsor gap.
- **"Phase IIc" competitor: NOTABLE.**
  - ATORTUB has a registered 
Phase IIC selection trial with extended follow-up, designed as a pilot Phase III.
 (NCT06199921).
  - The ATORTUB group 
recently completed Phase IIA and IIB studies.

  - I cannot say whether this is the CG-funded trial. If the grant funds this trial, it is not a new gating step. If it funds a different trial, ATORTUB is an existing parallel pipeline, which lowers q. Check this first.
- **Expected speedup formula: VERIFIED.** q·H_eff + (1−q)·D with H_eff ≈ 10 and q = 0.1–0.2 gives about 1.9–3 years, assuming D ≈ 1.
- **"SROI roughly 20× higher": ARITHMETICALLY EXPLAINED, but conceptually weak.**
  - 7 ÷ 0.32 ≈ 22, so the 20× is just the ratio of the all-in cost to CG's own cost.
  - It credits CG with all benefits while charging only CG's $320k. If the counterfactual is "never", the other funders' $6.7M is a real cost that exists only because of the grant (see Critique 2). Under a delay counterfactual it is displaced spending.
  - Either way the 20× needs a justified attribution rule, such as a leverage or fractional-credit approach, before it can be reported.
- **Cross-reference error.** The text says the ratio is robust to q "(see Critique 1)", and uses H_eff from "my Critique 1 calculation". In this set that derivation is in Critique 2, not Critique 1. The finding also conflicts with the claim that SROI could be 20× higher: robustness to q means the all-in ratio does not change, so the uplift comes only from the change of cost basis.

**EVIDENCE FOUND**
- There is a real pipeline: StAT-TB (NIAID), StatinTB (EDCTP/NIAID), ROSETTA, and ATORTUB. A review noted 
four ongoing statin-TB clinical trials, calling statins one of the most promising HDT drugs in the pipeline.

- The ROSETTA null result reduces expected Phase III appetite for the whole class. That raises q for "never" for rosuvastatin-like approaches, and it reduces p_success.
- I did not search the TAG pipeline, Working Group on New TB Drugs, Unitaid portfolio, or NIH RePORTER directly. Those remain open.

**OVERALL VERDICT: PARTIALLY VERIFIED**

**REVISED CRITIQUE**
- Verified facts: the Phase II statin-TB landscape is populated by NIH, EDCTP and Wellcome-funded work; dose-finding explicitly precedes a larger follow-up trial; generics have no obvious commercial sponsor.
- The claim that funders disfavor HDT is UNGROUNDED, and Phase II funding evidence cuts against it. No Phase III statin-TB trial funder was found, so the "never" branch remains plausible but unquantified.
- A competing registered Phase IIC trial (ATORTUB) must be checked against the CG grant. If it is the same trial, the redundancy case in the critique's last sentence applies, not the leverage case.
- The "20× higher SROI" should be dropped or re-derived with an explicit attribution rule. Fix the cross-reference to Critique 2.
- Direction: uncertain rather than clearly up. Strength: medium.

--- Critique: The funding landscape for a generic-statin TB program makes "never" a live branch. The speedup is a poor proxy for the grant's real counterfactual. ---

## Critique 1: TB Phase III reference class and WHO evidence package

**CLAIM CHECK**
- **"Phase III TB trials (Study 31/A5349, STREAM, endTB, TRUNCATE-TB, SimpliciTB) enrolled hundreds to thousands of participants": PLAUSIBLE, only partly verified.**
  - The trials are real. I confirmed that 
endTB is a Phase III, randomized, open-label, non-inferiority, multi-country trial of five shortened all-oral MDR-TB regimens
. I also confirmed that 
STREAM was a phase-III non-inferiority RCT.

  - The endTB launch statement said 
750 patients would take part in the clinical trial across six countries.

  - I did not retrieve enrollment figures for Study 31, TRUNCATE-TB or SimpliciTB, so those remain from memory. SimpliciTB may be registered as a Phase 2 or 2/3 trial rather than Phase III, so the label needs a check.
- **"Budgets were generally in the tens of millions of dollars": PLAUSIBLE, with partial support.**
  - TB-PRACTECAL was an MSF-sponsored phase 2b-3 trial. Its 
total cost was €33.9 million, an average of €61,460 per patient.

  - The same paper reports a literature range of 
US$7–221 million per trial for pharmaceutical phase 2 and 3 trials.

  - It also cites an 
average of US$23 million for anti-infective and respiratory phase 3 trials.

  - Outside TB, 
the median cost of a single phase III trial was $19 million
 in a JAMA IM analysis of 138 pivotal trials for FDA-approved drugs.
  - The endTB "US$60M" figure is not a trial budget. 
It is a four-year Unitaid project that also covers an estimated 2,600-patient treatment cohort.
 Do not use it as a single-trial cost.
  - I found no budgets for Study 31, STREAM or TRUNCATE-TB. Those would need NIH RePORTER, EDCTP and Unitaid lookups.
- **"WHO may require more than one trial or an IPD meta-analysis": UNVERIFIABLE.**
  - I found no WHO requirement of this kind. The WHO Global TB Report 2025 says its drug-resistant TB update drew on 
two clinical trials, BEAT-TB and endTB.
 That shows WHO sometimes relies on more than one trial. It is a drug-resistant TB example, and it does not show a requirement.
  - Subgroup evidence looks less likely to multiply costs for statins. A preprint notes 
pregnant women are unlikely to be on statins because of teratogenicity concerns.
 That suggests a pregnancy subgroup would probably be excluded, and the recommendation would likely carry a caveat instead. This is a weak source.
  - The StAT-TB protocol notes that 
statins and antiretrovirals can be co-administered with drug and dose selection.
 The HIV subgroup is therefore a real design question.
- **Arithmetic: VERIFIED.**
  - $20–60M divided by $7M is 2.9–8.6×.
  - $3,050 divided by 3–9 is about 340–1,020×.
  - $30M gives about 710×.

**EVIDENCE FOUND**
- The reference class is supported, but it mixes novel-drug registrational trials with different cost drivers. The TB-PRACTECAL paper says its cost 
included investment in trial infrastructure and medical expenditures not typical of standard clinical trials.
 A cheap oral adjunct with a routine-care endpoint could cost well below $20M. The Investigator's counterargument stands.
- Cost scales with per-patient cost and sample size. The review's lower bound of $7M overlaps the BOTEC figure. The $7M budget is therefore at the very bottom of the range and is not impossible.

**OVERALL VERDICT: PARTIALLY VERIFIED**

**REVISED CRITIQUE**
- Published cost data support a reference class of roughly $19–34M for a single Phase III trial, with a very wide range ($7–221M). Examples are the $19M Phase III median, $23M for anti-infective trials and €33.9M for TB-PRACTECAL.
- A $7M all-in budget sits at the low end of that range. It is not clearly implausible for a low-cost adjunct trial.
- The "multiple trials or IPD meta-analysis" requirement is UNGROUNDED. The pregnancy subgroup would probably be excluded for statins, so the multiplier is probably smaller than implied.
- Drop endTB's $60M as a trial cost.
- The 350–1,000× SROI range is correct arithmetic, but only if a $20–60M cost is accepted.
- Strength: medium, direction: uncertain, with a downward lean on SROI.

---

## Critique 2: Mismatched counterfactuals (speedup benefit vs. all-in cost)

**CLAIM CHECK**
- **Pure-delay algebra: VERIFIED as a derivation, with one caveat.**
  - If the whole program shifts by D years, benefits and costs both scale by e^(−rD). The net effect is (1−e^(−rD))·PV_B against (1−e^(−rD))·PV_C. The ratio is PV_B/PV_C, independent of D.
  - This is a standard result for pure time-shifts under a constant discount rate. It holds only if the benefit stream and cost stream shift by the same D. If the benefit lag is longer than the cost lag, the ratio changes.
- **"Never" and mixture branches: VERIFIED.** Both numerator and denominator scale by the same factor, so the ratio is PV_B/PV_C.
- **Numbers: VERIFIED as arithmetic, with one undocumented input.**
  - 1/0.06 ≈ 16.7. Multiplying by 0.6–0.7 gives about 10–11.7. Dividing by 0.85 gives about 12–13.8.
  - With r = 4% only, 25 × 0.6–0.7 ÷ 0.85 is about 17.6–20.6, so "about 18x" holds.
  - 3,050 × 12.5 ≈ 38,000 and 3,050 × 18 ≈ 55,000. The "30,000–55,000x" range is consistent.
  - The 0.6–0.7 delay factor is unexplained. It presumably reflects benefit onset after trial, WHO review and rollout. It should be stated explicitly because it drives the result.
- **"The BOTEC counts one year of plateau deaths averted and charges the full $7M": UNVERIFIABLE.** I do not have the CEA, so the diagnosis that the numerator and denominator come from different counterfactuals rests on the Investigator's reading.
- **Hybrid framing may be deliberate conservatism: UNGROUNDED, as the Investigator says.**
- **Displacement of other funders' money: a valid conceptual point.** The delay-branch ratio is PV_B/PV_C only if the other funders' dollars are valued at zero opportunity cost. The Investigator flags this but does not quantify it. If the displaced money would fund equally cost-effective research, the delay benefit shrinks toward zero and the 10–20× uplift would not hold.

**EVIDENCE FOUND**
- No external empirical evidence is needed for the core argument. I found nothing that contradicts it.
- The result is highly sensitive to the benefit horizon. The Investigator notes this but then states a 30,000–55,000× headline. That headline should be treated as an upper-bound illustration only.
- Real-world constraints on the horizon are visible in the statin evidence. ROSETTA found 
rosuvastatin 10 mg was safe but did not produce substantive benefits on culture conversion overall.
 Its PET-CT analysis showed 
no effect on microbiological or radiological outcomes.
 A 
phase IIA atorvastatin study showed a significant reduction in sputum mycobacterial load.
 Statin class and dose effects are uncertain, and p_success should be modest. The Investigator says p_success is included in PV_B, so this lowers the level but not the ratio logic.

**OVERALL VERDICT: PARTIALLY VERIFIED**

**REVISED CRITIQUE**
- Under a pure time-shift, "never", or a mixture of the two, the benefit-to-cost ratio is PV_B/PV_C. The BOTEC's "one year of benefit against full cost" is internally inconsistent if that is what the BOTEC does. That last point needs confirmation against the CEA.
- The uplift is plausibly about 10–20× under the stated horizon and discount assumptions. It depends heavily on the unexplained delay factor, the horizon, and treating other funders' dollars as free.
- Report the uplift as an illustrative range, not as "30,000–55,000×".
- Direction: the ratio rises, but displacement and horizon limits could pull it back down. Strength: large conceptually, medium once displacement is applied.

---

## Critique 3: Funding landscape and the "never" branch

**CLAIM CHECK**
- **"NIH and Johns Hopkins have published preclinical and early clinical work": VERIFIED.**
  - StAT-TB (NCT03882177) is a 
NIAID-sponsored Phase 2b dose-finding pravastatin study.
 It is 
completed.

  - The protocol lists 
Petros Karakousis of Johns Hopkins as US Principal Investigator.

  - It states the findings will 
inform dose selection for an anticipated larger follow-up study testing treatment-shortening potential.
 This supports the "dose-finding precedes Phase III" structure.
- **"Public-health funders have so far favored novel regimens and vaccines over host-directed therapies": UNVERIFIED, and partly contradicted.**
  - EDCTP funded StatinTB, a 
proof-of-concept Phase IIB placebo-controlled trial in Khayelitsha
 under grant RIA2017T-2004.
  - NIAID also funded it, through 
R01AI160501.

  - Wellcome has co-funded related work.
  - ROSETTA was a 
phase 2b trial run in the Philippines, Viet Nam and Uganda.
 I did not identify its funder.
  - Public funders have clearly supported Phase II statin-TB work. The open question is Phase III, where I found no funded trial.
- **"No commercial sponsor for generic statins": PLAUSIBLE.** The StAT-TB protocol itself says 
statins are attractive because of the widespread availability of less costly generics.
 That is the flip side of weak commercial incentive. I found no repurposing-literature source for the sponsor gap.
- **"Phase IIc" competitor: NOTABLE.**
  - ATORTUB has a registered 
Phase IIC selection trial with extended follow-up, designed as a pilot Phase III.
 (NCT06199921).
  - The ATORTUB group 
recently completed Phase IIA and IIB studies.

  - I cannot say whether this is the CG-funded trial. If the grant funds this trial, it is not a new gating step. If it funds a different trial, ATORTUB is an existing parallel pipeline, which lowers q. Check this first.
- **Expected speedup formula: VERIFIED.** q·H_eff + (1−q)·D with H_eff ≈ 10 and q = 0.1–0.2 gives about 1.9–3 years, assuming D ≈ 1.
- **"SROI roughly 20× higher": ARITHMETICALLY EXPLAINED, but conceptually weak.**
  - 7 ÷ 0.32 ≈ 22, so the 20× is just the ratio of the all-in cost to CG's own cost.
  - It credits CG with all benefits while charging only CG's $320k. If the counterfactual is "never", the other funders' $6.7M is a real cost that exists only because of the grant (see Critique 2). Under a delay counterfactual it is displaced spending.
  - Either way the 20× needs a justified attribution rule, such as a leverage or fractional-credit approach, before it can be reported.
- **Cross-reference error.** The text says the ratio is robust to q "(see Critique 1)", and uses H_eff from "my Critique 1 calculation". In this set that derivation is in Critique 2, not Critique 1. The finding also conflicts with the claim that SROI could be 20× higher: robustness to q means the all-in ratio does not change, so the uplift comes only from the change of cost basis.

**EVIDENCE FOUND**
- There is a real pipeline: StAT-TB (NIAID), StatinTB (EDCTP/NIAID), ROSETTA, and ATORTUB. A review noted 
four ongoing statin-TB clinical trials, calling statins one of the most promising HDT drugs in the pipeline.

- The ROSETTA null result reduces expected Phase III appetite for the whole class. That raises q for "never" for rosuvastatin-like approaches, and it reduces p_success.
- I did not search the TAG pipeline, Working Group on New TB Drugs, Unitaid portfolio, or NIH RePORTER directly. Those remain open.

**OVERALL VERDICT: PARTIALLY VERIFIED**

**REVISED CRITIQUE**
- Verified facts: the Phase II statin-TB landscape is populated by NIH, EDCTP and Wellcome-funded work; dose-finding explicitly precedes a larger follow-up trial; generics have no obvious commercial sponsor.
- The claim that funders disfavor HDT is UNGROUNDED, and Phase II funding evidence cuts against it. No Phase III statin-TB trial funder was found, so the "never" branch remains plausible but unquantified.
- A competing registered Phase IIC trial (ATORTUB) must be checked against the CG grant. If it is the same trial, the redundancy case in the critique's last sentence applies, not the leverage case.
- The "20× higher SROI" should be dropped or re-derived with an explicit attribution rule. Fix the cross-reference to Critique 2.
- Direction: uncertain rather than clearly up. Strength: medium.

--- Critique: Discounting quantified properly with an S-curve ramp and discounted costs. The net effect is about −20% to −31%, not the benefit-only −21% to −35%. ---

## Critique 1: Discounting with an S-curve ramp and discounted costs

**OVERALL VERDICT: PARTIALLY VERIFIED.**
- The arithmetic is largely correct, and the direction and size of the effect hold.
- The institutional claims (GiveWell rate, CG convention, the ~2,000x bar) could not be verified.
- The critique has labelling and consistency problems.
- Because the ramp, spend timing, and baseline SROI are assumed, it is still a sensitivity illustration and not a finding.

**CLAIM CHECK**

I recomputed each number by hand. I could not open the source CEA or the BOTEC document.

- **Flat-discount factors at 8.5 years (0.77 / 0.71 / 0.65): VERIFIED.** e^(−0.255)=0.775, e^(−0.34)=0.712, e^(−0.425)=0.654.
- **Thread's 8–9 year range (×0.64–0.79) and "−21% to −35%": VERIFIED.** The range is 0.787 to 0.638, so the upper end is closer to −36%, which is rounding.
- **Ramp formula e^(−rT0)(1−e^(−rL))/(rL): VERIFIED as an approximation.**
  - The exact value for a shifted, infinite-horizon ramp multiplies it by (1−e^(−rΔ))/(rΔ).
  - That extra factor is about 0.98, which explains the critique's "about 0.62" note at 4%.
- **Benefit factors (0.71 / 0.63 / 0.57): VERIFIED, with a small rounding issue.**
  - The formula gives 0.709 / 0.633 / 0.565.
  - The exact versions are about 0.698 / 0.620 / 0.551.
  - The 3% and 5% table values use the approximation, while the 4% net factor uses the exact one. This is a minor inconsistency.
- **Cost factors (0.88 / 0.85 / 0.82): VERIFIED.**
  - Spreading $6.7M uniformly over years 1–8 and adding $0.32M at t=0 gives about 0.881 / 0.845 / 0.812.
- **Net factors (0.80 / 0.73 / 0.69) and "−20 / −27 / −31%": VERIFIED within rounding.**
  - Using exact benefit factors gives about −21 / −27 / −32%.
- **L=10 ramp (≈0.57 at 4%, ≈0.51 at 5%): VERIFIED.**
  - The approximate formula gives 0.587 at 4% (about 0.575 with the exact version) and 0.515 at 5%.
- **SROI levels (≈2,440x / 2,230x / 2,100x): internally consistent but depend on an unstated baseline.**
  - They imply an undiscounted SROI of about 3,050x. The critique never states this figure, and I cannot verify it.
- **"Conflict with Critique 1" / "Critique 4": FLAG.**
  - This critique appears to be Critique 1 and cites itself, and Critique 4 is not in this batch.
  - These cross-references should be removed or re-keyed.
- **GiveWell uses roughly 4%: UNVERIFIED.** My search returned nothing on GiveWell's rate. I believe this is roughly right from memory, but I have no source to cite here.
- **CG applies or omits discounting inconsistently; "How we use BOTECs" (May 2025): UNVERIFIABLE.** The search did not surface that document or any CG discounting guidance.
- **Bar of about 2,000x: UNVERIFIED.** I found no source in this session. I recall Open Phil's GHW bar being raised from 1,000x to about 2,000x, but that is memory, not a finding.

**EVIDENCE FOUND**
- 
In global health, evaluations typically apply a 3% discount rate to health outcomes and costs.
 
One review argues for at least 5% for low- and lower-middle-income countries and about 4% for upper-middle-income countries.
 This supports the critique's 3–5% range and shows that costs and benefits are conventionally discounted together.
- Inference, not sourced:
  - The Critique 3 threshold of about 0.65 years is consistent with a bar of about 2,000x against a baseline of about 3,050x (2,000/3,050 ≈ 0.656).
  - That means the bar is crossed at about −34%, not at the "25% materiality line".
  - Under this critique's own numbers, the L=10 ramp at 5% gives about −37% (≈1,900x), which falls below the bar. The other scenarios stay above it.
  - The investigator should state which threshold defines "material".

**REVISED CRITIQUE**
- Discounting benefits alone (about −21% to −35%) overstates the penalty when costs are discounted consistently. Under the assumed ramp (T0=8.5, L=6) and uniform spend over years 1–8, the net effect is about −21% / −27% / −32% at 3% / 4% / 5%.
- A longer ramp (L=10) deepens the benefit penalty. At 5% it could push SROI below the bar if the baseline is about 3,050x. This relies on the inferred baseline.
- **Strength: medium, direction a reduction in SROI.** All timing assumptions are illustrative and need the CEA's real timeline. The CG discounting convention and the bar level remain UNGROUNDED.
- Remove the self-referential "Critique 1" and "Critique 4" cross-references.

---

## Critique 2: Asymmetric probability weighting of benefit and cost

**OVERALL VERDICT: PARTIALLY VERIFIED.**
- The logic and arithmetic are sound. The factual premise (that CG's $7M is a nominal, ungated sum) is unverifiable without the CEA.
- Retain it as a flagged hypothesis, **UNGROUNDED — plausible but needs empirical support.** The investigator already conditions it correctly.

**CLAIM CHECK**
- **Expected cost = $0.32M + s×$6.7M: VERIFIED as arithmetic.**
  - At s=0.6, cost is $4.34M and SROI rises by 7.02/4.34 ≈ 1.62x. ✔
  - At s=0.4, cost is $3.0M and SROI rises by about 2.34x. ✔
  - The "$7M" is really $7.02M, which is immaterial.
- **Benefit risk-adjusted while cost is nominal is a "double penalty": PLAUSIBLE.**
  - Stage-weighting costs is standard practice in risk-adjusted pharma valuation (general knowledge, not searched).
  - Whether the CEA does this is UNVERIFIABLE.
- **Counterpoint that s lies between p_success (0.4) and 1: VERIFIED as logic.**
  - Stage-reach probability cannot be below the end-to-end success probability.
  - Late failures incur most of the cost, so the correction may be modest.
- **Direction "increases": correct conditional on a nominal-sum cost.** It would not apply if the $7M is already an expected value, as the investigator says.

**EVIDENCE FOUND**
- No external evidence on how CG built the $7M. My searches were not designed to surface this, and the CEA cells were not accessible.
- Two further ways the critique could fail:
  - If p_success=0.40 refers only to the final stage, gating the earlier costs adds nothing.
  - If some downstream spend is by other funders and excluded from "all-in cost," s matters less.

**REVISED CRITIQUE**
- If the CEA's all-in cost is a nominal sum while benefits are multiplied by p_success, the SROI is understated.
  - The understatement is bounded roughly between 1.0x and 1.6–2.3x for s between 1.0 and 0.4.
  - Late-stage failure pushes the effective s toward 1, so a realistic effect is probably at the low end.
- **Strength: medium-to-low until the cost build-up is inspected. Direction: increases.** The key unknown is whether the $7M is nominal or expected.

---

## Critique 3: A 1-year speedup of trial results is not necessarily a 1-year speedup of adoption

**OVERALL VERDICT: PARTIALLY VERIFIED.**
- The structural point stands. Speedup is an uncertain quantity and not a defensible point value.
- The specific "lumpy guideline cycle" mechanism is weakened for TB by the cases the investigator suggested checking. Direction should be treated as uncertain, with a lean toward "approximately 1 year at the WHO step."
- The investigator's arithmetic is right: slack of more than 0.35 years takes the speedup below 0.65.

**CLAIM CHECK**
- **WHO guidelines come via a GDG process: VERIFIED.**
  - For Study 31, WHO 
received data from the Study 31 investigators in 2021 and convened a GDG to review the results.

- **WHO updates occur on a roughly fixed schedule, so earlier results are absorbed into waiting time: NOT SUPPORTED by the two TB examples.**
  - Study 31 was 
published online May 5, 2021
, and WHO's rapid communication on it was dated June 2021 (
GDG convened in 2021 after Study 31 data were received, with detailed results published 6 May 2021
).
  - That is roughly one month, so the GDG was convened in response to data and not on a fixed cycle.
  - The consolidated guideline update followed in 
May 2022
.
- **BPaLM: GDG timing followed data availability.**
  - 
The GDG met in February–March 2022, using new evidence from the TB-PRACTECAL and ZeNix trials.

  - 
TB-PRACTECAL stopped enrolling once its data safety board indicated BPaLM was superior.

  - 
The interim analysis used outcomes up to March 18, 2021.
 That is about 11 months before the GDG, so most of the delay sat in data analysis and sponsor sharing, not in a WHO queue.
  - 
WHO then published its rapid communication in May 2022.

- **Downstream lags exist and are additive: VERIFIED for Study 31.**
  - 
CDC issued guidance on a 4-month rifapentine-moxifloxacin regimen on February 25, 2022
, about 9.5 months after publication.
  - These sequential lags shift with the trial date and do not by themselves absorb the speedup.
- **Missing a guideline window costs a full cycle (2+ years): UNVERIFIED.** I found no evidence of fixed windows at WHO's TB programme. The sources suggest ad hoc GDGs, so the asymmetry may not apply.
- **Threshold arithmetic ("more than a third of a year" of slack): VERIFIED.** It is 1−0.65=0.35.

**EVIDENCE FOUND**
- **Limits of the evidence:**
  - These are two TB regimen cases with unusually high-profile, sponsor-supported trials. The investigator's "generic adjunct drug" may face a slower process.
  - The BPaLM case shows WHO acting on interim, pre-publication data. For a trial result, "available to WHO" and "published" are different dates, and the speedup definition needs to say which one is meant.
- No source found quantifying lags for adjunct or host-directed therapies, or for national policy and procurement steps.

**REVISED CRITIQUE**
- The model's one-for-one translation of the adoption curve holds only if the trial is the binding constraint at every step, and the speedup should be treated as a distribution.
- For TB specifically, two recent regimens show WHO's GDG responding within about one to two months of data being shared. That favours a speedup close to 1 year at the WHO stage and weakens the "fixed guideline cycle" mechanism and the asymmetric "lost cycle" upside.
- The remaining uncertainty lies in national adoption and procurement lags, plus the unspecified definition of the trial-result date. The post-WHO lags are untested here.
- **Strength: low-to-medium. Direction: uncertain (slightly toward "≈1 year or modestly less").** The lumpy-cycle claim is UNGROUNDED for TB. I recommend a sensitivity band on speedup_years instead of a point value.

--- Critique: Probability weighting is asymmetric between benefit and cost. ---

## Critique 1: Discounting with an S-curve ramp and discounted costs

**OVERALL VERDICT: PARTIALLY VERIFIED.**
- The arithmetic is largely correct, and the direction and size of the effect hold.
- The institutional claims (GiveWell rate, CG convention, the ~2,000x bar) could not be verified.
- The critique has labelling and consistency problems.
- Because the ramp, spend timing, and baseline SROI are assumed, it is still a sensitivity illustration and not a finding.

**CLAIM CHECK**

I recomputed each number by hand. I could not open the source CEA or the BOTEC document.

- **Flat-discount factors at 8.5 years (0.77 / 0.71 / 0.65): VERIFIED.** e^(−0.255)=0.775, e^(−0.34)=0.712, e^(−0.425)=0.654.
- **Thread's 8–9 year range (×0.64–0.79) and "−21% to −35%": VERIFIED.** The range is 0.787 to 0.638, so the upper end is closer to −36%, which is rounding.
- **Ramp formula e^(−rT0)(1−e^(−rL))/(rL): VERIFIED as an approximation.**
  - The exact value for a shifted, infinite-horizon ramp multiplies it by (1−e^(−rΔ))/(rΔ).
  - That extra factor is about 0.98, which explains the critique's "about 0.62" note at 4%.
- **Benefit factors (0.71 / 0.63 / 0.57): VERIFIED, with a small rounding issue.**
  - The formula gives 0.709 / 0.633 / 0.565.
  - The exact versions are about 0.698 / 0.620 / 0.551.
  - The 3% and 5% table values use the approximation, while the 4% net factor uses the exact one. This is a minor inconsistency.
- **Cost factors (0.88 / 0.85 / 0.82): VERIFIED.**
  - Spreading $6.7M uniformly over years 1–8 and adding $0.32M at t=0 gives about 0.881 / 0.845 / 0.812.
- **Net factors (0.80 / 0.73 / 0.69) and "−20 / −27 / −31%": VERIFIED within rounding.**
  - Using exact benefit factors gives about −21 / −27 / −32%.
- **L=10 ramp (≈0.57 at 4%, ≈0.51 at 5%): VERIFIED.**
  - The approximate formula gives 0.587 at 4% (about 0.575 with the exact version) and 0.515 at 5%.
- **SROI levels (≈2,440x / 2,230x / 2,100x): internally consistent but depend on an unstated baseline.**
  - They imply an undiscounted SROI of about 3,050x. The critique never states this figure, and I cannot verify it.
- **"Conflict with Critique 1" / "Critique 4": FLAG.**
  - This critique appears to be Critique 1 and cites itself, and Critique 4 is not in this batch.
  - These cross-references should be removed or re-keyed.
- **GiveWell uses roughly 4%: UNVERIFIED.** My search returned nothing on GiveWell's rate. I believe this is roughly right from memory, but I have no source to cite here.
- **CG applies or omits discounting inconsistently; "How we use BOTECs" (May 2025): UNVERIFIABLE.** The search did not surface that document or any CG discounting guidance.
- **Bar of about 2,000x: UNVERIFIED.** I found no source in this session. I recall Open Phil's GHW bar being raised from 1,000x to about 2,000x, but that is memory, not a finding.

**EVIDENCE FOUND**
- 
In global health, evaluations typically apply a 3% discount rate to health outcomes and costs.
 
One review argues for at least 5% for low- and lower-middle-income countries and about 4% for upper-middle-income countries.
 This supports the critique's 3–5% range and shows that costs and benefits are conventionally discounted together.
- Inference, not sourced:
  - The Critique 3 threshold of about 0.65 years is consistent with a bar of about 2,000x against a baseline of about 3,050x (2,000/3,050 ≈ 0.656).
  - That means the bar is crossed at about −34%, not at the "25% materiality line".
  - Under this critique's own numbers, the L=10 ramp at 5% gives about −37% (≈1,900x), which falls below the bar. The other scenarios stay above it.
  - The investigator should state which threshold defines "material".

**REVISED CRITIQUE**
- Discounting benefits alone (about −21% to −35%) overstates the penalty when costs are discounted consistently. Under the assumed ramp (T0=8.5, L=6) and uniform spend over years 1–8, the net effect is about −21% / −27% / −32% at 3% / 4% / 5%.
- A longer ramp (L=10) deepens the benefit penalty. At 5% it could push SROI below the bar if the baseline is about 3,050x. This relies on the inferred baseline.
- **Strength: medium, direction a reduction in SROI.** All timing assumptions are illustrative and need the CEA's real timeline. The CG discounting convention and the bar level remain UNGROUNDED.
- Remove the self-referential "Critique 1" and "Critique 4" cross-references.

---

## Critique 2: Asymmetric probability weighting of benefit and cost

**OVERALL VERDICT: PARTIALLY VERIFIED.**
- The logic and arithmetic are sound. The factual premise (that CG's $7M is a nominal, ungated sum) is unverifiable without the CEA.
- Retain it as a flagged hypothesis, **UNGROUNDED — plausible but needs empirical support.** The investigator already conditions it correctly.

**CLAIM CHECK**
- **Expected cost = $0.32M + s×$6.7M: VERIFIED as arithmetic.**
  - At s=0.6, cost is $4.34M and SROI rises by 7.02/4.34 ≈ 1.62x. ✔
  - At s=0.4, cost is $3.0M and SROI rises by about 2.34x. ✔
  - The "$7M" is really $7.02M, which is immaterial.
- **Benefit risk-adjusted while cost is nominal is a "double penalty": PLAUSIBLE.**
  - Stage-weighting costs is standard practice in risk-adjusted pharma valuation (general knowledge, not searched).
  - Whether the CEA does this is UNVERIFIABLE.
- **Counterpoint that s lies between p_success (0.4) and 1: VERIFIED as logic.**
  - Stage-reach probability cannot be below the end-to-end success probability.
  - Late failures incur most of the cost, so the correction may be modest.
- **Direction "increases": correct conditional on a nominal-sum cost.** It would not apply if the $7M is already an expected value, as the investigator says.

**EVIDENCE FOUND**
- No external evidence on how CG built the $7M. My searches were not designed to surface this, and the CEA cells were not accessible.
- Two further ways the critique could fail:
  - If p_success=0.40 refers only to the final stage, gating the earlier costs adds nothing.
  - If some downstream spend is by other funders and excluded from "all-in cost," s matters less.

**REVISED CRITIQUE**
- If the CEA's all-in cost is a nominal sum while benefits are multiplied by p_success, the SROI is understated.
  - The understatement is bounded roughly between 1.0x and 1.6–2.3x for s between 1.0 and 0.4.
  - Late-stage failure pushes the effective s toward 1, so a realistic effect is probably at the low end.
- **Strength: medium-to-low until the cost build-up is inspected. Direction: increases.** The key unknown is whether the $7M is nominal or expected.

---

## Critique 3: A 1-year speedup of trial results is not necessarily a 1-year speedup of adoption

**OVERALL VERDICT: PARTIALLY VERIFIED.**
- The structural point stands. Speedup is an uncertain quantity and not a defensible point value.
- The specific "lumpy guideline cycle" mechanism is weakened for TB by the cases the investigator suggested checking. Direction should be treated as uncertain, with a lean toward "approximately 1 year at the WHO step."
- The investigator's arithmetic is right: slack of more than 0.35 years takes the speedup below 0.65.

**CLAIM CHECK**
- **WHO guidelines come via a GDG process: VERIFIED.**
  - For Study 31, WHO 
received data from the Study 31 investigators in 2021 and convened a GDG to review the results.

- **WHO updates occur on a roughly fixed schedule, so earlier results are absorbed into waiting time: NOT SUPPORTED by the two TB examples.**
  - Study 31 was 
published online May 5, 2021
, and WHO's rapid communication on it was dated June 2021 (
GDG convened in 2021 after Study 31 data were received, with detailed results published 6 May 2021
).
  - That is roughly one month, so the GDG was convened in response to data and not on a fixed cycle.
  - The consolidated guideline update followed in 
May 2022
.
- **BPaLM: GDG timing followed data availability.**
  - 
The GDG met in February–March 2022, using new evidence from the TB-PRACTECAL and ZeNix trials.

  - 
TB-PRACTECAL stopped enrolling once its data safety board indicated BPaLM was superior.

  - 
The interim analysis used outcomes up to March 18, 2021.
 That is about 11 months before the GDG, so most of the delay sat in data analysis and sponsor sharing, not in a WHO queue.
  - 
WHO then published its rapid communication in May 2022.

- **Downstream lags exist and are additive: VERIFIED for Study 31.**
  - 
CDC issued guidance on a 4-month rifapentine-moxifloxacin regimen on February 25, 2022
, about 9.5 months after publication.
  - These sequential lags shift with the trial date and do not by themselves absorb the speedup.
- **Missing a guideline window costs a full cycle (2+ years): UNVERIFIED.** I found no evidence of fixed windows at WHO's TB programme. The sources suggest ad hoc GDGs, so the asymmetry may not apply.
- **Threshold arithmetic ("more than a third of a year" of slack): VERIFIED.** It is 1−0.65=0.35.

**EVIDENCE FOUND**
- **Limits of the evidence:**
  - These are two TB regimen cases with unusually high-profile, sponsor-supported trials. The investigator's "generic adjunct drug" may face a slower process.
  - The BPaLM case shows WHO acting on interim, pre-publication data. For a trial result, "available to WHO" and "published" are different dates, and the speedup definition needs to say which one is meant.
- No source found quantifying lags for adjunct or host-directed therapies, or for national policy and procurement steps.

**REVISED CRITIQUE**
- The model's one-for-one translation of the adoption curve holds only if the trial is the binding constraint at every step, and the speedup should be treated as a distribution.
- For TB specifically, two recent regimens show WHO's GDG responding within about one to two months of data being shared. That favours a speedup close to 1 year at the WHO stage and weakens the "fixed guideline cycle" mechanism and the asymmetric "lost cycle" upside.
- The remaining uncertainty lies in national adoption and procurement lags, plus the unspecified definition of the trial-result date. The post-WHO lags are untested here.
- **Strength: low-to-medium. Direction: uncertain (slightly toward "≈1 year or modestly less").** The lumpy-cycle claim is UNGROUNDED for TB. I recommend a sensitivity band on speedup_years instead of a point value.

--- Critique: A 1-year speedup of trial results does not necessarily become a 1-year speedup of adoption, in either direction. ---

## Critique 1: Discounting with an S-curve ramp and discounted costs

**OVERALL VERDICT: PARTIALLY VERIFIED.**
- The arithmetic is largely correct, and the direction and size of the effect hold.
- The institutional claims (GiveWell rate, CG convention, the ~2,000x bar) could not be verified.
- The critique has labelling and consistency problems.
- Because the ramp, spend timing, and baseline SROI are assumed, it is still a sensitivity illustration and not a finding.

**CLAIM CHECK**

I recomputed each number by hand. I could not open the source CEA or the BOTEC document.

- **Flat-discount factors at 8.5 years (0.77 / 0.71 / 0.65): VERIFIED.** e^(−0.255)=0.775, e^(−0.34)=0.712, e^(−0.425)=0.654.
- **Thread's 8–9 year range (×0.64–0.79) and "−21% to −35%": VERIFIED.** The range is 0.787 to 0.638, so the upper end is closer to −36%, which is rounding.
- **Ramp formula e^(−rT0)(1−e^(−rL))/(rL): VERIFIED as an approximation.**
  - The exact value for a shifted, infinite-horizon ramp multiplies it by (1−e^(−rΔ))/(rΔ).
  - That extra factor is about 0.98, which explains the critique's "about 0.62" note at 4%.
- **Benefit factors (0.71 / 0.63 / 0.57): VERIFIED, with a small rounding issue.**
  - The formula gives 0.709 / 0.633 / 0.565.
  - The exact versions are about 0.698 / 0.620 / 0.551.
  - The 3% and 5% table values use the approximation, while the 4% net factor uses the exact one. This is a minor inconsistency.
- **Cost factors (0.88 / 0.85 / 0.82): VERIFIED.**
  - Spreading $6.7M uniformly over years 1–8 and adding $0.32M at t=0 gives about 0.881 / 0.845 / 0.812.
- **Net factors (0.80 / 0.73 / 0.69) and "−20 / −27 / −31%": VERIFIED within rounding.**
  - Using exact benefit factors gives about −21 / −27 / −32%.
- **L=10 ramp (≈0.57 at 4%, ≈0.51 at 5%): VERIFIED.**
  - The approximate formula gives 0.587 at 4% (about 0.575 with the exact version) and 0.515 at 5%.
- **SROI levels (≈2,440x / 2,230x / 2,100x): internally consistent but depend on an unstated baseline.**
  - They imply an undiscounted SROI of about 3,050x. The critique never states this figure, and I cannot verify it.
- **"Conflict with Critique 1" / "Critique 4": FLAG.**
  - This critique appears to be Critique 1 and cites itself, and Critique 4 is not in this batch.
  - These cross-references should be removed or re-keyed.
- **GiveWell uses roughly 4%: UNVERIFIED.** My search returned nothing on GiveWell's rate. I believe this is roughly right from memory, but I have no source to cite here.
- **CG applies or omits discounting inconsistently; "How we use BOTECs" (May 2025): UNVERIFIABLE.** The search did not surface that document or any CG discounting guidance.
- **Bar of about 2,000x: UNVERIFIED.** I found no source in this session. I recall Open Phil's GHW bar being raised from 1,000x to about 2,000x, but that is memory, not a finding.

**EVIDENCE FOUND**
- 
In global health, evaluations typically apply a 3% discount rate to health outcomes and costs.
 
One review argues for at least 5% for low- and lower-middle-income countries and about 4% for upper-middle-income countries.
 This supports the critique's 3–5% range and shows that costs and benefits are conventionally discounted together.
- Inference, not sourced:
  - The Critique 3 threshold of about 0.65 years is consistent with a bar of about 2,000x against a baseline of about 3,050x (2,000/3,050 ≈ 0.656).
  - That means the bar is crossed at about −34%, not at the "25% materiality line".
  - Under this critique's own numbers, the L=10 ramp at 5% gives about −37% (≈1,900x), which falls below the bar. The other scenarios stay above it.
  - The investigator should state which threshold defines "material".

**REVISED CRITIQUE**
- Discounting benefits alone (about −21% to −35%) overstates the penalty when costs are discounted consistently. Under the assumed ramp (T0=8.5, L=6) and uniform spend over years 1–8, the net effect is about −21% / −27% / −32% at 3% / 4% / 5%.
- A longer ramp (L=10) deepens the benefit penalty. At 5% it could push SROI below the bar if the baseline is about 3,050x. This relies on the inferred baseline.
- **Strength: medium, direction a reduction in SROI.** All timing assumptions are illustrative and need the CEA's real timeline. The CG discounting convention and the bar level remain UNGROUNDED.
- Remove the self-referential "Critique 1" and "Critique 4" cross-references.

---

## Critique 2: Asymmetric probability weighting of benefit and cost

**OVERALL VERDICT: PARTIALLY VERIFIED.**
- The logic and arithmetic are sound. The factual premise (that CG's $7M is a nominal, ungated sum) is unverifiable without the CEA.
- Retain it as a flagged hypothesis, **UNGROUNDED — plausible but needs empirical support.** The investigator already conditions it correctly.

**CLAIM CHECK**
- **Expected cost = $0.32M + s×$6.7M: VERIFIED as arithmetic.**
  - At s=0.6, cost is $4.34M and SROI rises by 7.02/4.34 ≈ 1.62x. ✔
  - At s=0.4, cost is $3.0M and SROI rises by about 2.34x. ✔
  - The "$7M" is really $7.02M, which is immaterial.
- **Benefit risk-adjusted while cost is nominal is a "double penalty": PLAUSIBLE.**
  - Stage-weighting costs is standard practice in risk-adjusted pharma valuation (general knowledge, not searched).
  - Whether the CEA does this is UNVERIFIABLE.
- **Counterpoint that s lies between p_success (0.4) and 1: VERIFIED as logic.**
  - Stage-reach probability cannot be below the end-to-end success probability.
  - Late failures incur most of the cost, so the correction may be modest.
- **Direction "increases": correct conditional on a nominal-sum cost.** It would not apply if the $7M is already an expected value, as the investigator says.

**EVIDENCE FOUND**
- No external evidence on how CG built the $7M. My searches were not designed to surface this, and the CEA cells were not accessible.
- Two further ways the critique could fail:
  - If p_success=0.40 refers only to the final stage, gating the earlier costs adds nothing.
  - If some downstream spend is by other funders and excluded from "all-in cost," s matters less.

**REVISED CRITIQUE**
- If the CEA's all-in cost is a nominal sum while benefits are multiplied by p_success, the SROI is understated.
  - The understatement is bounded roughly between 1.0x and 1.6–2.3x for s between 1.0 and 0.4.
  - Late-stage failure pushes the effective s toward 1, so a realistic effect is probably at the low end.
- **Strength: medium-to-low until the cost build-up is inspected. Direction: increases.** The key unknown is whether the $7M is nominal or expected.

---

## Critique 3: A 1-year speedup of trial results is not necessarily a 1-year speedup of adoption

**OVERALL VERDICT: PARTIALLY VERIFIED.**
- The structural point stands. Speedup is an uncertain quantity and not a defensible point value.
- The specific "lumpy guideline cycle" mechanism is weakened for TB by the cases the investigator suggested checking. Direction should be treated as uncertain, with a lean toward "approximately 1 year at the WHO step."
- The investigator's arithmetic is right: slack of more than 0.35 years takes the speedup below 0.65.

**CLAIM CHECK**
- **WHO guidelines come via a GDG process: VERIFIED.**
  - For Study 31, WHO 
received data from the Study 31 investigators in 2021 and convened a GDG to review the results.

- **WHO updates occur on a roughly fixed schedule, so earlier results are absorbed into waiting time: NOT SUPPORTED by the two TB examples.**
  - Study 31 was 
published online May 5, 2021
, and WHO's rapid communication on it was dated June 2021 (
GDG convened in 2021 after Study 31 data were received, with detailed results published 6 May 2021
).
  - That is roughly one month, so the GDG was convened in response to data and not on a fixed cycle.
  - The consolidated guideline update followed in 
May 2022
.
- **BPaLM: GDG timing followed data availability.**
  - 
The GDG met in February–March 2022, using new evidence from the TB-PRACTECAL and ZeNix trials.

  - 
TB-PRACTECAL stopped enrolling once its data safety board indicated BPaLM was superior.

  - 
The interim analysis used outcomes up to March 18, 2021.
 That is about 11 months before the GDG, so most of the delay sat in data analysis and sponsor sharing, not in a WHO queue.
  - 
WHO then published its rapid communication in May 2022.

- **Downstream lags exist and are additive: VERIFIED for Study 31.**
  - 
CDC issued guidance on a 4-month rifapentine-moxifloxacin regimen on February 25, 2022
, about 9.5 months after publication.
  - These sequential lags shift with the trial date and do not by themselves absorb the speedup.
- **Missing a guideline window costs a full cycle (2+ years): UNVERIFIED.** I found no evidence of fixed windows at WHO's TB programme. The sources suggest ad hoc GDGs, so the asymmetry may not apply.
- **Threshold arithmetic ("more than a third of a year" of slack): VERIFIED.** It is 1−0.65=0.35.

**EVIDENCE FOUND**
- **Limits of the evidence:**
  - These are two TB regimen cases with unusually high-profile, sponsor-supported trials. The investigator's "generic adjunct drug" may face a slower process.
  - The BPaLM case shows WHO acting on interim, pre-publication data. For a trial result, "available to WHO" and "published" are different dates, and the speedup definition needs to say which one is meant.
- No source found quantifying lags for adjunct or host-directed therapies, or for national policy and procurement steps.

**REVISED CRITIQUE**
- The model's one-for-one translation of the adoption curve holds only if the trial is the binding constraint at every step, and the speedup should be treated as a distribution.
- For TB specifically, two recent regimens show WHO's GDG responding within about one to two months of data being shared. That favours a speedup close to 1 year at the WHO stage and weakens the "fixed guideline cycle" mechanism and the asymmetric "lost cycle" upside.
- The remaining uncertainty lies in national adoption and procurement lags, plus the unspecified definition of the trial-result date. The post-WHO lags are untested here.
- **Strength: low-to-medium. Direction: uncertain (slightly toward "≈1 year or modestly less").** The lumpy-cycle claim is UNGROUNDED for TB. I recommend a sensitivity band on speedup_years instead of a point value.

--- Critique: Post-TB lung disease morbidity is likely the largest unvalued channel (~50–60k central, wide range) ---

## Critique 1: Post-TB lung disease morbidity (~55k central)

**CITATION CHECK**
- Menzies et al. 2021 (Lancet Glob Health 9:e1679–87): **VERIFIED, and the Investigator's baseline looks too low.**
  - 
The paper estimates 12.1 DALYs per incident TB case, of which 6.3 are from the disease episode and 5.8 from the post-TB period.
 That makes post-TB roughly half of lifetime burden. A later paper says it contributes 
up to 47% of the disease burden in DALYs.

  - 
Post-TB mortality and morbidity were both estimated from decreased lung function.
 The 5.8 DALYs therefore combine morbidity and premature death. I could not find the split in the sources retrieved.
  - 
28% of total DALYs accrue 15 or more years after incident TB.
 This supports the point that these are long-tail DALYs.
- International Post-TB Symposium and Allwood et al.: **PARTIALLY VERIFIED.** The symposium paper and Allwood's "The long shadow post-tuberculosis" exist (
"Post-tuberculosis lung health: perspectives from the First International Symposium"
). I did not check their prevalence figures in detail.

**CLAIM CHECK**
- Post-TB lung disease is common and long-lasting: **VERIFIED.** 
Reviews put respiratory impairment among TB survivors at 15–60%.
 The "~30% with meaningful impairment" input sits inside that range.
- Baseline of 0.75 DALYs per patient: **PLAUSIBLE but probably low.**
  - Menzies reports 5.8 post-TB DALYs per case, including deaths, against the Investigator's 0.75 for morbidity alone.
  - The morbidity-only share is unknown, so the gap cannot be quantified. It is likely large.
  - Menzies may also be discounted or modelled differently, which I did not check.
- Arithmetic: **VERIFIED.** 3.3M × 0.75 ≈ 2.5M, × 5% ≈ 124k, × 0.45 ≈ 56k. The high end of ~300k is also consistent.
- 5% reduction in long-term lung burden: **UNGROUNDED**, as the Investigator stated.
- "The trial's strongest signal was reduced lung damage": **UNVERIFIABLE, and possibly contradicted.** The source trial is not identified in my materials.
  - The ROSETTA trial (rosuvastatin) 
found no substantive benefit on culture conversion, on proportion of lung affected by chest x-ray, or on spirometry.

  - 
Its PET-CT sub-study also found no effect.

  - If the critique's premise comes from a different statin trial, such as StAT-TB with pravastatin, I found no published results to check it against. The premise needs confirming.
- Intervention-to-long-term link: **UNGROUNDED.** I found no long-term outcome data. A 2025 case-definition paper says 
the definition was developed without data on long-term patient outcomes.


**EVIDENCE FOUND**
- Menzies's 5.8 post-TB DALYs per case suggests the unvalued pool could be several times larger than 2.5M DALYs per adoption-year if the Investigator's baseline is raised. That would raise the ceiling, but not the central estimate unless the effect size is also supported.
- Double-counting risk with Critique 2: post-TB mortality is inside Menzies's post-TB DALYs. If baselines are taken from Menzies, Critiques 1 and 2 overlap.
- The convention flag is correct. Menzies shows a large share of DALYs accrue after 15 or more years, so discounting would cut this channel materially.

**OVERALL VERDICT: PARTIALLY VERIFIED**

**REVISED CRITIQUE:** Post-TB lung disease is a large, real burden. Menzies 2021 puts about 5.8 of 12.1 lifetime DALYs per case in the post-TB phase, and these are long-tail DALYs that discounting would cut. A BOTEC that assigns this channel zero value omits a potentially important term. The central estimate of ~55k rests on two unsupported inputs: the 5% effect size and the "lung damage signal" premise. The premise is **UNVERIFIED** and is contradicted by ROSETTA, which found no lung benefit on x-ray, spirometry or PET-CT. The 0.75 DALY baseline is probably too low compared with Menzies, though that source mixes morbidity and mortality. Keep the strength at medium-to-low, conditional on identifying which trial showed the lung signal. Report discounted and undiscounted versions. Avoid double-counting with Critique 2.

---

## Critique 2: Post-treatment excess mortality and life-expectancy adjustment

**CITATION CHECK**
- Romanowski et al. 2019 (Lancet Infect Dis 19:1129–37): **VERIFIED.**
  - It is a systematic review and meta-analysis of long-term all-cause mortality in people treated for TB.
  - Commentary describes 
TB survivors as having approximately three to four times the mortality of local populations.

  - The pooled figure is cited as 
2.91 (95% CI 2.21–3.84) times higher than in those who never had TB.

  - This fills in the number the Investigator could not recall. "A multiple of the general population's" is correct.

**CLAIM CHECK**
- Elevated post-treatment mortality: **VERIFIED.** A large 2025 Brazilian cohort also found 
an elevated natural-cause mortality risk in the treated cohort (RR 1.77, 95% CI 1.55–2.03).
 
Risk ratios were raised for respiratory deaths, among other causes.

- Respiratory disease as a major driver of excess deaths: **PARTIALLY VERIFIED.** One review states that 
respiratory diseases remain the leading cause of excess deaths in people who recover from TB.
 The 40% attributable share is not directly sourced. For comparison, Romanowski attributed 20% (95% CI 15–26) of the excess to cardiovascular disease (
per the Basham et al. discussion
). A respiratory share of 40% is therefore plausible but **UNGROUNDED**.
- ~10% cumulative excess mortality over 10 years: **PLAUSIBLE.** An SMR of ~2.9 on typical LMIC adult background mortality could give excess mortality of that order. The Investigator labelled this as illustrative.
- 5% intervention effect: **UNGROUNDED.**
- Arithmetic for (a): **VERIFIED.** 0.1 × 0.4 × 0.05 = 0.002; × 15 = 0.03; × 3.3M ≈ 99k; × 0.45 ≈ 45k. Part (b): 5–10% of 535k = 27–54k, which matches the stated −25k to −55k.
- Part (b), that rescued patients have worse residual life expectancy: **UNVERIFIABLE.** It is logically sound, since late diagnosis and immunocompromise raise the risk of lasting impairment (
per a Lancet ID commentary
). I found no quantification. The 5–10% overstatement is the Investigator's own figure.
- Statin cardiovascular benefit over about 6 months treated as zero: **PLAUSIBLE.** I did not verify it.

**EVIDENCE FOUND**
- Menzies's post-TB DALYs include post-TB mortality, so this channel overlaps with Critique 1 if both are added.
- Mortality is elevated in the Cerqueira-Silva cohort even in treated patients, supporting the existence of the excess-death pool but not the 40% lung share or the 5% effect.
- The net effect is unsigned. The Investigator's own conclusion that the two adjustments may cancel is reasonable.

**OVERALL VERDICT: PARTIALLY VERIFIED**

**REVISED CRITIQUE:** TB survivors have substantially elevated long-term mortality (pooled SMR ~2.9 in Romanowski 2019). Respiratory causes are a major contributor, but the 40% share is **UNGROUNDED**. The upside channel (~45k) depends on three unsupported inputs: a 5% effect, a 10% excess mortality, and a 40% respiratory share. Treat it as a flagged hypothesis with a wide range of roughly 0–50k. The downside life-expectancy adjustment is logically sound but its size is unquantified (**UNGROUNDED**). Treat the net as approximately zero with uncertain sign. Merge or net this against Critique 1 to avoid double-counting. Strength: low-to-medium.

---

## Critique 3: Transmission benefit (~10–30k central)

**CITATION CHECK**
No specific studies were cited. The Investigator asked the Verifier to find relevant modelling studies.

**CLAIM CHECK**
- Most transmission occurs before diagnosis and treatment start: **VERIFIED.** A review on infectiousness and treatment effect says 
most TB transmission occurs before diagnosis and effective treatment initiation.
 A Bayesian modelling study finds 
a disproportionate share of future transmission arises from undiagnosed smear-positive subclinical TB.

- Infectiousness falls quickly after effective therapy starts: **VERIFIED, with caveats.**
  - A population model of shorter regimens assumes 
bacillary burden drops rapidly and patients are non-infectious after the first two weeks.

  - The same review reports that 
30–40% of patients who produce cough aerosols rapidly become nonculturable after treatment initiation.

  - Human-to-guinea-pig experiments show a rapid effect of effective treatment on transmission.
  - However, 
the exact duration of infectiousness after treatment initiation remains uncertain and likely varies between individuals.
 A 1–5% post-start transmission share is directionally supported but not directly measured.
- Culture conversion at 8 weeks does not map one-to-one to infectiousness: **PLAUSIBLE.** Conversion at 8 weeks is a phase 2b efficacy endpoint (
usually measured at 2 months
). Infectiousness collapses much earlier than culture conversion, so the Investigator's discount is warranted.
- ROSETTA, a statin trial, found no benefit on culture conversion. 
Another trial using rosuvastatin did not affect sputum culture conversion.
 
An atorvastatin phase IIA study did show a significant reduction in sputum mycobacterial load.
 The premise of faster conversion is therefore contested across trials.
- Secondary cases per index case of 0.3–1: **UNVERIFIABLE** here. It is plausible for high-burden settings but not sourced.
- 10 DALYs per secondary case: **PLAUSIBLE.** Menzies gives an average of 12.1 DALYs per incident case.
- Arithmetic: **VERIFIED.** 3.3M × 0.5 × 0.003 × 10 ≈ 49.5k; × 0.4 ≈ 20k. The net 0.1–1% follows from 1–5% × 10–20%. The 3k–150k range is unverified.

**EVIDENCE FOUND**
- Modelling sources that fit the Investigator's logic:
  - The shorter-regimen model (PMC4015982).
  - Dowdy-type pre-diagnosis transmission analyses (PMC9907102).
  - The infectiousness and effective-treatment review (PMC12054730).
- Shorter-regimen modelling treats on-treatment infectiousness as short-lived. This supports the idea that conversion speed after week 2 matters little.
- Counterweight to the Investigator's logic: a lung-sparing adjunct does not shorten diagnostic delay, which is the dominant transmission window. This reinforces the small-effect conclusion.

**OVERALL VERDICT: PARTIALLY VERIFIED**

**REVISED CRITIQUE:** Most transmission occurs before diagnosis, and infectiousness falls within days to weeks of effective treatment. Any transmission benefit from faster culture conversion is therefore small. This is supported by the transmission and modelling literature above. The numerical inputs (post-start transmission share of 1–5%, 10–20% reduction, 0.5 secondary cases) are unsourced and should be flagged **UNGROUNDED**. The central estimate of ~20k is a bounded order-of-magnitude figure, with real downside if the statin has no culture-conversion effect (ROSETTA found none). Consider lowering the central estimate toward ~10k or below, and widening the low end toward zero. Strength: low. This is a minor channel, and the thread label ("post-TB lung disease") does not match its content.

--- Critique: Post-treatment excess mortality (~40–50k central) and a related sign-reversing adjustment ---

## Critique 1: Post-TB lung disease morbidity (~55k central)

**CITATION CHECK**
- Menzies et al. 2021 (Lancet Glob Health 9:e1679–87): **VERIFIED, and the Investigator's baseline looks too low.**
  - 
The paper estimates 12.1 DALYs per incident TB case, of which 6.3 are from the disease episode and 5.8 from the post-TB period.
 That makes post-TB roughly half of lifetime burden. A later paper says it contributes 
up to 47% of the disease burden in DALYs.

  - 
Post-TB mortality and morbidity were both estimated from decreased lung function.
 The 5.8 DALYs therefore combine morbidity and premature death. I could not find the split in the sources retrieved.
  - 
28% of total DALYs accrue 15 or more years after incident TB.
 This supports the point that these are long-tail DALYs.
- International Post-TB Symposium and Allwood et al.: **PARTIALLY VERIFIED.** The symposium paper and Allwood's "The long shadow post-tuberculosis" exist (
"Post-tuberculosis lung health: perspectives from the First International Symposium"
). I did not check their prevalence figures in detail.

**CLAIM CHECK**
- Post-TB lung disease is common and long-lasting: **VERIFIED.** 
Reviews put respiratory impairment among TB survivors at 15–60%.
 The "~30% with meaningful impairment" input sits inside that range.
- Baseline of 0.75 DALYs per patient: **PLAUSIBLE but probably low.**
  - Menzies reports 5.8 post-TB DALYs per case, including deaths, against the Investigator's 0.75 for morbidity alone.
  - The morbidity-only share is unknown, so the gap cannot be quantified. It is likely large.
  - Menzies may also be discounted or modelled differently, which I did not check.
- Arithmetic: **VERIFIED.** 3.3M × 0.75 ≈ 2.5M, × 5% ≈ 124k, × 0.45 ≈ 56k. The high end of ~300k is also consistent.
- 5% reduction in long-term lung burden: **UNGROUNDED**, as the Investigator stated.
- "The trial's strongest signal was reduced lung damage": **UNVERIFIABLE, and possibly contradicted.** The source trial is not identified in my materials.
  - The ROSETTA trial (rosuvastatin) 
found no substantive benefit on culture conversion, on proportion of lung affected by chest x-ray, or on spirometry.

  - 
Its PET-CT sub-study also found no effect.

  - If the critique's premise comes from a different statin trial, such as StAT-TB with pravastatin, I found no published results to check it against. The premise needs confirming.
- Intervention-to-long-term link: **UNGROUNDED.** I found no long-term outcome data. A 2025 case-definition paper says 
the definition was developed without data on long-term patient outcomes.


**EVIDENCE FOUND**
- Menzies's 5.8 post-TB DALYs per case suggests the unvalued pool could be several times larger than 2.5M DALYs per adoption-year if the Investigator's baseline is raised. That would raise the ceiling, but not the central estimate unless the effect size is also supported.
- Double-counting risk with Critique 2: post-TB mortality is inside Menzies's post-TB DALYs. If baselines are taken from Menzies, Critiques 1 and 2 overlap.
- The convention flag is correct. Menzies shows a large share of DALYs accrue after 15 or more years, so discounting would cut this channel materially.

**OVERALL VERDICT: PARTIALLY VERIFIED**

**REVISED CRITIQUE:** Post-TB lung disease is a large, real burden. Menzies 2021 puts about 5.8 of 12.1 lifetime DALYs per case in the post-TB phase, and these are long-tail DALYs that discounting would cut. A BOTEC that assigns this channel zero value omits a potentially important term. The central estimate of ~55k rests on two unsupported inputs: the 5% effect size and the "lung damage signal" premise. The premise is **UNVERIFIED** and is contradicted by ROSETTA, which found no lung benefit on x-ray, spirometry or PET-CT. The 0.75 DALY baseline is probably too low compared with Menzies, though that source mixes morbidity and mortality. Keep the strength at medium-to-low, conditional on identifying which trial showed the lung signal. Report discounted and undiscounted versions. Avoid double-counting with Critique 2.

---

## Critique 2: Post-treatment excess mortality and life-expectancy adjustment

**CITATION CHECK**
- Romanowski et al. 2019 (Lancet Infect Dis 19:1129–37): **VERIFIED.**
  - It is a systematic review and meta-analysis of long-term all-cause mortality in people treated for TB.
  - Commentary describes 
TB survivors as having approximately three to four times the mortality of local populations.

  - The pooled figure is cited as 
2.91 (95% CI 2.21–3.84) times higher than in those who never had TB.

  - This fills in the number the Investigator could not recall. "A multiple of the general population's" is correct.

**CLAIM CHECK**
- Elevated post-treatment mortality: **VERIFIED.** A large 2025 Brazilian cohort also found 
an elevated natural-cause mortality risk in the treated cohort (RR 1.77, 95% CI 1.55–2.03).
 
Risk ratios were raised for respiratory deaths, among other causes.

- Respiratory disease as a major driver of excess deaths: **PARTIALLY VERIFIED.** One review states that 
respiratory diseases remain the leading cause of excess deaths in people who recover from TB.
 The 40% attributable share is not directly sourced. For comparison, Romanowski attributed 20% (95% CI 15–26) of the excess to cardiovascular disease (
per the Basham et al. discussion
). A respiratory share of 40% is therefore plausible but **UNGROUNDED**.
- ~10% cumulative excess mortality over 10 years: **PLAUSIBLE.** An SMR of ~2.9 on typical LMIC adult background mortality could give excess mortality of that order. The Investigator labelled this as illustrative.
- 5% intervention effect: **UNGROUNDED.**
- Arithmetic for (a): **VERIFIED.** 0.1 × 0.4 × 0.05 = 0.002; × 15 = 0.03; × 3.3M ≈ 99k; × 0.45 ≈ 45k. Part (b): 5–10% of 535k = 27–54k, which matches the stated −25k to −55k.
- Part (b), that rescued patients have worse residual life expectancy: **UNVERIFIABLE.** It is logically sound, since late diagnosis and immunocompromise raise the risk of lasting impairment (
per a Lancet ID commentary
). I found no quantification. The 5–10% overstatement is the Investigator's own figure.
- Statin cardiovascular benefit over about 6 months treated as zero: **PLAUSIBLE.** I did not verify it.

**EVIDENCE FOUND**
- Menzies's post-TB DALYs include post-TB mortality, so this channel overlaps with Critique 1 if both are added.
- Mortality is elevated in the Cerqueira-Silva cohort even in treated patients, supporting the existence of the excess-death pool but not the 40% lung share or the 5% effect.
- The net effect is unsigned. The Investigator's own conclusion that the two adjustments may cancel is reasonable.

**OVERALL VERDICT: PARTIALLY VERIFIED**

**REVISED CRITIQUE:** TB survivors have substantially elevated long-term mortality (pooled SMR ~2.9 in Romanowski 2019). Respiratory causes are a major contributor, but the 40% share is **UNGROUNDED**. The upside channel (~45k) depends on three unsupported inputs: a 5% effect, a 10% excess mortality, and a 40% respiratory share. Treat it as a flagged hypothesis with a wide range of roughly 0–50k. The downside life-expectancy adjustment is logically sound but its size is unquantified (**UNGROUNDED**). Treat the net as approximately zero with uncertain sign. Merge or net this against Critique 1 to avoid double-counting. Strength: low-to-medium.

---

## Critique 3: Transmission benefit (~10–30k central)

**CITATION CHECK**
No specific studies were cited. The Investigator asked the Verifier to find relevant modelling studies.

**CLAIM CHECK**
- Most transmission occurs before diagnosis and treatment start: **VERIFIED.** A review on infectiousness and treatment effect says 
most TB transmission occurs before diagnosis and effective treatment initiation.
 A Bayesian modelling study finds 
a disproportionate share of future transmission arises from undiagnosed smear-positive subclinical TB.

- Infectiousness falls quickly after effective therapy starts: **VERIFIED, with caveats.**
  - A population model of shorter regimens assumes 
bacillary burden drops rapidly and patients are non-infectious after the first two weeks.

  - The same review reports that 
30–40% of patients who produce cough aerosols rapidly become nonculturable after treatment initiation.

  - Human-to-guinea-pig experiments show a rapid effect of effective treatment on transmission.
  - However, 
the exact duration of infectiousness after treatment initiation remains uncertain and likely varies between individuals.
 A 1–5% post-start transmission share is directionally supported but not directly measured.
- Culture conversion at 8 weeks does not map one-to-one to infectiousness: **PLAUSIBLE.** Conversion at 8 weeks is a phase 2b efficacy endpoint (
usually measured at 2 months
). Infectiousness collapses much earlier than culture conversion, so the Investigator's discount is warranted.
- ROSETTA, a statin trial, found no benefit on culture conversion. 
Another trial using rosuvastatin did not affect sputum culture conversion.
 
An atorvastatin phase IIA study did show a significant reduction in sputum mycobacterial load.
 The premise of faster conversion is therefore contested across trials.
- Secondary cases per index case of 0.3–1: **UNVERIFIABLE** here. It is plausible for high-burden settings but not sourced.
- 10 DALYs per secondary case: **PLAUSIBLE.** Menzies gives an average of 12.1 DALYs per incident case.
- Arithmetic: **VERIFIED.** 3.3M × 0.5 × 0.003 × 10 ≈ 49.5k; × 0.4 ≈ 20k. The net 0.1–1% follows from 1–5% × 10–20%. The 3k–150k range is unverified.

**EVIDENCE FOUND**
- Modelling sources that fit the Investigator's logic:
  - The shorter-regimen model (PMC4015982).
  - Dowdy-type pre-diagnosis transmission analyses (PMC9907102).
  - The infectiousness and effective-treatment review (PMC12054730).
- Shorter-regimen modelling treats on-treatment infectiousness as short-lived. This supports the idea that conversion speed after week 2 matters little.
- Counterweight to the Investigator's logic: a lung-sparing adjunct does not shorten diagnostic delay, which is the dominant transmission window. This reinforces the small-effect conclusion.

**OVERALL VERDICT: PARTIALLY VERIFIED**

**REVISED CRITIQUE:** Most transmission occurs before diagnosis, and infectiousness falls within days to weeks of effective treatment. Any transmission benefit from faster culture conversion is therefore small. This is supported by the transmission and modelling literature above. The numerical inputs (post-start transmission share of 1–5%, 10–20% reduction, 0.5 secondary cases) are unsourced and should be flagged **UNGROUNDED**. The central estimate of ~20k is a bounded order-of-magnitude figure, with real downside if the statin has no culture-conversion effect (ROSETTA found none). Consider lowering the central estimate toward ~10k or below, and widening the low end toward zero. Strength: low. This is a minor channel, and the thread label ("post-TB lung disease") does not match its content.

--- Critique: Transmission benefit is small, with a bounded calculation (~10–30k central) ---

## Critique 1: Post-TB lung disease morbidity (~55k central)

**CITATION CHECK**
- Menzies et al. 2021 (Lancet Glob Health 9:e1679–87): **VERIFIED, and the Investigator's baseline looks too low.**
  - 
The paper estimates 12.1 DALYs per incident TB case, of which 6.3 are from the disease episode and 5.8 from the post-TB period.
 That makes post-TB roughly half of lifetime burden. A later paper says it contributes 
up to 47% of the disease burden in DALYs.

  - 
Post-TB mortality and morbidity were both estimated from decreased lung function.
 The 5.8 DALYs therefore combine morbidity and premature death. I could not find the split in the sources retrieved.
  - 
28% of total DALYs accrue 15 or more years after incident TB.
 This supports the point that these are long-tail DALYs.
- International Post-TB Symposium and Allwood et al.: **PARTIALLY VERIFIED.** The symposium paper and Allwood's "The long shadow post-tuberculosis" exist (
"Post-tuberculosis lung health: perspectives from the First International Symposium"
). I did not check their prevalence figures in detail.

**CLAIM CHECK**
- Post-TB lung disease is common and long-lasting: **VERIFIED.** 
Reviews put respiratory impairment among TB survivors at 15–60%.
 The "~30% with meaningful impairment" input sits inside that range.
- Baseline of 0.75 DALYs per patient: **PLAUSIBLE but probably low.**
  - Menzies reports 5.8 post-TB DALYs per case, including deaths, against the Investigator's 0.75 for morbidity alone.
  - The morbidity-only share is unknown, so the gap cannot be quantified. It is likely large.
  - Menzies may also be discounted or modelled differently, which I did not check.
- Arithmetic: **VERIFIED.** 3.3M × 0.75 ≈ 2.5M, × 5% ≈ 124k, × 0.45 ≈ 56k. The high end of ~300k is also consistent.
- 5% reduction in long-term lung burden: **UNGROUNDED**, as the Investigator stated.
- "The trial's strongest signal was reduced lung damage": **UNVERIFIABLE, and possibly contradicted.** The source trial is not identified in my materials.
  - The ROSETTA trial (rosuvastatin) 
found no substantive benefit on culture conversion, on proportion of lung affected by chest x-ray, or on spirometry.

  - 
Its PET-CT sub-study also found no effect.

  - If the critique's premise comes from a different statin trial, such as StAT-TB with pravastatin, I found no published results to check it against. The premise needs confirming.
- Intervention-to-long-term link: **UNGROUNDED.** I found no long-term outcome data. A 2025 case-definition paper says 
the definition was developed without data on long-term patient outcomes.


**EVIDENCE FOUND**
- Menzies's 5.8 post-TB DALYs per case suggests the unvalued pool could be several times larger than 2.5M DALYs per adoption-year if the Investigator's baseline is raised. That would raise the ceiling, but not the central estimate unless the effect size is also supported.
- Double-counting risk with Critique 2: post-TB mortality is inside Menzies's post-TB DALYs. If baselines are taken from Menzies, Critiques 1 and 2 overlap.
- The convention flag is correct. Menzies shows a large share of DALYs accrue after 15 or more years, so discounting would cut this channel materially.

**OVERALL VERDICT: PARTIALLY VERIFIED**

**REVISED CRITIQUE:** Post-TB lung disease is a large, real burden. Menzies 2021 puts about 5.8 of 12.1 lifetime DALYs per case in the post-TB phase, and these are long-tail DALYs that discounting would cut. A BOTEC that assigns this channel zero value omits a potentially important term. The central estimate of ~55k rests on two unsupported inputs: the 5% effect size and the "lung damage signal" premise. The premise is **UNVERIFIED** and is contradicted by ROSETTA, which found no lung benefit on x-ray, spirometry or PET-CT. The 0.75 DALY baseline is probably too low compared with Menzies, though that source mixes morbidity and mortality. Keep the strength at medium-to-low, conditional on identifying which trial showed the lung signal. Report discounted and undiscounted versions. Avoid double-counting with Critique 2.

---

## Critique 2: Post-treatment excess mortality and life-expectancy adjustment

**CITATION CHECK**
- Romanowski et al. 2019 (Lancet Infect Dis 19:1129–37): **VERIFIED.**
  - It is a systematic review and meta-analysis of long-term all-cause mortality in people treated for TB.
  - Commentary describes 
TB survivors as having approximately three to four times the mortality of local populations.

  - The pooled figure is cited as 
2.91 (95% CI 2.21–3.84) times higher than in those who never had TB.

  - This fills in the number the Investigator could not recall. "A multiple of the general population's" is correct.

**CLAIM CHECK**
- Elevated post-treatment mortality: **VERIFIED.** A large 2025 Brazilian cohort also found 
an elevated natural-cause mortality risk in the treated cohort (RR 1.77, 95% CI 1.55–2.03).
 
Risk ratios were raised for respiratory deaths, among other causes.

- Respiratory disease as a major driver of excess deaths: **PARTIALLY VERIFIED.** One review states that 
respiratory diseases remain the leading cause of excess deaths in people who recover from TB.
 The 40% attributable share is not directly sourced. For comparison, Romanowski attributed 20% (95% CI 15–26) of the excess to cardiovascular disease (
per the Basham et al. discussion
). A respiratory share of 40% is therefore plausible but **UNGROUNDED**.
- ~10% cumulative excess mortality over 10 years: **PLAUSIBLE.** An SMR of ~2.9 on typical LMIC adult background mortality could give excess mortality of that order. The Investigator labelled this as illustrative.
- 5% intervention effect: **UNGROUNDED.**
- Arithmetic for (a): **VERIFIED.** 0.1 × 0.4 × 0.05 = 0.002; × 15 = 0.03; × 3.3M ≈ 99k; × 0.45 ≈ 45k. Part (b): 5–10% of 535k = 27–54k, which matches the stated −25k to −55k.
- Part (b), that rescued patients have worse residual life expectancy: **UNVERIFIABLE.** It is logically sound, since late diagnosis and immunocompromise raise the risk of lasting impairment (
per a Lancet ID commentary
). I found no quantification. The 5–10% overstatement is the Investigator's own figure.
- Statin cardiovascular benefit over about 6 months treated as zero: **PLAUSIBLE.** I did not verify it.

**EVIDENCE FOUND**
- Menzies's post-TB DALYs include post-TB mortality, so this channel overlaps with Critique 1 if both are added.
- Mortality is elevated in the Cerqueira-Silva cohort even in treated patients, supporting the existence of the excess-death pool but not the 40% lung share or the 5% effect.
- The net effect is unsigned. The Investigator's own conclusion that the two adjustments may cancel is reasonable.

**OVERALL VERDICT: PARTIALLY VERIFIED**

**REVISED CRITIQUE:** TB survivors have substantially elevated long-term mortality (pooled SMR ~2.9 in Romanowski 2019). Respiratory causes are a major contributor, but the 40% share is **UNGROUNDED**. The upside channel (~45k) depends on three unsupported inputs: a 5% effect, a 10% excess mortality, and a 40% respiratory share. Treat it as a flagged hypothesis with a wide range of roughly 0–50k. The downside life-expectancy adjustment is logically sound but its size is unquantified (**UNGROUNDED**). Treat the net as approximately zero with uncertain sign. Merge or net this against Critique 1 to avoid double-counting. Strength: low-to-medium.

---

## Critique 3: Transmission benefit (~10–30k central)

**CITATION CHECK**
No specific studies were cited. The Investigator asked the Verifier to find relevant modelling studies.

**CLAIM CHECK**
- Most transmission occurs before diagnosis and treatment start: **VERIFIED.** A review on infectiousness and treatment effect says 
most TB transmission occurs before diagnosis and effective treatment initiation.
 A Bayesian modelling study finds 
a disproportionate share of future transmission arises from undiagnosed smear-positive subclinical TB.

- Infectiousness falls quickly after effective therapy starts: **VERIFIED, with caveats.**
  - A population model of shorter regimens assumes 
bacillary burden drops rapidly and patients are non-infectious after the first two weeks.

  - The same review reports that 
30–40% of patients who produce cough aerosols rapidly become nonculturable after treatment initiation.

  - Human-to-guinea-pig experiments show a rapid effect of effective treatment on transmission.
  - However, 
the exact duration of infectiousness after treatment initiation remains uncertain and likely varies between individuals.
 A 1–5% post-start transmission share is directionally supported but not directly measured.
- Culture conversion at 8 weeks does not map one-to-one to infectiousness: **PLAUSIBLE.** Conversion at 8 weeks is a phase 2b efficacy endpoint (
usually measured at 2 months
). Infectiousness collapses much earlier than culture conversion, so the Investigator's discount is warranted.
- ROSETTA, a statin trial, found no benefit on culture conversion. 
Another trial using rosuvastatin did not affect sputum culture conversion.
 
An atorvastatin phase IIA study did show a significant reduction in sputum mycobacterial load.
 The premise of faster conversion is therefore contested across trials.
- Secondary cases per index case of 0.3–1: **UNVERIFIABLE** here. It is plausible for high-burden settings but not sourced.
- 10 DALYs per secondary case: **PLAUSIBLE.** Menzies gives an average of 12.1 DALYs per incident case.
- Arithmetic: **VERIFIED.** 3.3M × 0.5 × 0.003 × 10 ≈ 49.5k; × 0.4 ≈ 20k. The net 0.1–1% follows from 1–5% × 10–20%. The 3k–150k range is unverified.

**EVIDENCE FOUND**
- Modelling sources that fit the Investigator's logic:
  - The shorter-regimen model (PMC4015982).
  - Dowdy-type pre-diagnosis transmission analyses (PMC9907102).
  - The infectiousness and effective-treatment review (PMC12054730).
- Shorter-regimen modelling treats on-treatment infectiousness as short-lived. This supports the idea that conversion speed after week 2 matters little.
- Counterweight to the Investigator's logic: a lung-sparing adjunct does not shorten diagnostic delay, which is the dominant transmission window. This reinforces the small-effect conclusion.

**OVERALL VERDICT: PARTIALLY VERIFIED**

**REVISED CRITIQUE:** Most transmission occurs before diagnosis, and infectiousness falls within days to weeks of effective treatment. Any transmission benefit from faster culture conversion is therefore small. This is supported by the transmission and modelling literature above. The numerical inputs (post-start transmission share of 1–5%, 10–20% reduction, 0.5 secondary cases) are unsourced and should be flagged **UNGROUNDED**. The central estimate of ~20k is a bounded order-of-magnitude figure, with real downside if the statin has no culture-conversion effect (ROSETTA found none). Consider lowering the central estimate toward ~10k or below, and widening the low end toward zero. Strength: low. This is a minor channel, and the thread label ("post-TB lung disease") does not match its content.

--- Critique: The "lung benefit without mortality benefit" scenario is structurally less valuable than a simple p_success weighting implies ---

## Critique 1: "Lung benefit without mortality benefit" is worth less than a simple p_success weighting implies

**OVERALL VERDICT: UNVERIFIABLE on the empirical side, with the logic mostly sound (PARTIALLY VERIFIED).** The Investigator marked this UNGROUNDED, and I agree. I could not identify the specific trial or grant. I therefore could not check the Phase IIc or planned Phase III endpoints, the "3.3M patients" figure, or the 60% uptake assumption. The arithmetic mostly holds. The "increases" direction label is inconsistent with the argument.

**CLAIM CHECK**
- **Adoption in the lung-only branch is ≤10–20%:** UNVERIFIABLE. It is a judgment call, and no source on WHO guideline handling of lung-function surrogates turned up.
- **Realistic weighting adds ~0.02–0.06 to the 0.4 base:** VERIFIED as arithmetic. 0.6 × (0.3–0.5) × (0.1–0.2) = 0.018–0.06, so the total is about 0.42–0.46.
- **Naive weighting gives "up to ~2×":** PARTIALLY VERIFIED. At the stated inputs, 0.4 + 0.6 × (0.3–0.5) = 0.58–0.70, which is about 1.45–1.75× the base. "Up to ~2×" is a mild overstatement.
- **Conflation of terms:** MISLEADING WORDING. The text calls 0.6 the "60% uptake". In the formula, 0.6 is P(mortality fails), which is 1 − 0.4. These are different parameters.
- **Direction label:** FLAG. The argument says the lung channel is worth *less* than a naive weighting implies. That is a correction toward ~1×, not an increase. "Increases" only makes sense relative to the 0.4 base, and the size is negligible (+0.02–0.06).

**EVIDENCE FOUND**
- Lung function is a recognized preliminary-efficacy outcome in adjunctive host-directed therapy trials. A Phase 2 RCT of CC-11050 and everolimus 
suggests they might enhance recovery of FEV1, a measure of lung function and predictor of all-cause mortality
. This supports P(lung holds) being non-trivial. It says nothing about whether FEV1 alone would drive a WHO recommendation.
- I found no evidence on how WHO guideline groups weigh lung-function surrogates.

**REVISED CRITIQUE**
Treat this as a structural caveat, not a quantified adjustment. If the trial's registered endpoint is not lung function, a lung-only result probably earns a lower adoption probability than the main-case uptake. The 0.45 figure is arithmetically consistent with the Investigator's inputs. The 10–20% conditional adoption is UNGROUNDED. The direction should read "neutral to slightly decreases relative to a naive weighting". Magnitude is small, not medium.

---

## Critique 2: The sweat-based diagnostic has speculative option value (~10–30k)

**OVERALL VERDICT: PARTIALLY VERIFIED.** The hypothesis is plausible, and the key inputs are UNGROUNDED (as the Investigator said). New evidence on the counterfactual (WHO tongue-swab endorsement) strengthens the discount. I could not identify the specific sweat-based test funded alongside the trial.

**CLAIM CHECK**
- **"Roughly 2–3M TB cases per year undiagnosed or unreported":** VERIFIED. WHO reports 
8.3 million people diagnosed in 2024, 78% of estimated incident cases
. Incidence was 
an estimated 10.7 million
. The gap is therefore about 2.4M.
- **Sweat as a diagnostic biofluid:** PLAUSIBLE but early. A proteomic proof-of-concept found 
26 proteins exclusively detected in the sweat of active TB patients
. That study pooled specimens from 32 TB patients. A ClinicalTrials.gov study (NCT03667742) is examining sweat protein markers. Neither is the funded test, and I found nothing on its stage, accuracy or regulatory path. The broader sputum-free field is described as 
mostly at an early developmental phase
, which fits a low P(adoption).
- **Counterfactual non-sputum diagnostics are advancing:** VERIFIED, and stronger than the Investigator assumed.
  - WHO has now recommended 
near-point-of-care molecular tests, tongue swabs, and sputum pooling
.
  - Tongue swabs are meant for 
when sputum cannot be produced
. They are less sensitive than sputum, so they only partly displace a new test.
  - A multi-country evaluation found tongue-swab tests 
meet or exceed WHO minimum accuracy targets for near-POC non-sputum tests
.
  - This directly targets the "people who can't produce sputum" population. It supports a lower incremental-yield estimate (1–3% of incidence is possibly generous).
  - Urine-LAM as a competitor is not confirmed by my searches. It is background knowledge, not verified here.
- **Calculation:** VERIFIED as arithmetic. 0.05 × 200k × 5 = 50k. The step from 50k to "10–30k" is a 0.2–0.6 discount with no stated derivation.
- **5 DALYs per additional case (20% CFR × 25 DALYs):** UNVERIFIED. I did not check the untreated case-fatality rate. Published untreated CFRs may be higher, so this input could be conservative.
- **Units:** FLAG. The 50k figure is "per year", but the headline "10–30k central" doesn't say whether it is annual or total.
- **Cost-inclusion consistency point:** UNVERIFIABLE without the grant documents. If the $7M cost includes the diagnostic's funding, the omission biases against the intervention. If it doesn't, treating it separately is defensible.

**EVIDENCE FOUND**
- Tongue-swab and NPOC-NAAT recommendations came in early 2026. A WHO and Stop TB toolkit followed in 
May 2026
. Both push toward lower incremental value for any new non-sputum test.
- WHO reports 
almost 100 diagnostic products in development
 as of August 2025. This reinforces crowding.

**REVISED CRITIQUE**
CG assigns zero value to the sweat diagnostic. The unaddressed gap in non-notified cases (~2.4M/yr) is real. The incremental value is low and uncertain. WHO's 2026 tongue-swab and NPOC recommendations substantially weaken the counterfactual. The ~10–30k figure is UNGROUNDED and should be treated as an illustrative upper-range option value. Direction is "uncertain" and leans neutral-to-negative given the new evidence. Magnitude is small. The cost-inclusion question must be settled against CG's actual cost model.

---

## Critique 3: 60% steady-state uptake has no precedent among comparable TB program additions

**OVERALL VERDICT: PARTIALLY VERIFIED.** The core claim is supported. TB program additions often scale slowly, and the 4-month regimen and WRD examples hold up. The title ("no precedent") is overstated, because the best-documented analog is near, not far below, 60%. The dexamethasone and pyridoxine examples are unverified. The Investigator's WRD recollection ("roughly 40–50%") is slightly low.

**CITATION CHECK**
- **WHO Global TB Report, WRD as initial test:** VERIFIED, with a correction. 
In 2024, a WRD was the initial test for 54% (4.5 million) of 8.3 million people newly diagnosed, up from 48%
. The Investigator's "roughly 40–50%" is outdated. Xpert was endorsed in 2010, so about 14 years in, global coverage is ~54%.
- **Country heterogeneity:** In 2023, 
68 countries reached at least 80%, but coverage was under 20% in 25 countries
. That is a bimodal pattern, not a uniform ceiling. In 2024, 
37 of 49 high-burden countries reported WRD use as the initial test for more than half of people newly diagnosed
. The global target is 
100% by 2027
.
- **4HPMZ (WHO 2022):** VERIFIED. The 2022 guideline is confirmed. One source states 
global uptake has been slow, largely due to implementation challenges including limited worldwide availability of rifapentine
. A Lancet Global Health paper also called rollout 
limited in high-burden settings
. A US program evaluation found only 
14% of eligible patients prescribed 4-HPMZ, and 36% of those initiating completed treatment
.
- **Dexamethasone for TBM (evidence 2004) and pyridoxine with isoniazid:** UNVERIFIED. I found no coverage data. Corticosteroids are 
"standard for TB meningitis"
 in clinical practice, but that says nothing about coverage.
- **GDF/HPMZ order data:** NOT FOUND.

**CLAIM CHECK**
- **"Comparable additions often take many years to reach moderate coverage":** VERIFIED for WRD (14 years to 54%) and 4HPMZ.
- **"Some stall below 50%":** PARTIALLY VERIFIED. 4HPMZ is well below 50%. WRD is at 54%, not below 50%.
- **The 4HPMZ analogy is imperfect.** Its slow uptake is driven mainly by rifapentine supply, adverse events and a high pill burden. A cheap generic adjunct isn't supply-constrained in the same way. The Investigator's claim that an adjunct is a "harder sell" than regimens that simplify care is a reasonable inference, but it is inference.
- **WRD is also an imperfect analog.** It needs instruments, cartridges and labs. A generic pill avoids that infrastructure barrier.
- **"60% has no precedent":** FALSE as worded. The WRD benchmark (54% after 14 years, with many countries above 80%) suggests 60% is reachable but optimistic on a short horizon. "Plausibly an upper-bound or optimistic-case value" is defensible. "No precedent" is not.
- **Arithmetic:** VERIFIED. Cutting the ceiling from 60% to 40% or 30% reduces SROI by 33% or 50% under linear scaling. The "materiality line is 0.39" is internal to the model and unverifiable here.
- **"Ceiling matters more than ramp":** PLAUSIBLE. It is logically sound for an undiscounted infinite horizon. The Investigator acknowledges the caveats (finite horizon, incidence decline, discounting).

**EVIDENCE FOUND**
- WRD coverage rose in 24 African countries 
from 37% in 2018 to 58% in 2023
. That is about 4 percentage points per year, a useful ramp-rate benchmark.
- WHO's Guideline Development Group framed the 4-month regimen as an option whose uptake would grow 
"in future as uptake of this regimen improves"
. This shows WHO itself anticipated gradual uptake.

**REVISED CRITIQUE**
CG's 60% steady-state uptake looks optimistic relative to TB program precedent. The strongest verified analogs are WRD at 54% global coverage after ~14 years (heavily skewed by country) and 4HPMZ with slow, supply- and tolerability-limited uptake. Neither is a clean analog for a cheap generic adjunct. Reducing the ceiling to 0.30–0.40 cuts SROI by about 33–50% under linear scaling. The 60% figure is a plausible optimistic or upper-central case, not an impossible one. The dexamethasone and pyridoxine examples should be dropped or flagged as UNVERIFIED. Direction is "decreases". Magnitude is medium to large, but the evidence supports the ceiling being uncertain rather than demonstrably too high. I would rate the critique's strength as moderate. Pulling country-level adoption data for comparable adjuncts would strengthen it.

--- Critique: The sweat-based diagnostic carries real option value but is speculative (~10–30k central) ---

## Critique 1: "Lung benefit without mortality benefit" is worth less than a simple p_success weighting implies

**OVERALL VERDICT: UNVERIFIABLE on the empirical side, with the logic mostly sound (PARTIALLY VERIFIED).** The Investigator marked this UNGROUNDED, and I agree. I could not identify the specific trial or grant. I therefore could not check the Phase IIc or planned Phase III endpoints, the "3.3M patients" figure, or the 60% uptake assumption. The arithmetic mostly holds. The "increases" direction label is inconsistent with the argument.

**CLAIM CHECK**
- **Adoption in the lung-only branch is ≤10–20%:** UNVERIFIABLE. It is a judgment call, and no source on WHO guideline handling of lung-function surrogates turned up.
- **Realistic weighting adds ~0.02–0.06 to the 0.4 base:** VERIFIED as arithmetic. 0.6 × (0.3–0.5) × (0.1–0.2) = 0.018–0.06, so the total is about 0.42–0.46.
- **Naive weighting gives "up to ~2×":** PARTIALLY VERIFIED. At the stated inputs, 0.4 + 0.6 × (0.3–0.5) = 0.58–0.70, which is about 1.45–1.75× the base. "Up to ~2×" is a mild overstatement.
- **Conflation of terms:** MISLEADING WORDING. The text calls 0.6 the "60% uptake". In the formula, 0.6 is P(mortality fails), which is 1 − 0.4. These are different parameters.
- **Direction label:** FLAG. The argument says the lung channel is worth *less* than a naive weighting implies. That is a correction toward ~1×, not an increase. "Increases" only makes sense relative to the 0.4 base, and the size is negligible (+0.02–0.06).

**EVIDENCE FOUND**
- Lung function is a recognized preliminary-efficacy outcome in adjunctive host-directed therapy trials. A Phase 2 RCT of CC-11050 and everolimus 
suggests they might enhance recovery of FEV1, a measure of lung function and predictor of all-cause mortality
. This supports P(lung holds) being non-trivial. It says nothing about whether FEV1 alone would drive a WHO recommendation.
- I found no evidence on how WHO guideline groups weigh lung-function surrogates.

**REVISED CRITIQUE**
Treat this as a structural caveat, not a quantified adjustment. If the trial's registered endpoint is not lung function, a lung-only result probably earns a lower adoption probability than the main-case uptake. The 0.45 figure is arithmetically consistent with the Investigator's inputs. The 10–20% conditional adoption is UNGROUNDED. The direction should read "neutral to slightly decreases relative to a naive weighting". Magnitude is small, not medium.

---

## Critique 2: The sweat-based diagnostic has speculative option value (~10–30k)

**OVERALL VERDICT: PARTIALLY VERIFIED.** The hypothesis is plausible, and the key inputs are UNGROUNDED (as the Investigator said). New evidence on the counterfactual (WHO tongue-swab endorsement) strengthens the discount. I could not identify the specific sweat-based test funded alongside the trial.

**CLAIM CHECK**
- **"Roughly 2–3M TB cases per year undiagnosed or unreported":** VERIFIED. WHO reports 
8.3 million people diagnosed in 2024, 78% of estimated incident cases
. Incidence was 
an estimated 10.7 million
. The gap is therefore about 2.4M.
- **Sweat as a diagnostic biofluid:** PLAUSIBLE but early. A proteomic proof-of-concept found 
26 proteins exclusively detected in the sweat of active TB patients
. That study pooled specimens from 32 TB patients. A ClinicalTrials.gov study (NCT03667742) is examining sweat protein markers. Neither is the funded test, and I found nothing on its stage, accuracy or regulatory path. The broader sputum-free field is described as 
mostly at an early developmental phase
, which fits a low P(adoption).
- **Counterfactual non-sputum diagnostics are advancing:** VERIFIED, and stronger than the Investigator assumed.
  - WHO has now recommended 
near-point-of-care molecular tests, tongue swabs, and sputum pooling
.
  - Tongue swabs are meant for 
when sputum cannot be produced
. They are less sensitive than sputum, so they only partly displace a new test.
  - A multi-country evaluation found tongue-swab tests 
meet or exceed WHO minimum accuracy targets for near-POC non-sputum tests
.
  - This directly targets the "people who can't produce sputum" population. It supports a lower incremental-yield estimate (1–3% of incidence is possibly generous).
  - Urine-LAM as a competitor is not confirmed by my searches. It is background knowledge, not verified here.
- **Calculation:** VERIFIED as arithmetic. 0.05 × 200k × 5 = 50k. The step from 50k to "10–30k" is a 0.2–0.6 discount with no stated derivation.
- **5 DALYs per additional case (20% CFR × 25 DALYs):** UNVERIFIED. I did not check the untreated case-fatality rate. Published untreated CFRs may be higher, so this input could be conservative.
- **Units:** FLAG. The 50k figure is "per year", but the headline "10–30k central" doesn't say whether it is annual or total.
- **Cost-inclusion consistency point:** UNVERIFIABLE without the grant documents. If the $7M cost includes the diagnostic's funding, the omission biases against the intervention. If it doesn't, treating it separately is defensible.

**EVIDENCE FOUND**
- Tongue-swab and NPOC-NAAT recommendations came in early 2026. A WHO and Stop TB toolkit followed in 
May 2026
. Both push toward lower incremental value for any new non-sputum test.
- WHO reports 
almost 100 diagnostic products in development
 as of August 2025. This reinforces crowding.

**REVISED CRITIQUE**
CG assigns zero value to the sweat diagnostic. The unaddressed gap in non-notified cases (~2.4M/yr) is real. The incremental value is low and uncertain. WHO's 2026 tongue-swab and NPOC recommendations substantially weaken the counterfactual. The ~10–30k figure is UNGROUNDED and should be treated as an illustrative upper-range option value. Direction is "uncertain" and leans neutral-to-negative given the new evidence. Magnitude is small. The cost-inclusion question must be settled against CG's actual cost model.

---

## Critique 3: 60% steady-state uptake has no precedent among comparable TB program additions

**OVERALL VERDICT: PARTIALLY VERIFIED.** The core claim is supported. TB program additions often scale slowly, and the 4-month regimen and WRD examples hold up. The title ("no precedent") is overstated, because the best-documented analog is near, not far below, 60%. The dexamethasone and pyridoxine examples are unverified. The Investigator's WRD recollection ("roughly 40–50%") is slightly low.

**CITATION CHECK**
- **WHO Global TB Report, WRD as initial test:** VERIFIED, with a correction. 
In 2024, a WRD was the initial test for 54% (4.5 million) of 8.3 million people newly diagnosed, up from 48%
. The Investigator's "roughly 40–50%" is outdated. Xpert was endorsed in 2010, so about 14 years in, global coverage is ~54%.
- **Country heterogeneity:** In 2023, 
68 countries reached at least 80%, but coverage was under 20% in 25 countries
. That is a bimodal pattern, not a uniform ceiling. In 2024, 
37 of 49 high-burden countries reported WRD use as the initial test for more than half of people newly diagnosed
. The global target is 
100% by 2027
.
- **4HPMZ (WHO 2022):** VERIFIED. The 2022 guideline is confirmed. One source states 
global uptake has been slow, largely due to implementation challenges including limited worldwide availability of rifapentine
. A Lancet Global Health paper also called rollout 
limited in high-burden settings
. A US program evaluation found only 
14% of eligible patients prescribed 4-HPMZ, and 36% of those initiating completed treatment
.
- **Dexamethasone for TBM (evidence 2004) and pyridoxine with isoniazid:** UNVERIFIED. I found no coverage data. Corticosteroids are 
"standard for TB meningitis"
 in clinical practice, but that says nothing about coverage.
- **GDF/HPMZ order data:** NOT FOUND.

**CLAIM CHECK**
- **"Comparable additions often take many years to reach moderate coverage":** VERIFIED for WRD (14 years to 54%) and 4HPMZ.
- **"Some stall below 50%":** PARTIALLY VERIFIED. 4HPMZ is well below 50%. WRD is at 54%, not below 50%.
- **The 4HPMZ analogy is imperfect.** Its slow uptake is driven mainly by rifapentine supply, adverse events and a high pill burden. A cheap generic adjunct isn't supply-constrained in the same way. The Investigator's claim that an adjunct is a "harder sell" than regimens that simplify care is a reasonable inference, but it is inference.
- **WRD is also an imperfect analog.** It needs instruments, cartridges and labs. A generic pill avoids that infrastructure barrier.
- **"60% has no precedent":** FALSE as worded. The WRD benchmark (54% after 14 years, with many countries above 80%) suggests 60% is reachable but optimistic on a short horizon. "Plausibly an upper-bound or optimistic-case value" is defensible. "No precedent" is not.
- **Arithmetic:** VERIFIED. Cutting the ceiling from 60% to 40% or 30% reduces SROI by 33% or 50% under linear scaling. The "materiality line is 0.39" is internal to the model and unverifiable here.
- **"Ceiling matters more than ramp":** PLAUSIBLE. It is logically sound for an undiscounted infinite horizon. The Investigator acknowledges the caveats (finite horizon, incidence decline, discounting).

**EVIDENCE FOUND**
- WRD coverage rose in 24 African countries 
from 37% in 2018 to 58% in 2023
. That is about 4 percentage points per year, a useful ramp-rate benchmark.
- WHO's Guideline Development Group framed the 4-month regimen as an option whose uptake would grow 
"in future as uptake of this regimen improves"
. This shows WHO itself anticipated gradual uptake.

**REVISED CRITIQUE**
CG's 60% steady-state uptake looks optimistic relative to TB program precedent. The strongest verified analogs are WRD at 54% global coverage after ~14 years (heavily skewed by country) and 4HPMZ with slow, supply- and tolerability-limited uptake. Neither is a clean analog for a cheap generic adjunct. Reducing the ceiling to 0.30–0.40 cuts SROI by about 33–50% under linear scaling. The 60% figure is a plausible optimistic or upper-central case, not an impossible one. The dexamethasone and pyridoxine examples should be dropped or flagged as UNVERIFIED. Direction is "decreases". Magnitude is medium to large, but the evidence supports the ceiling being uncertain rather than demonstrably too high. I would rate the critique's strength as moderate. Pulling country-level adoption data for comparable adjuncts would strengthen it.

--- Critique: 60% steady-state uptake has no precedent among comparable TB program additions ---

## Critique 1: "Lung benefit without mortality benefit" is worth less than a simple p_success weighting implies

**OVERALL VERDICT: UNVERIFIABLE on the empirical side, with the logic mostly sound (PARTIALLY VERIFIED).** The Investigator marked this UNGROUNDED, and I agree. I could not identify the specific trial or grant. I therefore could not check the Phase IIc or planned Phase III endpoints, the "3.3M patients" figure, or the 60% uptake assumption. The arithmetic mostly holds. The "increases" direction label is inconsistent with the argument.

**CLAIM CHECK**
- **Adoption in the lung-only branch is ≤10–20%:** UNVERIFIABLE. It is a judgment call, and no source on WHO guideline handling of lung-function surrogates turned up.
- **Realistic weighting adds ~0.02–0.06 to the 0.4 base:** VERIFIED as arithmetic. 0.6 × (0.3–0.5) × (0.1–0.2) = 0.018–0.06, so the total is about 0.42–0.46.
- **Naive weighting gives "up to ~2×":** PARTIALLY VERIFIED. At the stated inputs, 0.4 + 0.6 × (0.3–0.5) = 0.58–0.70, which is about 1.45–1.75× the base. "Up to ~2×" is a mild overstatement.
- **Conflation of terms:** MISLEADING WORDING. The text calls 0.6 the "60% uptake". In the formula, 0.6 is P(mortality fails), which is 1 − 0.4. These are different parameters.
- **Direction label:** FLAG. The argument says the lung channel is worth *less* than a naive weighting implies. That is a correction toward ~1×, not an increase. "Increases" only makes sense relative to the 0.4 base, and the size is negligible (+0.02–0.06).

**EVIDENCE FOUND**
- Lung function is a recognized preliminary-efficacy outcome in adjunctive host-directed therapy trials. A Phase 2 RCT of CC-11050 and everolimus 
suggests they might enhance recovery of FEV1, a measure of lung function and predictor of all-cause mortality
. This supports P(lung holds) being non-trivial. It says nothing about whether FEV1 alone would drive a WHO recommendation.
- I found no evidence on how WHO guideline groups weigh lung-function surrogates.

**REVISED CRITIQUE**
Treat this as a structural caveat, not a quantified adjustment. If the trial's registered endpoint is not lung function, a lung-only result probably earns a lower adoption probability than the main-case uptake. The 0.45 figure is arithmetically consistent with the Investigator's inputs. The 10–20% conditional adoption is UNGROUNDED. The direction should read "neutral to slightly decreases relative to a naive weighting". Magnitude is small, not medium.

---

## Critique 2: The sweat-based diagnostic has speculative option value (~10–30k)

**OVERALL VERDICT: PARTIALLY VERIFIED.** The hypothesis is plausible, and the key inputs are UNGROUNDED (as the Investigator said). New evidence on the counterfactual (WHO tongue-swab endorsement) strengthens the discount. I could not identify the specific sweat-based test funded alongside the trial.

**CLAIM CHECK**
- **"Roughly 2–3M TB cases per year undiagnosed or unreported":** VERIFIED. WHO reports 
8.3 million people diagnosed in 2024, 78% of estimated incident cases
. Incidence was 
an estimated 10.7 million
. The gap is therefore about 2.4M.
- **Sweat as a diagnostic biofluid:** PLAUSIBLE but early. A proteomic proof-of-concept found 
26 proteins exclusively detected in the sweat of active TB patients
. That study pooled specimens from 32 TB patients. A ClinicalTrials.gov study (NCT03667742) is examining sweat protein markers. Neither is the funded test, and I found nothing on its stage, accuracy or regulatory path. The broader sputum-free field is described as 
mostly at an early developmental phase
, which fits a low P(adoption).
- **Counterfactual non-sputum diagnostics are advancing:** VERIFIED, and stronger than the Investigator assumed.
  - WHO has now recommended 
near-point-of-care molecular tests, tongue swabs, and sputum pooling
.
  - Tongue swabs are meant for 
when sputum cannot be produced
. They are less sensitive than sputum, so they only partly displace a new test.
  - A multi-country evaluation found tongue-swab tests 
meet or exceed WHO minimum accuracy targets for near-POC non-sputum tests
.
  - This directly targets the "people who can't produce sputum" population. It supports a lower incremental-yield estimate (1–3% of incidence is possibly generous).
  - Urine-LAM as a competitor is not confirmed by my searches. It is background knowledge, not verified here.
- **Calculation:** VERIFIED as arithmetic. 0.05 × 200k × 5 = 50k. The step from 50k to "10–30k" is a 0.2–0.6 discount with no stated derivation.
- **5 DALYs per additional case (20% CFR × 25 DALYs):** UNVERIFIED. I did not check the untreated case-fatality rate. Published untreated CFRs may be higher, so this input could be conservative.
- **Units:** FLAG. The 50k figure is "per year", but the headline "10–30k central" doesn't say whether it is annual or total.
- **Cost-inclusion consistency point:** UNVERIFIABLE without the grant documents. If the $7M cost includes the diagnostic's funding, the omission biases against the intervention. If it doesn't, treating it separately is defensible.

**EVIDENCE FOUND**
- Tongue-swab and NPOC-NAAT recommendations came in early 2026. A WHO and Stop TB toolkit followed in 
May 2026
. Both push toward lower incremental value for any new non-sputum test.
- WHO reports 
almost 100 diagnostic products in development
 as of August 2025. This reinforces crowding.

**REVISED CRITIQUE**
CG assigns zero value to the sweat diagnostic. The unaddressed gap in non-notified cases (~2.4M/yr) is real. The incremental value is low and uncertain. WHO's 2026 tongue-swab and NPOC recommendations substantially weaken the counterfactual. The ~10–30k figure is UNGROUNDED and should be treated as an illustrative upper-range option value. Direction is "uncertain" and leans neutral-to-negative given the new evidence. Magnitude is small. The cost-inclusion question must be settled against CG's actual cost model.

---

## Critique 3: 60% steady-state uptake has no precedent among comparable TB program additions

**OVERALL VERDICT: PARTIALLY VERIFIED.** The core claim is supported. TB program additions often scale slowly, and the 4-month regimen and WRD examples hold up. The title ("no precedent") is overstated, because the best-documented analog is near, not far below, 60%. The dexamethasone and pyridoxine examples are unverified. The Investigator's WRD recollection ("roughly 40–50%") is slightly low.

**CITATION CHECK**
- **WHO Global TB Report, WRD as initial test:** VERIFIED, with a correction. 
In 2024, a WRD was the initial test for 54% (4.5 million) of 8.3 million people newly diagnosed, up from 48%
. The Investigator's "roughly 40–50%" is outdated. Xpert was endorsed in 2010, so about 14 years in, global coverage is ~54%.
- **Country heterogeneity:** In 2023, 
68 countries reached at least 80%, but coverage was under 20% in 25 countries
. That is a bimodal pattern, not a uniform ceiling. In 2024, 
37 of 49 high-burden countries reported WRD use as the initial test for more than half of people newly diagnosed
. The global target is 
100% by 2027
.
- **4HPMZ (WHO 2022):** VERIFIED. The 2022 guideline is confirmed. One source states 
global uptake has been slow, largely due to implementation challenges including limited worldwide availability of rifapentine
. A Lancet Global Health paper also called rollout 
limited in high-burden settings
. A US program evaluation found only 
14% of eligible patients prescribed 4-HPMZ, and 36% of those initiating completed treatment
.
- **Dexamethasone for TBM (evidence 2004) and pyridoxine with isoniazid:** UNVERIFIED. I found no coverage data. Corticosteroids are 
"standard for TB meningitis"
 in clinical practice, but that says nothing about coverage.
- **GDF/HPMZ order data:** NOT FOUND.

**CLAIM CHECK**
- **"Comparable additions often take many years to reach moderate coverage":** VERIFIED for WRD (14 years to 54%) and 4HPMZ.
- **"Some stall below 50%":** PARTIALLY VERIFIED. 4HPMZ is well below 50%. WRD is at 54%, not below 50%.
- **The 4HPMZ analogy is imperfect.** Its slow uptake is driven mainly by rifapentine supply, adverse events and a high pill burden. A cheap generic adjunct isn't supply-constrained in the same way. The Investigator's claim that an adjunct is a "harder sell" than regimens that simplify care is a reasonable inference, but it is inference.
- **WRD is also an imperfect analog.** It needs instruments, cartridges and labs. A generic pill avoids that infrastructure barrier.
- **"60% has no precedent":** FALSE as worded. The WRD benchmark (54% after 14 years, with many countries above 80%) suggests 60% is reachable but optimistic on a short horizon. "Plausibly an upper-bound or optimistic-case value" is defensible. "No precedent" is not.
- **Arithmetic:** VERIFIED. Cutting the ceiling from 60% to 40% or 30% reduces SROI by 33% or 50% under linear scaling. The "materiality line is 0.39" is internal to the model and unverifiable here.
- **"Ceiling matters more than ramp":** PLAUSIBLE. It is logically sound for an undiscounted infinite horizon. The Investigator acknowledges the caveats (finite horizon, incidence decline, discounting).

**EVIDENCE FOUND**
- WRD coverage rose in 24 African countries 
from 37% in 2018 to 58% in 2023
. That is about 4 percentage points per year, a useful ramp-rate benchmark.
- WHO's Guideline Development Group framed the 4-month regimen as an option whose uptake would grow 
"in future as uptake of this regimen improves"
. This shows WHO itself anticipated gradual uptake.

**REVISED CRITIQUE**
CG's 60% steady-state uptake looks optimistic relative to TB program precedent. The strongest verified analogs are WRD at 54% global coverage after ~14 years (heavily skewed by country) and 4HPMZ with slow, supply- and tolerability-limited uptake. Neither is a clean analog for a cheap generic adjunct. Reducing the ceiling to 0.30–0.40 cuts SROI by about 33–50% under linear scaling. The 60% figure is a plausible optimistic or upper-central case, not an impossible one. The dexamethasone and pyridoxine examples should be dropped or flagged as UNVERIFIED. Direction is "decreases". Magnitude is medium to large, but the evidence supports the ceiling being uncertain rather than demonstrably too high. I would rate the critique's strength as moderate. Pulling country-level adoption data for comparable adjuncts would strengthen it.

--- Critique: A Phase III cannot be powered on mortality, so the WHO GDG would be recommending on surrogate or composite endpoints ---

## Critique 1: A Phase III cannot be powered on mortality, so the WHO GDG would be recommending on surrogate or composite endpoints

**OVERALL VERDICT: PARTIALLY VERIFIED.** The statistical argument and the GRADE mechanism are sound. The baseline mortality figure and the size of the uptake effect remain ungrounded.

**CLAIM CHECK**
- **Sample size of about 30,000 per arm: VERIFIED (arithmetic).**
  - The Investigator's formula gives about 29,800.
  - The standard two-proportion formula (5% vs 4.5%, alpha 0.05 two-sided, 80% power) gives about 28,400 per arm.
  - Both round to roughly 30,000, so the conclusion holds. It depends entirely on the 5% baseline and 10% relative reduction.
- **GRADE downgrades for indirectness when a surrogate stands in for a patient-important outcome: VERIFIED.**
  - 
GRADE guidance says that when a surrogate is used, authors should rate down the quality of evidence for indirectness of outcome.

  - WHO's own SAGE guidance lists 
surrogate end-points as an example of indirectness.

  - WHO guidelines that follow the WHO handbook define indirectness as including 
differences in populations, interventions, comparisons or outcomes of interest between the research and the target context.

  - WHO's DR-TB guidelines also 
list indirectness among the criteria for rating certainty down.

  - I could not retrieve the handbook text itself. The claim is supported through WHO documents that apply it.
- **On-treatment DS-TB mortality of about 3–6%: UNVERIFIABLE in this session.**
  - My search for WHO Global TB Report treatment-outcome data failed.
  - From background knowledge the range is plausible, but I have no citation.
  - It still needs sourcing.
- **The realistic Phase III will use culture conversion, relapse-free cure, unfavorable outcome or lung function: PLAUSIBLE.**
  - Existing statin and host-directed-therapy trials use surrogate endpoints.
  - 
An atorvastatin phase IIA study measured mycobacterial load in sputum, and a rosuvastatin trial measured sputum culture conversion.

  - A phase 2 host-directed-therapy trial used 
recovery of FEV1.

- **Lower uptake, a delayed or conditional recommendation, or subgroup-only recommendations: PLAUSIBLE but UNGROUNDED.**
  - The "a third of patients, so uptake cut by half or more" scenario is self-labelled speculative, and I found nothing to confirm or refute it.
  - I also could not check CG's "if it works → 60%" figure or the claim that CG's value is "entirely mortality-based." Those come from the source materials.

**EVIDENCE FOUND**
- The GRADE downgrade applies specifically to the mortality outcome. If the Phase III reports unfavorable outcome, which includes death, WHO TB guidelines have historically treated treatment outcomes as critical outcomes. A recommendation therefore need not stall. It would simply carry a "mortality benefit not directly shown" caveat. This weakens the "delay" pathway and leaves the "modeled benefit is unverified" pathway intact.
- The sample-size problem is worse for a trial restricted to a high-risk subgroup, because the trial then enrolls fewer patients.

**REVISED CRITIQUE**
A Phase III powered on mortality is infeasible. About 28,000–30,000 per arm would be needed at a 5% baseline and 10% relative reduction, and both inputs are assumptions. The trial will likely use a surrogate or composite endpoint. GRADE and WHO methods support downgrading the mortality evidence for indirectness. The realized mortality effect, and so relative_reduction variance, stays unverified. Effects on adoption timing and uptake are plausible but unquantified.
- **Flag:** the baseline mortality figure is UNGROUNDED and needs a WHO Global TB Report source.
- **Flag:** the uptake magnitude is speculative.
- **Strength:** medium, perhaps medium-low for the uptake channel.

---

## Critique 2: Clinical eligibility and monitoring barriers cap the achievable prescribing share

**OVERALL VERDICT: PARTIALLY VERIFIED.** The pharmacology and DILI premises are real, and the DILI incidence is understated. The eligibility-exclusion shares are ungrounded, as the Investigator said.

**CLAIM CHECK**
- **Anti-TB DILI affects a non-trivial minority, "low single digits to ~10%": VERIFIED but the range is too narrow.**
  - A recent review reports 
a global incidence of 11.5%, with rates from 2% to 28%.

  - Another review gives 
2.55 to 36.75%, depending on definitions, populations and regimens.

  - 
Among TB/HIV-coinfected patients, 37% developed liver injury after starting anti-TB treatment.

  - A recent cohort found a much lower 
2.1% (13/610).
 This shows how much the definition matters.
  - Overall the evidence supports the critique, and the upper bound is more severe than stated.
- **Rifampicin lowers atorvastatin exposure: VERIFIED.**
  - A crossover study found 
rifampin reduced atorvastatin acid AUC by 80%.

  - The interaction is two-sided. 
A single rifamycin dose raises atorvastatin exposure by inhibiting OATP1B1/1B3, but after multiple doses induction dominates and AUC falls.

  - The label advises 
simultaneous co-administration of atorvastatin and rifampin.

- **PI-based ART raises atorvastatin and efavirenz lowers it: VERIFIED.**
  - The label table shows 
tipranavir/ritonavir raised atorvastatin AUC about 9.4-fold.

  - The label also 
names efavirenz among CYP3A inducers that can variably reduce atorvastatin concentrations.

  - I did not access the Liverpool database.
- **Statin label cautions on liver disease and transaminases: PLAUSIBLE.** I did not retrieve the label text for this point, but it is standard.
- **Statins "historically avoided in pregnancy": PLAUSIBLE.**
  - My search on this failed.
  - From background knowledge, the FDA asked in 2021 for removal of the blanket pregnancy contraindication.
  - The word "historically" is therefore appropriate, but the exclusion should not be treated as absolute for current labels.
- **LFTs are not routinely done for DS-TB in many NTPs: PLAUSIBLE, UNVERIFIED.** The DILI literature recommends 
regular liver function monitoring during anti-TB treatment.
 That does not show what programs actually do.
- **Arithmetic: UNGROUNDED and slightly loose.** Excluding 10–20% from 0.60 gives 0.48–0.54. Reaching 0.45–0.50 needs an extra program-adoption factor of about 0.9, which is not stated.

**EVIDENCE FOUND**
- The existing statin-in-TB trials are small and short. One example is 
rosuvastatin 10 mg daily for 8 weeks with standard HRZE.

- Trial eligibility criteria will probably exclude liver disease, so any recommendation would inherit those exclusions.
- The choice of statin matters. Atorvastatin is heavily CYP3A4-dependent, and CG's candidate is in the source materials, which I could not check. A less CYP3A4-dependent statin would soften the ART and rifamycin interaction arguments, though not the DILI-attribution argument.

**REVISED CRITIQUE**
Eligibility and monitoring barriers plausibly reduce adult_uptake. Supported premises:
- Anti-TB DILI is common. The pooled estimate is about 11.5%, and it is much higher in some settings and in HIV coinfection.
- Rifamycin, PI and efavirenz interactions with atorvastatin are documented.
- A statin adds a confounder when attributing liver injury.

**Flags:**
- The 10–20% exclusion share and the 0.45–0.50 figure are UNGROUNDED and the arithmetic is incomplete.
- The NTP LFT-monitoring gap is unsourced.
- The pregnancy exclusion should be stated with current label status.

**Strength:** medium. The direction is well supported, but the magnitude is not.

---

## Critique 3: Delivered dose and adherence diverge from trial conditions, notably with rifapentine regimens

**OVERALL VERDICT: PARTIALLY VERIFIED.** The adherence and dose-transfer logic holds. The rifapentine claim is overstated: the evidence does not show it is a stronger inducer than rifampicin. Its main point, that rifamycin induction reduces statin exposure, is supported.

**CLAIM CHECK**
- **Rifapentine is a CYP3A4 inducer "comparable to or stronger than rifampicin in some dosing contexts": PARTIALLY VERIFIED / PARTLY MISREPRESENTED.**
  - A pharmacology review ranks the inductive potency of rifamycins as 
rifampin > rifapentine > rifabutin.

  - It adds that 
rifapentine's induction approaches 85–100% of rifampin's when used daily and is more moderate with once- or twice-weekly dosing.

  - A diabetes-focused review rates rifapentine's induction magnitude as 
"++" against "+++" for rifampicin.

  - In human hepatocytes, 
the potency hierarchy was rifampin > rifabutin > rifapentine.

  - "Comparable at daily dosing" is defensible. "Stronger" is not supported by anything I found.
  - The critique's differential argument also fails. Rifapentine is not shown to reduce atorvastatin exposure more than rifampicin does, so HPMZ regimens are not worse than HRZE for statin exposure. They are about equally affected.
- **Rifamycin co-administration lowers atorvastatin exposure: VERIFIED.** See Critique 2 (about 80% AUC reduction with rifampin).
- **Rifapentine–atorvastatin interaction magnitude: UNVERIFIABLE.**
  - I found no direct study.
  - Rifapentine's induction may be 
delayed in onset but may persist beyond the end of treatment.
 That could matter for statin dosing timing.
- **Dose-finding on a rifampicin-based regimen: PLAUSIBLE.** The visible statin trials use HRZE as the backbone, for example the 
rosuvastatin phase 2b.
 The Phase IIc design itself is in the source materials, which I could not check.
- **A shorter 4-month window shortens the co-administration period: LOGICAL but conditional.** It would not matter if the statin course is about 8 weeks, as in existing trials. That depends on CG's design.
- **Adjunct pills are less adherent than anti-TB drugs, and general statin adherence is poor: UNVERIFIABLE here.**
  - I did not search for this.
  - It is widely reported in general populations, but the transfer to a 6-month TB course is an assumption.
  - The Investigator admits having no TB-specific source.
- **Arithmetic: VERIFIED.** 0.60 × 0.70 = 0.42, a 30% reduction.
- **Internal error:** the text says the effect "compounds with Critiques 1 and 3." This should read Critiques 1 and 2.
- **HPMZ is "currently small but growing": UNVERIFIED.**

**EVIDENCE FOUND**
- Rifamycin-driven statin exposure reduction is a stronger point against the dose-transfer assumption than the HPMZ-specific argument. Even in HRZE regimens the interaction is large and variable between patients. Dose selection in Phase IIc already has to account for it. Whether it carries over to HPMZ depends on whether rifapentine is dosed daily, since the induction estimates above are for daily use.
- Pravastatin showed variable rifampicin interaction, with 
AUC at 50% or less in five of ten subjects.
 The statin choice therefore changes the size of this problem.

**REVISED CRITIQUE**
Two separate concerns remain:
1. **Adherence and delivered dose.** Real-world adherence to an out-of-FDC adjunct plausibly falls below trial adherence. Illustratively, 70% adherence would cut effective uptake from 0.60 to 0.42. The 70% figure is a framing assumption, not data, and the TB-specific adherence evidence is UNGROUNDED. This part keeps medium strength.
2. **Rifamycin interaction and dose transfer.** Rifamycins substantially lower atorvastatin exposure. Daily rifapentine induces CYP3A4 at roughly 85–100% of rifampicin's level. Intermittent dosing induces less. A dose chosen on one rifamycin regimen may not transfer exactly to another, and rifapentine's induction effect may persist after treatment ends. The claim that rifapentine is "stronger" than rifampicin should be dropped, and the interaction should not be presented as specifically worse in HPMZ. The rifapentine magnitude is UNGROUNDED. Reduce this part to **low** strength.

Overall strength: medium for adherence and low-to-medium for the rifapentine component. The reference to "Critique 3" in the compounding sentence should be corrected to Critique 2.

**Limits of this verification:** my search quota ran out before I could check the FDA pregnancy label change, WHO treatment-outcome mortality data, statin adherence literature and HPMZ uptake. Those items are flagged above as unverified rather than refuted.

--- Critique: Clinical eligibility and monitoring barriers cap the achievable prescribing share below the "generic and cheap" logic ---

## Critique 1: A Phase III cannot be powered on mortality, so the WHO GDG would be recommending on surrogate or composite endpoints

**OVERALL VERDICT: PARTIALLY VERIFIED.** The statistical argument and the GRADE mechanism are sound. The baseline mortality figure and the size of the uptake effect remain ungrounded.

**CLAIM CHECK**
- **Sample size of about 30,000 per arm: VERIFIED (arithmetic).**
  - The Investigator's formula gives about 29,800.
  - The standard two-proportion formula (5% vs 4.5%, alpha 0.05 two-sided, 80% power) gives about 28,400 per arm.
  - Both round to roughly 30,000, so the conclusion holds. It depends entirely on the 5% baseline and 10% relative reduction.
- **GRADE downgrades for indirectness when a surrogate stands in for a patient-important outcome: VERIFIED.**
  - 
GRADE guidance says that when a surrogate is used, authors should rate down the quality of evidence for indirectness of outcome.

  - WHO's own SAGE guidance lists 
surrogate end-points as an example of indirectness.

  - WHO guidelines that follow the WHO handbook define indirectness as including 
differences in populations, interventions, comparisons or outcomes of interest between the research and the target context.

  - WHO's DR-TB guidelines also 
list indirectness among the criteria for rating certainty down.

  - I could not retrieve the handbook text itself. The claim is supported through WHO documents that apply it.
- **On-treatment DS-TB mortality of about 3–6%: UNVERIFIABLE in this session.**
  - My search for WHO Global TB Report treatment-outcome data failed.
  - From background knowledge the range is plausible, but I have no citation.
  - It still needs sourcing.
- **The realistic Phase III will use culture conversion, relapse-free cure, unfavorable outcome or lung function: PLAUSIBLE.**
  - Existing statin and host-directed-therapy trials use surrogate endpoints.
  - 
An atorvastatin phase IIA study measured mycobacterial load in sputum, and a rosuvastatin trial measured sputum culture conversion.

  - A phase 2 host-directed-therapy trial used 
recovery of FEV1.

- **Lower uptake, a delayed or conditional recommendation, or subgroup-only recommendations: PLAUSIBLE but UNGROUNDED.**
  - The "a third of patients, so uptake cut by half or more" scenario is self-labelled speculative, and I found nothing to confirm or refute it.
  - I also could not check CG's "if it works → 60%" figure or the claim that CG's value is "entirely mortality-based." Those come from the source materials.

**EVIDENCE FOUND**
- The GRADE downgrade applies specifically to the mortality outcome. If the Phase III reports unfavorable outcome, which includes death, WHO TB guidelines have historically treated treatment outcomes as critical outcomes. A recommendation therefore need not stall. It would simply carry a "mortality benefit not directly shown" caveat. This weakens the "delay" pathway and leaves the "modeled benefit is unverified" pathway intact.
- The sample-size problem is worse for a trial restricted to a high-risk subgroup, because the trial then enrolls fewer patients.

**REVISED CRITIQUE**
A Phase III powered on mortality is infeasible. About 28,000–30,000 per arm would be needed at a 5% baseline and 10% relative reduction, and both inputs are assumptions. The trial will likely use a surrogate or composite endpoint. GRADE and WHO methods support downgrading the mortality evidence for indirectness. The realized mortality effect, and so relative_reduction variance, stays unverified. Effects on adoption timing and uptake are plausible but unquantified.
- **Flag:** the baseline mortality figure is UNGROUNDED and needs a WHO Global TB Report source.
- **Flag:** the uptake magnitude is speculative.
- **Strength:** medium, perhaps medium-low for the uptake channel.

---

## Critique 2: Clinical eligibility and monitoring barriers cap the achievable prescribing share

**OVERALL VERDICT: PARTIALLY VERIFIED.** The pharmacology and DILI premises are real, and the DILI incidence is understated. The eligibility-exclusion shares are ungrounded, as the Investigator said.

**CLAIM CHECK**
- **Anti-TB DILI affects a non-trivial minority, "low single digits to ~10%": VERIFIED but the range is too narrow.**
  - A recent review reports 
a global incidence of 11.5%, with rates from 2% to 28%.

  - Another review gives 
2.55 to 36.75%, depending on definitions, populations and regimens.

  - 
Among TB/HIV-coinfected patients, 37% developed liver injury after starting anti-TB treatment.

  - A recent cohort found a much lower 
2.1% (13/610).
 This shows how much the definition matters.
  - Overall the evidence supports the critique, and the upper bound is more severe than stated.
- **Rifampicin lowers atorvastatin exposure: VERIFIED.**
  - A crossover study found 
rifampin reduced atorvastatin acid AUC by 80%.

  - The interaction is two-sided. 
A single rifamycin dose raises atorvastatin exposure by inhibiting OATP1B1/1B3, but after multiple doses induction dominates and AUC falls.

  - The label advises 
simultaneous co-administration of atorvastatin and rifampin.

- **PI-based ART raises atorvastatin and efavirenz lowers it: VERIFIED.**
  - The label table shows 
tipranavir/ritonavir raised atorvastatin AUC about 9.4-fold.

  - The label also 
names efavirenz among CYP3A inducers that can variably reduce atorvastatin concentrations.

  - I did not access the Liverpool database.
- **Statin label cautions on liver disease and transaminases: PLAUSIBLE.** I did not retrieve the label text for this point, but it is standard.
- **Statins "historically avoided in pregnancy": PLAUSIBLE.**
  - My search on this failed.
  - From background knowledge, the FDA asked in 2021 for removal of the blanket pregnancy contraindication.
  - The word "historically" is therefore appropriate, but the exclusion should not be treated as absolute for current labels.
- **LFTs are not routinely done for DS-TB in many NTPs: PLAUSIBLE, UNVERIFIED.** The DILI literature recommends 
regular liver function monitoring during anti-TB treatment.
 That does not show what programs actually do.
- **Arithmetic: UNGROUNDED and slightly loose.** Excluding 10–20% from 0.60 gives 0.48–0.54. Reaching 0.45–0.50 needs an extra program-adoption factor of about 0.9, which is not stated.

**EVIDENCE FOUND**
- The existing statin-in-TB trials are small and short. One example is 
rosuvastatin 10 mg daily for 8 weeks with standard HRZE.

- Trial eligibility criteria will probably exclude liver disease, so any recommendation would inherit those exclusions.
- The choice of statin matters. Atorvastatin is heavily CYP3A4-dependent, and CG's candidate is in the source materials, which I could not check. A less CYP3A4-dependent statin would soften the ART and rifamycin interaction arguments, though not the DILI-attribution argument.

**REVISED CRITIQUE**
Eligibility and monitoring barriers plausibly reduce adult_uptake. Supported premises:
- Anti-TB DILI is common. The pooled estimate is about 11.5%, and it is much higher in some settings and in HIV coinfection.
- Rifamycin, PI and efavirenz interactions with atorvastatin are documented.
- A statin adds a confounder when attributing liver injury.

**Flags:**
- The 10–20% exclusion share and the 0.45–0.50 figure are UNGROUNDED and the arithmetic is incomplete.
- The NTP LFT-monitoring gap is unsourced.
- The pregnancy exclusion should be stated with current label status.

**Strength:** medium. The direction is well supported, but the magnitude is not.

---

## Critique 3: Delivered dose and adherence diverge from trial conditions, notably with rifapentine regimens

**OVERALL VERDICT: PARTIALLY VERIFIED.** The adherence and dose-transfer logic holds. The rifapentine claim is overstated: the evidence does not show it is a stronger inducer than rifampicin. Its main point, that rifamycin induction reduces statin exposure, is supported.

**CLAIM CHECK**
- **Rifapentine is a CYP3A4 inducer "comparable to or stronger than rifampicin in some dosing contexts": PARTIALLY VERIFIED / PARTLY MISREPRESENTED.**
  - A pharmacology review ranks the inductive potency of rifamycins as 
rifampin > rifapentine > rifabutin.

  - It adds that 
rifapentine's induction approaches 85–100% of rifampin's when used daily and is more moderate with once- or twice-weekly dosing.

  - A diabetes-focused review rates rifapentine's induction magnitude as 
"++" against "+++" for rifampicin.

  - In human hepatocytes, 
the potency hierarchy was rifampin > rifabutin > rifapentine.

  - "Comparable at daily dosing" is defensible. "Stronger" is not supported by anything I found.
  - The critique's differential argument also fails. Rifapentine is not shown to reduce atorvastatin exposure more than rifampicin does, so HPMZ regimens are not worse than HRZE for statin exposure. They are about equally affected.
- **Rifamycin co-administration lowers atorvastatin exposure: VERIFIED.** See Critique 2 (about 80% AUC reduction with rifampin).
- **Rifapentine–atorvastatin interaction magnitude: UNVERIFIABLE.**
  - I found no direct study.
  - Rifapentine's induction may be 
delayed in onset but may persist beyond the end of treatment.
 That could matter for statin dosing timing.
- **Dose-finding on a rifampicin-based regimen: PLAUSIBLE.** The visible statin trials use HRZE as the backbone, for example the 
rosuvastatin phase 2b.
 The Phase IIc design itself is in the source materials, which I could not check.
- **A shorter 4-month window shortens the co-administration period: LOGICAL but conditional.** It would not matter if the statin course is about 8 weeks, as in existing trials. That depends on CG's design.
- **Adjunct pills are less adherent than anti-TB drugs, and general statin adherence is poor: UNVERIFIABLE here.**
  - I did not search for this.
  - It is widely reported in general populations, but the transfer to a 6-month TB course is an assumption.
  - The Investigator admits having no TB-specific source.
- **Arithmetic: VERIFIED.** 0.60 × 0.70 = 0.42, a 30% reduction.
- **Internal error:** the text says the effect "compounds with Critiques 1 and 3." This should read Critiques 1 and 2.
- **HPMZ is "currently small but growing": UNVERIFIED.**

**EVIDENCE FOUND**
- Rifamycin-driven statin exposure reduction is a stronger point against the dose-transfer assumption than the HPMZ-specific argument. Even in HRZE regimens the interaction is large and variable between patients. Dose selection in Phase IIc already has to account for it. Whether it carries over to HPMZ depends on whether rifapentine is dosed daily, since the induction estimates above are for daily use.
- Pravastatin showed variable rifampicin interaction, with 
AUC at 50% or less in five of ten subjects.
 The statin choice therefore changes the size of this problem.

**REVISED CRITIQUE**
Two separate concerns remain:
1. **Adherence and delivered dose.** Real-world adherence to an out-of-FDC adjunct plausibly falls below trial adherence. Illustratively, 70% adherence would cut effective uptake from 0.60 to 0.42. The 70% figure is a framing assumption, not data, and the TB-specific adherence evidence is UNGROUNDED. This part keeps medium strength.
2. **Rifamycin interaction and dose transfer.** Rifamycins substantially lower atorvastatin exposure. Daily rifapentine induces CYP3A4 at roughly 85–100% of rifampicin's level. Intermittent dosing induces less. A dose chosen on one rifamycin regimen may not transfer exactly to another, and rifapentine's induction effect may persist after treatment ends. The claim that rifapentine is "stronger" than rifampicin should be dropped, and the interaction should not be presented as specifically worse in HPMZ. The rifapentine magnitude is UNGROUNDED. Reduce this part to **low** strength.

Overall strength: medium for adherence and low-to-medium for the rifapentine component. The reference to "Critique 3" in the compounding sentence should be corrected to Critique 2.

**Limits of this verification:** my search quota ran out before I could check the FDA pregnancy label change, WHO treatment-outcome mortality data, statin adherence literature and HPMZ uptake. Those items are flagged above as unverified rather than refuted.

--- Critique: Effective delivered dose and adherence diverge from trial conditions, and programmatic dose may be lower than the trial dose, notably with rifapentine regimens ---

## Critique 1: A Phase III cannot be powered on mortality, so the WHO GDG would be recommending on surrogate or composite endpoints

**OVERALL VERDICT: PARTIALLY VERIFIED.** The statistical argument and the GRADE mechanism are sound. The baseline mortality figure and the size of the uptake effect remain ungrounded.

**CLAIM CHECK**
- **Sample size of about 30,000 per arm: VERIFIED (arithmetic).**
  - The Investigator's formula gives about 29,800.
  - The standard two-proportion formula (5% vs 4.5%, alpha 0.05 two-sided, 80% power) gives about 28,400 per arm.
  - Both round to roughly 30,000, so the conclusion holds. It depends entirely on the 5% baseline and 10% relative reduction.
- **GRADE downgrades for indirectness when a surrogate stands in for a patient-important outcome: VERIFIED.**
  - 
GRADE guidance says that when a surrogate is used, authors should rate down the quality of evidence for indirectness of outcome.

  - WHO's own SAGE guidance lists 
surrogate end-points as an example of indirectness.

  - WHO guidelines that follow the WHO handbook define indirectness as including 
differences in populations, interventions, comparisons or outcomes of interest between the research and the target context.

  - WHO's DR-TB guidelines also 
list indirectness among the criteria for rating certainty down.

  - I could not retrieve the handbook text itself. The claim is supported through WHO documents that apply it.
- **On-treatment DS-TB mortality of about 3–6%: UNVERIFIABLE in this session.**
  - My search for WHO Global TB Report treatment-outcome data failed.
  - From background knowledge the range is plausible, but I have no citation.
  - It still needs sourcing.
- **The realistic Phase III will use culture conversion, relapse-free cure, unfavorable outcome or lung function: PLAUSIBLE.**
  - Existing statin and host-directed-therapy trials use surrogate endpoints.
  - 
An atorvastatin phase IIA study measured mycobacterial load in sputum, and a rosuvastatin trial measured sputum culture conversion.

  - A phase 2 host-directed-therapy trial used 
recovery of FEV1.

- **Lower uptake, a delayed or conditional recommendation, or subgroup-only recommendations: PLAUSIBLE but UNGROUNDED.**
  - The "a third of patients, so uptake cut by half or more" scenario is self-labelled speculative, and I found nothing to confirm or refute it.
  - I also could not check CG's "if it works → 60%" figure or the claim that CG's value is "entirely mortality-based." Those come from the source materials.

**EVIDENCE FOUND**
- The GRADE downgrade applies specifically to the mortality outcome. If the Phase III reports unfavorable outcome, which includes death, WHO TB guidelines have historically treated treatment outcomes as critical outcomes. A recommendation therefore need not stall. It would simply carry a "mortality benefit not directly shown" caveat. This weakens the "delay" pathway and leaves the "modeled benefit is unverified" pathway intact.
- The sample-size problem is worse for a trial restricted to a high-risk subgroup, because the trial then enrolls fewer patients.

**REVISED CRITIQUE**
A Phase III powered on mortality is infeasible. About 28,000–30,000 per arm would be needed at a 5% baseline and 10% relative reduction, and both inputs are assumptions. The trial will likely use a surrogate or composite endpoint. GRADE and WHO methods support downgrading the mortality evidence for indirectness. The realized mortality effect, and so relative_reduction variance, stays unverified. Effects on adoption timing and uptake are plausible but unquantified.
- **Flag:** the baseline mortality figure is UNGROUNDED and needs a WHO Global TB Report source.
- **Flag:** the uptake magnitude is speculative.
- **Strength:** medium, perhaps medium-low for the uptake channel.

---

## Critique 2: Clinical eligibility and monitoring barriers cap the achievable prescribing share

**OVERALL VERDICT: PARTIALLY VERIFIED.** The pharmacology and DILI premises are real, and the DILI incidence is understated. The eligibility-exclusion shares are ungrounded, as the Investigator said.

**CLAIM CHECK**
- **Anti-TB DILI affects a non-trivial minority, "low single digits to ~10%": VERIFIED but the range is too narrow.**
  - A recent review reports 
a global incidence of 11.5%, with rates from 2% to 28%.

  - Another review gives 
2.55 to 36.75%, depending on definitions, populations and regimens.

  - 
Among TB/HIV-coinfected patients, 37% developed liver injury after starting anti-TB treatment.

  - A recent cohort found a much lower 
2.1% (13/610).
 This shows how much the definition matters.
  - Overall the evidence supports the critique, and the upper bound is more severe than stated.
- **Rifampicin lowers atorvastatin exposure: VERIFIED.**
  - A crossover study found 
rifampin reduced atorvastatin acid AUC by 80%.

  - The interaction is two-sided. 
A single rifamycin dose raises atorvastatin exposure by inhibiting OATP1B1/1B3, but after multiple doses induction dominates and AUC falls.

  - The label advises 
simultaneous co-administration of atorvastatin and rifampin.

- **PI-based ART raises atorvastatin and efavirenz lowers it: VERIFIED.**
  - The label table shows 
tipranavir/ritonavir raised atorvastatin AUC about 9.4-fold.

  - The label also 
names efavirenz among CYP3A inducers that can variably reduce atorvastatin concentrations.

  - I did not access the Liverpool database.
- **Statin label cautions on liver disease and transaminases: PLAUSIBLE.** I did not retrieve the label text for this point, but it is standard.
- **Statins "historically avoided in pregnancy": PLAUSIBLE.**
  - My search on this failed.
  - From background knowledge, the FDA asked in 2021 for removal of the blanket pregnancy contraindication.
  - The word "historically" is therefore appropriate, but the exclusion should not be treated as absolute for current labels.
- **LFTs are not routinely done for DS-TB in many NTPs: PLAUSIBLE, UNVERIFIED.** The DILI literature recommends 
regular liver function monitoring during anti-TB treatment.
 That does not show what programs actually do.
- **Arithmetic: UNGROUNDED and slightly loose.** Excluding 10–20% from 0.60 gives 0.48–0.54. Reaching 0.45–0.50 needs an extra program-adoption factor of about 0.9, which is not stated.

**EVIDENCE FOUND**
- The existing statin-in-TB trials are small and short. One example is 
rosuvastatin 10 mg daily for 8 weeks with standard HRZE.

- Trial eligibility criteria will probably exclude liver disease, so any recommendation would inherit those exclusions.
- The choice of statin matters. Atorvastatin is heavily CYP3A4-dependent, and CG's candidate is in the source materials, which I could not check. A less CYP3A4-dependent statin would soften the ART and rifamycin interaction arguments, though not the DILI-attribution argument.

**REVISED CRITIQUE**
Eligibility and monitoring barriers plausibly reduce adult_uptake. Supported premises:
- Anti-TB DILI is common. The pooled estimate is about 11.5%, and it is much higher in some settings and in HIV coinfection.
- Rifamycin, PI and efavirenz interactions with atorvastatin are documented.
- A statin adds a confounder when attributing liver injury.

**Flags:**
- The 10–20% exclusion share and the 0.45–0.50 figure are UNGROUNDED and the arithmetic is incomplete.
- The NTP LFT-monitoring gap is unsourced.
- The pregnancy exclusion should be stated with current label status.

**Strength:** medium. The direction is well supported, but the magnitude is not.

---

## Critique 3: Delivered dose and adherence diverge from trial conditions, notably with rifapentine regimens

**OVERALL VERDICT: PARTIALLY VERIFIED.** The adherence and dose-transfer logic holds. The rifapentine claim is overstated: the evidence does not show it is a stronger inducer than rifampicin. Its main point, that rifamycin induction reduces statin exposure, is supported.

**CLAIM CHECK**
- **Rifapentine is a CYP3A4 inducer "comparable to or stronger than rifampicin in some dosing contexts": PARTIALLY VERIFIED / PARTLY MISREPRESENTED.**
  - A pharmacology review ranks the inductive potency of rifamycins as 
rifampin > rifapentine > rifabutin.

  - It adds that 
rifapentine's induction approaches 85–100% of rifampin's when used daily and is more moderate with once- or twice-weekly dosing.

  - A diabetes-focused review rates rifapentine's induction magnitude as 
"++" against "+++" for rifampicin.

  - In human hepatocytes, 
the potency hierarchy was rifampin > rifabutin > rifapentine.

  - "Comparable at daily dosing" is defensible. "Stronger" is not supported by anything I found.
  - The critique's differential argument also fails. Rifapentine is not shown to reduce atorvastatin exposure more than rifampicin does, so HPMZ regimens are not worse than HRZE for statin exposure. They are about equally affected.
- **Rifamycin co-administration lowers atorvastatin exposure: VERIFIED.** See Critique 2 (about 80% AUC reduction with rifampin).
- **Rifapentine–atorvastatin interaction magnitude: UNVERIFIABLE.**
  - I found no direct study.
  - Rifapentine's induction may be 
delayed in onset but may persist beyond the end of treatment.
 That could matter for statin dosing timing.
- **Dose-finding on a rifampicin-based regimen: PLAUSIBLE.** The visible statin trials use HRZE as the backbone, for example the 
rosuvastatin phase 2b.
 The Phase IIc design itself is in the source materials, which I could not check.
- **A shorter 4-month window shortens the co-administration period: LOGICAL but conditional.** It would not matter if the statin course is about 8 weeks, as in existing trials. That depends on CG's design.
- **Adjunct pills are less adherent than anti-TB drugs, and general statin adherence is poor: UNVERIFIABLE here.**
  - I did not search for this.
  - It is widely reported in general populations, but the transfer to a 6-month TB course is an assumption.
  - The Investigator admits having no TB-specific source.
- **Arithmetic: VERIFIED.** 0.60 × 0.70 = 0.42, a 30% reduction.
- **Internal error:** the text says the effect "compounds with Critiques 1 and 3." This should read Critiques 1 and 2.
- **HPMZ is "currently small but growing": UNVERIFIED.**

**EVIDENCE FOUND**
- Rifamycin-driven statin exposure reduction is a stronger point against the dose-transfer assumption than the HPMZ-specific argument. Even in HRZE regimens the interaction is large and variable between patients. Dose selection in Phase IIc already has to account for it. Whether it carries over to HPMZ depends on whether rifapentine is dosed daily, since the induction estimates above are for daily use.
- Pravastatin showed variable rifampicin interaction, with 
AUC at 50% or less in five of ten subjects.
 The statin choice therefore changes the size of this problem.

**REVISED CRITIQUE**
Two separate concerns remain:
1. **Adherence and delivered dose.** Real-world adherence to an out-of-FDC adjunct plausibly falls below trial adherence. Illustratively, 70% adherence would cut effective uptake from 0.60 to 0.42. The 70% figure is a framing assumption, not data, and the TB-specific adherence evidence is UNGROUNDED. This part keeps medium strength.
2. **Rifamycin interaction and dose transfer.** Rifamycins substantially lower atorvastatin exposure. Daily rifapentine induces CYP3A4 at roughly 85–100% of rifampicin's level. Intermittent dosing induces less. A dose chosen on one rifamycin regimen may not transfer exactly to another, and rifapentine's induction effect may persist after treatment ends. The claim that rifapentine is "stronger" than rifampicin should be dropped, and the interaction should not be presented as specifically worse in HPMZ. The rifapentine magnitude is UNGROUNDED. Reduce this part to **low** strength.

Overall strength: medium for adherence and low-to-medium for the rifapentine component. The reference to "Critique 3" in the compounding sentence should be corrected to Critique 2.

**Limits of this verification:** my search quota ran out before I could check the FDA pregnancy label change, WHO treatment-outcome mortality data, statin adherence literature and HPMZ uptake. Those items are flagged above as unverified rather than refuted.

--- Critique: Private-sector treatment share and the reach of national guidelines are not modeled ---

## Critique 1: Private-sector treatment share and the reach of national guidelines are not modeled

**OVERALL VERDICT: PARTIALLY VERIFIED.** The hypothesis is sound and the one number the Investigator gave is accurate. The direction and the 5–15% magnitude are inference only and stay flagged as such. The claim that private providers "may not use FDCs" and the claim about what drives private-sector uptake are not supported by anything I found.

**CLAIM CHECK**
- **India's private-sector notifications are "roughly a third" of the total: VERIFIED.**
  - 
In 2023 the private sector accounted for 33% (0.84 million) of total notifications.

  - The Government of India's WHO statement gives 
30% in 2022 and 32% in 2023.

  - The Investigator's "UNGROUNDED as to numbers" label can be dropped for India.
- **A large share of DS-TB care happens in the private sector (India, Indonesia, Pakistan, Philippines): VERIFIED.**
  - In India, 
more than 50% of patients seek initial care from private providers.

  - Another source notes that 
in Pakistan, the Philippines and Indonesia, most first-contact care happens in the private sector.

  - The 2019 Global TB Report's PPM trend data are patchy. A WHO private-engagement document says 
reporting on private-sector notifications from countries remains highly inconsistent.

- **Unnotified or "missing" cases are a large share in the same countries: PARTIALLY VERIFIED, and outdated for India.**
  - WHO's 2025 report says the largest notification gaps in 2024 were 
Indonesia (10%), India (8.8%), the Philippines (7.5%), Pakistan (7.2%) and China (6.9%) of the global gap.

  - India's own gap has shrunk sharply, 
from 1.2 million missed notifications in 2015 to 0.3 million in 2023.

  - The "missing cases never see the guideline" argument is therefore stronger for Indonesia, the Philippines and Pakistan than for India now.
- **Private providers frequently deviate from national guidelines: PLAUSIBLE, with a caveat on what the evidence covers.**
  - Standardized-patient studies show poor adherence at the diagnostic and management stage. Correct management was seen in 
959 of 2,602 interactions (37%) in Mumbai and Patna.

  - In Mumbai, 
correct management against national guidelines was 75% in the public sector versus 35% in the private sector.

  - Those studies measure testing and referral, not regimen, dosing or FDC use. For regimens, a Chennai survey concluded that 
TB management practices in India's urban private sector are heterogeneous and often suboptimal.

  - The same paper reports that 
over three-quarters of providers in a systematic review prescribed a regimen potentially consistent with ISTC guidelines for new patients.
 That cuts against a strong "non-standard dosing" claim. Treatment-regimen deviation is therefore only moderately supported.
- **"May not use FDCs": UNVERIFIABLE.** I found nothing on FDC use in the private sector.
- **Uptake in the private sector depends on professional societies, pharma marketing and mandatory notification rather than NTP procurement: PARTIALLY VERIFIED.**
  - India's mechanisms include 
mandatory notification by gazette, incentives, PPSA and collaboration with professional bodies such as the IMA.

  - Private-sector drug sales are large, and one source notes that 
enormous quantities of TB drugs are sold in the Indian private market.

  - I found no evidence on pharma marketing as a driver of guideline uptake.
- **Net effect of about 5–15% of the benefit: UNGROUNDED.** This is the Investigator's inference, as they stated.

**EVIDENCE FOUND**
- **Undermining or complicating:** Notified private patients are increasingly inside the programme. A 2025 analysis reports that private-sector engagement models improved 
"TB notification and drug uptake"
 in India. For notified private patients, the "NTP procurement doesn't reach them" premise is therefore weaker.
- **Supporting:** Notification itself remains incomplete. An older estimate put private-provider notifications at 
only 22% of the estimated cases treated in that sector
 across Bangladesh, India, Indonesia and Myanmar.
- **Sign ambiguity:** The Investigator's point that the sign could flip is reasonable. Private providers show high use of adjunct tests such as chest X-rays and antibiotics (see the Mumbai study).

**REVISED CRITIQUE:** A substantial share of DS-TB care in the highest-burden countries is private. India's private notifications are about 30–33% of the total, and more than half of patients first seek care privately. Sector-specific guideline adherence is documented for diagnosis and management but not clearly for regimen or dosing. The model uses a single uptake figure across public, notified-private and unnotified-private settings. Whether this lowers effective uptake is uncertain. The direction is probably down but could be neutral or positive in some countries. The 5–15% magnitude is UNGROUNDED. Missing-case data support the argument for Indonesia, the Philippines and Pakistan more than for India. **Strength: low-to-medium.**

---

## Critique 2: Zero modeled lag between Phase III completion and adoption; speedup assumes trial timing is the binding constraint

**OVERALL VERDICT: PARTIALLY VERIFIED.** The core logic holds. One factual detail is wrong: WHO guidance on the HPMZ regimen did not wait until 2022. The Xpert details come from my own background knowledge and I could not check them in this session.

**CITATION CHECK**
- **Study 31/A5349 published 2021: VERIFIED.** 
Detailed results were published on 6 May 2021.
 The NEJM reference is 
N Engl J Med 2021;384:1705–18.

- **"WHO guidance followed in 2022": MISREPRESENTED / imprecise.**
  - Topline results were presented in October 2020, and 
WHO welcomed them at the Union World Conference.

  - WHO 
convened a GDG meeting on 27–30 April 2021.
 It then issued a "Rapid Communication" in June 2021, roughly one month after publication and about eight months after topline data.
  - A fully integrated guideline update came later, which I believe was 2022. I did not confirm that date here.
  - This supports the Investigator's point that the WHO step can be short. It also shows the "WHO guidance followed in 2022" wording is wrong.
- **Xpert WHO endorsement in 2010, with many years of implementation afterwards: NOT CHECKED.** From background knowledge the endorsement was December 2010. I did not verify it by search.
- **Albert et al. and Cazabon et al.: NOT CHECKED.** The Investigator also hadn't confirmed their findings.

**CLAIM CHECK**
- **WHO step is short on a rapid-communication path: VERIFIED** (timeline above).
- **National adoption and procurement take additional years: PLAUSIBLE, with partial support.** The WHO rapid communication itself said wider uptake 
would be more feasible if the cost of rifapentine is reduced.
 That points to cost and procurement as the bottleneck, not the guideline.
- **A generic drug has no commercial sponsor, so Phase III funding could be the gating constraint: PLAUSIBLE.** This is logical inference. I found no empirical evidence either way.
- **Added years of lag reduce benefit by about 2% per year, so 3–5 years is roughly 6–10%: UNVERIFIABLE.** The 2% rate comes from the model's formula, which I haven't seen. The arithmetic is internally consistent.
- **Lumpiness alone doesn't lower expected speedup under uniform timing: LOGICALLY SOUND.** This is a good self-correction by the Investigator.
- **TB trials with 12–24 month relapse follow-up often slip: PLAUSIBLE.** This is general knowledge. No specific slippage data were retrieved.

**EVIDENCE FOUND**
- WHO acted fast once data existed. The delay lay in trial execution and rapid generation of results, and in downstream access. That supports the point that the binding constraint is not WHO guideline convening.
- Study 31/A5349 is described as 
the first 4-month regimen endorsed by both WHO and the U.S.
 (CDC). I include this only as context on the endorsement path.

**REVISED CRITIQUE:** The model sets lag between Phase III completion and adoption at zero. The HPMZ precedent shows WHO endorsement can follow within about a month of publication (June 2021 rapid communication, after a May 2021 NEJM publication). It also shows that practical uptake was constrained by drug cost and availability, not by WHO. An expected speedup below one year per year of Phase IIc acceleration depends on the trial not being the critical path. Phase III funding for a generic is a plausible but ungrounded gating factor. The lag-cost arithmetic depends on the unverified formula. The Xpert precedent is unverified. **Strength: low-to-medium.** The lag piece is modest, and the "not on the critical path" piece is the more important one but is ungrounded.

---

## Critique 3: Survivors' excess mortality and comorbidity shrink the 27 DALYs per death

**OVERALL VERDICT: PARTIALLY VERIFIED.** The citation is real and the SMR figure is approximately right. The Gompertz arithmetic is correct. Two points could not be checked: how "27" was derived and the "17.7 threshold" are both internal to the source model. The effect size depends heavily on those, so the "large" rating is only conditionally supported.

**CITATION CHECK**
- **Romanowski et al. 2019, Lancet Infect Dis: VERIFIED.** It is 
Romanowski K, Baumann B, Basham CA, et al., Lancet Infect Dis 2019;19:1129–1137
, and it is a systematic review and meta-analysis. The DOI is 10.1016/S1473-3099(19)30309-3.
- **Pooled SMR "roughly 3–4": PARTIALLY VERIFIED, slightly high at the low end.**
  - A later article reports that the review 
found the force of mortality for TB survivors to be 2.91 (95% CI 2.21–3.84) times higher than in those who never had TB.

  - The accompanying Lancet ID comment summarizes it as 
approximately three-times to four-times greater mortality than local populations, including among younger adults.

  - Using "about 3" is fine. "3–4" matches the commentary but overstates the pooled point estimate.

**CLAIM CHECK**
- **TB patients carry high rates of smoking, alcohol use, diabetes, undernutrition and HIV: VERIFIED.** A Lancet seminar says 
progression to disease is higher in people with undernourishment, immunosuppression, or who smoke, drink alcohol, or have diabetes.
 A Georgia, USA cohort found that 
HIV co-infection, excess alcohol use, diabetes and end-stage renal disease were associated with post-treatment death.

- **Post-TB lung damage drives excess mortality: VERIFIED.** A Lancet Global Health review states that 
respiratory diseases remain the leading cause of excess deaths in people who recover from TB, with mortality three to six times that of local peers.

- **Gompertz arithmetic: VERIFIED.** ln(3) ≈ 1.10. Dividing by 0.09–0.10 gives about 11–12 years of effective ageing, as stated. Whether b ≈ 0.09–0.10 applies to LMIC adult mortality was not checked. It is roughly standard for adult mortality.
- **Remaining life expectancy of about 30–35 years at age 40 and mid-20s at age 52 in LMICs: PLAUSIBLE.** I did not look up life tables. The 20–30% reduction follows from those inputs.
- **Result: 27 falls to about 19–22: CONDITIONAL.** This is only valid if 27 was derived from general-population life tables. That was not established.
- **"Near or below the 17.7 threshold": UNVERIFIABLE.** This refers to the source model.

**Weaknesses in the mechanism (my additions)**
1. **SMR heterogeneity.** The Georgia cohort found a 
pooled SMR of 0.89 (95% CI 0.73–1.05)
, well below the Romanowski pooled estimate. It was a US cohort, but it shows SMR varies widely by setting. Romanowski's pooled value may not transfer to the countries where the HPMZ regimen would be used. A single hazard multiplier applied across all ages is also a simplification, since the commentary says excess mortality is notable among younger adults.
2. **Double-counting.** Part of the excess mortality is caused by TB sequelae, which the model may already treat elsewhere. A lifetime-burden study estimated 
12.1 DALYs per incident TB case, of which 5.8 were post-TB.
 If 27 is already a healthy-life figure from a TB-specific population, the adjustment would partly double-count. The Investigator acknowledged this.
3. **Averted-death patients are not the same population as treated survivors.** The Romanowski cohort was treated and survived. Patients whose deaths a shorter regimen averts are likely sicker at presentation, which supports the Investigator's direction. But it also means that applying a survivor SMR is an approximation.

**EVIDENCE FOUND**
- No source for how "27" was derived. Without it, whether the proposed adjustment applies cannot be settled.
- The direction (downward) is well supported by the literature. The magnitude (20–30%) rests on assumptions that cannot be verified here.

**REVISED CRITIQUE:** TB survivors have about three times the mortality of local populations (Romanowski 2019, pooled 2.91, 95% CI 2.21–3.84). Patients whose death is averted are not average members of the population, so a general-population life table likely overstates their remaining healthy years. A simple Gompertz scaling gives an effective ageing of about 11–12 years and a 20–30% reduction in remaining life expectancy at age 40. This is the Investigator's own illustration and was not sourced. The magnitude depends on whether "27" came from a general-population table, which is unknown, and on whether the SMR transfers to the relevant countries and ages. Caveats: SMR varies by setting, and TB-specific life tables may already include much of the effect. **Direction: decreases (well supported). Magnitude: medium-to-large, conditional on the derivation of 27.** The SMR is real and the mechanism is sound. The exact size of the effect is UNGROUNDED until the derivation of 27 is checked.

--- Critique: Zero modeled lag between Phase III completion and adoption, and a speedup that assumes trial timing is the binding constraint ---

## Critique 1: Private-sector treatment share and the reach of national guidelines are not modeled

**OVERALL VERDICT: PARTIALLY VERIFIED.** The hypothesis is sound and the one number the Investigator gave is accurate. The direction and the 5–15% magnitude are inference only and stay flagged as such. The claim that private providers "may not use FDCs" and the claim about what drives private-sector uptake are not supported by anything I found.

**CLAIM CHECK**
- **India's private-sector notifications are "roughly a third" of the total: VERIFIED.**
  - 
In 2023 the private sector accounted for 33% (0.84 million) of total notifications.

  - The Government of India's WHO statement gives 
30% in 2022 and 32% in 2023.

  - The Investigator's "UNGROUNDED as to numbers" label can be dropped for India.
- **A large share of DS-TB care happens in the private sector (India, Indonesia, Pakistan, Philippines): VERIFIED.**
  - In India, 
more than 50% of patients seek initial care from private providers.

  - Another source notes that 
in Pakistan, the Philippines and Indonesia, most first-contact care happens in the private sector.

  - The 2019 Global TB Report's PPM trend data are patchy. A WHO private-engagement document says 
reporting on private-sector notifications from countries remains highly inconsistent.

- **Unnotified or "missing" cases are a large share in the same countries: PARTIALLY VERIFIED, and outdated for India.**
  - WHO's 2025 report says the largest notification gaps in 2024 were 
Indonesia (10%), India (8.8%), the Philippines (7.5%), Pakistan (7.2%) and China (6.9%) of the global gap.

  - India's own gap has shrunk sharply, 
from 1.2 million missed notifications in 2015 to 0.3 million in 2023.

  - The "missing cases never see the guideline" argument is therefore stronger for Indonesia, the Philippines and Pakistan than for India now.
- **Private providers frequently deviate from national guidelines: PLAUSIBLE, with a caveat on what the evidence covers.**
  - Standardized-patient studies show poor adherence at the diagnostic and management stage. Correct management was seen in 
959 of 2,602 interactions (37%) in Mumbai and Patna.

  - In Mumbai, 
correct management against national guidelines was 75% in the public sector versus 35% in the private sector.

  - Those studies measure testing and referral, not regimen, dosing or FDC use. For regimens, a Chennai survey concluded that 
TB management practices in India's urban private sector are heterogeneous and often suboptimal.

  - The same paper reports that 
over three-quarters of providers in a systematic review prescribed a regimen potentially consistent with ISTC guidelines for new patients.
 That cuts against a strong "non-standard dosing" claim. Treatment-regimen deviation is therefore only moderately supported.
- **"May not use FDCs": UNVERIFIABLE.** I found nothing on FDC use in the private sector.
- **Uptake in the private sector depends on professional societies, pharma marketing and mandatory notification rather than NTP procurement: PARTIALLY VERIFIED.**
  - India's mechanisms include 
mandatory notification by gazette, incentives, PPSA and collaboration with professional bodies such as the IMA.

  - Private-sector drug sales are large, and one source notes that 
enormous quantities of TB drugs are sold in the Indian private market.

  - I found no evidence on pharma marketing as a driver of guideline uptake.
- **Net effect of about 5–15% of the benefit: UNGROUNDED.** This is the Investigator's inference, as they stated.

**EVIDENCE FOUND**
- **Undermining or complicating:** Notified private patients are increasingly inside the programme. A 2025 analysis reports that private-sector engagement models improved 
"TB notification and drug uptake"
 in India. For notified private patients, the "NTP procurement doesn't reach them" premise is therefore weaker.
- **Supporting:** Notification itself remains incomplete. An older estimate put private-provider notifications at 
only 22% of the estimated cases treated in that sector
 across Bangladesh, India, Indonesia and Myanmar.
- **Sign ambiguity:** The Investigator's point that the sign could flip is reasonable. Private providers show high use of adjunct tests such as chest X-rays and antibiotics (see the Mumbai study).

**REVISED CRITIQUE:** A substantial share of DS-TB care in the highest-burden countries is private. India's private notifications are about 30–33% of the total, and more than half of patients first seek care privately. Sector-specific guideline adherence is documented for diagnosis and management but not clearly for regimen or dosing. The model uses a single uptake figure across public, notified-private and unnotified-private settings. Whether this lowers effective uptake is uncertain. The direction is probably down but could be neutral or positive in some countries. The 5–15% magnitude is UNGROUNDED. Missing-case data support the argument for Indonesia, the Philippines and Pakistan more than for India. **Strength: low-to-medium.**

---

## Critique 2: Zero modeled lag between Phase III completion and adoption; speedup assumes trial timing is the binding constraint

**OVERALL VERDICT: PARTIALLY VERIFIED.** The core logic holds. One factual detail is wrong: WHO guidance on the HPMZ regimen did not wait until 2022. The Xpert details come from my own background knowledge and I could not check them in this session.

**CITATION CHECK**
- **Study 31/A5349 published 2021: VERIFIED.** 
Detailed results were published on 6 May 2021.
 The NEJM reference is 
N Engl J Med 2021;384:1705–18.

- **"WHO guidance followed in 2022": MISREPRESENTED / imprecise.**
  - Topline results were presented in October 2020, and 
WHO welcomed them at the Union World Conference.

  - WHO 
convened a GDG meeting on 27–30 April 2021.
 It then issued a "Rapid Communication" in June 2021, roughly one month after publication and about eight months after topline data.
  - A fully integrated guideline update came later, which I believe was 2022. I did not confirm that date here.
  - This supports the Investigator's point that the WHO step can be short. It also shows the "WHO guidance followed in 2022" wording is wrong.
- **Xpert WHO endorsement in 2010, with many years of implementation afterwards: NOT CHECKED.** From background knowledge the endorsement was December 2010. I did not verify it by search.
- **Albert et al. and Cazabon et al.: NOT CHECKED.** The Investigator also hadn't confirmed their findings.

**CLAIM CHECK**
- **WHO step is short on a rapid-communication path: VERIFIED** (timeline above).
- **National adoption and procurement take additional years: PLAUSIBLE, with partial support.** The WHO rapid communication itself said wider uptake 
would be more feasible if the cost of rifapentine is reduced.
 That points to cost and procurement as the bottleneck, not the guideline.
- **A generic drug has no commercial sponsor, so Phase III funding could be the gating constraint: PLAUSIBLE.** This is logical inference. I found no empirical evidence either way.
- **Added years of lag reduce benefit by about 2% per year, so 3–5 years is roughly 6–10%: UNVERIFIABLE.** The 2% rate comes from the model's formula, which I haven't seen. The arithmetic is internally consistent.
- **Lumpiness alone doesn't lower expected speedup under uniform timing: LOGICALLY SOUND.** This is a good self-correction by the Investigator.
- **TB trials with 12–24 month relapse follow-up often slip: PLAUSIBLE.** This is general knowledge. No specific slippage data were retrieved.

**EVIDENCE FOUND**
- WHO acted fast once data existed. The delay lay in trial execution and rapid generation of results, and in downstream access. That supports the point that the binding constraint is not WHO guideline convening.
- Study 31/A5349 is described as 
the first 4-month regimen endorsed by both WHO and the U.S.
 (CDC). I include this only as context on the endorsement path.

**REVISED CRITIQUE:** The model sets lag between Phase III completion and adoption at zero. The HPMZ precedent shows WHO endorsement can follow within about a month of publication (June 2021 rapid communication, after a May 2021 NEJM publication). It also shows that practical uptake was constrained by drug cost and availability, not by WHO. An expected speedup below one year per year of Phase IIc acceleration depends on the trial not being the critical path. Phase III funding for a generic is a plausible but ungrounded gating factor. The lag-cost arithmetic depends on the unverified formula. The Xpert precedent is unverified. **Strength: low-to-medium.** The lag piece is modest, and the "not on the critical path" piece is the more important one but is ungrounded.

---

## Critique 3: Survivors' excess mortality and comorbidity shrink the 27 DALYs per death

**OVERALL VERDICT: PARTIALLY VERIFIED.** The citation is real and the SMR figure is approximately right. The Gompertz arithmetic is correct. Two points could not be checked: how "27" was derived and the "17.7 threshold" are both internal to the source model. The effect size depends heavily on those, so the "large" rating is only conditionally supported.

**CITATION CHECK**
- **Romanowski et al. 2019, Lancet Infect Dis: VERIFIED.** It is 
Romanowski K, Baumann B, Basham CA, et al., Lancet Infect Dis 2019;19:1129–1137
, and it is a systematic review and meta-analysis. The DOI is 10.1016/S1473-3099(19)30309-3.
- **Pooled SMR "roughly 3–4": PARTIALLY VERIFIED, slightly high at the low end.**
  - A later article reports that the review 
found the force of mortality for TB survivors to be 2.91 (95% CI 2.21–3.84) times higher than in those who never had TB.

  - The accompanying Lancet ID comment summarizes it as 
approximately three-times to four-times greater mortality than local populations, including among younger adults.

  - Using "about 3" is fine. "3–4" matches the commentary but overstates the pooled point estimate.

**CLAIM CHECK**
- **TB patients carry high rates of smoking, alcohol use, diabetes, undernutrition and HIV: VERIFIED.** A Lancet seminar says 
progression to disease is higher in people with undernourishment, immunosuppression, or who smoke, drink alcohol, or have diabetes.
 A Georgia, USA cohort found that 
HIV co-infection, excess alcohol use, diabetes and end-stage renal disease were associated with post-treatment death.

- **Post-TB lung damage drives excess mortality: VERIFIED.** A Lancet Global Health review states that 
respiratory diseases remain the leading cause of excess deaths in people who recover from TB, with mortality three to six times that of local peers.

- **Gompertz arithmetic: VERIFIED.** ln(3) ≈ 1.10. Dividing by 0.09–0.10 gives about 11–12 years of effective ageing, as stated. Whether b ≈ 0.09–0.10 applies to LMIC adult mortality was not checked. It is roughly standard for adult mortality.
- **Remaining life expectancy of about 30–35 years at age 40 and mid-20s at age 52 in LMICs: PLAUSIBLE.** I did not look up life tables. The 20–30% reduction follows from those inputs.
- **Result: 27 falls to about 19–22: CONDITIONAL.** This is only valid if 27 was derived from general-population life tables. That was not established.
- **"Near or below the 17.7 threshold": UNVERIFIABLE.** This refers to the source model.

**Weaknesses in the mechanism (my additions)**
1. **SMR heterogeneity.** The Georgia cohort found a 
pooled SMR of 0.89 (95% CI 0.73–1.05)
, well below the Romanowski pooled estimate. It was a US cohort, but it shows SMR varies widely by setting. Romanowski's pooled value may not transfer to the countries where the HPMZ regimen would be used. A single hazard multiplier applied across all ages is also a simplification, since the commentary says excess mortality is notable among younger adults.
2. **Double-counting.** Part of the excess mortality is caused by TB sequelae, which the model may already treat elsewhere. A lifetime-burden study estimated 
12.1 DALYs per incident TB case, of which 5.8 were post-TB.
 If 27 is already a healthy-life figure from a TB-specific population, the adjustment would partly double-count. The Investigator acknowledged this.
3. **Averted-death patients are not the same population as treated survivors.** The Romanowski cohort was treated and survived. Patients whose deaths a shorter regimen averts are likely sicker at presentation, which supports the Investigator's direction. But it also means that applying a survivor SMR is an approximation.

**EVIDENCE FOUND**
- No source for how "27" was derived. Without it, whether the proposed adjustment applies cannot be settled.
- The direction (downward) is well supported by the literature. The magnitude (20–30%) rests on assumptions that cannot be verified here.

**REVISED CRITIQUE:** TB survivors have about three times the mortality of local populations (Romanowski 2019, pooled 2.91, 95% CI 2.21–3.84). Patients whose death is averted are not average members of the population, so a general-population life table likely overstates their remaining healthy years. A simple Gompertz scaling gives an effective ageing of about 11–12 years and a 20–30% reduction in remaining life expectancy at age 40. This is the Investigator's own illustration and was not sourced. The magnitude depends on whether "27" came from a general-population table, which is unknown, and on whether the SMR transfers to the relevant countries and ages. Caveats: SMR varies by setting, and TB-specific life tables may already include much of the effect. **Direction: decreases (well supported). Magnitude: medium-to-large, conditional on the derivation of 27.** The SMR is real and the mechanism is sound. The exact size of the effect is UNGROUNDED until the derivation of 27 is checked.

--- Critique: Survivors' excess mortality and comorbidity shrink the 27 DALYs per death ---

## Critique 1: Private-sector treatment share and the reach of national guidelines are not modeled

**OVERALL VERDICT: PARTIALLY VERIFIED.** The hypothesis is sound and the one number the Investigator gave is accurate. The direction and the 5–15% magnitude are inference only and stay flagged as such. The claim that private providers "may not use FDCs" and the claim about what drives private-sector uptake are not supported by anything I found.

**CLAIM CHECK**
- **India's private-sector notifications are "roughly a third" of the total: VERIFIED.**
  - 
In 2023 the private sector accounted for 33% (0.84 million) of total notifications.

  - The Government of India's WHO statement gives 
30% in 2022 and 32% in 2023.

  - The Investigator's "UNGROUNDED as to numbers" label can be dropped for India.
- **A large share of DS-TB care happens in the private sector (India, Indonesia, Pakistan, Philippines): VERIFIED.**
  - In India, 
more than 50% of patients seek initial care from private providers.

  - Another source notes that 
in Pakistan, the Philippines and Indonesia, most first-contact care happens in the private sector.

  - The 2019 Global TB Report's PPM trend data are patchy. A WHO private-engagement document says 
reporting on private-sector notifications from countries remains highly inconsistent.

- **Unnotified or "missing" cases are a large share in the same countries: PARTIALLY VERIFIED, and outdated for India.**
  - WHO's 2025 report says the largest notification gaps in 2024 were 
Indonesia (10%), India (8.8%), the Philippines (7.5%), Pakistan (7.2%) and China (6.9%) of the global gap.

  - India's own gap has shrunk sharply, 
from 1.2 million missed notifications in 2015 to 0.3 million in 2023.

  - The "missing cases never see the guideline" argument is therefore stronger for Indonesia, the Philippines and Pakistan than for India now.
- **Private providers frequently deviate from national guidelines: PLAUSIBLE, with a caveat on what the evidence covers.**
  - Standardized-patient studies show poor adherence at the diagnostic and management stage. Correct management was seen in 
959 of 2,602 interactions (37%) in Mumbai and Patna.

  - In Mumbai, 
correct management against national guidelines was 75% in the public sector versus 35% in the private sector.

  - Those studies measure testing and referral, not regimen, dosing or FDC use. For regimens, a Chennai survey concluded that 
TB management practices in India's urban private sector are heterogeneous and often suboptimal.

  - The same paper reports that 
over three-quarters of providers in a systematic review prescribed a regimen potentially consistent with ISTC guidelines for new patients.
 That cuts against a strong "non-standard dosing" claim. Treatment-regimen deviation is therefore only moderately supported.
- **"May not use FDCs": UNVERIFIABLE.** I found nothing on FDC use in the private sector.
- **Uptake in the private sector depends on professional societies, pharma marketing and mandatory notification rather than NTP procurement: PARTIALLY VERIFIED.**
  - India's mechanisms include 
mandatory notification by gazette, incentives, PPSA and collaboration with professional bodies such as the IMA.

  - Private-sector drug sales are large, and one source notes that 
enormous quantities of TB drugs are sold in the Indian private market.

  - I found no evidence on pharma marketing as a driver of guideline uptake.
- **Net effect of about 5–15% of the benefit: UNGROUNDED.** This is the Investigator's inference, as they stated.

**EVIDENCE FOUND**
- **Undermining or complicating:** Notified private patients are increasingly inside the programme. A 2025 analysis reports that private-sector engagement models improved 
"TB notification and drug uptake"
 in India. For notified private patients, the "NTP procurement doesn't reach them" premise is therefore weaker.
- **Supporting:** Notification itself remains incomplete. An older estimate put private-provider notifications at 
only 22% of the estimated cases treated in that sector
 across Bangladesh, India, Indonesia and Myanmar.
- **Sign ambiguity:** The Investigator's point that the sign could flip is reasonable. Private providers show high use of adjunct tests such as chest X-rays and antibiotics (see the Mumbai study).

**REVISED CRITIQUE:** A substantial share of DS-TB care in the highest-burden countries is private. India's private notifications are about 30–33% of the total, and more than half of patients first seek care privately. Sector-specific guideline adherence is documented for diagnosis and management but not clearly for regimen or dosing. The model uses a single uptake figure across public, notified-private and unnotified-private settings. Whether this lowers effective uptake is uncertain. The direction is probably down but could be neutral or positive in some countries. The 5–15% magnitude is UNGROUNDED. Missing-case data support the argument for Indonesia, the Philippines and Pakistan more than for India. **Strength: low-to-medium.**

---

## Critique 2: Zero modeled lag between Phase III completion and adoption; speedup assumes trial timing is the binding constraint

**OVERALL VERDICT: PARTIALLY VERIFIED.** The core logic holds. One factual detail is wrong: WHO guidance on the HPMZ regimen did not wait until 2022. The Xpert details come from my own background knowledge and I could not check them in this session.

**CITATION CHECK**
- **Study 31/A5349 published 2021: VERIFIED.** 
Detailed results were published on 6 May 2021.
 The NEJM reference is 
N Engl J Med 2021;384:1705–18.

- **"WHO guidance followed in 2022": MISREPRESENTED / imprecise.**
  - Topline results were presented in October 2020, and 
WHO welcomed them at the Union World Conference.

  - WHO 
convened a GDG meeting on 27–30 April 2021.
 It then issued a "Rapid Communication" in June 2021, roughly one month after publication and about eight months after topline data.
  - A fully integrated guideline update came later, which I believe was 2022. I did not confirm that date here.
  - This supports the Investigator's point that the WHO step can be short. It also shows the "WHO guidance followed in 2022" wording is wrong.
- **Xpert WHO endorsement in 2010, with many years of implementation afterwards: NOT CHECKED.** From background knowledge the endorsement was December 2010. I did not verify it by search.
- **Albert et al. and Cazabon et al.: NOT CHECKED.** The Investigator also hadn't confirmed their findings.

**CLAIM CHECK**
- **WHO step is short on a rapid-communication path: VERIFIED** (timeline above).
- **National adoption and procurement take additional years: PLAUSIBLE, with partial support.** The WHO rapid communication itself said wider uptake 
would be more feasible if the cost of rifapentine is reduced.
 That points to cost and procurement as the bottleneck, not the guideline.
- **A generic drug has no commercial sponsor, so Phase III funding could be the gating constraint: PLAUSIBLE.** This is logical inference. I found no empirical evidence either way.
- **Added years of lag reduce benefit by about 2% per year, so 3–5 years is roughly 6–10%: UNVERIFIABLE.** The 2% rate comes from the model's formula, which I haven't seen. The arithmetic is internally consistent.
- **Lumpiness alone doesn't lower expected speedup under uniform timing: LOGICALLY SOUND.** This is a good self-correction by the Investigator.
- **TB trials with 12–24 month relapse follow-up often slip: PLAUSIBLE.** This is general knowledge. No specific slippage data were retrieved.

**EVIDENCE FOUND**
- WHO acted fast once data existed. The delay lay in trial execution and rapid generation of results, and in downstream access. That supports the point that the binding constraint is not WHO guideline convening.
- Study 31/A5349 is described as 
the first 4-month regimen endorsed by both WHO and the U.S.
 (CDC). I include this only as context on the endorsement path.

**REVISED CRITIQUE:** The model sets lag between Phase III completion and adoption at zero. The HPMZ precedent shows WHO endorsement can follow within about a month of publication (June 2021 rapid communication, after a May 2021 NEJM publication). It also shows that practical uptake was constrained by drug cost and availability, not by WHO. An expected speedup below one year per year of Phase IIc acceleration depends on the trial not being the critical path. Phase III funding for a generic is a plausible but ungrounded gating factor. The lag-cost arithmetic depends on the unverified formula. The Xpert precedent is unverified. **Strength: low-to-medium.** The lag piece is modest, and the "not on the critical path" piece is the more important one but is ungrounded.

---

## Critique 3: Survivors' excess mortality and comorbidity shrink the 27 DALYs per death

**OVERALL VERDICT: PARTIALLY VERIFIED.** The citation is real and the SMR figure is approximately right. The Gompertz arithmetic is correct. Two points could not be checked: how "27" was derived and the "17.7 threshold" are both internal to the source model. The effect size depends heavily on those, so the "large" rating is only conditionally supported.

**CITATION CHECK**
- **Romanowski et al. 2019, Lancet Infect Dis: VERIFIED.** It is 
Romanowski K, Baumann B, Basham CA, et al., Lancet Infect Dis 2019;19:1129–1137
, and it is a systematic review and meta-analysis. The DOI is 10.1016/S1473-3099(19)30309-3.
- **Pooled SMR "roughly 3–4": PARTIALLY VERIFIED, slightly high at the low end.**
  - A later article reports that the review 
found the force of mortality for TB survivors to be 2.91 (95% CI 2.21–3.84) times higher than in those who never had TB.

  - The accompanying Lancet ID comment summarizes it as 
approximately three-times to four-times greater mortality than local populations, including among younger adults.

  - Using "about 3" is fine. "3–4" matches the commentary but overstates the pooled point estimate.

**CLAIM CHECK**
- **TB patients carry high rates of smoking, alcohol use, diabetes, undernutrition and HIV: VERIFIED.** A Lancet seminar says 
progression to disease is higher in people with undernourishment, immunosuppression, or who smoke, drink alcohol, or have diabetes.
 A Georgia, USA cohort found that 
HIV co-infection, excess alcohol use, diabetes and end-stage renal disease were associated with post-treatment death.

- **Post-TB lung damage drives excess mortality: VERIFIED.** A Lancet Global Health review states that 
respiratory diseases remain the leading cause of excess deaths in people who recover from TB, with mortality three to six times that of local peers.

- **Gompertz arithmetic: VERIFIED.** ln(3) ≈ 1.10. Dividing by 0.09–0.10 gives about 11–12 years of effective ageing, as stated. Whether b ≈ 0.09–0.10 applies to LMIC adult mortality was not checked. It is roughly standard for adult mortality.
- **Remaining life expectancy of about 30–35 years at age 40 and mid-20s at age 52 in LMICs: PLAUSIBLE.** I did not look up life tables. The 20–30% reduction follows from those inputs.
- **Result: 27 falls to about 19–22: CONDITIONAL.** This is only valid if 27 was derived from general-population life tables. That was not established.
- **"Near or below the 17.7 threshold": UNVERIFIABLE.** This refers to the source model.

**Weaknesses in the mechanism (my additions)**
1. **SMR heterogeneity.** The Georgia cohort found a 
pooled SMR of 0.89 (95% CI 0.73–1.05)
, well below the Romanowski pooled estimate. It was a US cohort, but it shows SMR varies widely by setting. Romanowski's pooled value may not transfer to the countries where the HPMZ regimen would be used. A single hazard multiplier applied across all ages is also a simplification, since the commentary says excess mortality is notable among younger adults.
2. **Double-counting.** Part of the excess mortality is caused by TB sequelae, which the model may already treat elsewhere. A lifetime-burden study estimated 
12.1 DALYs per incident TB case, of which 5.8 were post-TB.
 If 27 is already a healthy-life figure from a TB-specific population, the adjustment would partly double-count. The Investigator acknowledged this.
3. **Averted-death patients are not the same population as treated survivors.** The Romanowski cohort was treated and survived. Patients whose deaths a shorter regimen averts are likely sicker at presentation, which supports the Investigator's direction. But it also means that applying a survivor SMR is an approximation.

**EVIDENCE FOUND**
- No source for how "27" was derived. Without it, whether the proposed adjustment applies cannot be settled.
- The direction (downward) is well supported by the literature. The magnitude (20–30%) rests on assumptions that cannot be verified here.

**REVISED CRITIQUE:** TB survivors have about three times the mortality of local populations (Romanowski 2019, pooled 2.91, 95% CI 2.21–3.84). Patients whose death is averted are not average members of the population, so a general-population life table likely overstates their remaining healthy years. A simple Gompertz scaling gives an effective ageing of about 11–12 years and a 20–30% reduction in remaining life expectancy at age 40. This is the Investigator's own illustration and was not sourced. The magnitude depends on whether "27" came from a general-population table, which is unknown, and on whether the SMR transfers to the relevant countries and ages. Caveats: SMR varies by setting, and TB-specific life tables may already include much of the effect. **Direction: decreases (well supported). Magnitude: medium-to-large, conditional on the derivation of 27.** The SMR is real and the mechanism is sound. The exact size of the effect is UNGROUNDED until the derivation of 27 is checked.

--- Critique: The 6% is a mix of deaths, and only a fraction is reachable and modifiable by atorvastatin ---

## Critique 1: The 6% is a mix of deaths, and only a fraction is reachable and modifiable by atorvastatin

**OVERALL VERDICT: PARTIALLY VERIFIED.** The qualitative hypothesis is well supported. The quantitative decomposition is ungrounded, and it risks double-counting.

**CLAIM CHECK**
- **Waitt & Squire 2011 (IJTLD) exists. VERIFIED.** 
It is Int J Tuberc Lung Dis 2011;15(7):871-85, PMID 21496360.

  - I could only see how other papers describe it, not the paper itself. 
One describes its risk factors as HIV co-infection, advancing immunosuppression, smear-negative disease and malnutrition.
 The investigator's recollection of HIV and malnutrition is therefore right.
  - The recollection of older age is not confirmed by that secondary description.
  - The claim that "many deaths occur early" is not verified as a finding of that review. Other studies support it (see below).
- **Deaths are concentrated early. VERIFIED (multiple cohorts).**
  - Zambia: 
75.7% of deaths occurred in the first two months, with a median time to death of 21 days.
 
More than half (58.1%) occurred in the first month.

  - Taiwan: 
Underweight predicted mortality only in the first 8 weeks.
 This supports the malnutrition link.
  - Another cohort found 
TB-related deaths occurred early, with a median survival of 20 days.

  - Ethiopia: 
56.7% of deaths occurred in the intensive phase.

  - Counter-evidence: in the Andhra Pradesh cohort, 
deaths were described as fairly evenly distributed across treatment.
 The early concentration is therefore not universal.
- **Some deaths are not TB-attributable. PLAUSIBLE/VERIFIED in direction.**
  - One cohort split deaths into TB-related and non-TB-related. 
Liver cirrhosis was the only comorbidity associated with TB-related death.

  - I found no pooled share of non-TB deaths, so the 15% is a placeholder.
- **The rifampicin–atorvastatin interaction is established, but the investigator's framing is too simple. PARTIALLY VERIFIED.**
  - The interaction is real but works in two directions. 
A single rifampicin dose inhibits OATP1B1/1B3 and raises atorvastatin exposure about 6.8-fold. After multiple doses, induction can overcome this and lower exposure.

  - 
These opposing effects make the interaction hard to manage, with either reduced or raised statin levels.

  - 
Labelling recommends simultaneous co-administration, because delayed atorvastatin after rifampicin is associated with a significant drop in plasma concentration.

  - Early exposure could even be higher, not lower. The inference that onset of benefit is delayed is not supported. It also contradicts the unqualified "limited by rifampicin induction."
- **The arithmetic is correct.** 6% × 0.7 × 0.85 = 3.57%. I cannot verify the 3.9% threshold, because it comes from the source materials.

**EVIDENCE FOUND**
- Early-death concentration is strongly supported in sub-Saharan African cohorts (Zambia, Ethiopia, Cameroon). Taiwan adds that malnutrition-related excess mortality is confined to the first 8 weeks.
- Double-counting risk, from my own reasoning. If the statin effect size comes from a trial or meta-analysis of all-cause mortality in enrolled patients, early and non-TB deaths are already reflected in that effect. Applying the "addressable share" haircut to the baseline as well would penalise the same deaths twice. The decomposition only holds if the model applies the effect as a relative reduction to unselected WHO-cohort mortality. This is an unverified inference.
- Trial populations usually exclude the sickest patients. This makes the haircut more defensible if effect sizes come from healthier trial populations.

**REVISED CRITIQUE**
On-treatment TB deaths are concentrated in the first 1–2 months in many high-burden cohorts. Zambia shows about 75%, though some cohorts show flatter timing. Deaths in this window are often among malnourished, advanced-HIV or very sick patients. The rifampicin–atorvastatin interaction is bidirectional, so whether benefit onset is delayed is **UNGROUNDED**. The share of the 6% that is addressable is likely below 100%. The 30% and 15% figures and the 3.6% result are **illustrative only**.
- The critique must state how the effect size was derived, to avoid double-counting.
- Strength: medium, direction uncertain-to-decreasing. This holds only if effect sizes come from unselected populations.

---

## Critique 2: Under-ascertained deaths push true mortality up

**OVERALL VERDICT: PARTIALLY VERIFIED.** The mechanism is sound and some direction-of-effect evidence exists. The magnitude is plausible but weakly grounded. There are definitional problems and a labelling error.

**CLAIM CHECK**
- **WHO outcome categories are as described. VERIFIED.** 
The categories are treatment success, failed, died, lost to follow-up and not evaluated.
 
The denominator is everyone who started rifampicin-susceptible treatment.
 So deaths among LTFU and not-evaluated patients are not in the "died" numerator.
- **Specific global percentages (5–6% died, 3–4% LTFU, a few percent not evaluated). UNVERIFIABLE from my searches.**
  - I confirmed only that 
global treatment success was 88% in 2023 and 2022.

  - Kenya's 2022 national data were about 
6% died and 5% lost to follow-up.

  - A Kenyan county surveillance dataset had 
5.5% died, 2.6% LTFU and 5.8% not evaluated.
 That makes LTFU plus NE 8.4% there, higher than the 6–7% assumed.
  - Not-evaluated can be very large in some programmes. 
Zimbabwe reports high percentages of not-evaluated outcomes.

- **A meaningful share of LTFU patients die. VERIFIED in direction. The 10–20% range is plausible but evidence is mixed.**
  - A Kilifi, Kenya tracing study (medRxiv preprint) 
found 14 of 140 patients identified for tracing (10%) had died, with 36 traced and 90 relocated.
 That matches the low end of the investigator's range.
  - 
A Georgia study of second-line (MDR/XDR) treatment found 107 of 461 LFU patients (23%) died.
 This is drug-resistant TB, so it is not a good analogue for drug-susceptible TB.
  - 
An Estonian study found 30% of the 102 traced LFU patients died.
 It mixed drug-susceptible and drug-resistant TB.
  - A Brazilian preprint found 
8.0% of LFU patients died, at a median of 17.5 months after LTFU.
 It also found 
a two- to three-fold increased hazard of late mortality after LTFU.

  - The Brazilian deaths occur long after the on-treatment window. This undermines treating them as "on-treatment mortality."
- **Deaths before treatment start or among untreated patients push true mortality up. PARTIALLY MISREPRESENTED.**
  - The 6% is a share of patients who started treatment, so pre-treatment deaths are outside both the numerator and the denominator. They do not make "mortality among treated patients" higher.
  - They matter only if the model's population is broader than the WHO treated cohort. In Cape Town, 
17.1% of initially lost patients died, 69.7% of them within 30 days.
 That is a different population.
  - Under WHO definitions, transfers out fall into "not evaluated". This is from my background knowledge, not verified in these searches.
- **The arithmetic is correct.** 0.6 and 1.4 pp are right, giving 6.6–7.4% and a 10–23% proportional rise.
- **Internal labelling error.** The title says "opposite of Critiques 1–2", but this is Critique 2. It presumably means Critiques 1 and 3. This should be fixed.

**EVIDENCE FOUND**
- The Kenyan surveillance paper says 
the vital status of the 8.4% who were LTFU or not evaluated could not be ascertained.
 This directly supports the under-ascertainment mechanism.
- The Kilifi tracing study (10%) supports the low end of the range. The drug-resistant TB studies (23–30%) are less applicable.
- The timing of deaths among LTFU patients undermines the "on-treatment" framing and the statin-attributable fraction.

**REVISED CRITIQUE**
WHO "died" excludes deaths among LTFU and not-evaluated patients. Tracing studies show non-trivial mortality among LTFU patients, about 10% in a Kenyan drug-susceptible-dominant setting and higher in drug-resistant cohorts. This could push true mortality among those who started treatment above 6%. A plausible range is perhaps +0.3 to +1.4 pp. The statin-attributable share of these deaths is uncertain, because they may occur after treatment interruption. The pre-treatment-death and untreated-case claims should be dropped or reframed, since they do not affect mortality among treated patients. Global WHO percentages are **UNVERIFIED**. Strength: **low-to-medium**, direction increases.

---

## Critique 3: Covariance between mortality and DALYs per death

**OVERALL VERDICT: PARTIALLY VERIFIED.** The logic and arithmetic are correct, and the direction of the age–mortality relationship is supported. The magnitude (−10 to −15%) rests entirely on invented numbers. The critique may not apply at all, depending on how the 27 was derived.

**CLAIM CHECK**
- **The arithmetic is correct. VERIFIED.**
  - Mean mortality is 0.7×4% + 0.3×12% = 6.4%.
  - Death-weighted DALYs are (0.98+0.54)/0.064 = 23.75.
  - Expected DALYs per patient are 1.52, against 6.4%×27 = 1.728, so 12% lower.
- **Higher-mortality subgroups tend to be older. VERIFIED.**
  - In a South African cohort of 190,472 TB cases, 
advancing age was the strongest risk factor for death, followed by HIV co-infection or unknown HIV status.

  - Kenyan data also associate older age with mortality: 
other comorbidities, clinical diagnosis, undernourishment and older age were positively associated with mortality.

  - Turkey: 
advanced age increased mortality risk.

- **HIV pushes the other way. PLAUSIBLE/VERIFIED in part.** 
HIV co-infection (OR 2.2) and unknown HIV status (OR 2.8) were independently associated with death.
 Age-at-death for HIV-positive patients was not retrieved. The Kenyan cohort had 
a median age of 32 years.
 This supports the point that many TB patients, and deaths, are young adults in high-HIV settings.
- **"If 27 was derived without death weighting, the product is biased." CONDITIONAL.**
  - GBD-style total DALYs (or YLLs) divided by total deaths is already a death-weighted mean. In that case no covariance bias arises.
  - The bias arises only if 27 came from something else, such as life expectancy at an average age or a patient-weighted average age. I cannot see how 27 was derived.
- **GBD 2021 can be used to compute this. PLAUSIBLE, not run.** I did not verify the specific GBD tables.
- **The −10 to −15% effect in low-HIV settings. UNGROUNDED.** It is an artefact of the invented group parameters. The investigator flagged this.

**EVIDENCE FOUND**
- The relevant quantity is DALYs per *averted* death, which depends on who benefits from the statin. The statin might benefit older or comorbid patients differently, which adds further uncertainty.
- Standard life-table YLLs overstate remaining life expectancy for sick patients. This is my own reasoning, not verified, and it suggests a further downward bias on top of the covariance issue.
- Direction is uncertain overall: age pushes DALYs down, HIV and young-adult TB push them up.

**REVISED CRITIQUE**
Mortality is positively associated with age, and years lost per death fall with age. If dalys_per_death was computed as a population or patient-weighted average, multiplying by mean mortality overstates expected DALYs averted. If it was computed as total DALYs divided by total deaths, which is the GBD approach, the bias largely disappears. In high-HIV settings, young-adult deaths push the opposite way. The size of the effect is **UNGROUNDED** and the sign is uncertain.
- The critique should be conditioned on how 27 was derived.
- A GBD age/HIV-stratified death-weighted YLL calculation would settle it.
- Strength: **low-to-medium**, direction **uncertain, leaning decreases** in low-HIV settings.

--- Critique: Under-ascertained deaths push true mortality up, and the direction is the opposite of Critiques 1–2 ---

## Critique 1: The 6% is a mix of deaths, and only a fraction is reachable and modifiable by atorvastatin

**OVERALL VERDICT: PARTIALLY VERIFIED.** The qualitative hypothesis is well supported. The quantitative decomposition is ungrounded, and it risks double-counting.

**CLAIM CHECK**
- **Waitt & Squire 2011 (IJTLD) exists. VERIFIED.** 
It is Int J Tuberc Lung Dis 2011;15(7):871-85, PMID 21496360.

  - I could only see how other papers describe it, not the paper itself. 
One describes its risk factors as HIV co-infection, advancing immunosuppression, smear-negative disease and malnutrition.
 The investigator's recollection of HIV and malnutrition is therefore right.
  - The recollection of older age is not confirmed by that secondary description.
  - The claim that "many deaths occur early" is not verified as a finding of that review. Other studies support it (see below).
- **Deaths are concentrated early. VERIFIED (multiple cohorts).**
  - Zambia: 
75.7% of deaths occurred in the first two months, with a median time to death of 21 days.
 
More than half (58.1%) occurred in the first month.

  - Taiwan: 
Underweight predicted mortality only in the first 8 weeks.
 This supports the malnutrition link.
  - Another cohort found 
TB-related deaths occurred early, with a median survival of 20 days.

  - Ethiopia: 
56.7% of deaths occurred in the intensive phase.

  - Counter-evidence: in the Andhra Pradesh cohort, 
deaths were described as fairly evenly distributed across treatment.
 The early concentration is therefore not universal.
- **Some deaths are not TB-attributable. PLAUSIBLE/VERIFIED in direction.**
  - One cohort split deaths into TB-related and non-TB-related. 
Liver cirrhosis was the only comorbidity associated with TB-related death.

  - I found no pooled share of non-TB deaths, so the 15% is a placeholder.
- **The rifampicin–atorvastatin interaction is established, but the investigator's framing is too simple. PARTIALLY VERIFIED.**
  - The interaction is real but works in two directions. 
A single rifampicin dose inhibits OATP1B1/1B3 and raises atorvastatin exposure about 6.8-fold. After multiple doses, induction can overcome this and lower exposure.

  - 
These opposing effects make the interaction hard to manage, with either reduced or raised statin levels.

  - 
Labelling recommends simultaneous co-administration, because delayed atorvastatin after rifampicin is associated with a significant drop in plasma concentration.

  - Early exposure could even be higher, not lower. The inference that onset of benefit is delayed is not supported. It also contradicts the unqualified "limited by rifampicin induction."
- **The arithmetic is correct.** 6% × 0.7 × 0.85 = 3.57%. I cannot verify the 3.9% threshold, because it comes from the source materials.

**EVIDENCE FOUND**
- Early-death concentration is strongly supported in sub-Saharan African cohorts (Zambia, Ethiopia, Cameroon). Taiwan adds that malnutrition-related excess mortality is confined to the first 8 weeks.
- Double-counting risk, from my own reasoning. If the statin effect size comes from a trial or meta-analysis of all-cause mortality in enrolled patients, early and non-TB deaths are already reflected in that effect. Applying the "addressable share" haircut to the baseline as well would penalise the same deaths twice. The decomposition only holds if the model applies the effect as a relative reduction to unselected WHO-cohort mortality. This is an unverified inference.
- Trial populations usually exclude the sickest patients. This makes the haircut more defensible if effect sizes come from healthier trial populations.

**REVISED CRITIQUE**
On-treatment TB deaths are concentrated in the first 1–2 months in many high-burden cohorts. Zambia shows about 75%, though some cohorts show flatter timing. Deaths in this window are often among malnourished, advanced-HIV or very sick patients. The rifampicin–atorvastatin interaction is bidirectional, so whether benefit onset is delayed is **UNGROUNDED**. The share of the 6% that is addressable is likely below 100%. The 30% and 15% figures and the 3.6% result are **illustrative only**.
- The critique must state how the effect size was derived, to avoid double-counting.
- Strength: medium, direction uncertain-to-decreasing. This holds only if effect sizes come from unselected populations.

---

## Critique 2: Under-ascertained deaths push true mortality up

**OVERALL VERDICT: PARTIALLY VERIFIED.** The mechanism is sound and some direction-of-effect evidence exists. The magnitude is plausible but weakly grounded. There are definitional problems and a labelling error.

**CLAIM CHECK**
- **WHO outcome categories are as described. VERIFIED.** 
The categories are treatment success, failed, died, lost to follow-up and not evaluated.
 
The denominator is everyone who started rifampicin-susceptible treatment.
 So deaths among LTFU and not-evaluated patients are not in the "died" numerator.
- **Specific global percentages (5–6% died, 3–4% LTFU, a few percent not evaluated). UNVERIFIABLE from my searches.**
  - I confirmed only that 
global treatment success was 88% in 2023 and 2022.

  - Kenya's 2022 national data were about 
6% died and 5% lost to follow-up.

  - A Kenyan county surveillance dataset had 
5.5% died, 2.6% LTFU and 5.8% not evaluated.
 That makes LTFU plus NE 8.4% there, higher than the 6–7% assumed.
  - Not-evaluated can be very large in some programmes. 
Zimbabwe reports high percentages of not-evaluated outcomes.

- **A meaningful share of LTFU patients die. VERIFIED in direction. The 10–20% range is plausible but evidence is mixed.**
  - A Kilifi, Kenya tracing study (medRxiv preprint) 
found 14 of 140 patients identified for tracing (10%) had died, with 36 traced and 90 relocated.
 That matches the low end of the investigator's range.
  - 
A Georgia study of second-line (MDR/XDR) treatment found 107 of 461 LFU patients (23%) died.
 This is drug-resistant TB, so it is not a good analogue for drug-susceptible TB.
  - 
An Estonian study found 30% of the 102 traced LFU patients died.
 It mixed drug-susceptible and drug-resistant TB.
  - A Brazilian preprint found 
8.0% of LFU patients died, at a median of 17.5 months after LTFU.
 It also found 
a two- to three-fold increased hazard of late mortality after LTFU.

  - The Brazilian deaths occur long after the on-treatment window. This undermines treating them as "on-treatment mortality."
- **Deaths before treatment start or among untreated patients push true mortality up. PARTIALLY MISREPRESENTED.**
  - The 6% is a share of patients who started treatment, so pre-treatment deaths are outside both the numerator and the denominator. They do not make "mortality among treated patients" higher.
  - They matter only if the model's population is broader than the WHO treated cohort. In Cape Town, 
17.1% of initially lost patients died, 69.7% of them within 30 days.
 That is a different population.
  - Under WHO definitions, transfers out fall into "not evaluated". This is from my background knowledge, not verified in these searches.
- **The arithmetic is correct.** 0.6 and 1.4 pp are right, giving 6.6–7.4% and a 10–23% proportional rise.
- **Internal labelling error.** The title says "opposite of Critiques 1–2", but this is Critique 2. It presumably means Critiques 1 and 3. This should be fixed.

**EVIDENCE FOUND**
- The Kenyan surveillance paper says 
the vital status of the 8.4% who were LTFU or not evaluated could not be ascertained.
 This directly supports the under-ascertainment mechanism.
- The Kilifi tracing study (10%) supports the low end of the range. The drug-resistant TB studies (23–30%) are less applicable.
- The timing of deaths among LTFU patients undermines the "on-treatment" framing and the statin-attributable fraction.

**REVISED CRITIQUE**
WHO "died" excludes deaths among LTFU and not-evaluated patients. Tracing studies show non-trivial mortality among LTFU patients, about 10% in a Kenyan drug-susceptible-dominant setting and higher in drug-resistant cohorts. This could push true mortality among those who started treatment above 6%. A plausible range is perhaps +0.3 to +1.4 pp. The statin-attributable share of these deaths is uncertain, because they may occur after treatment interruption. The pre-treatment-death and untreated-case claims should be dropped or reframed, since they do not affect mortality among treated patients. Global WHO percentages are **UNVERIFIED**. Strength: **low-to-medium**, direction increases.

---

## Critique 3: Covariance between mortality and DALYs per death

**OVERALL VERDICT: PARTIALLY VERIFIED.** The logic and arithmetic are correct, and the direction of the age–mortality relationship is supported. The magnitude (−10 to −15%) rests entirely on invented numbers. The critique may not apply at all, depending on how the 27 was derived.

**CLAIM CHECK**
- **The arithmetic is correct. VERIFIED.**
  - Mean mortality is 0.7×4% + 0.3×12% = 6.4%.
  - Death-weighted DALYs are (0.98+0.54)/0.064 = 23.75.
  - Expected DALYs per patient are 1.52, against 6.4%×27 = 1.728, so 12% lower.
- **Higher-mortality subgroups tend to be older. VERIFIED.**
  - In a South African cohort of 190,472 TB cases, 
advancing age was the strongest risk factor for death, followed by HIV co-infection or unknown HIV status.

  - Kenyan data also associate older age with mortality: 
other comorbidities, clinical diagnosis, undernourishment and older age were positively associated with mortality.

  - Turkey: 
advanced age increased mortality risk.

- **HIV pushes the other way. PLAUSIBLE/VERIFIED in part.** 
HIV co-infection (OR 2.2) and unknown HIV status (OR 2.8) were independently associated with death.
 Age-at-death for HIV-positive patients was not retrieved. The Kenyan cohort had 
a median age of 32 years.
 This supports the point that many TB patients, and deaths, are young adults in high-HIV settings.
- **"If 27 was derived without death weighting, the product is biased." CONDITIONAL.**
  - GBD-style total DALYs (or YLLs) divided by total deaths is already a death-weighted mean. In that case no covariance bias arises.
  - The bias arises only if 27 came from something else, such as life expectancy at an average age or a patient-weighted average age. I cannot see how 27 was derived.
- **GBD 2021 can be used to compute this. PLAUSIBLE, not run.** I did not verify the specific GBD tables.
- **The −10 to −15% effect in low-HIV settings. UNGROUNDED.** It is an artefact of the invented group parameters. The investigator flagged this.

**EVIDENCE FOUND**
- The relevant quantity is DALYs per *averted* death, which depends on who benefits from the statin. The statin might benefit older or comorbid patients differently, which adds further uncertainty.
- Standard life-table YLLs overstate remaining life expectancy for sick patients. This is my own reasoning, not verified, and it suggests a further downward bias on top of the covariance issue.
- Direction is uncertain overall: age pushes DALYs down, HIV and young-adult TB push them up.

**REVISED CRITIQUE**
Mortality is positively associated with age, and years lost per death fall with age. If dalys_per_death was computed as a population or patient-weighted average, multiplying by mean mortality overstates expected DALYs averted. If it was computed as total DALYs divided by total deaths, which is the GBD approach, the bias largely disappears. In high-HIV settings, young-adult deaths push the opposite way. The size of the effect is **UNGROUNDED** and the sign is uncertain.
- The critique should be conditioned on how 27 was derived.
- A GBD age/HIV-stratified death-weighted YLL calculation would settle it.
- Strength: **low-to-medium**, direction **uncertain, leaning decreases** in low-HIV settings.

--- Critique: Covariance between mortality and DALYs per death means the product of means is not the mean of the product ---

## Critique 1: The 6% is a mix of deaths, and only a fraction is reachable and modifiable by atorvastatin

**OVERALL VERDICT: PARTIALLY VERIFIED.** The qualitative hypothesis is well supported. The quantitative decomposition is ungrounded, and it risks double-counting.

**CLAIM CHECK**
- **Waitt & Squire 2011 (IJTLD) exists. VERIFIED.** 
It is Int J Tuberc Lung Dis 2011;15(7):871-85, PMID 21496360.

  - I could only see how other papers describe it, not the paper itself. 
One describes its risk factors as HIV co-infection, advancing immunosuppression, smear-negative disease and malnutrition.
 The investigator's recollection of HIV and malnutrition is therefore right.
  - The recollection of older age is not confirmed by that secondary description.
  - The claim that "many deaths occur early" is not verified as a finding of that review. Other studies support it (see below).
- **Deaths are concentrated early. VERIFIED (multiple cohorts).**
  - Zambia: 
75.7% of deaths occurred in the first two months, with a median time to death of 21 days.
 
More than half (58.1%) occurred in the first month.

  - Taiwan: 
Underweight predicted mortality only in the first 8 weeks.
 This supports the malnutrition link.
  - Another cohort found 
TB-related deaths occurred early, with a median survival of 20 days.

  - Ethiopia: 
56.7% of deaths occurred in the intensive phase.

  - Counter-evidence: in the Andhra Pradesh cohort, 
deaths were described as fairly evenly distributed across treatment.
 The early concentration is therefore not universal.
- **Some deaths are not TB-attributable. PLAUSIBLE/VERIFIED in direction.**
  - One cohort split deaths into TB-related and non-TB-related. 
Liver cirrhosis was the only comorbidity associated with TB-related death.

  - I found no pooled share of non-TB deaths, so the 15% is a placeholder.
- **The rifampicin–atorvastatin interaction is established, but the investigator's framing is too simple. PARTIALLY VERIFIED.**
  - The interaction is real but works in two directions. 
A single rifampicin dose inhibits OATP1B1/1B3 and raises atorvastatin exposure about 6.8-fold. After multiple doses, induction can overcome this and lower exposure.

  - 
These opposing effects make the interaction hard to manage, with either reduced or raised statin levels.

  - 
Labelling recommends simultaneous co-administration, because delayed atorvastatin after rifampicin is associated with a significant drop in plasma concentration.

  - Early exposure could even be higher, not lower. The inference that onset of benefit is delayed is not supported. It also contradicts the unqualified "limited by rifampicin induction."
- **The arithmetic is correct.** 6% × 0.7 × 0.85 = 3.57%. I cannot verify the 3.9% threshold, because it comes from the source materials.

**EVIDENCE FOUND**
- Early-death concentration is strongly supported in sub-Saharan African cohorts (Zambia, Ethiopia, Cameroon). Taiwan adds that malnutrition-related excess mortality is confined to the first 8 weeks.
- Double-counting risk, from my own reasoning. If the statin effect size comes from a trial or meta-analysis of all-cause mortality in enrolled patients, early and non-TB deaths are already reflected in that effect. Applying the "addressable share" haircut to the baseline as well would penalise the same deaths twice. The decomposition only holds if the model applies the effect as a relative reduction to unselected WHO-cohort mortality. This is an unverified inference.
- Trial populations usually exclude the sickest patients. This makes the haircut more defensible if effect sizes come from healthier trial populations.

**REVISED CRITIQUE**
On-treatment TB deaths are concentrated in the first 1–2 months in many high-burden cohorts. Zambia shows about 75%, though some cohorts show flatter timing. Deaths in this window are often among malnourished, advanced-HIV or very sick patients. The rifampicin–atorvastatin interaction is bidirectional, so whether benefit onset is delayed is **UNGROUNDED**. The share of the 6% that is addressable is likely below 100%. The 30% and 15% figures and the 3.6% result are **illustrative only**.
- The critique must state how the effect size was derived, to avoid double-counting.
- Strength: medium, direction uncertain-to-decreasing. This holds only if effect sizes come from unselected populations.

---

## Critique 2: Under-ascertained deaths push true mortality up

**OVERALL VERDICT: PARTIALLY VERIFIED.** The mechanism is sound and some direction-of-effect evidence exists. The magnitude is plausible but weakly grounded. There are definitional problems and a labelling error.

**CLAIM CHECK**
- **WHO outcome categories are as described. VERIFIED.** 
The categories are treatment success, failed, died, lost to follow-up and not evaluated.
 
The denominator is everyone who started rifampicin-susceptible treatment.
 So deaths among LTFU and not-evaluated patients are not in the "died" numerator.
- **Specific global percentages (5–6% died, 3–4% LTFU, a few percent not evaluated). UNVERIFIABLE from my searches.**
  - I confirmed only that 
global treatment success was 88% in 2023 and 2022.

  - Kenya's 2022 national data were about 
6% died and 5% lost to follow-up.

  - A Kenyan county surveillance dataset had 
5.5% died, 2.6% LTFU and 5.8% not evaluated.
 That makes LTFU plus NE 8.4% there, higher than the 6–7% assumed.
  - Not-evaluated can be very large in some programmes. 
Zimbabwe reports high percentages of not-evaluated outcomes.

- **A meaningful share of LTFU patients die. VERIFIED in direction. The 10–20% range is plausible but evidence is mixed.**
  - A Kilifi, Kenya tracing study (medRxiv preprint) 
found 14 of 140 patients identified for tracing (10%) had died, with 36 traced and 90 relocated.
 That matches the low end of the investigator's range.
  - 
A Georgia study of second-line (MDR/XDR) treatment found 107 of 461 LFU patients (23%) died.
 This is drug-resistant TB, so it is not a good analogue for drug-susceptible TB.
  - 
An Estonian study found 30% of the 102 traced LFU patients died.
 It mixed drug-susceptible and drug-resistant TB.
  - A Brazilian preprint found 
8.0% of LFU patients died, at a median of 17.5 months after LTFU.
 It also found 
a two- to three-fold increased hazard of late mortality after LTFU.

  - The Brazilian deaths occur long after the on-treatment window. This undermines treating them as "on-treatment mortality."
- **Deaths before treatment start or among untreated patients push true mortality up. PARTIALLY MISREPRESENTED.**
  - The 6% is a share of patients who started treatment, so pre-treatment deaths are outside both the numerator and the denominator. They do not make "mortality among treated patients" higher.
  - They matter only if the model's population is broader than the WHO treated cohort. In Cape Town, 
17.1% of initially lost patients died, 69.7% of them within 30 days.
 That is a different population.
  - Under WHO definitions, transfers out fall into "not evaluated". This is from my background knowledge, not verified in these searches.
- **The arithmetic is correct.** 0.6 and 1.4 pp are right, giving 6.6–7.4% and a 10–23% proportional rise.
- **Internal labelling error.** The title says "opposite of Critiques 1–2", but this is Critique 2. It presumably means Critiques 1 and 3. This should be fixed.

**EVIDENCE FOUND**
- The Kenyan surveillance paper says 
the vital status of the 8.4% who were LTFU or not evaluated could not be ascertained.
 This directly supports the under-ascertainment mechanism.
- The Kilifi tracing study (10%) supports the low end of the range. The drug-resistant TB studies (23–30%) are less applicable.
- The timing of deaths among LTFU patients undermines the "on-treatment" framing and the statin-attributable fraction.

**REVISED CRITIQUE**
WHO "died" excludes deaths among LTFU and not-evaluated patients. Tracing studies show non-trivial mortality among LTFU patients, about 10% in a Kenyan drug-susceptible-dominant setting and higher in drug-resistant cohorts. This could push true mortality among those who started treatment above 6%. A plausible range is perhaps +0.3 to +1.4 pp. The statin-attributable share of these deaths is uncertain, because they may occur after treatment interruption. The pre-treatment-death and untreated-case claims should be dropped or reframed, since they do not affect mortality among treated patients. Global WHO percentages are **UNVERIFIED**. Strength: **low-to-medium**, direction increases.

---

## Critique 3: Covariance between mortality and DALYs per death

**OVERALL VERDICT: PARTIALLY VERIFIED.** The logic and arithmetic are correct, and the direction of the age–mortality relationship is supported. The magnitude (−10 to −15%) rests entirely on invented numbers. The critique may not apply at all, depending on how the 27 was derived.

**CLAIM CHECK**
- **The arithmetic is correct. VERIFIED.**
  - Mean mortality is 0.7×4% + 0.3×12% = 6.4%.
  - Death-weighted DALYs are (0.98+0.54)/0.064 = 23.75.
  - Expected DALYs per patient are 1.52, against 6.4%×27 = 1.728, so 12% lower.
- **Higher-mortality subgroups tend to be older. VERIFIED.**
  - In a South African cohort of 190,472 TB cases, 
advancing age was the strongest risk factor for death, followed by HIV co-infection or unknown HIV status.

  - Kenyan data also associate older age with mortality: 
other comorbidities, clinical diagnosis, undernourishment and older age were positively associated with mortality.

  - Turkey: 
advanced age increased mortality risk.

- **HIV pushes the other way. PLAUSIBLE/VERIFIED in part.** 
HIV co-infection (OR 2.2) and unknown HIV status (OR 2.8) were independently associated with death.
 Age-at-death for HIV-positive patients was not retrieved. The Kenyan cohort had 
a median age of 32 years.
 This supports the point that many TB patients, and deaths, are young adults in high-HIV settings.
- **"If 27 was derived without death weighting, the product is biased." CONDITIONAL.**
  - GBD-style total DALYs (or YLLs) divided by total deaths is already a death-weighted mean. In that case no covariance bias arises.
  - The bias arises only if 27 came from something else, such as life expectancy at an average age or a patient-weighted average age. I cannot see how 27 was derived.
- **GBD 2021 can be used to compute this. PLAUSIBLE, not run.** I did not verify the specific GBD tables.
- **The −10 to −15% effect in low-HIV settings. UNGROUNDED.** It is an artefact of the invented group parameters. The investigator flagged this.

**EVIDENCE FOUND**
- The relevant quantity is DALYs per *averted* death, which depends on who benefits from the statin. The statin might benefit older or comorbid patients differently, which adds further uncertainty.
- Standard life-table YLLs overstate remaining life expectancy for sick patients. This is my own reasoning, not verified, and it suggests a further downward bias on top of the covariance issue.
- Direction is uncertain overall: age pushes DALYs down, HIV and young-adult TB push them up.

**REVISED CRITIQUE**
Mortality is positively associated with age, and years lost per death fall with age. If dalys_per_death was computed as a population or patient-weighted average, multiplying by mean mortality overstates expected DALYs averted. If it was computed as total DALYs divided by total deaths, which is the GBD approach, the bias largely disappears. In high-HIV settings, young-adult deaths push the opposite way. The size of the effect is **UNGROUNDED** and the sign is uncertain.
- The critique should be conditioned on how 27 was derived.
- A GBD age/HIV-stratified death-weighted YLL calculation would settle it.
- Strength: **low-to-medium**, direction **uncertain, leaning decreases** in low-HIV settings.

--- Critique: A global-average mortality may not match the countries where an atorvastatin adjunct would actually be deployed ---

I ran out of search budget partway through, so some items could not be checked. Where I rely on background knowledge instead of a retrieved source, I say so.

## Critique 1: Global-average mortality vs. deployment-country mix

**CLAIM CHECK**
- **Country-level on-treatment mortality (India ~4–5%, South Africa ~8–10%): UNVERIFIABLE this session.** My searches did not return WHO country outcome tables. The Investigator labeled these figures "from memory, UNVERIFIED". From my background knowledge, India sits below the global average and South Africa above it. Treat that as unconfirmed.
- **HIV prevalence drives country differences in on-treatment mortality: PLAUSIBLE.**
  - The ACT HIV trial gives indirect support. 
12-month death occurred in 44.1% of the dexamethasone arm and 49.0% of the placebo arm
 in HIV-positive adults with TB meningitis. That is a severe form of TB, not typical pulmonary TB.
  - It still shows how much HIV can raise mortality in some TB subpopulations.
- **"Weighted mean depends on deployment mix": TRUE arithmetically.** The 4.5% figure is only as good as the unverified country inputs. The 3.9% threshold comes from the model, which I cannot see.
- **Deployment countries (India, South Africa, Indonesia, Nigeria, Philippines): UNVERIFIABLE.** This is a list of plausible high-burden countries, not a sourced deployment plan.

**EVIDENCE FOUND**
- Nothing directly supports or refutes the country figures.
- One further consideration is my own inference, not sourced. Phase III trial sites (South Africa is common) may not match eventual deployment (India-heavy by case share). That would add a gap between trial-population mortality and deployment mortality.

**OVERALL VERDICT: PARTIALLY VERIFIED (hypothesis sound, evidence UNGROUNDED).**
- What survives: the logical point that a case-weighted mean replaces a global figure.
- What doesn't: every quantitative input is unverified.

**REVISED CRITIQUE**
- baseline_mortality is a global figure, and the right input is a case-weighted average over deployment countries.
- The direction is uncertain and depends on the HIV and age mix.
- All country figures are UNGROUNDED, so this is a sensitivity flag, not a demonstrated bias.
- Keep it as a low-to-medium strength flag. Retain it only if someone pulls the WHO Global TB Report cohort outcomes (death share among evaluated cases) for the top 5–8 countries.

---

## Critique 2: Industry base rates imply ~15–25%, not 40%

**CITATION CHECK**
- **BIO/Informa/QLS 2021 (2011–2020): VERIFIED for Phase II→III and Phase III→NDA/BLA.**
  - 
The table shows 28.9% for Phase II and 57.8% for Phase III.

  - A second paper reports its own Phase II→III estimates 
(28.4% for 2012–2020 and 28.8% for 2011–2019, close to BIO's 28.9%)
.
  - The ~91% filing→approval figure was not shown in my results. I believe it is ~90.6%, but this is unverified here.
  - The implied overall from Phase II (0.289 × 0.578 × 0.906 ≈ 15%) is arithmetically consistent.
- **Wong, Siah & Lo (2019), Biostatistics: the paper EXISTS.**
  - The citation is 
Biostatistics 2019;20(2):273–286
.
  - There is a corrigendum: 
errors were found in Tables 1 and 2, specifically the Phase 2→3 and Phase 3→APP columns
.
  - Whether its figures are "similar" to BIO's is UNVERIFIED. Anyone checking should use the corrected tables.
- **Infectious-disease-specific rates: PARTIALLY CONTRADICTED.** The Investigator assumed Phase III ≈ 65% for infectious disease. I found sources suggesting this may be too low.
  - One study reports that 
infectious diseases have the highest unconditional success rate at 14.0%, with a Phase III success rate of 80.9% and an application success rate of 95.6%
.
  - Another finds that 
anti-infective drugs have, in general, the highest hazard curves across all three phases
.
  - Wong/Siah/Lo also have a separate anti-infective paper: 
it uses 6,829 non-vaccine infectious-disease programs from 2000 to 2020
. I could not retrieve its numbers.

**CLAIM CHECK**
- **"All-indication P(II and III both succeed) ≈ 0.29 × 0.58 ≈ 17%": VERIFIED.** The inputs are verified and the arithmetic is correct.
- **"Infectious-disease-adjusted ≈ 24–26%, at or below the 0.26 break-even": NOT ROBUST.**
  - If Phase III is ~80% rather than 65%, and Phase II is 37–40%, the product is ~30–32%. That is above the break-even.
  - The 0.26 break-even is from the model, which I cannot see.
  - The conclusion is therefore sensitive to which infectious-disease dataset is used.
- **"Premium of 1.6–2.7×": arithmetically correct** (0.40/0.25 = 1.6; 0.40/0.15 ≈ 2.7). The "1.6×" end depends on the contested 65% assumption.
- **"Moving from 0.40 to 0.20–0.25 cuts expected cost-effectiveness 37–50%": VERIFIED arithmetically** (linear).
- **"Dominant failure mode is lack of efficacy, so repurposing helps mainly safety attrition": PLAUSIBLE.** This is widely accepted but I did not retrieve a source for it.
- **"CG names no reference class for 40%": UNVERIFIABLE.** I do not have the source model.
- **The decomposition (0.5 × 0.40–0.55 × 0.7–0.85 ≈ 0.14–0.30): the Investigator's own inference, labeled as such.**
  - P(adopted | III) of 0.7–0.85 is not an industry phase-transition parameter.
  - It is a different kind of parameter than the BIO benchmark, so the comparison to "industry 17%" is partly apples-to-oranges.

**EVIDENCE FOUND**
- The BIO and academic figures are corroborated.
- Infectious-disease/anti-infective programs do show above-average success, with a very high late-stage rate in at least one dataset. This partly undermines the "at or below break-even" claim and moves the reasonable range up.
- Success measured as "approval" is not the same as "adopted at scale in LMICs", which is the model's likely endpoint.

**OVERALL VERDICT: PARTIALLY VERIFIED.**
- What survives:
  - The all-indication base rate is ~15–17%.
  - 40% needs a stated justification and a named reference class.
  - Infectious disease is above average.
- What doesn't: the claim that the infectious-disease-adjusted figure is at or below 0.26 is not established.

**REVISED CRITIQUE**
- CG gives no reference class for 40%. Industry phase-transition data (BIO 2011–2020) give ~29% (Phase II→III) × ~58% (Phase III→filing), or ~17%, and ~15% to approval for all indications.
- Infectious-disease and anti-infective programs perform better than average. Estimates of the uplift vary, and one dataset puts Phase III success above 80%.
- A reasonable range for infectious-disease-adjusted P(II and III) is roughly 20–32%, which brackets the 0.26 break-even rather than clearly falling below it.
- The decomposition is the Investigator's own inference and should be flagged as such. The repurposing-premium argument is UNGROUNDED.
- Strength: medium-large, because the direction is robust but the magnitude and the break-even crossing are uncertain.

---

## Critique 3: TB-specific reference classes have a worse record than 40%

**CITATION CHECK**
- **REMoxTB, OFLOTUB, RIFAQUIN: VERIFIED.**
  - 
WHO states that REMoxTB, OFLOTUB and RIFAQUIN failed to demonstrate non-inferiority of shorter regimens
.
  - A pooled analysis confirms that 
in each of the three trials, the 4-month regimen did not satisfy non-inferiority criteria
.
  - Nuance: in RIFAQUIN, 
the 6-month regimen proved non-inferior, but non-inferiority could not be declared for the 4-month regimen
.
  - These are antibiotic-regimen trials with a non-inferiority design. They are not host-directed or adjunctive therapies, so they are an analogy for "surrogate to Phase III", not members of the HDT class.
  - The claim that they had "encouraging mouse and Phase II culture-conversion data" was not checked.
- **Study 31/A5349: VERIFIED.**
  - 
The 4-month rifapentine-moxifloxacin regimen was non-inferior to the standard 6-month regimen.

  - WHO issued a conditional recommendation: 
people aged 12 or older with drug-susceptible pulmonary TB may receive a 4-month regimen of isoniazid, rifapentine, moxifloxacin and pyrazinamide
.
  - The shortening class has a second success: 
the SHINE trial showed a 4-month regimen non-inferior to the 6-month regimen in children
. The Investigator didn't mention it.
- **ACT HIV (2023): VERIFIED.**
  - 
Death occurred in 44.1% (dexamethasone) vs 49.0% (placebo); HR 0.85, 95% CI 0.66–1.10, P = 0.22.

  - 
The earlier 2004 Vietnam trial showed benefit overall, though the benefit was uncertain in the 98 HIV-positive participants.

  - The Investigator's "did not generalize" framing is fair, but "looked effective in the earlier trial population" needs the caveat that the HIV-positive subgroup was small and uncertain from the start.
- **Thwaites 2004 (dexamethasone, TBM): VERIFIED (secondary).**
  - 
A Vietnam trial published in 2004 found that dexamethasone significantly reduced overall mortality from TB meningitis.

  - 
The relative risk of death was 0.69 (95% CI 0.52–0.92).

  - The newer LAST ACT trial muddies this: 
neither non-inferiority nor superiority of placebo was established in HIV-negative LTA4H CC/CT-genotype adults
. The authors still conclude that 
the pooled data support a modest survival benefit in HIV-negative adults
.
- **Vitamin D (Wejse 2009, Guinea-Bissau; Martineau 2011, London): NOT CHECKED (search budget).** From background knowledge, both are real and neither showed an overall primary-endpoint benefit. Martineau 2011 reported a genotype-specific subgroup effect. Treat as plausible, not verified.
- **Pravastatin mouse data (Karakousis group), Wallis & Hafner, Kolloli & Subbian: NOT CHECKED.**
- **"No HDT is WHO-recommended for drug-sensitive pulmonary TB": NOT CHECKED.** It is plausible, but I only verified the dexamethasone TBM recommendation context.

**CLAIM CHECK**
- **"Class success rate 10–20%": UNGROUNDED (the Investigator labeled it as inference).**
  - There are no denominators, and the class is defined post hoc from a few salient failures and successes.
  - The count includes at least three successes (Study 31, SHINE, TBM corticosteroids), so it is not a clean "mostly failures" record.
  - Design differences matter. Non-inferiority regimen-shortening trials and superiority adjunct trials have different success definitions.
- **"At 0.15, CE is ~38% of the base case": VERIFIED arithmetic** (0.15/0.40 = 0.375).
- **"Blend of TB class and industry priors gives 0.2–0.3": UNGROUNDED but reasonable.** It is the Investigator's own inference.
- **Estimated direction "uncertain" is inconsistent with the argument.** The whole argument points to a lower p_success.

**EVIDENCE FOUND**
- The strongest verified analogue for an anti-inflammatory adjunct is the corticosteroid sequence. There was a positive early trial in a mostly HIV-negative population (RR 0.69), then a null result in HIV-positive adults (HR 0.85, P = 0.22), then an ambiguous genotype-stratified trial. That supports a "benefit may be heterogeneous and not generalize" caution, and the population of statin trials matters.
- The shortening class is not uniformly bad. The negative result came from simple fluoroquinolone substitution, and the positive one from a different design (rifapentine plus moxifloxacin).

**OVERALL VERDICT: PARTIALLY VERIFIED.**
- What survives:
  - The antibiotic-shortening and ACT HIV facts are accurate.
  - A TB-specific prior is more pessimistic than a generic one.
- What doesn't: the quantitative class rate, and the vitamin D and HDT-pipeline claims, which are unverified here. Presenting regimen-shortening trials as HDT-class evidence overstates the relevance.

**REVISED CRITIQUE**
- No named reference class supports 40%. The nearest TB analogues are mixed:
  - Three fluoroquinolone 4-month trials (REMoxTB, OFLOTUB, RIFAQUIN) failed non-inferiority.
  - Study 31 succeeded and was conditionally recommended by WHO, and SHINE succeeded in children.
  - The anti-inflammatory adjunct dexamethasone worked in TBM overall, but ACT HIV was null in HIV-positive adults.
- No quantitative success rate for "TB host-directed therapy" is available, so a 10–20% rate is UNGROUNDED. A blended range of ~0.2–0.3 is plausible but also inferential.
- Vitamin D and statin-preclinical claims should be marked "unchecked, plausible" until sourced.
- Direction: lowers p_success. Strength: medium, not large, until a sourced class rate exists.

--- Critique: Industry phase-transition base rates put "II and III both succeed" at roughly 15–25%, so 40% requires an unstated premium of about 1.6–2.7× ---

I ran out of search budget partway through, so some items could not be checked. Where I rely on background knowledge instead of a retrieved source, I say so.

## Critique 1: Global-average mortality vs. deployment-country mix

**CLAIM CHECK**
- **Country-level on-treatment mortality (India ~4–5%, South Africa ~8–10%): UNVERIFIABLE this session.** My searches did not return WHO country outcome tables. The Investigator labeled these figures "from memory, UNVERIFIED". From my background knowledge, India sits below the global average and South Africa above it. Treat that as unconfirmed.
- **HIV prevalence drives country differences in on-treatment mortality: PLAUSIBLE.**
  - The ACT HIV trial gives indirect support. 
12-month death occurred in 44.1% of the dexamethasone arm and 49.0% of the placebo arm
 in HIV-positive adults with TB meningitis. That is a severe form of TB, not typical pulmonary TB.
  - It still shows how much HIV can raise mortality in some TB subpopulations.
- **"Weighted mean depends on deployment mix": TRUE arithmetically.** The 4.5% figure is only as good as the unverified country inputs. The 3.9% threshold comes from the model, which I cannot see.
- **Deployment countries (India, South Africa, Indonesia, Nigeria, Philippines): UNVERIFIABLE.** This is a list of plausible high-burden countries, not a sourced deployment plan.

**EVIDENCE FOUND**
- Nothing directly supports or refutes the country figures.
- One further consideration is my own inference, not sourced. Phase III trial sites (South Africa is common) may not match eventual deployment (India-heavy by case share). That would add a gap between trial-population mortality and deployment mortality.

**OVERALL VERDICT: PARTIALLY VERIFIED (hypothesis sound, evidence UNGROUNDED).**
- What survives: the logical point that a case-weighted mean replaces a global figure.
- What doesn't: every quantitative input is unverified.

**REVISED CRITIQUE**
- baseline_mortality is a global figure, and the right input is a case-weighted average over deployment countries.
- The direction is uncertain and depends on the HIV and age mix.
- All country figures are UNGROUNDED, so this is a sensitivity flag, not a demonstrated bias.
- Keep it as a low-to-medium strength flag. Retain it only if someone pulls the WHO Global TB Report cohort outcomes (death share among evaluated cases) for the top 5–8 countries.

---

## Critique 2: Industry base rates imply ~15–25%, not 40%

**CITATION CHECK**
- **BIO/Informa/QLS 2021 (2011–2020): VERIFIED for Phase II→III and Phase III→NDA/BLA.**
  - 
The table shows 28.9% for Phase II and 57.8% for Phase III.

  - A second paper reports its own Phase II→III estimates 
(28.4% for 2012–2020 and 28.8% for 2011–2019, close to BIO's 28.9%)
.
  - The ~91% filing→approval figure was not shown in my results. I believe it is ~90.6%, but this is unverified here.
  - The implied overall from Phase II (0.289 × 0.578 × 0.906 ≈ 15%) is arithmetically consistent.
- **Wong, Siah & Lo (2019), Biostatistics: the paper EXISTS.**
  - The citation is 
Biostatistics 2019;20(2):273–286
.
  - There is a corrigendum: 
errors were found in Tables 1 and 2, specifically the Phase 2→3 and Phase 3→APP columns
.
  - Whether its figures are "similar" to BIO's is UNVERIFIED. Anyone checking should use the corrected tables.
- **Infectious-disease-specific rates: PARTIALLY CONTRADICTED.** The Investigator assumed Phase III ≈ 65% for infectious disease. I found sources suggesting this may be too low.
  - One study reports that 
infectious diseases have the highest unconditional success rate at 14.0%, with a Phase III success rate of 80.9% and an application success rate of 95.6%
.
  - Another finds that 
anti-infective drugs have, in general, the highest hazard curves across all three phases
.
  - Wong/Siah/Lo also have a separate anti-infective paper: 
it uses 6,829 non-vaccine infectious-disease programs from 2000 to 2020
. I could not retrieve its numbers.

**CLAIM CHECK**
- **"All-indication P(II and III both succeed) ≈ 0.29 × 0.58 ≈ 17%": VERIFIED.** The inputs are verified and the arithmetic is correct.
- **"Infectious-disease-adjusted ≈ 24–26%, at or below the 0.26 break-even": NOT ROBUST.**
  - If Phase III is ~80% rather than 65%, and Phase II is 37–40%, the product is ~30–32%. That is above the break-even.
  - The 0.26 break-even is from the model, which I cannot see.
  - The conclusion is therefore sensitive to which infectious-disease dataset is used.
- **"Premium of 1.6–2.7×": arithmetically correct** (0.40/0.25 = 1.6; 0.40/0.15 ≈ 2.7). The "1.6×" end depends on the contested 65% assumption.
- **"Moving from 0.40 to 0.20–0.25 cuts expected cost-effectiveness 37–50%": VERIFIED arithmetically** (linear).
- **"Dominant failure mode is lack of efficacy, so repurposing helps mainly safety attrition": PLAUSIBLE.** This is widely accepted but I did not retrieve a source for it.
- **"CG names no reference class for 40%": UNVERIFIABLE.** I do not have the source model.
- **The decomposition (0.5 × 0.40–0.55 × 0.7–0.85 ≈ 0.14–0.30): the Investigator's own inference, labeled as such.**
  - P(adopted | III) of 0.7–0.85 is not an industry phase-transition parameter.
  - It is a different kind of parameter than the BIO benchmark, so the comparison to "industry 17%" is partly apples-to-oranges.

**EVIDENCE FOUND**
- The BIO and academic figures are corroborated.
- Infectious-disease/anti-infective programs do show above-average success, with a very high late-stage rate in at least one dataset. This partly undermines the "at or below break-even" claim and moves the reasonable range up.
- Success measured as "approval" is not the same as "adopted at scale in LMICs", which is the model's likely endpoint.

**OVERALL VERDICT: PARTIALLY VERIFIED.**
- What survives:
  - The all-indication base rate is ~15–17%.
  - 40% needs a stated justification and a named reference class.
  - Infectious disease is above average.
- What doesn't: the claim that the infectious-disease-adjusted figure is at or below 0.26 is not established.

**REVISED CRITIQUE**
- CG gives no reference class for 40%. Industry phase-transition data (BIO 2011–2020) give ~29% (Phase II→III) × ~58% (Phase III→filing), or ~17%, and ~15% to approval for all indications.
- Infectious-disease and anti-infective programs perform better than average. Estimates of the uplift vary, and one dataset puts Phase III success above 80%.
- A reasonable range for infectious-disease-adjusted P(II and III) is roughly 20–32%, which brackets the 0.26 break-even rather than clearly falling below it.
- The decomposition is the Investigator's own inference and should be flagged as such. The repurposing-premium argument is UNGROUNDED.
- Strength: medium-large, because the direction is robust but the magnitude and the break-even crossing are uncertain.

---

## Critique 3: TB-specific reference classes have a worse record than 40%

**CITATION CHECK**
- **REMoxTB, OFLOTUB, RIFAQUIN: VERIFIED.**
  - 
WHO states that REMoxTB, OFLOTUB and RIFAQUIN failed to demonstrate non-inferiority of shorter regimens
.
  - A pooled analysis confirms that 
in each of the three trials, the 4-month regimen did not satisfy non-inferiority criteria
.
  - Nuance: in RIFAQUIN, 
the 6-month regimen proved non-inferior, but non-inferiority could not be declared for the 4-month regimen
.
  - These are antibiotic-regimen trials with a non-inferiority design. They are not host-directed or adjunctive therapies, so they are an analogy for "surrogate to Phase III", not members of the HDT class.
  - The claim that they had "encouraging mouse and Phase II culture-conversion data" was not checked.
- **Study 31/A5349: VERIFIED.**
  - 
The 4-month rifapentine-moxifloxacin regimen was non-inferior to the standard 6-month regimen.

  - WHO issued a conditional recommendation: 
people aged 12 or older with drug-susceptible pulmonary TB may receive a 4-month regimen of isoniazid, rifapentine, moxifloxacin and pyrazinamide
.
  - The shortening class has a second success: 
the SHINE trial showed a 4-month regimen non-inferior to the 6-month regimen in children
. The Investigator didn't mention it.
- **ACT HIV (2023): VERIFIED.**
  - 
Death occurred in 44.1% (dexamethasone) vs 49.0% (placebo); HR 0.85, 95% CI 0.66–1.10, P = 0.22.

  - 
The earlier 2004 Vietnam trial showed benefit overall, though the benefit was uncertain in the 98 HIV-positive participants.

  - The Investigator's "did not generalize" framing is fair, but "looked effective in the earlier trial population" needs the caveat that the HIV-positive subgroup was small and uncertain from the start.
- **Thwaites 2004 (dexamethasone, TBM): VERIFIED (secondary).**
  - 
A Vietnam trial published in 2004 found that dexamethasone significantly reduced overall mortality from TB meningitis.

  - 
The relative risk of death was 0.69 (95% CI 0.52–0.92).

  - The newer LAST ACT trial muddies this: 
neither non-inferiority nor superiority of placebo was established in HIV-negative LTA4H CC/CT-genotype adults
. The authors still conclude that 
the pooled data support a modest survival benefit in HIV-negative adults
.
- **Vitamin D (Wejse 2009, Guinea-Bissau; Martineau 2011, London): NOT CHECKED (search budget).** From background knowledge, both are real and neither showed an overall primary-endpoint benefit. Martineau 2011 reported a genotype-specific subgroup effect. Treat as plausible, not verified.
- **Pravastatin mouse data (Karakousis group), Wallis & Hafner, Kolloli & Subbian: NOT CHECKED.**
- **"No HDT is WHO-recommended for drug-sensitive pulmonary TB": NOT CHECKED.** It is plausible, but I only verified the dexamethasone TBM recommendation context.

**CLAIM CHECK**
- **"Class success rate 10–20%": UNGROUNDED (the Investigator labeled it as inference).**
  - There are no denominators, and the class is defined post hoc from a few salient failures and successes.
  - The count includes at least three successes (Study 31, SHINE, TBM corticosteroids), so it is not a clean "mostly failures" record.
  - Design differences matter. Non-inferiority regimen-shortening trials and superiority adjunct trials have different success definitions.
- **"At 0.15, CE is ~38% of the base case": VERIFIED arithmetic** (0.15/0.40 = 0.375).
- **"Blend of TB class and industry priors gives 0.2–0.3": UNGROUNDED but reasonable.** It is the Investigator's own inference.
- **Estimated direction "uncertain" is inconsistent with the argument.** The whole argument points to a lower p_success.

**EVIDENCE FOUND**
- The strongest verified analogue for an anti-inflammatory adjunct is the corticosteroid sequence. There was a positive early trial in a mostly HIV-negative population (RR 0.69), then a null result in HIV-positive adults (HR 0.85, P = 0.22), then an ambiguous genotype-stratified trial. That supports a "benefit may be heterogeneous and not generalize" caution, and the population of statin trials matters.
- The shortening class is not uniformly bad. The negative result came from simple fluoroquinolone substitution, and the positive one from a different design (rifapentine plus moxifloxacin).

**OVERALL VERDICT: PARTIALLY VERIFIED.**
- What survives:
  - The antibiotic-shortening and ACT HIV facts are accurate.
  - A TB-specific prior is more pessimistic than a generic one.
- What doesn't: the quantitative class rate, and the vitamin D and HDT-pipeline claims, which are unverified here. Presenting regimen-shortening trials as HDT-class evidence overstates the relevance.

**REVISED CRITIQUE**
- No named reference class supports 40%. The nearest TB analogues are mixed:
  - Three fluoroquinolone 4-month trials (REMoxTB, OFLOTUB, RIFAQUIN) failed non-inferiority.
  - Study 31 succeeded and was conditionally recommended by WHO, and SHINE succeeded in children.
  - The anti-inflammatory adjunct dexamethasone worked in TBM overall, but ACT HIV was null in HIV-positive adults.
- No quantitative success rate for "TB host-directed therapy" is available, so a 10–20% rate is UNGROUNDED. A blended range of ~0.2–0.3 is plausible but also inferential.
- Vitamin D and statin-preclinical claims should be marked "unchecked, plausible" until sourced.
- Direction: lowers p_success. Strength: medium, not large, until a sourced class rate exists.

--- Critique: The TB-specific reference classes (host-directed therapy, adjunctives, regimen-shortening) have a much worse record than 40% ---

I ran out of search budget partway through, so some items could not be checked. Where I rely on background knowledge instead of a retrieved source, I say so.

## Critique 1: Global-average mortality vs. deployment-country mix

**CLAIM CHECK**
- **Country-level on-treatment mortality (India ~4–5%, South Africa ~8–10%): UNVERIFIABLE this session.** My searches did not return WHO country outcome tables. The Investigator labeled these figures "from memory, UNVERIFIED". From my background knowledge, India sits below the global average and South Africa above it. Treat that as unconfirmed.
- **HIV prevalence drives country differences in on-treatment mortality: PLAUSIBLE.**
  - The ACT HIV trial gives indirect support. 
12-month death occurred in 44.1% of the dexamethasone arm and 49.0% of the placebo arm
 in HIV-positive adults with TB meningitis. That is a severe form of TB, not typical pulmonary TB.
  - It still shows how much HIV can raise mortality in some TB subpopulations.
- **"Weighted mean depends on deployment mix": TRUE arithmetically.** The 4.5% figure is only as good as the unverified country inputs. The 3.9% threshold comes from the model, which I cannot see.
- **Deployment countries (India, South Africa, Indonesia, Nigeria, Philippines): UNVERIFIABLE.** This is a list of plausible high-burden countries, not a sourced deployment plan.

**EVIDENCE FOUND**
- Nothing directly supports or refutes the country figures.
- One further consideration is my own inference, not sourced. Phase III trial sites (South Africa is common) may not match eventual deployment (India-heavy by case share). That would add a gap between trial-population mortality and deployment mortality.

**OVERALL VERDICT: PARTIALLY VERIFIED (hypothesis sound, evidence UNGROUNDED).**
- What survives: the logical point that a case-weighted mean replaces a global figure.
- What doesn't: every quantitative input is unverified.

**REVISED CRITIQUE**
- baseline_mortality is a global figure, and the right input is a case-weighted average over deployment countries.
- The direction is uncertain and depends on the HIV and age mix.
- All country figures are UNGROUNDED, so this is a sensitivity flag, not a demonstrated bias.
- Keep it as a low-to-medium strength flag. Retain it only if someone pulls the WHO Global TB Report cohort outcomes (death share among evaluated cases) for the top 5–8 countries.

---

## Critique 2: Industry base rates imply ~15–25%, not 40%

**CITATION CHECK**
- **BIO/Informa/QLS 2021 (2011–2020): VERIFIED for Phase II→III and Phase III→NDA/BLA.**
  - 
The table shows 28.9% for Phase II and 57.8% for Phase III.

  - A second paper reports its own Phase II→III estimates 
(28.4% for 2012–2020 and 28.8% for 2011–2019, close to BIO's 28.9%)
.
  - The ~91% filing→approval figure was not shown in my results. I believe it is ~90.6%, but this is unverified here.
  - The implied overall from Phase II (0.289 × 0.578 × 0.906 ≈ 15%) is arithmetically consistent.
- **Wong, Siah & Lo (2019), Biostatistics: the paper EXISTS.**
  - The citation is 
Biostatistics 2019;20(2):273–286
.
  - There is a corrigendum: 
errors were found in Tables 1 and 2, specifically the Phase 2→3 and Phase 3→APP columns
.
  - Whether its figures are "similar" to BIO's is UNVERIFIED. Anyone checking should use the corrected tables.
- **Infectious-disease-specific rates: PARTIALLY CONTRADICTED.** The Investigator assumed Phase III ≈ 65% for infectious disease. I found sources suggesting this may be too low.
  - One study reports that 
infectious diseases have the highest unconditional success rate at 14.0%, with a Phase III success rate of 80.9% and an application success rate of 95.6%
.
  - Another finds that 
anti-infective drugs have, in general, the highest hazard curves across all three phases
.
  - Wong/Siah/Lo also have a separate anti-infective paper: 
it uses 6,829 non-vaccine infectious-disease programs from 2000 to 2020
. I could not retrieve its numbers.

**CLAIM CHECK**
- **"All-indication P(II and III both succeed) ≈ 0.29 × 0.58 ≈ 17%": VERIFIED.** The inputs are verified and the arithmetic is correct.
- **"Infectious-disease-adjusted ≈ 24–26%, at or below the 0.26 break-even": NOT ROBUST.**
  - If Phase III is ~80% rather than 65%, and Phase II is 37–40%, the product is ~30–32%. That is above the break-even.
  - The 0.26 break-even is from the model, which I cannot see.
  - The conclusion is therefore sensitive to which infectious-disease dataset is used.
- **"Premium of 1.6–2.7×": arithmetically correct** (0.40/0.25 = 1.6; 0.40/0.15 ≈ 2.7). The "1.6×" end depends on the contested 65% assumption.
- **"Moving from 0.40 to 0.20–0.25 cuts expected cost-effectiveness 37–50%": VERIFIED arithmetically** (linear).
- **"Dominant failure mode is lack of efficacy, so repurposing helps mainly safety attrition": PLAUSIBLE.** This is widely accepted but I did not retrieve a source for it.
- **"CG names no reference class for 40%": UNVERIFIABLE.** I do not have the source model.
- **The decomposition (0.5 × 0.40–0.55 × 0.7–0.85 ≈ 0.14–0.30): the Investigator's own inference, labeled as such.**
  - P(adopted | III) of 0.7–0.85 is not an industry phase-transition parameter.
  - It is a different kind of parameter than the BIO benchmark, so the comparison to "industry 17%" is partly apples-to-oranges.

**EVIDENCE FOUND**
- The BIO and academic figures are corroborated.
- Infectious-disease/anti-infective programs do show above-average success, with a very high late-stage rate in at least one dataset. This partly undermines the "at or below break-even" claim and moves the reasonable range up.
- Success measured as "approval" is not the same as "adopted at scale in LMICs", which is the model's likely endpoint.

**OVERALL VERDICT: PARTIALLY VERIFIED.**
- What survives:
  - The all-indication base rate is ~15–17%.
  - 40% needs a stated justification and a named reference class.
  - Infectious disease is above average.
- What doesn't: the claim that the infectious-disease-adjusted figure is at or below 0.26 is not established.

**REVISED CRITIQUE**
- CG gives no reference class for 40%. Industry phase-transition data (BIO 2011–2020) give ~29% (Phase II→III) × ~58% (Phase III→filing), or ~17%, and ~15% to approval for all indications.
- Infectious-disease and anti-infective programs perform better than average. Estimates of the uplift vary, and one dataset puts Phase III success above 80%.
- A reasonable range for infectious-disease-adjusted P(II and III) is roughly 20–32%, which brackets the 0.26 break-even rather than clearly falling below it.
- The decomposition is the Investigator's own inference and should be flagged as such. The repurposing-premium argument is UNGROUNDED.
- Strength: medium-large, because the direction is robust but the magnitude and the break-even crossing are uncertain.

---

## Critique 3: TB-specific reference classes have a worse record than 40%

**CITATION CHECK**
- **REMoxTB, OFLOTUB, RIFAQUIN: VERIFIED.**
  - 
WHO states that REMoxTB, OFLOTUB and RIFAQUIN failed to demonstrate non-inferiority of shorter regimens
.
  - A pooled analysis confirms that 
in each of the three trials, the 4-month regimen did not satisfy non-inferiority criteria
.
  - Nuance: in RIFAQUIN, 
the 6-month regimen proved non-inferior, but non-inferiority could not be declared for the 4-month regimen
.
  - These are antibiotic-regimen trials with a non-inferiority design. They are not host-directed or adjunctive therapies, so they are an analogy for "surrogate to Phase III", not members of the HDT class.
  - The claim that they had "encouraging mouse and Phase II culture-conversion data" was not checked.
- **Study 31/A5349: VERIFIED.**
  - 
The 4-month rifapentine-moxifloxacin regimen was non-inferior to the standard 6-month regimen.

  - WHO issued a conditional recommendation: 
people aged 12 or older with drug-susceptible pulmonary TB may receive a 4-month regimen of isoniazid, rifapentine, moxifloxacin and pyrazinamide
.
  - The shortening class has a second success: 
the SHINE trial showed a 4-month regimen non-inferior to the 6-month regimen in children
. The Investigator didn't mention it.
- **ACT HIV (2023): VERIFIED.**
  - 
Death occurred in 44.1% (dexamethasone) vs 49.0% (placebo); HR 0.85, 95% CI 0.66–1.10, P = 0.22.

  - 
The earlier 2004 Vietnam trial showed benefit overall, though the benefit was uncertain in the 98 HIV-positive participants.

  - The Investigator's "did not generalize" framing is fair, but "looked effective in the earlier trial population" needs the caveat that the HIV-positive subgroup was small and uncertain from the start.
- **Thwaites 2004 (dexamethasone, TBM): VERIFIED (secondary).**
  - 
A Vietnam trial published in 2004 found that dexamethasone significantly reduced overall mortality from TB meningitis.

  - 
The relative risk of death was 0.69 (95% CI 0.52–0.92).

  - The newer LAST ACT trial muddies this: 
neither non-inferiority nor superiority of placebo was established in HIV-negative LTA4H CC/CT-genotype adults
. The authors still conclude that 
the pooled data support a modest survival benefit in HIV-negative adults
.
- **Vitamin D (Wejse 2009, Guinea-Bissau; Martineau 2011, London): NOT CHECKED (search budget).** From background knowledge, both are real and neither showed an overall primary-endpoint benefit. Martineau 2011 reported a genotype-specific subgroup effect. Treat as plausible, not verified.
- **Pravastatin mouse data (Karakousis group), Wallis & Hafner, Kolloli & Subbian: NOT CHECKED.**
- **"No HDT is WHO-recommended for drug-sensitive pulmonary TB": NOT CHECKED.** It is plausible, but I only verified the dexamethasone TBM recommendation context.

**CLAIM CHECK**
- **"Class success rate 10–20%": UNGROUNDED (the Investigator labeled it as inference).**
  - There are no denominators, and the class is defined post hoc from a few salient failures and successes.
  - The count includes at least three successes (Study 31, SHINE, TBM corticosteroids), so it is not a clean "mostly failures" record.
  - Design differences matter. Non-inferiority regimen-shortening trials and superiority adjunct trials have different success definitions.
- **"At 0.15, CE is ~38% of the base case": VERIFIED arithmetic** (0.15/0.40 = 0.375).
- **"Blend of TB class and industry priors gives 0.2–0.3": UNGROUNDED but reasonable.** It is the Investigator's own inference.
- **Estimated direction "uncertain" is inconsistent with the argument.** The whole argument points to a lower p_success.

**EVIDENCE FOUND**
- The strongest verified analogue for an anti-inflammatory adjunct is the corticosteroid sequence. There was a positive early trial in a mostly HIV-negative population (RR 0.69), then a null result in HIV-positive adults (HR 0.85, P = 0.22), then an ambiguous genotype-stratified trial. That supports a "benefit may be heterogeneous and not generalize" caution, and the population of statin trials matters.
- The shortening class is not uniformly bad. The negative result came from simple fluoroquinolone substitution, and the positive one from a different design (rifapentine plus moxifloxacin).

**OVERALL VERDICT: PARTIALLY VERIFIED.**
- What survives:
  - The antibiotic-shortening and ACT HIV facts are accurate.
  - A TB-specific prior is more pessimistic than a generic one.
- What doesn't: the quantitative class rate, and the vitamin D and HDT-pipeline claims, which are unverified here. Presenting regimen-shortening trials as HDT-class evidence overstates the relevance.

**REVISED CRITIQUE**
- No named reference class supports 40%. The nearest TB analogues are mixed:
  - Three fluoroquinolone 4-month trials (REMoxTB, OFLOTUB, RIFAQUIN) failed non-inferiority.
  - Study 31 succeeded and was conditionally recommended by WHO, and SHINE succeeded in children.
  - The anti-inflammatory adjunct dexamethasone worked in TBM overall, but ACT HIV was null in HIV-positive adults.
- No quantitative success rate for "TB host-directed therapy" is available, so a 10–20% rate is UNGROUNDED. A blended range of ~0.2–0.3 is plausible but also inferential.
- Vitamin D and statin-preclinical claims should be marked "unchecked, plausible" until sourced.
- Direction: lowers p_success. Strength: medium, not large, until a sourced class rate exists.

--- Critique: "Success" probably means a surrogate or composite endpoint, but the model needs a 10% mortality reduction, so P(adopted AND 10% mortality benefit) < P(trials succeed) ---

**Scope note:** No source materials were attached, and I found nothing public on the CG model. I could not check any CG parameter: p_success = 0.40, the 10% relative mortality reduction, 60% uptake, the $7M cost, the 8-year timeline, the 0.26 break-even threshold, or how the Phase IIc defines success. Every claim about the CG model is therefore unverified. I checked the external trial facts and the arithmetic.

---

## Critique 1: Surrogate or composite "success" versus the 10% mortality-reduction assumption

**OVERALL VERDICT: PARTIALLY VERIFIED.** The arithmetic and the endpoint claims check out. The 4% baseline mortality is probably too high for DS-TB trials, which makes the argument stronger. The 5–7% "realized RR" and the "large" magnitude are ungrounded.

**CLAIM CHECK**
- **Sample-size arithmetic (4% → 3.6%, about 36,000 per arm): VERIFIED.** I recomputed it. The sum p₁q₁ + p₂q₂ is 0.0731 and d² is 1.6×10⁻⁵. That gives about 35,800 per arm.
- **"Even at 6% it is tens of thousands per arm": VERIFIED.** At 6% → 5.4% I get about 23,400 per arm.
- **Standard TB Phase III trials enroll hundreds to a few thousand: VERIFIED.**
  - 
Study 31 had 2,234 participants assessable for its primary outcome.

  - TRUNCATE-TB's two arms shown in the NEJM table had 
181 and 184 participants.

  - I did not find the TRUNCATE-TB total enrollment.
- **Primary endpoints are composites or surrogates: VERIFIED, with a nuance.**
  - 
Study 31's primary efficacy outcome was survival free of tuberculosis at 12 months.

  - 
REMoxTB's primary outcome was a composite of bacteriological or clinical failure or relapse within 18 months.

  - 
TRUNCATE-TB's primary outcome was a composite of death, ongoing treatment, or active disease at week 96.

  - 
Regulatory guidance and recent Phase III trials use a composite of mainly bacteriological failure and relapse.

  - Death is a component of some of these composites, so they are not purely bacteriological surrogates. None of them tests all-cause mortality alone.
- **Baseline mortality of about 4% in DS-TB trial populations: LIKELY OVERSTATED.**
  - In Study 31, 
mortality was 0.6% in the overall study population.

  - 
Among people with HIV on treatment it was 1.5%.

  - WHO's review reports 
0.4% all-cause mortality within 14 days of the end of treatment.

  - At around 1% baseline, a 10% relative reduction would need several hundred thousand participants. Programmatic mortality of 4–6% (Critique 1's range) is plausible from general knowledge, but I did not verify it here.
- **Surrogate-to-mortality relationship for TB adjuncts is ungrounded: AGREED.** I found no validated link.
- **Success may be declared on a non-mortality endpoint (supported for adjuncts):**
  - A recent review says 
host-directed therapy trial designs have focused on safety, biological activity and intermediate outcomes, rather than being powered for mortality.

  - It also says 
no adjunctive host-directed therapy has shown sufficient, reproducible efficacy for routine use.

- **"If E[RR | surrogate success] is 5–7%, benefit falls 30–50%": arithmetic correct, premise UNGROUNDED.** 5–7% versus 10% is a 30–50% shortfall. The 5–7% figure is an assumption.

**EVIDENCE FOUND**
- **Higher-mortality populations are less extreme but still large.**
  - TB Fast Track's primary outcome was all-cause mortality in advanced HIV: 
19.0 versus 21.6 deaths per 100 person-years, HR 0.92, not significant.

  - At 20% baseline, a 10% relative reduction needs about 6,000 per arm by the Critique's formula (my calculation). That is still large.
- **TB meningitis is the best-grounded case for a mortality endpoint.** 
Dexamethasone is the only evidence-based adjunctive therapy there and gives a modest reduction in short-term mortality.
 If the CG drug targets TBM or advanced HIV, the critique's baseline changes materially. I could not tell which population CG uses.
- **Sample-size concerns also apply at Phase II.** In the four-drug HDT Phase 2 trial, 
the main shortcomings were a small sample size and low statistical power.
 
Its efficacy signal was FEV₁, a predictor of long-term all-cause mortality.
 That is a surrogate-based "success" in this class.
- **Cost implication:** a mortality-powered Phase III of 12,000 to 70,000 participants would likely cost far more than a $7M budget covering later trials. This is my inference, not verified.

**REVISED CRITIQUE (strength: MEDIUM–LARGE, direction: decreases)**
A Phase III TB trial powered for a 10% relative mortality reduction would need on the order of 10⁴–10⁵ participants. This holds for baseline mortality from about 1% to about 20%, and the required size is larger at low baseline mortality (my calculations). Published Phase III TB trials (Study 31, REMoxTB, TRUNCATE-TB) used composite clinical endpoints and enrolled hundreds to low thousands. Trial "success" is therefore unlikely to demonstrate a 10% mortality benefit directly. The model should either (a) state how the 10% was derived, or (b) run a sensitivity analysis with E[RR | trial success] below 10%. **UNGROUNDED:** the 5–7% figure and the 30–50% loss. The "4%" baseline should be replaced with a population-specific figure. Trial-population mortality in DS-TB is closer to 0.4–1.5%.

---

## Critique 2: Missing P(adoption | Phase III success) and P(Phase III funded | IIc success)

**OVERALL VERDICT: PARTIALLY VERIFIED.** The logic and arithmetic hold. The key dependency, how the 60% uptake was derived, is unverifiable here. The quantitative inputs (0.75–0.85, 0.8) are admitted guesses.

**CLAIM CHECK**
- **Arithmetic: VERIFIED.**
  - 0.40 × 0.75 = 0.30, a 25% reduction.
  - 0.40 × 0.85 = 0.34, a 15% reduction.
  - Applying a further 0.8 funding factor gives 0.24–0.27, which is near the 0.26 threshold.
  - The threshold itself is a CG figure I could not check.
- **WHO recommendations go through a guideline development group and evidence review: VERIFIED in outline.**
  - For Study 31, 
a WHO-convened GDG considered the 4-month regimen.

  - 
The other 4-month arm did not meet non-inferiority and was not reviewed by the GDG.

  - That document is a June 2021 WHO rapid communication, so adoption can be quick for a clean positive Phase III. The 2021 rapid communication followed Study 31's results within a short window. I did not verify the exact timing.
  - I did not find the GRADE rating wording on that page.
- **A conditional recommendation or none for low-certainty mortality evidence: PLAUSIBLE, UNVERIFIED.** It matches how GRADE works, but I found no TB-specific example.
- **Generics lack a commercial sponsor, so funding risk is higher: PLAUSIBLE.** Repurposed-drug HDT trials in the results were philanthropy- or public-funded. For example, 
the HDT Phase 2 trial was supported by the Gates Foundation and the South African MRC.
 This is consistent with the critique but does not quantify P(funded).
- **"Many Phase II→III failures are strategic or funding exits": PLAUSIBLE.** This matches general industry analyses, but I did not verify it here.
- **60% uptake covers country-level implementation only: UNVERIFIABLE.** The critique itself concedes it collapses to a documentation issue if the 60% already embeds adoption.

**EVIDENCE FOUND**
- No source gives P(adoption | positive Phase III) for TB adjuncts. The Study 31 and WHO pathway shows a clean non-inferiority trial being adopted within months, which argues against a heavy discount in the best case. An adjunct with only low-certainty mortality evidence (Critique 1) is the harder case, and this links the two critiques.
- The cost-versus-funding gap is also linked to Critique 1. A mortality-powered Phase III is much more expensive than a standard TB composite-endpoint trial, so P(funded) is not independent of the endpoint.

**REVISED CRITIQUE (strength: MEDIUM, conditional)**
The CG chain should show explicit factors for P(Phase III funded | IIc success) and P(WHO or national adoption | Phase III success), or state that the 60% uptake already includes them. The critique's directional claim (decreases) follows if either factor is below 1. **UNGROUNDED:** the values 0.75–0.85 and 0.8. Treat the 15–25% reduction as an illustrative sensitivity range, not an estimate. The "near the 0.26 threshold" claim holds only if CG's break-even really is 0.26 and the 60% excludes adoption.

---

## Critique 3: Phase IIc as a weak gate

**OVERALL VERDICT: PARTIALLY VERIFIED.** The REMoxTB precedent and the statistical point are valid. The premise that the IIc is a PK or dose-finding trial is unverified, and TB usage of "Phase IIc" may contradict it. The direction claim is internally inconsistent. The "winner's curse" argument is partly misapplied. The cross-reference to Critique 2 is wrong.

**CLAIM CHECK**
- **REMoxTB: early culture-conversion signals did not translate to Phase III: VERIFIED.**
  - 
Earlier time to culture conversion failed to predict successful 4-month fluoroquinolone regimens and had limited use as a surrogate in REMoxTB.

  - A REMoxTB reanalysis found 
faster culture conversion with the moxifloxacin regimens, even though the smear-conversion analysis showed no treatment difference.

  - 
Culture conversion has only a limited role in deciding which regimens advance to Phase III.

- **"See Critique 2": WRONG REFERENCE.** REMoxTB is not discussed in Critique 2, only in Critique 1's suggested evidence.
- **Phase IIc is mainly dose-finding or PK/safety, as the "exclusion list implies": UNVERIFIABLE, and RISKY.**
  - In the TB field, Phase IIb trials usually use culture-conversion endpoints: 
Phase IIb trials continue to use culture-conversion primary endpoints as the best available marker.

  - From general knowledge, "Phase IIc" in TB usually means a larger or longer proof-of-efficacy trial with clinical-outcome endpoints. I did not confirm this by search.
  - If so, the critique's premise that P(IIc) is 0.6–0.8 and uninformative may be wrong. The protocol or grant rationale needs checking, which the Investigator also recommended.
- **Industry Phase II success of about 29%: PLAUSIBLE, NOT VERIFIED HERE.** The figure matches my recollection of Phase II→III transition rates in industry benchmarking. It is a transition rate, not Phase II→approval, so the critique's phrase "Phase II→approval statistics" mixes two measures. Industry likelihood of approval from Phase II is much lower than 40%, which would support the broader point that CG's 40% for both stages is high (not verified).
- **0.7 × 0.3 = 0.21: arithmetic correct.** The 0.3 for P(III | weak signal) is an assumption with no support. Nothing in the critique shows that 0.3 is a better estimate than 0.57, the value implied by 0.40 ÷ 0.7.
- **E[p·RR] ≠ p·E[RR] when both depend on the true effect: VALID.** This is basic probability: the two differ by the covariance.
- **Winner's curse (realized effect below the planning value): PARTLY MISAPPLIED.** Winner's curse biases the estimated effect in a successful trial. Deaths averted depend on the true effect. Conditional on success, the true effect is selected upward, which is the opposite direction, as the critique acknowledges. The net direction is therefore ambiguous. This conflicts with the critique's header "Estimated Direction: decreases", and with its own "direction is ambiguous".
- **"Same linear effect on p_success as Critique 1": MINOR ERROR.** Critique 1 is about the RR term, not p_success.

**EVIDENCE FOUND**
- Phase 2 HDT trials in TB often define success by safety and surrogates. The four-HDT Phase 2 trial in South Africa (
200 patients
) assessed 
safety and preliminary efficacy.
 Its efficacy signal was FEV₁ recovery, 
a predictor of long-term all-cause mortality.
 This supports the "weak gate" idea for HDT-type adjuncts in general. It does not show how this specific IIc defines success.
- 
More data are needed before any endpoint can be used as a surrogate in a confirmatory Phase III trial.
 That fits the concern that Phase II signals transmit little information.

**REVISED CRITIQUE (strength: LOW–MEDIUM, direction: ambiguous, conditional on IIc definition)**
If the IIc endpoint is PK, dose or surrogate-based (a condition not yet verified), then P(IIc success) is likely high. Phase III then carries most of the risk, and the realistic joint probability could fall below 0.40. REMoxTB is a verified precedent for Phase II signals not translating. Because p_success and the true effect size are correlated, E[p·RR] ≠ p·E[RR]. Whether this raises or lowers the expected benefit needs a scenario analysis over a prior on the true effect. The winner's-curse point should be dropped or reframed as an effect-size selection argument. **UNGROUNDED:** P(IIc) = 0.7, P(III | weak signal) = 0.3, the 0.21 product, and the premise that IIc is dose-finding. **Correct** the "see Critique 2" reference to Critique 1 and fix the "Phase II→approval" wording.

--- Critique: P(adoption | Phase III success) and P(Phase III gets funded and run | Phase IIc success) are missing, and the 60% uptake factor may not cover them ---

**Scope note:** No source materials were attached, and I found nothing public on the CG model. I could not check any CG parameter: p_success = 0.40, the 10% relative mortality reduction, 60% uptake, the $7M cost, the 8-year timeline, the 0.26 break-even threshold, or how the Phase IIc defines success. Every claim about the CG model is therefore unverified. I checked the external trial facts and the arithmetic.

---

## Critique 1: Surrogate or composite "success" versus the 10% mortality-reduction assumption

**OVERALL VERDICT: PARTIALLY VERIFIED.** The arithmetic and the endpoint claims check out. The 4% baseline mortality is probably too high for DS-TB trials, which makes the argument stronger. The 5–7% "realized RR" and the "large" magnitude are ungrounded.

**CLAIM CHECK**
- **Sample-size arithmetic (4% → 3.6%, about 36,000 per arm): VERIFIED.** I recomputed it. The sum p₁q₁ + p₂q₂ is 0.0731 and d² is 1.6×10⁻⁵. That gives about 35,800 per arm.
- **"Even at 6% it is tens of thousands per arm": VERIFIED.** At 6% → 5.4% I get about 23,400 per arm.
- **Standard TB Phase III trials enroll hundreds to a few thousand: VERIFIED.**
  - 
Study 31 had 2,234 participants assessable for its primary outcome.

  - TRUNCATE-TB's two arms shown in the NEJM table had 
181 and 184 participants.

  - I did not find the TRUNCATE-TB total enrollment.
- **Primary endpoints are composites or surrogates: VERIFIED, with a nuance.**
  - 
Study 31's primary efficacy outcome was survival free of tuberculosis at 12 months.

  - 
REMoxTB's primary outcome was a composite of bacteriological or clinical failure or relapse within 18 months.

  - 
TRUNCATE-TB's primary outcome was a composite of death, ongoing treatment, or active disease at week 96.

  - 
Regulatory guidance and recent Phase III trials use a composite of mainly bacteriological failure and relapse.

  - Death is a component of some of these composites, so they are not purely bacteriological surrogates. None of them tests all-cause mortality alone.
- **Baseline mortality of about 4% in DS-TB trial populations: LIKELY OVERSTATED.**
  - In Study 31, 
mortality was 0.6% in the overall study population.

  - 
Among people with HIV on treatment it was 1.5%.

  - WHO's review reports 
0.4% all-cause mortality within 14 days of the end of treatment.

  - At around 1% baseline, a 10% relative reduction would need several hundred thousand participants. Programmatic mortality of 4–6% (Critique 1's range) is plausible from general knowledge, but I did not verify it here.
- **Surrogate-to-mortality relationship for TB adjuncts is ungrounded: AGREED.** I found no validated link.
- **Success may be declared on a non-mortality endpoint (supported for adjuncts):**
  - A recent review says 
host-directed therapy trial designs have focused on safety, biological activity and intermediate outcomes, rather than being powered for mortality.

  - It also says 
no adjunctive host-directed therapy has shown sufficient, reproducible efficacy for routine use.

- **"If E[RR | surrogate success] is 5–7%, benefit falls 30–50%": arithmetic correct, premise UNGROUNDED.** 5–7% versus 10% is a 30–50% shortfall. The 5–7% figure is an assumption.

**EVIDENCE FOUND**
- **Higher-mortality populations are less extreme but still large.**
  - TB Fast Track's primary outcome was all-cause mortality in advanced HIV: 
19.0 versus 21.6 deaths per 100 person-years, HR 0.92, not significant.

  - At 20% baseline, a 10% relative reduction needs about 6,000 per arm by the Critique's formula (my calculation). That is still large.
- **TB meningitis is the best-grounded case for a mortality endpoint.** 
Dexamethasone is the only evidence-based adjunctive therapy there and gives a modest reduction in short-term mortality.
 If the CG drug targets TBM or advanced HIV, the critique's baseline changes materially. I could not tell which population CG uses.
- **Sample-size concerns also apply at Phase II.** In the four-drug HDT Phase 2 trial, 
the main shortcomings were a small sample size and low statistical power.
 
Its efficacy signal was FEV₁, a predictor of long-term all-cause mortality.
 That is a surrogate-based "success" in this class.
- **Cost implication:** a mortality-powered Phase III of 12,000 to 70,000 participants would likely cost far more than a $7M budget covering later trials. This is my inference, not verified.

**REVISED CRITIQUE (strength: MEDIUM–LARGE, direction: decreases)**
A Phase III TB trial powered for a 10% relative mortality reduction would need on the order of 10⁴–10⁵ participants. This holds for baseline mortality from about 1% to about 20%, and the required size is larger at low baseline mortality (my calculations). Published Phase III TB trials (Study 31, REMoxTB, TRUNCATE-TB) used composite clinical endpoints and enrolled hundreds to low thousands. Trial "success" is therefore unlikely to demonstrate a 10% mortality benefit directly. The model should either (a) state how the 10% was derived, or (b) run a sensitivity analysis with E[RR | trial success] below 10%. **UNGROUNDED:** the 5–7% figure and the 30–50% loss. The "4%" baseline should be replaced with a population-specific figure. Trial-population mortality in DS-TB is closer to 0.4–1.5%.

---

## Critique 2: Missing P(adoption | Phase III success) and P(Phase III funded | IIc success)

**OVERALL VERDICT: PARTIALLY VERIFIED.** The logic and arithmetic hold. The key dependency, how the 60% uptake was derived, is unverifiable here. The quantitative inputs (0.75–0.85, 0.8) are admitted guesses.

**CLAIM CHECK**
- **Arithmetic: VERIFIED.**
  - 0.40 × 0.75 = 0.30, a 25% reduction.
  - 0.40 × 0.85 = 0.34, a 15% reduction.
  - Applying a further 0.8 funding factor gives 0.24–0.27, which is near the 0.26 threshold.
  - The threshold itself is a CG figure I could not check.
- **WHO recommendations go through a guideline development group and evidence review: VERIFIED in outline.**
  - For Study 31, 
a WHO-convened GDG considered the 4-month regimen.

  - 
The other 4-month arm did not meet non-inferiority and was not reviewed by the GDG.

  - That document is a June 2021 WHO rapid communication, so adoption can be quick for a clean positive Phase III. The 2021 rapid communication followed Study 31's results within a short window. I did not verify the exact timing.
  - I did not find the GRADE rating wording on that page.
- **A conditional recommendation or none for low-certainty mortality evidence: PLAUSIBLE, UNVERIFIED.** It matches how GRADE works, but I found no TB-specific example.
- **Generics lack a commercial sponsor, so funding risk is higher: PLAUSIBLE.** Repurposed-drug HDT trials in the results were philanthropy- or public-funded. For example, 
the HDT Phase 2 trial was supported by the Gates Foundation and the South African MRC.
 This is consistent with the critique but does not quantify P(funded).
- **"Many Phase II→III failures are strategic or funding exits": PLAUSIBLE.** This matches general industry analyses, but I did not verify it here.
- **60% uptake covers country-level implementation only: UNVERIFIABLE.** The critique itself concedes it collapses to a documentation issue if the 60% already embeds adoption.

**EVIDENCE FOUND**
- No source gives P(adoption | positive Phase III) for TB adjuncts. The Study 31 and WHO pathway shows a clean non-inferiority trial being adopted within months, which argues against a heavy discount in the best case. An adjunct with only low-certainty mortality evidence (Critique 1) is the harder case, and this links the two critiques.
- The cost-versus-funding gap is also linked to Critique 1. A mortality-powered Phase III is much more expensive than a standard TB composite-endpoint trial, so P(funded) is not independent of the endpoint.

**REVISED CRITIQUE (strength: MEDIUM, conditional)**
The CG chain should show explicit factors for P(Phase III funded | IIc success) and P(WHO or national adoption | Phase III success), or state that the 60% uptake already includes them. The critique's directional claim (decreases) follows if either factor is below 1. **UNGROUNDED:** the values 0.75–0.85 and 0.8. Treat the 15–25% reduction as an illustrative sensitivity range, not an estimate. The "near the 0.26 threshold" claim holds only if CG's break-even really is 0.26 and the 60% excludes adoption.

---

## Critique 3: Phase IIc as a weak gate

**OVERALL VERDICT: PARTIALLY VERIFIED.** The REMoxTB precedent and the statistical point are valid. The premise that the IIc is a PK or dose-finding trial is unverified, and TB usage of "Phase IIc" may contradict it. The direction claim is internally inconsistent. The "winner's curse" argument is partly misapplied. The cross-reference to Critique 2 is wrong.

**CLAIM CHECK**
- **REMoxTB: early culture-conversion signals did not translate to Phase III: VERIFIED.**
  - 
Earlier time to culture conversion failed to predict successful 4-month fluoroquinolone regimens and had limited use as a surrogate in REMoxTB.

  - A REMoxTB reanalysis found 
faster culture conversion with the moxifloxacin regimens, even though the smear-conversion analysis showed no treatment difference.

  - 
Culture conversion has only a limited role in deciding which regimens advance to Phase III.

- **"See Critique 2": WRONG REFERENCE.** REMoxTB is not discussed in Critique 2, only in Critique 1's suggested evidence.
- **Phase IIc is mainly dose-finding or PK/safety, as the "exclusion list implies": UNVERIFIABLE, and RISKY.**
  - In the TB field, Phase IIb trials usually use culture-conversion endpoints: 
Phase IIb trials continue to use culture-conversion primary endpoints as the best available marker.

  - From general knowledge, "Phase IIc" in TB usually means a larger or longer proof-of-efficacy trial with clinical-outcome endpoints. I did not confirm this by search.
  - If so, the critique's premise that P(IIc) is 0.6–0.8 and uninformative may be wrong. The protocol or grant rationale needs checking, which the Investigator also recommended.
- **Industry Phase II success of about 29%: PLAUSIBLE, NOT VERIFIED HERE.** The figure matches my recollection of Phase II→III transition rates in industry benchmarking. It is a transition rate, not Phase II→approval, so the critique's phrase "Phase II→approval statistics" mixes two measures. Industry likelihood of approval from Phase II is much lower than 40%, which would support the broader point that CG's 40% for both stages is high (not verified).
- **0.7 × 0.3 = 0.21: arithmetic correct.** The 0.3 for P(III | weak signal) is an assumption with no support. Nothing in the critique shows that 0.3 is a better estimate than 0.57, the value implied by 0.40 ÷ 0.7.
- **E[p·RR] ≠ p·E[RR] when both depend on the true effect: VALID.** This is basic probability: the two differ by the covariance.
- **Winner's curse (realized effect below the planning value): PARTLY MISAPPLIED.** Winner's curse biases the estimated effect in a successful trial. Deaths averted depend on the true effect. Conditional on success, the true effect is selected upward, which is the opposite direction, as the critique acknowledges. The net direction is therefore ambiguous. This conflicts with the critique's header "Estimated Direction: decreases", and with its own "direction is ambiguous".
- **"Same linear effect on p_success as Critique 1": MINOR ERROR.** Critique 1 is about the RR term, not p_success.

**EVIDENCE FOUND**
- Phase 2 HDT trials in TB often define success by safety and surrogates. The four-HDT Phase 2 trial in South Africa (
200 patients
) assessed 
safety and preliminary efficacy.
 Its efficacy signal was FEV₁ recovery, 
a predictor of long-term all-cause mortality.
 This supports the "weak gate" idea for HDT-type adjuncts in general. It does not show how this specific IIc defines success.
- 
More data are needed before any endpoint can be used as a surrogate in a confirmatory Phase III trial.
 That fits the concern that Phase II signals transmit little information.

**REVISED CRITIQUE (strength: LOW–MEDIUM, direction: ambiguous, conditional on IIc definition)**
If the IIc endpoint is PK, dose or surrogate-based (a condition not yet verified), then P(IIc success) is likely high. Phase III then carries most of the risk, and the realistic joint probability could fall below 0.40. REMoxTB is a verified precedent for Phase II signals not translating. Because p_success and the true effect size are correlated, E[p·RR] ≠ p·E[RR]. Whether this raises or lowers the expected benefit needs a scenario analysis over a prior on the true effect. The winner's-curse point should be dropped or reframed as an effect-size selection argument. **UNGROUNDED:** P(IIc) = 0.7, P(III | weak signal) = 0.3, the 0.21 product, and the premise that IIc is dose-finding. **Correct** the "see Critique 2" reference to Critique 1 and fix the "Phase II→approval" wording.

--- Critique: Phase IIc "success" is a weak gate. If it is defined by PK or dose selection, it passes easily and transmits little information, so the probability of the whole chain should be weighted toward Phase III ---

**Scope note:** No source materials were attached, and I found nothing public on the CG model. I could not check any CG parameter: p_success = 0.40, the 10% relative mortality reduction, 60% uptake, the $7M cost, the 8-year timeline, the 0.26 break-even threshold, or how the Phase IIc defines success. Every claim about the CG model is therefore unverified. I checked the external trial facts and the arithmetic.

---

## Critique 1: Surrogate or composite "success" versus the 10% mortality-reduction assumption

**OVERALL VERDICT: PARTIALLY VERIFIED.** The arithmetic and the endpoint claims check out. The 4% baseline mortality is probably too high for DS-TB trials, which makes the argument stronger. The 5–7% "realized RR" and the "large" magnitude are ungrounded.

**CLAIM CHECK**
- **Sample-size arithmetic (4% → 3.6%, about 36,000 per arm): VERIFIED.** I recomputed it. The sum p₁q₁ + p₂q₂ is 0.0731 and d² is 1.6×10⁻⁵. That gives about 35,800 per arm.
- **"Even at 6% it is tens of thousands per arm": VERIFIED.** At 6% → 5.4% I get about 23,400 per arm.
- **Standard TB Phase III trials enroll hundreds to a few thousand: VERIFIED.**
  - 
Study 31 had 2,234 participants assessable for its primary outcome.

  - TRUNCATE-TB's two arms shown in the NEJM table had 
181 and 184 participants.

  - I did not find the TRUNCATE-TB total enrollment.
- **Primary endpoints are composites or surrogates: VERIFIED, with a nuance.**
  - 
Study 31's primary efficacy outcome was survival free of tuberculosis at 12 months.

  - 
REMoxTB's primary outcome was a composite of bacteriological or clinical failure or relapse within 18 months.

  - 
TRUNCATE-TB's primary outcome was a composite of death, ongoing treatment, or active disease at week 96.

  - 
Regulatory guidance and recent Phase III trials use a composite of mainly bacteriological failure and relapse.

  - Death is a component of some of these composites, so they are not purely bacteriological surrogates. None of them tests all-cause mortality alone.
- **Baseline mortality of about 4% in DS-TB trial populations: LIKELY OVERSTATED.**
  - In Study 31, 
mortality was 0.6% in the overall study population.

  - 
Among people with HIV on treatment it was 1.5%.

  - WHO's review reports 
0.4% all-cause mortality within 14 days of the end of treatment.

  - At around 1% baseline, a 10% relative reduction would need several hundred thousand participants. Programmatic mortality of 4–6% (Critique 1's range) is plausible from general knowledge, but I did not verify it here.
- **Surrogate-to-mortality relationship for TB adjuncts is ungrounded: AGREED.** I found no validated link.
- **Success may be declared on a non-mortality endpoint (supported for adjuncts):**
  - A recent review says 
host-directed therapy trial designs have focused on safety, biological activity and intermediate outcomes, rather than being powered for mortality.

  - It also says 
no adjunctive host-directed therapy has shown sufficient, reproducible efficacy for routine use.

- **"If E[RR | surrogate success] is 5–7%, benefit falls 30–50%": arithmetic correct, premise UNGROUNDED.** 5–7% versus 10% is a 30–50% shortfall. The 5–7% figure is an assumption.

**EVIDENCE FOUND**
- **Higher-mortality populations are less extreme but still large.**
  - TB Fast Track's primary outcome was all-cause mortality in advanced HIV: 
19.0 versus 21.6 deaths per 100 person-years, HR 0.92, not significant.

  - At 20% baseline, a 10% relative reduction needs about 6,000 per arm by the Critique's formula (my calculation). That is still large.
- **TB meningitis is the best-grounded case for a mortality endpoint.** 
Dexamethasone is the only evidence-based adjunctive therapy there and gives a modest reduction in short-term mortality.
 If the CG drug targets TBM or advanced HIV, the critique's baseline changes materially. I could not tell which population CG uses.
- **Sample-size concerns also apply at Phase II.** In the four-drug HDT Phase 2 trial, 
the main shortcomings were a small sample size and low statistical power.
 
Its efficacy signal was FEV₁, a predictor of long-term all-cause mortality.
 That is a surrogate-based "success" in this class.
- **Cost implication:** a mortality-powered Phase III of 12,000 to 70,000 participants would likely cost far more than a $7M budget covering later trials. This is my inference, not verified.

**REVISED CRITIQUE (strength: MEDIUM–LARGE, direction: decreases)**
A Phase III TB trial powered for a 10% relative mortality reduction would need on the order of 10⁴–10⁵ participants. This holds for baseline mortality from about 1% to about 20%, and the required size is larger at low baseline mortality (my calculations). Published Phase III TB trials (Study 31, REMoxTB, TRUNCATE-TB) used composite clinical endpoints and enrolled hundreds to low thousands. Trial "success" is therefore unlikely to demonstrate a 10% mortality benefit directly. The model should either (a) state how the 10% was derived, or (b) run a sensitivity analysis with E[RR | trial success] below 10%. **UNGROUNDED:** the 5–7% figure and the 30–50% loss. The "4%" baseline should be replaced with a population-specific figure. Trial-population mortality in DS-TB is closer to 0.4–1.5%.

---

## Critique 2: Missing P(adoption | Phase III success) and P(Phase III funded | IIc success)

**OVERALL VERDICT: PARTIALLY VERIFIED.** The logic and arithmetic hold. The key dependency, how the 60% uptake was derived, is unverifiable here. The quantitative inputs (0.75–0.85, 0.8) are admitted guesses.

**CLAIM CHECK**
- **Arithmetic: VERIFIED.**
  - 0.40 × 0.75 = 0.30, a 25% reduction.
  - 0.40 × 0.85 = 0.34, a 15% reduction.
  - Applying a further 0.8 funding factor gives 0.24–0.27, which is near the 0.26 threshold.
  - The threshold itself is a CG figure I could not check.
- **WHO recommendations go through a guideline development group and evidence review: VERIFIED in outline.**
  - For Study 31, 
a WHO-convened GDG considered the 4-month regimen.

  - 
The other 4-month arm did not meet non-inferiority and was not reviewed by the GDG.

  - That document is a June 2021 WHO rapid communication, so adoption can be quick for a clean positive Phase III. The 2021 rapid communication followed Study 31's results within a short window. I did not verify the exact timing.
  - I did not find the GRADE rating wording on that page.
- **A conditional recommendation or none for low-certainty mortality evidence: PLAUSIBLE, UNVERIFIED.** It matches how GRADE works, but I found no TB-specific example.
- **Generics lack a commercial sponsor, so funding risk is higher: PLAUSIBLE.** Repurposed-drug HDT trials in the results were philanthropy- or public-funded. For example, 
the HDT Phase 2 trial was supported by the Gates Foundation and the South African MRC.
 This is consistent with the critique but does not quantify P(funded).
- **"Many Phase II→III failures are strategic or funding exits": PLAUSIBLE.** This matches general industry analyses, but I did not verify it here.
- **60% uptake covers country-level implementation only: UNVERIFIABLE.** The critique itself concedes it collapses to a documentation issue if the 60% already embeds adoption.

**EVIDENCE FOUND**
- No source gives P(adoption | positive Phase III) for TB adjuncts. The Study 31 and WHO pathway shows a clean non-inferiority trial being adopted within months, which argues against a heavy discount in the best case. An adjunct with only low-certainty mortality evidence (Critique 1) is the harder case, and this links the two critiques.
- The cost-versus-funding gap is also linked to Critique 1. A mortality-powered Phase III is much more expensive than a standard TB composite-endpoint trial, so P(funded) is not independent of the endpoint.

**REVISED CRITIQUE (strength: MEDIUM, conditional)**
The CG chain should show explicit factors for P(Phase III funded | IIc success) and P(WHO or national adoption | Phase III success), or state that the 60% uptake already includes them. The critique's directional claim (decreases) follows if either factor is below 1. **UNGROUNDED:** the values 0.75–0.85 and 0.8. Treat the 15–25% reduction as an illustrative sensitivity range, not an estimate. The "near the 0.26 threshold" claim holds only if CG's break-even really is 0.26 and the 60% excludes adoption.

---

## Critique 3: Phase IIc as a weak gate

**OVERALL VERDICT: PARTIALLY VERIFIED.** The REMoxTB precedent and the statistical point are valid. The premise that the IIc is a PK or dose-finding trial is unverified, and TB usage of "Phase IIc" may contradict it. The direction claim is internally inconsistent. The "winner's curse" argument is partly misapplied. The cross-reference to Critique 2 is wrong.

**CLAIM CHECK**
- **REMoxTB: early culture-conversion signals did not translate to Phase III: VERIFIED.**
  - 
Earlier time to culture conversion failed to predict successful 4-month fluoroquinolone regimens and had limited use as a surrogate in REMoxTB.

  - A REMoxTB reanalysis found 
faster culture conversion with the moxifloxacin regimens, even though the smear-conversion analysis showed no treatment difference.

  - 
Culture conversion has only a limited role in deciding which regimens advance to Phase III.

- **"See Critique 2": WRONG REFERENCE.** REMoxTB is not discussed in Critique 2, only in Critique 1's suggested evidence.
- **Phase IIc is mainly dose-finding or PK/safety, as the "exclusion list implies": UNVERIFIABLE, and RISKY.**
  - In the TB field, Phase IIb trials usually use culture-conversion endpoints: 
Phase IIb trials continue to use culture-conversion primary endpoints as the best available marker.

  - From general knowledge, "Phase IIc" in TB usually means a larger or longer proof-of-efficacy trial with clinical-outcome endpoints. I did not confirm this by search.
  - If so, the critique's premise that P(IIc) is 0.6–0.8 and uninformative may be wrong. The protocol or grant rationale needs checking, which the Investigator also recommended.
- **Industry Phase II success of about 29%: PLAUSIBLE, NOT VERIFIED HERE.** The figure matches my recollection of Phase II→III transition rates in industry benchmarking. It is a transition rate, not Phase II→approval, so the critique's phrase "Phase II→approval statistics" mixes two measures. Industry likelihood of approval from Phase II is much lower than 40%, which would support the broader point that CG's 40% for both stages is high (not verified).
- **0.7 × 0.3 = 0.21: arithmetic correct.** The 0.3 for P(III | weak signal) is an assumption with no support. Nothing in the critique shows that 0.3 is a better estimate than 0.57, the value implied by 0.40 ÷ 0.7.
- **E[p·RR] ≠ p·E[RR] when both depend on the true effect: VALID.** This is basic probability: the two differ by the covariance.
- **Winner's curse (realized effect below the planning value): PARTLY MISAPPLIED.** Winner's curse biases the estimated effect in a successful trial. Deaths averted depend on the true effect. Conditional on success, the true effect is selected upward, which is the opposite direction, as the critique acknowledges. The net direction is therefore ambiguous. This conflicts with the critique's header "Estimated Direction: decreases", and with its own "direction is ambiguous".
- **"Same linear effect on p_success as Critique 1": MINOR ERROR.** Critique 1 is about the RR term, not p_success.

**EVIDENCE FOUND**
- Phase 2 HDT trials in TB often define success by safety and surrogates. The four-HDT Phase 2 trial in South Africa (
200 patients
) assessed 
safety and preliminary efficacy.
 Its efficacy signal was FEV₁ recovery, 
a predictor of long-term all-cause mortality.
 This supports the "weak gate" idea for HDT-type adjuncts in general. It does not show how this specific IIc defines success.
- 
More data are needed before any endpoint can be used as a surrogate in a confirmatory Phase III trial.
 That fits the concern that Phase II signals transmit little information.

**REVISED CRITIQUE (strength: LOW–MEDIUM, direction: ambiguous, conditional on IIc definition)**
If the IIc endpoint is PK, dose or surrogate-based (a condition not yet verified), then P(IIc success) is likely high. Phase III then carries most of the risk, and the realistic joint probability could fall below 0.40. REMoxTB is a verified precedent for Phase II signals not translating. Because p_success and the true effect size are correlated, E[p·RR] ≠ p·E[RR]. Whether this raises or lowers the expected benefit needs a scenario analysis over a prior on the true effect. The winner's-curse point should be dropped or reframed as an effect-size selection argument. **UNGROUNDED:** P(IIc) = 0.7, P(III | weak signal) = 0.3, the 0.21 product, and the premise that IIc is dose-finding. **Correct** the "see Critique 2" reference to Critique 1 and fix the "Phase II→approval" wording.

--- Critique: Baseline year is stale and the 5.5M figure is sensitive to it ---

## Critique 1: Baseline year is stale and the 5.5M figure is sensitive to it

**OVERALL VERDICT: VERIFIED.** I could not check what baseline CG actually used, because I don't have CG's source. The WHO numbers and the arithmetic hold up. One nuance sharpens the critique: notifications stopped rising in 2024.

**CLAIM CHECK**
- **2022 notifications of ~7.5M:** VERIFIED. 
WHO reported about 8.2 million newly diagnosed in 2023, up from 7.5 million in 2022.

- **~8.2M in 2023:** VERIFIED. 
8.2 million was the highest single-year number since the mid-1990s, up from the previous record of 7.5M in 2022.

- **"Notifications continuing to rise":** PARTIALLY VERIFIED. They rose through 2023, then levelled off. 
In 2024, 8.3 million were newly diagnosed and notified, similar to 8.2 million in 2023 and 17% above the pre-pandemic level of 7.1 million.
 The better statement is that 2024 is a plateau at about 8.3M, which is 10.7% above 7.5M.
- **"2022 was a post-COVID recovery year":** VERIFIED. WHO says 
those diagnosed in 2022 and 2023 probably included a sizeable backlog of people whose diagnosis was delayed by COVID-related disruptions.
 This applies to 2023 as well. Part of the 8.2M may be one-off backlog, so it is not a clean steady-state anchor either.
- **Arithmetic:** VERIFIED. 8.2/7.5 = +9.3% and 8.3/7.5 = +10.7%. Applied to 5.5M, that gives ~6.0–6.1M. The result is below the ±25% materiality bar.

**EVIDENCE FOUND**
- The 2024 data point (8.3M, from the WHO Global TB Report 2025) post-dates the Investigator's recollection. It supports "upward, small."
- The backlog caveat means the upward correction may be slightly overstated if the baseline is treated as a steady-state level.

**REVISED CRITIQUE:** Same as stated, with these edits.
- Replace "continuing to rise" with "rose to 8.2M in 2023 and plateaued at 8.3M in 2024."
- Add the backlog caveat.
- Strength remains small, direction up (+9–11%).

---

## Critique 2: A 2%/yr decline in notified counts contradicts the observed trend

**OVERALL VERDICT: PARTIALLY VERIFIED.** The core hypothesis is well supported by WHO data. Three things don't survive as stated.
- The claim about CG's method is unverifiable.
- The "+29%" figure double-counts Critique 1.
- The 2025 funding-shock point is ungrounded.

**CLAIM CHECK**
- **Rates fall about 1–2%/yr:** VERIFIED. WHO describes 
declines of about 2% per year between 2010 and 2020, reversed by a 4.6% rise from 2020 to 2023.
 
The net reduction in the rate from 2015 to 2024 was 12.3%
, which is about 1.4%/yr.
- **Rate down ~8% over 2015–2023:** VERIFIED. 
The net reduction was 8.3%.

- **Counts are roughly flat while rates fall:** VERIFIED for the recent period, but "since 2015" is unconfirmed. 
Incident cases fell 1% in 2024, from 10.8M to 10.7M, but remain above the 2020 level of 10.3M.
 I did not retrieve a 2015 absolute figure.
- **Population growth drives counts:** VERIFIED in direction. WHO states 
most of the global increase in incident cases between 2022 and 2023 reflects population growth.

- **~25% of incident cases are not notified:** VERIFIED, and now somewhat better. 
In 2024 about 2.4 million people were not diagnosed or not reported, and notifications were 78% of incidence.
 In 2023 the gap was 
about 2.7 million, down from around 4 million in 2020 and 2021.
 This supports "detection gaps are closing."
- **Notified counts are flat to rising, not falling 2%/yr:** VERIFIED. Notifications went from 7.1M in 2019 to 8.3M in 2024. 
In the African Region they were 38% above 2019.

- **"CG applies a 2%/yr decline to counts":** UNVERIFIABLE. I have no CG source. This is the pivotal premise, so it should stay flagged.
- **Scenario arithmetic:** the arithmetic is correct.
  - 8.2 × 0.96 × 0.90 = 7.09M, which is +29% versus 5.5M.
  - With +1%/yr growth, 8.2 × 1.01⁸ × 0.864 = 7.67M.
  - The 6.5M lower bound corresponds to about −1%/yr.
- **Double-counting problem:** the +29% already includes Critique 1.
  - Flat counts remove 8 years of 2%/yr decline (0.98⁸ ≈ 0.85), which is worth +17.5% on its own.
  - The baseline update adds about +9% (1.093 × 1.175 ≈ 1.28).
  - Critique 2 alone is therefore about +17.5% for flat counts, or about +27% with +1%/yr growth.
  - Crossing the 25% bar needs Critique 1 or a rise in counts. The Investigator's wording ("combined with Critique 1") is right, but the +29% should not be presented as Critique 2's standalone effect.
- **2025 funding disruptions could cut notifications:** UNVERIFIABLE. My searches returned no data on the size of this effect, and the 2024 data pre-date it. It stays flagged as ungrounded.
- **Direction field "uncertain":** the text argues the error is probably upward, so the label is internally inconsistent. The evidence supports "likely increases," with downside risk from funding and from the backlog fading.

**EVIDENCE FOUND**
- WHO notes that 
the recovery in reported newly diagnosed cases in 2022–2024 first slowed increases in incidence, then reversed the upward trend.
 Notifications and incidence estimates are therefore linked, which weakens any "independent" notification trend.
- Counter-consideration: WHO's 2.4M gap bounds how much notifications can rise from detection alone. The ceiling is about +28% above 8.3M, and only in the unrealistic case of 100% detection.

**REVISED CRITIQUE:** Rate declines in WHO reporting are not the same as declines in case counts. Observed notifications rose from 7.5M (2022) to 8.3M (2024), and incident counts have been about flat (10.3–10.8M since 2020). If CG applies 2%/yr to counts, it likely understates the eligible population by roughly 17% (flat counts) to 27% (+1%/yr), before the baseline correction in Critique 1.
- Combined with Critique 1, eligible is about 6.5–7.7M.
- The CG-method premise and the funding-shock point stay flagged as UNGROUNDED.
- Strength: medium. Direction: up, with downside risk.

---

## Critique 3: "Adult DS notified" is not "eligible for the trial label"

**OVERALL VERDICT: PARTIALLY VERIFIED.** The WHO shares are broadly right, and the direction (filters reduce eligibility) is sound. One denominator is mis-stated, one share is slightly high, and the exclusion list is the Investigator's own inference.

**CLAIM CHECK**
- **Extrapulmonary TB ~15%:** VERIFIED. 
In 2024, 84% of notified cases were pulmonary and 16% extrapulmonary
, and the 2023 figures were the same (
84% and 16%
). Regional variation is large. 
South-East Asia is 25% extrapulmonary
, and 
India and Bangladesh are above 20%.
 The ×0.85 filter is therefore too lenient for India and South Asia, the biggest contributors.
- **Clinically diagnosed "~35–40% of notifications":** MISSTATED. 
Of 6.9 million pulmonary cases in 2024, 64% were bacteriologically confirmed, up from 62% in 2023.
 The 62–64% is a share of pulmonary cases, not of all notifications, so 36–38% of pulmonary cases are clinically diagnosed.
  - The stacked arithmetic does apply ×0.62 after the pulmonary filter, so it is consistent.
  - Of all notifications, confirmed pulmonary cases are only about 0.84 × 0.64 ≈ 54%.
- **HIV coinfection ~6–8%:** SLIGHTLY HIGH. 
5.8% of incident cases in 2024 were among people living with HIV
, and 
6.1% in 2023.
 Notified HIV-positive cases were 
413,516 in 2024
, about 5% of 8.3M. A range of 5–7% is better. The share is concentrated in Africa, with 
over 50% in parts of southern Africa.

- **Hr-TB ~7%:** VERIFIED. 
Hr-TB prevalence was estimated at 7.4% among new cases and 11.4% among previously treated cases.
 Another source gives 
7.1% of new cases.
 It is 
treated with a modified regimen including levofloxacin since 2018.
 I did not verify how routinely Hr-TB is detected. Isoniazid DST is not routine, so many Hr-TB patients are probably in "DS" cohorts in practice. That blunts the filter's real-world effect but not a trial-eligibility one.
- **Pregnancy, hepatic disease, existing statin use, drug interactions:** UNVERIFIABLE. These are inference from standard trial design, as the Investigator says. The ×0.85 for "other filters" is also ungrounded. HIV plus Hr-TB alone gives about 0.87, so 0.85 is plausible but unsupported.
- **Stack arithmetic:** correct.
  - 5.5 × 0.85 = 4.7M, then × 0.85 = 4.0M, then × 0.62 = 2.5M.
  - Restricting to bacteriologically confirmed cases is a trial-design choice. A label population may not carry it.

**EVIDENCE FOUND**
- Applying Critique 2's upside to these filters:
  - 7.1M (flat, adjusted) × 0.85 × 0.85 = 5.1M. That is about −7% versus 5.5M, so it roughly nets out to the current figure, as the Investigator suggests.
  - Adding the confirmed-only restriction gives about 3.2M, below the 3.6M bar.
- The conclusion therefore hinges on whether the label or trial requires bacteriological confirmation. That is the single most decision-relevant unknown.
- Applying the filters to the regional mix makes this worse. India and South Asia have the highest extrapulmonary share, and Africa has the highest HIV share.

**REVISED CRITIQUE:** Notified adult cases overstate the population that fits a pulmonary, trial-like label. Verified WHO figures:
- Extrapulmonary share is 16% globally and ~25% in South-East Asia.
- Pulmonary cases are 64% bacteriologically confirmed (the denominator is pulmonary, not all notifications).
- HIV is about 5–6%.
- Hr-TB is about 7%.

An illustrative stack gives 4.0M without confirmation and ~2.5M with it, before the upside from Critique 2. The statin-specific exclusions and the ×0.85 factor are the Investigator's own assumptions and are flagged as UNGROUNDED. Strength: medium. Standalone direction: down. Net direction when combined with Critique 2: uncertain.

--- Critique: A 2%/yr decline in notified case counts probably contradicts the observed trend; incidence rates fall slowly while counts do not ---

## Critique 1: Baseline year is stale and the 5.5M figure is sensitive to it

**OVERALL VERDICT: VERIFIED.** I could not check what baseline CG actually used, because I don't have CG's source. The WHO numbers and the arithmetic hold up. One nuance sharpens the critique: notifications stopped rising in 2024.

**CLAIM CHECK**
- **2022 notifications of ~7.5M:** VERIFIED. 
WHO reported about 8.2 million newly diagnosed in 2023, up from 7.5 million in 2022.

- **~8.2M in 2023:** VERIFIED. 
8.2 million was the highest single-year number since the mid-1990s, up from the previous record of 7.5M in 2022.

- **"Notifications continuing to rise":** PARTIALLY VERIFIED. They rose through 2023, then levelled off. 
In 2024, 8.3 million were newly diagnosed and notified, similar to 8.2 million in 2023 and 17% above the pre-pandemic level of 7.1 million.
 The better statement is that 2024 is a plateau at about 8.3M, which is 10.7% above 7.5M.
- **"2022 was a post-COVID recovery year":** VERIFIED. WHO says 
those diagnosed in 2022 and 2023 probably included a sizeable backlog of people whose diagnosis was delayed by COVID-related disruptions.
 This applies to 2023 as well. Part of the 8.2M may be one-off backlog, so it is not a clean steady-state anchor either.
- **Arithmetic:** VERIFIED. 8.2/7.5 = +9.3% and 8.3/7.5 = +10.7%. Applied to 5.5M, that gives ~6.0–6.1M. The result is below the ±25% materiality bar.

**EVIDENCE FOUND**
- The 2024 data point (8.3M, from the WHO Global TB Report 2025) post-dates the Investigator's recollection. It supports "upward, small."
- The backlog caveat means the upward correction may be slightly overstated if the baseline is treated as a steady-state level.

**REVISED CRITIQUE:** Same as stated, with these edits.
- Replace "continuing to rise" with "rose to 8.2M in 2023 and plateaued at 8.3M in 2024."
- Add the backlog caveat.
- Strength remains small, direction up (+9–11%).

---

## Critique 2: A 2%/yr decline in notified counts contradicts the observed trend

**OVERALL VERDICT: PARTIALLY VERIFIED.** The core hypothesis is well supported by WHO data. Three things don't survive as stated.
- The claim about CG's method is unverifiable.
- The "+29%" figure double-counts Critique 1.
- The 2025 funding-shock point is ungrounded.

**CLAIM CHECK**
- **Rates fall about 1–2%/yr:** VERIFIED. WHO describes 
declines of about 2% per year between 2010 and 2020, reversed by a 4.6% rise from 2020 to 2023.
 
The net reduction in the rate from 2015 to 2024 was 12.3%
, which is about 1.4%/yr.
- **Rate down ~8% over 2015–2023:** VERIFIED. 
The net reduction was 8.3%.

- **Counts are roughly flat while rates fall:** VERIFIED for the recent period, but "since 2015" is unconfirmed. 
Incident cases fell 1% in 2024, from 10.8M to 10.7M, but remain above the 2020 level of 10.3M.
 I did not retrieve a 2015 absolute figure.
- **Population growth drives counts:** VERIFIED in direction. WHO states 
most of the global increase in incident cases between 2022 and 2023 reflects population growth.

- **~25% of incident cases are not notified:** VERIFIED, and now somewhat better. 
In 2024 about 2.4 million people were not diagnosed or not reported, and notifications were 78% of incidence.
 In 2023 the gap was 
about 2.7 million, down from around 4 million in 2020 and 2021.
 This supports "detection gaps are closing."
- **Notified counts are flat to rising, not falling 2%/yr:** VERIFIED. Notifications went from 7.1M in 2019 to 8.3M in 2024. 
In the African Region they were 38% above 2019.

- **"CG applies a 2%/yr decline to counts":** UNVERIFIABLE. I have no CG source. This is the pivotal premise, so it should stay flagged.
- **Scenario arithmetic:** the arithmetic is correct.
  - 8.2 × 0.96 × 0.90 = 7.09M, which is +29% versus 5.5M.
  - With +1%/yr growth, 8.2 × 1.01⁸ × 0.864 = 7.67M.
  - The 6.5M lower bound corresponds to about −1%/yr.
- **Double-counting problem:** the +29% already includes Critique 1.
  - Flat counts remove 8 years of 2%/yr decline (0.98⁸ ≈ 0.85), which is worth +17.5% on its own.
  - The baseline update adds about +9% (1.093 × 1.175 ≈ 1.28).
  - Critique 2 alone is therefore about +17.5% for flat counts, or about +27% with +1%/yr growth.
  - Crossing the 25% bar needs Critique 1 or a rise in counts. The Investigator's wording ("combined with Critique 1") is right, but the +29% should not be presented as Critique 2's standalone effect.
- **2025 funding disruptions could cut notifications:** UNVERIFIABLE. My searches returned no data on the size of this effect, and the 2024 data pre-date it. It stays flagged as ungrounded.
- **Direction field "uncertain":** the text argues the error is probably upward, so the label is internally inconsistent. The evidence supports "likely increases," with downside risk from funding and from the backlog fading.

**EVIDENCE FOUND**
- WHO notes that 
the recovery in reported newly diagnosed cases in 2022–2024 first slowed increases in incidence, then reversed the upward trend.
 Notifications and incidence estimates are therefore linked, which weakens any "independent" notification trend.
- Counter-consideration: WHO's 2.4M gap bounds how much notifications can rise from detection alone. The ceiling is about +28% above 8.3M, and only in the unrealistic case of 100% detection.

**REVISED CRITIQUE:** Rate declines in WHO reporting are not the same as declines in case counts. Observed notifications rose from 7.5M (2022) to 8.3M (2024), and incident counts have been about flat (10.3–10.8M since 2020). If CG applies 2%/yr to counts, it likely understates the eligible population by roughly 17% (flat counts) to 27% (+1%/yr), before the baseline correction in Critique 1.
- Combined with Critique 1, eligible is about 6.5–7.7M.
- The CG-method premise and the funding-shock point stay flagged as UNGROUNDED.
- Strength: medium. Direction: up, with downside risk.

---

## Critique 3: "Adult DS notified" is not "eligible for the trial label"

**OVERALL VERDICT: PARTIALLY VERIFIED.** The WHO shares are broadly right, and the direction (filters reduce eligibility) is sound. One denominator is mis-stated, one share is slightly high, and the exclusion list is the Investigator's own inference.

**CLAIM CHECK**
- **Extrapulmonary TB ~15%:** VERIFIED. 
In 2024, 84% of notified cases were pulmonary and 16% extrapulmonary
, and the 2023 figures were the same (
84% and 16%
). Regional variation is large. 
South-East Asia is 25% extrapulmonary
, and 
India and Bangladesh are above 20%.
 The ×0.85 filter is therefore too lenient for India and South Asia, the biggest contributors.
- **Clinically diagnosed "~35–40% of notifications":** MISSTATED. 
Of 6.9 million pulmonary cases in 2024, 64% were bacteriologically confirmed, up from 62% in 2023.
 The 62–64% is a share of pulmonary cases, not of all notifications, so 36–38% of pulmonary cases are clinically diagnosed.
  - The stacked arithmetic does apply ×0.62 after the pulmonary filter, so it is consistent.
  - Of all notifications, confirmed pulmonary cases are only about 0.84 × 0.64 ≈ 54%.
- **HIV coinfection ~6–8%:** SLIGHTLY HIGH. 
5.8% of incident cases in 2024 were among people living with HIV
, and 
6.1% in 2023.
 Notified HIV-positive cases were 
413,516 in 2024
, about 5% of 8.3M. A range of 5–7% is better. The share is concentrated in Africa, with 
over 50% in parts of southern Africa.

- **Hr-TB ~7%:** VERIFIED. 
Hr-TB prevalence was estimated at 7.4% among new cases and 11.4% among previously treated cases.
 Another source gives 
7.1% of new cases.
 It is 
treated with a modified regimen including levofloxacin since 2018.
 I did not verify how routinely Hr-TB is detected. Isoniazid DST is not routine, so many Hr-TB patients are probably in "DS" cohorts in practice. That blunts the filter's real-world effect but not a trial-eligibility one.
- **Pregnancy, hepatic disease, existing statin use, drug interactions:** UNVERIFIABLE. These are inference from standard trial design, as the Investigator says. The ×0.85 for "other filters" is also ungrounded. HIV plus Hr-TB alone gives about 0.87, so 0.85 is plausible but unsupported.
- **Stack arithmetic:** correct.
  - 5.5 × 0.85 = 4.7M, then × 0.85 = 4.0M, then × 0.62 = 2.5M.
  - Restricting to bacteriologically confirmed cases is a trial-design choice. A label population may not carry it.

**EVIDENCE FOUND**
- Applying Critique 2's upside to these filters:
  - 7.1M (flat, adjusted) × 0.85 × 0.85 = 5.1M. That is about −7% versus 5.5M, so it roughly nets out to the current figure, as the Investigator suggests.
  - Adding the confirmed-only restriction gives about 3.2M, below the 3.6M bar.
- The conclusion therefore hinges on whether the label or trial requires bacteriological confirmation. That is the single most decision-relevant unknown.
- Applying the filters to the regional mix makes this worse. India and South Asia have the highest extrapulmonary share, and Africa has the highest HIV share.

**REVISED CRITIQUE:** Notified adult cases overstate the population that fits a pulmonary, trial-like label. Verified WHO figures:
- Extrapulmonary share is 16% globally and ~25% in South-East Asia.
- Pulmonary cases are 64% bacteriologically confirmed (the denominator is pulmonary, not all notifications).
- HIV is about 5–6%.
- Hr-TB is about 7%.

An illustrative stack gives 4.0M without confirmation and ~2.5M with it, before the upside from Critique 2. The statin-specific exclusions and the ×0.85 factor are the Investigator's own assumptions and are flagged as UNGROUNDED. Strength: medium. Standalone direction: down. Net direction when combined with Critique 2: uncertain.

--- Critique: "Adult DS notified" is not "eligible for the trial label": missing applicability filters ---

## Critique 1: Baseline year is stale and the 5.5M figure is sensitive to it

**OVERALL VERDICT: VERIFIED.** I could not check what baseline CG actually used, because I don't have CG's source. The WHO numbers and the arithmetic hold up. One nuance sharpens the critique: notifications stopped rising in 2024.

**CLAIM CHECK**
- **2022 notifications of ~7.5M:** VERIFIED. 
WHO reported about 8.2 million newly diagnosed in 2023, up from 7.5 million in 2022.

- **~8.2M in 2023:** VERIFIED. 
8.2 million was the highest single-year number since the mid-1990s, up from the previous record of 7.5M in 2022.

- **"Notifications continuing to rise":** PARTIALLY VERIFIED. They rose through 2023, then levelled off. 
In 2024, 8.3 million were newly diagnosed and notified, similar to 8.2 million in 2023 and 17% above the pre-pandemic level of 7.1 million.
 The better statement is that 2024 is a plateau at about 8.3M, which is 10.7% above 7.5M.
- **"2022 was a post-COVID recovery year":** VERIFIED. WHO says 
those diagnosed in 2022 and 2023 probably included a sizeable backlog of people whose diagnosis was delayed by COVID-related disruptions.
 This applies to 2023 as well. Part of the 8.2M may be one-off backlog, so it is not a clean steady-state anchor either.
- **Arithmetic:** VERIFIED. 8.2/7.5 = +9.3% and 8.3/7.5 = +10.7%. Applied to 5.5M, that gives ~6.0–6.1M. The result is below the ±25% materiality bar.

**EVIDENCE FOUND**
- The 2024 data point (8.3M, from the WHO Global TB Report 2025) post-dates the Investigator's recollection. It supports "upward, small."
- The backlog caveat means the upward correction may be slightly overstated if the baseline is treated as a steady-state level.

**REVISED CRITIQUE:** Same as stated, with these edits.
- Replace "continuing to rise" with "rose to 8.2M in 2023 and plateaued at 8.3M in 2024."
- Add the backlog caveat.
- Strength remains small, direction up (+9–11%).

---

## Critique 2: A 2%/yr decline in notified counts contradicts the observed trend

**OVERALL VERDICT: PARTIALLY VERIFIED.** The core hypothesis is well supported by WHO data. Three things don't survive as stated.
- The claim about CG's method is unverifiable.
- The "+29%" figure double-counts Critique 1.
- The 2025 funding-shock point is ungrounded.

**CLAIM CHECK**
- **Rates fall about 1–2%/yr:** VERIFIED. WHO describes 
declines of about 2% per year between 2010 and 2020, reversed by a 4.6% rise from 2020 to 2023.
 
The net reduction in the rate from 2015 to 2024 was 12.3%
, which is about 1.4%/yr.
- **Rate down ~8% over 2015–2023:** VERIFIED. 
The net reduction was 8.3%.

- **Counts are roughly flat while rates fall:** VERIFIED for the recent period, but "since 2015" is unconfirmed. 
Incident cases fell 1% in 2024, from 10.8M to 10.7M, but remain above the 2020 level of 10.3M.
 I did not retrieve a 2015 absolute figure.
- **Population growth drives counts:** VERIFIED in direction. WHO states 
most of the global increase in incident cases between 2022 and 2023 reflects population growth.

- **~25% of incident cases are not notified:** VERIFIED, and now somewhat better. 
In 2024 about 2.4 million people were not diagnosed or not reported, and notifications were 78% of incidence.
 In 2023 the gap was 
about 2.7 million, down from around 4 million in 2020 and 2021.
 This supports "detection gaps are closing."
- **Notified counts are flat to rising, not falling 2%/yr:** VERIFIED. Notifications went from 7.1M in 2019 to 8.3M in 2024. 
In the African Region they were 38% above 2019.

- **"CG applies a 2%/yr decline to counts":** UNVERIFIABLE. I have no CG source. This is the pivotal premise, so it should stay flagged.
- **Scenario arithmetic:** the arithmetic is correct.
  - 8.2 × 0.96 × 0.90 = 7.09M, which is +29% versus 5.5M.
  - With +1%/yr growth, 8.2 × 1.01⁸ × 0.864 = 7.67M.
  - The 6.5M lower bound corresponds to about −1%/yr.
- **Double-counting problem:** the +29% already includes Critique 1.
  - Flat counts remove 8 years of 2%/yr decline (0.98⁸ ≈ 0.85), which is worth +17.5% on its own.
  - The baseline update adds about +9% (1.093 × 1.175 ≈ 1.28).
  - Critique 2 alone is therefore about +17.5% for flat counts, or about +27% with +1%/yr growth.
  - Crossing the 25% bar needs Critique 1 or a rise in counts. The Investigator's wording ("combined with Critique 1") is right, but the +29% should not be presented as Critique 2's standalone effect.
- **2025 funding disruptions could cut notifications:** UNVERIFIABLE. My searches returned no data on the size of this effect, and the 2024 data pre-date it. It stays flagged as ungrounded.
- **Direction field "uncertain":** the text argues the error is probably upward, so the label is internally inconsistent. The evidence supports "likely increases," with downside risk from funding and from the backlog fading.

**EVIDENCE FOUND**
- WHO notes that 
the recovery in reported newly diagnosed cases in 2022–2024 first slowed increases in incidence, then reversed the upward trend.
 Notifications and incidence estimates are therefore linked, which weakens any "independent" notification trend.
- Counter-consideration: WHO's 2.4M gap bounds how much notifications can rise from detection alone. The ceiling is about +28% above 8.3M, and only in the unrealistic case of 100% detection.

**REVISED CRITIQUE:** Rate declines in WHO reporting are not the same as declines in case counts. Observed notifications rose from 7.5M (2022) to 8.3M (2024), and incident counts have been about flat (10.3–10.8M since 2020). If CG applies 2%/yr to counts, it likely understates the eligible population by roughly 17% (flat counts) to 27% (+1%/yr), before the baseline correction in Critique 1.
- Combined with Critique 1, eligible is about 6.5–7.7M.
- The CG-method premise and the funding-shock point stay flagged as UNGROUNDED.
- Strength: medium. Direction: up, with downside risk.

---

## Critique 3: "Adult DS notified" is not "eligible for the trial label"

**OVERALL VERDICT: PARTIALLY VERIFIED.** The WHO shares are broadly right, and the direction (filters reduce eligibility) is sound. One denominator is mis-stated, one share is slightly high, and the exclusion list is the Investigator's own inference.

**CLAIM CHECK**
- **Extrapulmonary TB ~15%:** VERIFIED. 
In 2024, 84% of notified cases were pulmonary and 16% extrapulmonary
, and the 2023 figures were the same (
84% and 16%
). Regional variation is large. 
South-East Asia is 25% extrapulmonary
, and 
India and Bangladesh are above 20%.
 The ×0.85 filter is therefore too lenient for India and South Asia, the biggest contributors.
- **Clinically diagnosed "~35–40% of notifications":** MISSTATED. 
Of 6.9 million pulmonary cases in 2024, 64% were bacteriologically confirmed, up from 62% in 2023.
 The 62–64% is a share of pulmonary cases, not of all notifications, so 36–38% of pulmonary cases are clinically diagnosed.
  - The stacked arithmetic does apply ×0.62 after the pulmonary filter, so it is consistent.
  - Of all notifications, confirmed pulmonary cases are only about 0.84 × 0.64 ≈ 54%.
- **HIV coinfection ~6–8%:** SLIGHTLY HIGH. 
5.8% of incident cases in 2024 were among people living with HIV
, and 
6.1% in 2023.
 Notified HIV-positive cases were 
413,516 in 2024
, about 5% of 8.3M. A range of 5–7% is better. The share is concentrated in Africa, with 
over 50% in parts of southern Africa.

- **Hr-TB ~7%:** VERIFIED. 
Hr-TB prevalence was estimated at 7.4% among new cases and 11.4% among previously treated cases.
 Another source gives 
7.1% of new cases.
 It is 
treated with a modified regimen including levofloxacin since 2018.
 I did not verify how routinely Hr-TB is detected. Isoniazid DST is not routine, so many Hr-TB patients are probably in "DS" cohorts in practice. That blunts the filter's real-world effect but not a trial-eligibility one.
- **Pregnancy, hepatic disease, existing statin use, drug interactions:** UNVERIFIABLE. These are inference from standard trial design, as the Investigator says. The ×0.85 for "other filters" is also ungrounded. HIV plus Hr-TB alone gives about 0.87, so 0.85 is plausible but unsupported.
- **Stack arithmetic:** correct.
  - 5.5 × 0.85 = 4.7M, then × 0.85 = 4.0M, then × 0.62 = 2.5M.
  - Restricting to bacteriologically confirmed cases is a trial-design choice. A label population may not carry it.

**EVIDENCE FOUND**
- Applying Critique 2's upside to these filters:
  - 7.1M (flat, adjusted) × 0.85 × 0.85 = 5.1M. That is about −7% versus 5.5M, so it roughly nets out to the current figure, as the Investigator suggests.
  - Adding the confirmed-only restriction gives about 3.2M, below the 3.6M bar.
- The conclusion therefore hinges on whether the label or trial requires bacteriological confirmation. That is the single most decision-relevant unknown.
- Applying the filters to the regional mix makes this worse. India and South Asia have the highest extrapulmonary share, and Africa has the highest HIV share.

**REVISED CRITIQUE:** Notified adult cases overstate the population that fits a pulmonary, trial-like label. Verified WHO figures:
- Extrapulmonary share is 16% globally and ~25% in South-East Asia.
- Pulmonary cases are 64% bacteriologically confirmed (the denominator is pulmonary, not all notifications).
- HIV is about 5–6%.
- Hr-TB is about 7%.

An illustrative stack gives 4.0M without confirmation and ~2.5M with it, before the upside from Critique 2. The statin-specific exclusions and the ×0.85 factor are the Investigator's own assumptions and are flagged as UNGROUNDED. Strength: medium. Standalone direction: down. Net direction when combined with Critique 2: uncertain.

--- Critique: Shorter and new regimens erode both the eligible population and the incremental benefit ---

## Critique 1: Shorter and new regimens erode both the eligible population and the incremental benefit

**CLAIM CHECK**

- **WHO (2022) recommended a 4-month HPMZ regimen for people aged 12 and over: VERIFIED.**
  - 
The WHO 2022 DS-TB module recommends a 4-month isoniazid, rifapentine, moxifloxacin and pyrazinamide regimen for people aged 12 or older with pulmonary DS-TB.
 It is a conditional recommendation with moderate certainty of evidence.
  - WHO also said that 
clinicians should weigh eligibility criteria, patient preference and local factors such as the availability of rifapentine.
 This supports the supply and uptake caveat, though it does not quantify it.
- **Dorman et al., NEJM 2021 (Study 31/A5349): VERIFIED, with an incomplete check.**
  - I did not retrieve the paper directly. A trial protocol states that 
a four-month rifapentine regimen containing moxifloxacin was non-inferior to the standard 6-month regimen (Dorman et al., 2021).

  - A ClinicalTrials.gov reference list also carries the matching title, "Four-Month Rifapentine Regimens with or without Moxifloxacin for Tuberculosis."
- **Paton et al., NEJM 2023 (TRUNCATE-TB): VERIFIED, but MISCHARACTERISED as a "regimen" alternative.**
  - The citation is correct: 
Paton NI et al., "Treatment Strategy for Rifampin-Susceptible Tuberculosis," N Engl J Med 2023;388(10):873-887.

  - It tested a management strategy, not a drop-in regimen. 
An initial 8-week bedaquiline–linezolid regimen was noninferior to standard treatment for a composite clinical outcome at week 96.

  - The strategy includes monitoring and retreatment of relapses. A later exploratory analysis found 
all four 8-week regimens had lower efficacy than the standard 24-week regimen.
 Its authors say that 
even the best 8-week bedaquiline-linezolid regimen should only be used within the TRUNCATE management strategy.

  - This makes TRUNCATE-TB a weaker candidate for displacing HRZE at scale by ~2033 than the critique implies. I found no WHO recommendation for it.
- **"Bedaquiline-containing short regimens" in the pipeline: PLAUSIBLE/VERIFIED as pipeline.**
  - Bedaquiline-containing regimens are being tested for DS-TB, for example 
the SimpliciTB bedaquiline-pretomanid-moxifloxacin-pyrazinamide trial.
 There is also a Phase 2 trial of TBAJ-876 or bedaquiline with pretomanid and linezolid (NCT06058299).
  - These are Phase 2 or 2c. None is a recommended DS-TB standard of care.
- **"Rifapentine is a stronger CYP3A4 inducer than rifampicin": UNVERIFIED, and probably wrong as stated.**
  - I found no source in my searches. My background understanding, which I could not re-check this session, is that rifapentine is usually described as a CYP3A4 inducer of similar or somewhat lower potency than rifampicin, not a stronger one.
  - What does survive: both are strong rifamycin inducers, so a statin interaction concern applies to HPMZ as well. The "may worsen" wording should be dropped.
- **Slow HPMZ uptake because of rifapentine supply and cost: PLAUSIBLE, UNVERIFIED.**
  - One 2025 abstract notes that 
the high rifapentine dose may limit use in clinical practice, particularly in patients with comorbidities.
 That is a clinical limitation, not a supply or cost finding. I found no programme-level uptake data.
- **20–40% adoption scenario: UNGROUNDED, as the Investigator admits.** The arithmetic is correct: 5.5M × 0.6–0.8 = 3.3–4.4M.
- **The 5.5M eligible figure and the 3.6M bar** come from the CEA source materials, which I do not have. I could not check them.

**EVIDENCE FOUND**
- WHO's conditional recommendation, and its explicit reference to rifapentine availability, supports a slow-uptake scenario.
- 
Adolescents aged 12–16 have three options: 4-month HPMZ, 4-month 2HRZ(E)/2HR, or standard 6-month.
 The 4-month 2HRZ(E)/2HR regimen for non-severe paediatric TB is still rifampicin-based. It reduces duration, not the backbone.
- Concerning "shortening" benefit: the 4-month 2HRZ(E)/2HR regimen applies only to non-severe TB in children under 16. It is not a general adult option.
- No evidence was found on the effect of a statin adjunct on shorter regimens. This is a genuine gap.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The HPMZ and Dorman facts are correct. The core logic (new backbones reduce applicability and incremental benefit) is sound but ungrounded quantitatively. The rifapentine "stronger inducer" claim is unverified and probably wrong. TRUNCATE-TB is mischaracterised.

**REVISED CRITIQUE**
- **Hypothesis:** By the benefit horizon, some DS-TB patients may be on the WHO-recommended 4-month HPMZ regimen, which includes rifapentine and moxifloxacin in place of rifampicin and ethambutol. 
This applies to people aged 12 or older.
 A statin trial on HRZE may not transfer to that backbone.
- **Retained:**
  1. Applicability: the evidence is HRZE-specific.
  2. Incremental value: shorter regimens leave less room for a duration-shortening adjunct.
  3. Rifamycin interaction concerns would likely apply to rifapentine as well as rifampicin. The direction and size of any difference is unverified.
- **Corrections:**
  - TRUNCATE-TB is a strategy trial with bedaquiline–linezolid, not a WHO-endorsed standard regimen, so it is a weaker driver of displacement.
  - Bedaquiline-based DS-TB regimens remain in Phase 2 or 2c.
- **Flagged UNGROUNDED:** the 20–40% adoption range and the slow-uptake claim. The drop to 3.3–4.4M is arithmetic on an assumed range.
- **Strength:** medium, direction uncertain. The adoption share is the key unknown. The "at or near 3.6M" conclusion depends wholly on the assumed range.

---

## Critique 2: M72/AS01E and other incidence shocks

**CITATION CHECK**
- **Tait et al., NEJM 2019: VERIFIED.**
  - It is the "Final Analysis of a Trial of M72/AS01E Vaccine to Prevent Tuberculosis," N Engl J Med 2019;381:2429–39.
  - 
Vaccine efficacy at month 36 was 49.7% (90% CI 12.1–71.2; 95% CI 2.1–74.2).

  - The ~50% efficacy figure is accurate. Note the very wide confidence interval and that the original 2018 report (Van Der Meeren) gave 
54.0% efficacy.

- **Harris et al.: PARTIALLY VERIFIED, MISATTRIBUTED.**
  - Rebecca Harris of LSHTM is first author of 
"Age-targeted tuberculosis vaccination in China and implications for vaccine development: a modelling study," Lancet Glob Health 2019.

  - That paper models generic vaccine profiles, with the intermediate profile at 
60% efficacy, 10-year protection and 70% coverage.
 It is not an M72-specific projection.
  - I could not find a Harris paper projecting M72 impacts "mostly in the 2040s." The Investigator already says they cannot cite a figure.

**CLAIM CHECK**
- **Phase III started 2024: VERIFIED.** 
In March 2024, M72 went into phase 3 trials.
 The registered trial is NCT06062238, run by the Gates Medical Research Institute (
ongoing registrational efficacy trial.
).
- **~20,000 participants: PARTIALLY VERIFIED.** Sources vary.
  - Nature reports 
around 26,000 participants across seven countries.

  - A design paper models 
18,000 IGRA-positive participants
 for the primary analysis, with the full trial larger once other groups are added.
  - ~20,000 is not wrong for the IGRA+ core, but ~26,000 is the better-supported total.
- **Results "late 2020s": PLAUSIBLE.** The design paper projects 
a 90% probability of accruing 110 events within 3.5 to 4 years.
 With enrolment starting in 2024, a primary readout near 2028 is consistent. Licensure around 2028–30 is therefore plausible but unconfirmed.
- **Phase IIb efficacy was in a small, selected population: VERIFIED.**
  - It enrolled 
3,573 HIV-negative adults aged 18–50 who were IGRA-positive.

  - It rested on 
39 primary-analysis cases (13 in the vaccine group, 26 on placebo).

  - The Investigator's caution about probability-weighting is well founded.
- **Vaccine impact mostly via preventing progression in the already-infected: VERIFIED as the efficacy basis, with modelling nuance.**
  - Phase IIb efficacy was measured only in infected people. LSHTM modellers note that 
a pre- and post-infection vaccine had a much greater impact on 2050 incidence than a post-infection-only vaccine.
 That supports the idea that impact accrues gradually.
  - An analysis of the trial found that 
the most plausible models needed protection against at least two of the three routes to active TB.
 So the mechanism is not settled.
- **Slow rollout needing Gavi financing: PLAUSIBLE.** A recent M72 demand-forecast paper includes 
an "upside" scenario with higher efficacy, more global funding (Gavi and others) and faster rollout than the base case.
 This implies the base case assumes slower and more constrained rollout.
- **LSHTM-type models project larger impacts in the 2040s: PLAUSIBLE, UNVERIFIED.** LSHTM-linked India modelling 
projects over 2025–2050
 and reports results as cumulative impact by 2050. That is consistent with late-accruing impact but does not show a 2040s-specific finding. This modelling assumes 
non-vaccine scale-up toward a 50% incidence reduction by 2035,
 which would itself shrink the eligible pool independently of vaccines.
- **Own estimate of a 5–15% incidence reduction by 2033–35: UNGROUNDED.** The arithmetic is right: 5.5M × 0.85–0.95 = ~4.7–5.2M. The 20–35% average reduction over a 15+-year horizon is also ungrounded and depends on the CEA structure.

**EVIDENCE FOUND**
- Global M72 demand-forecast work and country models exist and could ground the rollout assumptions. I did not extract specific numbers.
- An M72-specific South Africa model and India models exist (
49.7% efficacy over 3 years in previously sensitised adolescents and adults
 as the input). These would be better sources than Harris 2019 for a sensitivity analysis.
- Efficacy was assessed only in IGRA+ individuals, and its uncertainty and duration of protection (10 years is an assumed value in one model) add further uncertainty to any projected incidence effect.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The Tait citation, the Phase III existence and timing, and the logic that vaccine impact is a later-horizon effect hold. The Harris citation is misattributed, the participant number is imprecise, and all impact magnitudes are ungrounded.

**REVISED CRITIQUE**
- **Hypothesis:** The M72/AS01E Phase III (NCT06062238, began March 2024, ~20,000–26,000 participants depending on source) follows a Phase IIb in which 
efficacy was 49.7% (95% CI 2.1–74.2)
 in IGRA+, HIV-negative adults. If it succeeds, licensure is plausibly ~2028–30 with a slow rollout.
- **Retained:** Population-level incidence effects are unlikely to be large by 2033–35, and they matter more over a long benefit horizon. The CEA's constant eligible population of 5.5M may therefore overstate eligible patients in later years. The probability of vaccine success should be modelled separately.
- **Removed or corrected:**
  - Harris 2019 is a generic China age-targeting model, not an M72 projection. Replace it with M72-specific models (India, South Africa) for future citations.
  - The participant count should be stated as a range.
- **Flagged UNGROUNDED:** the 5–15% incidence reduction by 2033–35, the 30–50% later-year reduction, and the 20–35% average-eligible reduction. A CEA sensitivity analysis is required.
- **Strength:** medium, direction decreases. The size depends on trial success, coverage and the CEA's treatment of post-adoption years.

--- Critique: M72/AS01E and other incidence shocks are likely not large enough by year 8–10, but should be modelled ---

## Critique 1: Shorter and new regimens erode both the eligible population and the incremental benefit

**CLAIM CHECK**

- **WHO (2022) recommended a 4-month HPMZ regimen for people aged 12 and over: VERIFIED.**
  - 
The WHO 2022 DS-TB module recommends a 4-month isoniazid, rifapentine, moxifloxacin and pyrazinamide regimen for people aged 12 or older with pulmonary DS-TB.
 It is a conditional recommendation with moderate certainty of evidence.
  - WHO also said that 
clinicians should weigh eligibility criteria, patient preference and local factors such as the availability of rifapentine.
 This supports the supply and uptake caveat, though it does not quantify it.
- **Dorman et al., NEJM 2021 (Study 31/A5349): VERIFIED, with an incomplete check.**
  - I did not retrieve the paper directly. A trial protocol states that 
a four-month rifapentine regimen containing moxifloxacin was non-inferior to the standard 6-month regimen (Dorman et al., 2021).

  - A ClinicalTrials.gov reference list also carries the matching title, "Four-Month Rifapentine Regimens with or without Moxifloxacin for Tuberculosis."
- **Paton et al., NEJM 2023 (TRUNCATE-TB): VERIFIED, but MISCHARACTERISED as a "regimen" alternative.**
  - The citation is correct: 
Paton NI et al., "Treatment Strategy for Rifampin-Susceptible Tuberculosis," N Engl J Med 2023;388(10):873-887.

  - It tested a management strategy, not a drop-in regimen. 
An initial 8-week bedaquiline–linezolid regimen was noninferior to standard treatment for a composite clinical outcome at week 96.

  - The strategy includes monitoring and retreatment of relapses. A later exploratory analysis found 
all four 8-week regimens had lower efficacy than the standard 24-week regimen.
 Its authors say that 
even the best 8-week bedaquiline-linezolid regimen should only be used within the TRUNCATE management strategy.

  - This makes TRUNCATE-TB a weaker candidate for displacing HRZE at scale by ~2033 than the critique implies. I found no WHO recommendation for it.
- **"Bedaquiline-containing short regimens" in the pipeline: PLAUSIBLE/VERIFIED as pipeline.**
  - Bedaquiline-containing regimens are being tested for DS-TB, for example 
the SimpliciTB bedaquiline-pretomanid-moxifloxacin-pyrazinamide trial.
 There is also a Phase 2 trial of TBAJ-876 or bedaquiline with pretomanid and linezolid (NCT06058299).
  - These are Phase 2 or 2c. None is a recommended DS-TB standard of care.
- **"Rifapentine is a stronger CYP3A4 inducer than rifampicin": UNVERIFIED, and probably wrong as stated.**
  - I found no source in my searches. My background understanding, which I could not re-check this session, is that rifapentine is usually described as a CYP3A4 inducer of similar or somewhat lower potency than rifampicin, not a stronger one.
  - What does survive: both are strong rifamycin inducers, so a statin interaction concern applies to HPMZ as well. The "may worsen" wording should be dropped.
- **Slow HPMZ uptake because of rifapentine supply and cost: PLAUSIBLE, UNVERIFIED.**
  - One 2025 abstract notes that 
the high rifapentine dose may limit use in clinical practice, particularly in patients with comorbidities.
 That is a clinical limitation, not a supply or cost finding. I found no programme-level uptake data.
- **20–40% adoption scenario: UNGROUNDED, as the Investigator admits.** The arithmetic is correct: 5.5M × 0.6–0.8 = 3.3–4.4M.
- **The 5.5M eligible figure and the 3.6M bar** come from the CEA source materials, which I do not have. I could not check them.

**EVIDENCE FOUND**
- WHO's conditional recommendation, and its explicit reference to rifapentine availability, supports a slow-uptake scenario.
- 
Adolescents aged 12–16 have three options: 4-month HPMZ, 4-month 2HRZ(E)/2HR, or standard 6-month.
 The 4-month 2HRZ(E)/2HR regimen for non-severe paediatric TB is still rifampicin-based. It reduces duration, not the backbone.
- Concerning "shortening" benefit: the 4-month 2HRZ(E)/2HR regimen applies only to non-severe TB in children under 16. It is not a general adult option.
- No evidence was found on the effect of a statin adjunct on shorter regimens. This is a genuine gap.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The HPMZ and Dorman facts are correct. The core logic (new backbones reduce applicability and incremental benefit) is sound but ungrounded quantitatively. The rifapentine "stronger inducer" claim is unverified and probably wrong. TRUNCATE-TB is mischaracterised.

**REVISED CRITIQUE**
- **Hypothesis:** By the benefit horizon, some DS-TB patients may be on the WHO-recommended 4-month HPMZ regimen, which includes rifapentine and moxifloxacin in place of rifampicin and ethambutol. 
This applies to people aged 12 or older.
 A statin trial on HRZE may not transfer to that backbone.
- **Retained:**
  1. Applicability: the evidence is HRZE-specific.
  2. Incremental value: shorter regimens leave less room for a duration-shortening adjunct.
  3. Rifamycin interaction concerns would likely apply to rifapentine as well as rifampicin. The direction and size of any difference is unverified.
- **Corrections:**
  - TRUNCATE-TB is a strategy trial with bedaquiline–linezolid, not a WHO-endorsed standard regimen, so it is a weaker driver of displacement.
  - Bedaquiline-based DS-TB regimens remain in Phase 2 or 2c.
- **Flagged UNGROUNDED:** the 20–40% adoption range and the slow-uptake claim. The drop to 3.3–4.4M is arithmetic on an assumed range.
- **Strength:** medium, direction uncertain. The adoption share is the key unknown. The "at or near 3.6M" conclusion depends wholly on the assumed range.

---

## Critique 2: M72/AS01E and other incidence shocks

**CITATION CHECK**
- **Tait et al., NEJM 2019: VERIFIED.**
  - It is the "Final Analysis of a Trial of M72/AS01E Vaccine to Prevent Tuberculosis," N Engl J Med 2019;381:2429–39.
  - 
Vaccine efficacy at month 36 was 49.7% (90% CI 12.1–71.2; 95% CI 2.1–74.2).

  - The ~50% efficacy figure is accurate. Note the very wide confidence interval and that the original 2018 report (Van Der Meeren) gave 
54.0% efficacy.

- **Harris et al.: PARTIALLY VERIFIED, MISATTRIBUTED.**
  - Rebecca Harris of LSHTM is first author of 
"Age-targeted tuberculosis vaccination in China and implications for vaccine development: a modelling study," Lancet Glob Health 2019.

  - That paper models generic vaccine profiles, with the intermediate profile at 
60% efficacy, 10-year protection and 70% coverage.
 It is not an M72-specific projection.
  - I could not find a Harris paper projecting M72 impacts "mostly in the 2040s." The Investigator already says they cannot cite a figure.

**CLAIM CHECK**
- **Phase III started 2024: VERIFIED.** 
In March 2024, M72 went into phase 3 trials.
 The registered trial is NCT06062238, run by the Gates Medical Research Institute (
ongoing registrational efficacy trial.
).
- **~20,000 participants: PARTIALLY VERIFIED.** Sources vary.
  - Nature reports 
around 26,000 participants across seven countries.

  - A design paper models 
18,000 IGRA-positive participants
 for the primary analysis, with the full trial larger once other groups are added.
  - ~20,000 is not wrong for the IGRA+ core, but ~26,000 is the better-supported total.
- **Results "late 2020s": PLAUSIBLE.** The design paper projects 
a 90% probability of accruing 110 events within 3.5 to 4 years.
 With enrolment starting in 2024, a primary readout near 2028 is consistent. Licensure around 2028–30 is therefore plausible but unconfirmed.
- **Phase IIb efficacy was in a small, selected population: VERIFIED.**
  - It enrolled 
3,573 HIV-negative adults aged 18–50 who were IGRA-positive.

  - It rested on 
39 primary-analysis cases (13 in the vaccine group, 26 on placebo).

  - The Investigator's caution about probability-weighting is well founded.
- **Vaccine impact mostly via preventing progression in the already-infected: VERIFIED as the efficacy basis, with modelling nuance.**
  - Phase IIb efficacy was measured only in infected people. LSHTM modellers note that 
a pre- and post-infection vaccine had a much greater impact on 2050 incidence than a post-infection-only vaccine.
 That supports the idea that impact accrues gradually.
  - An analysis of the trial found that 
the most plausible models needed protection against at least two of the three routes to active TB.
 So the mechanism is not settled.
- **Slow rollout needing Gavi financing: PLAUSIBLE.** A recent M72 demand-forecast paper includes 
an "upside" scenario with higher efficacy, more global funding (Gavi and others) and faster rollout than the base case.
 This implies the base case assumes slower and more constrained rollout.
- **LSHTM-type models project larger impacts in the 2040s: PLAUSIBLE, UNVERIFIED.** LSHTM-linked India modelling 
projects over 2025–2050
 and reports results as cumulative impact by 2050. That is consistent with late-accruing impact but does not show a 2040s-specific finding. This modelling assumes 
non-vaccine scale-up toward a 50% incidence reduction by 2035,
 which would itself shrink the eligible pool independently of vaccines.
- **Own estimate of a 5–15% incidence reduction by 2033–35: UNGROUNDED.** The arithmetic is right: 5.5M × 0.85–0.95 = ~4.7–5.2M. The 20–35% average reduction over a 15+-year horizon is also ungrounded and depends on the CEA structure.

**EVIDENCE FOUND**
- Global M72 demand-forecast work and country models exist and could ground the rollout assumptions. I did not extract specific numbers.
- An M72-specific South Africa model and India models exist (
49.7% efficacy over 3 years in previously sensitised adolescents and adults
 as the input). These would be better sources than Harris 2019 for a sensitivity analysis.
- Efficacy was assessed only in IGRA+ individuals, and its uncertainty and duration of protection (10 years is an assumed value in one model) add further uncertainty to any projected incidence effect.

**OVERALL VERDICT: PARTIALLY VERIFIED.** The Tait citation, the Phase III existence and timing, and the logic that vaccine impact is a later-horizon effect hold. The Harris citation is misattributed, the participant number is imprecise, and all impact magnitudes are ungrounded.

**REVISED CRITIQUE**
- **Hypothesis:** The M72/AS01E Phase III (NCT06062238, began March 2024, ~20,000–26,000 participants depending on source) follows a Phase IIb in which 
efficacy was 49.7% (95% CI 2.1–74.2)
 in IGRA+, HIV-negative adults. If it succeeds, licensure is plausibly ~2028–30 with a slow rollout.
- **Retained:** Population-level incidence effects are unlikely to be large by 2033–35, and they matter more over a long benefit horizon. The CEA's constant eligible population of 5.5M may therefore overstate eligible patients in later years. The probability of vaccine success should be modelled separately.
- **Removed or corrected:**
  - Harris 2019 is a generic China age-targeting model, not an M72 projection. Replace it with M72-specific models (India, South Africa) for future citations.
  - The participant count should be stated as a range.
- **Flagged UNGROUNDED:** the 5–15% incidence reduction by 2033–35, the 30–50% later-year reduction, and the 20–35% average-eligible reduction. A CEA sensitivity analysis is required.
- **Strength:** medium, direction decreases. The size depends on trial success, coverage and the CEA's treatment of post-adoption years.