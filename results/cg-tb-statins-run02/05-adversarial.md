--- Critique: "Success" in Phase III is unlikely to be a mortality result, so the 10% mortality effect is not what a "success" would establish ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION: "Success" in Phase III is unlikely to be a mortality result, so the 10% mortality effect is not what a "success" would establish

**EXISTING COVERAGE:**

1. The BOTEC does not claim that a Phase III will observe a 10% mortality reduction. It assumes a 10% relative reduction *conditional on a positive result*, then multiplies by a 40% probability that Phase II and III both succeed. The expected relative reduction is therefore 4%, not 10%.
2. The 40% already includes worlds where the effect is zero or the drug fails. The critique's mixture, E[r|success] = (1−f)(0.10) + f·r_s, partly re-penalizes risk that the 40% was meant to absorb. The BOTEC never defines "success," so we cannot tell how much overlap there is. If the 40% was set with a surrogate-success reading in mind, the critique double-counts. If it was set with a mortality-success reading, the critique is right.
3. The grant funds a Phase IIc testing "survival, infection clearance and lung damage." CG therefore expects to learn something about survival before committing to Phase III. This is a staged-gate structure, not a blind extrapolation from surrogates.
4. Adoption of TB regimens on non-mortality endpoints has precedent, so a surrogate or composite "success" can still drive uptake. Example: Study 31/A5349 (Dorman et al., NEJM 2021) tested a 4-month rifapentine–moxifloxacin regimen on TB disease-free survival at 12 months, not mortality. This supports modeling "success" as a route to adoption, which is what the 40% × 60% uptake chain represents. It does not support the separate claim that the mortality effect is 10%.
5. The parameter map notes that only on-treatment mortality is valued. Morbidity, post-treatment mortality, transmission and diagnostic value are implicit zeros. If surrogate success reflects less lung damage, real benefits exist that the BOTEC omits. This is a partial offset to the critique's discounting, though I cannot quantify it.

**EVIDENCE WEAKNESSES:**

1. The critique's two central parameters are, by its own admission, unsourced: f = 0.5 and r_s = 0.03. Its headline conclusion ("exactly at the threshold") rests entirely on these two guesses.
2. I checked the threshold arithmetic. Going from ~3,000x to 2,000x requires cutting E[r|success] from 0.10 to about 0.067 (3,000 × 0.067/0.10 ≈ 2,000). The crossing condition is therefore f·(0.10 − r_s) > ~0.033.
   - With f = 0.5, r_s must be below ~0.033.
   - With f = 0.5 and r_s = 0.04, SROI is ~2,100x, above the bar.
   - With f = 0.3, even r_s = 0 gives E[r] = 0.07 and ~2,100x.
   - The conclusion is therefore fragile to values the critic says it cannot ground.
3. The sample-size arithmetic checks out under the standard two-proportion formula. I got ~35,800 per arm at 4% baseline, ~17,200 at 8%, and ~73,000 at 2%, matching the critic. But the critique used 4% baseline, not CG's 6%. At 6% baseline and a 10% relative reduction, the same formula gives ~23,400 per arm. This is still very large, so the point survives, but the critique's figures are not calibrated to CG's own baseline.
4. "No TB drug trial approaches this scale" is asserted without a cited survey of trial sizes. I cannot ground a counterexample either. It is plausible, but it is the critic's recollection, not a verified fact.
5. The Phase IIB evidence the critique cites (open-label design, more muscle pain with atorvastatin, reduced peripheral neuropathy) bears on surrogate reliability and safety. None of it shows the mortality effect is smaller than 10%. The critique establishes "no mortality evidence," which is not the same as "mortality effect below 10%."

**MAGNITUDE CHALLENGE:**

1. The critique itself labels its magnitude "unknown." It supplies a direction and an illustrative scenario, not a derived range.
2. The critique treats r_s as bounded above by 0.10 in effect, but I see no grounding for that bound. Statins' proposed mechanism is host-directed (less lung inflammation and damage). If so, the mortality effect could be larger than 10% in worlds where surrogates improve strongly. I accept this arguendo and note the critique has no evidence for the other direction either. The true conditional distribution is two-sided, and the critique considers only the downside.
3. A mortality-powered Phase III being implausible cuts two ways. A trial powered for a larger effect, say 20–30% relative (I cannot source a figure), would only declare success if the observed effect were large. Conditional on a mortality-endpoint success, the true effect would then likely exceed 10%. This weakens the claim that "success" systematically implies a lower effect than 10%.
4. A defensible conservative adjustment is a modest haircut, not a 50% cut. With f between 0.3 and 0.5 and r_s between 0.03 and 0.05, E[r|success] ranges from 0.065 to 0.080 (computed from the critic's own formula). That implies SROI of ~1,950x to ~2,400x. This straddles the bar rather than clearly falling below it.

**OFFSETTING FACTORS:**

1. The BOTEC values only on-treatment mortality. The parameter map lists morbidity DALYs, post-treatment mortality (lung damage reduction), transmission, and diagnostic value as unvalued. A surrogate-only success, such as reduced lung damage, plausibly carries real unvalued benefit. The critique discounts the mortality channel without crediting these.
2. A 6% baseline mortality was used, which is higher than the 4% or 2% the critique uses for sample sizes. The parameter map also notes that notified-cohort mortality may understate true mortality via unascertained deaths. This potentially raises the baseline, offsetting a lower relative effect.
3. The drug is generic and cheap, so a surrogate-based guideline change may need less evidence than a branded drug would. This supports the adoption assumption that the critique does not challenge.
4. The Phase IIc generates survival and lung-damage data, which narrows uncertainty before the Phase III decision. That is a reason to think the 40% is not arbitrary.

**OVERALL ASSESSMENT:** Partial defense.

- The critique's direction is credible. The BOTEC defines neither "success" nor how a 10% mortality figure derives from surrogate data. Large mortality trials are infeasible, which makes the critic's reading of "success" plausible.
- The defense is only partial because I cannot show that CG's 40% was set with a mortality-success definition. If it was, the critique has force.
- The critique's quantification rests on two unsourced parameters and crosses the 2,000x line only in part of the parameter space. It also ignores upside channels (lung-damage benefit, higher true baseline mortality, larger effect needed for powered-trial success).

**CONCESSIONS:**

1. CG gives no derivation of the 10% relative reduction from surrogate evidence. Nothing in the evidence package supports 10% from human mortality data.
2. The BOTEC does not define "success," which leaves open the surrogate-versus-mortality ambiguity the critique identifies.
3. A mortality-powered Phase III at the sample sizes the critique computes (and the ~23,400 per arm I computed at CG's 6% baseline) is implausible, so a Phase III "success" is probably not a mortality result.
4. A reasonable discount of E[r|success] below 0.10 is warranted. The size of the discount is unresolved, and it could take SROI from ~3,000x to near or somewhat below 2,000x.
5. The p_success and relative_reduction parameters are plausibly correlated rather than independent, as the parameter map flags.

### Challenger
REBUTTAL: "Success" in Phase III is unlikely to be a mortality result, so the 10% mortality effect is not what a "success" would establish

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the 40% p_success already absorbs zero-effect and failure worlds, so the critique's mixture E[r|success] partly double-counts. Whether it does depends on whether the 40% was set under a surrogate-success or a mortality-success reading.

1. **The 40% cannot absorb a discount on the conditional effect.**
   - The BOTEC multiplies 10% × 40%. That structure treats 10% as the effect *given* success.
   - p_success governs whether the event occurs. It says nothing about what mortality effect the event implies.
   - The critique is about E[r | success]. That quantity sits outside the 40% by construction.

2. **The Advocate's two branches do not both help the defense.**
   - If the 40% was set under a surrogate-success reading, the critique does not double-count. That is the world in which the 10% is unsupported.
   - Double-counting arises only if the 40% was set as P(a real ~10% mortality effect materializes). That is a different event from the Advocate's own description of the 40% as "Phase II and III both succeed."
   - Neither the Advocate nor the verifier found anything supporting that reading. At best it is an unverified possibility. It is not a rebuttal.

3. **The Phase IIc "survival" readout does not discipline the 10%.**
   - By the Advocate's own arithmetic, detecting a 10% relative reduction at CG's 6% baseline needs ~23,400 per arm. I reproduce this: 7.84 × 0.1075 / 0.006² ≈ 23,400.
   - A Phase IIc cannot plausibly be that large. I cannot ground its actual size; treat that as an uninformed prior.
   - A Phase IIc survival signal would therefore be a noisy point estimate or a safety check. It would not be a test of whether the effect is 10% versus 3%.
   - It gates whether to fund Phase III. It does not calibrate r.

4. **Study 31 supports the critique's mechanism.**
   - The Advocate concedes that adoption on a non-mortality endpoint "does not support the separate claim that the mortality effect is 10%."
   - If adoption is expected via composite or surrogate endpoints, then success worlds are largely surrogate worlds. That raises f, which is the critique's point.
   - The cheap-generic argument also supports the adoption leg. That leg was never contested. It does nothing for E[r|success].

5. **The unvalued benefits are not a quantified offset.**
   - The Advocate says it "cannot quantify" them.
   - The only non-mortality signals in the evidence package are reduced peripheral neuropathy and the chest X-ray score from an open-label trial. Neither is a valued outcome in the model, and the verifier found no hard-outcome evidence for lung-damage benefit.
   - An unquantified, unmodeled upside does not cancel a specific overstatement in a modeled parameter.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

1. **Conceded.** f = 0.5 and r_s = 0.03 are unsourced, and the Advocate's crossing condition f·(0.10 − r_s) > ~0.033 is correct. This follows from linearity, SROI ≈ 3,000 × E[r]/0.10.

2. **The Advocate's counter-values are equally unsourced, and they conflict with its own concessions.**
   - The Advocate picks f = 0.3 to show fragility.
   - It also concedes (Concession 3) that a Phase III success is "probably not a mortality result." That implies f is above 0.5, not below it.
   - Using the Advocate's own r_s range of 0.03–0.05, and the formula SROI ≈ 30,000 × E[r]:

   | f | r_s | E[r] | SROI |
   |---|---|---|---|
   | 0.7 | 0.04 | 0.058 | ~1,740x |
   | 0.7 | 0.05 | 0.065 | ~1,950x |
   | 0.8 | 0.05 | 0.060 | ~1,800x |
   | 0.9 | 0.05 | 0.055 | ~1,650x |

   - Once f ≥ 0.7, crossing requires only r_s < ~0.053. The Advocate's "straddles the bar" result depends on keeping f at 0.5 or below.

3. **Sample-size calibration.** Conceded that the critique used 4% rather than CG's 6%. The Advocate's ~23,400 per arm still makes the point.

4. **"No TB drug trial approaches this scale."** Conceded as unsourced recollection. The Advocate has not offered a counterexample either, and its own 23,400 per arm figure shows the scale is far beyond what the Advocate itself suggests a Phase III would be.

5. **Nothing supports 10%.**
   - The Advocate is right that "no mortality evidence" is not the same as "effect below 10%."
   - But the verifier's finding is that nothing in human data supports 10%.
   - The 10% is the model's input and the one the SROI multiplies. A parameter with no support and a plausible downward bias to its conditioning event is a legitimate flag even if the correct value is unknown.

6. **Open-label design.** Cultures and chest X-ray scores in an open-label trial with differential muscle pain (16% vs 5%) are more exposed to bias, so f·r_s is plausibly overstated even within the surrogate-only world. The verifier flagged that this affects how much the 97% vs 85% result can be trusted.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: the true conditional distribution is two-sided. A trial powered for a larger effect (20–30%) would declare success only on a large observed effect, so conditional on a mortality-endpoint success the true effect likely exceeds 10%.

1. **Significance does not imply the true effect exceeds the powered effect.**
   - Take a trial powered for 25% at 6% baseline: ~3,460 per arm (7.84 × 0.0994 / 0.015²).
   - If the true effect were 10%, its power would be ~19%. This is z ≈ 0.006/0.00557 ≈ 1.08, and the probability of exceeding 1.96 is P(Z > 0.88).
   - So success is compatible with a true effect of 10% or lower, and significant results are inflated by selection (winner's curse). The observed effect conditional on success overstates the truth.
   - With a prior concentrated on small effects (no human mortality data supports the 10%), the posterior conditional on success is shrunk, not raised.

2. **The 25% figure is unsourced, as the Advocate admits.** It requires a true effect of at least that size, which is further from the evidence than the 10% the critique questions.

3. **Symmetry of ignorance does not equal symmetry of burden.** The Advocate notes that the critique has no evidence for a smaller effect either. The model, however, is the one that fixes a point estimate of 10% that the verifier could not support. The critique's claim is that "success" is a poor guarantor of that figure, not that the truth is 3%.

4. **The "modest haircut" range 0.065–0.080 is the Advocate's choice of f ∈ [0.3, 0.5].** As shown above, this is not the range implied by the Advocate's own concession that success is probably not a mortality result.

5. **Minimum defensible magnitude.** At f = 0.5 and r_s = 0.05, E[r] = 0.075 and SROI ≈ 2,250x. A 25% reduction from the headline is still notable, and it moves the result to within a modest margin of the bar. That minimum depends on the unsourced f and r_s.

**RESPONSE TO "OFFSETTING FACTORS":**

1. **Unvalued benefits (morbidity, post-treatment mortality, transmission).** The offset is real in principle but unquantified (Advocate: "I cannot quantify"). It also assumes surrogate success reflects a genuine host benefit, which is exactly what the open-label surrogate data cannot establish. It is a hypothesis, not a modeled offset.

2. **6% baseline and unascertained deaths.**
   - The 6% is already in the model. It is not an offset to the discount on r.
   - The claim that true mortality is higher than notified-cohort mortality is speculative and unquantified here.
   - Raising the baseline would also raise the sample size needed for a mortality-powered trial only modestly, so it does not rescue the feasibility problem.

3. **Cheap generic, so a lower evidence bar for guidelines.** This supports the 60% uptake link, which the critique does not dispute. It does not bear on E[r|success].

4. **Phase IIc data narrowing uncertainty.** It narrows uncertainty about whether to proceed, but as shown above it cannot calibrate a 10% mortality effect at feasible Phase IIc sizes.

**KEY UNRESOLVED QUESTIONS:**

- How does CG define "success" for the 40%: as P(a real mortality benefit of the assumed magnitude) or as P(regulatory/guideline-grade surrogate or composite win)? This one factual answer decides whether the critique double-counts.
- What is the Phase IIc's size and primary endpoint? Is "survival" a powered outcome or a descriptive one?
- What is f, the share of success worlds that are surrogate or composite wins? The Advocate's concession implies it is above 0.5, but no one has an estimate.
- What is r_s, the true mortality effect conditional on surrogate success? I cannot ground it. TB surrogates such as culture conversion and radiographic score are not validated mortality predictors in the evidence package.
- Are p_success and the effect size correlated, as the parameter map flags? A positive correlation would change the expected product relative to the independent treatment.

### Judge Audit
Surviving strength: moderate
Justification: The Challenger made grounded moves the Advocate could not answer: p_success cannot absorb a conditional-effect discount, the Phase IIc cannot calibrate mortality, and the winner's-curse refutation holds. The Advocate itself conceded that the 10% is unsupported and that a mortality-powered trial is infeasible, so the direction of the critique survives. The magnitude does not survive in any grounded form. Both sides' f/r_s ranges are unsourced. The Challenger's f > 0.5 derivation has a logical gap, and the Advocate never made its best defense: that the 10% may already be a surrogate-to-mortality translation, i.e. r_s ≈ 0.10.
Recommended action: 1. CONCLUDE NOW: With moderate-high confidence, flag the 10% relative mortality reduction as an unsupported input with a plausible downward bias. Phase III success will almost certainly rest on non-mortality endpoints, and no human mortality data supports 10%. Report SROI as conditional on the crossing condition f·(0.10 − r_s) < 0.033 rather than as a point estimate. State that the headline ~3,000x falls to ~2,000x or below only if a substantial share of success worlds carry a true effect well under 0.10. That share is currently ungrounded, so the quantitative claim that SROI drops below the bar does not survive.

Two items should be resolved before any downward revision:
- Ask CG (a single, feasible query) whether the 10% was meant as the mortality effect expected *given* a surrogate/composite success. If yes, the critique reduces to "the surrogate-to-mortality translation is unjustified" and the f-mixture should not be applied on top.
- Drop the Phillips/Wallis claim unless it is separately verified.
Action feasibility: actionable_now
Advocate failures: ["sound_synthesis_noted: The crossing condition f·(0.10 − r_s) > ~0.033 follows correctly from SROI being linear in E[r|success]. The recomputed sample size of ~23,400 per arm at CG's 6% baseline is also correct (7.84 × 0.1075 / 0.006² ≈ 23,400). Both are grounded and moved the debate forward.", 'unsupported_estimate_pseudo: Magnitude Challenge 3 argues that a trial "powered for a larger effect, say 20–30% relative (I cannot source a figure)" would declare success only if the true effect were large, so "conditional on a mortality-endpoint success, the true effect would then likely exceed 10%." The conclusion does not follow. Significance in an under-powered trial is compatible with a smaller true effect, and it inflates the observed effect (winner\'s curse). The Challenger correctly took this apart.', 'call_to_ignorance: Magnitude Challenge 2 says "the mortality effect could be larger than 10% in worlds where surrogates improve strongly… the critique has no evidence for the other direction either." This uses the absence of evidence to posit upside. The correct move was to accept that 10% is ungrounded in both directions.', 'unsupported_estimate_counter: Magnitude Challenge 4 calls "f between 0.3 and 0.5 and r_s between 0.03 and 0.05" a "defensible conservative adjustment," but these ranges have no more grounding than the critic\'s. The f range also sits awkwardly with the Advocate\'s own Concession 3, which says Phase III success is "probably not a mortality result.', 'false_definitiveness: The Advocate asserts "A defensible conservative adjustment is a modest haircut, not a 50% cut" while also conceding that "the size of the discount is unresolved.', 'misrepresenting_evidence_status: Existing Coverage 3 and Offsetting Factor 4 present the Phase IIc as testing "survival," and say it means CG "expects to learn something about survival." The verifier package says the STEP Phase IIC (n=440) lists culture conversion, chest X-ray score and lung function as outcomes, with mortality not primary. The Advocate overstated what the trial is designed to show.']
Challenger failures: ['sound_synthesis_noted: The winner\'s-curse rebuttal is correctly computed. A trial at ~3,460 per arm, powered for 25% at 6% baseline, has ~19% power for a true 10% effect (SE ≈ 0.00557, z ≈ 1.08). This validly refutes the Advocate\'s "success implies larger effect" argument. The argument that p_success cannot absorb a discount on E[r|success] is also logically sound.', 'unsupported_estimate_pseudo: The table with f = 0.7–0.9 is derived from the Advocate\'s concession that success is "probably not a mortality result." That concession concerns the *endpoint type*. The critique\'s f is the share of success worlds in which the *true mortality effect* is r_s rather than 0.10. A success measured on a non-mortality endpoint does not entail a lower true mortality effect. The inference from P(non-mortality endpoint) > 0.5 to f > 0.5 has a clear logical gap, and the specific values 0.7, 0.8 and 0.9 are chosen rather than derived.', 'strawmanning: The Challenger says Study 31 "supports the critique\'s mechanism… success worlds are largely surrogate worlds." Study 31\'s endpoint was TB disease-free survival at 12 months, a clinical outcome rather than a culture or radiographic surrogate. The response treats it as surrogate-only, which is a category swap.', 'strawmanning: The Advocate\'s Offsetting Factor 2 said a higher true baseline mortality raises the absolute benefit. The Challenger responded on trial feasibility instead: "would also raise the sample size needed… only modestly." That claim is also wrong in direction. A higher baseline *reduces* the required sample size for a fixed relative effect.', 'misrepresenting_evidence_status: On the Phase IIc, the Challenger writes "I cannot ground its actual size; treat that as an uninformed prior." The verifier package reports STEP at 440 patients with non-mortality outcomes. The conclusion (it cannot calibrate a 10% mortality effect) is correct and in fact stronger with that evidence, but the Challenger misstated what the evidence base contains.', 'unsupported_estimate_fabricated (minor): With a prior concentrated on small effects… the posterior conditional on success is shrunk." The prior\'s shape is asserted without grounding, though the qualitative winner\'s-curse point stands without it.']
Debate resolved: The debate established several points:
- No human mortality evidence supports the 10% relative reduction.
- A mortality-powered Phase III is infeasible (~17,000–73,000 per arm, ~23,400 at CG's 6% baseline), so a Phase III "success" is very likely a non-mortality-endpoint result.
- The Advocate's argument that success implies a *larger* effect fails on winner's-curse grounds.
- SROI falls below 2,000x if and only if f·(0.10 − r_s) exceeds ~0.033.
Debate unresolved: Three questions remain open:
- How CG defines "success" for the 40%.
- Whether the 10% was already intended as the mortality translation of a surrogate success. If it was, the mixture double-counts.
- The values of f and r_s. Both sides traded ungrounded ranges, and the Challenger's push to f ≥ 0.7 rests on conflating endpoint type with true-effect world.

--- Critique: A large share of on-treatment deaths is unreachable by a weeks-scale host-directed adjunct, and shorter regimens shrink the headroom further ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: A large share of on-treatment deaths is unreachable by a weeks-scale host-directed adjunct, and shorter regimens shrink the headroom further

EXISTING COVERAGE:
- The parameter map confirms CG does not model "unreachable deaths" by name. I do not claim it does.
- The 10% is a population-level relative reduction in all-cause on-treatment mortality among treated drug-susceptible patients (6% baseline → 5.4%). It is not a claim that every death is equally modifiable.
  - The decomposition r_eff = reachable fraction × effect among reachable is an algebraic re-expression of the same parameter.
  - If the 10% was meant as a net figure, it already embeds a reachable share. For example, a 14% effect on a 70% reachable share gives 10%.
  - CG gives no derivation either way. The critique therefore shows the 10% is unexplained, not that it is too high.
- The 10% is conditional on success. The expected relative reduction is already discounted to 4% by the 40% p_success.
- The Phase IIc is explicitly testing "dosing strategies for survival, infection clearance and lung damage." Mortality effect size is an open question the grant is designed to resolve, not something CG treats as settled.
- The BOTEC values only on-treatment mortality. Morbidity (lung damage), post-treatment mortality, transmission and diagnostic value are implicit zeros (parameter map). Any unreachable-death haircut is therefore applied to a benefit stack that is deliberately incomplete.

EVIDENCE WEAKNESSES:
- The critique's own hypothesis says the 25–35% unreachable figure is UNGROUNDED. The mechanism and materiality conclusions rest entirely on that number.
- The only empirical anchor offered is a 1.8–33.3% range. That range is wide enough to include a haircut well below the materiality threshold.
  - At 1.8%, r_eff ≈ 0.098 and SROI ≈ 2,950x.
  - At 33.3%, r_eff ≈ 0.067 and SROI ≈ 2,000x.
  - A range that spans "negligible" to "borderline" does not establish a decision-relevant effect.
  - I cannot ground which end applies to the CG target population. The critique cannot either.
- The Sensitivity Results are empty ({}). No quantification was run, so "notable" materiality is asserted rather than shown.
- The claim that early deaths are "often tied to advanced HIV, comorbidity and non-TB causes" is plausible but is not tied to a specific cohort in the critique.
  - Whether those deaths are unreachable is a separate question from whether they occur.
  - Advanced HIV with TB involves immunopathology and inflammatory complications, which are exactly the targets of host-directed therapy.
- The inference from "2-month and 16-week atorvastatin courses overlap the early-death period only partly" to "the adjunct can't reach early deaths" is not supported.
  - A statin begun at treatment initiation overlaps weeks 0–8 almost entirely. Only the onset-of-effect lag matters, and the critique gives no data on that lag.
- Adjunct host-directed therapy can reduce early mortality in at least one TB setting. Thwaites et al. (NEJM 2004) found adjunctive dexamethasone reduced death in TB meningitis (hazard ratio about 0.69 at 9 months).
  - This is not statins, and it is a different disease form, so it is only an existence proof.
  - A counterexample is the IMPI trial (Mayosi et al., NEJM 2014), where prednisolone in TB pericarditis showed no mortality benefit. Evidence is mixed, and I lean toward "reachability is uncertain, not systematically low" because the mechanism is anti-inflammatory and early deaths often involve inflammatory complications.

MAGNITUDE CHALLENGE:
- SROI is linear in relative_reduction. Using 3,000x as the base:
  - A 25% haircut (r = 0.075) gives ≈ 2,250x. This is above the 2,000x bar.
  - A 35% haircut (r = 0.065) gives ≈ 1,950x. This is about 2.5% below the bar.
  - Only the far end of an ungrounded range crosses the bar, and only marginally.
- The haircut is applied to a parameter already assumed rather than derived. Because the 10% is unanchored, a neutral prior is symmetric: it could be 5% or 15%. The critique argues only for the downward side.
- The 10% may even be conservative conditional on success.
  - Derivation: detecting 6% → 5.4% mortality at 80% power and 5% two-sided alpha needs n ≈ 7.84 × (0.06×0.94 + 0.054×0.946) / (0.006)² ≈ 7.84 × 0.1075 / 0.000036 ≈ 23,000 per arm.
  - A $7M Phase III is very unlikely to enroll that many.
  - If "success" means a statistically significant mortality result in a smaller trial, the observed effect must be substantially larger than 10%. A winner's-curse caveat applies.
  - If instead success is a surrogate (the likelier reading), this argument fails and the mortality effect is unanchored. That is a different critique, about the definition of success.
- The 4-month HPMZ point has no quantification.
  - It would only reduce headroom if baseline mortality on the regimen at adoption falls below 6%.
  - The critique gives no data for that.
  - A 4-month rifapentine–moxifloxacin regimen was shown noninferior to the standard regimen (Dorman et al., NEJM 2021, Study 31/A5349), as I recall it. The adopted regimen mix by the 8-year horizon is unknown.
  - The critique itself says to remove or flag this claim as UNGROUNDED.

OFFSETTING FACTORS:
- Omitted benefit channels all go in the upward direction (parameter map): lung-damage morbidity, post-treatment survival, transmission averted and diagnostic value. Any of these could offset a reachable-share haircut.
- The 27 DALYs per death is described as remaining healthy life expectancy. Because deaths among young adults with HIV are often high-DALY, the DALYs per death averted may not fall even if the pool of reachable deaths shifts toward them. I cannot ground this further.
- The parameter map notes unascertained deaths could raise true baseline mortality above 6%. That would scale the absolute benefit up if the reachable share is a fixed fraction.

OVERALL ASSESSMENT:
Partial defense.
- The direction of the critique is sensible. A uniform 10% across all deaths is an unexplained simplification, and CG has no adjustment for reachability.
- The critique does not meet its burden on magnitude. Its central number is self-declared ungrounded, its sensitivity table is empty, and even its own range puts SROI at 1,950–2,250x for the conditional-on-success case.
- The result straddles the bar only at the pessimistic end. The 10% itself is equally uncertain in both directions.

CONCESSIONS:
- CG gives no derivation of the 10% and no decomposition into reachable and unreachable deaths. The critique is right that this is a transparency gap.
- The 25–35% placeholder should not be cited as evidence. It is a hypothesis.
- The HPMZ headroom argument is ungrounded and should be dropped or flagged, as the critique itself suggests.
- Early-death clustering and the HIV/comorbidity share are plausible reasons to expect the effective reduction to fall below a naive uniform figure. A modest downward revision to the 10% is defensible, but I cannot say how large.
```

### Challenger
REBUTTAL: A large share of on-treatment deaths is unreachable by a weeks-scale host-directed adjunct, and shorter regimens shrink the headroom further

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the 10% is a net population-level figure that could already embed a reachable share (e.g., 14% × 70%), and CG's 40% p_success already discounts it to 4%.

- **Embedding is hypothetical.** The Advocate's own concession is that CG gives no derivation. "It could already embed reachability" is therefore unfalsifiable. A parameter that might embed the adjustment cannot be treated as having made it. The 14% × 70% example is invented to fit the 10%, not drawn from CG's reasoning.
- **p_success discounts a different risk.** It prices the probability that the intervention works at all. The reachability haircut applies to the effect size in the success state.
  - The two factors multiply: 0.4 × 0.10 × reachable share.
  - Discounting for failure does not reduce the overstatement conditional on success. A 30% overstatement of the success-state effect is still a 30% overstatement of the expected value.
- **The "Phase IIc will resolve it" argument does not help.** The BOTEC is the thing being used to justify the grant before that resolution. An effect size that is "an open question" and enters the SROI at a point value of 10% is the transparency gap the Advocate concedes.
- **"Implicit zeros" on morbidity, transmission and diagnostics is not an offset.** It is an argument that the model is conservative elsewhere.
  - That does not tell us whether the mortality parameter is right.
  - The omitted lung-damage channel shares the critique's mechanism. If a shorter regimen shrinks the on-treatment damage burden, it also shrinks the morbidity benefit the Advocate is counting as upside.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the 25–35% figure is self-declared ungrounded, the 1.8–33.3% range spans "negligible" to "borderline," and the sensitivity table is empty.

- **Concessions.**
  - The 25–35% figure is a placeholder.
  - The Sensitivity Results are empty.
  - The critique supplies no cohort-level data on onset-of-effect lag.
- **The Advocate's r_eff computations assume a meaning for the range that the evidence package does not state.**
  - The package says only that "the reachable share depends strongly on setting and HIV prevalence." It does not say 1.8–33.3% is the unreachable fraction.
  - The Advocate's 0.098 and 0.067 figures follow only if it is.
  - If the range measures something else (e.g., proportion of deaths in a specific category), the computed SROI band of 2,000–2,950x is not established.
  - The Advocate has not marked this assumption as an assumption.
- **The range's width is a setting-dependence finding, not evidence of a negligible haircut.** The decision-relevant question is where CG's target population sits. Neither side can ground that. A conditional follows: if the target is a high-HIV-burden setting, the upper end is the relevant one, and there the Advocate's own arithmetic gives about 2,000x, i.e., at the bar.
- **The statin-timing point is partly conceded.**
  - A statin started at initiation does overlap weeks 0–8 in calendar terms. The critique was loose in saying "only partly."
  - The residual is onset of effect. Neither party has data on it, so the Advocate's "almost entirely" is as ungrounded as the critique's "partly."
  - The verifier evidence item itself says the overlap depends on onset of effect.
- **The steroid analogies are weaker than presented.**
  - The Advocate concedes that Thwaites 2004 (TBM) is a different disease form, and that IMPI (Mayosi 2014, TB pericarditis, no mortality benefit) points the other way.
  - From memory, and hedged, the ACT HIV trial (Donovan et al., NEJM 2023) found no significant survival benefit from dexamethasone in HIV-associated TBM. That is the subgroup most relevant to the "advanced HIV" deaths at issue.
  - The Advocate's own accounting is one positive existence proof in a non-comparable condition against one explicit null. My recalled HIV-TBM null would add a second.
  - Adjunctive anti-inflammatory therapy therefore has a mixed record for mortality in the HIV-advanced population. That supports the critique's direction.
  - I am not claiming these studies measure statins or the on-treatment pulmonary population.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: SROI is linear in r; a 25–35% haircut gives roughly 2,250x to 1,950x, so only the far end crosses the 2,000x bar, and by about 2.5%. The 10% could equally be 5% or 15%. The 10% may even be conservative given the power calculation.

- **The linear arithmetic is correct, and I concede it.**
  - From a 3,000x base, the bar is crossed when r falls to 6.67%, a 33% total haircut.
  - A single reachability haircut at the midpoint of the 1.8–33.3% range (17.55%) gives r ≈ 0.082 and about 2,470x. That is still above the bar.
  - On this one factor alone, materiality depends on the pessimistic tail.
- **The critique's decomposition has a second factor, effect among reachable deaths, that is also below 10% unless the 10% was already net.**
  - The Advocate's "10% could be 14% × 70%" defense requires a 14% effect among reachable deaths. That is a larger biological effect than the net figure CG chose.
  - Either the 10% is net, so there is no embedded headroom and the reachability haircut compounds with any shortfall in effect, or it is gross and overstated. The Advocate cannot have it both ways.
  - The critique's own gap is that the second factor is not quantified. That limits the claim to "small-to-medium," which the critique already says.
- **The symmetric-prior argument is not neutral.**
  - Reachable fraction is a structural ceiling. Moving to 15% requires a biological effect among reachable deaths of at least 15% ÷ reachable share.
  - The mortality record for adjunctive host-directed therapy in TB is mixed to null (IMPI; ACT HIV per my hedged recall). The upper tail is therefore thinner than the lower tail.
  - I cannot ground a quantitative asymmetry. This is a structural argument, not a numerical one.
- **The Advocate's power calculation is arithmetically right but works against CG.**
  - 7.84 × 0.1075 ÷ 0.000036 ≈ 23,400 per arm checks out.
  - The Advocate concedes that success is more likely a surrogate. In that case the 10% mortality effect is not anchored by any powered mortality result.
  - That strengthens the critique's central point that the 10% is not derived from evidence on reachable deaths.
- **The HPMZ point is dropped.** The critique itself says to flag it as UNGROUNDED. The Advocate's Dorman 2021 citation is correct about noninferiority but does not address whether CG's model uses a 4-month regimen. That is a model-structure question, not an evidence one.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: omitted benefit channels, high DALYs per death among young HIV-positive adults, and under-ascertained baseline mortality all push upward.

- **Omitted channels are real but not in the model.**
  - Two errors in opposite directions do not validate the point estimate.
  - The Advocate cannot quantify any of them. The Advocate says "I cannot ground this further" on DALYs. The offsets are therefore as speculative as the haircut.
- **Omitted channels are correlated with the reachability concern.**
  - Post-treatment survival and transmission benefits flow through the same pathophysiology (bacterial clearance, lung damage) that the critique says is the only reachable portion.
  - If early deaths are driven by advanced HIV and comorbidity, the adjunct plausibly offers less on those channels too.
- **The DALY argument cuts both ways.** If reachable deaths shift toward younger, high-DALY patients, the pool is also smaller. The Advocate does not show the net direction.
- **Higher true baseline mortality scales the absolute benefit only if the reachable fraction is fixed.**
  - Unascertained deaths (loss to follow-up, deaths outside facilities) are likelier to be unreachable still. They tend to be sicker, late-presenting or post-discharge.
  - That would lower reachability, so the offset may shrink as it grows.

**KEY UNRESOLVED QUESTIONS:**
- What does the 1.8–33.3% range measure? If it is not the unreachable fraction, the Advocate's 2,000–2,950x band is not established.
- How was CG's 10% derived: from a mortality signal, a surrogate such as culture conversion or lung damage, or judgment? Without this, the "already net" and "gross but overstated" readings cannot be separated.
- What is the onset-of-effect lag for atorvastatin relative to the peak early-death window (first weeks)? The overlap argument is unresolved in both directions.
- Does CG's model assume a 4-month or 6-month regimen at adoption? The HPMZ headroom issue stands or falls on this.
- Is the target population high-HIV-burden? If so, the upper end of the reachability range applies, and the combined haircut with a lower effect among reachable deaths could reach the 33% threshold.

### Judge Audit
Surviving strength: moderate
Justification: - Both sides did real analytical work. The SROI arithmetic and the power calculation are sound and were mutually verified. The Challenger's point that p_success and reachability multiply rather than substitute is correct, and so is its structural argument that the reachable fraction caps the upside.
- The critique's quantitative materiality claim did not survive. The Challenger conceded that a midpoint haircut leaves SROI at about 2,470x, above the bar, and that the second factor (effect among reachable deaths) is unquantified.
- What survives is a directionally valid, small-magnitude concern plus a transparency gap. This is consistent with the critique's own "small-to-medium" self-rating, toward the small end.
- Both sides used speculative offsets, and the Challenger's net/gross dilemma was flawed. These failures temper confidence but did not dominate the exchange.
Recommended action: 1. CONCLUDE NOW (moderate confidence): The critique's direction is valid. A uniform 10% relative reduction across all on-treatment deaths is underived and probably does not account for deaths beyond an adjunct's reach. The quantitative claim that this crosses the materiality bar does not survive the debate: only a haircut of about 33% or more flips the decision. CG should take three steps:
   - Flag the 10% as an assumption with no stated derivation.
   - Add a reachability sensitivity row covering about 0–35% unreachable, with SROI of about 3,000x→1,950x.
   - Drop the HPMZ claim.

   Two cheap follow-ups could sharpen this:
   - Ask CG whether the 10% was derived from a mortality signal, a surrogate, or judgment. This resolves the net-versus-gross question.
   - Have the verifier identify the source and definition of the 1.8–33.3% range.

   Both are feasible with existing tooling. Neither is required to act on the conclusion above.
Action feasibility: actionable_now
Advocate failures: ['unsupported_estimate_pseudo: The Advocate computes "At 1.8%, r_eff ≈ 0.098 and SROI ≈ 2,950x. At 33.3%, r_eff ≈ 0.067 and SROI ≈ 2,000x." This treats the verifier\'s 1.8–33.3% range as the unreachable fraction of deaths without flagging that as an assumption. The verifier only says the range "shows that the reachable share depends strongly on setting." Reading the range as directly comparable to the 25–35% figure is a defensible interpretation, and the arithmetic itself is correct. But the Advocate then concludes that the range "spans negligible to borderline" without marking the interpretive step, and the Challenger rightly caught this.', 'unsupported_estimate_counter: Because the 10% is unanchored, a neutral prior is symmetric: it could be 5% or 15%." This symmetric band is offered to neutralize the critique\'s downward argument, but it has no grounding. The Challenger\'s structural point stands: a reachable-fraction ceiling plus a mixed adjunct-mortality record make the upper tail thinner. The Advocate gave no reason to expect symmetry.', 'call_to_ignorance: Under Offsetting Factors, the Advocate says "Any of these could offset a reachable-share haircut." The same applies to the claim that unascertained deaths "could raise true baseline mortality." These are unquantified channels presented as counterweights. The Advocate admits "I cannot ground this further" on DALYs.', "sound_synthesis_noted: Two pieces of the Advocate's analysis are sound:"]
Challenger failures: ['strawmanning: Either the 10% is net, so there is no embedded headroom and the reachability haircut compounds with any shortfall in effect, or it is gross and overstated. The Advocate cannot have it both ways.', 'unsupported_estimate_pseudo: The Challenger objects that the Advocate wrongly assumes the 1.8–33.3% range is the unreachable fraction. Two paragraphs later, the Challenger uses the same range in that same way: "midpoint of the 1.8–33.3% range (17.55%) gives r ≈ 0.082" and "if the target is a high-HIV-burden setting, the upper end is the relevant one." The Challenger applies its own objection inconsistently.', 'call_to_ignorance: Unascertained deaths … are likelier to be unreachable still. They tend to be sicker, late-presenting or post-discharge." The same applies to "If early deaths are driven by advanced HIV and comorbidity, the adjunct plausibly offers less on those channels too." These are speculative claims with no evidence, offered to neutralize the Advocate\'s offsets. They mirror the Advocate\'s own call to ignorance.', 'call_to_ignorance: If a shorter regimen shrinks the on-treatment damage burden, it also shrinks the morbidity benefit." This leans on the HPMZ premise that the Challenger itself drops later as ungrounded and not in the registered regimens.', 'unsupported_estimate_fabricated: A 30% overstatement of the success-state effect is still a 30% overstatement of the expected value." This is illustrative, but the 30% figure has no source and implicitly carries the ungrounded 25–35% placeholder back in. The underlying point is correct: p_success and the reachability haircut multiply, so discounting for failure does not fix an overstated success-state effect.']
Debate resolved: Both sides agree on four points:
- The 25–35% unreachable figure is a placeholder.
- The HPMZ headroom argument should be dropped.
- CG's 10% is underived, which is a genuine transparency gap.
- SROI is linear in r, and the 2,000x bar is crossed only at a total haircut of about 33%.

The debate therefore established that the critique's direction is reasonable. On the reachability factor alone, its materiality depends on the pessimistic tail.
Debate unresolved: Three questions remain open:
- Is the 10% a net figure, with reachability already embedded, or a gross figure, so that a further haircut applies? This depends on how CG derived it, which neither side knows.
- What does the 1.8–33.3% range actually measure, and where does CG's target population sit within it? Both sides used the range as the unreachable fraction while disputing that reading.
- How long is atorvastatin's onset-of-effect lag relative to the early-death window? Both sides acknowledged this is unknown.

--- Critique: Rifampicin induction structurally limits atorvastatin exposure in routine programs, and the trial exposure does not transfer ---

### Advocate
**DEFENSE OF GIVEWELL'S POSITION: Rifampicin induction structurally limits atorvastatin exposure in routine programs**

**EXISTING COVERAGE:**

1. **The signal already comes from atorvastatin under rifampicin.** The Challenger's own revision concedes the Phase IIA/IIB was atorvastatin. The statin-transfer worry (pravastatin or rosuvastatin signals not applying to atorvastatin) therefore does not apply to CG's evidence base. CG's 10% relative reduction is anchored to a signal generated under the interaction.
2. **The Phase IIc is built to resolve this.** The BOTEC says the grant tests "dosing strategies," and the Challenger's evidence shows a registered popPK-PD sub-study (20/40/60 mg, 16 weeks, with exposure correlated to outcomes). The trial is the mitigation. It produces the exposure data the Challenger says is missing.
3. **Exposure shortfall mostly lands in `p_success`, not `relative_reduction`.**
   - The 10% is conditional on a positive result.
   - If rifampicin limits exposure so that no dose works, the trial fails and the 40% joint success probability absorbs that.
   - If a dose works, the Phase III and later guidance specify that dose, so the realized effect is the effect at an exposure the trial showed to be achievable.
   - A further multiplier on `r` after conditioning on success partly double-counts.

**EVIDENCE WEAKNESSES:**

1. **The Challenger admits the central quantity is ungrounded.** Net chronic-dosing exposure at the site of action is labelled UNGROUNDED, and the hepatocyte effect is "unknown" per the label.
2. **The AUC findings are short-term and plasma-based.** The 80% cut (separated dosing) and the preserved-or-raised AUC (simultaneous dosing) are 7-day plasma measurements. The Challenger itself says these do not establish lung-lesion exposure. Plasma AUC under induction is a weak proxy for the effect CG is betting on.
3. **The direction of the bias is unresolved.** On the Challenger's own account, simultaneous dosing preserves or raises AUC, so the interaction does not unambiguously reduce exposure. A "structural limit" is not established.
4. **The dose-response assumption is speculative.** The Challenger says "steep (unknown)." If the response saturates, halving exposure costs little. The mechanism claim needs a steep response, and nothing in the evidence shows one.
5. **The rifapentine point is unverified.**
   - The Challenger says it "did not verify" the rifapentine–atorvastatin interaction.
   - Arguendo, if a Phase III used an HPMZ-type regimen, the rifampicin-specific guidance would not map directly.
   - That cuts both ways: the interaction could be larger or smaller.
   - The BOTEC assumes standard drug-susceptible treatment. Whether Phase III uses a rifapentine regimen is itself speculation.
6. **The trial-to-routine transfer concern is generic.** Dosing timing and adherence differences between trial and routine care apply to nearly any adjunct drug. The Challenger identifies no mechanism specific to atorvastatin and rifampicin that makes the gap larger than usual.

**MAGNITUDE CHALLENGE:**

1. The 0.5–0.8 multiplier is self-described as "my guess, not derived from data." It has no derivation chain, so it cannot be treated as an estimate.
2. The Challenger gives no sensitivity results. Mechanically, a multiplier on `r` scales SROI linearly. Starting from ~3,000x, that gives 0.5 → ~1,500x and 0.8 → ~2,400x.
3. Only multipliers below about 0.67 (2,000/3,000) would cross CG's bar. So the guess range straddles the bar, and the conclusion depends on an ungrounded number.
4. The multiplier is plausibly smaller for the following reasons.
   - Because the Phase IIc includes a 60 mg arm, dose escalation can offset induction.
   - Because the Phase IIA/IIB signal was observed under rifampicin, part of any exposure penalty is already embedded in the 10%.
   - Only the incremental gap between trial and routine conditions is a candidate adjustment. The Challenger frames the penalty as relative to the label-level interaction, which overstates the increment.

**OFFSETTING FACTORS:**

1. **Zero-valued benefit channels.** The model values only on-treatment mortality. Morbidity DALYs, post-treatment mortality, transmission averted and diagnostic value are all implicit zeros (CEA Parameter Map). Any plausible positive value from these could offset a modest haircut to `r`. This does not show the net is positive, only that the BOTEC is not one-sided.
2. **Dose scaling.** Atorvastatin is cheap and generic, so a higher dose to counter induction costs little. This differs from drugs where compensating for induction is prohibitive.
3. **Conservatism of the 10% figure.** A 10% relative reduction is modest. I cannot ground whether it is conservative relative to the Phase IIA/IIB effect, because the report gives no derivation. I do not rely on this point.

**OVERALL ASSESSMENT:** **Partial defense.**

- The statin-transfer half of the critique is substantially neutralized by the Challenger's own correction.
- The exposure-in-routine-care half is real but unquantified, is partly handled by `p_success` and the dosing design of the trial, and rests on an admitted guess.
- The materiality is conditional. It matters only if the multiplier falls below ~0.67.

**CONCESSIONS:**

1. The CEA Parameter Map confirms CG has no explicit treatment of rifampicin-induced exposure reduction, so this is an unaddressed topic, not merely an unnamed one.
2. The 10% figure has no stated derivation, so I cannot show it is already net of exposure effects. I can only argue it plausibly is, given the signal came from rifampicin-treated patients.
3. Routine-program dosing timing and adherence could differ from trial conditions in ways the Phase IIc will not fully reveal. The popPK-PD sub-study helps with exposure but not with real-world adherence or timing.
4. ART interactions are not addressed in the BOTEC. I have no defense beyond noting that the Challenger has not quantified them either.
5. If the true multiplier were in the lower part of the Challenger's range, the estimate could drop below the bar. I cannot rule that out, but neither can the Challenger rule it in.

### Challenger
REBUTTAL: Rifampicin induction structurally limits atorvastatin exposure in routine programs

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: because the Phase IIA/IIB signal came from atorvastatin given with rifampicin, the statin-transfer concern is neutralized and CG's 10% is already anchored to the interaction.

- **Conceded.** The "different statin" half of the original critique is substantially defused, and the critique itself retracted it.
- **Tension within the Advocate's own defense.** Concession 2 admits the 10% has no stated derivation, so the Advocate cannot show it is net of exposure effects. "Plausibly embedded" is an inference, not coverage.
- **What the signal covers.** It was generated under trial conditions: supervised dosing and a trial-chosen timing relative to rifampicin. The residual concern is whether routine programs reproduce those conditions. That is a transfer from trial to routine for the same drug, and the Phase IIA/IIB signal says nothing about it.

> The Advocate claims: the Phase IIc, with its popPK-PD sub-study, is the mitigation because it produces the missing exposure data.

- **Timing.** The sub-study resolves the question after the funding decision. The BOTEC's `r` is applied now, as if exposure were settled. The registry says PK-PD correlation "will be essential," which shows the investigators treat exposure as open. That supports the critique.
- **Internal inconsistency.** In Evidence Weakness 2 the Advocate calls plasma AUC "a weak proxy" for lung-lesion exposure. A plasma popPK sub-study cannot then close the lung/hepatocyte gap. Either plasma exposure is informative, which makes the sub-study useful and the critique's unknown smaller, or it is weak, in which case the sub-study does not resolve the gap.
- **Scope.** The Advocate concedes (Concession 3) that the sub-study does not capture real-world adherence or timing. Those are the residual risk.

> The Advocate claims: exposure shortfall lands in `p_success`, so a further multiplier on `r` double-counts.

- **Partly valid.** If no dose works, the failure is absorbed in `p_success`. I accept that for the "no dose works" branch.
- **The gap.** `p_success` is a probability of trial success. `r` is the effect size in routine delivery after success. A trial can succeed at a supervised, timing-controlled, possibly 60 mg exposure, while routine delivery yields lower exposure. That is a trial-to-routine wedge in `r`, not a trial-failure event, so `p_success` does not capture it.
- **Unshown claim.** The double-counting claim assumes the 40% was constructed to include exposure risk. The Advocate shows no derivation of the 40% either, so this is asserted rather than demonstrated.
- **Dose specification.** The Advocate says the Phase III "specifies that dose" and so the effect is realized at an exposure the trial showed to be achievable. That shows achievability under trial supervision. It does not show routine delivery of that exposure, which is the critique's residual claim.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the central quantity is admitted UNGROUNDED, and the AUC findings are short-term plasma measurements.

- **Not a defense of the point estimate.** "Ungrounded" means the model's `r` is unconstrained in the downward direction. It does not mean the risk is zero. A point estimate with no exposure adjustment embeds an implicit multiplier of 1.0, which is also ungrounded.
- **The 7-day plasma finding is still informative about timing sensitivity.** The critique cites an ~80% AUC drop with separated dosing versus preserved or raised AUC with simultaneous dosing. The label recommends simultaneous coadministration. The point is not that the direction is ambiguous. Exposure depends strongly on a dosing-schedule variable that a trial controls and routine programs may not.

> The Advocate claims: the direction of bias is unresolved, so no "structural limit" is established.

- **Partially accepted.** The word "structural" overreaches, and the critique itself downgraded to medium strength.
- **Residual.** The interaction is dosing-timing-dependent. Routine programs, with fixed-dose rifampicin combinations and variable adherence, may not hold the favorable timing. That is a risk, not a certainty.

> The Advocate claims: the dose-response assumption is speculative, since saturation would make halving exposure cheap.

- **Symmetric uncertainty.** Nothing shows saturation either. The registered design tests three doses (20/40/60 mg) and correlates PK-PD with outcomes. If the investigators expected a flat response, that design would be unnecessary. This is an inference about their expectations, not direct evidence of steepness.
- **Conditional framing.** If the response is not saturated at the exposures achieved under induction, the haircut applies. If it is saturated, it does not. The model currently assumes the second case without support.

> The Advocate claims: the rifapentine point is unverified, and it cuts both ways.

- **Verification status.** The verifier marked the rifapentine–atorvastatin interaction as not verified. That is UNVERIFIABLE, not REJECTED. The verifier did confirm that rifapentine is a CYP3A4 inducer.
- **Direction.** "Cuts both ways" needs rifapentine to induce less than rifampicin. I cannot ground that. The one verified fact, that it is a CYP3A4 inducer, points toward the same sign of interaction.
- **Agreed.** Whether a Phase III uses a rifapentine regimen is speculation. I treat this as a minor point.

> The Advocate claims: trial-to-routine transfer is generic to any adjunct drug.

- **Not generic here.** For most adjuncts, exposure does not depend on a dosing-schedule variable relative to a co-administered inducer. The atorvastatin–rifampicin timing dependence, with an ~80% AUC change from timing alone per the critique's cited findings, is a drug-pair-specific mechanism.
- **Open ART interactions.** The Advocate concedes ART interactions are unaddressed and notes only that the critique did not quantify them. That does not defend the BOTEC.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

- **Conceded.** The 0.5–0.8 range is an admitted guess and cannot be treated as an estimate.
- **The Advocate's arithmetic is right as a mechanical matter.** The break-even multiplier is about 0.67 (2,000/3,000), taking the Advocate's ~3,000x baseline as given.
- **The guess range straddles the bar rather than sitting above it.** The midpoint is (0.5 + 0.8)/2 = 0.65, just below 0.67. If the multiplier were uniform over the guess range, the share below 0.667 would be (0.667 − 0.5)/0.3 ≈ 56%. I label this illustrative: it inherits the guess's lack of grounding and only shows that the guess range does not clearly favor staying above the bar.
- **The Advocate's reasons for a smaller multiplier are not established.**
  - *60 mg arm offsets induction:* the 60 mg arm is a trial arm. Nothing shows routine programs would use it or tolerate it. The dose-response relationship that makes escalation helpful is the same one the Advocate calls speculative.
  - *Signal embedded under rifampicin:* this is the unshown inference addressed above.
- **Floor.** I cannot ground a minimum multiplier. The honest statement is that the downside is unbounded by evidence in the file, and an ungrounded 1.0 is as unsupported as an ungrounded 0.65.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: zero-valued benefit channels (morbidity, post-treatment mortality, transmission, diagnostic value) offset a modest haircut to `r`.

- **The Advocate concedes this does not show net positive.**
- **Offsets are correlated with the haircut.** Morbidity and transmission benefits would also depend on adequate statin exposure at the site of action. If exposure is limited, those channels shrink along with `r`. They are not independent cushions.
- **Nothing in the file grounds those channels as positive and sizable.** They are unquantified upside, while the haircut is an unquantified downside. That makes the BOTEC uncertain, not offset.

> The Advocate claims: dose scaling is cheap because atorvastatin is generic.

- **Cost is not the binding constraint.** Whether escalation to 60 mg offsets induction depends on monotonic exposure-response and on tolerability within a rifampicin-containing regimen. I cannot ground tolerability from the evidence package. The Phase IIc arms exist to test it, which again shows it is not yet known.

**KEY UNRESOLVED QUESTIONS:**

- Does the 10% `r` reflect atorvastatin exposure under the Phase IIA/IIB dosing timing, and would routine delivery reproduce that timing and adherence?
- Is the 40% joint success probability constructed to include exposure failure, or is it generic trial-success risk? Without this, the double-counting claim cannot be checked.
- Is the atorvastatin exposure–response relationship steep or saturating at the exposures achievable under rifampicin induction? The popPK-PD sub-study may answer this for plasma, but not necessarily for lung lesions.
- Does the sub-study's plasma PK-PD correlate with lung or lesion-site effect, given that the Advocate treats plasma as a weak proxy?
- What is the atorvastatin interaction with rifapentine, and with ART regimens in co-infected patients? Both are UNVERIFIABLE in the current evidence, not rejected.

### Judge Audit
Surviving strength: moderate
Justification: - **Challenger's grounded moves.** The Challenger made three arguments the Advocate's defense did not adequately answer:
  - the `p_success`/`r` wedge distinction;
  - the drug-pair-specific timing dependence, which rebuts "generic";
  - the plasma-proxy inconsistency in the Advocate's defense.
- **Advocate's grounded moves.** The Advocate neutralized the statin-transfer premise and the "structural" framing. It also supplied a sound break-even calculation showing materiality hinges on a multiplier below ~0.67.
- **Limits of the surviving critique.** Its empirical core, that routine timing drifts from the favorable condition, has no supporting evidence. Its magnitude rests entirely on a guess. The Challenger leaned on call-to-ignorance and a false 1.0-vs-0.65 equivalence to keep the downside alive.
- **Verdict.** The concern survives as a real but unquantified qualitative risk. It does not justify a numerical adjustment.
Recommended action: SPECIFIC INVESTIGATION, with an interim conclusion.

**Conclude now:** Do not apply a quantitative haircut to `r` on the basis of this critique. Record rifampicin dosing-timing dependence and ART interactions (especially protease inhibitors, given the 9.4-fold AUC rise with tipranavir/ritonavir) as unmodeled risks to the 10% figure. Confidence is moderate.

**Evidence that would change the answer:**
1. **Phase IIA/IIB dosing schedule.** Pull the ATORTUB Phase IIA/IIB protocol or publication to determine:
   - the atorvastatin dosing time relative to rifampicin;
   - whether dosing was directly observed.

   If dosing was simultaneous and unsupervised, the trial-to-routine wedge is small. This is feasible with existing search tooling.
2. **CG's parameter derivations.** Ask CG, or check the report, how the 40% `p_success` and the 10% `r` were derived. This determines whether exposure risk is already priced in. It is feasible as a direct query.
3. **Chronic co-administration PK.** Run targeted verifier searches for atorvastatin PK under more than 2 weeks of simultaneous rifampicin co-administration, to resolve the conflicting reviews on chronic AUC. This is feasible, though the data may not exist. One review states it was never investigated.
4. **Post-trial exposure data.** Flag the ATORTUB popPK-PD sub-study results as the decisive input once available, noting they address plasma exposure rather than lesion-site exposure.
Action feasibility: requires_specified_evidence
Advocate failures: ['sound_synthesis_noted: a multiplier on `r` scales SROI linearly. Starting from ~3,000x, that gives 0.5 → ~1,500x and 0.8 → ~2,400x... Only multipliers below about 0.67 (2,000/3,000) would cross CG\'s bar." Each step is shown and the arithmetic is mechanical. The ~3,000x baseline comes from the BOTEC, not the verifier package, but the Challenger accepted it. This is legitimate break-even analysis.', 'false_definitiveness: The multiplier is plausibly smaller [i.e., the penalty is smaller]... Because the Phase IIc includes a 60 mg arm, dose escalation can offset induction.', 'strawmanning (mild, internal inconsistency rather than a classic strawman): Evidence Weakness 2 calls plasma AUC "a weak proxy for the effect CG is betting on." Existing Coverage 2 then presents the plasma popPK-PD sub-study as "the mitigation" that "produces the exposure data the Challenger says is missing.', 'misrepresenting_evidence_status (minor): On rifapentine, "That cuts both ways: the interaction could be larger or smaller.']
Challenger failures: ['unsupported_estimate_pseudo: The midpoint is (0.5 + 0.8)/2 = 0.65, just below 0.67. If the multiplier were uniform over the guess range, the share below 0.667 would be... ≈ 56%.', 'whataboutism: A point estimate with no exposure adjustment embeds an implicit multiplier of 1.0, which is also ungrounded." Also: "an ungrounded 1.0 is as unsupported as an ungrounded 0.65.', 'call_to_ignorance: the downside is unbounded by evidence in the file." Also: "Routine programs, with fixed-dose rifampicin combinations and variable adherence, may not hold the favorable timing.', 'misrepresenting_evidence_status (minor): The verifier did confirm that rifapentine is a CYP3A4 inducer." The verifier stated this in passing as background, not as a checked item. This is a modest overstatement of its evidentiary status.', 'sound_synthesis_noted: The `p_success` vs. `r` distinction.', 'sound_synthesis_noted: Offsets are correlated with the haircut. Morbidity and transmission channels would also depend on site-of-action exposure, so they are not independent cushions. This is a valid structural point.']
Debate resolved: The debate eliminated two parts of the critique:
- the statin-transfer half, because the signal came from atorvastatin under rifampicin;
- the claim of a "structural" limit, because simultaneous dosing preserves 7-day plasma AUC.

It also established that `p_success` absorbs the "no dose works" scenario but not a trial-to-routine exposure wedge in `r`. The surviving concern is therefore narrow: routine programs may not reproduce trial dosing timing and adherence, plus unmodeled ART interactions. It carries no grounded magnitude, and the 0.5–0.8 multiplier was conceded by both sides to be a guess.
Debate unresolved: Four questions remain open:
- whether routine programs would actually deviate from same-time dosing, for which neither side offered evidence;
- whether the 10% `r` and 40% `p_success` were constructed to include exposure risk, since neither derivation is available;
- whether atorvastatin exposure-response is steep or saturating under induction;
- whether chronic simultaneous dosing lowers AUC, given the conflicting reviews in the verifier package.

--- Critique: Winner's-curse and reference-class patterns imply the conditional effect should sit well below the surrogate-implied one, and r and p_success should not be independent ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: Winner's-curse and reference-class patterns / r and p_success independence
```

Note: "GiveWell" here means Coefficient Giving (CG).

**EXISTING COVERAGE:**

1. **Independence is not a separate assumption in this BOTEC.**
   - CG's structure is p_success (40%) × benefit given a positive result, with the 10% stated as "conditional on a positive result."
   - A conditional effect multiplied by the probability of the condition is E[r·1{success}]. This is the joint expectation itself.
   - The critique says E[r×p] falls below the product of means in a mixture of "real" and "surrogate-only" worlds. That compares against an *unconditional* mean r, which the BOTEC does not use.
   - Once r is defined as conditional on success, the correlation between r and p is already built into the structure.
   - What remains is whether 10% is the right value of r given success. That is a question about the level of r, not about independence.
   - The critique itself concedes that "the sign of the effect on E[rp] depends on how success is defined." This is consistent with my point.
   - If success means a real mortality benefit, selection into success raises conditional r. That argues against the critique's claimed direction.

2. **The 40% already discounts for much of the "surrogate-only or null world."**
   - Failure of Phase II or III is the null-world outcome. The 40% is applied to the whole benefit stream.
   - The critique's remaining concern is the narrower case where a trial "succeeds" on a surrogate but the true mortality effect is smaller than 10%.
   - The parameter map shows CG does not define "success," so this narrower gap is real. It is not a gap in the whole structure.

3. **The 10% is already modest in relative terms.**
   - It is a 0.6 percentage-point absolute reduction on a 6% baseline.
   - The BOTEC does not extrapolate from a surrogate effect size.
   - I cannot ground a claim that 10% is "conservative" relative to the surrogate effects seen in the prior trial. Treat that as an uninformed prior.

**EVIDENCE WEAKNESSES:**

1. **The shrinkage factor is ungrounded.** The critique labels the 0.7–0.9 range an "illustrative assumption." No cited study yields it, so the magnitude rests on an arbitrary choice.

2. **The winner's-curse mechanism does not fit the critic's own evidence.**
   - Winner's curse requires an effect estimate selected for being positive or significant.
   - The critique concedes that the 10% "likely rests on preclinical and observational anchoring, not a winner's-curse-selected human trial."
   - The critique then argues for a "larger downward adjustment than shrinkage alone," but gives no quantification of it.

3. **The critic's search did not find the human atorvastatin evidence, but CG's premise states it exists.**
   - The critique says atorvastatin evidence "in these results is preclinical."
   - CG's text says a recent Phase IIa/b trial suggested atorvastatin speeds clearance and reduces lung damage on chest X-ray.
   - The verifier did not confirm or refute that trial. If the CG premise is right, the critique's claim that the 10% rests on preclinical and observational data is wrong.
   - I accept arguendo that the search result is accurate and respond to its implications below.

4. **The rosuvastatin null is adjacent evidence.**
   - It is a different drug. Rosuvastatin is hydrophilic and atorvastatin is lipophilic, which could matter for tissue and lung penetration. I cannot ground whether this matters for TB.
   - The cited result is HR 1.30 (95% CI 0.88–1.91, p=0.19), with median time to culture conversion of 42 days in both arms.
   - The interval is wide, so this is an underpowered non-significant result, not evidence of no effect.
   - I cannot confirm from the evidence package which direction HR>1 denotes. If it is the conversion hazard, the point estimate favors rosuvastatin.
   - The PET-CT null is a single null on a single imaging endpoint. It says nothing about atorvastatin.
   - StAT-TB (pravastatin) is "completed" with no results found. That is absence of retrieved data, not a null.

5. **Martineau 2011 is adjacent.** The critic describes it as a post-hoc subgroup signal that did not replicate. It is not a statin study. I do not know if CG's Phase IIa/b signal was post-hoc.

6. **The failed-translation examples were removed.** CC-11050, everolimus and metformin were struck by the critic as "unproven, not refuted." This leaves the reference class thin: one vitamin D-type example plus rosuvastatin.

**MAGNITUDE CHALLENGE:**

1. **Derivation of SROI at the critic's range.**
   - CG baseline: ($54B / $7M) × 0.4 = 7,714 × 0.4 ≈ 3,086x.
   - SROI is linear in r.
   - At 0.9 shrinkage, SROI ≈ 2,777x, a 10% decline.
   - At 0.8, ≈ 2,469x, a 20% decline.
   - At 0.7, ≈ 2,160x, a 30% decline.

2. **Materiality of the critic's own range.**
   - Only the bottom of the critic's range exceeds the ~25% materiality threshold.
   - Even at 0.7, the result stays above the ~2,000x bar.
   - The critic's quantified sensitivity results are empty (`{}`), so the "material" label is not backed by a computed result.

3. **The larger downward adjustment is unquantified.** The claim that the true adjustment is larger than shrinkage alone is directional only. I cannot rebut a number that was not given, but the critique has not met its burden on size.

**OFFSETTING FACTORS:**

1. **CG's formula sets several benefit channels to zero.** Per the parameter map, the formula states "only mortality is valued." Zero-valued channels include:
   - morbidity DALYs, including lung damage on chest X-ray;
   - post-treatment mortality;
   - transmission-averted cases;
   - diagnostic value from the sweat-based workstream.
   Any shrinkage of on-treatment mortality r should be netted against these omitted upsides. The critique does not do this.

2. **Rosuvastatin's null on culture conversion and PET-CT is not an on-treatment mortality null.** Even if surrogate benefits are absent, the mechanism for a mortality effect may be different. I cannot ground this; it is a conditional point only.

3. **CG treats the 40% as covering both Phase II and Phase III.** If human statin data are mostly null, as the critic argues, that is information the 40% should already reflect. The critique does not show that 40% is too high.

**OVERALL ASSESSMENT:** Partial defense.
- The independence sub-critique is largely answered. The BOTEC's conditional structure is the joint expectation, and the critic concedes the sign is ambiguous.
- The winner's-curse sub-critique is weakly supported. The shrinkage factor is ungrounded and the critic admits the mechanism does not match the evidence.
- The point that the 10% is likely too high remains plausible. No derivation of 10% appears in the CG text, and the rosuvastatin data are mildly discouraging for statins in TB generally.

**CONCESSIONS:**

1. CG gives no derivation of the 10% (per the parameter map), and "success" is undefined. A surrogate-driven success followed by a smaller true mortality effect is a real, unmodeled pathway.

2. Directionally, a selected-positive early signal usually overstates the true effect. Some downward adjustment of r is warranted, though the 0.7–0.9 size is not grounded.

3. The rosuvastatin null, even though it involves a different drug and is underpowered, makes the class prior less favorable than the BOTEC's framing implies.

4. The critic is right that "r and p_success independent" is a modeling simplification. It only misleads if r is read as an unconditional effect rather than conditional on success, and CG's text does not define success clearly enough to rule that out.

### Challenger
REBUTTAL: Winner's-curse and reference-class patterns / r and p_success independence

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: because the BOTEC multiplies p_success (40%) by a benefit "conditional on a positive result," it already computes E[r·1{success}], so independence is not a separate assumption and only the level of r is at issue.

- **Conceded:** if r is strictly E[r | success], then p × E[r | success] is the joint expectation and no independence assumption is needed. The "product of means" framing in the critique is weaker than stated, and the critique itself conceded that the sign is ambiguous.
- **The concession moves the problem rather than removing it.** Everything now depends on what "success" means, and the Advocate concedes CG does not define it.
  - If success = a positive surrogate or Phase II/III endpoint (clearance, CXR), then E[r | success] is the mortality effect given a surrogate win. That is the quantity the surrogate-to-outcome gap pushes down.
  - If success = a demonstrated mortality benefit, the Advocate says selection raises conditional r. But selection on a significant result also inflates the *estimated* effect. A 10% anchor taken from a positive result therefore needs shrinkage toward the true effect.
  - The Advocate's "selection raises conditional r" argument holds only under the second definition, which the text doesn't establish.
- **The 40% does not cover the narrower gap.** The Advocate concedes that "surrogate-driven success followed by a smaller true mortality effect is a real, unmodeled pathway." p_success gates whether the benefit stream exists. It says nothing about the size of the stream in the success world.
- **"The 40% should already reflect the human null data" is an assumption.** Nothing in the evidence package says the 40% was set with the rosuvastatin results in view. I cannot ground the opposite either, so the point is unresolved rather than answered.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: winner's curse does not fit because the critic admits the 10% likely rests on preclinical/observational anchoring, and CG's premise says a human atorvastatin Phase IIa/b exists that the critic's search missed.

- **The two Advocate points form a dilemma, and both horns push r down.** The verifier labelled the atorvastatin evidence "preclinical in these results." That is neither REJECTED nor confirmed, so I treat the CG premise as a conditional.
  - *If the human atorvastatin Phase IIa/b exists:* it is a small, early, positive surrogate result (clearance, CXR) in a class where rosuvastatin showed an identical 42-day median culture conversion in both arms (HR 1.30, 0.88–1.91, p=0.19) and no PET-CT effect. That is the textbook winner's-curse setup. The mechanism fits directly, contrary to the Advocate's point 2.
  - *If it does not exist:* the 10% rests on guinea-pig synergy and confounded observational data. That is translation risk plus confounding, which the critique argues warrants a larger adjustment.
  - Either way the 10% needs a haircut. The only open question is its size.
- **The Advocate's objection that the rosuvastatin trial is imprecise cuts against the atorvastatin signal too.**
  - Conceded: a CI of 0.88–1.91 is compatible with benefit, I cannot confirm HR direction, and rosuvastatin is a different drug.
  - A comparably small atorvastatin Phase IIa/b would be equally imprecise. An imprecise positive is exactly what regresses toward the mean.
  - So the width argument does not rescue the 10%. It shows that neither human dataset pins it down.
- **Hydrophilic vs lipophilic.** The Advocate says this could matter and cannot ground it. I cannot ground it either. From general pharmacology, not the evidence package, pravastatin (StAT-TB) is also hydrophilic. The only human statin-in-TB data in the package therefore come from drugs unlike atorvastatin, so they are adjacent, not decisive. Concede that.
- **StAT-TB.** Conceded: "completed, no results found" is absence of retrieved data, not a null. I do not count it.
- **Martineau 2011 and the thin reference class.** Conceded: the class is thin after the removals. A thin class means the shrinkage should come from broader priors, and I cannot ground such a prior from the evidence package. The 0.7–0.9 range stays an illustrative assumption.
- **What does come from the package:** an editorial notes no clear consensus on biomarkers or endpoints for HDT trials. This is general support that surrogate-to-mortality translation is unvalidated in this field.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: SROI is linear in r, so shrinkage of 0.9/0.8/0.7 gives about −10%/−20%/−30% from ~3,086x, only the bottom of the range crosses the ~25% materiality threshold, and the result stays above ~2,000x.

- **Arithmetic conceded.** ($54B/$7M) × 0.4 ≈ 3,086x, and linear scaling gives 2,777x, 2,469x and 2,160x. The empty sensitivity results mean "material" was never computed by the critic.
- **The margin is thinner than the Advocate implies.**
  - Break-even factor to 2,000x: 2,000 / 3,086 ≈ 0.65, i.e. r ≈ 6.5%.
  - That sits just below the critic's 0.7 floor, not far outside it.
- **The critic's own conclusion is that translation risk implies a larger adjustment than shrinkage alone.** Stacking translation risk onto winner's-curse shrinkage makes crossing 0.65 plausible. I cannot ground a specific stacked factor, so this is a break-even, not a point estimate.
- **p_success is not held fixed in the critique's logic.** The human null evidence bears on both r and p.
  - Illustration, not a grounded estimate: r factor 0.8 with p cut from 0.4 to 0.3 gives 0.8 × 0.75 = 0.6 of baseline, ≈ 1,850x.
  - That is below the Advocate's 2,000x bar. The Advocate analyzed r in isolation.
- **Minimum defensible impact:** about −10% to −30% on r alone, which does not flip a decision at the Advocate's bar. The decision-relevant question is whether r and p move together.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: CG values only mortality, zeroing morbidity, post-treatment mortality, transmission and diagnostic value, so downward r should be netted against these upsides; the mortality mechanism might also differ from the surrogates; and the 40% already covers human nulls.

- **The omitted channels are real in the formula but unquantified.** The Advocate gives no magnitude, so there is nothing to net against a −10% to −30% change.
- **Several offsets are correlated with the downside rather than independent of it.**
  - Lung damage on CXR is one of the surrogates at issue.
  - Transmission-averted cases depend on faster clearance, which is the surrogate rosuvastatin did not move (equal 42-day median).
  - If the surrogate signal is overstated, those omitted benefits shrink too. They are not a free cushion.
- **The "different mortality mechanism" point is conditional, and it undercuts the Advocate.** If mortality benefit is decoupled from clearance and CXR, then positive atorvastatin surrogates are also uninformative about mortality. The 10% then has no empirical anchor in either direction. The Advocate cannot use surrogate-null irrelevance to blunt the rosuvastatin result while also relying on the surrogate-positive premise for the 10%.
- **The 40% covering Phase II and III** is addressed above. It is an unverified assumption about how CG set the number.

**KEY UNRESOLVED QUESTIONS:**
- How does CG define "success" for p_success: a surrogate endpoint, a mortality endpoint, or regulatory/deployment approval? The sign and size of the joint-expectation effect depend on it.
- Does the human atorvastatin Phase IIa/b cited in CG's premise exist, and what were its endpoints, sample size and pre-specification? The verifier marked it unverified, not refuted.
- Was the 40% set with the rosuvastatin Phase 2b and PET-CT results in view?
- What is the derivation of the 10%, and is it an effect given a surrogate win or given a mortality win?
- What is the HR direction in the rosuvastatin trial, and what does it imply for the atorvastatin signal?
- Is there a grounded cross-field prior on surrogate-to-mortality translation for host-directed therapy that could replace the ungrounded 0.7–0.9 range?

### Judge Audit
Surviving strength: moderate
Justification: The Challenger made grounded moves the Advocate could not fully answer:
- The definition-of-success dilemma after conceding the joint-expectation point.
- The observation that "selection raises conditional r" ignores selection inflation of the estimate.
- The point that omitted surrogate-linked benefits are correlated with the downside.
These keep the directional claim, that 10% is likely too high, alive. However, the quantitative claim does not survive:
- The 0.7–0.9 factor is admittedly ungrounded.
- On r alone, it does not cross the decision bar.
- The Challenger's only decision-flipping scenario rests on a fabricated p cut and an ungrounded "stacking" argument.
The critique therefore survives as a directional concern of uncertain, probably sub-decisive, magnitude.
Recommended action: 2. SPECIFIC INVESTIGATION, paired with a conclusion for now.

**Conclusion for now:** Apply a directional downward flag to the 10% conditional mortality effect. On r alone, this does not change the decision; SROI stays above ~2,000x unless r falls below ~6.5%.

**Targeted checks:**

(a) **Atorvastatin trial.** Re-run the verifier with targeted searches for the atorvastatin adjunctive TB Phase IIa/b trial that CG cites. Retrieve its sample size, its primary versus post-hoc endpoints (culture clearance, chest X-ray), and its effect sizes and confidence intervals. This determines whether winner's-curse shrinkage applies at all. It is feasible with existing tooling.

(b) **Success definition and the 40%.** Check CG's source text or ask the grant investigators directly:
- whether p_success refers to a surrogate endpoint, a mortality endpoint, or regulatory approval;
- whether the 40% already accounts for the rosuvastatin results.

This is feasible via document review or a direct query.

(c) **StAT-TB results.** Retrieve the pravastatin StAT-TB results if they are published.

If (b) shows that success is surrogate-defined and the 40% predates the rosuvastatin data, revisit a joint r/p adjustment explicitly, avoiding double-counting. Otherwise, close the critique as directionally valid but sub-decisive.
Action feasibility: requires_specified_evidence
Advocate failures: ['sound_synthesis_noted: The SROI derivation was sound. The Advocate computed ($54B / $7M) × 0.4 ≈ 3,086x, noted that SROI is linear in r, and mapped the 0.9 / 0.8 / 0.7 shrinkage factors to 2,777x / 2,469x / 2,160x against a stated ~25% materiality threshold and a ~2,000x bar. Every step is shown and the Challenger accepted it.', 'sound_synthesis_noted: The Advocate\'s structural argument about the joint expectation was valid. It showed that p_success × E[r | success] = E[r·1{success}], so "independence" is not a separate assumption once r is defined as conditional on success. The Challenger explicitly conceded this.', 'call_to_ignorance: The Advocate leaned on unknowns to discount the rosuvastatin null:', 'call_to_ignorance: If human statin data are mostly null… that is information the 40% should already reflect. The critique does not show that 40% is too high." Nothing in the package shows the 40% was set with the rosuvastatin results in view. The Advocate asserts it and shifts the burden onto the critic.', 'misrepresenting_evidence_status: The Advocate wrote, "The critique concedes that the 10% \'likely rests on preclinical and observational anchoring…\'" That statement comes from the verifier\'s synthesis, not from the critique. Attributing it to the critic as an admission that undermines the critic\'s own mechanism overstates its status. This is minor.']
Challenger failures: ["sound_synthesis_noted: The break-even calculation is grounded. 2,000 / 3,086 ≈ 0.65, so r ≈ 6.5%, which sits just below the critic's 0.7 floor. This is an informative reframing of the Advocate's own numbers.", "unsupported_estimate_counter: Illustration, not a grounded estimate: r factor 0.8 with p cut from 0.4 to 0.3 gives… ≈ 1,850x. That is below the Advocate's 2,000x bar.", 'call_to_ignorance: Stacking translation risk onto winner\'s-curse shrinkage makes crossing 0.65 plausible." The Challenger admits it cannot ground a stacked factor, yet still uses the possibility to suggest a decision flip.', 'call_to_ignorance: In the dilemma\'s first horn, the Challenger asserts that a human atorvastatin Phase IIa/b would be "small, early… the textbook winner\'s-curse setup" and "would be equally imprecise." Nothing is known about that trial\'s size, endpoints, or pre-specification; the Challenger itself lists these as unresolved. The horn assumes the trial\'s characteristics rather than knowing them.']
Debate resolved: The independence sub-critique collapses into a question about the level of r and the definition of "success." The "product of means" framing does not survive as stated.

Both sides agree on the following:
- Some downward adjustment to the 10% conditional effect is warranted.
- Applied to r alone, the critic's 0.7–0.9 range lowers SROI by 10–30%, to about 2,160–2,777x.
- That does not cross the ~2,000x bar. Break-even requires a factor of about 0.65, or r ≈ 6.5%.
Debate unresolved: The debate surfaced but did not settle four questions:
- Whether CG's "success" is surrogate-defined. If so, the surrogate-to-mortality gap bites.
- Whether a human atorvastatin Phase IIa/b exists, and with what design. This determines whether winner's-curse shrinkage or translation/confounding risk is the operative mechanism.
- Whether the rosuvastatin null should lower p_success as well as r, without double-counting.
- Whether the 40% was set with that evidence already in view.

--- Critique: Hepatotoxicity and myopathy add a negative tail, and the combined attenuations compound ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION: Hepatotoxicity and myopathy add a negative tail, and the combined attenuations compound

(Funder read as CG. "Cells" are the BOTEC parameters.)

**EXISTING COVERAGE:**

*Harm tail*
- CG's 40% `p_success` is defined as "Phase II and Phase III trials both succeed." A drug with a hepatotoxicity or myopathy signal on top of HRZ would be expected to fail one of those trials. That outcome is already in the 60% failure mass.
- The Challenger's "10% probability of net-zero" is also already covered. A net-zero effect is a failed trial, not a successful one with zero benefit.
- The Challenger's own correction notes the harm tail "may double-count p_success." I agree. The only residual is a harm that is small enough to pass a Phase III yet still net-negative at population scale. That is a narrow slice of the 10% the Challenger uses.
- The BOTEC's benefit is "conditional on a positive result." Adoption only follows a Phase III. A Phase III powered on survival or clearance would also record serious adverse events, so a harm tail large enough to matter would be partly observed before scale-up.

*Compounding*
- The PK attenuation and reachable-fraction factors both operate inside any trial run on standard HRZE. If a Phase III shows a mortality benefit, that observed effect already reflects rifampicin's effect on statin exposure and the share of deaths that adjunctive therapy can reach.
- The 10% relative reduction is an assumed value, not the Phase IIa/b surrogate effect. The parameter map confirms there is "no stated derivation." It is plausibly already a haircut from larger surrogate signals. The Challenger concedes CG's 10% "may already partly embed some attenuation."
- Applying three further multipliers to a figure that may already be net of them risks double-counting.

**EVIDENCE WEAKNESSES:**
- The Challenger labels the magnitude "UNGROUNDED." The three compounding ranges (0.65–0.75, 0.5–0.8, 0.7–0.9) are, in the Challenger's words, "all assumptions, and they overlap." The arithmetic checks out (0.65×0.5×0.7 = 0.23; 0.75×0.8×0.9 = 0.54), but no input is sourced.
- The toxicity evidence is adjacent rather than direct:
  - Pravastatin showing the least toxicity in THP-1 and Vero cells is in-vitro cell-line data. It does not bear directly on human clinical hepatotoxicity.
  - It concerns pravastatin, whereas CG's BOTEC is built on atorvastatin.
  - StAT-TB's choice of pravastatin reflects the programme's own interaction and toxicity concerns. It does not show that toxicity occurred.
- The one clinical safety datum the Challenger cites, the rosuvastatin trial, is described as "mildly reassuring." It points against a material harm tail, even though the trial was underpowered for mortality.
- The ART-myopathy point is conceded as "weak for rifampicin-based regimens."
- I cannot ground a specific rate of statin-associated serious hepatic or muscle injury in TB patients on HRZ. The Challenger has not supplied one either. The −0.01 is a hypothetical (10% × 0.10), not an empirical estimate.

**MAGNITUDE CHALLENGE:**
- The harm-tail adjustment is a −0.01 shift on 0.10, about 10%. That is below CG's ~25% materiality threshold, and the Challenger agrees it is not threshold-crossing alone.
- Reducing it for the p_success overlap pushes it lower. If most of the 10% is already in the 60% failure mass, the residual harm-tail effect on SROI is plausibly low single-digit percent. I cannot ground a tighter number than that.
- The compounded range is where the stakes are. Since SROI is linear in r, 3,000× × (0.23–0.54) ≈ 690×–1,620×, all below the ~2,000× bar. I do not dispute the arithmetic. The range depends entirely on:
  - treating the three factors as independent and fully additive to CG's existing 10%;
  - the Challenger's own caveat that "CG's 10% may already partly embed some attenuation";
  - the Challenger's own caveat that the factors are correlated.
- Correlated factors do not multiply cleanly. If reachable fraction and PK attenuation are both proxies for "less effect than the surrogate suggests," multiplying them overstates the joint shrinkage. The lower bound of 0.23 therefore looks too aggressive.
- Even the Challenger calls the range an "upper-bound illustration" of the downside.

**OFFSETTING FACTORS:**
- The parameter map lists several benefit channels as implicit zeros in the BOTEC: morbidity DALYs (lung damage on chest X-ray), post-treatment mortality, transmission averted, and diagnostic value from the sweat-based test. The formula notes "only mortality is valued."
- Any of these would offset a reduction in on-treatment mortality effect. The parameter map flags that the intervention's main value could be in morbidity and long-term survival, which would "make the estimate robust even if Thread 1 finds a small on-treatment mortality effect."
- To keep SROI at 2,000× against a compounded r of 0.23–0.54× CG's, the omitted channels would need to raise value by roughly 1.2× to 2.9×. I cannot ground that figure from the available material. I flag it only as the size of offset required, not as an estimate that it is met.
- A harm tail and an unmodeled benefit tail are both symmetric omissions. The critique counts only one side.

**OVERALL ASSESSMENT: Partial defense**
- Harm-tail component: strong defense. It is largely absorbed by `p_success`, small even before that overlap is removed, and based on indirect in-vitro and pravastatin evidence. The Challenger concedes the double-counting risk and that the myopathy point is weak.
- Compounding component: weak-to-partial defense. The concern that CG's 10% is an unexplained, undecomposed figure is legitimate. If the 10% is not already net of PK and reachability effects, the compounded range would move SROI below the bar. My defense there rests on overlap and correlation arguments, not on evidence that CG's 10% is in fact conservative.

**CONCESSIONS:**
- CG gives no derivation of 10% and no statement of what it embeds. This leaves the double-counting question unresolved in both directions.
- Winner's-curse shrinkage is a valid concern. An effect large enough to trigger a positive Phase III will systematically overstate the true effect, and that part is not covered by the "trial already embeds it" argument.
- A harm tail not detected in Phase III-scale safety monitoring, such as rare hepatotoxicity in a real-world population with comorbidity, is plausible. I have no data to bound it.
- If the three compounding factors are even partly additive to CG's 10%, the estimate could fall below the 2,000× bar. I cannot rule that out from the report.

### Challenger
REBUTTAL: Hepatotoxicity and myopathy add a negative tail, and the combined attenuations compound

**RESPONSE TO "EXISTING COVERAGE":**

*Harm tail*

> The Advocate claims: a hepatotoxic or myopathic drug would fail Phase II/III, so the harm tail and the "net-zero" case already sit inside the 60% failure mass of `p_success`.

- **Concession.** Harm large enough to be seen in a trial is plausibly absorbed by `p_success`. I agree this part of the critique is small and mostly double-counted, as the original critique itself said.
- **Net-zero false positives are not in the failure mass.** The 60% failure mass contributes zero to SROI. It is not a negative or a zero-effect case inside the success branch.
  - A trial can "succeed" with a true effect of zero or below, through chance or selection. The Advocate concedes this in the winner's-curse concession.
  - Those false positives sit inside the 40% success branch. The BOTEC applies r = 0.10 to all of that branch.
  - So "a net-zero effect is a failed trial" is true of the trial label but not of the true effect size. The harm-tail issue is about the true effect conditional on success, which `p_success` does not model.
- **Rare harms are invisible to a survival-powered Phase III.** The Advocate says a Phase III "would also record serious adverse events." Recording is not detecting.
  - The Advocate concedes it has "no data to bound" rare hepatotoxicity in a real-world population with comorbidity.
  - The residual is therefore post-approval harm in a less-monitored population. No trial gate screens that out.
- **Net.** I accept that the harm tail is about −0.01 or less. I do not accept that it is zero by construction.

*Compounding*

> The Advocate claims: any Phase III effect already embeds PK attenuation and reachable fraction, and the 10% may already be a haircut, so stacking three multipliers double-counts.

- **The Advocate's argument is internally in tension.**
  - It says the 10% has "no stated derivation," meaning it is not tied to any trial output.
  - It also says the 10% already embeds what a Phase III would show.
  - If the 10% is an unanchored assumption, nothing supports the claim that it embeds PK and reachability effects. That claim is as ungrounded as my ranges.
  - Both sides lack grounding. Embedding is an assumption, not a defense.
- **Partial concession on PK.** If the efficacy trial uses standard HRZE, PK attenuation is plausibly embedded in an observed effect. I will drop it and test the remaining claim.
  - Reachable fraction × shrinkage = 0.65×0.7 = 0.455 to 0.75×0.9 = 0.675.
  - Using the Advocate's 3,000× baseline, SROI ≈ 1,365×–2,025×.
  - That is below the ~2,000× bar across almost the entire range, even with the strongest of the Advocate's overlap arguments granted.
- **What the bar crossing requires.** Shrinkage alone (0.7–0.9) gives 2,100×–2,700×, which stays above the bar. The critique therefore needs shrinkage plus at least one other factor to be additive to the 10%.
  - The Advocate has conceded shrinkage is valid and "not covered by the trial already embeds it argument."
  - That leaves reachable fraction as the swing factor, and the Advocate offers no argument that it is embedded.
- **On "correlated factors do not multiply cleanly."**
  - Statistical co-movement of the factors raises the expected product slightly. This is the covariance term in E[XY]. I concede that and cannot size it.
  - The Advocate's argument is different: that the factors are conceptually the same thing counted twice. PK exposure, population coverage, and selection bias are distinct mechanisms, and no evidence is offered that they are one.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

- **Concession.** The three compounding ranges are unsourced, and the −0.01 is hypothetical. The critique's own "UNGROUNDED" flag already says so. My argument rests on the conditional structure above, not on those numbers being right.
- **Pravastatin and in-vitro data.** The Advocate is correct that THP-1/Vero data do not show human hepatotoxicity.
  - The evidence still shows that the programme designers' prior was that toxicity and interaction risks were large enough to drive drug selection (verifier items 1–3). That is a relevant signal about how seriously domain experts treat the harm channel, not a toxicity incidence rate.
  - If CG's benefit is built on atorvastatin, as the Advocate states, then the programme's choice of a different statin because of those concerns means the BOTEC's drug is not the one being tested. I cannot verify the atorvastatin premise from my materials. Conditional on it, effect transfer is imperfect.
- **Rosuvastatin safety result.** The Advocate reads "mildly reassuring" as pointing against a material harm tail.
  - The verifier item says the result is "underpowered for mortality." The same underpowering limits what it can say about rare hepatic or muscle events.
  - It is also a different statin from the one in the BOTEC. "Mildly reassuring" is not evidence of an absent tail.
  - I have no verifier evidence for a quantified rate of serious statin-attributable harm on HRZ. Neither side does.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

- **Harm tail alone.** The range is 0 to −0.01, about 10% of r at most. I concede it is below CG's ~25% materiality threshold and not threshold-crossing alone. After the `p_success` overlap, "low single digits" is a fair characterization, though the Advocate also cannot ground it.
- **Compounding minimum.**
  - Granting PK is embedded, the bound is 1,365×–2,025× (derived above).
  - Granting both PK and reachability are embedded, it is 2,100×–2,700×, above the bar.
  - The minimum plausible magnitude is therefore binary. It is near zero if only shrinkage applies, and bar-crossing if reachability also applies.
  - The question that decides the critique's materiality is whether reachability is additive to the 10%. The Advocate did not address this specifically.
- **"Upper-bound illustration."** The Advocate quotes this as if it concedes the range is overstated. It labels the downside case. It does not say the central case is near 1.0.

**RESPONSE TO "OFFSETTING FACTORS":**

- **Offsets are real omissions but unquantified.** The Advocate says it "cannot ground" the 1.2×–2.9× offset needed. The parameter-map statement that the estimate would be "robust" through morbidity and long-term survival is a hypothesis, not an estimate.
- **Offsets are not independent of the attenuations.**
  - Morbidity benefit and post-treatment survival benefit also come from the same statin acting on the same patients under the same rifampicin PK interaction.
  - The same shrinkage applies to them if the surrogate signal was over-read. The offsets are therefore partly correlated with the compounding factors and are not a clean additive buffer.
  - The sweat-test diagnostic value and transmission averted are different mechanisms. They do not depend on the statin effect, but the Advocate gives no sizing for them.
- **Harm is not offset by benefit channels.** A real hepatotoxic or myopathic tail is a cost to participants. Unmodeled benefits do not reduce it. They offset only the net SROI figure.
- **A symmetric omission is not a symmetric magnitude.** Unmodeled benefit channels have not been shown to be as large as the attenuations. The offset argument is only conditional.

**KEY UNRESOLVED QUESTIONS:**
- Does CG's 10% embed reachable-fraction effects, or only a generic haircut? This single answer largely decides whether the compounded range crosses the bar, per the 1,365×–2,025× vs 2,100×–2,700× split above.
- Is the 10% an observed or imagined trial effect? The Advocate cannot hold both "no derivation" and "already embeds trial realities."
- What fraction of the 40% success branch is true-null or winner's-curse false positives? This is conceded as valid but unquantified, and it drives the shrinkage factor.
- What is the incidence of serious hepatic or muscle injury for the chosen statin on HRZ in a TB population with comorbidity? Neither side has data.
- Are the omitted benefit channels (morbidity, post-treatment mortality, transmission, diagnostics) independent of the on-treatment effect, or do they carry the same attenuations?

### Judge Audit
Surviving strength: moderate
Justification: The debate was substantive rather than guess-trading. Both sides produced correct, explicitly conditional syntheses, and the Challenger narrowed the critique to a single bar-deciding question. However, the critique's titular harm-tail claim was effectively conceded down to a negligible magnitude. The surviving compounding concern rests on unsourced ranges borrowed from other critiques, plus a Challenger mischaracterization that the Advocate never addressed reachability. That rules out "strong." It stays above "weak" because the Advocate could not ground its claim that CG's 10% already embeds reachability or shrinkage.
Recommended action: 1. **CONCLUDE NOW** (harm tail, high confidence): Treat the hepatotoxicity/myopathy harm tail as at most a ~−0.01 adjustment to r, mostly overlapping p_success. Do not apply it as a separate material adjustment, and drop the ART-myopathy point.

2. **SPECIFIC INVESTIGATION** (compounding): Inspect CG's BOTEC (or ask CG) to determine two things:
   - (a) whether the 10% relative mortality reduction is applied to all on-treatment TB deaths or only to statin-reachable deaths;
   - (b) whether the 10% was derived from, or haircut from, the Phase IIa/b surrogate signals.

   If (a) is "all deaths" with no reachability discount, the reachability × shrinkage product (≈0.46–0.68) is additive and the critique is plausibly bar-crossing. Otherwise only shrinkage remains and it is not. This is feasible if the model or a CG clarification is obtainable.

   Separately, evaluate the compounding at the portfolio level alongside Critiques 1–4 rather than inside this critique, to avoid double-counting.
Action feasibility: requires_specified_evidence
Advocate failures: ['strawmanning: A net-zero effect is a failed trial, not a successful one with zero benefit." The critique\'s "net-zero or small negative effect" refers to the drug\'s true effect. The Advocate recast it as a claim about the trial label, which is a category swap. The Challenger correctly noted that false-positive successes with a true effect near zero sit inside the 40% success branch.', 'call_to_ignorance: The 10% "is plausibly already a haircut from larger surrogate signals." The Advocate supports this only by noting there is "no stated derivation." The absence of a derivation is being used as grounds that the figure is conservative. The Advocate later concedes the point ("not on evidence that CG\'s 10% is in fact conservative"), but the Existing Coverage section relies on it.', 'unsupported_estimate_pseudo: Correlated factors do not multiply cleanly… The lower bound of 0.23 therefore looks too aggressive." Positive statistical correlation among multiplicative factors does not shrink the product\'s lower bound. The valid argument is conceptual overlap (the same attenuation counted twice), which is a different claim. The chain from "correlated" to "lower bound too aggressive" has a logical gap, and the Challenger caught it.', 'unsupported_estimate_fabricated: The residual harm-tail effect on SROI is plausibly low single-digit percent. I cannot ground a tighter number than that." This is mild. The direction follows from the p_success overlap, but "low single-digit" is asserted without any sizing of the residual. The Advocate partly self-flags this.', 'false_definitiveness: A harm tail and an unmodeled benefit tail are both symmetric omissions." This asserts symmetry with confidence right after admitting the offset "cannot [be] ground[ed]." Structural symmetry is not shown to be symmetry of magnitude.', 'sound_synthesis_noted: SROI ≈ 3,000× × (0.23–0.54) = 690×–1,620×, and the required offset is 2,000/1,620 ≈ 1.2× to 2,000/690 ≈ 2.9×. Both are correctly derived and properly labeled as "size of offset required, not an estimate.']
Challenger failures: ['strawmanning: That leaves reachable fraction as the swing factor, and the Advocate offers no argument that it is embedded… The Advocate did not address this specifically." This is inaccurate. The Advocate explicitly argued that an observed Phase III effect "already reflects… the share of deaths that adjunctive therapy can reach." The Challenger\'s internal-tension point is a valid response to that argument, but claiming the argument was never made misrepresents the exchange.', 'whataboutism: That claim is as ungrounded as my ranges. Both sides lack grounding." This is mild. The surrounding tension argument is substantive: the Advocate cannot hold both "no derivation" and "embeds trial realities." But the "as ungrounded as my ranges" framing deflects rather than defends the Challenger\'s own unsourced inputs.', 'call_to_ignorance: The residual is therefore post-approval harm in a less-monitored population. No trial gate screens that out." This is mild. Undetectability is treated as support for a nonzero tail. It is mitigated because the Challenger caps the tail at ≤ −0.01 and concedes it is not threshold-crossing.', 'sound_synthesis_noted: With PK dropped, the Challenger computes reachability × shrinkage = 0.455–0.675, giving SROI 1,365×–2,025×. Shrinkage alone gives 2,100×–2,700×. Both are arithmetically correct and explicitly conditional on the unsourced ranges ("my argument rests on the conditional structure"). This was the most productive move in the debate: it isolates reachability as the single bar-deciding question.']
Debate resolved: The harm-tail component on its own is small (0 to −0.01 on r = 0.10, below the ~25% materiality threshold). It is largely absorbed by p_success, and both sides agree the ART-myopathy point is weak. If efficacy is measured on HRZE, PK attenuation is plausibly embedded. Shrinkage alone (0.7–0.9) does not push SROI below the ~2,000× bar.
Debate unresolved: The critique's materiality turns on one question: whether reachable-fraction attenuation is additive to CG's undocumented 10%. This depends on what population CG applies the 10% to and how the figure was derived. Neither side could answer it, and the input ranges driving the 1,365×–2,025× result remain unsourced.

--- Critique: A $7M Phase III cannot be powered on mortality, and the CEA's benefit is mortality only ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION: A $7M Phase III cannot be powered on mortality, and the CEA's benefit is mortality only

**EXISTING COVERAGE:**

1. The $7M is explicitly all-in. CG states that it includes "later Phase III trials, guideline changes, dissemination and validation." The BOTEC therefore does budget for a Phase III. The critique's real claim is that the budget is too small, not that the Phase III is missing.
2. CG applies a 40% probability that Phase II and Phase III both succeed. The Parameter Map notes that CG does not define "success." The 40% is therefore the only place where a surrogate-to-mortality translation gap, or an underpowered mortality readout, could already be priced in. It is a weak cover, but not zero.
3. The Phase IIc trial is described as testing dosing strategies for "survival, infection clearance and lung damage." Mortality data therefore begin accumulating before Phase III. They could be pooled with Phase III results or used to design it.
4. CG values only mortality. The Parameter Map lists morbidity DALYs, post-treatment mortality, transmission and diagnostic value as implicit zeros. The prior Phase IIa/b signal was on lung damage and clearance, not mortality. A surrogate-endpoint Phase III would support a benefit channel the BOTEC does not count.
5. The 1/cost scaling is only fully valid if the whole Phase III cost is attributable to this grant. CG credits one year of speedup, not permanent adoption. If the Phase III would happen eventually without the grant, which is what a speedup framing assumes, only the cost of accelerating it is counterfactual.
   - Charging the full Phase III cost against one year of benefit is already conservative.
   - Raising the Phase III cost 5× does not raise the attributable cost 5×.
   - The Parameter Map itself notes that CG does not reconcile the speedup and all-in-cost framings.

**EVIDENCE WEAKNESSES:**

1. The sample-size arithmetic is correct. I re-derived it with the standard two-proportion formula (80% power, α = 0.05, two-sided).
   - 5.0% → 4.5% gives about 28,400 per arm.
   - 8% → 7.2% gives about 17,200 per arm.
   - At CG's own 6% → 5.4%, I get about 23,400 per arm, or about 47,000 in total.
   - I cannot defend against the sample size, only against the cost attached to it.
2. The cost half of the critique is the weak half. The Challenger concedes per-participant cost is "UNGROUNDED," with a range of about $100 to tens of thousands of dollars. The $25–40M central case depends on assuming $500–1,000 per participant. That assumption is unsourced.
3. CG's $7M is arithmetically consistent with the lean end of that range.
   - $7M ÷ ~47,000 participants ≈ $149 per participant, before subtracting the $320K Phase IIc, guideline work and dissemination.
   - The implied Phase III per-participant cost is therefore roughly $100–140.
   - That sits at the embedded-trial end of the Challenger's own range.
4. Whether $100 per participant is achievable depends on the RECOVERY-style comparison, which the Verifier did not verify. I accept it arguendo. If a large pragmatic TB trial could be run at that cost, the critique's central case moves toward its own "narrows toward ~1×" scenario. I cannot ground that from the evidence package, so treat it as an open conditional.
5. The claim that a surrogate-endpoint Phase III fails to support the mortality benefit rests on the WHO GDG endpoint claim, which is also unverified. Under that unverified premise, the critique's strongest conclusion (mortality benefit unsupported) is not established. Neither is its opposite.
6. The critique assumes the generalisable Phase III must be powered for a 10% relative effect. N scales with 1/effect², so it is highly sensitive to the assumed design effect.
   - At 6% baseline and a 20% relative reduction (6% → 4.8%), I get about 5,560 per arm, or about 11,100 total.
   - At $500–1,000 per participant, that is about $5.6–11M, close to CG's $7M.
   - I flag the cost of this move (see Concessions): a trial powered for 20% has only about 28% power if the true effect is 10%.

**MAGNITUDE CHALLENGE:**

1. The Challenger's Phase III range is $5M–$100M+. That is a spread of over 20×, driven almost entirely by an ungrounded per-participant cost. A point estimate of 570× (range 300–1,000×) overstates how precisely the cost is known.
2. The Challenger's own low end ($5M) returns SROI to roughly the published 3,000×, or higher. The critique is therefore not a one-directional 3–10× reduction. It is a widening of uncertainty with a shifted center.
3. The 3,000 × 7/37 ≈ 570× calculation assumes 1/cost proportionality. Under the speedup-attribution argument (Existing Coverage, point 5), the true attributable cost rises by less than the all-in cost. The 1/cost elasticity is therefore less than 1, so the SROI reduction is overstated.
4. Even a partial reduction in the multiplier matters. At 25% below 3,000× (2,250×) CG is still near the bar, but at a ≥1.5× cost increase it drops below 2,000×. The critique clears the materiality threshold at fairly modest cost revisions. I do not claim the cost concern is immaterial.

**OFFSETTING FACTORS:**

1. Excluded benefit channels (morbidity/lung damage, post-treatment mortality, transmission, diagnostic value) are currently zero in the formula. If a cheaper surrogate-based Phase III is what gets funded, its natural output (lung or clearance endpoints) supports exactly those uncounted channels. I cannot quantify their size from the evidence package.
2. The speedup framing credits only one year of benefits. The Phase III cost is charged in full (see Existing Coverage, point 5).
3. Phase II/III results may also provide mortality evidence that adds to the evidence base for a guideline decision. For generic, cheap, low-toxicity drugs, decision thresholds may be lower than for new agents. I cannot ground this from the Verifier's package, so treat it as an uninformed prior.

**OVERALL ASSESSMENT:** Partial defense.

- The sample-size calculation is sound, and CG gives no breakdown of the $7M or endpoint reconciliation.
- At the Challenger's own central cost assumption, SROI falls below the 2,000× bar.
- The case for the central cost rests on an unsourced per-participant cost. The lean-design case rests on an unverified RECOVERY comparison, and the proportionality of cost to SROI is weakened by the speedup-attribution argument.
- The defense is not strong because the core tension between $7M and a mortality-powered Phase III is real.

**CONCESSIONS:**

1. A mortality-powered Phase III for a 10% relative effect needs about 35,000–57,000 participants. CG gives no derivation showing $7M covers this.
2. The Parameter Map is correct that CG does not state what endpoint the Phase III is powered on, or how that endpoint maps onto the mortality benefit used.
3. If the trial instead uses a surrogate endpoint, CG's 40% probability and 10% mortality effect are not directly supported by what that trial would produce. Defining "success" is a genuine gap.
4. Powering for a larger effect (such as 20%) to cut costs has a real downside. A true 10% effect would then be detected only about 28% of the time, so success-conditional effect sizes would be inflated, and the 40% p_success would be harder to defend.
5. The cost uncertainty cuts both ways, but the central case of $20–40M is a reasonable reading if sites are standard LMIC pragmatic TB sites. I cannot rule it out.

### Challenger
REBUTTAL: A $7M Phase III cannot be powered on mortality, and the CEA's benefit is mortality only

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the $7M is explicitly all-in and so includes a Phase III. The 40% p_success is the only place a surrogate-to-mortality gap could be priced in. Phase IIc mortality data could be pooled. The surrogate-based Phase III would support uncounted channels. Attributable cost scales less than 1:1 under the speedup framing.

1. **The all-in point.**
   - I agree the Phase III is budgeted. The critique is about adequacy, which the Advocate concedes ("CG gives no derivation showing $7M covers this").

2. **The 40% as hidden cover.**
   - The Advocate calls it "weak, but not zero." A probability that CG never defines cannot price a power shortfall.
   - Take the Advocate's own number: a trial sized for a 20% effect has about 28% power at a true 10% effect.
   - Check: n = 5,560 per arm, SE ≈ 0.0044, effect 0.006, z ≈ 1.37, so power ≈ 28%.
   - Conditional derivation, with an assumption I cannot verify: if CG's 40% silently embeds conventional 80% Phase III power, the cheap design gives 40% × 0.28/0.80 ≈ 14%.
   - That is about a 2.9× cut in expected value, on top of any cost effect. The cost-saving move therefore trades one problem for another.

3. **Pooling Phase IIc mortality.**
   - Phase IIc costs $320K, so it is tiny relative to a trial needing roughly 47,000 participants at CG's own 6% baseline.
   - Even 1,000 participants would add about 2% of the required information, and I cannot ground the actual Phase IIc size.
   - Pooling does not change whether the Phase III can detect a 10% effect.

4. **Uncounted benefit channels.**
   - The CEA's benefit is mortality only. A trial that reports lung damage or clearance does not support the 10% mortality effect that is actually in the formula.
   - Pointing to channels valued at zero is not a defense of the quantified channel.
   - The Advocate admits it cannot size these channels.

5. **Speedup attribution (elasticity < 1).**
   - The idea is conceptually coherent, but CG does not model it, and the Advocate gives no elasticity.
   - It also depends on the Phase III happening anyway. A repurposed-generic HDT has no obvious commercial sponsor, and nothing in the evidence package says one would step in.
   - The Advocate also notes that CG charges the full cost. CG chose that framing, and the critique tests the number inside CG's own framing.
   - Switching frameworks at the rebuttal stage does not show the existing number is robust.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the cost half is the weak half. $7M ÷ ~47,000 ≈ $149 per participant, which sits at the embedded-trial end of the range. The RECOVERY comparison is unverified, so it is an open conditional. The WHO GDG claim is unverified, so the mortality-unsupported conclusion is not established.

1. **The $149 figure is the floor, not a midpoint.**
   - The verifier's package says a very lean design bounds the Phase III near $5M.
   - CG's $7M sits at that floor. It is not a central case that happens to fall in the range.
   - After subtracting Phase IIc, guideline work and dissemination, the implied Phase III per-participant cost is about $100–140. The Advocate agrees.
   - CG's number therefore requires the most favourable cost scenario at the same time as the most demanding statistical design.

2. **The materiality threshold is close to CG's implied cost.**
   - A 25% SROI fall needs cost ×1.33, which is about $9.3M.
   - $9.3M ÷ 47,000 ≈ $198 per participant.
   - Any per-participant cost above roughly $200 breaches materiality, about 1.4–2× above what CG implicitly assumes.
   - The critique does not need the unsourced $500–1,000 assumption. It only needs costs not to be at the very bottom of the range.

3. **The RECOVERY comparison is UNVERIFIABLE, not rejected.**
   - Conditional: if a 47,000-person embedded trial really costs about $100–150 per person, the critique shrinks toward the ~1× scenario. I concede that.
   - I cannot ground that premise either. The Advocate has not given it positive support. The Advocate says it "cannot ground that from the evidence package."
   - Both sides are in the same state: the lean-cost scenario is plausible but unsupported.

4. **The WHO GDG claim is not load-bearing.**
   - The surrogate problem does not depend on it. The Advocate concedes (Concession 3) that a surrogate trial does not directly support CG's 10% mortality effect and 40% p_success, and that "success" is undefined.
   - The verifier's finding that "no clear consensus exists on appropriate endpoints for HDT trials" supports uncertainty about what evidence suffices. It does not reject the critique.
   - The Advocate's "neither is its opposite established" is true, but the burden is on CG to link the trial's endpoint to the mortality benefit it claims.

5. **The 20% design.**
   - The Advocate's 5,560-per-arm design works against CG's own effect assumption of 10%. Powering for 20% means a 10% effect, which the CEA treats as the central case, would usually go undetected.
   - The Advocate acknowledges this. It means the cost reduction is bought by making CG's own p_success harder to defend.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: a $5M–$100M+ range makes 570× falsely precise. The low end returns to ~3,000× or higher, so this is a widening rather than a one-directional reduction. Elasticity is below 1. Materiality is still cleared at ≥1.5× cost.

1. **The range is asymmetric around CG's number.**
   - CG's $7M is at the favourable tail. The only cost outcomes better than it lie between about $5M and $7M. The rest lie above it.
   - Illustrative expected-value calculation. This is my assumption, an uninformed log-uniform prior over the critique's stated range.
   - The log-uniform prior gives E[1/C] = (1/ln 20) × (1/5 − 1/100) per $M ≈ 0.0634, an effective Phase III cost of about $15.8M.
   - That is about 2.3× above $7M, implying SROI near 1,300×.
   - Truncating the range to $5–40M gives an effective cost of about $11.9M, or about 1.7×, implying SROI near 1,800×.
   - Both fall below the 2,000× bar. The prior is mine, so this is a sensitivity illustration and not a finding.

2. **"Widening, not a reduction" is incomplete.**
   - Widening around a point sitting at the best-case end shifts the expected value and the median downward.
   - Only designs between about $5M and $7M give SROI at or above 3,000×.

3. **On elasticity below 1.**
   - It is unquantified and not in CG. I treat it as a possible partial discount, not a demonstrated one.
   - It would need to be implausibly low to offset a 1.7–2.3× shift, because the Advocate has not shown the Phase III is truly counterfactual.

4. **Minimum plausible impact.**
   - At the favourable end ($5–7M), the cost correction is roughly zero.
   - The Advocate concedes materiality is cleared at modest cost revisions. The Advocate's own threshold is ≥1.5×, or $10.5M. My $9.3M figure uses the critique's 25% bar.

**RESPONSE TO "OFFSETTING FACTORS":**

1. **Excluded benefit channels.**
   - They are zero in the formula and unquantified. The Advocate calls their size unknowable from the evidence package.
   - A hypothetical, unsized offset cannot neutralize a quantified cost and power shortfall.
   - Counting them would also require a new p_success and effect size, since a surrogate endpoint is not the mortality effect.

2. **The one-year speedup credit.**
   - It is already in the 3,000× headline. It is not an additional offset to the cost correction.
   - Listing it here double counts a feature of CG's own framing.

3. **Phase II/III mortality evidence and lower decision thresholds.**
   - The Advocate labels this an uninformed prior. The verifier's package has nothing on it, and the verifier found no consensus on HDT endpoints.
   - It carries no evidential weight in either direction.

**KEY UNRESOLVED QUESTIONS:**

- What per-participant cost is achievable for a roughly 35,000–57,000-person pragmatic TB mortality trial of a generic HDT? The $100–150 level implied by CG's $7M is unverified, and the verifier found only a $5M lean-design bound.
- What does CG mean by "success" in its 40%? Does it embed the power to detect a 10% mortality effect, or only a surrogate signal?
- If the Phase III is powered for 20%, what is the right p_success when the true effect is 10%?
- Would the Phase III happen without the grant, and how much of its cost is truly attributable to the grant?
- Can a surrogate-endpoint trial support a guideline change on its own, so that the mortality benefit would be credited? The verifier found no consensus on HDT endpoints.

### Judge Audit
Surviving strength: strong
Justification: The Challenger's key arguments were grounded, arithmetically verified, and largely conceded by the Advocate:
- the $198-per-participant materiality threshold;
- the asymmetry of CG's $7M at the low tail;
- the power/p_success trade-off for cheaper designs.
The Advocate's remaining defenses (elasticity below 1, uncounted channels, lower decision thresholds) were unquantified and partly rested on unestablished premises. The Advocate's own self-assessment of "strong" is contradicted by its body text and its concessions. The strength applies to the direction and materiality of the critique, not to its specific 3–10× magnitude, which rests on an ungrounded per-participant cost.
Recommended action: 1. CONCLUDE NOW: With moderately high confidence, CG's $7M all-in cost is inconsistent with a mortality-powered Phase III unless per-participant costs stay below about $200, which is atypical for TB trials per the verifier's evidence. The alternative cheaper designs undercut the 40% p_success and the 10% mortality effect.
   - The SROI should be treated as materially overstated, likely by at least 1.3×.
   - The point estimate of the reduction is uncertain, with 570× as a plausible central case rather than an established one.
   - CG should be asked to state the Phase III endpoint and power assumption behind "success."

   A targeted follow-up would sharpen the magnitude and is feasible with existing tooling. The verifier should retrieve published per-participant costs for large pragmatic DS-TB or HIV-TB trials in LMICs, especially those using mortality or vital-status endpoints.
Action feasibility: actionable_now
Advocate failures: ['sound_synthesis_noted: The Advocate independently re-derived sample sizes, and the figures check out:', 'false_definitiveness: The 1/cost elasticity is therefore less than 1, so the SROI reduction is overstated." This is stated as a conclusion. It depends on an unestablished premise: that the Phase III would happen without the grant. The Advocate offers no elasticity value and no evidence of a counterfactual sponsor. At most it is a possible discount, not a demonstrated overstatement.', 'call_to_ignorance: Offsetting Factors 1 and 3 have the same structure. They propose unquantified excluded channels and "lower decision thresholds for generic drugs" as offsets, while admitting neither can be sized or grounded ("uninformed prior"). The disclosure is honest. Listing them as offsets still amounts to treating unknowns as weight on the Advocate\'s side.', 'misrepresenting_evidence_status: The Advocate says $100 per participant is achievable only via the unverified RECOVERY comparison. It presents CG\'s implied $100–140 as sitting "at the embedded-trial end" of the range, with no further qualification.', 'generic_recommendation: There is a self-assessment inconsistency. The body concludes "OVERALL ASSESSMENT: Partial defense." The self-assessment says "strong." Given five substantive concessions, including that the $20–40M central case "cannot be ruled out," "strong" is not credible. (This does not fit the generic_recommendation definition well; it is flagged here only as a calibration issue.)']
Challenger failures: ['sound_synthesis_noted: The materiality threshold derivation is correct.', 'sound_synthesis_noted: The log-uniform E[1/C] calculation is arithmetically correct (0.19/ln20 ≈ 0.0634, giving about $15.8M; truncated to $5–40M, about $11.9M). It is explicitly flagged as resting on the Challenger\'s own prior ("a sensitivity illustration and not a finding").', 'sound_synthesis_noted: The 40% × 0.28/0.80 ≈ 14% p_success adjustment is clearly labelled conditional on an unverified assumption that the 40% embeds 80% power.', 'strawmanning: Switching frameworks at the rebuttal stage does not show the existing number is robust." The Advocate did not switch frameworks. The Advocate pointed out that CG\'s own model fails to reconcile its speedup framing with its all-in-cost framing, which the Parameter Map also notes. That internal inconsistency is a legitimate critique of applying 1/cost scaling within CG\'s framing. The Challenger\'s other response, that no counterfactual sponsor is evident, is the valid answer.', 'false_definitiveness: It would need to be implausibly low to offset a 1.7–2.3× shift." No derivation is given for what elasticity would be needed or why it would be implausible. Also, "A repurposed-generic HDT has no obvious commercial sponsor" is a reasonable but unsupported assertion. It is softened appropriately by "nothing in the evidence package says one would step in.', 'misrepresenting_evidence_status: This is minor. The Challenger states "the verifier found only a $5M lean-design bound." This understates the verifier\'s material. The verifier also supplied the $97 median and the TB-PRACTECAL figure of about €61k per patient. Neither side used the verifier\'s explicit TB-specific caveat, which favored the Challenger.']
Debate resolved: The sample sizes are settled: roughly 35,000–57,000 participants, or about 47,000 at CG's 6% baseline.

The debate also established that CG's $7M implies a Phase III cost of about $100–150 per participant. That is at the extreme favorable tail of the cost distribution, and materiality is breached at roughly $200 per participant.

Finally, it established a dilemma. A mortality-powered trial needs near-floor costs. A cheaper surrogate-powered or 20%-powered design undermines CG's 10% mortality effect and its 40% p_success. The Advocate conceded both horns.
Debate unresolved: Two questions remain open:
- Whether a mortality-endpoint pragmatic LMIC TB trial can actually be run at about $150–200 per participant.
- Whether any of the Phase III cost is non-counterfactual under CG's speedup framing.

Together these determine whether the reduction is roughly 1.3× or the critique's 3–10×. The debate did not establish the 3–10× point magnitude.

--- Critique: The all-in framing counts benefits for every treated patient but not the cost of treating them ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: The all-in framing counts benefits for every treated patient but not the cost of treating them

EXISTING COVERAGE:
- CG does not itemize delivery costs. The parameter map confirms this: "No costs of delivering the drug" and "No account of who bears delivery costs."
- Three existing features partly absorb the concern:
  1. The 60% uptake is justified as "generic and cheap." Price sensitivity is therefore already in the uptake assumption. A drug expected to cost the system little is what supports 60%.
  2. The 40% probability of success is applied to the whole numerator. Delivery spending occurs only if both trials succeed and the drug is adopted, so the critique's own formula mishandles this (see MAGNITUDE).
  3. "Only mortality is valued." Four benefit channels are implicit zeros: lung-damage morbidity, post-treatment survival, transmission averted and diagnostic value (parameter map, benefit-terms entry). These are the benefits that would accompany the same delivered courses. The critique adds the cost of the courses but leaves out these benefits.

EVIDENCE WEAKNESSES:
- The critique's D ($3–33M) rests on a $1–10 per-course procurement price. By the critique's own admission, "I could not verify prices." I cannot ground a price either.
- The critique labels this range "the thread's range," which is not a source.
- The 3.3M patient figure is unverified in the critique. It is simply the BOTEC's own 60% × 5.5M. The critique inherits the BOTEC's scale and then applies a cost to it.
- Monitoring costs are "plausibly material" only by analogy to first-line TB drug liver monitoring (Critique 2). That is an inference, not evidence of an atorvastatin-specific requirement.
  - Conditional on the Phase IIa/b signal being real, I see no evidence in the package that a statin add-on requires monitoring beyond what TB programs already do. The marginal monitoring cost could be near zero.
- The Phase IIC trial record (NCT06199921) establishes that dosing is unsettled. It does not establish a per-course cost. Dose affects D only through tablet count, which is a modest multiplier on a number that is itself unknown.
- The critique labels its "counterfactual-value convention" point as ungrounded. The 20–30% of face value is its own assumption.

MAGNITUDE CHALLENGE:
1. **The critique's break-even math ignores the 40% probability, which is a structural error.**
   - Delivery cost D is incurred only if the trials succeed and the drug is adopted. In expected-value terms it is weighted by 0.4, as the benefits are.
   - The critique instead adds D to the denominator at full weight and then multiplies by 0.4 again. This double-penalizes D.
2. **Derivation under consistent weighting.**
   - Expected benefit = 0.4 × $54B = $21.6B. This is straight from the BOTEC.
   - Expected cost = $7M (CG treats it as spent in full) + 0.4 × D.
   - Break-even at 2,000x: $21.6B / 2,000 = $10.8M total. So 0.4D = $3.8M, giving D ≈ $9.5M, or about $2.9 per patient across 3.3M.
   - The critique's break-even is $3.7M, or $1.10 per patient. Correcting for probability weighting makes the tolerable D about 2.6× larger.
3. **Central case under consistent weighting.**
   - At the critique's central D of $10M, expected cost = $7M + $4M = $11M.
   - SROI = $21.6B / $11M ≈ 1,960x, against the critique's 1,250x.
   - That is a ~36% decline from 3,086x and sits right at the bar. It is not a "2–3× reduction."
4. **Per-course cost needed to fall below the bar.** Using the corrected threshold of about $2.9 per patient:
   - At the low end of the critique's range ($1–3 per course), the result stays at or above the bar.
   - At $10 per course, it falls clearly below.
   - The conclusion therefore depends on the unverified price, which I cannot ground either way.
5. **Counterfactual-value convention.**
   - The 2,000x bar is calibrated to CG's marginal alternative use of its own dollar. Treating a government or Global Fund dollar at face value in the denominator implicitly values it at that same bar. Those funders' marginal alternatives are probably lower-return than CG's bar, because the bar is set at the frontier of what CG funds.
   - I cannot ground a specific discount. The critique's 20–30% is one assumption. At 25% face value, D_effective ≈ 0.25 × $10M × 0.4 = $1M, and SROI ≈ $21.6B / $8M ≈ 2,700x. That is a ~12% decline, below the 25% materiality threshold.
6. **Timing.** The benefit of a 1-year speedup is one additional year of treated cohorts, so the cost of treating that cohort is a real increment. I do not argue that delivery costs wash out.

OFFSETTING FACTORS:
- Excluded benefit channels, per the parameter map: lung-damage morbidity, post-treatment mortality, transmission averted and diagnostic value. Any positive value on these partly offsets D.
  - I have no grounded magnitude. Conditional on the Phase IIa/b lung-damage signal being real, the offset is positive, not zero.
- Probability-weighting of D (above) is the largest offset and requires no new assumptions.
- Uptake: if actual uptake in the first years is below 60% (the parameter map flags no ramp-up), then D and benefits shrink proportionally. The critique treats D as fixed while the benefit scale is already generous.
  - This changes the benefit-to-cost ratio of delivery only if delivery costs have fixed components, which seems unlikely for a generic oral add-on.

OVERALL ASSESSMENT: Partial defense.
- The critique identifies a real omission: CG does not state how delivery costs are treated.
- It overstates the effect through the double-penalty on D and an untested price range.
- Properly weighted, the central case is ~1,960x, essentially at the bar, rather than 1,250x.
- Under a plausible counterfactual-value discount, the change is under the 25% threshold.
- The conclusion is sensitive to a price I cannot verify.

CONCESSIONS:
- CG's convention for third-party delivery costs is unstated. That is a legitimate transparency gap.
- Under the face-value convention and a per-course cost around $10, SROI falls below 2,000x even after my correction.
- The unmodeled monitoring cost is real if any extra monitoring is needed. I cannot rule that out from the evidence package.
- My counterfactual-value argument is reasoned but ungrounded. It supports a discount below face value, not a specific number.
```

### Challenger
REBUTTAL: The all-in framing counts benefits for every treated patient but not the cost of treating them

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: three existing features partly absorb the concern: (1) the 60% uptake already embeds "generic and cheap"; (2) the 40% success probability covers the whole numerator; (3) excluded benefit channels offset the omitted cost.

1. **Uptake does not put a dollar in the denominator.**
   - The 60% is a count of patients. It adds no dollar cost to the denominator.
   - The "generic and cheap" justification is the same unverified price claim the Advocate says it cannot ground.
   - A cheap-drug assumption used to justify high uptake makes the omission worse. It maximizes the number of patients benefits are counted for, with no cost attached.

2. **The Advocate's probability-weighting point is valid, and I concede it.**
   - The Advocate's description of the critique is slightly off. The critique's numerator (3,086x × 7/17) is already 0.4-weighted, so the 0.4 is not applied "again."
   - The substance still stands. D is conditional on success and should be weighted by 0.4, as the $7M trial spend is not.
   - My concern is what remains after this correction (see MAGNITUDE).

3. **The Advocate concedes the core finding.**
   - It agrees the parameter map says "No costs of delivering the drug" and "No account of who bears delivery costs."
   - So none of the three features is a delivery-cost adjustment. They are neighboring assumptions that overlap only incidentally.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

1. **Price is unverified, but the break-even does not need a precise price.**
   - The Advocate's own corrected break-even is ≈$2.9 per patient, all-in.
   - That figure must cover pills, supply chain, dispensing and any added monitoring.
   - I cannot ground a tender price for atorvastatin. Treat my sense that pills alone could consume much of $2.9 over a multi-month course as an uninformed prior.
   - The Advocate also cannot show the all-in cost is below $2.9. The critique has "verified at retail," so the price is not a pure guess. Neither side has a number.
   - A threshold this low (a few dollars) makes the conclusion sensitive to the unstated cost. The critique should not be dismissed on price alone.

2. **"The 3.3M is inherited from the BOTEC" is not a weakness.**
   - The benefits are computed on the same 3.3M patients. Costs and benefits therefore scale together, which is the internal-consistency point the critique makes.
   - If 3.3M is wrong, benefits shrink too.

3. **Monitoring: "could be near zero" is the Advocate's inference, and the Advocate concedes it cannot rule out material monitoring.**
   - The verifier's package lists monitoring costs as "plausibly material," not as REJECTED.
   - The critique's monitoring point is therefore an open, unresolved question, and the Advocate has not refuted it.
   - Separately, rifampicin is a known CYP3A4 inducer that lowers atorvastatin exposure. This is outside the verifier package and I am relying on general pharmacology, so treat it as a conditional. It would add to the dose uncertainty the verifier did confirm, since Phase IIC tests different doses in 440 patients.

4. **The Advocate accepts that Phase IIC dosing "is a modest multiplier."**
   - Against a threshold of only ~$2.9, even a 2–3× tablet multiplier moves the result across the bar.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: with D probability-weighted, the central case is ≈1,960x, "essentially at the bar," not 1,250x. Under a plausible counterfactual-value discount the decline is ~12%, below the 25% materiality threshold.

Take the Advocate's correction as given. Its derivation, applied across the critique's own price range, at face value:

| Per-course cost | D (3.3M patients) | Expected cost = $7M + 0.4D | SROI = $21.6B / cost | vs. 3,086x |
|---|---|---|---|---|
| $1 | $3.3M | $8.3M | ≈2,600x | −16% |
| $3 (high end of the Advocate's "stays above the bar" range) | $9.9M | $11.0M | ≈1,960x | −36% |
| $10 | $33M | $20.2M | ≈1,070x | −65% |

(The $10M row in the Advocate's text corresponds to ~$3 per patient, which is the same row as $3.)

1. **The Advocate's own central case is a 36% decline, which exceeds the 25% materiality threshold it cites.**
   - It uses 25% to dismiss the discounted case but does not apply it to the face-value case.
   - Under its own correction, the face-value convention is material at the central and upper values.

2. **The central estimate sits at the decision threshold.**
   - A result at ~1,960x is a 2% shortfall against 2,000x. Any plausible D above ~$9.5M tips it, and the Advocate concedes $10 per course falls "clearly below."
   - The prior was ~3,086x, comfortably above the bar. The recommendation's margin has gone from ~54% to ≈0, so the omitted cost is decision-relevant.

3. **The discount case depends on an ungrounded convention that the Advocate admits it cannot ground.**
   - Its 25% face-value figure is its own assumption, the same status it assigns to the critique's 20–30%.
   - At 25% and the $33M upper D: 0.25 × 33 × 0.4 = $3.3M, cost $10.3M, SROI ≈2,100x. That is still above the bar.
   - I concede that under a substantial discount the effect is small. The critique itself says so.
   - The residual finding is therefore as the critique states: the result ranges from "no meaningful change" to "below the bar," depending on a convention CG does not state.

4. **The Advocate's argument for a discount is reasoning without data.**
   - The bar is calibrated to CG's marginal dollar. That is a coherent argument for some discount.
   - It does not tell us whether the discount is 10% or 75%, and it applies equally to every comparison grant that counts third-party costs.
   - I cannot ground which convention CG uses elsewhere either.

**RESPONSE TO "OFFSETTING FACTORS":**

1. **Probability-weighting of D: real, no new assumptions, already conceded.** It is the only offset that is both real and quantified, and it has been absorbed in the table above.

2. **Excluded benefit channels (lung-damage morbidity, post-treatment mortality, transmission averted, diagnostic value) are not a quantified offset.**
   - The Advocate states it has "no grounded magnitude."
   - An unquantified buffer cannot be netted against a quantified cost. It argues for a different correction (add the benefits), not for leaving the cost out.
   - The model does not say the omission is a deliberate conservative buffer. It records the benefit terms as implicit zeros.
   - If those benefits are real, a corrected model would include both. That would not leave the omission of D a non-issue.

3. **Uptake below 60% is not an offset by the Advocate's own logic.**
   - It says the ratio changes "only if delivery costs have fixed components." If costs scale proportionally with benefits, the ratio is unchanged.
   - That is neutrality, not an offset.

4. **Timing: the Advocate concedes D is a real increment.**
   - The 1-year speedup treats one extra cohort, so D for that cohort is genuinely added.

**KEY UNRESOLVED QUESTIONS:**
- What is the all-in per-patient delivery cost, including supply chain, dispensing and any added monitoring? Is it above or below the ~$2.9 break-even implied by the Advocate's correction?
- Does CG's convention treat government and Global Fund spending at face value, at a discount, or at zero? The discount factor determines whether the critique is immaterial or decisive.
- Does the Phase IIC dose-finding result change tablet count, or require extra monitoring, relative to the Phase IIa/b regimen?
- Are the excluded benefit channels large enough, once quantified, to offset a delivery cost in the $10–33M range?
- Is "no delivery costs" a deliberate scoping decision (benefits and costs both marginal to CG) rather than an omission? That is a question for CG, and the answer would collapse most of this critique.

### Judge Audit
Surviving strength: moderate
Justification: The Advocate's probability-weighting correction is a grounded synthesis that both sides accepted. It cut the critique's central-case magnitude roughly in half. The Challenger then showed, using the Advocate's own arithmetic, that the face-value central case is still a 36% decline to the bar. Both sides traded some unsupported moves: the Advocate's near-zero monitoring claim and its unquantified offsets, and the Challenger's 2–3× dose multiplier. But the core quantitative exchange was substantive. The question is narrowed to two identifiable parameters rather than settled.
Recommended action: 1. CONCLUDE NOW (moderate confidence).** The critique's qualitative point holds. CG counts benefits for all treated patients without stating how delivery costs are handled, and under face-value accounting this moves SROI from about 3,086x to roughly 1,960x at about $3 per patient. The critique's "2–3× reduction" should be restated as "about a 35% reduction to roughly at-the-bar at a central cost, with a larger reduction only if the all-in cost approaches $10 per course." Under any substantial discount on third-party money, the effect is immaterial.

**2. SPECIFIC INVESTIGATION.** Two checks would settle the remaining questions:
   - **Tender price.** Re-run the verifier with targeted retrieval of the MSH International Drug Price Indicator Guide and the GDF/UNICEF catalog entries for atorvastatin 20 mg and 40 mg. Multiply by the 112-tablet course. This shows whether drug procurement alone is clearly below or above the $2.9 per patient break-even. It is feasible with existing tooling, since these are public sources the verifier failed to retrieve.
   - **CG's convention.** Check CG and Open Philanthropy published SROI or leverage methodology for how third-party implementation costs are treated in other grants. If the denominator is CG-only by design, the critique reduces to a transparency note.
Action feasibility: requires_specified_evidence
Advocate failures: []
Challenger failures: []
Debate resolved: Both sides now accept that D should be probability-weighted by 0.4. Under that correction:
- At face value, the break-even all-in delivery cost is about $2.9 per patient.
- The critique's central case moves from about 1,250x to about 1,960x. That is a 36% decline, which is material and sits right at the 2,000x bar.
- Under a substantial counterfactual discount on third-party money, the effect is small. At the $33M upper D it stays at about 2,100x.

The critique's "2–3× reduction" survives only at the top of the price range under face-value accounting. The core finding stands: CG's convention for delivery costs is unstated, and the omission is decision-relevant.
Debate unresolved: Two questions remain open:
1. **Delivery cost against the break-even.** Is the all-in per-patient cost (tender drug price plus supply chain, dispensing and any added monitoring) above or below about $2.9? The grounded retail evidence (about $10–26 per course) sits above it, and tender prices are unverified.
2. **CG's convention.** Does CG value government and Global Fund delivery spending at face value, at a discount, or exclude it by deliberate scoping? Neither side could ground any convention.

--- Critique: Regulatory, pharmacovigilance and dissemination costs for an off-patent drug have no obvious payer, and the $7M likely under-budgets them ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: Regulatory, pharmacovigilance and dissemination costs for an off-patent drug have no obvious payer, and the $7M likely under-budgets them
```

**EXISTING COVERAGE:**
- The $7M is not a trial-only figure. The BOTEC says the all-in cost includes "later Phase III trials, guideline changes, dissemination and validation." Guideline and dissemination costs are therefore in scope. The critique's claim is about magnitude, not omission.
- The $7M is about 22x the $320k Phase IIc cost ($7M / $0.32M ≈ 21.9). The BOTEC thus already leaves roughly $6.7M for Phase III, guideline work and dissemination. The critique asserts "a Phase IIc of $320k plus any plausible Phase III already uses most of it." That assertion rests on a Phase III cost the critique never supplies.
- SROI is computed on all-in costs against all-in benefits, so CG does not pretend the grant's own $320k is the whole cost. The "no obvious payer" problem is handled by counting everyone's costs, not just CG's.
- The critique's pharmacovigilance concern (hepatotoxicity overlapping with isoniazid, rifampicin and pyrazinamide) is a cost-of-monitoring concern. It is a different category from the adverse-event-management cost the CEA map flags as unmodeled, but both sit under the generic "dissemination and validation" heading CG names.

**EVIDENCE WEAKNESSES:**
- The Quantifier states every dollar magnitude is UNGROUNDED ($5–20M, $4M, "70–300%"). The sensitivity-results field is empty. The critique therefore contains no measured cost datum, only an illustration.
- The only evidence cited is that the Phase IIc is "a stepping stone" and that "important questions need answering before a more expensive Phase III." That shows a Phase III will exist. It does not show the Phase III or its follow-on costs exceed what the $7M already allocates. The critique itself says this "is not a budget figure."
- The critique's own countervailing evidence cuts against it. Early-phase safety data are favourable, so monitoring is "likely a guideline-driven choice rather than a demonstrated necessity." If monitoring is optional or light-touch, the cost driver is weaker than the headline suggests.
- Atorvastatin is a long-established generic with extensive existing safety experience. I cannot cite a specific study here, so treat this as general background. The TB-specific interaction is real, but the baseline safety profile is not that of a new molecular entity requiring heavy post-marketing surveillance.

**MAGNITUDE CHALLENGE:**
- **Headroom.** The published SROI is about 3,086x ($54B / $7M × 0.4). The cost at which it reaches the 2,000x bar is about $10.8M ($54B × 0.4 / 2,000). The $7M can therefore absorb roughly $3.8M (about 54%) of extra cost before crossing. The critique's "$10.7M threshold" matches this, so the arithmetic is not in dispute.
- **Probability weighting.** The BOTEC applies the 40% joint success probability to benefits but treats the $7M as certain. Post-adoption pharmacovigilance, guideline rollout and dissemination are incurred only if Phase II and Phase III both succeed.
  - Derivation: take the critique's own illustrative $4M add-on, which is ungrounded and used here only conditionally. It is incurred only in the 40% success branch, so its expected cost is $4M × 0.4 = $1.6M.
  - Total expected cost is $7M + $1.6M = $8.6M.
  - SROI = $54B / $8.6M × 0.4 ≈ 2,512x, still above the bar.
  - The critique's "$4M pushes past $10.7M" treats a success-contingent cost as unconditional.
- **Caveat on that derivation.** It is only as good as the $4M figure, which I cannot ground either. It also assumes the $7M already reflects only a modest probability-weighting of its Phase III component, and the BOTEC does not say how $7M was built. The point is structural, not a replacement estimate: contingent costs should be weighted by the probability they occur.
- **The critique's top-end.** A $5–20M add-on is a 70–300% increase on $7M, and the critique labels it "no empirical basis." Even weighted by 0.4, the $20M end gives $8M expected, for a total of $15M and an SROI of about 1,440x. That outcome is only reachable at a figure the critique itself cannot support.

**OFFSETTING FACTORS:**
- Per the parameter map, the benefit side values only mortality. Reduced lung damage, post-treatment mortality, transmission effects and the sweat diagnostic are all implicit zeros. Upward benefit omissions can absorb some cost upside without crossing the bar.
- The Phase IIc is explicitly testing dosing strategies. If those results shape a leaner Phase III design, the Phase III could cost less than a generic pivotal-trial template. I cannot ground this; treat it as an uninformed prior.
- Guideline and dissemination costs for a cheap generic adjunct are plausibly borne partly by existing WHO and national TB-programme processes. I cannot cite a source for the cost share. The critique's "no payer" framing assumes the cost must be newly funded, which is not established.

**OVERALL ASSESSMENT:** Partial defense.
- The critique rests on no quantified evidence, and by the Quantifier's own admission it is "wholly unquantified." The omission framing is partly wrong, because dissemination and guidelines are explicitly in the $7M.
- The strongest defensive point is that success-contingent costs should be probability-weighted by the 40% figure. That roughly halves the impact of the critique's own illustration and keeps SROI above 2,000x.
- The critique's structural observation survives. The BOTEC gives no breakdown of the $7M, so its adequacy cannot be verified. Headroom to the bar is only about 54% of the stated cost, which is thin for a figure with no stated derivation. That makes this an unresolved uncertainty, not a demonstrated error.

**CONCESSIONS:**
- The $7M has no published breakdown or reconciliation with typical TB Phase III costs, so I cannot show it is adequate.
- The TB-drug hepatotoxicity overlap makes some monitoring cost plausible. I do not dispute that it exists, only that it is large.
- The headroom to the 2,000x bar is modest. Without probability-weighting and without the unvalued benefit channels, a cost add-on of $4M or more would take SROI below the bar.
- Direction leans upward, as the critique says. I contest the magnitude and the unconditional treatment of the cost, not the direction.

### Challenger
REBUTTAL: Regulatory, pharmacovigilance and dissemination costs for an off-patent drug have no obvious payer, and the $7M likely under-budgets them

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the $7M already includes Phase III, guideline changes and dissemination, so the critique is about magnitude rather than omission. The ~22x multiple over the $320k Phase IIc leaves ~$6.7M for those items, and the critique never supplies a Phase III cost.

- **Conceded.** The omission framing is wrong, and the critique is only a magnitude claim. The critique's own "Keep" language already points that way.
- **Subtraction is not adequacy.** "$7M − $0.32M = $6.7M of room" shows that room exists. It does not show the room is enough.
  - The Advocate concedes the BOTEC gives no breakdown of the $7M and that its adequacy "cannot be verified."
  - A defense whose central premise is "the number may be fine, but nobody can check" is not coverage. It is an absence of coverage.
- **The burden argument is symmetric.** The critique supplies no Phase III cost, and neither does the Advocate. Neither side has grounded the $6.7M as sufficient or insufficient.
- **The Advocate's two coverage arguments conflict.**
  - Under "existing coverage," the Advocate says SROI counts everyone's costs, so the "no payer" problem is handled.
  - Under "offsetting factors," the Advocate says WHO and national TB programmes may bear guideline and dissemination costs, so the "no payer" framing is wrong.
  - Both cannot hold. If all-in cost counts everyone's costs, shifting cost to national programmes does not shrink the required budget. It only means the $7M must already include those costs, which is the very thing nobody can verify.
- **The verifier evidence cuts against assumed safety.**
  - The record says "important questions need answering before a more expensive Phase III study."
  - That makes it hard to assume the safety and regulatory path is settled enough for a lean budget.
  - The TB-drug hepatotoxicity overlap, which the Advocate concedes, means a regulator or guideline committee has a specific reason to ask for monitoring.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: every dollar figure is ungrounded, the cited evidence shows only that a Phase III will exist, and the critique's own favourable-safety caveat undercuts the monitoring cost.

- **Conceded.** The critique has no measured cost datum. Its $5–20M, $4M and 70–300% figures are self-labelled illustrations. The verifier evidence confirms "it is not a budget figure."
- **The favourable-safety point does not cut as far as the Advocate suggests.**
  - The critique said monitoring is "likely a guideline-driven choice rather than a demonstrated necessity." It did not say monitoring is optional.
  - Guideline bodies make exactly those choices, and TB guidelines already include liver-function monitoring for first-line drugs. I cannot cite a specific document here, so treat that as background rather than evidence.
  - Early-phase safety data come from small trials, and the Phase IIc is itself running to resolve open questions. "Favourable so far" does not equal "monitoring not required."
- **The Advocate's atorvastatin point is self-disclaimed ("I cannot cite a specific study").** It addresses general safety, not the TB-specific interaction the Advocate concedes is real. The relevant question is whether co-administration with hepatotoxic TB drugs raises the monitoring burden, and baseline generic safety does not answer it.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: success-contingent post-adoption costs should be weighted by the 40% joint success probability. The critique's $4M illustration therefore has an expected cost of $1.6M, giving SROI ≈ 2,512x. Even the $20M end gives ≈ 1,440x.

I accept the arithmetic and the structural point. Contingent costs should not be treated as certain. The 0.4 weight is the wrong weight for much of what the critique describes, though, and the Advocate's conclusion depends on it.

- **0.4 is a joint probability, not a per-cost probability.**
  - The Advocate describes it as "Phase II and Phase III both succeed." Joint = P(II) × P(III|II), so P(II) ≥ 0.4 by construction.
  - Costs incurred after Phase II success but before Phase III resolves are therefore weighted at P(II) > 0.4. That includes regulatory interaction, in-trial hepatotoxicity monitoring and safety-database costs during Phase III.
  - Only fully post-Phase-III costs, such as guideline rollout and dissemination, are weighted at 0.4.
  - The critique's "regulatory" and "pharmacovigilance" items include the earlier category. I cannot ground the P(II)/P(III|II) split, so the correct weight for those items lies somewhere in [0.4, 1].
- **Break-even weights show where the argument turns.** Each is my derivation from the Advocate's figures: bar-cost $10.8M, base $7M, so headroom $3.8M.
  - For the $4M illustration: 7 + 4w = 10.8 gives w = 0.95. At 0.4 the critique fails, and only near-certainty of incurrence rescues it.
  - For the $20M end: 7 + 20w = 10.8 gives w = 0.19. At any plausible weight it crosses.
  - For an unweighted add-on at w = 0.4: the break-even is $3.8M / 0.4 = $9.5M. At w = 1 it is $3.8M.
  - The real dispute is therefore whether the nominal unfunded cost is above or below roughly $3.8M–$9.5M, depending on timing. The critique's $5–20M range straddles that band, but it is ungrounded, as the Advocate says.
- **The weighting asymmetry is also unresolved.**
  - The Advocate applies 0.4 to the add-on but takes the $7M as given, and admits "the BOTEC does not say how $7M was built."
  - If the $7M is already expected-value-weighted, the Advocate's calculation is right.
  - If it is a nominal budget, a consistent treatment would reweight the base too.
  - Which holds is not knowable from the record, so the 2,512x figure inherits that uncertainty.
- **Benefit scale and cost scale are tied together.**
  - The $54B figure presupposes successful adoption across TB-endemic countries. The cost of achieving that adoption is a single line inside the $7M, with no stated derivation.
  - Weighting by success probability fixes the timing of cost but not its scale. The success branch the 40% describes is the large-adoption branch, and that branch is where dissemination costs are highest.
  - This is a structural argument, not a number. I cannot ground a scale factor.
- **Minimum plausible magnitude.** It is near zero if existing WHO and national processes absorb the work at negligible incremental cost. That is not excluded, but the Advocate concedes it is also ungrounded.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: unvalued benefit channels (lung damage, post-treatment mortality, transmission, sweat diagnostic) can absorb cost upside, a lean Phase III is possible, and WHO or national programmes may carry guideline costs.

- **Benefit omissions are not in the model.**
  - They are implicit zeros per the parameter map, so they do not offset anything in the computed SROI. They are a separate argument that the SROI is understated.
  - They also come with a counterweight. The verifier evidence says efficacy is "mixed across statins," and the rosuvastatin result bears on benefit magnitude. Offsetting a cost-side risk with benefit-side upside, while benefit-side downside is also live, nets to unknown.
- **Lean Phase III and WHO cost-sharing are, by the Advocate's own labels, uninformed priors.** Neither is quantified or in the model. They cannot be netted against a critique that the Advocate also calls unquantified. They are symmetric speculation.
- **The WHO cost-sharing point conflicts with the Advocate's all-in-cost argument,** as shown above.

**KEY UNRESOLVED QUESTIONS:**
- How was the $7M built? Is it a nominal budget or probability-weighted, and what share is Phase III versus guideline work versus dissemination? Everything else depends on this.
- What are the P(Phase II success) and P(Phase III | Phase II) components of the 40%? This determines whether pharmacovigilance and regulatory costs are weighted near 0.4 or closer to 1.
- Is the nominal unfunded post-adoption cost above or below the $3.8M–$9.5M band? Nobody has grounded a figure on either side.
- Does the TB-drug hepatotoxicity overlap trigger guideline-mandated monitoring in practice, or only optional monitoring? The Phase IIc's open safety questions bear on this directly.
- Would WHO and national programme cost-sharing, if real, be counted in an "all-in" SROI? The Advocate has argued both ways.

### Judge Audit
Surviving strength: moderate
Justification: The exchange was more productive than most. Both sides showed their derivations, and the Challenger's break-even analysis and P(II) ≥ 0.4 argument were grounded refinements that the Advocate's single-weight calculation did not anticipate. Even so, the Challenger produced no grounded evidence that the $7M is actually inadequate. The critique's quantitative content was conceded as illustrative, its omission framing collapsed, and its "uses most of the $7M" claim rests on an unverifiable $320k and an unstated Phase III cost. What survives is a real structural concern, not a demonstrated error: an unexplained $7M sits only about 54% below the threshold-crossing cost, and timing-dependent weighting could erase the Advocate's cushion.
Recommended action: 2. SPECIFIC INVESTIGATION:
   - **Step 1 (most decisive, cheapest).** Obtain the derivation of the $7M all-in cost from the BOTEC author or grantee. Determine whether it is nominal or probability-weighted, how it splits across Phase III, guidelines and dissemination, and how the 0.4 joint probability splits into P(Phase II) and P(Phase III | Phase II). This alone determines whether the relevant break-even is closer to $3.8M or $9.5M.
   - **Step 2 (re-run the verifier with targeted searches).** Search for three reference-class costs:
     - Pivotal TB treatment trials, such as TBTC Study 31/A5349 and REMoxTB budgets.
     - Post-trial rollout and guideline-adoption costs for recent TB regimen changes, such as Unitaid or Global Fund funding for BPaL/BPaLM or 4-month rifapentine regimen introduction.
     - Whether WHO-recommended liver-function monitoring for first-line TB therapy already covers adjunct-drug pharmacovigilance at negligible incremental cost.

   Both steps are feasible with existing tooling. Until they are done, treat the $7M as a flagged uncertainty with modest headroom, and make no quantitative adjustment.
Action feasibility: requires_specified_evidence
Advocate failures: ['sound_synthesis_noted: The headroom calculation ($54B × 0.4 / 2,000 ≈ $10.8M bar-cost, about $3.8M or 54% headroom) uses only figures from the BOTEC and the critique, and each step is shown. The probability-weighting argument ($4M × 0.4 = $1.6M expected, SROI ≈ 2,512x) is explicitly conditional on the critique\'s own ungrounded figure. The Advocate states the caveat that the result is "only as good as the $4M figure" and that the build of the $7M is unknown. This is legitimate structural analysis, not guess-trading.', 'call_to_ignorance: Two offsetting factors are offered after being self-labelled as ungrounded.', 'false_definitiveness: The self-assessment reads "strong," while the body concludes "Partial defense." The body also concedes that the $7M "cannot [be shown] adequate" and that a $4M+ unweighted add-on breaks the bar. The self-rating is inconsistent with the Advocate\'s own analysis. I assess the defense as partial.', 'strawmanning: The general-safety point ("Atorvastatin is a long-established generic with extensive existing safety experience") answers a question nobody asked. The critique\'s concern is the TB-drug co-administration interaction, which the Advocate concedes is real, not baseline statin safety. The Advocate also flagged the point as uncited.']
Challenger failures: ['sound_synthesis_noted: The break-even analysis is clean and every step is shown.', 'strawmanning: Both cannot hold. If all-in cost counts everyone\'s costs, shifting cost to national programmes does not shrink the required budget." The Advocate\'s WHO point is most charitably read as *low incremental cost via existing processes*. That reading is fully compatible with all-in costing, and the Challenger\'s own "minimum plausible magnitude… near zero if existing WHO and national processes absorb the work" concedes as much. The inconsistency charge is partly valid on the Advocate\'s wording ("no payer framing… not established") but overstated.', 'whataboutism: The burden argument is symmetric. The critique supplies no Phase III cost, and neither does the Advocate." The burden of quantifying an under-budget claim sits with the critique. Noting that the defender also lacks a figure does not rehabilitate the critique\'s unsupported assertion that Phase III "uses most of" the $7M.', 'misrepresenting_evidence_status: The Challenger treats the verifier\'s "important questions need answering before a more expensive Phase III" as implying unsettled *safety and regulatory* questions. It then lists "the Phase IIc\'s open safety questions" as a key unresolved item. The verifier package does not say the questions are safety-related, and the Advocate notes that the Phase IIc tests dosing strategies. This reads content into the evidence that it does not contain.', 'call_to_ignorance: The success branch… is the large-adoption branch, and that branch is where dissemination costs are highest." This is a plausible structural point, but the Challenger explicitly cannot ground a scale factor. It is mild because it is disclosed.']
Debate resolved: - **Omission framing is dead.** The critique's omission framing does not survive: guideline, dissemination and Phase III costs are explicitly inside the $7M, so the critique is purely a magnitude claim. All of its dollar figures are ungrounded.
- **Decision band established.** The SROI clears the 2,000x bar unless the nominal add-on exceeds roughly **$3.8M** if the cost is incurred with certainty, or roughly **$9.5M** if it is incurred only in the 40% joint-success branch.
- **Weighting principle agreed.** Both sides agreed that success-contingent costs should be probability-weighted, with a weight between 0.4 and 1 depending on timing.
Debate unresolved: - **Size of the cost.** Neither side grounded whether the true nominal incremental cost falls below or above the $3.8M–$9.5M band.
- **Composition of the base.** It remains unclear whether the $7M is a nominal budget or already expected-value weighted, and how it splits across Phase III, guidelines and dissemination. The 2,512x figure depends entirely on this.
- **Incremental monitoring cost.** Neither side settled whether existing TB-programme liver monitoring makes the incremental pharmacovigilance cost near zero.

--- Critique: Unclear scope boundary for the sweat-diagnostic workstream ---

### Advocate
**DEFENSE OF GIVEWELL'S (CG's) POSITION: Unclear scope boundary for the sweat-diagnostic workstream**

**EXISTING COVERAGE:**
- The first branch of the critique's mechanism is "diagnostic costs excluded but diagnostic-linked benefits counted." The published BOTEC does not do this.
  - The benefit calculation values only on-treatment TB mortality: 19,900 deaths × 27 DALYs × $OP 100,000. The parameter map confirms "only mortality is valued" and that diagnostic value is an implicit zero.
  - So no diagnostic benefit sits in the numerator. A cost/benefit mismatch of the kind described cannot arise from this branch.
- The remaining branches are:
  - Diagnostic costs are inside the $7M. This is correct accounting.
  - Diagnostic costs are separate and benefits are not counted. This has no effect on SROI, as the critique itself says.
- The $7M is described as all-in. It covers "later Phase III trials, guideline changes, dissemination and validation." The BOTEC does not say whether "validation" includes diagnostic work, so I do not claim it does.
- The share arithmetic gives a consistency check. 4.5% × $7M ≈ $315K, which is close to the stated $320K current trial cost.
  - This suggests the grant's own spending is the numerator of the share.
  - If the grant funds the diagnostic work alongside the trial, as the context says, that work is plausibly already inside the $320K.
  - This is inference, not attestation.

**EVIDENCE WEAKNESSES:**
- The critique offers no evidence of any diagnostic budget. The sensitivity results are empty. The item is explicitly a clarification question and not a finding.
- The "Open Philanthropy listed as collaborator on the Phase IIC record" point concerns funding links. It says nothing about the size or accounting of the diagnostic budget.
- The one substantive piece of evidence is the exploratory sweat-test outcome inside ATORTUB. By the critique's own reading, this points to a low-cost add-on, which undercuts the threshold-breach scenario.
- If the Verifier left the scope question UNVERIFIABLE, that means no direct evidence either way. It does not support the "large separate budget" reading. I engage with that reading conditionally below.

**MAGNITUDE CHALLENGE:**
- The breach threshold derivation:
  - At the 2,000x bar, the maximum all-in cost is (0.4 × $OP 53.95B) / 2,000 ≈ $10.8M.
  - That is about $3.8M above the $7M. The critique's ~$3.7M is close.
- Conditional on a hidden diagnostic budget, the scenarios compare as follows:
  - The diagnostic would need to cost about $3.8M, roughly 12× the entire $320K trial cost.
  - A $0.32M diagnostic (doubling the grant-level cost) would give SROI ≈ $OP 21.58B / $7.32M ≈ 2,950x.
  - A $1M diagnostic would give ≈ 2,700x.
  - Both stay above the bar.
- A multi-million-dollar diagnostic program is an unlikely add-on to a $320K trial. Such a program would normally be a separate grant evaluated on its own BOTEC, with its own benefits and costs. That falls into the "separate, no effect" branch.

**OFFSETTING FACTORS:**
- Any added diagnostic cost would be paired with a real omitted benefit. The BOTEC values none of the following:
  - the diagnostic's value,
  - morbidity and lung-damage benefits,
  - post-treatment survival,
  - transmission effects.
- The parameter map flags these as implicit zeros. If the denominator moved up to include the diagnostic, consistent accounting would also move the numerator up. The net effect is not clearly negative.

**OVERALL ASSESSMENT:** Strong defense.
- The branch that would inflate SROI by miscounting benefits does not match the published BOTEC.
- The only branch that does matter (diagnostic spending omitted from the denominator while benefits are zero) needs a budget about 12× the trial cost to breach the bar.
- The critique's own evidence points toward a small budget.

**CONCESSIONS:**
- The BOTEC gives no breakdown of the $7M, so it cannot be confirmed that diagnostic spending is inside it. A clarification question is legitimate.
- The critique mis-specifies the mechanism, but a related real branch exists. If the grant funds diagnostic work that is excluded from the denominator, the cost side is slightly understated even with no diagnostic benefit counted. I judge this immaterial unless the diagnostic budget is large.
- I cannot ground the actual diagnostic budget. My claim that it is small rests on the critique's own reading of the ATORTUB evidence and on the $315K vs $320K share arithmetic.

### Challenger
REBUTTAL: Unclear scope boundary for the sweat-diagnostic workstream

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the "costs excluded, diagnostic-linked benefits counted" branch can't occur, because the BOTEC values only on-treatment TB mortality (19,900 deaths × 27 DALYs) and assigns the diagnostic an implicit zero.

Response:
- I concede that no line item in the BOTEC is labelled "diagnostic benefit."
- That does not settle whether the 19,900 deaths are diagnostic-linked. Whether the Phase III program, and so the mortality benefit, depends on the diagnostic is not documented. For example, the test could be a pharmacodynamic readout or a patient-selection tool that the later trials rely on.
- Neither the Advocate nor the Verifier shows that the mortality benefit is independent of the diagnostic. The Advocate has shown that the benefit is not explicitly attributed to the diagnostic, which is a weaker claim.
- I treat this as conditional. If the Phase III design uses the sweat test, the mismatch branch is live. If it does not, the Advocate is right.

> The Advocate claims: 4.5% × $7M ≈ $315K, close to the stated $320K trial cost, so the grant's own spending is the numerator of the share and diagnostic work is plausibly already inside it.

Response:
- The Advocate labels this inference. I add that it is a numerical coincidence, not a derivation. Nothing in the evidence package says how the 4.5% was built or that its numerator is the $320K.
- Even if the match is real, it only covers the current ATORTUB trial cost. The critique's concern is a "diagnostic workstream," which could extend past the exploratory outcome inside ATORTUB into development or validation.
- The Advocate admits the $7M's "validation" line is ambiguous on diagnostic work.
- So the share arithmetic supports "the exploratory sweat-test outcome is inside the trial cost." It says nothing about any larger diagnostic workstream.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the critique offers no evidence of a diagnostic budget, and the Open Philanthropy collaborator listing says nothing about size or accounting.

Response:
- Agreed on the collaborator listing. It shows a funding link and nothing about scope.
- The Advocate says the ATORTUB exploratory outcome "undercuts" the threshold-breach scenario. That evidence shows the sweat test is exploratory inside ATORTUB. It does not show that the diagnostic workstream is only that.
- The distinction matters because the critique asks about the workstream's boundary. The evidence bears on one component of it.
- The Verifier did not mark the scope question REJECTED. Absence of a budget figure is not evidence of a small budget.
- The Advocate handles this conditionally, which is appropriate. The conditional leaves the question open, and I concede it is not evidence for a breach.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: breaching the bar needs a ~$3.8M diagnostic, "roughly 12× the entire $320K trial cost," which is implausible as an add-on.

Response:
- I accept the arithmetic. The bar is 0.4 × $53.95B / 2,000 ≈ $10.8M, and the headroom is ≈ $3.8M.
- The baseline is wrong. The $7M is the all-in cost covering later Phase III trials, guideline changes, dissemination and validation. The relevant comparison is the headroom against the $7M, about 54%, not against the $320K current trial cost.
- A diagnostic cost that is trivial next to a Phase II trial could be material next to a Phase III-scale program. If the diagnostic workstream scales with later phases, the 12× framing overstates the implausibility.
- I cannot ground a figure for the cost of diagnostic validation. Treat any number I might offer as an uninformed prior.
- The Advocate's "separate grant with its own BOTEC → no effect" is an assumption about how CG structures grants. It restates the open question and does not answer it.
- Minimum defensible impact: zero. If the diagnostic is inside the $320K or the $7M, there is no effect. The critique's value is as a clarification flag, as it says itself.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: any added diagnostic cost would be paired with an omitted benefit (diagnostic value, morbidity, post-treatment survival, transmission), so the net effect is not clearly negative.

Response:
- The omitted benefits are real as a matter of conservatism. They are also implicit zeros, unquantified in the model, so they cannot offset a specific cost that moves the stated SROI.
- Consistent accounting would add the diagnostic's benefits to the numerator. That is a re-specification of the BOTEC. It is not an offset the published model contains.
- The offset also works against the Advocate's first-branch argument. If the diagnostic has no benefit in the numerator, adding its cost lowers SROI. If it has benefits, they belong in the numerator, and the "no diagnostic benefit counted" claim no longer applies.
- The Advocate can use one of these arguments or the other, but not both without qualification.
- Whether the sign is net negative depends on the unknown size of the diagnostic cost relative to its omitted benefits, and neither side has that figure.

**KEY UNRESOLVED QUESTIONS:**
- Does the Phase III design or the mortality benefit depend on the sweat test, for example for patient selection or response monitoring? If so, the benefit is diagnostic-linked.
- Does the 4.5% share have the $320K as its numerator, or is the $315K match coincidental?
- Does "validation" in the $7M include diagnostic validation, which would put the cost inside the denominator?
- Does the diagnostic workstream extend beyond the exploratory outcome inside ATORTUB? If so, what is its funding source and its accounting under CG's grant structure?

### Judge Audit
Surviving strength: weak
Justification: - The critique labelled itself small in magnitude, uncertain in sign, and lower priority than Critiques 1 and 2.
- The debate did not strengthen it. The Challenger conceded a zero floor, could not ground any diagnostic budget, and kept the material branch alive only through speculative conditionals.
- The Advocate's arithmetic shows that a breach would require roughly 54% headroom spent on an unevidenced component.
- The Challenger's best move, the baseline correction, weakens the Advocate's plausibility framing. It does not supply any positive reason to expect a large budget.
- The verdict is weak because the critique has little material content that survives. The debate itself was reasonably productive.
Recommended action: 1. **CONCLUDE NOW:** Make no adjustment to the SROI. This should stay a low-priority clarification item, with moderate-high confidence that the effect is immaterial.
   - Fold it into the existing CG clarification list as two yes/no questions:
     - (a) Does the $7M all-in figure include any sweat-diagnostic development or validation costs?
     - (b) Does the planned Phase III design use the sweat test for patient selection or response monitoring?
   - Only a "no" to (a) combined with a "yes" to (b) would reopen the question, and it would then need a diagnostic budget above about $3.7M.
   - Asking these questions is feasible at no marginal cost, because CG clarification questions are already being compiled.
Action feasibility: actionable_now
Advocate failures: []
Challenger failures: []
Debate resolved: Both sides agree on four points:
- **Breach threshold:** the cost headroom before SROI falls below 2,000x is about $3.7–3.8M.
- **Published model:** the BOTEC contains no explicit diagnostic benefit, so the critique's "costs excluded, benefits counted" branch can only arise if the mortality benefit itself depends on the diagnostic.
- **Budget evidence:** no evidence of any diagnostic budget exists, and the only relevant evidence (an exploratory outcome inside a 150-patient trial) points toward a small add-on.
- **Floor and status:** the minimum defensible impact is zero, and the item functions as a clarification flag rather than a finding.
Debate unresolved: - Whether any diagnostic workstream extends beyond the exploratory ATORTUB outcome.
- If it does, whether its costs sit inside the $7M "validation" or Phase III lines.
- Whether the Phase III design relies on the sweat test at all. The Challenger raised this, but only speculatively.

--- Critique: Reference-class check: TB Phase III trials, and the evidence package WHO may require, point to more than one trial ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION: Reference-class check, TB Phase III cost and the evidence package WHO may require

**EXISTING COVERAGE:**
- CG's $7M is explicitly "all-in." It covers the $320K Phase IIc trial plus "later Phase III trials, guideline changes, dissemination and validation." CG therefore did not omit the Phase III cost.
- CG computes SROI on all-in costs against all-in benefits, not on its own ~4.5% share. This already penalizes the estimate for costs that other funders might bear.
- Arithmetic check: 4.5% × $7M ≈ $315K, which matches the $320K trial. So CG's own spend is the Phase IIc trial, and the remaining ~$6.7M is the assumed cost of everything downstream.
- The Parameter Map says CG gives no breakdown of the $7M and no reconciliation with typical TB Phase III costs. I cannot point to an explicit CG justification, so coverage is real but thin.

**EVIDENCE WEAKNESSES:**
1. The reference class mixes trial types.
   - The $19M figure is a Phase III median across therapeutic areas.
   - The $23M figure is for anti-infective trials.
   - The €33.9M figure is TB-PRACTECAL, a novel-regimen registrational trial.
   - The critique's own evidence notes that TB-PRACTECAL's cost "included investment in trial infrastructure and medical expenditures not typical of standard clinical trials." That makes it an upper-end comparator for a generic adjunct, not a central one.
2. The critique concedes that endTB's $60M should be dropped. So the $20–60M range in the Mechanism section is wider than the evidence supports. The supportable range is $19–34M, and the critique itself calls that a mixed class.
3. The "multiple trials or IPD meta-analysis" requirement is, by the critique's own statement, UNGROUNDED, and the pregnancy-subgroup extra trial is probably not needed for statins. Taking that conditionally, I accept that more than one trial is possible. But the critique supplies no evidence that CG's single-Phase-III assumption is wrong, so the multiplier should not be applied.
4. The review's range is $7–221M, and $7M is its lower bound. The critique itself says "$7M is not impossible" and "not clearly implausible for a low-cost adjunct trial." Neither the Verifier nor the Quantifier produced a trial of a generic oral adjunct with a routine-care endpoint costing above $20M. The comparison is to analogues, not to a matched trial.
5. The critique labels its own direction "uncertain." Its central $30M is just the reference-class mean, with no adjustment for the cost drivers it identifies as favorable to CG.

**MAGNITUDE CHALLENGE:**
- Arithmetic: SROI = $54B × 0.4 / cost ≈ $21.6B / cost.
  - At $7M: ~3,090x.
  - At $19M: ~1,137x.
  - At $30M: ~720x.
  - At $60M: ~360x.
- The critique's "350–1,000x" range only holds at $20–60M, and the upper end is endTB-driven, which the critique itself says to drop. Dropping endTB gives ~$20–34M, or SROI of roughly 635–1,080x.
- A defensible adjusted range for a generic adjunct, between CG's $7M and the $19M cross-area median, is $7–19M. I cannot ground a narrower number than that, and a cost-driver adjustment from the $19M median toward $7M is my judgment, not a derived figure. Treat it as an uninformed prior.
- The $30M central estimate takes the mean of a heterogeneous class without adjusting for the drivers the critique says are favorable (generic drug, no manufacturing or novel-safety package, routine endpoint). It is therefore likely too high as a central value.

**OFFSETTING FACTORS:**
1. Generic atorvastatin costs essentially nothing as a trial drug. Novel-drug registrational trials carry drug supply, safety-package and regulatory costs that an adjunct trial may avoid. I cannot quantify the saving.
2. The critique's own evidence notes that a routine-care endpoint could cost well below $20M.
3. CG counts all-in costs but credits only 4.5% of benefits to itself, a conservative convention. If a public funder such as NIH or a Global Fund-type body pays much of the Phase III, the true cost to the counterfactual decision-maker is arguably lower than $7M-equivalent. The critique does not address this. I raise it conditionally because it is not grounded in the evidence package.
4. The critique only pushes downward on cost. It does not consider that the $7M may also cover the sweat-diagnostic workstream, which would make the Phase III share even smaller. The Parameter Map flags this as unclear.

**OVERALL ASSESSMENT:** Partial defense, leaning toward weak on the final numbers.
- The critique's central $30M and 700x are overstated, because they average over trial types with different cost drivers and rely partly on a figure the critique itself says to drop.
- But the break-even is $21.6B / 2,000 ≈ $10.8M. Any all-in cost above about $10.8M puts SROI below the 2,000x bar.
- Even my adjusted range of $7–19M straddles that threshold, so the conclusion is fragile and depends on a cost estimate CG never justified.

**CONCESSIONS:**
1. $7M is at the bottom of the published range ($7–221M), and CG gives no breakdown or reconciliation. That is a genuine transparency gap.
2. The break-even cost is only ~$10.8M, about 1.5× CG's figure. The finding is material even with the critique's overstatements removed.
3. A Phase III powered for mortality at CG's own assumed effect would be very large. Taking 6% baseline mortality and a 10% relative reduction (5.4%), the standard two-proportion formula (α = 0.05, 80% power) gives roughly 23,000 per arm, or ~47,000 total.
   - Derivation: n per arm ≈ (1.96+0.84)² × (0.06×0.94 + 0.054×0.946) / 0.006² ≈ 7.84 × 0.1075 / 0.000036.
   - A trial that size is unlikely to cost $7M. So either the Phase III uses a surrogate endpoint, which weakens the evidence for 60% uptake and for the 40% success probability, or the cost is higher.
   - This supports the critique's concern and interacts with p_success and uptake, which the critique does not itself note.
4. The cost-driver adjustment in my magnitude section is my judgment and not derived from a matched-trial cost, so the true central estimate could sit anywhere between ~$7M and ~$30M.

### Challenger
REBUTTAL: Reference-class check, TB Phase III cost and the evidence package WHO may require

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: CG's $7M is explicitly all-in, covering the Phase IIc trial plus later Phase III, guidelines and dissemination. Coverage is therefore "real but thin," not omitted.

- I concede that CG did not omit downstream costs. The question is whether $7M is a credible number for them.
- The Advocate's own arithmetic undercuts the coverage claim. The Phase IIc is ~$320K, so about $6.7M must cover the Phase III, guideline changes, dissemination and validation together.
- The reference class ($19M median, $23M anti-infective, €33.9M TB-PRACTECAL) is for a single Phase III alone.
- The $7M review minimum is therefore being compared against a Phase III-only number, while CG's $7M also has to fund everything else. The gap is larger than the critique's framing suggests.
- "Coverage is real" is true of scope but says nothing about adequacy. The Advocate concedes there is no breakdown and no reconciliation. The all-in convention penalizes the benefit side only if the cost figure is itself sound.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the reference class mixes trial types, endTB should be dropped, no matched generic-adjunct trial above $20M has been produced, and the multi-trial multiplier is ungrounded.

1. **Mixed reference class.**
   - Conceded as a reason to discount TB-PRACTECAL. The critique already says so.
   - It does not move the lower anchors. The $19M cross-area median and $23M anti-infective figure are not novel-drug-specific, and both sit above the $10.8M break-even the Advocate computed.
2. **endTB.** Conceded. The critique itself drops it, so the $20–60M range should be read as ~$20–34M.
3. **"No matched trial above $20M was produced."**
   - This is an argument from absence. The Verifier's package says the $7M is "not impossible" and the counterargument "stands." It does not say a matched trial was searched for and found cheap.
   - Neither side has a matched comparator. The Advocate's "$7–19M" range is, by the Advocate's own admission, an uninformed prior.
   - The only grounded points are that $7M is the minimum of a $7–221M range and that the median is $19M. A project whose budget sits at the minimum needs a reason to be there. CG supplied none.
4. **Multi-trial multiplier.**
   - Conceded as ungrounded. The Advocate says the multiplier "should not be applied," and I agree it should not be applied as a central case.
   - The Advocate also says the critique "supplies no evidence that CG's single-Phase-III assumption is wrong." That shifts the burden. The multiplier is an upside risk to cost, not a basis for the central estimate. The central issue is the single-trial cost.
5. **Mortality-powered trial, the Advocate's Concession 3.**
   - I checked the derivation. With 6% vs 5.4%, n ≈ 7.84 × 0.1075 / 0.000036 ≈ 23,400 per arm, or ~47,000 total. The arithmetic is correct. The 6% baseline and 10% reduction are the Advocate's assumptions, which I have not verified against CG's parameters.
   - Sensitivity at a 20% relative reduction (6% vs 4.8%):
     - n ≈ 7.84 × (0.0564 + 0.0457) / 0.000144 ≈ 5,560 per arm, or ~11,100 total.
     - $7M all-in across ~11,100 patients is ~$630 per patient, and that must also fund guidelines and dissemination.
   - At the Advocate's 47,000, $7M is about $150 per patient all-in.
   - The Advocate is right that this creates a dilemma. Either the cost is higher than $7M, or the endpoint is a surrogate, which weakens the p_success and uptake assumptions. Both resolutions lower SROI. The Advocate's concession is more damaging to CG's $7M than the Advocate's final assessment allows.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: a defensible range is $7–19M, the $30M central is too high, and SROI at endTB-free costs is ~635–1,080x.

- I concede the $30M / 700x central is more aggressive than the evidence supports once the favorable cost drivers are weighed. A central estimate between $15M and $25M is more defensible.
- At the Advocate's own range endpoints:
  - $19M gives ~1,137x.
  - The break-even is ~$10.8M.
  - The median of the Advocate's $7–19M interval is ~$13M. That gives $21.6B / $13M ≈ 1,660x, still below 2,000x.
- The Advocate concedes the SROI conclusion is "fragile." Using only the Advocate's own range, the 2,000x bar fails over roughly two-thirds of the interval, from $10.8M to $19M.
- The minimum defensible impact is that SROI is no longer a comfortable 3,000x. It becomes ~1,100–2,000x unless one assumes the all-in cost sits in the bottom ~$4M of the Advocate's own range.

**RESPONSE TO "OFFSETTING FACTORS":**

1. **Generic drug cost.**
   - The Advocate admits it cannot quantify the saving. In a large outcome trial, drug supply is typically a minor share relative to site costs, follow-up and monitoring. I cannot ground that share from the evidence package, so treat it as an uninformed prior.
   - The Verifier's note that routine-care endpoints "could" cost well below $20M is a possibility, not a measured cost. Even at "well below $20M," the break-even is $10.8M.
2. **Routine-care endpoint.** This is the same point as above, so it is not an independent offset.
3. **Public-funder cost-sharing.** This is internally inconsistent with the Advocate's own Existing Coverage section.
   - CG's SROI uses all-in costs. Who pays does not change the denominator.
   - The Advocate says the "true cost to the counterfactual decision-maker is arguably lower than $7M-equivalent." That is a different metric from the all-in SROI under dispute, and it is ungrounded.
   - It is not an offset to the all-in critique.
4. **Sweat-diagnostic workstream.**
   - The Advocate presents this as a CG-favorable offset. It is not.
   - If $7M also funds the diagnostic workstream, the Phase III budget is even smaller than $6.7M. That makes it less plausible against a ≥$19M reference class, which supports the critique.

**KEY UNRESOLVED QUESTIONS:**
- What endpoint and sample size does CG's $7M Phase III assume? If it is mortality-powered, the Advocate's ~47,000 (or ~11,000 at 20% effect) implies a very low per-patient cost. If it is a surrogate, how does that change p_success and uptake?
- How is the $7M split between the Phase III, guideline and dissemination work, and any diagnostic workstream? Without a split, the $7M cannot be compared to a Phase III-only reference class.
- Is there any matched pragmatic trial of a generic adjunct in TB or a similar infectious disease with a published cost? Neither side produced one. This is UNVERIFIABLE, not REJECTED. Its absence does not confirm that $7M is realistic.
- Does WHO's evidence standard for a TB host-directed therapy require more than one trial? The critique marks this ungrounded and the Verifier did not resolve it. It affects the upside risk to cost but not the central case.

### Judge Audit
Surviving strength: moderate
Justification: - **Grounded work on both sides.** Both sides did genuine analytic work. The break-even calculation, the Phase III-only versus all-in mismatch, and the conditional sample-size dilemma are all sound syntheses.
- **What did not survive.** The critique's specific quantitative claim ($30M, ~700x) did not survive. The Challenger conceded it.
- **What strengthened.** The underlying concern grew stronger: CG's figure sits at the published minimum with no breakdown, and the threshold is only ~$10.8M.
- **Weaknesses on each side.**
  - The Challenger's attempt to rescue a higher central estimate leaned on a mischaracterization of the $19M median and on midpoint-of-uninformed-prior reasoning.
  - The Advocate overconceded the mortality-endpoint dilemma and missed the treatment-outcome-endpoint defense.
- **Net.** The direction (SROI plausibly below the bar) is supported, but the magnitude remains genuinely open.
Recommended action: 2. SPECIFIC INVESTIGATION:

1. **Obtain CG's breakdown of the $7M.** This means the split between the Phase III, guideline and dissemination work, validation, and any sweat-diagnostic workstream, plus the planned Phase III design (primary endpoint, target sample size). The StAT-TB protocol, already cited by the verifier, is the first place to look. This is feasible via direct request or protocol review.
2. **Run targeted verifier searches for published per-patient costs of pragmatic or routine-care-embedded RCTs** of repurposed generic adjuncts in TB or comparable infectious diseases. Candidate sources are EDCTP- or NIH-funded host-directed therapy trials, pragmatic statin outcome trials, and NIH RePORTER award amounts for Study 31 and TRUNCATE-TB. This is feasible with existing tooling.

**Interim conclusion (moderate confidence):**
- Discard the critique's $30M / 700x central estimate.
- Flag that CG's SROI exceeds 2,000x only if all-in costs stay below ~$10.8M, a figure CG has not justified.
Action feasibility: requires_specified_evidence
Advocate failures: ["sound_synthesis_noted: SROI ≈ $21.6B / cost, with values at $7M, $19M, $30M and $60M, and break-even ≈ $10.8M at the 2,000x bar. Each step is shown and follows from stated inputs. This break-even became the debate's central anchor.", 'sound_synthesis_noted: Concession 3\'s sample-size calculation is arithmetically correct: (1.96+0.84)² × 0.1075 / 0.000036 ≈ 23,400 per arm. However, the inputs (6% baseline mortality, 10% relative reduction) are attributed to "CG\'s own assumed effect" but do not appear in the verifier package. The derivation is sound only conditionally. It should have been labeled as resting on unverified parameters.', 'call_to_ignorance: Neither the Verifier nor the Quantifier produced a trial of a generic oral adjunct... costing above $20M." The Advocate uses the absence of a matched expensive comparator as support for $7M being plausible. No matched cheap comparator exists either, so this cuts both ways. The Challenger correctly flagged it.', 'false_definitiveness: The Advocate calls the $7–19M range "an uninformed prior" with no derived narrowing. It then asserts $30M is "likely too high as a central value" and that the critique\'s central figure is "overstated." The direction of the adjustment is reasonable. The confident conclusion still rests on a range the Advocate itself disclaims.', 'unsupported_estimate_fabricated: Offsetting factor 3 claims the "true cost to the counterfactual decision-maker is arguably lower than $7M-equivalent." This has no grounding, as the Advocate admits. It also contradicts the Advocate\'s own Existing Coverage point that CG uses all-in costs.']
Challenger failures: ['sound_synthesis_noted: The Challenger notes that the ~$6.7M remaining after the Phase IIc must cover the Phase III plus guidelines, dissemination and validation, while the reference class is Phase III-only. This is a grounded, correct point that sharpens the critique.', 'sound_synthesis_noted: The sensitivity check at a 20% relative reduction (≈5,560 per arm, ~11,100 total, ~$630 per patient all-in) is arithmetically correct. It is explicitly conditioned on unverified Advocate inputs. This is good practice.', 'misrepresenting_evidence_status: The $19M cross-area median and $23M anti-infective figure are not novel-drug-specific.', 'unsupported_estimate_counter: A central estimate between $15M and $25M is more defensible." No derivation is given. It is offered to replace both the critique\'s $30M and the Advocate\'s $7–19M.', "unsupported_estimate_pseudo: The median of the Advocate's $7–19M interval is ~$13M... the 2,000x bar fails over roughly two-thirds of the interval.", 'unsupported_estimate_fabricated: In a large outcome trial, drug supply is typically a minor share relative to site costs." The Challenger does acknowledge it is an uninformed prior. It still serves as the substantive rebuttal to the generic-drug offset.', 'false_definitiveness: The minimum defensible impact is that SROI... becomes ~1,100–2,000x unless one assumes the all-in cost sits in the bottom ~$4M." This is framed as a floor, yet it is built on the same uninformed range and the midpoint reasoning flagged above.']
Debate resolved: - **Points of agreement:**
  - endTB's $60M is not a trial cost.
  - The critique's $30M / ~700x central estimate is overstated, because it averages a heterogeneous, novel-drug-weighted reference class.
  - The multi-trial multiplier is an ungrounded upside risk, not a central case.
- **Points established through grounded arithmetic:**
  - Break-even all-in cost is ~$10.8M, only ~1.5× CG's figure.
  - CG's $7M is unreconciled and must cover more than a single Phase III.
  - The conclusion is therefore fragile even if the critique's overstatements are removed.
Debate unresolved: - **The real cost of the Phase III.** What a pragmatic Phase III of a generic oral adjunct with a routine-care endpoint would actually cost is unknown. Neither side produced a matched comparator, and both "central" ranges ($7–19M, $15–25M) are ungrounded.
- **Endpoint and sample size.** Whether CG's assumed Phase III is mortality-powered, which would imply implausibly low per-patient cost, or uses a TB treatment-outcome endpoint is unsettled. So is whether the latter would actually weaken p_success and uptake.

--- Critique: The speedup benefit and the all-in cost come from different counterfactuals. Every coherent framing gives roughly 10–20x higher SROI. ---

### Advocate
```
DEFENSE OF GIVEWELL'S (CG's) POSITION: Speedup benefit and all-in cost come from different counterfactuals

EXISTING COVERAGE:
- The BOTEC does not hide the structure. It states a 1-year acceleration, all-in costs (~$7M including Phase III, guidelines and dissemination), and the 4.5% credit-share convention. The Parameter Map notes "No time discounting." The pairing the critique targets is therefore deliberate and visible.
- The BOTEC's "1 year" is not defined as a pure time-shift. It could be an expected effective acceleration that blends a "pathway happens a bit later" branch with a "pathway never happens" branch. Nothing in the report rules this out. The critique's key premise ("if that is what the BOTEC does") is flagged by the Quantifier itself as unconfirmed.
- Derivation showing the blended reading can reproduce the BOTEC. Take the critique's own figures: H = effective PV benefit-years if the grant is pivotal for the drug existing at all, with H ≈ 1/(0.04+0.02) × 0.65 ≈ 16.7 × 0.65 ≈ 10.8. Let q = probability the grant is pivotal and d = delay in the other branch. Effective years E = q·H + (1−q)·d.
  - d = 1 gives E = 1 only at q = 0.
  - d = 0.5 gives E = 1 at q ≈ 0.5/10.3 ≈ 5%.
  - d = 0 gives E = 1 at q ≈ 1/10.8 ≈ 9%.
  - q = 25% with d = 1 gives E ≈ 3.5, and q = 50% gives E ≈ 5.9.
- So the BOTEC's 1 year is coherent for q up to roughly 5–9%. The critique's 10–18× on the benefit side needs q near 1. "Every coherent framing gives 10–20×" is therefore too broad as stated. I cannot ground q in either direction; treat it as an uninformed prior.
- The attribution convention (credit ≈ cost share, 4.5%) is a standard way to split credit when the trial and the downstream Phase III are complements. It is conservative if CG is actually pivotal. It is not an arithmetic error.

EVIDENCE WEAKNESSES:
- The critique concedes it has no external empirical evidence. The 10–20× is hand arithmetic, and the Sensitivity Results field is empty, so nothing was run on a replica of the formula chain.
- The multiple rests on three assumptions the critique admits it "had to assume":
  - r = 4%. The BOTEC uses 0%, so this is an imported value.
  - A "delay factor" of 0.6–0.7 that the critique calls unexplained. 1.04^-8 ≈ 0.73 and 1.04^-10 ≈ 0.68, so it may be discounting to the adoption year plus a ramp, but this is my reading. If so, it is double-counted against any separate discount in the cost term.
  - An effectively unbounded benefit horizon. The 1/(r+g) formula extends the 2% case decline indefinitely, but the BOTEC specifies that decline only until Phase III ends.
- The critique's own statin evidence cuts against a long horizon and a high p_success. ROSETTA found rosuvastatin 10 mg safe but with no substantive culture-conversion benefit overall, and its PET-CT analysis showed no microbiological or radiological effect. The phase IIA atorvastatin study showed only reduced sputum mycobacterial load. This is evidence on level, not on the ratio logic, but it bears on whether a 17-year horizon is plausible.
- The report mixes two outputs. The Hypothesis says to report an "illustrative range, not as 30,000–55,000×". The Mechanism says "the number to report is the coherent ratio." The Evidence section calls 30,000–55,000× an "upper-bound illustration only." The critique has not settled on what it asserts.

MAGNITUDE CHALLENGE:
- The 10–20× uplift is the upper end of a continuum. On the benefit side, E runs from 1 (q = 0) to about 11–18 (q ≈ 1). At q = 25–50% the uplift is about 3.5–6×, not 10–20×. The critique has not shown that q is near 1.
- Horizon constraints push down. Regimen obsolescence (e.g., 4-month regimens, per the Parameter Map), vaccine or incidence shocks, and non-confirmatory mortality results could each shorten the effective horizon. The critique concedes the ranking holds only for horizons above ~1.5–2 effective years, but the multiple falls proportionally below the 17-year case. A 5-year effective horizon gives only about 4–5 discounted benefit-years.
- Displacement is unquantified, and the critique says it is "medium once displacement is applied." It applies mainly in the never branch, where other funders' ~$6.7M is a real cost. The critique gives no figure, so its "large conceptually, medium once displacement is applied" cannot be checked.
- The critique stacks p_success on top without adjusting it. Given the ROSETTA nulls, the 40% joint success probability is not conservative for a sped-up drug that may fail to reach Phase III success. The critique says this "lowers the level but not the ratio logic". That is correct, but the level is what the bar comparison uses.

OFFSETTING FACTORS:
- Any upward revision from the framing comes with downward pressures the critique names but does not net out:
  - horizon limits (obsolescence, vaccines, regimen changes)
  - displacement of other funders' dollars
  - a statin-specific risk of failure (ROSETTA)
  - discounting of a benefit stream that starts ~8 years out
- The Parameter Map lists further unmodelled downward factors: uptake ramp rather than an instant 60%, no delivery costs, no adverse-event management, and a possible zero or negative effect. If these are included in a coherent time-shifted or never-branch framing, they reduce PV_B or raise PV_C, shrinking the uplift.
- The BOTEC's omitted benefit channels (morbidity, post-treatment survival, transmission, diagnostics) push the other way. They sit outside this critique and do not rescue the framing mismatch.

OVERALL ASSESSMENT: Partial defense, leaning weak on direction.
- Strong on magnitude and framing breadth. The "10–20× under every coherent framing" claim is unsupported, because the benefit-side uplift depends on an ungrounded pivotality probability q and an assumed horizon.
- Weak on direction. In the extreme "pure delay" branch (q = 0), the correct cost is incremental, about $320k rather than $7M, because the other funders' spending occurs in both worlds. That is a ~22× uplift (7/0.32 ≈ 21.9). In the extreme "never" branch (q ≈ 1) with all-in cost, the uplift is about 11–18×. Only the mixture the BOTEC appears to use (1 year of benefit against all-in cost) is internally mismatched, and it is conservative either way.

CONCESSIONS:
- If the BOTEC's 1 year means a pure time-shift of the whole pathway, charging all-in cost (including other funders' Phase III spending) is incoherent. The all-in cost would be incurred in both worlds, so the framing understates SROI.
- If the grant is the pivotal link, so that Phase III funding is conditional on the Phase IIc result and the pathway would otherwise never occur, the BOTEC understates the benefit stream by roughly an order of magnitude on the critique's own horizon assumption.
- The BOTEC gives no derivation of "1 year," no definition of the counterfactual, and no discounting. A reader cannot tell which framing was intended. This is a documentation weakness even if the number is defensible.
- I cannot ground q, d, the delay factor, or the effective horizon. The right response is to report the framing as unresolved and give a wide illustrative range (about 3× to 20× uplift, conditional on q and horizon). The critique's 10–20× / 30,000–55,000× headline should not be adopted as a point estimate.
```

### Challenger
REBUTTAL: Speedup benefit and all-in cost come from different counterfactuals

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the BOTEC's "1 year" may be a blended expected acceleration. It is consistent with the BOTEC only if the probability q that the grant is pivotal is about 5–9%. At realistic q (25–50%) the uplift is only about 3.5–6×, so "every coherent framing gives 10–20×" is too broad.

1. **The Advocate blends the benefit but not the cost.** The Advocate's own concession says the pure-delay branch has an incremental cost of about $320k, because other funders' Phase III spending happens in both worlds. If the benefit is a mixture over branches, the cost must be the same mixture:
   - Expected cost C(q) = q·$7M + (1−q)·$0.32M.
   - The Advocate's "3.5–6×" divides the blended E by the full $7M at every q. That is the same mismatch the critique identifies, reintroduced inside the Advocate's rebuttal.

2. **Redoing the Advocate's own table with matched costs.** I use the Advocate's H ≈ 10.8 and d = 1. The uplift is (E/C) ÷ (1/7), with C in $M.

| q | E = q·10.8 + (1−q)·1 | C = 7q + 0.32(1−q) | Uplift |
|---|---|---|---|
| 0 | 1.0 | 0.32 | 21.9× |
| 0.05 | 1.49 | 0.654 | 15.9× |
| 0.25 | 3.45 | 1.99 | 12.1× |
| 0.50 | 5.9 | 3.66 | 11.3× |
| 1.0 | 10.8 | 7.0 | 10.8× |

   - With d = 0.5 the uplift is still about 10.8× at both q = 0 and q = 0.5.
   - So at the critique's horizon, the 10–20× range holds across the whole q range. The Advocate's claim that it needs q near 1 is an artifact of the cost mismatch.

3. **The Advocate's "BOTEC is coherent for q ≤ 5–9%" does not rescue the BOTEC.** At q = 9% with d = 0, the blended cost is about $0.92M, not $7M. The BOTEC's 1 year against $7M is still about 7× too low. The BOTEC is coherent only if q ≈ 0 and the cost is also all-in, and that combination is the one the Advocate concedes is incoherent.

4. **The 4.5% credit-share convention is not separate conservatism.** The CG cost is about $320k, and $0.32M/$7M ≈ 4.6%. Applying 4.5% of the benefit against CG's own cost is arithmetically the same as full benefit against all-in cost. It does not independently protect the BOTEC from the counterfactual question.

5. **The Advocate's conclusion contradicts its own concession.** It labels the defense "partial, leaning weak on direction" and concedes the BOTEC "is conservative either way." Yet it still argues the framing is internally defensible. Those two positions are hard to hold together.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the 10–20× is hand arithmetic resting on three imported assumptions (r = 4%, an unexplained delay factor of 0.6–0.7, an unbounded horizon). The delay factor may be double-counted against cost discounting, and the 2% decline is specified only until Phase III ends.

1. **The "no external evidence" objection does not apply here.** The verifier marked the core argument as needing no external evidence, and found nothing contradicting it. The argument is an arithmetic consistency check on pairing a benefit with a cost. The Advocate's own spreadsheet-style derivation above confirms the structure.

2. **The 2%-decline objection cuts the wrong way.** If the decline applies only until Phase III ends, benefits decay less than the critique assumed.
   - Without the decline and with r = 4%, the critique already gives about 18× (verifier-listed mechanism).
   - Undiscounted at r = 0 with only a 2% decline, 1/g = 50 benefit-years. That is larger still.
   - Both imported assumptions (r = 4%, indefinite decline) lower the uplift relative to a literal reading of the BOTEC. The critique's 10–11 benefit-years is the conservative side.

3. **The double-counting claim is speculative and structurally unlikely.**
   - The Advocate says it is "my reading". The delay factor acts on the timing of the benefit stream (about 1.04^-8 to 1.04^-10).
   - The ÷0.85 adjustment acts on the timing of Phase III spending.
   - These are different streams, so they are not double-counted. The Advocate offers no demonstration that they are.

4. **The statin evidence bears on the level, not the ratio.** The Advocate concedes this ("This is evidence on level, not on the ratio logic").
   - p_success enters both the BOTEC and any coherent framing, so it cancels in the uplift multiple.
   - ROSETTA (rosuvastatin 10 mg: safe, no substantive culture-conversion benefit overall, no PET-CT effect) versus the phase IIA atorvastatin result (reduced sputum mycobacterial load) shows class and dose uncertainty. It does not show the multiple is wrong.
   - I concede it may affect whether a 17-year horizon is realistic.

5. **The critique's reporting inconsistency is fair but minor.** Its Hypothesis, Mechanism and Evidence sections do disagree about the headline format. The Hypothesis and Evidence sections both call for an illustrative range or upper bound. That is the format both sides now agree on, and it does not affect the substance.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

1. **Minimum plausible multiple, long horizon.** From the table above, 10.8× at q = 1 is the floor on the critique's assumptions, and the multiple is higher at lower q. I cannot ground q, so I do not claim a point estimate within 11–22×.

2. **Short horizon.** I concede the Advocate's point here.
   - A 5-year effective horizon gives about 4–5 discounted benefit-years.
   - At q = 1 that gives a 4–5× uplift. At q = 0 with d = 1 it is still about 22×, since the cost is incremental.
   - Even at the pessimistic corner (q = 1, short horizon), the uplift is above 1×. The direction survives in every cell I can construct, with the possible exception of d = 0 and q near 0, where nothing is gained.

3. **Displacement is partly already priced in.**
   - In the never branch, the all-in cost already charges other funders' $6.7M at par. That is displacement at a 1:1 value ratio.
   - Residual displacement exists only if those dollars would have bought something more cost-effective than CG's marginal dollar.
   - In the delay branch, displacement is zero, because the money is spent in both worlds.
   - So displacement does not "pull the ratio back down" without an argument that other funders' alternative uses beat CG's. The critique's hypothesis wording ("treating other funders' dollars as free") is inaccurate, and I do not defend it. The all-in cost does not treat them as free.

4. **The p_success point.** The Advocate says the "level is what the bar comparison uses." Halving p_success halves both the BOTEC and the coherent SROI.
   - A 3,050× BOTEC implies roughly 33,000× on the critique's 11× multiple.
   - Whether a given p_success reduction changes the bar comparison depends on the bar. I cannot ground the bar from the materials, so I make no claim here.

**RESPONSE TO "OFFSETTING FACTORS":**

1. **Most of the listed offsets are level adjustments, not differential adjustments.** Uptake ramp, adverse-event management, delivery costs and a possible zero or negative effect affect the BOTEC's 1 year and the coherent framing similarly. They do not specifically close the gap between the two.

2. **Delivery costs are the partial exception, and I concede it.** Delivery costs scale with benefit-years, so they would erode a longer-horizon framing more than a one-year framing. The Advocate has not quantified this and neither can I.

3. **Horizon limits and discounting.**
   - Discounting is already in the critique's 10–11 benefit-years.
   - Obsolescence and vaccine shocks are real downward pressures, but unquantified in the Advocate's own defense. They are not a reason to leave the 1-year-vs-all-in pairing unchanged.

4. **Omitted upside channels push the same direction.** The Advocate concedes that morbidity, post-treatment survival, transmission and diagnostics push upward. Net, the unmodeled factors are roughly two-sided, while the framing mismatch is one-directional.

**KEY UNRESOLVED QUESTIONS:**

- What does the BOTEC's "1 year" represent: a pure delay, a never-vs-ever mixture, or an unexplained input? The Quantifier has not confirmed this against the CEA.
- What is the probability q that the Phase IIc result is pivotal for Phase III funding? Neither side can ground it. Once costs are matched to branches, the uplift is fairly insensitive to q (about 11–22× at a 17-year horizon).
- What is the realistic effective benefit horizon after regimen obsolescence, statin class and dose uncertainty, and incidence shifts? This is the dominant parameter, with an uplift of about 4–5× at 5 years versus about 11× at the critique's horizon.
- Do other funders' Phase III dollars have an alternative use more cost-effective than CG's marginal dollar? If not, the all-in cost already prices displacement and the "medium once displacement is applied" qualifier has little force.

### Judge Audit
Surviving strength: moderate
Justification: The Challenger made a grounded, correctly computed argument (the matched-cost table) that the Advocate's central magnitude defense could not withstand. This establishes the *direction* of the critique firmly and shows the uplift is roughly q-insensitive at long horizons. However, the critique's headline claim ("every coherent framing gives 10–20×") did not survive intact: the Challenger itself conceded the uplift falls to ~4–5× under a short horizon. Its foundational premise about what the BOTEC's "1 year" represents also remains UNVERIFIABLE against the CEA. Strong on direction, contingent on horizon for magnitude, so moderate overall.
Recommended action: 1. CONCLUDE NOW: With moderate-to-high confidence, the BOTEC's pairing of a 1-year speedup benefit with all-in program cost is internally inconsistent and conservative in direction. Under any coherent branch-matched framing, SROI is higher than ~3,050×. The magnitude should be reported as a horizon-conditional range rather than a point estimate:
   - roughly 4–5× uplift at a ~5-year effective horizon;
   - roughly 11× at the critique's ~17-year horizon;
   - up to ~20× in the pure-delay corner, which is likely overstated because the time cost of accelerated other-funder spending is omitted.

   Two concrete steps follow, both feasible with existing materials:
   - **Confirm against the CEA** whether "1 year" is defined as a pure delay or a mixture, and whether the $7M is all-in cost. This is the one premise that could overturn the direction claim.
   - **Rebuild the q × horizon sensitivity table** (q ∈ {0, 0.25, 0.5, 1}; horizon ∈ {5, 10, 17+} years). Use branch-matched costs and include the discounted time cost of accelerating other funders' ~$6.7M.
Action feasibility: actionable_now
Advocate failures: ['unsupported_estimate_pseudo: The table "q = 25% with d = 1 gives E ≈ 3.5, and q = 50% gives E ≈ 5.9", and the conclusion that "at q = 25–50% the uplift is about 3.5–6×", divide a branch-blended benefit by the full $7M all-in cost at every q.', 'unsupported_estimate_pseudo: BOTEC\'s 1 year is coherent for q up to roughly 5–9%". This derivation also holds cost at $7M across the mixture. Once costs are blended consistently, the coherence claim does not follow.', 'call_to_ignorance: The delay factor "may be discounting to the adoption year plus a ramp... If so, it is double-counted against any separate discount in the cost term." The Advocate concedes this "is my reading".', "sound_synthesis_noted: Several pieces of the Advocate's defense are grounded:", 'sound_synthesis_noted: A 5-year effective horizon gives only about 4–5 discounted benefit-years" is roughly correct (Σ1.04^−t over 5 years ≈ 4.45). If the 0.6–0.7 delay factor is also applied it would be nearer ~3, so the estimate is if anything generous to the critique.']
Challenger failures: ["sound_synthesis_noted: The matched-cost table C(q) = 7q + 0.32(1−q) reproduces correctly from the Advocate's own inputs (H ≈ 10.8, d = 1). It gives 21.9×, 15.9×, 12.1×, 11.3× and 10.8×, and the d = 0.5 checks also hold (~10.8–10.9×).", 'sound_synthesis_noted: $0.32M/$7M ≈ 4.6%... Applying 4.5% of the benefit against CG\'s own cost is arithmetically the same as full benefit against all-in cost." This is a correct and important equivalence. It shows the credit-share convention does not independently shield the BOTEC.', 'unsupported_estimate_pseudo: The q = 0 corner (21.9×) and "uplift is fairly insensitive to q (about 11–22×)" have two weaknesses:', 'strawmanning: The Advocate\'s conclusion contradicts its own concession... Yet it still argues the framing is internally defensible." This is partial. The Advocate\'s final position was that the "10–20× under every coherent framing" claim is too broad, and it explicitly conceded the BOTEC\'s mixture is mismatched. The Challenger overstates the inconsistency.', 'false_definitiveness: Net, the unmodeled factors are roughly two-sided, while the framing mismatch is one-directional." The "roughly two-sided" balance is asserted, not derived. Neither side quantified morbidity, transmission, delivery costs or obsolescence.', 'misrepresenting_evidence_status: On displacement, the Challenger states "In the delay branch, displacement is zero" and that displacement "has little force". It does so without engaging the verifier\'s explicit caveat that, if displaced money would fund equally cost-effective research, the delay benefit "shrinks toward zero".']
Debate resolved: Once costs are matched to the same counterfactual branch as benefits, the BOTEC's pairing of "1 year of benefit against all-in $7M" understates SROI under every coherent framing the debate constructed (pure delay, never, or mixture). The Advocate's main magnitude rebuttal (3.5–6× at moderate q) was shown to be an artifact of reintroducing the cost mismatch. The debate also established that the 4.5% credit-share convention is arithmetically equivalent to an all-in framing and provides no separate conservatism. Both sides agree the 30,000–55,000× figure should not be adopted as a point estimate.
Debate unresolved: 1. **Horizon.** The magnitude depends on the effective benefit horizon. The Challenger conceded ~4–5× at a 5-year horizon versus ~11× at the critique's horizon, and neither side grounded it.
2. **The CEA's meaning of "1 year".** Whether the CEA actually defines "1 year" as a pure delay, a mixture, or something else remains unverified.
3. **Displacement and time cost.** The size of the q ≈ 0 corner is uncertain. It turns on displacement valuation and on the time cost of accelerating other funders' spending, which was unaddressed.

--- Critique: The funding landscape for a generic-statin TB program makes "never" a live branch. The speedup is a poor proxy for the grant's real counterfactual. ---

### Advocate
**DEFENSE OF CG'S POSITION: The funding landscape makes "never" a live branch, so the 1-year speedup is a poor proxy**

**EXISTING COVERAGE**

- CG's BOTEC is built as an all-in calculation. Benefits are one year of the adoption-cohort (19,900 deaths/year × 27 DALYs = $OP 54B), matching the 1-year speedup. That is divided by the all-in cost of ~$7M, which explicitly includes "later Phase III trials, guideline changes, dissemination and validation."
- If the grant causes the whole pathway (the "never" branch), then the Phase III and guideline costs are also caused by the grant. The correct denominator is still ~$7M, not $320k.
- The critique's "~20× higher SROI" comes from keeping the larger benefit while shrinking the denominator to $320k. $7M / $320k ≈ 21.9, so the 20× is just the cost ratio.
- This is an attribution inconsistency, not a finding about the counterfactual. It credits the grant with the benefits of Phase III while giving the Phase III funders' spending away for free.
- CG's own 4.5% share ($320k / $7M ≈ 4.6%) already encodes this logic. It credits itself with its share of costs and its share of benefits.
- The Verifier's recommendation to drop or re-derive the 20× figure with an explicit attribution rule is correct. The 20× should not count against CG.
- Part of the "never" concern is already in the 40% p_success, which covers both Phase II and Phase III succeeding. Benefits are not credited in the scenarios where a Phase III is never run or fails.
- The critique's own sensitivity results are empty (`{}`). No quantified effect was demonstrated.

**EVIDENCE WEAKNESSES**

- The Verifier found no evidence that funders disfavor HDT (host-directed therapy). The "never" branch therefore rests on an absence-of-evidence argument: no Phase III funder was found.
  - Accepting this conditionally, the absence is expected. Phase III funding is normally sought after Phase II readouts, so no named funder at this stage says little about what happens afterward.
- The same landscape evidence cuts toward a lower "never" probability.
  - Four statin-TB trials are running: StAT-TB (NIAID), StatinTB (EDCTP/NIAID), ROSETTA and ATORTUB.
  - NIH, EDCTP and Wellcome are all active in this area.
  - A field with several public funders and trials in progress is more likely to reach a Phase III eventually than a field with one orphan trial. This pushes toward a finite speedup, not an infinite one.
- The ROSETTA null result is rosuvastatin-specific. The critique extends it to the whole class without showing the extension is warranted. If it does lower Phase III appetite, it also lowers p_success, which CG already sets at 40% without a stated reference class.
- The critique itself says the direction is "uncertain rather than clearly up." It does not argue that CG's estimate is biased in a specific direction.
- Three searches the Quantifier did not run (the TAG pipeline, Unitaid, and NIH RePORTER) would bear directly on q. The critique cannot yet distinguish the "never" branch from the "redundant" branch.

**MAGNITUDE CHALLENGE**

I cannot ground a value for q (the probability that Phase III is never run absent this grant); treat any figure below as an uninformed illustration. The structure of the calculation still matters.

- An expected-value speedup is E[s] = (1−q)·s_base + q·H_eff. Here H_eff is the effective benefit horizon in the "never" branch.
- Take a 20-year horizon. At a 4% discount rate (my assumption; CG uses 0), the effective years are (1 − 1.04⁻²⁰)/(1 − 1/1.04) ≈ 14.1.
- Take s_base = 1.
  - At q = 10%, E[s] ≈ 0.9 + 0.1×14.1 ≈ 2.3 (2.9 undiscounted).
  - At q = 25%, E[s] ≈ 0.75 + 0.25×14.1 ≈ 4.3 (5 undiscounted).
- These are illustrative, not estimates. They show that a modest q could move the effective speedup by 2–4×.
- The Verifier found the redundancy branch (ATORTUB or another funded trial makes the grant redundant) equally plausible. That branch has s ≈ 0, which pulls E[s] down.
- The "never" branch and the redundancy branch partially offset. The mean of a distribution with mass near 0, a mode near 1, and a right tail is not obviously above 1 until q and the redundancy probability are separately estimated. This has not been done.
- The "never" branch needs further qualification:
  - Benefits over a long horizon are subject to the 2% annual incidence decline.
  - They may be overtaken by shorter regimens (the 4-month regimen noted in the Parameter Map).
  - They would be partially replicated by off-label statin use after Phase II data.
  - All of these shrink H_eff relative to a naive 20-year horizon.
- The 20× is not a defensible magnitude. A defensible upward adjustment would be a factor of roughly 1–4× on the benefit side with the all-in denominator held at $7M, with wide uncertainty.

**OFFSETTING FACTORS**

- Redundancy: if ATORTUB or another funded trial is the same Phase IIc, the grant's counterfactual impact is near zero. The critique acknowledges this but does not weigh it.
- The ROSETTA null result lowers p_success. CG's 40% is therefore more likely too high than too low, and any upward speedup correction would partly be offset by a downward p_success correction.
- CG uses zero discounting. Extending the horizon in the "never" branch is worth less than it appears once a discount rate is applied (14.1 versus 20 effective years above).
- The Parameter Map flags several other unmodeled factors that push down:
  - no adoption lag;
  - uptake that ramps over years rather than jumping to 60%;
  - no treatment-delivery costs.
  These would compress the benefit stream in any counterfactual.

**OVERALL ASSESSMENT: Partial defense**

- Strong on the 20× number. It is an attribution inconsistency (large benefit, small denominator) that CG's all-in accounting avoids. The Verifier also recommended dropping it.
- Weak-to-moderate on the underlying point. A fixed 1-year speedup is a point estimate for what is plausibly a highly skewed distribution. The expected value could be above 1.
  - CG gives no justification for the 1 year.
  - CG has not explicitly modeled the "never" or redundancy branches.
- The sign of the net correction is genuinely uncertain, as the critique itself says.
- A real upward revision would need three things:
  - a grounded q;
  - a grounded redundancy probability;
  - a discounted horizon.
  None is available here.

**CONCESSIONS**

- CG's 1-year speedup is unjustified in the text. A proper expected-value treatment would likely give an E[s] different from 1, and it could plausibly be higher.
- The "never" branch is not excluded by the landscape evidence. No Phase III funder was identified, and the ROSETTA null may reduce appetite.
- CG's 4.5% attribution leaves open how credit should be split if the grant is what triggers the other funders' spending. This is a legitimate methodological gap, though it does not imply 20×.
- Whether ATORTUB is the same trial as the CG-funded Phase IIc is unresolved. If it is, the redundancy case applies and CG's estimate is too high.

### Challenger
REBUTTAL: The funding landscape for a generic-statin TB program makes "never" a live branch

**RESPONSE TO "EXISTING COVERAGE"**

> The Advocate claims: The ~20× figure is just the $7M/$320k cost ratio. It pairs a Phase-III-sized benefit with a grant-sized denominator, and CG's all-in denominator plus 4.5% share already handles attribution correctly.

Response:

1. **Concession.** The 20× figure as written is an attribution artifact. It should be dropped or re-derived, and I do not defend it.

2. **The all-in denominator is only correct in the "never" branch.**
   - In the accelerator branch, Phase III happens anyway, so its cost is incurred in both worlds. It is not caused by the grant.
   - Charging the grant for $7M while crediting only a 1-year speedup then overstates the denominator.
   - In the "never" branch, the $7M is correctly caused by the grant. But then the benefit should span many years, not one.
   - So "$7M against a 1-year speedup" is internally consistent in neither branch. It pairs the accelerator-branch benefit with the never-branch cost.
   - The Advocate's argument shows the 20× is wrong. It does not show that the 1-year/$7M pairing is right.

3. **The 4.5% share does not answer the counterfactual question.**
   - A cost-share rule is an attribution convention.
   - The critique asks which world the grant buys. The Advocate concedes this is "a legitimate methodological gap."

4. **p_success does not encode q.**
   - The Advocate says benefits are "not credited in scenarios where a Phase III is never run or fails," so part of the "never" concern is already covered.
   - That addresses the with-grant world: does the pathway succeed?
   - The critique's q concerns the without-grant world: would anyone fund Phase III absent the grant?
   - A low p_success shrinks the numerator. It does nothing to the baseline against which the speedup is measured.

5. **Empty sensitivity results.** `{}` means not computed, not computed-and-null. The Advocate's own illustrative calculation shows the effect is not negligible.

**RESPONSE TO "EVIDENCE WEAKNESSES"**

> The Advocate claims: No Phase III funder is named, but that is expected at this stage. Several active public funders make eventual Phase III more likely, which pushes toward a finite speedup. The ROSETTA null is rosuvastatin-specific.

Response:

1. **The absence cuts both ways.** If the lack of a named funder "says little" about what happens later, it also cannot support a low q. The Advocate concedes this: "The 'never' branch is not excluded."

2. **Phase II funders are weak evidence for Phase III funding.**
   - The Advocate infers Phase III likelihood from the number of Phase II funders.
   - I cannot ground a Phase II→Phase III funder-conversion rate for generic-drug HDT, and the Advocate cites none either.
   - Phase III costs are an order of magnitude larger than Phase II, on CG's own ~$7M all-in versus $320k.
   - The inference is plausible but unsourced.

3. **Funding appetite and p_success are different quantities.**
   - The Advocate says the ROSETTA null, if it lowers Phase III appetite, "also lowers p_success."
   - A null in one agent can lower funder appetite (raising q) without lowering the efficacy probability of a different statin.
   - The two effects are partly independent, so the p_success offset is not one-for-one.

4. **Class extension.**
   - The ROSETTA null is rosuvastatin-specific, and the Advocate is right that this is a fair objection.
   - The verifier found it "reduces expected Phase III appetite for the whole class." I cannot independently ground this beyond the verifier's statement.
   - Funders could plausibly reason at the class level, but that is a conditional, not an established fact.

5. **UNGROUNDED versus REJECTED.**
   - The "funders disfavor HDT" claim was marked UNGROUNDED. It was not rejected.
   - The Advocate cannot cite it as evidence for a low q. It also does not support a high q.
   - The three unrun searches (TAG pipeline, Unitaid, NIH RePORTER) leave q open in both directions.

**RESPONSE TO "MAGNITUDE CHALLENGE"**

> The Advocate claims: Illustrative q values give E[s] of 2.3–4.3, but the redundancy branch (s≈0) partly offsets, so E[s] is "not obviously above 1." A defensible adjustment is 1–4× upward with wide uncertainty.

Response:

1. **Show the offset condition from the Advocate's own structure.**
   - Let q be P(never), r be P(redundant, s=0), and H_eff the never-branch horizon. The remaining mass gets s=1.
   - Then E[s] = (1−q−r)·1 + q·H_eff = 1 − r + q(H_eff − 1).
   - E[s] < 1 requires r > q(H_eff − 1).
   - With the Advocate's discounted H_eff = 14.1, this requires r > 13.1q. With the undiscounted H=20, it requires r > 19q.
   - So redundancy must be 13–19× more probable than "never" to cancel it. At q=10%, r would have to exceed 100%, which is impossible.
   - The offset is not a coin-flip between two comparable branches. It requires near-certainty of redundancy or a very small q.

2. **Misstatement of the verifier.**
   - The Advocate says the Verifier found redundancy "equally plausible."
   - The verifier only said ATORTUB "must be checked." It did not rate the branches' relative plausibility.
   - The redundancy probability is unquantified, as is q.

3. **The Advocate's H_eff shrinkers are real but modest.**
   - The 2% incidence decline: the average of 0.98^t over t=0..19 is (1−0.98²⁰)/(20×0.02) ≈ (1−0.668)/0.4 ≈ 0.83. That is about a 17% reduction.
   - Shorter regimens and off-label use are legitimate but unquantified.
   - For the correction to vanish at r=q=10%, H_eff would need to fall below 2. That means essentially all never-branch benefit disappears within two years, which seems implausible for a generic drug with no other sponsor.

4. **Minimum defensible magnitude.** The Advocate's own range is 1–4× on the benefit side. Even at q=5% with r=0, the Advocate's formula gives E[s] ≈ 0.95 + 0.05×14.1 ≈ 1.65. A change of that size is material to an SROI, though I cannot ground q=5% either.

**RESPONSE TO "OFFSETTING FACTORS"**

> The Advocate claims: Redundancy, a lower p_success after ROSETTA, zero discounting, and unmodeled factors (adoption lag, uptake ramp, delivery costs) all push down.

Response:

1. **Redundancy.** It is real but unresolved. Whether ATORTUB is the same trial is an open factual question, and the redundancy case is not an offset until that is checked. It is also bounded by the arithmetic in item 1 above.

2. **p_success.** See above. It is partly independent of q, and CG's 40% was set without a stated reference class. A ROSETTA-driven cut to p_success is a separate correction. It does not neutralize a speedup correction.

3. **Discounting.**
   - CG uses zero discounting for both the 1-year benefit and a longer horizon. Applying a discount rate only to the extension is asymmetric within the calculation.
   - If discounting is applied, it should shrink the baseline 1-year benefit too, since that benefit falls after Phase III timing.
   - The 14.1 versus 20 comparison therefore overstates the offset.

4. **Adoption lag, ramp, delivery costs.**
   - These scale the benefit stream in both branches.
   - They lower the absolute SROI level but do not change E[s] relative to 1.
   - They are not offsets to the speedup correction. They are separate downward corrections, and not part of this critique's claim.

**KEY UNRESOLVED QUESTIONS**

- Is ATORTUB the same trial as the CG-funded Phase IIc? This determines whether the redundancy branch dominates.
- What is the Phase III funding probability for generic-drug HDT after a positive Phase IIc? None of us can ground q, and the unrun TAG/Unitaid/NIH RePORTER searches would bear directly on it.
- Is CG's 4.5% share an attribution convention or a counterfactual claim? That determines whether the all-in $7M denominator is appropriate when the benefit is a 1-year speedup.
- Does the ROSETTA null move class-level funder appetite (q) independently of efficacy (p_success)?

### Judge Audit
Surviving strength: moderate
Justification: - **Headline magnitude defeated.** The critique's 20× claim did not survive, and the Challenger conceded it.
- **Core mechanism strengthened.** The Challenger's grounded derivation (r > 13q) showed that the Advocate's offset argument fails for any non-negligible q. That argument rested partly on a misstatement that the verifier rated redundancy "equally plausible."
- **Limits.** No one quantified q. The single factual question that could reverse the direction, ATORTUB's identity, remains unchecked. Together these keep the critique from reaching "strong."
Recommended action: 2. SPECIFIC INVESTIGATION:**
1. Look up the sponsor and funding sources for ATORTUB (NCT06199921) on ClinicalTrials.gov and compare them with the CG grant description.
   - If they match, the redundancy branch applies and CG's speedup should be revised toward 0.
   - If they do not match, ATORTUB is a parallel pipeline. That lowers q but supports E[s] ≥ 1.
2. Run the three verifier searches that were not performed, to establish whether any Phase III or post-Phase-II funding pathway exists for statin host-directed therapy:
   - NIH RePORTER, for statin TB Phase III or "treatment-shortening" awards;
   - the TAG pipeline report;
   - the Unitaid portfolio.

Both steps are feasible with existing tooling.

**In the meantime, conclude now:**
- Drop the 20× SROI figure.
- Replace CG's fixed 1-year speedup with the explicit expected-value form E[s] = 1 − r + q(H_eff − 1).
- Note that CG's estimate is likely understated if the trial is not ATORTUB and q is at least about 5%. Confidence in this is moderate.
Action feasibility: requires_specified_evidence
Advocate failures: ['misrepresenting_evidence_status: The Advocate wrote, "The Verifier found the redundancy branch (ATORTUB or another funded trial makes the grant redundant) equally plausible." The verifier said only that ATORTUB\'s identity is unknown and must be checked. It assigned no relative plausibility to the redundancy and "never" branches. The Advocate then used this invented parity to argue the two branches "partially offset." The Challenger correctly caught this.', 'unsupported_estimate_pseudo: The Advocate first labeled its q values (10%, 25%) "uninformed illustration[s]," which is a legitimate move. It then concluded, "A defensible upward adjustment would be a factor of roughly 1–4×." That turns admittedly ungrounded inputs into a range it calls "defensible." The illustration was fine; relabeling its output as a defensible magnitude is not.', 'false_definitiveness: The defense\'s body is headed "OVERALL ASSESSMENT: Partial defense" and rates the core point "weak-to-moderate." The appended self-assessment nonetheless reads "strong." The defense\'s own substance supports "partial," and I assess it as partial. It is strong only on the 20× figure.', "sound_synthesis_noted: The Advocate's discounted-horizon calculation is correctly derived from stated assumptions and supports a legitimate structural point."]
Challenger failures: ["sound_synthesis_noted: The Challenger formalized the Advocate's own structure as E[s] = 1 − r + q(H_eff − 1), from which:", "sound_synthesis_noted: The incidence-decline adjustment, mean of 0.98^t over 20 years ≈ 0.83, is correctly computed and properly sizes one of the Advocate's H_eff shrinkers.", 'strawmanning: The Challenger said that applying the discount rate "only to the extension is asymmetric" and that the "14.1 versus 20 comparison therefore overstates the offset.']
Debate resolved: On the 20× figure:** Both sides agree it is an attribution artifact (the $7M/$320k cost ratio) and must be dropped.

**On the structure of the correction:**
- p_success does not encode the counterfactual q.
- CG's "$7M all-in cost against a 1-year speedup" pairing is not internally consistent under either pure branch.
- Given the Challenger's derivation, any non-trivial q (around 5–10%) yields E[s] meaningfully above 1, unless:
  - redundancy is roughly 13 or more times as probable as "never", or
  - H_eff collapses toward 2 years.
Debate unresolved: - Whether ATORTUB (NCT06199921) is the CG-funded trial. If it is, the redundancy branch dominates and the critique's direction flips.
- The actual value of q, which nobody could ground.
- The correct attribution rule, given that CG's 4.5% share and the $7M denominator may encode different counterfactual assumptions.

--- Critique: Discounting quantified properly with an S-curve ramp and discounted costs. The net effect is about −20% to −31%, not the benefit-only −21% to −35%. ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION: Discounting quantified with an S-curve ramp and discounted costs

**EXISTING COVERAGE:**
- CG does not discount. The parameter map records "No time discounting" and an implicit discount rate of 0. I cannot claim the BOTEC covers this explicitly.
- CG's all-in cost framing partly mitigates the issue. The $7M includes later Phase III, guideline and dissemination costs. Because those costs fall in the future, a consistent discounter would also discount them, which is the cost offset the critique itself invokes.
- The BOTEC is a deliberately coarse tool. The source describes it as a back-of-the-envelope calculation. CG's own bar is "about 2,000x" against "about 3,000x" published. A margin of roughly 1.5x is the headroom CG chose to rely on for unmodeled second-order terms such as discounting.

**EVIDENCE WEAKNESSES:**
1. **The headline numbers cannot be reproduced from the stated assumptions.**
   - Take the benefit as a point at T0 = 8.5 years: the factor is 1/1.03^8.5 = 0.778, 1/1.04^8.5 = 0.717 and 1/1.05^8.5 = 0.661. These match the critique's benefit-only penalties of about −22% to −34%.
   - Take costs spread uniformly over years 1–8, with a mean timing of about 4.5 years: the factor is 1/1.03^4.5 = 0.875, 1/1.04^4.5 = 0.838 and 1/1.05^4.5 = 0.803.
   - The net ratio is then 0.778/0.875 = 0.889 (−11%), 0.717/0.838 = 0.856 (−14%) and 0.661/0.803 = 0.823 (−18%).
   - That is meaningfully smaller than the critique's −20% / −27% / −31%. The critique does not show the ramp calculation that would close the gap.
   - A ramp spreads benefits around T0, and with convex discounting that tends to raise the average discount factor, not lower it. So the ramp does not obviously explain a larger penalty.
   - The net penalty is at best uncertain, and my point-timing derivation suggests it is roughly 10–18%, below the 25% materiality line.
2. **The timing inputs are self-described as illustrative.** The critique says "all timing assumptions are illustrative and need the CEA's real timeline." T0 = 8.5, L = 6, L = 10 and uniform spend over years 1–8 are not drawn from the CG text. The text gives only a Phase III finishing at year 8.
3. **The cost timing is probably wrong in a direction that shrinks the offset, but the critique does not establish it.**
   - The $7M includes post-trial guideline and dissemination costs, which fall after year 8. Those would be discounted more heavily than uniform years 1–8 spend.
   - This is an argument that the net penalty could be larger than my −11% to −18%. I raise it because the critique's own cost assumption is unsupported either way.
4. **The discount rate rests on weak sourcing.**
   - The cited evidence is a general convention of 3% for health outcomes and costs, and one review arguing for at least 5% in low- and lower-middle-income countries.
   - Neither source is specific to CG's $OP framework, in which value is anchored to log-utility income and a fixed $100,000 per DALY.
   - The critique itself marks the CG discounting convention as UNGROUNDED.
5. **The bar and baseline are inferred.** The 3,050x baseline and the 0.656 threshold ratio are described as "inference, not sourced." The published figure is "about 3,000x."

**MAGNITUDE CHALLENGE:**
- By the critique's own numbers, only one scenario falls below the 2,000x bar: L = 10 at 5%, at about −37%.
- That scenario stacks the highest discount rate with a ramp length that nothing in the CG text supports.
- The 3% and 4% cases are −20% and −27%, which are close to or at the 25% line. They remain well above 2,000x. For example, 3,050 × 0.73 ≈ 2,230x.
- On my point-timing derivation, the net effect is −11% to −18% (roughly 2,500–2,700x), which does not threaten the bar and does not exceed the 25% change criterion.
- The critique's central estimates therefore rest on an unreproduced cost-side figure. Without that figure, the finding does not reach materiality.

**OFFSETTING FACTORS:**
1. **Omitted benefit channels.** The parameter map lists implicit zeros for morbidity DALYs from reduced lung damage, post-treatment mortality, transmission-averted cases and diagnostic value. Any positive value in these channels offsets a discounting penalty. I cannot size them, so this is directional only.
2. **Constant treated share and flat case counts after year 8.** The BOTEC counts one year of speedup at the year-8 caseload. Adding discounting without modeling the other post-year-8 benefit dynamics gives only a partial correction.
3. **The critique's own framing concession.** The critique says that under any coherent counterfactual framing, discounting is "second-order" compared with the speedup-versus-counterfactual framing issue. If that is right, the discounting finding should not be treated as a decision-driver in its own right.

**OVERALL ASSESSMENT:** Partial defense.
- Zero discounting is a real omission, and the direction (SROI falls) is not in doubt.
- The magnitude is overstated relative to what the stated inputs imply, and the crossing of the 2,000x bar needs an unsupported combination of assumptions.
- The critique does not meet the burden for "bar-crossing." It is closer to meeting the burden for "a modest downward adjustment of roughly 10–30%."

**CONCESSIONS:**
- CG applies no discounting, and a conventional 3–5% rate would lower SROI.
- Consistent treatment of costs and benefits shrinks the penalty relative to benefit-only discounting, as the critique argues. I agree with that direction.
- At 4–5% with a long ramp, the result could approach the bar. I cannot rule this out because the real timeline is not in the CG text.
- The 25% materiality line is plausibly reached at the upper end of the discount-rate range if the critique's net numbers are correct.

### Challenger
REBUTTAL: Discounting with an S-curve ramp and discounted costs

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: CG applies no discount rate, so nothing in the BOTEC covers this. But the all-in $7M cost and the roughly 1.5x gap between the "about 3,000x" estimate and the 2,000x bar act as informal headroom for second-order terms like discounting.

- **Zero discounting is not covered.** The Advocate concedes this.
- **The "headroom" claim has no source.** Nothing in the CG text says the 1.5x margin was left for discounting. It is the Advocate's inference, and it is a weaker inference than the critique's baseline-of-3,050x, which the Advocate calls unsourced.
- **Discounting alone could consume the whole margin.**
  - The verifier's package puts the bar-crossing at about −34% (2,000/3,050 ≈ 0.656).
  - The critique's net penalty is −20% to −31%, so discounting alone would use roughly 60–90% of the margin at 3–5%.
  - That leaves little room for the other second-order terms the margin is supposedly meant to absorb.
- **The all-in cost framing is the critique's offset, not a defense.** The critique already includes it in the net figures (−20/−27/−31% versus benefit-only −21 to −35%). It does not take the penalty to zero.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the critique's net figures cannot be reproduced. Point timing (benefit at T0=8.5, costs uniform over years 1–8 with mean 4.5) gives only −11/−14/−18%. A ramp should raise the average discount factor, not lower it.

- **I concede the Advocate's arithmetic.** I checked 0.778/0.875 = 0.889 and found it correct for point timing.
- **The Jensen argument only works if the ramp is symmetric around T0, and that is not established.**
  - The only timeline anchor the Advocate cites is that Phase III finishes at year 8. Benefits cannot start before that.
  - If T0=8.5 marks the start of the ramp, the ramp lies in years 8.5 to 14.5 with a mean near 11.5, not 8.5.
- **My derivation shows this reading roughly reproduces the critique.**
  - Benefit factor at mean 11.5: 1.03^-11.5 = 0.712, 1.04^-11.5 = 0.637, 1.05^-11.5 = 0.570.
  - Cost factors at mean 4.5, from the Advocate's numbers: 0.875, 0.838, 0.803.
  - Net: 0.814 (−19%), 0.760 (−24%), 0.710 (−29%).
  - These sit close to the critique's −20/−27/−31%. This is a mean-timing approximation, not a full S-curve integral.
- **I cannot confirm this is the critique's reading.** The critique does not show its ramp calculation, and the Advocate is right to ask for it. But the Advocate's −11 to −18% is a floor, since it puts all benefit at the earliest feasible date. It is not a central estimate.
- **Correction on the Advocate's cost-timing point (their item 3).**
  - The Advocate says post-year-8 dissemination costs could make the net penalty larger.
  - Later costs are discounted more, which lowers DF_C and makes net = DF_B/DF_C closer to 1.
  - That shrinks the penalty, so it cuts against the critique.
  - I concede the direction. Its size depends on what share of the $7M falls after year 8, which neither side has.
- **The critique's own "illustrative" caveat applies equally to the Advocate's point-timing.** Neither side has the CEA's real timeline. The honest range is roughly −11% (Advocate's floor) to −31% (critique), not a rebuttal of the critique.
- **The discount-rate sourcing is adequate for a 3–5% range.**
  - The verifier confirmed 3% as the global health convention for outcomes and costs.
  - It also confirmed a review arguing for at least 5% in low- and lower-middle-income countries.
  - The Advocate's point that these sources are not CG-specific is true. It does not support a rate of 0, for which the Advocate offers no rationale.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: only L=10 at 5% (−37%) crosses the 2,000x bar, which needs an unsupported stack of assumptions. The other cases stay above the bar, and the central estimate is only −11% to −18%.

- **The Advocate's own floor is about −11% at 3% and −18% at 5%.** That is a nonzero downward revision in a direction CG ignores entirely.
- **The L=10 ramp is not obviously more exotic than L=6.** Neither value comes from the CG text, and a 10-year adoption ramp for a TB diagnostic or treatment guideline is not implausible. The verifier flagged this scenario as crossing the bar.
- **Two thresholds are in play, and the Advocate switches between them.**
  - The 25% line is the materiality criterion.
  - The −34% line is the bar-crossing threshold from the verifier's inference.
  - On my ramp-start reading, 4–5% reaches or exceeds 25%, and 5% with L=10 crosses the bar.
  - The Advocate's "does not exceed the 25% criterion" conclusion depends on the point-timing floor.
- **Concession.** At 3% under any reading, the effect is about −11% to −20% and not decision-relevant by itself.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: omitted benefit channels (morbidity, post-treatment mortality, transmission, diagnostic value) and flat post-year-8 caseloads offset the discounting penalty. And the critique itself calls discounting second-order relative to framing.

- **The Advocate cannot size the omitted benefit channels.** The offset is directional only, and an unsized offset cannot neutralize a quantified penalty.
- **The omitted channels are not a discounting-specific offset.** They would apply to any downward adjustment, so they do not rebut this one.
- **The "flat caseload" point has no stated direction.** The Advocate calls it only a "partial correction." Neither side knows if it raises or lowers the benefit.
- **"Second-order" is not the same as "immaterial."**
  - The critique says discounting matters less than the framing question.
  - A −20% to −31% change in SROI is still comparable to the 25% materiality criterion.
  - It also interacts with the framing choice, since the critique says discounting is smaller under a counterfactual framing.
  - That supports labeling this a refinement. It does not support dismissing it.

**KEY UNRESOLVED QUESTIONS:**
- What are the CEA's real timing inputs? Specifically, is T0 the start of the benefit ramp, its midpoint, or the end of Phase III? This one input moves the net penalty between roughly −11% and −29%.
- What share of the $7M falls after year 8? It determines how much the cost offset grows.
- Which threshold defines "material": the 25% change criterion or the −34% bar-crossing?
- Is the 3,050x baseline right, or is the "about 3,000x" figure CG published the better anchor? The bar-crossing depends on it.
- Does CG have a deliberate rationale for a zero discount rate? The Advocate found none in the text.

### Judge Audit
Surviving strength: moderate
Justification: The Advocate's main quantitative attack rested on misreading the ramp as centred on T0 and on claiming the numbers were irreproducible when the verifier had reproduced them. It also contained a sign error on cost timing that the Challenger correctly reversed. The critique's arithmetic therefore survives largely intact. However, the critique's inputs are self-described as illustrative, and the bar and baseline are unverified. The bar-crossing claim survives only in the L=10 / 5% scenario, which the Challenger defended only by appeal to non-implausibility. Both sides made grounded arguments, and the decisive input (the real timeline) remains open. That supports moderate rather than strong.
Recommended action: 1. CONCLUDE NOW, with moderate confidence:
   - CG's zero-discounting is an omission that lowers SROI.
   - Under consistent discounting of costs and benefits with a post-year-8 benefit ramp, the net reduction is about −20% / −27% / −31% at 3% / 4% / 5%. That is material by the 25% criterion at 4–5%, but not at 3%.
   - The claim that discounting alone pushes SROI below the bar should be downgraded to a single conditional scenario (L=10, 5%) that depends on an unverified baseline and bar.
   - The critique should be revised in four ways:
     - Remove the self-referential "Critique 1/4" cross-references.
     - State the 3,050x baseline explicitly.
     - Specify which threshold defines "material".
     - Report net factors using the exact ramp formula consistently (−21/−27/−32%).
   - The one input that would change this conclusion is the CEA's benefit-onset timing: ramp start versus a one-year speedup pulse near year 8. Extracting it from the CEA/BOTEC source is feasible if that document is accessible.
Action feasibility: actionable_now
Advocate failures: ['misrepresenting_evidence_status: The Advocate says "the headline numbers cannot be reproduced from the stated assumptions" and "the critique does not show the ramp calculation." The verifier\'s package contradicts this. It states the ramp formula e^(−rT0)(1−e^(−rL))/(rL) and marks it VERIFIED. It also marks the benefit factors (0.71/0.63/0.57), the cost factors (0.88/0.85/0.82) and the net factors (−20/−27/−31%) as VERIFIED within rounding. The Advocate treats verified arithmetic as unreproducible.', 'strawmanning: A ramp spreads benefits around T0, and with convex discounting that tends to raise the average discount factor." The verified formula is the average discount factor of a uniform spread starting at T0 and running to T0+L. It is not a spread centred on T0. The Jensen argument therefore rebuts a ramp model the critique did not use.', 'unsupported_estimate_pseudo: My point-timing derivation suggests it is roughly 10–18%, below the 25% materiality line" (and "roughly 2,500–2,700x").', "misrepresenting_evidence_status: CG's own bar is 'about 2,000x'… A margin of roughly 1.5x is the headroom CG chose to rely on for unmodeled second-order terms such as discounting.", 'false_definitiveness: Item 3 claims post-year-8 dissemination costs "could make the net penalty larger." This has the sign backwards. Later costs lower DF_C and push DF_B/DF_C toward 1, which shrinks the penalty. The claim was stated confidently and the Challenger correctly reversed it.', 'sound_synthesis_noted (missed defense): The Advocate notes in passing that the BOTEC "counts one year of speedup at the year-8 caseload." This was a stronger defense than the one they ran. If the BOTEC\'s benefit is a one-year speedup pulse near year 8–9, an infinite-horizon S-curve ramp may not match the BOTEC\'s own benefit structure. That mismatch would make point-like timing more defensible. The Advocate never connected this to the ramp dispute.', 'sound_synthesis_noted (missed defense): The verifier flagged the "conflict with Critique 1" cross-reference as self-citing. The Advocate leaned on that "second-order" framing concession instead of noting that the structural argument behind it is malformed in this batch.']
Challenger failures: ['sound_synthesis_noted: The ramp-start reading derives mean benefit timing of about 11.5 years and net factors of 0.814/0.760/0.710.', "sound_synthesis_noted: The correction of the Advocate's cost-timing sign error (later costs shrink the penalty) is correct. The Challenger conceded the direction against their own side and acknowledged the size is unknown.", 'strawmanning: It does not support a rate of 0, for which the Advocate offers no rationale." The Advocate never argued for a zero rate. They explicitly conceded that "Zero discounting is a real omission.', 'strawmanning: Two thresholds are in play, and the Advocate switches between them." The Advocate\'s Magnitude Challenge addresses both the 25% line and the 2,000x bar separately and explicitly. The accurate objection is the one the Challenger also made: the Advocate\'s sub-25% conclusion depends on the point-timing floor.', 'whataboutism: The headroom claim "is a weaker inference than the critique\'s baseline-of-3,050x, which the Advocate calls unsourced." This is a comparative jab at the Advocate\'s broader position. The Challenger\'s substantive point (that no source attributes a purpose to the margin) stands without it.', 'call_to_ignorance: A 10-year adoption ramp for a TB diagnostic or treatment guideline is not implausible." No evidence is offered. Non-implausibility is used to keep the bar-crossing scenario alive.', 'misrepresenting_evidence_status (minor): The honest range is roughly −11% (Advocate\'s floor) to −31%." This treats the Advocate\'s point-timing figure as a legitimate endpoint. It is actually a model that departs from the critique\'s verified ramp structure, and the Challenger\'s own derivation showed why it is a floor.']
Debate resolved: The debate established three things:
- The direction of the effect: SROI falls under any conventional 3–5% rate.
- Consistent cost discounting shrinks the penalty relative to benefit-only discounting.
- At 3% the net effect (about −11% to −20%) is below both the 25% line and the bar.

It also established that the critique's −20/−27/−31% figures follow arithmetically once T0 is read as the start of the benefit ramp, as the verified formula implies. The Advocate's sub-materiality estimate depends on a point-benefit model the critique did not use.
Debate unresolved: Three questions remain contested:
- Whether the real CEA timeline supports a post-year-8 ramp of L=6 or L=10, or whether the speedup framing implies a near-point benefit pulse. This one choice moves the net penalty between about −11% and −31%.
- What share of the $7M falls after year 8.
- Whether the bar-crossing claims hold at all. They rest on a 2,000x bar and a 3,050x baseline, and neither was verified.

--- Critique: Probability weighting is asymmetric between benefit and cost. ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: Probability weighting is asymmetric between benefit and cost

EXISTING COVERAGE:
- The BOTEC says "all-in costs are about $7 million" and "including later Phase III trials, guideline changes, dissemination and validation." It does not say whether this is a budget if everything proceeds or an expected spend.
- The critique itself concedes that "if the $7M already reflects expected values, the critique does not apply." It also says it "cannot determine this without the CEA." So the claimed asymmetry is a hypothesis about an undocumented cost build-up, not a demonstrated error.
- The 40% is defined as the probability that "Phase II and Phase III trials both succeed." It is a joint probability across a staged pathway, not a single-stage figure. Treating it as a joint probability already partly addresses the critique, because the benefit side is gated by the whole sequence.
- CG's convention is to compute SROI on all-in costs and all-in benefits rather than its own 4.5% share. This is a deliberately inclusive denominator.
  - If I read the convention charitably, it errs toward not under-counting costs.
  - This is a conditional reading of CG's intent. I have no source stating that intent.

EVIDENCE WEAKNESSES:
- The critique offers no external evidence. The Quantifier's sensitivity results are empty ({}), and the critique rates its own strength "medium-to-low."
- The critique names three ways it could fail, and none has been ruled out:
  - p_success may refer only to the final stage.
  - Some downstream spend may be by other funders and excluded from the $7M.
  - The $7M may already be expected-value.
- Most of the critique's range depends on an s that is not credible. Its 1.6–2.3x range uses s between 0.6 and 0.4.
  - Derivation: if Phase III is only run after Phase II succeeds, then p_success = p2 × p3 = 0.40, so s (the chance Phase III spending occurs) = p2 = 0.40 / p3.
  - s = 0.4 therefore requires p3 = 100%, meaning Phase III always succeeds once Phase II does. I think this is implausible, though I cannot cite a TB-specific Phase III reference class.
  - s = 0.6 requires p3 ≈ 67%.
- The critique's own "subtle counterpoint" concedes that the correct s lies between 0.4 and 1, and that the effect "might be small."

MAGNITUDE CHALLENGE:
- Using s = 0.40 / p3, my illustrative values for p3 are uninformed priors, not sourced figures. For each, I apply the critique's own formula, expected cost = $0.32M + s × $6.7M:

  | p3 | s | Expected cost | SROI multiplier on $7M |
  |---|---|---|---|
  | 0.5 | 0.80 | $5.68M | ~1.23x |
  | 0.7 | 0.57 | ~$4.15M | ~1.69x |

  So a plausible range is roughly 1.2–1.7x, not 1.6–2.3x. The top of the critique's range requires a near-certain Phase III.
- The critique treats the whole $6.7M as gated by s. That is too aggressive.
  - Guideline change, dissemination and validation occur only after Phase III success, so they are gated by 0.40 (or higher), not s.
  - That component makes the understatement larger than the Phase III-only estimate, not smaller.
  - I cannot ground the split between Phase III cost and post-trial cost, so I cannot say which effect dominates. This is a gap in my defense, not a rebuttal.
- Late failure after most spending is already incurred pushes s toward 1. The critique acknowledges this.

OFFSETTING FACTORS:
- The parameter map says the $7M excludes costs of delivering the drug:
  - procurement, monitoring and health-worker time
  - adverse-event management
  - possibly the sweat-diagnostic workstream (unclear)
- If these are real costs of reaching the benefit, they are incurred only on success, and the benefit side already carries a 3.3M-person uptake. Adding them raises the all-in cost and lowers SROI.
  - Their size is unknown, and I cannot ground a number for them.
  - They push in the opposite direction from this critique, partly or fully offsetting it. The net sign is undetermined.
- The BOTEC has other conservative omissions: morbidity, lung-damage benefits and the diagnostic are all valued at zero. These sit on the benefit side and are not a direct offset to a cost-weighting error, but they bear on whether the net estimate is biased downward.

OVERALL ASSESSMENT:
Partial defense.
- The critique rests on an unverified assumption (nominal $7M) and no external evidence.
- Its upper range (s = 0.4, 2.3x) is close to implausible, since it requires a near-certain Phase III.
- If the $7M is nominal, a real upward understatement of about 1.2–1.7x remains under my illustrative p3 range.
- That understatement is meaningful, above the 25% materiality threshold. I cannot show that CG already handled it.
- The critique cannot be dismissed. It is credible conditional on one cost-structure fact that neither side can verify.

CONCESSIONS:
- The wording "all-in costs are about $7 million," next to a benefit explicitly multiplied by 40%, reads more naturally as a nominal budget. If so, the structure is asymmetric.
- Even with a high p3, s cannot fall below 0.4, and under most plausible values the expected cost is meaningfully below $7M. The direction of the bias (SROI understated) is probably right.
- CG gives no breakdown of the $7M, so the asymmetry cannot be ruled out from the published text.
- The delivery-cost offset is a point I cannot quantify, so I cannot claim it neutralizes the critique.
```

### Challenger
REBUTTAL: Probability weighting is asymmetric between benefit and cost

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: defining 40% as the joint probability of Phase II and Phase III success, and using an all-in denominator, "partly addresses" the critique.

Response:

1. **The joint probability does not touch the cost side.** The critique is that the benefit is multiplied by 0.40 while the cost may not be. Gating the benefit by a joint probability is the benefit half of that asymmetry. It cannot "partly address" a concern about the denominator.
2. **"All-in" describes scope, not probability weighting.** An inclusive denominator means every funder's spend is counted. It does not mean each dollar is weighted by its probability of being spent. The Advocate admits "I have no source stating that intent." A charitable reading of CG's intent is therefore not coverage.
3. **The BOTEC wording reads as a budget.** "All-in costs are about $7 million... including later Phase III trials, guideline changes, dissemination and validation" lists future spending items as a contingent pathway. The Advocate concedes it "reads more naturally as a nominal budget."
4. **No offsetting mechanism has been identified in the model.** The Advocate cites none. The remaining defense is that the cost structure is undocumented, which is a gap in the defense and not a rebuttal.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the critique has no external evidence, rates itself medium-to-low, and names three failure modes that are not ruled out.

Response:

1. **UNVERIFIABLE is not REJECTED.** The verifier did not find contradicting evidence. It could not access the CEA cells. "None of the failure modes has been ruled out" holds equally for the critique's mechanism.
   - The right frame is conditional: if the $7M is a nominal budget, SROI is understated.
   - The Advocate accepts this, and the BOTEC wording points toward the nominal reading.
2. **I concede the s = 0.4 point.** The Advocate's derivation is right. If s = p2 = 0.40/p3, then s = 0.4 requires p3 = 1, so the 2.3x endpoint is the extreme case.
3. **The central estimate still lands near 1.5x.** A symmetric split of the 0.40 joint probability gives p2 = p3 = √0.40 ≈ 0.63.
   - Expected cost = 0.32 + 0.63 × 6.7 ≈ $4.55M.
   - The multiplier is 7 / 4.55 ≈ 1.54x.
   - This is the midpoint of the Advocate's own 1.2–1.7x range. The symmetric split is my own illustration, not a sourced reference-class figure. I cannot ground a TB-specific Phase III success rate, and neither can the Advocate.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: the plausible range is about 1.2–1.7x, not 1.6–2.3x.

Response:

1. **The Advocate's table is not a ceiling.** The Advocate concedes that guideline change, dissemination and validation occur only after Phase III success, so they are gated by 0.40 and not by s.
   - Those costs then get a weight lower than the s used in the table.
   - In the limit where all $6.7M is gated by 0.40, the multiplier is 7 / (0.32 + 0.4 × 6.7) = 7 / 3.0 ≈ 2.33x.
   - The Advocate's 1.2–1.7x therefore understates the upside whenever post-trial costs are a meaningful share. The Advocate admits they cannot ground that split.
2. **The Advocate's materiality claim is slightly off at the low end.** The p3 = 0.5 row gives 1.23x, which is below the 25% threshold the Advocate invokes. The low end is borderline and not clearly material.
3. **The true floor is 1.0x.** It is reached if p3 ≤ 0.4, so that Phase III spend is near-certain. The honest range is therefore about 1.0–2.3x, with a central estimate around 1.5x. The upper and central values depend on facts neither side can verify.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: excluded delivery costs (procurement, monitoring, adverse-event management) are incurred on success and offset the understatement, with an undetermined net sign.

Response:

1. **This is a separate error, not an offset.** If the cost side omits delivery costs while the benefit side includes uptake by 3.3M people, that is its own mismatch. Two errors in opposite directions do not cure the asymmetry. They only bias the result by an amount that depends on their relative size.
2. **The offset shrinks under consistent weighting.** The Advocate says delivery costs are incurred only on success. If they were added on the same expected-value basis as the benefit, they would be weighted by about 0.40.
   - Adding delivery cost D nominally overstates the offset by 2.5x relative to adding 0.40 × D.
   - The Advocate has not quantified D, so the offset is speculative in both size and sign.
3. **The Advocate concedes the benefit-side omissions.** Morbidity, lung damage and the diagnostic are not offsets to a cost-weighting error.

**KEY UNRESOLVED QUESTIONS:**

- Is the $7M a nominal budget or an expected spend? This is the single fact that decides whether the critique applies. It requires inspecting the CEA build-up.
- How is the $7M split between Phase II costs, which are incurred unconditionally, Phase III costs, and post-trial costs?
  - The critique's formula gates all $6.7M (the non-CG share). That share may include unconditional Phase II spend, in which case the effect shrinks.
  - Post-trial costs gated by 0.40 would increase the effect.
  - The net direction is not determinable from the published text.
- Is $0.32M (about 4.5% of $7M) CG's own funding of an early stage that is certain to occur, as the critique's formula assumes?
- What is a defensible TB Phase III success rate? Neither side has a grounded reference class, and the central range of 1.2–1.7x depends on it.

### Judge Audit
Surviving strength: moderate
Justification: The Advocate made a grounded derivation (s = 0.40/p3) that narrowed the critique's range, and the Challenger conceded it. The Challenger in turn correctly showed that the Advocate's range is not a ceiling and caught the Advocate's materiality error. Both sides relied on ungrounded stage-success inputs (the Advocate's p3 priors and the Challenger's √0.40 split) to produce "central" figures. As a result, the magnitude is illustrative rather than established. The critique survives as a credible, directionally correct, conditional concern whose applicability hinges on one uninspected fact.
Recommended action: 2. SPECIFIC INVESTIGATION: Inspect the CEA cost build-up, or ask CG directly, to answer three questions:
   - **(a)** Is the $7M a full-pathway budget or a probability-weighted spend?
   - **(b)** How is it split among Phase II costs (unconditional), Phase III costs (gated by p2), and guideline/dissemination/validation costs (gated by roughly 0.40)?
   - **(c)** Does the $0.32M CG share correspond to an early, certain stage?

   With that split, the expected cost can be computed directly. If p2 is also needed, anchor it to published infectious-disease phase-transition rates rather than a symmetric split. This is a single document request or spreadsheet inspection and is feasible.

   Until that check is done, the critique stands as a conditional concern: the direction is upward, and the realistic magnitude is likely 1.0–1.7x rather than up to 2.3x, with the low end possibly immaterial.
Action feasibility: requires_specified_evidence
Advocate failures: ['sound_synthesis_noted: The Advocate derives "s = p2 = 0.40 / p3" from the staged structure of the joint probability, which the BOTEC defines as the chance that "Phase II and Phase III trials both succeed." From this it shows that s = 0.4 requires p3 = 100% and s = 0.6 requires p3 ≈ 67%. The derivation is clean and the arithmetic in the table checks out: 0.32 + 0.8 × 6.7 = 5.68, giving 1.23x; 0.32 + 0.571 × 6.7 ≈ 4.15, giving 1.69x. This was the most productive move in the debate, and the Challenger conceded it.', 'unsupported_estimate_pseudo: The p3 inputs of 0.5 and 0.7 are disclosed as "uninformed priors, not sourced figures." The Advocate then calls the output "a plausible range [of] roughly 1.2–1.7x." The disclosure is honest. However, calling the result "plausible" gives it more authority than two arbitrary inputs can support. The range is an illustration, not an estimate.', 'false_definitiveness: In the overall assessment, the Advocate says the 1.2–1.7x understatement "is meaningful, above the 25% materiality threshold." This is wrong. The Advocate\'s own 1.23x row falls below 25%. The Challenger correctly caught it.', 'false_definitiveness: The Advocate says treating 40% as a joint probability "already partly addresses the critique, because the benefit side is gated by the whole sequence." Gating the benefit is half of the alleged asymmetry, not a remedy for it. The claim of coverage is asserted without any mechanism on the cost side.']
Challenger failures: ['unsupported_estimate_counter: A symmetric split of the 0.40 joint probability gives p2 = p3 = √0.40 ≈ 0.63 … multiplier ≈ 1.54x," which the Challenger then labels a "central estimate.', 'strawmanning: The Challenger argues that "Adding delivery cost D nominally overstates the offset by 2.5x relative to adding 0.40 × D." The Advocate never proposed adding D nominally. The Advocate explicitly said delivery costs are "incurred only on success," which implies probability weighting.', "sound_synthesis_noted: The limiting-case calculation is correct: 7 / (0.32 + 0.4 × 6.7) ≈ 2.33x if all post-Phase III costs are gated by 0.40. It properly shows that the Advocate's 1.2–1.7x table is not a ceiling once the Advocate's own concession about post-trial costs is applied. The Challenger also correctly separated UNVERIFIABLE from REJECTED and framed the critique conditionally."]
Debate resolved: The debate established the following:
- **Direction:** If the $7M is a nominal budget, SROI is understated, and both sides agree on this direction.
- **The 2.3x figure:** It is not a realistic Phase III-only case. It requires either p3 = 1 or all $6.7M being post-trial spending gated at 0.40.
- **Most of the $6.7M is Phase III spending:** The Phase III-gating effect plausibly falls in a low-to-mid range, roughly 1.2–1.7x, under illustrative assumptions.
- **Low end not material:** The low end of that range sits at or below the 25% materiality threshold.
Debate unresolved: The decisive fact remains unresolved: whether the $7M is a nominal budget or an expected spend. Neither side could answer it.

The composition of the $6.7M also surfaced as a genuinely open question that cuts both ways:
- Unconditional Phase II spending would shrink the effect.
- Post-trial spending gated at 0.40 would enlarge it.

The size of the excluded delivery-cost offset also remains unquantified.

--- Critique: A 1-year speedup of trial results does not necessarily become a 1-year speedup of adoption, in either direction. ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION: A 1-year speedup of trial results does not necessarily become a 1-year speedup of adoption

**EXISTING COVERAGE:**

- CG's 1-year figure is a point estimate of an expected speedup, and the critique does not show it is biased. The critique's own summary says the direction is "uncertain (slightly toward ≈1 year or modestly less)."
- SROI is linear in `speedup_years`, as the critique's Mechanism section states. Expected SROI therefore depends only on the mean of the speedup distribution, not its spread.
- The critique's two mechanisms point in opposite directions: lost guideline cycles push the speedup above 1, and slack absorption pushes it below. Without probabilities for either, it gives no reason to think the mean differs from 1.
- The recommended "sensitivity band instead of a point value" widens the uncertainty range. It does not move expected SROI unless the band is asymmetric, and the critique does not argue that it is.
- The ramp-shape concern is already neutralized by the structure of a horizontal shift. This is my own derivation, not a cited source.
  - Let A(t) be the adoption curve rising to a plateau A∞. A speedup of s shifts it to A(t+s).
  - Undiscounted benefit gained = ∫[A(t+s) − A(t)]dt = s·A∞, whatever the ramp shape.
  - So the model's "1 year × plateau-year benefit" arithmetic is exact for a pure shift. Only the size of s matters, not whether uptake jumps or ramps.
  - The 2% annual decline in cases changes this only slightly over a one-year shift.

**EVIDENCE WEAKNESSES:**

- The critique's own evidence package supports the model more than it undercuts it.
  - The two TB regimen cases show WHO's guideline group responding within about 1–2 months of data being shared.
  - That makes a near-1-year speedup at the WHO stage plausible, and it weakens the "fixed guideline cycle" mechanism the critique raises.
- The "lumpy cycle" mechanism is, by the critique's own admission, UNGROUNDED for TB. Treated conditionally, it is a possibility with no probability or magnitude attached, so it cannot show a deviation from 1 year.
- The post-WHO lag concern is "untested here." The critique has no source on national policy or procurement lags for adjunct therapies.
- The critique has no sensitivity results (`{}`), so it never shows that any plausible band crosses the materiality threshold.

**MAGNITUDE CHALLENGE:**

- By the critique's own calculation, the threshold is a speedup of about 0.65 years, i.e. a reduction of more than a third.
- Slack absorption would have to bind for more than a third of the year. The critique offers no evidence for that.
- Post-WHO lags (national adoption, procurement) shift the whole downstream chain by the same year if they are fixed durations that start after the guideline. Only calendar-gated steps, such as replenishment or national review cycles, absorb a speedup.
- A slower process for a generic adjunct does not by itself shrink the speedup. It lengthens the lags but shifts the curve equally. This weakens the critique's "generic adjunct may face a slower process" point as an argument for a speedup below 1.
- A calendar-gated step can also create the upside the critique identifies, where a lost cycle makes the effective speedup exceed 1. The sign is genuinely two-sided.

**OFFSETTING FACTORS:**

- The upside (a lost cycle) and the downside (slack absorption) are explicitly offsetting in the critique's own framing.
- The WHO-stage evidence points to speedup ≥ roughly 1 at that stage. That leaves the downside risk concentrated in the untested post-WHO steps.

**OVERALL ASSESSMENT:** Strong defense.

- The critique is a variance and definitional point, not a demonstrated bias in the mean.
- It is rated "low-to-medium" with uncertain direction and no quantification.
- Because SROI is linear in the speedup, symmetric uncertainty leaves the expected SROI near 3,000x.
- The critique would need to show a mean speedup below about 0.65 years to threaten the ~2,000x bar, and it does not.

**CONCESSIONS:**

- CG gives no justification for exactly 1 year. The figure is an assumption, not a derived quantity.
- The "trial-result date" is undefined. "Available to WHO" and "published" differ, and the BPaLM case shows WHO acting on pre-publication data.
- Two sponsor-supported TB regimen trials do not establish WHO lag for a generic adjunct such as atorvastatin, so the WHO-stage evidence generalizes imperfectly.
- No source quantifies post-WHO lags (national policy, procurement) for host-directed therapies. I cannot ground a claim that these lags are fixed-duration rather than calendar-gated, so I treat that as an uninformed prior.
- A sensitivity band on `speedup_years` would improve transparency, even if it does not move the central estimate.

### Challenger
REBUTTAL: A 1-year speedup of trial results does not necessarily become a 1-year speedup of adoption

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: CG's 1 year is an expected-value point estimate. SROI is linear in `speedup_years`, so only the mean matters, and the two mechanisms (lost cycle up, slack absorption down) offset each other, so the mean is plausibly 1.

1. **The mean is not established.**
   - The Advocate concedes that "CG gives no justification for exactly 1 year."
   - The defense calls 1 year "an expected speedup," but that is the Advocate's reading. A figure with no derivation cannot be assumed to be a mean.
   - Linearity makes the mean the only thing that matters. It does not tell us the mean is 1.

2. **The offset argument conflicts with the evidence the Advocate relies on.**
   - The Advocate uses the TB cases (WHO acting 1–2 months after data) to say the WHO stage supports about 1 year.
   - That same evidence weakens the fixed-guideline-cycle mechanism for TB. Without a fixed cycle, the "lost cycle" upside goes away.
   - The Advocate then states "WHO-stage evidence points to speedup ≥ roughly 1." The evidence supports ≈1, not ≥1.
   - At the WHO stage, the distribution is therefore capped near 1 with little upside.
   - Any post-WHO deviation can only be neutral or downward, unless a calendar-gated national step creates a new upside.
   - The Advocate's one-sided offset is therefore not grounded for TB. The Advocate admits it cannot ground whether post-WHO lags are fixed-duration or calendar-gated.
   - So the symmetric-offset claim and the downside-concentration claim cannot both stand. The Advocate asserts both.

3. **The horizontal-shift derivation assumes what the critique questions.**
   - ∫[A(t+s) − A(t)]dt = s·A∞ is correct for a pure translation of the curve.
   - The critique's slack-absorption mechanism is precisely a case where the curve is not purely translated. Some steps are calendar-gated while others shift, so the curve is partly compressed or partly unmoved.
   - Calling the ramp-shape concern "neutralized" is circular. The derivation shows the arithmetic is right if s is the true shift. It says nothing about whether s equals the trial speedup.
   - I concede the narrower point that ramp shape per se does not matter for a pure shift.

4. **The mean's link to the bar is not remote.**
   - Using the Advocate's own numbers (~3,000x at s=1, ~2,000x bar, linear), SROI ≈ 3,000 × s.
   - An average speedup of 0.5 years gives ~1,500x, below the bar.
   - The threshold is s ≈ 0.65 to 0.67, so a mean reduction of about a third crosses it. I cannot say how likely that is.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the critique's evidence supports the model, the lumpy-cycle mechanism is ungrounded, the post-WHO lag is "untested," and the empty sensitivity results show no crossing of materiality.

1. **Concession.** The two TB cases do support near-1-year speedup at the WHO stage and do weaken the lumpy-cycle story. The critique says this itself.

2. **"Untested" is not "rejected."**
   - The verifier found no source on post-WHO or adjunct-therapy lags. That is UNVERIFIABLE, not REJECTED.
   - The Advocate cites the absence of a source as a weakness of the critique. But the 1-year figure has no source for these stages either, and the Advocate admits this.
   - Conditionally: if post-WHO steps are calendar-gated or slower for a generic adjunct, the speedup is below 1. The Advocate concedes it cannot rule this out.

3. **The empty `{}` sensitivity is not evidence of immateriality.** It reflects that no analysis was run. The linear arithmetic above can be done by hand.

4. **Generic-adjunct generalization.**
   - The Advocate says a slower process "shifts the curve equally." That holds only if the added lag is fixed-duration and starts after the trial result.
   - A slower, less sponsor-driven process is more likely to depend on advocacy, meetings, or national review cycles. These are calendar-gated, not fixed-duration.
   - I cannot ground this. It is an uninformed prior, and the Advocate's fixed-duration assumption is the same.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

1. **Slack must bind "more than a third of the year."**
   - This is a statement about average absorption across all steps, not about one step.
   - Several calendar-gated steps (national review, procurement or funding cycles) could each absorb part of the year.
   - I have no data on their number or length.

2. **Honest minimum.** If WHO-stage evidence generalizes and post-WHO lags are fixed-duration, the impact is near zero. That scenario is live, and the critique's own "low-to-medium" rating reflects it.

3. **The definitional gap is a separate, real issue.**
   - The Advocate concedes the "trial-result date" is undefined.
   - If "available to WHO" differs from "published" by several months, the effective speedup depends on which date the 1-year refers to.
   - This can move s in either direction, but the model does not specify it.

**RESPONSE TO "OFFSETTING FACTORS":**

1. **The offsets are not shown to exist in TB.** The upside requires fixed cycles that the TB evidence weakens. The downside is untested.

2. **The offsets are not in the model.** The model has a single point value and no mechanism, so it neither captures nor balances either direction.

3. **A calendar-gated post-WHO step could create upside, as the Advocate says.** I accept this. But the Advocate's own concession that the lag structure is ungrounded means the offset is as speculative as the downside.

**KEY UNRESOLVED QUESTIONS:**
- Are post-WHO adoption steps (national policy, procurement) for a generic adjunct fixed-duration after the guideline, or calendar-gated? This determines whether s is below, at, or above 1.
- Is the "1 year" defined relative to trial completion, results availability to WHO, or publication? The BPaLM case shows these can differ.
- Does the TB WHO-stage responsiveness (two sponsor-supported regimen cases) extend to an adjunct drug without a sponsor pushing the process?
- What is the model's implied mean? Without a derivation of the 1 year, the "mean is 1" claim cannot be checked.

### Judge Audit
Surviving strength: weak
Justification: - The Challenger's best grounded move exposed the Advocate's inconsistent symmetry argument, but it did not establish a downward-biased mean.
- Its downward case for post-WHO steps rested on an acknowledged uninformed prior and on a calendar-gating inference that does not hold in expectation.
- The only evidence in the package (two TB cases) supports the model's 1:1 translation at the WHO stage. The critique's own lumpy-cycle mechanism was conceded as ungrounded.
- Nothing in the debate brought a mean reduction of more than a third into evidential view.
- What survives is a variance and definitional point, not a threat to the central estimate.
Recommended action: 1. CONCLUDE NOW, with moderate confidence:
   - Retain speedup_years = 1 as the central estimate. The debate produced no grounded reason to think the mean is below about 0.65, and WHO-stage TB evidence supports about 1.
   - Adopt two low-cost fixes from the critique:
     - (a) Define the trial-result date as "results available to WHO GDG," consistent with BPaLM and Study 31 practice.
     - (b) Report a sensitivity band on speedup_years, for example 0.5–1.25, noting that SROI crosses the 2,000x bar only below about 0.67.
   - Optional, feasible follow-up: for the 4-month HP-Moxi and BPaLM regimens, compare WHO rapid-communication dates against national guideline adoption and GDF procurement dates in several high-burden countries. This would test whether post-WHO steps behave as fixed lags or as non-trial binding constraints. It could change the band, but it is unlikely to change the central estimate.
Action feasibility: actionable_now
Advocate failures: ['sound_synthesis_noted: The horizontal-shift derivation, ∫[A(t+s) − A(t)]dt = s·A∞. The derivation is correct, the Advocate labels it as their own reasoning, and the Challenger concedes the narrow point. It also establishes that only s matters for a pure translation.', 'strawmanning: The Advocate frames the derivation as neutralizing a "ramp-shape concern." The critique never raised ramp shape. Its hypothesis was that the size of s may not equal the trial speedup when the trial is not the binding constraint at every step. The derivation is sound but answers a question the critique did not ask. It was then presented under "EXISTING COVERAGE" as if it addressed the critique.', 'false_definitiveness: The WHO-stage evidence points to speedup ≥ roughly 1 at that stage." The evidence package supports roughly 1 (GDG convened about 1 month after Study 31 data, BPaLM GDG timed to data availability). It does not support "≥". The evidence actually removes the lost-cycle upside rather than establishing it. The Challenger correctly caught this.', 'false_definitiveness: Under OFFSETTING FACTORS, the Advocate first calls the two mechanisms "explicitly offsetting." Two lines later it says "the downside risk [is] concentrated in the untested post-WHO steps." It then concludes "symmetric uncertainty leaves the expected SROI near 3,000x." The Advocate concedes an asymmetry and then asserts symmetry, which leaves the mean-equals-1 conclusion internally inconsistent.']
Challenger failures: ['sound_synthesis_noted: SROI ≈ 3,000 × s … threshold s ≈ 0.65 to 0.67." This correctly derives the threshold from the model\'s linearity and the bar of about 2,000x. The 0.5-year example is explicitly illustrative and conditional, not an estimate.', 'whataboutism: the 1-year figure has no source for these stages either… the Advocate\'s fixed-duration assumption is the same." This responds to "the critique has no source for post-WHO lags" by pointing to the model\'s own lack of grounding.', 'call_to_ignorance: Conditionally: if post-WHO steps are calendar-gated or slower for a generic adjunct, the speedup is below 1. The Advocate concedes it cannot rule this out." Also: "Several calendar-gated steps… could each absorb part of the year. I have no data on their number or length." The Challenger acknowledges the gap and then uses the possibility directionally.', 'unsupported_estimate_pseudo: A slower, less sponsor-driven process is more likely to depend on advocacy, meetings, or national review cycles. These are calendar-gated, not fixed-duration." This is not numeric, but the inference chain has a logical gap of the same kind. Calendar gating with unknown phase is mean-preserving, so the step does not entail a downward shift in the mean of s. The Challenger acknowledges the claim is an "uninformed prior" but still treats it as directionally downward.', 'strawmanning: The Challenger calls the shift derivation "circular" because "it says nothing about whether s equals the trial speedup." The Advocate never claimed it did. The Advocate claimed only that "only the size of s matters, not whether uptake jumps or ramps." The underlying observation is valid, because the derivation is non-responsive to the critique. But "circular" mischaracterizes the Advocate\'s claim.']
Debate resolved: Both sides accept the following:
- For TB, the WHO guideline stage translates a trial speedup roughly one-for-one.
- The fixed-cycle / lost-cycle upside is not supported at that stage.
- Ramp shape is irrelevant for a pure shift.
- The materiality threshold is a mean speedup of about 0.65–0.67 years.
- A sensitivity band and an explicit trial-result-date definition would improve the model without changing the central estimate.
Debate unresolved: Neither side grounded any claim about whether post-WHO steps (national policy, procurement, funding) for an unsponsored generic adjunct involve:
- a non-trial binding constraint, which would bias s downward, or
- merely fixed-duration or calendar-gated lags, which would be mean-preserving.

Neither side clearly separated these two mechanisms. The undefined reference date ("available to WHO" versus "published") also remains unresolved.

--- Critique: Post-TB lung disease morbidity is likely the largest unvalued channel (~50–60k central, wide range) ---

### Advocate
**DEFENSE OF GIVEWELL'S POSITION (CG): Post-TB lung disease morbidity as an unvalued channel**

**EXISTING COVERAGE:**
- CG states that only mortality is valued. The parameter map notes that morbidity, lung damage and diagnostics are deliberately outside the formula. This is a stated conservative simplification, not an oversight. A conservative omission that raises the estimate if corrected is a different kind of flaw from an inflated parameter.
- CG's headline is ~3,000x against a ~2,000x bar, a ~50% cushion. The Challenger's own central estimate (~55k DALYs) leaves the decision unchanged.
- Derivation: 55k / 539.5k base DALYs ≈ 10% uplift. That is below the ~25% materiality line in the run instructions.
- Only the Challenger's upper tail (~300k / 539.5k ≈ 56%) crosses that line. The Challenger says the channel "reaches the threshold only in the upper half of the range."
- The Phase IIc trial is described as testing "lung damage" as an outcome. If lung benefit is real, the grant's trial design would surface it, so the channel is not ignored in the research plan.

**EVIDENCE WEAKNESSES:**
- **The central input has no source.** The Challenger says the 5% effect size is unsupported and the "lung damage signal" premise is UNVERIFIED. The channel's central value is therefore a product of two inputs the critique itself cannot ground.
- **ROSETTA points the other way.** Per the Challenger's own evidence, ROSETTA found no lung benefit on x-ray, spirometry or PET-CT. If ROSETTA is the relevant adjacent trial, the lung effect may be zero. The 5% central is then not "deliberately lower than the signal" but an effect with no confirmed signal behind it.
- **The surrogate gap is large.**
  - CG's context cites reduced lung damage on chest X-ray in a Phase IIa/b trial.
  - The baseline burden (post-TB impairment, disability weight 0.1–0.2 over 15–25 years) is a different construct from short-term radiographic change.
  - The Challenger supplies no link between X-ray improvement and long-run functional impairment.
- **The baseline is an inference, not a measurement.**
  - The ~30% impairment share, the 0.1–0.2 disability weight (flagged "which I'd verify") and the 15–25 year duration are all unsourced.
  - Menzies 2021 is cited for 5.8 post-TB DALYs per case, but the Challenger concedes it mixes morbidity and mortality.
  - Using it to raise the baseline would double-count with Critique 2, as the Challenger acknowledges.
  - The "several times larger" ceiling is therefore not a clean morbidity figure.

**MAGNITUDE CHALLENGE:**
- **The 0.45 probability weight is generous.**
  - It adds a branch where the mortality endpoint fails but a lung benefit still drives adoption.
  - CG's 60% uptake is justified by "if it works" on mortality (survival is the headline outcome). A drug adopted on a lung surrogate alone, after ROSETTA-type null findings, would plausibly see lower uptake and slower guideline adoption.
  - Applying full 60% uptake and full adoption to that branch overstates it. The weight is more plausibly 0.4 or below, which trims the central estimate by at least ~10% (0.40/0.45 ≈ 0.89).
- **Discounting cuts the channel.** The Challenger concedes the no-discounting convention inflates it.
  - Annuity factor over 20 years at 4%: (1 − 1.04⁻²⁰)/0.04 ≈ 13.6, versus 20 undiscounted, so ~68% before any deferral.
  - Post-TB DALYs start after treatment, so deferral lowers the factor further.
  - The 4% rate is my illustrative choice, not a CG-specified rate.
  - Applied to a ~55k central, this gives roughly ≤37k, a ≤7% uplift on the 539.5k base. The mortality DALYs would also shrink, but morbidity is back-loaded, so its share falls.
- **The upper range is not defensible on current evidence.** The 15% reduction and 1.5 DALY baseline combine two unsupported maxima. CG's own mortality effect is only 10% relative, and a lung-function effect larger than the mortality effect has no cited basis.
- **The central case for the mortality channel's relative size is unchanged.** On the Challenger's numbers the channel adds ~10% at the central estimate.

**OFFSETTING FACTORS:**
- **Unaccounted downside risks sit beside this upside.** The parameter map lists hepatotoxicity with isoniazid/rifampicin/pyrazinamide and myopathy as unmodeled. It also lists rifampicin-reduced statin exposure and unreachable early deaths. All of these push the other way, so the net effect of "adding what was left out" is not clearly upward.
- **Mortality-channel interaction.** The 27 DALYs per averted death does not net out post-TB morbidity in survivors, but the Challenger does not examine this. Lives saved who then live with lung impairment would have somewhat lower DALY value per death averted. I cannot ground the size of this, so treat it as an unquantified offset.
- **Correlation with p_success.** If the lung signal is spurious (ROSETTA), the mortality signal is also less likely to be real. The channel is then positively correlated with the main channel's failure, not additive in the success state. The Challenger's independent addition overstates the expected increment.

**OVERALL ASSESSMENT:** Partial defense.
- The channel's direction is upward and CG's zero is a real omission.
- The central magnitude (~10% uplift, ≤7% discounted) is below the materiality line. The inputs are unsourced and partly contradicted by ROSETTA. The probability weight is generous.
- The critique has merit as a "report this in the writeup" item, but not as a basis to move the SROI estimate materially.

**CONCESSIONS:**
- Assigning zero value to a plausibly nonzero channel is a genuine omission. If the lung benefit is real, it is a conservative bias.
- The 0.75 DALY baseline may be low relative to Menzies. I cannot show it is correct, because Menzies mixes mortality and morbidity.
- The upper tail (~300k) could push the estimate by more than 25%. I cannot rule that out on evidence, only argue it is poorly supported.
- CG should state explicitly that the morbidity channel is omitted. It should report discounted and undiscounted values if it includes it, and avoid overlap with the post-TB mortality channel.

### Challenger
REBUTTAL: Post-TB lung disease morbidity as an unvalued channel

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: CG's mortality-only scope is a deliberate, stated conservative simplification. The ~10% central uplift leaves a ~3,000x vs ~2,000x headline unchanged. The Phase IIc design tests lung damage, so the channel is not ignored.

- **Concede:** the central uplift is about 10% (55k / 539.5k). That is below the ~25% line, and the omission is conservative in direction.
- **A stated omission is not a valued term.** That the Phase IIc trial measures lung damage means the research plan will surface the benefit later. It does not put any value for it into the BOTEC now. The gap is real regardless of the trial design.
- **The "no change to decision" conclusion depends on the baseline.** Under the Advocate's own concession that 0.75 DALYs "may be low relative to Menzies", the central estimate can cross 25% (see Magnitude).
- **The cushion argument cuts both ways.** An upward omission is relevant precisely because it can offset downward adjustments to the mortality channel. Calling it "not material alone" does not show it is immaterial to the net estimate.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the 5% effect and the lung-signal premise are unsourced, ROSETTA points to zero, X-ray change is a weak surrogate for long-run impairment, and the baseline is inference.

- **The Advocate is internally inconsistent on the premise.**
  - They say the central input "has no source".
  - They also cite CG's own context that a Phase IIa/b trial showed reduced lung damage on chest X-ray.
  - So the premise has a grant-context attestation. What the critique left UNVERIFIED is which trial and how large the effect was, not whether any signal was reported.
  - The verifier marked this unverified, not rejected. The right framing is conditional: if the Phase IIa/b X-ray signal is real, the effect is not zero.
- **ROSETTA is conditional evidence, not a rebuttal.**
  - Whether ROSETTA tested the same agent or a comparable one is not established in the evidence package.
  - Conceded: if it is the relevant adjacent trial, the effect could be zero.
  - That is a reason to haircut the effect size or add a P(lung benefit real) term, which the critique's 0.45 does not explicitly include. It is not a reason to value the channel at zero.
- **Surrogate gap: conceded, and already priced in.**
  - The critique sets 5% "deliberately lower" than the trial signal to allow for attenuation.
  - The Advocate asks for an X-ray-to-function link. Its absence supports a lower effect size. It does not support a zero point estimate.
- **Baseline: the Advocate's Menzies objection supports a higher baseline, not a lower one.**
  - Menzies puts 5.8 of 12.1 DALYs per case in the post-TB phase (verifier evidence).
  - The critique's 0.75 would equal Menzies's post-TB figure only if morbidity were 0.75/5.8 ≈ 13% of post-TB DALYs.
  - So 0.75 is too low unless post-TB mortality accounts for more than ~87% of post-TB DALYs. I cannot ground that split.
  - Double-counting with Critique 2 is avoidable by netting out the mortality share. It is a bookkeeping issue, not a reason to leave the baseline at 0.75.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: 0.45 should be about 0.40, discounting cuts the channel to ≤37k (≤7% uplift), and the 15% / 1.5 DALY upper range has no basis.

- **0.45 → 0.40 is a ~11% trim of a ~55k figure, about 6k DALYs.** It is immaterial.
- **The discounting calculation is internally inconsistent.**
  - The Advocate discounts the numerator (55k → ≤37k) but divides by the undiscounted 539.5k base.
  - They concede the mortality DALYs would also shrink. The 27 DALYs per averted death is also a long-horizon quantity.
  - The relevant ratio is discounted morbidity over discounted mortality. Mortality is also back-loaded, so the ratio falls by less than 32%.
  - The "≤7%" figure therefore overstates the discounting effect.
- **The Menzies-based baseline pushes the central estimate across the line.**
  - The channel is linear in baseline. The critique's 55.7k = 3.3M × 0.75 × 0.05 × 0.45.
  - Scale by (5.8f / 0.75), where f is the morbidity share of Menzies's post-TB DALYs. I cannot ground f, so I show the sensitivity:

| f | Baseline (DALYs) | Channel | Uplift on 539.5k |
|---|---|---|---|
| 0.25 | 1.45 | ≈108k | ≈20% |
| 0.50 | 2.9 | ≈215k | ≈40% |

  - The 25% line (~135k) is crossed at f ≈ 0.31, holding 5% effect and 0.45 weight fixed.
  - Caveats: Menzies's figures are undiscounted per case, and equating them to "per treated patient" is an assumption.
- **Minimum plausible:** the critique's low end is ~10k (≈2%), which is immaterial. If the lung effect is truly zero, the channel is zero. I concede this.
- **Upper tail (15%):** the Advocate is right that it is weakly supported. Mortality and lung-damage relative effects are on different scales, so the 10% mortality effect does not bound the lung effect. I cannot ground 15%, so I rest the case on the central 5% with a higher baseline.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: unmodeled harms (hepatotoxicity, myopathy, statin interaction) push the other way, lung-impaired survivors lower the mortality value, and lung benefit is correlated with p_success so the addition overstates.

- **Unmodeled harms:**
  - The Advocate gives no magnitude for these.
  - An unquantified downside cannot net against a quantified upside, and the parameter map does not size them.
  - Conceded: they are real omissions of opposite sign. That makes the net direction unknown, not clearly upward or downward.
- **Survivor impairment offset is bounded, using the critique's own inputs (unverified):**
  - 30% impairment × ~0.15 disability weight ≈ 4.5% of remaining-life value for averted deaths.
  - That is small relative to a channel that can be 10–40% of the base.
  - It also applies only to averted deaths, and the same drug is claimed to reduce that impairment.
- **The correlation argument has the sign wrong for the main branch.**
  - Expected value is additive regardless of correlation. Correlation changes variance and the conditional structure.
  - If lung benefit and mortality success are positively correlated, then in the p_success = 0.4 state lung benefit is more likely real, which raises the increment there.
  - Correlation does shrink the small "mortality fails, lung real" branch (~0.05 of the 0.45).
  - Conceded: the critique has no explicit P(lung real) term, and ROSETTA justifies a haircut there.

**KEY UNRESOLVED QUESTIONS:**
- Which trial showed the lung signal, and does ROSETTA apply to the same agent or a comparable one?
- What fraction of Menzies's 5.8 post-TB DALYs per case is morbidity rather than mortality? The 25% materiality line is crossed at f ≈ 0.31.
- Should the comparison be discounted morbidity over discounted mortality? The Advocate's ≤7% figure mixes the two bases.
- What is P(lung benefit real) conditional on mortality success? It is currently absent as an explicit term.
- How large are the unmodeled harms (hepatotoxicity, myopathy, statin interaction)? Until they are sized, the net direction of the omissions is unknown.

### Judge Audit
Surviving strength: moderate
Justification: - The debate was largely substantive. Both sides offered grounded derivations, and the failure modes were real but secondary.
- The Challenger successfully defended the omission's existence and exposed the Advocate's mixed-base discounting error.
- The Challenger's route to materiality rests on an ungrounded f and on an effect-size premise the verifier rates as unverifiable and possibly contradicted by a same-class trial. The Challenger conceded both points.
- The critique therefore survives as a valid but, at central inputs, sub-material omission (~10%). Its materiality claim remains conditional and unproven.
Recommended action: 2. SPECIFIC INVESTIGATION: Two targeted checks would move the answer, and both are feasible with existing tooling:

1. **Menzies decomposition.** Extract from Menzies et al. 2021 (Lancet Global Health) the YLD vs YLL decomposition of post-TB DALYs, and whether the figures are discounted. This directly yields f and determines whether the f ≈ 0.31 break-even is reached. While doing so, check the disability weights Menzies assigns to post-TB lung disease against the critique's 0.1–0.2 assumption.

2. **Lung-signal trial.** Identify the Phase IIa/b trial cited in CG's context for the chest X-ray lung-damage signal. Record the agent, effect size and sample size, and compare it with ROSETTA's null findings. If the cited trial is small or uses the same statin class, apply an explicit P(lung benefit real) haircut, plausibly well below 1.

Interim conclusion, pending these checks:
- Add the channel to the writeup as an acknowledged conservative omission at ~10% central uplift (undiscounted), with a discounted variant computed on a consistent base.
- Net it against the post-TB mortality share to avoid overlap with Critique 2.
- Do not revise the headline estimate on the strength of this channel alone.
Action feasibility: requires_specified_evidence
Advocate failures: ['unsupported_estimate_pseudo: The discounting argument concludes that the channel falls to "≤37k, a ≤7% uplift on the 539.5k base." The 0.68 annuity factor is shown and is arithmetically fine. The problem is the denominator. The Advocate discounts the numerator but divides by the undiscounted mortality base, while conceding in the same paragraph that "the mortality DALYs would also shrink." That is a clear logical gap, because the ratio mixes discounted and undiscounted bases. The claim that "morbidity is back-loaded, so its share falls" is also asserted without derivation. Averted-death YLLs (~27 per death) plausibly extend over a longer horizon than 15–25 years of post-treatment morbidity, so the direction is not obvious.', 'unsupported_estimate_counter: The weight is more plausibly 0.4 or below." The move to 0.40 is a reasonable "drop the side branch" adjustment. The "or below" has no grounding. The Challenger correctly showed this matters by only ~6k DALYs, so the move is low-stakes.', 'misrepresenting_evidence_status: The central input has no source… an effect with no confirmed signal behind it." In the same section the Advocate cites "CG\'s context cites reduced lung damage on chest X-ray in a Phase IIa/b trial." The verifier marked the lung-signal premise UNVERIFIABLE, not REJECTED. A grant-context attestation exists. Collapsing "unverified" into "no source" overstates the case, and the Challenger rightly caught the inconsistency.', 'whataboutism: The "Offsetting factors" section invokes hepatotoxicity, myopathy and the rifampicin–statin interaction as unmodeled downsides "beside this upside." These are separate omissions with no magnitude attached. They do not bear on whether this channel\'s value is correctly estimated. They are relevant to the net BOTEC, but deployed here they deflect from the channel-specific question.', 'sound_synthesis_noted: The materiality derivation (55k / 539.5k ≈ 10%; 300k / 539.5k ≈ 56%) is grounded in verifier-confirmed arithmetic. The Challenger conceded it.']
Challenger failures: ['false_definitiveness: The section header "The Menzies-based baseline pushes the central estimate across the line" asserts that the threshold is crossed. The body then admits "I cannot ground f," and the crossing occurs only if f > ~0.31. The later phrase "a channel that can be 10–40% of the base" similarly leans on the ungrounded upper f value as though it were an established range.', 'misrepresenting_evidence_status: Whether ROSETTA tested the same agent or a comparable one is not established in the evidence package." The verifier identifies ROSETTA as a rosuvastatin trial, and the debate context makes clear the intervention is a statin. ROSETTA\'s comparability as a same-class trial is reasonably established. Only same-agent identity is open. This understates the counter-evidence, although the Challenger then partially concedes a haircut is warranted.', 'sound_synthesis_noted: The f-sensitivity table is a transparent conditional synthesis. It uses linear scaling of the verified arithmetic, solves for a break-even f ≈ 0.31, and states its caveats (undiscounted, per-case ≠ per-treated). The analysis is legitimate. Only the framing around it overreaches.', "sound_synthesis_noted: The survivor-impairment offset estimate (30% × 0.15 ≈ 4.5%) is explicitly labelled as using the critique's unverified inputs. It is engaged with conditionally, which is correct handling.", 'sound_synthesis_noted: Several rebuttals are correct and well-reasoned:']
Debate resolved: Both sides accept the following:
- CG's zero valuation of post-TB morbidity is a real, conservative-direction omission.
- At the critique's own central inputs the channel adds ~10% to the base, which is below the 25% materiality line.
- The 15% upper-tail effect is poorly supported.
- The 0.45 → 0.40 probability-weight dispute is immaterial (~6k DALYs).
- The Advocate's "≤7% discounted" figure is miscomputed because it mixes discounted and undiscounted bases. The discounting question is therefore not settled in the Advocate's favour.
Debate unresolved: Whether the channel becomes material depends on two inputs the exchange surfaced but could not ground:
- **The morbidity share f of Menzies's 5.8 post-TB DALYs.** The break-even is f ≈ 0.31. Unexamined disability-weight assumptions could also cut the baseline in the opposite direction.
- **Whether the lung effect is nonzero at all.** This turns on reconciling the CG-cited Phase IIa/b X-ray signal with ROSETTA's null results across x-ray, spirometry and PET-CT in a same-class statin trial.

--- Critique: Post-treatment excess mortality (~40–50k central) and a related sign-reversing adjustment ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION (CG): Post-treatment excess mortality and the related sign-reversing adjustment

**EXISTING COVERAGE:**
- CG does not model post-treatment mortality. The BOTEC states that only on-treatment mortality is valued, so the upside channel is an acknowledged zero. That is a conservative omission, not an oversight that inflates the estimate.
- The downside channel is partly covered by the 27 DALYs per death figure, which the BOTEC describes as remaining *healthy* life expectancy. It is therefore already below raw remaining life expectancy.
- The Quantifier's downside assumes deaths averted are valued at standard life expectancy. That assumption is not obviously true of a healthy-life-expectancy figure. The 5–10% overstatement is the Quantifier's own assumption, and the Quantifier flagged it as UNGROUNDED.
- Baseline mortality, 10% relative reduction, and 40% success probability are separate parameters. This critique touches none of them.

**EVIDENCE WEAKNESSES:**
- **Pooled SMR supports only the existence of an excess-death pool.**
  - The Romanowski 2019 pooled SMR of ~2.9 and the Cerqueira-Silva cohort support that survivors have elevated mortality.
  - The Quantifier says explicitly that neither source supports the 40% respiratory share or the 5% effect.
- **The upside is a product of three unsupported inputs.** These are a 10% excess mortality, a 40% respiratory share, and a 5% effect.
  - The Quantifier's own label for these inputs is "illustrative assumption" or UNGROUNDED.
  - I accept arguendo that each is plausible. The product has no stated uncertainty bounds, and the Quantifier's own range of 0–50k reflects that.
- **The 5% effect lacks a mechanism chain.** It requires that a statin's on-treatment effect on lung damage (an X-ray surrogate in a Phase IIa/b trial) translates into fewer deaths from respiratory sequelae years later. No evidence is given for that chain. Surrogate-to-long-term-outcome translation is also the very uncertainty the 40% p_success is meant to cover.
- **The downside is a logical argument, not a measurement.** The Quantifier gives no source for the 5–10% overstatement.
- **Double-counting risk.** The Quantifier concedes that Menzies's post-TB DALYs overlap with Critique 1. This critique's upside cannot be added to Critique 1 without netting.

**MAGNITUDE CHALLENGE:**
- **The two adjustments are on inconsistent bases.**
  - The upside is stated as ~100k pre-p, then ~45k after weighting. By my arithmetic, 0.4 × 100k = 40k, not 45k. The gap is small and unexplained.
  - The downside is applied to the unweighted 535k, giving −25k to −55k.
  - On a consistent pre-p basis, the net is about +100k − (27k to 54k) = +46k to +73k.
  - On a consistent weighted basis, the net is about +40k − (11k to 22k) = +18k to +29k.
  - So "nearly cancel" does not follow from the Quantifier's own numbers. The net is more likely mildly positive.
- **Decision relevance is low either way.**
  - The CG threshold is about 25% of the 539.5k DALYs.
  - The gross upside of ~100k pre-p is about 18.5% of 539.5k.
  - The consistent-basis net is roughly 3–14% of 539.5k.
  - None of these crosses the threshold.
- **Net effect on SROI.**
  - A +3% to +14% change would move ~3,000x to roughly 3,100–3,400x. It would not threaten the 2,000x bar.
  - The only direction in which it matters is up, and not materially.
- **The upside could be lower than assumed.** The 15 DALYs per death is applied to late deaths in survivors who already have an SMR of 2.9. If the 5% effect is optimistic, the upside shrinks toward zero. The Quantifier's range already includes zero.

**OFFSETTING FACTORS:**
- **Netting with Critique 1.** The Quantifier flags that the upside overlaps with Menzies's post-TB DALYs. If Critique 1 is accepted, this upside is largely already in it, and only the downside remains as new content.
- **Downside and upside are linked.** If the statin reduces lung damage, the saved patients' survival is not at the same excess-mortality level as the untreated population. The downside would shrink in the scenario where the upside is large. So treating them as independent overstates the spread of the net.
- **Probability weighting.** If the 5% effect is tied to the same success event as the 10% on-treatment effect, it should carry the same 40% p_success. That is already reflected in the weighted figure.

**OVERALL ASSESSMENT:** Strong defense.
- The Quantifier rates the strength as low-to-medium, the net as approximately zero with uncertain sign, and the materiality as "notable" only because of the gross upside.
- The central inputs are ungrounded.
- The critique's own numbers imply a net below the 25% materiality threshold on every consistent basis.
- CG's omission of this channel is conservative and disclosed.

**CONCESSIONS:**
- CG does not adjust for survivors' excess mortality, and the parameter map correctly lists this as a gap. Excess mortality in TB survivors is real.
- The downside logic is sound in principle. If averted deaths occur in people with higher baseline mortality, 27 DALYs per death is likely somewhat generous. I cannot ground the 5–10% size.
- The upside channel could be real if lung-damage reduction translates to long-term survival. The net direction is more likely positive than zero, contrary to the Quantifier's framing.
- Any inclusion should be done once, via Critique 1, with the downside netted in the same step.

### Challenger
REBUTTAL: Post-treatment excess mortality and the related sign-reversing adjustment

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: CG's omission of post-treatment mortality is a conservative, disclosed zero. The downside is partly absorbed because 27 DALYs/death is a *healthy* life expectancy figure, already below raw life expectancy.

- **Concede:** CG does not model the upside channel, and it says so. The Advocate also concedes the net is more likely positive than zero. Where the omission understates benefit, I accept the Advocate's "conservative" label.
- **Where "conservative" fails:** The critique has two opposite-signed parts. An omission that is conservative on the upside is not conservative on the downside. For the downside, the omission pushes the estimate up.
- **Healthy life expectancy doesn't address the downside.**
  - Healthy life expectancy is a population-level adjustment. It discounts for morbidity in a typical person of that age.
  - The downside concerns a different quantity: the elevated *mortality hazard* of the specific people whose deaths are averted.
  - Romanowski 2019's pooled SMR of ~2.9 (verified as supporting an excess-death pool) is a hazard multiplier. A morbidity-weighted general-population figure doesn't incorporate it.
  - I can't verify exactly how CG's 27 figure was built. The Advocate's claim that it "is already below raw remaining life expectancy" doesn't show it is below the life expectancy of *this* subpopulation.
- **The Advocate's "5–10% is the Quantifier's own assumption" cuts both ways.**
  - A crude bound: under a constant-hazard model, expected remaining life scales as 1/hazard, so an SMR of 2.9 could cut remaining life by up to ~65%.
  - This is a ceiling, not an estimate. SMRs decay with time since treatment, the pooled SMR covers all survivors rather than those saved at the margin, and constant hazard is unrealistic.
  - It does show that 5–10% is not obviously a cautious figure. The downside could be larger than the Quantifier stated.
  - I cannot ground a specific value. The point is only that the Advocate's defense doesn't constrain the downside's size.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: The upside is a product of three ungrounded inputs. The 5% effect lacks a mechanism chain from an X-ray surrogate to late respiratory deaths. The downside is logic, not measurement.

- **Concede:** The 40% respiratory share and the 5% effect are ungrounded. The verifier found the evidence supports the existence of the excess-death pool but not those two figures. I don't claim they are validated.
- **Status of the inputs:** The verifier's finding is that these inputs are unsupported, not that they are contradicted. They are a conditional hypothesis: *if* the statin reduces long-term respiratory mortality at all, the arithmetic applies. The Advocate's "no evidence is given" is accurate but doesn't show the effect is small.
- **Zero is also an estimate.** The model's implicit value for this channel is 0%. That is a specific assumption, with no more empirical grounding than 5%. The Advocate's own range (0 to ~100k pre-p) shows the real uncertainty is one-sided: the plausible values lie at or above zero.
- **Surrogate-to-outcome point:** The Advocate says this is "the very uncertainty the 40% p_success is meant to cover." That makes the point about double-counting, not about evidence. I concede the p_success weighting should apply here.
- **Double counting:** I concede the upside overlaps with Menzies-based post-TB DALYs in Critique 1. It should be netted, not added.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: On a consistent basis the net is +18–29k (weighted) or +46–73k (pre-p), not ~0, and all of that is under 25% of 539.5k, so decision relevance is low.

- **Concede:** The 45k vs 0.4×100k = 40k discrepancy is real and unexplained. I also concede the decision-threshold conclusion at these magnitudes, at least on the Advocate's reading of the bases.
- **The basis is ambiguous, and the Advocate resolved it in one direction.**
  - The critique says the downside is "applied to 535k" without stating whether 535k is pre- or post-p.
  - If 535k is already weighted, the downside is −25k to −55k against a +45k upside. The net is roughly −10k to +20k, which supports "nearly cancel."
  - I can't determine from the materials which reading is right. The Advocate's "net is mildly positive" depends on the choice, so the "cancel" claim is not refuted.
- **The Advocate's 3,000x → 3,100–3,400x SROI figures** are not in the critique or the verifier package. I can't confirm them.
- **Minimum magnitude:** The minimum is approximately zero, which both sides accept. The critique never claimed more than "notable" on a flagged hypothesis, so the Advocate's defense leaves intact the point that this is a bounded, unsigned issue.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: The downside shrinks if the upside is large, since saved patients no longer carry the full excess mortality. So treating the two as independent overstates the spread.

- **The link is quantitatively negligible by the critique's own numbers.**
  - The upside assumes a 5% reduction in the respiratory-attributed share of excess deaths. That share is 40% of the excess.
  - The reduction in total excess mortality is 0.05 × 0.40 = 2%.
  - The downside concerns the whole excess pool: HIV, malnutrition, advanced disease and so on. A 2% shrinkage cannot meaningfully offset a 5–10% downside.
- **The correlation is real in direction only.** The Advocate has described a correlation that is vanishingly small in size.
- **Netting with Critique 1:** I agree this is real and should be done once. Note the consequence: if the upside is absorbed into Critique 1, the downside is the only new content here, and it has no offset.
- **p_success weighting:** I agree it should apply to the upside, and the weighted figure already does so. It does not apply to the downside, which concerns on-treatment deaths already valued under p_success. That is part of why the bases matter.

**KEY UNRESOLVED QUESTIONS:**
- Is the 535k base for the downside pre- or post-p-weighting? The sign of the net depends on it.
- How was CG's 27 DALYs/death figure built? Does it reflect elevated mortality in the population whose deaths are averted, or only a morbidity adjustment?
- What is the actual size of the life-expectancy overstatement for patients with an SMR near 2.9? The 5–10% figure is ungrounded and could be low.
- Is there any evidence linking statin-induced lung-damage reduction to long-term respiratory mortality? That would settle whether the upside is above zero.
- Once the upside is netted into Critique 1, is the remaining downside quantified anywhere?

### Judge Audit
Surviving strength: weak
Justification: The debate was reasonably productive. Both sides offered sound syntheses, including the basis recomputation, the 2% offset quantification and the hazard ceiling. The verdict is weak because the critique has little decision-relevant content left after that engagement, not because the debate was unproductive.
- The Challenger conceded the materiality conclusion and the double-counting.
- The Challenger conceded that the upside inputs are ungrounded.
- The Challenger's surviving points are an ambiguity about the basis and an unsized downside, and both sit within a range the Challenger accepts is below threshold.
- The critique's own claim ("net ≈ 0, uncertain sign, low-to-medium") survives, but that claim does not threaten the CEA.
Recommended action: 1. CONCLUDE NOW: Make no separate adjustment for this critique (moderate-to-high confidence).
   - Handle the post-treatment upside only through Critique 1's Menzies-based post-TB DALYs, to avoid double-counting.
   - Record the residual downside as a disclosed qualitative caveat. That caveat is that averted on-treatment deaths may occur in people with elevated mortality hazard, so 27 DALYs/death may be generous.
   - On any reading of the bases, the net is below the materiality threshold and cannot move the SROI below the 2,000x bar.

   Optional verification, a document lookup rather than research: check in the CG BOTEC whether the 535k figure is pre- or post-p_success, and how the 27 DALYs/death was derived. This would fix the sign of the net, but it would not change the decision.
Action feasibility: actionable_now
Advocate failures: ['strawmanning: The Advocate defended against the downside by saying 27 DALYs/death is a *healthy* life expectancy figure and so is "already below raw remaining life expectancy." The critique\'s claim is different. It concerns the elevated *mortality hazard* of a specific high-risk subpopulation (HIV, malnutrition, advanced disease), not population-average morbidity. A morbidity-adjusted, population-level figure does not address a subpopulation mortality hazard. The Challenger correctly caught this swap.', 'false_definitiveness: The Advocate wrote that "\'nearly cancel\' does not follow from the Quantifier\'s own numbers. The net is more likely mildly positive." This rests on labelling 535k as "the unweighted 535k," which the critique never states. The Advocate gave no support for that reading. The conclusion is delivered confidently, but it depends on an unverified assumption about which basis the figure is on.', 'sound_synthesis_noted: The consistent-basis recomputation shows its steps and is correct under its stated assumption:', 'sound_synthesis_noted (with gap): The "upside and downside are linked" argument is directionally valid, but the Advocate did not quantify it. The Challenger later quantified it as negligible.']
Challenger failures: ['whataboutism: Zero is also an estimate. The model\'s implicit value for this channel is 0%… no more empirical grounding than 5%." The Advocate never claimed zero was grounded. The claim was that zero is a *conservative, disclosed* omission. Pointing out that the model\'s zero is also ungrounded does not answer the argument that the 5% input lacks a mechanism chain.', 'sound_synthesis_noted: The constant-hazard bound is derived explicitly: remaining life scales as 1/SMR, and 1/2.9 ≈ 0.35, so up to ~65% reduction. The Challenger labels it "a ceiling, not an estimate" and lists caveats: SMR decay, the pooled versus marginal population, and the unrealistic constant hazard. This is a legitimate bound. Its only use is to show that 5–10% is not obviously conservative. It does not support any specific larger value, and the Challenger says so.', 'sound_synthesis_noted: The offset quantification is sound. A 5% reduction in a 40% share is 2% of the excess pool, so the correlation offset is negligible. This neutralizes the Advocate\'s unquantified "linked" argument. The units are loosely mixed (2% of excess hazard versus a 5–10% DALY overstatement), but the conclusion holds: the downside shrinks by roughly 2% of itself.', "sound_synthesis_noted: The basis-ambiguity recomputation is arithmetically correct. If 535k is weighted, the net is +45k − (25–55k), roughly −10k to +20k. This is a legitimate challenge to the Advocate's resolution of the ambiguity."]
Debate resolved: Several points are now settled:
- **The excess-death pool is real.** Both sides agree it exists.
- **The upside inputs are ungrounded.** The 40% respiratory share and the 5% effect are conditional hypotheses, not estimates.
- **The upside overlaps Critique 1.** It must be netted there rather than added.
- **The upside–downside correlation is negligible.**
- **The net adjustment is immaterial on either basis.** Both sides concede it falls below the 25% materiality threshold, so it cannot move the decision.
Debate unresolved: - **The sign of the net.** It depends on whether the 535k downside base is pre- or post-p_success weighting, and neither side established which.
- **The size of the downside.** It also depends on whether CG's 27 DALYs/death reflects the elevated mortality of the rescued subpopulation or only a population-level morbidity adjustment. The 5–10% overstatement remains ungrounded, bounded only loosely by the ~65% ceiling.

--- Critique: Transmission benefit is small, with a bounded calculation (~10–30k central) ---

### Advocate
DEFENSE OF CG'S POSITION: Transmission benefit is small (~10–30k DALYs central)

**Framing note.** This critique mostly agrees with CG's current treatment. CG's BOTEC values only mortality, so transmission-averted cases are an implicit zero. The critique says that channel is small, which supports leaving it out. The only live question is whether the omission understates the estimate by a decision-relevant amount (more than ~25%, or enough to move SROI materially relative to the ~2,000x bar).

**EXISTING COVERAGE:**
- CG states that "only mortality is valued." Transmission, morbidity, lung-damage and diagnostic channels are left out explicitly, not overlooked.
- Omitting a small positive channel is a conservative simplification. The critique's own logic, that this channel is minor, implies the omission costs little.
- The success probability of 40% already multiplies all benefits. The critique's "~20k after weighting" applies the same 40%, so there is no double-counting issue.
- CG does not model transmission, but a mechanism-based reason for it to be near zero is available. A lung-sparing adjunct does not shorten diagnostic delay, which the critique's own sources identify as the dominant transmission window (PMC9907102, pre-diagnosis transmission analyses). It also does not alter on-treatment infectiousness beyond the first weeks (PMC4015982, PMC12054730).

**EVIDENCE WEAKNESSES:**
- The numerical inputs are unsourced: the post-start transmission share of 1–5%, the 10–20% reduction, and 0.5 secondary cases. The critique itself labels them UNGROUNDED. The cited modelling papers support the direction (small) but not any of the specific magnitudes.
- The sputum-culture-conversion pathway is the premise for any transmission effect, and the critique concedes that ROSETTA found no conversion effect. If that pathway is absent, the transmission benefit is zero, not 20k.
- CG's "success" condition is a mortality benefit. A mortality benefit does not by itself imply faster culture conversion. The critique's channel is therefore only weakly coupled to the event that drives the 40% probability.
- The PMC sources were checked for logical fit with the argument. They were not checked for quantitative match to a statin adjunct.

**MAGNITUDE CHALLENGE:**
- I rebuilt the arithmetic: 3.3M × 0.5 × 0.003 × 10 = 49,500 DALYs pre-probability. Weighted by 40%, that is ~19,800. This matches the critique.
- The comparison base is CG's benefit of 539,500 DALYs pre-probability, or ~215,800 weighted. The critique's central figure is therefore ~9% of CG's benefit (49.5k / 539.5k). The critique's own suggested range of ~10k (weighted) is ~4.6% of weighted benefit, and 30k is ~14%.
- Only the heavy upper tail of ~150k pre-p (~60k weighted, ~28%) crosses the ~25% materiality line, and the critique itself recommends moving the central estimate down, not up.
- The 10 DALYs per secondary case looks high on CG's own parameters. CG uses ~6% mortality among treated drug-susceptible cases and 27 DALYs per death, which gives 0.06 × 27 ≈ 1.6 DALYs from on-treatment mortality per treated case. Reaching 10 requires substantial untreated cases or large post-TB morbidity, and the critique does not source either. If I use ~1.6–5 DALYs per case instead (the upper end allowing for some untreated cases and sequelae), the central weighted figure falls to ~3k–10k, i.e. ~1.5–5% of weighted benefit. This is my derivation from CG's own inputs, not an attested figure.
- Two further downward adjustments, both named in the critique, are not in the central calculation:
  - Week-8 culture conversion does not map one-to-one to infectiousness.
  - CG's constant-treated-share assumption interacts with how many secondary cases are actually averted.

**OFFSETTING FACTORS:**
- The critique treats this as a net addition. Possible offsets exist but are ungrounded. The main one is that if the statin lowers mortality, some patients survive longer. I cannot ground whether this raises or lowers transmission, and I do not rely on it.
- The more relevant offset is that any added transmission term would sit alongside other omitted terms (morbidity, post-TB lung disease) that the parameter map lists as zero. That is a matter for the Synthesizer, not for this defense.

**OVERALL ASSESSMENT:** Strong defense.
- The critique's own conclusion is that the omitted channel is small and should be revised downward, which supports CG's simplification.
- At the critique's central values, including the channel adds about 9% (pre-p basis), which is below the 25% materiality threshold.
- At the critique's recommended lower values (≤10k weighted), the addition is about 5% or less.
- The "notable" materiality label is overstated relative to the critique's own numbers.

**CONCESSIONS:**
- The inputs are ungrounded, as the critique says. My own downward adjustment of DALYs per case is a derivation from CG parameters, not an empirical finding.
- CG does not document why transmission is excluded, which is a transparency gap.
- The upper tail (~150k pre-p) would be material if realized. The critique gives no evidence that the tail is likely, and its own sources point the other way.
- The critique's own caveat stands: the channel depends on a culture-conversion effect that ROSETTA did not find.
- The "post-TB lung disease" thread label does not match the content, as the critique notes. This is a labeling issue and does not affect the substance.

### Challenger
REBUTTAL: Transmission benefit is small, with a bounded calculation (~10–30k central)

**Preliminary concession.** The critique and the Advocate largely agree on direction: the channel is small and the omission is defensible. I do not contest that. My rebuttal is limited to four points where the defense is weaker than it appears:
- the derivation of DALYs per secondary case,
- the dismissal of the upper tail,
- the materiality framing,
- the treatment of the sign of the effect.

---

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: CG's "only mortality is valued" scope explicitly zeroes transmission, and since the channel is small, the omission is a conservative simplification that costs little.

- **Explicit scope is not the same as an examined exclusion.** The Advocate concedes CG "does not document why transmission is excluded." Listing a channel as out of scope is not a finding that it is small.
- **The smallness argument comes from the critique, not from CG.** The ~9% figure (49.5k / 539.5k) exists only because the critique supplied an estimate. CG's record contains no estimate to compare against.
- **The omission is not clearly conservative.** The Advocate calls omitting a "small positive channel" conservative. That framing assumes the sign is positive.
  - If the statin reduces mortality without any culture-conversion effect (ROSETTA found none), survivors who would otherwise have died stay infectious for longer.
  - I cannot ground the magnitude of this effect and the verifier evidence package does not address it.
  - It is a conditional. If mortality falls and conversion is unchanged, the transmission term is zero or slightly negative, not a small positive. The critique's advice to widen the low end "toward zero" may therefore understate the downside.
  - This is a reason the channel is not reliably a one-sided omission.

---

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the numerical inputs are ungrounded, the PMC sources were checked only for logical fit, and the culture-conversion pathway is weakly coupled to the mortality benefit that drives the 40% success probability.

- **I concede the Advocate's points on weak coupling and ungrounded inputs.** The coupling point actually strengthens the critique's downward recommendation. If the 40% probability attaches to a mortality benefit and not to conversion, then applying 40% to the transmission term likely overstates it. Using the "~20k weighted" central figure is therefore generous, which supports moving toward ~10k or below.
- **Status of the evidence.** The verifier recorded the PMC sources as fitting the logic. It did not mark any quantity as rejected. The 1–5% post-start share and 10–20% reduction are unverified, not contradicted.
- **Symmetry of the uncertainty.**
  - The Advocate treats the ungrounded inputs as grounds to doubt the upper tail.
  - The same absence of grounding applies to the lower end.
  - The sources constrain direction only. They support "pre-diagnosis dominates" but do not bound the 1–5% figure numerically.

---

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: 10 DALYs per secondary case is too high. Using CG's ~6% treated mortality × 27 DALYs per death gives ~1.6 DALYs per case, and up to ~5 with some allowance for untreated cases and sequelae. This drops the weighted central figure to ~3–10k, or 1.5–5% of weighted benefit.

- **The derivation imports CG's mortality-only scope into the denominator.**
  - The 1.6 figure counts only on-treatment mortality among treated cases.
  - A secondary case's DALYs also include untreated or delayed-diagnosis disease, relapse, and morbidity during illness.
  - Using the same restriction that makes CG's own benefit a lower bound to deflate the transmission term is circular. It reproduces the exclusion rather than testing it.
- **The 6% mortality input is not in the verifier evidence package.** The Advocate states it as a CG parameter. I cannot confirm it, and the derivation is only as good as that number.
- **The Advocate concedes** that ~5 is an upper bound "allowing for some untreated cases and sequelae," and calls the whole range "my derivation... not an attested figure." The 10 DALYs input is also unsourced, but the Advocate's replacement range is not better grounded.
- **The 0.5 secondary-cases input is unsourced and unchallenged.** The Advocate rebuilt the arithmetic but did not test this input, even though it scales the result linearly.
- **Dismissing the tail.**
  - The Advocate says the critique "gives no evidence" that the ~150k pre-p tail is likely. The tail comes from the same unverified product of the 1–5% share and 10–20% reduction.
  - The sources point toward the low end, but only qualitatively.
  - At ~150k pre-p, the channel is ~28% of CG's benefit (150k / 539.5k), above the Advocate's own 25% line.
  - I cannot assign a probability to this tail. It is bounded by unverified inputs, not excluded by evidence.
- **Materiality threshold.** The Advocate relies on a 25% line and the "~2,000x bar." I do not know how close CG's SROI sits to that bar, and the Advocate does not say. If it is close, a 5–9% shift matters more than the Advocate implies. I cannot ground this, but it is a gap in the "below threshold" conclusion.

---

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: possible offsets (e.g., survivors living longer) are ungrounded, and other omitted terms (morbidity, post-TB lung disease) belong to the Synthesizer.

- **The Advocate does not rely on the survivor offset, and neither do I as a quantified item.** As noted above, it matters conditionally for the sign of the effect, not for the central estimate.
- **Other omitted terms are not offsets to this channel.** They are separate additions. They make the overall omission less conservative, not more.
- **No quantified offset exists in CG's model.** CG's model contains no term that nets against transmission. The ~9% figure stands unreduced by any modelled offset.

---

**KEY UNRESOLVED QUESTIONS:**
- What is the correct DALY burden per secondary case once untreated or delayed disease, relapse, and morbidity are included? The range from the Advocate's ~1.6 to the critique's 10 is unresolved.
- If the statin reduces mortality but not culture conversion, is the sign of the transmission effect zero or negative because survivors remain infectious longer?
- How close is CG's SROI to the ~2,000x bar? This determines whether a ~5–9% omission is decision-relevant.
- Are the post-start transmission share (1–5%) and the 0.5 secondary-cases input within plausible bounds? The verifier did not test either quantitatively.

### Judge Audit
Surviving strength: weak
Justification: The critique's own claim, that the channel is small and should be revised toward ~10k or below, survived intact. The Challenger explicitly conceded the direction, and the Advocate's arithmetic confirmed the figure is below materiality. As a challenge to CG's estimate, however, the critique implies at most a single-digit-percent upward adjustment, and possibly zero given the null conversion trials. The Challenger's attempts to enlarge its relevance rested on ungrounded moves: the sign conjecture, SROI proximity, and the tail "not excluded by evidence." The debate was reasonably productive, but what it established is that this channel does not matter much.
Recommended action: 1. CONCLUDE NOW: Keep transmission at zero in the BOTEC. Add a documented note covering three points:
   - The transmission benefit is a small, possibly null upside. A plausible range is 0 to about 20k DALYs weighted, or roughly 0–10% of benefit.
   - The benefit is contingent on a culture-conversion effect that ROSETTA did not find.
   - The 1–5% post-start share, the 10–20% reduction and the 0.5 secondary cases are all ungrounded inputs.

   Do not adopt the Advocate's 1.6 DALYs-per-case figure. If the term is ever modelled, use about 10–12 DALYs per case, consistent with Menzies. Confidence: moderate-high that the omission is not decision-relevant.
Action feasibility: actionable_now
Advocate failures: ['unsupported_estimate_pseudo: The Advocate argued that "0.06 × 27 ≈ 1.6 DALYs from on-treatment mortality per treated case" should replace the critique\'s 10 DALYs per secondary case. The chain has a clear logical gap. Averting a secondary case averts all of that case\'s burden, including untreated and delayed-diagnosis mortality and morbidity. Treated-case mortality alone does not measure that. The derivation also ignores the verifier\'s evidence that Menzies gives about 12.1 DALYs per incident case, which supports the critique\'s 10 rather than undermining it.', 'unsupported_estimate_fabricated: The upper value of the "~1.6–5 DALYs per case" range ("the upper end allowing for some untreated cases and sequelae") has no source or derivation. The 5 is asserted. The Advocate does concede it is "not an attested figure.', "sound_synthesis_noted: The arithmetic reconstruction is correct and properly based: 49.5k pre-p, ~19.8k weighted, ~9% of 539.5k, and ~4.6% and ~14% at the critique's 10k and 30k bounds. The tail check is also correct (~150k pre-p ≈ 28%). These figures use stated CG and critique inputs, and they are the most decision-relevant content in the debate."]
Challenger failures: ['misrepresenting_evidence_status: The Challenger wrote, "The 10 DALYs input is also unsourced." The verifier marked this input PLAUSIBLE and cited Menzies at 12.1 DALYs per incident case. The Challenger therefore missed its strongest available rebuttal to the Advocate\'s 1.6 figure and treated a supported input as ungrounded.', 'call_to_ignorance: The sign argument holds that survivors "stay infectious for longer," so the transmission term "may be zero or slightly negative." The Challenger acknowledges this is ungrounded, but still uses it to argue the critique "may therefore understate the downside." The verifier\'s evidence points the other way: patients on effective treatment become non-infectious within about two weeks, so extra treated survivors add little transmission. The conditional framing is partly acceptable, but the conclusion leans on speculation.', 'call_to_ignorance: On SROI materiality, the Challenger wrote: "If it is close, a 5–9% shift matters more… I cannot ground this." This raises an unexamined possibility as a gap without any evidence that SROI sits near the bar. The move is mild.', "sound_synthesis_noted: The Challenger's circularity point is substantive and correct. Using CG's mortality-only scope to deflate the transmission term reproduces the exclusion rather than testing it. The Challenger also correctly notes that the 0.5 input went unchallenged, and correctly distinguishes unverified inputs from contradicted ones."]
Debate resolved: Both sides agree that the transmission channel is small. At the critique's central values it equals roughly 4–14% of CG's benefit, and only the unsupported upper tail crosses a 25% materiality line. CG's omission is therefore not decision-relevant on current evidence. The Advocate's attempt to cut DALYs per case to about 1.6 did not survive scrutiny, and the verifier's Menzies figure supports keeping roughly 10.
Debate unresolved: The premise for any transmission effect remains contested: ROSETTA and the rosuvastatin trial found no conversion effect, while an atorvastatin phase IIA trial found reduced bacillary load. Neither side resolved this, and it determines whether the channel is about 0 or about 10–20k. How close CG's SROI sits to the ~2,000x bar was raised but not answered.

--- Critique: The "lung benefit without mortality benefit" scenario is structurally less valuable than a simple p_success weighting implies ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: The "lung benefit without mortality benefit" scenario is structurally less valuable than a simple p_success weighting implies
```

**EXISTING COVERAGE:**
- CG's formula values only mortality. The BOTEC says "only mortality is valued", and the chest X-ray lung-damage finding never enters the calculation. A lung-only branch therefore adds zero to the published ~3,000x.
- The critique's own conclusion is that the lung channel is worth about 1× its p_success-weighted value, not 2×. That conclusion supports CG's choice not to add a lung term. Any lung channel would be a small positive add-on, so omitting it is conservative.
- The Phase IIc trial is explicitly designed to test "survival, infection clearance and lung damage." CG's 40% is attached to a benefit stream valued entirely through the mortality reduction. This is a reasonable reading: success means the endpoint that drives the valued benefit.
- The critique describes itself as a "correction to how Critiques 1–3 are weighted, not a separate value term." It does not identify an error in any CEA parameter.

**EVIDENCE WEAKNESSES:**
- The only cited study is the Phase 2 RCT of CC-11050 and everolimus on FEV1 recovery. Those are different drugs from atorvastatin. The study supports only that lung function is a recognized preliminary-efficacy outcome, and the critique concedes it says nothing about WHO adoption.
- The critique reports no evidence on how WHO guideline groups weigh lung-function surrogates.
- Two inputs are ungrounded by the critique's own admission: P(lung holds | mortality fails) = 0.3–0.5, and conditional adoption of 10–20%. I cannot ground either, and I treat both as uninformed priors.
- The "~2×" upper bound is loosely stated. Taking the critique's own formula with full adoption, 0.4 + 0.6 × (0.3–0.5) gives 0.58–0.70. That is 1.45–1.75× the 0.4 base, or about 1.3–1.55× the 0.45 figure, not 2×.

**MAGNITUDE CHALLENGE:**
- Using the critique's own inputs, the lung-only branch adds 0.6 × (0.3–0.5) × (0.1–0.2) = 0.018–0.06 to the 0.4 base. That is a 4.5–15% relative change in probability weight.
- Even at the top of that range, the change is below the ~25% materiality threshold. It also applies to a branch whose per-success value is not specified, and that value is plausibly lower than the mortality value.
- The critique labels the direction "neutral to slightly decreases," and the materiality "notable" sits in tension with a magnitude it calls small. Nothing here moves the SROI materially toward or below 2,000x.

**OFFSETTING FACTORS:**
- Lung benefit and mortality benefit are likely positively correlated, since lung damage is a plausible pathway to death. This makes the "lung holds, mortality fails" branch smaller than a naive independent weighting suggests. That is a further reason the branch is minor.
- The parameter map notes that morbidity and long-term survival channels are implicit zeros. Those omissions raise the true value and partly offset any downward pressure from a surrogate-only success.

**OVERALL ASSESSMENT:** Strong defense.
- The critique is a self-limited weighting caveat. It does not show that CG's formula is wrong, and its own arithmetic implies a small effect.
- The residual issue is a definitional one about what "success" means, which I concede below.

**CONCESSIONS:**
- CG does not define "success." If the 40% implicitly includes lung-only or surrogate-only passes, it overstates the probability of the mortality benefit that the formula actually values. This is a genuine ambiguity.
- A lung-only result is likely to earn a lower adoption probability than the main case. The critique is right about the direction, though I cannot ground the size.
- Nothing in the cited evidence tells us how guideline groups treat FEV1 or X-ray surrogates. That gap cuts both ways and is not resolved by CG's text.
- The size of the effect is unquantified and depends on ungrounded inputs. I defend it only as small under the critique's own assumptions.

### Challenger
REBUTTAL: The "lung benefit without mortality benefit" scenario is structurally less valuable than a simple p_success weighting implies

**Overall position.** The critique is self-limited, and the Advocate's arithmetic corrections are mostly right. My rebuttal therefore concentrates on the one place where the defense is incomplete: what CG's 40% means. I concede the rest.

---

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: CG values only mortality, so a lung-only branch adds zero to the ~3,000x. Omitting a lung term is therefore conservative.

Response:
1. The conclusion that adding no lung value is conservative is correct, and I concede it.
2. It answers a different question from the one the critique raises, which is what the 40% is a probability of.
   - If "success" means "mortality benefit shown and adopted," omitting lung value is conservative.
   - If "success" is looser, so that the 40% includes surrogate-only passes (lung damage on X-ray, infection clearance), the formula multiplies a probability that includes lung-only passes by a value that counts only mortality. That is anti-conservative.
   - The Advocate cannot call the model conservative on both readings.
3. The Advocate concedes CG never defines "success." The claim that "success means the endpoint that drives the valued benefit" is therefore an inference, not something in CG's text.
4. The trial is designed to test "survival, infection clearance and lung damage." That is three outcomes, and "success" on any one of them is a natural reading of the 40%.
5. The Advocate also notes that the critique "does not identify an error in any CEA parameter." That is true, but the ambiguity sits inside p_success itself. A parameter can be numerically unchanged and still be misdefined.

---

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the only cited study concerns different drugs, nothing is known about WHO weighting, and the two key inputs are ungrounded.

Response:
1. I concede all three points. The CC-11050/everolimus RCT supports only the claim that FEV1 is a recognized preliminary-efficacy outcome and a mortality predictor. It does not support any adoption probability.
2. The verifier did not find evidence that WHO groups discount lung surrogates. It also did not find evidence that they credit them. This is an absence of evidence, not a rejection, so the Advocate's "cuts both ways" is correct. The direction (lung-only earns lower adoption) therefore rests on the Advocate's concession and on reasoning, not on a sourced finding.
3. I concede the Advocate's arithmetic correction.
   - At full adoption, 0.4 + 0.6 × (0.3–0.5) gives 0.58–0.70, which is 1.45–1.75× the 0.4 base.
   - So the "~2×" in the critique was loose.

---

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: the lung-only branch adds 0.018–0.06, a 4.5–15% change, below the ~25% materiality threshold, and the critique's "notable" label contradicts its "small" magnitude.

Response:
1. The Advocate's arithmetic is correct: 0.6 × (0.3–0.5) × (0.1–0.2) = 0.018–0.06.
2. I concede the internal tension between "notable" and "small." The critique's own text supports "small."
3. The relevant magnitude is the exposure on CG's side, not this branch's weight.
   - If CG's 40% includes lung-only passes at the critique's own upper-bound weight of 0.06, the mortality-valued probability falls from 0.40 to about 0.34, a 15% reduction.
   - This is the critique's upper bound reused, not an independent estimate.
   - It is still below the Advocate's 25% threshold, and I cannot ground that threshold either way.
4. At the low end (0.018), the change is under 5%, which is negligible. The residual is small, and I do not claim otherwise.

---

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: (a) lung and mortality benefits are positively correlated, so the lung-only branch is smaller than an independent weighting implies; (b) implicit zeros for morbidity and long-term survival raise true value.

Response:
1. **(a) Correlation double-counts.**
   - The critique's inputs are already conditional: P(lung holds | mortality fails) = 0.3–0.5.
   - A conditional probability already embeds any correlation, so invoking correlation as a further reason the branch is small counts it twice.
   - The Advocate's own concession, that FEV1 predicts all-cause mortality, also cuts the other way. It supports P(lung holds | mortality fails) being non-trivial.
   - A Phase IIc trial may be underpowered for mortality, which would weaken the correlation. I cannot ground trial power, so this is conditional reasoning only.
2. **(b) The implicit zeros are a different channel.**
   - They raise value in other parameters. They do not fix the possible overstatement of the mortality-valued probability.
   - They offset the net result in direction only. The Advocate has not quantified them, and nothing links them to the lung-only branch.

---

**KEY UNRESOLVED QUESTIONS:**
- Does CG's 40% denote P(mortality benefit shown and adopted), or P(any prespecified trial success)? CG's text does not say.
- What is the Phase IIc trial's registered primary endpoint? The critique's conditional ("if not lung function") has not been checked.
- How do WHO guideline groups treat surrogate-only results for adjunctive TB therapy? The verifier found no evidence, so this is unverifiable, not rejected.
- Is the 10–20% conditional adoption defensible? It is ungrounded on both sides.
- Is a Phase IIc trial powered to detect mortality? That determines whether "lung holds, mortality fails" is a real branch or mostly an underpowering artifact.

### Judge Audit
Surviving strength: weak
Justification: - The Challenger openly conceded nearly every point against the critique as written: the arithmetic, the ungrounded 10–20% adoption input, the ungrounded 0.3–0.5 conditional probability, the "notable vs. small" tension, and the evidence weakness. Its only substantive gain was a reframed definitional concern.
- The Advocate's "immaterial" conclusion rests on a fabricated 25% threshold and a double-counted correlation argument. So the critique's smallness is established by its own arithmetic, not by a rigorous defense.
- The Challenger's one quantitative exposure estimate (0.40 → 0.34) was a pseudo-derivation.
- What survives is a small, ungrounded caveat plus a separate definitional ambiguity that neither side resolved with evidence.
Recommended action: 1. CONCLUDE NOW: The critique's quantitative claim does not survive as a material adjustment, and I hold this with moderate-to-high confidence. Under its own inputs, the lung-only branch shifts probability weight by at most +0.02–0.06, which supports leaving the ~0.45 figure unchanged and adding no lung value term. The critique should be recorded as a structural caveat with a corrected direction ("corrects a naive weighting toward ~1×; negligible versus the 0.4 base").

   The separate definitional issue the Challenger raised should be logged as its own item. It can be settled cheaply by looking up the Phase IIc atorvastatin TB trial's registered primary endpoint (e.g., ClinicalTrials.gov or ISRCTN) and checking whether CG's 40% is tied to it. This is feasible with existing tooling and does not require further debate.
Action feasibility: actionable_now
Advocate failures: ['unsupported_estimate_fabricated: Even at the top of that range, the change is below the ~25% materiality threshold." The 25% threshold has no source or derivation, yet it carries the conclusion that the effect is immaterial. The Challenger noted that it "cannot ground that threshold either way.', 'false_definitiveness: Nothing here moves the SROI materially toward or below 2,000x." The 2,000x benchmark appears without explanation. No calculation links a 4.5–15% probability shift to the SROI, and the ~3,000x figure leaves only a one-third margin to 2,000x. The Advocate states the claim as settled but never shows it.', 'unsupported_estimate_pseudo: Lung benefit and mortality benefit are likely positively correlated… This makes the \'lung holds, mortality fails\' branch smaller than a naive independent weighting suggests." The critique\'s input is already conditional (P(lung holds | mortality fails)). Citing correlation as a further reduction double-counts it, so the reasoning has a clear logical gap. The Challenger correctly identified this.', 'whataboutism: Morbidity and long-term survival channels are implicit zeros… Those omissions raise the true value and partly offset any downward pressure." This points to separate, unquantified omissions in other channels. It does not address whether p_success is correctly defined.', 'false_definitiveness: The Advocate self-rates "Strong defense" while conceding that "CG does not define \'success\'… This is a genuine ambiguity." It also concedes that if the 40% includes surrogate-only passes, it overstates the valued probability. That concession is the central vulnerability, and it is inconsistent with a "strong" rating. My assessment is that the defense was partial.', 'sound_synthesis_noted: The arithmetic is correct and taken from the verifier package. The lung-only add-on is 0.6 × (0.3–0.5) × (0.1–0.2) = 0.018–0.06. The naive bound is 0.58–0.70, which is 1.45–1.75× the base, not "~2×." Each step is shown and sound.']
Challenger failures: ["unsupported_estimate_pseudo: If CG's 40% includes lung-only passes at the critique's own upper-bound weight of 0.06, the mortality-valued probability falls from 0.40 to about 0.34.", 'sound_synthesis_noted: The correlation double-counting rebuttal is correct and well reasoned. A conditional probability already embeds dependence. The Challenger also correctly separated the implicit-zero channels from the p_success definition issue, and correctly treated the WHO-weighting gap as UNVERIFIABLE rather than REJECTED.']
Debate resolved: Both sides agree on the critique's arithmetic:
- The lung-only branch adds 0.018–0.06, a 4.5–15% relative change.
- The "~2×" naive bound is actually 1.45–1.75×.
- The direction is a correction toward ~1×, and the magnitude is small.

As written, the critique is a self-limiting caveat that identifies no error in any CEA parameter. The original critique also mislabeled 0.6 as "uptake" and stated the direction confusingly.
Debate unresolved: The exchange surfaced a different question that is genuinely open. Does CG's 40% denote P(mortality benefit shown) or P(any prespecified trial success, including lung-damage or infection-clearance endpoints)? If it is the latter, the model is mildly anti-conservative, and the size of that exposure was not validly estimated by either side.

--- Critique: The sweat-based diagnostic carries real option value but is speculative (~10–30k central) ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION: The sweat-based diagnostic carries real option value but is speculative (~10-30k central)

**EXISTING COVERAGE:**
- CG's BOTEC values only statin mortality benefits. The parameter map confirms "only mortality is valued," and the sweat diagnostic is mentioned as context but enters the formula nowhere.
- This is a conservative simplification, not an oversight. Valuing a diagnostic workstream with a ~5% adoption chance would require a separate probability tree, and the BOTEC's stated purpose is a quick estimate on the main value driver.
- The critique's own hypothesis concedes the direction is "uncertain" and "leans neutral-to-negative." If the diagnostic's true value is near zero, as the critique's own WHO evidence suggests, CG's zero is approximately correct.

**EVIDENCE WEAKNESSES:**
- The critique labels P(adoption) ≈ 5% and the 1-3% incremental detection share as UNGROUNDED. They are placeholders, not findings.
- The 10-30k discount from the raw 50k is unexplained. The critique says it allows for "delay" and "counterfactual displacement" but shows no derivation.
- The only cited evidence points against the critique's own positive-value case:
  - WHO's early-2026 tongue-swab and NPOC-NAAT recommendations.
  - The May 2026 WHO/Stop TB toolkit.
  - About 100 products in the pipeline as of August 2025.
  - All of these lower the incremental value of a new non-sputum test.
- The mechanism may also overstate incremental detection. The 2.4M non-notified cases are only partly a test-performance problem. Reasoning, not an attested fact: many are missed because of access, health-seeking and linkage barriers, which a better sample type does not fix. The 1-3% share does not account for this, and it is not shown to hold.
- The critique does not establish which specific sweat-test product CG funds, its performance, or its stage. A figure built on "typical early-stage-diagnostic base rates" cannot be tied to this project.

**MAGNITUDE CHALLENGE:**
- Here is the effect of the central range on SROI, using CG's numbers:
  - 10-30k DALYs × $OP 100,000 = $OP 1-3 billion.
  - Dividing by the $7M all-in cost gives about +143x to +429x.
  - Against the ~3,086x baseline (54B × 0.4 / 7M), that is about +4.6% to +14%.
  - This is below CG's ~25% materiality threshold and nowhere near changing the bar-clearing conclusion, since the estimate is already above 2,000x.
- The central range is also generous, because it treats the full diagnostic benefit as attributable to this grant.
  - The grant funds one workstream, and the critique's calculation applies no attribution share for a diagnostic with many other developers (about 100 products in the pipeline).
  - I cannot ground a specific attribution share. The point is that the critique applies none, so its range is, if anything, an upper-leaning figure.
- Only the critique's tail (100k DALYs, i.e. $OP 10B ÷ $7M ≈ +1,430x, or about +46%) would be material. That tail sits at the top of an explicitly ungrounded range and would require the 5% adoption probability and the 1-3% detection share both to be right or low. The critique itself places it at the extreme (range "0 to ~100k").
- The timing is also unclear. The statin's 539,500 DALYs is a one-year-speedup benefit. The critique's diagnostic figure is "per year" with no stated speedup or duration, so it cannot be added on a like-for-like basis. This is unresolved, not a clean upward correction.

**OFFSETTING FACTORS:**
- Cost side. The critique raises a consistency point: if the $7M includes diagnostic funding while diagnostic benefits are zero, the estimate is biased downward.
  - The parameter map says it is unclear whether the diagnostic workstream sits inside the $7M.
  - The $7M is described as covering "later Phase III trials, guideline changes, dissemination and validation," which reads as statin-specific. On that reading the exclusion is internally consistent.
  - If the diagnostic is included, the bias could favour the critique. But I cannot ground the diagnostic's cost share, so I cannot size the offset. This remains open.
- Negative adjustments omitted from a diagnostic valuation:
  - Crowding from tongue-swab and NPOC (the critique's own evidence).
  - The probability that the product fails.
  - Dependence on linkage to care.
  - Attribution to this grant's share of a many-developer field.
- These are all downward pressures, and they are absent from the 10-30k figure.

**OVERALL ASSESSMENT:** Strong defense.
- The critique's central estimate would move SROI by roughly +5% to +14%, below the materiality threshold.
- Its inputs are acknowledged as ungrounded.
- Its only grounded evidence (2026 WHO recommendations) argues for lower value.
- The cost-inclusion question is the one genuine unresolved issue.

**CONCESSIONS:**
- CG assigns exactly zero to a workstream it chose to fund. Zero is not a literal expected value, so the estimate is slightly conservative on this dimension.
- The cost-boundary ambiguity is real: if diagnostic costs are in the $7M, the treatment is asymmetric and biased against the grant. CG should state which applies.
- The tail case (~100k DALYs) would be material (+~46%). I cannot rule it out with grounded evidence. I can only say it is unsupported.
- Because the critique's net direction is "neutral-to-negative," the main practical recommendation is documentation, not a numerical change.

### Challenger
REBUTTAL: The sweat-based diagnostic carries real option value but is speculative (~10-30k central)

**Preliminary concession.** The critique's own inputs (5% adoption, 1-3% incremental share, the 50k→10-30k discount) are labelled UNGROUNDED. The only verified evidence (WHO 2026 tongue-swab/NPOC-NAAT recommendations, the May 2026 toolkit, ~100 pipeline products) points toward lower value. I do not defend the 10-30k figure as an estimate. My rebuttal targets where the Advocate's defense overreaches or leaves residual issues.

---

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: CG's zero is a deliberate, conservative simplification. Since the critique concedes the net direction is neutral-to-negative, zero is approximately correct.

- **The Advocate's inference does not follow.**
  - The critique says "uncertain, leaning neutral-to-negative." That is a claim about direction under crowding, not a claim that the expected value is zero.
  - The WHO evidence lowers the *incremental* value of a new non-sputum test. It does not establish that the value is nil.
  - The Advocate concedes elsewhere that "zero is not a literal expected value."
- **The two statements are inconsistent.** The Advocate says zero is "approximately correct" and also that the estimate is "slightly conservative." The Advocate cannot ground which is true, because no probability tree exists.
- **Residual gap:** CG treats a workstream it chose to fund as having exactly zero benefit. That is a documentation gap even if the numerical effect is small.

---

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the 10-30k discount is unexplained, and the critique's inputs are placeholders.

- **Conceded.** The raw calculation is 0.05 × 200k × 5 = 50k. The step to 10-30k is a judgment discount with no shown derivation, so it is a ~40-80% haircut on an ungrounded base. I cannot rebuild it from the evidence package.

> The Advocate claims: the 2.4M non-notified cases are partly an access and linkage problem, so a better sample type does not fix them. This is flagged as reasoning, not attested fact.

- **This cuts both ways, and I cannot ground either direction.**
  - The Advocate's argument is plausible.
  - A non-invasive sweat sample could also lower access barriers, for example through community or non-clinic collection. That would raise the incremental share.
  - Neither direction is in the verifier's evidence. This is UNVERIFIABLE, not rejected, so it is an open parameter and not a reason to discount the 1-3% share.

> The Advocate claims: the critique does not identify the specific sweat product, its performance or its stage.

- **Fair.** The verifier package does not establish these either. This supports the critique's own "UNGROUNDED" label, but it equally means nobody can say the true value is lower than 10-30k.

---

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: 10-30k DALYs × $OP 100,000 ÷ $7M gives +143x to +429x. Against a ~3,086x baseline, that is +4.6% to +14%, below materiality.

- **The arithmetic checks out.** 1B/7M ≈ 143, 3B/7M ≈ 429, and 54B × 0.4/7M ≈ 3,086.
- **The "~25% materiality threshold" does not appear in the verifier evidence package.** If it is CG's actual convention, the conclusion holds. If not, the "below threshold" framing rests on an unsourced benchmark.
- **The Advocate conceded two points that matter:**
  - The ~100k tail would be roughly +46%, and cannot be ruled out with grounded evidence.
  - The units are not like-for-like. The statin's 539,500 DALYs is a one-year-speedup benefit, while the diagnostic figure is "per year" with no duration. If the diagnostic benefit persists across multiple years, the SROI contribution is larger than the Advocate's single-year comparison. The Advocate called this "unresolved," and it is an upward uncertainty the Advocate's headline percentages ignore.
- **The Advocate's "no attribution share applied" point is partly double-counted.** The critique already applies a "counterfactual displacement" discount, which is functionally an attribution adjustment. The Advocate's claim that the range is "upper-leaning" because it has no attribution share is therefore overstated. The critique did not apply a *separate* share for the grant's portion of the field, so some residual overstatement remains.
- **Minimum defensible impact:** about 0 (the critique's own range floor). At the central range, the effect is +5% to +14% on the Advocate's arithmetic. This is a small effect and the critique should not be treated as moving the bottom line.

---

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: crowding, product failure, linkage dependence and attribution are all downward pressures that are absent from the 10-30k figure.

- **Two of these are already in the critique's mechanism.**
  - *Crowding.* The critique's incremental share is defined as cases detected "beyond what alternative tests would detect (e.g., tongue-swab PCR)." That is crowding by construction.
  - *Product failure.* The 5% P(reaches adoption) is a failure and attrition probability.
  - The Advocate's claim that these are "absent" is incorrect as stated.
- **Linkage to care is partly present.** The "DALYs per treated case" input assumes treatment. Whether linkage is already priced in is unclear.
- **Attribution is only partly present,** via the displacement discount as noted above.
- **Cost boundary (the one open item).**
  - The Advocate reads the $7M ("later Phase III trials, guideline changes, dissemination and validation") as statin-specific. That is a reading of the description, not a verified fact. The parameter map itself says it is unclear.
  - If the diagnostic is inside the $7M, there is a clean asymmetry: costs counted, benefits zero. That bias favors the critique.
  - The Advocate says the offset cannot be sized. That is correct, but it also means the Advocate's claim that exclusion is "internally consistent" is unverified.

---

**KEY UNRESOLVED QUESTIONS:**

- Does the $7M all-in cost include any diagnostic funding? This is the one question that could turn the issue from "documentation" into "asymmetric bias."
- Is the diagnostic benefit a one-year or multi-year flow? The answer changes the SROI contribution by a multiple.
- What is the real incremental detection share, given that a sweat sample could either help or fail to help with access barriers? Neither side can ground this.
- Does CG's ~25% materiality threshold actually govern this analysis, or is it the Advocate's frame?

### Judge Audit
Surviving strength: weak
Justification: The Challenger explicitly abandoned the critique's quantitative claim ("I do not defend the 10-30k figure as an estimate"), and the Advocate's SROI arithmetic, which the Challenger verified, shows the central range is small. The Challenger's main remaining upward arguments rest on call-to-ignorance moves:
- Multi-year persistence.
- The claim that "nobody can say the true value is lower."
- Treating the 1–3% share as neutral despite the verifier calling it "possibly generous."
What survives is a documentation point and an unverified cost-boundary question, not a material valuation error.
Recommended action: 1. CONCLUDE NOW: The critique does not support a numerical adjustment to CG's estimate (moderate-high confidence). The 10–30k option value is ungrounded, the verified evidence lowers it, and even at face value it moves SROI by roughly +5–14%. CG should take two documentation steps:
   - State explicitly that the sweat diagnostic is assigned zero benefit as a conservative simplification.
   - Confirm from the grant documents whether any diagnostic funding sits inside the $7M. If it does, either remove those costs from the denominator or note the asymmetry.

   The cost check is a simple document lookup, not open-ended research. If diagnostic funding is included, the correction runs in the grant's favour and is likely small.
Action feasibility: actionable_now
Advocate failures: ['unsupported_estimate_fabricated: This is below CG\'s ~25% materiality threshold." The verifier package contains no 25% threshold, and the Advocate gives no source. The "not material" conclusion depends on this benchmark. The Challenger correctly flagged it.', 'strawmanning: The Advocate lists "Crowding from tongue-swab and NPOC" and "The probability that the product fails" as downward adjustments "absent from the 10-30k figure." Both are already in the critique\'s mechanism:', 'false_definitiveness: If the diagnostic\'s true value is near zero, as the critique\'s own WHO evidence suggests, CG\'s zero is approximately correct." The WHO evidence lowers incremental value; it does not establish near-zero value. The Advocate later concedes "Zero is not a literal expected value… slightly conservative." Asserting near-correctness and conceding bias in the same defense is an equivocal position stated confidently.', 'sound_synthesis_noted: The magnitude calculation is a sound synthesis, and the Challenger verified the arithmetic.', 'sound_synthesis_noted: The access/linkage argument (the 2.4M gap is partly not a sample-type problem) is explicitly labelled "Reasoning, not an attested fact." That is appropriate handling of an unverified claim.']
Challenger failures: ['call_to_ignorance: This supports the critique\'s own \'UNGROUNDED\' label, but it equally means nobody can say the true value is lower than 10-30k." The absence of product-specific data does not lend support to an ungrounded figure. The uncertainty is not symmetric when the only grounded evidence (WHO 2026) points downward.', 'misrepresenting_evidence_status: On incremental share, the Challenger says "Neither direction is in the verifier\'s evidence… not a reason to discount the 1-3% share." This is inaccurate. The verifier reported that tongue-swab tests meet WHO near-POC accuracy targets for exactly the population concerned. The verifier explicitly said the 1–3% share is "possibly generous." The verifier evidence leans in one direction, and the Challenger treated it as neutral. Treating the ungrounded 1–3% as the default anchor compounds the error.', 'call_to_ignorance: The units point: "If the diagnostic benefit persists across multiple years… The answer changes the SROI contribution by a multiple." No evidence was offered for multi-year persistence. The upward possibility is raised only because duration is unknown, and the crowding-driven speedup counterargument is not addressed.', 'sound_synthesis_noted: The Challenger made two correct points:']
Debate resolved: Both sides agree on three points:
- The 10–30k central estimate is ungrounded.
- The only verified evidence (the WHO 2026 tongue-swab/NPOC recommendations and pipeline crowding) pushes incremental value down.
- At the central range, the effect on CG's SROI is about +5% to +14% and does not change the bar-clearing conclusion.

The debate also established that crowding and failure probability are already inside the critique's mechanism. They are not additional offsets.
Debate unresolved: Two questions remain open:
- Whether the $7M all-in cost includes diagnostic workstream funding. This would create a costs-counted, benefits-zero asymmetry.
- Whether the diagnostic benefit should be treated as a short counterfactual speedup or a multi-year flow.

The source and applicability of the ~25% materiality threshold were also left unverified.

--- Critique: 60% steady-state uptake has no precedent among comparable TB program additions ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION: 60% steady-state uptake has no precedent among comparable TB program additions

**EXISTING COVERAGE:**
- The BOTEC does not apply 60% as an uptake level at a fixed date. It applies it as the share of adult patients who "would add atorvastatin if it works", justified by the drug being "generic and cheap". That is a long-run ceiling conditional on success.
- Two other parts of the chain already discount this ceiling:
  - The 40% probability that Phase II and III both succeed multiplies the whole benefit stream.
  - The 1-year speedup credits only the first year of the shift, so the model never counts decades of uptake that could be at different levels.
- The Quantifier's own mechanism note says the ramp "matters little" for a one-year speedup over an infinite horizon. This means CG's omission of an explicit ramp is not a material flaw. The only live issue is the ceiling.
- I concede the report states no empirical derivation of 60%. The parameter map says so explicitly.

**EVIDENCE WEAKNESSES:**
- **The analogs are weak.**
  - The critique's "strongest verified analogs" are WRD (a rapid molecular diagnostic) and 4HPMZ (a regimen replacement). The critique itself says neither is a clean analog for a cheap generic adjunct.
  - WRD needs platforms, cartridges, lab or near-point-of-care infrastructure, and sample logistics. 4HPMZ needs procurement of newer drug combinations, plus tolerability and supply management.
  - Atorvastatin is an oral generic added to an existing regimen. It needs neither new infrastructure nor a new supply chain. The barriers that held back both analogs are largely absent, so their uptake is more plausibly a floor than a ceiling.
- **WRD's 54% is not a ceiling.**
  - The verified figure is 54% global coverage after ~14 years, a point-in-time measure on a still-rising curve.
  - Within the evidence package, coverage in 24 African countries rose from 37% (2018) to 58% (2023). That is (58−37)/5 ≈ 4.2 pp per year, with no sign of saturation.
  - At that rate, the critique's own ramp benchmark would reach 60% in under a year from the 2023 level. A measure that was still climbing past 58% in a subset of high-burden countries does not support a ceiling of 30–40%.
- **The WHO quote cuts the other way.**
  - The GDG language that uptake would grow "in future as uptake of this regimen improves" is evidence of expected gradual growth.
  - It says nothing about where growth stops. It is evidence about the ramp, which the critique agrees matters little.
- **The "no precedent" title overstates the critique.**
  - The critique's own hypothesis says 60% is "a plausible optimistic or upper-central case, not an impossible one".
  - It also says "the evidence supports the ceiling being uncertain rather than demonstrably too high".
  - The Verifier found no adjunct-specific adoption data, and the dexamethasone and pyridoxine examples are unverified and should be dropped. So the critique has no direct evidence for the 0.30–0.40 range. That range is a judgment, not a measured quantity.

**MAGNITUDE CHALLENGE:**
- **The range is not anchored.** The 0.30–0.40 range has no derivation from the evidence cited. Neither analog yields 30–40% as a long-run ceiling.
  - WRD is at 54–58% and rising.
  - 4HPMZ has no verified quantitative ceiling in the evidence package.
- **Only part of the range matters.**
  - From the sensitivity output, the baseline is 3,055x. At 0.30 the result is 1,527x (−50%), and at 0.40 it is about 2,037x (−33%).
  - The materiality line is 0.39, where SROI ≈ 3,055 × (0.39/0.60) ≈ 1,986x.
  - So only the bottom sliver of the critique's range clears the bar. At 0.40 SROI sits right at the 2,000x bar, not clearly below it.
- **The sensitivity is two-sided.** The high case is +25% at 0.75, so uncertainty in the ceiling is not a one-way risk. The critique's own judgment is that 60% is "upper-central", not clearly above the central estimate.
- **Why 60% rather than ~100% is itself discounting.** The 60% already leaves 40% of adults not taking the drug. That implicitly covers contraindications, clinician non-adoption, private-sector gaps, and patients lost before treatment.

**OFFSETTING FACTORS:**
- **Value omitted by the model.** The BOTEC states "only mortality is valued". It gives zero credit for morbidity (reduced lung damage on chest X-ray), post-treatment survival, transmission, and diagnostic value. If uptake were lowered, these omitted channels still offset some of the loss. I do not claim they fully offset it.
- **Adopter composition.** A cheap, safe-seeming generic is plausibly adopted more readily in high-burden settings where mortality is concentrated. That could make the effective uptake among deaths averted higher than the average across all patients. I cannot ground this with a specific source. Treat it as an uninformed prior.
- **Constant treated share.** The BOTEC holds treatment coverage constant and does not assume improved case-finding. This is neutral to slightly conservative.

**OVERALL ASSESSMENT:** Partial defense.
- The critique correctly says 60% has no direct empirical support, but it provides no evidence that the true ceiling is below 0.39.
- Its analogs are structurally harder-to-adopt interventions, and WRD is mid-ramp, not at a ceiling.
- The ramp point is irrelevant for a one-year speedup.
- Even so, 60% is an unsupported assumption entering the formula linearly. A fair summary is that the parameter is uncertain, not that it is wrong.

**CONCESSIONS:**
- CG offers no empirical precedent for 60%, and I cannot supply a verified adjunct-specific benchmark.
- The linear sensitivity is real: a ceiling below ~0.39 would put SROI under the bar.
- "Uptake" in the BOTEC conflates prescribing with adherence. The parameter map notes that adherence, monitoring requirements, and rifampicin-reduced statin exposure are not modeled. These could lower effective uptake even if prescribing reaches 60%.
- The ramp matters when discounting and a finite horizon are introduced (Thread 3). The defense that ramp shape is negligible holds only under the BOTEC's current undiscounted, infinite-horizon structure.

### Challenger
REBUTTAL: 60% steady-state uptake has no precedent among comparable TB program additions

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the 60% is a long-run ceiling conditional on success, and it is already discounted by the 40% Phase II/III success probability and by the one-year-speedup structure.

- **The 40% success probability does not discount the uptake ceiling.**
  - It multiplies the whole benefit stream and is independent of adult_uptake.
  - A factor that multiplies by 0.4 leaves the 60%-versus-35% question exactly where it was.
  - The sensitivity run confirms this: halving uptake halves SROI regardless of the success probability.
- **The one-year speedup does not reduce exposure to the ceiling. It is the reason the ceiling enters linearly.**
  - The Advocate's own point is that benefit ≈ ceiling × one year of cases.
  - That makes the ceiling the single most leveraged adoption parameter.
  - The Advocate cites this structure as protection when it is actually the transmission mechanism.
- **The claim that "the 40% not taking the drug implicitly covers contraindications, non-adoption, and private-sector gaps" is a post-hoc reading.**
  - The BOTEC's stated justification is "generic and cheap". The Advocate concedes no derivation exists.
  - A reading that attributes a hidden haircut to an undocumented number cannot be verified.
- **The Advocate's concession on prescribing versus adherence undercuts the "ceiling conditional on success" framing.**
  - If 60% means prescribing, effective uptake is 0.60 × adherence × other unmodeled factors.
  - The materiality line of 0.39 is reached when that combined multiplier is 0.39/0.60 = 0.65.
  - I cannot ground a specific adherence figure for statins co-administered with rifampicin-based TB therapy. I note only that the parameter map, per the Advocate, lists adherence, monitoring requirements, and rifampicin-reduced statin exposure as unmodeled.
  - Those are three separate effective-uptake haircuts. Together they need only a 35% combined shortfall to cross the bar.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the analogs (WRD, 4HPMZ) face infrastructure and supply barriers that atorvastatin lacks, so their uptake is "more plausibly a floor than a ceiling".

- **The "floor" claim is asserted with no evidence.**
  - The Advocate cites no cheap generic adjunct and no adoption figure for one.
  - The Verifier found no adjunct-specific adoption data. That is an UNVERIFIABLE status, not a REJECTED one, and it cuts both ways.
  - The Advocate's inference that "no infrastructure means higher uptake" is as unsupported as the critique's inference that it means lower.
- **The Advocate treats supply and infrastructure as the only barriers. Atorvastatin faces others.**
  - It would need guideline inclusion, national program adoption, and clinician willingness to add a non-TB drug to a regimen.
  - The Advocate concedes monitoring requirements and the rifampicin interaction are unmodeled, which are clinical barriers to adoption.
  - I cannot ground whether national TB programs would stock statins through the TB supply channel. I flag that as an uninformed prior, not a finding.
- **"No sign of saturation" is not supported by two data points.**
  - The verified evidence is two endpoints, 37% (2018) and 58% (2023), in 24 African countries.
  - Two points cannot show the absence of a plateau.
  - The Advocate's extrapolation to "60% in under a year" is a straight line through two points: (60−58)/4.2 ≈ 0.5 years. It ignores that late-stage coverage typically slows.
  - That slowdown is a general feature of S-curves, not a verified WRD finding, so treat it as a prior.
- **The WRD data support a different point than the Advocate draws.**
  - The critique's verified global figure is 54% after ~14 years. A ceiling of 60% is therefore not conservative even for an intervention with large donor and WHO backing.
  - The 24-country subset is not the global figure. The subset's 58% is higher than the global 54%, so the subset is already the better-performing group.
- **I concede the WHO quote speaks to ramp, not ceiling.** It shows WHO anticipated gradual growth for 4HPMZ and does not bear on where growth stops.
- **I concede the title "no precedent" overstates the critique.** The critique itself calls 60% "plausible optimistic or upper-central". The remaining dispute is where in the distribution 60% sits.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: the 0.30–0.40 range is unanchored, only its lowest sliver crosses the 0.39 line, and the sensitivity is two-sided (+25% at 0.75).

- **I concede that 0.40 does not cross the bar.**
  - 3,055 × (0.40/0.60) ≈ 2,037, which sits just above 2,000.
  - Crossing requires ≤0.39, where SROI ≈ 1,986.
  - The critique's range straddles the line rather than sitting wholly beneath it.
- **I concede the 0.30–0.40 range is a judgment, not a derived figure.** Neither WRD nor 4HPMZ yields it.
- **The Advocate's two-sided argument is weaker than it looks.**
  - The upside is bounded at 100%, which gives +67% (1.0/0.6), not +25%.
  - The downside to 0.30 is −50%.
  - The distribution is wide in both directions, and the central question is where its mean lies.
  - The Advocate's "upper-central" reading of the critique is itself an argument that the point estimate is above the median.
- **The minimum defensible impact is not zero.**
  - Any shift of the point estimate from 0.60 to 0.50 gives about −17% (3,055 × 0.5/0.6 ≈ 2,546).
  - That is not threshold-crossing, but it is a direct linear reduction with no offset in the model.
  - Combined with the conceded adherence and monitoring haircuts, a 0.65 effective multiplier is the whole distance to the bar.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: omitted morbidity, transmission, and post-treatment survival value partly offset any uptake reduction, and adopters may skew toward high-burden settings.

- **The omitted-value channels do not offset an uptake reduction. They scale with it.**
  - Morbidity reduction, transmission effects, and diagnostic value all require patients to actually take the drug.
  - If uptake is 35% instead of 60%, those channels shrink by the same ratio.
  - They are upside to the level of benefit, not a hedge against the ceiling.
  - They are also unquantified, so they cannot be netted against a quantified downside.
- **The adopter-composition argument is self-described as ungrounded.** The Advocate says "treat it as an uninformed prior". It should carry no weight against the critique.
- **"Constant treated share" is not an offset.** The Advocate calls it "neutral to slightly conservative". Neutral means it offsets nothing.

**KEY UNRESOLVED QUESTIONS:**
- Does 60% represent prescribing, or adherent receipt? If prescribing, a combined adherence-and-other multiplier of 0.65 or lower crosses the bar. No source in the package settles this.
- What do country-level adoption curves look like for other cheap generic adjuncts added to TB or other infectious-disease guidelines, after a positive Phase III? Nobody has pulled this data.
- Does WRD's 4 pp/year trend plateau above or below 60%? Only two data points are verified.
- How would statin uptake be affected by the rifampicin interaction and monitoring needs once guidance is written? The parameter map flags these as unmodeled, and neither side can quantify them.
- Does the BOTEC's 60% embed an implicit haircut for non-adoption, as the Advocate suggests, or is it a ceiling before such haircuts? The report states no derivation.

### Judge Audit
Surviving strength: moderate
Justification: The debate was substantive. Both sides used the verified sensitivity arithmetic, and the Challenger made several honest concessions. Those concessions gutted the critique's quantitative claim: the range is unanchored, 0.40 does not cross the bar, and "no precedent" is false. What survives is a directional claim that 60% sits in the optimistic part of an uncertain distribution, plus a conditional threshold-crossing pathway via unmodeled adherence and monitoring haircuts. That pathway is arithmetically valid but empirically ungrounded and possibly double-counted. The Advocate's defense contained real logical errors on the "already discounted" claim and the offset framing. The Advocate also missed its strongest evidence: many countries exceeded 80% WRD coverage. Had the Advocate used it, the verdict would lean toward weak.
Recommended action: 1. CONCLUDE NOW: Treat 60% as an optimistic-but-plausible central value, not a demonstrated overestimate.
   - The debate does not support moving the point estimate below the 0.39 materiality line. The critique's threshold-crossing claim does not survive.
   - At most, the debate supports a modest downward sensitivity flag, such as reporting a 0.45–0.50 alternative case. This should be labeled as judgment, not evidence.
   - Confidence: moderate.
   - One feasible, targeted check could change this conclusion. Determine from the BOTEC and its trial source whether (a) "uptake" denotes prescribing and (b) the efficacy estimate is ITT.
     - If efficacy is not ITT and uptake means prescribing, the adherence haircut is a genuine, separate adjustment. Ceiling-crossing then becomes more plausible.
     - If efficacy is ITT, the adherence argument largely collapses.
   - This is a document check, not new data collection.
Action feasibility: actionable_now
Advocate failures: ['unsupported_estimate_pseudo: The Advocate claims WRD shows "no sign of saturation" and that the ramp "would reach 60% in under a year from the 2023 level." This is a straight-line extrapolation through two verified endpoints (37% in 2018, 58% in 2023). Two points cannot show the absence of a plateau. The extrapolation also moves from a 24-country diagnostic-coverage subset to an adoption ceiling for a drug, without justifying the transfer. The 4.2 pp/year arithmetic is correct. The inference drawn from it is not.', 'unsupported_estimate_pseudo: The Advocate says the 40% Phase II/III success probability and the one-year-speedup structure "already discount this ceiling." This is a non-numerical chain with a clear logical gap. An independent multiplier leaves the relative effect of changing adult_uptake unchanged. The speedup structure is what makes the ceiling enter linearly. The Challenger correctly identified both points, and the Advocate\'s framing does not survive.', 'call_to_ignorance: The Advocate argues that "Why 60% rather than ~100% is itself discounting … implicitly covers contraindications, clinician non-adoption, private-sector gaps." The Advocate concedes 60% has no stated derivation, then fills that documentation gap with a favorable hidden haircut. The BOTEC\'s only stated justification is "generic and cheap.', 'false_definitiveness: The Advocate says omitted value channels mean that if uptake were lowered, these channels "still offset some of the loss." As framed, this is wrong. Morbidity and transmission benefits scale with uptake in proportion, so they do not offset a relative reduction. The hedge ("I do not claim they fully offset it") sits alongside a confident claim of partial offset. A valid version of the argument existed but was not made (see missed defenses).', 'sound_synthesis_noted: The threshold arithmetic was grounded in the verified linear scaling and the stated sensitivity output: 3,055 × (0.40/0.60) ≈ 2,037x and 3,055 × (0.39/0.60) ≈ 1,986x. From this the Advocate showed that only the bottom of the 0.30–0.40 range crosses the bar. The Challenger conceded the point. This was the most productive move in the debate.', 'sound_synthesis_noted: The Advocate correctly flagged the adopter-composition argument as "an uninformed prior." The Advocate also made honest concessions on prescribing versus adherence, unmodeled rifampicin interaction, and ramp relevance under discounting.']
Challenger failures: ['false_definitiveness: The Challenger says three separate unmodeled haircuts "together … need only a 35% combined shortfall to cross the bar," and later that "a 0.65 effective multiplier is the whole distance to the bar." The Challenger explicitly admits being unable to ground any adherence figure. The phrasing "need only" nonetheless implies crossing is likely. The arithmetic (0.39/0.60 = 0.65) is correct, but the conditional is presented as if it were probable. The Challenger also does not consider whether adherence is already embedded in the trial effect size.', 'unsupported_estimate_fabricated: Under the heading "The minimum defensible impact is not zero," the Challenger posits a shift to 0.50, giving about −17%. The 0.50 figure has no grounding. The label "minimum defensible" implies an evidence-based floor on the downward revision that the debate never established. The arithmetic is fine, but the anchor is invented.', 'strawmanning: On constant treated share, the Challenger writes: "Neutral means it offsets nothing." The Advocate said "neutral to slightly conservative." The Challenger drops the "slightly conservative" half and rebuts only "neutral." This is minor, but it is a selective restatement.', 'sound_synthesis_noted: The Challenger correctly showed that the 40% success probability is independent of adult_uptake and that the speedup structure transmits rather than buffers ceiling sensitivity. The Challenger also correctly distinguished UNVERIFIABLE from REJECTED for adjunct data ("it cuts both ways"). Both the S-curve slowdown and the national-program stocking question were properly labeled as priors. The concessions on 0.40, on the "no precedent" title, and on the unanchored range were honest.', 'sound_synthesis_noted: The Challenger\'s response on omitted value ("they scale with it") is correct about relative effects. It misses that including omitted value would lower the materiality threshold. This is an incomplete engagement rather than a listed failure.']
Debate resolved: The debate established four things:

- The "no precedent" title is false, and the 0.30–0.40 range is a judgment rather than a derived figure.
- Only values at or below about 0.39 cross the bar, so 0.40 does not.
- Neither the 40% success probability nor the one-year-speedup structure buffers the ceiling. It enters linearly, and the WHO quote bears only on the ramp.
- Both available analogs (WRD, 4HPMZ) are structurally imperfect, and neither side can derive an adjunct ceiling from them.
Debate unresolved: Three questions remain contested:

- Whether BOTEC "uptake" means prescribing or adherent receipt. Relatedly, whether trial-derived efficacy already absorbs adherence.
- Where a cheap generic adjunct's real-world ceiling sits relative to WRD's 54–58% and still-rising coverage. Neither side produced any adjunct-specific adoption data.
- Whether the omitted value channels would move the materiality line meaningfully below 0.39.

--- Critique: A Phase III cannot be powered on mortality, so the WHO GDG would be recommending on surrogate or composite endpoints ---

### Advocate
DEFENSE OF GIVEWELL'S (CG'S) POSITION: A Phase III cannot be powered on mortality, so the WHO GDG would be recommending on surrogate or composite endpoints

**EXISTING COVERAGE:**
- The BOTEC already conditions on the scenario the critique worries about.
  - The 10% relative mortality reduction applies "conditional on a positive result."
  - The 40% p_success covers Phase II and Phase III jointly.
  - The 60% uptake is already a haircut from universal use, applied "if it works."
- Expected uptake and expected effect are already discounted. The expected relative reduction is 4% (10% × 40%), and uptake is 60% rather than near 100%.
- The "years_to_adoption / delay" pathway is largely neutralized by the structure of the speedup.
  - The grant's value is a 1-year acceleration relative to a counterfactual.
  - If a GDG requests more evidence, that delay applies to both the grant-funded and counterfactual timelines.
  - The effect on speedup_years is therefore second-order. It matters only if the delay were asymmetric.
- The critique's own evidence concedes much of the delay pathway. It says that if Phase III reports "unfavorable outcome, which includes death," a recommendation "need not stall." That weakens the case for a timing effect.
- The parameter map notes that the $7M all-in cost explicitly includes "later Phase III trials, guideline changes, dissemination and validation." CG has therefore priced a trial of some design. Whether that design is realistic is the all_in_cost critique (Thread 1 interaction), not a new uptake or timing parameter.

**EVIDENCE WEAKNESSES:**
1. **The sample-size premise is partly wrong for CG's inputs.**
   - The critique uses a 5% baseline. CG uses 6%.
   - Standard two-proportion formula: n per arm ≈ (1.96+0.84)² × [p₁(1−p₁)+p₂(1−p₂)] / (p₁−p₂)².
   - At 6% baseline and a 10% relative reduction (p₂ = 5.4%): 7.84 × 0.1075 / 0.000036 ≈ 23,400 per arm.
   - I get ≈28,400 per arm at 5%, which matches the critique's figure. So the critique's number is correct for its input, but it rests on an input CG did not use. The headline infeasibility claim is similar either way (~23–28k per arm).
2. **The "high-risk subgroup makes the sample-size problem worse" claim runs the wrong way.**
   - Required n falls as baseline mortality rises, because absolute differences grow.
   - Illustration at a 12% baseline (my assumption, not a grounded figure, e.g. a high-risk subgroup): p₂ = 10.8%, so n ≈ 7.84 × 0.2019 / 0.000144 ≈ 11,000 per arm.
   - That is less than half the 6% requirement, though still large. Enrollment pools are smaller, but the required n drops faster than the plausible pool shrinks only if the subgroup is not too narrow. The critique asserts "worse" without showing this.
3. **The GRADE argument is generic.**
   - Downgrading for indirectness is real GRADE methodology, but the critique offers no TB-specific precedent of a WHO TB recommendation stalled or downgraded to "conditional with low uptake" for this reason.
   - WHO TB guidance has repeatedly been built on composite treatment outcomes. The 4-month rifapentine-moxifloxacin regimen (Dorman et al., NEJM 2021, Study 31/A5349) rested on a non-inferiority endpoint of TB disease-free survival, not mortality. WHO adopted it in 2022. I cite this as a precedent for composite endpoints driving recommendations, not as proof that this trial would do so.
4. **Trials need not be powered on all-cause mortality to show a mortality signal.** Dexamethasone for TB meningitis (Thwaites et al., NEJM 2004) showed a survival benefit in roughly 545 patients because baseline mortality in that population was very high. This is a counterexample on feasibility, though it does not transfer directly to general TB.
5. **The uptake channel is unquantified by the critique's own admission.** Its example ("a third of patients ... cut effective uptake by half or more") is labelled speculative. A speculative scenario does not meet the burden of proof for shifting a parameter.
6. **The baseline-mortality flag is unresolved.** I cannot ground a WHO-based figure here. For rough context, WHO Global TB Report headline numbers (~1.2M deaths on ~10.8M incident cases, from memory, so treat as unverified) imply much higher mortality than 6% across all cases. That would only matter in the direction of making a mortality trial easier. I treat this as uninformed prior.

**MAGNITUDE CHALLENGE:**
- The model is multiplicative and linear in relative_reduction and adult_uptake. Expected SROI depends on their means, not their variance.
- "Unverified" raises the spread of the realized relative_reduction. It lowers the expected value only if the 10% is biased upward. The critique does not show bias. It only says the mortality effect is not directly tested.
- A 10% effect is already a modest surrogate-to-mortality translation. A surrogate-based recommendation could plausibly carry smaller or larger true effects. The direction of bias is unestablished.
- The uptake haircut is the only parameter that moves. Assume a conditional recommendation cuts uptake from 60% to 30–40%, which is my illustrative range, not a sourced one. SROI would then fall from ~3,000x to roughly 1,500–2,000x, which would cross the bar.
  - That is the strongest version of the critique, and I cannot rule it out.
  - But it requires three things simultaneously: (a) the trial is not mortality-powered, (b) GRADE downgrades to conditional, and (c) a conditional recommendation substantially depresses uptake of a cheap generic drug.
  - The critique supports (a) and partially (b). It gives no evidence for (c).
- The critique's Sensitivity Results are empty ({}), so no tested magnitude supports the claim.

**OFFSETTING FACTORS:**
- Atorvastatin is cheap, generic, and widely used for cardiovascular indications. Clinicians already know its safety profile. This lowers barriers to adoption under a conditional recommendation, and national programs can adopt on weaker evidence for low-cost, low-risk adjuncts.
- CG values only on-treatment mortality. Morbidity (lung damage), post-treatment survival, and transmission effects are implicit zeros (parameter map, Thread 4). If a surrogate-based recommendation is driven by lung damage and clearance, the benefits that justify adoption are partly uncounted. This offsets the "mortality unverified" concern.
- The 40% p_success may already absorb some of this concern. "Both Phase II and III succeed" with no stated definition could plausibly include adoption risk.

**OVERALL ASSESSMENT:** Partial defense.
- The delay pathway is weak. Symmetric timelines mostly cancel it, and the critique concedes the "unfavorable outcome" route.
- The variance pathway does not move expected SROI absent bias.
- The uptake pathway is the one real vulnerability.
- The trial-feasibility premise is directionally right, but it is partly mis-specified. It uses a 5% baseline rather than CG's 6%, and its subgroup claim runs the wrong way.

**CONCESSIONS:**
- A Phase III powered on mortality at ~23–28k per arm is implausible within a $7M all-in budget. This also creates a cost-realism problem for all_in_cost (Thread 1 interaction), which I do not defend here.
- CG does not define "success." The 40% p_success and 60% uptake are not linked to an endpoint, so the surrogate-versus-mortality distinction is genuinely unaddressed.
- If conditional recommendations materially depress uptake (not shown by the critique, but plausible), SROI could fall below the 2,000x bar. The critique's strength rating of medium to medium-low seems fair, and I cannot rule out the downside.

### Challenger
REBUTTAL: A Phase III cannot be powered on mortality, so the WHO GDG would be recommending on surrogate or composite endpoints

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the 10% effect is already "conditional on success," 40% p_success covers Phase II and III, and the 60% uptake is already a haircut, so the scenario is priced in.

- **The Advocate's own concession undercuts this.** The Advocate concedes that CG "does not define success" and that p_success and uptake "are not linked to an endpoint."
  - A parameter cannot both already absorb surrogate-endpoint risk and be unlinked to any endpoint.
  - "May already absorb some of this" is speculation about an undefined quantity. It is not coverage.
- **The haircut's basis is unestablished.** I cannot ground what the 60% represents. The Advocate does not claim to know either.
  - The relevant question is whether 60% is conditional on a mortality-confirmed result or on a surrogate-driven recommendation.
  - Nothing in the BOTEC separates those cases.
- **The threshold is lower than the Advocate's framing implies.** I take the Advocate's ~3,000x SROI and 2,000x bar, plus the linearity in uptake the Advocate accepts.
  - Breakeven uptake is 60% × (2,000/3,000) = 40%.
  - A relative uptake reduction of one-third therefore reaches the bar.
  - The critique's "half or more" scenario would overshoot it. The Advocate calls this "the one real vulnerability."

> The Advocate claims: the delay pathway is neutralized because a GDG evidence request delays the grant-funded and counterfactual timelines equally.

- **I concede most of this.** The speedup is a difference between timelines, and a symmetric delay mostly cancels. The verifier's note that a recommendation "need not stall" points the same way.
- **One narrow residual remains.** The cancellation holds only if the counterfactual faces the identical evidence requirement. I have no evidence either way.
- **I do not press this channel further.** The remaining weight sits on uptake and effect verification.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the critique's 5% baseline differs from CG's 6%.

- **I concede the input mismatch.** My recomputation matches the Advocate's: ≈28,400 per arm at 5% and ≈23,400 at 6%, using (1.96+0.84)² = 7.84.
- **The conclusion is unchanged.** The Advocate also concedes ~47,000 participants in total is implausible within $7M.
- **That concession is essentially the critique's first premise.** The surrogate or composite trial is the only affordable design, so what remains contested is what follows from it.

> The Advocate claims: the "subgroup makes sample size worse" claim runs the wrong way, because required n falls as baseline risk rises.

- **I concede the arithmetic.** At 12%, ≈11,000 per arm versus ≈23,400 at 6%, holding a 10% relative reduction.
- **The verifier's phrasing does not survive as stated.** "Worse because fewer patients enroll" is the weaker claim.
- **A narrower residual remains, and it is conditional on three things.**
  - The Advocate's 12% is, by their own label, ungrounded.
  - The subgroup must be identifiable at enrollment and found at sites that can run a trial of ~22,000 total.
  - Even then the trial is large, roughly 11,000 per arm.
- **A recommendation from a subgroup trial would likely be limited to that subgroup.** This links back to the uptake channel and is not a separate feasibility problem.

> The Advocate claims: Dorman et al. (NEJM 2021, Study 31/A5349) shows WHO adopting a regimen on a composite endpoint, and Thwaites et al. (NEJM 2004) shows a mortality signal in a small trial.

- **The Study 31 precedent is not analogous on the key point.**
  - There, the composite (TB disease-free survival) was the outcome the intervention targets. The regimen's value is cure.
  - Here, CG values only mortality reduction. A composite recommendation does not directly validate the modeled benefit, which is exactly the "indirectness" concern.
- **Composite outcomes can dilute death.**
  - "Unfavorable outcome" includes failure, relapse and loss to follow-up as well as death.
  - A positive composite is consistent with a mortality effect below 10%, or none.
  - I cannot ground how much of the composite is death for an atorvastatin adjunct.
- **I concede the TBM dexamethasone case does not transfer.** The Advocate says so too. Its sample size reflects a high-mortality population and a large effect. A 10% relative reduction in a ~6% baseline is neither.
- **The baseline-mortality flag is unresolved on both sides.**
  - The Advocate's WHO-level figures are from memory and are marked unverified.
  - I cannot ground this either; treat it as an uninformed prior.
  - Population-level fatality includes untreated cases, so it is not clearly the trial-eligible baseline.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: the model is linear, so only means matter, and "unverified" raises variance without showing bias in the 10%.

- **Linearity is correct for the variance claim.** The variance pathway alone does not move expected SROI.
- **There is a plausible selection mechanism for bias, though I cannot quantify it.**
  - The 10% is explicitly "conditional on a positive result."
  - If "positive" is declared on a surrogate or composite, the selection runs on that endpoint, not on mortality.
  - The expected mortality effect conditional on a surrogate win is then plausibly below the nominal figure.
  - Surrogate-to-mortality translation in TB trials is generally imperfect. I recall the literature on culture conversion as a trial-level surrogate but have not verified specifics, so I cite no figures.
- **The Advocate's mean argument cuts both ways.** The Advocate says "a 10% effect is already modest" and that bias direction is unestablished. That is an argument that the 10% is not demonstrably unbiased, not that it is unbiased.
- **The Advocate's own breakeven analysis is the strongest point.**
  - Uptake of 30–40% gives SROI of 1,500–2,000x, at or below the bar.
  - The Advocate says (c), the link from conditional recommendation to low uptake, has no evidence. I agree it is not shown, and the critique labels it speculative.
  - Whether (c) holds is a conditional question, and the required effect size is a one-third cut in uptake.

**RESPONSE TO "OFFSETTING FACTORS":**

- **Atorvastatin is cheap, so adoption barriers are lower.**
  - This is reasoning from drug cost to adoption, and the Advocate offers no source.
  - The relevant barriers for a conditional recommendation are guideline authority, program training and clinician belief in the effect. These do not fall with drug price.
  - The offset is plausible but unquantified and absent from the model.
- **Uncounted morbidity benefits offset the concern.**
  - CG's model assigns zero value to morbidity, so the benefit is real but not in the SROI.
  - If a surrogate-driven recommendation is adopted on lung-damage grounds, the mortality-denominated SROI still rests on the unverified mortality effect. The morbidity benefit does not repair that.
  - Using it as an offset requires adding a valuation the model does not contain.
- **p_success may absorb adoption risk.** See the existing-coverage section: this conflicts with the Advocate's concession that p_success is not tied to an endpoint.

**KEY UNRESOLVED QUESTIONS:**
- What endpoint does the planned Phase III use, and what share of any composite is death?
- Is CG's 60% uptake conditional on a mortality-confirmed result, or a generic discount?
- What is the realistic trial-eligible mortality baseline (WHO source still needed)? Is a high-risk subgroup trial feasible, and would the resulting recommendation be restricted to that subgroup?
- Does a conditional WHO recommendation cut uptake of a cheap generic adjunct by at least one-third (the breakeven)? Neither side has evidence.
- Is the 10% effect biased when selected on a surrogate "success"?

### Judge Audit
Surviving strength: moderate
Justification: The exchange was productive, with few failure modes. Both sides did correct arithmetic and made clean concessions. The Advocate successfully dismantled the delay, variance, and subgroup-feasibility components. However, the Advocate conceded that the uptake channel could push SROI to or below the bar. The Challenger sharpened this into a concrete one-third breakeven and gave a non-trivial Study 31 disanalogy: the composite there was the intended benefit, whereas CG values mortality only. The surviving channel still rests on an ungrounded link from a conditional recommendation to lower uptake. That keeps the verdict at moderate rather than strong.
Recommended action: 1. CONCLUDE NOW (high confidence):
   - Drop the years_to_adoption and variance-only pathways from this critique.
   - Accept the feasibility premise: the Phase III will be surrogate- or composite-endpoint.
   - Correct the baseline to CG's 6% (~23,400 per arm).
   - Strike the verifier's "subgroup makes it worse" note.

2. SPECIFIC INVESTIGATION (feasible with existing tooling): These are three targeted lookups that would settle the surviving uptake channel.
   - **(a) CG's source materials.** Determine what the 60% uptake and 40% p_success are conditioned on. Specifically, check whether "success" is defined on a surrogate or composite endpoint or on a mortality-confirmed result.
   - **(b) Uptake after WHO TB recommendations.** Search for national-level uptake following WHO TB recommendations graded conditional versus strong. Candidate sources include the WHO TB Knowledge Sharing Platform, Stop TB/MSF "Step Up for TB" policy-adoption surveys, and adoption timelines for conditionally recommended interventions such as 3HP preventive therapy and shorter regimens. Test whether conditional status is associated with a relative uptake shortfall of at least one-third.
   - **(c) Trial-eligible baseline.** Retrieve WHO Global TB Report treatment-outcome data, specifically the "died" proportion among treated DS-TB cohorts.

   If (b) shows typical shortfalls well below one-third, downgrade the critique to weak. If it shows shortfalls above one-third, the critique becomes decision-relevant.
Action feasibility: requires_specified_evidence
Advocate failures: ['sound_synthesis_noted: The sample-size recomputations are correct and fully shown. 6% → p₂ = 5.4%, giving 7.84 × 0.1075 / 0.000036 ≈ 23,400 per arm. 5% → ≈ 28,400 per arm. 12% → ≈ 11,000 per arm. The point that required n falls as baseline risk rises is a valid correction of the verifier\'s "subgroup makes it worse" note. The symmetric-delay argument is also structurally sound: speedup is a difference of timelines, so a common delay cancels.', 'sound_synthesis_noted: The breakeven framing derives SROI under alternative uptake from CG\'s ~3,000x via the model\'s linearity. The 30–40% uptake range is explicitly labelled "illustrative, not sourced." This is a scenario test, not a fabricated claim. It honestly identifies the critique\'s strongest channel.', 'unsupported_estimate_pseudo: The Advocate cites "~1.2M deaths on ~10.8M incident cases, from memory." From this they infer that a mortality trial would be easier ("would only matter in the direction of making a mortality trial easier"). The inference does not follow. Population case fatality includes untreated and undiagnosed cases and says little about on-treatment mortality among trial-eligible patients. The verifier\'s plausible on-treatment range (3–6%) sits at or below CG\'s 6%, which would make the trial larger, not smaller. The figure is flagged as unverified, which mitigates the problem, but the directional conclusion drawn from it is wrong.', 'call_to_ignorance: The 40% p_success may already absorb some of this concern... could plausibly include adoption risk." This fills an undefined parameter with a favourable interpretation. It also contradicts the Advocate\'s own concession that p_success "is not linked to an endpoint.', 'false_definitiveness: The Advocate claims that cheap, familiar generics face lower adoption barriers and that "national programs can adopt on weaker evidence for low-cost, low-risk adjuncts." This is stated as a general fact with no source or TB precedent, and it is used as an offset.']
Challenger failures: ['sound_synthesis_noted: The Challenger computes breakeven uptake as 60% × (2,000/3,000) = 40%, so a one-third relative cut in uptake reaches the bar. This is built transparently from the Advocate\'s accepted figures and linearity. It is the most useful quantitative move in the debate, because it converts the critique\'s vague "half or more" into a concrete threshold. The Challenger also replicated the sample-size arithmetic and openly conceded the 6% input, the subgroup direction, the delay pathway, and the TBM case.', 'call_to_ignorance: The Challenger argues that "the expected mortality effect conditional on a surrogate win is then plausibly below the nominal figure." They follow this with: "That is an argument that the 10% is not demonstrably unbiased, not that it is unbiased." The selection mechanism is articulated, so this is not pure speculation. But the second sentence shifts the burden: the critique, not CG, must show the direction of bias. The Challenger admits they cannot cite surrogate-validity figures.', 'strawmanning: The Advocate\'s adoption-barrier offset combined low cost, clinician familiarity with the safety profile, and low-risk adjunct status. The Challenger rebuts only the price component ("reasoning from drug cost to adoption... barriers... do not fall with drug price"). The familiarity and safety elements go unaddressed. The counter-assertion is also unsourced.', 'false_definitiveness: A parameter cannot both already absorb surrogate-endpoint risk and be unlinked to any endpoint." This is overstated. An undefined p_success could still implicitly absorb some generic success and adoption risk. The valid point is that coverage cannot be demonstrated, not that it is logically impossible.']
Debate resolved: The debate established the following:
- **Feasibility premise accepted.** A mortality-powered Phase III (~23–28k per arm at a 5–6% baseline, 10% relative reduction) is infeasible within the $7M all-in budget. Both sides accept this.
- **Delay pathway largely neutralized.** A symmetric delay mostly cancels in the speedup calculation.
- **Variance pathway inert alone.** Higher variance does not move expected SROI unless the effect estimate is biased.
- **Subgroup claim reversed.** The "subgroup makes sample size worse" claim runs the wrong way.

The critique therefore narrows to two live channels:
1. Uptake under a conditional or subgroup-restricted recommendation, which reaches the 2,000x bar if uptake falls by one-third (60% → 40%).
2. Possible downward bias in the 10% effect when "success" is declared on a surrogate.
Debate unresolved: Three questions remain open, and neither side produced evidence on them:
- Whether a WHO conditional or subgroup-limited recommendation for a cheap generic adjunct reduces uptake by at least one-third.
- Whether selecting on surrogate or composite success biases the expected mortality effect below 10%.
- Whether CG's 60% uptake already assumes a non-mortality-confirmed recommendation.

--- Critique: Clinical eligibility and monitoring barriers cap the achievable prescribing share below the "generic and cheap" logic ---

### Advocate
DEFENSE OF GIVEWELL'S (CG'S) POSITION: Clinical eligibility and monitoring barriers cap achievable prescribing share

**EXISTING COVERAGE:**
- CG's 60% uptake is not a "generic and cheap, so near-universal" assumption. It already removes 40 percentage points from the 5.5M eligible adults.
  - The BOTEC does not say what the 40% non-uptake represents.
  - Liver disease, DILI, pregnancy, polypharmacy, program reluctance and discontinuation are the obvious frictions that would fill that gap. If so, the critique's 10–20% exclusion partly or wholly double-counts a haircut that is already in the 60%.
  - I cannot show that CG intended this. I raise it as a conditional: if 60% was set with such frictions in mind, the critique's adjustment is mostly redundant.
- The 5.5M × 60% base is also restricted to adults. This already removes the pediatric share, though the parameter map notes the BOTEC does not make this explicit.
- The 40% probability of success covers both trials and is applied multiplicatively.
  - A Phase III that fails to produce a usable, safe regimen contributes no benefit.
  - The eligibility and safety questions in the critique (liver disease, interactions, statin choice) are exactly what Phase IIc and III dosing and safety data would resolve. They are partly priced into p_success rather than only into uptake.
- Monitoring and adverse-event management costs are not in the $7M, and I concede that below.

**EVIDENCE WEAKNESSES:**
- The central number is self-described as "my own illustrative scenario, not a sourced estimate." The critique's own flags mark the 10–20% exclusion share and the 0.45–0.50 figure as UNGROUNDED.
  - The arithmetic is also incomplete. 0.60 × (0.80–0.90) = 0.48–0.54. Reaching 0.45–0.50 needs an unspecified "program-adoption factor" that has no source.
- The 11.5% pooled DILI figure does not measure an exclusion share.
  - It is an incidence during anti-TB treatment, mostly attributable to HRZE itself.
  - It does not show that 11.5% of patients would be ineligible to start an adjunct statin. DILI during treatment is typically managed by pausing drugs, which is a discontinuation or temporary-hold issue, not a permanent loss of the whole eligible pool.
  - The critique treats incidence as if it were a pre-treatment exclusion rate.
- The "NTP LFT-monitoring gap" is unsourced. I engage with it conditionally: if routine LFT monitoring were mandated for statin co-prescription and unavailable, uptake or cost would be affected.
  - My recollection, unverified, is that WHO guidance recommends routine LFTs mainly for patients with pre-existing liver disease or other risk factors, not for all patients. If so, adding a statin need not imply universal LFT monitoring.
  - I cannot ground this further. It is an uninformed prior, not a rebuttal.
- Trial exclusion criteria are only a guess ("will probably exclude liver disease"). Even if true, standard drug labels routinely carry hepatic-disease cautions without collapsing real-world use among eligible patients.
- The drug-interaction argument is partly about statin choice, which the critique itself concedes.
  - The critique notes that a less CYP3A4-dependent statin would soften the ART and rifamycin arguments.
  - The critique's own trial example is rosuvastatin. By general pharmacology (not verified here), rosuvastatin is only minimally CYP-metabolized.
  - Statins have been co-prescribed with ART at scale. The REPRIEVE trial (pitavastatin in people with HIV, NEJM 2023) is an example of a statin tested in a large HIV population. I cite it only as evidence that statin–ART co-prescribing is operationally manageable, not as evidence about TB patients.
- Rifampicin lowering statin exposure is an efficacy and dosing issue (relative_reduction). It is not an eligibility or uptake issue, and it is outside this parameter. The Phase IIc dosing-strategy work targets it directly.
- The pregnancy point has a current-label wrinkle I can state. In 2021 the FDA asked for removal of the blanket contraindication to statin use in pregnancy from statin labels. I recall this but have not re-verified it. If so, "pregnancy" is a weaker exclusion than the critique's framing implies, and pregnant patients are a small subset of adult TB cases in any case.
- The Sensitivity Results are empty ({}). The critique asserts "material" without having run the formula chain.

**MAGNITUDE CHALLENGE:**
- Take the critique's own illustrative range: 0.60 → 0.45–0.50.
  - Relative change: 0.45/0.60 = −25%, and 0.50/0.60 = −16.7%.
  - Because uptake enters the BOTEC multiplicatively, SROI moves by the same proportions. CG's unrounded SROI is (54e9/7e6) × 0.4 ≈ 3,086x. That gives roughly 2,300x to 2,570x.
- Both ends stay above the ~2,000x bar.
  - The change is at most about 25%, which is at the edge of the "more than ~25%" materiality threshold and not clearly beyond it.
  - Even the critique's most pessimistic self-constructed scenario therefore does not by itself make the finding decision-relevant. The "material" label depends on the unsourced low end and on further stacking from LFT monitoring costs, which are unquantified.
- The more defensible range is narrower than the critique's.
  - If part of the 10–20% exclusion is already in CG's 60%, the net adjustment is smaller than 17–25%.
  - Only the part of the exclusion that CG did not already cover would count, and I cannot ground how much that is.

**OFFSETTING FACTORS:**
- The BOTEC values only on-treatment mortality. Per the parameter map, these channels are implicit zeros: morbidity and lung-damage DALYs, post-treatment mortality, transmission averted, and the diagnostic. These omissions bias the estimate down and could offset a modest uptake haircut.
- Prescribing is a decision made by clinicians and programs. A guideline-endorsed generic adjunct may be adopted in a risk-stratified way. That means higher uptake among low-risk patients, who are the majority, with exclusions applied to the highest-risk patients.

**OVERALL ASSESSMENT:** Partial defense.
- The direction of the critique is sound: clinical exclusions and monitoring friction plausibly reduce uptake below a naive "cheap generic" reading.
- The critique's magnitude is unsourced. It may double-count the existing 40-point haircut. Even at the critique's own worst case, SROI stays above the bar and the change sits at the edge of the materiality threshold.
- I cannot show that CG deliberately embedded these frictions in the 60%. The defense therefore rests on the conditional double-counting argument and on the weakness of the quantification, not on the concern being already covered.

**CONCESSIONS:**
- CG gives no empirical precedent or breakdown for the 60% figure, so the critique's request for grounding is fair.
- Monitoring costs (LFTs, adverse-event management) are not in the $7M all-in cost. If monitoring is required, the effect is on cost, not only on uptake, and the two effects compound.
- If excluded subgroups (HIV coinfection, liver disease, advanced disease) carry disproportionate shares of the 6% baseline mortality, excluding them reduces benefit by more than their headcount share. This would worsen the effect beyond the pure uptake arithmetic. The parameter map notes that CG does not decompose this.
- DILI attribution confounding with a statin is a real practical issue that could produce program reluctance. I cannot quantify it, and it is plausibly larger than the pure incidence numbers suggest.

### Challenger
REBUTTAL: Clinical eligibility and monitoring barriers cap the achievable prescribing share

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: CG's 60% uptake already removes 40 points from the 5.5M eligible adults. The frictions the critique lists (liver disease, DILI, pregnancy, polypharmacy, reluctance, discontinuation) would plausibly fill that gap, so the 10–20% exclusion double-counts.

- **The conditional cuts both ways.**
  - The Advocate concedes they cannot show CG intended this and that CG gives no breakdown for the 60%.
  - The 40% gap could equally hold other frictions: diagnosis and delivery gaps, procurement, guideline lag, and clinician inertia in national TB programs. If so, none of the clinical frictions are covered.
  - An unsourced number that nobody can decompose cannot be relied on to absorb a specific haircut. The double-counting argument shows only that the overlap is unknown, not that it is large.
- **Even if the double-counting holds, it covers only headcount.** The Advocate concedes that excluded subgroups (HIV coinfection, liver disease, advanced disease) may carry a disproportionate share of the 6% baseline mortality.
  - The BOTEC applies one baseline mortality to everyone.
  - A 60% headcount haircut, however composed, does not capture that excluded patients are the highest-mortality patients.
  - So there is a residual that no reading of the 40% removes. Its size is unquantified, but it points downward.
- **The p_success argument conflates two things.** The Advocate says eligibility and safety questions are "partly priced into p_success" because Phase IIc/III data will resolve them.
  - p_success is the probability that the trials show a usable regimen. Uptake is what share of eligible adults receive it after the trials succeed.
  - Trial success does not remove exclusions. It writes them into the evidence base. The verifier's evidence item says trial eligibility criteria "will probably exclude liver disease, so any recommendation would inherit those exclusions." That item is an inference, not a verified fact.
  - Resolving the safety questions can fix what the label says. It does not enlarge the population the label covers.
- **The pediatric point is not a rebuttal.** The critique concerns adults, and the Advocate agrees the BOTEC does not make the restriction explicit.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

- **Concede: 11.5% DILI incidence is not a pre-treatment exclusion share.** The Advocate is right.
  - It still bears on mechanisms (b) and (c): discontinuation and program reluctance.
  - The Advocate concedes that DILI attribution confounding is real and "plausibly larger than the pure incidence numbers suggest."
  - A statin co-prescribed with HRZE gives clinicians a reason to stop the statin at the first transaminase rise. That is a continuation loss, not a permanent exclusion.
  - Whether `adult_uptake` is meant to capture continuation is unknown. If it is, this is a real loss. If not, it is an omitted factor elsewhere in the model.
- **The statin-choice argument rests on an unverified assumption.** The Advocate argues the critique's own example is rosuvastatin, which is minimally CYP-metabolized.
  - The verifier's evidence says CG's actual candidate is "in the source materials, which I could not check."
  - The rosuvastatin trial is an example of existing evidence, not CG's chosen agent.
  - The Advocate's pharmacology is flagged by the Advocate as unverified. I cannot ground a counter-claim either. The statin-choice question is open, not resolved in CG's favor.
  - The Advocate concedes the DILI-attribution argument is untouched by statin choice.
- **REPRIEVE shows co-prescription is operationally manageable in HIV populations.** It does not address TB, rifamycins, or HRZE hepatotoxicity, as the Advocate acknowledges. It does not rebut the concern.
- **The LFT-monitoring dispute is a stalemate.** The critique's gap claim is unsourced. The Advocate's counter-recollection about WHO guidance is also unverified, and the Advocate labels it "an uninformed prior, not a rebuttal." Neither side has moved the evidence.
- **The label-cautions analogy has no cited example.** The Advocate says labels carry hepatic cautions without collapsing use, but names no drug or program. It is an analogy, not evidence.
- **Concede: the pregnancy exclusion is probably weaker than framed.** The FDA's 2021 label change is recalled but unverified. Pregnant patients are a small share of adult TB cases.
- **Rifampicin lowering statin exposure is mainly a `relative_reduction` issue.** I concede it is largely outside uptake, apart from a possible dose-escalation or monitoring burden that I cannot ground.
- **"Sensitivity Results are empty" is not an evidence objection.** The Advocate ran the arithmetic themselves in the next section.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

- **Check the Advocate's arithmetic.** 3,086 × 0.75 ≈ 2,314 and 3,086 × 0.833 ≈ 2,571. The numbers are right, and both stay above ~2,000x.
- **Bar-crossing needs only a modest extra stack.** The factor needed to reach 2,000x is 2,000 / 3,086 ≈ 0.648, a 35% total reduction.
  - Starting from the critique's 0.75–0.83 uptake factor, the remaining required factor is 0.648/0.75 ≈ 0.86 down to 0.648/0.833 ≈ 0.78.
  - So another 14–22% reduction would be needed from the other effects.
- **The Advocate concedes those other effects exist but are unmodeled.**
  - Mortality-weighting of excluded subgroups.
  - LFT and adverse-event costs outside the $7M.
  - Reluctance from DILI attribution.
  - The critique's 0.45–0.50 is explicitly "before adherence."
  - I cannot ground that these three together reach 14–22%. They compound multiplicatively and all point down. The Advocate's "at most 25%" treats the critique's illustration as a ceiling, but by the Advocate's own concessions it is a partial figure.
- **The floor is genuinely unknown.**
  - If the double-counting were fully true, the adjustment would be near zero. The critique's range is therefore bounded by what is ungrounded on both sides.
  - The Advocate's "at the edge of materiality" is a fair description of the visible, quantified portion. It does not describe the whole.
- **The relevant comparison is not only the ~2,000x bar.** I cannot ground how close the SROI sits to any decision threshold beyond what the Advocate states, so I do not push this further.

**RESPONSE TO "OFFSETTING FACTORS":**

- **The implicit zeros are real in direction but unquantified.** Morbidity, post-treatment mortality, transmission and the diagnostic are omitted.
  - They sit in other parameters and are not tied to uptake.
  - The Advocate offers no figure for them. An unquantified upward bias cannot cancel a specific downward adjustment without a sizing.
  - I cannot ground whether a mortality-reducing adjunct would generate transmission benefit, so I do not rely on that channel.
- **Risk-stratified adoption works against the offset.** The Advocate says clinicians would use the drug in low-risk patients and exclude the highest-risk. The Advocate also concedes the highest-risk subgroups carry disproportionate baseline mortality.
  - So risk-stratified uptake concentrates use where mortality is lowest and leaves out where benefit is greatest.
  - That is a mortality-weighted haircut larger than the headcount figure, the opposite of an offset.
  - The claim that low-risk patients are "the majority" is ungrounded, though it is plausible for headcount.

**KEY UNRESOLVED QUESTIONS:**
- What does the 40% non-uptake in CG's 60% represent? Clinical exclusions, delivery failure, or an unexamined round number? The double-counting argument turns entirely on this, and no source resolves it.
- What is the baseline mortality in the excluded or deferred subgroups (HIV coinfection, liver disease, advanced disease) relative to the 6% average? This would convert a headcount haircut into a benefit-weighted one.
- Which statin is CG's candidate? This determines how much of the interaction argument survives. The verifier could not check.
- Is LFT monitoring actually required for statin co-prescription in TB programs? If so, what does it cost? Both sides' claims are unverified.
- Does `adult_uptake` include on-treatment continuation, or is discontinuation after DILI absent from the model?

### Judge Audit
Surviving strength: moderate
Justification: The debate was productive. Both sides showed their arithmetic and made appropriate concessions. The Advocate grounded the point that, on the critique's own worst-case illustration, SROI stays above the bar and the change sits at the edge of the 25% materiality threshold. The Challenger landed a valid conceptual point that p_success does not absorb label-population restrictions. It also raised a plausible but unestablished mortality-weighting argument. Neither side's push beyond the visible magnitude was grounded: the Challenger's stacking of unsized downward factors and the Advocate's unsized upward offsets. So the direction survives firmly and the decision-relevance remains genuinely open.
Recommended action: CONCLUDE NOW: Treat clinical eligibility and monitoring as a valid downward adjustment to `adult_uptake` of roughly 15–25%, with moderate confidence in direction and low confidence in magnitude. On its own, this adjustment does not move SROI below ~2,000x. Uncertainty notes should flag that the adjustment may partly overlap CG's existing 40-point haircut. It should not be stacked with adherence or discontinuation unless those are confirmed absent from other parameters.

Two targeted checks are feasible with existing tooling and could change the conclusion:
1. **CG's source materials.** Check them for (a) the stated rationale for the 60% uptake figure and (b) the specific statin candidate. This resolves the double-counting and interaction questions directly.
2. **Mortality literature.** Retrieve published on-treatment mortality for HIV-coinfected and pre-existing-liver-disease TB patients relative to the overall drug-susceptible TB average, a well-studied quantity. This tests whether mortality-weighting could plausibly supply the missing 14–22%.
Action feasibility: actionable_now
Advocate failures: ["sound_synthesis_noted: The Magnitude Challenge computes CG's unrounded SROI as (54e9/7e6) × 0.4 ≈ 3,086x. It then applies the critique's own 0.45–0.50 range (−25% / −16.7%) to get ≈2,314x–2,571x. Each step is shown, and the Challenger independently confirmed the arithmetic. This is legitimate analysis, not guess-trading.", 'call_to_ignorance: The Advocate says the implicit-zero channels (morbidity, post-treatment mortality, transmission, diagnostic) "bias the estimate down and could offset a modest uptake haircut." The omissions are documented in the parameter map, so the direction is grounded. But no sizing is offered, and an unquantified upward bias is presented as a possible counterweight to a specific downward adjustment. This is mild, because the Advocate frames it as "could." The Challenger correctly identified the problem.', 'unsupported_estimate_fabricated: Two qualitative-quantitative claims carry no grounding:']
Challenger failures: ['sound_synthesis_noted: The bar-crossing arithmetic is shown step by step:', 'call_to_ignorance: After conceding "I cannot ground that these three together reach 14–22%," the Challenger still argues that "they compound multiplicatively and all point down." It then concludes that the Advocate\'s "at most 25%" is "a partial figure" and that "the floor is genuinely unknown." Listing unsized downward factors as a reason the magnitude may be larger mirrors the Advocate\'s unsized offset move. The Challenger is admirably explicit about the lack of grounding, which reduces but does not remove the problem.', 'false_definitiveness: The Challenger makes two confident claims:', 'strawmanning (minor): The Challenger offers "diagnosis and delivery gaps" as alternative contents of CG\'s 40% non-uptake. The base is 5.5M eligible adults, who are presumably already diagnosed and notified TB patients, so diagnosis gaps are likely already outside the denominator. The broader point still stands: procurement, guideline lag and clinician inertia could fill the gap, and the overlap is unknown.']
Debate resolved: Both sides agree the direction of the critique is sound. The two sides also agree on these points:
- **Weakened sub-components.** The 11.5% DILI figure is an incidence, not an exclusion share. The pregnancy exclusion is weaker under current labeling. The rifampicin–statin interaction belongs mainly to `relative_reduction`.
- **Shared arithmetic.** The critique's own illustrative uptake range moves SROI from ≈3,086x to ≈2,314–2,571x, which is still above the ~2,000x bar.
- **Bar-crossing requirement.** Crossing the bar requires a ≈35% total reduction. That means a further 14–22% from effects neither side has sized.
Debate unresolved: Three questions remain open:
- whether CG's 40-point non-uptake already absorbs the clinical exclusions, which decides the double-counting question;
- whether the excluded or deferred subgroups carry materially higher baseline mortality than the 6% average, which would convert a headcount haircut into a larger benefit-weighted one;
- which statin CG's candidate is, which determines how much of the CYP3A4 interaction argument survives.

--- Critique: Effective delivered dose and adherence diverge from trial conditions, and programmatic dose may be lower than the trial dose, notably with rifapentine regimens ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION (CG): Effective delivered dose and adherence diverge from trial conditions, with a rifapentine dose-transfer concern

**EXISTING COVERAGE:**
1. **Dose selection under rifamycin co-treatment is the stated purpose of the grant.** The CEA describes the Phase IIc trial as testing "dosing strategies for survival, infection clearance and lung damage." The critique itself concedes that "dose selection in Phase IIc already has to account for" the rifamycin interaction.
2. **The 10% relative reduction is conditional on a positive result.** That result would come from patients taking atorvastatin alongside standard TB therapy. If the trial population is on rifamycin-based regimens, the interaction is already embedded in the effect size and the chosen dose. I cannot confirm the trial's regimen composition from the CG text, so this holds conditionally.
3. **The 60% uptake is a loose aggregate, not a precise adherence-free ceiling.** CG says 60% of adult patients "would add atorvastatin if it works." That is a coarse judgment of real-world willingness, and it plausibly already discounts for friction. I cannot ground how CG derived it.
4. **The 40% p_success applies to the whole chain.** The Phase II and III success probability covers dose-finding failure, including failure to find a dose that works despite rifamycin induction. A sizeable share of the interaction risk is therefore already priced in on the success side. I cannot say how much.
5. **The parameter map is clear that CG does not model adherence or the rifampicin interaction explicitly.** My defense is partial for that reason.

**EVIDENCE WEAKNESSES:**
1. **The 70% adherence figure is a framing assumption.** The critique says so itself, and TB-specific adherence evidence is UNGROUNDED. The 0.60→0.42 arithmetic is correct, but it illustrates a hypothetical rather than measuring anything.
2. **The only interaction data cited is for pravastatin.** It showed AUC at 50% or less in five of ten subjects on rifampicin. That is a small sample and a different statin. Pravastatin is not primarily a CYP3A4 substrate, so it does not directly quantify the atorvastatin problem. The critique concedes that statin choice changes the size of the problem.
3. **The rifapentine magnitude is UNGROUNDED, and the critique downgrades this part to low strength.** The cited induction level (~85–100% of rifampicin for daily dosing) implies the interaction is not worse than with rifampicin. By the critique's own account, the HPMZ-specific argument is weak.
4. **The critique does not show that interaction-driven exposure loss translates into lost mortality benefit.** It cites no evidence of a dose-response relationship for atorvastatin's effect on TB mortality. If the effect plateaus, partial exposure loss costs less than proportionally. This is conditional, and I have no source for a plateau.
5. **Statin adherence is mostly studied in long-term chronic prevention.** I could not ground the adherence literature, and the verifier's quota ran out before checking it. A months-long adjunct taken during supervised TB treatment is a different setting, so extrapolating chronic-use adherence is a weak basis.
6. **The sensitivity results are empty (`{}`).** The "near the materiality threshold" claim rests on the single illustrative 30% reduction, not on a computed sensitivity.

**MAGNITUDE CHALLENGE:**
1. **Adherence reduction.** If SROI scales linearly with effective uptake, 70% adherence takes ~3,000x to ~2,100x. That sits at the ~2,000x bar and does not clearly cross it. Because 70% is an assumption, any higher adherence figure puts the result inside the ±25% band.
2. **Double-counting risk.** If the 10% relative reduction comes from a trial with imperfect adherence, applying a full adherence haircut on top counts the same loss twice. The critique does not separate the two.
3. **Rifapentine and HPMZ.** The critique says this affects "only the share of patients on HPMZ, which is currently small." Its aggregate effect on SROI is therefore bounded by that share. I cannot ground the current HPMZ share, and the verifier flagged HPMZ uptake as unverified.
4. **Post-treatment persistence of induction.** This matters only if statin dosing continues after TB therapy ends. Nothing in the CG text indicates that.

**OFFSETTING FACTORS:**
1. **Atorvastatin is cheap and generic.** If interaction lowers exposure, dose escalation or a different statin is a low-cost fix. This is plausible but untested here, and the trial is designed to explore dosing.
2. **Several benefit channels are currently set to zero.** The parameter map lists morbidity DALYs, post-treatment mortality, transmission averted, and diagnostic value. Any positive contribution offsets an adherence-driven loss in mortality benefit.
3. **The 60% uptake is applied to all 5.5 million eligible people.** The map notes that "adult" is not consistently handled, and that cuts the other way (downward), so I do not count it as an offset.

**OVERALL ASSESSMENT:** Partial defense.
- The dose-transfer component is well defended. The Phase IIc design targets dosing, p_success already prices in dose-finding failure, and the rifapentine element rests on ungrounded magnitude and an interaction no worse than rifampicin's.
- The adherence component is only weakly defended. CG's BOTEC does not model adherence, and the 60% uptake figure has no stated derivation. My counterarguments (a coarse figure that may already net out friction, possible double-counting, a possible dose-response plateau) are conditional and unsourced.

**CONCESSIONS:**
1. CG does not explicitly model adherence or delivered dose. The parameter map confirms "No adherence" and "No consideration of rifampicin-induced reduction in statin exposure."
2. Rifamycin interaction with atorvastatin is real and variable between patients, so the dose-transfer concern is a legitimate risk even if its size is unquantified.
3. Real-world adherence to an adjunct outside a fixed-dose combination plausibly falls below trial adherence. The direction is downward, though the magnitude is unknown.
4. The rifapentine-specific point should be treated as low strength, as the critique itself says.

### Challenger
REBUTTAL: Effective delivered dose and adherence diverge from trial conditions, with a rifapentine dose-transfer concern

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: Phase IIc exists to find a dose under rifamycin co-treatment, so the interaction is embedded in the 10% effect size and the chosen dose.

- This defends the trial, not the programme. A dose found under trial conditions is the dose delivered under trial adherence.
- The Advocate says it "cannot confirm the trial's regimen composition." The coverage claim is therefore conditional on an unverified premise.
- Even if the trial is rifamycin-based, it embeds the interaction only for the regimen studied. The critique's dose-transfer point is that the programmatic regimen mix (HRZE, HPMZ, intermittent vs daily rifamycin) may differ from the trial's.
- The Advocate itself concedes that CG explicitly models neither adherence nor the interaction (concession 1).

> The Advocate claims: The 60% uptake is a coarse aggregate that plausibly already discounts for friction.

- The Advocate admits it "cannot ground how CG derived it." This is a possibility, not a defense.
- The CEA wording the Advocate quotes is that 60% of patients "would add atorvastatin if it works." That describes willingness to add the drug. It does not describe sustained pill-taking over months.
- Reading it as already netting out adherence requires an assumption the text does not support. The parameter map's "No adherence" cuts against it.

> The Advocate claims: The 40% p_success already prices in dose-finding failure, so much of the interaction risk is on the success side.

- This conflates two events. p_success prices the probability that the trial gate is passed.
- The critique concerns what happens conditional on success: a dose that works in trial erodes in delivery. That is post-gate attrition, and p_success cannot price it.
- The Advocate says "I cannot say how much" is priced in. That is an admission of no quantified coverage.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: The pravastatin data is small and a different statin, so it does not quantify the atorvastatin problem.

- Conceded. Ten subjects and a different statin cannot size the atorvastatin effect, and the critique already says statin choice changes the magnitude.
- The verifier's evidence item is broader than pravastatin, though. It says the rifamycin-driven statin exposure reduction is "large and variable between patients" even in HRZE regimens.
- The Advocate's objection answers the supporting data point, not the general interaction finding. The Advocate concedes the interaction is real (concession 2).

> The Advocate claims: There is no evidence that exposure loss translates into lost mortality benefit, and a plateau is possible.

- The Advocate has "no source for a plateau." This is a conditional with no evidence, and it is symmetric: nothing grounds a plateau, and nothing grounds linearity either.
- The 10% effect is attached to the exposure achieved in the trial. Any delivered exposure below that moves away from the only exposure with an attributed effect.
- A plateau would help only if the trial dose sits well above the plateau. The Advocate offers nothing on that.

> The Advocate claims: Chronic statin adherence literature is a weak basis for a months-long adjunct taken during supervised TB treatment.

- The verifier marked the statin adherence literature as unverified because the search quota ran out. It was not refuted, and the Advocate should not treat it as absent.
- The Advocate asserts the adjunct is taken under supervision. The evidence package does not show this. Supervision of the FDC does not necessarily extend to a separate add-on pill, which is the critique's premise.
- The TB-specific adherence evidence is ungrounded in both directions.

> The Advocate claims: Sensitivity results are empty, so "near materiality" rests on one illustrative 30% cut.

- Conceded. The 0.60→0.42 arithmetic is illustrative, not computed from the model.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: 70% adherence takes ~3,000x to ~2,100x, which does not clearly cross the ~2,000x bar.

- Using the Advocate's own figures, the break-even is 2,000/3,000 ≈ 67% adherence. That is three points below the illustrative 70%.
- A single further 5% loss in the fraction achieving effective exposure, the second factor in the critique's mechanism, gives 0.70 × 0.95 = 0.665, or about 1,995x. This crosses the bar.
- The result sits on the threshold, not safely inside the ±25% band.
- Any adherence figure below 67% crosses it. The Advocate's "any higher figure" argument is one-sided.
- The Advocate does not address that the critique's mechanism has two factors, adherence and effective exposure, not just one.

> The Advocate claims: Applying a full adherence haircut on top of trial-derived effect size double counts.

- Partly conceded. The correct haircut is programmatic adherence relative to trial adherence, so the absolute 0.70 overstates the gap if trial adherence was below 100%.
- The Advocate concedes that real-world adherence "plausibly falls below trial adherence" (concession 3), so the gap is not zero.
- I cannot ground its size. This is an uninformed prior, not a derived estimate.

> The Advocate claims: The rifapentine effect is bounded by the HPMZ share, and post-treatment persistence matters only if dosing continues.

- Both are conceded. This part of the critique is already rated low, and nothing in the CG text indicates statin continuation after TB therapy.
- The critique's surviving weight is on adherence and general rifamycin dose transfer.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: Cheap generic atorvastatin means dose escalation or a different statin is a low-cost fix.

- The Advocate calls this "plausible but untested." Dose escalation is a trial outcome, so it depends on the same p_success the Advocate already cited.
- Escalation addresses the exposure factor but not adherence.
- I cannot ground the safety or pill-burden trade-offs of escalation. I flag only that the Advocate has not shown the model captures any escalation cost.

> The Advocate claims: Benefit channels currently set to zero (morbidity DALYs, post-treatment mortality, transmission averted, diagnostic value) offset an adherence-driven mortality loss.

- These channels are zero in the model, so they cannot offset a loss in the computed result. They are unmodeled upside.
- Most of them require the patient to actually take the drug, so they are exposed to the same adherence and exposure erosion. They are not independent offsets. I cannot ground that for the diagnostic channel.

**KEY UNRESOLVED QUESTIONS:**
- What adherence did the trial achieve, and what regimen mix did it use? This determines both double-counting and dose transfer.
- Does "60% would add atorvastatin" mean prescription uptake, or sustained use?
- Is atorvastatin's mortality effect dose-responsive in the exposure range that rifamycins produce?
- Is the add-on pill supervised under DOT, or is it outside the FDC and self-administered?
- What is the current and projected HPMZ share, and is rifapentine dosed daily or intermittently in it?

### Judge Audit
Surviving strength: moderate
Justification: The Challenger made two grounded moves the Advocate could not answer:
- p_success does not price post-success delivery erosion.
- "Would add" describes willingness, not adherence.
Together with the Advocate's concessions, these leave a directionally valid, unmodeled downward adjustment. However, the quantitative materiality claim did not survive. The 70% figure is admitted to be illustrative. The Challenger conceded it overstates the relevant (relative) gap. The Challenger's push past the threshold relied on a fabricated 5% factor. The rifapentine component is effectively reduced to a generic regimen-transfer point.
Recommended action: 1. CONCLUDE NOW (moderate confidence):
   - The adherence/delivered-dose concern is a valid omission in the CEA, but its magnitude is unknown and probably smaller than the illustrative 30%, because the relevant gap is programmatic versus trial adherence.
   - The rifapentine-specific claim should be dropped and folded into a general note that the selected dose may not transfer across rifamycin regimens.
   - The CEA should carry an explicit relative-adherence sensitivity parameter rather than an implicit 100%.

2. SPECIFIC INVESTIGATION (feasible): Pull the Phase IIc protocol from the source materials the verifier could not access. Check:
   - backbone regimen(s), including whether HPMZ is included and whether rifapentine is dosed daily;
   - statin course duration;
   - whether the statin is DOT-administered;
   - how trial adherence is measured.

   Separately, ask CG how the 60% uptake was derived. These are document lookups, not new research, and they would settle the double-counting and dose-transfer questions.
Action feasibility: requires_specified_evidence
Advocate failures: ['sound_synthesis_noted: If SROI scales linearly with effective uptake, 70% adherence takes ~3,000x to ~2,100x." The linearity assumption is stated, the arithmetic follows from the critique\'s own 0.60→0.42, and the result is compared to the ~2,000x bar. This is a legitimate synthesis, and the Challenger engaged with it.', 'sound_synthesis_noted: The double-counting argument says the correct haircut is programmatic adherence *relative to* trial adherence, not an absolute 70%. This is a valid structural correction. The Challenger conceded it, and it is the most important analytic move in the debate.', 'false_definitiveness: A sizeable share of the interaction risk is therefore already priced in on the success side. I cannot say how much." This asserts "sizeable" and disclaims any magnitude in the same breath. The Challenger also showed that p_success mostly prices gate failure, not post-gate delivery erosion.', 'call_to_ignorance: [The 60% uptake] plausibly already discounts for friction." The Advocate admits it "cannot ground how CG derived it." This is offered as coverage when it is only the absence of evidence against it. The plateau argument is better flagged ("no source for a plateau"), but it still functions as a speculative defense.', 'call_to_ignorance: The offsetting factor that "any positive contribution" from zeroed benefit channels offsets the adherence loss. These channels are unquantified and, as the Challenger noted, mostly share the same adherence exposure.', 'strawmanning: The defense refers to "a months-long adjunct taken during supervised TB treatment." The evidence package does not establish that the add-on is supervised. The critique\'s premise is specifically that it sits outside the FDC.']
Challenger failures: ["sound_synthesis_noted: The break-even of 2,000/3,000 ≈ 67% adherence comes directly from the Advocate's figures. This is valid and correctly shows the 70% case sits on the threshold, not comfortably inside the band.", 'unsupported_estimate_counter: A single further 5% loss in the fraction achieving effective exposure... gives 0.70 × 0.95 = 0.665, or about 1,995x. This crosses the bar." The 5% has no source or derivation. It was chosen to push the result just past 2,000x and counter the Advocate\'s "does not clearly cross" claim.', 'false_definitiveness: The Challenger concedes "the absolute 0.70 overstates the gap if trial adherence was below 100%," calling it "an uninformed prior." It still asserts "The result sits on the threshold, not safely inside the ±25% band." Once the haircut is conceded to be overstated, the 70% threshold case no longer supports a confident threshold-crossing claim.', 'strawmanning: The verifier marked the statin adherence literature as unverified... The Advocate should not treat it as absent." The Advocate explicitly said "I could not ground the adherence literature, and the verifier\'s quota ran out." It did not treat the literature as absent. Its actual argument concerned the relevance of chronic-use adherence data to a short adjunct, and the Challenger did not address that.']
Debate resolved: Both sides agree on four points:
- CG models neither adherence nor the rifamycin–statin interaction.
- The rifapentine/HPMZ component is low strength, because HPMZ is not worse than HRZE at daily dosing and is bounded by an unverified HPMZ share.
- The correct adherence adjustment is relative to trial adherence, not absolute.
- Under linear scaling, the critique's illustrative 70% figure puts the result roughly at the ~2,000x bar (break-even ≈ 67%).
Debate unresolved: Four questions remain open:
- What adherence and regimen mix the Phase IIc trial uses. This determines both the size of the relative adherence gap and whether dose transfer across regimens is a real issue.
- Whether CG's 60% means initial uptake or sustained use.
- Whether the add-on pill is DOT-supervised.
- Whether atorvastatin's mortality effect is dose-responsive in the rifamycin-reduced exposure range.

--- Critique: Private-sector treatment share and the reach of national guidelines are not modeled ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: Private-sector treatment share and the reach of national guidelines are not modeled
```

**EXISTING COVERAGE:**

1. **The 60% uptake is already a large haircut, and CG does not say how it was built.** The BOTEC applies 60% to adult patients "if it works," which leaves 40% of patients unreached. Reduced reach in private or unnotified settings is one of several reasons for that gap (alongside contraindications, clinician hesitancy and adherence). The parameter map lists "no private-sector treatment share" as unmodeled, but a single blended figure can absorb it. I cannot ground the claim that CG consciously built it that way; this is inference from the structure.
2. **The base population is already limited to treated patients.** The 5.5M figure is derived using "the share of cases being treated stays constant." Patients who never enter any care, public or private, are already excluded. The critique therefore concerns only treated patients whose care sits outside the NTP, a narrower group than the headline "private share" suggests.
3. **The critique's own evidence undercuts the premise that the NTP is the delivery channel.** The 2025 analysis it cites reports that private-sector engagement models improved "TB notification and drug uptake" in India. Notified private patients are increasingly inside the programme, so the NTP-reach concern is shrinking for the largest-burden country.

**EVIDENCE WEAKNESSES:**

1. **The magnitude is self-declared ungrounded.** The 5–15% range is described as "inference, not sourced." No component evidence supports it, and no derivation chain connects the cited facts to it. The critique has not met its burden of proof on magnitude.
2. **The evidence measures notification, not regimen uptake.**
   - The older estimate (private notifications at about 22% of estimated cases treated in that sector across Bangladesh, India, Indonesia and Myanmar) measures completeness of reporting.
   - A patient can be unnotified and still receive any drug a private provider chooses to prescribe.
   - The critique itself concedes that sector-specific adherence is documented for diagnosis and management but "not clearly for regimen or dosing." The parameter at issue, adult_uptake of an add-on drug, has no direct evidence in the critique.
3. **The Mumbai finding points the other way.** The cited high use of adjunct tests and antibiotics by private providers is evidence that private providers readily add things to standard regimens. For an add-on generic, that is evidence for equal or higher uptake. It does not support a haircut.
4. **The dating and scope of the 22% figure are weak.** It is described as "older" and covers four countries. It does not describe the current notification environment, which the 2025 India analysis suggests is changing.
5. **The country-level support is uneven.** The critique concedes that the missing-case data fit Indonesia, the Philippines and Pakistan more than India. India has the largest share of global TB cases (my recollection of WHO Global TB Report figures; treat as unverified). The argument is weakest in the country that matters most for the global average.
6. **The critique's own strength rating is low-to-medium.** It describes the sign as uncertain, the direction as "probably down but could be neutral or positive," and the effect as "plausibly" modest.

**MAGNITUDE CHALLENGE:**

1. **Even the top of the critique's range is below the materiality threshold.** The context sets decision-relevance at roughly a 25% change in SROI. A 15% reduction in uptake scales SROI linearly, since uptake enters multiplicatively: 3,000 × 0.85 ≈ 2,550. The bottom of the range (5%) gives about 2,850. The critique's own range therefore does not cross the stated materiality line. The Sensitivity Results field is empty, so no run contradicts this.
2. **The 60% figure is itself a round-number judgment with wide uncertainty.** A 5–15% relative adjustment, equivalent to moving 60% to about 51–57%, is well inside the noise of the base estimate. An unsourced adjustment of this size to an unsourced parameter does not clearly improve accuracy.
3. **The sign is genuinely ambiguous.** The Quantifier says "the sign could flip in specific countries." A symmetric-uncertainty adjustment centered near zero is the null hypothesis, and the critique has not shown that the center sits below zero.

**OFFSETTING FACTORS:**

1. **Private patients pay out of pocket, and the drug is cheap.** CG's uptake rationale is that atorvastatin is generic and cheap. That rationale does not depend on NTP procurement reaching the patient. Whether private pharmacies stock and sell it is an empirical question I cannot ground, but the critique's "NTP procurement doesn't reach them" premise has limited force for a cheap generic.
2. **Private prescribers' documented willingness to add adjuncts** (the Mumbai study the critique cites) is a positive offset to any dosing-quality concern.
3. **A positive trial result is what would trigger private-sector adoption.** If private providers adopt faster than the NTP once evidence exists, uptake in that segment could exceed the public-sector rate. This is conditional reasoning, not an attested finding.
4. **Dosing quality may matter less than the critique implies.** The grant's Phase IIc trial tests dosing strategies, so a defined effective dose is a product of the trial. Whether private-sector non-standard dosing meaningfully reduces mortality benefit is unknown. I cannot ground a magnitude and treat it as an uninformed prior.

**OVERALL ASSESSMENT:** **Strong defense**, with modest caveats.

- The critique is ungrounded in magnitude and ambiguous in sign. Its direct evidence is about notification, not regimen uptake.
- Its own supporting and undermining evidence roughly offset.
- Its stated range falls below the materiality threshold.
- The residual weakness is real: CG gives no sector breakdown or reference for the 60%, and the counterfactual-speedup channel is unexamined.

**CONCESSIONS:**

1. CG does not decompose the 60% uptake by sector, and no empirical precedent is given for it. The parameter map's "no private-sector treatment share" is accurate as a description of the BOTEC.
2. If private providers would adopt a cheap statin for TB before national guidelines change, the 1-year speedup credited to the grant could shrink. This acts on speedup_years rather than adult_uptake. The critique flags it but does not quantify it, and I cannot quantify it either.
3. For Indonesia, the Philippines and Pakistan, the missing-case evidence is directionally supportive of a downward adjustment. I accept this arguendo, but those countries carry less weight in the global average than India.
4. The 22% notification figure shows that unnotified private care persists in some high-burden countries. That is a legitimate reason to treat the 60% as an upper-middle estimate for those settings.

### Challenger
REBUTTAL: Private-sector treatment share and the reach of national guidelines are not modeled

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the 60% uptake figure is already a large haircut, so a blended number can absorb private-sector reach without a separate adjustment.

- **The Advocate concedes this is inference.** They say they "cannot ground the claim that CG consciously built it that way." A parameter that could contain the adjustment is not evidence that it does.
- **The defense is internally strained.** Under Coverage, the 60% is a cushion that absorbs sector effects. Under Magnitude, it is "a round-number judgment" whose noise swamps a 5–15% adjustment. If it is that unspecified, nobody can confirm the private-sector concern was priced in. That unverifiability is the critique's point, and the Advocate's own concession 1 accepts that the BOTEC has no sector breakdown.

> The Advocate claims: the base population (5.5M) already excludes patients who never reach care, so the concern is limited to treated patients outside the NTP.

- **Conceded in part.** The never-treated are out of scope.
- **The remaining group is still large.** Treated patients outside the NTP are the group the critique is about. The critique reports India's private notifications at about 30–33% of the total, and more than half of patients first seek care privately.
- **Unnotified private patients plausibly stay in the "treated" base.** The older estimate shows private notification at 22% of estimated cases treated in that sector. That means most private-sector treated patients were not captured by notification, but they are still treated patients. Nothing in the Advocate's argument shows the 5.5M base excludes them.

> The Advocate claims: the 2025 India analysis shows notified private patients are increasingly inside the programme, so NTP-reach concerns are shrinking.

- **The cited phrase is thin.** It says engagement models improved "TB notification and drug uptake." The package gives no level, no baseline and no definition of "drug uptake." It most plausibly refers to anti-TB drugs, not an add-on.
- **A trend is not a level.** "Improved" does not show that the gap closed. If the 22% figure is outdated, the package supplies no current figure, so the Advocate cannot conclude the residual is small.
- **The package marks this evidence as "undermining or complicating," not rejecting.** It narrows the critique but does not remove it.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the evidence measures notification, not regimen uptake, and the critique concedes there is no direct evidence on regimen or dosing.

- **Conceded.** The critique says sector adherence is documented for diagnosis and management, not clearly for regimen or dosing. No direct evidence on add-on uptake is on the table.
- **That gap does not favor the null.** It is symmetric ignorance. The Advocate treats the lack of regimen-level data as grounds to leave the 60% alone. It equally supports not assuming the private sector matches the public sector.

> The Advocate claims: the Mumbai finding, high private use of adjunct tests and antibiotics, points toward equal or higher uptake of an add-on.

- **The finding does not support that inference.**
  - Chest X-rays are tests, not add-on drugs.
  - Antibiotic use there is evidence of non-standard prescribing. It shows private providers add things readily, but not that they do so consistently, at a defined dose, for a defined duration.
- **The critique's mechanism turns on dosing and duration.** Unsupervised, non-standard dosing lowers benefit even when the drug is prescribed. High propensity to prescribe and low fidelity of exposure are compatible, and the Mumbai finding speaks only to the first.
- **I concede the sign ambiguity.** The critique itself labeled this sign-ambiguous. The Advocate's step from ambiguous to "evidence for equal or higher uptake" overreaches in the other direction.

> The Advocate claims: the 22% figure is old and covers four countries.

- **Conceded on dating.** But the 22% implies about 78% of private-sector treatment went unnotified. Even if the current figure is double, most private treatment would remain outside notification, and the 2025 analysis gives no number showing otherwise.

> The Advocate claims: the argument is weakest in India, the highest-burden country.

- **Partly fair, but the critique already says so.** India still has a 30–33% private notification share and a majority private first-contact rate. The weaker evidence for India concerns missing-case data, not the existence of the private channel.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: even 15% is below the roughly 25% materiality threshold, since uptake enters multiplicatively (3,000 × 0.85 ≈ 2,550).

- **The arithmetic is conceded.** A uniform 5–15% uptake cut gives a proportional SROI cut.
- **A single critique's range is not the relevant comparison if the adjustment is directional and systematic.** I do not know how this adjustment interacts with others in the review, and I will not assert a stack. But "below threshold alone" is not "immaterial in aggregate."
- **The magnitude is ungrounded.** The critique says so itself. I can show only what the 5–15% would require, not that it is correct.
  - Take India's private share at about 31% of notifications (midpoint of the critique's 30–33%). A 5% aggregate cut requires private effective uptake to be about 0.05 / 0.31 ≈ 16% lower than public. A 15% aggregate cut requires about 0.15 / 0.31 ≈ 48% lower.
  - The low end needs only a modest private-sector quality gap. The high end is aggressive.
  - This is a plausibility check on the critique's range, not an independent estimate. It also ignores unnotified private patients, who would raise the effective private share.
- **The "symmetric uncertainty centered on zero" claim does not hold.** The Advocate concedes directional support for a downward adjustment in Indonesia, the Philippines and Pakistan. The critique's mechanism, non-standard dosing and unsupervised exposure, is one-directional for effective exposure. The upside channel works mainly through prescribing propensity and adoption timing, which the Advocate concedes acts on speedup_years, not adult_uptake. The sign is uncertain in some countries, but the center is not demonstrably zero.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: private patients pay out of pocket, the drug is cheap, so NTP procurement matters less.

- **The Advocate says this cannot be grounded.** It is a conditional, not an offset.
- **A cheap drug does not create uptake.** Uptake needs a prescriber to prescribe it, and in a setting with no guideline change that prescriber needs a reason to. Cost is only one barrier. Out-of-pocket payment is also a possible barrier that NTP free provision removes. The package has no evidence on either side.

> The Advocate claims: private providers' willingness to add adjuncts is a positive offset.

- **Already addressed above.** It is test and antibiotic evidence, not evidence on a statin add-on or its dosing.

> The Advocate claims: a positive trial result would trigger private adoption, potentially exceeding the public rate.

- **This sits in tension with concession 2.** If private adoption is triggered by the trial, it is attributable to the grant and could raise uptake. If private adoption would happen independent of the trial or of guidelines, it shrinks speedup_years and the counterfactual value. The Advocate counts the first as an offset and concedes the second, but does not net them. Faster private adoption is therefore not clearly an offset for this grant's SROI.
- **It is hypothetical.** The Advocate labels it "conditional reasoning, not an attested finding," and it is not in GiveWell's model.

> The Advocate claims: the trial defines an effective dose, so dosing quality may matter less.

- **A defined dose is not delivered exposure.** The critique's concern is whether private-sector dosing follows the defined dose. The Advocate calls this an uninformed prior, which is not an offset.

**KEY UNRESOLVED QUESTIONS:**

- What share of the 5.5M treated base is private and unnotified? Does the base include them, or only notified cases?
- What does "drug uptake" mean in the 2025 India analysis: anti-TB drug uptake or something else? What is the current private notification rate?
- Does private-sector prescribing of an add-on in TB patients, conditional on a positive trial, run at a lower, equal or higher fidelity than public-sector prescribing? No regimen- or dosing-level evidence has been presented.
- Is faster private adoption attributable to the trial, which raises uptake, or independent of it, which shortens speedup_years? These push in opposite directions and the Advocate has not netted them.
- Did CG fold private-sector reach into the 60% judgment, and was the 60% anchored to public-sector delivery?

### Judge Audit
Surviving strength: weak
Justification: The debate was largely substantive, with sound syntheses on both sides. Those syntheses establish that the critique's own range is below the materiality threshold, and the Challenger conceded the arithmetic. The Challenger's surviving points have three weaknesses:
- The unverifiability of the 60% is a documentation critique, not a magnitude one.
- The appeal to unspecified aggregation is a call to ignorance.
- The claim that the effect is not centered at zero relies on a dosing mechanism the only regimen-level evidence partly contradicts, and on a strawmanned reading of Concession 2.
The critique survives as a valid qualitative caveat, namely that CG gives no sector decomposition. It does not survive as a decision-relevant quantitative adjustment.
Recommended action: 1. CONCLUDE NOW: Do not adjust adult_uptake for private-sector reach. The critique's own upper bound (15%) is below materiality, its sign is ambiguous, and the only regimen-level evidence (over three-quarters of private providers prescribing ISTC-consistent regimens) weakens the dosing-fidelity mechanism. Record it as a qualitative caveat that the 60% has no sector basis. Separately flag the speedup_years channel (private adoption before guidelines) as an unquantified downside, since that channel was conceded but is distinct from this critique. Confidence: moderate-high that this critique alone is not decision-relevant.

   One low-cost follow-up would close the main structural question: check CG's BOTEC documentation for whether the 5.5M base is derived from notified cases or from estimated treated incidence. This is feasible from existing materials.
Action feasibility: actionable_now
Advocate failures: ['misrepresenting_evidence_status: Under Evidence Weakness 1, the Advocate says of the 5–15% range that "No component evidence supports it, and no derivation chain connects the cited facts to it." The second half is fair, since the critique offered no derivation. The first half overstates. The verifier package does contain usable components:', 'false_definitiveness: The Advocate says the Mumbai adjunct-test and antibiotic finding "is evidence for equal or higher uptake. It does not support a haircut." The verifier filed this finding under "sign ambiguity." The chain from "private providers order chest X-rays and prescribe antibiotics" to "private providers will adopt a statin add-on at equal or higher effective uptake" has a clear gap: X-rays are tests, not drugs. The Advocate turned ambiguous evidence into a confident directional claim.', 'false_definitiveness: The Advocate calls "a symmetric-uncertainty adjustment centered near zero" the null hypothesis. The Advocate then concedes, in Concession 3, that the missing-case evidence for Indonesia, the Philippines and Pakistan is "directionally supportive of a downward adjustment." These two positions are inconsistent. The center cannot be asserted as zero while directional evidence is conceded for several high-burden countries.', 'call_to_ignorance: Under Coverage 1, the Advocate says "a single blended figure can absorb it," meaning the 60% might already contain the private-sector haircut. The Advocate honestly labels this as inference, which softens the failure. Still, the argument amounts to "the 60% might already include this because we don\'t know that it doesn\'t." The Advocate also undercuts it later by calling the 60% an unanchored round number.', 'sound_synthesis_noted: The materiality arithmetic is sound and was conceded by the Challenger:']
Challenger failures: ['strawmanning: The Challenger says "the upside channel works mainly through prescribing propensity and adoption timing, which the Advocate concedes acts on speedup_years, not adult_uptake." The Advocate\'s Concession 2 covered only adoption that happens *before guidelines change* or independently of the trial, and its effect on the speedup. Prescribing propensity, meaning willingness to add adjuncts, is an uptake channel. The Challenger folded both into the speedup concession, which wrongly removes the upward-uptake channel from the adult_uptake question.', 'call_to_ignorance: The Challenger says "\'Below threshold alone\' is not \'immaterial in aggregate.\'" The Challenger does disclaim asserting any stack of adjustments. Even so, the point offers possible interaction with unspecified other adjustments as a reason to doubt immateriality, with no evidence. It amounts to "this might matter in aggregate because we don\'t know that it doesn\'t.', 'call_to_ignorance: The Challenger calls the dosing mechanism "one-directional for effective exposure." That is true conditional on the mechanism operating. However, the Challenger treats the mechanism\'s existence as given, when the only regimen evidence in the package (over three-quarters ISTC-consistent) cuts against it. The Challenger asserts the mechanism without ever engaging that finding.', "sound_synthesis_noted: The Challenger's plausibility check is a transparent, correctly labeled synthesis from verifier components:", 'sound_synthesis_noted: The Challenger correctly rebuts the Mumbai inference: tests are not drugs, and prescribing propensity is not the same as dosing fidelity. The Challenger also correctly identifies that the Advocate did not net the trial-triggered adoption offset against Concession 2.']
Debate resolved: Both sides accept the arithmetic: even the top of the critique's own 5–15% range moves SROI from about 3,000 to about 2,550, below the roughly 25% materiality threshold. Both sides also agree that the evidence on the table concerns notification and diagnostic management, not add-on regimen uptake or dosing. Neither the Mumbai finding nor the notification data establishes the sign of the effect on adult_uptake.
Debate unresolved: Two questions remain open:
- **Where the effect is centered.** The Advocate says zero; the Challenger says modestly negative. Neither side engaged the ISTC-consistency evidence that bears directly on this.
- **What the 5.5M treated base contains.** It is unclear whether the base includes unnotified private patients, which determines how large the at-risk segment is.

A separate, unquantified question is whether private adoption independent of the trial erodes speedup_years.

--- Critique: Zero modeled lag between Phase III completion and adoption, and a speedup that assumes trial timing is the binding constraint ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION: Zero modeled lag between Phase III completion and adoption, and a speedup that assumes trial timing is the binding constraint

**EXISTING COVERAGE:**
- **Lag simplification.** The BOTEC sets Phase III completion at 8 years and applies the eligible-case count at that point. It also assumes the treated share stays constant and that 60% of adult patients adopt "if it works." Zero lag is therefore a stated simplification, not a hidden error.
- **Guideline step.** The critique's own evidence supports treating the guideline step as near-instant. WHO issued its rapid communication about a month after the May 2021 NEJM publication of Study 31/A5349. That is evidence for CG's near-zero lag on this step, not against it.
- **Downstream access lag.** The HPMZ constraint was drug cost and availability. The CG model addresses this through the "generic and cheap" justification for 60% uptake. That justification speaks directly to the access barrier the critique raises.
- **Speedup is a judgment, not a mechanical output.** The 1-year figure is an assumption, and the BOTEC does not say whether it is a best case or an expected value. I can't determine which from the text, so I don't claim it already nets out the "trial not on critical path" scenario.

**EVIDENCE WEAKNESSES:**
- **The central claim is ungrounded.** The critique says the "not on the critical path" piece is the more important one and that it is ungrounded. It calls Phase III funding for a generic "plausible but ungrounded" and the Xpert precedent "unverified." The claim therefore rests on conjecture.
- **HPMZ is a weak analogy for access.**
  - The critique cites drug cost and availability as the binding constraint for HPMZ.
  - Atorvastatin is, per the CG text, a generic and cheap drug. The HPMZ access bottleneck is the very factor that differs most.
  - So the HPMZ precedent transfers poorly to the access-lag question.
- **No sensitivity result.** The Quantifier's sensitivity results are empty. The critique asserts materiality without a computed parameter impact.
- **Mixed evidence.** The HPMZ evidence cuts both ways. It shows the guideline step is fast, which supports CG's lag assumption. It shows access lag is real, which supports the critique only if the same barriers apply to a generic.
- **The Study 31 endorsement point is context only.** The critique itself describes it as context. It adds no weight to the speedup argument.

**MAGNITUDE CHALLENGE:**
- **The lag piece is not decision-relevant on its own.** The critique concedes that ~2%/yr decline means 3–5 years of lag lowers benefits ~6–10%. Applied to the 3,000x estimate, that gives roughly 2,700–2,820x, still above the 2,000x bar and below the ~25% materiality threshold.
- **Discounting is a separate thread.**
  - The CEA applies no time discounting, which Thread 3 covers.
  - As a rough illustration, at 3–5% a 5-year lag gives factors of 1/1.03^5 ≈ 0.86 and 1/1.05^5 ≈ 0.78, so a 14–22% reduction.
  - Combined with the ~10% decline effect, this could approach or cross the 25% line. I concede that interaction.
  - It belongs to the discounting critique, not to a distinct finding about lag.
- **Speedup has a break-even.**
  - SROI is linear in speedup_years.
  - Break-even against the 2,000x bar is 2,000/3,000 ≈ 0.67 years.
  - If the trial is not on the critical path with probability p (speedup 0) and otherwise gives 1 year, expected speedup is 1−p, so break-even p ≈ 33%.
  - That is a real threshold, but the critique offers no grounded estimate of p.
  - The lag-cost arithmetic also depends on the unverified formula, as the critique admits.
- **The critique's low-to-medium strength rating is fair.** The critique rates itself low-to-medium. I agree it has not met a burden of proof for moving the estimate.

**OFFSETTING FACTORS:**
- **Possible upside from a generic with no sponsor.**
  - The CG text describes atorvastatin as generic and cheap.
  - It is my inference, not a sourced fact, that generics typically lack a commercial sponsor for Phase III. If so, the Phase IIc result may be what unlocks Phase III funding, which makes the trial the critical path.
  - In that case the true counterfactual delay could exceed 1 year, and the 1-year speedup would be conservative.
  - This argument is ungrounded and no stronger than the critique's mirror-image claim.
  - It does show the speedup uncertainty is two-sided, so the critique's directional push downward is not established.
- **Discounting offsets the two-sided uncertainty only partly.** An upside scenario would also be partly eroded by the discounting concern above.
- **Cheap adoption supports the access assumption.** For a cheap generic, the HPMZ-style access barrier (drug cost and supply) is likely smaller. That reduces the expected access lag relative to the precedent the critique cites.

**OVERALL ASSESSMENT:** **Partial defense.**
- The lag component is not material alone, by the critique's own arithmetic. The HPMZ evidence mostly supports CG on the guideline step.
- The speedup component is genuinely vulnerable. CG gives no reasoning for the 1-year figure or for the trial being on the critical path.
- The critique has not grounded a lower speedup, but CG has not grounded 1 year either.
- The break-even is only a ~33% chance that the trial is non-binding. That is not a remote scenario.

**CONCESSIONS:**
- Zero adoption lag is an unjustified simplification, and a ramp-up of uptake over years is plausible. The CEA lacks the modeling to defend it.
- Combined with the missing discounting, a 3–5 year lag could plausibly reduce the estimate by around 20–30%. That lands near the materiality threshold, though the discounting rate is not set by this critique.
- The speedup_years assumption of 1 year is unsupported in CG's text. If the Phase III timeline is driven by factors other than Phase IIc results, expected speedup could fall below the ~0.67 break-even.
- I cannot ground a probability that the trial is or is not on the critical path. I treat any estimate of it, mine or the critique's, as an uninformed prior.

### Challenger
REBUTTAL: Zero modeled lag between Phase III completion and adoption, and a speedup that assumes trial timing is the binding constraint

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: zero lag is a stated simplification, and the 60% "adopt if it works" uptake, justified by the drug being generic and cheap, already addresses the access barrier the critique raises.

- **A level is not a timing.** The 60% figure sets the terminal share of adopters. It says nothing about how many years pass between Phase III completion and reaching that share. The Advocate has no answer to this, because the two assumptions measure different things.
- **"Generic and cheap" covers only part of the HPMZ constraint.** The Advocate reads the HPMZ constraint as cost. The evidence package says the delay lay in "downstream access," and the critique says "cost and availability."
  - Cheapness plausibly reduces the cost barrier.
  - I cannot ground whether it reduces supply, procurement, national guideline adoption, or clinician uptake lags. Treat that as an uninformed prior.
  - The Advocate's inference, "cheap, therefore short lag," is the same kind of ungrounded inference the Advocate faults in the critique.
- **The guideline-step point is conceded but incomplete.** WHO acting about a month after the NEJM publication is real evidence that the WHO step is near-instant.
  - It is also a single precedent.
  - A WHO rapid communication is not national adoption. The model's "adoption" is population-level, not a WHO announcement.
  - The Advocate's point supports zero lag at the WHO step only.
- **The Advocate's own admission on speedup.** The Advocate says it cannot tell whether 1 year is a best case or an expected value. So "existing coverage" cannot be claimed for the critical-path concern. The Advocate concedes this under "Overall Assessment."

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the "not on the critical path" claim is conjecture, HPMZ transfers poorly to a cheap generic, and the evidence is mixed.

- **Conceded: the verifier evidence cuts against the critique on one point.** It says "the delay lay in trial execution and rapid generation of results." That reads as the trial being on the critical path, which supports CG's speedup assumption.
  - What remains is that the evidence also lists downstream access as a delay.
  - Whether the access delay is independent of trial timing is not answered by the evidence.
- **Conceded: the critique's central claim is ungrounded.** The critique labels the Phase III funding gate "plausible but ungrounded" and the Xpert precedent "unverified." Those are UNVERIFIABLE, not REJECTED. The Advocate is right that they cannot move the estimate alone.
- **Conditional framing.** If Phase III funding or execution for a generic is independent of Phase IIc timing, then the speedup per year of acceleration is below 1. The Advocate's own derivation shows the consequence is linear and quantifiable.
- **"No sensitivity result" is answered by the Advocate's own break-even.** SROI is linear in speedup. Break-even against the 2,000x bar is 2,000/3,000 ≈ 0.67 years. Any combination of partial or zero speedup scenarios averaging below 0.67 breaks the bar.
  - The Advocate also notes this is not a 0-or-1 matter. A partial shortening of Phase III yields intermediate values that count toward the same expectation.
  - The empty Quantifier field does not mean the impact is small. The impact is derivable in one line.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: lag alone costs about 6–10% (roughly 2,700–2,820x), discounting belongs to a separate thread, and the speedup break-even requires a ~33% chance that the trial is non-binding, for which there is no grounded estimate.

- **Combined arithmetic from the Advocate's own numbers.**
  - Discount factors are 0.863 (3%) and 0.784 (5%) over 5 years.
  - The lag-decline factor is ~0.90.
  - Combined: 0.863 × 0.90 ≈ 0.777 and 0.784 × 0.90 ≈ 0.706.
  - Applied to 3,000x, this gives about 2,118–2,331x. That is still above 2,000x, but the margin is only 6–17%.
- **What the margin implies for speedup.** Under those combined adjustments, expected speedup must be at least 2,000/2,331 ≈ 0.86 to 2,000/2,118 ≈ 0.94 years.
  - The 0.67 break-even holds only in isolation.
  - With lag and discounting included, the tolerable shortfall in speedup shrinks to roughly 6–14%, which is a much smaller scenario probability than 33%.
  - Example: expected speedup of 0.8 with the 0.706 factor gives about 3,000 × 0.8 × 0.706 ≈ 1,694x.
- **"Discounting belongs to another thread" is bookkeeping.** The decision-relevant question is whether the estimate clears the bar, and it depends on the stacked adjustments. The Advocate concedes the stack lands near the materiality threshold.
- **Minimum plausible impact.** In isolation, the lag piece is about 6–10%. The critique itself called it modest.
- **The speedup piece is the only one that can matter alone.** The Advocate concedes that "CG gives no reasoning for the 1-year figure."

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: a generic with no sponsor might need the Phase IIc result to unlock Phase III funding, so the true speedup could exceed 1 year, making the uncertainty two-sided.

- **The Advocate labels this offset ungrounded.** It is an inference, not a sourced fact. It is not in the CG model and I cannot ground it either.
- **Two-sided uncertainty does not offset a point estimate with no basis.** The Advocate's mirror-image argument establishes only that the 1-year figure is unsupported in both directions.
  - With SROI linear in speedup, symmetric noise leaves the expected value unchanged.
  - It does raise the probability of falling below 2,000x, especially once lag and discounting have consumed most of the margin.
- **I do not claim the critique shows the direction is downward.** I claim the point estimate has no support and the buffer is thin.
- **The cheap-adoption offset is not in the model.** It is the "generic and cheap" argument for uptake level, and it does not address time to uptake (see above).
- **Discounting erodes the upside scenario too.** The Advocate concedes this.

**KEY UNRESOLVED QUESTIONS:**
- Is the CG 1-year speedup intended as a best case or an expected value? The Advocate cannot determine this from the text.
- Is Phase III timing for a generic statin gated by Phase IIc results (funding or sponsor), or does it proceed on an independent schedule? Neither side can ground this.
- How long does the post-WHO interval to national adoption and procurement take for a cheap generic? This is distinct from the WHO guideline step, and the HPMZ precedent does not quantify it for atorvastatin.
- Once discounting is set in Thread 3, how much of the roughly 6–17% margin over the 2,000x bar remains for speedup shortfalls?

### Judge Audit
Surviving strength: moderate
Justification: The debate did real analytical work. Both sides used sound, shared arithmetic: the linear SROI, the 0.67 break-even, and the stacked factors. The Challenger's extension, showing that lag plus discounting compresses the tolerable speedup shortfall, is a grounded and genuine contribution the Advocate did not anticipate.
However, the critique's "more important" claim, that the trial is not on the critical path, remains ungrounded. The only relevant verifier evidence leans against it. The Challenger's thin-margin conclusion also depends on worst-case lag assumptions and an unset discount rate.
The critique therefore survives as a valid sensitivity concern, not as a demonstrated downward adjustment.
Recommended action: 1. CONCLUDE NOW** (moderate-high confidence): Drop the lag component as a standalone finding. It is under 10% alone, and its interaction with discounting should be handled in Thread 3. Record that the 1-year speedup is an unsupported point estimate with a quantified break-even: about 0.67 years in isolation, and about 0.86–0.94 years if Thread 3 adopts 3–5% discounting and a 5-year lag is accepted.

**2. SPECIFIC INVESTIGATION** (feasible with existing tooling): Check whether a Phase III trial of adjunctive atorvastatin for TB is planned, funded, or registered, and whether funders condition it on Phase IIc results.
- Search trial registries such as ClinicalTrials.gov and ISRCTN.
- Search funder announcements from Unitaid, NIH/ACTG, and EDCTP.
- Separately, check whether CG intends the 1-year speedup as an expected value or a best case. Look in any accompanying grant writeup.

Either finding would directly resolve the critical-path question, which is the only part of the critique that can matter on its own.
Action feasibility: requires_specified_evidence
Advocate failures: ['sound_synthesis_noted: The break-even derivation is sound. SROI is linear in speedup, 2,000/3,000 ≈ 0.67 years, and with speedup 0 at probability p, expected speedup is 1−p, so break-even p ≈ 33%. Each step follows. This anchored the rest of the debate.', "sound_synthesis_noted: The lag-only arithmetic is correct. A 6–10% reduction gives about 2,700–2,820x. The discount factors 1/1.03^5 ≈ 0.86 and 1/1.05^5 ≈ 0.78 are also correct. Both are explicitly conditional on the critique's unverified 2%/yr formula.", 'unsupported_estimate_pseudo: The concession says "a 3–5 year lag could plausibly reduce the estimate by around 20–30%." That range uses 5-year factors only. At a 3-year lag and 3% discounting, the combined factor is about 0.915 × 0.94 ≈ 0.86, a reduction of roughly 14%, not 20%. The low end of the stated range does not follow from the Advocate\'s own inputs. This is minor, but it overstates the concession.']
Challenger failures: ["sound_synthesis_noted: The stacked arithmetic is correct. 0.863 × 0.90 ≈ 0.777 and 0.784 × 0.90 ≈ 0.706, giving 2,118–2,331x. The required speedup of 0.86–0.94 years is also correct. The point that the 0.67 break-even holds only in isolation is a legitimate and substantive extension of the Advocate's own derivation.", 'false_definitiveness: The Challenger says "the margin is only 6–17%" and "the tolerable shortfall in speedup shrinks to roughly 6–14%.', 'strawmanning (mild): The Challenger says "The Advocate has no answer to this" regarding level versus timing. The Advocate had already conceded that "zero adoption lag is an unjustified simplification" and that ramp-up is plausible. The Challenger rebuts a position the Advocate had largely abandoned. The substantive point, that 60% is a level and not a timing, is nonetheless correct.']
Debate resolved: Three things are settled.

1. **The lag component is immaterial on its own.** It costs about 6–10% conditional on the unverified formula, and the WHO guideline step is near-instant per the HPMZ precedent.
2. **The 1-year speedup is an unsupported point estimate in both directions.** Neither side grounded a probability that the trial is off the critical path. The only direct evidence (delay lay in trial execution) leans toward the trial being on it.
3. **The decision threshold is now explicit.** In isolation, expected speedup must stay above about 0.67 years. If stacked lag-plus-discounting adjustments are accepted, that rises to roughly 0.86–0.94 years.
Debate unresolved: - Whether Phase III timing for a generic statin is gated by Phase IIc results or runs on an independent schedule. Neither side could ground this.
- How long post-WHO national adoption takes for a cheap generic.
- Whether the thin stacked margin is real. It depends on the actual lag length and on the discount rate Thread 3 adopts. The Challenger's 6–17% figure reflects only the 5-year-lag case.

--- Critique: Survivors' excess mortality and comorbidity shrink the 27 DALYs per death ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: Survivors' excess mortality and comorbidity shrink the 27 DALYs per death
```

**EXISTING COVERAGE:**

- CG describes the 27 as "remaining healthy life expectancy," not raw life expectancy. A healthy-life measure already discounts remaining years for morbidity. The critique's concern (survivors are sicker than average) partly overlaps with what HALE is meant to capture.
- I cannot show how 27 was derived, and neither can the critique. The Parameter Map confirms CG gives no explicit adjustment for survivors' excess mortality. So I do not claim explicit coverage.
- My inference is that 27 is not a frontier-style reference life table value. The critique itself puts LMIC remaining life expectancy at age 40 in the "low-to-mid 30s." A healthy-life figure of 27 sits about 10–20% below that. This is consistent with 27 already being a country-level, health-adjusted number. It is an inference from the critique's own figures, not a verified fact.
- The BOTEC also leaves several benefit channels at zero. These include morbidity and lung-damage DALYs, transmission averted, and diagnostic value (Parameter Map: "only mortality is valued"). That is a structural cushion against modest downward revisions to dalys_per_death.

**EVIDENCE WEAKNESSES:**

- **The 20–30% figure is explicitly the Investigator's own illustration.** It is unsourced and was never checked against a life table. The critique concedes that its magnitude is "UNGROUNDED."
- **Romanowski 2019 (pooled SMR 2.91, 95% CI 2.21–3.84) establishes the direction.** It does not establish that the SMR transfers to the age and country mix of this trial's patients. I cannot ground how much of that SMR comes from LMIC cohorts. The critique flags this uncertainty itself.
- **The SMR is a relative comparison with the general population.** Part of it reflects confounders such as HIV, smoking, alcohol and poverty. Those confounders would also affect the saved patient, so confounding does not remove the effect. It does mean the SMR cannot be read as a TB-sequelae penalty alone, and the Gompertz scaling treats it as a pure hazard multiplier.
- **The Gompertz equivalence assumes a constant proportional hazard multiplier across all remaining ages.** I cannot cite a source for how SMRs after TB vary with age or time since treatment. If the excess is front-loaded or attenuates at older ages, the "~11–12 years of effective ageing" overstates the loss. This is a general modeling caveat, not a sourced finding.
- **The critique's arithmetic is internally correct.** ln(3)/0.09 ≈ 12.2 and ln(3)/0.10 ≈ 11.0. The weakness is the choice of b, not the calculation.

**MAGNITUDE CHALLENGE:**

- **Possible double-counting in the critique's own derivation.**
  - The critique computes a 20–30% cut to life expectancy (low-to-mid 30s down to mid-20s).
  - It then applies that percentage to 27, which is described as already a healthy-life figure.
  - If 27 already embeds a morbidity discount, some of the "comorbidity" effect is already in the number. A full 20–30% on top would overstate the shift.
  - A defensible lower bound is therefore a smaller cut than 20%.
- **The critique's own range does not by itself breach the bar.**
  - The critique states a threshold of 17.7 DALYs per death.
  - Its own range of 19–22 stays above that threshold.
  - It reaches "near or below" only by "combining with any other downward adjustment," which is not this critique's burden to carry.
  - On the 25% change criterion, only the upper end of the range (a 30% cut) is clearly material. A 20% cut is not.
- **Gompertz slope in LMIC settings is an open question.**
  - A lower b would imply more effective ageing, which favors the critique.
  - I cannot ground b for LMICs and do not claim it is higher.
- **The adjustment is a one-time proportional cut.** It applies equally to the whole 539,500 DALYs, so it moves SROI linearly (3,000x to roughly 2,300–2,500x at 20–30%, ignoring other changes).

**OFFSETTING FACTORS:**

- **The BOTEC values only on-treatment mortality.** The CG context says the trial also measures lung damage on chest X-ray. If statins reduce lung damage, any post-treatment morbidity and excess mortality that stem from TB sequelae would also fall. Those benefits are currently valued at zero.
- **Baseline mortality may be understated.** The Parameter Map notes that notified-cohort mortality may miss unascertained deaths, which would raise baseline_mortality. This has not been quantified.
- **The 6% baseline mortality may skew toward sicker patients.** I cannot resolve this. It could cut either way for the average patient whose death is averted, so I do not claim it as an offset.
- **Counterfactual credit and timing are not at issue here.**

**OVERALL ASSESSMENT:** Partial defense.

- The direction of the critique is sound and well supported. Survivors do have elevated mortality, and a general-population life table would overstate their years gained.
- The defense rests on three points:
  1. The magnitude is unsourced.
  2. 27 may already be a health-adjusted LMIC figure, so the full 20–30% cut risks double counting.
  3. The BOTEC leaves positive benefit channels at zero.
- I cannot confirm any of these, because the derivation of 27 is unknown. The critique's central uncertainty is therefore also my central uncertainty.

**CONCESSIONS:**

- CG's BOTEC contains no explicit adjustment for survivors' excess mortality or comorbidity. A reader cannot tell whether the 27 includes one.
- A downward revision of some size is more likely than not. A cut in the range of roughly 10–25% is a reasonable working expectation, but I cannot ground that range. Treat it as an uninformed prior.
- The effect is non-trivial for a grant at about 3,000x against a 2,000x bar. A 30% cut would leave SROI around 2,150x, which is much closer to the bar.

### Challenger
REBUTTAL: Survivors' excess mortality and comorbidity shrink the 27 DALYs per death

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: CG labels 27 "remaining healthy life expectancy," so a morbidity discount is already built in. The Advocate infers 27 is a health-adjusted country-level number because it sits 10–20% below the critique's "low-to-mid 30s" life expectancy.

- **Morbidity and excess mortality are different channels.**
  - A HALE-type discount scales years by a general-population disability burden.
  - The critique's mechanism is a hazard multiplier that shortens the years themselves. Romanowski 2019 measures this as an SMR of 2.91 (95% CI 2.21–3.84).
  - A health adjustment taken from a general-population table does not contain TB-survivor mortality. Calling the label "healthy" does not address the critique.
- **The inference is circular.**
  - The "10–20% below" comparison uses the critique's own unsourced "low-to-mid 30s" figure.
  - The same gap would arise if 27 were raw life expectancy at a somewhat older average age or from a different country's table.
  - The Advocate admits this is not a verified fact. It should carry no weight toward "already covered."
- **The Advocate concedes the key fact.**
  - The Parameter Map shows no explicit survivor-mortality adjustment.
  - The Advocate cannot show 27 was built from TB-specific data.
  - The only version of "already covered" that fully answers the critique is a TB-survivor-based table. There is no evidence for it.
- **The zero-valued channels are not coverage.**
  - Lung-damage DALYs, transmission and diagnostic value do not change dalys_per_death.
  - The lung-damage channel depends on an unverified assumption that statins reduce sequelae.
  - A cushion that is neither modeled nor quantified cannot offset a quantified parameter bias.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

- **Unsourced is not rejected.**
  - The verifier marked the magnitude as unverifiable, not contradicted.
  - The critique's central claim, that the direction is downward, is "well supported by the literature" per the verifier.
  - The Advocate agrees on direction, so this is a dispute about size.
- **The Advocate's own concession removes the confounding objection.** The Advocate says HIV, smoking, alcohol and poverty would also affect the saved patient, so confounding "does not remove the effect." That objection therefore has no bearing on the number.
- **The constant-multiplier objection is real but cuts both ways.**
  - I cannot cite an age-specific SMR pattern, and I concede attenuation at older ages would shrink the effect.
  - Life expectancy is dominated by mortality at older ages. Attenuation there matters most, so the concern is not trivial.
  - Against that, the patients whose death is averted by treatment are by selection high-risk TB patients. They are plausibly worse off than the average survivor in Romanowski's pooled cohorts.
  - I cannot ground the size of that selection effect. It is a logical direction, not a number.
- **The Advocate is right that b is the weak point.**
  - The Gompertz slope b ≈ 0.087 corresponds to mortality doubling roughly every 8 years (ln2/8). That figure is general demographic knowledge, not from this evidence package.
  - At b = 0.087, ln(3)/0.087 ≈ 12.6 years of effective ageing, consistent with the critique.
  - The Advocate concedes that a lower b in LMICs would raise the effect. I cannot ground LMIC b, so this is conditional only.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: applying 20–30% to a number that is already health-adjusted double-counts, so the defensible lower bound is below 20%.

- **The double-counting argument conflates two things.**
  - Suppose 27 = (life expectancy) × (health factor). A hazard multiplier shortens the life expectancy term. The health factor then applies to fewer years, so the two effects compound multiplicatively.
  - Double counting would require the health factor to be built from TB-survivor mortality. That is the same unknown on which the Advocate's whole coverage claim rests.
  - Without that, nothing supports a bound below 20%.
- **Even the low end of the SMR confidence interval gives roughly 18%.** The chain, using the critique's own unsourced life-table figures:
  - ln(2.21) ≈ 0.79. At b = 0.09 this is about 8.8 years of effective ageing.
  - The critique's table implies remaining life expectancy of about 33 years at age 40 and about 25 at age 52, a loss of roughly 0.67 years per year of ageing.
  - 8.8 × 0.67 ≈ 5.9 years, which is about 18% of 33.
  - At the upper CI (ln 3.84 ≈ 1.35, about 14.9 years), the loss is about 10 years, or 30%.
  - The 95% CI therefore implies roughly 18–30% under the critique's life-table assumptions. This is an inference from an unverified table, not an independent estimate.
- **I concede the Advocate's threshold arithmetic.**
  - Getting from 3,000x to 2,000x needs a cut of about 33%. Getting from 27 to 17.7 needs about 34%.
  - The critique alone, even at 30%, does not cross the bar.
  - Its materiality is as a substantial downward factor that narrows the margin to about 2,100–2,500x, not as a standalone breach.
- **The Advocate's own prior is ungrounded.** It offers 10–25% and labels it an uninformed prior. The SMR-based range of about 18–30% is the only derived range in the debate.

**RESPONSE TO "OFFSETTING FACTORS":**

- **Lung-damage benefit.**
  - It is not in the model and depends on an unverified assumption that statins reduce sequelae.
  - It would raise total benefit. It would not change DALYs per death averted.
  - It is hypothetical, not an offset.
- **Baseline mortality understated.**
  - The Advocate admits this is unquantified.
  - It affects a different parameter, the count of deaths averted, not the years gained per death.
  - It does not offset the per-death correction.
- **6% baseline skews sicker.**
  - The Advocate declines to claim it, and I agree it is unresolved.
  - If anything, a sicker-than-average mix of averted deaths points the same way as the critique.
- **No offset is both quantified and in the model.** The residual downward pressure therefore stands at roughly 18–30%, conditional on the derivation of 27.

**KEY UNRESOLVED QUESTIONS:**

- How was 27 derived? Is it a general-population LE or HALE, a country-weighted figure, or based on TB-specific data? This decides whether the adjustment applies at all.
- What is the age distribution of patients whose deaths are averted? The effective-ageing arithmetic depends on it.
- Does Romanowski's pooled SMR transfer to the trial's LMIC setting? Does it attenuate with age or time since treatment?
- Is the marginal patient whose death is averted sicker than the average survivor in the SMR cohorts?
- What is the actual remaining-life-expectancy schedule and Gompertz slope in the relevant country? The 33 and 25 figures are the critique's own unsourced numbers.

### Judge Audit
Surviving strength: moderate
Justification: The Challenger made two grounded moves that the Advocate's position could not withstand:
- a sound synthesis from the verified SMR CI to an 18–30% conditional range;
- a correct rebuttal of the Advocate's HALE double-counting argument.
The Advocate's strongest move was the threshold arithmetic: the critique alone stays above 17.7. That was well grounded and conceded by the Challenger. It caps the critique's materiality as a standalone breach.
Both sides overlooked the verifier's heterogeneity evidence, so the magnitude rests on an untested transfer assumption. The direction is solid, and the conditional magnitude is meaningful but not threshold-breaking.
Recommended action: 2. SPECIFIC INVESTIGATION: Find the source of "27" in CG's BOTEC or supporting documents, or ask CG directly. Specifically, determine:
   - whether 27 is GBD/WHO HALE or a country life-table value;
   - the age it was evaluated at;
   - whether any TB-specific adjustment was applied.

   If it is a general-population figure, re-run the adjustment using setting-specific SMRs from Romanowski 2019's subgroup or LMIC estimates, and test sensitivity to the Georgia-type low-SMR scenario. Both steps are feasible with existing tooling and a document request.

   Interim conclusion (moderate confidence): treat dalys_per_death as likely overstated by roughly 10–30% if 27 is a general-population figure. This implies SROI of about 2,100–2,700x. The figure is material to the margin but does not by itself push the grant below the 2,000x bar.
Action feasibility: requires_specified_evidence
Advocate failures: ['unsupported_estimate_fabricated: A cut in the range of roughly 10–25% is a reasonable working expectation, but I cannot ground that range. Treat it as an uninformed prior." The Advocate discloses that the number is ungrounded, which is better than hiding it. But the range still has no derivation, and its lower end (10%) sits below anything the SMR evidence implies. Disclosure does not turn a guess into a defense.', 'unsupported_estimate_pseudo: If 27 already embeds a morbidity discount… A full 20–30% on top would overstate the shift. A defensible lower bound is therefore a smaller cut than 20%." The chain has a clear logical gap. Suppose 27 = LE × health factor, and the health factor comes from the general population. Then a proportional cut to LE carries straight through to 27; nothing is counted twice. Double counting arises only if the health adjustment already reflects TB-survivor mortality, and the Advocate gives no evidence of that. The argument also blurs morbidity (a HALE discount) with excess mortality (the SMR channel).', 'unsupported_estimate_pseudo: The "Existing coverage" inference says that because 27 sits "about 10–20% below" the critique\'s own unsourced "low-to-mid 30s" figure, 27 is likely a country-level, health-adjusted number. This is consistent with that reading but does not support it, as the Challenger noted. To the Advocate\'s credit, it is flagged as an inference.', 'unsupported_estimate_pseudo: The SROI arithmetic is internally inconsistent. The Advocate says a 20–30% cut takes 3,000x to "roughly 2,300–2,500x," but 3,000 × 0.7–0.8 = 2,100–2,400x. The Advocate\'s own concession later gives about 2,150x at a 30% cut. This is a minor slip, but it overstates the remaining margin.', 'call_to_ignorance: If statins reduce lung damage, any post-treatment morbidity and excess mortality that stem from TB sequelae would also fall. Those benefits are currently valued at zero." This offers an unverified efficacy channel as a "structural cushion." It is speculative. It also does not act on dalys_per_death, the parameter under dispute.', "sound_synthesis_noted: The Advocate correctly checks the Gompertz arithmetic (ln3/0.09 ≈ 12.2, ln3/0.10 ≈ 11.0). It correctly identifies the constant-multiplier assumption as a modeling weakness. It honestly concedes that the critique's 19–22 range does not cross 17.7 on its own. That last point is the Advocate's strongest and best-grounded move."]
Challenger failures: ["sound_synthesis_noted: The 18–30% range is derived step by step. It takes the verifier-confirmed Romanowski CI (2.21–3.84), converts it via ln(k)/b to 8.8–14.9 years of effective ageing, interpolates about 0.67 years of LE lost per year of ageing from the critique's table, and lands at about 18% and about 30%. The arithmetic checks out. The Challenger states that it rests on the critique's unverified life-table figures. This is legitimate analysis.", "sound_synthesis_noted: The compounding rebuttal is correct. A hazard multiplier shortens the LE term, and a general-population health factor then applies to fewer years. The Advocate's double-counting objection only works if the health factor is built from TB-survivor mortality.", 'false_definitiveness: No offset is both quantified and in the model. The residual downward pressure therefore stands at roughly 18–30%, conditional on the derivation of 27." The range covers only the sampling uncertainty of one pooled SMR. It ignores the between-setting heterogeneity that the verifier explicitly flagged (Georgia SMR 0.89). It also ignores the attenuation concern the Challenger itself conceded "is not trivial." Stating a CI-bounded range as "the residual" overstates how settled the magnitude is.', 'misrepresenting_evidence_status: Without that, nothing supports a bound below 20%" and "The SMR-based range of about 18–30% is the only derived range in the debate." The verifier package does contain evidence pointing to smaller effects:', 'unsupported_estimate_pseudo (minor): b ≈ 0.087 … general demographic knowledge, not from this evidence package." The value is disclosed and roughly standard for adult mortality, so it is not fabricated. But it is imported from outside the evidence package to bolster the critique, and its applicability to LMIC settings is unaddressed.']
Debate resolved: Both sides agree that the direction is downward. They also agree that the critique alone does not reach the 17.7 threshold: about a 34% cut is needed, and the critique's own range tops out near 30%. Its effect is to narrow SROI to roughly 2,100–2,450x, not to breach the bar.

The debate also established that the "27 is labeled healthy life expectancy" argument does not neutralize the adjustment. A survivor hazard multiplier compounds with a general-population health factor. It is double-counted only if 27 was built from TB-specific mortality data.

Conditional on a general-population table and on the Romanowski SMR transferring, the implied cut is about 18–30%.
Debate unresolved: Two questions remain open:
1. **How was 27 derived?** If it comes from a general-population LE or HALE, the adjustment applies. If it is TB-specific, it does not. Neither side could resolve this, and it controls whether the adjustment applies at all.
2. **Does the pooled SMR of 2.91 transfer** to the trial's LMIC, age and time-since-treatment profile? Neither side engaged with the verifier's Georgia SMR of 0.89. The Challenger raised the selection argument (averted-death patients may be sicker than survivors) but did not quantify it.

--- Critique: The 6% is a mix of deaths, and only a fraction is reachable and modifiable by atorvastatin ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: The 6% is a mix of deaths, and only a fraction is reachable and modifiable by atorvastatin

EXISTING COVERAGE:
- CG's calculation does not apply the effect to the baseline as a separate step. It assumes a 10% relative cut in mortality among treated drug-susceptible patients, and the 0.6 pp figure is simply 10% × 6%.
- The 10% is an assumption about all-cause on-treatment mortality in the treated population. If it was meant as a population-level effect, it already nets out early deaths, non-TB deaths and non-responders.
- The Challenger's own evidence section concedes this. It says an addressable-share haircut on the baseline "would penalise the same deaths twice" if the effect is a relative reduction on all-cause mortality.
- Under that reading, the decomposition 6% × 0.7 × 0.85 = 3.6% double-counts. The critique is then a request to clarify what the 10% means, not a reason to lower the baseline.
- The "share of the population eligible for statin" term overlaps with the 60% adult uptake. That 60% is applied to all adult patients, so about 40% of patients are already assumed not to take the drug. This plausibly includes contraindicated and very sick patients.
- The 10% is also small relative to the stated surrogate-level signal (faster clearance, less lung damage on X-ray). CG does not derive the 10% from that signal, so I cannot show it is conservative. I only note that it is a modest relative figure and the 40% success probability is applied on top of it.
- The Phase IIc trial is explicitly testing dosing strategies. That is the route by which the rifampicin–atorvastatin exposure problem would be addressed before Phase III.

EVIDENCE WEAKNESSES:
- Every share in the decomposition (30% early or ineligible, 15% non-TB, 0.7, 0.85) is labelled illustrative or a placeholder. The 3.6% is therefore not an estimate. It is an arithmetic example chosen to land just under the threshold.
- The Zambia, Ethiopia and Cameroon cohorts show when deaths occur (about 75% early in Zambia). They do not show how many of those deaths are beyond reach of a statin.
- The critique's own hypothesis says whether benefit onset is delayed is UNGROUNDED. The "after statin could plausibly act" factor therefore has no support.
- Conditional on early deaths being unreachable, the critique would work. That conditional is the missing premise. A host-directed, anti-inflammatory mechanism might act on early TB-driven deaths too, but I cannot ground that either. I am not asserting it.
- The Taiwan result is that malnutrition-related excess mortality is confined to the first 8 weeks. This is a timing result, not a result on whether statins can alter those deaths.
- The critique concedes trial populations usually exclude the sickest patients. Whether the haircut is justified therefore depends on an unresolved question: does the 10% come from a selected trial population, or is it applied to the unselected WHO cohort?
- The sensitivity results are empty. The critique supplies no tested range, so "material" is asserted rather than shown.

MAGNITUDE CHALLENGE:
- SROI in the BOTEC is linear in baseline mortality. Derivation: $OP 54B / $7M ≈ 7,714; × 40% ≈ 3,086x. Scaling by 3.6/6 gives ≈ 1,850x, which is below 2,000x. So the arithmetic works if the haircut is applied in full.
- The effective baseline is highly sensitive to the placeholder shares. Applying only the 15% non-TB haircut gives 5.1% and ≈ 2,620x, which clears the bar. Applying only the 30% early/ineligible haircut gives 4.2% and ≈ 2,160x, which also clears it.
- The threshold is crossed only if both haircuts are applied and neither is already embedded in the effect size. The critique itself flags this as the unverified step.
- With no grounded values for either share, I cannot offer a better counter-estimate. Treat my statement that the haircut is likely smaller than 40% as an uninformed prior, not a finding.

OFFSETTING FACTORS:
- The model values only on-treatment mortality. The parameter map lists morbidity, post-treatment mortality, transmission and diagnostic value as implicit zeros. Any positive value there offsets part of a baseline haircut, though I cannot quantify it.
- The parameter map also notes that notified-cohort mortality may understate true mortality through unascertained deaths. That would push the baseline up.
- Some non-TB deaths, such as cardiovascular events in older patients, might actually be reduced by a statin. The critique treats them as wholly unreachable.
- The 60% uptake already removes a large share of patients. If the 10% relative effect is thought of as applying to those who take the drug, the effective cohort is already narrowed.

OVERALL ASSESSMENT:
Partial defense.
- The critique's headline mechanism, a haircut on the 6% baseline, is undermined by the Challenger's own double-counting point. It applies only if the 10% was meant as an effect on an unselected population.
- GiveWell (CG) did not state how the 10% was derived. This leaves open that the 10% is optimistic for an unselected cohort and that early, very sick patients are disproportionately lost. I cannot rule that out.
- The numbers show the conclusion is fragile on this parameter. Combined haircuts of about 40% would put SROI below the bar, though the specific shares are ungrounded.

CONCESSIONS:
- The BOTEC does not say whether the 10% is a trial-population or an unselected-population effect. That ambiguity is real and decides whether the baseline haircut applies.
- Early-death concentration in sub-Saharan African cohorts is well supported. If statins act only after weeks, a meaningful share of the 6% is not addressable, and the double-counting defense would not apply.
- The uptake overlap argument is imperfect. If excluded patients are sicker and carry disproportionate mortality, the 60% uptake haircut understates the loss of baseline deaths.
- The rifampicin–atorvastatin interaction and the delayed-onset question are unaddressed in the BOTEC beyond the Phase IIc dosing focus.
```

### Challenger
REBUTTAL: The 6% is a mix of deaths, and only a fraction is reachable and modifiable by atorvastatin

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: The 10% is a relative cut in all-cause on-treatment mortality, so it already nets out early deaths, non-TB deaths and non-responders. An addressable-share haircut on the 6% would therefore double-count.
>
> Response:

- I concede the logic. If the 10% was derived as an all-cause effect in an unselected treated population, the haircut double-counts.
- The Advocate's own concessions say CG does not state how the 10% was derived, and that it is not derived from the surrogate signal. The "nets out" claim therefore rests on a premise nobody can verify.
- The verifier labelled the double-counting point an "unverified inference." The critique raised it first, but it is not established.
- An ungrounded number cannot be assumed to have netted anything out. The 10% could just as easily be a round number placed on a surrogate-level signal (faster clearance, less lung damage on X-ray).
- Surrogate signals come from patients who survive long enough to be measured. They say nothing about patients who die in the first weeks.
- The verifier's third point is that trial populations usually exclude the sickest patients. If the 10% leans on that kind of evidence, it is a selected-population effect applied to an unselected 6% baseline. That is the exact case where the decomposition holds.
- The Advocate says the critique "is a request to clarify what the 10% means." That is a real finding. The conclusion flips on an undocumented assumption, and the BOTEC does not disclose which reading applies.

> The Advocate claims: The 60% adult uptake plausibly already removes contraindicated and very sick patients, so it overlaps with the "eligible share" term.
>
> Response:

- The Advocate concedes this is imperfect. Here is how far it matters.
- The uptake factor scales deaths averted proportionally. That is correct only if non-takers carry mortality proportional to their headcount (40% of patients, 40% of deaths).
- If excluded patients are sicker, the takers' share of deaths is below 60%.
- Derivation: the 3.9% threshold is 65% of 6%, so SROI falls below 2,000x if takers hold less than 0.65 × 60% ≈ 39% of baseline deaths.
- By itself, this overlap argument does not cross the threshold. A 50% death share for takers gives about 2,570x. But it is a third unquantified leak, and it compounds with the other two.

> The Advocate claims: Phase IIc is testing dosing strategies, which is how the rifampicin–atorvastatin exposure problem gets addressed.
>
> Response:

- Dosing addresses drug exposure. It does not address when in the treatment course a benefit appears.
- On the Advocate's own description, the existing signal is surrogate-level. Surrogate success would not show whether the mortality effect reaches deaths in weeks 0–8.
- The 40% success probability is applied on top of the 10%. It is not a mortality-timing adjustment.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: The shares are placeholders. The cohort data show timing, not reachability. The Taiwan result is about timing, not statin modifiability. The delayed-onset factor is UNGROUNDED and so unsupported.
>
> Response:

- I concede the 3.6% is an arithmetic illustration, not an estimate.
- "UNGROUNDED" is not "REJECTED." The critique labelled delayed onset as ungrounded, and the verifier did not find contrary evidence. The right treatment is conditional: if a statin needs weeks to act, how much of the 6% is lost?
- The 75% early-death share in Zambia is attested (verifier item 1). It lets me do the conditional without placeholders.
- Take a Zambia-like cohort where 75% of deaths fall in the early window. Let r be the statin's relative effectiveness on those early deaths compared with later ones.
- Addressable share = 0.25 + 0.75r. The threshold requires this to be below 0.65.
- Solving gives r < 0.53. If the statin is less than about 53% as effective on early deaths as on later ones, the SROI drops below 2,000x. This uses no non-TB or ineligibility haircut.
- At r = 0, the effective baseline is 1.5% and SROI is about 3,086 × 0.25 ≈ 770x.
- Caveats:
  - Cohorts differ. The critique says some show flatter timing.
  - The 75% is from one country.
  - The double-counting defense still applies if the 10% is a true unselected all-cause effect.
- This answers "the critique has no tested range." The sensitivity is a one-parameter calculation from an attested timing figure. The open question is r, not the placeholder shares.
- The Advocate says a host-directed mechanism "might act on early deaths too" but does not assert it. That is symmetric ignorance, and it leaves a critical parameter (r) unspecified in the BOTEC.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: Either haircut alone leaves SROI above the bar (≈2,620x or ≈2,160x). The threshold is crossed only if both apply and neither is embedded in the effect.
>
> Response:

- The arithmetic is right for the placeholder shares. The Advocate's figures follow from linearity.
- The margin is thin. The required reduction is only 35% of baseline (3.9/6 = 0.65). The Advocate's single-haircut result of ≈2,160x is only 8% above 2,000x.
- Realistic values for the early-death share are not placeholders. The Zambia figure (75%) is an attested upper-range number.
- The timing derivation above shows the threshold can be crossed with a single mechanism (reduced early efficacy), without invoking the non-TB haircut.
- The minimum plausible magnitude is zero. If the 10% is an unselected all-cause effect, no haircut applies.
- The maximum is the r = 0 case (≈770x). Both ends are within what the evidence cannot exclude.
- The Advocate's own conclusion is that the result "is fragile on this parameter." That is the substance of the critique.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: Unquantified morbidity, post-treatment mortality, transmission and diagnostic value are implicit zeros. Unascertained deaths push the baseline up. Some non-TB deaths might be reduced by a statin. The 60% uptake narrows the cohort.
>
> Response:

- The implicit zeros are an offset to SROI generally, not to the baseline decomposition. The Advocate cannot quantify them. They are speculative until someone shows positive values, and in the BOTEC they are zero.
- Unascertained deaths are plausibly deaths before or outside treatment. This is my reasoning, not a verified finding. A drug given to treated patients cannot avert deaths that occur before diagnosis or initiation. So this pushes the notified baseline up, but not the addressable baseline.
- Non-TB deaths reduced by a statin: the Advocate admits it cannot ground this. I cannot ground the time course of cardiovascular benefit either. The offset is hypothetical.
- The 60% uptake does not offset anything. It is already a separate multiplier, and the Advocate concedes its overlap with the eligible-share term is imperfect.
- None of these offsets is in the model with a value. They cannot restore a margin that the model's single parameter already leaves at risk.

**KEY UNRESOLVED QUESTIONS:**

- What is the source of the 10%: an all-cause effect in an unselected cohort, a selected trial population, or a judgmental discount from surrogate outcomes? This decides whether the haircut applies at all.
- What is r, the relative statin effect on deaths in the first 8 weeks compared with later deaths? The threshold sits at r ≈ 0.53 for a Zambia-like timing profile.
- Is the 75% early-death share representative of the cohorts that determine the 6% baseline, or does it overstate concentration?
- Do patients excluded from or declining the drug (the 40%) carry a disproportionate share of deaths?
- Does the rifampicin–atorvastatin interaction delay onset of benefit, as well as reduce exposure? Phase IIc dosing work does not obviously resolve this.

### Judge Audit
Surviving strength: moderate
Justification: Both sides reasoned largely from the evidence package with shown derivations, and both made appropriate concessions. The critique's quantitative claim (3.6%, below threshold) did not survive as an estimate. Its structural claim survived and was sharpened: the BOTEC result is fragile to an undisclosed assumption about the 10%, and the threshold requires only a 35% effective-baseline reduction. The Challenger's r-derivation is a grounded conditional the Advocate had no chance to answer. However, the Challenger misstated the verifier's contrary pharmacokinetic evidence and overstated the downside bound, so the critique is not strong.
Recommended action: 2. SPECIFIC INVESTIGATION: Determine how CG derived the 10% relative mortality reduction. Specifically, establish whether it is a judgmental discount from surrogate endpoints (sputum clearance, CXR) in a trial population, or an assumed all-cause effect in unselected notified cohorts. This is feasible by checking the BOTEC source notes or asking the analysts, and it decides whether any baseline haircut applies.

If the 10% is surrogate or trial-derived, the verifier should then run targeted searches for:
- Time-to-death distributions in WHO-notified drug-susceptible TB cohorts beyond Zambia, to bound the early-death share.
- Any adjunctive host-directed therapy trial (statins or others) reporting mortality by treatment phase, to bound r.

The first search is feasible with existing tooling. The second may find little.

Interim conclusion: do not apply the 6% × 0.7 × 0.85 decomposition. Instead, flag in the CEA that SROI falls below 2,000x if the effective addressable baseline drops by more than about 35%. This is plausible if the 10% is not an unselected all-cause effect and early deaths are substantially less responsive.
Action feasibility: requires_specified_evidence
Advocate failures: ['sound_synthesis_noted: The SROI linearity derivation ($54B / $7M ≈ 7,714 × 40% ≈ 3,086x, scaled by 3.6/6 ≈ 1,850x) is sound. So is the single-haircut decomposition (5.1% → ≈2,620x; 4.2% → ≈2,160x). Each step is shown, and the derivation correctly isolates that both haircuts are needed to cross the bar under the placeholder values.', 'sound_synthesis_noted: The Advocate labels "haircut likely smaller than 40%" as "an uninformed prior, not a finding." This is correct epistemic labelling of a number the Advocate could not ground. It is not a failure.', 'call_to_ignorance: Under Offsetting Factors, the Advocate writes: "Some non-TB deaths, such as cardiovascular events in older patients, might actually be reduced by a statin." This is offered as an offset with no grounding. The time course of cardiovascular benefit within a 6-month treatment window is not supported. The Advocate disclaimed a parallel speculation (host-directed early action) in Evidence Weaknesses, but not this one.', 'misrepresenting_evidence_status: The Advocate calls the double-counting point "the Challenger\'s own evidence section" and says it "undermines" the headline mechanism. That point is the verifier\'s own reasoning, explicitly labelled "an unverified inference." The Advocate partly corrects this by later conditioning on "if the 10% was meant as a population-level effect," so this is a mild instance.']
Challenger failures: ['sound_synthesis_noted: The early-death efficacy calculation is a sound conditional synthesis. It sets addressable share = 0.25 + 0.75r against a 0.65 threshold, giving r < 0.53, and r = 0 gives ≈770x. It starts from an attested timing figure (Zambia 75%), shows each step, and caveats single-country provenance, flatter cohorts, and the double-counting defense. It converts placeholder shares into a single identifiable unknown, which is real analytical progress.', 'sound_synthesis_noted: The uptake-overlap calculation (takers must hold < 0.65 × 60% ≈ 39% of deaths; a 50% share gives ≈2,570x) is arithmetically correct. The Challenger also honestly concedes it does not cross the threshold on its own.', 'misrepresenting_evidence_status: The Challenger writes: "The critique labelled delayed onset as ungrounded, and the verifier did not find contrary evidence." The verifier did report contrary mechanistic evidence: early atorvastatin exposure may be higher under rifampicin, and the delay inference "is not supported." The Challenger\'s key unresolved question again frames the interaction as possibly delaying onset, without acknowledging this finding. A low r could still arise for non-pharmacokinetic reasons, such as patients being too advanced to benefit. However, the Challenger did not make that argument and instead misstated the evidence record.', 'call_to_ignorance: The Challenger writes: "The 10% could just as easily be a round number placed on a surrogate-level signal." This counters one unverified premise with an equally unsupported alternative. The follow-on conditional ("If the 10% leans on that kind of evidence…") is legitimate. The "just as easily" framing is not.', 'false_definitiveness: The Challenger calls the Zambia 75% "an attested upper-range number," then in the same section says "Realistic values for the early-death share are not placeholders." It then presents r = 0 with 75% early concentration (≈770x) as a plausible maximum "within what the evidence cannot exclude." Pairing an admitted upper-range input with the most extreme efficacy assumption, then framing it as a realistic bound, overstates the downside.']
Debate resolved: Both sides agree on three points:
- The 3.6% figure is an arithmetic illustration, not an estimate.
- The uptake overlap alone cannot cross the threshold.
- The critique's validity hinges on whether CG's undocumented 10% effect is an all-cause effect in an unselected cohort (haircut double-counts) or a selected-population or surrogate-derived figure (haircut applies).

The Challenger also usefully reduced the timing mechanism to one parameter. For a Zambia-like profile, the bar is crossed if statin efficacy on early deaths is less than about 53% of its efficacy on later deaths.
Debate unresolved: Three questions remain open:
- The provenance of the 10%.
- The value of r. Neither side grounded it, and the verifier's pharmacokinetic evidence weighs somewhat against a drug-exposure route to low r. That evidence was not engaged.
- Whether the 75% early-death concentration is representative of the cohorts underlying the 6% baseline.

--- Critique: Under-ascertained deaths push true mortality up, and the direction is the opposite of Critiques 1–2 ---

### Advocate
**DEFENSE OF GIVEWELL'S (CG's) POSITION: Under-ascertained deaths push true mortality up**

**EXISTING COVERAGE:**
- CG's BOTEC says only "mortality among treated drug-susceptible patients is about 6%." It does not say the 6% is the WHO "died" share of a notified cohort. The critique's premise, that the 6% omits LTFU deaths, is therefore a conjecture about the source of the number. The Parameter Map itself lists "no distinction between notified-cohort and true mortality" as a gap, which means the provenance is unstated rather than shown to be WHO-cohort-based.
- The model counts only deaths that statins could plausibly avert (a 10% relative cut applied to the 6% baseline). It does not claim to count all TB deaths. The relevant quantity is therefore treated-patient deaths that adjunctive therapy can modify. That quantity is only loosely tied to the number of ascertained deaths.
- CG applies 60% uptake and a 40% success probability to this chain. Neither is calibrated to LTFU patients, who are the group the critique adds deaths for.

**EVIDENCE WEAKNESSES:**
- The Kenyan surveillance paper establishes that vital status was unknown for 8.4% of patients. It does not give a death rate for them. The 6–7% LTFU-plus-not-evaluated share is the critique's own assumption, taken from one Kenyan setting and applied globally.
- "Not evaluated" under WHO definitions includes transfers out and unknown outcomes. This is from my knowledge of WHO definitions and is not in the evidence package. If that is right, many of these patients are alive and evaluated elsewhere. Applying a 10–20% death rate to the whole combined category would then overstate the hidden mortality.
- The Kilifi tracing study (10%) is a single-site estimate from a drug-susceptible-dominant, high-HIV-burden setting. I have no sample size for it. It cannot be assumed to represent the global new-case population CG models.
- The drug-resistant studies (23–30%) are the only support for the upper end of the range. The critique itself says they are "less applicable," and CG's model is 96% drug-susceptible. The applicable evidence therefore supports roughly 10%, not 10–20%.
- The Global WHO percentages are unverified. The size of the unascertained pool, which drives the whole calculation, is not grounded beyond the one Kenyan figure.
- The sensitivity output is empty. The impact figures are hand arithmetic, not a run of the formula chain. I checked the arithmetic: SROI is linear in baseline mortality, so +0.6 to +1.4 pp on a 6% base gives +10% to +23%.

**MAGNITUDE CHALLENGE:**
- The critique is internally inconsistent. The hypothesis states +0.3 to +1.4 pp, but the mechanism computes 0.6–1.4 pp. The 0.3 pp low end corresponds to +5%.
- Restricting to the applicable evidence (Kilifi, ~10%) and the critic's own 6–7% pool gives 0.6–0.7 pp, or +10–12% on SROI. Even the critic's stated maximum (+23%) falls below the ~25% decision-relevance threshold.
- The statin-attributable share f is unknown, and the critique concedes this. The added effect scales with f. Using f = 0.5 as an agnostic midpoint (a convention, not an evidenced figure), the added deaths are 0.3–0.7 pp and the SROI change is about +5–12%.
- I have no data to support any particular f. The mechanism does point below 1. LTFU patients by definition did not complete treatment, so their statin exposure is truncated. Deaths after interruption are less likely to be reduced by a drug that works through clearance and lung-damage pathways.
- The uptake and relative-reduction parameters were not calibrated for this population. This argues against adding deaths at full weight.

**OFFSETTING FACTORS:**
- The Parameter Map notes that CG makes no adjustment for deaths unreachable by adjunctive therapy (early deaths, HIV and comorbidity deaths). LTFU deaths are plausibly dominated by these categories. This is a conjecture, but it pushes the same hidden-death pool toward lower modifiability.
- The Map also notes there is no adjustment for survivors' excess mortality. This shrinks the 27 DALYs per death. Any increase in baseline mortality comes with a similar-direction DALY issue for these patients: those who die as LTFU patients may already have lower remaining life expectancy than 27 years. This is conditional reasoning, not measured.
- The benefit mechanism (preventing deaths) is applied to a 5.5M treated population. Higher mortality among LTFU patients does not by itself imply a larger benefit per statin-treated patient.
- The ~6% is explicitly "about 6%" in a BOTEC where relative_reduction (10%) is far more uncertain, plausibly spanning zero to several times the point estimate. A one-time 5–12% shift in baseline is small relative to that.

**OVERALL ASSESSMENT:** **Partial defense.**
- The direction is probably right: CG's number is more likely an undercount than an overcount of hidden deaths among treated patients.
- The magnitude is overstated. Applicable evidence plus a statin-attributable discount puts the effect at roughly +5–12%, below the 25% materiality threshold.
- The critique's own upper bound (+23%) also falls below that threshold. Only a combination of the drug-resistant mortality rates, a large pool, and full statin attribution would approach it, and those inputs conflict with CG's 96% drug-susceptible population.

**CONCESSIONS:**
- Unascertained deaths among LTFU and not-evaluated patients are a real mechanism. CG's BOTEC provides no derivation of the 6% to show that this is already included.
- If the 6% is the WHO "died" share of notified cohorts, it is biased low, and the direction of the correction is upward.
- I cannot ground the global size of the unascertained pool or the statin-attributable share. Those are the two numbers that determine the critique's materiality, and neither is established.
- The pre-treatment-death and untreated-case claims were rightly dropped, so I do not defend against them.

### Challenger
REBUTTAL: Under-ascertained deaths push true mortality up

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: CG's 6% has no stated provenance, so the premise that it omits LTFU deaths is conjecture. The model only counts statin-modifiable deaths anyway, and the uptake and success parameters aren't calibrated to LTFU patients.

- **Provenance cuts both ways.**
  - The Advocate says the source of the 6% is unstated. That means the model has no evidence that LTFU deaths are included.
  - The Advocate's own cited Parameter Map gap, "no distinction between notified-cohort and true mortality", says the model does not separate the two. A number that isn't tied to true mortality can't be assumed to capture it.
  - The Advocate concedes that if the 6% is the WHO "died" share, the correction runs upward. The dispute is therefore conditional on provenance, not on direction.
  - I cannot ground that the 6% is the WHO "died" share. That is the critique's own unverified premise.
- **"Only modifiable deaths" does not insulate the baseline.**
  - The Advocate agrees SROI is linear in baseline mortality and that the 10% relative reduction is applied to the 6% baseline.
  - So any omitted deaths in the base enter proportionally unless they are specifically non-modifiable. That is the f discount, addressed below.
  - "Loosely tied to ascertained deaths" is not an adjustment in the model. The model contains no deduction for unmodifiable deaths, a gap the Advocate itself cites.
- **Uptake and success calibration.**
  - These parameters don't separately treat LTFU patients. That is a reason the model is silent on this population, not a reason the added deaths are already offset.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the Kenyan paper gives no death rate for the 8.4%. The 6–7% pool is the critic's assumption. "Not evaluated" includes transfers out. Kilifi is a single site. The upper range rests on drug-resistant studies that the critique itself calls less applicable.

- **Conceded points.**
  - The Kenyan paper attests an unascertained pool, not a death rate. It is mechanism support only.
  - The 10–20% range is too wide on the upper side. The drug-resistant studies (23–30%) are less applicable to a mostly drug-susceptible cohort, so ~10% is the applicable anchor.
  - The "not evaluated includes transfers out" point is plausible. It is the Advocate's own knowledge and is not in the evidence package.
- **The pool size is not just the critic's assumption.**
  - The only attested figure in the evidence package is 8.4%, which is larger than the critique's 6–7%.
  - Derivation, applying the conceded ~10% Kilifi rate to the Kenyan pool: 8.4% × 10% = 0.84 pp. 0.84 / 6 = +14% on SROI.
  - That lies inside the critique's range and above the Advocate's 10–12% restriction.
  - This is a single Kenyan setting, so the global pool is still UNVERIFIED, not rejected.
- **The transfer-out point is only a partial discount.**
  - Kilifi is a tracing study of LTFU patients, so the 10% should be applied to the LTFU share only. It should not be applied to the whole 8.4%.
  - Conversely, transfers out are a different component, and some are unobserved. I cannot ground the split between LTFU and transferred out. This is the main open quantity.
- **UNVERIFIED is not REJECTED.**
  - The Advocate's remark that global WHO percentages are "not grounded" is accurate. It does not make the pool smaller.
  - The honest framing is "pool size is unknown, with one attested data point at 8.4%."
- **Empty sensitivity.**
  - Both sides did the same linear hand arithmetic, and the Advocate confirmed it. This is not a point against the critique specifically.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: the critique's range is internally inconsistent (0.3 vs 0.6 pp). Applicable evidence gives +10–12%. With a statin-attributable share f = 0.5, the effect is +5–12%. All of this is below a ~25% threshold.

- **The inconsistency is conceded.** The 0.3 pp lower bound isn't supported by the stated mechanism arithmetic.
- **A defensible floor is not +5%.**
  - The Advocate's floor comes from setting f = 0.5. The Advocate says explicitly this is "a convention, not an evidenced figure."
  - A counter-estimate offered to neutralize the critique is itself ungrounded here, and f = 0.5 is no more supported than f = 1.
  - Without f, the only grounded chain is the 8.4% × 10% derivation above, giving +14%, or the Advocate's +10–12% on the critique's own 6–7% pool.
  - I'd put the unadjusted range at +10–14%, with f unknown. I cannot ground f.
- **The case for f < 1 is real but not decisive.**
  - Interrupted-treatment deaths plausibly have lower statin exposure. I concede this.
  - The verifier's item says death timing among LTFU undermines the "on-treatment" framing. That supports f < 1, but it does not give a value for f.
  - I cannot ground the claim that f is closer to 0.5 than to 0.9.
  - LTFU patients typically received some treatment before dropping out, so exposure is truncated, not zero. I cannot cite a source for the timing of LTFU, so treat that as an uninformed prior.
- **The 25% threshold.**
  - That is the Advocate's framing, and the critique's own materiality label was "notable," not "decisive."
  - Below the threshold does not mean zero. The direction is conceded, and an expected bias of +5–14% remains.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: LTFU deaths are likely dominated by unmodifiable causes (early, HIV). Lower life expectancy shrinks DALYs per death. The benefit per statin patient doesn't rise. The relative-reduction uncertainty swamps a 5–12% shift.

- **None of these offsets is in the model or measured.** The Advocate labels the first two "a conjecture" and "conditional reasoning, not measured."
- **The unmodifiable-deaths offset is the f argument restated.** It should not be counted twice alongside the f = 0.5 discount.
- **The life-expectancy offset has a separate home.**
  - Excess survivor mortality is a different parameter gap. It lowers DALYs per death for all deaths averted, whether or not the baseline is revised.
  - It does not offset a baseline understatement. They are independent corrections with their own sign.
  - Lower remaining life expectancy for LTFU deaths specifically is unsupported.
- **"Benefit per patient doesn't rise" misframes the issue.**
  - The critique isn't about per-patient benefit. It is about the baseline deaths the 10% reduction is applied to.
  - By the Advocate's own linearity concession, raising the baseline raises the effect.
- **Uncertainty in relative_reduction is variance, not a directional offset.**
  - A wide spread around the 10% parameter does not cancel a one-directional bias in the 6%.
  - If anything, it means this correction sits alongside a larger uncertainty and shouldn't be ignored for being small.

**KEY UNRESOLVED QUESTIONS:**
- Is CG's ~6% derived from WHO-reported "died" outcomes in notified cohorts? The critique's materiality is conditional on this, and neither side has verified it.
- What is the global LTFU versus transferred-out split within the unascertained pool, and how large is the pool outside Kenya (attested at 8.4% there)?
- What fraction f of LTFU and unascertained deaths is statin-modifiable? Neither side can ground it. It moves the result between roughly +5% and +14%.
- Is the Kilifi 10% representative of LTFU mortality in the global drug-susceptible population? No sample size is available.

### Judge Audit
Surviving strength: moderate
Justification: The mechanism survived intact. The verifier confirmed WHO definitions exclude these deaths, and the Advocate conceded both direction and the missing derivation of the 6%. The Challenger's variance-vs-bias and double-counting points were grounded and went unanswered. However, the magnitude shrank substantially. Both sides used ungrounded numbers at the edges: the Advocate's f = 0.5 and 25% threshold, and the Challenger's +14% chain, which it undercut itself. Neither used the LTFU/NE split in the evidence package, which points to a smaller effect than either side's headline range. The critique stands as a real but modest upward correction, not a materially decision-changing one.
Recommended action: 1. CONCLUDE NOW: With moderate confidence, the critique identifies a valid upward bias in baseline mortality. The grounded magnitude is about +4–8% on SROI before any statin-attributable discount. This comes from applying ~10% LTFU mortality to a 2.6–5% LTFU share. The +14–23% upper figures do not survive. Record the correction as conditional on CG's 6% being a WHO-cohort "died" share. Kenya's national ~6% died figure is consistent with this but does not confirm it.

   Two low-cost checks would tighten the estimate:
   - Confirm the citation behind CG's 6% in the BOTEC source notes.
   - Re-read the Kilifi preprint to learn whether the 90 "relocated" patients had known vital status, which determines whether 10% is a point estimate or a lower bound.

   Both are feasible with existing tooling. f is unlikely to be resolvable from available evidence and should be carried as an explicit uncertainty band rather than set to a point value.
Action feasibility: actionable_now
Advocate failures: ['unsupported_estimate_fabricated: Using f = 0.5 as an agnostic midpoint (a convention, not an evidenced figure)…" The Advocate discloses that the number is ungrounded. It still uses it to produce the +5% floor and the headline "+5–12%" conclusion. Disclosure reduces the fault but does not cure it, because the number carries the materiality conclusion.', 'unsupported_estimate_fabricated: below the ~25% decision-relevance threshold." No source or derivation is given for 25%. The Advocate\'s main magnitude conclusion ("below the materiality threshold") depends entirely on it.', 'unsupported_estimate_fabricated: relative_reduction is "plausibly spanning zero to several times the point estimate." This is asserted without grounding.', 'whataboutism: A one-time 5–12% shift in baseline is small relative to that [relative_reduction uncertainty]." This deflects from a directional bias by pointing to variance in another parameter. The Challenger correctly identifies it as variance rather than an offset.', 'false_definitiveness: The overall assessment states "Applicable evidence plus a statin-attributable discount puts the effect at roughly +5–12%." This presents as evidence-derived a range whose lower half rests on the self-admitted conventional f = 0.5.', 'call_to_ignorance: LTFU deaths are plausibly dominated by these categories [early, HIV, comorbidity]," and "those who die as LTFU patients may already have lower remaining life expectancy." Both are labelled conjecture but are still offered as offsets. The first double-counts the f discount. The second conflates a separate DALY parameter gap with the baseline question.', 'strawmanning: Higher mortality among LTFU patients does not by itself imply a larger benefit per statin-treated patient." The critique is about the baseline to which the 10% reduction is applied, not per-patient benefit. The point also contradicts the Advocate\'s own linearity concession.', 'misrepresenting_evidence_status: Kilifi: "I have no sample size for it." The evidence package gives 14 of 140 identified for tracing (36 traced, 90 relocated).', "sound_synthesis_noted: The Advocate verified that SROI is linear in baseline mortality. It identified the internal inconsistency between the 0.3 and 0.6 pp lower bounds. It derived 0.6–0.7 pp (+10–12%) from the ~10% Kilifi rate and the critique's 6–7% pool, with each step shown."]
Challenger failures: ['unsupported_estimate_pseudo: 8.4% × 10% = 0.84 pp … +14% on SROI." The Challenger then concedes that "the 10% should be applied to the LTFU share only. It should not be applied to the whole 8.4%." Yet it keeps +14% as the top of its "defensible" range. The chain is contradicted by the Challenger\'s own next bullet.', 'misrepresenting_evidence_status: I cannot ground the split between LTFU and transferred out." The LTFU vs. not-evaluated split (2.6% vs. 5.8%) is in the evidence package. Only the composition within NE is unattested. Treating the split as wholly unknown lets the inflated +14% stand.', 'misrepresenting_evidence_status: Kilifi: "No sample size is available." The evidence package gives n = 140. This repeats the Advocate\'s error rather than correcting it.', 'false_definitiveness: an expected bias of +5–14% remains." The +5% floor comes from the f = 0.5 the Challenger rejected two bullets earlier as "no more supported than f = 1." The +14% ceiling comes from the flawed chain above. The range is asserted as if established.', 'strawmanning: the critique\'s own materiality label was \'notable,\' not \'decisive.\'" The critique labelled its strength "low-to-medium"; "notable" does not appear. This is minor but a misattribution.', 'sound_synthesis_noted: Three arguments were correct and well grounded:']
Debate resolved: The debate established three things. First, the direction is upward, conditional on CG's ~6% being a WHO "died" share of a notified cohort. Second, the drug-resistant 23–30% figures do not apply, so ~10% is the relevant anchor for drug-susceptible LTFU mortality. Third, the critique's 0.3 pp lower bound and its +23% upper bound are not supported by the evidence package. On grounded inputs, before any statin-attributable discount, the effect is in the single digits to low teens. Applying ~10% to the LTFU share alone (2.6–5%) gives roughly +4–8%. Applying it to the whole pool gives at most about +14%, which over-applies an LTFU rate to NE patients.
Debate unresolved: Three questions remain open. Neither side established the provenance of CG's 6%. Neither could ground the statin-attributable fraction f, though both agreed f < 1. The mortality of not-evaluated patients, as distinct from LTFU patients, is unknown, and so is whether post-LTFU deaths occurring months later belong in the comparison window at all.

--- Critique: Covariance between mortality and DALYs per death means the product of means is not the mean of the product ---

### Advocate
**DEFENSE OF GIVEWELL'S (CG's) POSITION: Covariance between mortality and DALYs per death**

**EXISTING COVERAGE:**
- The BOTEC describes 27 as "DALYs per TB death (remaining healthy life expectancy)". This is a per-death quantity, which is the correct unit for the formula. Deaths averted × DALYs per death does not require a patient-weighted average.
- The report does not say how 27 was derived. The critique itself says its force is "conditioned on how 27 was derived" and that a GBD-style total-DALYs/total-deaths calculation makes the bias "largely disappear."
- The critique therefore has no demonstrated bias. It names a possible failure mode and concedes that the standard derivation avoids it.
- "Healthy" life expectancy is already lower than raw life expectancy. Some health-adjustment for decedents may therefore already be built into 27.

**EVIDENCE WEAKNESSES:**
1. **No empirical grounding.** The critique labels its size UNGROUNDED. The sensitivity results are empty. All numbers are "my own, assumed".
2. **The illustrative arithmetic is internally inconsistent.**
   - The critique's two groups give a patient-weighted mean of 0.7×35 + 0.3×15 = 29 DALYs, not 27.
   - It compares the death-weighted 23.8 against 27, which is not the population-average figure in its own example.
   - The "~12% lower" result mixes an arbitrary baseline with the weighting effect.
   - Against the correct population-average baseline of 29, the gap would be larger (1.52 vs 0.064×29 = 1.86, about 18%). The example therefore does not isolate the covariance effect it claims to illustrate.
   - The size of the covariance effect is determined by the assumed group parameters, and none of them is sourced.
3. **The relevant weighting is not the patient-weighted one.**
   - The BOTEC computes deaths averted as 0.6 percentage points × treated patients. It then applies DALYs per death.
   - If the relative reduction is roughly uniform across subgroups, averted deaths are proportional to deaths in each subgroup.
   - The correct DALYs per averted death is then the death-weighted average, which is what a decedent-based life-expectancy figure estimates.
   - The critique's own Evidence section concedes this. The bias arises only if 27 was patient-weighted, which nothing in the report suggests.
4. **The direction is uncertain by the critique's own admission.** Age pushes DALYs down, and HIV and young-adult TB push them up. A critique with an unsigned effect and no quantification offers little basis to move the estimate.
5. **The "life-table YLLs overstate for sick patients" point is unverified own reasoning.**
   - Engaging with it conditionally: if TB decedents have excess comorbidity, 27 is somewhat high.
   - That is a separate issue from covariance. It belongs to the parameter map's existing note on "survivors' excess mortality," and it is not a new covariance finding.

**MAGNITUDE CHALLENGE:**
- The critique's own range is −10% to −15% in low-HIV settings, and it says this could be near zero or reversed in high-HIV settings.
- Applying a −10% to −15% change to SROI (~3,000x) gives roughly 2,550–2,700x. That is under the ~25% materiality threshold and above the ~2,000x bar.
- I cannot ground a tighter counter-estimate. The only grounded statement is that the critique's own range does not cross the decision thresholds.
- The critique's "notable" materiality rating is not supported by its own numbers.

**OFFSETTING FACTORS:**
- The CEA values only on-treatment mortality. The parameter map lists morbidity DALYs, post-treatment survival, transmission averted, and diagnostic value as implicit zeros. Any downward adjustment of 10–15% to DALYs per death sits against these omitted positive channels.
- TB mortality in high-HIV settings disproportionately involves young adults, which pushes DALYs per death up. The critique acknowledges this and does not net it out.

**OVERALL ASSESSMENT:** **Strong defense.**
- The critique is conditional on an unobserved derivation and has no grounding.
- Its illustrative example does not isolate the effect it claims.
- The correct weighting for averted deaths is plausibly the death-weighted average, so no bias follows.
- Even taken at face value, the range falls below the materiality threshold and has an uncertain sign.

**CONCESSIONS:**
- If 27 was computed as a patient- or population-weighted average of age-specific YLLs, the bias is real and downward in low-HIV settings. The report does not state the derivation, so this cannot be ruled out. Documenting the derivation of 27 would be worthwhile.
- Applying generic life-table figures to TB patients with excess comorbidity may overstate years gained. This is a legitimate, separate downward consideration that is ungrounded here.
- The statin may benefit patients differently by age or comorbidity, so DALYs per averted death need not equal DALYs per death. This is a real, unquantified source of uncertainty.

### Challenger
REBUTTAL: Covariance between mortality and DALYs per death

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: 27 is labelled a per-death quantity, which is the correct unit. The critique itself concedes the bias disappears under a GBD-style total-DALYs/total-deaths derivation. No bias is therefore demonstrated.

- **Concede the unit label.** "DALYs per TB death" is the right unit for the formula. If 27 is a death-weighted figure, this critique has no force.
- **The derivation is UNVERIFIABLE, not rejected.** The Advocate treats "the report doesn't say" as grounds for dismissal.
  - The verifier found nothing either way.
  - The Advocate's own concession says that if 27 is a patient- or population-weighted average, "the bias is real and downward in low-HIV settings."
  - So the defense does not show the bias is absent. It shows it is conditional on an undocumented step.
- **"Healthy life expectancy" does not clearly protect against this.**
  - HALE is a general-population construct, and the label suggests a life-table input.
  - A HALE-style adjustment accounts for morbidity in the average person. It does not account for the age distribution of TB decedents or for comorbidity specific to TB patients.
  - The Advocate says "some adjustment may already be built in." That is speculation of the same kind as the critique's, and it does not close the gap.
- **The residual risk is a documentation gap.** A parameter that drives roughly 100% of the benefit calculation has an undisclosed derivation with one identifiable failure mode. That is a legitimate request for transparency even if the final answer turns out to be benign.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the illustrative arithmetic is internally inconsistent. The patient-weighted mean is 29, not 27, so the example doesn't isolate the covariance effect.

- **Concede the arithmetic error.** The patient-weighted mean is 0.7×35 + 0.3×15 = 29. Comparing 23.8 to 27 mixed in an arbitrary baseline.
- **The correction goes in the critique's direction.**
  - Against the correct baseline of 29: 0.064 × 29 = 1.856, versus 1.52 for the death-weighted figure.
  - The gap is (1.856 − 1.52)/1.856 ≈ 18%, larger than the 12% originally stated.
  - The Advocate's own calculation shows this. The example was sloppy, but fixing it increases the illustrated effect.
- **The example is illustrative only.** I agree the group parameters (70/30 split, 4%/12% mortality, 35/15 DALYs) are unsourced. The example shows that the mechanism exists and can be material. It does not estimate the actual size.

> The Advocate claims: if the relative mortality reduction is uniform across subgroups, averted deaths are proportional to deaths, so the death-weighted average is correct, and no bias follows.

- **Concede conditionally.** Under a uniform relative risk reduction, the death-weighted average is the right weighting. That is a real defense.
- **The BOTEC specifies an absolute reduction (0.6 percentage points), not a relative one.**
  - Whether the benefit is uniform in relative or absolute terms across age strata is an empirical question about the statin's effect.
  - The Advocate asserts "if roughly uniform" without evidence. I cannot ground the opposite claim either, so treat it as an open question.
  - If the effect is closer to uniform in absolute terms, or concentrated in lower-risk, longer-lived patients, the weighting moves toward the patient-weighted figure and the bias reappears.
- **The Advocate partly misreads the critique's Evidence section.** The critique says the correct quantity is DALYs per averted death and that it depends on who benefits. The Advocate calls this a concession. It is a statement that the weighting depends on an unmeasured effect-heterogeneity assumption.
- **"Unsigned effect means no basis to move the estimate" is only half right.**
  - In low-HIV settings the sign is plausibly negative, and the Advocate concedes this.
  - The sign is genuinely ambiguous only in high-HIV settings, which depends on where the program is deployed.
  - An unquantified, deployment-dependent sign is a reason to document the assumption, not to dismiss it.

> The Advocate claims: the "life-table YLLs overstate for sick patients" point is a separate issue, not covariance.

- **Concede it is separate.** It is the critique's own unverified reasoning, and the Advocate concedes it is a real downward consideration. It points the same direction as the covariance concern in low-HIV settings, so the net exposure is one-sided downward there. Its size is ungrounded.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: a −10% to −15% change takes SROI from ~3,000x to ~2,550–2,700x, which is below the 25% materiality threshold and above the 2,000x bar.

- **Concede the arithmetic on the critique's own range.** On its own, this item does not cross the decision bar.
- **The range is not a grounded floor or ceiling.**
  - It comes from a flawed illustrative example.
  - With the corrected baseline (18%) and a 3,000x starting point, the result is ~2,460x.
  - That is still above 2,000x, so the conclusion survives. The cushion is smaller than the Advocate suggests.
- **The effect could be larger or smaller.** Group-parameter choices drive it. I cannot ground a different number, so treat the range as an uninformed prior bracketed by "near zero" and "~18%."
- **The Advocate has conceded two additive downward effects.** These are the covariance issue (conditional on derivation) and comorbidity overstating years gained. Neither is quantified. Their combination is more plausible than either alone, but a combined figure would be unsupported.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: omitted positive channels (morbidity DALYs, post-treatment survival, transmission, diagnostics) offset any downward adjustment, and high-HIV young-adult deaths push DALYs up.

- **The omitted-benefit offset is not an offset to this parameter.**
  - A correct estimate of DALYs per averted death should not be left biased because other benefits are omitted elsewhere.
  - Those channels are listed as implicit zeros, not quantified positives. This is the same ungrounded status the Advocate objects to in the critique.
  - Netting omitted benefits against a parameter error hides both problems.
- **The HIV offset is setting-dependent.**
  - It applies only where HIV-associated TB is a large share of deaths.
  - In low-HIV deployments, which the critique specifically scopes, it does not apply.
  - The Advocate says the critique "does not net it out." Nobody can without the deployment HIV prevalence, which is not provided here.

**KEY UNRESOLVED QUESTIONS:**
- How was 27 derived: a death-weighted YLL from GBD, a population-weighted life-table average, or something else? This one fact largely decides whether the critique has any force.
- Is the statin's benefit roughly proportional to baseline mortality (relative effect) or roughly uniform in absolute terms across age and comorbidity strata? The trial subgroup data, if any exist, would settle this.
- What is the HIV prevalence among TB patients in the intended deployment settings? It determines the sign of the offsetting factor.
- Does any HALE-style adjustment in 27 correct for TB-specific comorbidity, or only for general-population morbidity?

### Judge Audit
Surviving strength: weak
Justification: **Justification:**
- The Challenger conceded the unit label, the arithmetic error, the conditional validity of death-weighting, and that even the worst corrected case (~18%) leaves SROI above the decision bar.
- The Challenger's main attempt to revive the bias (the absolute-uniform-effect argument) has the direction wrong. Correctly analysed, that branch weakens or reverses the critique.
- The critique survives only as a request to document the derivation of 27. Its quantitative claim and its signed direction did not hold up. The Advocate's failures (the HALE speculation, the whataboutism offset, and overclaiming "no bias follows") did not rescue the critique, because the Challenger's grounded concessions did that work.
Recommended action: 1. CONCLUDE NOW** (moderate-high confidence):
- The covariance critique does not support a signed adjustment to DALYs per death.
- Its sign depends on the interaction between how 27 was derived and how the treatment effect is distributed across strata. Under at least one plausible combination (GBD death-weighted 27 with a uniform absolute effect), it would go the other way.
- Even the largest illustrative magnitude (~18%) does not cross the 2,000x bar.
- Record it as a documentation item. Add a single low-cost check: state the source of 27 and whether it is death-weighted. If a source is given, compare it with GBD 2021 TB YLLs divided by deaths for the deployment country.
- Do not apply a −10 to −15% adjustment.

**action_feasibility:** actionable_now
Action feasibility: actionable_now
Advocate failures: []
Challenger failures: []
Debate resolved: The critique has force only on a joint condition: 27 must be a patient- or population-weighted figure *and* the statin's benefit must scale with baseline mortality. Even with the corrected illustrative effect of about 18%, SROI stays around 2,460x, above the ~2,000x bar, so this item alone cannot change the decision. Both sides accepted that the critique's numbers are illustrative only and that the "12%" figure was miscomputed.
Debate unresolved: How 27 was derived, and whether the 0.6 pp benefit is uniform in absolute terms or proportional to stratum mortality, are both open. Together they determine whether the bias is zero, downward, or upward. Neither side correctly worked out the full sign matrix: the Challenger got the absolute-uniform branch backwards, and the Advocate missed it as a defense.

--- Critique: A global-average mortality may not match the countries where an atorvastatin adjunct would actually be deployed ---

### Advocate
**DEFENSE OF GIVEWELL'S POSITION: A global-average mortality may not match the countries where an atorvastatin adjunct would be deployed**

**EXISTING COVERAGE:**
- CG's population denominator is global. The ~5.5M eligible people come from current global new TB cases, with 96% drug-susceptible and a 2% annual decline.
- The model assumes 60% uptake across all adult patients, not uptake in selected countries. It therefore applies a uniform adoption assumption to a global case base.
- A global case-weighted mortality figure is the matching numerator for that denominator.
- A country-weighted mean equals the global mean whenever deployment is proportional to case share, and the BOTEC implicitly assumes that.
- Using country-specific mortality with a global denominator would be internally inconsistent. It would require a country-by-country uptake and timing model, which the critique does not propose and which would add false precision to a BOTEC.
- The parameter map notes that CG's 6% is a notified-cohort figure. It lists "unascertained deaths" as a factor that could raise true baseline mortality. This partly offsets any downward pull from low-mortality, India-heavy deployment (see offsetting factors).

**EVIDENCE WEAKNESSES:**
- The critique concedes that all country figures are UNGROUNDED and from memory. The India figure (4–5%) and the South Africa figure (8–10%) are unverified, so the mechanism rests on numbers the critique itself disclaims.
- The sensitivity results are empty. The critique does not show the global mean differing from 6% by any amount.
- The trial-site versus deployment-site gap is described as the critique's own unsourced inference.
- Accepting that inference arguendo, it concerns trial generalizability, which affects `relative_reduction`, not `baseline_mortality`. It does not bear on whether 6% is the right baseline.
- The critique does not claim 6% is wrong for the global treated cohort. It claims only that the weighting could differ, with the direction unknown.

**MAGNITUDE CHALLENGE:**
- **Breakeven.** I derive the 3.9% threshold myself. Published SROI is (54B / 7M) × 0.4 ≈ 3,086x. SROI scales linearly with `baseline_mortality`, so reaching 2,000x requires 6% × (2,000 / 3,086) ≈ 3.9%.
- **Critique's low case.** The critique's own India-dominated scenario of ~4.5% gives 3,086 × (4.5 / 6) ≈ 2,300x. That is still above the bar, and it is a reduction of about 25%.
- **Reaching the breakeven.** Pushing the weighted mean below 3.9% would require nearly all deployment to sit in countries below the lowest figure the critique cites (4%). Even the critique's recalled India range does not get there.
- **Plausibility of the low case.** An India-only mix is not plausible for a global guideline change. I cannot ground India's exact case share; treat my recollection that it is roughly a quarter of global incidence as an uninformed prior. The critique's own framing is that the weighted mean depends on the mix.
- **Symmetry.** The critique also gives a high case (>6% with a high-HIV mix) that would raise SROI. So the range is two-sided, and the downside case still clears the bar.

**OFFSETTING FACTORS:**
- **Upward pressure.** The parameter map flags that notified-cohort mortality understates true mortality because of unascertained deaths. This pushes the true baseline up, not down.
- **High-HIV settings.** Higher mortality in high-HIV settings raises the baseline. Whether statin benefit is reachable in those deaths is a `relative_reduction` question and is handled in a separate thread.
- **No "global figure" bias.** Case-weighting is already what a global figure does. The critique's proposed fix amounts to re-deriving the same quantity.

**OVERALL ASSESSMENT:** Strong defense.
- The critique is explicitly framed as a low-to-medium sensitivity flag with an unknown direction and no grounded country numbers.
- On the critique's own illustrative numbers, the low case stays above the bar.
- The global-average choice is consistent with the global denominator and uptake assumption.

**CONCESSIONS:**
- CG does not derive or cite the 6% figure (for example, from WHO Global TB Report cohort outcomes). The critique's suggested check, pulling death share among evaluated cases for the top 5–8 countries, would be a cheap and legitimate verification.
- If deployment were concentrated in a low-mortality country mix near 4%, SROI would approach the 2,000x bar. That scenario is implausible, but I cannot rule it out from grounded evidence.
- The trial-population versus deployment-population gap is a real generalizability question. It belongs with `relative_reduction`, not this parameter.

### Challenger
REBUTTAL: A global-average mortality may not match the countries where an atorvastatin adjunct would actually be deployed

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: a global-average mortality is the matching numerator for CG's global denominator, so using it is internally consistent and the country-weighted mean equals the global mean under proportional deployment.

- **The argument assumes the 6% is a global case-weighted mean of on-treatment death.** The Advocate concedes that CG "does not derive or cite the 6% figure." Consistency between numerator and denominator can't be established for a number with no stated provenance. The defense assumes the very thing the critique's suggested check would test.
- **The parameter map describes the 6% as a "notified-cohort figure."** That says what population it covers. It does not say it was built by weighting country cohort outcomes by case share. It could be a trial figure, a single-country figure, or a rounded global figure. The Advocate treats "global-average" as a settled property, but the evidence only says it is a notified-cohort number.
- **The proportional-deployment premise is itself an assumption.** The 60% uniform uptake is one input. Real adoption of an adjunct depends on guideline adoption, procurement, and national program decisions, which are heterogeneous. If uptake is uncorrelated with country mortality, the global mean holds. If it is correlated, it doesn't. Neither side has data on this.
- **The "unascertained deaths" offset is flagged but not quantified.** Being listed as a factor that could raise mortality is not the same as being in the model. I address this further under offsetting factors.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the country figures are self-disclaimed as ungrounded, the sensitivity results are empty, and the trial-versus-deployment gap belongs to `relative_reduction`.

- **Concession.** The India (4–5%) and South Africa (8–10%) figures are unverified recollections, and the critique says so. The mechanism can't be shown to move the number from the evidence in hand.
- **The verifier's status is UNVERIFIABLE, not REJECTED.** "Nothing directly supports or refutes the country figures." The Advocate's phrasing ("rests on numbers the critique itself disclaims") is fair as far as it goes. It must not be read as evidence that the figures are wrong. The question is conditional: if country on-treatment mortality does vary by a factor of about 2 across high-burden settings, as the critique's recalled figures imply, does a single unsourced 6% become a material input? It does, because of the next point.
- **Elasticity is 1.0 and the input is unsourced.** On the Advocate's own derivation, SROI ≈ 3,086x at 6%, so each percentage point of baseline mortality is worth about 3,086/6 ≈ 514x, or ~17% of the headline. An unsourced input with unit elasticity is where a cheap verification is most valuable. The Advocate concedes this check is "cheap and legitimate."
- **The trial-site gap is only partly a `relative_reduction` issue.**
  - Part of it is a `relative_reduction` transport question, and I concede that.
  - If the 6% was informed by trial-population or single-setting mortality, the gap sits directly in the baseline parameter. The Advocate can't rule this out because the 6% has no provenance.
  - If a statin's effect depends on the composition of deaths (for example inflammatory or pulmonary versus HIV-related), the baseline and the relative effect aren't separable by country. The Advocate's own phrase that "statin benefit [may not be] reachable in those deaths" concedes this coupling.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: the critique's own low case (~4.5%) still gives ~2,300x, above the 2,000x bar, and the range is two-sided.

- **I accept the arithmetic.** 3,086 × 4.5/6 ≈ 2,315x.
- **A 25% haircut leaves a thin margin.** The remaining buffer is about 15% above the bar. The 3.9% breakeven is just 35% below 6%. Any other parameter that moves adversely (for example `relative_reduction` or uptake) consumes that margin. The Advocate evaluates this parameter in isolation, but the bar is crossed jointly.
- **The 4.5% figure is derived from ungrounded recollections.** That cuts both ways. The Advocate's claim that the low case "stays above the bar" rests on numbers neither side can verify, and the Advocate has no grounded floor either. Their own concession is that a mix near 4% would approach the bar and "I cannot rule it out from grounded evidence."
- **The Advocate's "India-only isn't plausible" is an uninformed prior.** They disclaim it themselves ("treat as uninformed prior"). The critique never needs India-only. A heavily India-weighted mix with some other low-mortality settings could approach the low case, and neither side has grounded the shares.
- **The symmetry argument is weaker than it looks.**
  - Higher baseline mortality in high-HIV settings may not translate into more avertable deaths. The Advocate says statin benefit reachability there is a separate `relative_reduction` question.
  - So the upside branch (>6%) is plausibly discounted by that same question, while the downside branch (low-mortality settings) passes through at close to full proportion.
  - The range is nominally two-sided, but the realized effect may be skewed downward. This is my own reasoning and is not quantified.
- **Minimum defensible impact.** If the 6% is already a correct global case-weighted mean, the impact is near zero. I can't exclude that, and the Advocate can't establish it. The residual is an unverified parameter whose plausible error band has the headline above the bar by only ~15–50%.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: unascertained deaths push true mortality above notified-cohort figures, offsetting any downward pull from India-heavy deployment.

- **The offset is not shown to be in the model.** The parameter map lists it as a factor that could raise baseline mortality, but the Advocate gives no magnitude and no indication that CG adds an adjustment. An unquantified directional note can't be netted against a quantified low case.
- **It may apply asymmetrically.** Unascertained deaths (loss to follow-up, unevaluated cases) are likely concentrated in weak-reporting settings. Whether those deaths are avertable by an in-treatment adjunct is questionable, because patients lost from care don't receive it reliably. I can't ground this, so treat it as a conditional concern: if unascertained deaths are mostly among those who would never receive the adjunct, the offset doesn't apply to the treated cohort.
- **"Case-weighting is already what a global figure does" is circular.** It assumes the 6% was built by case-weighting. That is the claim in dispute and has no provenance.

**KEY UNRESOLVED QUESTIONS:**
- What is the source of CG's 6%? Is it a WHO Global TB Report cohort-outcomes aggregate, a trial figure, or a rounded estimate? A case-weighted calculation from the top 5–8 countries' death share among evaluated cases would settle whether the global mean is near 6%.
- Is deployment plausibly proportional to case share, or is uptake correlated with country mortality?
- Are unascertained deaths avertable in a treated cohort, and does CG apply any adjustment for them?
- Does the effect of statins depend on the composition of deaths? If so, `baseline_mortality` and `relative_reduction` can't be varied independently by country mix.
- What is the joint margin once adverse moves in other parameters are combined with a lower baseline? A 15% buffer under the low case is small relative to typical BOTEC uncertainty.

### Judge Audit
Surviving strength: moderate
Justification: - The Advocate's grounded breakeven synthesis effectively defeated the critique's quantitative threat: on the critique's own illustrative numbers, the bar is not crossed.
- The Challenger did not produce any grounded scenario below 3.9%. Several of its supporting moves were speculative, including provenance alternatives, downside asymmetry, and the joint-margin appeal.
- However, the Challenger's elasticity point (~17% of headline per percentage point on an unsourced input) is sound. It exposed that the Advocate's "global figure is already case-weighted" claim rests on an unverified assumption, which the Advocate partly conceded.
- What survives is a well-founded sensitivity flag with a cheap resolution path, not a demonstrated bias. That sits at the low end of moderate.
Recommended action: 2. SPECIFIC INVESTIGATION:

**Data to pull.** From the WHO Global TB Report treatment-outcome data (the WHO TB data portal outcomes dataset is publicly downloadable), pull the percentage "died" among new and relapse cases in the most recent reported cohort for:
- the global aggregate
- the top 8 countries by incidence: India, Indonesia, China, Philippines, Pakistan, Nigeria, Bangladesh, DR Congo
- South Africa, as a high-HIV comparator

**Calculation.** Compute the case-weighted mean and compare it with CG's 6%.

**Decision rule.**
- If the weighted mean falls within roughly 5–7.5%, close the critique as resolved.
- If it falls below ~4.5%, escalate. The margin to the 3.9% breakeven would then be under ~15% and would warrant revisiting jointly with `relative_reduction`.

**Feasibility.** This is a single public dataset and a short spreadsheet calculation, so it is feasible within existing tooling.

**Conclusion available now (moderate confidence).** On the critique's own figures, the deployment-mix mechanism does not push SROI below the bar. The critique should be retained only as a provenance check on the 6%, not as a magnitude adjustment.
Action feasibility: requires_specified_evidence
Advocate failures: ['sound_synthesis_noted: Breakeven derivation: "(54B / 7M) × 0.4 ≈ 3,086x … 6% × (2,000 / 3,086) ≈ 3.9%". The low case is "3,086 × (4.5 / 6) ≈ 2,300x." Every step is shown, and the linear-elasticity premise is stated. The Challenger accepted the arithmetic. This is the most productive move in the debate.', 'false_definitiveness: Case-weighting is already what a global figure does. The critique\'s proposed fix amounts to re-deriving the same quantity." This treats the 6% as a known case-weighted global mean. The Advocate\'s own concession says CG "does not derive or cite the 6% figure." The Challenger correctly identified the circularity.', 'false_definitiveness: The "unascertained deaths" factor is presented as something that "partly offsets any downward pull." It is given no magnitude and no evidence that CG applies any adjustment. A directional note from the parameter map is treated as a netting term.', 'false_definitiveness: The self-assessment is "Strong defense," yet the concessions admit the core input is unsourced and that a ~4% scenario "cannot [be ruled] out from grounded evidence." The defense is solid on magnitude. It is not strong on provenance, which is where the critique\'s residual value lies. I assess it as partial-to-strong, not strong.']
Challenger failures: ['sound_synthesis_noted: each percentage point of baseline mortality is worth about 3,086/6 ≈ 514x, or ~17% of the headline." The margin figures are also correct: "The 3.9% breakeven is just 35% below 6%" and the buffer is ~15% at 4.5% versus ~54% at 6%. These follow from the agreed derivation and make the value-of-information case well.', 'call_to_ignorance: It could be a trial figure, a single-country figure, or a rounded global figure" and "If the 6% was informed by trial-population or single-setting mortality, the gap sits directly in the baseline parameter.', 'strawmanning: The Advocate\'s own phrase that \'statin benefit [may not be] reachable in those deaths\' concedes this coupling." The Advocate actually wrote "Whether statin benefit is reachable in those deaths is a `relative_reduction` question." The Advocate posed a question and assigned it to another parameter. The bracketed edit turns that into an admission.', 'whataboutism: Any other parameter that moves adverse (for example `relative_reduction` or uptake) consumes that margin … the bar is crossed jointly." Joint uncertainty is real. But this imports unquantified weaknesses in other parameters to inflate this parameter\'s importance. It does not engage with whether this critique\'s mechanism moves this parameter.', 'call_to_ignorance: the upside branch (>6%) is plausibly discounted … while the downside branch … passes through at close to full proportion. … the realized effect may be skewed downward.', 'sound_synthesis_noted (evidence status handled correctly): The verifier\'s status is UNVERIFIABLE, not REJECTED … The question is conditional." This correctly distinguishes evidence statuses and engages the claim conditionally.']
Debate resolved: - Both sides agree on the arithmetic:
  - `baseline_mortality` has unit elasticity on SROI.
  - The breakeven is ≈3.9%.
  - The critique's own low-case scenario (~4.5%) yields ≈2,300x, which still clears the 2,000x bar.
- Both sides agree that CG's 6% has no stated derivation, and that the critique's proposed WHO cohort-outcome check is cheap and legitimate.
Debate unresolved: - Whether CG's 6% is in fact a case-weighted global on-treatment death share, or a figure of different origin, is unresolved.
- Also unresolved: whether real-world deployment would be roughly case-proportional or correlated with country mortality.
- The Challenger's claim that baseline and relative effect are coupled by death composition was raised but neither grounded nor refuted.

--- Critique: Industry phase-transition base rates put "II and III both succeed" at roughly 15–25%, so 40% requires an unstated premium of about 1.6–2.7× ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: Industry phase-transition base rates put
"II and III both succeed" at roughly 15–25%, so 40% requires an unstated premium
```

**EXISTING COVERAGE:**

- CG states 40% as a single probability that "Phase II and Phase III trials both succeed". The parameter map confirms no reference class, decomposition, or definition of success is given. I do not claim an explicit adjustment exists.
- The structure of the BOTEC offers partial coverage of the adoption-risk piece. Uptake is set at 60% "if it works", and the map notes adoption "may be partly captured in uptake."
- The critique's decomposition multiplies by P(adopted | III) ≈ 0.7–0.85 on top of this uptake assumption. That risks double-counting. Uptake is already a haircut on the benefit side for imperfect real-world adoption.
- The Phase IIc trial is an additional step after a Phase IIa/b that already showed a signal. The CG context describes the Phase IIc as testing "dosing strategies", not as a first test of whether the drug works.

**EVIDENCE WEAKNESSES:**

1. **Wrong reference class for the starting point.**
   - The BIO 2011–2020 transition rates (~29% Phase II→III, ~58% Phase III→filing, per the Verifier-corroborated figures) are pooled across all indications and mostly novel molecular entities.
   - For those drugs, Phase II is typically the first efficacy test in patients.
   - Atorvastatin is a generic drug with decades of human safety data. A prior Phase IIa/b already showed an effect on infection clearance and lung damage.
   - The critique's own Phase IIc estimate (0.5, versus the 29–40% industry rate) concedes this. That concession shows the raw 17% figure is not the right anchor.

2. **Attrition causes differ for repurposed drugs.**
   - From memory, and not verified here: Harrison (2016, *Nat Rev Drug Discov*, Phase II/III failures 2013–2015) and Sun et al. (2022, *Acta Pharm Sin B*) attribute roughly half of late-stage failures to lack of efficacy and a quarter to a third to safety or toxicity.
   - A well-characterized generic removes much of the safety share. That is a conditional argument, not a measured premium for repurposing.
   - The critique labels the repurposing premium UNGROUNDED. I accept that and cannot ground a numeric premium either. The point is that the unadjusted base rate is biased downward for this drug class, by an amount neither side can currently quantify.

3. **The infectious-disease uplift cuts against the critique's own range.**
   - The Verifier found infectious-disease and anti-infective programs perform above average. At least one dataset shows Phase III success above 80%.
   - If Phase III|IIc is 0.6–0.8 rather than 0.40–0.55, then 0.5 × 0.7 = 0.35, close to CG's 0.40.
   - The critique's 0.40–0.55 for Phase III is its own inference and contradicts its own Verifier note. It is not drawn from a source.

4. **"Approval" is not the model's endpoint.**
   - The BIO figures measure progression to filing or approval. CG's "success" plausibly means a positive trial result, which could include a surrogate or dose-finding result.
   - A different definition of success moves the base rate in either direction. The critique's 15–17% figure is therefore not a like-for-like benchmark for CG's 40%.

5. **The decomposition is self-described as unsourced, and its arithmetic is loose.**
   - The stated components multiply as follows:
     - Low end: 0.5 × 0.40 × 0.70 = 0.14.
     - High end: 0.5 × 0.55 × 0.85 ≈ 0.23.
   - The stated upper bound of 0.30 does not follow from the stated component ranges. It would require P(IIc) of about 0.65.
   - The central ~0.20 depends on the adoption factor I argued above may be double-counted.

**MAGNITUDE CHALLENGE:**

1. **Break-even.** SROI = 3,000 × (p / 0.40), so break-even at 2,000x is p ≈ 0.267. This matches the critique's 0.26.

2. **Dropping the adoption factor.** If adoption risk is largely handled by the 60% uptake assumption:
   - P(IIc) × P(III | IIc) = 0.5 × (0.40 to 0.55) = 0.20–0.275, with a midpoint of ~0.24.
   - That is within about 10% of the break-even point, not 50% below CG's 0.40.

3. **A modestly higher Phase IIc rate crosses break-even.**
   - Say a PK/dose-selection trial after a positive IIa/b has P(IIc) = 0.65. I cannot ground this; it is a sensitivity test, not a claim.
   - Then 0.65 × 0.475 ≈ 0.31, above the 0.267 break-even.
   - The critique's conclusion therefore depends on a single ungrounded input (P(IIc) = 0.5) that has no more support than CG's 0.40.

4. **The critique's own range straddles the threshold.** It states 20–32% for the infectious-disease-adjusted estimate, which "brackets the 0.26 break-even rather than clearly falling below it." The headline claim that 0.40 requires a 1.6–2.7× unstated premium uses unadjusted base rates, which the critique itself says are not the right anchor. Against the adjusted range, the implied premium is 1.25–2×.

5. **Linearity is accepted.** A move from 0.40 to 0.25 cuts expected SROI by about 37%. The mechanism is correct; the dispute is only about the input.

**OFFSETTING FACTORS:**

- The BOTEC values only on-treatment mortality. The parameter map lists implicit zeros for morbidity DALYs, post-treatment mortality, transmission averted, and diagnostic value. These are upside terms.
- If statin-induced lung-damage reduction translates into long-term survival, the benefit conditional on success is understated. This partially offsets a lower p_success, though it also depends on the same p_success.
- The sweat-diagnostic workstream is not in the benefit stream at all, so it is also a source of upside.
- None of these offsets is quantified in the CG text. They are directional only.

**OVERALL ASSESSMENT:** Partial defense.

- The critique correctly identifies that the 40% has no stated reference class. It also correctly notes that taken alone, the BIO base rates are well below 40%.
- Its strongest result, that 40% is above the unadjusted base rate, does not by itself show that 0.40 is wrong. The adjusted range it ends up with (20–32%) straddles break-even.
- The adjusted range relies on a self-described own inference, an unsourced P(IIc) of 0.5, a P(III|IIc) range that conflicts with the Verifier's infectious-disease finding, and an adoption haircut that likely overlaps with the uptake parameter.
- I cannot defend 0.40 as well-founded. The honest position is that 0.40 is probably somewhat high, with a more defensible range of about 0.25–0.35.

**CONCESSIONS:**

1. CG gives no reference class, decomposition, or definition of success for the 40%. This is a real transparency gap.
2. Unadjusted industry base rates are well below 40%, and the direction of the critique (0.40 is likely too high) is plausible.
3. "Approval" is not "adopted at scale in LMICs." Some adoption risk beyond the 60% uptake factor probably exists, so the double-counting argument is partial.
4. A central estimate near 0.25–0.30 is defensible. That would reduce SROI to about 1,900–2,250x, which straddles the 2,000x bar. The critique is therefore decision-relevant, even though its stated central value of ~0.20 is not well supported.

### Challenger
REBUTTAL: Industry phase-transition base rates put "II and III both succeed" at roughly 15–25%, so 40% requires an unstated premium

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: The 60% uptake parameter already haircuts the benefit side for imperfect adoption, so multiplying p_success by P(adopted | III) ≈ 0.7–0.85 risks double-counting.

Response:
- The parameter map says adoption "may be partly captured" in uptake. That is a hedge, not a finding. The Advocate concedes in Concession 3 that some adoption risk beyond uptake probably exists.
- The two parameters plausibly measure different things:
  - Uptake given "it works" is a coverage fraction among eligible patients.
  - P(adopted | III) is whether guideline, procurement, or WHO adoption happens at all.
  - The first is an intensive margin and the second an extensive margin. Whether CG intended 60% to include the second is unresolved, so double-counting is a possibility, not an established flaw.
- The critique's own range is not hostage to this point. The Advocate's computation without the adoption factor is 0.20–0.275, midpoint ~0.24. That is still below the 0.267 break-even.
- The adoption factor therefore moves the central estimate from below break-even to further below. It does not move it from above to below.

> The Advocate claims: The Phase IIc follows a positive IIa/b and tests "dosing strategies," so it is not a first efficacy test.

Response:
- The critique already priced this in. Its P(IIc) = 0.5 sits above the 29–40% industry Phase II rate precisely because the trial is PK/dose-selection.
- Citing repurposing status to say the raw 17% is the wrong anchor re-applies an adjustment the decomposition has already made. The critique never anchors on 17%; it uses 17% to show the size of the unstated premium.
- If the Phase IIc is easy to pass, the residual risk shifts to Phase III. The IIa/b signal was on infection clearance and lung damage. Those are intermediate measures, and a Phase III endpoint is presumably clinical.
- I cannot ground a surrogate-to-clinical translation rate for this case. It is a conditional risk that the "already showed a signal" argument does not remove.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: Attrition causes differ for repurposed drugs, since a well-characterized generic removes the safety share of failures. This is from memory (Harrison 2016, Sun et al. 2022) and is explicitly unverified.

Response:
- I accept the Advocate's figures conditionally. The Advocate itself says they are unverified.
- Phase II derivation:
  - Phase II failure is 1 − 0.29 = 0.71 (BIO).
  - If 25–33% of failures are safety and a generic eliminates all of them, failure is 0.71 × (0.67–0.75) = 0.48–0.53.
  - Success is therefore about 0.47–0.52.
- This lands on the critique's P(IIc) = 0.5. On the Advocate's own numbers, the critique's input is already the ceiling of the safety-removal argument, not a pessimistic choice.
- Phase III derivation:
  - Phase III failure is 1 − 0.58 = 0.42.
  - Removing 25–33% of it gives success of about 0.69–0.72.
  - Combined with 0.5, that is about 0.35.
- Two things follow:
  - **Concession:** this is the most favorable repurposing reading. It still yields about 0.35, below 0.40 (SROI ≈ 2,625x, above the bar). The decision does not flip at that bound.
  - **Gap:** it assumes zero safety failures. In a TB population that is optimistic. Rifampicin's CYP3A4 induction lowering statin exposure is general pharmacology that I have not verified in the evidence package. It is the kind of issue a dose-selection Phase IIc exists to address.
- Reaching 0.40 requires roughly P(III | IIc) ≈ 0.8 if P(IIc) = 0.5. That is the top of the single high dataset the Verifier found, and well above the 58% all-indication Phase III→filing rate.

> The Advocate claims: The infectious-disease uplift pushes P(III | IIc) to 0.6–0.8, so 0.5 × 0.7 ≈ 0.35, close to CG's 0.40, and this contradicts the critique's 0.40–0.55.

Response:
- Concede that the critique's 0.40–0.55 is its own inference.
- The Advocate's 0.6–0.8 is equally unsourced. The Verifier said only "above-average," with a very high late-stage rate in at least one dataset. That does not establish 0.6–0.8 for a host-directed repurposed therapy in TB.
- Anti-infective datasets are dominated by pathogen-directed agents. I cannot ground whether the uplift transfers to host-directed therapy. That is a gap in the evidence, not a rejection of either side.
- The Advocate's "close to 0.40" is 12.5% below 0.40. This reinforces that 0.40 is not reached even in the favorable case.

> The Advocate claims: "Approval" is not the model's endpoint, so the BIO figures are not a like-for-like benchmark. CG's "success" may mean a positive trial result.

Response:
- The headline 17% product uses Phase II→III and Phase III→filing, not approval. Approval (~15%) is a secondary figure.
- Phase III→filing is close to "positive pivotal result."
- To the extent the definition differs from the BIO endpoint, the model's likely endpoint (LMIC adoption, per the Verifier) is further downstream. That pushes the benchmark down, not up.
- Ambiguity in CG's definition is a transparency problem, which both sides concede. It does not support the direction of 0.40.

> The Advocate claims: The decomposition's arithmetic is loose, because the stated components give 0.14–0.23, not 0.14–0.30.

Response:
- Concede the arithmetic. The 0.30 upper bound does not follow from the stated component ranges.
- The correction makes the stated decomposition wholly below the 0.267 break-even (0.14–0.23). That helps the critique's direction. The Advocate's point costs the critique only its upper bound.
- The critique's "20–32%" adjusted range is therefore looser than its own components warrant. The components alone yield 0.14–0.23, or 0.20–0.275 without the adoption factor.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: P(IIc) = 0.65 would give 0.31, above break-even, so the conclusion hinges on one ungrounded input.

Response:
- The Advocate labels 0.65 a sensitivity test, not a claim. As a sensitivity test it shows break-even is fragile in both directions. It is not evidence that 0.65 is plausible.
- 0.65 is more than twice the BIO Phase II rate (29%) and above the Advocate's own safety-removal ceiling of ~0.52 (derived above).
- Minimum defensible magnitude, using the Advocate's own most favorable inputs: 0.35. That is a 12.5% reduction in SROI, to about 2,625x.
- The Advocate's concession is about 0.25–0.30 central, giving about 1,900–2,250x. That straddles the bar.
- Under that central estimate, any residual adoption risk beyond the 60% uptake pushes it below the bar. The Advocate concedes such risk exists. That makes the break-even crossing the more probable outcome.
- The Advocate's reduced "implied premium" of 1.25–2× is still a premium CG never stated or justified.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: Implicit zeros (morbidity, post-treatment mortality, transmission, diagnostics) are unquantified upside that partially offsets a lower p_success.

Response:
- These offsets are directional only, as the Advocate admits. They are not in the model and not quantified, so they cannot be netted against a quantified 37–50% cut.
- The post-treatment-mortality and lung-damage upside is conditional on success. It scales with p_success, so a lower p_success shrinks it proportionally.
- The sweat-diagnostic workstream is a separate benefit stream. It does not offset the statin success probability.
- The implicit zeros reflect conservatism about unmodeled benefits. They are not a calibrated hedge against one optimistic input.
- I cannot show that conservatism and the optimistic p_success cancel.

**KEY UNRESOLVED QUESTIONS:**
- Does CG's 60% uptake already include the probability of guideline or procurement adoption, or only coverage conditional on adoption? This determines whether the adoption factor is double-counting.
- Does the above-average infectious-disease Phase III rate (one dataset above 80%) transfer to host-directed repurposed therapy in TB? The Verifier did not establish this either way.
- What does CG mean by "success" for Phase IIc: a positive PK/dose result, or a trial that advances to Phase III? This changes P(IIc) substantially.
- Do the IIa/b intermediate signals (clearance, lung damage) translate to a clinical Phase III endpoint? Neither side has data.

### Judge Audit
Surviving strength: moderate
Justification: - **What survived:** The critique's direction withstood a genuinely grounded test. The Challenger's safety-removal synthesis, built from the Advocate's own conditional figures, could not get above ~0.35. The Advocate conceded that a 0.25–0.30 central estimate is decision-relevant.
- **What did not survive:** The critique's magnitude claims were cut back substantially:
  - The central value of ~0.20 rests on the contested adoption factor and on an internally inconsistent Phase III input.
  - The 0.30 upper bound was shown to be arithmetically unsupported.
  - The 1.6–2.7× premium shrinks to about 1.25–2× against the adjusted range.
- **Why not stronger or weaker:** Both sides produced sound syntheses alongside some unsupported counter-estimates (the Advocate's 0.6–0.8; the Challenger's "ceiling" and "more probable" framings). The debate was substantive but left the decisive break-even question open.
Recommended action: 1. CONCLUDE NOW: Treat CG's 0.40 as moderately optimistic and lacking a reference class.
   - A defensible working range is about 0.25–0.35 (central ~0.30). This implies SROI of roughly 1,875–2,625x, which straddles the 2,000x bar.
   - The critique's directional claim stands with moderate-to-high confidence.
   - Its quantitative claims should not be adopted: the central value of 0.20, the 0.14–0.30 range, and the 1.6–2.7× premium.
   - Report the program as near-threshold and sensitive to p_success, not as clearly below the bar.
   - One targeted check would materially sharpen this: confirm from CG's model notes whether the 60% uptake is conditional on guideline/WHO adoption, and how Phase IIc "success" is defined. This is a document lookup and is feasible now. It decides whether the 0.7–0.85 adoption factor applies, which is what moves the estimate across break-even.
Action feasibility: actionable_now
Advocate failures: ['unsupported_estimate_counter: If Phase III|IIc is 0.6–0.8 rather than 0.40–0.55, then 0.5 × 0.7 = 0.35, close to CG\'s 0.40." The Verifier said only "above-average" with "at least one dataset" above 80% for Phase III. That supports an upward move. It does not ground a 0.6–0.8 range for a host-directed repurposed TB therapy. This number is offered to neutralize the critique\'s equally unsourced 0.40–0.55, and the Challenger correctly flagged it.', 'unsupported_estimate_pseudo: The honest position is that 0.40 is probably somewhat high, with a more defensible range of about 0.25–0.35.', 'misrepresenting_evidence_status: The Advocate says the critique\'s 0.40–0.55 "contradicts its own Verifier note." The Verifier said the infectious-disease data "move the reasonable range up." It did not establish a specific Phase III value that 0.40–0.55 contradicts. "In tension with" would have been accurate; "contradicts" overstates it. This is minor.', 'sound_synthesis_noted: Three pieces of reasoning are sound:']
Challenger failures: ['sound_synthesis_noted: The safety-removal derivation is transparent and grounded.', 'false_definitiveness: On the Advocate\'s own numbers, the critique\'s input is already the ceiling of the safety-removal argument." It is a ceiling only for that single channel, and only if the BIO Phase II rate is the right base. A dose-selection IIc that follows a positive IIa/b is not a standard Phase II. Commercial and strategic attrition is also ignored. Calling 0.35 "the most favorable repurposing reading" overstates what the derivation shows.', 'misrepresenting_evidence_status: Reaching 0.40 requires roughly P(III | IIc) ≈ 0.8... That is the top of the single high dataset the Verifier found." The Verifier reported Phase III success *above* 80% in that dataset. So 0.8 is at or below that figure, not "the top" of it. This framing makes 0.40 sound less attainable than the evidence package indicates.', 'false_definitiveness: Any residual adoption risk beyond the 60% uptake pushes it below the bar... That makes the break-even crossing the more probable outcome." Earlier in the same rebuttal, the Challenger called the uptake/adoption overlap "unresolved" and "a possibility." It then uses that unresolved residual to assert which side of break-even is more probable, without quantifying it.', 'call_to_ignorance: The Challenger invokes the rifampicin CYP3A4 interaction (self-flagged as unverified) to argue that assuming zero safety failures is optimistic. This is speculation filling an evidence gap. It is also a partial category slip: reduced statin exposure is an efficacy and dosing problem, not a safety-attrition problem. The Challenger half-acknowledges this ("the kind of issue a dose-selection Phase IIc exists to address"). This is low severity.']
Debate resolved: Both sides agree on four points:
- CG's 0.40 has no stated reference class, decomposition, or success definition.
- The critique's own components multiply to 0.14–0.23, not up to 0.30.
- Its headline "1.6–2.7× premium" relies on unadjusted base rates it concedes are the wrong anchor.
- Even the most favorable grounded-arithmetic reading (the safety-removal synthesis, ~0.35) lands below 0.40.

The debate therefore established the *direction* of the critique: 0.40 is likely somewhat high. It also established that the plausible central range (~0.25–0.35, roughly 1,900–2,600x SROI) straddles the 2,000x bar rather than sitting clearly below it.
Debate unresolved: Whether the true value falls above or below the ~0.267 break-even remains contested. It hinges on three questions:
- Does CG's 60% uptake already include guideline and procurement adoption (the double-counting question)?
- Does the high infectious-disease Phase III rate transfer to a host-directed repurposed therapy?
- Does CG's "success" for the Phase IIc mean a positive PK/dose result or progression to Phase III?

The critique's own Phase III input is internally inconsistent with its stated upward adjustments. Neither side resolved this.

--- Critique: The TB-specific reference classes (host-directed therapy, adjunctives, regimen-shortening) have a much worse record than 40% ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: TB-specific reference classes imply p_success well below 40%
```

**EXISTING COVERAGE:**

- **The 40% is a joint probability.**
  - CG's BOTEC applies it to "Phase II and Phase III trials both succeed," so it is already a compounded two-stage figure.
  - It already applies a 60% haircut to the headline benefit.
  - The expected relative mortality reduction is therefore 0.40 × 10% = 4%.
- **The input is not a cold-start compound.**
  - The grant follows a Phase IIa/b trial that was positive on clearance and chest X-ray lung damage.
  - The 40% is conditional on that signal, not on a generic TB drug candidate.
  - A TB-wide failure rate across all adjunct or shortening programs, including those without a positive Phase II, is therefore not the right comparator.
- **The critique accepts that the shortening class is heterogeneous.**
  - It concedes the negative results came from simple fluoroquinolone substitution, while rifapentine plus moxifloxacin (Study 31) succeeded.
  - That concession undercuts treating "TB-specific" as a single low-success reference class.

**EVIDENCE WEAKNESSES:**

1. **The critique's own analogue tally is consistent with 40%.**
   - Successes named: Study 31, SHINE, and dexamethasone in TBM overall (RR 0.69). That is 3.
   - Failures named: REMoxTB, OFLOTUB, RIFAQUIN, and ACT HIV (null, HR 0.85, P = 0.22). That is 4.
   - 3/7 ≈ 43%.
   - This is a convenience sample, not a systematic reference class, and "success" is defined differently across trials. I offer it only to show that the cited evidence does not point clearly below 40%.
2. **The critique labels its own low numbers ungrounded.**
   - It says the 10–20% rate is "UNGROUNDED" and that no quantitative success rate for TB host-directed therapy is available.
   - The 0.10–0.25 range is described as "my inference," and the 0.2–0.3 blend as "also inferential."
   - It rates its own strength "medium, not large, until a sourced class rate exists."
   - On its own terms, the critique has not displaced 40%. It has shown that 40% is also unsourced.
3. **The fluoroquinolone analogues are the wrong design.**
   - REMoxTB, OFLOTUB and RIFAQUIN were non-inferiority trials of shortened regimens against a highly effective standard of care. The bar was matching a regimen that already cures about 95% of patients in trials.
   - The statin trial adds an adjunct to standard therapy and tests superiority on survival or surrogates.
   - The two designs fail for different reasons, so the former's failure rate transfers imperfectly.
4. **The dexamethasone sequence is mixed, not a clear failure.**
   - It was positive overall in TBM, null in HIV-positive adults, and ambiguous in the genotype-stratified trial.
   - It shows heterogeneity, not a failed drug.
   - CG's population is 96% drug-susceptible patients with a 60% uptake assumption, so a benefit confined to HIV-negative or particular subgroups would reduce effect size more than it would zero out success.
5. **Vitamin D and statin-preclinical claims are self-flagged "unchecked, plausible."** They should carry no weight here.

**MAGNITUDE CHALLENGE:**

- **The break-even is a specific threshold.**
  - Baseline SROI is about 3,055x at p = 0.40. SROI is linear in p_success.
  - SROI falls below 2,000x only when p < 0.40 × 2,000 / 3,055 ≈ 0.26.
  - The critique's blended range of 0.2–0.3 straddles that threshold. Its upper half does not cross the bar.
- **The Quantifier's central case does not move.**
  - The sensitivity output shows central = baseline (3,055x, `crosses_bar_central: false`).
  - Only the low case (p = 0.20, SROI ≈ 1,527x) crosses.
  - The decision-relevant claim therefore rests on the unsourced 10–20% end.
- **A defensible counter-range is narrow and still weakly grounded.**
  - If I weight the critique's blended range of 0.2–0.3 and the 3/7 tally of ~0.43 equally, the midpoint is about 0.33. That is a 17.5% reduction from 0.40, below the 25% materiality threshold.
  - This is a synthesis of two inferential figures, not a sourced estimate.
  - I do not claim 0.33 is the true value. My claim is that the evidence does not support moving far from 0.40 in either direction.

**OFFSETTING FACTORS:**

1. **Upside channels that the BOTEC leaves out.**
   - Only on-treatment mortality is valued.
   - The following are all zero in the model: morbidity DALYs from lung damage (the Phase IIa/b endpoint), post-treatment mortality, transmission averted, and the sweat-diagnostic value.
   - These are not reflected in p_success, but they offset the SROI impact of a lower p_success.
2. **The drug is generic, cheap and well characterized.** This lowers development and adoption barriers relative to a novel TB agent.
3. **Ambiguity about "success" cuts both ways.**
   - If success includes a clearance or lung-damage surrogate that supports guideline inclusion, then 40% may be conservative relative to a strict mortality endpoint.
   - The critique treats the TB-class prior as applying to a mortality-powered result, which is a stricter definition.

**OVERALL ASSESSMENT:** **Partial defense.**

- The critique is not ungrounded in direction. TB drug development has real attrition, and surrogate-to-clinical failures such as the fluoroquinolone trials are relevant to a statin trial built on clearance and X-ray surrogates.
- The critique rests on no sourced class rate.
- Its own analogue list is roughly balanced.
- Its central sensitivity case does not cross the bar.
- It needs p < ~0.26 to change the decision, and the evidence for that range is the same kind of unsourced inference it faults CG for.
- The defense is only partial because CG's 40% is equally unsourced, so I cannot show 40% is better than 25%.

**CONCESSIONS:**

1. The 40% has no stated reference class, and the critique is right that CG has not shown one.
2. The fluoroquinolone failures are a valid warning about moving from a positive surrogate result to a clinical endpoint, which is the path this grant depends on.
3. The dexamethasone sequence is a valid caution that effects may be heterogeneous and may not generalize, for example to HIV-positive patients.
4. A p_success of 0.20–0.25 is plausible and would bring SROI to or below the ~2,000x bar. I cannot rule it out.
5. The tail risk is real but not demonstrated. It supports a request to document the reference class, not a conclusion that the grant falls below the bar.

### Challenger
REBUTTAL: TB-specific reference classes imply p_success well below 40%

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the 40% is already a two-stage joint probability, conditioned on a positive Phase IIa/b signal, so a TB-wide attrition rate is the wrong comparator.

- **Surrogate-positive Phase II is the situation the TB failures arose from.**
  - The fluoroquinolone shortening trials were also launched on favorable earlier surrogate data. As I recall from background knowledge, not from the verifier package, moxifloxacin improved 2-month culture conversion in Phase II work (Dorman 2009; Conde 2009). REMoxTB, OFLOTUB and RIFAQUIN then failed non-inferiority (Gillespie 2014, Merle 2014, Jindani 2014). I hold this at moderate confidence.
  - The Advocate concedes this (Concession 2): the fluoroquinolone failures are "a valid warning about moving from a positive surrogate result to a clinical endpoint, which is the path this grant depends on."
  - So "conditional on a positive Phase II" does not separate this grant from the failing analogues. It places it among them.
- **"Already compounded" is not "already adjusted for TB."**
  - The Advocate concedes (Concession 1) that the 40% has no stated reference class. A joint-probability framing says how the number is structured, not that it is calibrated to TB.
  - Being two-stage lowers it only if the per-stage inputs are sourced. The Advocate has not shown that they are.
- **There is a tension in the Advocate's framing.**
  - The Advocate says the 40% is conditional on an already-positive signal. The Advocate also says the BOTEC's 40% covers "Phase II and Phase III both succeed."
  - If a Phase II remains to be run, the existing positive IIa/b is not the end of that stage. The "conditional on signal" argument then supports a higher per-stage probability, but nothing in the record says how much higher.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the critique's own tally (3 successes, 4 failures) gives about 43%, consistent with 40%.

- **The tally cannot do the work the Advocate gives it.**
  - The Advocate calls it "a convenience sample, not a systematic reference class," then uses it as one of two inputs to a 0.33 midpoint.
  - Named analogues are recalled because they were notable. Successes are more likely to be remembered than quiet failures, so 3/7 is more plausibly an upper bound than a central estimate. I cannot quantify that bias, and I am not claiming a number for it.
  - The critique's own list omits the third corticosteroid trial, which the verifier describes as "ambiguous." Counting it as a non-success gives 3/8 ≈ 38%. Counting it as half gives 3.5/8 ≈ 44%. The tally is unstable to one coding decision.
- **The tally mixes disease sites and question types.**
  - Dexamethasone in TBM (a CNS disease), SHINE (children, drug-susceptible shortening), and Study 31 are different problems from an adjunct in the target population.
  - Averaging them gives a rate for "TB trials people remember," not for this intervention class.
- **The Advocate is right that the critique's low numbers are ungrounded.**
  - The verifier treats the TB-class success rate as unverifiable, not rejected. The 10–20% figure remains an inference.
  - The correct conditional is: if the TB-class rate for host-directed or adjunct therapy is in the 0.2–0.3 range, the decision flips. Nothing in the record rules that out.

> The Advocate claims: non-inferiority trials against a ~95%-cure standard are a different design from a superiority adjunct, so the failure rate transfers imperfectly.

- **That the designs differ does not show that the adjunct's failure rate is lower.**
  - The Advocate offers no superiority-adjunct base rate.
  - A ~95% cure ceiling cuts against the adjunct. There is little room to show benefit on cure, so the trial must detect a difference on mortality or lung outcomes. That typically needs larger samples and is more exposed to population heterogeneity, which is the dexamethasone lesson.

> The Advocate claims: dexamethasone heterogeneity would shrink effect size rather than zero out success, because the population is 96% drug-susceptible with 60% uptake.

- **Heterogeneity can produce a failed trial, not only a smaller effect.**
  - ACT HIV (HR 0.85, P = 0.22) is exactly a trial that missed significance in a different population after an earlier positive result (RR 0.69).
  - The 96% drug-susceptible share and the 60% uptake assumption are effect-size modifiers in the BOTEC. Neither says anything about the HIV composition of the Phase III population, which is the dexamethasone-relevant variable. The Advocate does not address it.

> The Advocate claims: the vitamin D and statin-preclinical claims should carry no weight.

- Agreed. They add nothing to either side.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: the break-even is p ≈ 0.26, the critique's 0.2–0.3 range straddles it, and the central case does not cross.

- **The arithmetic is right, and I concede it.** SROI is linear in p, so 3,055 × (0.26/0.40) ≈ 1,986.
- **"Central = baseline" is not evidence.**
  - The sensitivity output sets central equal to baseline. It was not computed from a TB-class estimate.
  - It shows the Quantifier did not move the central case. It does not show the central case should not move.
- **Straddling means more than half of the critique's range crosses.**
  - Under a uniform distribution over 0.2–0.3, P(p < 0.26) = (0.26 − 0.20)/0.10 = 60%.
  - The critique's mechanism range of 0.10–0.25 lies entirely below the threshold.
  - The midpoint of the blended range alone, 0.25, gives 3,055 × 0.25/0.40 ≈ 1,909x, which is below the bar.
- **The Advocate's 0.33 depends on one choice.**
  - Averaging the critique's blend (0.25 midpoint) with the 3/7 tally (0.43) gives about 0.34, which is the Advocate's figure.
  - Equal weighting of an inference range and an acknowledged convenience tally has no stated rationale.
  - The Advocate's own Concession 4 says 0.20–0.25 is plausible and cannot be ruled out.
- **The minimum defensible position is narrow.**
  - If the 40% has no reference class (Concession 1) and the tally is unstable, then the decision rests on an unsourced central value.
  - A range of 0.25–0.43 spans the bar.
  - I accept that this shows decision-relevant uncertainty, not that the bar is failed.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: morbidity DALYs, post-treatment mortality, transmission averted and sweat-diagnostic value are in no part of the model and offset a lower p_success.

- **They are real in direction but unquantified, and the Advocate gives no numbers.** They are also not independent of p_success.
  - The morbidity, lung-damage and transmission channels are tied to the same clearance and X-ray surrogates whose translation to clinical benefit is in doubt. If the surrogate-to-clinical step fails, these channels likely fail too.
  - They are therefore correlated with the risk being critiqued, not a hedge against it.
- **The sweat-diagnostic value is not a statin-efficacy outcome.** It is not an offset against failed efficacy.

> The Advocate claims: if success includes a surrogate such as clearance or lung damage, 40% may be conservative.

- **The success definition must match the benefit being priced.**
  - The Advocate's own account is that only on-treatment mortality is valued in the BOTEC.
  - A surrogate-only "success" does not deliver that benefit. The 40% would justify the model's value only if it is the probability of a mortality-relevant result.
  - The Advocate's argument concedes that the BOTEC prices one outcome and the 40% may measure another.

> The Advocate claims: the drug is generic and cheap, lowering adoption barriers.

- **Cheapness bears on adoption and cost, not on the probability that a trial succeeds.** If adoption is in the model separately, this is double-counted. If it is not, the Advocate should say where.

**KEY UNRESOLVED QUESTIONS:**

- What does the 40% represent: a Phase II/III joint probability for a mortality-relevant endpoint, or for a surrogate endpoint? The BOTEC prices mortality, so the answer determines whether the offset about "success definition" helps or hurts.
- Is there a sourced base rate for adjunct or host-directed TB therapy moving from a positive Phase II surrogate result to a positive Phase III clinical endpoint? Neither side has produced one.
- What is the HIV and other subgroup composition of the intended Phase III population? This determines whether the dexamethasone heterogeneity risk applies directly.
- Does a surrogate-positive Phase II in TB have a materially different success rate than the fluoroquinolone programmes? If not, the "conditional on a positive signal" defense gives no protection.
- Should the unmodelled upside channels (morbidity, transmission) be added to the model? If so, the break-even p would fall below 0.26 and part of this critique would be absorbed.

### Judge Audit
Surviving strength: moderate
Justification: The debate was mostly substantive. Both sides showed their arithmetic, disclosed their uncertainty, and conceded key points: the Advocate made Concessions 1–4, and the Challenger conceded the break-even and that "this shows decision-relevant uncertainty, not that the bar is failed."
The critique's quantitative mechanism did not survive. The 0.15 → 38% claim rests on an ungrounded range, and the Challenger's best numerical support (uniform-distribution 60%, a "decision flips" overstatement) was weak. However, the Challenger landed grounded structural points the Advocate could not fully answer:
- the tension in "conditional on a positive Phase II" versus "covers Phase II and III";
- the mismatch between a surrogate-defined success and the mortality the BOTEC prices;
- the correlation between the upside offsets and surrogate risk.
The direction survives with decision-relevant uncertainty. The magnitude does not.
Recommended action: 2. SPECIFIC INVESTIGATION:

(a) Pull the CG BOTEC and grant documentation to determine three things, all feasible from existing documents:
- what "success" means in the 40% (mortality, or a surrogate leading to guideline inclusion);
- whether a further Phase II is actually planned;
- the expected HIV prevalence in the Phase III population.

If success is surrogate-defined, the 40% overstates the priced benefit and the critique strengthens.

(b) Re-run the verifier with targeted searches for:
- systematic reviews of TB host-directed and adjunctive therapy trials, such as statins, metformin, everolimus, CC-11050, auranofin and corticosteroids, recording Phase II→III outcomes;
- infectious-disease Phase II→III and III→approval transition rates from industry clinical-development success-rate datasets.

This is feasible with existing tooling and would supply the sourced class rate both sides lack.

**Interim conclusion while this is pending:** Flag CG's 40% as undocumented, and do not lower the central p_success below the 0.26 break-even on current evidence.
Action feasibility: requires_specified_evidence
Advocate failures: ["sound_synthesis_noted: The break-even derivation is correct and grounded in the model's linear structure: SROI is linear in p, so the bar is crossed at p < 0.40 × 2,000 / 3,055 ≈ 0.26. The Challenger accepted it. The 3/7 ≈ 43% tally is also correct arithmetic on the critique's own list, and the Advocate disclosed it as a convenience sample with inconsistent success definitions.", 'unsupported_estimate_pseudo: The 0.33 counter-midpoint comes from equally weighting the critique\'s inferential 0.2–0.3 blend and the 3/7 tally. The Advocate had just called that tally "not a systematic reference class," and gives no reason for equal weights. There is also a small arithmetic slip: (0.25 + 0.43)/2 ≈ 0.34, not 0.33. The Advocate disclaims that 0.33 is the "true value," but still uses it to say the shift falls "below the 25% materiality threshold." That conclusion leans on an unjustified weighting step.', 'false_definitiveness: The Advocate says the unmodelled upside channels (morbidity, post-treatment mortality, transmission, sweat diagnostic) "offset the SROI impact of a lower p_success." It gives no magnitude and does not consider that most of these channels depend on the same surrogate-to-clinical translation being questioned. The Challenger correctly identified this correlation.']
Challenger failures: ['sound_synthesis_noted: Re-coding the tally with the omitted third corticosteroid trial (3/8 ≈ 38% or 3.5/8 ≈ 44%) is a grounded demonstration that the tally is unstable. The midpoint check (0.25 → ≈1,909x) is correct. The point that "central = baseline" in the sensitivity output is a default rather than an estimate is valid. The argument that the unmodelled upside channels correlate with surrogate-translation risk is substantive.', 'unsupported_estimate_pseudo: Under a uniform distribution over 0.2–0.3, P(p < 0.26) = 60%." The arithmetic is shown, but it imposes a uniform distribution on a range the verifier marked UNGROUNDED. The 60% therefore carries no more information than the range itself, yet it is presented as showing that "more than half of the critique\'s range crosses." The Challenger also reuses the 0.10–0.25 mechanism range ("lies entirely below the threshold") as magnitude support, despite having just conceded that it is ungrounded.', 'false_definitiveness: If the TB-class rate … is in the 0.2–0.3 range, the decision flips." This is false for roughly 0.26–0.30, by the break-even the Challenger itself conceded a few lines later. The conditional framing is appropriate in form, but the stated consequence is overstated.', 'call_to_ignorance: 3/7 is more plausibly an upper bound than a central estimate" because successes are more memorable. No evidence is given for the direction of the bias. The critique\'s list was assembled to illustrate failures, so selection could plausibly run the other way. The Challenger admits it "cannot quantify that bias" but still asserts its direction.']
Debate resolved: Both sides agree on four points:
- The decision threshold is p_success ≈ 0.26.
- CG's 40% has no documented reference class.
- The critique's 0.10–0.25 and 0.2–0.3 figures are unsourced inference.
- The named TB analogues form a small, non-systematic, unstable tally that does not clearly point below 40%.

The debate therefore narrowed the critique to a direction-plus-uncertainty claim: plausible values of p span the bar, but there is no grounded case that the bar is failed. The Challenger explicitly conceded this.
Debate unresolved: - Whether the 40% is meant to be the probability of a mortality-relevant result, which is what the BOTEC prices, or of a surrogate result. The Advocate's own offset argument exposed this mismatch.
- Whether surrogate-positive Phase II TB adjunct or host-directed programmes have a Phase III success rate materially below 0.26.
- Whether the planned Phase III population has an HIV share that makes the dexamethasone heterogeneity lesson directly applicable.

--- Critique: "Success" probably means a surrogate or composite endpoint, but the model needs a 10% mortality reduction, so P(adopted AND 10% mortality benefit) < P(trials succeed) ---

### Advocate
DEFENSE OF GIVEWELL'S (CG'S) POSITION: "Success" probably means a surrogate, but the model needs a 10% mortality reduction

**EXISTING COVERAGE:**
- **Success is defined as a conditional assumption.** The BOTEC says "a positive result is assumed to cut [mortality] by 10% relative." It does not say that trial success demonstrates a 10% mortality reduction.
  - The 10% is therefore an assumed true effect given a positive result, not a trial-powered effect size.
  - The critique's sample-size argument (10⁴–10⁵ participants for a 10% mortality effect) shows that a mortality-powered trial is unlikely. It does not show that the true effect conditional on success is below 10%.
- **The Phase IIc trial names survival as an outcome.** The grant tests dosing "for survival, infection clearance and lung damage." Mortality is at least nominally in scope.
- **The 40% already discounts the 10%.** The expected relative reduction is 4%. The critique's own 5–7% replacement for E[RR | success] is flagged "UNGROUNDED" in the critique itself.
- **The critique mislabels a parameter.**
  - It says the "4%" baseline should be replaced with a population-specific figure.
  - In the BOTEC, baseline mortality is 6%, and 4% is the probability-weighted relative reduction (40% × 10%).
  - The 0.4–1.5% figure is a trial-population mortality, not the target-population figure the benefit calculation needs.
  - Trial populations are typically healthier than the global treated population, so the gap does not show that the 6% is wrong. It shows that the trial would struggle to measure mortality, which is a different point.
- **The benefit side has implicit zeros.** The parameter map says "only mortality is valued." The BOTEC counts nothing for lung-damage morbidity, post-treatment mortality, transmission, or the diagnostic.

**EVIDENCE WEAKNESSES:**
- **The sample-size calculation is the critique's own.** It is labeled "my calculations" and was not verified against a primary source. I accept it arguendo. It supports "a mortality-powered Phase III is expensive." It does not support "E[RR | success] < 10%."
- **The key quantity is ungrounded.** The 5–7% E[RR | success] and the 30–50% loss are labeled UNGROUNDED. The 30–50% is just arithmetic from 5–7% vs 10%, so the whole magnitude rests on an unsupported input.
- **The cited trials are not analogues.**
  - Study 31, REMoxTB and TRUNCATE-TB tested antibiotic regimens with a bacteriological or composite unfavourable-outcome endpoint. That endpoint is the natural primary outcome for antimicrobials.
  - They do not show what endpoint an adjunctive host-directed therapy would use for guideline change.
  - TB Fast Track tested empirical TB treatment in advanced HIV, a different intervention and a different population.
- **The one mortality-endpoint example is compatible with a ~10% effect.** TB Fast Track's HR of 0.92 (19.0 vs 21.6 deaths per 100 person-years) is an ~8% reduction. It was not significant, but the point estimate is the same order as CG's 10%. It cannot be used to claim true effects must be much smaller, and I do not claim it validates 10%.
- **The FEV₁ point cuts partly against the critique.** The critique notes that FEV₁ "predicts long-term all-cause mortality." If a lung-function surrogate is the trial's success signal, the benefit plausibly runs through long-term survival. The BOTEC does not count that channel (see Offsetting Factors).
- **The Phase II power point is not decisive.** The critique cites small sample size and low power in the four-drug HDT Phase 2 trial. That shows Phase II trials in this class are noisy. It says nothing about the effect conditional on a successful Phase III and adoption.
- **The cost inference is unverified.** The claim that a 12,000–70,000-participant trial would exceed the $7M budget is labeled "my inference, not verified." I engage with it conditionally under Magnitude below.

**MAGNITUDE CHALLENGE:**
- **Break-even derivation.**
  - SROI in the BOTEC is linear in relative_reduction. At 10% it is ~3,000x.
  - The ~2,000x bar is reached when RR = 10% × (2,000 / 3,000) ≈ 6.7%, all else equal.
  - The critique's range is 5–7%.
  - At 7% the SROI is ~2,100x, still above the bar, and at 6.7% it is at the bar.
  - Only the lower half of the critique's own range (5% → ~1,500x) falls below it.
  - The critique's claim of "material" therefore depends on where in an ungrounded range the truth lies.
- **The two failure modes are largely alternatives.**
  - The critique says success may be surrogate-based, which lowers E[RR | success].
  - It also says that if success requires a real 10% mortality effect, p_success is lower still.
  - These are mutually exclusive readings of "success," so the compounding is overstated. If success is surrogate-based, p_success is not penalized for mortality power. If it is mortality-based, E[RR | success] is plausibly ≥10%, since only a trial that detects a mortality effect can "succeed."
- **Conditioning on success does not obviously lower the true effect.**
  - Adoption conditional on a positive trial selects for larger true effects (the same selection that drives the 40% filter).
  - Winner's curse is a counter-argument, since observed effects overstate true effects.
  - I cannot ground a size for either force, so I treat the sign of the net conditioning effect as uncertain, not clearly negative.
- **Conditional on the critique's cost point, the issue is cost, not effect.**
  - If a mortality-powered Phase III would cost more than $7M, the likelier implication is that adoption proceeds on non-mortality evidence, or that the all-in cost is understated.
  - Neither of these directly lowers the true mortality effect. The critique's effect-size claim does not follow from its cost claim.

**OFFSETTING FACTORS:**
- **Four uncounted benefit channels.** The parameter map lists morbidity DALYs from reduced lung damage, post-treatment mortality, transmission-averted cases, and diagnostic value. All are currently zero in the formula.
- **The surrogate route may add value.** If the critique's FEV₁-to-mortality link holds, a surrogate-based success may deliver post-treatment survival benefits that the on-treatment mortality channel misses entirely. That would offset any shortfall in on-treatment mortality.
- **Cheap, generic drug.** For a generic with low cost, guideline bodies might adopt on a surrogate benefit plus safety data, so the success definition may not need to equal a powered mortality effect. I cannot ground this precedent for TB adjunctives specifically. Treat it as an uninformed prior.

**OVERALL ASSESSMENT:** Partial defense.
- The critique identifies a real internal-consistency gap: no definition of "success," and no derivation of the 10%.
- Its quantification is not grounded. The 5–7% figure is labeled UNGROUNDED by its author, and the sensitivity results are empty.
- On the critique's own range, the finding is material only if E[RR | success] falls below ~6.7%.
- The "compounding" claim is partly double counting, and the unmodelled benefit channels may offset a reduction.

**CONCESSIONS:**
- **The 10% is underived.** The BOTEC gives no derivation from the Phase IIa/b surrogate effects, and no definition of what success means.
- **The $7M may not be consistent with a mortality-powered Phase III.** Either all-in cost is understated, or success rests on a surrogate and the 10% needs separate justification. The model does not reconcile this.
- **A sensitivity analysis is warranted.** Sensitivity on RR in roughly the 5–10% range, with p_success held fixed, would show the break-even near 6.7%. The BOTEC's omission of this is a legitimate documentation gap.
- **The implied independence of p_success and relative_reduction is an unstated assumption.** I cannot defend it as correct.

### Challenger
REBUTTAL: "Success" probably means a surrogate or composite endpoint, but the model needs a 10% mortality reduction

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the BOTEC treats 10% as an assumed true effect conditional on a positive result, not a trial-powered effect, so the sample-size argument shows only that a mortality-powered trial is unlikely.

- I concede the sample-size argument alone does not entail E[RR | success] < 10%. The critique's own 5–7% figure is labeled UNGROUNDED.
- The Advocate's reading helps GiveWell less than it appears. If 10% is an assumption rather than a trial-demonstrated effect, the question becomes what supports it.
  - The Advocate concedes the 10% is "underived," with no link from Phase IIa/b surrogate effects.
  - An underived parameter that drives SROI linearly is the gap the critique identifies.
  - Calling it "conditional" restates the problem. It does not answer it.

> The Advocate claims: the 40% already discounts the 10%, since the expected reduction is 4%.

- The 40% is a probability of success. It discounts for the chance that no effect materializes.
- It does not discount for the case where the trial succeeds on a surrogate and the true mortality effect is smaller than 10%.
- Multiplying 40% by 10% gives expected value only if E[RR | success] = 10%, which is the contested quantity.

> The Advocate claims: the critique mislabels the "4%" as a baseline mortality figure. The BOTEC baseline is 6%, and 4% is 40% × 10%.

- Conceded. The critique's line about replacing the "4%" baseline is mislabeled.
- The residual point stands but is narrower. A trial population with 0.4–1.5% mortality (the critique's figure, ungrounded) is one in which mortality cannot be the success endpoint. That bears on what "success" means, which the Advocate calls "a different point" but which is the critique's core question.

> The Advocate claims: the Phase IIc trial lists survival among its outcomes, so mortality is nominally in scope.

- Phase IIc is a Phase II trial. Verifier evidence says Phase 2 trials in this class (the four-drug HDT trial) are limited by small sample size and low power.
- A "survival" outcome in an underpowered trial supports a signal at most. It does not support a 10% effect conditional on adoption.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: Study 31, REMoxTB, TRUNCATE-TB and TB Fast Track are not analogues. The antibiotic trials use bacteriological endpoints naturally, and Fast Track tested a different intervention.

- Agreed that they are not host-directed-therapy analogues. The critique's use of them is narrower. It says feasible TB Phase III designs overwhelmingly use composite endpoints, so a successful trial is unlikely to deliver mortality evidence.
- The closest analogue in the verifier package is the four-drug HDT Phase 2 trial. Its efficacy signal was FEV₁, a surrogate. The Advocate does not dispute this, so the class-specific evidence points toward surrogate success.

> The Advocate claims: TB Fast Track's HR of 0.92 (about 8%) is compatible with a ~10% effect.

- Agreed that it does not show true effects must be much smaller. I do not claim it does.
- The relevant fact is that a mortality-endpoint trial in a high-mortality population (19.0–21.6 deaths per 100 person-years) still could not distinguish an 8% reduction from zero.
- If the adopted drug's evidence base looks like this, adoption rests on non-significant mortality estimates or on surrogates.

> The Advocate claims: the FEV₁ point cuts against the critique, because lung function predicts long-term all-cause mortality, so a surrogate success may deliver survival benefit.

- "Predictor of long-term mortality" is a prognostic association. It does not show that raising FEV₁ with an adjunctive drug lowers mortality. Whether it does is the surrogate-validity question, and the verifier package contains no evidence on it.
- Even if the link holds, it is a post-treatment, long-horizon channel. It is not the 10% on-treatment mortality reduction the BOTEC applies.
- The Advocate's reading also relocates the benefit to a channel the model does not value. It does not support the 10% the model uses.

> The Advocate claims: the 5–7% and 30–50% figures are ungrounded, so the magnitude is unsupported.

- Agreed on the status of those numbers. The verifier did not reject the underlying mechanism.
- Lack of a grounded replacement for 10% is not evidence that 10% is right. Both numbers are uninformed.
- The asymmetry that matters is that the model needs a defensible number and the critique asks for a sensitivity range. The Advocate concedes a sensitivity analysis is warranted.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: SROI is linear in RR, so the ~2,000x bar is reached at RR ≈ 6.7%. Only the lower half of the critique's 5–7% range falls below it.

- I accept the arithmetic: 3,000 × (RR/10%) = 2,000 gives RR ≈ 6.7%.
- The break-even is only ~3.3 percentage points below the model's point estimate, a one-third relative cut.
- The relevant question is how much probability mass E[RR | success] has below 6.7% given an underived 10% and a surrogate-driven success definition. Neither side can ground that mass.
- Break-even proximity is not a defense. A parameter whose break-even is a one-third haircut, with no derivation behind it, is a decision-relevant uncertainty. The critique's "material" label does not depend on its 5–7% range being right.

> The Advocate claims: the two failure modes (surrogate success lowers RR, mortality-based success lowers p_success) are mutually exclusive, so the compounding is double counting.

- Partially conceded: they are not simultaneously true of one trial.
- But the model does not know which definition of success applies. Under uncertainty about the definition, expected benefit is a mixture:
  - w × (surrogate branch: lower E[RR | success])
  - plus (1−w) × (mortality branch: lower p_success)
- Both branches reduce benefit relative to the BOTEC. So the mixture is below the BOTEC for any w. This is not double counting.
- The critique's sentence that "the two parameters cannot both be right" is better read as saying that the BOTEC implicitly takes the favorable side of each branch.

> The Advocate claims: conditioning on success has an ambiguous sign. Selection favors larger true effects, but winner's curse works the other way.

- The signs are not symmetric. Selecting on a noisy observed significant result gives E[true effect | significant] < observed estimate when the trial is underpowered for the effect (Type M error, Gelman & Carlin 2014).
- Selection favors larger true effects only through the observed signal. Net of that, the observed effect overstates the true one.
- The sign is thus negative relative to any 10% anchored on observed or hoped-for effects.
- If the 10% is anchored on something else, I cannot ground the sign either. The model does not say.

> The Advocate claims: if a mortality-powered Phase III exceeds the $7M budget, the likely implication is cost understatement or adoption on non-mortality evidence, neither of which lowers the true effect.

- This is a dilemma that concedes the critique:
  - If cost is understated, SROI falls (cost enters the denominator). This is a material error on the cost side.
  - If adoption proceeds on non-mortality evidence, the 10% has no trial-derived support and is unanchored to what the adopting evidence shows.
- The cost inference is unverified, not rejected. Conditional on it, either branch hurts the model.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: four uncounted benefit channels (morbidity, post-treatment mortality, transmission, diagnostic) are zero in the formula and may offset a shortfall.

- The channels are real in the parameter map but unquantified. The Advocate offers no magnitudes.
- Two of them (morbidity, post-treatment mortality) depend on the same unproven surrogate-to-outcome link. They are not independent of the critique's uncertainty.
- Zeros in other channels do not make 10% on-treatment mortality correct. If the zeros are an intentional conservatism buffer for model risk generally, spending that buffer on this specific parameter gap leaves less margin elsewhere.
- I cannot ground whether those zeros were designed as a buffer.

> The Advocate claims: a cheap generic might be adopted on surrogate plus safety data.

- The Advocate disclaims this as an uninformed prior, and I agree it has no grounded support.
- It also cuts against the model: adoption on surrogate-plus-safety data is the scenario in which E[RR | adoption] is least likely to be 10%.

**KEY UNRESOLVED QUESTIONS:**
- What does CG's trial program define as "success"? If this cannot be answered from the grant documents, the 10% cannot be tied to any observable result.
- What is the target population (general DS-TB, TB meningitis, or advanced HIV)? The verifier could not tell. It determines baseline mortality and whether a mortality endpoint is feasible.
- Does the FEV₁-to-mortality association hold causally for the drug class? Verifier evidence supports prediction only.
- How much probability mass does E[RR | success] have below 6.7%? Neither side has grounded it.
- Is the $7M cost estimate consistent with whatever Phase III the adoption pathway requires? This is unverified, and either answer matters.

### Judge Audit
Surviving strength: moderate
Justification: - The structural core of the critique survived. The Advocate conceded that the 10% is underived, that independence between p_success and RR is an unstated assumption, and that a sensitivity analysis is warranted. The Challenger's separation of the 40% discount from the conditional effect was grounded and went unrebutted.
- The quantitative claim did not survive. The 5–7% and 30–50% figures stay ungrounded, and both sides agree on that.
- The "compounding" claim was only partly rescued by the mixture argument, because the Challenger overstated it ("for any w").
- Both sides made substantive, mostly grounded moves with modest failure modes. That is above "weak," but the magnitude remains open.
Recommended action: 1. CONCLUDE NOW: The critique validly identifies an internal-consistency gap, but its proposed magnitude does not survive. Confidence is moderate–high on the gap and low on the magnitude.
   - **Structural point:** The BOTEC's 10% relative mortality reduction is unanchored to any defined trial success criterion.
   - **Magnitude:** The 30–50% benefit reduction is not established.
   - **Model change:**
     - Add a sensitivity analysis on E[RR | success] across 5–10%, holding p_success fixed. This explicitly shows break-even at ~6.7%.
     - Add a one-line statement of what endpoint defines "success" and how the 10% follows from it.
   - **Document check:** Check the grant documents for the Phase IIc/III primary endpoint and target population. This is a document lookup, not new research, and it determines whether a composite including death (partial mortality tracking) or a pure surrogate applies.
   - **Out of scope:** Treat the cost-understatement point as a separate critique.
Action feasibility: actionable_now
Advocate failures: ['sound_synthesis_noted: The break-even derivation is clean. SROI is linear in RR and is ~3,000x at 10%, so the ~2,000x bar falls at RR ≈ 6.7%. Each step is shown, and the Challenger accepted the arithmetic. This is substantive analysis, not guess-trading.', 'misrepresenting_evidence_status: The Advocate wrote, "The sample-size calculation is the critique\'s own… not verified against a primary source. I accept it arguendo." The verifier explicitly marked the arithmetic VERIFIED, recomputing ~35,800 per arm at 4% and ~23,400 at 6%. Accepting it "arguendo" softens the damage, but the Advocate still describes a verified claim as unverified.', 'call_to_ignorance: The Advocate wrote, "a surrogate-based success may deliver post-treatment survival benefits… That would offset any shortfall in on-treatment mortality." It also wrote that the unmodelled channels "may offset a reduction.', 'false_definitiveness: The Advocate wrote, "If it is mortality-based, E[RR | success] is plausibly ≥10%, since only a trial that detects a mortality effect can \'succeed.']
Challenger failures: ['misrepresenting_evidence_status: The Challenger wrote, "A trial population with 0.4–1.5% mortality (the critique\'s figure, ungrounded).', 'false_definitiveness: The mixture argument says "Both branches reduce benefit relative to the BOTEC. So the mixture is below the BOTEC for any w.', 'unsupported_estimate_pseudo: The Challenger wrote, "The sign is thus negative relative to any 10% anchored on observed or hoped-for effects," citing Gelman & Carlin 2014.', 'sound_synthesis_noted: The Challenger correctly separates the 40% probability-of-success discount from the conditional effect size. The 40% × 10% expected value is valid only if E[RR | success] = 10%. This is a grounded correction of the Advocate\'s "40% already discounts the 10%" point.', 'sound_synthesis_noted: The Challenger rebuts the FEV₁ offset well.']
Debate resolved: Both sides agree on four points:
- The 10% relative mortality reduction is underived, and "success" is undefined in the model.
- A mortality-powered Phase III is infeasible at typical TB trial sizes; the verifier confirmed this arithmetic.
- The critique's "4% baseline" line is a mislabel, since the BOTEC baseline is 6% and 4% is 40% × 10%.
- The decision-relevant break-even is RR ≈ 6.7%, a one-third haircut, which means the critique's ungrounded 5–7% replacement figure is not needed to establish decision relevance.
Debate unresolved: Four questions remain open after the exchange:
- How much probability mass E[RR | success] has below 6.7%.
- Whether "success" is defined on a composite that includes death, a pure surrogate, or mortality.
- What the target population is, which determines whether a mortality endpoint is feasible at all.
- Whether the mortality-branch trade-off between lower p_success and higher conditional RR nets out negative.

--- Critique: P(adoption | Phase III success) and P(Phase III gets funded and run | Phase IIc success) are missing, and the 60% uptake factor may not cover them ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION: P(adoption | Phase III success) and P(Phase III funded | IIc success) are missing, and the 60% uptake may not cover them

**EXISTING COVERAGE:**

*Phase III funded and run*
- The 40% is defined as the probability that "Phase II and Phase III trials both succeed." A Phase III that is never funded or run cannot succeed, so P(Phase III run | IIc success) is plausibly inside the 40% as a link in the chain. CG does not itemize it, but the Parameter Map's own gap, "no separation of probabilities for Phase IIc, Phase III, and adoption," is a documentation gap rather than proof of omission.
- The $7M all-in cost explicitly includes "later Phase III trials, guideline changes, dissemination and validation." The Phase III cost is therefore already charged to the project.

*Adoption given Phase III success*
- The 60% uptake is stated as the share of adult patients who would add atorvastatin "if it works." It is not 100%, even though the drug is generic and cheap. A blended 60% across all patients is compatible with partial or delayed guideline adoption in some jurisdictions.
- The Parameter Map says adoption "may be partly captured in uptake, but this is not explicit." The critique's own mechanism section concedes that if the 60% embeds adoption, the critique "mostly collapses to a documentation concern."
- Arguendo, suppose the 60% is purely within-country clinician and patient uptake and excludes guideline adoption. The critique's adoption factor then has real force. I address its magnitude below.

**EVIDENCE WEAKNESSES:**
- The critique cites no source for P(adoption | positive Phase III) for TB adjuncts. Its own flag says the values 0.75–0.85 and 0.8 are UNGROUNDED, to be treated as "an illustrative sensitivity range, not an estimate." The direction is trivially true, since any factor below 1 lowers SROI. The magnitude carries no evidential weight.
- The only empirical anchor, the Study 31/WHO pathway, shows a clean non-inferiority trial adopted within months. That cuts against a heavy discount in the favorable case.
- The "harder case" argument (an adjunct with low-certainty mortality evidence) depends on Critique 1. It is not independent evidence on adoption. Adoption risk for a successful Phase III is also lower than for a marginal one, because a Phase III that meets its endpoint is by construction the evidence WHO needs.
- The "near the 0.26 threshold" claim rests on stacking two ungrounded factors on top of a 40% that may already include one of them. That risks double counting.

**MAGNITUDE CHALLENGE:**
Derivation from CG's published numbers:
- SROI = ($54B / $7M) × 0.40 = 7,714 × 0.40 ≈ 3,086x. Break-even against the 2,000x bar requires p = 2,000 / 7,714 ≈ 0.259. This confirms the critique's 0.26.
- *Adoption factor alone.* The critique's 0.75–0.85 range gives 0.40 × 0.75–0.85 = 0.30–0.34, and SROI of about 2,315x–2,623x. Both are above 2,000x. The factor would have to fall below 2,000/3,086 ≈ 0.65 to breach the bar by itself, which is well outside the critique's own range.
- *Funding factor, which is not a pure numerator haircut.* Phase III is about 95% of the all-in cost ($6.68M of $7M). If Phase III is not funded, its cost is not incurred, so expected cost falls along with expected benefit.
  - Take the critique's f = 0.8 and the worst case for this offset, where IIc succeeds with certainty. Expected cost = $0.32M + 0.8 × $6.68M = $5.66M, which is 0.809 of $7M.
  - Net SROI multiplier = 0.8 / 0.809 ≈ 0.99, essentially neutral.
  - If IIc can fail (it is a trial, and the 40% is explicitly less than 1), expected cost falls further and the funding factor is net positive for SROI. The BOTEC charges the full $7M in every state of the world, which is conservative on this dimension.
- *The critique's combined case.* The "near 0.26" result applies 0.8 to the numerator only. It omits the matching cost reduction, so it overstates the funding effect by roughly 20%. The combined effect is approximately the adoption factor alone, which stays above the bar.

**OFFSETTING FACTORS:**
- The cost-side offset above is the main one. The Phase III cost is only incurred in worlds where IIc succeeds.
- The BOTEC values only on-treatment mortality. The Parameter Map lists morbidity (lung damage), post-treatment mortality, transmission, and diagnostic value as implicit zeros. Any one of these is an upside buffer against a 15–25% adoption haircut.
- If adoption failure is correlated with Critique 1 (weak mortality evidence), the Phase III would likely be a larger and more convincing trial. This partially offsets the funding concern, because a funded mortality-powered Phase III producing a positive result is a stronger adoption case.

**OVERALL ASSESSMENT:** Partial defense.
- *Funding factor:* strong defense. It is plausibly already in the 40%, and where it is not, it nearly cancels against lower expected cost.
- *Adoption factor:* partial defense. It is not explicit in the CG chain, and the 60% might not cover it. But even the critique's own illustrative values leave SROI at about 2,300–2,600x, above the bar.

**CONCESSIONS:**
- CG does not state whether the 60% includes guideline or national adoption. The critique is right that this is a transparency gap.
- If the 60% is purely within-country uptake, the adoption factor is a real, uncompensated downward adjustment of unknown size, with no cost offset in the guideline or dissemination component.
- Adoption risk is plausibly higher for an adjunct whose evidence is surrogate-based or low-certainty. That interaction with Critique 1 is legitimate, though I cannot quantify it from the evidence package.
- The critique's "close to the threshold" result requires either a significantly lower adoption factor (below about 0.65) or the numerator-only treatment of the funding factor, which I have shown is internally inconsistent.

### Challenger
REBUTTAL: P(adoption | Phase III success) and P(Phase III funded | IIc success) are missing, and the 60% uptake may not cover them

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: P(Phase III run) is plausibly inside the 40%, because a Phase III that never runs cannot succeed. The $7M also already charges for Phase III, and the 60% is "compatible with" partial adoption.

- **Funding, conceded in part.** Because the $7M includes Phase III, "funded" is closer to a CG decision than an exogenous risk. The critique's funding factor is therefore mostly a documentation point.
- **Adoption, not shown to be covered.** "Compatible with" is not evidence that the 60% was built to include guideline adoption.
  - The Parameter Map says adoption "may be partly captured… but this is not explicit."
  - Neither side has shown that 60% was derived as (national adoption × within-country uptake).
  - The Advocate's own quote, "the share of adult patients who would add atorvastatin if it works," reads most naturally as a clinician/patient-level uptake conditional on a working drug. That is the reading under which adoption is a separate factor.
- **Verifier status.** Whether the 60% embeds adoption is not REJECTED. It is simply unresolved. The Advocate's "plausibly already in the 40%" is an assumption, not a finding.
- **Conditional on the natural reading.** If the 60% is within-country uptake, the adoption factor is multiplicative and has no cost offset. The Advocate concedes this.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the 0.75–0.85 values are ungrounded, the Study 31 anchor argues against a heavy discount, and a successful Phase III is "by construction the evidence WHO needs."

- **Ungrounded values.** I agree that 0.75–0.85 is ungrounded and cannot be treated as an estimate. I cannot ground a replacement either. Treat any value I give as an uninformed prior.
- **"By construction" is an assertion.** The 40% is defined as both trials "succeed." That tells us nothing about whether success means a statistically significant mortality reduction at GRADE-sufficient certainty.
  - If Phase III success is defined by a non-mortality endpoint, hitting it does not supply the evidence a guideline body needs for a mortality claim.
  - The Advocate's inference only holds if the endpoint is mortality, which is exactly the Critique 1 dependency the Advocate otherwise treats as non-independent.
- **Study 31 is the favorable case.** The verifier called it "the best case."
  - Study 31 tested a regimen change in a pathway where WHO was already positioned to adopt.
  - An adjunct adds a drug on top of an existing regimen, and the verifier flags its mortality evidence as low-certainty.
  - This is my reasoning, not a cited finding. It does show that the one anchor is not a like-for-like comparator.
- **Double counting runs both ways.** It is a risk only if the 40% includes adoption. That is the same unresolved question as above, so it cannot be used to discount the critique.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: (a) adoption at 0.75–0.85 leaves SROI at ~2,315–2,623x, above the 2,000x bar; (b) the funding factor nets to ~0.99 because Phase III cost is only incurred if IIc succeeds; (c) the critique's "near 0.26" result is numerator-only and overstated by ~20%.

I concede the following:
- The break-even of 0.259 is confirmed.
- Adoption alone at 0.75–0.85 does not breach the bar.
- A numerator-only funding haircut is internally inconsistent if the cost is actually conditional.

Four residual problems remain.

1. **The cost offset depends on an unsourced cost split.**
   - The "$6.68M of $7M" figure is the Advocate's. I cannot ground it from the evidence package.
   - With funding factor f = 0.8 and Phase III cost share s, the net multiplier is f / (1 − s + s·f).
   - At s = 0.95 the multiplier is 0.988, which is the Advocate's result.
   - At s = 0.5 it is 0.889, and at s = 0.2 it is 0.833.
   - The "neutral" conclusion is sensitive to a split nobody has verified.

2. **The real exposure is cost, not funding probability.**
   - The verifier's evidence says a mortality-powered Phase III is "much more expensive" than a composite-endpoint TB trial. The Advocate's offset assumes the $6.68M Phase III budget is right.
   - Break-even cost: 0.40 × $54B / 2,000 = $10.8M total. With $0.32M of non-Phase-III cost, Phase III can cost at most $10.48M, about 1.57× the Advocate's $6.68M.
   - This is a breach threshold, not an estimate of the overrun. At 1.5× Phase III cost, total ≈ $10.34M and SROI ≈ 2,089x. At 2×, total ≈ $13.68M and SROI ≈ 1,579x. The 1.5× and 2× multiples are illustrative sensitivities, not grounded estimates.
   - The cost offset helps only when Phase III is not run. It gives no protection when Phase III is run at a higher cost.

3. **The critique does not need to breach the bar alone.**
   - Headroom is 3,086 → 2,000, about 35%.
   - Adoption at 0.75 uses about 25% of it, which leaves SROI at 2,315x. Any further haircut above ~13.6% then breaches the bar.
   - Adoption at 0.85 leaves SROI at 2,623x, and a further haircut above ~23.8% breaches.
   - A 15–25% haircut is a large share of the total margin, even though it does not breach the bar by itself.

4. **Minimum magnitude.** At a mild adoption value of 0.9, SROI is ~2,777x. The critique alone is not decisive at the low end, and I concede that. Its force lies in how it interacts with the cost and endpoint questions.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: the cost offset, unmodeled morbidity/transmission/post-treatment benefits, and a larger, more convincing Phase III in the weak-evidence world all offset the haircut.

- **Cost offset.** It is real in structure but unverified in size, as shown above. It also reverses if Phase III is more expensive than budgeted.
- **Unmodeled benefits.** The Parameter Map lists these as implicit zeros.
  - They are not in the model and not quantified.
  - They carry their own probability of being real.
  - They cannot cancel a specific modeled haircut in a threshold comparison without a number attached.
- **"Larger, more convincing Phase III."**
  - A mortality-powered trial raises adoption odds but, per the verifier, also raises cost and lowers P(funded).
  - It trades the adoption concern for the cost concern rather than offsetting both.
  - The Advocate's offset appears in neither the CG chain nor the $7M figure.

**KEY UNRESOLVED QUESTIONS:**
- Does the 60% include guideline or national adoption? This single fact decides whether the adoption factor is real or only a documentation gap.
- What is the Phase III endpoint in the 40%, and is the $6.68M budget sized for a mortality-powered trial? If not, cost-overrun risk is a bigger lever than either probability factor.
- What share of the $7M is Phase III? The Advocate's "neutral" funding result depends on it.
- Who funds Phase III? If CG commits to it, funding is a decision. If third parties fund it, the probability is real, and so is cost uncertainty outside CG's control.
- Is adoption risk for a low-certainty adjunct materially below the Study 31 case? Neither side can quantify this from the evidence package.

### Judge Audit
Surviving strength: moderate
Justification: The critique's headline quantitative claim (combined factors bring the base case near the threshold) did not survive. The Advocate's sound cost-offset structure and the Challenger's own concessions defeated it. What survives is narrower: an adoption factor that may be uncaptured, whose plausible range would consume a large share of the margin without breaching it alone. Both sides contributed grounded arithmetic, which keeps the rating above weak. The Challenger's moves that most extend the critique (cost overrun, stacking with other haircuts) are conditional or out of scope, which keeps it below strong.
Recommended action: 1. CONCLUDE NOW (moderate confidence):
   - **Funding factor:** drop it as a quantitative adjustment. It is mostly captured by CG's inclusion of Phase III cost in the $7M, and a correct treatment nets out much of its effect.
   - **Adoption factor:** treat it as a valid transparency gap with a bounded sensitivity. If the 60% excludes adoption, a 0.75–0.85 factor lowers SROI to ~2,300–2,600x but does not breach 2,000x alone. It matters mainly in combination with other downward critiques, especially Critique 1 on mortality evidence.
   - **Two document checks resolve the open points:** confirm from CG's BOTEC or documentation (a) how the 60% uptake was derived, and (b) the Phase IIc/Phase III split of the $7M. Both are feasible desk lookups or a direct question to CG, and neither requires new research.
Action feasibility: actionable_now
Advocate failures: ['unsupported_estimate_fabricated: Phase III is about 95% of the all-in cost ($6.68M of $7M)." The verifier package contains no cost split, and the Advocate cites no source. The whole "funding factor is essentially neutral (≈0.99)" result rests on this number. The Advocate rates the funding defense "strong," but its quantitative core is unsourced. The Challenger\'s sensitivity formula shows the result moves materially at lower cost shares.', 'sound_synthesis_noted: Break-even p = 2,000 / 7,714 ≈ 0.259. Adoption must fall below ≈0.65 to breach the bar alone. Expected cost = $0.32M + f·$6.68M gives a net multiplier of f / expected-cost-ratio. This derivation is structurally correct, and the point that a numerator-only funding haircut is internally inconsistent is a genuine, well-grounded contribution. The structure is sound even though the input share is unsourced.', 'false_definitiveness: Adoption risk for a successful Phase III is also lower than for a marginal one, because a Phase III that meets its endpoint is by construction the evidence WHO needs." This is asserted as definitional. It only holds if the Phase III endpoint is mortality at GRADE-sufficient certainty, which the Advocate elsewhere treats as an open Critique 1 dependency.', 'call_to_ignorance: The unmodeled morbidity, transmission, post-treatment mortality and diagnostic value are invoked as an "upside buffer against a 15–25% adoption haircut." The Parameter Map lists these as implicit zeros, and none is quantified. Using unknown upside to absorb a specific modeled downside is filling a gap with speculation.', 'call_to_ignorance: If adoption failure is correlated with Critique 1… the Phase III would likely be a larger and more convincing trial." This is a speculative offset with no evidence. It also cuts against the Advocate\'s own cost-offset argument, because a larger trial means higher cost and lower P(funded).']
Challenger failures: ['strawmanning: The Advocate\'s \'plausibly already in the 40%\' is an assumption, not a finding." This is placed under the discussion of whether the *60%* embeds *adoption*. The Advocate\'s "plausibly inside the 40%" claim was about the *funding* factor, not adoption. This is a category swap.', 'strawmanning: Double counting runs both ways. It is a risk only if the 40% includes adoption." The Advocate\'s double-counting concern was that the 40% may already include the *funding* link ("stacking two ungrounded factors on top of a 40% that may already include one of them"). Rebutting it as an adoption-in-the-40% claim answers an argument that was not made.', 'sound_synthesis_noted: The net multiplier f / (1 − s + s·f), evaluated at s = 0.95 / 0.5 / 0.2, correctly shows that the Advocate\'s "neutral" funding result depends on the unverified cost share. The break-even total cost of $10.8M, and the headroom arithmetic (35% total headroom, with 0.75 adoption using about 25%), are also correct and clearly derived. The 1.5× and 2× overrun multiples are explicitly labeled illustrative, so they are not failures.', 'unsupported_estimate_counter (mild): The cost-overrun argument (point 2) uses the Advocate\'s $6.68M as its base right after calling it ungrounded. It then advances Phase III cost overrun as "a bigger lever than either probability factor." This is presented conditionally, which mitigates it. However, the argument effectively introduces a new critique (budget adequacy) that is outside the original critique\'s scope. It does not strengthen the probability-factor claim actually under review.']
Debate resolved: The debate established three things:
- The break-even is ≈0.26.
- The adoption factor alone, at the critique's own 0.75–0.85 range, leaves SROI at ~2,300–2,600x, above the bar.
- The critique's "near the 0.26 threshold" combined result is overstated because it applies the funding factor to the numerator only.

Both sides effectively agree that the funding factor reduces mostly to a documentation point, since the $7M already charges for Phase III.
Debate unresolved: The debate did not settle whether CG's 60% uptake embeds guideline or national adoption. That single fact decides whether the adoption factor is a real 15–25% multiplicative haircut, consuming most of the ~35% headroom, or only a transparency gap. The Phase III share of the $7M, which the funding-offset magnitude depends on, also remains unsourced.

--- Critique: A 2%/yr decline in notified case counts probably contradicts the observed trend; incidence rates fall slowly while counts do not ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: A 2%/yr decline in notified case counts probably contradicts the observed trend

EXISTING COVERAGE:
1. CG's model is explicitly a constant-treated-share model. The BOTEC says "the share of cases being treated stays constant." The eligible pool therefore scales with incidence, not with independent notification growth.
   - Notification growth from closing the detection gap (the 2.4M gap) is excluded by construction.
   - The critique's 8.3M notification figure is therefore not the right comparator for a constant-share model. The comparator is the trend in incidence counts.
2. I reverse-engineered the 5.5M and it is consistent with the critique's premise.
   - 7.5M × 0.98^8 (0.851) × 0.96 × 0.90 ≈ 5.5M.
   - The 7.5M is the critique's own 2022 notification figure, and the 0.90 is the adult share.
   - This is my reconstruction, not a CG statement. It suggests CG did apply 2% to counts from a 2022-type baseline, so I do not dispute the premise.
   - The baseline-year issue belongs to Critique 1. This critique concerns only the trend exponent.
3. The parameter map confirms CG has no sensitivity analysis on the decline rate or the baseline year. I cannot claim an existing adjustment covers this.

EVIDENCE WEAKNESSES:
1. The 7.5M → 8.3M rise is mostly post-COVID catch-up, not a trend.
   - The critique's own evidence says the recovery in reported cases first slowed the rise in estimated incidence and then reversed it.
   - That describes a backlog of previously missed cases being diagnosed, which is a one-time level shift.
   - Extrapolating it as ongoing growth (+1%/yr for 8 years) is not supported by that source.
   - The critique's own +1%/yr scenario has no cited basis.
2. The critique's two inputs about the latest year point toward flat or slightly declining counts.
   - Its baseline of 8.2M versus 8.3M for 2024 implies roughly +1% from 2023 to 2024. I am inferring 2023 ≈ 8.2M from that baseline. This is inference, not a verified figure.
   - From my recollection of the WHO Global TB Reports, which I cannot ground here, estimated incidence went from about 10.8M (2023) to about 10.7M (2024). That is a slight count decline, and the rate fell roughly 1.7%.
   - If that recollection is right, the latest data are closer to CG's assumption than to "flat or rising."
3. The critique's own counter-consideration limits upside.
   - The 2.4M gap means notification growth cannot continue indefinitely from detection alone.
   - Under constant treated share, further growth would require rising incidence, which WHO's own framing says has reversed.
4. The funding-shock point is UNGROUNDED in the critique. Conditionally, if the 2025 TB-programme funding disruptions are real and large, they push notifications and treated counts down in the near term. That is the opposite direction from the critique's headline.

MAGNITUDE CHALLENGE:
1. The critique's arithmetic is correct. 1/0.851 = 1.175, and 1.083/0.851 = 1.273. SROI is linear in the eligible population, so +17% to +27% on this term would carry straight through to SROI.
2. The upper end rests on an ungrounded +1%/yr growth path. The lower end rests on "flat counts," which is roughly right for 2020-2024 but includes the COVID trough and recovery.
3. A more conservative trend uses my recalled recent figures.
   - Rate decline of ~1.7%/yr, partly offset by population growth of roughly 0.9%/yr (UN World Population Prospects, my recollection), gives a count change of about -0.8%, which I round to -1%/yr.
   - 0.99^8 = 0.923, and 0.923/0.851 ≈ 1.085, so the trend-only correction is about +8%.
   - This is below the ~25% materiality threshold on its own.
   - The recalled inputs are not verifier-grounded, so treat this as a plausible lower bound for the trend effect, not a finding.
4. The trend effect alone is therefore about +8% to +17%, with +27% requiring sustained growth the evidence does not support. The >25% crossing in the critique comes mainly from stacking Critique 1's baseline correction, which is a separate argument.
5. The sensitivity results are empty. The critique's magnitude comes from hand arithmetic, not from the replicated formula chain.

OFFSETTING FACTORS:
1. Near-term funding disruption lowers notifications and treated counts, partly or fully offsetting upward revisions. Its size is ungrounded, but the direction is not in doubt.
2. The M72/AS01E vaccine and scale-up of newer diagnostics could accelerate incidence decline late in the window. The parameter map notes CG has no vaccine shock either. This is speculative and probably small before year 8.
3. The one-time catch-up in notifications is exhausted. Under constant treated share, the only additional growth would come from incidence growth, which is not observed.

OVERALL ASSESSMENT:
Partial defense.
- A flat-to-slightly-declining count is better supported than a 2%/yr count decline. CG's assumption is probably somewhat pessimistic, and the direction of error is upward.
- The critique overstates the size. A trend-only correction is plausibly +8% to +17%, not +27%. The >25% materiality claim depends on Critique 1's baseline argument.
- The critique's own caveats about the funding shock and the unreliability of the premise are fair.

CONCESSIONS:
1. A 2%/yr decline in counts is more aggressive than the 2020-2024 observed pattern in estimated incidence counts.
2. CG gives no justification for treating 2% as a count decline rather than a rate decline.
3. The direction of error is upward, so correcting it would raise SROI.
4. The critique's arithmetic for the flat and +1%/yr scenarios is correct.
5. CG has no sensitivity analysis on this parameter, so the 2% assumption is untested in the published BOTEC.
```

### Challenger
REBUTTAL: A 2%/yr decline in notified case counts probably contradicts the observed trend

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: CG's model holds the treated share constant, so the eligible pool should track incidence counts rather than notifications. The 8.3M notification figure is therefore the wrong comparator.

1. **The comparator switch does not rescue the 2%/yr count decline.**
   - The critique also cites incidence counts: roughly flat at 10.3–10.8M since 2020.
   - Under the Advocate's preferred comparator, a count decline of 2%/yr (0.98^8 = 0.851) still contradicts the data.
   - The Advocate concedes this directly (Concession 1).

2. **The Advocate's own reconstruction undercuts the constant-share framing.**
   - The reconstruction (7.5M × 0.851 × 0.96 × 0.90 ≈ 5.5M) reproduces CG's figure: 7.5 × 0.7353 = 5.51.
   - That match suggests CG's starting point is a notification count (7.5M), not an incidence-derived treated count.
   - If so, the notification trend is the relevant comparator for projecting forward.
   - The "constant share" is then implicitly the 2022 share. Using the critique's incidence range, that is about 69–73% (7.5 / 10.3–10.8). The 2024 share is about 77–81% (8.3 / 10.3–10.8).
   - A constant-share model anchored to the 2022 share therefore understates the 2024 treated pool. This is a level problem, but it shows the constant-share defense does not neutralise the notification data.

3. **I concede the Advocate's point that no existing CG adjustment covers this.** The disagreement is therefore only about size.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the 7.5M → 8.3M rise is a one-time catch-up, not a trend, so extrapolating +1%/yr is unsupported.

1. **I concede that the +1%/yr scenario has no cited basis.** I would treat flat to slightly declining counts as the central case and +1%/yr as a tail.

2. **The catch-up argument supports a correction rather than defeating one.**
   - A one-time level shift is permanent unless reversed. The post-catch-up level (about 8.2–8.3M) is the correct anchor for a decline path.
   - If CG anchors to 7.5M and then applies 2%/yr, it ignores the shift and also compounds a decline from a depressed level.
   - The Advocate moves this to Critique 1, but the model's output error is the product of both. The critique states it is "before the baseline correction."

> The Advocate claims: from recollection, estimated incidence went from about 10.8M (2023) to about 10.7M (2024), so the latest data are close to CG's assumption.

3. **The recollection is explicitly ungrounded, and it does not support the conclusion.**
   - A change of 10.8 → 10.7M is −0.9%. That is less than half CG's −2% and consistent with "approximately flat."
   - The Advocate says this brings the data "closer to CG's assumption." It is closer only in sign, not in magnitude.
   - One year of data on a noisy estimate cannot distinguish −0.9% from 0%.

4. **The Advocate's derivation of the count change has an internal problem.**
   - It nets the rate decline against population growth to get about −0.8%, and CG's 2% applies to counts.
   - Even if the rate fell a full 2%/yr, counts would fall only about 1.1%/yr using the Advocate's 0.9% population growth. That gives 0.989^8 ≈ 0.915 and 0.915/0.851 ≈ +7.5%.
   - So the +8% floor already assumes the rate keeps falling at about its recent pace. If counts are flat, the correction is +17%.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

1. **I accept the Advocate's trend-only range of roughly +8% to +17%.** The +27% case requires sustained growth I cannot ground.

2. **The Advocate is right that the >25% crossing depends on stacking with Critique 1.** My calculation, using the critique's own numbers:
   - Critique 1 alone (8.2M baseline, 2%/yr decline): 8.2 × 0.851 × 0.96 × 0.90 ≈ 6.03M, or +10% against 5.5M.
   - Adding the Advocate's −1%/yr trend gives about 6.5M, or +18%.
   - Flat counts give about 7.1M, or +29%.
   - +1%/yr gives about 7.7M, or +40%.
   - The combined range is therefore +18% to +40%. The critique's 6.5–7.7M is mostly above the threshold, but its lower end falls below it.

3. **Because SROI is linear in the eligible pool, the sub-threshold trend correction still passes through one-for-one.** A directional bias of +8% to +17% on a single parameter is not trivial when no sensitivity analysis exists.

4. **The empty sensitivity results are a fair criticism.** The magnitude here is hand arithmetic, which I cannot upgrade.

**RESPONSE TO "OFFSETTING FACTORS":**

1. **Funding disruption conflicts with the Advocate's own framing.**
   - The Advocate argues that notifications are the wrong comparator under a constant-share model.
   - It then invokes a notification-side shock as an offset. If the model ignores notification dynamics, it ignores them in both directions.
   - A funding shock lowers the treated share and does not change incidence. That is not captured by a constant-share model either.
   - The size is ungrounded, as the critique itself flagged. It is a symmetric uncertainty, not an offset the model contains.

2. **The vaccine and diagnostics offset is speculative.** The Advocate concedes it is probably small before year 8, and it is not in the model.

3. **The 2.4M gap does not bind the +1%/yr scenario.**
   - +1%/yr over 8 years takes notifications from 8.3M to about 9.0M, which uses only about 0.7M of the 2.4M gap.
   - The 28% ceiling in the verifier evidence concerns a 100% detection scenario that neither of us defends. It limits the extreme tail, not the central range.

**KEY UNRESOLVED QUESTIONS:**
- Was CG's 2% intended as a rate or a count decline, and which baseline year and treated share does it anchor to? Neither the Advocate nor I can confirm this from the BOTEC; both rely on a reverse-engineered match.
- What is the 2023→2024 change in estimated incidence counts? The Advocate's figure is an unverified recollection, and the verifier did not confirm it.
- How much of the funding-related notification dip is a lasting level change and how much is temporary? Neither side can ground this.
- Does CG's "constant treated share" hold at the 2022 share or the current one? That choice moves the answer by roughly the 2022-to-2024 share difference, about 8–12 percentage points under the critique's incidence range.

### Judge Audit
Surviving strength: moderate
Justification: Both sides reasoned largely from correct arithmetic and engaged the substance. The Advocate conceded the direction and premise, and narrowed the magnitude with a transparent, if partly recall-based, derivation. The Challenger accepted the narrowed range and produced a correct combined-scenario table. The critique survives on direction, but its standalone magnitude is sub-threshold (+8% to +17.5%), and its materiality claim rests on Critique 1. Both sides misread the verifier's verified 2024 incidence figure, which kept the trend question more open than it needed to be.
Recommended action: 1. CONCLUDE NOW: With moderate-to-high confidence, CG's 2%/yr decline, if applied to counts, is pessimistic. Correcting it would raise the eligible population.
   - The standalone trend correction should be booked at about +8% to +17.5%, central around +12%. Flat to slightly declining counts are supported by the verified −1% change in 2024 and the ~1.4%/yr rate decline.
   - The critique's +27% upper bound and its >25% materiality claim should not be attributed to this critique alone. Materiality depends on combining it with Critique 1.
   - The pivotal premise that CG applies 2% to counts remains UNVERIFIABLE. It should be confirmed against the CG BOTEC source text, which is a quick document check, before the adjustment is applied.
   - The funding-shock downside remains unquantified and should be noted as a one-directional caveat.
Action feasibility: actionable_now
Advocate failures: ['misrepresenting_evidence_status: The Advocate calls the 10.8M (2023) → 10.7M (2024) incidence figure "my recollection… which I cannot ground here." The verifier package states it directly: "Incident cases fell 1% in 2024, from 10.8M to 10.7M." The Advocate understated the status of its own best evidence. This is self-harming rather than misleading, but it is still a misreading of the package.', 'unsupported_estimate_fabricated: The "rate decline of ~1.7%/yr" and "population growth of roughly 0.9%/yr (UN WPP, my recollection)" are recalled inputs with no grounding.', 'false_definitiveness: Offsetting Factor 3 states "The one-time catch-up in notifications is exhausted" with no support.', "sound_synthesis_noted: The reverse-engineered reconstruction 7.5M × 0.98⁸ × 0.96 × 0.90 ≈ 5.51M is correct arithmetic. It is honestly labelled as a reconstruction. It was used to concede the critique's pivotal premise (which the verifier marked UNVERIFIABLE) rather than to exploit that gap.", "sound_synthesis_noted: The Advocate separates the trend-only effect (+17.5% flat, +27% at +1%/yr) from the baseline correction of Critique 1. This matches the verifier's double-counting note and correctly isolates the critique's standalone magnitude."]
Challenger failures: ['misrepresenting_evidence_status: Under Key Unresolved Questions, the Challenger says the 2023→2024 incidence count figure is "an unverified recollection, and the verifier did not confirm it." The verifier explicitly verified 10.8M → 10.7M (−1%).', 'false_definitiveness: The Challenger calls the funding shock "a symmetric uncertainty, not an offset.', 'unsupported_estimate_fabricated (minor): A funding shock lowers the treated share and does not change incidence" is asserted without support. Reduced treatment can plausibly raise incidence over time through transmission. Over an 8-year window this matters.', "sound_synthesis_noted: The combined-scenario table is correct, and it usefully shows the critique's lower bound sits below the 25% threshold:", 'sound_synthesis_noted: The 2.4M-gap rebuttal is correct and correctly scoped. At +1%/yr, 8.3M × 1.01⁸ ≈ 9.0M, which uses only about 0.7M of the gap. The 28% ceiling binds only the 100% detection tail.', "sound_synthesis_noted: The Challenger turns the Advocate's reconstruction against the constant-share defense. It points out that a 7.5M anchor implies a 2022 share of about 69–73% versus about 77–81% in 2024. This is a grounded, substantive engagement."]
Debate resolved: Both sides converged on four points:
- A 2%/yr count decline is more pessimistic than observed incidence and notification counts.
- The error direction is upward.
- The trend-only correction is roughly +8% (−1%/yr counts) to +17.5% (flat counts), below the 25% materiality threshold on its own.
- The +1%/yr scenario (+27%) lacks grounding.

The debate also established that the >25% crossing depends on stacking with Critique 1. The combined range is about +18% to +40%, with the lower end below the threshold.
Debate unresolved: Two questions remain open:
- Whether CG's 2% was meant as a rate or a count decline, and whether its "constant treated share" is anchored at the 2022 or 2024 share. Both sides rely on an unverified reverse-engineered match.
- Whether the forward count trend is closer to −1%/yr (recent rate decline netted against population growth) or flat. The verified 2024 datapoint is a single year and cannot distinguish them.

--- Critique: "Adult DS notified" is not "eligible for the trial label": missing applicability filters ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION: "Adult DS notified" is not "eligible for the trial label": missing applicability filters

**EXISTING COVERAGE:**

1. CG's 5.5M is not meant as a strict label-eligible count. It is a pool of "people who could benefit," and the benefit calculation then applies a separate 60% uptake factor to adult patients.
   - The 60% is described as uptake "if it works," justified by the drug being generic and cheap.
   - A haircut that large (40% of the pool) is plausibly where clinician discretion, contraindications, pregnancy, hepatic concerns and drug-interaction caution are meant to live.
   - The critique's stack applies those exclusions on top of the 60% without asking how much the 60% already absorbs. This is a partial double-count risk. I cannot say how much, because CG gives no derivation of the 60%.
2. The 96% drug-susceptible filter already removes the rifampicin-resistant/MDR share. Only Hr-TB (about 7%) is a genuinely new exclusion on the drug-resistance axis.
3. The model is explicitly about guideline adoption, not a regulatory label. The report speaks of the "path to guideline adoption," and atorvastatin is generic.
   - Label-style restrictions such as "bacteriologically confirmed only" therefore bind less than the critique implies.
   - A repurposed generic added to a standard regimen is typically adopted through treatment guidelines and clinician practice.

**EVIDENCE WEAKNESSES:**

1. The critique's most consequential step (×0.62 for bacteriological confirmation) rests on an assumption, not on evidence.
   - The Challenger itself calls the confirmation requirement "the single most decision-relevant unknown."
   - The WHO 64% figure is verified, but whether a guideline would require confirmation is not.
2. Some of the ×0.85 factors are ungrounded. The statin-specific exclusions (pregnancy, hepatic) and the ×0.85 factor are the Investigator's own assumptions, flagged UNGROUNDED.
3. The verified WHO figures give a gentler stack than the illustrative one.
   - From the verified numbers alone: extrapulmonary 16% (×0.84), HIV ~5–6% (×~0.945), Hr-TB ~7% (×0.93).
   - Product: 0.84 × 0.945 × 0.93 ≈ 0.74. The critique's ×0.85 × ×0.85 gives 0.72, so it is a bit more aggressive than the grounded components alone.
4. Treating the filters as independent probably overstates the exclusion.
   - HIV-positive patients are more likely to have extrapulmonary disease. The extrapulmonary and HIV groups therefore overlap, and multiplying the shares double-counts that overlap.
   - This is my reasoning, not a verified figure. The direction is nonetheless clear.
5. The 25% South-East Asia extrapulmonary share and the Africa HIV share are regional. Applying them regionally would also need regional weights on the 5.5M. The critique asserts "this makes this worse" without computing it.

**MAGNITUDE CHALLENGE:**

Using the critique's own numbers, SROI scales linearly with the eligible population, so 5.5M ↔ ~3,000x and the 2,000x bar sits at about 3.6–3.7M.

1. Without confirmation, the full stack stays above the bar.
   - Standalone, 4.0M gives 3,000 × 4.0/5.5 ≈ 2,180x, still above ~2,000x.
   - Netted with Critique 2 (5.1M), SROI is about 2,780x (−7%), well inside the ±25% materiality band.
2. Only the confirmation restriction crosses the bar.
   - With confirmation, the figures are 2.5M standalone (~1,360x) or 3.2M netted (~1,750x).
   - Let q be the probability that confirmation is required, applied to the netted 5.1M: expected eligible = 5.1M × (1 − 0.38q).
   - The ~3.6–3.7M threshold requires q ≳ 0.74–0.77 (derivation: 3.67/5.1 = 0.72, so (1 − 0.72)/0.38 ≈ 0.74; with 3.6M the figure is 0.77).
   - For q = 0.2, expected eligible ≈ 4.7M (−14% versus 5.5M), which is not decision-relevant.
3. A high q is hard to defend.
   - The 0.62 factor treats all clinically diagnosed pulmonary cases as ineligible for a recommendation. That is the strongest possible reading.
   - From general knowledge, not in the verifier package: WHO regimens for drug-susceptible TB are generally the same for bacteriologically confirmed and clinically diagnosed pulmonary cases. I cannot ground this here, so treat it as a prior.
   - If correct, a guideline would be unlikely to restrict an adjunct to confirmed cases only.
   - A more realistic middle case is that uptake is lower in clinically diagnosed patients. That is already within the haircut of the 60% uptake.

**OFFSETTING FACTORS:**

1. The critique itself notes that, combined with Critique 2 (decline overstated), the non-confirmation filters roughly net to the current figure (−7%).
2. The 60% uptake is a single blunt haircut, and its justification ("generic and cheap") plausibly covers exclusions without further adjustment.
3. Overlap between the HIV and extrapulmonary groups (point 4 above) means the true combined exclusion is smaller than a naive product.
4. The CEA's implicit-zero benefit channels (morbidity, post-treatment mortality, transmission, diagnostic value) are unvalued. The parameter map notes they could make the estimate robust. These offsets are not quantified, so I do not lean on them numerically.

**OVERALL ASSESSMENT:** Partial defense.

- The non-confirmation filters are largely absorbed by the netting with Critique 2 and by the 60% uptake. Even standalone, they leave SROI at ~2,200x, above the bar.
- The confirmation restriction is the only filter that would breach the bar. It needs q ≳ 75% to do so, and the critique supplies no evidence for that level.
- The critique is correct that CG gives no explicit applicability decomposition, which is a genuine transparency gap.

**CONCESSIONS:**

1. CG states no pulmonary-only, HIV, pregnancy, hepatic or Hr-TB filters. Hr-TB in particular is not covered by the 96% drug-susceptible factor.
2. If a guideline did restrict use to bacteriologically confirmed pulmonary TB, SROI would fall to about 1,750x (netted) or about 1,360x (standalone), below the bar. The defense rests on that being unlikely, not on it being impossible.
3. I cannot establish how much of the 60% uptake already reflects clinical exclusions, so some double-counting in the critique's stack is possible but unquantified.
4. If excluded subgroups (HIV, extrapulmonary) have different mortality from the 6% average, the baseline mortality parameter would need recalibrating on the filtered population. I cannot ground the direction or size of that effect.

### Challenger
REBUTTAL: "Adult DS notified" is not "eligible for the trial label": missing applicability filters

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: CG's 60% uptake factor is a blunt 40% haircut that plausibly already absorbs clinician discretion, pregnancy, hepatic concerns and drug-interaction caution. Stacking those exclusions on top is therefore a partial double-count.

Response:
- **The 60% is described as uptake "if it works," justified by the drug being generic and cheap.** That is a rationale for adoption, not for contraindications. Cheapness does not remove a hepatic exclusion or a pregnancy exclusion. The Advocate concedes the 60% has no derivation, so "it plausibly absorbs exclusions" cannot be tested.
- **The absorption claim has an implication the Advocate does not state.**
  - The Advocate's own grounded-only filter product is 0.74.
  - If the 60% already contains that exclusion, then 0.60 / 0.74 ≈ 0.81 of clinically eligible adults are assumed to receive the drug.
  - That is high adoption among eligible patients for a new adjunct to a standard regimen.
  - The double-count argument therefore only works by quietly raising implied conditional uptake to about 81%.
- **The same 40% haircut is asked to do two jobs.** The Advocate says it covers the non-confirmation filters, and later also says it covers lower uptake in clinically diagnosed patients. A fixed haircut cannot be spent on both without implying even higher adoption among those who remain.
- **Concession on Hr-TB.** The 96% DS factor covers rifampicin resistance, so Hr-TB is the only new drug-resistance exclusion. This trims the stack but does not change its direction.
- **"Guideline, not label" only addresses the confirmation filter.**
  - Pulmonary-only scope, HIV, pregnancy and hepatic exclusions are clinical and evidentiary constraints. They bind under a guideline as much as under a label.
  - For the confirmation filter, I cannot ground that WHO guidelines would mirror trial inclusion criteria. Treat that as a prior.
  - Conditionally, though: if the evidence base is a trial in a restricted population, a guideline for other populations has no direct evidence to rest on.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: ×0.62 is an assumption, the statin-specific ×0.85 is ungrounded, the verified-only stack is gentler (0.74 vs 0.72), and HIV/extrapulmonary overlap means the product overstates exclusion.

Response:
- **×0.62.** The verifier did not mark it rejected. The 64% WHO figure is verified, and whether confirmation is required is unknown, which the critique itself says. The right framing is conditional, not "no evidence for it." The Advocate's counter ("WHO regimens are the same for clinically diagnosed and confirmed cases") is, by the Advocate's own disclaimer, ungrounded. It also concerns the backbone regimen, not whether an adjunct's evidence base extends to unconfirmed cases.
- **The 0.74 vs 0.72 comparison undercuts the Advocate.**
  - 0.74 comes from extrapulmonary, HIV and Hr-TB only (0.84 × 0.945 × 0.93).
  - It leaves out pregnancy, hepatic and other statin-specific exclusions entirely.
  - The critique's extra ungrounded exclusions therefore add only about 0.02 (0.74 → 0.72). That is hardly aggressive. The two stacks are essentially the same.
- **Overlap correction is bounded and small.**
  - HIV is ~5–6% of cases. Even if every HIV case were also extrapulmonary, the combined exclusion would move from 1 − 0.84 × 0.945 = 20.6% to 16%.
  - That is a correction of at most ~5 percentage points, and realistically much less because overlap is partial.
  - This is my own derivation from the verified shares. It does not change the standalone conclusion, because 0.74 vs ~0.78 on a 5.5M base is about 0.2M.
- **Regional weights.**
  - The Advocate is right that the critique did not compute regional weighting.
  - The direction is verified. Using the SEA figure (25%) instead of the global figure (16%) gives ×0.75 instead of ×0.84, about −11% relative.
  - I cannot ground the share of CG's 5.5M that sits in SEA, so I do not claim a magnitude.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: without confirmation the stack stays above the bar (4.0M ≈ 2,180x; 5.1M ≈ 2,780x), and confirmation would need q ≳ 0.74–0.77 to breach it. At q = 0.2, eligible is ~4.7M (−14%), which is not decision-relevant.

Response:
- **The q threshold quietly imports Critique 2.**
  - The 0.74–0.77 threshold is computed on the netted 5.1M. The critique says net direction with Critique 2 is uncertain.
  - On the standalone 4.0M, the same formula at q = 0.2 gives 4.0 × (1 − 0.38 × 0.2) ≈ 3.70M. That is at the ~3.6–3.7M bar, not comfortably above it.
  - The threshold on the standalone base is 3.67/4.0 = 0.92, so (1 − 0.92)/0.38 ≈ 0.21. A 20% probability of a confirmation requirement is enough to hit the bar.
  - Whether the 0.74 or the 0.21 threshold is relevant depends entirely on whether Critique 2's upside is accepted. That is not settled.
- **Even in the Advocate's favoured case, −14% is not trivial.** It sits inside the ±25% band the Advocate invokes, but it stacks with other downward factors the Advocate leaves out:
  - the regional extrapulmonary weighting,
  - the baseline mortality recalibration the Advocate concedes in point 4.
- **"Low q" is not grounded.** The Advocate offers general knowledge, which it flags as ungrounded. The minimum plausible magnitude, with no confirmation restriction and the overlap correction applied, is about 4.0M standalone, or about −27% on 5.5M. That is already near the edge of the materiality band before any q is applied.
- **Concession.** Netted with Critique 2 and with q low, the critique's effect is small. The critique already says this.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: Critique 2's upside nets the filters to −7%, the 60% uptake covers exclusions, the HIV/extrapulmonary overlap shrinks the exclusion, and unvalued benefit channels remain upside.

Response:
- **Critique 2 netting.** This is a real offset only if Critique 2 holds. It is a different critique and has its own uncertainty. It cannot be used to dismiss this critique without conceding that this critique's sign depends on Critique 2.
- **The 60% uptake as offset.** See above. It implies about 81% uptake among eligible patients, and it is already spent on the clinically diagnosed uptake argument.
- **Overlap.** Real but bounded at ~5 percentage points.
- **Unvalued channels.** The Advocate rightly declines to lean on them numerically. They are not a quantified offset, and they do not reduce the eligible-pool overstatement. They only widen the margin if the pool shrinks.

**KEY UNRESOLVED QUESTIONS:**
- Does the evidence base for adoption (trial inclusion, guideline reasoning) require bacteriologically confirmed pulmonary TB? On the standalone base, the bar is crossed at q ≈ 0.21, so even a modest chance matters.
- Does CG's 60% uptake reflect clinical exclusions or only behavioural adoption? If it reflects exclusions, it implies about 81% uptake among eligible adults.
- Is Critique 2's upside real? That decides whether this critique nets to −7% or stands at about −27%.
- What share of the 5.5M is in SEA versus high-HIV regions, and does the 6% baseline mortality hold on the filtered population?

### Judge Audit
Surviving strength: moderate
Justification: Both sides did real quantitative work grounded in the verifier's figures: the Advocate's 0.74 stack, the Challenger's overlap bound, and the standalone q re-derivation. The Challenger's showing that q ≈ 0.21 suffices on the standalone base materially weakened the Advocate's central magnitude defence, which rested on a netted base. However, the Challenger's 81% uptake argument partly strawmanned the absorption claim, and its "minimum −27%" figure ignored its own overlap correction. The critique survives as a material but probably sub-threshold standalone adjustment, with a plausible threshold-crossing path that hinges on one unresolved design question.
Recommended action: 2. SPECIFIC INVESTIGATION:
- **Trial inclusion criteria.** Retrieve the registered inclusion and exclusion criteria of the atorvastatin/statin adjunctive TB trial(s) that CG's model relies on, from ClinicalTrials.gov or the trial protocol. Check whether they require bacteriologically confirmed pulmonary TB and whether they exclude people living with HIV, pregnancy, or hepatic impairment.
- **WHO precedent.** Check WHO consolidated TB treatment guidelines for whether prior adjunct or regimen-shortening recommendations were restricted to the trial's confirmation status. For example, the 4-month HPMZ regimen was recommended with eligibility mirroring its trial population.
- **Feasibility.** Both checks can be done now with existing search tooling, and either would directly shift q.

In the meantime, conclude now, with moderate confidence, that the CEA should model applicability filters explicitly at roughly ×0.74–0.78 for the non-confirmation filters. Report the confirmation restriction as a scenario rather than folding it silently into the 60% uptake.
Action feasibility: requires_specified_evidence
Advocate failures: ['sound_synthesis_noted: The grounded-only filter product, 0.84 × 0.945 × 0.93 ≈ 0.74, is built entirely from verifier-verified components, and the arithmetic is correct. The q-threshold formula, 5.1M × (1 − 0.38q), is also algebraically correct, giving q ≈ 0.74–0.77. This is legitimate analysis. Its weakness is the choice of base, not the logic.', 'call_to_ignorance: The Advocate says the 60% uptake "is plausibly where clinician discretion, contraindications, pregnancy, hepatic concerns and drug-interaction caution are meant to live." In the same passage it concedes "CG gives no derivation of the 60%." The absence of a derivation is used as room to assume the factor absorbs exclusions.', 'false_definitiveness: The Overall Assessment states that "the non-confirmation filters are largely absorbed by the netting with Critique 2 and by the 60% uptake." Concession 3 says the Advocate "cannot establish how much of the 60% uptake already reflects clinical exclusions.', 'false_definitiveness: The headline q ≳ 0.74 threshold is computed on the 5.1M base, which is netted with Critique 2. The critique explicitly says the net direction with Critique 2 is uncertain. The Advocate presents "needs q ≳ 75%" as the operative bar without disclosing that it is conditional on another contested critique. The standalone threshold, which the Advocate did not compute, is about 0.21.']
Challenger failures: ['sound_synthesis_noted: Re-deriving the q threshold on the standalone 4.0M base is correct and is the most important move in the debate.', 'strawmanning: The "implied ~81% conditional uptake" argument (0.60 / 0.74) divides by the extrapulmonary × HIV × Hr-TB product.', 'unsupported_estimate_pseudo: The Challenger gives the "minimum plausible magnitude, with no confirmation restriction and the overlap correction applied, is about 4.0M standalone, or about −27%." The chain does not follow.', 'misrepresenting_evidence_status: The Challenger lists "the baseline mortality recalibration the Advocate concedes in point 4" among "other downward factors." The Advocate explicitly said it "cannot ground the direction or size of that effect." Treating it as directionally downward misstates its status.', 'false_definitiveness: The Challenger asserts that "Pulmonary-only scope, HIV, pregnancy and hepatic exclusions … bind under a guideline as much as under a label." This is unhedged, but nothing in the verifier package establishes it.']
Debate resolved: The non-confirmation filters, using verified WHO shares, reduce the pool by roughly 22–28% standalone, to about 4.0–4.3M. That leaves SROI near 2,200x, above the bar but material. The statin-specific ungrounded exclusions add almost nothing (0.74 → 0.72), and HIV/extrapulmonary overlap can correct the stack by at most about 5 percentage points.

The debate also established that the bacteriological-confirmation restriction is the only filter that crosses the bar. The probability needed to cross it depends sharply on Critique 2:
- about 0.21 standalone;
- about 0.74 netted with Critique 2.
Debate unresolved: 1. Whether the adoption pathway (the trial evidence base and the guideline) would restrict a statin adjunct to bacteriologically confirmed pulmonary TB. Neither side grounded its prior on this.
2. Whether CG's 60% uptake already embeds clinical exclusions.
3. Whether Critique 2's upside should be netted in, which decides whether a modest q is decision-relevant.

--- Critique: Shorter and new regimens erode both the eligible population and the incremental benefit ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION: Shorter and new regimens erode both the eligible population and the incremental benefit

**EXISTING COVERAGE:**

1. CG's 60% uptake is already a 40% haircut on the eligible pool, applied "if it works." Patients on non-HRZE regimens at the benefit horizon could plausibly be part of the 40% who do not add atorvastatin. The critique applies the displacement to the 5.5M eligible pool as if it were fully additive to the uptake haircut. If the two overlap, the effective loss is smaller than 20–40%. This overlap is an inference, not something CG states.
2. The 5.5M figure comes from a model that already declines incidence 2% per year and excludes the 4% non-drug-susceptible cases. The critique's own pediatric evidence shows the 4-month 2HRZ(E)/2HR regimen is still rifampicin-based. It shortens duration but does not change the backbone, so it does not create a transfer problem for that group.
3. The CG benefit mechanism is a 10% relative cut in on-treatment mortality (0.6 percentage points). It is not duration shortening. The critique's "shorter regimens leave less room for a duration-shortening adjunct" point targets a mechanism CG does not use. Whether HPMZ changes the baseline 6% mortality or the statin's proportional effect is unverified in the critique's own evidence ("No evidence was found").
4. The 40% p_success, which covers both Phase II and Phase III, already discounts for the possibility that results fail to generalise.

**EVIDENCE WEAKNESSES:**

1. The critique flags its own central input as UNGROUNDED. The 20–40% adoption range is "my own scenario" and is "not grounded in published projections." The conclusion "at or near the 3.6M bar" follows arithmetically from an assumed range and nothing else.
2. The only grounded evidence on uptake points to slow adoption. WHO's recommendation of HPMZ is conditional, and it explicitly refers to rifapentine availability. The critique concedes that "the low end is more likely than the high end." The grounded evidence therefore favours the less damaging part of its own range.
3. The 4-month HPMZ regimen applies to people aged 12 or older. The critique's evidence shows adolescents aged 12–16 also have 4-month 2HRZ(E)/2HR and standard 6-month options, so HPMZ is not the default even within its eligible age group.
4. The critique itself corrects the TRUNCATE-TB point. It is a strategy trial with bedaquiline–linezolid, not a WHO-endorsed standard regimen. Bedaquiline-based DS-TB regimens remain at Phase 2 or 2c. Neither is therefore a near-term displacement driver.
5. The "rifamycin interaction would apply to rifapentine too" point has an unverified direction. It could cut either way and is not evidence of erosion.

**MAGNITUDE CHALLENGE:**

1. SROI scales linearly with the eligible pool. The published estimate is about 3,000x, so a 20–40% displacement implies the following:
   - At 20%: 3,000 × 0.8 = 2,400x, which is above the ~2,000x bar.
   - At 40%: 3,000 × 0.6 = 1,800x, which is below the bar.
   - Only the upper half of the critique's own range crosses the bar, and the critique says the lower end is more likely.
   - The midpoint, 30%, gives 2,100x, still above the bar.
2. The shift is a roughly 3–17% overshoot relative to the bar on the central scenario, so the critique's materiality of "notable" is generous. The effect is compounded only if the statin's proportional effect shrinks on newer backbones. The critique has no evidence for that.
3. Displacement is measured at the benefit horizon, which is the single year of speedup, around year 8–9 after the grant. Forecasting regimen shares that far out is very uncertain. The same uncertainty applies to the critique's 20–40% range as to CG's implicit 0%.

**OFFSETTING FACTORS:**

1. The Phase III is assumed to finish about 8 years after the grant. A trial running over that horizon could plausibly adapt to the prevailing standard regimen, so displacement would not necessarily reduce applicability. This is reasoning, not evidence.
2. The parameter map says CG values mortality only. Implicit zeros include morbidity DALYs, lung damage reduction, post-treatment mortality, transmission averted and diagnostic value. These upside terms could outweigh a 20–40% reduction in the eligible pool.
3. The statin may still add value on HPMZ through lung-damage reduction, which a shorter regimen does not eliminate. This is speculative, so I treat it as a conditional point.

**OVERALL ASSESSMENT:** Partial defense.

- The headline risk rests on an ungrounded adoption range.
- The grounded evidence points toward the low-displacement end.
- The conclusion depends on the critique's high end, and CG's omitted benefit channels could offset it.
- But CG's BOTEC has no regimen-change adjustment at all, and the critique's "no evidence on statin adjunct with shorter regimens" gap is real. The defense cannot show the concern is already covered.

**CONCESSIONS:**

1. CG does not model regimen change at all, and the parameter map confirms that no regimen change adjustment exists.
2. There is no evidence on statin adjunct effects on HPMZ or other short regimens. I cannot show transferability from HRZE.
3. At 40% displacement the SROI falls below the bar. I can argue this is the less likely scenario, but I cannot rule it out with grounded evidence.
4. My overlap argument between displacement and the 60% uptake is an inference. If the two are independent, the full 20–40% reduction applies.
5. The direction of the rifapentine interaction is unknown. It could reduce statin exposure by more than rifampicin does.

### Challenger
REBUTTAL: Shorter and new regimens erode both the eligible population and the incremental benefit

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: CG's 60% uptake already haircuts the eligible pool by 40%, and patients on non-HRZE regimens may sit inside that 40%, so the 20–40% displacement would double-count.

- The Advocate concedes this is "an inference, not something CG states" (Concession 4). Nothing in the evidence package ties the 60% to regimen composition. It is an "if it works" adoption parameter.
- The two filters answer different questions. Uptake asks whether a clinician or programme adds atorvastatin. Displacement asks whether the trial result applies to the patient's backbone.
- If they are independent, the effective pool is 0.6 × (1−d) × 5.5M. The critique's 20–40% reduction then applies in full.
- Overlap would require the 60% to have been derived from regimen heterogeneity. I see no sign it was.

> The Advocate claims: the 2HRZ(E)/2HR paediatric regimen is still rifampicin-based, so it creates no transfer problem for that group.

- I concede this, and it is the verifier's finding. The paediatric 4-month regimen applies only to non-severe TB in children under 16 and is not a general adult option.
- The displacement risk therefore sits in HPMZ, not the paediatric regimen. The critique already says this.

> The Advocate claims: CG's mechanism is a 10% relative cut in on-treatment mortality, not duration shortening, so the "less room for a duration-shortening adjunct" point targets a mechanism CG does not use.

- I concede that the incremental-value limb is weaker against CG's stated mechanism. I will not press it as an independent loss.
- The residual is the transfer question: does a 10% relative effect on HRZE carry to HPMZ, which swaps rifampicin for rifapentine and ethambutol for moxifloxacin?
- The Advocate says this is "unverified in the critique's own evidence." The verifier's finding is a genuine gap, not a REJECTED claim. The Advocate also concedes it "cannot show transferability from HRZE" (Concession 2).
- A gap that cuts against the defender's ability to claim transfer is not neutral. CG's model assumes full transfer for 100% of the pool.

> The Advocate claims: the 40% p_success, covering Phase II and III, already discounts for failure to generalise.

- p_success is a probability that the trial shows an effect. It is not a coverage factor for the share of future patients to whom a positive result applies.
- A positive Phase III on HRZE can succeed and still apply to only 60–80% of patients if the regimen mix has shifted. These are separate risks, and the 40% does not absorb the second.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the 20–40% range is ungrounded, and the only grounded uptake evidence (WHO's conditional recommendation, rifapentine availability) points to the low end.

- I concede the range is a scenario, and the critique says so. The "at or near 3.6M" conclusion is conditional on it.
- Two limits on the slow-uptake inference:
  - The evidence describes current constraints, namely a conditional recommendation and rifapentine availability. Those are supply and cost frictions, not a ceiling on adoption.
  - The benefit horizon is about year 8–9 after the grant, which the Advocate itself stresses. Current slow uptake is weak evidence about regimen share that far out. I cannot ground a trajectory, so this is an open question, not a counter-estimate.
- The Advocate says forecasting uncertainty applies equally to CG's implicit 0% (Magnitude point 3). I accept that. The implication is that the correct input is a distribution over displacement. Any distribution with positive mean lowers SROI below the point estimate. Zero is the extreme edge of the uncertainty, not a neutral default.

> The Advocate claims: HPMZ is not the default even for ages 12+, since adolescents aged 12–16 have 2HRZ(E)/2HR and standard 6-month options.

- The verifier's evidence shows the 2HRZ(E)/2HR alternative applies only to non-severe TB in children under 16.
- For people 16 and older, the options are HPMZ or the standard 6-month regimen. So the Advocate's point covers only the 12–16 slice of the 12+ group.
- I cannot ground the age distribution of the pool. I disclaim any claim about how large the 12–16 slice is. The point simply does not generalise to adults.

> The Advocate claims: TRUNCATE-TB and bedaquiline-based DS-TB regimens are not near-term displacement drivers.

- Agreed. The critique itself made this correction and the point should stay corrected. It leaves HPMZ as the sole driver, which is the critique's core case anyway.

> The Advocate claims: the rifapentine interaction direction is unverified and could cut either way.

- It is unverified, not rejected. The Advocate concedes it could reduce statin exposure by more than rifampicin does (Concession 5).
- I do not claim it is erosion evidence. It is another untested step in the transfer assumption.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: SROI scales linearly, so only the upper half of the range crosses the bar.

- The arithmetic checks out: 3,000 × 0.8 = 2,400, 3,000 × 0.7 = 2,100, and 3,000 × 0.6 = 1,800.
- The Advocate's "3–17% overshoot" does not follow from these numbers. 2,100 against 2,000 is 5% above the bar, 2,400 is 20% above, and 1,800 is 10% below.
- The bar-crossing displacement is 1 − 3.6/5.5 ≈ 35%, or 33% on the Advocate's 2,000/3,000 framing.
- On a uniform distribution over 20–40%, the probability of crossing is roughly (40−34)/20 ≈ 30%. The critique's own view that the low end is likelier would lower that. I treat it as my derivation from the critique's assumed range, not as grounded.
- The residual is that a 20–40% displacement consumes most of the headroom, which is roughly 35% in pool terms. It is not mandatory to cross the bar for this to matter. The margin left for any other parameter error shrinks from about 35% to about 5–15%.
- The Advocate's "3–17% overshoot" frames this as safe. A 5% cushion at the midpoint is thin, not comfortable.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: an adaptive Phase III could track the prevailing regimen, so displacement would not reduce applicability.

- The Advocate labels this "reasoning, not evidence."
- If it is correct, adaptation adds costs: arms, enrolment, time. The model has no line for those costs, and the shift in the transfer risk is only moved into trial design.
- Testing statin on HPMZ is exactly the evidence gap the verifier found. Adding that arm raises the Phase III failure risk, which CG's 40% was not calibrated for.

> The Advocate claims: omitted benefit channels (morbidity, lung damage, transmission) could outweigh a 20–40% pool reduction.

- This is a claim that CG's model is conservative, not that displacement is already priced in.
- It applies equally to every critique of the model and is not specific to this one. It cannot offset a regimen-transfer loss unless someone quantifies the omitted channels. The Advocate does not, and calls the lung-damage channel speculative.
- The verifier found no evidence that the statin acts on lung damage, so this is a conditional with no grounding.

**KEY UNRESOLVED QUESTIONS:**
- What share of DS-TB patients aged 16 and over will be on HPMZ, or another non-HRZE backbone, by about year 8–9? The WHO conditional recommendation and rifapentine supply constraints describe the present, not the horizon.
- Does the statin's 10% relative on-treatment mortality effect hold with rifapentine and moxifloxacin? Neither side has evidence, and the verifier found none.
- Is the 60% uptake independent of regimen composition? If CG has any internal derivation, the overlap question resolves. If not, the multiplicative treatment is the default.
- Would an adaptive Phase III covering HPMZ change the 40% p_success or the 8-year timeline? Neither side has grounded this.

### Judge Audit
Surviving strength: moderate
Justification: The Challenger made grounded, well-caveated moves the Advocate could not answer:
- p_success is distinct from applicability share.
- Non-negative displacement implies 0 is an edge case, not a neutral default.
- The headroom arithmetic holds.
The Advocate conceded that CG has no regimen-change adjustment and cannot show transfer. However, the critique's headline claim ("at or near 3.6M") depends entirely on an ungrounded 20–40% range. Grounded evidence tilts toward the low end, where the bar is not crossed. Both sides' speculative offsets (adaptive trials, omitted channels) were weak. What survives is a real but unquantified unmodelled factor, not a demonstrated bar-crossing.
Recommended action: 1. CONCLUDE NOW: The critique identifies a valid structural omission. CG's BOTEC applies HRZE-derived benefit to 100% of the future DS-TB pool with no regimen-transfer adjustment. The quantitative claim that this pushes the grant to the bar does not survive, because it rests on an ungrounded range whose likelier low end leaves SROI above the bar at about 2,400x. Moderate confidence on three points:
   - Replace the implicit 0% displacement with an explicit, modest displacement parameter. The ~10–20% suggested by the critique's own reasoning about the low end is a scenario anchor, not a grounded estimate.
   - Run a sensitivity check showing the bar-crossing threshold at ≈33–35%.
   - Flag effect transfer to HPMZ as an untested assumption.

   An optional, feasible refinement is to pull rifapentine procurement volumes from the Global Drug Facility, plus any national programme HPMZ adoption reports. This would be a short targeted search with existing tooling that could anchor the displacement trajectory.
Action feasibility: actionable_now
Advocate failures: ['unsupported_estimate_pseudo: The Advocate described the central scenario as "a roughly 3–17% overshoot relative to the bar." This does not follow from its own figures of 2,400x, 2,100x and 1,800x against a ~2,000x bar. Those figures give +20%, +5% and −10%. The Challenger correctly caught this.', "sound_synthesis_noted: The SROI linear-scaling calculation (3,000 × 0.8 / 0.7 / 0.6 against a ~2,000x bar) is a transparent, checkable synthesis. The 2,000/3,000 ratio (≈0.67) is consistent with the 3.6M/5.5M bar (≈0.65). It correctly shows that only the upper part of the critique's range crosses the bar. Note that the 3,000x and 2,000x inputs come from CEA materials the verifier could not check.", 'call_to_ignorance: The Advocate argued that omitted channels ("morbidity DALYs, lung damage reduction, post-treatment mortality, transmission averted… could outweigh a 20–40% reduction") might offset the loss. No magnitude was offered, and the lung-damage channel is self-described as speculative. Labelling it "speculative" is partial mitigation, but the move still asks unquantified possibilities to offset a quantified loss.', 'call_to_ignorance: The Advocate claimed the Phase III "could plausibly adapt to the prevailing standard regimen." This is labelled "reasoning, not evidence," so the mitigation is honest. It still has no grounding that adaptation is planned or feasible within the 40% p_success and 8-year assumptions.', 'whataboutism: Magnitude point 3 says "The same uncertainty applies to the critique\'s 20–40% range as to CG\'s implicit 0%." This deflects rather than defends. As the Challenger showed, symmetric uncertainty over a non-negative quantity actually argues against a point estimate of 0, so the move backfires.', 'misrepresenting_evidence_status: Evidence weakness 3 says "HPMZ is not the default even within its eligible age group" because 12–16-year-olds have 2HRZ(E)/2HR options. The verifier limits that regimen to non-severe TB in under-16s. The Advocate generalised a narrow-scope finding to the whole 12+ group.']
Challenger failures: ["sound_synthesis_noted: The Challenger derived a bar-crossing displacement of ≈33–35% (1 − 3.6/5.5) and a ~30% crossing probability under a uniform 20–40% distribution. It explicitly flagged this as a derivation from the critique's assumed range, not a grounded estimate. The steps are shown and the caveats are honest.", 'sound_synthesis_noted: The Challenger made two further sound moves:', 'false_definitiveness: The Challenger asserted that "Adding that arm raises the Phase III failure risk, which CG\'s 40% was not calibrated for," and that adaptation "adds costs." Both are stated as fact with no grounding. They mirror the Advocate\'s speculative offset with a speculative counter.', 'misrepresenting_evidence_status: The Challenger claimed "The verifier found no evidence that the statin acts on lung damage, so this is a conditional with no grounding." The verifier\'s gap concerned statin effects on shorter regimens; it did not search for lung-damage mechanisms. The Challenger turned not-investigated into not-found.']
Debate resolved: The debate removed several limbs from the critique:
- TRUNCATE-TB and bedaquiline regimens are not near-term displacement drivers.
- The paediatric 2HRZ(E)/2HR regimen creates no transfer problem.
- The "duration-shortening adjunct" limb does not bite against CG's mortality-based mechanism.

This leaves HPMZ uptake among people aged 16+ and effect transfer as the sole live channel. The debate also established that:
- p_success does not absorb applicability share.
- The bar is crossed only at displacement of ≈33–35% or more.
- The critique's own preferred low end (~20%) leaves SROI above the bar but consumes most of the headroom.
Debate unresolved: Three questions remain open:
- The actual HPMZ, or other non-HRZE, share among DS-TB patients aged 16+ at year 8–9. Both sides agree current slow uptake is weak evidence about the horizon.
- Whether the 10% relative on-treatment mortality effect transfers to a rifapentine/moxifloxacin backbone.
- Whether the 60% uptake parameter is independent of regimen composition.

--- Critique: M72/AS01E and other incidence shocks are likely not large enough by year 8–10, but should be modelled ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: M72/AS01E and other incidence shocks are likely not large enough by year 8–10, but should be modelled

EXISTING COVERAGE:
1. The CEA already includes a secular incidence decline. New cases fall 2% per year for 8 years (parameters: decline_per_year, eligible_people_at_8y). That compounds to roughly 1 − 0.98^8 ≈ 15% lower incidence at adoption. This is a generic trend assumption, not a vaccine-specific one, so I do not claim it explicitly models M72. But it is a downward adjustment of the same kind the critique asks for, and the critique does not say why 2% per year would not already include some vaccine-related decline.
2. The critique's "benefit horizon beyond ~15 years" and "average eligible 20–35% lower" arguments do not fit the CEA's structure.
   - The BOTEC credits a 1-year speedup applied to one cohort of 5.5M at adoption (year 8). It does not integrate benefits over a long horizon.
   - Only the eligible population at year 8 enters the formula. Post-adoption years are not modelled, so there is no "average eligible over the horizon" to reduce.
   - The critique itself says "I cannot determine this without seeing how the CEA treats post-adoption years." The parameter map answers that: the CEA has no post-adoption years.
   - The 20–35% figure is therefore not applicable, and the relevant effect is the –5 to –15% at year 8.
3. A separate probability of vaccine success is partly redundant. The CEA's 40% Phase II/III success probability applies to statins, not to M72. Any vaccine scenario is itself probabilistic, so its expected effect on the year-8 population is the conditional effect multiplied by the vaccine's success probability.

EVIDENCE WEAKNESSES:
1. The critique flags its own key numbers as UNGROUNDED: the 5–15% incidence reduction by 2033–35, the 30–50% later-year reduction, and the 20–35% average-eligible reduction. It says "I did not extract specific numbers." The sensitivity results are empty ({}). No quantified case is on the table.
2. The only direct input cited is the Phase IIb efficacy of 49.7% (95% CI 2.1–74.2).
   - The population was IGRA+, HIV-negative, previously sensitised adolescents and adults, with 3 years of follow-up.
   - The lower CI bound (2.1%) is close to zero.
   - Efficacy in HIV-positive people was not assessed, and that group carries a large share of TB deaths. This weakens any projection of population-level incidence effects in the settings the statin trial targets.
3. The critique concedes that Harris 2019 is a generic China age-targeting model, not an M72 projection. The M72-specific South Africa and India models are mentioned but no numbers are extracted, so they currently support only "such models exist."
4. The 10-year duration of protection is described as "an assumed value in one model." That is an assumption, not an observation.

MAGNITUDE CHALLENGE:
1. Derivation of a plausible bound on the year-8 effect. Population incidence reduction ≈ efficacy × effective coverage of the incidence-generating population, ignoring waning and indirect effects.
   - Using the Phase IIb point estimate of 49.7%, a 5% reduction requires about 0.05/0.497 ≈ 10% effective coverage.
   - A 15% reduction requires about 0.15/0.497 ≈ 30% effective coverage.
   - The critique itself puts licensure at ~2028–30 with slow rollout, leaving only ~3–5 years of rollout before 2033.
   - The Phase IIb efficacy applies to IGRA+, HIV-negative people. Real-world effective efficacy across the whole target population is likely lower, which pushes the required coverage up.
   - So the low end (~5%) looks more plausible than the high end (~15%). This is my synthesis from the critique's own inputs, not an attested figure.
2. The critique's –5 to –15% appears to be conditional on vaccine success, as it separately says success probability "should be weighted." If the vaccine succeeds with probability p < 1, the expected reduction is p × (5–15%). At an illustrative p = 50% (I cannot ground this value), that gives 2.5–7.5%.
3. Linearity. The SROI formula is linear in eligible_people. A –5% to –15% change in the eligible population moves SROI from ~3,000x to ~2,550–2,850x. That is below the ~25% materiality threshold set in the run context. Only the critique's unapplicable 20–35% horizon-average range would approach that threshold.
4. The critique's own title says the shocks are "likely not large enough by year 8–10." Its materiality rating is "notable," not "decision-relevant."

OFFSETTING FACTORS:
1. The 2% annual decline already removes ~15% of cases by year 8. If some of the decline reflects TB-control improvements that would also be fed by new tools, the vaccine effect is partly double-counted. I cannot quantify the overlap.
2. The 2% decline is itself uncertain in both directions. The parameter map notes the CEA has no sensitivity to the baseline year of notifications. Population growth or improved case detection in high-burden countries could raise notified cases, offsetting a vaccine-driven decline. I cannot ground a magnitude for this.
3. The vaccine reduces new TB cases, not necessarily the share of treated cases that die. The relevant statin parameters (6% baseline mortality, 60% uptake) stay the same per treated case. The shock acts only through case counts.
4. A vaccine that lowers incidence could, over time, also reduce the transmission-driven case load. That is an additional downward effect and is not an offset, but it is also outside the year-8 window the critique projects.

OVERALL ASSESSMENT:
Strong defense.
- The critique's largest-magnitude claim (20–35% average-eligible reduction over a long horizon) misreads the CEA's structure. The BOTEC uses a one-year speedup applied to the year-8 cohort and has no long post-adoption horizon.
- The critique's applicable claim (–5 to –15% at year 8) is ungrounded, has no sensitivity results, and by my derivation is likely at the low end. Even at –15%, SROI stays within the ~25% materiality band.

CONCESSIONS:
1. The CEA does not mention M72 or any named incidence shock, and the 2% decline is not derived from any source. A short sensitivity run on decline_per_year would be inexpensive and would be good practice.
2. If the CEA were extended to model post-adoption years, the critique's horizon argument would become relevant. The current formula does not do this.
3. The direction of the effect (lower eligible population) is plausible, and the vaccine's success probability should be weighted if it were modelled.
4. Harris 2019 is not a suitable M72 citation. M72-specific models would be better sources for any future version.
```

### Challenger
REBUTTAL: M72/AS01E and other incidence shocks

I concede some points up front. The defense is right that the critique's 20–35% horizon-average figure does not fit a single-cohort year-8 BOTEC. It is also right that the –5 to –15% figure is ungrounded and that the low end is more plausible than the high end. My rebuttal covers what remains after those concessions.

---

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: The CEA's 2%/year secular decline (~15% over 8 years) is the same kind of adjustment the critique asks for, and the critique does not explain why it would not already absorb some vaccine effect.

Response:
1. The Advocate concedes that the 2% is "not derived from any source" and is "not vaccine-specific." An unsourced generic trend cannot be said to cover a specific, identifiable intervention.
2. The "absorbs some vaccine effect" claim fails on arithmetic. Converting the critique's range into an equivalent annual rate:
   - A 5% year-8 reduction is (0.95)^(1/8) ≈ 0.9936, or about 0.6 percentage points per year.
   - A 15% reduction is (0.85)^(1/8) ≈ 0.980, or about 2.0 percentage points per year.
   - So the vaccine effect equals one-third to all of the existing 2% decline.
   - For the 2% to contain the vaccine effect, a pre-licensure secular trend would have to be largely vaccine-driven. That contradicts the Advocate's own description of it as generic.
3. If instead the 2% reflects the historical secular trend, which predates any M72 rollout, then a vaccine effect is incremental to it. Whether it is incremental or already included is itself an open question. The Advocate resolves it by speculation, and the burden-shifting ("the critique does not say why 2% would not already include...") does not answer it.
4. The Advocate does not say whether the 5.5M figure is before or after the 8-year decline. The critique calls it "constant." If it is post-decline, the vaccine effect is additive. If it is pre-decline, the baseline is different again. This is a structural ambiguity that the "already covered" argument depends on.

> The Advocate claims: A separate success probability is "partly redundant" because the CEA's 40% Phase II/III probability applies to statins, not M72.

Response:
1. This argument undercuts itself. The 40% applies to statins, so there is no M72 success probability anywhere in the CEA. That makes it a missing parameter, not a redundant one.
2. The Advocate's own magnitude section then multiplies by an M72 success probability p. The Advocate agrees, in effect, that p must be modelled. "Redundant" and "the expected effect is conditional × p" cannot both be the position.

> The Advocate claims: The 20–35% horizon-average reduction is inapplicable because the CEA has no post-adoption years.

Response:
1. Conceded, conditional on the Advocate's reading of the parameter map. The critique itself said it could not judge this without seeing the CEA's structure.
2. This concession narrows the debate to the year-8 effect, so the question becomes whether –5 to –15% (or the probability-weighted version) is worth a sensitivity run. It does not make the critique wrong.

---

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: The critique self-flags its numbers as UNGROUNDED, has empty sensitivity results, and the M72 models are cited without numbers.

Response:
1. The self-flagging is accurate and I do not defend the 5–15% figure as measured. That is a statement about the critique's precision. It is not evidence that the effect is zero or negligible.
2. The verifier did not REJECT any part of this. The existence of M72-specific South Africa and India models and a global demand forecast was confirmed. The missing step is extraction of the numbers, and the Advocate did not extract them either. The Advocate's own anchor, p = 50%, is explicitly "illustrative… cannot ground."
3. Both sides are therefore reasoning from the same 49.7% (95% CI 2.1–74.2) Phase IIb input. The correct conclusion is that the magnitude is open, not that it is small.

> The Advocate claims: HIV-positive people were not assessed, the lower CI bound is near zero, and 10-year protection is only an assumption.

Response:
1. The wide CI and the HIV-negative restriction are genuine reasons to expect lower real-world effect. I concede this, and it supports the critique's own "retained" language that the effect is unlikely to be large by 2033–35.
2. The 10-year duration assumption matters only for long horizons. For a year-8 effect it matters little, since 3 years of observed efficacy covers much of a 2030–34 rollout window. The Advocate cannot use it against the year-8 estimate while also saying the long horizon is inapplicable.
3. The efficacy population (IGRA+) is, plausibly, much of the population that generates incident adult TB through reactivation. I cannot ground the share, so treat this as uninformed. The Advocate's claim that effective efficacy is "likely lower" across the target population is equally ungrounded.

---

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: Required effective coverage is 10% for a 5% reduction and 30% for a 15% reduction. Given 3–5 rollout years, the low end is more plausible, and at p = 50% the expected effect is 2.5–7.5%.

Response:
1. The derivation is sound as a synthesis, and I accept the low end as more plausible. Each step follows from the critique's inputs: 0.05/0.497 ≈ 10% and 0.15/0.497 ≈ 30%.
2. The chain does not show that 10% effective coverage is hard to reach. The Advocate gives no reason why 10% coverage of the incidence-generating population by year 8 is implausible, only that 30% is. I cannot ground a coverage estimate for this window and do not claim one.
3. The minimum defensible effect is therefore about 2–3% at year 8, taking the low end of the Advocate's expected-value range. That is small. The strongest residual case is the upper tail: if the vaccine succeeds and rollout is faster than assumed, the effect approaches 15%. I cannot ground the probability of that tail.

> The Advocate claims: Linearity puts a 15% reduction at SROI ~2,550x versus ~3,000x, below the 25% materiality threshold, and the critique itself calls the shocks "likely not large enough."

Response:
1. Conceded on arithmetic. A 15% change in a linear input is a 15% change in output, and the critique's own materiality tag is "notable," not "decision-relevant."
2. The residual point is that 15% is 60% of the threshold, and the CEA's decline_per_year is untested. Moving it from 2% to 3% alone shifts eligible people by (0.97/0.98)^8 − 1 ≈ −7.9%. The vaccine's plausible effect is therefore the same order as an uncertainty the CEA does not currently test. This supports the Advocate's materiality argument but also supports a sensitivity run, which the Advocate concedes would be "good practice."

---

**RESPONSE TO "OFFSETTING FACTORS":**

1. Offset 1 (double-counting with the 2% decline): the Advocate admits it cannot quantify the overlap. It is also weak on its own logic, because a historical secular trend cannot contain a vaccine not yet licensed.
2. Offset 2 (population growth and case detection raising notifications): the Advocate admits it cannot ground a magnitude. This offset is hypothetical, and nothing in the CEA models it.
3. Offset 3 (the vaccine acts on case counts, not on the statin parameters): this is not an offset. It only says the shock enters through one parameter, which is how the critique already framed it.
4. Offset 4 (transmission effects): the Advocate itself says this is "not an offset" and lies outside year 8.
5. Net: none of the four offsets is quantified, and two are not offsets at all. The "other incidence shocks" in the critique's title (e.g. other vaccine candidates, expanded preventive therapy, or incidence-raising shocks) are not addressed by the Advocate at all. The defense treats the critique as an M72-only claim.

---

**KEY UNRESOLVED QUESTIONS:**
- Is the 5.5M eligible-population figure before or after the 2%/year decline? This determines whether any vaccine effect is incremental.
- What do the M72-specific South Africa and India models project for year-8 (c. 2033–35) incidence, and what coverage do they assume? Both sides need those numbers, and neither extracted them.
- What probability should M72 licensure by ~2028–30 carry? The Advocate's 50% is explicitly unsupported.
- Does the 2% decline come from a sourced trend (and what is its historical range), or is it a placeholder? Moving it from 2% to 3% alone is about as large as the vaccine effect.
- Does the single-cohort year-8 structure hold, or do the statin benefits persist beyond one cohort? If they persist, the critique's horizon argument returns.

### Judge Audit
Surviving strength: weak
Justification: This verdict does not reflect an unproductive debate. Both sides offered sound syntheses: the Advocate's coverage derivation and linearity argument, and the Challenger's annualisation and decline-rate sensitivity. The critique is weak because the Challenger, on the substance, conceded the inapplicability of the horizon argument, the plausibility of the low end, and the sub-threshold arithmetic. The Challenger's remaining moves rested on an ungrounded 2–3% floor, an ungrounded upper tail, and a tu quoque on efficacy. What survives is not the critique's M72-specific claim. It is a separate, adjacent point that decline_per_year is unsourced and untested. The Advocate had already conceded that point.
Recommended action: 1. CONCLUDE NOW (moderate-high confidence): Under the CEA's single-cohort year-8 structure, an M72 incidence effect is not decision-relevant. Even the conditional upper bound (−15%) moves SROI by less than the materiality threshold, and the probability-weighted, realistic-rollout effect is likely in the low single digits.

   Two cheap, specific checks should accompany this conclusion, both feasible within existing tooling:
   - (a) Confirm from the CEA spreadsheet whether 5.5M is computed after the 2%/yr decline.
   - (b) Run a one-way sensitivity on decline_per_year over roughly 1–5%/yr. The upper end should be informed by the End TB-style scale-up assumption in the verifier-cited India modelling.

   If (b) shows SROI crossing the materiality threshold at plausible decline rates, open a new critique on the secular-decline parameter. Do not reopen it as an M72 critique. Drop the horizon-average claim unless the CEA is later extended to post-adoption cohorts.
Action feasibility: actionable_now
Advocate failures: ["sound_synthesis_noted: The coverage derivation: population incidence reduction ≈ efficacy × effective coverage, so 0.05/0.497 ≈ 10% and 0.15/0.497 ≈ 30% effective coverage. This is combined with the critique's own ~2028–30 licensure and slow-rollout framing to argue the low end is more plausible. Each step is shown and labelled as synthesis. The Challenger accepted it.", 'sound_synthesis_noted: The linearity argument. SROI is linear in eligible_people, so a −5% to −15% change moves ~3,000x to ~2,550–2,850x, below the ~25% materiality threshold. This is the decisive move of the debate, and it is grounded in the CEA structure, not in guesswork.', 'unsupported_estimate_fabricated: At an illustrative p = 50% (I cannot ground this value), that gives 2.5–7.5%." The value is disclosed as ungrounded, which lessens the failure. It is minor because the Advocate\'s materiality conclusion does not depend on it: the linearity argument holds even at p = 1.', 'call_to_ignorance: Existing Coverage 1 says "the critique does not say why 2% per year would not already include some vaccine-related decline." Offset 1 adds "the vaccine effect is partly double-counted. I cannot quantify the overlap." Both suggest the existing decline might absorb the vaccine effect only because no one has shown it doesn\'t. This also shifts the burden of proof to the critic.', 'call_to_ignorance: Offset 2 says population growth or improved case detection "could raise notified cases, offsetting a vaccine-driven decline. I cannot ground a magnitude for this." This is a speculative offset with no evidential anchor.', 'false_definitiveness: The self-assessment is "Strong defense," yet the "partly redundant" success-probability argument contradicts itself. The Advocate says the CEA\'s 40% applies to statins, which means there is *no* M72 probability in the model. The Advocate\'s own magnitude section then multiplies by an M72 p. The overall defense is good, but this section is presented more confidently than its logic supports.']
Challenger failures: ['sound_synthesis_noted: Converting the year-8 range into annual rates: (0.95)^(1/8) ≈ 0.6 pp/yr and (0.85)^(1/8) ≈ 2.0 pp/yr. This shows the vaccine effect would equal one-third to all of the existing 2% decline. It is correct arithmetic and engages directly with the Advocate\'s "already covered" claim.', 'sound_synthesis_noted: (0.97/0.98)^8 − 1 ≈ −7.9% for moving decline_per_year from 2% to 3%. The 3% is an illustrative choice, not an estimate. As an illustration it validly shows the untested parameter carries uncertainty of the same order as the vaccine effect.', 'strawmanning: a historical secular trend cannot contain a vaccine not yet licensed." The Advocate never described the 2% as historical. It is a forward-looking 8-year projection, which could in principle embed expected new tools. The Challenger hedged correctly in Existing Coverage point 3 ("If instead...") but drops the hedge in the Offsets response and treats the historical reading as settled.', 'unsupported_estimate_pseudo: The minimum defensible effect is therefore about 2–3% at year 8, taking the low end of the Advocate\'s expected-value range." This floor rests on the Advocate\'s p = 50%, which the Challenger had just criticised as ungrounded. The "therefore" does not follow from grounded components.', 'whataboutism: The Advocate\'s claim that effective efficacy is \'likely lower\' across the target population is equally ungrounded." This contradicts the Challenger\'s own concession two points earlier that the HIV-negative restriction and wide CI are "genuine reasons to expect lower real-world effect." The Advocate\'s directional claim *is* grounded in verifier-confirmed population restrictions. Calling it equally ungrounded is a tu quoque, not engagement.', 'call_to_ignorance: The strongest residual case is the upper tail: if the vaccine succeeds and rollout is faster than assumed, the effect approaches 15%. I cannot ground the probability of that tail." Even granting the tail, 15% stays below the materiality threshold the Challenger had already conceded.', 'misrepresenting_evidence_status: The \'other incidence shocks\' in the critique\'s title... are not addressed by the Advocate at all." The critique\'s mechanism and evidence concern only M72. The verifier package contains nothing on other shocks. Faulting the Advocate for not rebutting claims that were never substantiated treats an absent argument as an unanswered one.']
Debate resolved: Both sides agreed that the critique's 20–35% horizon-average reduction does not apply to a BOTEC that credits a single year-8 cohort. They also agreed that the applicable year-8 effect (−5 to −15%, low end more plausible, lower still once success probability is weighted) cannot reach the ~25% materiality threshold, because SROI is linear in eligible_people. The vaccine-specific critique therefore does not survive as a decision-relevant adjustment under the current CEA structure.
Debate unresolved: Two questions remain open:
- Whether the 5.5M eligible figure is already net of the 2%/yr decline, and so whether any vaccine effect is incremental to it.
- Whether decline_per_year itself is well set. The Challenger showed a 1 pp change moves eligible people by ~8%, and the unused verifier evidence suggests scenarios with far steeper declines.

Whether statin benefits really end with a single cohort was raised but not argued by either side.