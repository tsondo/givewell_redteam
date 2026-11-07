--- Critique: "Success" in Phase III is unlikely to be a mortality result, so the 10% mortality effect is not what a "success" would establish ---

### Advocate
```
DEFENSE OF GIVEWELL'S (CG'S) POSITION: "Success" in Phase III is unlikely to be a mortality result, so the 10% mortality effect is not what a "success" would establish
```

**EXISTING COVERAGE**

- The BOTEC does not define "success" (see CONCESSIONS). It does not assume a mortality-powered Phase III either. It says only that "a positive result is assumed to cut [mortality] by 10% relative" and that there is a 40% chance both Phase II and III succeed.
- The 10% and the 40% are two subjective judgments that form one expected effect of 4%. Neither is derived from a stated reference class. Both are CG's all-things-considered priors. The critique treats the 40% as fixed and re-prices only the 10%. That is internally one-sided (see MAGNITUDE CHALLENGE).
- The Phase IIc trial is explicitly designed to test "survival, infection clearance and lung damage." Survival is already a named endpoint in the program being funded, so a mortality signal is not outside the evidence-generation plan.
- The BOTEC values only on-treatment mortality. The parameter map lists four zero-valued channels: morbidity DALYs, post-treatment mortality, transmission averted, and diagnostic value. The context names reduced lung damage on chest X-ray as the Phase IIa/b finding, and it is not valued. Surrogate-only success worlds are therefore not zero-value worlds in the underlying reality. The model just doesn't count what they would deliver.

**EVIDENCE WEAKNESSES**

1. The sample-size arithmetic uses a 4% baseline, but CG's baseline is 6%. Using the critique's own standard formula (80% power, α = 0.05) at CG's numbers (6% → 5.4%):
   - Variance term: 0.06×0.94 + 0.054×0.946 = 0.0564 + 0.0511 = 0.1075.
   - n per arm = 7.84 × 0.1075 / (0.006)² ≈ 23,400, or about 47,000 total.
   - This is still very large, so the core point survives. But the critique's 36,000 per arm is about 50% too high for CG's own inputs.
2. The 2% baseline figure is "as I recall," and the claim that no TB trial approaches this scale is unsourced. The critique itself flags this. The 8% HIV-enriched case (17,000 per arm) shows the requirement is sensitive to enrichment strategy, and CG could choose a higher-risk population.
3. The cited review concerns 2–3 month LJ culture positivity as a surrogate for long-term clinical outcome. The evidence package does not say it is about statins, adjunctive host-directed therapy, or mortality specifically. It is adjacent evidence about culture surrogates in general. It does not establish that a statin surrogate success would leave mortality unaffected.
4. The rosuvastatin trial finding no effect on culture conversion is evidence about whether the surrogate succeeds. That bears on p_success, a separate parameter, not on E[r | success]. It does not show that surrogate success would coexist with no mortality effect.
5. The inference from "a mortality-powered trial is implausible" to "success therefore does not imply a mortality effect" has a gap. Guideline bodies can adopt a cheap, generic, low-risk adjunct on surrogate evidence. If so, the true mortality effect conditional on adoption is positively correlated with the surrogate effect. It is not necessarily zero.
6. The parameters f (share of surrogate-only successes) and r_s (their true mortality effect) are both assumptions. The critique states that r_s = 0.03 is "my assumption, not sourced." The quantifier central of 0.07 implies f ≈ 0.43 at r_s = 0.03, solving (1−f)(0.10) + f(0.03) = 0.07. That f is also unsourced.

**MAGNITUDE CHALLENGE**

- SROI is linear in r. Baseline is about 3,055 at r = 0.10, so SROI = 3,055 × r/0.10. The 2,000x bar is crossed at r ≈ 0.0655.
- Crossing the bar requires:
  - f ≥ 0.345 if surrogate-only successes have zero mortality effect (r_s = 0), since 0.10(1−f) = 0.0655.
  - f ≥ 0.49 if r_s = 0.03, since 0.10 − 0.07f = 0.0655.
- The quantifier's own central case (r = 0.07) gives about 2,138x, which is above the bar. Only the low case (r = 0.05) crosses it. The bar-crossing claim therefore rests on the pessimistic end of two unsourced parameters acting together.
- The critique holds p_success at 40% while lowering r | success. Consider the two readings of CG's 40%:
  - If it was set against a mortality-relevant definition of success, the surrogate-only worlds are not "successes" and the critique's mechanism doesn't apply.
  - If it was set against a looser surrogate-based success, then 40% is lower than it would otherwise be, because a looser hurdle should have a higher pass probability. In that case p × r is partly protected, and the right comparison is p_surrogate × r_s plus p_mortality × 0.10, not a simple haircut on r.
  - In both readings the product is less exposed than the critique's one-sided haircut implies. I cannot quantify the offset, because CG gives no reference class.
- A zero r_s requires the surrogates (bacterial load, culture conversion, lung damage on X-ray) to be entirely uninformative about death. The critique's own review calls culture a poor surrogate for long-term outcome. That is weaker than zero.

**OFFSETTING FACTORS**

1. Unvalued benefit channels (morbidity, post-treatment lung-damage consequences, transmission, diagnostic value) are implicit zeros in the BOTEC. In surrogate-success worlds, these channels, especially reduced lung damage, are the ones most likely to carry value. The parameter map notes this could "make the estimate robust even if Thread 1 finds a small on-treatment mortality effect."
2. The sweat-based diagnostic workstream is funded in the grant but contributes no value. Its inclusion in the $7M cost with zero benefit is a conservative structural choice, though the parameter map notes it is unclear whether it sits inside the $7M.
3. Higher p under looser success definitions (see above).
4. The 10% relative reduction is modest. It is 0.6 percentage points on a 6% baseline. A drug effective enough to deliver a clear surrogate success could plausibly deliver a mortality effect of that size.

**OVERALL ASSESSMENT**

Partial defense.

- The critique correctly identifies that CG never defines "success." Its core logic (a mortality-powered Phase III is implausible, so 10% | success is overstated) is sound in direction.
- The magnitude is overstated:
  - The sample-size inputs don't match CG's baseline.
  - f and r_s are unsourced.
  - The mechanism holds p fixed.
  - The quantifier's central case stays above the bar.
- I cannot show that the critique's central 30% reduction is wrong. I can only show it is unanchored and that it ignores offsets in p and in unvalued benefit channels.

**CONCESSIONS**

- CG does not define "success," and the parameter map confirms the BOTEC is silent on whether it means mortality or surrogate benefit.
- A mortality-powered Phase III would need about 47,000 participants at CG's own 6% baseline (about 23,400 per arm). That is very large for the $7M all-in cost.
- E[r | success] is plausibly below 10% if surrogate-only success is common. The 30% reduction in the quantifier's central case exceeds CG's 25% materiality threshold, even though it does not cross 2,000x.
- The independence of p_success and relative_reduction is not justified in the BOTEC. A joint treatment would be more defensible than either parameter alone.
- I cannot supply a grounded estimate of f or r_s. Any value I gave would be an uninformed prior.

### Challenger
REBUTTAL: "Success" in Phase III is unlikely to be a mortality result, so the 10% mortality effect is not what a "success" would establish

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: The BOTEC is silent on what "success" means. The Phase IIc design names survival as an endpoint. The BOTEC also zero-values several benefit channels (morbidity, lung damage, transmission, diagnostics), so surrogate-only worlds are not zero-value worlds in reality.

- **Silence is not coverage.** The Advocate concedes that CG never defines "success." The 10% is therefore not an adjusted figure that already embeds surrogate-only outcomes. It is an unconditioned figure applied to an undefined event.
- **"Survival is a named endpoint" does not answer the critique.**
  - The 10% is conditional on Phase III success, not on Phase IIc.
  - Listing survival as an endpoint says nothing about whether any funded trial is powered to detect a 10% mortality effect.
  - By the Advocate's own arithmetic, that would take about 47,000 participants at CG's 6% baseline. No Phase IIc is that size.
- **The unvalued channels are not a rebuttal to this critique.**
  - The critique concerns whether E[r | success] is 0.10 on the on-treatment mortality channel.
  - Value in other channels is not in the model, and no one has quantified it.
  - Those channels may support a different CE estimate, but they do not repair the parameter being challenged.
  - The Advocate cites the parameter map's remark that unvalued channels could make the estimate "robust." That is a hypothesis about unmodeled value, not a quantified offset.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

*Point 1 (sample size at 6% baseline).* I concede this fully.
- I rechecked the Advocate's arithmetic: 7.84 × 0.1075 / 0.006² ≈ 23,400 per arm. It is correct.
- The critique's 36,000 per arm used a 4% baseline, not CG's 6%.
- The correction does not change the conclusion. About 47,000 participants is still far beyond what a $7M all-in program can fund.

*Point 2 (enrichment).*
- The Advocate says CG could pick a higher-risk population. I checked the critique's 8% case with the same formula: 7.84 × (0.0736 + 0.0668) / 0.008² ≈ 17,200 per arm, about 34,400 total.
- Even under favorable enrichment, a mortality-powered trial is roughly 34,000 or more participants.
- The enrichment objection therefore does not rescue the "mortality-powered Phase III" reading.

*Point 3 (the review is generic).*
- Conceded: the review concerns 2–3 month LJ culture positivity as a surrogate for long-term clinical outcome, not statins specifically.
- The verifier also found that the prior human atorvastatin data are on surrogates (bacterial load).
- Together these establish the two links the critique needs:
  - The available statin evidence is on surrogates.
  - Culture-based surrogates are not accepted as predictors of long-term outcome.
- The Advocate cannot cite any statin evidence on mortality.

*Point 4 (rosuvastatin bears on p, not r).*
- This is correct for the null result's direct role.
- The result also shows that surrogate effects are not a class-wide, reliable signal across statins. That makes a surrogate pass a noisier proxy for a true mortality effect.
- I do not claim this quantifies f. It is a reason not to treat surrogate success as strongly informative about mortality.

*Point 5 (positive correlation between surrogate and mortality effect).*
- Conceded: a positive correlation is plausible, and r_s = 0 is the extreme case.
- But positive correlation does not imply r_s equals 0.10. The question is the magnitude of the gap.
- The critique's own formula at r_s = 0.03 and f = 0.2 gives 0.10 − 0.07 × 0.2 = 0.086, a 14% cut. The 14% cut sits below CG's 25% materiality threshold, but it is nonzero.
- The Advocate has not offered any basis for why r_s would be near 0.10.

*Point 6 (f and r_s unsourced).* I concede this. The critique labels both as assumptions. The residual argument rests on the structure: undefined success, an infeasible mortality trial, and surrogate-only evidence.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

- **Advocate's claim:** the quantifier's central case (r = 0.07, about 2,138x) stays above the 2,000x bar, so bar-crossing depends on pessimistic values.
- **Concession:** this is arithmetically correct, and the bar-crossing claim is weaker than the critique's hypothesis suggests.
- **What remains:**
  - The central case is a 30% reduction in SROI, above CG's 25% materiality threshold, as the Advocate concedes.
  - The low case (r = 0.05) crosses the bar, and the Advocate has not shown that case to be implausible.
  - The Advocate's own break-even is f ≥ 0.345 with r_s = 0. That is not an extreme share if mortality-powered trials are infeasible at this budget.
- **The "p is protected" argument.**
  - Reading 1: the 40% was set against a mortality-relevant success definition.
    - That requires a Phase III of roughly 34,000–47,000 participants (see Points 1–2).
    - Such a trial is not credibly funded by this program.
    - If CG did intend this reading, the 40% is itself questionable, since it would be the probability of completing and winning an infeasible trial.
  - Reading 2: the 40% was set against a looser surrogate-based success definition.
    - The Advocate argues p should then be higher than 40%.
    - That is speculation, and the Advocate admits "I cannot quantify the offset."
    - The Advocate's own decomposition, p_surrogate × r_s + p_mortality × 0.10, has r_s < 0.10 by construction. Whether it beats 0.4 × 0.10 depends entirely on an unestimated p_surrogate.
  - Neither reading supplies a quantified offset. An unquantified possible offset does not cancel a quantified mechanism, though it does prevent me from claiming the full 30%.

**RESPONSE TO "OFFSETTING FACTORS":**

1. **Unvalued channels (morbidity, lung damage, transmission, diagnostics).**
   - They are not in the model, so they cannot offset a model parameter.
   - The Advocate gives no magnitude for them.
   - Lung-damage benefit seen on chest X-ray is also a surrogate-type endpoint. The verifier's evidence does not establish that it maps to the long-term outcomes it would be credited for.
2. **Sweat diagnostic workstream.** The parameter map itself says it is unclear whether this sits inside the $7M, so its offset is not established.
3. **Looser success implies higher p.** Covered above. It is hypothetical and unquantified.
4. **"10% is modest, so a clear surrogate success could deliver it."**
   - This is a conditional possibility with no cited evidence.
   - The verifier's package contains no statin mortality data.
   - I cannot ground a counter-estimate either, and I treat any value for the true r_s as an uninformed prior.

**KEY UNRESOLVED QUESTIONS:**
- What did CG mean by "Phase III success" when it set 40% for Phase II and III combined? A mortality result, a surrogate result, or a regulatory or guideline threshold?
- If it meant mortality, what trial design and budget does CG believe delivers that? Even the most favorable enrichment case (8% baseline) needs about 34,000 participants.
- What is the relationship between statin effects on bacterial load, culture conversion, or lung damage and on-treatment mortality? The verifier's package shows the surrogates but no mortality bridge.
- Are p_success and relative_reduction jointly dependent in CG's judgment? The Advocate concedes the independence assumption is unjustified.
- Would unvalued channels such as lung-damage reduction be valued at a level that offsets a 14–30% cut in the mortality channel? No one has estimated this.

### Judge Audit
Surviving strength: moderate
Justification: - **What survives.** The directional core held up. The Challenger closed the enrichment escape with correct arithmetic, and the Advocate conceded the undefined-success problem and the implausibility of a mortality-powered trial.
- **What was cut back.** The Advocate's sound break-even synthesis showed that the critique's headline claim (pushing SROI below 2,000x) depends on pessimistic values of two unsourced parameters acting together. The Challenger conceded this.
- **Why moderate rather than weak or strong.** The remaining quantitative claim, a roughly 30% cut exceeding the 25% materiality threshold, also rests on an unsourced f. Both sides made grounded moves, and the failure modes were mostly secondary. The substantive magnitude question remains open, so neither "weak" nor "strong" fits.
Recommended action: 1. CONCLUDE NOW, at moderate confidence:
   - The critique validly shows that CG's 10% relative mortality reduction is conditioned on an undefined "success" that, in practice, would likely rest at least partly on surrogate endpoints. E[r | success] is therefore probably overstated.
   - The claim that this pushes SROI below 2,000x does not survive. It requires f ≥ 0.35–0.49, and nothing in the evidence anchors f at that level.
   - Report the issue as a material, directionally downward adjustment of uncertain size. Present it as a sensitivity table over f ∈ {0.2, 0.35, 0.5} and r_s ∈ {0, 0.03}, rather than as a point haircut or a threshold breach.

2. SPECIFIC INVESTIGATION (feasible, optional): Two inexpensive steps would move the answer:
   - Ask CG directly what endpoint "Phase III success" refers to when setting the 40% and the 10%. This is one clarifying question.
   - Have the verifier check the largest completed DS-TB treatment trial sizes, to confirm or refute "no TB trial approaches this scale." This is feasible with existing tooling.
Action feasibility: actionable_now
Advocate failures: ["sound_synthesis_noted: The Advocate recomputed the sample size at CG's 6% baseline: 7.84 × 0.1075 / 0.006² ≈ 23,400 per arm, about 47,000 total. The arithmetic is correct and uses the critique's own formula with CG's input. The Challenger rechecked it and conceded.", "sound_synthesis_noted: The Advocate derived the break-even point. SROI = 3,055 × r/0.10, so the 2,000x bar is crossed at r ≈ 0.0655. That implies f ≥ 0.345 when r_s = 0, and f ≥ 0.49 when r_s = 0.03. The Advocate also showed the quantifier's central case (r = 0.07) yields about 2,138x, which is above the bar. Each step is shown and follows. This is the most decision-relevant analysis in the debate.", 'false_definitiveness: In both readings the product is less exposed than the critique\'s one-sided haircut implies," followed immediately by "I cannot quantify the offset.', 'call_to_ignorance: Offsetting factor 4: "A drug effective enough to deliver a clear surrogate success could plausibly deliver a mortality effect of that size." No evidence is offered. Possibility is offered as a counterweight.', 'call_to_ignorance: Offsetting factor 1 asserts that the unvalued channels, "especially reduced lung damage, are the ones most likely to carry value" in surrogate-success worlds. This is offered as an offset with no magnitude. The structural observation that these channels are zero-valued in the model is legitimate. The claim that they offset this particular parameter is speculation.']
Challenger failures: ['sound_synthesis_noted: The Challenger independently recomputed the 8% enrichment case: 7.84 × 0.1404 / 0.008² ≈ 17,200 per arm. This is correct and properly closes the enrichment objection.', 'unsupported_estimate_counter: The f = 0.2 illustration (0.086, a 14% cut) is chosen arbitrarily. It is then carried into the closing questions as a range: "offsets a 14–30% cut in the mortality channel.', 'false_definitiveness: About 47,000 participants is still far beyond what a $7M all-in program can fund" and "Such a trial is not credibly funded by this program.', 'misrepresenting_evidence_status: The Challenger says "Culture-based surrogates are not accepted as predictors of long-term outcome.', 'whataboutism: The Advocate cannot cite any statin evidence on mortality" and "The Advocate has not offered any basis for why r_s would be near 0.10." These shift the burden onto a claim the Advocate never made. The Advocate argued only that r_s > 0, not that r_s ≈ 0.10. The Challenger\'s own case for any particular f or r_s is equally ungrounded, as it concedes.']
Debate resolved: Both sides agree on three points:
- CG never defines "success."
- A mortality-powered Phase III would require roughly 34,000–47,000 participants even under favorable baselines or enrichment, so a "success" is likely to rest at least partly on surrogate endpoints.
- E[r | success] is therefore plausibly below 0.10 in direction.

The debate also established, with sound arithmetic, that the critique's bar-crossing claim fails at the quantifier's central case (about 2,138x). Crossing 2,000x requires f ≥ 0.345 even with r_s = 0.
Debate unresolved: Three questions remain open:
- **Magnitude.** The size of the haircut depends entirely on f and r_s. Both sides concede these are unsourced, and neither side offered a grounded value.
- **CG's 40%.** It is unresolved whether CG's 40% was calibrated against a surrogate or a mortality definition of success, which determines whether a joint p × r adjustment partially offsets the cut.
- **Unvalued channels.** It is unresolved whether zero-valued channels such as lung damage would recover value in surrogate-only worlds. No one quantified them.

--- Critique: A large share of on-treatment deaths is unreachable by a weeks-scale host-directed adjunct, and shorter regimens shrink the headroom further ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: A large share of on-treatment deaths is unreachable by a weeks-scale host-directed adjunct, and shorter regimens shrink the headroom further

EXISTING COVERAGE:
1. CG's 10% is a relative reduction in all-cause mortality among treated drug-susceptible patients, conditional on a positive result (BOTEC step 3). It is a population-level effect, not an effect among "reachable" deaths.
2. The Quantifier's mechanism (r_eff = fraction reachable × 10% among reachable) treats 10% as the within-reachable effect. CG does not say that. If 10% is read as the trial-observable all-cause effect, the unreachable share is already inside it, and there is no double-count to correct.
3. "Success" is a Phase II/III trial result, and the trial measures all-cause mortality in treated patients (per the Phase IIc description). Any success-conditional effect is therefore net of early, HIV-driven and non-TB deaths by construction.
4. The remaining issue is whether 10% is too high as a success-conditional estimate. That is a challenge to the unexplained 10% (which I concede below), not a separate unreachable-deaths adjustment.
5. CG also applies a 40% probability of Phase II and III success, giving an expected relative reduction of 4%. This is a separate discount, but it means the headline is not a naive 10% applied with certainty.

EVIDENCE WEAKNESSES:
1. The Quantifier's own hypothesis labels the 25–35% unreachable figure and the HPMZ headroom claim UNGROUNDED. I treat this arguendo as "unverified," not false. Even so, the critique supplies no source for the size of the haircut. It rests entirely on a plausible direction.
2. The critique's own evidence undercuts its framing. It says early deaths from fulminant septic shock are inflammatory, so "a host-directed drug is not obviously irrelevant." It also says there is no data showing statins reduce early TB mortality. That is absence of evidence in both directions, so it cannot support a specific unreachable fraction.
3. The HPMZ point is conditional reasoning with no cited data. The claims that a 4-month regimen "likely lowers the on-treatment lung-damage burden" and shrinks adjunct benefit are hypotheses. I cannot ground the opposite, but I also cannot ground the critique's version.
4. The critique itself rates strength as "Medium, with direction supported and magnitude unknown."

MAGNITUDE CHALLENGE:
1. Derivation from the Quantifier's sensitivity output: baseline SROI is 3,054.9 at r = 0.10 and is linear in r. The 2,000x bar is therefore reached at r = 0.10 × 2000 / 3054.9 ≈ 0.0655.
2. At the Quantifier's central r = 0.085, SROI ≈ 2,597. That is about 30% above the bar and does not cross it.
3. Only the low end (r = 0.065, i.e. 35% unreachable with a full 10% among the reachable) gives SROI ≈ 1,986. That is about 0.7% below the bar, a trivial miss.
4. A "crossing" therefore needs the pessimistic end of an ungrounded range and a within-reachable effect equal to CG's full 10%. If the within-reachable effect is also lower, the result falls further. But that is a separate, unquantified stacking of assumptions.
5. The central case does move SROI by -15%, which is below the ~25% materiality threshold. Only the low case (-35%) exceeds it, and it rests on the number the critique itself calls ungrounded.

OFFSETTING FACTORS:
1. The parameter map lists channels CG values at zero: morbidity DALYs, post-treatment mortality DALYs, transmission-averted cases and diagnostic value. The BOTEC says "only mortality is valued."
2. The prior trial's signal was on lung damage and clearance (per the BOTEC context). The critique's own mechanism says lung damage is what statins are meant to reduce. If that benefit is real, it plausibly carries into post-treatment survival that the model does not count. That would offset some of the on-treatment headroom loss.
3. I cannot size these offsets from the evidence provided. I flag them only as asymmetric omissions that the critique's downward adjustment leaves uncounted.
4. The HPMZ-induced baseline reduction applies only to patients on that regimen. I cannot ground the share of patients who would be on it at the time of adoption, so the effect on the 6% baseline is unquantified, not zero.

OVERALL ASSESSMENT:
Partial defense.
- Strong points: the unreachable-share adjustment is conceptually folded into a trial-observed all-cause effect, the magnitude is ungrounded, and the central case stays above the bar (~2,600x).
- Weak points: CG never derives the 10%, and it never discusses early deaths or regimen changes. Whether 10% is a sensible success-conditional effect is genuinely open. The critique correctly shows that the headline is fragile to this one parameter.

CONCESSIONS:
1. The direction is valid: all-cause on-treatment mortality includes deaths a weeks-scale adjunct plausibly cannot reach, and CG gives no reasoning on this.
2. The 10% has no stated derivation from the prior trial's surrogate results, so I cannot rule out that it is optimistic.
3. A shorter regimen such as 4-month HPMZ could lower the 6% baseline. CG does not consider this, and it would reduce absolute benefit.
4. The low-end case sits at the bar, so the estimate has little margin if the haircut is at the pessimistic end.
```

### Challenger
REBUTTAL: A large share of on-treatment deaths is unreachable by a weeks-scale host-directed adjunct, and shorter regimens shrink the headroom further

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: CG's 10% is a success-conditional, population-level all-cause effect. The unreachable share is therefore already inside it by construction, so there is no double-count to correct.

1. **The critique is not a double-count claim.** I concede that if 10% were a realized trial effect, it would already be net of unreachable deaths. But 10% is not a realized effect. It is CG's assumption about what a successful trial would show. "Net of unreachable deaths by construction" holds for the observed number, not for the assumed one.
2. **Reachability is a sanity check on the assumed 10%.** The reachable/unreachable decomposition asks whether 10% is a plausible all-cause effect given what share of deaths a weeks-scale drug could plausibly influence. The Advocate concedes at point 4 that this is open ("whether 10% is too high as a success-conditional estimate"). Calling it "a challenge to the unexplained 10%, not a separate adjustment" relabels the critique rather than answering it.
3. **The Advocate's own account of the evidence base makes this worse.** They say the prior signal was on lung damage and clearance, which are surrogates. Translating a surrogate signal into an all-cause mortality effect is where reachability matters most. Nothing in the defense shows that translation was done.
4. **The 40% success probability does not guard against an inflated effect size.** It discounts the chance of a positive result. It says nothing about how large the effect is given a positive result. Effect sizes conditional on statistical significance tend to be overestimated when trials are modestly powered (Gelman & Carlin 2014, Type M error). I cannot say whether the Phase IIc/III design is underpowered, so this is a conditional concern, not an established one.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the 25–35% figure and the HPMZ claim are ungrounded, the verifier evidence cuts both ways on early deaths, and the critique rates its own magnitude as unknown.

1. **Conceded:** the 25–35% haircut has no source. The verifier evidence does not support a specific unreachable fraction. I am not defending that number as a point estimate.
2. **The evidence does not cut equally both ways for the model.** The inflammatory-septic-shock point weakens the "unreachable" framing for some early deaths. The verifier also found no data that statins reduce early TB mortality. Together they leave the reachable fraction undetermined.
3. **Neither item has been REJECTED.** Both are verifier observations, not refutations. Absence of data on early-death effects is not evidence the effect is zero, and it is not evidence the effect is 10%. A parameter the model treats as a point estimate needs a derivation, and the Advocate concedes none exists.
4. **HPMZ is conditional reasoning, and the Advocate concedes the same about the offsets.** I agree it is unquantified. The direction is not in dispute: the Advocate concedes at Concession 3 that a shorter regimen could lower the 6% baseline and reduce absolute benefit.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: the bar is crossed only at r ≈ 0.0655. The central case (~2,597) clears it by ~30%. Only the 35% haircut with a full 10% among the reachable barely misses (~1,986, 0.7% below).

1. **Arithmetic conceded.** From the sensitivity output, 0.10 × 2000 / 3054.857 = 0.0655. The central case sits ~30% above the bar.
2. **The margin is the right frame, and it is thin.** The bar is crossed at 65.5% of CG's assumed r, so any combined haircut above ~34.5% crosses. The Advocate concedes CG gives no derivation for the 10%. A true success-conditional effect below ~6.5% therefore crosses the bar. I cannot ground whether that is likely, but the margin is narrow relative to the uncertainty the Advocate concedes.
3. **The sensitivity run varies only one of the channels.** It holds the within-reachable effect at 10% and leaves baseline mortality at 6%. The Advocate calls stacking "a separate, unquantified" assumption. It is a conditional, not a hidden one, because SROI is linear in both. Here is the derivation from the Advocate's own numbers:
   - At the central r = 0.085, SROI ≈ 2,597.
   - Reaching the bar needs a further multiplicative factor of 2000/2597 ≈ 0.77.
   - That corresponds to roughly a 23% haircut from either a weaker within-reachable effect or a lower HPMZ baseline.
   - If the baseline is lower by x% and the effect is unchanged, SROI scales by (1 − x). I cannot ground x.
4. **The Advocate's "trivial miss" at the low end is correct as arithmetic.** But any additional haircut at that end, however small, pushes it further below. So the low end is not a knife-edge in a protective direction.
5. **Materiality threshold versus bar.** The Advocate notes that −15% is below the ~25% threshold. The question the pipeline asks is bar-crossing, and the Quantifier's own output flags `crosses_bar_low: true`. The central case does not cross, which I concede.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: unvalued channels (post-treatment survival, morbidity, transmission) may offset the loss, and the HPMZ baseline effect applies only to a share of patients.

1. **The offsets are unquantified, as the Advocate admits.** "I cannot size these offsets" means they cannot be netted against a haircut. They show that the model omits some benefits, not that the on-treatment mortality parameter is right.
2. **The offset depends on the same channel HPMZ weakens.** The Advocate argues that a lung-damage benefit may carry into post-treatment survival. But the critique's mechanism says a shorter regimen likely reduces on-treatment lung-damage burden, which is the very thing statins are meant to address. If that holds, the post-treatment offset shrinks along with the on-treatment benefit. They are correlated, not independent.
3. **A lung-damage benefit does not imply a 10% reduction in on-treatment deaths.** If the benefit runs through lung damage, it may be real without producing an on-treatment mortality effect of the assumed size. The offset therefore does not rescue the 10% parameter itself.
4. **Conceded:** the HPMZ baseline effect applies only to patients on that regimen, and I cannot ground the share. So the effect is unquantified, not zero, as the Advocate says.

**KEY UNRESOLVED QUESTIONS:**
- What is the basis for 10% as an all-cause success-conditional effect, given the prior signal was on surrogates (lung damage, clearance)? Is it a trial-powered target or a surrogate extrapolation?
- Does "success" in CG's 40% require an effect of ~10%, or any significant effect? If the latter, the conditional expected effect could be lower than 10%.
- What share of the 6% baseline mortality is early (e.g. within the first weeks), and does any evidence show a statin effect on that segment? The verifier found none.
- What share of adopting patients would be on a 4-month regimen such as HPMZ, and by how much would that lower baseline mortality?
- Is the post-treatment lung-damage offset independent of the HPMZ shortening, or do both shrink together?

### Judge Audit
Surviving strength: moderate
Justification: - **What the Challenger landed:** It dismantled the Advocate's main conceptual defense, the assumed-versus-realized distinction. It also showed the 40% success probability does not guard against an inflated conditional effect size.
- **What the Advocate landed:** Its grounded arithmetic showed that the critique's own central case stays ~30% above the bar. Crossing requires the pessimistic end of a range both sides concede is unsourced.
- **Why moderate:** Both sides used sound syntheses and few failure modes. The direction is supported by verifier data (early-death clustering, comorbidity, HIV), but the magnitude needed to cross the bar was not established.
Recommended action: 1. CONCLUDE NOW: Retain the critique as a directional flag that CG's 10% success-conditional all-cause effect is underived and likely optimistic, because a meaningful share of on-treatment deaths is early, HIV-driven or non-TB. Drop the 25–35% unreachable figure and the HPMZ headroom claim as quantitative inputs.
   - State the decision-relevant threshold explicitly: the estimate falls below 2,000x only if the effective conditional effect is below ~6.5%, a combined ~35% haircut from 10%.
   - The debate does not show that this threshold is likely to be crossed (moderate confidence).
   - A feasible follow-up is to ask whether CG's 10% is the trial's powered minimum detectable effect or a surrogate extrapolation. This is a single document check with CG, and if 10% is a powered target the Type M concern sharpens.
Action feasibility: actionable_now
Advocate failures: ['sound_synthesis_noted: The Advocate derived the bar-crossing threshold from the sensitivity output: r = 0.10 × 2000 / 3054.9 ≈ 0.0655. They computed central-case SROI ≈ 2,597 at r = 0.085 and low-case ≈ 1,986. Each step is shown and grounded in model output. The Challenger accepted the arithmetic.', 'strawmanning: Existing Coverage points 2–3 recast the critique as a double-count claim: "the unreachable share is already inside it, and there is no double-count to correct." The critique argued that an assumed 10% all-cause effect is implausibly high given the reachable pool. It did not argue that a realized effect was double-counted. "Net of unreachable deaths by construction" holds only for an observed trial effect, not for CG\'s assumed one. The Challenger correctly exposed this. The Advocate\'s own point 4 partly concedes the reframing.', 'strawmanning: Existing Coverage point 5 offers the 40% success probability as context against a "naive 10% applied with certainty." The critique never claimed certainty. The success probability is orthogonal to effect size conditional on success, so it does not address the critique.', 'call_to_ignorance: Offsetting Factors point 2 says a lung-damage benefit "plausibly carries into post-treatment survival that the model does not count. That would offset some of the on-treatment headroom loss." No evidence is cited for post-treatment survival effects. This is mitigated by the explicit admission "I cannot size these offsets," but the point is still used rhetorically as a counterweight.']
Challenger failures: ['sound_synthesis_noted: The Challenger built on the Advocate\'s numbers: 2000/2597 ≈ 0.77, so a further ~23% multiplicative haircut from either channel crosses the bar. They noted correctly that SROI is linear in both effect and baseline. This is grounded and transparent, and is properly framed as conditional ("I cannot ground x").', 'sound_synthesis_noted: The Type M error point cites Gelman & Carlin 2014. It is explicitly flagged as "a conditional concern, not an established one." It is a legitimate rebuttal to the Advocate\'s use of the 40% success probability.', 'false_definitiveness: Magnitude point 4 says the low end "is not a knife-edge in a protective direction... any additional haircut, however small, pushes it further below." This treats only downward adjustments as live. It ignores the possibility, raised by the verifier, that some early inflammatory deaths are reachable, which would push upward. The point is minor.', 'false_definitiveness: Magnitude point 2 says "the margin is narrow relative to the uncertainty." This is delivered after conceding "I cannot ground whether that is likely." A ~34.5% combined haircut is a meaningful margin unless there is evidence the haircut is that large, and none was offered. The point is mild, and is offset by honest hedging elsewhere.']
Debate resolved: The debate established three things:
- **Bar-crossing threshold:** The bar is crossed only if the effective success-conditional all-cause effect falls below ~6.5%, i.e. a combined haircut above ~34.5% from CG's 10%. The critique's central case (r = 0.085, SROI ≈ 2,600) does not cross.
- **The "already inside the trial effect" defense fails:** It fails because CG's 10% is an assumption, not a realized trial result.
- **Direction of bias:** Both sides agree the 10% is underived and that reachability and shorter regimens plausibly bias it downward.
Debate unresolved: The size of the unreachable fraction remains open, specifically whether early inflammatory deaths are reachable by a host-directed adjunct. Also open is whether CG's 10% is a trial-powered target or a surrogate extrapolation. Neither side could ground the HPMZ uptake share, the baseline reduction, or the post-treatment offsets.

--- Critique: Rifampicin induction structurally limits atorvastatin exposure in routine programs, and the trial exposure does not transfer ---

### Advocate
DEFENSE OF GIVEWELL'S (CG's) POSITION: Rifampicin induction limits atorvastatin exposure, and trial exposure does not transfer

**EXISTING COVERAGE:**

1. **The 10% is conditional on a positive result, and success is already discounted.**
   - The BOTEC applies r = 10% only if Phase II and Phase III succeed, and it multiplies the result by 40%.
   - Conditional on success, the Phase III will have shown benefit at whatever dose and timing was tested, with rifampicin-containing background therapy. That is the standard first-line regimen that all adult drug-susceptible patients receive.
   - Any exposure-limiting rifampicin effect therefore lowers the probability of reaching "success." It does not mechanically lower r given success. That channel sits in p_success, which is already 0.4 and not 1.0.
   - The critique's own "Remove" list concedes that the atorvastatin signal comes from atorvastatin itself. The prior positive data therefore came from the drug whose exposure is in question, not from a different statin.

2. **The grant funds the dosing question.**
   - The Phase IIc tests "dosing strategies for survival, infection clearance and lung damage" (CG text).
   - Testing dosing strategies is the standard way to find a regimen that overcomes an exposure problem. If rifampicin induction lowers exposure, the trial is designed to detect it and to find a dose or timing that compensates.
   - The parameter map says CG does not consider rifampicin-induced reduction in statin exposure. That is true by name. But the trial design is a structural response to unresolved dose-exposure questions.

3. **The dosing-time asymmetry favors routine programs.**
   - On the Verifier's evidence, co-administered dosing gives a modest AUC rise. Only separated dosing (the 80% fall) is harmful.
   - TB drugs are taken together once daily, often as fixed-dose combinations under direct observation. Co-administration is the natural default.
   - The 80% scenario therefore requires patients or clinics to deviate from the simplest regimen. It is not the structural default in routine programs.

**EVIDENCE WEAKNESSES:**

1. **The magnitude has no empirical basis.** The critique says so itself: the 0.5–0.8 multiplier is "my guess, not derived from data." The steep dose-response assumption and the applicability to rifapentine-based HPMZ are flagged UNGROUNDED. The Verifier rated the strength medium, not large.

2. **The "steep dose-response" is an assumption, not a finding.**
   - Halving exposure could cut the effect by more than half (the critique's "(unknown)").
   - It could equally cut it by less. Many host-directed adjuncts show plateauing or threshold dose-response.
   - The critique offers no evidence for either direction. A symmetric uncertainty is not grounds for a directional downward revision.

3. **The preclinical THP-1 evidence addresses a different parameter.**
   - The finding is that atorvastatin did not inhibit Mtb growth at non-toxic doses in THP-1 cells, whereas simvastatin, fluvastatin and pravastatin did.
   - This is an in vitro, single-cell-line result. It says nothing about human immunomodulatory or lung-lesion effects, which is where a statin adjunct plausibly works.
   - It is evidence on whether atorvastatin works at all (mechanism-limited). That is a p_success question, already discounted to 40%, not an r-conditional-on-success question.
   - Applying it to r would double count against the 40%.
   - The human Phase IIa/b signal on atorvastatin itself is more directly relevant than a cell-line growth assay.

4. **The ART and rifapentine concerns are unquantified.** The critique identifies plausible interactions but gives no data on how much they change statin exposure.

5. **The concern about "chronic co-administered exposure" is not evidence of a problem.** "Unknown" cuts both ways.

**MAGNITUDE CHALLENGE:**

1. **The Quantifier's own central case stays above the bar.**
   - A multiplier of 0.85 on r gives r = 0.085 and SROI ≈ 2,597x (-15%).
   - This is below the 25% "decision-relevant" change threshold and above the ~2,000x bar.

2. **Only the aggressive end crosses the bar.**
   - SROI is linear in r. The break-even multiplier is 2,000 / 3,054.9 ≈ 0.655, so r must fall below about 6.5% to cross the bar.
   - The critique's 0.5–0.8 range straddles this. Only about the lower half of the range (0.5–0.655) crosses.
   - That lower half corresponds to the "steep dose-response" assumption, which is itself ungrounded.
   - A multiplier of 0.5 (SROI ≈ 1,527x) requires halving effective exposure and a proportional effect loss.
   - On the 40% probability of success, such a scenario is more plausibly a failed-trial state, already counted in the 60% failure mass.

3. **The multiplier should not be applied to a conditional-on-success r.**
   - Applying it assumes the positive trial result was achieved at higher exposure than routine programs deliver. That is only true if routine practice systematically departs from the trial dosing protocol.
   - The residual real-world effect is therefore adherence drift from the validated regimen, not the full rifampicin interaction.
   - This is smaller than the 0.5–0.8 range implies. I cannot quantify it and treat it as an uninformed prior.

**OFFSETTING FACTORS:**

1. **Unvalued benefits.** The BOTEC counts only on-treatment mortality (parameter map: "only mortality is valued"). Lung-damage reduction, long-term post-treatment survival, transmission and the sweat diagnostic are implicit zeros. The parameter map says these "could make the estimate robust even if Thread 1 finds a small on-treatment mortality effect."

2. **Dose escalation.** Atorvastatin is generic and has a wide dose range. A rifampicin-induced exposure loss can in principle be offset by dosing, which the Phase IIc is explicitly testing. This is a mechanism-based argument, not empirically verified for this indication.

3. **The Verifier's co-administration finding.** Co-administered dosing gives a modest AUC rise, which runs against the critique's direction in the default scenario.

4. **The 10% could be conservative.** It is not derived from the prior trial's surrogate effects, so the uncertainty is two-sided. A downward adjustment from one mechanism without examining upward possibilities is partial.

**OVERALL ASSESSMENT:** **Partial defense.**
- The conceptual defense is strong: the interaction is mostly a p_success issue, not an r-given-success issue, and the trial is designed around dosing.
- The Quantifier's central case (-15%, ~2,600x) stays above the bar, and the magnitude is ungrounded.
- The defense is not "Strong" because CG's text does not explicitly state that the trial is run on rifampicin background with a regimen intended for routine use. My argument depends on that being so, which is standard for first-line TB care but not verified here.
- The parameter map also confirms CG does not explicitly consider the interaction.

**CONCESSIONS:**

1. CG does not name or address the rifampicin interaction. The Phase IIc dosing design implicitly addresses it, but the BOTEC contains no explicit reasoning.
2. The separated-dosing 80% AUC fall is real. If real-world programs deviate from co-administration, the effect on r could be larger than I assume.
3. Chronic exposure, rifapentine-based HPMZ and ART interactions are unresolved. If the 4-month regimen has stronger induction, the issue is not captured by the trial-conditional argument unless Phase III uses that regimen.
4. If the true multiplier is in the lower half of the critique's range (below ~0.65), SROI falls below the 2,000x bar. I cannot rule this out, only note that nothing grounds it.
5. The in vitro finding that atorvastatin is the weakest statin in THP-1 cells is a legitimate reason to doubt the 40%, but it belongs to p_success, not r.

### Challenger
REBUTTAL: Rifampicin induction structurally limits atorvastatin exposure in routine programs

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: Exposure limitation lowers the probability of reaching "success" (p_success = 0.4), not the effect size given success (r = 10%), because a successful Phase III will have been run on rifampicin-containing background therapy.

Response:
- **Concession.** If Phase III runs on rifampicin background with co-administration, and routine programs replicate that, then the interaction mostly affects whether the trial succeeds. This is the Advocate's strongest point, and it shrinks the residual critique to the cases where routine practice departs from trial conditions.
- **The 0.4 was never sized with this risk.** The Advocate concedes CG does not name or consider the interaction. A discount is "already there" only if it was sized with the risk in mind. Nothing shows the 40% priced in rifampicin induction, atorvastatin-specific weakness, or the ART and rifapentine issues.
- **Moving the channel does not remove the impact.** SROI is linear in both p_success and r. If the interaction belongs in p_success and the 40% omitted it, the product is still overstated by the same proportion. The Advocate relocates the channel but does not show the 0.4 is adequate.
- **The "r is conditional on a validated trial" argument is in tension with the Advocate's own position.**
  - The Advocate argues r|success is anchored to a trial result achieved under rifampicin.
  - But the Advocate also says the 10% "is not derived from the prior trial's surrogate effects."
  - If r is not calibrated to any trial effect, nothing ties it to trial-realized exposure. The conditional-on-success framing then protects a number that was never linked to the trial's exposure.
- **"The grant funds the dosing question" is not evidence the question is resolved.**
  - Phase IIc testing dosing strategies shows the sponsor recognizes dose uncertainty.
  - It does not show that a dosing solution exists that is feasible in routine programs.
  - Any escalated dose must also be tolerated alongside ART and a rifapentine-based regimen. Nothing in the record addresses this.
- **The co-administration default is stated, not shown, to hold in routine programs.**
  - The statin would be an add-on pill, not part of a TB fixed-dose combination. I cannot ground how timing would be handled in practice.
  - The Verifier found the separated-dosing 80% AUC fall is real. The Advocate concedes it.
- **The "modest AUC rise" under co-administration is not established as a chronic effect.**
  - The critique's Keep list says chronic co-administered exposure is unknown. The Verifier's evidence package does not say the modest rise was measured under daily dosing.
  - The pharmacology I know has single-dose rifampicin inhibiting hepatic uptake transporters (OATP1B1), while chronic dosing induces CYP3A4. I cannot cite a specific study from the evidence package for this, so treat it as background pharmacology.
  - If the rise is an acute effect, it is the wrong evidence for steady-state routine use. The Advocate uses it as an offset.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: The multiplier and dose-response steepness are ungrounded, and symmetric uncertainty does not justify a directional revision.

Response:
- **Concession.** The 0.5–0.8 multiplier is a guess, and the critique says so. The steepness of the dose-response is unknown, and it could plateau instead.
- **The critique is a stress test, not a point estimate.** The Verifier's finding is that the direction is plausible and the magnitude is empirically unsupported. That supports a sensitivity flag, not a claim that the multiplier is 0.5.
- **Unknown does cut both ways, but only for the dose-response shape.** The direction of the exposure change under chronic rifampicin is not symmetric. The Verifier's evidence shows the separated-dosing effect is a large fall (~80% AUC).

> The Advocate claims: The THP-1 result bears on p_success (mechanism-limited), not r, and applying it to r would double-count.

Response:
- **Concession.** The Verifier's wording is that the THP-1 result raises doubt that the effect is exposure-limited rather than mechanism-limited. That cuts against the exposure thesis, so it should not be used to support the rifampicin critique. The Advocate is right on this.
- **The Advocate concedes the finding is a legitimate reason to doubt the 40%.** "Already discounted" is not demonstrated for this specific evidence, as above.
- **"The human Phase IIa/b signal is more directly relevant" cannot be checked.** Nothing in the evidence package describes that signal's size or its background regimen.

> The Advocate claims: ART, rifapentine and chronic-exposure concerns are unquantified.

Response:
- **This is correct, and it is the substance of the residual risk.** These are UNVERIFIABLE, not REJECTED, and the Advocate cannot treat them as null.
- **The conditional argument.** If the 4-month HPMZ regimen induces CYP3A4 at least as strongly as rifampicin, and Phase III background differs from routine background, then the trial-conditional defense weakens. The Advocate concedes this in Concession 3.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: The central case (×0.85, SROI ≈ 2,597x, −15%) stays above the ~2,000x bar, and only the lower half of the 0.5–0.8 range crosses it.

Response:
- **The arithmetic is right.** The break-even multiplier is 2,000 / 3,054.9 ≈ 0.655, and ×0.85 gives 2,596.6.
- **The margin is thin once other discounts stack.** This is arithmetic, not an estimate of the actual discounts.
  - A −15% central case leaves 53% headroom above the bar (3,055 vs 2,000).
  - Two independent factors of 0.85 compound to 0.72, and three of 0.87 to about 0.66, which is at the break-even.
  - The critique's own list names several candidate discounts: ART interactions, rifapentine induction, chronic exposure and dosing adherence.
  - I cannot ground that these are independent or of that size. I am only showing that the central case does not need much extra to approach the bar.
- **"0.5 is a failed-trial state" holds only for trial-matched exposure.** The scenario the critique cares about is a trial that passes at one exposure and routine delivery that falls below it. The Advocate concedes this scenario is possible and cannot rule out ×<0.65.
- **Concession.** The Advocate's point that the residual real-world effect is adherence drift, not the full interaction, is reasonable. The residual is smaller than ×0.5–0.8 implies if trial and routine regimens match.
- **Minimum defensible impact.** With matched regimens and co-administration, the impact is near zero on r and sits in p_success. With mismatch, I cannot ground a number. The −15% central case is the Quantifier's, not derived from data.

**RESPONSE TO "OFFSETTING FACTORS":**

- **Unvalued benefits (lung damage, long-term survival, transmission).**
  - These are not in the model, so they do not offset the overstated modeled channel.
  - They are also plausibly driven by the same statin exposure. If exposure is limited, they are likely reduced too, so they are correlated with the downside, not independent offsets.
- **Dose escalation.**
  - The Advocate says this is mechanism-based and "not empirically verified for this indication."
  - It is not in the model.
  - Tolerability at escalated doses alongside ART and rifapentine is unaddressed.
- **Co-administration AUC rise.**
  - This is real in the Verifier's evidence for the co-administered case.
  - Its relevance to chronic steady-state exposure is the open question above, so I do not treat it as an established offset.
- **"The 10% could be conservative."**
  - The Advocate offers no evidence for an upward direction. Two-sided uncertainty on an ungrounded parameter does not cancel a specific identified downward mechanism.
  - If r is symmetric around 10%, the expected-value effect of a plausible downward channel is still downward.

**KEY UNRESOLVED QUESTIONS:**
- What background regimen (rifampicin or rifapentine-based HPMZ, with or without ART) will Phase IIc and Phase III use? Does it match the regimen the BOTEC assumes for routine delivery?
- Was the 10% anchored to any trial-realized effect? If not, the "conditional on success" defense does not protect it.
- Did the 40% p_success incorporate atorvastatin-specific weakness (THP-1) or induction risk? CG does not appear to have considered the interaction.
- What is steady-state atorvastatin exposure under chronic daily rifampicin and rifapentine, co-administered and separated? Is the "modest AUC rise" an acute single-dose result?
- Is exposure-limitation a feature of the statin effect at all, or is the effect mechanism-limited? The Verifier's evidence leans toward the latter, which would shift the whole issue to p_success.

### Judge Audit
Surviving strength: weak
Justification: - The Challenger conceded the Advocate's central structural argument: under matched regimens the effect sits in p_success, not r.
- The Challenger also conceded that the magnitude is ungrounded and that the THP-1 evidence cuts against the exposure mechanism. That leaves the critique's quantitative claim with no support.
- The Challenger's best surviving point is that the 0.4 was not demonstrably sized for this risk, and that relocating the channel does not zero it out. This is valid but unquantified.
- The Challenger's attempts to show proximity to the bar relied on invented compounding factors and a separated-versus-chronic category swap.
- The Challenger also misstated the evidence package on the Phase IIA background regimen. That trial was in fact run under rifampicin, which directly supports the Advocate's trial-conditional framing.
Recommended action: 1. CONCLUDE NOW: Do not apply the critique's 0.5–0.8 multiplier to r. This conclusion is held with moderate-to-high confidence.
   - The debate established that, under regimen-matched co-administration, the rifampicin interaction is a p_success consideration.
   - The positive atorvastatin signal was obtained under rifampicin-based therapy.
   - Record the issue as a qualitative sensitivity flag on p_success rather than an adjustment to r.
   - The flag should note that CG's 0.4 was set without explicit consideration of drug interactions or atorvastatin's weak in vitro profile.
   - One low-cost check could reopen the question: whether the Phase IIc/III protocol specifies (a) a rifapentine-based or rifampicin-based background, and (b) timing relative to the TB regimen. This can be done by reading the registered trial protocol.
   - Only a documented mismatch between trial and routine regimen would justify a residual adjustment to r, and even then its magnitude would need a PK/PD basis that does not currently exist.
Action feasibility: actionable_now
Advocate failures: ['sound_synthesis_noted: Break-even arithmetic: "SROI is linear in r. The break-even multiplier is 2,000 / 3,054.9 ≈ 0.655." The derivation is transparent and the Challenger confirmed it. It correctly shows that only the lower part of the critique\'s own 0.5–0.8 range crosses the bar.', "sound_synthesis_noted: Reallocating the interaction from r to p_success. The argument runs: conditional on a positive Phase III on rifampicin background, the exposure penalty is already embedded in the observed effect. The Challenger conceded this as the Advocate's strongest point.", 'unsupported_estimate_pseudo: On the 40% probability of success, such a scenario is more plausibly a failed-trial state, already counted in the 60% failure mass.', 'misrepresenting_evidence_status: The Advocate treats "co-administered dosing gives a modest AUC rise" as an established offset ("runs against the critique\'s direction in the default scenario"). The Verifier explicitly marked net steady-state exposure under chronic rifampicin as VERIFIED as uncertain. The Verifier also noted that prolonged co-administration has never been investigated. The Advocate turns an acute or uncharacterized finding into a chronic-use offset.', 'call_to_ignorance: The 10% could be conservative... the uncertainty is two-sided." No evidence is offered for upward movement. Ignorance is used to neutralize an identified downward mechanism.', 'unsupported_estimate_counter: Many host-directed adjuncts show plateauing or threshold dose-response.']
Challenger failures: ["misrepresenting_evidence_status: The human Phase IIa/b signal is more directly relevant' cannot be checked. Nothing in the evidence package describes that signal's size or its background regimen.", 'strawmanning: Category swap between chronic co-administered and separated dosing.', 'unsupported_estimate_fabricated: Two independent factors of 0.85 compound to 0.72, and three of 0.87 to about 0.66.', 'call_to_ignorance: If the 4-month HPMZ regimen induces CYP3A4 at least as strongly as rifampicin...', 'sound_synthesis_noted: SROI is linear in both p_success and r. If the interaction belongs in p_success and the 40% omitted it, the product is still overstated by the same proportion.']
Debate resolved: Several points were agreed by both sides:
- The transferability limb is dead. The positive human signal is atorvastatin's own.
- The 0.5–0.8 multiplier on r has no empirical basis.
- The break-even multiplier is ≈0.655.
- If the trial and routine regimens match and co-administration holds, the rifampicin interaction belongs in p_success rather than in r-given-success.
- The THP-1 evidence points toward a mechanism limit rather than an exposure limit, which undercuts rather than supports the critique's thesis.
Debate unresolved: Three questions remain contested:
- Whether CG's 0.4 p_success adequately prices induction, atorvastatin-specific weakness, and ART interactions, given that CG never named them.
- Whether routine delivery of an add-on statin will replicate trial dosing timing.
- Whether the Phase III background regimen (rifampicin versus rifapentine-based HPMZ, with or without ART) will match routine practice. This determines whether any residual effect on r exists.

--- Critique: Winner's-curse and reference-class patterns imply the conditional effect should sit well below the surrogate-implied one, and r and p_success should not be independent ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION: Winner's-curse and reference-class shrinkage of the conditional effect (r), and r–p_success dependence

**EXISTING COVERAGE:**
- **The 10% is already conditional on success.** CG applies it only "if positive," then multiplies by a 40% probability that Phase II and III both succeed. The expected relative reduction is therefore 4%. Null and surrogate-only worlds are meant to sit inside the 60% failure mass.
- **The critique's mixture structure is close to CG's structure.** Suppose p_success means "a mortality-relevant Phase III result is positive," and r is the effect conditional on that. Then the null world contributes r = 0 with probability 0.6, and E[r × p] = 0.04 with no gap between E[r × p] and E[r] × E[p].
- **A gap needs a specific definition of success.** E[r × p] falls below the product of means only if "success" can occur in worlds where the true mortality effect is zero. That happens if success is defined on a surrogate such as culture conversion or X-ray. The critique itself says the sign of the covariance "depends on how p_success is defined." CG's wording ("Phase II and Phase III both succeed," applied to a mortality benefit) does not obviously take that definition. This is an ambiguity in CG's text. It is not a demonstrated bias.
- **Winner's curse applies to the observed estimate, not the realized effect.** A selected Phase III estimate will overstate the true effect. But the lives saved depend on the true effect. So the relevant question is the true effect conditional on a positive confirmatory trial. That is a prior-shrinkage question, not a winner's-curse question. The critique's own 0.7–0.9 factor is explicitly "UNGROUNDED."
- **CG's 10% is not extrapolated from the atorvastatin surrogate signal.** The parameter map confirms there is "no stated derivation." The critique's framing, that the conditional effect should sit "below the surrogate-implied one," presumes a surrogate-implied number that CG never computed. The 10% is a round-number assumption, so shrinking it from a nonexistent anchor is not clearly warranted.

**EVIDENCE WEAKNESSES:**
- **The reference class is mostly different drugs with different mechanisms.** Vitamin D, metformin, CC-11050 and everolimus are host-directed agents. The critique itself concedes they "were never tested on mortality," so they cannot show that surrogate signals fail to translate to mortality. They show only that surrogate signals were inconsistent. I accept that this is a legitimate reference class for "how often do host-directed TB adjuncts show a clean surrogate benefit," but not for the size of a mortality effect.
- **The rosuvastatin result is better read as inconclusive than null.**
  - The reported figures are median time to conversion of 42 days in both arms and HR 1.30 (95% CI 0.88–1.91, p=0.19).
  - If HR > 1 favors faster conversion on rosuvastatin, which is the usual convention but which I cannot confirm from the evidence package, the point estimate is in the beneficial direction.
  - The interval is wide, spans roughly a 12% worse to 91% better hazard, and includes meaningful benefit.
  - The authors' conclusion of "no substantive benefit overall" is a statement about power.
  - The critique itself notes that rosuvastatin is not atorvastatin.
- **The atorvastatin Nigeria Phase II result is the grant's premise, not counter-evidence.** The critique calls it "the strongest on-point support." But its being a surrogate-only signal is exactly why CG funds a Phase IIc and a Phase III and applies a 40% probability. The evidence confirms that the effect is unproven. It does not show that the 40% is too generous.
- **The cited pattern supports a lower p_success better than a lower r.** Failed surrogate-to-surrogate translation is mainly evidence about the probability of a positive trial. Applying it again to r risks double-counting the same failure information, once in the 40% and again in a shrinkage factor.

**MAGNITUDE CHALLENGE:**
- **The critique's own range does not cross the bar.** The sensitivity baseline is 3,055x, and SROI scales linearly in r.
  - r = 0.09 gives about 2,750x (−10%).
  - r = 0.08, the Quantifier's central value, gives 2,444x (−20%).
  - r = 0.07 gives about 2,138x (−30%).
  - All three stay above the ~2,000x bar. The central case is also under the ~25% change threshold.
- **Only the −50% case crosses the bar.** That corresponds to r = 0.05, which lies outside the critique's own stated 0.07–0.09 shrinkage range. It has no derivation in the critique and requires roughly a 50% shrinkage that nothing in the evidence package supports.
- **The 0.7–0.9 factor is explicitly labeled illustrative.** The critique offers no chain from the reference class to that number. I cannot supply a better grounded estimate either, so the defensible reading is that the direction is plausibly downward and the size is uninformed.

**OFFSETTING FACTORS:**
- **CG values only on-treatment mortality.** The formula notes "only mortality is valued." Several benefit channels are implicit zeros:
  - morbidity DALYs, including the lung-damage endpoint the trial targets;
  - post-treatment mortality;
  - transmission averted;
  - diagnostic value.
  If r shrinks because mortality benefit is smaller, a drug that works on lung damage could still deliver value that the model does not count. The parameter map flags this as potentially making the estimate "robust even if Thread 1 finds a small on-treatment mortality effect."
- **Baseline mortality may be understated.** The map notes that notified-cohort mortality can miss unascertained deaths, which would partly offset a lower r.
- **The offset is not guaranteed.** The model also has no time discounting, which biases the other way. I'm not arguing that the offsets net to zero, only that the critique considers one direction of adjustment.

**OVERALL ASSESSMENT: Partial defense.**
- The downward pressure on r is plausible, and CG gives no derivation for the 10%.
- The critique is overstated in three ways:
  - Its reference class mostly concerns surrogate outcomes, not mortality.
  - Part of its content duplicates information already priced into the 40%.
  - Its own parameter range leaves SROI above 2,000x, at roughly 2,140–2,750x.
- The covariance point is only a problem if "success" is defined on a surrogate, which is an ambiguity in CG's text, not a demonstrated error.

**CONCESSIONS:**
- **No derivation of 10%.** CG offers none, so I cannot show that 10% is the right central value rather than a placeholder.
- **Atorvastatin evidence is surrogate-only.** It rests on a Phase II bacteriological signal and no mortality data, so a conditional effect below 10% is a reasonable prior.
- **"Success" is undefined.** If it can mean a surrogate win, the r–p_success independence assumption could overstate E[r × p]. CG should define it.
- **Direction is probably downward.** The expected effect is a modest reduction (about −10% to −30%), not an increase, though I cannot ground the magnitude.
- **Margin is thin at the low end.** At r = 0.07, SROI is about 2,140x, only about 7% above the bar. Any other downward adjustment from other critiques, such as uptake or Phase III cost, could then combine with this one to cross it.

### Challenger
REBUTTAL: Winner's-curse and reference-class shrinkage of r, and r–p_success dependence

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the 10% is already conditional on success, so null and surrogate-only worlds sit inside the 60% failure mass. E[r×p] = E[r]×E[p] holds unless "success" can be defined on a surrogate, and CG's text doesn't clearly do that.

- **The Advocate's own offset argument undercuts this.** To defend the model, the Advocate says the trial targets "the lung-damage endpoint" and that CG values "only mortality." If Phase II/III "success" is defined on lung damage or bacteriological endpoints, as the Advocate's offset argument implies, then success worlds can have zero mortality effect.
  - That is the covariance problem the critique describes. The Advocate cannot hold both that success is a mortality-relevant result (existing coverage) and that the trial's success endpoint is morbidity (offsets).
  - The Advocate frames this as a textual ambiguity. The ambiguity is the residual risk, and it is unresolved, not defended.
- **A simple derivation shows the stakes.** Let f be the fraction of "successes" that are surrogate-only, with zero mortality effect.
  - Expected relative reduction = 0.4 × (1−f) × 0.10.
  - With SROI linear in r (as the Advocate agrees), baseline 3,055x gives f = 0.2 → 2,444x, f = 0.3 → 2,138x, and f = 0.5 → 1,527x.
  - I cannot ground f. The reference class has no mortality data, so f is an uninformed prior. But the Advocate's coverage argument implicitly sets f = 0, and that is not grounded either.
- **On winner's curse versus prior shrinkage.** I accept the Advocate's semantic point. The relevant quantity is the true effect given a positive trial.
  - The Advocate also says the 10% has "no stated derivation." A conditional-on-success round number is most naturally read as "what a positive trial would show." That is an observed-effect anchor, and it is exactly the quantity that overstates the true effect.
  - I cannot verify how CG formed the 10%. If it is an observed-effect-style number, downward shrinkage follows. If it is a true-effect prior, the Advocate's point stands.
- **The "nonexistent anchor" point cuts both ways.** If 10% has no anchor, the Advocate cannot show it is a prudent central value. The Advocate concedes this ("I cannot show that 10% is the right central value rather than a placeholder").

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the reference class concerns surrogates, not mortality. Rosuvastatin is inconclusive rather than null (HR>1 may favor rosuvastatin). The atorvastatin signal is the grant's premise, not counter-evidence. And the pattern informs p_success, so using it for r double-counts.

- **Conceded:** the reference class (vitamin D, metformin, CC-11050, everolimus) never tested mortality, so it cannot calibrate a mortality effect size. The critique already says to drop the claim that these agents "failed to translate to outcome benefit." That caps its weight.
- **Rosuvastatin direction.** The Advocate says the usual convention and the favorable point estimate are unconfirmed ("I cannot confirm from the evidence package").
  - That is an unverified reading, not a rebuttal. The verifier package supports only: median 42 days in both arms, HR 1.30 (0.88–1.91), p = 0.19, and authors concluding no substantive benefit.
  - If the Advocate's reading is right, the same CI that "includes meaningful benefit" also includes a 12% harm. A trial of this kind cannot distinguish a real effect from noise. That is equally true of the Nigeria Phase II signal.
  - The "statement about power" claim is the Advocate's inference. No source is cited for it.
  - I accept the "class-adjacent, not atorvastatin" caveat. It was already flagged in the evidence.
- **"Atorvastatin is the premise."** The critique doesn't claim the 40% is too generous. It claims r, conditional on success, is optimistic.
  - The verifier notes the Nigeria trial is Phase II, bacteriological-load only, with no mortality data. This tells us r has no direct evidential anchor at all, which the Advocate partly concedes ("a conditional effect below 10% is a reasonable prior").
- **Double-counting.** This is the Advocate's strongest evidence point, and it is partly valid.
  - Surrogate failures are mainly evidence about whether trials turn positive, which p_success already prices.
  - But CC-11050 and everolimus had marginal FEV1 signals, and vitamin D had subgroup-only conversion benefit. Those are positive-but-small signals, which bear on effect size given a positive result.
  - The two parameters answer different questions, so the shrinkage is not strictly duplicative. The overlap is real but unquantified, and I cannot say how much.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: r = 0.07–0.09 keeps SROI at about 2,140–2,750x, above the ~2,000x bar. Only the −50% case crosses, and that is outside the critique's own range.

- **Arithmetic conceded.** 3,055 × 0.9/0.8/0.7 gives about 2,749 / 2,444 / 2,138, and the −50% case (r = 0.05) is not in the critique's stated 0.07–0.09 range.
- **The Advocate evaluates the channels in isolation.** The critique names two: shrinkage of r, and covariance between r and p_success.
  - Combining them (my derivation, both factors illustrative): r shrinkage ×0.8 and f = 0.2 gives 0.8 × 0.8 = 0.64, so 3,055 × 0.64 ≈ 1,955x. That is below the bar.
  - Both inputs are ungrounded, so this shows the conclusion is sensitive to the combination, not that it is likely.
- **The Advocate concedes the margin is thin.** At r = 0.07, SROI is only ~7% above the bar, and the Advocate says other downward adjustments "could then combine with this one to cross it."
  - The minimum plausible magnitude is therefore not a clearly-above-bar outcome. The Advocate's "partial defense" rests on the shrinkage-only reading.
- **The magnitude is uninformed.** I cannot ground the 0.7–0.9 factor either. What survives is the direction and the thin margin.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: CG values only on-treatment mortality, so morbidity, post-treatment mortality, transmission, and diagnostic value are implicit zeros. Baseline mortality may also be understated.

- **The offsets are not in the model.** They are unquantified zeros in the model, and the Advocate offers no magnitudes.
- **The morbidity offset depends on the same uncertain mechanism.** The Nigeria signal is bacterial load, not lung damage.
  - In a surrogate-only world, where r × p_success is overstated, there is no reason to assume a lung-function or morbidity benefit exists.
  - The reference class has FEV1 evidence (CC-11050, everolimus), and it was marginal. That is evidence against the lung-damage offset being large.
  - The offsets are correlated with the downside scenario, not independent of it.
- **Baseline mortality understatement** comes from the parameter map and is speculative as presented. It targets a different parameter, not r.
- **The Advocate concedes** the model has no time discounting, which biases against the offsets. The offsets are therefore a possibility, not a counterweight.

**KEY UNRESOLVED QUESTIONS:**
- How does CG define "Phase II and Phase III both succeed" (the primary endpoint, mortality or a surrogate)? This determines whether f is near 0 or materially positive.
- Is the 10% anchored on an observed or optimistic effect (winner's-curse exposure) or a true-effect prior? CG gives no derivation.
- What is the direction convention in the rosuvastatin HR 1.30? The verifier package does not settle it.
- Does the atorvastatin mechanism plausibly reduce mortality beyond reducing bacillary load? Neither side has direct evidence.
- How much of the reference-class signal is already reflected in the 40%, versus not yet applied to r?

### Judge Audit
Surviving strength: moderate
Justification: The shrinkage-only version of the critique did not survive as a bar-crossing concern. The Advocate's linear-scaling synthesis was conceded, and the 0.7–0.9 factor is ungrounded by everyone's admission. What survives is the definitional issue. The Challenger turned the Advocate's own "lung-damage endpoint" offset argument into a grounded case that success may be surrogate-defined, and the Advocate's coverage argument does not survive that inconsistency. The Challenger's push below the bar relied on stacking overlapping, ungrounded factors and on a misread of the FEV1 evidence. So the critique holds as a direction plus a consequential, unresolved ambiguity, not as a demonstrated quantitative error.
Recommended action: 2. SPECIFIC INVESTIGATION: Check CG's grant documentation and model notes for two things:
   - The primary endpoint of the funded Phase IIc and Phase III atorvastatin trials, and therefore what "success" in the 40% means.
   - The provenance of the 10% conditional effect: whether it is meant as an observed trial effect or a true-effect prior.

   This is a document lookup and is feasible now.
   - If success is defined on mortality, the covariance channel drops out and only modest r-shrinkage remains (SROI ~2,400–2,750x, above the bar).
   - If success is defined on a surrogate (bacillary load or lung function), add an explicit surrogate-only fraction f to the model as the single representation of the downside, not stacked on a separate shrinkage factor. The bar is then crossed at roughly f ≥ 0.35.

   Interim conclusion: treat r as downward-skewed with a central value around 0.08–0.09. On its own this does not overturn the bar, but it should be tracked as a contributor to cumulative downside alongside other critiques.
Action feasibility: requires_specified_evidence
Advocate failures: ["sound_synthesis_noted: The magnitude challenge scales the 3,055x baseline linearly by the critique's own range, giving r = 0.09/0.08/0.07 → ~2,750x/2,444x/2,138x. It also correctly notes that only r = 0.05 crosses the ~2,000x bar, and that this value lies outside the critique's stated range. Every step is shown, and the Challenger conceded the arithmetic.", 'sound_synthesis_noted: The double-counting argument says surrogate-translation failures are mainly evidence about p_success, which the 40% already prices, so applying them again as r-shrinkage risks counting the same information twice. This is a logical argument grounded in the model structure. The Challenger called it "partly valid.', 'unsupported_estimate_pseudo: The authors\' conclusion of \'no substantive benefit overall\' is a statement about power." The verifier package supports only the HR, CI, p-value and the authors\' conclusion. Recasting the null as underpowered is an inference with no source. The direction convention was properly flagged as unconfirmed, but the CI reading ("12% worse to 91% better") is built on that unconfirmed convention. The power claim then goes beyond what the data in the package establish. (Minor.)', 'call_to_ignorance: The offsetting factors list unvalued channels: morbidity DALYs, post-treatment mortality, transmission and diagnostic value. The Advocate suggests a drug "that works on lung damage could still deliver value." No magnitudes or evidence are given that atorvastatin affects lung damage. The Nigeria signal is bacillary load only. The Advocate hedges ("the offset is not guaranteed"), which mitigates this. Even so, the section relies on the possibility of unmodeled benefit rather than any evidence of it.']
Challenger failures: ['sound_synthesis_noted: The f-fraction derivation computes expected reduction = 0.4 × (1−f) × 0.10, giving f = 0.2/0.3/0.5 → 2,444x/2,138x/1,527x. The structure follows directly from the model. The Challenger explicitly states f is ungrounded and presents it as a sensitivity illustration, not an estimate. This is legitimate conditional analysis.', 'unsupported_estimate_pseudo: The Challenger combines the two channels: "r shrinkage ×0.8 and f = 0.2 gives 0.64… ≈1,955x. That is below the bar." The inputs are acknowledged as ungrounded. The chain also has a logical gap: it multiplies two channels as if independent when they substantially overlap. The critique\'s own mechanism presents the surrogate-only/real-effect mixture as the way to model the downward skew. Surrogate-only "successes" are also part of why a shrinkage factor would apply. The Challenger had just conceded overlap between reference-class signals and p_success in the double-counting response, then stacked overlapping adjustments without addressing it. This is the Challenger\'s only route below the bar.', 'strawmanning: The Advocate\'s coverage argument implicitly sets f = 0." The Advocate did not set f = 0. They said a gap arises only if success is surrogate-defined, called this "an ambiguity in CG\'s text," and conceded "CG should define it." This is a mild mischaracterization. The adjacent point about internal inconsistency was legitimate and stronger.', 'unsupported_estimate_pseudo: The Challenger writes, "The reference class has FEV1 evidence (CC-11050, everolimus), and it was marginal. That is evidence against the lung-damage offset being large." There are two problems:', 'false_definitiveness: The minimum plausible magnitude is therefore not a clearly-above-bar outcome." This follows directly from a combination the Challenger had just described as showing only "sensitivity… not that it is likely." The sentence hedges and asserts at once.']
Debate resolved: Both sides agree on four points:
- The shrinkage channel, at the critique's own 0.7–0.9 range, leaves SROI at ~2,140–2,750x, above the ~2,000x bar.
- The non-atorvastatin reference class cannot calibrate a mortality effect size.
- CG's 10% has no stated derivation.
- The direction of any adjustment is probably modestly downward.

The debate also established that the covariance channel bites only if "success" can occur on a surrogate endpoint, and that this hinges on an identifiable fact about CG's model.
Debate unresolved: The main open question is how CG defines "Phase II and Phase III both succeed": mortality or a surrogate (bacteriological or lung-function). This determines whether f is near zero or material, and f = 0.5 would push SROI to ~1,527x. A second open question is how much the shrinkage and covariance channels, and the 40% p_success, overlap. The Challenger's below-bar combination depends on treating them as independent, and neither side quantified the overlap.

--- Critique: Hepatotoxicity and myopathy add a negative tail, and the combined attenuations compound ---

### Advocate
**DEFENSE OF GIVEWELL'S POSITION (CG): Hepatotoxicity and myopathy add a negative tail, and the combined attenuations compound**

**EXISTING COVERAGE:**

1. **The harm tail is mostly inside the 40% failure probability.**
   - CG's formula is SROI = (benefit / cost) × 40%.
   - The 10% relative reduction is explicitly conditional on a positive result.
   - A world where atorvastatin is net-zero or harmful (hepatotoxicity with HRZ, myopathy) is a world where Phase II/III does not succeed. It is not a world where the drug is adopted with a negative effect.
   - A trial that detects harm stops adoption. It does not produce negative realized value at scale.
   - The Quantifier's −0.01 on E[r] applies a 10% harm probability to the conditional effect size. That double counts, because those worlds already carry zero benefit in the 60% non-success mass.
   - The critique's own framing, "CG models only a non-negative effect," is correct. But for an R&D grant the trial acts as a truncation filter on the downside.

2. **PK attenuation and the reachable fraction are partly embedded in the structure.**
   - The Phase III success criterion is an effect detected in patients on actual rifampicin-containing regimens. Any rifampicin–atorvastatin interaction operates inside the trial.
   - If the trial succeeds, the observed effect already reflects that interaction. PK attenuation therefore mainly lowers p_success. It does not scale the conditional effect, except through winner's-curse shrinkage.
   - The Phase IIc trial is described as testing "dosing strategies." That is the mechanism for finding a dose that overcomes enzyme induction, if induction matters.
   - A trial-measured relative reduction in all-cause on-treatment mortality includes early deaths and HIV-related deaths in its denominator. If CG's 10% is read as that kind of whole-population relative effect, a separate "reachable fraction" of 0.65–0.75 double counts. CG does not derive the 10%, and I concede this ambiguity below.

3. **Overlap and correlation.**
   - The critique concedes that its factors overlap with Critiques 1–4 and are correlated.
   - It also concedes that CG's 10% "may already partly embed some attenuation."
   - Multiplying three overlapping haircuts and then applying a harm tail layers four adjustments onto one parameter.

**EVIDENCE WEAKNESSES:**

1. **The additional evidence is adjacent, not direct.**
   - The StAT-TB protocol's pravastatin–rifampin interaction concerns pravastatin, not atorvastatin.
   - The metformin PK substudy (24% reduction in rifampicin bioavailability) concerns a different drug, and the direction is reversed. Metformin lowered rifampicin exposure, not rifampicin lowering metformin exposure. The critique itself calls this a "reference-class point."
   - The critique says it could not verify the atorvastatin–rifampicin interaction. Taking it conditionally, rifampicin is a CYP3A4 inducer and atorvastatin is a CYP3A4 substrate. A direction of effect is therefore plausible, but its magnitude is not established.

2. **No evidence supports the numbers.**
   - The ranges 0.65–0.75, 0.5–0.8 and 0.7–0.9 are self-described "illustrative" and "UNGROUNDED."
   - The hepatic harm claim rests on absence of evidence. The critique concedes that existing small trials "show no hepatic signal."
   - I cannot ground a specific background rate of serious statin hepatotoxicity from the verifier package. Treat any rate I might quote as an uninformed prior, and I do not rely on one.

3. **The "material" label is not supported by the sensitivity run.**
   - Every sensitivity case with a stated basis stays above the bar.
   - Low case (−20% on relative_reduction, implying about 0.08): SROI ≈ 2,444, above 2,000, with `crosses_bar_low: false`.
   - Quantifier central (0.095): SROI ≈ 2,902, a 5% change, far below the ~25% materiality threshold.
   - The compounded 0.023–0.054 range was not run. Materiality rests on an untested, ungrounded extrapolation.

**MAGNITUDE CHALLENGE:**

1. **Harm tail alone.**
   - A −5% change is a quarter of the ~25% decision-relevance threshold. The critique itself calls it "modest and not threshold-crossing."
   - The −5% also overstates the effect, because those worlds are already counted in the 60% failure mass.

2. **Compounded range.**
   - Product check: 0.65 × 0.5 × 0.7 = 0.2275 and 0.75 × 0.8 × 0.9 = 0.54. This matches the critique's 0.23–0.54.
   - Linear scaling of the baseline SROI of 3,055 (the model is linear in relative_reduction, consistent with the sensitivity result of −20% for −20%) gives roughly 3,055 × 0.23 ≈ 700 and 3,055 × 0.54 ≈ 1,650.
   - This would cross the bar. But it requires all three haircuts to be real, additive to CG's baseline, non-overlapping, and set at their most pessimistic ends. The critique disclaims each of those conditions.
   - Taking the midpoints (about 0.70 × 0.65 × 0.80 ≈ 0.36) is no more grounded. It is an average of bounds I cannot verify.

3. **Point estimates.** Without an empirical basis for any factor, the null hypothesis is that CG's 10% conditional effect is an order-of-magnitude assumption. It carries large uncertainty in both directions, not a biased central estimate.

**OFFSETTING FACTORS:**

1. **Zero-valued benefit channels.** The BOTEC values only on-treatment mortality. The context cites reduced lung damage on chest X-ray, and the parameter map lists implicit zeros for:
   - morbidity DALYs,
   - post-treatment mortality,
   - transmission averted,
   - diagnostic value.
   These are upside the compounding analysis ignores. They could offset a smaller on-treatment mortality effect.

2. **Symmetry of the uncertainty.** The 10% is an unanchored assumption. A critique that lowers it without considering that it might be conservative applies the haircuts in one direction only. I cannot ground a specific upward adjustment from the verifier package, so I note this only as a reason the critique's range is not an unbiased interval.

3. **Surrogate-to-mortality cascade.** If the surrogate benefit (faster clearance) is real, shortened treatment or reduced relapse could add value that the BOTEC does not count. This is conditional and ungrounded.

**OVERALL ASSESSMENT:**

- **Harm tail alone: Strong defense.**
  - It is largely a double count with the 40% p_success.
  - Its effect is −5% at most, far below the materiality threshold.
- **Compounding claim: Partial defense.**
  - It is self-flagged as illustrative and ungrounded.
  - It overlaps with other critiques.
  - It conflates effect-size attenuation with success-probability attenuation.
  - But a flat, underived 10% is exposed to exactly this kind of compounding, and my structural arguments rely on interpretations of what the 10% means that CG does not state.
- **Overall: Partial, leaning strong.** The harm-tail critique does not survive. The compounding concern is a legitimate sensitivity flag, not a demonstrated bias.

**CONCESSIONS:**

1. CG states no derivation of the 10% and no definition of what it covers. My argument that PK attenuation and unreachable deaths are already embedded depends on how the 10% is interpreted. If it is meant as an effect on an eligible subpopulation, the reachable-fraction haircut is not a double count.
2. Winner's-curse shrinkage between a Phase IIa/b surrogate signal and a Phase III mortality effect is a real mechanism. It is not captured by p_success unless "success" is defined to include a mortality effect size comparable to 10%. CG does not define success.
3. If the three haircuts were real and non-overlapping at their pessimistic ends, SROI would fall to roughly 700–1,650, below the bar. The structural defense and the unexamined overlap are what keep that from being a demonstrated finding.
4. The statin–rifampicin interaction is plausible, and drug-interaction evidence exists for other agents (pravastatin, metformin). The critique is right that CG's "no consideration" of this is a real gap in the document, even if the SROI impact is not demonstrated.

### Challenger
REBUTTAL: Hepatotoxicity and myopathy add a negative tail, and the combined attenuations compound

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the harm tail sits inside the 40% failure mass, because a trial that detects harm stops adoption, so applying −0.01 to the conditional effect double counts.

- **I concede the narrow point.** For harm that a Phase III mortality trial would detect, the truncation argument is sound. The critique itself calls the tail "modest and not threshold-crossing," and the sensitivity run shows −5%. I do not defend the harm tail as a standalone driver.
- **The truncation argument depends on a definition CG never gives.** The Advocate concedes that CG does not define "success." If success is "positive point estimate, or statistical significance on a surrogate," then a net-zero true effect can pass and the tail is not already in the 40%. If success means "mortality effect near 10% in a rifampicin regimen," the Advocate is right. Neither side can determine which applies.
- **Truncation does not filter rare or late harms.** Hepatotoxicity under HRZ is a tail event that a trial may be underpowered to detect. The critique concedes small trials "show no hepatic signal but cannot rule one out." Such a harm would lower the pooled effect at scale without necessarily stopping adoption. I cannot ground a rate for this, so it stays an open residual.

> The Advocate claims: PK attenuation operates inside the trial, so it mainly lowers p_success rather than the conditional effect, and "dosing strategies" in Phase IIc is the mechanism to overcome induction.

- **The argument moves the haircut rather than removing it.** If attenuation lowers p_success, then CG's flat 40% is overstated by the same logic. The Advocate shows no sign that CG adjusted the 40% for a known rifampicin interaction. The SROI is therefore still too high, and only the parameter that should absorb the correction changes.
- **Attenuation also shrinks the conditional effect.** A trial can succeed with a smaller-than-planned effect, for example a significant 6% reduction rather than 10%. Conditional on success, the effect is then below CG's flat 10%. The Advocate's "mainly lowers p_success" understates this channel. The Advocate also concedes that winner's-curse shrinkage is not captured by p_success.
- **The "dosing strategies" rescue is speculative.** It assumes induction matters, that a dose exists which overcomes it, and that the dose is tolerable. Higher atorvastatin doses raise the myopathy and hepatotoxicity concern in the critique's title. So the rescue connects to the harm channel.
- **The "reachable fraction double-counts" argument is conditional.** The Advocate concedes it holds only if the 10% is read as a whole-population effect. CG gives no derivation, so the point is unresolved, not refuted.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the pravastatin and metformin evidence is adjacent, the metformin direction is reversed, and no evidence supports the specific numbers.

- **Numbers.** I agree no evidence supports 0.65–0.75, 0.5–0.8 or 0.7–0.9. The critique labels them UNGROUNDED, so there is no dispute here.
- **Metformin direction.** I concede the Advocate's reading. Metformin lowering rifampicin exposure is a different interaction from rifampicin lowering statin exposure. It is better read as support for a harm channel: an adjunct that erodes first-line drug exposure could worsen TB outcomes. It does not support the attenuation factor, and I withdraw it for that purpose.
- **Pravastatin versus atorvastatin.** The Advocate treats the pravastatin interaction as merely adjacent. The StAT-TB protocol shows that rifampin–statin interactions are recognised in humans. From background knowledge, which I have not verified, atorvastatin is more CYP3A4-dependent than pravastatin. If so, the mechanistic exposure is likely larger for atorvastatin, not smaller.
- **Evidence status.** The verifier did not complete the rifampicin–atorvastatin check, so that claim is UNVERIFIABLE, not REJECTED. The Advocate agrees the direction is plausible. Conditional on a CYP3A4-induction effect of any size, the existence of the haircut is not in question, only its magnitude.
- **The materiality objection tests the wrong range.** The Advocate notes every sensitivity case stays above the bar. The low case was −20% on relative_reduction (about 0.08). The critique's compounded range is 0.023–0.054, so the run never probed the critique's claim. A "does not cross" result at 0.08 says nothing about 0.054.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

- **Headroom derivation.**
  - Baseline SROI is 3,054.9 and the bar is ~2,000 (the Advocate's figure). The model is linear in relative_reduction, per the −20% for −20% result.
  - 2,000 / 3,054.9 = 0.655. Any combined multiplier below 0.655, equivalent to relative_reduction below about 0.0655, crosses the bar.
  - Headroom is only about 35%, which is thin for a parameter with no derivation.
- **Where the critique's range falls.**
  - Every point in the critique's product range (0.23–0.54) is below 0.655, including the optimistic end.
  - The optimistic ends of all three factors multiplied give 0.54, which still crosses.
  - Reachable fraction at 0.65 alone gives about 1,986, a marginal cross.
  - Midpoints give 0.70 × 0.65 × 0.80 ≈ 0.36, or about 1,110.
- **Minimum plausible magnitude.**
  - Only the weakest single haircut fails to cross: shrinkage alone at 0.7–0.9 gives 2,138–2,750, plus the harm tail at 0.95 gives 2,031–2,612.
  - The decision turns on whether at least one more haircut at moderate size applies. For example, shrinkage midpoint 0.80 × PK midpoint 0.65 = 0.52 crosses without needing the reachable fraction.
  - I do not claim the central case is established. I claim a single moderate second haircut is enough to cross, and the Advocate concedes the shrinkage mechanism and the interaction direction are real.
- **Overlap.** I concede that stacking all four adjustments naively is wrong. That is a reason to estimate the net haircut once, not a reason to assume it is 1.0.

**RESPONSE TO "OFFSETTING FACTORS":**

- **The offsets are not in the model, and the Advocate admits they are ungrounded.** CG zeroes morbidity DALYs, post-treatment mortality, transmission and diagnostic value. The Advocate cannot ground an upward adjustment from the verifier package. I cannot ground one either, so this is symmetry-of-ignorance, not a quantified offset.
- **The offsets are correlated with the haircuts.** If rifampicin induction lowers atorvastatin exposure, it lowers the lung-damage and clearance benefits through the same pathway. If the surrogate effect does not translate to mortality (winner's curse), the surrogate-to-mortality cascade offset also weakens. These channels are not independent hedges against the attenuation.
- **The upside offset conflicts with the harm tail.** If hepatotoxicity or myopathy forces dose limits, the drug's benefit channels shrink in the same worlds.

**KEY UNRESOLVED QUESTIONS:**

- What does CG's "success" mean: a surrogate signal, or a mortality effect near 10%? This decides whether the harm tail and the winner's-curse shrinkage are already in the 40%.
- What population and endpoint does the 10% describe: a whole on-treatment cohort, or an eligible subgroup? This decides whether the reachable-fraction haircut double counts.
- What is the actual rifampicin effect on atorvastatin exposure (UNVERIFIABLE here), and does any tolerable dose overcome it?
- Does CG's 40% already reflect a known statin–rifampicin interaction, or should it be lowered?
- What is the net combined haircut after removing overlap? Headroom is only about 35%, so a net haircut above that is enough to cross the bar.

### Judge Audit
Surviving strength: moderate
Justification: **Justification:**
- **Harm-tail component (weak).** The Advocate's truncation argument holds, and the Challenger conceded it.
- **Compounding component (moderate).**
  - The Challenger's headroom derivation is grounded and exposes how fragile the flat 10% is.
  - The Advocate's main structural counters (PK lowers only p_success; the reachable fraction double counts) rest on interpretations of CG's parameters that the Advocate conceded CG never states. The Challenger correctly showed these counters relocate the haircut rather than eliminate it.
  - The Challenger's case for crossing the bar still leans on midpoints of ungrounded ranges and on an unproven exposure-to-efficacy link.
- **Overall.** The critique survives as a well-specified sensitivity flag, not as a demonstrated bias.
Recommended action: 1. **CONCLUDE NOW** (high confidence): Drop the harm tail as a standalone adjustment. It is largely inside the 40% failure mass and below materiality either way. Do not apply the 0.023–0.054 compounded range; it double counts overlapping factors.

2. **SPECIFIC INVESTIGATION** (feasible with existing tooling):
   - **(a) Interaction magnitude.** Re-run the verifier with targeted searches for:
     - published rifampin–atorvastatin drug-interaction studies, including atorvastatin labeling DDI tables reporting AUC changes;
     - whether the atorvastatin TB trials (e.g., the Nigeria Phase II) co-administered rifampicin and measured statin levels.
   - **(b) Grant terms.** Pull CG's grant or BOTEC documentation for the definition of Phase III "success" and the endpoint and population of the 10% relative reduction. This settles whether the shrinkage and reachable-fraction haircuts are double counts.
   - **(c) Threshold analysis.** Add one sensitivity case at relative_reduction = 0.065, and one at a single de-duplicated net multiplier informed by (a) and (b). This makes the 35% headroom an explicit, reportable threshold.

**action_feasibility:** requires_specified_evidence
Action feasibility: actionable_now
Advocate failures: []
Challenger failures: []
Debate resolved: Both sides agree on the following:

- **Harm tail.** It is not decision-relevant on its own. It is at most about −5%, and is largely or wholly absorbed in the 60% failure mass for any harm a trial would detect.
- **Factor values.** The three attenuation values are ungrounded and overlap, so their naive product is not an estimate.
- **Headroom.** It is only about 35%. The bar is crossed at a net multiplier of about 0.655, equivalent to relative_reduction of about 0.0655. So a single real, de-duplicated haircut of moderate size would flip the decision.
Debate unresolved: Whether the net haircut exceeds about 35% after overlap is removed remains contested. It turns on three things neither side could establish:

- what CG's "success" and its 10% effect refer to (surrogate versus mortality endpoint; whole cohort versus eligible subgroup);
- the actual rifampicin–atorvastatin exposure effect, and how it maps to efficacy;
- whether CG's 40% already reflects that interaction.

--- Critique: A $7M Phase III cannot be powered on mortality, and the CEA's benefit is mortality only ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: A $7M Phase III cannot be powered on mortality, and the CEA's benefit is mortality only

EXISTING COVERAGE:
- The $7M is explicitly "all-in": it covers "later Phase III trials, guideline changes, dissemination and validation." SROI is computed on all-in cost and all-in benefit, so CG did not leave the Phase III out of the denominator.
- The 40% probability that "Phase II and Phase III trials both succeed" is the existing place where endpoint risk is absorbed.
  - A surrogate-based Phase III that fails to move WHO guidelines, or a mortality-powered trial that misses, both reduce that 40%.
  - CG does not define "success" (CEA Parameter Map, p_success). That is a transparency gap, but the risk is nominally priced in.
- The Phase IIc already includes survival among its measured outcomes ("dosing strategies for survival, infection clearance and lung damage"). CG treats mortality as the target outcome, not a surrogate-only programme.
- The BOTEC values only mortality (Parameter Map: "only mortality is valued"). Lung-damage reduction, post-treatment survival, transmission and diagnostic value are all implicit zeros.
  - This matters for the "unsupported benefit" fork. If the Phase III is surrogate-based and succeeds, the surrogate benefit (lung damage) is an unvalued benefit stream, not a missing one.
  - I cannot quantify this offset from the evidence package. It is a direction-of-bias point, not a number.

EVIDENCE WEAKNESSES:
- The Quantifier's sample-size calculation is arithmetically correct but uses a 5% baseline.
  - Check at 5% to 4.5%: n per arm = (1.96+0.84)² × (0.05×0.95 + 0.045×0.955) / 0.005² ≈ 7.85 × 0.0905 / 0.000025 ≈ 28,400. This matches the Quantifier's figure.
  - At CG's own 6% baseline, 10% relative reduction: n per arm ≈ 7.85 × (0.0564+0.0510) / 0.000036 ≈ 23,400, or about 47,000 total. This is below the Quantifier's 57,000 upper figure.
- The per-participant cost is the weak link, and the Quantifier admits it.
  - The $500–$1,000 pragmatic-trial range and the "thousands of dollars" conventional-TB-trial cost are both labelled UNGROUNDED.
  - The RECOVERY per-participant cost, the key comparator for a large simple trial, was not checked (search limitation).
  - My recollection is that large pragmatic trials have run at hundreds of dollars per participant. I cannot ground that, so treat it as an uninformed prior, not a rebuttal.
- The Quantifier's own text concedes $120–$200 per participant is "not shown to be impossible." The critique establishes tension, not contradiction.
- The Phase II HDT trials cited (FEV1 and culture conversion in TB-HDT, time to culture conversion in the rosuvastatin trial) show that Phase II HDT trials use surrogates.
  - That is the norm for Phase II. It says little about what a Phase III or WHO guideline group would require.
  - The WHO GDG endpoint requirement was not verified.
  - If the GDG would accept a composite or unfavourable-outcome endpoint, the fork resolves toward a cheaper, smaller trial. That would not be an "unsupported" mortality-only benefit if the benefit is in fact driven by mortality.
- The 10% relative reduction and the trial design are not jointly pinned.
  - If the Phase III is powered for a larger effect, N falls sharply. At 6% baseline and a 25% relative reduction (6% to 4.5%): n per arm ≈ 7.85 × (0.0564+0.0431) / 0.000225 ≈ 3,470, or about 6,900 total.
  - A trial powered for 25% that "succeeds" would show an observed effect at least that large. That would not be consistent with a 10% assumed effect, so this is not a clean rescue. It does show that the N required depends on a design choice the critique treats as fixed.
- Enrichment is precedent-supported but limits generalisability.
  - Dexamethasone in TB meningitis was adopted on a mortality endpoint with roughly 545 patients (Thwaites et al., NEJM 2004; cited from memory).
  - The Quantifier already notes the generalisability problem for the drug-susceptible majority. I concede that point.

MAGNITUDE CHALLENGE:
- The Quantifier's text and sensitivity run disagree.
  - The narrative gives a Phase III central estimate of $25–40M and an SROI of about 570x (3,000 × 7/37, a 3–10× reduction).
  - The sensitivity run used $16M, giving 1,336.5x (−56%, about 2.3×). This is well short of the 3–10× headline.
  - So the sensitivity run does not support the 3–10× claim as stated. It supports about 2.3× at the central point and about 7× only at the high end (427.7x, implying about $50M).
- The $7M-to-$37M scaling has no stated baseline.
  - The Quantifier admits the "unclear baseline for the 7/37 scaling."
  - The $37M would equal the Phase III cost, plus the unscaled non-trial costs, plus the grant. None of these components are separately grounded.
- The central cost estimate rests on a chain with ungrounded inputs.
  - Chain: N (calculated, about 35,000–57,000) × per-participant cost (ungrounded) = Phase III cost.
  - The N step is sound. The cost step is not grounded.
  - The $15–100M range is wide enough to include the Quantifier's own $16M run and a roughly $7M "pragmatic" design.
- The bar is not a knife-edge on this parameter.
  - Break-even for 2,000x is 54e9 × 0.4 / 2,000 ≈ $10.8M all-in.
  - So the critique matters only if all-in costs exceed about $10.8M. The Quantifier's low end (about $15M plus) does clear that.

OFFSETTING FACTORS:
- The mortality-only benefit stream is conservative in ways the critique does not net out.
  - Morbidity or lung-damage DALYs, post-treatment mortality, transmission averted and the sweat diagnostic are all valued at zero.
  - If a surrogate-based Phase III is what makes the trial affordable, those unvalued benefits partially offset the "unsupported mortality benefit" half of the fork.
  - The magnitude is unquantified and I cannot ground one.
- The SROI is computed on all-in cost and all-in benefit. A higher Phase III cost that other funders (for example NIH or Wellcome) would bear still lowers SROI under this convention, but it does not change CG's marginal cost.
  - I raise this only as a framing point. It does not rescue the headline figure.

OVERALL ASSESSMENT: Partial defense, leaning weak on the core internal-consistency point.
- The following are not defended:
  - The BOTEC gives no breakdown of the $7M.
  - It does not say what endpoint the Phase III is powered on.
  - The implied $150–$300 per participant (about $7M over 23,000–47,000 participants at CG's own 6% baseline) is low relative to usual trial costs, even if not proven impossible.
  - Given CG's own parameter map, "no discussion of what endpoint a $7M-budget Phase III could be powered on" is a fair gap.
- What can be defended is the magnitude. The 3–10× headline is not supported by the Quantifier's own sensitivity run (2.3× at central), and the per-participant cost, the key input, is ungrounded.
- The null hypothesis is not clearly met. A $7M Phase III is plausible only for a very lean pragmatic design or a surrogate or enriched endpoint. In either case a note on endpoint in the BOTEC would be warranted.

CONCESSIONS:
- The fork is real. Either the Phase III is cheaper than typical mortality-powered trials (lean pragmatic design), or it uses a non-mortality or enriched endpoint (so the mortality-only, general-population benefit stream is weaker than modelled), or the cost is higher than $7M.
- All-in cost above about $10.8M takes SROI below the 2,000x bar, so the critique is decision-relevant if the cost is anywhere near the Quantifier's lower range.
- The undefined meaning of "success" in the 40% probability is a transparency weakness.
- I cannot show that the $7M is adequate, and I cannot show the Quantifier's $25–40M is wrong.
```

### Challenger
```
REBUTTAL: A $7M Phase III cannot be powered on mortality, and the CEA's benefit is mortality only

RESPONSE TO "EXISTING COVERAGE":

1. The Advocate claims: the $7M is "all-in", so the Phase III is already in the denominator.
   Response:
   - This restates the question rather than answering it. The critique asks whether $7M can plausibly cover a Phase III, not whether the Phase III was included.
   - The Advocate's own quote says the $7M covers "later Phase III trials, guideline changes, dissemination and validation." The Phase III therefore gets less than $7M.
   - At CG's own 6% baseline, the Advocate's calculation gives about 23,400 per arm, or about 46,900 total. The Phase III alone would then cost under $7M / 46,900 ≈ $149 per participant, before guideline and dissemination costs.

2. The Advocate claims: the 40% p_success absorbs endpoint risk.
   Response:
   - p_success scales benefits. It does not raise cost. If the Phase III is mortality-powered, the cost problem is untouched by a 40% haircut on benefit.
   - If the Phase III is surrogate-based, p_success prices "the trial fails." It does not price "the trial succeeds on a surrogate but the mortality benefit the model assumes is not demonstrated."
   - The model credits a mortality benefit conditional on success. The Advocate concedes that "success" is undefined, so it cannot be shown to absorb this gap. A 40% factor with no definition is not coverage of a specific mismatch.

3. The Advocate claims: Phase IIc includes survival, so mortality is the target.
   Response:
   - A Phase II survival measure is not a mortality-powered result, and the Advocate offers no sample size for it. It says nothing about the $7M Phase III budget.
   - The verified evidence is that the HDT Phase II trials found used surrogates: FEV1 and culture conversion in TB-HDT, and time to culture conversion at week 8 in the rosuvastatin trial. That supports the fork.

4. The Advocate claims: unvalued benefits (lung damage, transmission, diagnostics) offset the "unsupported mortality benefit" half of the fork.
   Response:
   - The Advocate concedes it cannot quantify this. An unquantified offset cannot neutralise a quantified cost gap.
   - It addresses only one branch. In the mortality-powered branch, extra unvalued benefits do nothing about the cost problem.
   - In the surrogate branch, lung-damage benefit would be valued only if a revised CEA valued it. The current model's mortality benefit would then still be unsupported.

RESPONSE TO "EVIDENCE WEAKNESSES":

1. The Advocate claims: Phase II surrogate use is the norm and says little about Phase III or GDG requirements.
   Response:
   - Conceded as far as it goes. The verifier marked the WHO GDG endpoint requirement as unverified, not contradicted. The search limitation was exhaustion, not a negative finding.
   - Treat it as a conditional. If the GDG accepts a composite or unfavourable-outcome endpoint, the trial may be smaller. But then the model's mortality-only benefit stream rests on an unmodelled translation from composite to mortality effect.
   - If the GDG requires mortality, the sample sizes are as computed.
   - Either branch produces a gap the BOTEC does not discuss. The Advocate concedes this ("a note on endpoint in the BOTEC would be warranted").

2. The Advocate claims: the per-participant cost is ungrounded, and its own recollection of "hundreds of dollars" is only an uninformed prior.
   Response:
   - Both sides lack a grounded per-participant cost. The Advocate explicitly disclaims its recollection, so it is not a counter-estimate.
   - The asymmetry is in what each side needs. For the $7M to hold, the cost must be at or below about $150, with a ceiling of about $120–$200 across the 35,000–57,000 range. The critique needs only that the cost not be that low.
   - The Advocate's own upper figure of about $300 is mis-derived. It divides $7M by about 23,000, which is the per-arm number, not the total. At 6% baseline with a 10% relative reduction, the total is about 47,000, giving about $149.
   - The Advocate's own numbers thus do not show $300 is a plausible upper bound for a design powered on a 10% effect.

3. The Advocate claims: powering for a 25% effect cuts N to about 6,900.
   Response:
   - The Advocate itself concedes this is "not a clean rescue." A trial powered for 25% is inconsistent with the 10% effect the benefit calculation assumes.
   - I do not know what effect size the CEA's mortality benefit assumes. I cannot ground one, and the Advocate has not identified it either.
   - A trial powered at 25% that came out at the true 10% effect would likely miss. That is a p_success issue, and it also weakens the model's assumed benefit.

4. The Advocate claims: the dexamethasone TBM precedent (Thwaites et al., NEJM 2004, about 545 patients) shows an enriched mortality endpoint works.
   Response:
   - Conceded as precedent for enrichment, and the Advocate already concedes the generalisability problem.
   - The benefit base is the drug-susceptible majority (the 3.3M-patient figure in the critique). An enriched TBM or advanced-HIV trial would not demonstrate benefit for that population.
   - The enrichment route therefore keeps cost down only by weakening the mortality benefit the model applies to everyone.

RESPONSE TO "MAGNITUDE CHALLENGE":

1. The Advocate claims: the sensitivity run (16M, −56%, about 2.3×) does not support the 3–10× headline.
   Response:
   - Partly conceded: the 3–10× rests on the $25–40M Phase III estimate, which is ungrounded.
   - The run's own arithmetic shows SROI scales as 1/cost: 1336.5 / 3054.9 = 0.4375 = 7/16. The $16M is at the low edge of the critique's $15–100M Phase III range.
   - So the sensitivity run is a favourable case, not the "central" case in the narrative. Even there SROI falls 56%, more than double the 25% materiality bar.
   - The high case (427.7x, −86%) is about 7× and also crosses the bar. Both cases the tool ran cross it.

2. The Advocate claims: the cost range includes a lean-pragmatic $7M design.
   Response:
   - The range includes it only at the extreme. The Advocate's own break-even gives $10.8M all-in for the 2,000x bar.
   - Derivation of the materiality threshold: a 25% SROI drop corresponds to cost ≈ $7M / 0.75 ≈ $9.3M all-in. This follows from SROI ∝ 1/cost, confirmed by the 7/16 ratio above.
   - The finding is therefore insensitive to the details: any all-in cost above about $9.3M, a roughly 33% overrun on the stated number, crosses materiality. That is a low bar for a trial of 35,000–57,000 people.

3. The Advocate claims: the 7/37 scaling has no stated baseline.
   Response:
   - Agreed that it is unclear. It matters only for the headline multiple, not for whether the bar is crossed.
   - Even if non-trial costs are not scaled at all, the Phase III cost alone at the $16M run is enough to cross the bar.

RESPONSE TO "OFFSETTING FACTORS":

1. The Advocate claims: other funders (NIH, Wellcome) might bear Phase III costs.
   Response:
   - The Advocate raises it as framing only and admits it "does not rescue the headline figure."
   - The model is described as computing SROI on all-in cost. Under that convention the cost is counted regardless of who pays.
   - If CG wants a counterfactual or marginal-cost framing, it should state the other-funder assumption and show it in the BOTEC. It is not in the model as presented.

2. The Advocate claims: mortality-only benefit is conservative, with morbidity, post-treatment survival and transmission valued at zero.
   Response:
   - This is a real direction-of-bias point, and I concede it. But it is unquantified, and nothing in the evidence package sizes it.
   - It would offset the benefit side only. The fork's cost side has no offset.
   - Using an unquantified conservatism to cancel a cost shortfall of up to about 2–7× (from the sensitivity runs) is not a defence.

KEY UNRESOLVED QUESTIONS:
- What endpoint is the Phase III assumed to be powered on, and what effect size does the CEA's benefit assume?
- What does the WHO GDG require to change guidance for an adjunctive HDT? Mortality, a composite unfavourable outcome, or a surrogate? This was not verified.
- What is the actual per-participant cost of comparable large pragmatic TB trials, for example RECOVERY-style designs? Neither side has grounded this.
- How much of the $7M is allocated to the Phase III versus guideline and dissemination work?
- Does "success" in the 40% probability require a demonstrated mortality benefit, or only a positive surrogate result?
```

### Judge Audit
Surviving strength: moderate
Justification: The Challenger made grounded arguments the Advocate did not adequately defend:
- the correct ≈$149 per participant derivation and the catch of the Advocate's per-arm error;
- the 7/16 proportionality check and the derived $9.3M materiality threshold;
- the point that p_success scales benefit, not cost.
The Advocate largely conceded the internal-consistency gap. The quantitative magnitude, however, still rests on an unverified per-participant cost. The Challenger overstated the cost gap as "quantified," and the strongest missed defence (WHO's precedent of accepting composite endpoints) was never tested. The qualitative critique is strong. Its decision-relevant magnitude remains open.
Recommended action: 2. SPECIFIC INVESTIGATION: Re-run the verifier with three targeted searches:
- **Per-participant cost of large simple and pragmatic trials:** RECOVERY's reported per-patient cost, and budgets for large TB trials such as Study 31/A5349, TRUNCATE-TB and SimpliciTB. This tests whether ≤$150 per participant is realistic.
- **WHO GDG evidence basis:** the endpoints WHO accepted for recent DS-TB guideline changes, for example composite unfavourable outcome in Study 31/A5349. This tests whether a composite-powered Phase III, needing a few thousand participants, would suffice.
- **CG's own model:** the breakdown of the $7M, the Phase III endpoint, and the assumed mortality effect size behind the benefit stream.

All three are feasible with existing tooling or a direct request to CG.

What can be concluded now, pending that evidence: the BOTEC should state its Phase III endpoint and budget split. The critique is decision-relevant if all-in cost exceeds about $9.3M. The 3–10× SROI reduction should not be adopted as stated.
Action feasibility: requires_specified_evidence
Advocate failures: ['unsupported_estimate_pseudo: The implied $150–$300 per participant (about $7M over 23,000–47,000 participants at CG\'s own 6% baseline)." The $300 upper bound divides $7M by the per-arm N (23,400), not the total N (about 47,000). The Advocate\'s own correct calculation implies about $149 per participant at the 6% baseline. The Challenger caught this correctly. The error loosens the apparent feasibility range by 2×.', 'strawmanning: It supports about 2.3× at the central point." This labels the $16M sensitivity run as the critique\'s "central" case. The critique\'s stated central estimate is $25–40M for the Phase III, or $30–45M all-in, so $16M sits below the low edge of the stated range. Calling the run "central" and then saying it fails to support 3–10× attacks a framing the critique did not use.', 'sound_synthesis_noted: Two derivations hold up:']
Challenger failures: ['false_definitiveness: The Challenger describes the cost side as quantified in three places:', 'false_definitiveness: That is a low bar for a trial of 35,000–57,000 people." The $9.3M threshold derivation is sound. However, the statement that a 33% overrun is easy to exceed assumes the trial is mortality-powered at a 10% effect. That is one branch of the fork, which the Challenger itself treats as unresolved.', 'sound_synthesis_noted: Several moves are grounded and well executed:']
Debate resolved: The debate established three things:
- **The fork is real and conceded by both sides.** Either the Phase III is mortality-powered and needs roughly 35,000–57,000 participants at ≤$150 each, or it uses a surrogate, composite or enriched endpoint that does not directly support the model's general-population, mortality-only benefit. The BOTEC addresses neither branch.
- **The materiality threshold is low.** Since SROI ∝ 1/cost, any all-in cost above about $9.3M crosses the 25% materiality bar, and above about $10.8M takes SROI below 2,000x.
- **The 3–10× headline is not supported.** It rests on ungrounded per-participant costs.
Debate unresolved: Four questions remain open:
- Whether ≤$150 per participant is achievable for a large simple TB trial. Neither side grounded a comparator.
- Whether WHO would change guidance on a composite unfavourable-outcome endpoint, which would make a much smaller trial sufficient.
- What effect size the CEA's mortality benefit actually assumes.
- How much of the $7M is allocated to the Phase III.

--- Critique: The all-in framing counts benefits for every treated patient but not the cost of treating them ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION: The all-in framing counts benefits for every treated patient but not the cost of treating them

**EXISTING COVERAGE:**
- **No explicit delivery-cost line.** The parameter map confirms the BOTEC has no term for procurement, monitoring, health-worker time or adverse-event management. I cannot claim an existing adjustment covers this directly.
- **Partial indirect coverage from conservative benefit omissions.** The map notes "only mortality is valued." The context mentions reduced lung damage on chest X-ray and a sweat-based diagnostic, but neither enters the formula. Post-treatment survival, morbidity and transmission are also zero. These implicit zeros partly offset the missing cost term, though the offset is unquantified.
- **The 40% success probability and 10% relative effect are already conservative-looking.** The expected relative reduction is 4%. These do not address delivery cost, but they set the margin the cost term must erode.
- **The source is a "sample BOTEC" in a methods post, and the text we hold is a close paraphrase.** An omitted line item there is weak evidence about what the full grant analysis considered. This is a conditional point. I cannot show CG did consider delivery costs.

**EVIDENCE WEAKNESSES:**
- **The Quantifier marks the convention UNGROUNDED, and the price range is unverified.**
  - The $1–10 procurement range is "the thread's range," and the Quantifier says they could not verify prices.
  - The monitoring and clinic-time costs that push D toward $33M or higher are speculative. No source is cited.
  - A rough check on the low end: 6 months is about 180 daily tablets, so $1–10 per course implies roughly $0.006–0.055 per tablet. That is plausible for a generic. It is my own back-calculation, not a sourced price.
- **The monitoring-cost premise is unsupported.**
  - The critique says costs are "plausibly higher" once monitoring and clinic time are included.
  - TB patients on treatment already attend scheduled visits or directly observed therapy.
  - If monitoring piggybacks on existing visits and liver checks, incremental D is closer to procurement alone. I cannot ground whether it does. This is a conditional argument, not an assertion.
- **The ATORTUB registry evidence is not about delivery cost.**
  - The NCT06199921 listing (Open Philanthropy as collaborator, 440 patients, phase III "more expensive" than IIb) relates to R&D headroom.
  - It does not bear on D. The Quantifier concedes it is adjacent, since they say they "can't confirm it is the grant in question."

**MAGNITUDE CHALLENGE:**
- **The Quantifier's narrative and their sensitivity run disagree.**
  - The narrative central D of about $10M gives total cost of about $17M and SROI of about 1,250x.
  - The sensitivity run's central is all-in cost of $8.98M, which is D of about $1.98M. It gives about 2,381x, a 22% decline from the 3,055 baseline.
  - The run's central matches the Quantifier's own discounted case (D_effective of about $2–3M), and it stays above the 2,000x bar and inside the 25% materiality threshold.
- **The bar is crossed only in the tail.**
  - Break-even is D below about $3.7M (3.7M ÷ 3.3M ≈ $1.12 per patient). I verified this from 3,055 × 7 / 2,000 = 10.7M, less 7M.
  - Crossing requires either (a) a gross D above $3.7M with CG valuing others' money at full face value, or (b) a gross D above roughly $14.8M if government money is valued at 25%. The 25% is the Quantifier's own assumption, not a CG figure.
  - Option (b) means more than about $4.5 per patient. That sits only in the upper half of the Quantifier's own $1–10 procurement range and above it once monitoring is added.
- **The "high" sensitivity case (1,059x, all-in about $20M) corresponds to D of about $13M.** That is about $4 per patient at full face value. It requires both the upper half of an unverified price range and no discounting of government money. It is a tail scenario, not a central one.
- **The full-face-value convention is questionable.**
  - SROI is expected $OP per dollar of CG-equivalent cost.
  - Spending that comes out of existing national TB or Global Fund budgets plausibly has an opportunity cost below CG's marginal grant. The extent of that discount is unknown, so I cannot give a defended number.

**OFFSETTING FACTORS:**
- **Benefit channels left at zero.** Lung damage reduction, post-treatment survival, relapse and transmission, and diagnostic value all enter at zero. The parameter map says this "could make the estimate robust even if Thread 1 finds a small on-treatment mortality effect." These could easily outweigh a few million dollars of delivery cost, but the size is unquantified.
- **Possible downstream savings.** If atorvastatin reduces lung damage and deaths, there are plausibly fewer retreatments and less post-TB lung disease care. This would reduce net D. I cannot size it from the evidence package.
- **No cost-side double counting.** The 3.3M patients already has the 60% uptake applied. D would scale with that figure, not the 5.5M eligible, so the Quantifier's range is not inflated on that axis.

**OVERALL ASSESSMENT:** **Partial defense.**
- The critique identifies a real structural asymmetry. A benefit is credited for every treated patient while no treatment cost enters the denominator. The one-year-speedup framing does not remove it, because the extra treated cohort in the accelerated year is a real cost.
- On magnitude, the Quantifier's own sensitivity run lands at about 2,381x (-22%), above the bar and below the materiality threshold. Only the tail crosses it.
- The tail rests on unverified prices and an unstated convention.
- I rate it partial rather than strong because break-even is only about $1.12 per patient at face value. Even modest monitoring costs can use up most of the 3,055 → 2,000 cushion if CG counts others' money fully.

**CONCESSIONS:**
- The BOTEC omits delivery costs entirely. A complete all-in framing should either include them or state why they are excluded.
- The break-even arithmetic is correct. Under full face-value counting, any delivery cost above about $1.12 per patient takes SROI below 2,000x.
- The unstated counterfactual-value convention for government and Global Fund spending is a legitimate documentation gap.
- I cannot rule out the 1,000–1,250x outcome. It requires only about $10M of gross D at full face value, which is about $3 per patient.
- The decision-relevant question is whether CG treats others' health budgets at face value. The BOTEC text does not answer it.

### Challenger
REBUTTAL: The all-in framing counts benefits for every treated patient but not the cost of treating them

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: no delivery-cost line exists, but unvalued benefits (lung damage, post-treatment survival, transmission, diagnostics) and the conservative 4% expected effect partly offset the omission.

- **Concession.** The Advocate concedes that no existing adjustment addresses delivery cost directly. The rest of this section concerns whether the proposed offsets repair the gap.
- **The benefit zeros are not a cost-side adjustment.** The parameter map says only mortality is valued. That is a choice about the numerator. It does not make the denominator complete. A BOTEC labelled "all-in" that omits the largest recurring cost has an internal inconsistency, whatever conservatism sits elsewhere.
- **The offset is unquantified and conditional.** The Advocate says "the offset is unquantified" and "I cannot size it." An offset with no size cannot be credited against a cost with a computable break-even of about $1.12 per patient.
- **The omitted benefits depend on the same uncertain effect.** Lung-damage reduction and post-treatment survival only exist if atorvastatin works. That is the 40% success event already in the model. They are not an independent cushion.
- **The "sample BOTEC in a methods post" point proves too much.** The Advocate says an omitted line in a sample BOTEC is weak evidence about the full analysis. The Advocate also admits it "cannot show CG did consider delivery costs." If a simplified illustration is exempt from the omission critique, then no BOTEC can be critiqued. The critique targets the framing as presented, and the Advocate has not produced a version that includes D.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the $1–10 range is unverified, the monitoring premise is unsupported because TB patients already attend visits, and the ATORTUB registry data do not bear on D.

- **Concession on the registry.** NCT06199921 is about R&D headroom, not delivery cost. I do not rely on it for D.
- **Concession on the price range.** The $1–10 figure is the thread's range and the Quantifier could not verify it. Note that the Advocate's own back-calculation, $0.006–0.055 per tablet over about 180 tablets, reproduces this range. The Advocate calls it "plausible for a generic" and offers no lower figure. So the one number the Advocate does examine does not undercut the range.
- **The piggyback argument is itself ungrounded.** The Advocate says monitoring may ride on existing TB visits but admits "I cannot ground whether it does." Two pharmacology points weigh against assuming zero incremental monitoring. Neither is in the verifier package, so treat them as general pharmacology that I cannot cite to a specific source here.
  - First-line TB regimens include hepatotoxic drugs (isoniazid, rifampicin, pyrazinamide). Adding a statin plausibly adds a reason for liver monitoring.
  - Rifampicin is a strong CYP3A4 inducer and atorvastatin is a CYP3A4 substrate. This could affect dosing or exposure, and so cost or monitoring.
- **What this argument does and does not establish.** I am not claiming monitoring is expensive. I am saying the Advocate's zero-incremental-cost scenario is as ungrounded as the Quantifier's higher-cost scenario.
- **The verifier evidence does not support delivery being free.** The verifier notes that procurement alone is cheap and that the result depends on monitoring and the counterfactual-value convention. That narrows the dispute to two unknowns. It does not resolve either in the Advocate's favor.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: the sensitivity run's central case (all-in cost $8.98M, about 2,381x, -22%) stays above the 2,000x bar and inside the 25% materiality threshold, so only the tail crosses.

- **The run's central case embeds an assumed discount.** It corresponds to D of about $1.98M, which is the Quantifier's discounted case. That case assumes government and Global Fund money is valued at 20–30% of face value. The Quantifier flags this as "my assumption," and the Advocate agrees the extent is "unknown, so I cannot give a defended number."
- **The Advocate's "central" and "tail" labels depend on that same unknown.**
  - At full face value, the Advocate concedes the bar is crossed at D above $3.7M, about $1.12 per patient.
  - On the face-value branch, even the cheapest end of the $1–10 range gives D of about $3.3M, which is right at break-even.
  - The Advocate's "tail" is therefore the default if CG counts others' money fully.
- **Even the discounted branch crosses the bar at mid-range procurement.**
  - The benefit-equivalent is 3,055 × 7 ≈ 21,384.
  - At the Advocate's 25% valuation and the range midpoint of $5.50 per patient, gross D is about $18.2M and D_eff is about $4.5M.
  - SROI is then about 21,384 / 11.5 ≈ 1,860x, below 2,000x.
- **The Advocate's threshold is mischaracterized.** The Advocate says the crossing threshold of about $4.5 per patient, derived from D above roughly $14.8M, sits "only in the upper half of the Quantifier's own $1–10 range." On a linear scale, $4.48 is below the $5.50 midpoint. It is only in the upper half on a log scale, which the Advocate does not invoke.
- **The 22% decline is close to the materiality line.** It is a point estimate under an unsourced 20–30% discount. A slightly lower discount rate of 25–30% moves it to or across 25%. At the discount rate the Advocate cites as central, the margin to materiality is only about 3 percentage points.
- **Minimum defensible magnitude.** If CG heavily discounts others' money and monitoring piggybacks on existing visits, the effect is about -5% (the run's low case of 2,890x). If neither holds, it is about -65% (the run's high case of 1,059x). The sensitivity run itself spans both outcomes, so the central case is not tightly identified.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: unvalued benefit channels, possible downstream savings, and absence of cost-side double counting offset or bound the concern.

- **Unvalued benefit channels.** These are zero in the model, so they offset nothing in the computed SROI. They are unquantified upside that the Advocate says "could easily outweigh" a few million dollars. "Could easily" with no size is not a quantified offset. The parameter map's own phrasing is that the estimate "could be robust" under a hypothetical, not that it is.
- **Downstream savings (fewer retreatments, less post-TB lung care).** The Advocate admits "I cannot size it from the evidence package." They are conditional on efficacy and the model does not capture them.
- **No double counting.** I accept this. D should scale with the 3.3M uptake-adjusted figure rather than 5.5M. It confirms the Quantifier's range is not inflated, but it is not an offset.
- **Net.** None of the claimed offsets is in the model or quantified. The only offset that is real and arithmetically defined is the possible discount on government money. That is the unstated convention, which the Advocate itself calls a "legitimate documentation gap."

**KEY UNRESOLVED QUESTIONS:**
- **Valuation convention.** Does CG value government and Global Fund TB spending at face value, at a discounted counterfactual value, or at zero? The Advocate concedes this is decision-relevant and the BOTEC does not say.
- **Incremental monitoring cost.** Does adding atorvastatin to a TB regimen require monitoring beyond existing visits (liver function, drug-interaction management, dose adjustment)? Neither side has sourced an answer.
- **Actual procurement price.** What is the actual LMIC procurement price per 6-month course at the doses used in the trial? The thread's $1–10 range is unverified.
- **Timing of D.** Does D enter only in the success state, since adoption follows a positive trial? If so, an expected D of about 40% of gross would shrink the effect. This cuts in the Advocate's favor and the model does not state it.
- **Cohort definition.** Is 3.3M the right cohort for D under the one-year-speedup framing, or only the incremental accelerated-year cohort? The Advocate asserts the latter is a real cost but does not size it.

### Judge Audit
Surviving strength: moderate
Justification: The Challenger made grounded, arithmetically transparent arguments that the Advocate's "tail" framing could not withstand:
- The face-value branch crosses at the low end of the price range.
- The 25%-valuation midpoint case gives about 1,860x.
- The "upper half" claim was a mischaracterization.
The Advocate's main offsets (unvalued benefits, downstream savings) were unquantified and rightly discounted. However, the critique's magnitude still rests on an unverified convention and an unverified price range. An obvious, unapplied adjustment (weighting D by the 40% success probability, with the verifier's shorter 2–4 month course) could cut the effect roughly in half. The critique is therefore not shown to be decision-changing.
Recommended action: 1. **CONCLUDE NOW:** The structural asymmetry is valid, with high confidence. An "all-in" SROI that credits benefits to every treated patient should either include delivery cost or explicitly state that third-party health-budget spending is excluded or discounted, and at what rate. The quantitative claim that SROI falls to roughly 1,000–1,250x is not established, with moderate confidence.

2. **SPECIFIC INVESTIGATION:** Re-run the BOTEC with three changes. This is feasible immediately with existing inputs:
   - Weight D by the 0.4 success probability.
   - Use the verifier's 56–112 tablet course at $1–6 instead of 180 tablets.
   - Report SROI at face value and at 25% valuation.

   The result will show whether the 2,000x bar is crossed under plausible procurement-only costs. If it is not, the critique reduces to a documentation gap plus an open monitoring-cost question.
Action feasibility: actionable_now
Advocate failures: ['false_definitiveness: The Advocate says "The bar is crossed only in the tail" and calls the high case "a tail scenario, not a central one." Yet it concedes that at full face value any D above about $1.12 per patient crosses the bar. It also concedes that ~$10M gross D (about $3 per patient) yields 1,000–1,250x and that it "cannot rule out" this outcome. The "tail" label holds only under an unstated discount the Advocate admits it "cannot give a defended number" for. The Advocate\'s self-assessment of "strong" also contradicts its own "Partial defense" heading. The judge rates the defense as partial at best.', 'unsupported_estimate_pseudo: The Advocate says a crossing threshold of about $4.5 per patient "sits only in the upper half of the Quantifier\'s own $1–10 procurement range." On a linear scale, $4.48 is below the $5.50 midpoint. The characterization does not follow from the numbers, and the Challenger correctly caught it.', 'unsupported_estimate_fabricated: The back-calculation assumes "6 months is about 180 daily tablets" with no source. The verifier package says the trial regimens were 2 months or 16 weeks, about 56–112 tablets. The error happens to work against the Advocate: a shorter course means a lower D. It is still an ungrounded input that contradicts the evidence on hand.', 'call_to_ignorance: The Advocate says the zero-valued benefit channels "could easily outweigh a few million dollars of delivery cost, but the size is unquantified." Naming the gap is fine. "Could easily outweigh" fills that gap with an asserted magnitude.', 'sound_synthesis_noted: The break-even reconstruction (3,055 × 7 / 2,000 = 10.7M; minus 7M = 3.7M; ÷ 3.3M ≈ $1.12) matches the verifier. The note that D scales with the 3.3M uptake-adjusted figure rather than 5.5M is correct and useful.']
Challenger failures: ['strawmanning: The Challenger says "The verifier evidence does not support delivery being free" and refers to "the Advocate\'s zero-incremental-cost scenario." The Advocate said incremental D would be "closer to procurement alone" if monitoring piggybacks. It did not say delivery is free, and it explicitly called this a conditional argument.', 'strawmanning: The Challenger says "If a simplified illustration is exempt from the omission critique, then no BOTEC can be critiqued." The Advocate did not claim exemption. It said the omission is weak evidence about the full grant analysis, and it acknowledged it "cannot show CG did consider delivery costs.', 'unsupported_estimate_pseudo: The Challenger says "A slightly lower discount rate of 25–30% moves it to or across 25%." This is internally garbled. Valuing money at 25–30% instead of 20–30% raises D_eff, so "lower discount rate" is ambiguous. No computation shows the resulting decline reaching 25%. The "~3 percentage points" margin is correct arithmetic. The claim that it is crossed is not derived.', 'unsupported_estimate_fabricated: The Challenger calls delivery cost "the largest recurring cost" with no support. This is minor.', "sound_synthesis_noted: The midpoint calculation is transparent and correct, conditional on its stated inputs. Those inputs are the Advocate's/Quantifier's 25% valuation and the $1–10 midpoint. The steps are 3,055 × 7 ≈ 21,384; gross D ≈ $18.2M; D_eff ≈ $4.5M; SROI ≈ 21,384 / 11.5 ≈ 1,860x. The face-value point is also sound: the low end of the range (D ≈ $3.3M) sits at break-even. The pharmacology points (hepatotoxic co-regimen; rifampicin as a CYP3A4 inducer with atorvastatin as a substrate) are correctly labelled as uncited and used only to show the piggyback assumption is ungrounded. That is a proper conditional use. Raising the success-state timing point, which cuts against the Challenger's own side, was good-faith engagement."]
Debate resolved: Both sides agree on three points:
- The BOTEC credits benefits to all 3.3M treated patients with no delivery-cost term.
- At full face value, break-even is about $1.12 per patient, so even the cheapest end of the plausible procurement range reaches the 2,000x bar.
- The Advocate's claim that crossing happens "only in the tail" holds only if CG heavily discounts third-party money. Under a 25% valuation, mid-range procurement still crosses the bar.

The question narrows to two unknowns. The first is the valuation convention for government and Global Fund money. The second is incremental monitoring cost.
Debate unresolved: Three questions remain open:
- Neither side established CG's valuation convention for third-party money or whether atorvastatin adds monitoring beyond existing TB visits.
- The success-state point was raised but never applied. If adoption cost should be weighted by p = 0.4, the face-value break-even rises to about $2.80 per patient, which could substantially shrink the effect.
- The correct cohort under the speedup framing was not tested.

--- Critique: Regulatory, pharmacovigilance and dissemination costs for an off-patent drug have no obvious payer, and the $7M likely under-budgets them ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: Regulatory, pharmacovigilance and dissemination costs for an off-patent drug have no obvious payer, and the $7M likely under-budgets them
```

**EXISTING COVERAGE:**

1. CG's $7M is explicitly described as including "later Phase III trials, guideline changes, dissemination and validation." The CEA Parameter Map lists this under what CG already accounts for. The critique therefore challenges the size of an included category, not an omitted one.
2. CG computes SROI on all-in costs and all-in benefits, not on its own 4.5% share. Any funder-agnostic cost, whoever ends up paying, is already supposed to be in the denominator. "No obvious payer" is a question about who pays, and CG's framing makes that irrelevant to the SROI.
3. The pharmacovigilance and monitoring component overlaps with Critique 1, as the Quantifier concedes. Delivery and monitoring cost should be evaluated once, in that critique. This one has to stand on guideline, dissemination and regulatory costs alone.

**EVIDENCE WEAKNESSES:**

1. The Quantifier labels the size of the shortfall UNGROUNDED and says the $5–20M figure has "no empirical basis." It also says the direction is uncertain and that "likely under-budgets" should not be asserted. The title nonetheless asserts it. On the critique's own terms, the quantitative claim has not been established.
2. The one concrete citation is the ATORTUB registry entry, which says Phase III will be "fully international and multicenter." That supports a Phase III that is large, but not that it exceeds CG's budget. The $7M has no published breakdown, so the registry entry cannot be compared against any line item. The statement that Phase III "is likely to take a large share of $7M" is an inference with no cost source behind it.
3. The Quantifier says it did not pull Unitaid or Global Fund documents. No evidence is offered that adoption-stage costs for off-patent drugs are large, or that no one pays them.
4. The verified atorvastatin hepatotoxicity point is real, but it is mainly a concern about effect size and net benefit. That belongs to relative_reduction and Critique 1, not to the size of regulatory or dissemination spending. No source links it to a specific cost line.
5. I cannot cite a source for the typical cost of WHO guideline development or of post-marketing surveillance for a new indication of an established drug. I treat my own sense that these are modest relative to a multi-country Phase III as an uninformed prior. The critique's opposing sense is equally ungrounded, so the question stays open.

**MAGNITUDE CHALLENGE:**

1. The bar-crossing arithmetic follows from the CEA. The published numerator is about $OP 53.5B × 40% ≈ $21.4B. Dividing by the 2,000x bar gives a breakeven all-in cost of about $10.7M. That is +$3.7M (+53%) over $7M.
2. The Quantifier's own central case is a $8.5M all-in cost, giving SROI ≈ 2,516x, which is −17.6%. That is above the 2,000x bar and inside CG's ~25% materiality band. The "material" rating rests only on the high case (SROI ≈ 1,782, implying roughly $12M). That case is built from the ungrounded $5–20M range.
3. The "low" case in the sensitivity table raises SROI by 7.7%. The Quantifier's own range is therefore two-sided, which fits a "direction uncertain" finding better than a "likely under-budgets" headline.
4. The $5–20M add-on is described as an illustration "with no empirical basis." A defender should not substitute a counter-number, and I do not. I note only that the +70–300% range was chosen without a reference class.

**OFFSETTING FACTORS:**

1. **Counterfactual cost.**
   - CG credits the grant with a 1-year acceleration, not with creating adoption. If Phase III, guideline and dissemination spending would occur anyway, only later, the marginal cost of the speedup is lower than $7M.
   - Putting the whole $7M in the denominator against only one year of acceleration benefit may already overstate the cost.
   - This is conditional on the counterfactual pathway existing, which the Parameter Map says CG does not examine. If it holds, additional adoption costs mostly shift in time rather than add to cost.
2. **Omitted benefits.** CG values only on-treatment mortality. The Parameter Map lists morbidity DALYs (the lung-damage finding), post-treatment mortality, transmission averted and diagnostic value as implicit zeros. These are the stated direction of error opposite to the cost concern. A cost under-budget of tens of percent is of the same order as the potential upside from these channels, which are also unquantified.
3. **Cheap adoption.** The adoption story relies on a generic, cheap drug with no new product to register or procure. That plausibly lowers regulatory and dissemination costs relative to a novel drug. The critique's "no commercial payer" point cuts both ways, because a generic drug also has none of the commercial overhead.
4. **No double counting.** The delivery and monitoring portion belongs to Critique 1. Stripping it out reduces this critique's scope to guideline and dissemination costs.

**OVERALL ASSESSMENT: Partial defense**

- The critique has no grounded magnitude and no stated direction. Its own central case stays above the bar and inside the 25% band.
- The vulnerability is real but thin. The $7M has no published breakdown, and the breakeven headroom is only about +53%. A multi-country Phase III alone could plausibly take much of that headroom. I cannot show this is not the case.
- I rate this partial rather than strong because the absence of any CG cost decomposition means the $7M is an assertion I cannot defend on its numbers. I rate it partial rather than weak because the critique itself concedes that its quantification is ungrounded.

**CONCESSIONS:**

1. CG gives no breakdown of the $7M and no reconciliation with typical TB Phase III costs. I cannot demonstrate the figure is adequate.
2. The headroom to the 2,000x bar is only about $3.7M. An unmodelled adoption cost of that size would erase the margin.
3. The "no obvious payer" point is valid as a risk to adoption. If no one funds guideline work or surveillance, the uptake or timing assumptions are at risk, not just the cost.
4. The Phase III registry description suggests the international trial is large. Its cost, relative to the $7M, is unknown to me.
5. The most defensible form of the critique is a request for a budget breakdown. A claim that the budget is "likely" too low is not supported by any cited evidence.

### Challenger
REBUTTAL: Regulatory, pharmacovigilance and dissemination costs for an off-patent drug have no obvious payer, and the $7M likely under-budgets them

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: CG's $7M already names Phase III, guidelines, dissemination and validation, and CG computes SROI on all-in cost, so "no obvious payer" is irrelevant to the denominator.

1. **Concede:** the categories are included. This critique cannot claim an omission, only inadequacy of the amount.
2. **Inclusion is not adequacy.** The Advocate concedes CG gives no breakdown of the $7M and no reconciliation with typical TB Phase III costs. Naming a category inside a lump sum, with no line items, does not show that the lump sum covers it. The Advocate's own phrase is that the $7M is "an assertion I cannot defend on its numbers."
3. **"Funder-agnostic denominator" only works if someone estimated the full cost.** If the estimate was made for the trial and the non-trial items were added loosely, the framing does not rescue it. The "no payer" point matters because it makes it more likely that unfunded items were left out of the estimate, not just that nobody pays them.
4. **Concede:** the monitoring and pharmacovigilance overlap with Critique 1 should be scored once. What remains here is guideline, dissemination and regulatory cost, plus Phase III scale.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the registry entry shows only that Phase III is large, not that it exceeds the budget. The shortfall is ungrounded, Unitaid and Global Fund documents were not pulled, and hepatotoxicity bears on effect size rather than cost.

1. **Concede:** the shortfall magnitude is ungrounded. I cannot cite a cost for WHO guideline development, post-marketing surveillance, or a multi-country TB Phase III. I treat any figure I could offer as an uninformed prior and will not offer one.
2. **Concede:** "likely under-budgets" in the title overreaches. The verifier did not mark any cost claim verified, only the hepatotoxicity point and the registry description.
3. **The registry evidence is a verified fact, not a number.** Phase III is described as "fully international and multicenter," and the entry is a pilot of that Phase III. The Advocate says it cannot be compared to a line item. That is true, and it cuts both ways: without a breakdown, the evidence cannot show adequacy either. The residual claim is modest: the headroom is thin relative to a trial of the described scope, and CG has not shown otherwise.
4. **Hepatotoxicity is partly a cost issue, conditionally.** The Advocate files it under effect size. If atorvastatin is the statin most often linked to liver injury (verified) and anti-TB drugs are also hepatotoxic, then pharmacovigilance and liver monitoring for the combined regimen are plausibly a specific cost driver. The verifier did not test whether this drives cost, so it is a conditional. It also falls inside the overlap with Critique 1, so I do not score it separately here.
5. **The missing Unitaid and Global Fund documents are a gap in the critique, not evidence for GiveWell.** Their absence leaves the question open, as the Advocate says in its point 5.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: the central case ($8.5M, SROI ≈ 2,516) stays above the 2,000x bar and within ~25%. The low case is +7.7%, so the range is two-sided, which fits "direction uncertain."

1. **Concede:** the arithmetic is right. Breakeven is about $10.7M, which is +$3.7M (+53%). The central case does not cross the bar.
2. **The range is not two-sided in any meaningful sense.** I back out the sensitivity cases from the table:
   - Baseline 3,054.857 = $21.384B / $7M.
   - Low 3,289.846 / 3,054.857 = 1.0769 = 7 / 6.5, so the low case is $6.5M, which is −$0.5M.
   - High 1,782 = $21.384B / $12M, so the high case is +$5M.
   - The Quantifier's own range runs −$0.5M to +$5M, roughly 10:1 skew. This follows from the Quantifier's inputs, which are themselves illustrative. It does not prove the direction.
3. **There is a structural reason for skew that does not depend on the $5–20M number.** The downside is bounded by whatever the $7M already allots to these items, which is unknown but cannot exceed $7M. Unfunded items have no cap. That does not show the budget is short, but it explains why "direction uncertain" understates the asymmetry.
4. **Minimum defensible magnitude:** nothing can be defended below about $0.5M of savings, and the credible downside is the $1.5M gap between $7M and the central $8.5M. This is below threshold and within the materiality band. I concede the "material" rating depends on the high case. The finding is a threshold-proximity risk, not a demonstrated crossing.
5. **Convexity.** SROI is proportional to 1/cost, so symmetric cost error produces larger SROI swings on the upside of cost than on the downside. Over a 20% error, for example, the SROI change is about +25% versus −17%.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: (1) the counterfactual means adoption costs would occur anyway, only later; (2) omitted benefits offset the cost risk; (3) a generic drug has lower regulatory and dissemination overhead; (4) there is no double counting once Critique 1 is stripped out.

1. **Counterfactual offset conflicts with the Advocate's own Concession 3.**
   - Concession 3 says that if no one funds guideline work or surveillance, uptake or timing is at risk.
   - Offset 1 assumes the same spending happens anyway.
   - If a payer exists, the cost is a real denominator item. If none exists, the counterfactual adoption assumption weakens.
   - The Advocate also concedes CG does not examine this pathway, so the offset is not in the model.
2. **Omitted benefits are real offsets at the SROI level.** CG's implicit zeros for morbidity, post-treatment mortality and transmission are in the Parameter Map. But they are unquantified and sit on a different parameter. They do not show the $7M is adequate. They show that SROI may be understated overall, which is a separate question.
3. **"Cheap generic, lower overhead" is ungrounded.** The Advocate offers no source. I cannot ground the opposite either, so this offset cannot be credited. It is a symmetrical prior.
4. **Concede offset 4:** scope should be reduced to guideline, dissemination and regulatory cost.

**KEY UNRESOLVED QUESTIONS:**
- What does the $7M contain by line item, and what Phase III scale does it assume? A breakdown from CG would resolve most of this critique.
- Does the pharmacovigilance or liver-monitoring requirement for a hepatotoxic drug used alongside anti-TB therapy sit in this critique or in Critique 1? It should be scored in only one.
- If no payer exists for guideline change and dissemination, does adoption proceed at all, and on what timeline? This would test whether the counterfactual offset or the "no payer" risk is correct.
- Where is the actual boundary? The headroom is $3.7M. Whether non-trial costs reach it is not answered by anything in this debate.

### Judge Audit
Surviving strength: weak
Justification: The debate was relatively productive, with sound syntheses on both sides and many explicit concessions. What it produced was mostly the dismantling of the critique's quantitative claim. The Challenger conceded that:
- the magnitude is ungrounded;
- the title overreaches;
- the central case stays within the band;
- the "material" rating rests only on the ungrounded $5–20M high case.
The Challenger's remaining arguments for upward skew rely on calls to ignorance ("unfunded items have no cap," "CG has not shown otherwise"), not on evidence. What survives is a valid transparency concern: there is no breakdown of the $7M, and headroom is only $3.7M. That concern does not demonstrate an under-budget.
Recommended action: 1. **CONCLUDE NOW** (moderate-high confidence):
   - Downgrade this critique from "likely under-budgets" to "unverified budget adequacy with thin threshold headroom ($3.7M, +53%)."
   - Drop the $5–20M illustration from any quantified adjustment.
   - Move all monitoring and pharmacovigilance cost to Critique 1.
   - Record the residual as a request to CG for a line-item breakdown of the $7M, including the assumed Phase III sample size and number of sites.
   - Do not apply a cost adjustment to the CEA on the basis of this critique.

2. **Optional targeted follow-up** (feasible with existing tooling):
   - Pull public award amounts for comparable publicly funded TB repurposing trials, such as the EDCTP2 StatinTB grant on CORDIS and other EDCTP/NIH multi-country TB Phase III awards.
   - Use these to benchmark whether a "fully international multicenter" Phase III plausibly consumes most of the $7M.
   - Only a benchmark above roughly $6M for the trial alone would revive the critique's directional claim.
Action feasibility: actionable_now
Advocate failures: ['sound_synthesis_noted: Breakeven derivation: numerator ≈ $OP 53.5B × 40% ≈ $21.4B, divided by the 2,000x bar, gives ≈ $10.7M, or +$3.7M (+53%) headroom. Each step is shown, and the Challenger accepted it.', 'unsupported_estimate_pseudo: Magnitude Challenge 3 says the low case is +7.7% SROI, so the Quantifier\'s range is "two-sided" and fits "direction uncertain." Backing out the cases shows −$0.5M against +$5M in cost. Calling a roughly 10:1 skewed range "two-sided" does not support the inference drawn from it. The Challenger exposed this gap correctly.', 'unsupported_estimate_fabricated: Offset 2 says "A cost under-budget of tens of percent is of the same order as the potential upside from these channels, which are also unquantified." This asserts a magnitude equivalence for channels the Advocate admits are unquantified.', 'whataboutism: Offset 2 answers a cost-adequacy critique by pointing to omitted benefits on a different parameter. That bears on overall SROI, not on whether the $7M covers adoption costs. The Challenger correctly called it "a separate question.', 'call_to_ignorance: Offset 3, "Cheap adoption," says a generic drug "plausibly lowers regulatory and dissemination costs." No source is given. It is offered as an offset even though Evidence Weakness 5 had already conceded such priors are uninformed.']
Challenger failures: ['sound_synthesis_noted: Backing out the sensitivity cases is correct:', 'sound_synthesis_noted: The convexity point (SROI ∝ 1/cost, so ±20% cost error gives about +25% / −17% SROI) is arithmetically correct and relevant to threshold proximity.', 'call_to_ignorance: Magnitude response 3 says "The downside is bounded… Unfunded items have no cap." This is trivially true but says nothing about the actual distribution of costs. It uses the absence of an upper bound to suggest upward skew. The Challenger partly hedges ("does not show the budget is short") but still uses it to argue that "direction uncertain" understates the asymmetry.', 'call_to_ignorance: Existing Coverage response 3 says "no payer… makes it more likely that unfunded items were left out of the estimate." This speculates about how CG built the estimate, with no evidence about that process.', 'call_to_ignorance: Evidence Weakness response 3 says that without a breakdown the registry "cannot show adequacy either… CG has not shown otherwise." This shifts the burden. Absence of a breakdown becomes support for "headroom is thin relative to a trial of the described scope," a scope that has no cost attached.', 'unsupported_estimate_pseudo: Magnitude response 4 calls "the $1.5M gap between $7M and the central $8.5M" the "credible" increase. The $8.5M central case comes from the same ungrounded illustrative inputs the Challenger conceded. Calling it "credible" gives it more standing than it has.']
Debate resolved: Both sides agree on five points:
- The $7M explicitly includes Phase III, guideline and dissemination costs, so the critique is about adequacy, not omission.
- No cost component of the shortfall is grounded, and "likely under-budgets" overreaches.
- Breakeven is about $10.7M, giving +$3.7M headroom.
- The Quantifier's central case ($8.5M) stays above the 2,000x bar and inside the materiality band.
- Monitoring and pharmacovigilance costs belong to Critique 1.

The debate also established that the illustrative sensitivity range is right-skewed (−$0.5M / +$5M), not two-sided. That skew comes from illustrative inputs and does not demonstrate the direction of error.
Debate unresolved: Whether the non-trial adoption costs plus a fully international multicenter Phase III actually fit within $7M remains open. Neither side could cite any cost benchmark, and CG provides no line-item breakdown.

It is also unresolved whether the absence of a commercial payer threatens adoption timing, which would undercut the counterfactual offset. The verified EDCTP precedent bears on this question, but neither side raised it.

--- Critique: Reference-class check: TB Phase III trials, and the evidence package WHO may require, point to more than one trial ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: Reference-class check on all_in_cost (TB Phase III cost, multiple-trial requirement)

EXISTING COVERAGE:
- CG's $7M is explicitly all-in. It covers "later Phase III trials, guideline changes, dissemination and validation," not just the $320K Phase IIc. The critique does not claim CG omitted the Phase III. It claims CG's Phase III figure is too low.
- CG's SROI uses all-in costs against all-in benefits and does not credit itself only with its ~4.5% share. This already avoids understating cost by counting only CG's own contribution.
- The 40% p_success is meant to cover failure of both Phase II and Phase III. Some of the cost risk is therefore partly priced in, because many failed trials stop before the full Phase III budget is spent. This is a partial offset only, since the formula applies 40% to benefits and divides by the full $7M.
- CG did not break down the $7M, and I concede that below. But the BOTEC is a prioritisation tool, and a wrong cost input would be a calibration error, not a structural omission.

EVIDENCE WEAKNESSES:
1. **The cost evidence is not TB-specific in one place and not DS-TB-specific in the other.**
   - The €33.9M TB-PRACTECAL figure comes from a hospital-based drug-resistant TB trial.
   - The Mullard/JAMA ~$19M median comes from FDA-approved novel-drug pivotal trials.
   - The critique's own Evidence section concedes the first "probably overstates cost" for a DS-TB adjunct.
   - Neither datum describes a Phase III of a generic, off-patent, repurposed drug.
2. **Atorvastatin's development path differs from a novel drug's.** Its safety profile and manufacturing are already established, so a Phase III needs no new-compound toxicology, CMC, or dose-finding from scratch. This is a structural reason the $19M novel-drug median overstates cost. I cannot ground a specific discount, so I treat the direction as supported and the size as unquantified.
3. **The multiple-trial / IPD meta-analysis requirement is marked UNGROUNDED by the critique itself.** Taken conditionally: if WHO required several trials, cost would rise. But the only quantified departure from $7M is the Quantifier's own adjustment, which has no stated component build-up.
4. **The five named trials' budgets are also ungrounded.** The "more than one trial" claim therefore rests on nothing the Verifier could check.

MAGNITUDE CHALLENGE:
1. **The critique gives three inconsistent ranges.**
   - The hypothesis says $15–30M, giving 700–1,400x.
   - The mechanism says the reference class is $20–60M, giving 350–1,000x.
   - The sensitivity run uses a central of $20M, giving 1,069x.
   - The $20–60M range has a lower bound above the one non-TB-specific median cited ($19M), and no cited datum supports the upper end. Only the TB-PRACTECAL point (€33.9M) sits inside it, and the critique concedes that point likely overstates cost.
2. **The $20M central is close to the Mullard/JAMA median plus CG's other items.**
   - Derivation: $19M median + $0.32M Phase IIc + guideline/dissemination costs ≈ $20M.
   - That is the cost of a typical novel-drug Phase III, not a derived cost for this trial design.
   - The component that would justify moving above or below it is the endpoint choice, and the critique leaves that open.
3. **The critique's own best case for CG is a pragmatic trial using routine-care endpoints.** In its words, that case supports a total of about $30M and ~700x. That is odd because "cheap pragmatic design" should push cost down, not up. I read this as an arithmetic or labelling slip, and the logic does not support it.
4. **The $7M could plausibly be low-end but not wildly wrong for a pragmatic adjunct design.** I cannot ground a per-patient cost for pragmatic DS-TB trials. Treat this as an uninformed prior, not a rebuttal figure.

OFFSETTING FACTORS:
1. **Higher cost likely comes with a stronger evidence base.**
   - The parameter map notes that a cheap Phase III implies a surrogate endpoint and weaker mortality evidence.
   - If cost rises to $20M because the trial is powered on a clinical endpoint, p_success conditional on adoption, or the credibility of the 10% relative reduction, may improve.
   - The critique holds those parameters fixed while raising cost, so it takes the full downside without the linked upside.
   - I cannot quantify this offset.
2. **Benefit channels CG deliberately leaves at zero.** The parameter map lists morbidity DALYs, post-treatment mortality, transmission averted, and the diagnostic as implicit zeros. This offsets cost-side revisions in general, not this critique specifically, so treat it as secondary.
3. **Phase III costs are borne by other funders.** All-in costing already treats these as real costs. If CG's counterfactual is partly "someone else runs this trial anyway," the all-in framing overstates the cost CG should attribute to this grant. I note this as a direction, with no figure.

OVERALL ASSESSMENT:
**Partial defense.**
- The critique has merit. A $7M all-in figure covering a Phase III, guideline work and dissemination is thin against any cited TB or pivotal-trial benchmark, and CG gives no breakdown.
- The critique's numbers are overstated or poorly grounded. The reference classes are mismatched to a generic repurposed DS-TB adjunct. The multiple-trial requirement is ungrounded. The ranges conflict with each other.
- Even a modest move to $15M puts SROI around 1,400x, below the 2,000x bar. The decision-relevant question is therefore whether $7M can be defended as a pragmatic-trial budget, and the evidence I have does not settle that. I cannot rule out that $7M is too low.

CONCESSIONS:
- CG provides no breakdown of the $7M and no reconciliation with TB Phase III benchmarks. The parameter map already flags this.
- A Phase III on a mortality endpoint (6% baseline, 10% relative reduction) would likely need a large trial. I cannot ground its cost, but I expect it to exceed $7M. A $7M budget is credible only for a pragmatic or surrogate-endpoint design.
- The sensitivity run shows the SROI falls below the 2,000x bar at any all-in cost above about $10.7M ($7M × 3,055/2,000). That is a low threshold relative to the cited benchmarks.
- The critique correctly identifies all_in_cost as a material parameter that CG treats with less rigor than its size warrants.
```

### Challenger
REBUTTAL: Reference-class check on all_in_cost (TB Phase III cost, multiple-trial requirement)

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: CG's $7M is already all-in (Phase III, guidelines, dissemination), and the 40% p_success partly prices in cost risk because failed trials stop before the full Phase III budget is spent.

Response:
1. I concede that $7M is labelled all-in. The critique is that the figure is too low, not that components are missing.
2. The early-stopping offset does not apply to the cost in question. Phase III spending is incurred only after Phase II succeeds. An early-stopping discount therefore applies to Phase II failures and does not reduce the Phase III budget. The Advocate concedes the formula divides by the full $7M, so no such discount is in the model.
3. CG gives no breakdown of the $7M. The Advocate concedes this and concedes that "a wrong cost input" is still a wrong input. Calling it a "calibration error, not a structural omission" does not make it immaterial. The Advocate's own breakeven is about $10.7M ($7M × 3,055/2,000), only about 1.5× CG's figure. A calibration error of that size is decision-relevant at this bar.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the reference classes (TB-PRACTECAL, Mullard/JAMA) don't match a generic repurposed DS-TB adjunct. Atorvastatin has established safety and manufacturing, so there is a structural reason the novel-drug median overstates cost.

Response:
1. I concede the mismatch. The verifier's evidence package says TB-PRACTECAL "probably overstates cost" for a DS-TB adjunct. It also says the $19M median "is not TB-specific." I will not defend TB-PRACTECAL as a point estimate.
2. The "no new toxicology/CMC/dose-finding" argument is weaker than presented. Those costs sit in preclinical and Phase I development and in the regulatory package. The Mullard/JAMA figure is the cost of pivotal trials, which are driven mainly by sample size, sites, monitoring and follow-up. This is my own reasoning, not a sourced finding. Even so, the Advocate's stated discount mechanism mostly acts on costs outside the $19M figure.
3. The Advocate concedes that a mortality-endpoint trial (6% baseline, 10% relative reduction) "would likely need a large trial." Here is the implied size.
   - Using the standard two-proportion formula with α=0.05 two-sided and 80% power, the effect is 6.0% → 5.4%.
   - n per arm ≈ (1.96+0.84)² × (0.06×0.94 + 0.054×0.946) / 0.006² ≈ 7.84 × 0.1075 / 0.000036 ≈ 23,400.
   - Total n is therefore about 47,000.
   - $7M spread over about 47,000 participants is roughly $150 per participant, covering enrolment, follow-up and also guideline and dissemination costs.
   - The baseline and effect inputs come from the parameter map as cited by the Advocate. Cluster or enriched high-risk designs could shrink n. I cannot quantify that, but it would also change the effect being tested.
4. This turns the open question into a dilemma for CG's $7M.
   - If the trial is powered on mortality, $7M implies a per-patient cost that looks very tight.
   - If it is a surrogate or pragmatic trial to keep cost at $7M, CG's benefits still credit a 10% mortality reduction. The mortality evidence behind that benefit would then be weaker than the model assumes.
   - Either branch lowers SROI. The cost-up branch is the one in this critique.
5. On the Advocate's point that the multi-trial and IPD claims and the five trials' budgets are "ungrounded":
   - The verifier did not reject these claims. They are unverified, not contradicted.
   - The critique's central range does not depend on them, because $15–30M comes from a single-trial reference class.
   - I concede they should carry no weight in the central case and should stay as an upside-risk flag.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: the critique gives inconsistent ranges ($15–30M, $20–60M, $20M central), the $20M is just the novel-drug median plus CG extras, and the "cheap pragmatic → $30M, ~700x" statement is a slip.

Response:
1. I concede the ranges are inconsistent and the $20–60M upper end has no cited datum. I also concede the pragmatic-design sentence is muddled, since a cheaper design should reduce cost.
2. The inconsistency is in range width, not direction. All the numbers on the table put SROI below 2,000x:
   - The Advocate's own derivation of about $20M gives 1,069x (verified in the sensitivity output).
   - The Advocate's "modest" $15M gives about 1,400x.
   - The critique's high case is $40M, which is what the sensitivity output implies (3,055 × 7 / 534.6), giving 535x.
3. The minimum defensible position is that $7M holds only if all-in cost stays at or below about $10.7M. The Advocate offers no source for a pivotal DS-TB or adjunct trial at or below that figure.
4. The Advocate calls $7M "plausibly low-end but not wildly wrong" and then says this is an uninformed prior. That does not rebut the critique, because the default benchmark it has on hand ($19M) is nearly 3× CG's figure.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: higher cost likely brings a stronger evidence base and better p_success; benefit channels set at zero offset cost increases; other funders may run the trial anyway.

Response:
1. **Stronger evidence base.**
   - The Advocate admits this is unquantified.
   - It also works against CG's current design. The dilemma in point 4 above shows the cheap case brings a weaker-evidence penalty that CG's model does not apply.
   - A p_success uplift is only warranted if CG's current p_success assumes a weak design. If it assumes an adequately powered trial, no uplift is owed.
2. **Zero-valued benefit channels.**
   - The Advocate itself says this is general and not specific to this critique.
   - It is also unquantified and does not touch the cost parameter. It is not an offset to this specific cost-side finding.
3. **Counterfactual funding.**
   - This cuts both ways. CG's SROI uses all-in benefits against all-in costs and does not credit CG with its ~4.5% share, as the Advocate notes.
   - If someone else would run the trial anyway, the attributable benefits fall along with the cost. The ratio does not improve.
   - Applying counterfactuals to cost only would be internally inconsistent.
4. No offset is both quantified and present in the model.

**KEY UNRESOLVED QUESTIONS:**
- Is the planned Phase III a mortality-endpoint trial or a surrogate/pragmatic trial? This determines whether $7M is credible or whether the benefit side needs a haircut instead.
- What is the real all-in cost per participant for a pragmatic adjunct trial in DS-TB? Neither side could ground a per-patient figure.
- Can enrichment or cluster designs reduce the required n enough to bring a mortality-powered trial near $10.7M?
- Does WHO require a single trial or an IPD meta-analysis? This is unverified, not rejected, and matters only for upside risk.
- Does CG's 40% p_success assume an adequately powered trial? If so, does it implicitly assume a budget above $7M?

### Judge Audit
Surviving strength: moderate
Justification: The Challenger made grounded arguments the Advocate could not counter:
- the explicit sample-size derivation;
- the $10.7M breakeven, which the Advocate itself derived;
- the cost-vs-evidence dilemma.
The Advocate conceded that a mortality-powered trial likely exceeds $7M. The critique's specific quantitative claims did not survive intact: the $15–30M, $20–60M and $20M central figures conflict, and the multi-trial claim was dropped. Both sides misread the verifier package in ways that skewed the exchange. The Advocate ignored the cheap pragmatic-protocol evidence, and both missed the $48.9M datum. The direction (SROI down, likely below 2,000x if the trial is mortality-powered) survives, but the magnitude is not settled.
Recommended action: 2. SPECIFIC INVESTIGATION: Extract the per-participant cost from NCT05575518 and apply it to the required trial size. This is feasible with existing tooling: a re-read of one protocol document plus arithmetic.
   - First, resolve whether the £226,734 per-site figure covers all 436 patients. If it does, that is about £520 (about $660) per patient.
   - Mortality-powered case: about $660 × about 47,000 ≈ $31M. That alone puts SROI near 700x.
   - Surrogate-endpoint trial of a few thousand participants: well under $7M.
   - Also check CG's documentation for the intended Phase III primary endpoint and whether the 40% p_success and 10% relative reduction assume a mortality-powered trial.

   Interim conclusion, at moderate confidence: CG's $7M is consistent only with a pragmatic or surrogate design. Under a mortality-powered design, all-in cost very likely exceeds the $10.7M breakeven. The critique's $15–30M central range is directionally plausible but not derived.
Action feasibility: requires_specified_evidence
Advocate failures: ['misrepresenting_evidence_status: The Advocate wrote, "The $20–60M range has a lower bound above the one non-TB-specific median cited ($19M), and no cited datum supports the upper end." The verifier package does contain an upper-end datum: a TB-specific cost model with a mean of **$48.9M** for trials with an active-drug control arm. It also cites a systematic review range of US$7–221M per Phase 2/3 trial. The upper end may be poorly matched to this design, but it is not unsupported.', 'misrepresenting_evidence_status: The Advocate wrote, "I cannot ground a per-patient cost for pragmatic DS-TB trials. Treat this as an uninformed prior." The verifier package contains the EDCTP-funded pragmatic DS-TB protocol (NCT05575518). It lists £226,734 in a per-site budget table, stated for 436 patients per site, and the verifier explicitly read this as showing that pragmatic DS-TB trials can be much cheaper per patient. Other usable items were also in the package:', 'call_to_ignorance: Offsetting factor 1 says that if cost rises because the trial uses a clinical endpoint, "p_success conditional on adoption, or the credibility of the 10% relative reduction, may improve." This upside has no evidence behind it and is offered as a counterweight. The Advocate admits it is unquantified but still uses it to argue that the critique "takes the full downside without the linked upside.', 'strawmanning: The Advocate reads the critique\'s "If it holds, a central total of $30M" as saying a cheap pragmatic design implies $30M, and calls this a slip. In the mechanism, "it" plausibly refers to the reference class holding, not the counterargument. The critique is ambiguous, so this is a mild flag. The Challenger accepted the misreading without checking it.', 'sound_synthesis_noted: Two derivations are correct:']
Challenger failures: ['misrepresenting_evidence_status: The Challenger wrote, "The Advocate offers no source for a pivotal DS-TB or adjunct trial at or below that figure [$10.7M]." Under Key Unresolved Questions it added, "Neither side could ground a per-patient figure." The verifier package has a per-site pragmatic DS-TB budget (NCT05575518) and a systematic-review lower bound of $7M. The Challenger used the Advocate\'s failure to cite these as if the evidence did not exist.', 'misrepresenting_evidence_status: The Challenger conceded that "the $20–60M upper end has no cited datum." This repeats the Advocate\'s error and overlooks the $48.9M TB-specific model mean in the verifier package. The concession happened to cost the Challenger, but it still misstates the evidence base.', 'false_definitiveness: The Challenger wrote, "Either branch lowers SROI." The cost-up branch is quantified. The surrogate/pragmatic branch, a haircut to the mortality-benefit credibility, is asserted with no magnitude, yet it is presented as equally decisive. Its direction is plausible, but how far it lowers SROI, and whether that falls below 2,000x, is unknown.', 'sound_synthesis_noted: The sample-size calculation is correct and grounded in parameter-map inputs:']
Debate resolved: The debate established three things:
- CG's $7M all-in figure has no breakdown, and the SROI drops below the 2,000x bar at about $10.7M.
- An individually randomized trial powered on the 6%→5.4% mortality effect would need about 47,000 participants, implausible at $7M.
- So $7M is credible only for a pragmatic or surrogate design, and such a design weakens the evidence for the mortality benefit the model credits.

Both sides also agreed that the critique's ranges are internally inconsistent and that the multi-trial/IPD claim should carry no weight in the central case.
Debate unresolved: Two questions remain open:
- What a pragmatic DS-TB adjunct trial would actually cost per participant at the required n. Both sides overlooked the NCT05575518 figure that bears directly on this.
- If the trial is pragmatic or surrogate-based, how large the corresponding haircut to the 10% mortality reduction or p_success should be.

--- Critique: The speedup benefit and the all-in cost come from different counterfactuals. Every coherent framing gives roughly 10–20x higher SROI. ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION: Speedup benefit and all-in cost come from different counterfactuals

**EXISTING COVERAGE:**
- **Shared-credit convention.** CG's BOTEC credits itself ~4.5% of benefits against a ~4.5% cost share ($320k of ~$7M). Computing SROI on all-in benefits and all-in costs is a standard way to handle a multi-funder pathway.
  - If every funder whose money is necessary claims full counterfactual credit, the claims sum to more than 100% of the benefit.
  - Charging the whole pathway cost against the speedup benefit is a deliberate guard against that overcounting. It is a simplification, not an oversight.
- **Alternative attribution.** The one-year speedup can be read as a probability-weighted expected acceleration across worlds, not a literal one-year delay.
  - On that reading it already blends the delay and never branches.
  - I cannot ground the 1-year figure. I note only that the BOTEC does not claim it is the literal delay.
- **Nothing from the critique is "ignored" in a way that flips the decision.**
  - The critique concedes that its delay branch is ambiguous in direction.
  - Only the never branch reliably raises SROI, and that branch needs the claim that the pathway would not occur without the grant. The critique offers no evidence for that claim.

**EVIDENCE WEAKNESSES:**
1. The critique states "Evidence: None external." The 10–20x multiple is labelled UNGROUNDED by the critic. Everything rests on assumed r, an assumed horizon and an assumed delay factor.
2. **The headline ratio does not match either branch it claims to describe.** The critique's own text is as follows.
   - It says that if other funders' dollars cost only time value, a consistent framing gives PV_B/PV_C.
   - "Time value only" is the delay-world cost logic: other funders pay either way, just earlier.
   - PV_B (the full discounted benefit stream) is never-world benefit logic. In the delay world the benefit is a shift of the curve, not the whole stream.
   - So the 10–20x multiple pairs never-world benefits with delay-world costs. That is the same mismatch the critique charges to the BOTEC.
   - If the critique were applied consistently, each branch would give a different number.
     - Delay branch: one year of benefit against ~$320k plus time value.
     - Never branch: full stream against ~$7M valued at the bar.
   - Neither equals "BOTEC × 10–20".
3. The critique's own caveat undercuts the point estimate. It says the multiple "depends on horizon assumptions that I had to assume," and then reports a 30,000–55,000x range anyway, derived from that multiple.

**MAGNITUDE CHALLENGE:**
- **The 17 benefit-years figure is the infinite-horizon limit.** It is 1/(0.04 + 0.02) ≈ 16.7, which assumes atorvastatin-plus-standard-regimen benefits persist indefinitely.
  - I computed the finite-horizon annuity factor at 6% as (1 − 1.06^−N)/0.06.
  - N = 10 gives about 7.4. Multiplying by the critique's own 0.65 delay factor gives about 4.8 benefit-years.
  - N = 5 gives about 4.2, or about 2.7 benefit-years after the 0.65 factor.
  - So under a 5–10 year effective use window, the multiple is roughly 3–5x, not 10–20x.
- **Horizon is plausibly finite.** The critique itself lists regimen obsolescence and drug obsolescence as bounds.
  - The BOTEC's own parameter map flags that newer regimens, such as 4-month HPMZ, could change the room for adjunctive benefit.
  - It also flags vaccine or other incidence shocks.
  - I cannot ground a specific horizon.
- **The sensitivity run does not map onto the critique's mechanism.**
  - The run varies speedup_years linearly, from 0.5 (1,527x) to 15 (45,823x), and Quantifier central 5 gives 15,274x.
  - A discounted-benefit multiple is not equivalent to a longer speedup. A shift in a discounted curve yields roughly r × PV_B, not PV_B.
  - So the "high" and "central" rows are linear scalings, not a faithful encoding of the critique.
- **Only the low row crosses the bar.** The low row (−50%, 1,527x) is the only one that crosses ~2,000x. It reflects a speedup shorter than 1 year, which the critique's mechanism does not argue for.

**OFFSETTING FACTORS:**
1. **Recurring delivery costs scale with benefit-years.** A multiplier on benefits needs a matching multiplier on costs, because costs recur each year the drug is delivered.
   - The BOTEC's $7M covers trials, guidelines, dissemination and validation, but not recurring procurement, monitoring or health-worker time (parameter map, all_in_cost).
   - Using only BOTEC numbers, annual expected benefit is $OP 54B × 0.4 = $OP 21.6B, and treated patients per year are about 3.3M.
   - For the recurring ratio to stay at the ~2,000x bar, delivery cost must be below 21.6B / 2,000 / 3.3M ≈ $3.3 per treated patient. This assumes costs are valued at the bar, as the critique says other funders' money should be.
   - I cannot ground the actual per-patient delivery cost. If it is above ~$3, a coherent never-branch with delivery costs does not scale with benefit-years the way the critique assumes.
2. **No discounting is applied to an 8-year-delayed benefit.** The BOTEC applies none, which implicitly favours the estimate, and the critique's "delay factor" is the only place this is acknowledged. Discounting at 4% over 8 years gives 1/1.04^8 ≈ 0.73.
3. **Displacement is symmetrical.** The critique admits that charging other funders' money at CG's bar could drop the delay branch to near or below the BOTEC. The all-in framing is a rough stand-in for that charge, so it is not purely conservative bias.

**OVERALL ASSESSMENT:** Partial defense.
- The critique identifies a real conceptual mismatch. But its quantitative conclusion (10–20x, 30,000–55,000x) is ungrounded and rests on an infinite-horizon limit.
- Its own headline ratio mixes branches, and it omits recurring costs that scale with the benefit-years it multiplies.
- The BOTEC's all-in framing has a defensible rationale as a credit-sharing convention.
- The most that is supported is that the true SROI is probably not lower because of this issue, and may be higher. The size of the upward move is unsupported.

**CONCESSIONS:**
- The BOTEC does pair a speedup-type benefit with a full-pathway cost without reconciling the two. The parameter map confirms there is "no reconciliation of the speedup framing with the all-in cost framing."
- Direction is more likely upward than downward for the never branch. Under a long horizon, any coherent treatment of that branch gives a higher ratio than the BOTEC.
- The critique is right that the BOTEC does not reflect a deliberate choice among the counterfactuals, and CG does not explain the choice.
- I cannot ground a counter-estimate of the true multiple. The 3–5x finite-horizon figure above is a derivation from assumed horizons of 5–10 years, not an evidence-based estimate.

### Challenger
REBUTTAL: Speedup benefit and all-in cost come from different counterfactuals

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: charging the full ~$7M pathway cost against the speedup benefit is a deliberate shared-credit convention. CG takes ~4.5% of benefits against a ~4.5% cost share, and this guards against funders' claims summing to more than 100%.

Response:
- Shared credit works only if the numerator is the whole pathway's benefit. The BOTEC's numerator is one year of plateau deaths averted. That is already CG's marginal counterfactual contribution in the delay world, because other funders pay either way.
- Applying a share-of-credit convention on top of a marginal-attribution numerator penalizes CG twice. The >100% overcounting problem arises only in the never world, where each necessary funder claims the full stream. In that world the benefit is the full stream, not one year.
- So the convention cannot justify this pairing in either world.
- The Advocate's own concession that there is "no reconciliation of the speedup framing with the all-in cost framing" undercuts the claim that the choice was deliberate. The Advocate also grants that CG does not explain it.

> The Advocate claims: the 1-year figure can be read as a probability-weighted expected acceleration that already blends the delay and never branches.

Response:
- The Advocate says it cannot ground that reading, and I cannot either. Take it as true for the argument.
- A blended numerator then requires a blended denominator: roughly p × (~$7M valued at the bar) + (1−p) × (~$320k plus time value). The BOTEC charges the full $7M with certainty.
- The blended reading therefore repairs the numerator and leaves the denominator at its never-world worst case. That is the same mismatch, one level up.

> The Advocate claims: the never branch needs evidence that the pathway wouldn't occur without the grant, and the critique offers none.

Response:
- The critique does not need the never branch to be certain. Any p > 0 moves the expected ratio. The BOTEC's 1-year framing is itself an unevidenced assertion that p ≈ 0.
- Expected ratio relative to the BOTEC is (1−p)·D + p·N, where D is the delay-branch multiple and N the never-branch multiple.
- Illustration: D = 1, N = 3–5 (the Advocate's own finite-horizon range), p = 0.1. This gives 0.9 + 0.1 × (3 to 5) = 1.2–1.4x. This is my illustration, not a grounded estimate. The direction is upward and the size is modest unless p is large.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the headline PV_B/PV_C mixes branches, because "time-value-only" cost logic is delay-world logic while full-stream PV_B is never-world benefit logic.

Response:
- This conflates two separate choices. One is which world generates the benefit (delay or never). The other is how to value other funders' dollars (at time value only, or at CG's bar). The second choice is an opportunity-cost valuation. It is not tied to a branch.
- "Never-world benefit with other funders' money valued cheaply" is a coherent cell in the 2×2. It is the optimistic corner, and the critique labels it a conditional upper scenario.
- I concede the critique's text is loose. It states a 5–20x range in one place and 10–20x in another, and it blurs the cells. The Advocate is right that the 30,000–55,000x range should not be reported as a central figure.
- But that is a presentation defect. It does not remove the underlying mismatch, which the Advocate concedes.

> The Advocate claims: the multiple is ungrounded, and the critique's own caveat undercuts the point estimate.

Response:
- Agreed that the multiple is ungrounded. The critique says so, and the Advocate says the same of its own 3–5x.
- A derived range under stated assumptions is not "no evidence" in the sense that would warrant dismissal. The question is which horizon is more defensible, and neither side has grounding.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: 17 benefit-years is the infinite-horizon limit. With N = 5–10 years and the 0.65 delay factor, the multiple is about 3–5x.

Response:
- The N = 5–10 window is the Advocate's own assumption. The Advocate says it cannot ground a horizon. The critique's longer horizon is assumed too, so this is a contest of assumptions, not of evidence.
- The Advocate's own numbers (2.7–4.8 effective benefit-years) are not trivial. Using the sensitivity file's baseline of 3,055x and linear scaling in speedup_years, they give roughly 3,055 × 2.7 ≈ 8,200x to 3,055 × 4.8 ≈ 14,700x. This is the Advocate's derivation applied to the model, and it is the floor of the critique's case.
- That is a 2.7–4.8x upward revision in the never branch. It is a material revision of the point estimate even though it does not flip a decision, since the baseline of ~3,055x is already above the ~2,000x bar.
- A 5–10 year horizon sits awkwardly with the BOTEC's own 2% annual decline in cases. That decline implies a multi-decade stream. The Advocate's cited obsolescence risks are real but unquantified.

> The Advocate claims: the sensitivity run does not map onto the critique's mechanism, because a discounted shift yields r × PV_B, not PV_B.

Response:
- The r × PV_B point describes the delay branch, and the delay branch is what the BOTEC's 1-year figure already represents.
- In the never branch, benefit-years are the multiplier. BOTEC benefit is linear in years of annual benefit, so setting speedup_years equal to effective discounted benefit-years is a faithful encoding of that branch.
- The "central 5 → 15,274x" row therefore corresponds to the never branch at 5 effective benefit-years. That sits inside the Advocate's own range.
- I concede that the "high" row (15 years, 45,823x) is an infinite-horizon-style upper bound and should not be treated as a central case. I also concede that only the low row crosses the bar. That row is a shorter-than-one-year speedup, which the critique's mechanism does not argue for.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: recurring delivery costs scale with benefit-years. Delivery would need to cost under ~$3.3 per patient for the never-branch ratio to stay at the bar.

Response:
- This is the Advocate's strongest point, and I concede its structure. Coherent ratio ≈ N·B / (C + N·D). As N grows, this tends to B/D, which could be below the BOTEC if D is large.
- But the Advocate cannot ground D. A $3.3 threshold means nothing without a delivery cost. That makes this offset conditional, not demonstrated.
- The BOTEC's single benefit-year already omits delivery costs for that year's patients, since all_in_cost excludes procurement and health-worker time. So the omission is in the baseline too. A proper correction lowers both the baseline and the coherent ratio.
- In the delay branch, recurring delivery costs are incurred in both worlds and are not attributable to the grant. They matter only for the never branch.

> The Advocate claims: the BOTEC applies no discounting to an 8-year-delayed benefit, and a 4% rate over 8 years gives 0.73.

Response:
- This double-counts. The Advocate already applied the critique's 0.65 delay factor in the magnitude section, and that factor is the 8-year discounting. Counting it again as an offset overstates the correction.

> The Advocate claims: displacement is symmetric, and the all-in framing is a rough stand-in for charging other funders' money at CG's bar.

Response:
- If displacement were the rationale, CG would have written it, and the Advocate concedes CG did not explain the choice.
- As a stand-in, the all-in charge is a never-world cost applied to a delay-world numerator. It is correct only if displaced funding is valued at the bar and the benefit is full-stream. Under delay-world logic with a one-year numerator, the all-in charge does not approximate displacement.
- I agree this is the one place where the critique's delay-branch direction is genuinely ambiguous.

**KEY UNRESOLVED QUESTIONS:**
- What is the probability that the TB-statin pathway would not occur without CG's grant? The BOTEC implicitly sets it near zero. If it is above ~10–20%, the expected correction is non-trivial.
- What is a realistic effective-use horizon for adjunctive statins, given regimen change (such as 4-month HPMZ) and the BOTEC's own 2% annual decline in cases?
- What is the per-patient delivery cost D, and is it attributable to CG in the never branch? This determines whether the coherent ratio rises or falls relative to the BOTEC.
- What is the opportunity cost of other funders' money? At time value only, the coherent ratio is far above the BOTEC. At CG's bar, the delay branch is at or below it.
- Did CG deliberately choose the all-in cost framing for conservatism or credit-sharing? Neither the verifier nor the Advocate found anything on this.

### Judge Audit
Surviving strength: moderate
Justification: - **What survives.** The conceptual core survived. The Challenger's 2×2 decomposition and blended-denominator argument were grounded, and the Advocate effectively conceded them ("no reconciliation…", "CG does not explain the choice").
- **What does not survive.** The quantitative claim was substantially cut back. The Advocate's sound finite-horizon synthesis reduced 10–20x to about 3–5x. Its delivery-cost breakeven showed that even the never-branch direction is conditional on an unknown D, and the Challenger conceded both the structure and that the high row is not central.
- **Quality of the exchange.** Both sides produced real syntheses alongside several pseudo-derivations and overstatements. The result is a moderate verdict on a narrowed critique, not a strong one.
Recommended action: 1. CONCLUDE NOW, with moderate confidence. The BOTEC should acknowledge that its numerator and denominator come from different counterfactuals and present SROI conditionally:
   - **Delay branch:** one year of benefit against the incremental cost (about $320k plus displacement). This is possibly at or below the current figure if other funders' money is valued near CG's bar.
   - **Never branch:** full discounted stream against the full pathway cost plus recurring delivery costs.

   The 30,000–55,000x range should be dropped. Any upward revision should be reported as about 3–5x, conditional on a 5–10 year horizon and low delivery costs. The funding decision does not change, since the baseline already clears the bar.

   One cheap, feasible check should accompany this conclusion. Look up generic atorvastatin procurement prices for the relevant course length, plus incremental monitoring costs, in high-burden TB countries, and compare them against the ~$3.3 per-patient breakeven. This determines the sign of the never-branch correction and can be done with existing tooling.
Action feasibility: actionable_now
Advocate failures: ['false_definitiveness: The Advocate asserts that charging the whole pathway cost "is a deliberate guard against that overcounting. It is a simplification, not an oversight." Its own concessions then say there is "no reconciliation of the speedup framing with the all-in cost framing" and that "CG does not explain the choice." Deliberateness is asserted confidently and then conceded away. The 4.5%/4.5% credit-share point is a fair observation, but it does not show that the choice was intentional.', 'call_to_ignorance: The Advocate says the 1-year speedup "can be read as a probability-weighted expected acceleration across worlds… On that reading it already blends the delay and never branches." It then admits "I cannot ground the 1-year figure." This offers an unevidenced reading as a possible rescue. The Advocate is partly transparent about the gap, so this is a mild instance.', 'unsupported_estimate_pseudo: The Advocate lists "No discounting is applied to an 8-year-delayed benefit… 1/1.04^8 ≈ 0.73" as an additional offset. It had already applied the critique\'s 0.65 "delay factor" in its magnitude section, and that factor plausibly encodes the same lag. Presenting the 0.73 as a separate offset double-counts the lag adjustment.', 'false_definitiveness: Displacement is symmetrical… The all-in framing is a rough stand-in for that charge, so it is not purely conservative bias." This is asserted with no basis in the BOTEC. It conflicts with the Advocate\'s concession that CG did not explain its framing.', 'sound_synthesis_noted: The finite-horizon annuity calculation is sound:', 'sound_synthesis_noted: The delivery-cost breakeven is also sound:']
Challenger failures: ['unsupported_estimate_pseudo: The expected-ratio formula "(1−p)·D + p·N", illustrated as "0.9 + 0.1 × (3 to 5) = 1.2–1.4x", has two logical gaps.', 'strawmanning: The BOTEC\'s 1-year framing is itself an unevidenced assertion that p ≈ 0." Two sentences earlier, the Challenger accepted arguendo the Advocate\'s reading that the 1-year figure is a blended expectation. A blended expectation is precisely not p≈0. The Challenger is therefore rebutting a framing it had just set aside.', 'false_definitiveness: The Challenger calls the 8,200–14,700x range "the floor of the critique\'s case." That range scales benefits linearly and ignores recurring delivery costs and displacement. The Challenger itself later concedes that delivery costs could pull the never-branch ratio below the BOTEC. It cannot be a floor and also be conditional on an unknown D.', 'unsupported_estimate_pseudo: A 5–10 year horizon sits awkwardly with the BOTEC\'s own 2% annual decline in cases. That decline implies a multi-decade stream." A slow decline in TB incidence says nothing about how long adjunctive statins stay part of standard care. Regimen obsolescence is a separate horizon. The inference does not follow.', 'false_definitiveness: That factor is the 8-year discounting." The verifier said the 0.6–0.7 factor is UNGROUNDED and only "probably reflect[s] lag," so the Challenger states this more firmly than the evidence allows. The double-count objection is directionally right, but it is not established.', 'call_to_ignorance: If displacement were the rationale, CG would have written it." This treats CG\'s silence as evidence that displacement was not the rationale. Absence of documentation does not establish the rationale either way.', 'misrepresenting_evidence_status: A $3.3 threshold means nothing without a delivery cost." A breakeven threshold is informative precisely because D is unknown. It converts an open question into a checkable one.', 'sound_synthesis_noted: Two Challenger moves engage the substance well.']
Debate resolved: Both sides agree on four points:
- The BOTEC pairs a speedup-type benefit with a full-pathway cost without reconciling them, and neither the shared-credit nor the blended-reading rationale repairs the mismatch.
- The 30,000–55,000x figure must not be reported as a central estimate.
- Under a 5–10 year horizon with no recurring delivery costs, the never-branch upward revision is about 3–5x (roughly 8,000–15,000x).
- The decision is not flipped, because the baseline (~3,055x) is already above the ~2,000x bar.
Debate unresolved: The sign and size of the correction depend on four ungrounded parameters that neither side could pin down:
- the per-patient delivery cost relative to the ~$3.3 breakeven;
- the opportunity cost of other funders' money, which decides whether the delay branch sits above or below the BOTEC;
- the probability that the pathway would not occur without CG;
- the effective-use horizon given regimen change.

The Challenger's expected-ratio framing for combining the branches was also structurally flawed. A correct E[B]/E[C] blend was never computed.

--- Critique: The funding landscape for a generic-statin TB program makes "never" a live branch. The speedup is a poor proxy for the grant's real counterfactual. ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: The funding landscape for a generic-statin TB program makes "never" a live branch. The speedup is a poor proxy for the grant's real counterfactual.
```

**EXISTING COVERAGE:**

1. The 40% p_success is a catch-all for "Phase II and Phase III both succeed." The parameter map notes that CG does not define success or break out its components. So a Phase III that is never funded or run is plausibly already inside the 60% failure mass. This is arguable rather than explicit, and I do not claim CG stated it.
2. CG computes SROI on all-in costs ($7M) and all-in benefits, not on its 4.5% share. That framing already charges the full downstream cost of Phase III, guidelines and dissemination to the benefit stream. The "never" branch is not ignored. It is priced as a 1-year speedup against the full $7M.
3. The critique's own hypothesis says to "drop the 'SROI about 20× higher' claim" because it credits full downstream benefit against only the $320k grant cost. Its mechanism section still states the ~20× figure. The one large quantified upside is therefore withdrawn by the critique itself, and what remains is a directional argument with no estimate of q.
4. CG's text states an 8-year Phase III completion assumption. That implies Phase III is not yet funded or planned. The model is built on the premise that the grant is an early-stage step in a pathway that still needs a sponsor. It does not assume a funded Phase III is already waiting.

**EVIDENCE WEAKNESSES:**

1. **Absence of a registered Phase III is not informative here.** The critique says "I found no registered statin-TB Phase III trial… This is not exhaustive." Phase III trials are typically registered when launched or funded. CG itself assumes Phase III completes 8 years out, so none would be registered yet. The observation fits equally well with "a sponsor will appear after a positive Phase IIc." The critique concedes it could not confirm the gap.
2. **The 2026 review that HDT candidates need large Phase III trials supports the need for Phase III.** That is what CG's all-in cost and 40% joint success probability already assume. It says nothing about who will fund it, or whether anyone would fund it without this grant.
3. **The rosuvastatin null is the main added evidence, and its transfer to atorvastatin is unestablished.** The Verifier evidence presented does not say the null bears on atorvastatin or on the endpoints CG's Phase IIc tests (survival, clearance, lung damage, dosing). If the null is informative about the statin class, p_success should fall (conditional argument, accepted arguendo). I flag that rosuvastatin and atorvastatin differ in lipophilicity and CYP3A4 metabolism, which is general pharmacology and not a cited TB result. I cannot ground from the evidence package that this makes the null uninformative, so I treat that as an open question.
4. **The critique's "NIAID funded Phase 2b, therefore a Phase III sponsor may exist" and "no sponsor, therefore never" arguments point in opposite directions.** The critique labels the direction ambiguous. That is honest, but it means the evidence does not support moving speedup_years in a particular direction.

**MAGNITUDE CHALLENGE:**

1. **The Quantifier's two central values nearly cancel.**
   - SROI is linear in both parameters (sensitivity table).
   - Baseline: 1 year × 0.4 = 0.40.
   - Quantifier central: 1.25 years × 0.30 = 0.375.
   - Ratio: 0.375 / 0.40 = 0.9375, so SROI ≈ 3,054.9 × 0.9375 ≈ 2,864.
   - That is a ~6% decrease, well under the ~25% materiality threshold and still above the ~2,000× bar.
   - Individually the Quantifier shows +25% (3,818.6) and −25% (2,291.1). Applied together, as the critique's own mechanism implies, they do not move the conclusion.
2. **Neither central value is derived.** The critique says the speedup distribution "depends on an unestimated q." The Quantifier's 1.25 and 0.3 therefore have no inspectable chain from the evidence. I cannot ground a counter-value either, so I do not offer one. This is a point about how much weight the critique's central values can carry, not a claim that they are wrong.
3. **A distribution over the speedup adds nothing beyond its mean.** The formula is linear in speedup_years, so only E[speedup] enters SROI. The critique's "model it as a distribution" point collapses to "is the mean above 1?", which depends entirely on q.
4. **The "never" branch cannot be taken at face value.** A literal never-branch gives an unbounded speedup. The critique's high case (3 years, +200%, 9,164.6) is an illustrative scenario, not an estimate. CG applies no time discounting, which already favors long-horizon benefits. A longer speedup would also shift benefits to later incidence. At CG's 2% annual decline, a 0.25-year shift costs about 0.98^0.25 ≈ 0.995, which is negligible. It would not be negligible for a multi-year speedup.
5. **The speedup and p_success adjustments are plausibly negatively correlated.** This is logic-only and I cannot ground it empirically. If the reason no sponsor would fund Phase III is funders' informed skepticism about efficacy, then the states of the world with a high speedup are also those with a lower probability that the drug works. Raising speedup and cutting p_success independently may overstate the swing. Conversely, if the gap is only a market failure for generics, the correlation disappears. The critique does not distinguish these.

**OFFSETTING FACTORS:**

1. The critique acknowledges the downside branch. If an existing, adequately funded statin-TB trial makes the grant redundant, then q ≈ 0 and D ≈ 0 and the speedup falls toward zero. The critique does not estimate the weights of up and down branches, so the net direction is unsigned.
2. The rosuvastatin null reduces p_success by the critique's own account, and it offsets the speedup gain, as computed above.
3. A "never" counterfactual also means the full $7M all-in cost is incurred only because of this program. CG's current framing already treats it that way, so no additional cost correction is needed. But any move to a "seed funder" framing needs a matching treatment of the denominator, which is the accounting conflict with Critique 2 that the critique flagged.

**OVERALL ASSESSMENT:** Partial defense.

- On materiality, the defense is fairly strong. The critique's own centrals (speedup 1.25, p_success 0.3) net to about −6% (≈2,864×), the ~20× claim is withdrawn, the direction is declared ambiguous, and q is unestimated.
- On parameter justification, the defense is weak. CG gives no basis for "1 year" (parameter map: "No justification for 1 year"), and the counterfactual funding landscape is a legitimate unmodeled uncertainty.
- The critique does not show that the estimate is wrong. It shows that the speedup parameter has no stated derivation and could plausibly move either way.

**CONCESSIONS:**

1. CG's 1-year speedup is asserted, not derived. A more realistic treatment would put a distribution over the counterfactual timeline, including a no-Phase-III branch. The expected speedup could plausibly exceed 1 year. I cannot rule this out.
2. If the rosuvastatin null is informative about atorvastatin, a p_success below 0.4 is defensible. The critique's direction on that parameter is reasonable, though the magnitude (0.3) is not derived.
3. The 40% figure carries no stated reference class, so I cannot show that it already prices the "never funded" branch. My claim that it does is arguable, not established.
4. The critique correctly notes that the all-in framing and a "grant-marginal" framing are not interchangeable. CG's use of all-in benefits against all-in costs while crediting only a 1-year speedup is internally ambiguous about what the counterfactual is.

### Challenger
REBUTTAL: The funding landscape for a generic-statin TB program makes "never" a live branch

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the 40% p_success is a catch-all that plausibly already contains "Phase III never funded or run."
>
> Response:
- This conflates two different worlds. A "never funded" outcome inside the failure mass is a with-grant world in which the program fails. The critique's "never" branch is a without-grant world in which no one else runs Phase III.
- The attributable benefit is p × [benefit(with grant) − benefit(without grant)]. A no-Phase-III counterfactual raises the second term. It cannot be absorbed into p.
- The Advocate concedes (Concession 3) that the 40% has no stated reference class. "Arguable, not established" is the right description, and it means this is not existing coverage.

> The Advocate claims: all-in costs ($7M) against all-in benefits already price the "never" branch as a 1-year speedup.
>
> Response:
- This is the residual gap, not coverage. If the counterfactual is "never," the $7M buys the entire benefit stream, not one year of it.
- Charging full-pathway cost against a 1-year benefit is only consistent if the without-grant world has Phase III arriving a year later. That assumption is exactly what is untested.
- The Advocate's Concession 4 admits CG is "internally ambiguous about what the counterfactual is."

> The Advocate claims: the critique withdrew the ~20× claim, so the quantified upside is gone.
>
> Response:
- I concede the critique is internally inconsistent here. The hypothesis says to drop the figure, but the mechanism section keeps it. I do not rely on 20×.
- Withdrawing one number does not withdraw the structural point that speedup_years has no derivation and a plausible right tail.

> The Advocate claims: CG's 8-year Phase III completion assumption implies Phase III is not yet funded.
>
> Response:
- I agree, and it supports the critique. If no sponsor exists today, "who funds it absent this grant" is an open question the model must answer.
- An 8-year timeline is a duration, not evidence that a sponsor will appear.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

- **Absence of a registered Phase III.** I concede this is weakly informative. It fits both "sponsor appears after a positive Phase IIc" and "no sponsor ever." I rest nothing on it.
- **The 2026 review.** The Advocate says it speaks to need, not funder. That is right, but it is not neutral. A 2026 review saying statins "still need" large stratified Phase III trials is direct evidence that none is yet underway, which is the premise of the gap.
- **Rosuvastatin null.**
  - The Advocate accepts the conditional, that p_success falls if the null transfers, so we agree on direction.
  - The Advocate's atorvastatin/rosuvastatin pharmacology contrast (lipophilicity, CYP3A4) is, by the Advocate's own admission, not grounded in a TB result.
  - The Verifier's package says the null "weakens efficacy priors." It does not say the null is class-specific. The defense therefore has no evidence for uninformativeness.
- **"NIAID funded Phase 2b" and "no sponsor" point in opposite directions.**
  - Yes. The critique labels direction ambiguous, and I accept that.
  - Ambiguity means the 1-year point estimate is not supported either. It does not mean 1 year is correct.

**Correlation argument (Advocate Magnitude point 5).**
- The Advocate argues that funder skepticism links a high speedup to a low p_success. This is logic-only, and I think it fails on its own logic.
- SROI only accrues in worlds where the drug actually works.
- In those worlds, funders' skepticism was wrong. Without the Phase IIc signal this grant buys, there is no positive result to attract a Phase III sponsor.
- So the speedup conditional on success is driven by generic-drug market failure, not by efficacy. The negative correlation the Advocate invokes mostly operates in worlds that contribute zero benefit.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: the two Quantifier centrals combine to 0.375/0.40 = 0.9375, about −6% (≈2,864×), so the conclusion is unmoved.
>
> Response:
- The arithmetic is correct. But the Advocate also says neither central is derived, so the −6% rests on numbers the Advocate calls ungrounded. It cannot show both that the centrals are meaningless and that their net is the best estimate of impact.
- The combined central shows that two unsupported adjustments cancel. It does not show the parameters are well-calibrated. The Quantifier's own range runs from −50% to +200% on speedup.
- Taking the Advocate's ~2,000× bar, break-even is a speedup·p product of 0.4 × (2000/3054.9) ≈ 0.262.
  - At p = 0.3, that requires speedup ≥ ~0.87 years.
  - So the downside redundancy branch (speedup ≈ 0, which the critique names) crosses the bar. The headline conclusion is sensitive to this parameter.

> The Advocate claims: a distribution adds nothing beyond its mean because SROI is linear in speedup.
>
> Response:
- Mathematically right, and I concede it.
- The residual point is about the mean. For a right-skewed counterfactual, E[S] exceeds the median or modal "1 year." We do not know which statistic CG's "1" represents.
- Derivation: write E[S] = (1−q)·1 + q·H, where q is the probability of never and H is the effective horizon-capped speedup. Then E[S] − 1 = q(H − 1).
  - With H = 3 (the critique's high case), the Quantifier's 1.25 implies q ≈ 12.5%.
  - E[S] = 2 would require q = 50%.
  - So 1.25 is a modest tail weight, not an aggressive one.

> The Advocate claims: a "never" branch is unbounded and the 3-year case is illustrative.
>
> Response:
- Agreed that it is not a point estimate. H is capped by the benefit horizon, as in the derivation above. Discounting is negligible at 0.25 years (0.995), as the Advocate says, so I concede that.

**RESPONSE TO "OFFSETTING FACTORS":**

- **p_success offset.**
  - It is real in direction, but no derivation supports the 0.3.
  - The Advocate's offset is as unquantified as the speedup upside. "Nearly cancel" therefore means "two guesses roughly cancel."
- **Redundancy downside (q ≈ 0).**
  - This is real and I accept it. The critique itself flags it.
  - I could not verify whether the NIAID rosuvastatin Phase 2b creates an adequately funded path for atorvastatin. That is UNVERIFIABLE, not rejected.
  - A rosuvastatin null also lowers the chance NIAID follows with a Phase III, which argues against redundancy.
- **Denominator.** The Advocate says CG already treats the whole $7M as caused by the program. If so, the benefit side must be consistent with that. The 1-year credit is the inconsistency, not an offset.

**KEY UNRESOLVED QUESTIONS:**
- What is the probability that a Phase III sponsor emerges within a comparable time without this grant, given a positive Phase IIc? Neither side can estimate this.
- Does CG's "1 year" represent a mean or a modal scenario?
- Does the rosuvastatin null carry over to atorvastatin and to CG's Phase IIc endpoints? The pharmacology differences are untested in TB.
- Does the 40% p_success encode Phase III funding risk? CG gives no reference class.
- Would a consistent grant-marginal framing (cost = $320k, benefit = full stream in the never branch) or an all-in framing be better? The critique and Critique 2 conflict on this and the conflict is unresolved.

### Judge Audit
Surviving strength: moderate
Justification: The Challenger made grounded structural arguments that the Advocate largely conceded. These were the with-grant versus without-grant distinction, the inconsistency of crediting a 1-year benefit against a $7M all-in cost, and a break-even calculation showing sensitivity to the redundancy branch. The critique's quantitative and directional claims did not survive: the 20× figure is withdrawn, q is unestimated, the centrals net to −6%, and the direction is ambiguous by the critique's own account. The debate was mostly substantive, with few fabricated numbers and real derivations on both sides. The critique therefore survives as a valid structural and uncertainty concern, not as a basis for adjusting the point estimate.
Recommended action: 1. CONCLUDE NOW, with moderate confidence:
   - Do not change the central SROI estimate.
   - Drop the "~20× higher" claim entirely.
   - Relabel speedup_years as an unsupported assumption.
   - Replace the one-sided sensitivity range with a two-sided one. On the low end, include a redundancy branch (speedup ≈ 0–0.5, which crosses the ~2,000× bar at p ≈ 0.3). On the high end, include a q-weighted never branch (E[S] = 1 + q(H − 1)).
   - Report the result as "sign of adjustment unknown; conclusion sensitive below ~0.87 years at p = 0.3."

   One targeted check would most change this: whether CG's Phase IIc is gating, given that StAT-TB and the rosuvastatin Phase 2b are complete. This can be done by comparing the grant's design and endpoints against those trials using grant documents or a direct query to CG. It is feasible with existing access.
Action feasibility: actionable_now
Advocate failures: ['strawmanning: Existing Coverage 1 argues that "a Phase III that is never funded or run is plausibly already inside the 60% failure mass" of p_success. This is a category swap. p_success describes failure in the *with-grant* world, while the critique\'s "never" branch describes the *without-grant* counterfactual. The Advocate rebuts a claim about success probability when the critique made a claim about the counterfactual timeline. The Challenger identified this correctly, and the Advocate\'s own Concession 3 undercuts the point.', 'false_definitiveness: Magnitude Challenge 1 states that the Quantifier centrals "applied together… do not move the conclusion" (≈2,864×, −6%). Magnitude Challenge 2 then says "neither central value is derived." The internal-consistency move is legitimate: the critique\'s own numbers net to roughly zero. But the confident "do not move the conclusion" framing overstates what two ungrounded numbers can establish.', 'sound_synthesis_noted: The combined-central arithmetic (1.25 × 0.30 / (1 × 0.40) = 0.9375) and the linearity point are correct. Linearity means only E[speedup] matters, which collapses "model it as a distribution" to a question about the mean. The Challenger conceded both.']
Challenger failures: ['strawmanning: The Challenger says the Advocate "cannot show both that the centrals are meaningless and that their net is the best estimate of impact." The Advocate never claimed the net was the best estimate. It made an internal-consistency argument: even on the critique\'s own numbers, the effect nets to about −6%. The Challenger treats this as a positive estimate claim. The broader point, that two cancelling guesses do not show calibration, is fair.', 'false_definitiveness: The Challenger calls the 2026 review "direct evidence that none is yet underway." A review saying statins "still need" Phase III trials is consistent with that premise, but it is not direct evidence about trial status. In any case, the Advocate had already granted the premise through the 8-year assumption, so the point adds little.', 'sound_synthesis_noted: The break-even derivation is sound. A speedup·p product of 0.4 × 2000/3054.9 ≈ 0.262 implies a speedup of at least ~0.87 years at p = 0.3. This shows the headline conclusion is sensitive to the redundancy branch. One caveat: it uses the p = 0.3 that the Challenger elsewhere calls underived, which is the same move it faults in the Advocate.', "sound_synthesis_noted: The tail-weight derivation E[S] − 1 = q(H − 1) is valid. It shows a 1.25 mean needs only q ≈ 12.5% at H = 3, and less at larger H. The chain silently assumes the non-never delay D = 1, which ignores the verifier's D < 1 caveat. Even so, it is a defensible, inspectable synthesis."]
Debate resolved: The debate established four things:
- The "~20× SROI" figure is unusable. Both sides set it aside.
- Treating the speedup as a distribution matters only through its mean.
- CG's 1-year speedup is asserted, not derived.
- p_success cannot absorb the without-grant counterfactual. The Advocate's "existing coverage" claim on this point failed.

It also established that the critique's own centrals net to about −6%. The conclusion would cross the ~2,000× bar only if the speedup·p product falls below about 0.26, for example via the redundancy branch.
Debate unresolved: Several questions remain open:
- What q and H are, which sets the weight of the never branch.
- Whether this Phase IIc is actually gating, given completed statin Phase 2b trials. Neither side engaged this.
- Whether the rosuvastatin null transfers to atorvastatin and to CG's endpoints.
- Whether an all-in or grant-marginal framing should govern. This conflicts with Critique 2.

Because the up branch (never) and the down branch (redundancy, lower p) are both unweighted, the net direction remains unsigned.

--- Critique: Discounting quantified properly with an S-curve ramp and discounted costs. The net effect is about −20% to −31%, not the benefit-only −21% to −35%. ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION: Discounting with an S-curve ramp and discounted costs (net −20% to −31%)

**EXISTING COVERAGE:**
- The BOTEC does not hide the zero discount rate. The formula notes "No time discounting", and the parameter map lists the implicit discount rate as an explicit zero. This is a disclosed simplification, not an oversight.
- The CG BOTEC already handles timing in some ways.
  - It builds in an 8-year delay to Phase III completion and a 2%/yr decline in cases over that period.
  - It treats benefit as a one-year speedup rather than a permanent flow.
  - The speedup framing already caps the benefit at one year of scaled-up flow, which limits how much any horizon assumption can inflate the result.
- The critique's own evidence says: "I found no CG or GiveWell rule on discounting R&D BOTECs." The critique therefore cannot claim CG departs from a stated convention. It argues only that a different convention would be better.
- I cannot ground what discounting assumption underlies the ~2,000x bar. If the bar was calibrated against opportunities evaluated on an undiscounted or differently-timed basis, applying a discount only to this BOTEC would compare unlike things. I flag this as an open conditional, not an established point.

**EVIDENCE WEAKNESSES:**
- The timeline is not from the CEA. The critique's inputs are all "illustrative":
  - ramp start of about year 8.5,
  - a 6-year linear or S-curve ramp,
  - costs spread over years 1–8.

  The BOTEC states none of these. It gives only "8 years to Phase III completion" and "60% uptake if it works." The −20% to −31% range is therefore a function of assumptions the critique itself says to "flag as sensitive."
- The discount rates (3%, 4%, 5%) are not tied to any CG source. The critique found no CG convention, so the choice of rate is exogenous.
- The only mechanics the Verifier confirmed are arithmetic. The L = 10 factor at 4% (≈0.59, versus the Investigator's 0.57) is correct as a formula. Arithmetic correctness does not show the inputs are right.
- The critique is explicitly self-rated "medium-low" and "second-order." It also says that under any coherent counterfactual framing, discounting is "dwarfed by the framing effect." On its own account, this critique's decision-relevance depends on a separate critique.

**MAGNITUDE CHALLENGE:**
- The bar test depends on the net factor.
  - Baseline SROI is 3,055x in the replica.
  - The factor that brings SROI to 2,000x is 2,000/3,055 ≈ 0.655.
- The critique's own central net factors are about 0.80 (3%), 0.73–0.75 (4%), and 0.69 (5%).
  - Applied to 3,055, these give about 2,444, 2,230–2,290, and 2,108.
  - All stay above 2,000x. This matches the sensitivity output: the quantifier central (0.74) gives 2,261x, with no bar crossing.
- Only the "low" case (−38%, factor 0.62, SROI 1,894x) crosses the bar. That case sits outside the critique's own stated central range, and it requires a longer ramp or a higher rate than the illustrative timeline.
- The benefit-only penalty (−21% to −35%) was correctly identified as overstated. Once costs are discounted, the net effect is smaller, and the critique's own corrections reduce its force.
- The critique also notes that probability-weighting costs by stage would shift the cost-side offset only "modestly." That leaves the net range unchanged.

**OFFSETTING FACTORS:**
- The parameter map lists implicit zeros in the BOTEC: morbidity DALYs (lung damage), post-treatment mortality, transmission-averted cases, and diagnostic value from the sweat test. The BOTEC says only mortality is valued.
  - Any positive value from these channels would offset a discount haircut.
  - A 20–30% discount penalty could be wholly or partly cancelled by omitted benefits of similar size.
  - I cannot ground a size for these channels. This is a conditional offset, not a quantified one.
- The critique applies a discount to benefits that accrue in the late 2030s. It does not consider that CG's $OP unit already values income via log utility. That unit may embed growth-related adjustments I cannot verify, so I do not rely on this point.

**OVERALL ASSESSMENT: Partial defense.**
- The critique is correct in direction. A zero discount rate is a real simplification, and a consistent positive rate would reduce SROI by roughly 20–30%.
- The defense rests on four points:
  - the critique's evidence for any CG convention is nil;
  - the timeline inputs are assumed;
  - the central estimates keep SROI above the ~2,000x bar;
  - the omitted benefit channels plausibly offset the haircut.
- None of these shows that a zero discount rate is right. They show that the effect is moderate, uncertain, and not independently bar-crossing in the central case.

**CONCESSIONS:**
- A consistent discount rate of 4–5% would lower the SROI by about 25–31% in the critique's illustrative timeline. That exceeds the 25% change threshold, so the critique is "material" by that criterion.
- CG offers no justification for a zero rate, and the BOTEC does not test sensitivity to it. That is a transparency gap.
- The −38% low case does cross the bar. Whether it is plausible depends on timeline inputs that CG has not specified.
- I cannot show that the omitted benefit channels fully offset the discount penalty.

### Challenger
REBUTTAL: Discounting quantified with an S-curve ramp and discounted costs (net −20% to −31%)

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the zero discount rate is a disclosed simplification ("No time discounting"), and the BOTEC already handles timing through the 8-year delay, the 2%/yr case decline, and the one-year-speedup framing.

- **Disclosure is not justification.** The Advocate concedes that "CG offers no justification for a zero rate" and that the BOTEC does not test sensitivity to it. Labelling the zero is not the same as showing it is harmless.
- **The 8-year delay and 2%/yr decline are not discounting.** They move when benefits start and how many cases there are. They do not reduce the weight of a benefit received in year 8 relative to year 0. Under a zero rate, a DALY or $OP in 2034 counts the same as one today. The existing timing features leave the time-value question untouched.
- **The one-year-speedup framing limits how large the benefit can be. It does not fix when the benefit arrives.** The framing caps the quantity, not the date, so the cap is irrelevant to the discount factor.
- **The bar-calibration conditional cuts both ways.**
  - The Advocate says that if the ~2,000x bar was set on an undiscounted basis, discounting only this BOTEC would compare unlike things. The Advocate labels this an open conditional.
  - The verifier marked nothing on this either way, so it is unresolved, not a point for the defense.
  - If the bar was set on a discounted basis, the undiscounted BOTEC is overstated.
  - The Advocate has not shown that the first case is more likely than the second.
  - From my own knowledge of GiveWell's published CEAs, which is not in the verifier package and is a weak prior, GiveWell models generally apply a positive discount rate (I recall ~4%). If that is right, the second case is at least as likely as the first.
- **The "dwarfed by framing effect" point is conditional.**
  - The critique says discounting is second-order *under a coherent counterfactual framing* (Critique 1).
  - If CG keeps the current speedup framing, that dwarfing does not occur.
  - So the Advocate's reliance on it assumes the other critique's resolution.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the timeline inputs (ramp start ~8.5, 6-year ramp, costs over years 1–8) are illustrative and not from the CEA, and the discount rates are exogenous, so the −20% to −31% range is assumption-driven.

- **Part of the timeline is in the BOTEC.** The 8-year delay to Phase III completion is a stated input, so benefits starting at ~year 8 or later is grounded. The ramp length and cost spread are assumed.
- **A floor follows from the stated delay.** Derivation, my own, at 4%:
  - Benefits starting instantly at year 8 get a factor of e^(−0.04·8) ≈ 0.726.
  - Costs spread uniformly over years 1–8 get an average factor of (1−e^(−0.32))/0.32 ≈ 0.856.
  - The net factor is 0.726/0.856 ≈ 0.85, about −15%, as the minimum with no ramp at all.
  - The critique's −20% to −31% therefore adds a ramp penalty on top of a grounded delay penalty. The effect is not purely an artifact of assumed inputs.
- **The ramp-length concern points one way.**
  - Any gradual uptake (the BOTEC itself mentions 60% uptake "if it works") pushes the factor below 0.85.
  - Instant full uptake at year 8 is the least plausible case for a new TB therapy.
- **Arithmetic correctness is relevant here.**
  - The Advocate says "arithmetic correctness does not show the inputs are right."
  - But the verifier's confirmation covers the sensitivity of the result to ramp length, which is exactly what the Advocate says makes the range unreliable.
  - The sensitivity is real and quantified, and it runs toward larger penalties (L=10 gives 0.57–0.59 benefit-only).
- **The rates are bracketed.** 3–5% is a conventional range for health CEAs. The critique reports all three, not a cherry-picked one.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: the central net factors (0.69–0.80) leave SROI above 2,000x, only the −38% low case crosses the bar, and that case is outside the central range.

- **Concession.** The Advocate's arithmetic is right. The bar-crossing factor is 2,000/3,055 ≈ 0.655, and the sensitivity output at 0.74 gives 2,261x with no crossing.
- **The gap to the bar is narrow at the pessimistic end of the critique's own parameter range.** Derivation, using the 0.856 cost factor above:
  - The L=10, 4% benefit factor of 0.57–0.59 gives a net factor of 0.57/0.856 ≈ 0.67 to 0.59/0.856 ≈ 0.69. That is 2–5% above the 0.655 crossing point.
  - The L=10, 5% benefit factor of 0.51 gives a net factor of roughly 0.51/0.82 ≈ 0.62. The 0.82 is my approximation of the 5% cost factor, (1−e^(−0.4))/0.4 ≈ 0.82. This is below 0.655, so the bar is crossed.
  - So one plausible step on either ramp length or rate moves the result across the bar.
- **The "low" case is not an outlier.** The −38% case is the low end of the sensitivity range tied to the critique's own parameters. It is not an arbitrary extreme.
- **The Advocate concedes materiality.** The Advocate accepts that 4–5% rates give −25% to −31%, which exceeds the 25% threshold. The dispute is whether the effect crosses the bar, not whether it is large.
- **The critique does not rest on the central case alone.** It says explicitly that the result is sensitive to the real timeline. The right takeaway is that the BOTEC's headline is within a few percentage points of the bar once a plausible discount is applied. That is information the zero-rate BOTEC hides.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: omitted benefit channels (morbidity, post-treatment mortality, transmission, sweat-test diagnostics) could partly or wholly cancel a 20–30% discount haircut.

- **The Advocate admits the offset is unquantified.** "I cannot ground a size for these channels."
  - It is a conditional with no magnitude, and it should not reduce confidence in a quantified critique by any specific amount.
  - It is not REJECTED evidence, but it is not support either.
- **Conceptually, omitted benefits do not offset a discount factor.**
  - Benefits from those channels would also accrue late, in the same period as the mortality benefit, so they would be discounted too.
  - The discount penalty applies multiplicatively to whatever the total is. Adding omitted benefits raises the pre-discount level but does not undo the discount.
  - The two matter together only for whether the final SROI clears the bar, which is a separate question that needs those channels sized.
- **The offset could argue against zero discounting only by accident.** Treating two independent simplifications as offsetting works only if their magnitudes are known to be close. The Advocate has no basis for that.
- **The cost side is already netted.** The 20–31% figure already credits costs being discounted. The remaining offset the critique identifies, probability-weighting costs by stage, is modest by the Advocate's own reading.
- **The log-utility/$OP point is withdrawn.** The Advocate says "I do not rely on this point," so there is nothing to rebut.

**KEY UNRESOLVED QUESTIONS:**
- Was the ~2,000x bar calibrated on a discounted or undiscounted basis? If discounted, the undiscounted BOTEC is directly overstated. If undiscounted, the comparison needs a bar adjustment rather than no change. Neither side can ground this.
- What is the real CG timeline for ramp and spend? A ramp longer than ~6 years at 4–5% pushes the net factor to or below the 0.655 crossing point.
- How large are the omitted benefit channels, and do they accrue on the same timeline? Without sizes, they cannot be used as an offset or dismissed.
- Will CG adopt a counterfactual framing (Critique 1)? That determines whether discounting is second-order or a leading refinement.

### Judge Audit
Surviving strength: moderate
Justification: The critique's core quantitative claim survived. The verifier confirmed the arithmetic, the Advocate conceded materiality at 4–5%, and the Challenger's grounded floor derivation showed that at least ~15% of the penalty follows from stated BOTEC inputs. However, the critique's decision-relevance is limited:
- The Advocate's bar-crossing arithmetic showed that the central cases do not change the funding conclusion.
- The Challenger's attempt to show that a single pessimistic step crosses the bar was contradicted by the Challenger's own numbers.
Both sides engaged in substantive synthesis rather than guess-trading. This supports a moderate verdict on a self-described medium-low, second-order critique.
Recommended action: 1. CONCLUDE NOW: Adopt the critique's corrected figures, with moderate-to-high confidence in the direction and magnitude given the illustrative timeline.
   - The net discount penalty is about −20% (3%), −25% (4%, using the verifier-corrected 0.633 benefit factor), and −31% (5%).
   - The BOTEC should add a discount-rate sensitivity row and disclose that the zero rate is unjustified.
   - The central SROI stays above ~2,000x, roughly 2,100–2,450x.
   - The bar is crossed only under the joint pessimistic case (ramp ≈10 years and 5% rate).
   - Treat the critique as a transparency and robustness fix, not a decision-changing finding.
   - Remove the garbled "conflict with Critique 1" passage.

   A secondary step is a single targeted query to CG: is the ~2,000x bar expressed in discounted terms, and what is the expected time from Phase III completion to scale-up? This is feasible and would decide whether the joint-pessimistic case is plausible.
Action feasibility: actionable_now
Advocate failures: ['strawmanning: The speedup framing already caps the benefit at one year of scaled-up flow, which limits how much any horizon assumption can inflate the result." This is a category swap. The critique is about *when* benefits arrive (time preference), not *how much* benefit accrues over a horizon. The Challenger correctly answered that the cap limits quantity, not date.', 'call_to_ignorance: A 20–30% discount penalty could be wholly or partly cancelled by omitted benefits of similar size." The Advocate admits "I cannot ground a size for these channels," yet treats the possibility as a defense. The caveat is honest, but the point is still offered as an offset with no magnitude.', 'false_definitiveness: The Overall Assessment lists "the omitted benefit channels plausibly offset the haircut" as one of four pillars of the defense. The Advocate\'s own Concessions say "I cannot show that the omitted benefit channels fully offset the discount penalty." The same unquantified point is hedged in one section and leaned on in another.', 'false_definitiveness: probability-weighting costs by stage would shift the cost-side offset only \'modestly.\' That leaves the net range unchanged." "Modestly" does not mean "unchanged." The critique\'s mechanism says probability-weighting pushes expected spend toward the near term. That brings the cost discount factor closer to 1, which makes the net penalty slightly *larger*, so the direction cuts against the defense.', "sound_synthesis_noted: The bar-crossing calculation (2,000/3,055 ≈ 0.655) is applied to the critique's own net factors and cross-checked against the sensitivity output (0.74 → 2,261x). It also uses the verifier-corrected 0.73–0.75 range at 4%. This is clean, grounded, and the Challenger conceded it."]
Challenger failures: ['unsupported_estimate_pseudo: So one plausible step on either ramp length or rate moves the result across the bar." The Challenger\'s own numbers contradict this:', 'unsupported_estimate_fabricated: The −38% case is the low end of the sensitivity range tied to the critique\'s own parameters. It is not an arbitrary extreme." No derivation links the −38% figure to the critique\'s stated parameters. Neither the verifier package nor the critique produces −38% from its stated inputs. The Challenger\'s own joint-pessimistic calculation gives roughly −37% to −38%, but only by combining both extremes.', 'sound_synthesis_noted: The no-ramp floor derivation:', 'sound_synthesis_noted: The argument that omitted benefits are themselves late-accruing, so the discount applies to them multiplicatively, is correct analysis. The Challenger then properly narrows the remaining relevance to the bar-clearing question.']
Debate resolved: 1. Under consistent discounting with the critique's illustrative timeline, the net penalty is about −20% / −25 to −27% / −31% at 3% / 4% / 5%. That is material by the 25% criterion at 4–5%, but it keeps SROI above the ~2,000x bar in every single-parameter variation.
2. A floor of roughly −15% at 4% follows from the BOTEC's own stated 8-year delay, so the effect is not purely an artifact of the assumed inputs.
3. The speedup cap and the 8-year delay do not substitute for discounting.
Debate unresolved: 1. Whether the ~2,000x bar was calibrated on a discounted or an undiscounted basis. This determines whether discounting only this BOTEC is even the right comparison.
2. CG's actual post-Phase-III rollout and ramp length. The bar is crossed only if a long ramp (≈10 years) coincides with a 5% rate, and neither side grounded the probability of that joint case.

--- Critique: A 1-year speedup of trial results does not necessarily become a 1-year speedup of adoption, in either direction. ---

### Advocate
**DEFENSE OF GIVEWELL'S POSITION: A 1-year speedup of trial results does not necessarily become a 1-year speedup of adoption**

**EXISTING COVERAGE:**
- CG's calculation treats the grant as moving the whole adoption pathway one year earlier, not just the trial readout. The $7M all-in cost includes "later Phase III trials, guideline changes, dissemination and validation." Costs and benefits are both measured over the full path to adoption, so the 1-year figure is meant to be a speedup of adoption, not of trial results alone.
- The 40% probability that both Phase II and III succeed is the only probability applied. It is a blunt instrument, but it does reduce the expected benefit.
- The adoption-curve shape is not a hidden problem for the speedup. If the counterfactual adoption curve is shifted one year earlier, the benefit is the area between the two curves. Over a long horizon that area is (one year) × (steady-state annual benefit), whatever the ramp shape. CG's "benefit = steady-state annual benefit × 1 year" therefore holds without an explicit ramp, provided the shift is a pure time translation. This is my own derivation from the model's structure, not a cited finding.
- The 1-year figure is a stated, user-adjustable assumption in a BOTEC. The critique does not identify an error in it. It says the figure is untested.

**EVIDENCE WEAKNESSES:**
- The critique's own evidence package does not support its directional lean.
  - The only grounded facts are that WHO guidance followed pivotal data within months in the Study 31/BPaLM cases, and that rifapentine had price and availability problems.
  - It states "I did not find data on national adoption lags, which is where slack-absorption would most plausibly occur."
  - It flags the national-level lag claim as UNGROUNDED. The "leaning down" direction rests on the part of the pathway where it has no data.
- The rifapentine precedent is weakly relevant to atorvastatin.
  - Rifapentine's problem was drug price and availability for a branded or limited-supplier product.
  - The CG BOTEC rests on atorvastatin being "generic and cheap." Procurement bottlenecks are plausibly smaller for a generic. I cannot ground how much smaller, so treat this as a conditional point.
- The mechanism for slack absorption needs fixed calendar-time gates downstream, such as national policy cycles or procurement cycles.
  - If downstream lags are independent of when the evidence arrives, an earlier readout shifts the whole pipeline and the speedup is the full year.
  - The critique concedes it has no evidence that such gates bind. It also concedes they would push the effective speedup above 1 year when a cycle is missed.
- The Quantifier's central value of 0.85 and low value of 0.5 are not derived from any source. The Quantifier says "I cannot estimate the probabilities." The −15% central and −50% low cases are illustrative, not evidence-based.

**MAGNITUDE CHALLENGE:**
- At the Quantifier's own central value (0.85 years), SROI is about 2,597x. That is still above the ~2,000x bar, and the −15% change is below the 25% materiality threshold.
- Only the low case (0.5 years, SROI about 1,527x) crosses the bar. The critique states the threshold is about 0.65 years. Slack absorption would have to consume more than a third of the year on average to get there.
- The critique's own evidence is that WHO responds in months and that national-level data is absent. Neither supports a mean slack absorption above 35%. That would require a large fraction of the pathway to be fixed-calendar-bound, which no cited source shows.
- The high case (1.2 years, +20%) is also below the 25% materiality threshold. The critique's "material" label rests entirely on an ungrounded low tail.

**OFFSETTING FACTORS:**
- Zero discounting and the exclusion of morbidity, transmission and diagnostic value are conservative omissions that CG's own notes list (the parameter map says "only mortality is valued" and "No time discounting"). The map also notes that lung-damage reduction and the sweat-diagnostic workstream are mentioned but not valued. These omissions push the estimate in the opposite direction from the critique, and I cannot size them.
- Missed-cycle effects in the critique's own framing push the effective speedup above 1. Downside slack absorption and upside missed windows plausibly partly offset, so the expected speedup is uncertain around 1 rather than clearly below it.
- The one grounded piece of evidence, fast WHO action, supports the model's assumption that the guideline step does not add friction.

**OVERALL ASSESSMENT:** Partial defense.
- The critique has a real point: nothing in the CG text justifies "1 year" as the effective adoption speedup. The parameter map confirms there is no justification and no reconciliation with the all-in cost framing.
- The critique supports only a symmetric uncertainty, not a downward bias. Its own central case (0.85 years) does not cross the bar, and the threshold-crossing case requires an ungrounded downstream bottleneck.
- Under the null hypothesis that the current estimate is approximately right, the critique has not met its burden of proof for "material."
- It is not a Strong defense because CG offers no positive evidence for the 1-year figure, and the model is linear in this parameter.

**CONCESSIONS:**
- The 1-year speedup is an assumption with no stated derivation. The effective speedup could plausibly be below 1 if national policy or procurement lags absorb some of the shift.
- Because SROI is linear in `speedup_years`, a speedup below ~0.65 years would put the estimate below the bar. That threshold is not far from 1.
- The Quantifier's concern that the "fixed schedule" and "2+ year cycle" claims are ungrounded is valid. I do not rely on them either. My defense is that the downside is also ungrounded, not that the speedup is known to be 1.
- A sensitivity range for this parameter (for example 0.5 to 1.2 years) should be shown alongside the point estimate, even though the central estimate does not clearly fail.

### Challenger
REBUTTAL: A 1-year speedup of trial results does not necessarily become a 1-year speedup of adoption

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the $7M all-in cost covers Phase III, guideline changes and dissemination, so the 1-year figure is meant as an adoption speedup. They add that if the whole adoption curve is a pure time translation, the benefit is (shift) × (steady-state annual benefit) whatever the ramp shape.

- **The translation derivation is correct but circular.** The critique's question is whether the shift is a pure translation. The Advocate's area argument assumes it is. It shows the model is internally coherent *if* the speedup is 1 year. It gives no evidence that it is.
- **Cost-side coverage does not establish benefit-side timing.** Paying for guideline work and dissemination buys those steps. It does not show that a year of earlier trial results becomes a year of earlier adoption. The Advocate concedes that "the parameter map confirms there is no justification and no reconciliation with the all-in cost framing."
- **The translation assumption fails under a binding non-evidence constraint.** This is the mechanism that gives a downward bias, and I derived it myself rather than citing it.
  - If some downstream step is capacity- or supply-limited (procurement, price, availability), earlier evidence does not shift the curve.
  - The curve starts at the same constraint-limited point, so the shift is less than 1.
  - The verifier's evidence includes rifapentine price and availability problems, which are a documented instance of this.
- **I concede one point on gates.** With a single periodic calendar gate and uniformly random phase, the expected speedup is exactly 1. Missed-cycle gains and slack losses average out.
  - So the downward lean cannot rest on calendar gates alone.
  - It rests on constraints that do not move with the evidence date.
  - That is a narrower claim than the original critique's "fixed schedule" framing, and I do not rely on that framing.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the downward lean rests on the national-lag part of the pathway, where the critique has no data. They also say rifapentine is weakly relevant because atorvastatin is generic, and that no evidence shows that downstream gates bind.

- **"No data" here means UNVERIFIABLE, not REJECTED.**
  - The verifier said "I did not find data on national adoption lags." That is an absence of evidence in both directions.
  - The Advocate's point that "no evidence gates bind" is the mirror image of the claim they are rebutting. The null of exactly 1.0 is not privileged by that absence.
  - The 1-year figure is also unsupported, as the Advocate concedes.
- **The fast-WHO evidence cuts against the Advocate's offset, not just for them.**
  - The verifier found WHO guidance followed pivotal data within months in both case studies. If WHO acts ad hoc and fast, there are no discrete guideline cycles to miss.
  - The "missed-cycle pushes it above 1" offset then loses its mechanism.
  - The Advocate cannot use fast WHO as evidence of no friction and also keep missed cycles as an offset. Taking the verifier's evidence at face value, the upside tail shrinks and the downside mechanisms remain. This is why the verifier states the direction as "more toward less than one year."
- **The generic-drug point cuts both ways.** The Advocate flags it as conditional, and I treat it as conditional too.
  - Generic status plausibly lowers price friction.
  - But a cheap generic repurposed for a new indication has no manufacturer with an incentive to file, promote or lobby for national adoption. I cannot ground this from the verifier package; treat it as an uninformed prior.
  - So the rifapentine analogy is imperfect, but the net direction of the generic point is not clearly in the Advocate's favor.
- **The WHO responsiveness evidence is narrow.** It comes from two TB regimen cases, and the BPaLM step is described as ad hoc. Whether a host-directed adjunct like a statin would get the same treatment is unknown. The verifier did not test this.
- **I concede that the 0.85 and 0.5 values are illustrative.** The Quantifier said it could not estimate the probabilities, so these are sensitivity points, not findings.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: at the 0.85 central value, SROI is about 2,597x, still above the bar. Only the 0.5 low case crosses, and that requires more than 35% mean slack absorption, which no cited source supports.

- **The headroom is thin, which is why the label is "material."**
  - Baseline is 3,055x and the bar is about 2,000x. The ratio is about 1.53, so the break-even speedup is about 0.65 years. Check: 3,055 × 0.65 ≈ 1,986.
  - The estimate fails if the effective speedup falls short of 1 year by more than about 35%. That is a modest miss on an assumption nobody has grounded.
- **The 0.85 case is not a robustness result.** The Advocate presents it as passing, but it is not derived from evidence. The −15% sits only 10 percentage points inside the 25% materiality line, and the tail beyond it is not excluded by anything in the evidence.
- **The 35% threshold is not remote.** The Advocate says no source shows a bottleneck that large. No source shows it is small either. The only documented downstream friction is rifapentine's price and availability problem, and its magnitude in years is not given in the verifier package. I cannot say whether it exceeded 0.35 years.
- **The tails are asymmetric if the missed-cycle mechanism is weak.**
  - If WHO acts in months, the upside is limited to about +20% (the 1.2-year case).
  - The downside reaches −50% through capacity constraints.
  - A bounded upside and a longer downside tail make the expectation lean below 1, even if the central case does not cross.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: zero discounting and omitted morbidity, transmission and diagnostic value push the estimate up. Missed cycles also push the speedup above 1, and fast WHO supports no friction.

- **The omitted benefits are real but unquantified.** The Advocate says "I cannot size them." An offset that cannot be sized does not neutralize a −35% to −50% parameter risk. It shows only that other omissions exist.
- **The missed-cycle offset is weakened by the Advocate's own evidence.** See above: fast, ad hoc WHO action removes the cycle structure that the upside needs.
- **"Fast WHO supports no friction" overreaches.** It covers the guideline step only. The verifier explicitly lacks data on the national step, which is the part the critique questions.
- **Zero discounting is not clearly an offset.** Whether it matters depends on how it interacts with the speedup. Delayed adoption would be discounted too, so I do not rely on it as an offset in either direction.

**KEY UNRESOLVED QUESTIONS:**
- Is there a non-evidence binding constraint (supply, price, national regulatory label change for a repurposed generic) in the atorvastatin pathway that would stop the adoption curve from translating?
- Do national TB programs adopt WHO guidance on a lag independent of when it is issued (translation, so a full year) or on pre-scheduled review cycles (slack or missed-cycle effects)? No grounded data exists.
- Does the $7M cost of "guideline changes and dissemination" actually fund national-level adoption work, or only WHO-level work? That would determine whether CG's cost framing covers the bottleneck in question.
- Would WHO's rapid response in Study 31/BPaLM generalize to an adjunct host-directed therapy with a weaker sponsor presence?
- What distribution over effective speedup is defensible? The Quantifier's 0.5/0.85/1.2 points are illustrative, and nobody has grounded the probability that the value falls below 0.65.

### Judge Audit
Surviving strength: moderate
Justification: - The Challenger landed one grounded blow. The verifier's fast-WHO evidence undercuts the Advocate's missed-cycle offset, so the critique's "leaning down" direction survives in narrowed form.
- The Advocate's magnitude point also stands unrebutted. Crossing the bar requires more than 35% mean slack absorption, and nothing grounds that.
- The Challenger's asymmetric-tails argument relied on recycling illustrative points as bounds.
- The Advocate misstated the verifier's directional finding and made an incorrect claim about discounting.
- The net result is a valid concern with an ungrounded quantitative claim. The substantive question remains open but has been narrowed.
Recommended action: 1. CONCLUDE NOW, with moderate confidence. The 1-year speedup should be presented as an uncertain parameter with a mild downward lean. The guideline-step upside is largely ruled out, and modest national or procurement friction is plausible.
   - Report a sensitivity range of roughly 0.5–1.2 years and state the 0.65-year break-even explicitly.
   - Optionally, use a central value modestly below 1 (e.g., 0.85–0.95). This keeps the estimate above the bar.
   - Do not treat the critique as having shown a threshold-crossing adjustment.
   - Correct the claim that zero discounting is conservative.

   Optional targeted follow-up that would change the central value: re-run the verifier to search for national TB guideline adoption lags after WHO rapid communications. Examples include MSF/Stop TB "Step Up for TB" policy-adoption surveys covering the 2021 4-month rifapentine regimen and the 2022 BPaLM regimen, and time-to-national-adoption of WHO EML generics. This is feasible with existing tooling.
Action feasibility: actionable_now
Advocate failures: ['misrepresenting_evidence_status: The Advocate wrote "The critique\'s own evidence package does not support its directional lean." The verifier said the opposite. It stated "the evidence points more toward \'less than one year\' through downstream bottlenecks," and it marked the claim that trial results are not the only binding constraint as SUPPORTED, citing rifapentine price and availability. The verifier rejected only the missed-window upside mechanism. The Advocate is entitled to say the magnitude of the downward lean is ungrounded. Saying the package does not support the direction misstates it.', 'call_to_ignorance: The Advocate wrote "Downside slack absorption and upside missed windows plausibly partly offset, so the expected speedup is uncertain around 1." The missed-window mechanism is the one the verifier found "NOT SUPPORTED, and partly CONTRADICTED" by the Study 31 and BPaLM cases. The Advocate also cites the same fast-WHO evidence as proof that the guideline step "does not add friction." Keeping an unsupported upside mechanism as an offset, while using evidence that removes it, fills the gap with speculation. The Challenger correctly exposed this.', 'false_definitiveness: The Advocate called zero discounting a "conservative omission" that "push[es] the estimate in the opposite direction from the critique.', "sound_synthesis_noted: The area-between-curves derivation is correct and is explicitly framed as the Advocate's own conditional derivation. Under a pure time translation, the benefit is the shift multiplied by the steady-state annual benefit, regardless of ramp shape. The arithmetic is also correct: 3,055 × 0.85 ≈ 2,597x, and the central illustrative case sits inside the 25% materiality line.", 'sound_synthesis_noted: The generic-drug point is properly flagged as conditional ("I cannot ground how much smaller"). This is legitimate conditional argument, not an unsupported estimate.']
Challenger failures: ['unsupported_estimate_pseudo: The Challenger wrote "If WHO acts in months, the upside is limited to about +20% (the 1.2-year case). The downside reaches −50% through capacity constraints.', 'false_definitiveness: The Challenger wrote "An offset that cannot be sized does not neutralize a −35% to −50% parameter risk." This frames an illustrative range as an established risk magnitude. Elsewhere the Challenger admits "I cannot say whether it exceeded 0.35 years.', 'call_to_ignorance: The Challenger argued that a repurposed generic "has no manufacturer with an incentive to file, promote or lobby for national adoption." It honestly labels this an "uninformed prior." It nonetheless uses it to conclude that the generic point\'s "net direction... is not clearly in the Advocate\'s favor." The disclosure mitigates the failure but does not remove it.', 'unsupported_estimate_pseudo: The Challenger offers rifapentine as "a documented instance" of a constraint that "does not shift" with the evidence date. The verifier package documents price and availability friction. It does not show that this friction was independent of when the evidence arrived. Plausibly, the price reduction was triggered by the evidence and guidance. The step from "documented friction" to "evidence-independent constraint" is a logical gap.', 'sound_synthesis_noted: The Challenger correctly identifies that the translation argument assumes what is in dispute. It concedes that a single periodic gate with uniform random phase gives an expected speedup of exactly 1. Its break-even check (3,055 × 0.65 ≈ 1,986) is correct.', "sound_synthesis_noted: The Challenger's strongest move is grounded in the verifier evidence. Fast, ad hoc WHO action removes the missed-cycle upside, while downstream frictions remain. This rebuts the Advocate's offset directly. It also correctly distinguishes UNVERIFIABLE from REJECTED regarding national lags."]
Debate resolved: Both sides agree on four points:
- The 1-year effective adoption speedup is an unjustified assumption.
- The "fixed schedule" and "2+ year cycle" claims should be dropped.
- The break-even is about 0.65 years.
- The central illustrative case (0.85 years) does not cross the bar.

The debate also established that fast WHO guideline action removes most of the missed-window upside. Any remaining uncertainty therefore sits in the national, procurement and supply steps, which gives a mild downward lean rather than symmetric uncertainty.
Debate unresolved: Two questions remain open:
- Whether any downstream constraint in the atorvastatin pathway is genuinely independent of when the evidence arrives. This would need to be a constraint other than one that loosens in response to evidence, such as rifapentine-style pricing.
- How large that constraint is, and therefore whether the probability that the effective speedup falls below 0.65 years is meaningful.

Neither side produced any grounding for the size of the national-adoption lag.

--- Critique: Post-TB lung disease morbidity is likely the largest unvalued channel (~50–60k central, wide range) ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION: Post-TB lung disease morbidity as an unvalued channel

**EXISTING COVERAGE:**

1. CG does not model this channel. The BOTEC states "only mortality is valued," and the lung-damage signal is mentioned only as context. I can't claim the adjustment chain captures it.
2. The omission is a stated simplification, not an oversight. A BOTEC that values only on-treatment mortality is conservative by construction. This critique raises the estimate, so it is a refinement of a lower bound, not evidence the grant is overstated.
3. One existing parameter partly interacts with the channel. The 27 DALYs per death averted assumes full remaining healthy life expectancy. The parameter map notes CG makes no adjustment for survivors' excess mortality. If post-TB lung disease is as large as the critique claims, an averted on-treatment death yields fewer than 27 clean DALYs, because the survivor carries sequelae. The critique's added morbidity DALYs are therefore partly offset by an overstatement already embedded in the baseline, and the critique does not net this out.

**EVIDENCE WEAKNESSES:**

1. **The key quantity is ungrounded.** The 5% reduction attributable to the intervention is labelled UNGROUNDED by the critique itself. It rests on two links, neither verified:
   - A Phase IIa/b chest X-ray lung-damage signal for atorvastatin.
   - The assumption that an early radiographic effect persists into long-term function and disability.
   The first is a surrogate in a small early trial. The second is untested for statins. A central estimate built on two unverified links is illustrative, as the critique concedes.
2. **The Menzies figure is the wrong denominator.**
   - The 5.8 of 12.1 lifetime DALYs per incident case is the total post-TB burden, not the part an adjunct could avert.
   - By the critique's own account it includes post-TB mortality and extrapulmonary cases, so it is not comparable to the 0.75 DALYs per patient used for lung morbidity alone.
   - A large total says little about how much of it a statin-driven reduction in early lung damage would remove.
3. **The 2025 Lancet Glob Health result has the same limitation.** Post-TB DALYs being 52.5% of the total under prompt treatment shows post-TB burden is large. It does not show the burden is modifiable by an adjunct, and the 5% reduction is the actual driver of the channel.
4. **The 0.75 DALYs per treated patient is a chain of inferences.**
   - It combines a 30% impairment share, a 0.1–0.2 disability weight and 15–25 years of duration.
   - The critique says the disability weight is something it "would verify," so it is unverified.

**MAGNITUDE CHALLENGE:**

1. **The central estimate is a modest uplift.**
   - The baseline expected benefit is about 539.5k DALYs × 0.4 ≈ 216k.
   - The critique's central 55k is about +25% on that figure.
   - It sits at the edge of the ~25% materiality threshold, and only in the favourable direction.
   - The sensitivity run shows no bar crossing at low, central or high. The central case moves SROI from ~3,055 to ~3,847 (+26%).
2. **The low end is immaterial.** The critique's low bound of ~10k DALYs is about 5% of the baseline expected benefit (10k / 216k), well under any decision threshold.
3. **The probability weight is generous.**
   - The 0.45 weight exceeds p_success of 0.4 because it adds a branch where the mortality endpoint fails but the lung benefit is "real and still leads to adoption."
   - That branch is speculative. A ~$7M all-in Phase III, with adoption 8 years out, is unlikely to be powered on decades-long lung function. Adoption on a lung-damage surrogate alone would need a different evidentiary path.
   - Using 0.4 gives about 49k, a small change. The point is that the extra branch is not independently supported.
4. **The "inflated by no discounting" concern is mostly neutral here.**
   - The critique says the no-discounting convention inflates this channel. The baseline 27 DALYs per death is also undiscounted over a similar horizon.
   - My derivation, using an annuity factor over 20 years: at 3%, (1 − 1.03⁻²⁰)/(0.03 × 20) ≈ 0.74. At 5%, (1 − 1.05⁻²⁰)/(0.05 × 20) ≈ 0.62.
   - Discounting would trim both channels. The post-TB channel's duration (15–25 years) is only modestly shorter than the 27-year baseline, so the relative uplift barely changes.
   - Absolute SROI would fall under discounting. That is a separate critique about the convention, not about this channel.
5. **The overlap with the post-treatment mortality critique reduces net uplift.** The critique concedes Menzies models post-TB mortality and morbidity jointly from lung function, and that both critiques apply the same 5% to the same pathway. Once combined, the net new value of this channel is smaller than its standalone figure suggests.

**OFFSETTING FACTORS:**

1. As in point 3 of Existing Coverage, the 27 DALYs per averted death is overstated if survivors carry post-TB impairment. This directly offsets part of the morbidity gain.
2. The channel does not account for the negative-effect risk in the parameter map. Hepatotoxicity alongside HRZ or myopathy could produce zero or negative net lung or survival effect. This is weighted into p_success only implicitly.
3. If the lung benefit comes mainly from earlier bacterial clearance, it may be partly redundant with the short-regimen improvements the parameter map flags as not considered. That would reduce the headroom for adjunctive benefit.
4. The channel adds no costs for the extra follow-up or adverse-event monitoring it would require to demonstrate and deliver the benefit.

**OVERALL ASSESSMENT:** Partial defense.

- The strongest points are that the 5% reduction is ungrounded, that Menzies' total burden is not the avertable burden, and that the baseline 27 DALYs and the double-counting overlap partly offset the uplift.
- I can't say CG already covers the channel, and the direction (upward) is probably right.
- The case that the channel is material is weak. The central uplift is ~25% at best, the low end is ~5%, and no sensitivity run crosses the bar. The decision-relevant effect is mainly upside.

**CONCESSIONS:**

1. Valuing post-TB morbidity at zero is a real omission. Given Menzies and the 2025 modelling, a nonzero positive value is more likely than not.
2. The Investigator's 0.75 DALYs per patient may well understate total post-TB burden, since mortality and extrapulmonary cases are excluded from it.
3. The "mortality only" framing could understate the intervention if the primary benefit is on lung outcomes. This matters for robustness if the on-treatment mortality effect is small.
4. I can't offer a better-grounded estimate than the critique's range. I'm only arguing that its central value is unverified and less decision-relevant than it appears.

### Challenger
REBUTTAL: Post-TB lung disease morbidity as an unvalued channel

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: CG's BOTEC omits the channel by design, so it is conservative. The one interaction is that the 27 DALYs per averted death assumes full healthy life expectancy. If sequelae are as large as the critique says, that figure is overstated, and the overstatement partly cancels the added morbidity value.

1. **Conservative by construction is not a defense of the value.** The Advocate concedes the channel is omitted and probably positive. A conservative omission still biases the decision downward. That matters when the omitted value spans +5% to +140% of SROI (sensitivity run: low +4.8%, central +25.9%, high +140.4%).

2. **The 27-DALY offset is real but small.** I can size it with the critique's own inputs:
   - Morbidity per treated patient is 0.75 DALYs, so the haircut to a 27-DALY survivor is 0.75/27 ≈ 2.8%.
   - Per affected patient it is ~2.5 DALYs, so 2.5/27 ≈ 9.3%.
   - Applied to the ~216k baseline expected benefit, the offset is roughly 6k–20k DALYs.
   - That is about 11–36% of the critique's 55k central value, and well short of cancelling it.

3. **The offset's size depends on survivor excess mortality, which neither side has quantified.** This is the same pathway as Critique 2. Counting the offset here and not counting the corresponding benefit there would be inconsistent. The two should be netted in one combined term.

4. **Residual risk:** the net central uplift after the offset is roughly 35k–49k, or +16–23%. That is still a non-trivial positive.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

1. **Conceded:** the 5% reduction is ungrounded, and Menzies' 5.8 DALYs is total burden, not avertable burden. The critique said both itself and set 5% below the trial signal to allow for surrogate attenuation. The Advocate offers no evidence that the true effect is below 5%, so ungrounded does not mean overstated.

2. **The 0.75 baseline is unverified, but the verifier's evidence points one way.**
   - The Advocate says the disability weight is unverified, which is fair.
   - The verifier found the baseline "looks too low relative to Menzies" (~2.5M vs ~19M DALYs). It also flagged that the scopes differ (mortality and extrapulmonary cases included in Menzies).
   - So the scope difference limits how far the comparison goes. It is not a REJECTED verdict, and the unverified chain is more likely biased downward than upward.
   - I am not claiming 0.75 is wrong. I am saying the Advocate's objection identifies uncertainty without identifying a direction.

3. **On the 2025 Lancet Glob Health paper:** the Advocate says it shows burden size, not modifiability. That is correct as far as the verifier's summary goes. The paper models progressive lung damage and finds post-TB DALYs at 52.5% of the total with prompt treatment. I cannot ground whether it quantifies how much of that share an adjunct could avert. I treat it as supporting the size of the pool only.

4. **The evidence gap sits in one link, the persistence of an early radiographic effect.** That link is a conditional, not a rejection. If persistence holds even partially, the pool is large enough that the 2–15% range spans +5% to +140% on SROI.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: the central uplift is ~+25%, at the edge of materiality. The low end is ~5%, no run crosses the bar, and the extra probability branch is unsupported.

1. **The central case is above the Advocate's own threshold.** The sensitivity run gives +25.9%, which is over the ~25% cutoff, not at its edge. The Advocate also says "only in the favourable direction" as though that were a limitation. For a grant that BOTEC-values mortality only, upside-skewed omitted value is the relevant direction.

2. **The range is skewed.** Low is +4.8%, central +25.9%, high +140%. The mean of this distribution is above the central value.

3. **The probability-weight point is conceded.** Moving from 0.45 to 0.4 gives ~49k instead of ~55k, a ~11% change. The adoption-via-surrogate branch is thin. I do not rest on it.

4. **Discounting:** I accept the Advocate's annuity method, but applied consistently it slightly favors the critique. The baseline horizon is 27 years, and the post-TB channel is 15–25 years (20 as a midpoint).
   - At 3%: 20-year factor 0.744; 27-year factor (1 − 1.03⁻²⁷)/(0.03 × 27) ≈ 0.679. The ratio is ~1.10.
   - At 5%: 20-year factor 0.623; 27-year factor (1 − 1.05⁻²⁷)/(0.05 × 27) ≈ 0.549. The ratio is ~1.13.
   - So discounting lifts the channel's share of baseline by ~10–13% rather than inflating it. The critique's "partly an artifact" concession is overcautious, and the Advocate's neutral framing is slightly too generous to the baseline.

5. **Overlap with Critique 2 is allocation, not reduction.** The Advocate says it "reduces net uplift". Combining two channels on one pathway removes the double count. The combined pathway value (mortality plus morbidity from the same lung-damage effect) is larger than either alone. The overlap is a reason to merge the terms, not to discount this one.

**RESPONSE TO "OFFSETTING FACTORS":**

1. **The 27-DALY overstatement is real and in the model's direction, but small.** See the sizing above.

2. **Hepatotoxicity and myopathy:** these risks affect the mortality channel equally, and the 0.45 weight already includes p_success. Counting them against this channel again double-counts them. They are not channel-specific.

3. **Redundancy with short regimens:** the parameter map's "not considered" is an absence of analysis, not evidence of redundancy. The Advocate offers no magnitude. The 5% was already set below the trial signal for attenuation. I cannot ground a redundancy discount in either direction.

4. **Extra monitoring costs:** I cannot ground their size. Adverse-event monitoring applies to the mortality trial and delivery too, and the ~$7M Phase III is already in cost. Only lung-function follow-up beyond that would be incremental, and the Advocate does not size it.

**KEY UNRESOLVED QUESTIONS:**

- Does an atorvastatin-driven reduction in early chest X-ray lung damage persist into long-term function loss? This is the 5% driver, and neither side has evidence beyond the Phase IIa/b signal.
- How large is the survivor-haircut offset to the 27 DALYs? It needs excess-mortality data for post-TB survivors, and it should be netted together with Critique 2.
- What share of the 5.8 Menzies DALYs is morbidity only, versus mortality and extrapulmonary? This decides whether 0.75 per patient is low or reasonable.
- If the mortality endpoint fails (60% branch), would lung-only evidence ever lead to adoption? This is the Critique 4 question, and it determines whether the weight should be 0.40 or 0.45.
- Is the combined morbidity-plus-mortality post-TB pathway large enough to change the bar crossing once Critiques 2 and 3 are merged? Neither side has run that merged calculation.

### Judge Audit
Surviving strength: moderate
Justification: Both sides produced grounded syntheses: the Advocate's p = 0.4 recalculation and annuity method, and the Challenger's offset sizing and completed discounting comparison. These meaningfully narrowed the magnitude, and the direction of the critique (a positive omitted value) survived uncontested. However, the critique's central number depends entirely on a 5% effect that both sides concede is assumed. The Challenger defended it partly through a call to ignorance and overclaimed materiality at +25.9%. The Advocate missed the strongest available counter-evidence (ROSETTA). The critique therefore survives as a valid but modestly sized, upside-only refinement whose decision relevance is unestablished.
Recommended action: 2. SPECIFIC INVESTIGATION: Take three feasible steps:
- **Identify the source trial.** Confirm the atorvastatin Phase IIa/b trial and the size of its chest X-ray lung-damage effect. Compare it against ROSETTA's null rosuvastatin result on lung involvement and spirometry. If the signal is not robust across statins, cut the central reduction toward the 2% low end.
- **Run a single merged sensitivity for Critiques 2 and 3.** Apply one lung-damage reduction parameter to joint post-TB morbidity and mortality. Use p = 0.40, net out the 27-DALY survivor haircut (≈6–20k), and report discounted and undiscounted versions with back-loaded accrual (Menzies: 28% at 15+ years).
- **Interpret the result against the bar.** If the merged term does not cross the 134k bar at the 5% central, conclude that this channel is a real but non-decision-changing upward adjustment.

Both steps are feasible with existing tooling: a targeted literature search and a re-run of the BOTEC.
Action feasibility: requires_specified_evidence
Advocate failures: ['sound_synthesis_noted: Re-deriving the central estimate at p = 0.4 (≈49k), and using sensitivity-run figures (SROI ~3,055 → ~3,847, +26%; low end ≈10k/216k ≈ 5%). These are grounded in the verifier package and the run outputs.', 'sound_synthesis_noted: The annuity-factor derivation for discounting (0.74 at 3%, 0.62 at 5% over 20 years) is correct in method. However, the conclusion that "relative uplift barely changes" was asserted without computing the comparison factor for the 27-year baseline. The Challenger exposed this gap.', 'false_definitiveness: It sits at the edge of the ~25% materiality threshold" and "the case that the channel is material is weak." The Advocate\'s own cited figure (+26%) is at or above that threshold. The Advocate declares immateriality while the central estimate meets the stated cutoff. The stronger available point was that the 134k bar is never crossed, but the Advocate leans on "edge of threshold" framing instead.', 'call_to_ignorance: Offsetting factor 3: the lung benefit "may be partly redundant with the short-regimen improvements the parameter map flags as not considered." No magnitude or evidence is given. An unanalysed possibility is offered as an offset.', 'call_to_ignorance: Offsetting factor 4, unsized extra monitoring costs, is offered as an offset with no indication of magnitude. Offsetting factor 2 (hepatotoxicity/myopathy) concedes it is "weighted into p_success implicitly" yet still lists it against this channel. That is effectively a speculative double count.', 'misrepresenting_evidence_status (self-assessment inconsistency, noted for calibration): The body text concludes "Partial defense," but the self-assessment field says "strong." The body is the more accurate description. Judged on substance, this was a partial defense.']
Challenger failures: ["sound_synthesis_noted: The sizing of the 27-DALY survivor offset is properly derived from the critique's own inputs: 0.75/27 ≈ 2.8% and 2.5/27 ≈ 9.3%, giving ≈6k–20k on 216k and a net central of ≈35k–49k. The Challenger also correctly flags that excess survivor mortality is unquantified and belongs in the merge with Critique 2.", "sound_synthesis_noted: The discounting comparison of 20-year and 27-year annuity factors is a legitimate correction that completes the Advocate's half-derivation. There is a minor arithmetic slip: the 27-year factor at 5% is ≈0.542, not 0.549, which makes the ratio ≈1.15 and slightly strengthens the Challenger's point. The analysis also assumes uniform accrual. It does not address the back-loading of post-TB morbidity, which would reduce the ratio.", 'call_to_ignorance: The Advocate offers no evidence that the true effect is below 5%, so ungrounded does not mean overstated." This treats the absence of disconfirming evidence as support for an admittedly assumed parameter. The Challenger also passes over ROSETTA in the verifier package, which is directionally relevant evidence that a statin lung effect may be near zero.', 'false_definitiveness: The Challenger says "the unverified chain is more likely biased downward than upward" and in the same passage "I am not claiming 0.75 is wrong." It also concedes that the Menzies comparison is a different scope. The directional claim rests on a comparison the Challenger itself says doesn\'t transfer.', 'false_definitiveness: +25.9%, which is over the ~25% cutoff, not at its edge." A 0.9-point margin on an ungrounded central estimate is the edge. The Challenger also passes over the fact that no sensitivity run crosses the 134k bar. Separately, "the mean of this distribution is above the central value" is asserted without any stated distribution.', "strawmanning: Overlap with Critique 2. The Advocate argued that this channel's *net new* value is smaller than its standalone figure once Critique 2 is counted. The Challenger responds that the *combined pathway* is larger than either alone. That is true but answers a different claim. The incremental value attributable to this critique, given Critique 2, does fall."]
Debate resolved: The debate established the following:
- Valuing post-TB morbidity at zero is a genuine, upward-biasing omission, and the arithmetic reproduces.
- The 0.45 probability weight is unsupported; 0.4 (≈49k) is the defensible figure.
- The survivor-haircut offset to the 27 DALYs is small (≈6–20k), not cancelling.
- Discounting does not shrink this channel relative to the mortality baseline under uniform accrual.

Net standalone central uplift is roughly +16–23%, and no tested scenario crosses the 134k bar.
Debate unresolved: The decisive parameter, the 5% persistent reduction, remains ungrounded on both sides. Neither side engaged with ROSETTA's null lung-imaging and spirometry result, or with the fact that the source trial is unidentified.

The merged Critique 2 + 3 calculation was not performed. That leaves open whether the combined lung-damage pathway, net of overlap and the survivor haircut, is decision-relevant.

--- Critique: Post-treatment excess mortality (~40–50k central) and a related sign-reversing adjustment ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: Post-treatment excess mortality and a related sign-reversing adjustment

EXISTING COVERAGE:
1. The 27 DALYs per TB death is described in the CG BOTEC as "remaining healthy life expectancy",
   not standard life expectancy. Healthy life expectancy is already discounted for expected
   morbidity, so (b)'s premise, that deaths are valued at standard life expectancy, does not
   match the report. Some of the 5–10% overstatement is therefore likely already absorbed.
   I cannot ground how much. This is conditional reasoning, not a verified figure.
2. The parameter map lists post-treatment mortality as an implicit zero in the formula chain
   ("only mortality is valued"). That is a known, acknowledged omission, and it is conservative
   for channel (a). CG's chain leaves the upside out of the estimate.
3. The critique's own evidence concedes that post-TB mortality is already modelled in Menzies'
   per-case DALYs, so (a) overlaps Critique 1. Counting it here would double-count any benefit
   credited there.
4. The CG model already shrinks the effect with a 10% relative reduction and a 40% success
   probability. An additional excess-death channel stacks on a mortality-reduction assumption
   that has no stated derivation.

EVIDENCE WEAKNESSES:
1. The only grounded input to (a) is the ~2.9× background mortality in TB survivors (Romanowski
   2019). The critique itself marks as UNGROUNDED or illustrative:
   - the 10% cumulative excess,
   - the 40% respiratory share,
   - the 5% reduction.
   That is three of four multiplicands, so the ~45k figure is an illustration, not an estimate.
2. The mechanism for (a) has a gap. The prior Phase IIa/b signal was on infection clearance and
   chest X-ray lung damage, which are surrogates. Nothing cited shows that reduced radiographic
   damage translates into fewer deaths years later. The 5% figure assumes it does.
3. The critique treats the statin's own cardiovascular benefit over ~6 months as zero, which
   shows the benefit must come entirely from the lung-sparing pathway. That pathway is the least
   established part of the evidence.
4. For (b), the 5–10% "overstatement" is asserted without a derivation. The critique does not
   show how much of the 6% mortality sits in higher-baseline-mortality subgroups, and the
   parameter map itself flags that no such decomposition exists. The sign and size are
   hypothesis, not finding.
5. The "~45k after weighting" step has no shown derivation from ~100k, so I cannot check it.
   The visible arithmetic is 0.10 × 0.4 × 0.05 × 15 × 3.3M ≈ 99k.

MAGNITUDE CHALLENGE:
1. The Quantifier's own sensitivity on dalys_per_death shows:
   - low case (−10%): 3,055x → 2,749x;
   - central case (27.5 DALYs): 3,111x, a +1.85% change;
   - high case (+18.5%): 3,621x.
2. Neither the low nor the central case crosses the ~25% materiality threshold. The central
   case moves SROI under 2%. The high case (+18.5%) is also under 25%, and rests on the most
   weakly grounded inputs.
3. The critique's own net range of −25k to +45k, around a ~535k baseline, is about −5% to +8%.
   That is far below the stated materiality threshold, even though the label says "material".
4. The two adjustments partly offset each other. The critique concedes "a net-zero effect is
   possible." A decision-relevant finding needs a directional case, and this critique
   explicitly lacks one.
5. The high case treats a 5% reduction in post-treatment respiratory deaths as plausible.
   CG's own on-treatment assumption is a 10% relative reduction, and that is conditional on
   success. Assuming a downstream effect half that size on a distant, indirectly caused
   outcome is not obviously conservative.

OFFSETTING FACTORS:
1. (a) and (b) offset each other directly. Both concern the post-treatment survival of the same
   population, so they should be evaluated jointly, as the critique itself says. The joint net
   is ≈0 at the midpoint.
2. Other omissions in the CG model carry the opposite sign. The parameter map lists morbidity
   DALYs and transmission-averted cases as implicit zeros (upside), and lists hepatotoxicity and
   reduced rifampicin-induced statin exposure as unmodelled (downside). Whether or not these
   net out, a one-channel adjustment to dalys_per_death is not a reason to move the headline.
3. As the parameter-map entry notes, the 10% relative-reduction input has a far larger plausible
   range than the DALY-per-death figure. The headline is more sensitive to relative_reduction
   and p_success than to the 27-DALY input.

OVERALL ASSESSMENT:
Strong defense.
- The critique's own strength rating is low–medium, and its net range is roughly ±5–8%.
- The Quantifier's sensitivity does not cross the materiality or bar thresholds.
- The upside channel overlaps Critique 1 and depends on three ungrounded multiplicands. The
  downside channel's premise, standard life expectancy, is at least partly contradicted by the
  report's "healthy life expectancy" wording.

CONCESSIONS:
1. The "Estimated Direction: decreases" label is ambiguous, as the critique says. The net sign
   is genuinely unclear.
2. CG gives no explicit statement of how the 27 DALYs treats survivors' excess mortality or
   comorbidity (the parameter map confirms this). Some downward pressure on dalys_per_death is
   plausible, though it is probably modest.
3. Post-treatment benefits are a real, unmodelled upside in principle. The conservative omission
   is genuine, but its size is unquantified.
4. If channel (a) overlaps Critique 1, the merge should be done once, not by adding both.
```

### Challenger
REBUTTAL: Post-treatment excess mortality and a related sign-reversing adjustment

**Overall:** The Advocate's magnitude argument is largely correct. My rebuttal narrows the critique to what survives, and I don't claim it is more than a low-materiality flag.

---

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: CG's 27 DALYs is "remaining healthy life expectancy," not standard life expectancy. It is therefore already discounted for morbidity, and some of the 5–10% overstatement in (b) is probably already absorbed.

Response:

1. Healthy life expectancy discounts for years lived in ill health. Channel (b) concerns something different: the *probability of surviving to realize those years* in a subpopulation with higher baseline mortality (HIV, malnutrition, advanced disease).
2. A HALE-based figure fixes the morbidity weighting but says nothing about whether the life table used reflects TB patients' elevated mortality. The Advocate's reading conflates the two.
3. The Advocate concedes "I cannot ground how much" is absorbed. The parameter map, by the Advocate's own concession 2, contains no explicit statement of how 27 DALYs treats survivors' excess mortality or comorbidity. That makes this UNVERIFIABLE, not REJECTED. The wording gives partial, not full, coverage of (b).
4. The Advocate's own concession 2 says some downward pressure on dalys_per_death is plausible. That is a concession that (b) has residual force.

> The Advocate claims: post-treatment mortality is an implicit zero in CG's chain, which is conservative for (a), and any (a) benefit also overlaps Critique 1, so counting it would double-count.

Response:

1. These two framings pull against each other. If CG's chain really values only on-treatment mortality, the omission is a genuine, unquantified upside. If Menzies' per-case DALYs already include post-TB mortality (verifier item 1), the benefit is already credited elsewhere.
2. The Advocate uses whichever framing neutralizes the point at hand. The honest position is that it is unresolved which path CG's headline number actually runs through.
3. I concede the merge should be done once, not additively (Advocate concession 4). That is a bookkeeping fix. It does not dispose of the residual sign question.

---

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: only the 2.9× background mortality is grounded. The 10%, 40% and 5% multiplicands are ungrounded, so the ~45k figure is illustrative rather than an estimate.

Response:

1. I concede this. Three of four multiplicands are ungrounded, and the critique says so itself.
2. I also concede the Advocate's point that the ~100k→~45k weighting step has no shown derivation. The visible arithmetic gives ≈99k. I cannot reconstruct the 45k and will not defend it. Treat it as an uninformed prior.

> The Advocate claims: the Phase IIa/b signal is on surrogates (infection clearance, chest X-ray damage), and nothing shows radiographic benefit translates into fewer deaths years later.

Response:

1. This is a fair point about the mechanism, and it is a gap in the critique.
2. It cuts against the *size* of (a), not its *direction*. The critique does not need the surrogate link to be proven. It needs only that the link not be zero.
3. I have no verifier-package evidence on the surrogate-to-mortality link. From memory only, and not in the evidence package: Pasipanodya et al. (Chest, 2007) documented persistent pulmonary impairment in a large share of treated TB patients. That supports plausibility of the mechanism, not any particular magnitude.
4. Romanowski 2019 (2.9×) establishes that excess mortality exists. It does not apportion it to respiratory causes. That 40% remains ungrounded.

> The Advocate claims: the 5% reduction in post-treatment deaths is not obviously conservative, given CG's own on-treatment effect is 10% conditional on success.

Response:

1. This is a reasonable challenge. I cannot ground 5% as either lower or higher than the true downstream effect.
2. I do not defend it as conservative. It is simply unanchored in both directions.

> The Advocate claims: the 5–10% for (b) has no derivation, and the parameter map flags that no subgroup decomposition exists.

Response:

1. Agreed that (b) is hypothesis. The absence of a decomposition is exactly why the critique is UNVERIFIABLE rather than rejected.
2. The Advocate cannot show the overstatement is zero either. It is a modeling choice CG has not documented.

---

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: sensitivity shows low −10%, central +1.85%, and high +18.5%, none crossing the 25% threshold. The critique's own net range of −25k to +45k is about −5% to +8% of the 535k baseline.

Response:

1. I concede the arithmetic. The Quantifier output (3,055x → 2,749x / 3,111x / 3,621x) shows no bar-crossing at any point.
2. The minimum plausible magnitude is ≈0, as the critique itself says ("net-zero effect is possible"). I cannot argue otherwise.
3. The only residual point is that the downside tail (−10% on dalys_per_death) and the upside tail (+18.5%) are each non-trivial. A single-parameter ±10–18% band is not nothing for a headline that already carries wide uncertainty on other inputs. But on this evidence, it does not move the decision.
4. The Advocate calls the net midpoint ≈0. The critique's range (−25k to +45k) has a midpoint near +10k, a mildly positive sign. That is within noise given the ungrounded inputs, so I do not press it.

---

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: (a) and (b) offset each other. Other omissions (morbidity DALYs, transmission averted, hepatotoxicity, reduced statin exposure under rifampicin) carry both signs, so a one-channel adjustment is no reason to move the headline.

Response:

1. The (a)/(b) offset is real in the critique's own framing, but it is a coincidence of two unquantified guesses, not a demonstrated cancellation.
2. The other omissions are listed as unmodelled in the parameter map. They are not quantified. "Whether or not these net out" is an admission that the offset is hypothetical. Unquantified opposing omissions justify symmetric uncertainty, not a point estimate of zero.
3. The claim that the headline is "more sensitive to relative_reduction and p_success" is true but answers a different question. It ranks parameters by importance. It does not show this adjustment is zero.

---

**KEY UNRESOLVED QUESTIONS:**

- Does CG's 27 DALYs per death use a life table or healthy-life-expectancy figure that reflects TB patients' elevated baseline mortality (HIV, malnutrition), or a general-population figure? The parameter map is silent, so this is UNVERIFIABLE.
- Is post-TB mortality credited through Menzies' per-case DALYs in the headline path, or is it truly an implicit zero? The Advocate's two framings conflict, and the answer determines whether (a) is a double-count or a conservative omission.
- What fraction of excess post-TB mortality is respiratory? The Romanowski 2.9× figure does not answer this, and the 40% remains an uninformed prior.
- Does reduced chest-X-ray lung damage translate into reduced late mortality at all? No evidence in the package addresses this.

### Judge Audit
Surviving strength: weak
Justification: The Challenger explicitly conceded the magnitude arithmetic, the ungrounded multiplicands, the underived 45k figure, and the absence of any bar-crossing. It retained only a "low-materiality flag." The Challenger's best moves did expose a real conceptual error (HALE ≠ survival adjustment) and an inconsistency in the Advocate's coverage framing. However, these affect bookkeeping and sign clarity, not decision relevance. The critique survives only as a sign-ambiguous, sub-threshold adjustment.
Recommended action: 1. CONCLUDE NOW: With moderate-high confidence, this critique does not move the cost-effectiveness estimate past any decision threshold. The net effect is sign-ambiguous and within roughly ±8%.

   - Merge channel (a) into Critique 1 as a single entry.
   - Record (b) as a plausible-direction, unquantified downward pressure on dalys_per_death.
   - Do a cheap bookkeeping check: read the CG BOTEC formula chain to determine whether post-TB mortality enters through Menzies' per-case DALYs or is excluded, and whether the 27-DALY figure uses a general-population or TB-adjusted life table. This is feasible directly from existing documents, and it resolves the double-count question without new research.
Action feasibility: actionable_now
Advocate failures: ['strawmanning: Existing Coverage #1 argues that because the 27 DALYs is "remaining *healthy* life expectancy," part of (b)\'s overstatement is "already absorbed." This is a category swap. HALE discounts for morbidity while alive. Critique (b) concerns reduced survival probability in a high-baseline-mortality subpopulation, which HALE does not address. The Advocate did hedge ("conditional reasoning, not a verified figure"), which softens the failure but does not fix the conflation. The Challenger correctly caught it.', 'false_definitiveness: Offsetting Factors #1: "The joint net is ≈0 at the midpoint." The critique\'s own range (−25k to +45k) has a midpoint of about +10k. Rounding this to zero, while relying elsewhere on ungrounded inputs, overstates how cleanly the channels cancel. The error is small in magnitude, but it is asserted with confidence.', 'whataboutism: Offsetting Factors #2–3 point to other unquantified omissions of both signs ("whether or not these net out") and note that the headline is more sensitive to relative_reduction and p_success. Neither point bears on whether this channel is real or what size it is. Both deflect to other parts of the model.', "sound_synthesis_noted: Magnitude Challenge #3 converts the critique's net range against the 535k base into −5% to +8% (25/535 ≈ 4.7%, 45/535 ≈ 8.4%). It also correctly reads the Quantifier sensitivity (−10% / +1.85% / +18.5%) against the 25% threshold. This is grounded and was the decisive move of the debate. Evidence Weakness #5, which points out that the 100k→45k weighting step is underived, is also a legitimate, checkable catch."]
Challenger failures: ['call_to_ignorance: The Advocate cannot show the overstatement is zero either." Also: the critique "needs only that the link not be zero." Both shift the burden by treating unproven non-zero effects as residual support. The Challenger mostly corrects for this by explicitly declining to press magnitude.', 'sound_synthesis_noted: The Challenger made several correct and specific moves:']
Debate resolved: The debate established that the critique is not decision-relevant at current evidence:
- Both sides agree the net effect is roughly −5% to +8% of the relevant base.
- No Quantifier scenario crosses the materiality threshold.
- Three of the four multiplicands in (a) and the entire magnitude of (b) are ungrounded.
- The 45k weighting figure is unreconstructable.

It also established that channel (a) must be merged with Critique 1 once, not added to it.
Debate unresolved: Two questions remain open:
- Does CG's headline path credit post-TB mortality (through Menzies) or treat it as an implicit zero? The Advocate asserted both, and the answer determines whether (a) is a double-count or a conservative omission.
- Does the 27-DALY figure use a life table that reflects TB patients' elevated baseline mortality? The HALE wording does not answer this.

--- Critique: Transmission benefit is small, with a bounded calculation (~10–30k central) ---

### Advocate
DEFENSE OF GIVEWELL'S (CG's) POSITION: Transmission benefit is small (~10–30k DALYs central)

**Framing note.** This critique mostly supports CG's treatment. It says the omitted transmission channel is small, so valuing only mortality loses little. My defense is that omitting it is reasonable and does not move the decision. This is the one place the critique could count against CG, as a small upward bias in the estimate if it is included.

EXISTING COVERAGE:
- CG states that "only mortality is valued." The parameter map lists transmission-averted cases as an implicit zero.
- The omission is a visible simplification and errs conservative. Any positive transmission term raises SROI, so ignoring it does not inflate the 3,000x headline.
- CG's formula has no time discounting. Secondary cases arise years after the index case, so a properly discounted transmission term would be worth less than the undiscounted ~20–50k DALYs.
- The 1-year speedup framing already limits the benefit window. Transmission credit accrues only to the one cohort-year of accelerated adoption.

EVIDENCE WEAKNESSES:
- The Quantifier labels the key inputs UNGROUNDED: the 1–5% post-start transmission share, the 10–20% fractional reduction, and the 0.3% net reduction. I treat them as an order-of-magnitude placeholder. I can neither confirm nor refute them, so the ~10–30k figure carries little weight.
- The guinea-pig evidence is thin for this use. The cited MDR-TB experiment shows 26.7% of animals infected before treatment and 27.8% at 72 hours. This is a single experiment, in animals, in MDR-TB, which is a different setting from drug-susceptible TB, where 96% of CG's cases fall. I have not independently verified these figures; I take them from the Quantifier's package.
- The same guinea-pig result is used for two opposite purposes. It "weakens the case" for incremental benefit and also "keeps an upper tail alive." The evidence cannot support a heavy upper tail while also supporting a low central value.
- The ROSETTA trial tested rosuvastatin, whereas CG's grant concerns atorvastatin. The critique itself says it cannot confirm this is informative about the actual trial.
- The 0.5 secondary cases per index case is an "inference." Many infections become latent rather than active disease, and the critique does not separate the two.

MAGNITUDE CHALLENGE:
- The Quantifier's own sensitivity run shows no decision-relevant movement:
  - Baseline is 3,054.9.
  - Low (+0.56%) gives 3,071.8.
  - Central (28.26 DALYs per death, +4.67%) gives 3,197.4.
  - High (+18.7%) gives 3,626.2.
  - None crosses the bar ("crosses_bar" is false everywhere), and none exceeds the ~25% materiality threshold.
- The "Materiality: material" label contradicts both the critique's own "Strength: low / least material channel" and this sensitivity output.
- The injection into `dalys_per_death` looks inconsistent with the stated derivation.
  - The critique's calculation gives ~50k DALYs pre-probability-weighting, or ~20k after the 40% weighting.
  - The central value of 28.26 adds 1.26 DALYs per death, which is about 1.26 × 19,900 ≈ 25k DALYs. This matches neither figure.
  - If the 20k is already p-weighted, entering it through `dalys_per_death` double-applies the 40%, because the SROI formula multiplies by 40% again.
  - If the pre-p figure of 50k is used, the add-on is 50k / 19,900 ≈ 2.5 DALYs per death, so 29.5 in total.
  - Scaling linearly, SROI ≈ 3,054.9 × 29.5 / 27 ≈ 3,338, a change of about +9%. This is still well under 25%.
- Two downward adjustments, which the critique itself names, are not in the central number:
  - Culture conversion at 8 weeks is an imperfect proxy for infectiousness.
  - Incidence is declining at 2% per year.
- Two other considerations plausibly push the estimate down, though I cannot ground them quantitatively:
  - The lag before secondary cases appear, with no discounting applied.
  - The share of secondary infections that become latent rather than active disease.

OFFSETTING FACTORS:
- CG omits other positive channels too: morbidity, lung-damage reduction, and diagnostic value. Their omission pushes the estimate down by more than transmission does. The total conservatism of "mortality only" is therefore larger than this channel, and the critique correctly concludes this single channel is small.
- Counting transmission would require a defensible link between culture conversion and infectiousness. That link is weakly established and would add model complexity without clear accuracy gain.
- The critique's own downward flags (weak conversion signal, imperfect proxy, saturation) mean the likely correction is toward the low end, around +0.5% to +5%.

OVERALL ASSESSMENT: **Strong defense.**
- The omitted channel is small relative to the ~25% materiality threshold at the Quantifier's own central and low values.
- Its inputs are acknowledged as ungrounded.
- Its direction is only upward and small, so it does not threaten the conclusion that the grant clears the bar.

CONCESSIONS:
- Omitting transmission is a small upward-correctable bias in CG's estimate. Strictly, an accurate estimate would include a small positive term.
- The upper tail is not negligible. The critique's own ~150k DALY upper bound would give 34.5 DALYs per death (150k / 19,900 ≈ 7.5 added), or SROI ≈ 3,054.9 × 34.5 / 27 ≈ 3,903 (+28%). That would cross the 25% threshold, though it requires stacking the most favorable ungrounded inputs.
- CG gives no reasoning for omitting transmission beyond "only mortality is valued." The omission is defensible but undocumented.

### Challenger
REBUTTAL: Transmission benefit is small, with a bounded calculation (~10–30k central)

**Framing.** The Advocate and the critique largely agree that this channel is small and that omitting it errs conservative. I concede that conclusion and rebut only the specific sub-arguments that don't hold, plus the residual risk.

---

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: omitting transmission is conservative, so it cannot inflate the 3,000x headline.

Response:
- Directionally correct, and I concede it.
- "Doesn't inflate" is not the same as "is captured." CG's only treatment is the phrase "only mortality is valued," which the Advocate concedes is "defensible but undocumented." The channel is not modeled at all.

> The Advocate claims: the model has no time discounting, so a properly discounted transmission term would be worth less than the undiscounted ~20–50k.

Response:
- If the model does not discount mortality DALYs, a transmission term entered on the same convention should also be undiscounted.
- Discounting only the omitted channel would put it on a different basis from the one CG applies to everything else.
- The discounting argument therefore does not reduce the like-for-like value of the term. It only shows that the term is uncertain.

> The Advocate claims: the 1-year speedup framing limits transmission credit to one cohort-year.

Response:
- I accept this, and the critique's 3.3M base already reflects a single cohort.

---

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the guinea-pig result is used for opposite purposes, supporting both a low center and a heavy upper tail.

Response:
- The two uses are compatible. They are two parts of one finding.
- Infectiousness drops sharply with effective therapy. That supports a low central value.
- The same experiment shows infectiousness at 72 hours (27.8%) equal to pre-treatment (26.7%). That shows the early-treatment window is not reliably near zero, so the upside is not zero.
- A wide interval with a low center is the expected shape when evidence points in both directions.

> The Advocate claims: the MDR-TB animal setting differs from drug-susceptible TB, where 96% of cases fall.

Response:
- I concede the transferability limit.
- Persistent early infectiousness in MDR-TB may reflect less effective regimens. If so, it overstates the DS-TB tail, and the upper tail should be trimmed accordingly.
- The verifier did not mark this evidence REJECTED, so it remains weak evidence, not refuted evidence.

> The Advocate claims: ROSETTA tested rosuvastatin, not atorvastatin, so it is uninformative.

Response:
- I concede this. The critique itself says it cannot confirm the finding for the actual trial.
- It supports shrinking the channel only conditionally.

> The Advocate claims: many infections become latent, and the critique does not separate latent from active.

Response:
- This misreads the critique. The mechanism line counts "direct secondary disease cases per index case: ~0.3–1," which already means active disease, not infections.
- The latent-share objection therefore double-counts a discount already in the input.
- The critique's count is direct cases only. It excludes tertiary and later generations, which is an omitted upward residual (see below).

---

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: the sensitivity run shows no decision-relevant movement, and the injection into `dalys_per_death` is inconsistent with the stated derivation.

Response on the sensitivity output:
- I concede that none of the low/central/high values crosses the bar or the ~25% threshold.
- I also concede that "Materiality: material" conflicts with the critique's own "Strength: low."

Response on the claimed inconsistency:
- The sensitivity implies 28.26 − 27 = 1.26 added DALYs per death. This ratio is checkable from the output: 3,197.4 / 3,054.9 = 1.0467 = 28.26 / 27.
- Converting to total DALYs depends on the Advocate's 19,900 deaths-averted figure. It is not in the verifier package, and I cannot independently ground it. I treat it as the Advocate's input.
- On that figure, 1.26 × 19,900 ≈ 25k, which sits inside the critique's stated "~10–30k central" range and close to the 20k p-weighted figure. It is not clearly inconsistent.

Response on the Advocate's own correction:
- The Advocate argues that if the 20k is already p-weighted, then entering it as `dalys_per_death` double-applies the 40%. That argument is unverified, because I do not have the SROI formula.
- Taking the correction at face value, the Advocate computes +9% on the pre-p 50k. That is about twice the sensitivity central of +4.67%.
- That contradicts the Advocate's later claim that "the likely correction is +0.5% to +5%." The Advocate's own corrected central exceeds its own stated range.

Upward residual not in the central figure:
- The critique counts only direct secondary cases. If each case's own secondary cases are also counted, the multiplier is the geometric sum 1/(1−R), where R is secondary cases per case.
- With R = 0.5 (the midpoint of the critique's 0.3–1 range, my choice), the multiplier is 2.
- Applied to the Advocate's 50k pre-p figure, that gives 100k, or 5.03 DALYs per death. SROI would be roughly 3,054.9 × 32.0 / 27 ≈ 3,620, about +18.5%.
- This is still below 25%, but it is much closer than the Advocate's +5%.
- The two downward flags (imperfect conversion proxy, saturation) cut against this. Neither side has quantified them.

Residual:
- The defensible range is about +0.5% to ~+18% at moderate assumptions. It reaches +28% at the upper bound, as the Advocate concedes.
- It is not tightly bounded at +5%.

---

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: other omitted channels (morbidity, lung damage, diagnostics) mean total conservatism exceeds this channel, so the critique correctly concludes this one is small.

Response:
- Those channels are not offsets. They are additional omitted upward terms, in the same direction as transmission.
- They show that the headline is conservative on several axes at once. They do not show that transmission alone is negligible.
- Those channels have no quantification in the package, so they neither shrink nor enlarge this one.

> The Advocate claims: counting transmission requires a defensible link between culture conversion and infectiousness, which is weak.

Response:
- This is a fair objection to precision.
- It does not support a zero value. The critique's own derivation still supports a positive term of order 10–50k DALYs.

---

**KEY UNRESOLVED QUESTIONS:**
- How does the SROI formula treat the 40% probability weight? This determines whether the sensitivity injection understates the channel by 2.5×.
- Where does the 19,900 deaths-averted figure come from, and is it the right base for converting DALYs per death?
- Is the effect on infectiousness a function of culture conversion at all, given the "regardless of culture status" evidence? If not, the channel shrinks toward zero, because the trial's effect operates through conversion.
- What is the true R for DS-TB cases that would be attributed to the post-start window? This sets the higher-generation multiplier.
- Does the trial being evaluated show a real culture-conversion effect, or a null like ROSETTA? Nothing in the package answers this.

### Judge Audit
Surviving strength: moderate
Justification: The critique's core claim survived intact and was largely endorsed by both sides: the channel is small, positive in expectation, and immaterial at the central estimate. Both sides produced sound, checkable syntheses (the Advocate's `dalys_per_death` re-derivation and the Challenger's geometric multiplier), and the Challenger won several grounded sub-points (discounting, latency, the Advocate's internal inconsistency). The rating stays at moderate rather than strong because:
- the key inputs remain UNGROUNDED per the verifier,
- both sides offered at least one under-grounded range,
- neither side resolved whether the mechanism operates through culture conversion at all, which could take the channel to roughly zero.
Recommended action: 1. CONCLUDE NOW, with moderate-to-high confidence:
   - Omitting the transmission channel is a small, conservative bias. The central estimate is about +2% to +9% on SROI, and it does not affect the funding decision.
   - The upper tail can approach or exceed 25% only by stacking the most favorable ungrounded inputs: pre-p weighting, a higher-generation multiplier, and a post-start share near 5%.
   - CG should document the omission and its rationale explicitly, rather than relying on "only mortality is valued."
   - A cheap side-check, feasible from CG's existing spreadsheet, would settle the factor-of-2.5 ambiguity in the sensitivity injection: confirm how the 40% probability weight enters the SROI formula and source the 19,900 deaths-averted base.
   - The critique's "Materiality: material" label should be corrected to "not material."
Action feasibility: actionable_now
Advocate failures: ['unsupported_estimate_counter: the likely correction is toward the low end, around +0.5% to +5%." No derivation is given for this range. It also contradicts the Advocate\'s own derivation two sections earlier, which put the corrected central at about +9% (29.5 / 27). The range was offered to shrink the critique\'s number, but it rests on less grounding than the Advocate\'s own calculation. The Challenger correctly caught this.', 'unsupported_estimate_fabricated: CG omits other positive channels too: morbidity, lung-damage reduction, and diagnostic value. Their omission pushes the estimate down by more than transmission does." This is a comparative magnitude claim with no quantification, and nothing in the verifier package addresses those channels. The framing as "offsetting factors" is also a direction error. These channels are additional omitted upward terms, not offsets, as the Challenger noted.', 'strawmanning: Many infections become latent rather than active disease, and the critique does not separate the two." The critique\'s mechanism explicitly counts "direct secondary disease cases per index case," which already means active disease. This is a category swap from infections to disease cases. The Challenger correctly identified it.', 'strawmanning: The same guinea-pig result is used for two opposite purposes... The evidence cannot support a heavy upper tail while also supporting a low central value.', 'false_definitiveness: The self-assessment is "Strong defense," yet the Advocate concedes that the upper bound gives about +28% and crosses the 25% threshold. The Advocate\'s own corrected central (+9%) also exceeds its stated likely range.', 'sound_synthesis_noted: The `dalys_per_death` re-derivation (50k / 19,900 ≈ 2.5 added, SROI ≈ 3,338, about +9%) and the upper-tail computation (150k gives about +28%) show every step.']
Challenger failures: ['sound_synthesis_noted: The higher-generation multiplier 1/(1−R) with R = 0.5 gives ×2, 100k DALYs, about 5.03 per death, and SROI ≈ 3,620 (+18.5%). The steps are shown and the assumption is flagged as "my choice." The multiplier logic is sound in principle: each averted secondary case also averts its own downstream chain.', 'unsupported_estimate_counter: The defensible range is about +0.5% to ~+18% at moderate assumptions." The +18% figure stacks two choices: the pre-p base the Challenger had just called unverified, and the multiplier. Labelling that stack "moderate assumptions" overstates its grounding. It is a conditional upper-middle scenario, not a defensible central range.', 'false_definitiveness: It does not support a zero value. The critique\'s own derivation still supports a positive term of order 10–50k DALYs." Yet the Challenger\'s own unresolved questions concede two things:']
Debate resolved: Both sides agree that the transmission channel is a small, conservative omission whose central value (about +2% to +9% on SROI) is well below the ~25% materiality threshold and does not change whether the grant clears the bar. The exchange also discarded several sub-arguments:
- the discounting objection,
- the latent-infection objection,
- treating other omitted channels as "offsets",
- the Advocate's +0.5–5% likely range, which is inconsistent with its own +9% derivation.
Debate unresolved: Two upper-tail questions remain open:
- Whether the tail realistically reaches the 25% threshold. This depends on how the 40% probability weight enters the SROI formula and whether a higher-generation multiplier applies.
- More fundamentally, whether an adjunct that speeds culture conversion has any transmission lever at all, given the evidence that infectiousness falls with effective therapy regardless of culture status, and given no confirmed conversion effect in the actual trial.

--- Critique: The sweat-based diagnostic carries real option value but is speculative (~10–30k central) ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION: The sweat-based diagnostic carries real option value but is speculative (~10–30k central)

**EXISTING COVERAGE:**
- CG's BOTEC states that "only mortality is valued." The diagnostic is mentioned only as context, so zero is an explicit scoping choice, not an oversight. The parameter map confirms diagnostic value is an implicit zero.
- The BOTEC holds "the share of cases being treated" constant. A diagnostic that raised case detection would contradict that assumption in the statin benefit chain. Keeping the two benefit streams separate is therefore internally coherent. The statin SROI is a claim about the statin pathway only.
- The $7M all-in cost is described as covering "later Phase III trials, guideline changes, dissemination and validation." No diagnostic costs are listed. On the text as published, the omitted-benefit-with-included-cost problem is not established. The parameter map itself calls this "unclear."
- I cannot ground the size of the diagnostic workstream relative to the $320k or the $7M. If the workstream is inside the cost base, the critique's bias argument holds to that extent (see Concessions).

**EVIDENCE WEAKNESSES:**
1. **The critique is self-labelled ungrounded.**
   - The Quantifier marks P(adoption) ~5% as "UNGROUNDED... not a figure from a source."
   - The "1–3% of incidence" incremental-detection figure is also uncited.
   - The Quantifier's own evidence section calls the 1–3% base "uncertain" and says displacement "could push the value toward the low end."
   - Every multiplicative term in the 50k figure is therefore an uninformed prior, and the product inherits that.
2. **The per-case DALY figure is inconsistent with CG's model.**
   - The critique uses ~20% untreated case fatality × ~25 DALYs = 5 DALYs per case. That treats diagnosis as eliminating all mortality risk.
   - CG's BOTEC assumes treated drug-susceptible mortality of ~6%, at 27 DALYs per death.
   - Using CG's own parameters, the net gain is (20% − 6%) × 27 ≈ 3.8 DALYs per case. That is about 24% lower than 5, and the 20% fatality figure is itself ungrounded.
3. **The evidence cited undercuts the thesis.**
   - The WHO tongue-swab and NPOC endorsement, as the critique describes it, narrows the gap a sweat test would fill.
   - The paediatric and no-sputum gap is a real opening, but the critique offers nothing showing sweat-based testing can reach adequate sensitivity.
   - The critique concedes a sweat test "would need its own evidence pathway and WHO policy review."
4. **The critique does not model grant pivotality.**
   - The grant funds "work on" a sweat diagnostic. The critique values the diagnostic's total annual adoption benefit.
   - It never estimates how much of that value this grant causes, or how many years it accelerates adoption.
   - The statin side of the BOTEC credits only a 1-year speedup. The diagnostic side needs the same treatment.
   - The critique's "delay and counterfactual displacement" haircut is a single unexplained step.

**MAGNITUDE CHALLENGE:**
1. **The scale is small relative to the benefit term.** CG's benefit is 539,500 DALYs.
   - The critique's central range of 10–30k DALYs is 1.9–5.6% of that figure.
   - Even the top of its 0–100k range is ~18.5%, below the ~25% decision-relevance threshold.
   - By the critique's own numbers, nothing in the stated range moves SROI by 25% or more.
2. **The sensitivity run does not match the critique's stated central.**
   - The run varies `relative_reduction`, and the Quantifier central is 0.1094 against a baseline of 0.10. That is +9.4%, giving 3,342x against 3,055x.
   - 9.4% × 539,500 ≈ 50.7k DALYs. That is the pre-haircut figure (0.05 × 200k × 5 = 50k), not the 10–30k central the critique says it prefers.
   - The "high" case, +14%, corresponds to ~75k DALYs.
   - At the stated central of 10–30k, the shift is +1.9% to +5.6%, so SROI moves from ~3,055x to roughly 3,110–3,225x.
   - The sensitivity output therefore overstates the critique's own central estimate by about 2–5×. Even so, `crosses_bar` is false everywhere.
3. **The "material" label does not follow.** The sensitivity results show no crossing of the 2,000x bar, since the SROI only rises. They show no change above 25% in any case. The materiality tag is not supported by the numbers supplied.
4. **A recurring annual figure is compared to a speedup term.**
   - The 50k is an annual steady-state benefit of adoption.
   - CG's 539.5k is a one-year speedup benefit.
   - Putting them on the same footing requires the grant's contribution to diagnostic timing, which the critique does not estimate.

**OFFSETTING FACTORS:**
- **Displacement, per the critique itself.** It notes that tongue-swab PCR and NPOC are moving fast and that displacement pushes value to the low end.
- **Delivery costs.** Diagnostic benefits require procurement, lab or point-of-care infrastructure, and health-worker time. None of this is netted out of the 50k.
- **Adoption risk beyond 5%.** Policy review, manufacturing and rollout are further hurdles. The 5% base rate for early-stage diagnostics is ungrounded and could be lower.
- **No-discounting symmetry.** The BOTEC applies no time discounting. A diagnostic adopted after additional delay would be worth less under any discounting, and the critique's "delay" haircut is unspecified.

**OVERALL ASSESSMENT:** Strong defense on materiality; the critique is honest but weak in evidence.
- The critique's own central range is 2–6% of the benefit term, and its upper bound is below the 25% threshold.
- The critique says its numbers are ungrounded and its direction is uncertain.
- The sensitivity run overstates the stated central by roughly 2–5×.
- The per-case DALY calculation ignores CG's own 6% treated-mortality assumption.
- The pivotality of this grant for the diagnostic is never estimated.
- The residual weakness is a scoping and cost-attribution matter rather than a numeric one. I rate this "Strong", because the decision-relevant claim fails on the critique's own arithmetic.

**CONCESSIONS:**
1. **Direction.** Valuing the diagnostic at zero is an omission that biases the estimate downward, if only slightly. CG's BOTEC could say so explicitly.
2. **Cost attribution.** If diagnostic funding is inside the $7M all-in cost, the zero-benefit treatment is inconsistent. The BOTEC text does not resolve this, and I cannot either. It should be clarified from the model, as the critique suggests.
3. **Residual gap.** A paediatric or no-sputum diagnostic could have value that WHO's tongue-swab scope does not cover, so a non-zero option value is plausible. This concession is on direction, not on size, and the supporting evidence is only that the tongue-swab recommendation is limited to adults and adolescents who cannot give sputum.

### Challenger
REBUTTAL: The sweat-based diagnostic carries real option value but is speculative (~10–30k central)

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: zero diagnostic value is an explicit scoping choice ("only mortality is valued"), and keeping the diagnostic stream separate from the statin chain is internally coherent. The $7M cost description lists no diagnostic costs, so omitted-benefit-with-included-cost is not established.

- **Scoping is not the same as unbiased.**
  - The critique does not say the omission is incoherent. It says it is one-directional: a nonzero true value is set to zero.
  - The Advocate concedes direction (Concession 1), so we agree on sign.
  - Coherence of separate streams does not answer whether the cost side is also separated.
- **The Advocate's own evidence points toward cost inclusion.**
  - In Evidence Weakness 4, the Advocate says "the grant funds 'work on' a sweat diagnostic."
  - If so, at least the direct grant cost (~$320k) pays for diagnostic work while the benefit term assigns it zero.
  - This sits uneasily with "the omitted-benefit-with-included-cost problem is not established."
  - The Advocate also says it cannot size the diagnostic workstream, so neither of us can say how much of the cost base is affected.
  - This is conditional: if the workstream is in the denominator, the bias is real. I cannot show that it is.
- **Where I agree with the Advocate.** The BOTEC text as published lists no diagnostic costs for the $7M. I cannot show otherwise. The critique already said this question should be resolved from the model, and the Advocate agrees.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: every multiplicative term is ungrounded, so the product is an uninformed prior.

- **Conceded.** The critique labels P(adoption)≈5% and the 1–3% incremental detection as ungrounded. I do not defend them as sourced.
- **One term is partly anchored.**
  - The verifier found that the WHO tongue-swab recommendation covers adults and adolescents who cannot produce sputum. Children and others are outside it.
  - From memory of the WHO Global TB Report (2023–24 editions), children are roughly 12% of incident TB, about 1.2–1.3M of ~10.8M. I am recalling this, not quoting it, so treat it as approximate.
  - On that basis, 1–3% of incidence is roughly 8–25% of the paediatric segment alone.
  - That makes the range plausible but not demonstrated. I cannot ground what fraction a sweat test would capture, or whether stool and nasopharyngeal-aspirate tests already cover part of that segment.

> The Advocate claims: the per-case DALY figure ignores CG's 6% treated mortality, giving (20%−6%)×27 ≈ 3.8 rather than 5.

- **The arithmetic is right and I concede it.** The correction lowers the per-case figure by about 24%.
- **The 20% untreated fatality is not clearly too high, though.**
  - Tiemersma et al. (2011, *PLoS ONE*) report roughly 70% ten-year case fatality for untreated smear-positive TB.
  - They report roughly 20% for smear-negative TB, as I recall.
  - The incremental cases from a non-sputum test are likelier to resemble the smear-negative group.
  - If so, 20% is a reasonable figure for these cases, not an inflated one.
  - A 24% adjustment is also small next to the 0–100k range.

> The Advocate claims: the evidence undercuts the thesis because tongue-swab and NPOC narrow the gap, and the critique shows nothing about sweat-test sensitivity.

- **Partly agreed.** The critique itself says the tongue-swab endorsement lowers incremental value, and that a sweat test needs its own evidence pathway. Those points are already in the 10–30k haircut.
- **Not the whole picture.** The verifier also found that tongue swabs are less sensitive than sputum. That leaves room for an alternative, though it does not prove a sweat test fills it.

> The Advocate claims: the critique never models grant pivotality.

- **Conceded as a gap.** Pivotality would lower the estimate.
- **The "annual vs. one-year speedup" mismatch is weaker than presented.**
  - CG's statin benefit credits a 1-year speedup.
  - If the same 1-year acceleration is applied to the diagnostic, the benefit equals one year of its steady-state annual benefit.
  - That is the annual figure the critique computed. Applying the Advocate's own symmetric treatment reproduces the critique's number.
  - The real open question is how many years the grant accelerates adoption. One year is symmetric with the statin side. More than one year raises the value, and a counterfactual of "never without the grant" raises it much more.
  - So this is a missing parameter, not a demonstrated overstatement.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: 10–30k is 1.9–5.6% of 539.5k, even 100k is ~18.5%, and nothing crosses the 25% threshold or the 2,000x bar.

- **Conceded in full.**
  - 10k/539.5k = 1.85%, 30k/539.5k = 5.56%, and 100k/539.5k = 18.5%.
  - The SROI only rises, from 3,055x to at most about 3,482x at the "high" run.
  - The "material" label is not supported by these numbers. It is also inconsistent with the critique's own "small magnitude" language.

> The Advocate claims: the sensitivity run (+9.4%) corresponds to about 50.7k DALYs, which is the pre-haircut figure, not the stated 10–30k central.

- **Conceded.** 0.094 × 539,500 ≈ 50.7k. The run reflects the unhaircut calculation, so the sensitivity output overstates the critique's own central.
- **Minimum defensible impact.** Using the Advocate's corrected 3.8 DALYs per case and the critique's lower haircut bound, the effect is roughly 7–8k DALYs, about 1.4% of the benefit term. Taking the critique's lower bound of 0 as given, the effect is nil.
  - I do not present a lower floor than this.
  - The 3.8 figure also leaves the 5% adoption and 1–3% incidence terms unchanged, and both remain ungrounded.
- **What is left.** A small, probably upward-only correction of roughly 1–6% on SROI, with a long uncertain tail. It does not change any decision threshold.

**RESPONSE TO "OFFSETTING FACTORS":**

- **Displacement.** This is already in the critique's haircut from ~50k to 10–30k, so counting it again as an offset is double counting.
- **Delay and discounting.**
  - The critique already says it discounts for delay.
  - The Advocate notes the BOTEC applies no discounting. A few years of delay at a typical 3–5% rate changes the value by a few percent, which is negligible against the range.
- **Delivery costs.** The Advocate names procurement, lab and health-worker costs but does not quantify them. They are real in principle, but they lower the net benefit without making it zero.
- **Adoption below 5%.** The Advocate argues it "could be lower," but that is as ungrounded as the critique's 5%. It does not move the central estimate in a known direction. The verifier's finding that a sweat test needs its own WHO pathway supports a low value, which the critique already reflects.

**KEY UNRESOLVED QUESTIONS:**

- **Cost attribution.** Does the $7M all-in cost, or the $320k grant, include the sweat-diagnostic workstream? The Advocate's own phrasing ("the grant funds work on a sweat diagnostic") suggests at least part of it does. The model must settle this.
- **Size of the diagnostic share.** If the workstream is inside the denominator, how large is it as a fraction of the cost? A small share makes the bias trivial. A large share makes the omission matter more than the 1–6% benefit estimate suggests.
- **Years of acceleration.** How many years does this grant advance a sweat test's adoption, and what is the "never without the grant" probability? This is the missing pivotality parameter, and it can move the value in either direction.
- **Sensitivity of a sweat test.** Is there any evidence a sweat-based test can reach sensitivity high enough to detect cases that tongue-swab PCR misses? Neither side can say, and without it the 1–3% incremental figure is not testable.

### Judge Audit
Surviving strength: weak
Justification: - The debate was largely productive. Both sides made grounded synthesis moves (the 3.8 DALY correction, the mapping of the sensitivity run to the pre-haircut figure, and the symmetric-speedup argument).
- The result of that productive exchange is that the critique's decision-relevant claim did not survive. The Challenger conceded materiality "in full" and conceded that every input term is ungrounded.
- What remains is a correct but small directional point and a cost-attribution consistency check that the critique itself deferred to the model owner.
- The Challenger's attempts to partly anchor the inputs (the paediatric share and the Tiemersma recall) did not ground the 5% adoption or 1–3% incremental-yield terms.
Recommended action: 1. CONCLUDE NOW, with moderate-to-high confidence. The zero valuation of the sweat diagnostic is a small upward-biased omission worth roughly 1–6% of the benefit term on the critique's own assumptions. It does not move SROI near any decision threshold.
   - CG's BOTEC should add a one-line note that diagnostic option value is excluded and that the exclusion biases the estimate slightly downward.
   - The sensitivity entry should be re-run at the stated 10–30k central (relative_reduction ≈ 0.102–0.106), not at 0.1094.
   - The model owner should run one check that is feasible now: confirm whether any sweat-diagnostic spend sits in the $320k or the $7M cost base. If it does and the share is non-trivial, either remove it from costs or note the inconsistency. No further research on the diagnostic's magnitude is warranted at this stage.
Action feasibility: actionable_now
Advocate failures: ['sound_synthesis_noted: The per-case correction "(20% − 6%) × 27 ≈ 3.8 DALYs per case" uses CG\'s own treated-mortality and DALY-per-death parameters. Each step is shown, and the Challenger accepted the arithmetic.', 'sound_synthesis_noted: The magnitude checks are correct. 10–30k / 539.5k gives 1.9–5.6%, and 100k gives 18.5%. The Advocate also showed that the +9.4% sensitivity run maps to ~50.7k DALYs, which is the *pre-haircut* figure rather than the stated 10–30k central. That diagnosis of the sensitivity output is a precise, useful catch.', 'false_definitiveness: Magnitude Challenge 1 states flatly that "nothing in the stated range moves SROI by 25% or more." It does this by comparing the critique\'s annual figure directly to CG\'s 539.5k one-year speedup benefit. Magnitude Challenge 4 then says the two figures are not on the same footing until the grant\'s effect on timing is estimated. The Advocate cannot hold both positions with full confidence. If the footing is unresolved, the materiality conclusion depends on an assumption of a one-year speedup. The Challenger later made that assumption explicit.', 'call_to_ignorance: Under Offsetting Factors: "The 5% base rate for early-stage diagnostics is ungrounded and could be lower." This offers an unknown as an offset with no evidence of direction. It is mild, because it is framed as a risk rather than an estimate.']
Challenger failures: ['unsupported_estimate_pseudo: One term is partly anchored": children are ~12% of incidence, so 1–3% of incidence is "8–25% of the paediatric segment.', 'unsupported_estimate_counter: The Tiemersma et al. figure of "roughly 20% for smear-negative TB, as I recall" is used to defend the 20% untreated fatality.', 'unsupported_estimate_fabricated: A few years of delay at a typical 3–5% rate changes the value by a few percent, which is negligible.', 'false_definitiveness: Delivery costs "lower the net benefit without making it zero." This asserts a bound on an unquantified quantity.', 'sound_synthesis_noted: The pivotality rebuttal is sound.', 'sound_synthesis_noted: The "minimum defensible impact" of ~7–8k DALYs comes from 10k × 3.8/5 ≈ 7.6k. The Challenger shows the derivation and correctly notes that the critique\'s own lower bound of 0 implies nil.']
Debate resolved: Both sides agree on three points:
- The omission biases CG's estimate upward-only in sign.
- On the critique's own numbers, after the per-case correction to 3.8 DALYs, the effect is roughly 1–6% of the 539.5k benefit term, and the 0–100k upper bound stays below the 25% threshold.
- The sensitivity run (+9.4%) reflects the un-haircut ~50k figure, so it overstates the critique's stated central by about 2–5×. The "material" label is unsupported.
Debate unresolved: Three questions remain open:
- **Cost attribution.** Does the $320k grant or the $7M all-in cost include a sweat-diagnostic workstream? If so, how large is it? The verifier marked this UNVERIFIABLE.
- **Years of acceleration.** How many years does this grant advance adoption? The Challenger correctly noted that a "never without the grant" counterfactual could push value well above the annual figure. Neither side grounded any value for this parameter.
- **Test performance.** Whether a sweat test can reach useful sensitivity is entirely unknown.

--- Critique: 60% steady-state uptake has no precedent among comparable TB program additions ---

### Advocate
**DEFENSE OF GIVEWELL'S POSITION: 60% steady-state uptake has no precedent among comparable TB program additions**

**EXISTING COVERAGE:**
- CG's 60% is conditional on the drug working ("60% of adult patients would add atorvastatin *if it works*"). Failure of the trial is handled separately by the 40% p_success. The uptake term therefore only has to describe a world where a Phase III has succeeded and, presumably, guidelines have changed.
- The ceiling is applied to adult patients only. Pediatric cases are excluded, which already trims the denominator.
- The grant is valued as a 1-year acceleration, not as the total value of adoption. Any uptake ceiling that holds in both the accelerated and counterfactual worlds scales both sides equally. CG's framing does not need the 60% to be exact. It needs the ceiling to be roughly right in the years the speedup matters.
- The BOTEC values only on-treatment mortality. The parameter map lists morbidity DALYs, post-treatment mortality, transmission and diagnostic value as implicit zeros. These are uncounted upside that partly cushions a lower ceiling.

**EVIDENCE WEAKNESSES:**
1. The critique's own hypothesis says the ceiling concern is **UNGROUNDED**. It also says not to use "stall below 50%" as support for 0.30–0.40.
2. The only direct ceiling-relevant data point in the evidence package points the other way. WRD coverage is at about 54% and rising, and the UN high-level meeting set a 100% target for 2027. The critique itself says this "suggests over 50% is feasible with sustained push."
3. The analogs cited are admitted to be poor matches for a generic oral adjunct.
   - Xpert needs capital equipment and laboratories.
   - HPMZ is supply-limited by rifapentine.
   - The critique concludes both bear "on the ramp more than on the ceiling."
4. The most relevant analogs, dexamethasone and pyridoxine, are unverified, and the GDF order data were not found. Engaging conditionally: if cheap-adjunct uptake were low, the 0.30–0.40 range would gain support. Nothing in the package shows that it is low. The range is currently an assertion, not a derived estimate.
5. The critique concedes that "adult_uptake" may be a different construct from "percent of notified cases tested," and the CG model's definition could not be checked. A coverage metric for a diagnostic does not map cleanly onto prescribing share for a drug.
6. "10+ years to reach about 50%" is a timing claim. It bears on years_to_adoption, not the steady-state ceiling that the title attacks.

**MAGNITUDE CHALLENGE:**
- The sensitivity run gives these results:
  - At the Quantifier's own central ceiling of 0.5, SROI falls from 3,055 to 2,546 (−16.7%). That is below the ~25% materiality line, and still above the ~2,000x bar.
  - Only the low case of 0.35 (1,782, −41.7%) crosses the bar. That is the ungrounded 0.30–0.40 range.
  - The high case of 0.7 raises SROI by 16.7%, so the ceiling uncertainty is two-sided around the published figure.
- On timing, moving years_to_adoption to the Quantifier's central 10 years changes SROI by −4.0%. Even the high case is −11.4%. Neither is material.
- The critique's mechanism supports this. A one-year shift of any ramp gains about (ceiling × one year of cases), so ramp shape matters little. The only material lever is the ceiling, and that is the part the critique says it cannot ground.
- The critique's reading of the WRD 54% figure is that it is "rising." A ceiling of 0.30–0.40 would sit below coverage already achieved by a tool that is harder to roll out. That makes the low range look too aggressive.

**OFFSETTING FACTORS:**
1. Uncounted benefit channels (parameter map): morbidity and lung damage, post-treatment mortality, transmission averted, and the diagnostic workstream. Each is a positive term the BOTEC sets to zero.
2. If case detection improves toward the 100% WRD target, notified cases could exceed the "constant treated share" assumption. This is conditional on the target being met, which I cannot ground, so I flag it only as a direction.
3. The BOTEC applies one uncapped uptake figure to the whole 5.5M cohort. The 2% annual case decline is also undiscounted but equally unadjusted for case-finding growth. Offsets of this kind are plausible but unquantified, and I do not assert a size.

**OVERALL ASSESSMENT:** **Strong defense** on materiality of the ceiling concern as stated. It is **partial** on the narrower ramp point, which is valid but immaterial (−4% to −11%).
- The ceiling critique is self-described as ungrounded.
- Its central case (0.5) falls below the materiality line.
- Only the ungrounded low range crosses the 2,000x bar.

**CONCESSIONS:**
1. CG offers no empirical precedent for 60%, and the parameter map correctly lists this as unaccounted for. The 60% is a judgment, not a derived number.
2. CG ignores the adoption lag. Timing and discounting interact with a finite horizon and a declining case base, so a ramp effect exists even though it is small in the sensitivity run.
3. The HPMZ experience (14% of eligible patients prescribed it, 64% of starters discontinued) is not a clean analog, but it shows that tolerability and prescriber behavior can cut real-world uptake. Statin-rifampicin interactions and hepatotoxicity are untreated risks for exactly this channel. This could depress the effective ceiling. It is a reason to doubt 60%, not evidence for 0.30–0.40.
4. A central ceiling of ~0.5, if that is the best estimate, would lower SROI by about 17%. I accept that as a modest downward revision to the point estimate, not a decision-relevant change.

### Challenger
REBUTTAL: 60% steady-state uptake has no precedent among comparable TB program additions

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: any uptake ceiling that applies in both the accelerated and counterfactual worlds "scales both sides equally," so CG's framing doesn't need the 60% to be exact.

- **The cancellation claim contradicts the sensitivity run.**
  - The grant's value is the difference between two worlds, and that difference is proportional to the ceiling.
  - Moving the ceiling from 0.6 to 0.35 changes SROI by −41.7%, and 0.35/0.6 = 0.583, so −41.7% is exactly the linear scaling.
  - The ceiling does not cancel. It is the dominant multiplier.
- **The decision threshold is a ceiling of about 0.39.**
  - My derivation is 0.6 × (2,000 / 3,055) ≈ 0.393, which matches the critique's "materiality line is 0.39".
  - The question is therefore whether the true ceiling is about 35% below CG's assumed 0.6.
  - Calling the 60% "roughly right" does not answer that. It needs a bound, and none is given.

> The Advocate claims: 60% is conditional on the drug working, with guidelines presumably changed, so the p_success term handles failure separately.

- **Success does not imply uptake.** The one verified post-guideline data point on prescriber behavior is HPMZ, where only 14% of eligible patients were prescribed it and 64% of starters discontinued (verifier evidence).
- **The Advocate concedes the HPMZ point.** They accept that tolerability and prescriber behavior "can cut real-world uptake" and that statin–rifampicin interactions and hepatotoxicity are "untreated risks for exactly this channel."
- **The conditioning therefore does not close the gap.** It removes trial failure. It does not remove post-success prescribing and discontinuation risk, which is the quantity the ceiling represents.

> The Advocate claims: pediatric exclusion already trims the denominator.

- The ceiling concern is about the share of adults who take the drug. Excluding children does not touch that share.

> The Advocate claims: uncounted benefit channels (morbidity, post-treatment mortality, transmission, diagnostics) partly cushion a lower ceiling.

- These channels are already zero in the BOTEC at the 0.6 ceiling. They are upside at every ceiling value, not a specific offset to a lower one.
- Morbidity, post-treatment mortality and transmission benefits all require patients to actually take the drug. They scale with uptake and would fall with it.
- The Advocate admits no size is asserted. An unquantified cushion cannot offset a quantified −17% to −42% shift.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the critique itself labels the ceiling UNGROUNDED, and nothing in the package shows cheap-adjunct uptake is low.

- **Concession.** The 0.30–0.40 range is not derived from data. I do not rest the case on it.
- **UNVERIFIABLE is not REJECTED.**
  - Dexamethasone and pyridoxine are unverified, and the GDF order data were not found. That is an evidence gap, not a contrary finding.
  - "Nothing shows it is low" treats the gap as support for 0.6.
- **The 60% is also ungrounded.** The Advocate concedes it is "a judgment, not a derived number" with no empirical precedent.
  - Two ungrounded numbers are being compared, so the issue is where the prior should sit.
  - The only verified quantitative uptake figures in the package are 54% (WRD, after more than a decade, with heavy funding) and 14% prescribed (HPMZ).
  - Both are below 60%, so the 60% sits at or above the top of the verified evidence.

> The Advocate claims: WRD at about 54% and rising points the other way, and a 0.30–0.40 ceiling would sit below coverage already achieved.

- **Even on the Advocate's own reading, the WRD figure sits below 60%.** It is a decade or more after endorsement, for a tool with sustained global funding. It is an argument for a central ceiling near 0.5, not 0.6.
- **The defense uses WRD two ways.** It dismisses WRD as a poor analog (capital equipment, labs) and as a different construct ("percent of notified cases tested" versus prescribing share). It then relies on WRD to rule out the low range. If the construct mismatch holds, WRD cannot bound the ceiling in either direction.
- **The 2027 target does not count as evidence.** The 100% target set in 2023 versus about 54% achieved shows how far targets run ahead of delivery. The verifier itself notes "a system target is not the same as steady-state achieved coverage."

> The Advocate claims: "10+ years to 50%" is a timing claim, not a ceiling claim.

- **Concession.** It is a timing claim, and the critique's own hypothesis says it bears on the ramp more than the ceiling.
- **Residual point.** The same evidence says the best analog tops out near 50% after a decade. That is data about level as well as timing.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

- **Concession.** At ceiling = 0.5 alone, SROI is 2,546 (−16.7%), below the ~25% materiality line and above the 2,000x bar. Only the 0.35 case crosses the bar.
- **The two central shifts compound.**
  - Central ceiling 0.5 gives 2,546. Central years_to_adoption = 10 is −3.96% on its own.
  - Assuming independence (my assumption, not tested in the run), the combined effect is 2,546 × 0.9604 ≈ 2,445, or about −20% from baseline.
  - That leaves roughly 22% headroom above 2,000 instead of the 53% the baseline implies.
  - Each shift is small in isolation, but the combined central case is thin.
- **The ceiling uncertainty is not symmetric.**
  - The Advocate treats the +16.7% high case (0.7) as balancing the low case.
  - The verified data (54%, 14% prescribed) offer no analog support for 0.7.
  - Evidence that exists points below 0.6, so the two-sided framing overstates the upside.
- **The ramp point stands.** I concede that the −4% to −11% timing effect is not material by itself.

**RESPONSE TO "OFFSETTING FACTORS":**

1. **Uncounted benefit channels.** They are real but unquantified, and they scale with uptake, as above.
2. **Case-detection growth.** The Advocate says this is conditional on a 100% WRD target being met, which they cannot ground. It is speculative and not in the model.
3. **Undiscounted 2% case decline and the uncapped cohort.** The Advocate calls these "plausible but unquantified" and asserts no size. They are not offsets in any sense that can be netted against the quantified ceiling effect.

None of the claimed offsets is both modeled and sized.

**KEY UNRESOLVED QUESTIONS:**

- How does the CG model define adult_uptake: share of all adult TB patients prescribed, share of notified cases, or share initiating and adhering? The HPMZ figures show these can differ by several-fold (14% prescribed versus 36% of starters retained).
- What is the baseline years_to_adoption? The sensitivity run gives −4% at 10 years, but the baseline value is not stated in this package, so the size of the gap being tested is unclear.
- What do cheap generic adjuncts such as dexamethasone and pyridoxine, and GDF order data, show about uptake? This evidence was unretrieved, and it is the most relevant analog class.
- How large is the real-world statin–rifampicin interaction and hepatotoxicity discontinuation risk? It is conceded to be untreated and could push the ceiling below 0.5.
- Is the ceiling correlated with p_success? A drug whose Phase III benefit is modest may attract lower uptake, which would compound the two discounts rather than leave them independent.

### Judge Audit
Surviving strength: moderate
Justification: The Challenger landed grounded, decisive points. It refuted the Advocate's cancellation argument with the linear-scaling check, and it derived the 0.39 threshold cleanly. That legitimately sustains the critique's core claim that the ceiling is the dominant, unprecedented, judgment-based multiplier.
However, the Challenger conceded that the 0.30–0.40 range is not data-derived. Its attempts to anchor a sub-0.6 prior rested on the "tops out near 50%" misreading and on non-comparable analogs (HPMZ preventive therapy). The supported magnitude is therefore about −17% to −20%, below materiality. The critique survives as a valid concern of medium magnitude, not as a decision-changing one, and the decisive question (above or below 0.39) remains open.
Recommended action: 2. SPECIFIC INVESTIGATION:
   1. **Retrieve CG's definition of adult_uptake** from the model or CG documentation: share of all adult TB patients prescribed, versus initiating, versus completing.
   2. **Re-run the verifier with targeted searches for cheap-adjunct uptake data.** Useful sources include:
      - Pyridoxine co-prescription rates with isoniazid in high-burden national TB programs.
      - Dexamethasone use in TB meningitis from hospital audits in high-burden settings.
      - GDF catalog order volumes for pyridoxine relative to isoniazid-containing regimens.
   3. **Find observed discontinuation rates for statin co-administration with rifampicin-based regimens.**

   All three are feasible with existing tooling. If the cheap-adjunct analogs show sustained coverage of 50% or more, the critique should be closed as a modest point-estimate revision. If they show coverage below about 40%, the critique becomes decision-relevant.

   **Interim conclusion (moderate confidence):** Revise the central ceiling to about 0.5 and apply the timing adjustment, giving SROI of about 2,450. Treat the result as above the bar but with thinner headroom (about 22%).
Action feasibility: requires_specified_evidence
Advocate failures: ['false_definitiveness: The Advocate says "Any uptake ceiling that holds in both the accelerated and counterfactual worlds scales both sides equally. CG\'s framing does not need the 60% to be exact." This is stated confidently but is wrong. The grant\'s value is the *difference* between the two worlds, and that difference is proportional to the ceiling. The Advocate\'s own sensitivity run (0.35 → −41.7%, exactly linear) contradicts it, and the Challenger correctly caught this.', 'false_definitiveness: The Advocate argues that "a ceiling of 0.30–0.40 would sit below coverage already achieved by a tool that is harder to roll out," so the low range "looks too aggressive." Elsewhere the defense argues that WRD is a poor analog and a different construct ("percent of notified cases tested" versus prescribing share). The Advocate uses WRD to bound the ceiling from below while dismissing it as non-comparable. The Challenger correctly identified this inconsistency.', 'call_to_ignorance: Offsetting factor 3 says the undiscounted case decline and uncapped cohort have "offsets of this kind [that] are plausible but unquantified." This offers unsized possibilities as cushioning. The Advocate partly mitigates it by explicitly declining to assert a size.', 'sound_synthesis_noted: The Magnitude Challenge uses the sensitivity run correctly:', 'sound_synthesis_noted: Evidence weakness 4 handles the unverified dexamethasone/pyridoxine analogs correctly as a conditional: "if cheap-adjunct uptake were low, the 0.30–0.40 range would gain support." It does not treat UNVERIFIABLE as REJECTED.']
Challenger failures: ["sound_synthesis_noted: The Challenger derives the decision threshold as 0.6 × (2,000/3,055) ≈ 0.393. This is consistent with the critique's 0.39 line. The Challenger also verifies that −41.7% equals linear scaling (0.35/0.6). Both are clean derivations, and they refute the cancellation claim.", 'sound_synthesis_noted: The Challenger compounds the two central shifts: 2,546 × 0.9604 ≈ 2,445 (about −20%). The independence assumption is explicitly flagged as untested. This is a transparent synthesis and appropriately caveated.', 'misrepresenting_evidence_status: The Challenger\'s "residual point" says the best analog "tops out near 50% after a decade" and that this is "data about level." The verifier explicitly marked the stall claim PARTIALLY CONTRADICTED: WRD is "still rising, not stalled," and 37 of 49 high-burden countries exceeded 50% in 2024, up from 31. "Tops out" reintroduces the ceiling reading that the verifier rejected and that the critique\'s own hypothesis disclaimed.', 'unsupported_estimate_pseudo: The Challenger says "the only verified quantitative uptake figures… are 54% (WRD) and 14% prescribed (HPMZ). Both are below 60%, so the 60% sits at or above the top of the verified evidence," and calls WRD "an argument for a central ceiling near 0.5.', 'strawmanning: The Challenger says "\'Nothing shows it is low\' treats the gap as support for 0.6." The Advocate did not argue this. The Advocate explicitly engaged conditionally ("if cheap-adjunct uptake were low, the 0.30–0.40 range would gain support") and concluded only that the low range "is currently an assertion." It also separately conceded that 60% is "a judgment, not a derived number.']
Debate resolved: The ceiling enters SROI linearly and does not cancel between the counterfactual worlds. The decision threshold is a ceiling of about 0.39. Both sides agree that neither 0.6 nor the 0.30–0.40 range is empirically derived. Both also agree that the ramp/timing effect (−4% to −11%) is immaterial on its own.

At the best available central estimates (ceiling 0.5, 10-year adoption), SROI falls about 20% to roughly 2,445. That is a real downward revision but remains above the 2,000x bar. The critique's original 33–50% magnitude therefore depends entirely on the ungrounded low range.
Debate unresolved: Whether the true adult-patient ceiling for a cheap generic oral adjunct sits above or below about 0.39 is still unsettled, for three reasons:
- **The relevant analog class is unretrieved.** This includes dexamethasone, pyridoxine and GDF orders.
- **The model's construct is unchecked.** It is unknown how CG defines adult_uptake (prescribed, initiated, or adherent).
- **Tolerability risk is unquantified.** The statin–rifampicin interaction and hepatotoxicity discontinuation risk is conceded but not sized.

--- Critique: A Phase III cannot be powered on mortality, so the WHO GDG would be recommending on surrogate or composite endpoints ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: A Phase III cannot be powered on mortality, so the WHO GDG would be recommending on surrogate or composite endpoints
```

**EXISTING COVERAGE:**

1. **The 40% probability of success already prices in this risk.**
   - The BOTEC applies a 40% probability that "Phase II and Phase III trials both succeed." That is a 60% haircut on all benefits.
   - A Phase III that yields only equivocal, surrogate-based evidence and fails to produce a recommendation is one way of not succeeding. So some of the critique's downside is already inside p_success.
   - The parameter map notes that "success" is not defined. That cuts both ways: the critique's scenario is not excluded from the 60% failure mass.

2. **Uptake is already well below 100% and is conditioned on the drug "working."**
   - The 60% uptake assumption already discounts for imperfect guideline translation, private-sector use and clinician reluctance. It is not a full-adoption assumption.
   - The critique's uptake effect is a reduction from an already-discounted figure. It must be a reduction beyond the generic friction 60% already embeds, and the critique does not separate the two.

3. **Delayed adoption is structurally cheap in this model.**
   - The benefit comes from a 1-year speedup. A GDG that asks for more evidence delays both the funded and counterfactual pathways.
   - The only mechanical loss from later adoption is a smaller eligible population, through the 2% annual decline in cases.
   - The Quantifier's own result confirms this. Moving years_to_adoption to 8.5 changes SROI by −1.0% at the central value and −3.0% at the high value.

**EVIDENCE WEAKNESSES:**

1. **The critique's own evidence is weak on the key link.**
   - The Verifier flags the uptake and timing effects as UNGROUNDED.
   - The one concrete study found, StAT-TB, is a Phase 2b dose-finding trial. It says nothing about what a Phase III endpoint or a GDG evidence standard would be.
   - Observational statin–mortality data in TB patients with ASCVD are a narrow subgroup. They show where a recommendation might be limited. They do not show that a recommendation would be limited.

2. **The critique's main counterweight is probably stronger than the critique treats it.**
   - The Verifier itself says WHO TB guideline groups routinely treat composite outcomes that include death (unfavourable outcome) as critical and direct. The Verifier did not search for this, and I treat it as an unverified claim made arguendo.
   - From my background knowledge, which I have not verified here, WHO's regimen recommendations rest on such composites. Examples are TB-PRACTECAL and the rifapentine–moxifloxacin Study 31/A5349.
   - If that holds, the indirectness downgrade is less likely, and "conditional because composite" does not follow.

3. **The sample-size premise is not itself in dispute, but it does not entail a surrogate outcome.**
   - My check: for 6% vs 5.4% (10% relative reduction), a two-sided α=0.05 test needs about 23,400 per arm at 80% power and about 31,400 at 90% power.
     - Derivation: n ≈ (z_α/2 + z_β)² × [p₁q₁ + p₂q₂] / Δ².
     - With p₁q₁ = 0.0564, p₂q₂ = 0.0511 and Δ = 0.006, 7.84 × 0.1075 / 0.000036 ≈ 23,400. At 90% power, 10.5 × 0.1075 / 0.000036 ≈ 31,400.
     - The critique's 28–30k sits inside this range, so I accept the premise.
   - The premise says a trial of a modest effect is large. It does not say the GDG would have no mortality-relevant evidence.
   - A Phase III could be powered on a death-inclusive composite, which has a higher event rate and needs a smaller sample. This is the critique's own counterweight.

**MAGNITUDE CHALLENGE:**

1. **The Quantifier's own central estimates are well below the materiality threshold.**
   - At the Quantifier's central uptake of 0.55, SROI falls from ~3,055 to ~2,800 (−8.3%). That is under the 25% change threshold and well above the 2,000 bar.
   - At the Quantifier's central years_to_adoption of 8.5, SROI falls −1.0%.
   - The Quantifier's low case (uptake 0.45) gives ~2,291 (−25%). It does not cross the bar (`crosses_bar_low: false`).
   - The critique was already downgraded to low-to-medium, which matches these numbers.

2. **The scenario that would cross the bar needs a high probability, and that probability is ungrounded.**
   - The only scenario that clearly crosses is the speculative "subgroup-only, effective uptake roughly halved" case. Halved uptake gives ~1,527, below 2,000.
   - For that scenario to move the expected value, it must be probability-weighted. Let q be its probability and the halving cost 50%.
     - To cross the 2,000 bar, the expected multiplier must fall to 2,000/3,055 ≈ 0.655, so a 34.5% cut. That requires q × 0.5 ≥ 0.345, so q ≥ ~0.69.
     - Even a 25% expected cut would need q ≥ 0.5.
   - The critique offers no basis for a probability of that size. By its own labelling, the scenario is speculative.
   - A conditional recommendation does not obviously halve uptake either. I cannot ground a figure here and treat my own view as an uninformed prior.

3. **The mortality-variance channel is not part of this critique.**
   - The claim that unverified mortality "raises the variance of relative_reduction" belongs to the relative_reduction thread. Variance alone does not change an expected-value BOTEC unless it shifts the mean.

**OFFSETTING FACTORS:**

1. **Surrogate-based adoption could raise uptake and speed.** If a GDG accepts a clearly beneficial, cheap, generic drug on a composite, the lower evidence bar would shorten the path to adoption. The critique only considers the downside direction.

2. **Benefits outside the model.**
   - The BOTEC values only on-treatment mortality. Morbidity (lung damage), post-treatment survival and transmission are implicit zeros, per the parameter map.
   - A recommendation grounded in a composite that includes unfavourable outcomes such as relapse and failure would plausibly carry these benefits as well. This is an unquantified upside that partly offsets the uptake risk.

3. **The drug is generic and cheap.** Clinician or programme adoption of a low-risk generic after a positive trial does not require a perfect guideline pathway. I do not have grounded evidence on the size of this effect, so I flag it as a qualitative offset only.

**OVERALL ASSESSMENT:** **Strong defense** on the specific parameters targeted (adult_uptake and years_to_adoption).

- The quantified central impacts are −8.3% and −1.0%, both under the materiality threshold.
- Part of the risk is already inside the 40% p_success and the 60% uptake.
- The critique's own counterweight (death-inclusive composites accepted as direct) is plausible, though unverified.
- The only bar-crossing scenario needs an ungrounded probability of ~0.69 or more.

**CONCESSIONS:**

1. The BOTEC does not define "success" or say what endpoint a $7M Phase III would be powered on. If the answer is a surrogate-only trial, some indirectness risk is real and only implicitly covered by p_success.
2. The 60% uptake has no empirical precedent in the BOTEC and does not model a GDG-specific subgroup limit. A subgroup-limited recommendation (e.g., ASCVD patients, where the observational mortality signal exists) would cut uptake materially, and I cannot rule it out.
3. The "composite is direct" counterweight is itself unverified, so my defense of the indirectness point rests partly on an unsearched claim.
4. The all_in_cost interaction (a cheap Phase III implying a surrogate endpoint) is a legitimate concern, but it belongs to the all_in_cost thread, and I am not defending it here.

### Challenger
REBUTTAL: A Phase III cannot be powered on mortality, so the WHO GDG would be recommending on surrogate or composite endpoints

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the 40% p_success already absorbs a Phase III that produces only equivocal, surrogate-based evidence, because that is one way of "not succeeding."

Response:
- The Advocate concedes that "success" is undefined in the BOTEC. A parameter whose definition is unknown cannot be shown to cover a specific scenario.
- The critique's scenario is Phase III hits its primary endpoint, but the GDG issues a conditional, subgroup-limited or delayed recommendation. If success means "trial positive," this scenario sits inside the 40% success branch, not the 60% failure mass.
- So the p_success defense works only under one of two unstated definitions. The Advocate cannot show the BOTEC uses that definition.

> The Advocate claims: the 60% uptake already embeds generic guideline-translation friction, so the critique's effect must be a reduction beyond that.

Response:
- The Advocate also concedes that the 60% "has no empirical precedent in the BOTEC and does not model a GDG-specific subgroup limit."
- A generic friction discount and a guideline-scope restriction are different mechanisms. The first lowers uptake within the eligible population. The second shrinks the eligible population.
- The Quantifier's central of 0.55 is a 5-point trim. It does not represent the scope-restriction mechanism, so it understates this critique's own scenario.

> The Advocate claims: delayed adoption is structurally cheap, as the Quantifier's −1.0% and −3.0% show.

Response:
- I concede this. The years_to_adoption channel is immaterial, and the critique's weight rests on adult_uptake.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: StAT-TB is Phase 2b and says nothing about Phase III endpoints or GDG standards. The ASCVD observational data show where a recommendation might be limited, not that it would be.

Response:
- I concede StAT-TB does not establish the GDG's behavior. The uptake and timing effects are UNGROUNDED, not REJECTED. The critique should be read as conditional: if the Phase III is not mortality-powered, does it follow that the recommendation is narrower? The Advocate's own concession 2 accepts that it could be.
- StAT-TB does show that the only trial-based statin evidence in TB has non-mortality primary endpoints (time to sputum-culture negativity, lung function), with mortality only as a tolerability measure. The pipeline is currently surrogate-first, and the Advocate does not dispute this.

> The Advocate claims: death-inclusive composites such as TB-PRACTECAL and Study 31/A5349 are treated as direct, so the indirectness downgrade is unlikely.

Response:
- The Advocate flags this as unverified background knowledge, as the Verifier did. It is not corroborated evidence.
- Even granting it, the cited trials are regimen trials. There the composite (unfavourable outcome: failure, relapse, death) is the efficacy question itself.
- The BOTEC's benefits come from a different question: whether a host-directed adjunct reduces on-treatment mortality. The model's relative_reduction applies to deaths only.
- A composite dominated by culture failure or relapse events could be positive without establishing a mortality effect. Conversely, a composite in which death is a minor component is only weakly informative about the mortality parameter.
- This is my own reasoning, not an attested finding. It shows the "composite is direct" counterweight transfers imperfectly from regimen trials to this use case.

> The Advocate claims: the sample-size premise is accepted (23,400–31,400 per arm), but a death-inclusive composite could be used instead.

Response:
- I agree on the premise. The Advocate's derivation is held at a 10% relative reduction. The required n scales with the effect size assumed, and I cannot ground what the BOTEC's relative_reduction is.
- The Advocate's route to a smaller trial concedes the critique's core point: the trial would not be powered on mortality alone. What remains is whether the GDG treats the composite as direct, and that is the unverified step.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: central estimates (−8.3%, −1.0%) are under the 25% threshold, and a bar-crossing scenario needs q ≥ ~0.69.

Response:
- The arithmetic is right for a 50% cut. But the critique's own scenario text is "a third of patients… about half or more."
  - If only a third of patients fall in scope and within-scope uptake stays at 60%, effective uptake falls by about 67%.
  - The required expected cut is 1 − 2,000/3,055 ≈ 34.5%. So q × 0.667 ≥ 0.345, giving q ≥ ~0.52, not 0.69.
- That is still a high probability. But the Advocate's threshold is sensitive to the assumed cut size, and the Advocate used the most favorable reading.
- The Quantifier's low case (uptake 0.45) yields ~2,291, −25%. That is about 14.5% above the 2,000 bar, not "well above" it. The low case is a modest, unstated-probability scenario, and it nearly reaches the materiality threshold.
- Floor: at the central estimate the effect is −8.3%, not crossing the bar. I do not claim more than that. What the critique shows is a real, one-directional downside that the central estimate understates because it models the scenario as a mere 5-point trim.

> The Advocate claims: variance in relative_reduction doesn't move expected value.

Response:
- I concede for this thread. Variance matters only if it shifts the mean, which belongs to the relative_reduction critique.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: a lower evidence bar from surrogate acceptance could raise uptake and speed.

Response:
- This is a different branch, not an offset. It is the world where the GDG accepts the surrogate. The critique concerns the world where it does not.
- Both branches belong in an expected value, but the Advocate offers no probability for either. The upside branch is also bounded: the BOTEC already assumes the drug is adopted at 60%, so there is little headroom above baseline.

> The Advocate claims: morbidity, post-treatment survival and transmission benefits are implicit zeros that offset the risk.

Response:
- Those benefits are real but absent from the model. They cannot offset a reduction in a model parameter.
- They accrue only if the drug is recommended and used, so they scale with the same uptake the critique says might fall.

> The Advocate claims: a cheap generic drug can be adopted without a perfect guideline pathway.

Response:
- The Advocate says this is ungrounded and offers it as a qualitative offset only.
- The BOTEC's mechanism routes benefits through a WHO recommendation after Phase III. If adoption doesn't depend on the guideline, the funded Phase III's counterfactual value is also weaker. The offset undercuts the model's own logic.

**KEY UNRESOLVED QUESTIONS:**
- What does the BOTEC mean by "success" in the 40%: trial positive, or recommendation issued at the assumed uptake? The coverage defense turns on this.
- Would a GDG treat a death-inclusive composite for a host-directed adjunct as direct evidence of mortality benefit, or only as it does for regimen trials? The Verifier did not search this.
- What share of TB patients would a likely conditional recommendation cover? A one-third subgroup is the critique's illustration. The ASCVD observational signal suggests one plausible scope, but the size is ungrounded.
- What is the probability of a subgroup-limited or conditional outcome? The materiality conclusion depends on whether it is nearer 0.2 or 0.5+, and neither side can ground a figure.

### Judge Audit
Surviving strength: moderate
Justification: The debate was largely clean. Both sides showed their arithmetic, labelled unverified claims as such, and conceded points appropriately; the Challenger, for example, dropped the timing and variance channels. The Challenger made two grounded arguments the Advocate could not fully answer: p_success does not demonstrably absorb a "positive trial, narrow recommendation" outcome, and the 0.55 central value models friction rather than scope restriction. Against that, the Challenger conceded that the central effect is ≈−8% and does not cross the bar. The scenario that does cross needs an ungrounded probability above 0.5. The critique therefore survives as a valid, one-directional, low-magnitude concern, not a material one.
Recommended action: 1. **CONCLUDE NOW** (moderate confidence)
   - Drop the years_to_adoption and variance channels from this critique.
   - Retain the adult_uptake channel as a low-magnitude downward adjustment of roughly −5% to −15% on SROI. It does not cross the 2,000 bar under any probability either side can defend.
   - Note explicitly in the model that p_success is undefined. If it means "trial positive," the narrow-recommendation risk is not priced in and should be added as a modest uptake haircut.

**Secondary targeted step (feasible with existing tooling).** One verifier search, on how WHO handled adjunctive host-directed TB therapies (e.g., corticosteroids in TB meningitis or pericarditis), would ground both open empirical questions:
   - which endpoint the recommendation rested on;
   - whether it was population-restricted.

If precedent shows subgroup recommendations target high-mortality populations, the proportional-cut assumption should be revised downward and the critique weakened further.
Action feasibility: actionable_now
Advocate failures: ['sound_synthesis_noted: The sample-size check is correct. At 6% vs 5.4%, (1.96+0.84)² × (0.0564+0.0511)/0.006² ≈ 23,400 per arm at 80% power, and ≈31,400 at 90%. Its claim that this "brackets" the critique\'s 28–30k is loose, because the critique\'s figure used a 5% baseline at 80% power, not 6%. The conclusion that the premise is accepted still holds.', 'sound_synthesis_noted: The break-even probability is derived correctly. The required expected cut is 1 − 2,000/3,055 ≈ 34.5%, and 0.5q ≥ 0.345 gives q ≥ 0.69. Halved uptake gives ≈1,527, and the low case at 0.45 gives ≈2,291. The arithmetic is correct and each step is shown. Its weakness is that it assumes a 50% cut rather than the critique\'s "half or more," which the Challenger exploited.', 'call_to_ignorance: Offsetting factor 1 says "Surrogate-based adoption could raise uptake and speed." This is a speculative upside branch with no evidence or probability attached. It fills a gap rather than acknowledging it. It is milder than a full instance because the Advocate is transparent elsewhere about ungrounded offsets, as in factor 3.', 'false_definitiveness: The Advocate self-rates as a "Strong defense" while conceding four points. These include that "success" is undefined, that the 60% uptake "does not model a GDG-specific subgroup limit," and that the key counterweight "rests partly on an unsearched claim." The magnitude defense is genuinely strong. The coverage defense, existing coverage point 1, is conditional on an undefined parameter and should have been presented that way. I assess this as partial-to-strong, not strong.']
Challenger failures: ['strawmanning: The Challenger says the Quantifier\'s low case of ~2,291 is "about 14.5% above the 2,000 bar, not \'well above\' it." The Advocate used "well above the 2,000 bar" for the central ~2,800, not the low case. For the low case the Advocate only said it "does not cross the bar." The rebuttal targets a claim not made. The 14.5% figure itself is arithmetically correct.', "sound_synthesis_noted: The re-derivation is correct and grounded in the critique's own scenario text. A one-third subgroup gives a ≈67% cut, and q × 0.667 ≥ 0.345 gives q ≥ ~0.52. It legitimately shows the Advocate's threshold depends on the assumed cut size. It shares the unexamined assumption that benefit scales linearly with uptake, which is the missed defense above.", "sound_synthesis_noted: Two arguments are clean, grounded rebuttals that the Advocate's concessions do not neutralize:", 'misrepresenting_evidence_status: This is a mild instance. The Challenger says "The pipeline is currently surrogate-first, and the Advocate does not dispute this," inferring this from StAT-TB alone. Phase 2b trials nearly always use surrogate primary endpoints. A single Phase 2b trial with culture conversion as its endpoint is not evidence about what a Phase III would be powered on. The Challenger treats a design-stage norm as a substantive signal about the eventual evidence base.']
Debate resolved: Both sides agree on four points:
- The sample-size premise holds (~23–31k per arm, depending on baseline and power).
- The years_to_adoption channel is immaterial (−1% to −3%).
- The variance channel belongs to the relative_reduction thread.
- At the Quantifier's central uptake of 0.55, the effect is ≈−8%, below the materiality threshold.

The debate also established that the bar-crossing scenario requires a probability of a subgroup-limited outcome of roughly 0.52–0.69 or more, depending on the assumed cut. Neither side can ground a probability that high.
Debate unresolved: Three questions remain open:
- Whether the BOTEC's 40% p_success covers "trial positive, but the recommendation is narrowed." This turns on an undefined parameter, and the Challenger showed the coverage defense depends on it.
- Whether a GDG would treat a death-inclusive composite for a host-directed adjunct as direct evidence of mortality benefit.
- Whether a subgroup-limited recommendation would cut deaths averted proportionally to uptake. Neither side raised this, but it determines whether the Challenger's 67% cut is the right input.

--- Critique: Clinical eligibility and monitoring barriers cap the achievable prescribing share below the "generic and cheap" logic ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: Clinical eligibility and monitoring barriers cap achievable prescribing share
```

**EXISTING COVERAGE:**

1. CG's 60% is already a 40-point haircut from universal uptake. The BOTEC says 60% of adult patients "would add atorvastatin if it works." That figure was never "everyone, because it's cheap."
   - A 40% non-uptake share already has room for liver-disease exclusions, clinician reluctance, pregnancy, and polypharmacy.
   - The critique's own illustrative exclusion is 10–20% of adults. That is a fraction of the 40% already left out.
   - The critique does not show that 60% fails to cover its listed barriers. It shows only that CG did not itemise them.

2. The 40% p_success is partly a hedge on real-world translation. The Parameter Map notes that adoption "may be partly captured in uptake, but this is not explicit." The 40% joint Phase II/III success probability and the 60% uptake are both coarse, judgment-based discounts that jointly absorb some non-ideal-world friction. Neither is a precise measure, but the model is not a frictionless "generic and cheap" calculation.

3. Adverse-event handling is outside this parameter. The critique's monitoring-cost point (extra LFT costs not in CG's cost) belongs to all_in_cost. It does not reduce adult_uptake, and the Parameter Map lists it under that separate parameter.

4. Discontinuation (mechanism c) risks double counting.
   - Conditional on relative_reduction being derived from a trial effect (CG's 10% is underived, but presumably anchored to trial evidence), trial-level discontinuation is already embedded in the effect size.
   - Counting discontinuation again in uptake would penalise the same loss twice.
   - Real-world adherence may be worse than in a trial. That is an argument about relative_reduction, not an eligibility argument.

**EVIDENCE WEAKNESSES:**

1. The critique labels its own central number UNGROUNDED. The 0.45–0.50 range comes from "my own illustrative scenario, not a sourced estimate." The 10–20% exclusion share has no citation. The evidence package supplies no study of statin-prescribing eligibility among TB patients.

2. The DILI evidence does not apply to the intervention.
   - The ~11.5% pooled incidence (range 2–28%) describes DILI caused by anti-TB drugs.
   - It says nothing about how often clinicians would withhold a statin, or how often a statin would cause or confound liver injury.
   - The meta-analysis authors' call for liver monitoring applies to anti-TB treatment regardless of statins. Programs already face that issue, so the incremental barrier from adding a statin is smaller than the headline DILI rate implies. This is a conditional argument; I have no study measuring the incremental barrier.

3. The critique partly undermines its own mechanism.
   - It concedes that the CYP3A4 and PI-boosted ART interaction arguments "largely fall away" for pravastatin. Pravastatin is the statin in the cited Phase 2b trial, and the critique says it is not substantially CYP3A4-metabolised (from background knowledge).
   - The surviving concerns are hepatotoxicity attribution and pill burden. These are soft, behavioural barriers, not hard contraindications.

4. On statin hepatotoxicity itself, my background recollection is that the FDA removed the requirement for routine periodic liver-enzyme monitoring from statin labels in 2012. I cannot cite a specific document from the evidence package, so treat this as an uninformed prior. If correct, it weakens the claim that mandated LFT monitoring would be a binding barrier.

5. The critique does not know which statin CG assumes. Its own text says "I do not know which statin CG assumes." Eligibility arguments built on statin-specific pharmacology are therefore conditional on an unresolved fact.

**MAGNITUDE CHALLENGE:**

1. The sensitivity results do not cross CG's materiality threshold at the central estimate.
   - Baseline SROI is about 3,055x.
   - At the Quantifier's central uptake of 0.51, SROI is about 2,597x, a 15% decline. This is below the ~25% materiality line and above the ~2,000x bar.
   - The low case (30% decline, implying uptake of 0.42) gives about 2,138x. That is still above 2,000x, and `crosses_bar_low` is false.
   - The high case is a 5% decline.
   - Only the low-end tail exceeds 25%, and it rests on the ungrounded assumption described above.

2. The "material" label overstates the Quantifier's own numbers. By the stated criterion (below ~2,000x or more than ~25% change), the central case is not decision-relevant.

3. The derivation chain is thin.
   - 0.60 → 0.51 = 0.60 × 0.85, so it implies a 15% effective reduction. That sits in the middle of the critique's own 10–20% exclusion range.
   - The critique then also applies an unquantified "program-adoption factor" and discontinuation. The path from 10–20% exclusion to 0.45–0.50 is not shown step by step, and mixing in unspecified factors makes the lower end look more supported than it is.

**OFFSETTING FACTORS:**

1. The BOTEC values only on-treatment mortality. The Parameter Map lists morbidity DALYs, post-treatment mortality, transmission averted, and diagnostic value as implicit zeros. Any non-zero value for these is an upward offset to the same SROI the critique is lowering.

2. If pravastatin is the real candidate, interaction-driven prescribing restrictions fall away. That removes one of the largest classes of eligibility exclusions, so the 10–20% exclusion range is more likely an upper bound than a midpoint. This is conditional on the statin identity, which is unknown.

3. Uptake could plausibly exceed 60% in some settings if the drug is cheap and given within an existing TB program regimen. I cannot ground a specific figure. The point is only that the uptake uncertainty is two-sided, while the critique presents only the downside.

**OVERALL ASSESSMENT:** Partial defense.

- The direction of the critique is credible. The Parameter Map confirms CG did not model monitoring, adherence, or any empirical precedent for 60% uptake.
- The magnitude is weakly supported. The key numbers are ungrounded, the main DILI evidence is about the wrong drugs, and the central case stays within CG's materiality tolerance and above the bar.
- I stop short of "Strong" because the missing empirical anchor for 60% is a real gap that I cannot close with evidence.

**CONCESSIONS:**

1. CG gives no empirical precedent for the 60% uptake figure, and neither side has grounded the correct figure.
2. Monitoring and adverse-event management costs are absent from the $7M all-in cost. This is a legitimate omission, though it falls under all_in_cost, not adult_uptake.
3. The low-end tail (−30%) does cross the 25% materiality threshold, even though it does not cross the 2,000x bar.
4. The hepatotoxicity-attribution and pill-burden concerns do not depend on statin identity. They could reduce prescribing willingness somewhat, though I have no evidence on how much.

### Challenger
REBUTTAL: Clinical eligibility and monitoring barriers cap the achievable prescribing share

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: CG's 60% is already a 40-point haircut from universal uptake, so it has room to absorb liver-disease exclusions, reluctance, pregnancy and polypharmacy. The critique shows only that CG did not itemise them.

Response:
1. The Advocate also concedes that CG gives no empirical precedent for the 60%. A haircut with no derivation cannot be shown to cover any specific barrier, so "room for" is not evidence of coverage.
2. The claim is also unfalsifiable. If the 40% absorbs a 10–20% exclusion, it would absorb any exclusion up to 40%, and no eligibility critique could ever move the parameter.
3. The Advocate's own quote of the BOTEC describes the 60% as adults who "would add atorvastatin if it works." That is a prescriber-willingness framing. If the denominator is all adult patients, eligibility exclusions sit on top of willingness rather than inside it. The Parameter Map says only that adoption "may be partly captured… but this is not explicit." I cannot resolve which reading is right, and neither can the Advocate.
4. I concede that some overlap is plausible, so the full 15% need not be incremental.

> The Advocate claims: p_success of 40% is partly a hedge for real-world translation.

Response:
5. A joint Phase II/III success probability measures the chance that efficacy is demonstrated. It does not measure the share of eligible patients a program prescribes to after success. Calling it a hedge on deployment friction is an inference, and the Parameter Map does not support it.

> The Advocate claims: discontinuation is double-counted because trial-level discontinuation is embedded in relative_reduction.

Response:
6. The Advocate concedes that CG's 10% relative_reduction is "underived." A parameter with no derivation cannot be said to embed trial discontinuation.
7. Even if it were trial-anchored, trial retention under protocol-driven follow-up differs from routine-program continuation. The Advocate concedes this ("Real-world adherence may be worse than in a trial").
8. I concede the double-counting risk is real for the discontinuation component and that it should be trimmed from the critique. It is the weakest of the three mechanisms.

> The Advocate claims: monitoring costs belong to all_in_cost, not adult_uptake.

Response:
9. Accepted as a labelling point. But monitoring costs and uptake are two channels of one barrier, and both lower the same SROI. Section 3 of the magnitude response below takes up the joint effect.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the 0.45–0.50 range and the 10–20% exclusion are self-declared ungrounded.

Response:
1. Conceded. The critique labels them "UNGROUNDED — plausible but needs empirical support." What survives is the direction (some exclusion exists) and not the size. The 60% is equally unsourced, so the size of the gap is unresolved by either side, not shown to be small.

> The Advocate claims: the DILI incidence concerns anti-TB drugs, not statins, and so does not apply.

Response:
2. The incidence figure was not offered as a measure of statin withholding, and I concede that it does not quantify one. Its role is narrower.
3. A pooled ~11.5% (range 2–28%) means a large minority of the adult population will develop liver injury during treatment. In those patients a clinician must decide whether to continue a co-administered statin, whose label carries hepatotoxicity warnings.
4. That creates an attribution problem which exists only if the statin is added. The Advocate's point that programs already monitor for anti-TB DILI explains why the monitoring cost might be small. It does not remove the stop-or-continue decision.
5. The decision's effect on uptake is unknown. If a share s of DILI patients have the statin stopped, the lost coverage is roughly 11.5% × s, before time-weighting. I cannot ground s, so this is an illustration of the mechanism and not an estimate.

> The Advocate claims: the critique concedes the CYP3A4 and PI-boosted ART arguments fall away under pravastatin, leaving only soft, behavioural barriers.

Response:
6. The Advocate's own quote of the BOTEC says "atorvastatin," and the critique says it does not know which statin CG assumes. Atorvastatin is CYP3A4-metabolised, which is the verifier's own background point. If CG's candidate is atorvastatin, the interaction arguments do not fall away.
7. In that case the 10% effect would also be anchored to a different statin from the one in the cited Phase 2b trial (pravastatin). This is a statin-identity mismatch that neither side can resolve. The Advocate cannot use "if pravastatin" to dismiss interaction barriers while quoting a BOTEC that names atorvastatin.
8. Prescribing share is a behavioural quantity. Calling the surviving barriers "soft" does not make them small. Pill burden and hepatotoxicity attribution operate precisely through prescriber and patient behaviour, which is what adult_uptake measures.

> The Advocate claims: FDA removed routine LFT monitoring requirements from statin labels in 2012 (offered as an uninformed prior).

Response:
9. The Advocate flags this as ungrounded, so I treat it as such. It also addresses only mandated monitoring cost. It does not address clinician reluctance or attribution among patients already undergoing hepatotoxicity surveillance for anti-TB drugs.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

1. **Conceded.** SROI is linear in uptake: 0.60 → 0.42 gives 3,055 → 2,138, a ratio of 0.70, which matches the sensitivity output. Setting 2,000 = 3,055 × (u / 0.60) gives a breakeven uptake of about 0.39. The critique's own range of 0.45–0.50 (SROI ≈ 2,291–2,546) does not cross the 2,000x bar. On uptake alone this is not decision-flipping.
2. **A correction to the Advocate's numbers.** The critique's stated range of 0.45–0.50 implies a 17–25% decline, not 15%. The 15% central is the Quantifier's 0.51, which is milder than the critique's text. The 30% low (uptake 0.42) is harsher than the critique's text. The two are not the same scenario, so the Advocate cannot read the −15% as "the critique's central estimate."
3. **The residual.** Margin over the bar is 3,055 / 2,000 ≈ 1.53×. A 25% uptake loss (to 0.75× of baseline) takes 3,055 to 2,291, leaving only 1.15× margin. Any additional monitoring cost loaded onto all_in_cost, which the Advocate concedes is omitted, multiplies against that margin. I cannot quantify the monitoring cost. The point is only that the buffer shrinks from 53% to roughly 15% at the critique's low end, before any other change.
4. The Advocate's point that the "material" label overstates the central case is fair on the Quantifier's own criterion (>25% change or below 2,000x). I do not defend the label at −15%.

**RESPONSE TO "OFFSETTING FACTORS":**

1. **Implicit zeros for morbidity, post-treatment mortality, transmission and diagnostics.** These are real upward considerations, but they are unmodelled in CG's SROI. They do not change what adult_uptake should be, and the critique concerns whether this parameter is overstated. They bear on whether the bar is crossed, not on whether the parameter is correct.
2. **Pravastatin as the offset.** As in point 6 above, this is a conditional that the Advocate's own BOTEC quote undercuts. It is hypothetical and not in the model.
3. **Uptake above 60%.** The Advocate admits this is ungrounded ("I cannot ground a specific figure"). Two-sided uncertainty is a fair framing, but a symmetric uncertainty around a number with no anchor is not a reason to leave the parameter unflagged. It is a reason to flag it.

**KEY UNRESOLVED QUESTIONS:**
- Is the 60% defined over all adult TB patients or over eligible, treatment-willing ones? This determines whether eligibility exclusions are incremental to it.
- Which statin does CG assume? The Advocate's quote says atorvastatin and the trial is pravastatin, and the answer determines whether CYP3A4 and PI-ART interaction exclusions apply.
- What share of anti-TB DILI cases would lead to statin discontinuation (the s above)? No study in the evidence package measures it.
- Would LFT monitoring, if required, be an incremental cost or already embedded in TB care? This sets the combined uptake and all_in_cost effect against the 1.53× margin.
- What empirical anchor exists for any adjunctive-therapy uptake share in TB programs? Neither side has one.

### Judge Audit
Surviving strength: moderate
Justification: **Justification:** The debate was substantive rather than guess-trading. Both sides produced sound SROI arithmetic, and the Challenger made several honest concessions. Those concessions eliminated the critique's quantitative claim and its "material" label at the central case, which pushes toward weak. However, the Challenger surfaced a grounded, unrebutted problem: the BOTEC names atorvastatin while the evidence base is a pravastatin trial. This revives the interaction-exclusion mechanism and exposes a deeper anchoring issue. The Challenger also showed the bar margin narrowing to about 1.15× at the critique's low end before any monitoring cost is added. The critique therefore survives as a valid but not decision-flipping concern.
Recommended action: 2. SPECIFIC INVESTIGATION:**

**What to check.** Read CG's BOTEC source text to answer two questions:
- (a) Which statin is assumed? The BOTEC wording says atorvastatin, but the effect evidence comes from pravastatin.
- (b) Is the 60% defined over all adult DS-TB patients or over eligible/willing patients?

Both are document lookups and feasible immediately.

**How the answers change the conclusion.**
- If the candidate is atorvastatin, add a flag that CYP3A4/rifampicin and ART interactions apply. Also flag that relative_reduction may be anchored to the wrong drug. This second issue is potentially larger than the uptake critique itself.
- If the 60% is defined over all adults, exclusions are partly absorbed. In that case, retain the critique only as a low-magnitude directional note.

**What can be concluded now.** Absent these checks, with moderate confidence: adult_uptake should be flagged as unanchored, with a plausible downward skew. However, this uptake channel alone does not move SROI below 2,000x. Monitoring and adverse-event costs should be noted as an omission under all_in_cost.

**action_feasibility:** requires_specified_evidence
Action feasibility: requires_specified_evidence
Advocate failures: []
Challenger failures: []
Debate resolved: Within the critique's own stated range (0.45–0.50), the uptake reduction alone does not cross the 2,000x bar, since breakeven uptake is about 0.39. The specific magnitude is ungrounded, the discontinuation channel is largely double-counting, and the DILI incidence figure does not quantify statin withholding. What survives is the direction (some downward pressure on uptake) and the finding that CG's 60% has no empirical anchor.
Debate unresolved: Two questions remain genuinely contested:
1. **Denominator:** Is the 60% defined over all adult TB patients or over eligible, willing ones? This determines whether exclusions are incremental.
2. **Statin identity:** Does CG assume atorvastatin (per the BOTEC wording) or pravastatin (per the cited trial)? This determines whether CYP3A4/ART interaction exclusions apply, and whether the 10% effect is anchored to the right drug.

--- Critique: Private-sector treatment share and the reach of national guidelines are not modeled ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: Private-sector treatment share and the reach of national guidelines are not modeled
```

**EXISTING COVERAGE:**

1. **The 60% is already a reach-and-adoption haircut.**
   - The BOTEC applies 60% of adult patients adding atorvastatin "if it works," justified by the drug being "generic and cheap."
   - The report does not decompose the 60%. Any reading of it as a blended average across public and private channels is my interpretation, not something CG states.
   - Still, the figure is not 100%, so some non-adoption is already priced in. The critique does not show that the 40% haircut omits private-sector shortfalls.
2. **The denominator is treated cases, not all cases.**
   - The BOTEC starts from "current new TB cases," holds "the share of cases being treated" constant, and applies uptake only to that pool.
   - Care-seeking that never reaches treatment (the critique's "half of symptomatic people consult private providers") is therefore not in the 5.5M base.
   - The critique's own figure is that the private sector handles about one-third of *notified* cases. Those patients are linked to the system and plausibly already sit in the treated pool.
   - If so, the private-sector concern applies only to the dosing and adherence quality of the notified private slice, not to its inclusion. That is a much smaller concern than the hypothesis implies.
3. **Other conservative layers sit upstream.**
   - 40% probability that both Phase II and III succeed.
   - Only on-treatment mortality is valued, with morbidity, transmission and the diagnostic at implicit zero (per the Parameter Map).
   - These are not offsets to this specific parameter, but they mean the uptake parameter is not the only place caution is embedded.

**EVIDENCE WEAKNESSES:**

1. **The critique labels its own direction and size UNGROUNDED.** It says the figure is "inference, not sourced" and that the sign "could flip in specific countries." It asserts no downward effect. It points to a possible one.
2. **The cited evidence cuts both ways.**
   - Mandatory notification of all TB cases by private practitioners has existed in India since the 2012 Gazette notification.
   - Enforcement is weak, but the critique's own evidence notes "rising private-sector linkage to NTP drugs."
   - Rising linkage argues against a net downward adjustment in India, the highest-burden country.
3. **No statin-specific evidence is offered.** Nothing shows private providers would prescribe a statin adjunct at lower effective exposure than NTP providers. The "unsupervised and non-standard dosing" claim is plausible but unsourced.
4. **The mechanism is geographically narrow.** It rests on India's private-sector structure. Whether it generalizes to other high-burden countries is not shown, and the critique concedes sign flips by country.

**MAGNITUDE CHALLENGE:**

1. **The sensitivity range is asymmetric and weakly anchored.**
   - Low case: -15%, giving 2,597 against a replica baseline of 3,055.
   - High case: +5%, giving 3,208.
   - Quantifier central: 0.57 uptake (-5%), giving 2,902.
   - The -15% is the critique's own "5–15%" figure, which it says not to assert, so the low end is an uninformed prior.
2. **No scenario crosses CG's decision bar.** The sensitivity output shows `crosses_bar_low: false` for all cases. The worst case (2,597) stays above the ~2,000x bar.
3. **No scenario meets the 25% change threshold either.** The largest move is -15%.
4. **The "material" label does not follow.** By the context's own definition (below ~2,000x or a change above ~25%), this critique is not decision-relevant, even at its pessimistic bound.
5. **The central estimate is minimal.** A 5% move on a figure that already carries a 40% success haircut and a 10% relative-effect assumption is well within the BOTEC's rounding precision. The published ~3,000x and the replica's 3,055 differ by about 2%.

**OFFSETTING FACTORS:**

1. **Private providers may adopt faster.** The critique concedes that private providers "readily prescribe adjuncts" and may adopt a cheap generic "faster than NTPs." Where that happens, effective uptake rises, which is the +5% case.
2. **Private-sector linkage is increasing.** The critique's own evidence says private-sector linkage to NTP drugs is rising. That narrows the quality gap over the 8-year horizon before adoption, while the BOTEC's uptake is a post-Phase III figure.
3. **Part of the sign ambiguity cuts against GiveWell, and I flag it.** Pre-guideline private adoption would reduce the counterfactual value of the trial. That falls under the speedup parameter, not adult_uptake, so it does not rescue this critique's central claim. I note it so the offset is not overstated.

**OVERALL ASSESSMENT:** **Strong defense.**

- The critique is self-declared as ungrounded, with ambiguous sign and low-to-medium strength.
- Its evidence partly argues against its own downward direction.
- At its worst-case bound the estimate stays above the bar and below the 25% change threshold.
- The treated-case denominator already excludes much of the care-seeking population the critique emphasizes.

**CONCESSIONS:**

1. **The 60% is not decomposed.** The BOTEC does not separate public from private channels, and it provides no empirical precedent for 60%. Both are legitimate transparency gaps, also noted in the Parameter Map.
2. **Quality of private-sector exposure is plausibly lower.** Dosing and duration in unsupervised private care could reduce effective benefit. I cannot ground a magnitude for this, so I treat the -5% central as an uninformed prior, not as evidence.
3. **Country heterogeneity is unmodeled.** A global average uptake can hide sign differences across countries. That would matter more if the benefit were concentrated in a single country than for a global average.
4. **The adoption-lag and ramp concern is separate.** It is a different line item in the Parameter Map and is not defended here.

### Challenger
REBUTTAL: Private-sector treatment share and the reach of national guidelines are not modeled

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the 60% uptake is already a haircut for non-adoption, so some private-sector shortfall is priced in, and the critique has not shown the 40% omits it.

Response:
- The Advocate concedes the 60% is undecomposed and has no empirical precedent. That concession matters more than the Advocate lets on.
- The only stated rationale for 60% is that the drug is "generic and cheap." That is a product-level reason for adoption. It says nothing about delivery-channel reach, such as whether a guideline gets into private practice at all.
- "Some non-adoption is priced in" is therefore not the same as "private-sector non-reach is priced in." The Advocate cannot show the 40% was built with channels in mind.
- The residual risk is that the 60% is an unexamined number. It could be too high or too low, and nobody can tell from the report.

> The Advocate claims: the BOTEC denominator is treated cases, so notified private cases are plausibly already in the pool, which shrinks the concern to dosing and adherence quality.

Response:
- I concede the denominator point narrows the issue. Inclusion in the base is a separate question from guideline reach.
- Being in the treated pool does not mean the guideline reaches the prescriber. The Advocate's reframing to "dosing and adherence quality of the notified private slice" is itself the residual channel. It is the mechanism the critique named.
- The Advocate's "plausibly already sit in the treated pool" is an inference, not a verified fact. The Advocate does not know how the "share of cases being treated" is built or whether private-treated, unnotified cases are counted.
- The verifier's evidence cuts against the Advocate's assumption of clean linkage. The notification mandate has existed since 2012, but enforcement is weak and notification "has not really become routine practice."
- That means a meaningful private slice may sit outside the notification and NTP-drug channels through which a guideline would propagate. Those patients are treated but less reachable.
- I cannot size this slice. I treat it as an open question, not as evidence of a downward effect.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the evidence cuts both ways, since rising private-sector linkage to NTP drugs argues against a net downward adjustment, and no statin-specific evidence exists.

Response:
- The evidence is mixed, and I concede the sign is genuinely ambiguous. The critique said so itself.
- The linkage evidence and the weak-enforcement evidence are both in the verifier package. The Advocate cites the first as decisive and does not weigh the second.
- Linkage of drugs to NTP supply is a different thing from adoption of an adjunct-therapy guideline. Linkage helps only if the guideline travels with the drug supply. That is plausible but not shown.
- On "no statin-specific evidence": the verifier did not REJECT the unsupervised-dosing mechanism. The verifier found no direct evidence either way, which is UNVERIFIABLE, not contradicted.
- As a conditional: if private providers dose and sequence adjuncts non-standardly, effective benefit per treated patient falls. If they adopt before guidelines, counterfactual trial value falls (the speedup parameter). The Advocate agrees both are plausible.
- The Advocate's geographic-narrowness point is fair. The mechanism is evidenced only for India. Whether India's weight in the global average makes it dominant is unquantified.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: no scenario crosses the ~2,000x bar or the 25% change threshold, so "material" does not follow.

Response:
- I concede this. The sensitivity output shows `crosses_bar_low: false` throughout, and the worst case is 2,597 against a baseline of 3,055. On this single parameter, the critique does not change the decision.
- The "material" label looks overstated given the bar the context defines.
- The minimum plausible magnitude is approximately zero, or slightly positive in the +5% case. The Advocate is right that the -15% is an uninformed prior, because the critique itself says not to assert it.
- Two points remain:
  - The Advocate's claim that 5% is "within rounding precision" is not supported. The replica-versus-published gap is about 2%, and 5% is more than double that.
  - The sensitivity is one-parameter only. If the 60% is also unexamined for adoption lag or country mix, errors could compound. I cannot ground a combined magnitude, so this is a flag for the Judge, not a number.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: faster private adoption and rising linkage offset the downside.

Response:
- Both offsets are real in direction but unquantified. The +5% high case is an illustrative sensitivity input, not a sourced estimate. Neither the critique nor the Advocate has grounded it.
- The Advocate rightly notes that pre-guideline adoption falls under the speedup parameter. It therefore does not offset a decline in adult_uptake. It is a separate cost to the trial's counterfactual value.
- That cost is a downside the Advocate acknowledges but does not net against the upside offsets. The offsets are not clearly symmetric.
- The "narrowing over 8 years" argument rests on a trend the verifier describes only qualitatively. It does not establish convergence on post-guideline dosing quality.

**KEY UNRESOLVED QUESTIONS:**
- What does the 60% represent? Is it a blended public/private figure, a product-adoption judgment, or a generic prior? The report does not say.
- How is "share of cases being treated" built? Specifically, are privately treated but unnotified cases included?
- Does a guideline reach private prescribers through PPSA or NTP-drug linkage in practice, given weak enforcement of notification?
- Does non-standard private dosing of an adjunct meaningfully reduce effective benefit, or are private providers closer to standard practice for statins specifically?
- Does India dominate the global-average uptake enough for its private-sector structure to move the aggregate?

### Judge Audit
Surviving strength: weak
Justification: - The debate was productive. The Advocate's grounded sensitivity analysis showed that the critique's worst case stays above the bar and below the change threshold, and the Challenger conceded this directly.
- The critique labels itself ungrounded and sign-ambiguous. The verifier package partly contradicts its downward direction for India.
- The Challenger's surviving points are a call for transparency about the 60% and a speculative compounding concern. Neither is grounded.
- The verdict is "weak" because the critique was tested and did not hold up as decision-relevant, not because the debate failed.
Recommended action: 1. CONCLUDE NOW: With moderate-to-high confidence, make no adjustment to adult_uptake for private-sector reach.
   - The concern is directionally ambiguous and unsourced in magnitude.
   - It is non-decision-relevant even at its pessimistic bound.
   - One residual valid point should be recorded as a documentation note, not a model change: the 60% uptake figure has no stated channel decomposition or empirical precedent.
   - If CG revisits the parameter, the cheapest useful step is to state what the 60% is intended to represent. No new evidence collection is warranted on the basis of this critique alone.
Action feasibility: actionable_now
Advocate failures: ['unsupported_estimate_pseudo: A 5% move ... is well within the BOTEC\'s rounding precision. The published ~3,000x and the replica\'s 3,055 differ by about 2%." A 2% replica gap does not show that a 5% parameter move is within precision. The Challenger correctly caught this gap. The point does not affect the Advocate\'s main magnitude argument, which rests on the bar and the threshold, not on rounding.', 'sound_synthesis_noted: The sensitivity cases are correctly derived from the replica baseline:', 'false_definitiveness: The overall assessment says "The treated-case denominator already excludes much of the care-seeking population the critique emphasizes." The body argued this only conditionally ("plausibly already sit in the treated pool"; "If so..."). The summary hardens a conditional inference into a settled point. This is mild, but it inflates the "strong" self-assessment.']
Challenger failures: ['strawmanning: The Advocate cites the first as decisive and does not weigh the second." The Advocate\'s heading was "The cited evidence cuts both ways," and it explicitly acknowledged that "enforcement is weak." The Advocate did not call linkage decisive.', 'call_to_ignorance: There are two instances.']
Debate resolved: Both sides agree, and the Challenger explicitly concedes, that this critique does not change the decision even at its pessimistic −15% bound: 2,597 against a ~2,000x bar, with no case crossing the 25% change threshold. Both sides also agree that the sign of the effect is genuinely ambiguous. The debate further established that the 60% uptake figure is undecomposed and rests on a product-level rationale rather than a channel-level one. This is a transparency gap, not a demonstrated bias.
Debate unresolved: Two questions remain contested:
- Whether privately treated patients in the BOTEC's treated pool are reachable by guideline channels (PPSA, NTP drugs, professional bodies), or sit outside them.
- Whether unsupervised private dosing materially reduces effective benefit for a cheap oral adjunct.

Neither side produced evidence on either question, and the Advocate did not deploy the available counter-evidence: the notification-gap reduction and the IMA engagement.

--- Critique: Zero modeled lag between Phase III completion and adoption, and a speedup that assumes trial timing is the binding constraint ---

### Advocate
DEFENSE OF GIVEWELL'S (CG's) POSITION: Zero modeled lag between Phase III completion and adoption, and a speedup that assumes trial timing is the binding constraint

**EXISTING COVERAGE:**

1. **Post-Phase-III lag barely matters in a speedup model.** CG's value is the benefit of shifting adoption earlier by 1 year, not the benefit of adoption itself. Any lag after Phase III (guideline adoption, national procurement) is plausibly common to the grant and no-grant timelines, so it shifts both adoption curves equally.
2. **Derivation: the shape of the ramp drops out without discounting.** Let A(t) be the adoption curve and s the speedup. The gain from the shift is ∫[A(t) − A(t−s)]dt, which equals s × A(∞) if A saturates. This is the same as one year at the steady-state 60% uptake, whatever the ramp shape or length. So the missing "ramp" and the missing lag do not bias the estimate in the undiscounted formula.
3. **The only channel through which lag enters is the 2% annual decline in eligible cases.** The Quantifier's own sensitivity run quantifies this:
   - Lag of about 5 extra years (years_to_adoption high) gives −9.6%. This matches 0.98⁵ ≈ 0.904.
   - The Quantifier's central of 10 years gives −3.96%.
   - Both are well inside the ~25% materiality threshold and nowhere near the ~2,000x bar (2,761x and 2,934x versus 3,055x baseline).
4. **The critique concedes this.** Its mechanism section says lag "is not material alone."
5. **Discounting is a separate thread.** The critique itself defers the discounting interaction to Thread 3. Lag only matters more once a discount rate is added, and that is a different parameter (the implicit discount rate), not a defect in the lag treatment.

**EVIDENCE WEAKNESSES:**

1. **The HPMZ case does not support the critique.** The critique admits that WHO acted within weeks of the 2021 publication, with consolidated guidelines in 2022. That cuts against a long post-trial lag. The critique says it "does not contradict" the central point, but it also does not support it.
2. **No country-uptake data were found.** The critique says so explicitly. The claim that national adoption adds material lag therefore rests on the Xpert analogy, which is qualitative.
3. **The Phase III funding gate and the claim that expected speedup is below 1 are flagged UNGROUNDED** in the critique's own hypothesis. UNGROUNDED does not mean false, but nothing in the evidence package pushes the speedup in either direction.
4. **The critique concedes lumpiness does not lower expected speedup.** If decision timing is uniformly random, the expected shift equals the trial shift. That removes one of the two stated reasons for a lower speedup. What remains is the claim that the trial is not on the critical path, which is exactly the ungrounded part.
5. **The Quantifier's central of 0.9 years has no derivation.** It is a 10% haircut with no source or chain behind it. The −10% result is just the arithmetic of that choice.

**MAGNITUDE CHALLENGE:**

1. **Speedup scales linearly.** To fall below the ~2,000x bar, speedup must drop to roughly 2,000/3,055 ≈ 0.65 years. That is a 35% reduction in the speedup, derived from the baseline in the sensitivity output. The central 0.9 does not get there.
2. **Even at 0.9, the move is −10%.** That is below the ~25% materiality line, and SROI stays at ~2,749x, above the bar.
3. **Only the low case of 0.5 years crosses the bar (−50%).** The critique offers no grounding for that value. It is a bound, not an estimate.
4. **Combining the two channels barely changes this.** The speedup and lag effects multiply roughly as 0.90 × 0.96 ≈ 0.86 at the Quantifier's centrals. That is about −14%, still above the bar.

**OFFSETTING FACTORS:**

1. **The critical-path argument cuts both ways.** If Phase III funding is gated on Phase IIc results, as the critique's own funding-gate hypothesis suggests, then without the grant the delay could exceed 1 year, or Phase III might never happen. The Quantifier's high case (speedup 1.25) gives +25%. Taking the funding-gate claim conditionally, it points toward more speedup, not less.
2. **The BOTEC leaves out several benefit channels** (see Parameter Map): morbidity and lung damage, post-treatment survival, transmission, and diagnostic value. These are implicit zeros and push the estimate down relative to a full accounting.
3. **The BOTEC's 2% annual decline in cases is applied through year 8.** The −9.6% sensitivity above assumes that decline continues through extra lag years. If the decline is slower, lag costs less than the −9.6% shown.

**OVERALL ASSESSMENT: Partial defense**

- The lag component is strongly defensible. It is mathematically near-neutral in an undiscounted speedup framework and costs at most ~4–10% through case decline.
- The speedup component is only partially defensible. CG gives no justification for exactly 1 year (Parameter Map: "No justification for 1 year rather than some other speedup"). The critique has not shown that the trial is off the critical path, but CG has not shown that it is on it either.
- The critique is rated low–medium by its own author, and its quantified downside at the Quantifier's central does not cross the bar. The residual vulnerability is the unexamined 1-year assumption, which is only decision-relevant if the true speedup is below ~0.65 years.

**CONCESSIONS:**

1. CG gives no derivation of the 1-year speedup. The point estimate is an assumption, not a result.
2. The speedup could plausibly be below 1 if the Phase III would have proceeded on a similar timeline without this trial. I cannot ground a probability for that.
3. Once discounting is introduced, lag and ramp shape begin to matter. The undiscounted neutrality argument above does not carry over, and that interaction is not resolved here.
4. National adoption lag is real in analogous cases such as Xpert. I accept that arguendo, but it does not change the speedup unless the lag differs between the grant and no-grant timelines.

### Challenger
REBUTTAL: Zero modeled lag between Phase III completion and adoption, and a speedup that assumes trial timing is the binding constraint

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: post-trial lag is common to the grant and no-grant timelines, so it shifts both adoption curves equally. Undiscounted, the gain is s × A(∞) regardless of ramp shape, so the only cost of lag is the 2%/yr case decline (−4% to −10%).

Response:

1. **"Lag is common to both timelines" assumes the conclusion in dispute.**
   - It holds only if post-trial steps are strictly sequential after the trial, so that trial delay maps one-for-one into adoption delay.
   - The critique's concern is the opposite case: guideline, procurement, or country-readiness gates run partly in parallel with the trial, or bind regardless of it. Then the trial shift is partly absorbed and speedup < trial shift.
   - The Advocate's argument establishes that lag doesn't matter given speedup = 1. It does not establish that speedup = 1.
   - This is a restatement of the critique's critical-path point, not a rebuttal of it.

2. **The s × A(∞) identity needs an unstated condition.**
   - It requires the horizon to extend far enough that both curves have saturated.
   - Over a finite horizon T, the gain is ∫[A(t) − A(t−s)]dt = ∫ from T−s to T of A(t)dt. That equals s × A(∞) only if A has saturated by T−s.
   - The Advocate says the decline is "applied through year 8," which suggests a finite horizon. I cannot confirm the model's horizon.
   - Conditional on a finite horizon, longer lag and a slower ramp push T−s into the ramp and reduce the gain below s × 60%. The "ramp drops out" claim is therefore not free.

3. **The Advocate's own concession 3 undercuts the "barely matters" framing.**
   - With discounting at rate r, a common shift of L years scales the whole gain by (1+r)^−L. Common lag does not cancel.
   - Illustrative only, with r = 4% as my assumption, not a model parameter:
     - From the sensitivity output, the 0.98-based figures imply a baseline of about 8 years, a central of 10 and a high of 13. This is inferred from −3.96% = 0.98² and −9.6% = 0.98⁵.
     - Central: 1.04^−2 = 0.925, so 0.9604 × 0.925 = 0.888 (about −11%), versus the Advocate's −4%.
     - High: 1.04^−5 = 0.822, so 0.904 × 0.822 = 0.743 (about −26%), versus −9.6%.
   - Combined with the 0.9 speedup central, the high case gives 0.743 × 0.90 ≈ 0.67 (about −33%), which is near or past the Advocate's 25% materiality line.
   - Deferring this to "Thread 3" doesn't remove it. The lag parameter is where the interaction would be realized.

4. **Concession.** At the undiscounted centrals, the Advocate's arithmetic (0.90 × 0.96 ≈ 0.86) is correct and stays above the bar. The lag channel alone is not decision-relevant undiscounted.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: HPMZ cuts against a long lag, no country-uptake data exist, the funding-gate and speedup<1 claims are UNGROUNDED, and the 0.9 central is an underived 10% haircut.

Response:

1. **HPMZ (WHO action within weeks).**
   - I concede this shrinks the WHO-step component of lag.
   - The verifier recorded that it does not contradict the critique and that no HPMZ country-uptake data were found. That is "not found," not contradicting evidence.
   - Whether national adoption adds lag is therefore an open question, not a refuted one. The Advocate treats the absence of data as mild support for its side.

2. **The 0.9 central is underived, and so is the 1.0 baseline.**
   - The Advocate concedes CG gives no justification for exactly 1 year.
   - The Advocate cites the lack of derivation for 0.9 to dismiss the −10%, but the conclusion "the critique doesn't cross the bar" depends on the speedup being near 1.
   - The accurate summary is that neither 1.0 nor 0.9 is grounded. The bar sits at 0.65, inside the range of plausible values (the Quantifier's own low bound is 0.5).

3. **Lumpiness.** Conceded. It does not lower the expected speedup. That leaves only the critical-path claim, which I agree is ungrounded.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: speedup must fall to about 0.65 to cross the bar, and 0.9 gives only −10% (about −14% combined).

Response:

1. **What 0.65 requires, as a probability.**
   - If the counterfactual is "Phase III proceeds on a similar timeline anyway" with probability p, giving speedup ≈ 0, and the speedup is 1 otherwise, then expected speedup = (1−p) × 1.
   - Setting that to 0.65 gives p = 0.35.
   - The Advocate concedes it cannot ground p, and I cannot either. The threshold is a 35% chance that the trial isn't binding, which is not an extreme claim for a program-funding counterfactual. This is a conditional, not an estimate.

2. **The Quantifier's own bounds are asymmetric around 1.**
   - Low is 0.5 (−50%) and high is 1.25 (+25%). The midpoint is (0.5 + 1.25)/2 = 0.875, or about −12.5%.
   - This supports a central slightly below 1 on the Quantifier's own range. It is not independent evidence for it.

3. **Minimum defensible impact.** About −10% to −14% undiscounted, and about −20% to −33% if discounting applies (point 3 above). That is below the bar at the centrals, but it sits near the materiality line. The critique's own author rates it low–medium, and I don't contest that.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: the funding gate cuts upward, omitted benefit channels push CE up, and slower case decline reduces lag cost.

Response:

1. **Funding gate cuts both ways.**
   - Conceded: if Phase III is gated on this grant, speedup could exceed 1.
   - The Quantifier caps the upside at 1.25. If Phase III would never happen, the speedup is unbounded.
   - This shows a symmetric-variance argument, not that 1.0 is unbiased. The gate claim is UNGROUNDED, so it cannot offset a downside risk that is also ungrounded.

2. **Omitted benefit channels (morbidity, transmission, diagnostics).**
   - These are real, but the Advocate gives no magnitudes.
   - They are also benefits of earlier adoption, so they scale with speedup. A lower speedup reduces them proportionally, and they are not independent of the critique.
   - They raise the level of CE but do not offset a proportional speedup reduction.

3. **Slower case decline.** The direction is right (less lag cost), but this is small relative to the other considerations. Slower decline also raises the baseline benefit, so the effect cancels in part.

**KEY UNRESOLVED QUESTIONS:**

- Is the model horizon finite? If so, does the saturated-ramp identity hold at the horizon, or does lag/ramp truncate the gain?
- Is the model discounted, or will it be (Thread 3)? If so, the "common lag cancels" argument fails, and the lag cost ranges from about 11% to 26% on my illustrative 4% rate.
- What is the probability that Phase III proceeds on a similar timeline without this trial? The bar corresponds to p ≈ 0.35.
- Are post-trial gates (guidelines, national procurement) sequential to the trial, or do they run in parallel with it? This is the crux of the critical-path claim, and no HPMZ country-uptake data exist to settle it.

### Judge Audit
Surviving strength: moderate
Justification: The debate was largely productive. Both sides made grounded derivations: the 0.65 threshold, the 0.98ⁿ decomposition, and the finite-horizon and discounting conditions on the shift-invariance identity. The Challenger exposed a real unstated condition in the Advocate's strongest argument. However, the critique's decision-relevant claim (speedup < ~0.65) remains ungrounded, and at all undiscounted centrals the effect (−10% to −14%) stays above the bar. The Challenger's push toward −33% relied on an assumed discount rate and a high-case lag mislabeled as a "minimum," so the critique survives as a valid flag of an unjustified parameter, not as a demonstrated material error.
Recommended action: 2. SPECIFIC INVESTIGATION, with these conclusions available now:

**Conclude now (moderate confidence):** The lag concern is immaterial in the current undiscounted model. The 1-year speedup should be flagged as an unjustified assumption, with a sensitivity band reported (e.g., 0.5–1.25), and the explicit note that the conclusion flips only below ~0.65 years.

**Investigate:**
- **(a) Model structure.** Inspect the model directly for its time horizon, whether adoption saturates before the horizon, and whether any discount rate is applied or planned under Thread 3. This is trivially feasible with model access and determines whether the lag channel matters at all.
- **(b) Phase III funding path.** Run targeted searches of trial registries and funder announcements (e.g., Unitaid, TB Alliance, NIH/ACTG, EDCTP) for this regimen. The aim is to establish whether a Phase III is already funded or committed independent of the IIc timing. This is feasible within existing verifier tooling and would directly bound p.
Action feasibility: requires_specified_evidence
Advocate failures: ['sound_synthesis_noted: The bar-crossing threshold (2,000/3,055 ≈ 0.65 years of speedup) is derived directly from the sensitivity baseline. The check that the −9.6% figure equals 1 − 0.98⁵ is correct. The combined-channel arithmetic (0.90 × 0.96 ≈ 0.86) is correct, and the Challenger conceded it. These are grounded, transparent derivations.', 'false_definitiveness: The Advocate calls the lag component "strongly defensible" and "mathematically near-neutral." Yet Concession 3 admits that under discounting "the undiscounted neutrality argument above does not carry over." The s × A(∞) identity is also stated without its saturation/infinite-horizon condition. That condition is a real gap, which the Challenger identified.', 'strawmanning: Offsetting Factor 1 reframes the funding gate in the opposite direction. The critique\'s "generic drug has no sponsor, so Phase III funding could gate the timeline" is an argument that funding, not IIc timing, is the binding constraint. The Advocate recasts it as "Phase III gated on Phase IIc results → without the grant, delay exceeds 1 year." That is a different causal structure, so the claimed reversal is not a fair reading of the critique.', 'whataboutism (mild): Offsetting Factor 2 argues that omitted benefit channels (morbidity, transmission, diagnostics) "push the estimate down." This is a separate weakness of the BOTEC and does not respond to a proportional reduction in speedup. The Challenger correctly noted these channels also scale with speedup.']
Challenger failures: ['sound_synthesis_noted: Three moves are sound, conditional, and well-labeled:', 'unsupported_estimate_pseudo: The Challenger labels "−20% to −33% if discounting applies" the "minimum defensible impact." This has three problems:', 'call_to_ignorance (mild): A 35% chance that the trial isn\'t binding … is not an extreme claim for a program-funding counterfactual." No base rate is offered. The fact that p cannot be grounded is used to suggest the threshold is plausibly reached.', 'strawmanning (mild): The Advocate treats the absence of data as mild support for its side." The Advocate\'s HPMZ point rested on positive evidence (fast WHO action), and its uptake point was that the claim rests only on a qualitative analogy. Neither treats absence of evidence as support.', 'false_definitiveness (minor): Slower decline … the effect cancels in part" is asserted without derivation.']
Debate resolved: Both sides agree on four points:
- Undiscounted, the post-trial lag channel costs roughly 4–10% and is not decision-relevant.
- Lumpiness does not lower expected speedup.
- HPMZ shows the WHO step can be very short.
- The CEA crosses the ~2,000x bar only if expected speedup falls to about 0.65 years. Under a binary counterfactual, that corresponds to roughly a 35% probability that Phase III proceeds on a similar timeline without this trial.

Both sides also agree that neither the 1.0 baseline nor the 0.9 central is derived.
Debate unresolved: Two questions remain open:
- Whether the model uses a finite horizon and/or discounting. If it does, common lag no longer cancels, and lag cost could plausibly reach the 10–25% range.
- Whether this trial is on the critical path, specifically whether Phase III funding and national gates are sequential to it or independent of it. Neither side produced evidence on this, and it determines whether speedup is near 1 or well below.

--- Critique: Survivors' excess mortality and comorbidity shrink the 27 DALYs per death ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: Survivors' excess mortality and comorbidity shrink the 27 DALYs per death
```

**EXISTING COVERAGE:**

1. **27 is described as "remaining healthy life expectancy."** This is a healthy-life measure, not raw remaining life expectancy.
   - Healthy life expectancy is already lower than total life expectancy, because it discounts years lived in poor health.
   - The critique itself puts remaining life expectancy for a ~40-year-old in an LMIC life table at "low-to-mid 30s." Against that, 27 is already about 10–20% below total life expectancy.
   - The 10–20% figure is my own arithmetic from the critique's life-table numbers (27 vs. 30–35). It is not a sourced HALE decomposition.
   - Part of what the critique wants to subtract (comorbidity and morbidity in survivors) may therefore already be in the 27. The critique concedes this ("partly offset if 27 is already a healthy-life measure").
2. **The provenance of 27 is unknown.** The critique labels it UNGROUNDED, and the CG text does not say which age or life table underlies it.
   - Any adjustment is conditional on how 27 was built. If it came from an age-appropriate or TB-population life table, some excess mortality may already be embedded.
   - I cannot ground which is true. I note only that the critique's central claim is conditional on an unresolved question.
3. **CG does not model survivors' excess mortality explicitly.** I concede this (see Concessions).

**EVIDENCE WEAKNESSES:**

1. **The pooled SMR is a poor fit for the averted-death population.**
   - Romanowski 2019 (SMR 2.91, CI 2.21–3.84) is a pooled all-cause estimate. The critique's own evidence package contains a 2026 cohort with RR 1.77, so the evidence base spans roughly 1.8–2.9, a wide range.
   - Choosing k is the main driver of the magnitude. The critique's own calculation shows that moving k from 2.9 to 1.8 roughly halves the reduction.
   - I cannot ground which estimate fits the statin-treated, mostly drug-susceptible population better. The critique cannot either.
2. **The Gompertz derivation is the critique's own inference and is labeled as such.** It assumes a proportional hazard multiplier that is constant across age.
   - The critique's own evidence says post-TB burden is greater in younger people.
   - If relative excess mortality varies with age, the "ageing by ln(k)/b years" shortcut is only approximate. It could err in either direction, and the critique does not test this.
3. **Confounding is untested.** All-cause SMR in survivors reflects HIV, smoking, alcohol, diabetes and poverty, not only TB sequelae.
   - These risks would also apply to any person whose death is averted. Conditional on that, the critique's direction holds.
   - But the 1.77 RR figure is already lower than the pooled estimate, which suggests confounding or adjustment explains part of the gap. The critique does not separate attributable from non-attributable excess.
4. **The lifetime-burden study (12.1 DALYs per case, 5.8 from sequelae) does not support a reduction in years gained per death averted.** It measures burden per incident case. The critique concedes it shows that such estimates "can include post-TB effects," so it is neutral at best on the question at hand.

**MAGNITUDE CHALLENGE:**

1. **The critique is internally inconsistent on size.** The hypothesis says 10–25%. The mechanism says 20–30%, which yields 19–22 DALYs.
   - Applying 10–25% to 27 gives 20.3–24.3, not 19–22. The critique's own range is therefore less severe than its mechanism text.
2. **The sensitivity run uses an extreme point.** The "low" case is 20 DALYs per death, a 25.9% decline, which sits at the extreme end of the critique's own 10–25% range.
   - The Quantifier's central value is 24, which gives SROI ≈ 2,715x and −11.1%.
   - Neither case crosses the 2,000x bar (`crosses_bar_low: false`, central also false). Even the low case (SROI ≈ 2,263x) stays above 2,000x.
   - The −11.1% central figure is below CG's ~25% decision-relevance threshold.
3. **The "27 falls near or below 17.7" claim does not follow from this critique alone.**
   - The 17.7 break-even is where SROI hits 2,000x. This is my arithmetic: 27 × 2,000 / 3,055 ≈ 17.7.
   - Reaching it needs a further ~10–20% reduction from other critiques, such as relative_reduction or p_success. The critique itself says "once combined with any other downward adjustment." This critique, taken alone, does not reach the break-even.
4. **If k is nearer 1.8, the reduction is roughly 5–12%.** This follows the critique's own statement that using k ≈ 1.8 about halves the effect. That falls well below the materiality threshold.

**OFFSETTING FACTORS:**

1. **CG's BOTEC values only on-treatment mortality.** The parameter map lists morbidity DALYs, post-treatment mortality DALYs, transmission and diagnostic value as "implicit zeros."
   - The trial tests lung damage. The critique's own evidence says 5.8 of 12.1 lifetime DALYs per case come from post-TB sequelae.
   - A statin that reduces lung damage would act on the very burden the critique invokes. That gain is not credited in the BOTEC.
2. **The 6% baseline mortality may be understated.** The parameter map flags notified-cohort deaths versus true mortality (unascertained deaths) as something that could raise baseline_mortality. That would offset a DALYs-per-death reduction.
3. **There is no discounting, which cuts the other way.** The critique's reduction concerns remaining years, but discounting would shrink far-future DALYs even more. I flag this only as a mechanism the critique does not address.

**OVERALL ASSESSMENT:** **Partial defense.**

- The direction of the critique is right. No explicit survivor-mortality adjustment exists in the BOTEC, and a general-population life expectancy applied to people with elevated mortality plausibly overstates years gained.
- The magnitude is overstated relative to the critique's own evidence. The central impact is about −11%, and even the extreme case stays above the 2,000x bar.
- The key dependency, how 27 was built, is unresolved. The healthy-life framing may already absorb part of the effect.

**CONCESSIONS:**

1. CG does not explicitly adjust for survivors' excess mortality. The "WHAT CG DOES NOT ACCOUNT FOR" list is accurate on this point.
2. Elevated all-cause mortality in TB survivors is supported by two independent sources (Romanowski 2019 and the 2026 cohort). A downward adjustment to 27 of at least ~5–15% is directionally warranted.
3. If 27 was derived from general-population HALE with no adjustment for TB survivors, the critique's amplified scenario applies. I cannot rule that out.
4. The critique stacks with other downward critiques on 27 and could contribute to crossing the 17.7 break-even in combination. That is a question for the Synthesizer, not a defect in this defense.

### Challenger
REBUTTAL: Survivors' excess mortality and comorbidity shrink the 27 DALYs per death

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: 27 is described as "remaining healthy life expectancy," so it is already about 10–20% below total life expectancy. Some survivor morbidity and excess mortality may therefore already be embedded in it.

1. **The 10–20% gap is not evidence that survivor effects are embedded.**
   - The Advocate computed it from the critique's illustrative "low-to-mid 30s" life expectancy, which was never sourced to CG's life table.
   - The comparison assumes an age of about 40, and the age underlying 27 is unknown.
   - A gap measured against an assumed benchmark cannot show that anything specific is "already in" the 27.
2. **A healthy-life adjustment and a survivor hazard multiplier are different mechanisms.**
   - HALE-type measures discount years for general-population ill health.
   - They do not apply a 1.8–2.9× hazard multiplier for having had TB.
   - If 27 is general-population HALE, the two effects stack. They do not substitute for each other.
   - The Advocate offers no basis for saying the HALE discount overlaps with the TB-specific excess.
3. **The provenance of 27 is UNGROUNDED, which is not the same as REJECTED.**
   - The Advocate treats the unknown as a possible offset ("some excess mortality may already be embedded").
   - The unknown is symmetric. The Advocate's own Concession 3 admits the amplified scenario cannot be ruled out.
   - An open question that is equally likely to cut either way is not "existing coverage."
4. **Residual risk.**
   - CG has no explicit survivor adjustment, which the Advocate concedes.
   - What remains unaddressed is the full 10–25% hypothesis range, scaled by the chance that 27 is an unadjusted general-population figure.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the pooled SMR (2.91) is a poor fit, the evidence spans 1.8–2.9, and choosing k drives the magnitude.

1. **Even the low end of k leaves a material reduction. The Advocate's "5–12%" is an arithmetic slip.**
   - The critique's mechanism gives 20–30% at k ≈ 3, and the verifier package says k ≈ 1.8 "roughly halves" that.
   - Halving 20–30% gives 10–15%, not 5–12%.
   - Derivation: ln(1.8) ≈ 0.588. Dividing by b = 0.09–0.10 gives about 5.9–6.5 years of effective ageing, against about 11–12 years for k = 3.
   - This matches the hypothesis's 10% lower bound. The k = 1.8 case therefore sits at the critique's floor, not below it.
2. **Both endpoints are cohort-derived estimates of excess mortality in treated populations.**
   - Romanowski 2019 reports SMR 2.91 (CI 2.21–3.84), and the 2026 cohort reports RR 1.77.
   - The Advocate says it cannot ground which fits the statin-treated population better.
   - The two sources therefore define the range, and no evidence supports a k near 1.
3. **On the constant-hazard Gompertz shortcut, the Advocate says the error could go "either direction." The evidence points one way.**
   - The verifier package says post-TB burden per case is greater for younger people.
   - That is per-case DALY burden, not SMR, so I treat it as suggestive only.
   - Pooled relative mortality risks usually fall with age, but I cannot ground that here. Treat it as an uninformed prior.
   - If relative risk is higher at younger ages, a constant multiplier understates the loss for the younger patients who dominate DALYs gained.
4. **Confounding does not weaken the adjustment. The Advocate half-concedes this.**
   - The relevant quantity is the life expectancy of the person whose death is averted, not the TB-attributable share.
   - HIV, smoking, alcohol and poverty travel with that person.
   - The "1.77 is lower, so confounding explains the gap" inference is speculation. Differences in population, setting and comparator could equally explain it, and the Advocate cannot ground it.
5. **Averted-death patients are probably sicker than the average survivor, so average SMRs may understate their excess mortality.**
   - This is an inference. The people whose deaths a statin averts are those who would otherwise have died on treatment, a more severe subset than the average survivor.
   - I cannot ground the size of this effect. It is a direction-of-bias flag, not a number.
6. **On the lifetime-burden study, I concede it is neutral on years gained per death averted.**
   - It supports only that post-TB burden is material and age-graded.
   - The Advocate also relies on its 5.8-of-12.1 sequelae figure in the offsets section, so it cannot be inert as evidence and live as an offset.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: the critique is internally inconsistent (10–25% vs 20–30%), the central impact is −11%, no case crosses 2,000x, and reaching 17.7 needs other critiques.

1. **I concede the internal inconsistency.**
   - 27 × (1 − 0.10 to 0.25) = 20.25–24.3, while the mechanism text implies 19–22.
   - The hypothesis range, which already incorporates the k ≈ 1.8 evidence, is the better-grounded one.
2. **I concede that this critique alone does not cross the bar.** The sensitivity output shows `crosses_bar_low: false`, and the low case is about 2,263x.
3. **The Quantifier's central of 24 sits near the low end of the critique's range.**
   - The midpoint of 10–25% is 17.5%, which gives 27 × 0.825 ≈ 22.3.
   - Scaling the baseline of 3,055x gives about 3,055 × 22.3/27 ≈ 2,520x, or −17.5%. The Quantifier's 24 gives −11.1% (2,715x).
   - The Advocate's "−11%" therefore rests on a choice of central value that is lenient toward the baseline.
4. **The stacking arithmetic depends on that choice.**
   - The break-even is 27 × 2,000/3,055 ≈ 17.7 (the Advocate's figure, which I verify).
   - From 24, a further reduction of 1 − 17.7/24 ≈ 26% is needed.
   - From 22.3, a further reduction of 1 − 17.7/22.3 ≈ 21% is needed.
   - From 20.25 (the −25% end), only about 13% more is needed.
   - This critique supplies one-third to three-quarters of the 34.5% total reduction needed (1 − 17.7/27). The Advocate concedes this is a question for the Synthesizer.
5. **The 25% decision threshold is not the right test for a component that stacks.** A −11% to −18% effect on one multiplicative input is relevant whenever other inputs also move down.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: CG values only on-treatment mortality, the 6% baseline mortality may be understated, and the lack of discounting cuts the other way.

1. **Unmodelled morbidity and lung-damage benefits are not offsets to this parameter.**
   - They would raise benefits through other channels, such as morbidity DALYs, which the parameter map lists as implicit zeros.
   - They would not make the 27 per death more accurate.
   - Their realisation also depends on trial lung-damage outcomes translating into fewer sequelae. The Advocate does not show that this is verified.
   - The Advocate cannot cite a quantified, in-model offset of this kind.
2. **The baseline-mortality point is flagged in the parameter map but unquantified.**
   - It is UNVERIFIABLE, not rejected, so it is a conditional: if mortality is understated, deaths averted rise.
   - It scales the number of deaths. It does not change years per death, so it does not offset a per-death reduction.
   - It would also apply regardless of this critique.
3. **The discounting point is mislabelled as an offset.**
   - Omitting discounting inflates far-future DALYs. That is the same direction as the critique (overstated value), not an offset.
   - The Advocate's mechanism does carry a real point: discounting would shrink the tail years that survivor excess mortality removes. That would reduce the size of this adjustment, but it is not in the model and not quantified.
4. **Net result.** No offset is both in the model and quantified.

**KEY UNRESOLVED QUESTIONS:**

- What age and life table underlie the 27, and is it a general-population HALE or a TB-population figure? Everything in the critique turns on this.
- Is the excess mortality of statin-averted-death patients closer to 1.8 or to 2.9, or higher, given they are a sicker subset?
- Does relative excess mortality decline with age enough to break the constant-hazard Gompertz shortcut, and in which direction?
- Should the Quantifier's central be the midpoint of the critique's range (about 22) instead of 24, given that it changes how much further reduction is needed to reach 17.7?
- Does any other critique reduce 27 or its inputs by at least 13–26%, depending on where within 10–25% this critique lands?

### Judge Audit
Surviving strength: moderate
Justification: The Challenger landed a grounded correction of the Advocate's k ≈ 1.8 arithmetic and a correct conceptual rebuttal of the "healthy life expectancy already absorbs it" defense. Together these keep the effect at roughly 10–25% rather than 5–12%. The Advocate, in turn, established through sound arithmetic that the critique overstated itself (19–22 versus 20.3–24.3) and that it does not cross the 2,000x bar on its own. The Advocate's strongest available defense was never made: excess mortality decays with time since treatment, so a lifelong constant k overstates the reduction. Its absence leaves the magnitude question genuinely open rather than settled in the critique's favour.
Recommended action: 1. CONCLUDE NOW: Apply a downward adjustment to 27 DALYs per death of about 10–20%, with a central estimate of about 15% (27 → about 23), with moderate confidence. Treat it as a stacking input for the Synthesizer, not a standalone decision-changer. Flag that the adjustment roughly doubles to the upper end if 27 is confirmed to be unadjusted general-population HALE, and shrinks if 27 was built from a TB-specific population.

2. SPECIFIC INVESTIGATION: Two targeted lookups would materially narrow the range, and both are feasible with existing tooling:
   - Determine CG's source for 27. Check whether it matches GBD/WHO HALE at a specific age (roughly 35–45) in a named country life table.
   - Retrieve Romanowski 2019's SMR stratified by time since treatment completion, to test whether a lifelong constant k is justified.
Action feasibility: actionable_now
Advocate failures: ['unsupported_estimate_pseudo: If k is nearer 1.8, the reduction is roughly 5–12%." The verifier said k ≈ 1.8 "roughly halves" the mechanism\'s 20–30% reduction, which gives about 10–15%. The Advocate appears to have halved the hypothesis range of 10–25% instead. That range already spans the k uncertainty, so halving it double-counts. A rough check confirms the error. About 6.5 years of effective ageing, at the critique\'s own gradient (about 8 years of life expectancy lost over 12 years of age), gives roughly a 13% reduction. The follow-on claim that this "falls well below the materiality threshold" rests on that slip.', 'unsupported_estimate_pseudo: The "27 is already about 10–20% below total life expectancy" argument. It compares 27 to the critique\'s unsourced "low-to-mid 30s" figure at an assumed age of 40. It then infers that survivor morbidity or excess mortality "may already be embedded." There is a gap in the chain. A general-population HALE discount is not a TB-specific hazard multiplier. Mitigating factors: the Advocate openly flagged the arithmetic as their own and used hedged language.', 'unsupported_estimate_pseudo: the 1.77 RR figure is already lower than the pooled estimate, which suggests confounding or adjustment explains part of the gap." Two estimates differing does not identify confounding as the cause. Differences in setting, comparator or follow-up period could explain the gap just as well. The Advocate\'s own concession also undercuts the point. If confounders travel with the averted-death patient, the TB-attributable share is not the relevant quantity.', 'whataboutism: The "Offsetting Factors" section rests mainly on unmodelled lung-damage and morbidity benefits and possibly understated baseline mortality. Both bear on other parameters, not on whether 27 years per death is accurate. They matter for the bottom-line SROI, but they are unquantified and do not answer the critique of this parameter. The discounting point is muddled. It is placed under offsets while conceding it "cuts the other way.', 'sound_synthesis_noted: Several pieces of arithmetic are correct and do real work:']
Challenger failures: ['false_definitiveness: The heading claims the Gompertz-shortcut error points one way ("The evidence points one way"). The body then concedes the evidence is "suggestive only" and that the age gradient of relative risk is "an uninformed prior." The heading asserts a direction that the body admits is not grounded.', 'call_to_ignorance: If relative risk is higher at younger ages, a constant multiplier understates the loss…" This is offered as a directional argument right after admitting the opposite pattern (relative risks falling with age) cannot be grounded. The point fills an evidence gap with a convenient conditional.', 'strawmanning: no evidence supports a k near 1." The Advocate never proposed k near 1. They argued that the 1.8–2.9 range is wide and that the choice of k drives the magnitude.', 'strawmanning: The Challenger said the Advocate\'s use of the lifetime-burden study "cannot be inert as evidence and live as an offset." The Advocate called it neutral on years per death averted and relevant to the morbidity channel. Those are different questions, not a contradiction.', 'sound_synthesis_noted: Several corrections and calculations are sound:', 'sound_synthesis_noted: The point that a HALE discount and a TB-specific hazard multiplier are distinct mechanisms that stack correctly rebuts the Advocate\'s "already embedded" argument. The point that an UNVERIFIABLE provenance is symmetric, and therefore not "existing coverage," correctly handles evidence status.']
Debate resolved: The following points were established:
- **Direction:** the critique's direction is valid. CG has no survivor excess-mortality adjustment, and a general-population HALE framing does not absorb a TB-specific hazard multiplier.
- **Magnitude range:** the reduction plausibly lies around 10–25%. The k ≈ 1.8 floor yields about 10–15%, not the Advocate's 5–12%. The mechanism text's 19–22 overstates the critique's own range.
- **Decision impact:** this critique alone does not push SROI below 2,000x, even at its low end.
Debate unresolved: Three questions remain open:
- The provenance of 27: the age at death, which life table was used, and whether it is general-population HALE.
- Whether the averted on-treatment deaths should carry a lifelong constant k. They may be a sicker subset with higher k, or excess mortality may decay with time since treatment, which would mean lower effective k.
- Whether the Quantifier's central value should be about 24 or about 22. That choice determines how much stacking from other critiques is needed to reach the 17.7 break-even.

--- Critique: The 6% is a mix of deaths, and only a fraction is reachable and modifiable by atorvastatin ---

### Advocate
```
DEFENSE OF GIVEWELL'S (CG's) POSITION: The 6% is a mix of deaths, and only a fraction is reachable and modifiable by atorvastatin
```

**EXISTING COVERAGE:**

1. **The 10% relative reduction is a population-average assumption.**
   - CG applies it to mortality among all treated drug-susceptible patients. It does not apply it to "deaths a statin could plausibly prevent."
   - The relevant question is whether 10% of all on-treatment deaths is a reasonable average effect. That is not the same as asking what share of deaths is addressable.
   - If 10% was chosen as a modest, conservative average effect, the addressable-share haircut is partly embedded in it. The critique itself concedes this double-counting risk.
   - The BOTEC gives no derivation for the 10% (the parameter map says so). I can't prove it was set with early deaths in mind, so this is a conditional argument.
   - Conditional on the 10% being a population-average effect from a trial-like population, stacking a further 6% × 0.7 × 0.85 haircut would count the same exclusion twice.

2. **Eligibility is partly handled by the 60% uptake.**
   - The BOTEC applies 60% uptake among adult patients "if it works." That implicitly allows for roughly 40% of patients not receiving the drug. Contraindication, clinician reluctance and monitoring concerns are plausible components of that gap.
   - The critique's formula multiplies in a separate "share of the population eligible for statin." It also never uses that factor in its worked example.
   - Applying eligibility a second time would double-count to the extent the 40% non-uptake already reflects ineligibility.

3. **The rifampicin interaction is plausibly reflected in the trial effect and addressed by the Phase IIc design.**
   - The Phase IIa/b signal came from atorvastatin added to anti-TB treatment. I infer that standard regimens include rifampicin, so the observed effect reflects reduced exposure.
   - The grant explicitly funds a Phase IIc testing "dosing strategies." That is the natural place to address a drug-interaction exposure problem.
   - This is an inference from the BOTEC text, not a verified fact about the trial.

4. **The 40% success probability already discounts the case where the mortality benefit doesn't materialize.** That includes the case where early or sick deaths are unreachable and the trial shows no effect on survival.

**EVIDENCE WEAKNESSES:**

1. **The timing evidence supports only the premise.**
   - Zambia, Kenya, Ethiopia, Turkey, Cameroon and India cohorts show deaths are front-loaded. That is not what matters for the model.
   - The critique's own hypothesis says the evidence it needs is statin time-to-effect, the TB-attributable share of deaths, and whether the effect size already reflects an enrolled trial population. All three are marked UNGROUNDED or not verified.
   - Front-loading alone does not tell us how much of the 10% relative effect is lost.

2. **The cohorts are skewed toward high-HIV, high-mortality settings.**
   - The cited cohorts are mostly African settings, where HIV-associated early deaths are prominent.
   - CG's 6% is applied to a global pool of drug-susceptible patients. If the pool includes lower-mortality settings, the early-death concentration among sick HIV-positive patients may not carry over proportionally.
   - I have no figure for the global timing distribution, so this is a caution about generalizability, not a counter-estimate.

3. **Early deaths may be partly reversible.**
   - The critique concedes that deaths within 14 days of starting anti-TB treatment suggest some mortality is reversible with earlier therapy.
   - This cuts against treating all very early deaths as unreachable.
   - I cannot say whether statins' host-directed mechanism acts fast enough. The critique cannot say it doesn't. Time-to-effect is unknown in both directions.

4. **The 30% and 15% shares are placeholders the critic says are unverified.** The "effective baseline" of 3.6% therefore has no empirical anchor.

**MAGNITUDE CHALLENGE:**

1. **The Quantifier's central estimate is not derived.**
   - The 4.5% central value is a 25% haircut, but the critique offers no grounded component for it. It is derived only from the placeholder shares.
   - At this central value, SROI is about 2,291x. That is still above the ~2,000x bar and is exactly at, not beyond, the ~25% change threshold.

2. **Crossing the bar requires a haircut of more than about 35%.**
   - The break-even baseline is 2,000 / 3,055 × 6% ≈ 3.93%. This matches the 3.9% threshold cited in the critique and implies a haircut of about 34.5%.
   - Only the low case (3%, a 50% haircut) crosses the bar. That case has no grounding either.
   - The critique's illustrative 3.6% (≈1,833x) crosses, but it depends entirely on the two ungrounded shares of 30% and 15%.

3. **The 15% non-TB share and the 30% unreachable share need not both apply to the effect.**
   - Non-TB deaths may still be affected if a 10% relative reduction is an all-cause effect measured in a trial.
   - Applying both haircuts presumes the effect works only on TB-attributable, late, eligible deaths. That is a stronger structural assumption than the CG formula makes.

**OFFSETTING FACTORS:**

1. **Unascertained deaths could raise the baseline.** The parameter map notes that CG makes no distinction between notified-cohort mortality and true mortality. Deaths in patients lost to follow-up would push the effective baseline up.

2. **Only on-treatment mortality is valued.**
   - The BOTEC states "only mortality is valued."
   - The following are all set implicitly to zero:
     - reduced lung damage, which is the Phase IIa/b finding;
     - post-treatment mortality and morbidity DALYs;
     - transmission-averted cases;
     - the sweat-diagnostic value.
   - If the benefit is partly in morbidity and long-term survival, the on-treatment death haircut matters less. The parameter map flags this offset.

3. **There is no time discounting in the BOTEC.** This works in the estimate's favour for benefits that arrive years later. It is also a bias in the other direction, so I don't lean on it here.

**OVERALL ASSESSMENT:** **Partial defense.**

- The critique is directionally plausible, and the front-loading premise is well supported.
- The size of the haircut is unsupported, and the critique itself flags this.
- A central haircut of 25% leaves SROI above the bar.
- The strongest part of the defense is the double-counting argument. The 10% relative effect is a population-average assumption, and eligibility is already partly in the 60% uptake.
- That argument is conditional. It holds only if the 10% was set as an average effect and not as an effect on a pre-selected subgroup, and the BOTEC doesn't say which.

**CONCESSIONS:**

1. CG gives no decomposition of the 6% and no derivation of the 10%. It is a real gap that deaths concentrated in the first weeks, or in the sickest patients, may be less modifiable by a host-directed adjunct.

2. The 60% uptake is a uniform average. If the patients who die are less likely than average to receive a statin (sicker, older, on interacting drugs), the effective uptake among decedents is below 60%. The uptake does not fully absorb the eligibility concern.

3. Rifampicin's effect on exposure is not discussed anywhere in the BOTEC. My argument that the trial and dosing work absorb it is inference, not documentation.

4. If the true haircut exceeds about 35%, SROI falls below the bar. The critique has not shown it does, but I cannot rule it out.

### Challenger
REBUTTAL: The 6% is a mix of deaths, and only a fraction is reachable and modifiable by atorvastatin

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the 10% relative reduction is a population-average assumption, so an addressable-share haircut would double-count exclusions already embedded in it.
>
> Response:
- The Advocate's own offsetting argument undercuts this. They say the Phase IIa/b finding was reduced lung damage and that the BOTEC values only mortality.
- If the observed signal was lung damage, the 10% mortality effect was not measured in an enrolled mortality-endpoint population. Phase IIc is the grant still being funded.
- The verifier's double-counting caveat is explicitly conditional on "if the model's statin effect size comes from a trial population." The Advocate has supplied the reason to doubt that condition.
- If the 10% is an extrapolation from a non-mortality signal, nothing in it has filtered out early or ineligible deaths. The haircut is then not double-counting.
- The Advocate concedes the BOTEC gives no derivation for the 10%. "It might embed the exclusion" is therefore not evidence that it does.

> The Advocate claims: the 40% success probability already discounts the case where early or sick deaths are unreachable and no survival effect appears.
>
> Response:
- A probability of success scales the whole benefit. It does not reduce the magnitude conditional on success.
- Take a trial that succeeds but whose effect applies only to the 25–45% of deaths occurring after the early window. That is the complement of the 55–75% figure in the verifier's evidence. A 10% reduction in all deaths is then not the right conditional effect.
- The 40% handles "no effect at all." It does not handle "real effect on a subset of deaths." These are different failure modes.

> The Advocate claims: eligibility is partly handled by the 60% uptake.
>
> Response:
- The Advocate concedes that uptake is a uniform average and that decedents plausibly have lower effective uptake. That concession is most of the rebuttal.
- Uptake addresses only one of the critique's three factors, eligibility. It does nothing for time-to-effect or for the TB-attributable share.
- The critique's own worked example omits the eligibility factor. The 3.6% figure (0.7 × 0.85) therefore does not double-count uptake.

> The Advocate claims: the rifampicin interaction is plausibly in the trial effect and addressed by Phase IIc dosing work.
>
> Response:
- The Advocate labels this inference and concedes the BOTEC never mentions rifampicin.
- Even granting that dosing work might fix exposure, that is a future outcome. The BOTEC applies 10% as if it were already achieved.
- If higher dosing is needed, that is a possible cost or safety change the BOTEC does not model. I cannot ground this; I flag it only as an unmodelled dependency.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the timing evidence supports only the premise, not the size of the haircut.
>
> Response:
- Conceded. The verifier rated the front-loading premise as strongly supported and nothing more. Time-to-effect and the TB-attributable share are ungrounded.
- But the BOTEC applies 6% × 10% flat, which is an implicit time-to-effect of zero. Uncertainty about time-to-effect does not justify that default.
- The Advocate says time-to-effect is "unknown in both directions." That is true, but the BOTEC's treatment is the extreme end of the possible range.

> The Advocate claims: the cohorts are skewed toward high-HIV African settings, so they may not generalize to CG's global pool.
>
> Response:
- The cohorts also span Turkey and India (verifier evidence), which are not high-HIV settings. The premise is not confined to one epidemiology.
- I cannot ground the share of CG's 6% that comes from high-burden, high-HIV settings. The Advocate concedes they have no counter-figure either. Treat this as an open question, not a reason to discount the timing evidence.

> The Advocate claims: early deaths may be partly reversible, which cuts against treating them as unreachable.
>
> Response:
- The reversibility evidence concerns earlier anti-TB therapy, not statins. Deaths within 14 days of treatment start suggest late presentation. They do not show that an adjunct could have averted them.
- My inference, not verified: a host-directed adjunct plausibly acts more slowly than the antimicrobial regimen, and patients who die that early are the ones with the least time. The Advocate concedes the statin's speed is unknown.
- "Partly reversible" supports a smaller haircut than 100% of early deaths. It does not support a haircut of zero.

> The Advocate claims: the 30% and 15% shares are unverified placeholders.
>
> Response:
- Agreed. The critique says so. The rebuttal below does not rely on them.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: the central 25% haircut leaves SROI at about 2,291x, still above the ~2,000x bar, and crossing needs more than a ~35% haircut.
>
> Response:
- Conceded. The break-even is 2,000 / 3,055 × 6% ≈ 3.93%, a haircut of about 34.5%. The central estimate does not cross.
- The critique's illustrative haircut is larger than the central one: 1 − 0.7 × 0.85 = 40.5%. It lands near 1,818x. The central 25% was not derived from it.
- Timing alone could reach the threshold. This is my derivation from the verifier's 55–75% of deaths within 1–2 months, and it assumes a time-to-effect that makes only half of those early deaths unreachable.
  - That half-reach figure is illustrative, not grounded.
  - 0.5 × 55% = 27.5% and 0.5 × 75% = 37.5%.
  - That range straddles the 34.5% threshold.
- Adding any non-TB, rifampicin-related or eligibility loss on top would push the total past the threshold. A final haircut of 30–40% is therefore not exotic. It is roughly what falls out if early deaths are only half reachable.
- I do not claim the bar is crossed. The claim is that the break-even sits inside the range the timing evidence allows.

> The Advocate claims: the 10% might be an all-cause effect, so non-TB deaths need not be excluded.
>
> Response:
- Partly conceded: the 15% non-TB haircut is the weakest of the critique's components.
- But the only mechanism evidence in the record, per the Advocate, is reduced lung damage, which is TB-specific. An all-cause effect has no support in the record.
- Dropping the non-TB haircut leaves 0.7, a 30% haircut. That is still just under the threshold, and it uses an ungrounded 30% for early or ineligible deaths.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: unascertained deaths could raise the effective baseline.
>
> Response:
- The direction is real, but it is unquantified and not in the model.
- Deaths among patients lost to follow-up are plausibly people who stopped treatment. My inference is that they are not receiving the statin and so are not addressable. That would blunt this offset.

> The Advocate claims: lung damage, post-treatment mortality, transmission and sweat diagnostics are valued at zero, so the mortality haircut matters less.
>
> Response:
- These are separate benefit streams set to zero in the model. They are not offsets inside the baseline_mortality parameter.
- Whether they exist is a separate question. This critique asks whether the parameter as used overstates the mortality benefit, which is unaffected.
- The Advocate flagged the no-discounting point and declined to lean on it. I agree it is not an offset.

**KEY UNRESOLVED QUESTIONS:**
- Was the 10% derived from, or anchored to, a mortality-endpoint trial population? Without this the double-counting defense is a coin flip, and the lung-damage finding points toward "no."
- What is statin time-to-effect on mortality? The break-even haircut of 34.5% corresponds to roughly half of early deaths being unreachable.
- Does the Phase IIc dosing strategy restore rifampicin-reduced exposure, and at what cost per patient?
- What share of CG's 6% comes from high-burden, high-HIV settings, where early deaths concentrate?
- Is the effect specific to TB-attributable deaths or all-cause? The record supports only TB-specific lung mechanisms.

### Judge Audit
Surviving strength: moderate
Justification: The Challenger made grounded arguments the Advocate could not fully defend:
- the probability-versus-magnitude distinction;
- the use of the lung-damage signal to undercut the double-counting condition;
- the point that uptake addresses only eligibility, not timing.
The Advocate's own concessions (decedents' lower effective uptake, the rifampicin interaction not in the BOTEC) also stand. However, the key quantitative claim, that the haircut crosses the bar, rests on an ungrounded half-reach factor delivered with some false definitiveness. The Advocate also correctly showed that the critique's own central estimate leaves SROI above the bar. The directional critique survives, but its decision relevance remains open.
Recommended action: 2. SPECIFIC INVESTIGATION: Two targeted checks would move the answer. Both are feasible with existing tooling.

(a) **Trace the provenance of CG's 10% relative mortality reduction.**
- Check the BOTEC source notes and the Phase IIa/b atorvastatin-TB trial publications.
- Determine whether the figure derives from an intention-to-treat mortality endpoint, a surrogate (lung damage or inflammation), or a judgment call.
- If it derives from ITT mortality, the double-counting defense largely holds and the critique should be downgraded.
- If it derives from a surrogate or judgment, the haircut applies.

(b) **Re-run the verifier on two inputs that let the haircut be computed rather than guessed:**
- cumulative death proportions at days 7, 14 and 28 from the Zambia cohort (n = 1,063);
- any published data on the onset of statin pleiotropic or anti-inflammatory effects (e.g., CRP reduction timing, which is typically on the order of 1–2 weeks).

Combining these gives an unreachable share under explicit onset assumptions.

**Interim conclusion:** Treat this as a credible downward adjustment of unknown size. Add a sensitivity flag noting that SROI falls below the ~2,000x bar if more than about 35% of on-treatment deaths are unaddressable.
Action feasibility: requires_specified_evidence
Advocate failures: ['sound_synthesis_noted: The break-even baseline is 2,000 / 3,055 × 6% ≈ 3.93%… implies a haircut of about 34.5%." Each step comes from model values and matches the 3.9% threshold in the critique. This is legitimate analysis, and the Challenger accepted it. It does assume SROI scales linearly with baseline mortality, which is reasonable for a multiplicative BOTEC.', 'misrepresenting_evidence_status: The critique concedes that deaths within 14 days… suggest some mortality is reversible." That point came from the verifier\'s evidence package, not the critique. The verifier also notes the Investigator did *not* raise the double-counting caveat, yet the Advocate attributes the double-counting concession to the critique.', 'strawmanning: Existing Coverage point 4 says "The 40% success probability already discounts the case where… early or sick deaths are unreachable." This recasts a critique about *conditional magnitude* (the size of the effect given success) as a critique about *probability of any effect*.']
Challenger failures: ['unsupported_estimate_pseudo: 0.5 × 55% = 27.5% and 0.5 × 75% = 37.5%. That range straddles the 34.5% threshold." The 0.5 "half-reach" factor is labeled illustrative, which is to the Challenger\'s credit. The chain still has a structural gap, though.', 'false_definitiveness: A final haircut of 30–40% is therefore not exotic. It is roughly what falls out if early deaths are only half reachable." This turns an admittedly ungrounded illustration into a confident characterization of the plausible range.', 'strawmanning: The BOTEC applies 6% × 10% flat, which is an implicit time-to-effect of zero." The Advocate\'s position was that the 10% is a *population-average* effect across all deaths. A population average already blends zero effect on early deaths with larger effects on later ones, so it does not imply zero time-to-effect.', 'sound_synthesis_noted: If the observed signal was lung damage, the 10% mortality effect was not measured in an enrolled mortality-endpoint population." This uses the Advocate\'s own offsetting argument to undercut the condition behind the double-counting defense. It is a well-grounded logical move.']
Debate resolved: The debate established four points:
- The front-loading premise is solid.
- The break-even haircut is about 34.5%, so the 25% central estimate does not cross the bar.
- The 40% success probability cannot absorb a conditional-magnitude haircut.
- The 15% non-TB component is the weakest part of the critique.

It also substantially weakened the double-counting defense. If the 10% is extrapolated from a lung-damage signal rather than a mortality endpoint, nothing in it filters out early deaths.
Debate unresolved: Whether the true addressable-share haircut exceeds about 34.5% remains contested. That turns on two things neither side could ground:
- statin time-to-effect relative to the death-timing distribution;
- whether the 10% is anchored to an intention-to-treat mortality population.

The Challenger's "half-reach" calculation shows the threshold is reachable under some assumptions, but not that those assumptions are likely.

--- Critique: Under-ascertained deaths push true mortality up, and the direction is the opposite of Critiques 1–2 ---

### Advocate
**DEFENSE OF GIVEWELL'S POSITION: Under-ascertained deaths push true mortality up**

**EXISTING COVERAGE:**
- CG's 6% is described as "mortality among treated drug-susceptible patients." CG does not say it is the WHO "died" outcome category. The critique's premise (the 6% is only the "died" share of evaluated outcomes) is an inference, not something the report states. If CG's 6% already reflects cohort-level all-cause mortality, the concern is partly or fully moot. I cannot verify which definition CG used.
- The BOTEC's benefit is the 10% relative reduction applied to on-treatment mortality. The critique's added deaths are mostly post-LTFU or pre-treatment deaths, which the statin cannot plausibly reach. The structure of the BOTEC (adjunct therapy during treatment) already excludes them from the benefit base, whatever the true all-cause mortality is.
- The parameter map lists related unmodeled factors that push the other way: deaths in the first 2–4 weeks, HIV and other comorbidity deaths, and survivors' excess mortality reducing DALYs per death. These are not modeled, but the 6% figure plus a flat 27 DALYs is a rough central estimate. Adjustments in both directions are unmodeled, and the net is unknown.

**EVIDENCE WEAKNESSES:**
- The key mechanism claims are ungrounded, as the critique admits. These are the WHO category shares and the 10–20% death rate for the not-evaluated group.
- The cited Kenyan tracing figure (~10% found dead) and the 2–7× SMRs apply to LTFU patients. The critique itself concedes that "not evaluated" includes transfers and missing records, and that most of these patients are probably alive. The 10–20% range therefore likely overstates deaths for the larger group.
- The 8.6% South African adult figure is a high-burden setting, probably with heavy HIV co-infection (my inference, not a cited fact). It shows that 6% is an average. It does not show that the global mean is above 6%, because low-mortality settings pull the average down. The critique shows variance, not bias.
- The critique offers no source that the global treated-cohort mean is miscalibrated upward.

**MAGNITUDE CHALLENGE:**
- The critique's own sensitivity run does not support "material." The high case, 6.8% mortality, gives +13.3% SROI (about 3,462x). The Quantifier's central value of 6.25% gives +4.2% (about 3,182x). Neither crosses the 25% threshold or moves SROI near the 2,000x bar.
- The 10–23% uplift in the narrative corresponds to 6.6–7.4% mortality. The sensitivity high case only tested 6.8%. Even the top of the narrative range (+23%) falls below the ~25% materiality line.
- That uplift assumes full proportional pass-through to SROI. The critique concedes that the statin may not affect these deaths because treatment was interrupted. If the pass-through is 0–50% of the added deaths, the effective uplift is roughly 0–11%. This follows from halving the 10–23% range. The 50% figure is an illustrative bound, not an empirical estimate.
- On the critique's own account, the true central effect is below the Quantifier's stated range, and it sits within the noise of a BOTEC that rounds to "about 3,000x."

**OFFSETTING FACTORS:**
- The critique concedes that it pulls opposite to Critique 1, so its net direction is undetermined.
- If LTFU decedents are disproportionately HIV-positive or comorbid (a conditional hypothesis, not verified), their remaining life expectancy is below 27 DALYs per death. That would reduce the DALY value of any extra deaths averted.
- Uptake of 60% is applied to all adult patients. Patients at high risk of LTFU likely have worse access to and adherence to an adjunctive pill. This is a conditional argument, not a cited finding.

**OVERALL ASSESSMENT:** Strong defense.
- The direction of the critique is plausible and I cannot rebut it. Its quantitative pass-through to SROI is weak, because the added deaths are mostly unaddressable by an on-treatment adjunct and the key rates are ungrounded.
- Its own sensitivity analysis shows the effect below the 25% materiality threshold and nowhere near the 2,000x bar.

**CONCESSIONS:**
- WHO treatment-outcome categories do under-ascertain some deaths. Settings with mortality above 6% exist, so 6% is not a floor.
- CG gives no derivation or definition for the 6%, so the critique cannot be fully dismissed. A small upward drift in baseline mortality is plausible.
- The "material" label is not supported by the critique's own sensitivity numbers, but the direction of the correction (up, not down) is a fair point.

### Challenger
REBUTTAL: Under-ascertained deaths push true mortality up

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: CG describes its 6% only as "mortality among treated drug-susceptible patients," so it may already be cohort-level all-cause mortality. If so, the critique is partly or fully moot.

- The Advocate says it "cannot verify" which definition CG used. That is an open question, not a defense.
- If 6% is all-cause cohort mortality, the critique falls. If 6% is the WHO "died" share, the critique holds. Neither side can tell which.
- CG gives no derivation. A baseline parameter that drives SROI proportionally and has no stated definition is a transparency gap. The critique does not have to show the gap is a bias.

> The Advocate claims: The BOTEC applies a 10% relative reduction to on-treatment mortality, so post-LTFU and pre-treatment deaths are already outside the benefit base.

- This is the Advocate's strongest point, and I concede it for deaths after treatment ends. Those deaths are unreachable by an on-treatment adjunct.
- It does not cover all the added deaths. WHO defines LTFU as treatment interrupted for 2 or more consecutive months. Some LTFU decedents therefore die in the early treatment window, before interruption is declared. Early treatment is when TB mortality concentrates. The Advocate's own parameter map lists "deaths in first 2–4 weeks" as an unmodeled factor.
- So pass-through is not zero. The Advocate's 0–50% range is, by its own admission, "an illustrative bound, not an empirical estimate." It is a haircut with no source, applied against a number that is also unsourced.

> The Advocate claims: The parameter map's unmodeled factors (early deaths, HIV and comorbidity, survivor excess mortality) push the other way, so the net is unknown.

- "Net unknown" is not "net zero." The Advocate names no sign or magnitude for the offsets.
- Early deaths push mortality up, the same direction as this critique, so that item is not an offset.
- Survivors' excess mortality lowers DALYs per death. It acts on a different parameter than baseline mortality, so it cannot cancel an error in this one.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: The 10–20% death rate for "not evaluated" is unsupported, and the Kenyan 10% and the 2–7× SMRs apply to LTFU only.

- I concede this fully. The verifier evidence package says the same thing: the 10–20% range "fits LTFU better than the not-evaluated group."
- I am narrowing the claim to the part with some grounding. The Kenyan tracing study found about 10% of LTFU patients dead. The SMRs are 2–7× higher than after cure.
- The sensitivity run's central value already reflects this narrowing. Assume SROI is proportional to mortality, as the critique does. Then 6.25% against 6% gives 6.25/6 − 1 = +4.2%, which matches the Quantifier's output.
- A derivation for that central value: an LTFU share *s* of the cohort times 10% dead adds 0.10·*s*. At a hypothetical *s* = 2.5%, that is +0.25 pp, giving 6.25%. I cannot ground *s*. It is an illustrative input chosen to reproduce the central value, not an independent estimate.

> The Advocate claims: The 8.6% South African figure shows variance, not bias, because low-mortality settings pull the global mean down.

- This is logically correct. One high-mortality setting does not show the mean is above 6%.
- I do not rely on the 8.6% figure to show bias. I use it only to show that 6% is not a floor, and the Advocate concedes that.
- Whether the case-weighted mean in CG's target geographies is above or below 6% depends on the HIV and setting mix. The Advocate's inference that the South African figure reflects heavy HIV co-infection is flagged as the Advocate's own. I cannot ground the weighting either, so this stays unresolved.

> The Advocate claims: The critique offers no source that the global mean is miscalibrated.

- The critique's mechanism is definitional under-ascertainment. It does not claim miscalibration of a measured mean.
- Proving a miscalibration would require knowing CG's source definition. That is the same unverifiable question as above.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: The sensitivity run shows +13.3% (high) and +4.2% (central), neither near the 25% threshold or the 2,000x bar, so "material" is unsupported.

- I concede this. In the sensitivity output, `crosses_bar_high` and `crosses_bar_central` are both false. The 3,462x high case and 3,182x central case are far from 2,000x.
- The narrative's 10–23% range is not what was tested. The high case of 6.8% is +13.3%, not +23%. But even +23% is under 25%. The "material" label overstates the result.
- The minimum defensible effect is the central +4% less any pass-through haircut. That is a small upward adjustment with no decision relevance on its own.
- The residual value of the critique is directional. If 6% is the "died" category, the BOTEC is biased conservatively on this parameter. That matters only when combined with other critiques of the model.

> The Advocate claims: The effect is within the noise of a BOTEC that rounds to "about 3,000x."

- At +4%, yes. At the high case, +13% is still within the rounding of "about 3,000x" but is not trivially small.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: LTFU decedents may be disproportionately HIV-positive, so DALYs per death are below 27. High-LTFU-risk patients also likely have lower uptake and adherence.

- The Advocate labels both conditional and unverified, and I agree.
- The uptake argument double-counts. The pass-through haircut already reduces the benefit for patients who interrupt treatment. Applying a lower-uptake offset to the same patients penalizes them twice.
- The HIV argument can be turned around. If high-mortality, HIV-heavy settings are where TB deaths concentrate, then the share of deaths in those settings is higher than their share of patients. A case-weighted baseline would then be above the global average, which supports the critique's direction.
- That turnaround is also a conditional, not a finding.
- The one real offset is Critique 1, which the critique itself concedes. Its net with this critique is undetermined, and I cannot resolve it.

**KEY UNRESOLVED QUESTIONS:**
- Does CG's 6% come from the WHO "died" category, from an all-cause cohort estimate, or from a mix of studies? The answer decides whether this critique applies at all.
- What fraction of LTFU deaths occur before the 2-month interruption threshold, during a period when the statin would be active? That fraction sets the pass-through. Neither side has a sourced figure.
- What are the LTFU share and the case-weighted baseline mortality in CG's target geographies? Without them, the central +4% cannot be confirmed or refuted.
- How does this critique net against Critique 1 in the combined model? That is a question for the Judge.

### Judge Audit
Surviving strength: weak
Justification: The Challenger conceded the critique's quantitative claim. It accepted the sensitivity flags showing no bar crossing and dropped the not-evaluated death rate. Its main remaining argument for nonzero pass-through, deaths during the pre-declaration window, does not establish that those patients were still taking the statin. It also misread the Advocate's early-deaths point as a mortality-level claim. What survives is a directional transparency point (CG's 6% is undefined), which by the Challenger's own account has "no decision relevance on its own." The critique is weak because it was substantively narrowed in a mostly productive exchange, not because the debate failed to test it.
Recommended action: 1. CONCLUDE NOW: With moderately high confidence, the critique raises a valid direction but makes no material quantitative claim.
   - If CG's 6% is the WHO "died" share, baseline mortality is likely slightly understated.
   - Most of the under-ascertained deaths (post-LTFU and pre-treatment) are structurally unreachable by an on-treatment adjunct.
   - The effective SROI uplift is therefore likely at or below the +4% central case, well within the noise of "about 3,000x."
   - Treat this critique as a small conservative-bias note to be netted against Critique 1, not as an adjustment.
   - One cheap, feasible check could zero out the critique entirely: confirm from CG's source documentation how the 6% was defined. If it is all-cause cohort mortality, the critique is moot.
Action feasibility: actionable_now
Advocate failures: ['unsupported_estimate_fabricated: If the pass-through is 0–50% of the added deaths, the effective uplift is roughly 0–11%." The 50% upper bound has no source. The Advocate does label it "an illustrative bound, not an empirical estimate," which mitigates the failure but does not ground the number. The halving arithmetic itself is correct.', 'false_definitiveness: The self-assessment says "Strong defense." Yet the Advocate concedes the direction is plausible and that it "cannot rebut it." It also concedes "a small upward drift in baseline mortality is plausible" and that CG\'s 6% definition cannot be verified. The magnitude rebuttal is strong; the overall defense is better described as partial-to-strong. The confident label overstates what was shown on the existence of the bias.', "sound_synthesis_noted: The magnitude challenge correctly reads the sensitivity output. 6.8/6 gives +13.3%, 6.25/6 gives +4.2%, and neither crosses the materiality threshold or the 2,000x bar. The Advocate also notes that even the narrative's +23% top falls under 25%. These steps are grounded and drive the outcome of the debate."]
Challenger failures: ['strawmanning: Early deaths push mortality up, the same direction as this critique, so that item is not an offset." The Advocate listed the "deaths in first 2–4 weeks" factor as something that pushes against the *benefit*. Deaths too early for an adjunct to act on are deaths it cannot avert. The Challenger recast this as a claim about the *baseline mortality level*. That is a category swap from benefit base to mortality level.', 'call_to_ignorance: Some LTFU decedents therefore die in the early treatment window, before interruption is declared... So pass-through is not zero." It is true that the 2-month declaration lag exists. But a patient who dies during that lag has already stopped taking pills, and so has stopped the statin. The Challenger offers no evidence that any LTFU decedent dies while still on the adjunct. It fills that gap with an inference that does not follow, and it reuses the Advocate\'s early-deaths item, which concerns on-treatment deaths, to support the point.', 'unsupported_estimate_pseudo: At a hypothetical s = 2.5%... It is an illustrative input chosen to reproduce the central value." This derivation is circular: s is reverse-engineered from the output. The Challenger openly says so, which mitigates the failure.', 'sound_synthesis_noted: Several moves are clean:']
Debate resolved: Both sides agree the critique's "material" framing does not survive. On the critique's own sensitivity run, the central uplift is about +4% and the high case about +13%, neither near the 25% threshold or the 2,000x bar. Both sides also agree that the 10–20% death rate for "not evaluated" patients is unsupported, and that post-treatment and pre-treatment deaths are outside the statin's reach.
Debate unresolved: Two questions remain open:
- Whether CG's 6% is the WHO "died" category or a cohort-level all-cause estimate. This decides whether the critique applies at all.
- Whether any meaningful fraction of the extra deaths occurs while patients are still taking the adjunct. The Challenger's "nonzero pass-through" claim rests on reasoning that conflates the LTFU declaration lag with on-treatment time.

--- Critique: Covariance between mortality and DALYs per death means the product of means is not the mean of the product ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: Covariance between mortality and DALYs per death

EXISTING COVERAGE:
- The BOTEC multiplies deaths averted by "27 DALYs per TB death (remaining healthy life expectancy)." The stated unit is per death, not per case or per patient.
  - The critique only bites if 27 is a case-weighted or population-average figure.
  - The critique itself says to check whether 27 is already a death-weighted figure (GBD YLL ÷ deaths) and to drop the critique if so.
- I cannot verify how CG derived 27. The text gives no source or derivation, and I cannot ground a claim either way.
- The wording is at least consistent with a death-weighted figure. Conditional on that, the covariance problem is already handled by construction.
- The model applies a constant 10% relative reduction to a 6% baseline.
  - Deaths averted are then proportional to deaths in every subgroup (Δm_g = 0.1·m_g).
  - The correct weight for d is therefore the death distribution, which is what a per-death figure is.
- The critique's own evidence list concedes that the right weight is deaths averted, not deaths. That only departs from the death-weighted figure if the statin effect is heterogeneous across subgroups, and nothing in the critique grounds such heterogeneity.
- I concede that the parameter map lists "no age or comorbidity weighting" as an unaddressed item. That is an absence of documentation, not evidence of bias.

EVIDENCE WEAKNESSES:
- The only quantitative support is the author's own illustrative arithmetic with assumed numbers. No GBD age-stratified YLL data or TB case-fatality-by-age data is cited.
- The illustration contains an internal inconsistency.
  - Its patient-weighted mean DALYs per death is 0.7×35 + 0.3×15 = 29, not 27.
  - The "12% lower" result compares 1.52 against 6.4%×27 = 1.73, a benchmark that is not the case-weighted mean of its own groups.
  - Against the true patient-weighted figure (6.4%×29 = 1.86), the gap would be about 18%.
  - The illustration therefore does not cleanly isolate the covariance effect. Its magnitude is set by the assumed 35-vs-15 DALY gradient and 3× mortality gradient, neither of which is sourced.
- The critique labels its own −10 to −15% magnitude "UNGROUNDED" and concedes the sign is uncertain. A hypothesis with unknown sign and unsourced magnitude has not met a burden of proof.
- The direction argument runs both ways.
  - Older decedents push d down.
  - HIV-associated deaths in younger adults push d up.
  - Treated TB is a global mix of both. I cannot ground the weights, and the critique does not supply them.

MAGNITUDE CHALLENGE:
- The Quantifier's sensitivity output has a central case of 27 with 0.0% change. Even the quantifier does not assign a directional adjustment. The −11.1% to +7.4% range is a symmetric-ish uncertainty band, not an expected shift.
- Baseline SROI is 3,055x.
  - The low case (24 DALYs per death, 2,715x) is −11.1%.
  - The high case (29 DALYs per death, 3,281x) is +7.4%.
  - Neither case crosses the ~2,000x bar, and both are well inside the ±25% decision-relevance threshold in the run's materiality definition.
- The critique's "material" label is not supported by its own sensitivity table under the stated criterion. The worst case is about half the 25% threshold.
- The low value of 24 corresponds to the illustration's death-weighted 23.8. That is a downside scenario built on assumed gradients, not a central estimate.

OFFSETTING FACTORS:
- The stated direction is "lean decreases in low-HIV settings only." The critique concedes that high-HIV settings, where TB burden is concentrated, could reverse the sign.
- Several benefit channels are set to zero in the BOTEC: morbidity/lung damage, post-treatment mortality, transmission, and the diagnostic. The parameter map lists these as implicit zeros.
  - They bias the estimate downward, in the opposite direction.
  - A modest negative covariance effect of ≤11% would sit within the range of that omitted upside.
  - I cannot size those channels here.

OVERALL ASSESSMENT:
Strong defense, with one open dependency. The structural point is correct, but it only applies if 27 is not a death-weighted figure. That is unverified, and the BOTEC's per-death wording points the other way. Even if it applies, the critique has no grounded central estimate and uncertain sign. Its sensitivity range (−11% to +7%) neither crosses the bar nor reaches the 25% threshold. Under the run's own materiality definition, this is not decision-relevant.

CONCESSIONS:
- E[m·d] ≠ E[m]·E[d] under covariance is mathematically correct.
- If 27 was computed as remaining healthy life expectancy at the mean age of TB cases rather than of TB decedents, and decedents skew older, the estimate is biased modestly upward in low-HIV settings. The BOTEC does not document the derivation, so I cannot rule this out.
- The parameter map is right that CG provides no age or comorbidity weighting. A one-line note on how 27 was derived would resolve the question.
```

### Challenger
REBUTTAL: Covariance between mortality and DALYs per death

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: The BOTEC labels 27 as "DALYs per TB death," so the figure is plausibly already death-weighted. If so, the covariance problem is handled by construction.

Response:

1. A "per death" label states the unit, not the weighting. A figure can be expressed per death and still be computed at the wrong age distribution.
2. The BOTEC's own gloss is "remaining healthy life expectancy." That is a life-table construct, usually evaluated at a reference age. It is not obviously "GBD YLL ÷ GBD deaths."
3. The Advocate concedes, and I agree, that the derivation is undocumented. Whether 27 is evaluated at the age of TB decedents or at some other age is an open question.
4. The Advocate's reading is therefore a conditional ("if 27 is death-weighted"). It is not evidence that 27 is death-weighted. The critique's own first instruction is to check this and drop the critique if so. That check has not been done by anyone, so the critique is unresolved rather than refuted.

> The Advocate claims: With a constant 10% relative reduction, deaths averted are proportional to deaths in every subgroup. So a death-weighted d is the correct weight.

Response:

1. I concede this. Under a homogeneous relative effect, deaths-averted weights equal death weights. The verifier's note that "the right weight is deaths averted" therefore does not move the result unless the effect is heterogeneous.
2. This narrows the live question to one point: how was 27 derived? If 27 is a death-weighted YLL figure, the critique fails. If it is a remaining life expectancy at a mean case age, it survives in the direction the Advocate also conceded (biased upward if decedents skew older).
3. The constant-RR assumption comes from the BOTEC structure. It is a modeling simplification, not evidence that the statin effect is uniform across age or HIV status. I cannot ground heterogeneity either, and I do not claim it.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: The illustration is internally inconsistent. The patient-weighted DALYs are 29, not 27, so the "12%" figure is not a clean isolation of covariance.

Response:

1. The arithmetic is correct and I concede it.
2. The correction cuts toward the critique's mechanism, not against it. Under the illustration's own assumptions, the relevant comparison is death-weighted 23.8 against patient-weighted 29. That is about −18% (23.8/29 ≈ 0.82). The illustration therefore understated the gap.
3. That comparison only applies if the BOTEC's 27 is a patient-weighted figure. The "12%" number overstated the case for the illustration's own setup in one respect and understated it in another. Neither number should be treated as an estimate.
4. The 35-vs-15 and 3× gradients are unsourced. I cannot ground them, so the magnitude stays an uninformed prior.

> The Advocate claims: The critique labels its own magnitude "UNGROUNDED" and concedes the sign is uncertain, so it has not met its burden.

Response:

1. The structural claim (E[m·d] ≠ E[m]·E[d] under covariance) is verified as mathematically correct. The unverified part is the empirical covariance and the derivation of 27. Those are UNVERIFIABLE, not REJECTED.
2. The right reading is conditional: if 27 is not death-weighted and decedent age differs from case age, a bias exists. The critique's remaining value is as a documentation request, which the Advocate also endorsed ("a one-line note … would resolve the question").
3. The Advocate says the direction runs both ways. That is fair, and the critique said so. But two-sided uncertainty about the sign is not a reason to assume zero. It is a reason to resolve it with GBD data.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: The sensitivity range (−11.1% to +7.4%) does not cross the ~2,000x bar and sits well under the 25% materiality threshold. The "material" label is unsupported.

Response:

1. I concede that neither endpoint crosses the bar: 2,715x at the low end is still above ~2,000x. I also concede the worst case is about −11%, below the 25% threshold the Advocate cites. I cannot verify the run's materiality definition, so I take the Advocate's description of it as stated.
2. The minimum plausible impact is zero, if 27 is death-weighted. The sensitivity range is bounded by the Quantifier's chosen low and high values (24 and 29). It is not a derived range, so it could understate the true gap if the age gradient is steeper than the illustration assumes. I cannot ground a steeper gradient.
3. The central case showing 0.0% change reflects a design choice (no directional adjustment applied to an ungrounded critique). It is not evidence that the effect is zero.
4. On the Advocate's own numbers, this critique is low-impact for the decision. I do not dispute that.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: Omitted benefit channels (morbidity, post-treatment mortality, transmission, diagnostic) bias the estimate downward, so they offset a modest covariance penalty.

Response:

1. The Advocate says it "cannot size" these channels. An unsized offset cannot be shown to cancel an effect of any particular size.
2. These channels are set to zero in the model, so GiveWell's model does not capture them. They are hypothetical offsets, not modeled ones.
3. A bias in one parameter is not cancelled by an unrelated omission elsewhere. The two would offset only by coincidence. The net effect is uncertain in both directions, which is a reason to fix each.
4. The high-HIV reversal is a real offset to the sign. But it makes the sign depend on deployment mix, which neither side has grounded.

**KEY UNRESOLVED QUESTIONS:**

- How was 27 derived: GBD YLL ÷ deaths, remaining life expectancy at the mean age of cases, or something else? This single fact decides whether the critique applies.
- If 27 is a life expectancy at a reference age, what is the age distribution of TB decedents in the deployment settings compared with that reference age?
- What is the HIV-coinfection share of TB deaths in the settings where the program would operate? That determines whether the sign is negative or positive.
- Is the statin effect on TB mortality homogeneous across age and HIV status? The constant-RR assumption is a modeling simplification, not an empirical finding.

### Judge Audit
Surviving strength: weak
Justification: **Justification:**
- The debate was largely productive, and its main effect was to shrink the critique.
- The Challenger conceded that the critique is low-impact for the decision on the Advocate's numbers.
- The Challenger also conceded that the illustrative gradients are unsourced and that the minimum plausible impact is zero.
- What survives is a documentation request about how 27 was derived, plus a bounded downside of about −11% that does not change the decision.
- The Advocate's weaker moves (the unsized offset, the overconfident reading of "per death") did not affect this outcome, because the Challenger's own concessions settle materiality.
Recommended action: 1. **CONCLUDE NOW:** The critique's mechanism is valid in principle but is not decision-relevant.
   - Under the worst case in either side's grounded range (about −11%), SROI stays well above the bar.
   - The sign is uncertain, and the effect is zero if 27 is already decedent-weighted.
   - Treat this as a documentation fix, not a model adjustment. Confidence: moderately high.
   - One low-cost check would close the question: ask for or locate the source of 27. As a cross-check, compare it to the GBD TB YLL ÷ TB deaths ratio for the main deployment countries. This is feasible with public GBD data.
   - If the GBD ratio is roughly 24–30, drop the critique.

**action_feasibility:** actionable_now
Action feasibility: actionable_now
Advocate failures: []
Challenger failures: []
Debate resolved: The debate established four things:

- The structural point is mathematically correct.
- Under the BOTEC's constant relative-risk structure, a death-weighted DALYs-per-death figure is the correct multiplier. Effect heterogeneity is therefore off the table absent new evidence.
- Whether the critique applies at all hinges on a single fact: how 27 was derived.
- Both sides agree that even the Quantifier's adverse case (24 DALYs/death, about −11%, SROI around 2,715x) neither crosses the ~2,000x bar nor reaches the 25% materiality threshold.
Debate unresolved: Two questions remain open:

- Is 27 a decedent-weighted figure (e.g., GBD YLL ÷ deaths) or life expectancy at a case or reference age?
- What is the net sign of any bias, given the age-skew versus HIV-skew of TB deaths in actual deployment settings? Neither side grounded the deployment mix.

--- Critique: A global-average mortality may not match the countries where an atorvastatin adjunct would actually be deployed ---

### Advocate
```
DEFENSE OF GIVEWELL'S (CG's) POSITION: Global-average mortality vs. deployment-country mortality

EXISTING COVERAGE:
- The BOTEC's population term is a global case count (about 5.5M at adoption). Aggregate deaths prevented = Σ(cases_i × mortality_i × uptake × relative reduction).
  - If uptake is roughly uniform across countries, which is what the single 60% assumes, Σ(cases_i × mortality_i) equals total cases × the case-weighted mean mortality.
  - The case-weighted mean is what a global figure is meant to be. A "case-weighted average over deployment countries" differs from the global figure only if deployment is not proportional to cases.
- The critique therefore reduces to a narrower claim: uptake is correlated with country mortality. It does not show that the global mean is the wrong object.
- The effect is modeled as a relative reduction (10%), so the absolute effect scales with local baseline mortality. A high-mortality country gains more absolute benefit and a low-mortality country gains less. This is the correct structure for a mixed-country average.
- The BOTEC already treats the 6% as "about 6%" and does not claim country resolution. It is a back-of-envelope figure.
- Trial-versus-programme mortality is a real issue, but it is mostly an effect-size question (relative_reduction), not a baseline question. The Phase III trial would estimate a relative effect, which is then applied to programmatic mortality. Applying a relative effect to a programme baseline is the standard way to transport a trial result.

EVIDENCE WEAKNESSES:
- The critique's own country figures (India 4–5%, South Africa 8–10%) are labelled "from memory, UNVERIFIED." The critique itself asks that they be removed. I treat them as an illustrative conditional, not as evidence.
- The cited evidence does not support the claimed spread.
  - WHO's 88% treatment success for drug-susceptible TB leaves a 12% residual that includes loss to follow-up, failure, and not-evaluated cases, not only deaths.
  - The 12% therefore does not show that mortality varies substantially by country. It shows that non-success exists.
- The critique concedes "direction: uncertain" and "strength: moderate-weak." It identifies no mechanism for a systematic bias, only variance around the 6%.
- Its own caveat (trial patients have lower mortality than programmatic cohorts) cuts toward lowering the baseline. But a Phase III relative effect applied to programmatic baseline mortality does not need a trial-population baseline. That caveat conflates the trial baseline with the deployment baseline.
- I cannot ground a specific WHO global on-treatment death rate for drug-susceptible TB, and I do not assert one. I also cannot ground the Quantifier's 5.5% "central." Treat both as uninformed priors.

MAGNITUDE CHALLENGE:
- Sensitivity runs give the following:

| Case | Change in SROI | SROI | Crosses ~2,000x bar? |
|---|---|---|---|
| Low (baseline mortality 4%, −33% from 6%) | −33% | about 2,037 | No |
| Quantifier central (5.5%) | −8.3% | about 2,800 | No |
| High (7.5%) | +25% | about 3,819 | No |

- The break-even mortality can be derived. SROI is linear in baseline mortality (the 10% relative reduction is held fixed). Break-even = 6% × 2,000 / 3,055 ≈ 3.9%. This matches the critique's "3.9% threshold."
- Reaching 3.9% would require a deployment-weighted mortality about 35% below the stated 6%. Even the critique's own India-dominated illustration (about 4.5%) stays above this.
- The Quantifier's low case of 4% appears to require nearly all deployment to be in low-mortality settings. The critique itself calls that mix a hypothetical.
- The Quantifier's central (5.5%) moves SROI by only −8%, well under the 25% decision-relevance threshold.
- The low case's −33% is built on figures the critique concedes are unsourced.

OFFSETTING FACTORS:
- The CEA parameter map notes that notified-cohort mortality likely understates true mortality because of unascertained deaths (post-notification deaths, loss to follow-up who die). That pushes baseline_mortality up.
- The critique's own high-HIV scenario (>6%) raises SROI. The critique's range is two-sided, so there is no net downward direction.
- If TB burden is concentrated where mortality is higher (HIV-endemic, delayed diagnosis), the global case-weighted mean would already reflect this. It would not make 6% too high.
- Higher-mortality settings also have more absolute benefit per treated patient under a relative effect. This partially offsets any lower uptake there.

OVERALL ASSESSMENT:
Strong defense.
- The critique is a request for a sensitivity range, not a demonstrated bias.
- Its mechanism is uptake-mortality correlation. It does not show that the global mean is mis-specified.
- Its quantitative inputs are unsourced by its own admission.
- Even the most pessimistic stated scenario stays above the bar.
- The cushion at the pessimistic end is thin (about 2,037 vs 2,000). If other critiques push the estimate down simultaneously, this parameter's low end could matter in combination.

CONCESSIONS:
- The 6% has no stated source or country decomposition. A sensitivity range (roughly 4–7.5%) would improve transparency.
- Heterogeneous uptake correlated with country mortality is a real second-order effect that the single 60% uptake does not capture.
- The −33% low case exceeds the 25% change threshold, although it does not cross the bar.
- The lack of a stated link between trial-population and programme mortality is a legitimate gap. It matters mainly for relative_reduction, which is outside this critique's scope.
- If the critique's illustrative India/South Africa figures were removed or sourced from WHO country cohort tables, as it requests, I would not object.
```

### Challenger
REBUTTAL: Global-average mortality vs. deployment-country mortality

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: with uniform uptake, Σ(cases_i × mortality_i) equals total cases × the case-weighted mean. A global figure is therefore the correct object, and the critique reduces to an uptake-mortality correlation.

Response:

1. **I concede the algebra.** If 6% is the case-weighted mean of on-treatment mortality over the same population the 5.5M case count refers to, and uptake is uniform, the Advocate's identity holds.
2. **The "if" is unestablished.** The Advocate concedes the 6% has no stated source or country decomposition, and says it "cannot ground" a WHO global death rate. The defense that "a global figure is what a case-weighted mean is" therefore protects a figure whose provenance neither side can show. Whether 6% is a case-weighted mean of anything is unverified.
3. **Uptake correlation is not obviously second-order.** The Advocate calls it "second-order" without quantifying it.
   - The bar-crossing margin is thin. Break-even is 6% × 2,000 / 3,055 ≈ 3.9%.
   - The critique's own low case is 4%, only about 0.1 percentage point above that. Any systematic skew of deployment toward lower-mortality settings moves the answer toward the bar.
4. **"Relative effect scales with local baseline" assumes the relative effect is constant across settings.**
   - That is an assumption in the model, not a finding. I cannot cite a trial establishing it for atorvastatin in TB.
   - Conditional argument: if excess deaths in high-HIV or late-presenting cohorts come from causes a statin adjunct does not modify (advanced HIV, delayed diagnosis), the relative reduction would be lower where baseline mortality is higher.
   - Then "high-mortality countries gain more absolute benefit" fails, and the offset the Advocate relies on shrinks.
5. **On trial-versus-programme mortality, I accept the Advocate's correction.**
   - The caveat bears mainly on whether the 10% relative reduction transports to programmatic populations, not on the baseline.
   - The Advocate also concedes the model states no link between trial and programme mortality.
   - That gap is real. It simply sits in a parameter outside this critique's scope.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

1. **The 88% treatment success figure.**
   - The Advocate is right that the 12% residual includes loss to follow-up, failure, and not-evaluated cases, not only deaths. It does not by itself show that death rates differ by country.
   - But it also does not show that mortality is uniform. It is a global aggregate, and the critique's request for country-level WHO cohort tables is exactly what would settle the question.
2. **The India and South Africa figures.**
   - The critique labels them from-memory and UNVERIFIED. That is not the same as rejected.
   - I treat them only as a conditional: if India is about 4–5% and South Africa about 8–10%, the weighted mean depends on the deployment mix.
   - Even without those numbers, the verifier's note that the 12% non-success "leaves room for substantial country spread" is the only evidence on the table about spread. The Advocate offers none showing narrow spread.
3. **"No mechanism for systematic bias."**
   - The critique said direction is uncertain. The Advocate's defense does not make the sensitivity range unnecessary.
   - The Advocate itself recommends a 4–7.5% range. That concession is the critique's central ask.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: the pessimistic cases don't cross the ~2,000x bar, the break-even is about 3.9%, the 4% low case requires an implausible all-low-mortality deployment, and the central case moves SROI only −8%.

Response:

1. **I confirm the arithmetic.**
   - SROI is linear in baseline mortality: 3,055 × (5.5/6) ≈ 2,800 (−8.3%).
   - The India-dominated illustration at 4.5% gives 3,055 × (4.5/6) ≈ 2,291 (−25%).
   - So at the critique's own illustration, the cushion above 2,000 is about 14.5%, which is not trivial.
2. **The minimum-impact claim does not follow from "stays above the bar."**
   - The Advocate's 2,291 figure is itself a −25% move, right at the 25% decision-relevance threshold the Advocate cites.
   - The Advocate then calls −8% "well under" the threshold. That is the central case, not the illustration the Advocate invokes for the pessimistic end.
3. **The low case is only 2% above the bar.**
   - 2,037 versus 2,000 leaves almost no margin. The Advocate acknowledges this.
   - The Advocate's response is that the 4% low case "appears to require nearly all deployment in low-mortality settings." This is an assertion. Neither side has a deployment-mix estimate, so I cannot judge the plausibility of the low case either way.
4. **Decision-relevance is asymmetric.** The bar is crossed only on the downside.
   - The Advocate's "two-sided, so no net direction" is correct for expected value.
   - For the funding decision, the high-HIV upside (+25%, 3,819) changes nothing, while the downside approaches the bar.
   - Symmetric uncertainty is not symmetric decision risk.
5. **Combination risk.** The Advocate concedes that if other critiques push the estimate down simultaneously, this parameter's low end "could matter." With a 2% cushion at the low end, almost any co-moving downward adjustment would cross.

**RESPONSE TO "OFFSETTING FACTORS":**

1. **Unascertained deaths push the baseline up.**
   - This rests on the Advocate's reading of the CEA parameter map, which I have not seen quantified.
   - It is a global adjustment. It does not address country heterogeneity, and it is not evidence that the 6% already includes it.
   - If the 6% already includes that adjustment, it is not an offset. If it does not, the size is unquantified. Either way it cannot be netted against a −33% low case.
2. **"Higher-mortality settings already reflected in the global mean."**
   - This is true only if the 6% is a properly case-weighted mean (see point 2 under Existing Coverage). The Advocate has no source for it.
3. **"More absolute benefit in high-mortality settings."**
   - This holds only under a constant relative effect. See the conditional in point 4 under Existing Coverage.
   - It also offsets uptake only if uptake is lower where mortality is higher, which is itself unquantified.
4. **The offsets are therefore hypothetical.** None is quantified, and none is established as being in the model.

**KEY UNRESOLVED QUESTIONS:**

- What is the source and population of the 6%? Is it a case-weighted global mean of notified-cohort deaths, a pooled trial figure, or a judgment?
- Is the 5.5M case count notified or incident, and does that match the mortality denominator?
- Is the statin relative reduction homogeneous across HIV status, age, and presentation delay? If not, the "relative effect scales with baseline" structure does not protect the estimate in high-mortality settings.
- What is the plausible deployment mix, and is uptake correlated with country mortality? A 4–4.5% effective baseline (the 2,037–2,291 range) is within reach if deployment skews low-mortality.
- Do other critiques also push SROI down? With a 2% cushion in the low case, combined effects could cross the bar.

### Judge Audit
Surviving strength: moderate
Justification: The core arithmetic was done soundly by both sides and is agreed. The Challenger's strongest grounded moves stand:
- The Advocate's "existing coverage" defense depends on an unsourced 6% that the Advocate itself calls an uninformed prior.
- The critique's own 4.5% illustration yields about −25%, a point the Advocate's framing glossed over.
Against this, the critique offers no evidence of directional bias, its country numbers are unverified, and no scenario crosses the bar. The Challenger's claims of spread and combination risk also lean on burden-shifting. The critique survives at its own self-rated "moderate-weak" level as a sensitivity request. Its quantitative illustration does not survive as evidence.
Recommended action: 2. SPECIFIC INVESTIGATION: Two lookups would settle the main open question, and both are feasible with existing tooling.
   - Retrieve the WHO Global TB Report country treatment-outcome data, specifically the "% died" for the new-and-relapse cohort (2021 or 2022), for the eight high-burden countries the verifier listed (India, Indonesia, China, Philippines, Pakistan, Nigeria, Bangladesh, South Africa). Compute the case-weighted mean and compare it to 6%.
   - Retrieve the pooled case-fatality estimate from the Indian systematic review the verifier located.
   - Separately, check the BOTEC documentation for the stated source of the 6%, and whether the 5.5M case count is notified or incident.

   Interim conclusion: if the case-weighted mean falls between 5% and 7%, close the critique with a documented sensitivity range. If it falls at or below about 4.5%, escalate it as a decision-relevant input to be combined with other downward critiques. Until then, the model should display a 4–7.5% range, and the unsourced country percentages should be removed.
Action feasibility: requires_specified_evidence
Advocate failures: ['sound_synthesis_noted: The Advocate derived break-even mortality from linearity: "SROI is linear in baseline mortality… Break-even = 6% × 2,000 / 3,055 ≈ 3.9%." This is a correct, transparent derivation. It also reproduces the critique\'s threshold independently, and the Challenger confirmed it.', 'false_definitiveness: The Advocate argues that "If TB burden is concentrated where mortality is higher… the global case-weighted mean would already reflect this. It would not make 6% too high." Elsewhere the Advocate concedes the 6% "has no stated source or country decomposition" and calls it an "uninformed prior." The core "existing coverage" argument confidently treats 6% as a case-weighted mean, but the Advocate admits it cannot show that it is one. The algebraic identity is correct. Applying it to this parameter is unestablished.', 'unsupported_estimate_fabricated: The Advocate says the 4% low case "appears to require nearly all deployment to be in low-mortality settings." This is a claim about which deployment mix is plausible. No country-level mortality levels or deployment-mix data back it, and the verifier found none. The Advocate cannot simultaneously reject the India figure as unsourced and use an implied country distribution to dismiss 4% as implausible.', 'false_definitiveness: The Advocate\'s framing of thresholds is selective. It stresses that the central case (−8.3%) is "well under the 25% decision-relevance threshold." It cites the critique\'s 4.5% illustration only as "stays above [the bar]." It never notes that 4.5% implies about −25%, which sits exactly at the threshold the Advocate invoked. The self-assessment of "Strong" is also inflated. The Advocate concedes the critique\'s central ask (a 4–7.5% sensitivity range), a real uptake–mortality gap, a −33% low case, and a 2% cushion. That record is a partial defense.', 'call_to_ignorance (mild): The Advocate offers "notified-cohort mortality likely understates true mortality… That pushes baseline_mortality up" as an offset. It is unquantified, and the Advocate does not establish whether the 6% already incorporates it.']
Challenger failures: ['sound_synthesis_noted: The Challenger computed "3,055 × (4.5/6) ≈ 2,291 (−25%)" and the resulting ~14.5% cushion. This is correct arithmetic and the most useful quantitative addition to the debate. It surfaces that the critique\'s own illustration lands at the decision-relevance threshold.', 'call_to_ignorance: The Challenger writes that "the verifier\'s note that the 12% non-success \'leaves room for substantial country spread\' is the only evidence on the table about spread. The Advocate offers none showing narrow spread." "Leaves room for" is not evidence of spread, and the Challenger had just conceded that the 12% "does not by itself show that death rates differ by country." Shifting the burden to the Advocate to disprove spread treats absence of evidence as support.', 'call_to_ignorance (mild, partially mitigated): The Challenger proposes a mechanism by which the relative reduction could be lower in high-HIV or late-presentation settings. It is explicitly framed as a conditional and admits no citation, which mitigates it. Two problems remain. The conditional is pure speculation in both directions. It also imports a relative_reduction heterogeneity argument after the Challenger had itself agreed that relative-effect transport is "outside this critique\'s scope.', 'strawmanning (minor misattribution): The Challenger refers to "The Advocate\'s 2,291 figure," but the Advocate never computed 2,291; the Challenger did. The Challenger also calls the 4% low case "the critique\'s own low case," when it originated with the Quantifier. The critique\'s illustration was 4.5%. These slips do not change the substance but blur provenance.', 'unsupported_estimate_counter (mild): The Challenger writes "With a 2% cushion at the low end, almost any co-moving downward adjustment would cross." This rests on the 4% low case, which the Challenger elsewhere says it "cannot judge the plausibility of." Combination risk with unnamed other critiques is asserted, not demonstrated.']
Debate resolved: Both sides agree on the following:
- SROI is linear in baseline mortality, with break-even near 3.9%. The central case (5.5%) gives −8%, the critique's illustration (4.5%) gives −25%, and the low case (4%) gives −33%.
- No stated scenario crosses the ~2,000x bar.
- The trial-versus-programme concern belongs to relative_reduction, not baseline_mortality.
- A sensitivity range of roughly 4–7.5% is warranted, and the unsourced India and South Africa figures should be removed or sourced.
- The critique therefore survives as a transparency and sensitivity request, not as a demonstrated directional bias.
Debate unresolved: - The provenance of the 6% is unknown. It could be a case-weighted global mean, a trial figure, or a judgment. Neither side can establish it, so the Advocate's "global mean already reflects heterogeneity" argument is unverified.
- Whether the plausible deployment mix could push the effective baseline to 4–4.5% remains open. That range sits at or beyond the 25% threshold and near the bar.
- It is unclear whether the case-count and mortality denominators match (notified versus incident cases).

--- Critique: Industry phase-transition base rates put "II and III both succeed" at roughly 15–25%, so 40% requires an unstated premium of about 1.6–2.7× ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION: Industry phase-transition base rates put "II and III both succeed" at roughly 15–25%, so 40% requires an unstated premium of about 1.6–2.7×

**EXISTING COVERAGE:**
- CG's 40% is an explicit probability haircut. It already cuts expected benefit by 60% (from $OP 54B to about $OP 21.6B). The BOTEC is not treating success as the default.
- CG's own framing is "Phase II and Phase III both succeed." The grant funds a Phase IIc that follows a positive Phase IIa/b signal on a drug with an established safety record. It is not a first-in-class Phase II. The 40% is therefore a conditional judgment, not a naive unconditional industry draw.
- The 60% uptake "if it works" is a second, separate haircut applied after success. The Parameter Map notes that adoption risk "may be partly captured in uptake." The critique's decomposition adds a separate P(adopted | III) of 0.7–0.85 on top of that, which risks double-counting.
- I concede that CG states no reference class and does not decompose the 40%. The Parameter Map confirms this. Coverage here is implicit only.

**EVIDENCE WEAKNESSES:**
1. **Definitional mismatch.** The critique itself flags that the BIO 2011–2020 transition rates (Phase II→III 28.9%, Phase III→filing 57.8%) are not defined like CG's p_success. These are the main support for the 15–25% claim, so the mismatch weakens the headline "1.6–2.7× premium" figure.
2. **Business-driven attrition.** The critique concedes that industry rates include business-driven terminations. For an off-patent generic funded by a philanthropic or public-health consortium, commercial and strategic attrition is largely irrelevant. This would push the applicable rate above the industry rate. The critique asserts this direction but cannot size it. I also cannot ground a size, so I treat the effect as unquantified.
3. **Phase III→filing includes a regulatory step.** Atorvastatin is already approved. CG needs a positive trial plus guideline adoption, not a new-drug filing. The 57.8% figure is therefore not the same event as CG's Phase III success.
4. **The decomposition is unsourced.** The critique labels it "my own inference, not from a source," and the P(IIc) ≈ 0.5 figure has no grounding. The stated range also does not follow from its own components. With the critique's own inputs, the product ranges from 0.5 × 0.40 × 0.70 = 0.14 to 0.5 × 0.55 × 0.85 ≈ 0.23. The stated upper bound of 0.30 does not come out of those factors.
5. **Mixed signals within the sources.** The infectious-disease Phase III figure (~81%) comes from a single analysis, and the critique says the Wong 2019 figures need checking against corrected tables. Hay et al. 2014 (non-oncology: 34.8% × 54% ≈ 0.19) is the only corroboration. It is a secondary-source citation and is not TB-specific.
6. **Cross-references are broken.** The "Critique 2" and "Critique 4" references do not match this batch's numbering, so I cannot check the TB-track-record or adoption inputs the decomposition relies on.

**MAGNITUDE CHALLENGE:**
- Baseline SROI is about 3,055x. Break-even against the 2,000x bar is p ≈ 2,000 / (3,055 / 0.40) ≈ 0.26.
- The Quantifier's own central value of 0.27 gives about 2,062x, a 32.5% decrease. That is still above the bar. At the Quantifier's central value the critique does not cross the bar, though it does exceed the 25% materiality line.
- Only the low case (p ≈ 0.17, −57.5%, about 1,298x) crosses the bar. That case is the unadjusted BIO product, which the critique itself says should be adjusted upward for infectious disease and repurposing.
- The critique's own adjusted range is 25–32%. That straddles the break-even and sits mostly above it, so it does not support "below the bar."
- **Double-counting of adoption.** Take the critique's P(IIc) × P(III | IIc) without the adoption factor, since uptake already handles part of that. At P(IIc) = 0.5 this gives 0.20–0.275. If P(IIc) were 0.7, which is plausible for a dose-selection trial that follows a positive IIa/b, it gives 0.28–0.385. This is arithmetic on the critique's own components. The 0.7 is a sensitivity value, not a grounded estimate. It shows the conclusion depends on an ungrounded P(IIc).
- A reasonable range for a more defensible p_success is about 0.25–0.40. The 40% sits at the top of that range and the Quantifier's 0.27 sits near the bottom.

**OFFSETTING FACTORS:**
- **Omitted benefit channels.** The BOTEC values only on-treatment mortality. It excludes lung-damage morbidity, post-treatment mortality, transmission, and diagnostic value. The Parameter Map identifies these as implicit zeros. A lower p_success applied to a benefit stream that omits these channels is a partial offset.
- **"Success" definition.** If Phase III success can be a surrogate endpoint (which the Parameter Map notes is undefined), success is easier to achieve than a mortality-powered trial implies. This cuts in favor of a higher p_success. It also raises the risk that the 10% mortality effect is overstated conditional on success. That is a separate parameter and I do not rely on it here.
- **Funding of Phase III.** CG's all-in cost already includes Phase III, so P(III is funded) is not an additional factor in the same way it would be for an industry candidate.

**OVERALL ASSESSMENT:** Partial defense.
- The direction of the critique is right: 40% is probably somewhat high, and CG gives no reference class.
- The size is overstated. The headline "1.6–2.7× premium" depends on unadjusted industry rates that the critique itself says are inapplicable.
- The critique's own decomposition has an arithmetic overreach and an adoption double-count, and the P(IIc) input is ungrounded.
- At the Quantifier's central value (0.27) the estimate stays above 2,000x, while the 32.5% drop crosses the 25% materiality threshold.

**CONCESSIONS:**
- CG provides no reference class and no decomposition for the 40%. That is a real transparency gap.
- Two independent industry sources (BIO and Hay et al. 2014) put the unadjusted product at roughly 0.17–0.19. A 0.40 value implies a premium of about 2× over those rates. CG would need to defend that explicitly.
- A p_success of about 0.27–0.30 is plausible and would reduce SROI by 25–33%. That is material by the 25% threshold even though it does not breach the bar.
- The margin over the bar is thin: break-even is 0.26, and the central adjusted value lies close to it.

### Challenger
REBUTTAL: Industry phase-transition base rates put "II and III both succeed" at roughly 15–25%, so 40% requires an unstated premium of about 1.6–2.7×

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the 40% is already an explicit 60% haircut, and it is conditional on a positive IIa/b signal and a known safety record, so it is not a naive industry draw.

- **A haircut is not a calibration.** The question is whether 40% is the right haircut, not whether some haircut exists. The Advocate concedes there is no reference class and no decomposition, so the 40% is currently unexplained.
- **Known safety removes only part of the attrition.** Safety history helps with safety-driven failure. The Phase II→III transition is mostly an efficacy filter, and efficacy is the main reason drugs fail in Phase II (Waring et al. 2015 is my recollection; I cannot verify the exact shares). The positive IIa/b signal is also not extra information relative to the base rate, because industry Phase II cohorts include drugs with early signals.
- **The critique's own inputs show how high 40% is.** Take the Phase III figure of about 81%, the most favorable one, from the infectious-disease analysis the critique cites. To reach 0.40, Phase II would have to succeed at 0.40 / 0.81 ≈ 49%.
  - That is well above both cited Phase II rates (28.9% BIO, 34.8% Hay).
  - The lower end of the critique's adjusted range is 0.289 × 0.81 ≈ 0.23, which is below the 0.26 break-even.
- **On the "double-counting" of adoption.** The Advocate's own source for the overlap is a Parameter Map note that adoption "may be partly captured in uptake." That is a hedge, not a finding.
  - Uptake of 60% "if it works" is a coverage share among eligible patients.
  - P(guideline adoption | positive trial) is a gate on whether coverage starts at all.
  - These are plausibly different events, and the Advocate has not shown that they overlap fully.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the definitional mismatch, business attrition, the regulatory step in Phase III→filing, the unsourced decomposition, thin corroboration, and broken cross-references weaken the 15–25% figure.

1. **Definitional mismatch.**
   - It cuts in both directions. If CG's p_success runs from Phase IIc to adoption, it contains an adoption step that BIO transitions exclude, which lowers p. Business attrition runs the other way. The Advocate has no basis for saying the net effect favors 40%.
   - The Advocate admits it cannot size the business-attrition offset. An unsized offset cannot justify a 2× premium.
2. **Regulatory step.**
   - As I recall the BIO 2011–2020 tables, Phase III→NDA/BLA (57.8%) is a trial-outcome-plus-filing-decision transition. The NDA/BLA→approval step is separate, at roughly 90%. I am fairly confident of this but did not re-check it.
   - If so, 57.8% does not embed regulatory approval. CG's event (positive trial plus guideline adoption) is no easier than the filing event.
3. **Hay et al. 2014 as sole corroboration.**
   - The Advocate calls this thin, but it is an independent source. By the Advocate's own computation (34.8% × 54% ≈ 0.19), it lands in the same band as BIO.
   - The Advocate's concession that two independent sources give about 0.17–0.19 undercuts "the evidence is mixed."
4. **Arithmetic on the decomposition.** I concede the Advocate is right that 0.5 × 0.55 × 0.85 ≈ 0.23, not 0.30, so the stated upper bound does not follow.
   - This correction lowers the critique's range. The decomposition then spans 0.14–0.23, entirely below the 0.26 break-even.
   - The decomposition is still the critique's own inference and ungrounded in P(IIc), and I do not rest the case on it.
5. **Broken cross-references.** This is an editing defect in the critique. It does not bear on the base-rate evidence.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

- **Concessions.**
  - At the Quantifier's central 0.27, SROI is about 2,062x, still above the 2,000x bar.
  - Only the 0.17 low case crosses the bar.
- **The −32.5% change is material.** It exceeds the 25% threshold the Advocate accepts, and the margin over the bar shrinks to about 3%.
- **The Advocate's "defensible range" is unsourced.**
  - Its 0.25–0.40 range comes with the admission that the 0.7 value for P(IIc) is "a sensitivity value, not a grounded estimate."
  - Without that value, the Advocate's own no-adoption arithmetic gives 0.20–0.275, which sits mostly at or below break-even.
  - The Advocate shows that 0.40 is reachable. It does not show that 0.40 is the expected value.
- **At the midpoint of the Advocate's own range** (0.325), SROI is 3,055 × 0.325 / 0.40 ≈ 2,482x, an 18.8% drop. That is under the materiality line, but it rests on the ungrounded range.
- **Minimum defensible impact.** The best-grounded numbers, BIO and Hay, imply 0.17–0.19. Infectious-disease and repurposing adjustments raise this to the 0.23–0.32 range computed above. Any point in that range falls below 0.40, and the lower half falls below break-even.

**RESPONSE TO "OFFSETTING FACTORS":**

- **Omitted benefit channels** (morbidity, transmission, diagnostics).
  - These are real omissions, but they are unquantified and are not in the model.
  - They are a separate parameter. They do not make a miscalibrated p_success correct. Whether net SROI clears the bar is a different question from whether 40% is justified.
- **Surrogate-endpoint success.** The Advocate itself says this could also inflate the 10% mortality effect conditional on success, so the net direction is unclear. I read this as a wash, not an offset.
- **Phase III funding already in cost.** I concede this. It means no extra funding-risk factor is needed, but it does nothing about scientific failure, which is what the base rates measure.

**KEY UNRESOLVED QUESTIONS:**

- What is the right P(Phase IIc success) for a PK/dose-selection trial? The 0.5 and 0.7 values are both ungrounded. Is there an analogous reference class, such as repurposed anti-infective dose-finding trials?
- Is CG's "success" defined as a positive Phase III trial, or as adoption? The answer decides how much the adoption factor and the uptake haircut overlap.
- How large is the upward correction for removing business-driven attrition in a publicly funded program? Neither side can size it.
- Does the 81% infectious-disease Phase III figure survive checking against the corrected Wong 2019 tables? The critique's adjusted range of 0.23–0.32 depends on it.

### Judge Audit
Surviving strength: moderate
Justification: The core directional claim survived. The Advocate conceded that 40% implies about a 2× premium over two independent base rates, with no stated justification. Both sides agreed a grounded adjusted value of about 0.27–0.30 produces a material (>25%) reduction. However, the critique's stronger claim, that p_success falls below the 0.26 break-even, was not established. That claim relied on the overreaching decomposition and the Challenger's dataset-mixed 0.23 lower bound. The Advocate's counter-range likewise rested on an ungrounded 0.7. The substantive question of whether the bar is crossed remains open, with the best-grounded point estimate sitting just above break-even.
Recommended action: 1. CONCLUDE NOW, with moderate confidence.
   - CG's 40% p_success is unsupported by any reference class and is likely too high.
   - The best-grounded adjusted range is about 0.25–0.32, using the infectious-disease Phase II of about 37–40% × Phase III of about 80%, or BIO/Hay with an upward adjustment.
   - This implies an SROI reduction of roughly 20–37% (about 1,900–2,450x). That should be treated as a material sensitivity which may or may not breach the 2,000x bar, not as a demonstrated bar-crossing.
   - CG should be asked to state its reference class and to say whether "success" includes guideline adoption.
   - The critique text should replace "24–26%" and the 0.14–0.30 decomposition with the 0.25–0.32 range and drop the claim that the central value is about 0.20.
   - One targeted check is feasible within existing tooling: pull the corrected Wong 2019 infectious-disease Phase II and Phase III transition rates, with the non-industry-sponsored breakdown. This would settle whether the range centres nearer 0.25 or 0.32.
Action feasibility: actionable_now
Advocate failures: ['strawmanning: The Advocate writes "The critique itself flags that the BIO 2011–2020 transition rates … are not defined like CG\'s p_success" and "The critique concedes that industry rates include business-driven terminations." Both points came from the verifier. The verifier explicitly says "The critique doesn\'t discuss this definitional mismatch." The Advocate attributes concessions to the critique that it never made. It then uses them to say the headline rests on rates "the critique itself says are inapplicable." The critique said the rates should be *adjusted upward*, not that they are inapplicable.', 'unsupported_estimate_pseudo: The "double-counting" argument. The Parameter Map says adoption "may be partly captured in uptake." The Advocate turns this into dropping the adoption factor *entirely*, which yields 0.20–0.275. Going from "partly captured" to "fully remove" is a clear logical gap.', 'unsupported_estimate_counter: A reasonable range for a more defensible p_success is about 0.25–0.40." The upper end depends on P(IIc) = 0.7, which the Advocate had just labelled "a sensitivity value, not a grounded estimate." A sensitivity bound was then presented as the edge of a "reasonable range." This is a counter-estimate with the same grounding deficit the Advocate criticises in the critique\'s P(IIc) = 0.5.', "sound_synthesis_noted: Several parts of the Advocate's case were sound:"]
Challenger failures: ["unsupported_estimate_pseudo: The lower end of the critique's adjusted range is 0.289 × 0.81 ≈ 0.23.", 'false_definitiveness: The positive IIa/b signal is not extra information relative to the base rate, because industry Phase II cohorts include drugs with early signals." This is asserted confidently with no support. It is also doubtful: a drug entering IIc after a completed positive IIa/b is conditionally past some Phase II attrition. A related problem is the efficacy-attrition claim from "Waring et al. 2015 … my recollection; I cannot verify." The Challenger was honest about the uncertainty but still used the claim as load-bearing.', 'strawmanning: The Advocate has no basis for saying the net effect favors 40%." The Advocate did not claim the net definitional effect justifies 40%. It said the mismatch weakens the 1.6–2.7× headline, and it explicitly treated the business-attrition offset as unquantified.', "sound_synthesis_noted: Several parts of the Challenger's case were sound:"]
Debate resolved: The debate established four points:
- CG offers no reference class or decomposition for the 40%.
- Unadjusted industry base rates (BIO, Hay) put the two-phase product at about 0.17–0.19.
- The critique's own decomposition tops out at about 0.23, not 0.30.
- Both sides accept that a plausible adjusted value of about 0.27–0.30 cuts SROI by roughly 25–33%. That is material under the 25% threshold but leaves the estimate at or just above the 2,000x bar, with break-even at about 0.26.
Debate unresolved: Four questions remain contested:
- **The IIc success probability.** P(IIc success) for a dose-selection trial following positive IIa/b is still ungrounded on both sides (0.5 vs 0.7).
- **The adoption overlap.** It is unclear whether CG's "success" includes adoption, which determines how far the adoption gate overlaps the 60% uptake haircut.
- **The 81% figure.** It is unclear whether the infectious-disease Phase III figure (about 81%) and its matching Phase II rate (about 37–40%) survive the corrected Wong 2019 tables.
- **Funding-related attrition.** It is unresolved whether public funding raises or lowers attrition relative to industry. Neither side engaged with the verifier's non-industry data.

--- Critique: The TB-specific reference classes (host-directed therapy, adjunctives, regimen-shortening) have a much worse record than 40% ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION: The TB-specific reference classes (host-directed therapy, adjunctives, regimen-shortening) have a much worse record than 40%

**EXISTING COVERAGE:**
- The 40% is already a joint probability that both Phase II and Phase III succeed, and it multiplies the whole benefit stream. CG has already discounted the benefit by 60%.
- The BOTEC is conditional on a prior positive Phase IIa/b human trial in TB patients showing faster clearance and less lung damage. The critique's examples are not obviously conditioned on a comparable signal.
- The CEA parameter map says no reference class is stated. So CG did not ignore the concern, but it did not document it either. I concede this.

**EVIDENCE WEAKNESSES:**
1. **The critique rates its own central numbers as ungrounded.** The 10–20% TB-class rate and the 0.2–0.3 blend are labelled "UNGROUNDED inferences," and the critique calls its strength "qualitative prior shift rather than a quantified one." The sensitivity run shows what rests on those numbers: the −62.5% result comes from p=0.15, the figure with the least support.
2. **The list is small and hand-picked.** The critique admits selection bias. It also admits several trials were not Phase II→III transitions, and that the statin class has no denominator because most of its evidence is preclinical. No rate can be computed from a class like that.
3. **The record is mixed, not "much worse than 40%."** On the critique's own evidence:
   - Dexamethasone in TB meningitis (Thwaites 2004) was positive in HIV-negative adults. Pooled analysis supports a survival benefit, and the drug was adopted.
   - ACT HIV (HR 0.85, 0.66–1.10) was a trial of the same drug in a different population. Counting it as a second class failure double-counts one drug that did reach practice.
   - The vitamin D meta-analysis found significantly higher culture conversion (OR 1.22, 1.04–1.43). The null is on time to conversion, not on the overall proportion converting.
4. **Endpoint mismatch.** ACT HIV and Thwaites concern TB meningitis mortality, and vitamin D concerns culture conversion. The critique concedes these differ from the pulmonary TB endpoint here, so the transfer to this trial is weak.
5. **The regimen-shortening examples are not adjuncts.** My recollection, not verified here, is that:
   - REMoxTB, RIFAQUIN and OFLOTUB (all 2014) failed to show non-inferiority for 4-month fluoroquinolone regimens.
   - Study 31/A5349 (Dorman, NEJM 2021) succeeded for a 4-month rifapentine-moxifloxacin regimen.
   - The critique itself says these items need checking.
   - Regimen shortening is a non-inferiority design, a different success criterion from showing a benefit on an add-on drug. A mixed record there tells us little about a mortality or surrogate superiority trial.

**MAGNITUDE CHALLENGE:**
- **Threshold arithmetic.** Baseline SROI is about 3,055x at p=0.40, and SROI is linear in p. The ~2,000x bar is therefore crossed only below p ≈ 0.40 × 2000/3055 ≈ 0.26.
- **The critique's central case sits at the bar.** The central p=0.25 gives about 1,909x, only ~4.5% under 2,000x. The blended range 0.2–0.3 straddles the threshold. At p=0.30, SROI is about 2,291x, still above the bar.
- **Only the low end is clearly decisive.** Only p ≲ 0.15, the least grounded value, produces a clear failure.
- **Implied stage probabilities.** I back out what 40% implies using the BIO/Informa/QLS 2011–2020 Phase III transition rate of ~58%. This is recalled, not verified in this package.
  - 0.40 / 0.58 ≈ 0.69 for Phase IIc.
  - 0.25 / 0.58 ≈ 0.43 for Phase IIc.
  - The difference is how likely a dose-optimization trial of a drug with a positive Phase IIa/b is to succeed. I cannot ground either number, but the gap is narrower than "much worse" suggests.
- **Where a generic prior would land.** The same BIO report's Phase II transition rate (~29%, also recalled) gives a joint of ~17%. That prior covers all Phase II trials, including weaker candidates. A drug with a positive human Phase IIa/b signal should sit above it, but I cannot say by how much.

**OFFSETTING FACTORS:**
- **Value omitted by the BOTEC.** The CEA values only on-treatment mortality. The parameter map lists four channels as implicit zeros: morbidity DALYs (the lung-damage endpoint is in the trial), post-treatment mortality, transmission averted, and diagnostic value. These could raise SROI, and they matter most in exactly the lower-p scenarios.
- **The critique's own counterweights.** The vitamin D overall-conversion finding and the persistent dexamethasone benefit in HIV-negative adults both show that some adjunctive classes do yield usable positive results.
- **Definition of success.** If "success" means a result strong enough for guideline adoption on a surrogate or morbidity endpoint, the probability of success is higher than for a mortality-powered trial. This is only a conditional point, because the CEA does not define success.

**OVERALL ASSESSMENT: Partial defense.**
- The qualitative direction (40% is probably generous compared with the generic Phase II→approval base rate, and CG gave no reference class) is hard to rebut.
- The quantified case rests on a small, selective, partly mismatched set of trials. Its central value (0.25) only reaches the bar, and the omitted benefit channels give a plausible offset.
- The critique is therefore a reasonable reason to move toward ~0.25–0.30, but not clearly to a decisive failure.

**CONCESSIONS:**
1. CG states no reference class or stage-by-stage breakdown for the 40%. A reader cannot check it.
2. The generic industry base rate for Phase II through approval, as I recall it, is below 40%. The adjunctive-TB record is at best mixed and probably does not support a higher figure.
3. Dexamethasone shows that even the successful adjunct had a modest and heterogeneous effect. That bears more on `relative_reduction` than on `p_success`, and it is a legitimate caution on the 10% conditional effect.
4. A p_success of 0.25–0.30 would put SROI near or slightly below the 2,000x bar, so the critique is decision-relevant in the narrow sense that the margin is thin.

### Challenger
REBUTTAL: TB-specific reference classes have a much worse record than 40%

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the 40% is a joint Phase II+III probability that already discounts the benefit stream by 60%, and the BOTEC is conditional on a positive Phase IIa/b human signal, which the critique's examples are not obviously conditioned on.

Response:
- **"Already discounted" restates the parameter; it does not defend its value.** The critique does not say p_success is missing. It says 0.40 has no stated reference class (the Advocate concedes this) and is higher than the available priors.
- **The Advocate's own derivation puts 0.40 above the generic prior.**
  - The Advocate recalls BIO/Informa/QLS rates of ~58% for Phase III and ~29% for Phase II.
  - Joint: 0.58 × 0.29 ≈ 0.17.
  - So 0.40 is about 2.4× the generic joint rate.
  - The Advocate flags both inputs as unverified, so this is a conditional argument.
  - If they are even roughly right, the 0.40 needs a documented justification for the 2.4× uplift. None exists.
- **The Phase IIa/b conditioning is not a clean uplift.**
  - A positive IIa/b signal is part of what a Phase II success is. The Advocate says it "should sit above" generic but "cannot say by how much."
  - So the conditioning is an unquantified hope, not coverage.
- **The conditioning argument also fails on its own terms for the TB-class examples.** The BOTEC's signal is "faster clearance and less lung damage."
  - The vitamin D meta-analysis found no shortening of time to conversion (verifier evidence item 1).
  - That is the same kind of signal the BOTEC conditions on.
  - Recalled, not in the evidence package: the 4-month fluoroquinolone regimens (REMoxTB, RIFAQUIN, OFLOTUB) were tested after positive earlier-phase culture-conversion data. I cannot ground this, and the critique itself says it needs checking.
  - If it holds, those are Phase II→III failures conditional on a positive signal, which is exactly the reference class the Advocate says the critique lacks.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the critique's central numbers (10–20%, 0.2–0.3) are self-labelled ungrounded, and the −62.5% result rests on the least-supported value, p=0.15.

Response:
- **Concede:** the 10–20% class rate has no denominator, and 0.15 is an inference.
- **Pivot:** the decision-relevance does not depend on 0.15. By the Advocate's own arithmetic, the bar is crossed below p ≈ 0.26.
  - The Advocate's recalled generic joint (~0.17) is below 0.26.
  - The Advocate's own "reasonable" range (0.25–0.30) straddles 0.26.
  - Only a prior above 0.26 keeps the intervention clear, and the Advocate supplies no grounded source for one.

> The Advocate claims: counting ACT HIV and Thwaites as separate data points double-counts one drug that reached practice.

Response:
- The critique does not say dexamethasone failed. It says the one adopted class member has a modest, heterogeneous effect.
- The verifier evidence supports that: the 2025 LAST ACT trial in HIV-negative adults, stratified by LTA4H genotype, did not establish non-inferiority or superiority of placebo in CC/CT-genotype adults. Pooled analysis supports only a "modest" survival benefit.
- Adoption of a modestly effective drug is evidence that the class can produce a usable result. It is not evidence that a given trial reaches a ~10% mortality reduction (the Advocate's concession 3 acknowledges this bears on the conditional effect).

> The Advocate claims: the vitamin D null is on time to conversion, not overall conversion (OR 1.22, 1.04–1.43).

Response:
- This is accurate, and the critique cited it as a counterweight.
- But the OR lower bound is 1.04, so the result is marginal.
- The null endpoint, time to conversion, is the one closest to "faster clearance" in the BOTEC's premise.
- Whether the overall-conversion result translated into practice change is not in the evidence package. I cannot ground it either way.

> The Advocate claims: the endpoints and populations differ (meningitis mortality, culture conversion), so transfer is weak.

Response:
- **Agreed, transfer is imperfect.** But a mismatch weakens the inference without reversing its direction. The Advocate offers no alternative TB reference class showing a rate above 0.26.
- The critique's mismatch concession was a disclosure of its limits. It does not turn the generic prior into the right one.

> The Advocate claims: regimen-shortening trials are non-inferiority designs, so they are not informative here.

Response:
- **Partly conceded.** The success criterion differs. The verifier did not verify these trials; they remain UNVERIFIABLE, not REJECTED. The Advocate is relying on the same recollection.
- Conditional on the Advocate's own recollection (three failures, REMoxTB/RIFAQUIN/OFLOTUB, and one success, Study 31), the empirical rate is 1/4 = 0.25.
  - With n=4 this is very imprecise.
  - It still lands at the Advocate's own central value.
  - It does not support 0.40.

**RESPONSE TO "MAGNITUDE CHALLENGE":**
- **Concede:** the threshold arithmetic is correct. SROI is linear in p, and the bar is crossed at p ≈ 0.26.
- **The minimum defensible impact is not trivial.**
  - The Advocate's own "reasonable" range of 0.25–0.30 maps to ~1,909–2,291x. This is a range centered on the bar, not safely above it.
  - The baseline margin is 3,055 / 2,000 ≈ 1.53×. A downward shift in p_success of about 35% flips the conclusion.
  - The Advocate's concession 4 acknowledges the critique is "decision-relevant in the narrow sense that the margin is thin."
  - For a go/no-go decision against a bar, a thin margin with no documented basis for the key parameter is the case where the critique matters.
- **The Advocate's own prior for the "weaker candidate" class (0.17) is below the bar.** The disagreement is whether a positive Phase IIa/b earns an uplift to above 0.26. That uplift is asserted, not shown.
- **Implied stage probabilities:** 0.40/0.58 ≈ 0.69 means a roughly two-in-three chance that a dose-optimization trial succeeds. That is high against a TB record where, by the verifier evidence, adjunctive trials are mixed to modest. Neither side can ground the number, but the Advocate has not shown 0.69 is plausible.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: the BOTEC omits morbidity DALYs, post-treatment mortality, transmission and diagnostic value, which could raise SROI, especially in lower-p scenarios.

Response:
- **These channels are implicit zeros, so they offset nothing in the model as it stands.** An unquantified omission does not neutralize a quantified sensitivity.
- **The claim that they "matter most in lower-p scenarios" is unsupported.**
  - Morbidity, transmission and post-treatment mortality benefits are realized only if the drug works.
  - They should therefore be multiplied by p_success like the mortality benefit and shrink with it.
  - If so, adding them raises the baseline but does not rescue the low-p case proportionally.
  - If the Advocate thinks they are not gated by p, that needs to be shown.
- **The Advocate gives no magnitude for these channels.** I cannot ground one either; this is an open question, not an offset.
- **The critique's counterweights (vitamin D OR 1.22, dexamethasone benefit) are already in the critique.** They do not offset it further.
- **The "definition of success" point cuts against itself.** If success means a weaker surrogate or morbidity endpoint, p_success rises, but the realized effect conditional on success falls.
  - The Advocate's concession 3 already grants that dexamethasone's modest effect bears on `relative_reduction`.
  - A looser success definition would worsen the 10% conditional-effect assumption, so it is not a free offset.

**KEY UNRESOLVED QUESTIONS:**
- What is the correct reference class for a Phase IIc dose-optimization trial of a host-directed agent with positive Phase IIa/b human data? Neither side has a grounded denominator.
- Were the 4-month fluoroquinolone trials (REMoxTB, RIFAQUIN, OFLOTUB) preceded by positive Phase II culture-conversion signals, and did Study 31 succeed (Dorman, NEJM 2021)? If so, they are the most relevant TB Phase II→III cases. Both sides are recalling, and the verifier did not check them.
- Are the omitted benefit channels (morbidity, transmission, post-treatment mortality) gated by p_success? If so, they raise the baseline but not the low-p case in proportion.
- What does CG's "success" mean (mortality, surrogate, or guideline adoption)? p_success and the conditional effect size both depend on it.
- Can CG document how 0.40 was derived? Until then the 0.40 versus 0.25 disagreement cannot be settled on the evidence available.

### Judge Audit
Surviving strength: moderate
Justification: Both sides produced sound syntheses: the Advocate's threshold at p≈0.26 and the Challenger's ~35% margin. The Advocate made substantial concessions that 0.40 is undocumented and likely generous relative to generic base rates. The Challenger, in turn, conceded that the critique's specific class rate and p=0.15 are ungrounded. What survives is the critique's direction and decision-relevance (thin margin, undocumented key parameter), not its magnitude. Both sides' weaker moves (the 1/4 = 0.25 pseudo-derivation, the vitamin D category swap, the speculative and then mis-rebutted omitted-channel argument) mean the debate did not settle where p actually lies within 0.17–0.40.
Recommended action: 2. SPECIFIC INVESTIGATION:
   - **What can be concluded now:** the critique's quantitative claim (p ≈ 0.15, ~38% of base case) should be dropped. The underlying concern stands: 0.40 is undocumented and a revision to ~0.25 would put SROI at the bar.

   Four targeted checks would move the answer, all feasible with existing tooling:
   - (a) **Verify the BIO/Informa/QLS 2011–2020 transition rates.** Include the infectious-disease-specific and, if relevant, repurposed-drug Phase II→III and Phase III→approval rates, to replace the recalled ~0.29/~0.58 anchors.
   - (b) **Ask for or locate CG's derivation of 0.40 and its definition of "success."** The definition could be a positive trial, guideline adoption, or a mortality endpoint.
   - (c) **Verify the TB regimen trials.** Check REMoxTB, RIFAQUIN, OFLOTUB and Study 31/A5349 outcomes, and whether each was preceded by positive Phase IIb culture-conversion data. This determines whether they form a valid "conditional on positive prior signal" reference class.
   - (d) **Quantify the omitted channels.** Make at least a rough estimate for morbidity and transmission as p-gated multipliers on benefit, and recompute the threshold p.

   If (a) and (b) show the 0.40 has no basis beyond the generic rate, revise p_success toward ~0.25–0.30 and treat the intervention as marginal against the bar.
Action feasibility: requires_specified_evidence
Advocate failures: ["sound_synthesis_noted: The threshold arithmetic is correct and fully shown. SROI is linear in p, so the 2,000x bar is crossed at p ≈ 0.40 × 2000/3055 ≈ 0.26. That gives p=0.25 → ~1,909x and p=0.30 → ~2,291x. This calculation reframed the debate: decision-relevance does not depend on the critique's weakest number (0.15). It depends on whether p falls below ~0.26.", 'sound_synthesis_noted: The stage decomposition (0.40/0.58 ≈ 0.69 implied Phase IIc success; generic joint ≈ 0.17) uses recalled BIO/Informa/QLS rates. The Advocate explicitly flags these as recalled and unverified, and frames them conditionally. That is legitimate conditional analysis, not fabrication.', 'call_to_ignorance: The omitted channels (morbidity DALYs, post-treatment mortality, transmission, diagnostic value) "could raise SROI." No magnitude is offered. Offering an unquantified possibility as an offset against a quantified sensitivity fills an evidence gap with speculation.', 'false_definitiveness: The claim that the omitted channels "matter most in exactly the lower-p scenarios" is asserted with no mechanism. If these channels are gated by p_success, as the Challenger argues, they scale with p. They then lower the threshold p by a fixed proportion and do not matter especially at low p.', 'strawmanning: The Advocate says counting ACT HIV as "a second class failure double-counts one drug that did reach practice." This is mild. The critique did not claim dexamethasone failed; it reported one null (HIV+) and one modest positive (HIV−). In a trial-level reference class, two trials in different populations are two legitimate data points. The double-counting objection rebuts a framing the critique did not use.']
Challenger failures: ['sound_synthesis_noted: The margin calculation is correct. 3,055/2,000 ≈ 1.53×, so a ~35% downward revision of p_success flips the conclusion (1 − 1/1.53 ≈ 0.35). This is a sound, shown derivation that correctly reframes the stakes.', 'sound_synthesis_noted: The "0.40 is ~2.4× the generic joint of ~0.17" point is explicitly conditional on the Advocate\'s recalled inputs, and the Challenger flags it as such. This is legitimate conditional engagement. The burden argument is fair: an uplift from ~0.17 to 0.40 for a positive IIa/b signal needs documentation that CG has not provided.', 'unsupported_estimate_pseudo: The Challenger computes "1/4 = 0.25" from REMoxTB/RIFAQUIN/OFLOTUB vs. Study 31, saying it "lands at the Advocate\'s own central value." The chain has clear gaps:', 'strawmanning: The Advocate argued that the critique\'s examples were not conditioned on a prior positive Phase IIa/b signal. The Challenger responds that vitamin D "found no shortening of time to conversion… the same kind of signal the BOTEC conditions on." This is a category swap: it is about the trial\'s endpoint, not about whether vitamin D had a positive prior human signal before the trial. It does not show a failure conditional on a positive prior signal, which was the Advocate\'s point.', 'false_definitiveness: The Challenger says the omitted channels, if gated by p, "raise the baseline but do not rescue the low-p case proportionally." Under the linear model both sides accepted, p-gated channels scale benefit by a constant factor. They therefore lower the threshold p proportionally. For example, a +20% benefit would move the bar from ~0.26 to ~0.22.', 'strawmanning (minor): The Challenger calls the 0.17 figure "the Advocate\'s own prior for the \'weaker candidate\' class." The Advocate presented it as a generic all-Phase-II benchmark it argued was too low for this drug, not as its own prior.']
Debate resolved: The debate settled three points:
1. **The critique's quantified headline does not survive.** The 10–20% class rate and the p=0.15 / "38% of base case" result rest on an ungrounded, selected list. Both sides accept this.
2. **The decision-relevant threshold is p ≈ 0.26.** This is shared arithmetic.
3. **The 0.40 is undocumented and sits close enough to the threshold to matter.** It has no stated reference class, and both sides' "reasonable" range (0.25–0.30) straddles the bar.

The debate also narrowed the real dispute to one question: does a positive Phase IIa/b human signal justify an uplift from a generic ~0.17 benchmark to above ~0.26?
Debate unresolved: - **Size of the positive-IIa/b uplift.** Neither side grounded how much a positive IIa/b signal should raise p_success above the generic prior, and the generic anchor itself rests on unverified recall.
- **Effect of the omitted benefit channels on the threshold.** If they are gated by p_success, they lower the threshold proportionally. Both sides mis-stated this, and neither quantified it.
- **What CG means by "success."** The debate surfaced a trade-off: a looser definition raises p_success but lowers the conditional effect. It did not resolve what "success" means in this CEA.

--- Critique: "Success" probably means a surrogate or composite endpoint, but the model needs a 10% mortality reduction, so P(adopted AND 10% mortality benefit) < P(trials succeed) ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: "Success" probably means a surrogate or composite endpoint, but the model needs a 10% mortality reduction

EXISTING COVERAGE:
- The model already conditions the 10% on a positive result. The BOTEC says "A positive result is assumed to cut that by 10% relative." The 40% then multiplies the whole benefit.
- The critique's coherent quantity is P(success) × P(adopted | success) × E[RR | success]. The BOTEC contains all three terms, though not under those labels:
  - 40% is P(success).
  - 60% uptake "if it works" is the adoption-given-success term.
  - 10% is E[RR | success].
- So the structure is the one the critique asks for. The dispute is whether 10% is the right conditional value, not whether the terms are separated.
- The Phase IIc trial is described as testing dosing "for survival, infection clearance and lung damage." Survival is named as a target endpoint, which is some evidence that "success" is meant to include mortality. The parameter map notes the definition of success is not stated, so this is suggestive, not conclusive.
- The model values only mortality (see "only mortality is valued" in the parameter map). Lung damage, morbidity, post-treatment mortality and transmission are implicit zeros. If adoption occurs on a surrogate, the surrogate-linked value is uncounted. This partly offsets the lower mortality effect (see Offsetting Factors).

EVIDENCE WEAKNESSES:
1. The Verifier's own flag is that the critique "does not apply in high-mortality populations" and that CG's definition of success "needs checking." The critique is explicitly conditional on a low-mortality DS-TB population, and the Quantifier says it could not see CG's model.
2. The 0.5–2% mortality figures (Study 31, TRUNCATE-TB) come from enrolled trial populations. These are typically screened and selected, and often exclude the sickest patients. The model's 6% is a treated-cohort figure for drug-susceptible patients. The two are not the same population. A Phase III could be run in higher-mortality settings, such as high-HIV-burden or programmatic cohorts. Whether CG intends that is unknown, but the critique's power argument does not apply to it.
3. The sample-size arithmetic changes at CG's stated baseline. Using the standard two-proportion formula, which reproduces the Verifier's ~36,000 per arm at 4%:
   - n ≈ (1.96 + 0.84)² × [p₁(1−p₁) + p₂(1−p₂)] / (p₁−p₂)².
   - At 6% vs 5.4% (10% RRR): 7.84 × 0.1075 / 0.000036 ≈ 23,400 per arm, or about 47,000 total.
   - This is roughly 35% smaller per arm than at 4%. It is still a very large trial, so I do not claim the concern vanishes.
4. If a Phase III were powered for a 10% mortality reduction, then "success" means the observed effect cleared the significance threshold. Conditional on success, the point estimate would be at or above roughly the powered effect. In that scenario E[RR | success] is not below 10% (apart from winner's-curse bias in the other direction). The critique's 5–7% figure applies only to the surrogate-endpoint scenario, so it is not a general result.
5. The 5–7% range is flagged UNGROUNDED by the Verifier. It is a placeholder with no derivation from a surrogate-to-mortality relationship.

MAGNITUDE CHALLENGE:
- The Quantifier's sensitivity run shows that at the 7% central value, SROI falls 30% to about 2,138x, still above the ~2,000x bar. Only the 5% low case (about 1,527x, −50%) crosses the bar.
- Because 7% is itself ungrounded, the only grounded statement is that the result is sensitive to this parameter. The data do not show that it fails.
- The sensitivity is mechanical. SROI scales linearly in the relative reduction, so any 30% haircut gives a 30% change. It carries no information about whether the haircut is warranted.
- The "compounding with p_success revision" is a separate, unquantified step. The 40% is also ungrounded in the package, so I cannot say whether compounding would be large or small.
- A reduction of ~10% on top of ~6% baseline mortality is a modest effect size (0.6 percentage points absolute). That is not an implausible assumption for an adjunct, and it is conditional on success.

OFFSETTING FACTORS:
1. The surrogate path has benefits the model excludes. If success is defined by lung damage or infection clearance, then adoption on that basis is likely to bring lung-function and morbidity gains, and possibly reduced post-treatment mortality. The parameter map notes the "main value" might lie in these channels and that this "could make the estimate robust even if... a small on-treatment mortality effect" is found. A lower mortality effect with a non-zero omitted morbidity benefit makes the net impact on SROI less than the Quantifier's pure −30%. I cannot quantify this offset from the evidence package.
2. The cost side may also be conservative. A $7M all-in cost with a mortality-powered Phase III would be in tension with the 47,000-patient arithmetic above. That tension is a separate matter. It does support the critique's inference that the model's Phase III may be surrogate-based, so I treat it as a concession rather than an offset.

OVERALL ASSESSMENT:
Partial defense.
- The critique's own framing is that the effect is "large if low-mortality, but conditional on that." The model's 6% baseline and its "survival" endpoint language point toward a population where a mortality finding is more plausible than in Study 31 or TRUNCATE-TB.
- The structural point is largely accommodated by the BOTEC's three-term structure.
- The remaining vulnerability is real: the BOTEC does not define "success," and the 10% is not derived from surrogate data.
- The central estimate remains above the bar (2,138x vs 2,000x) under the Quantifier's own central case. The defense is weakened because that margin is thin.

CONCESSIONS:
- The BOTEC never defines "success." If success is a surrogate or composite endpoint, then E[RR | success] is not necessarily 10%, and the 40% and 10% may not be jointly coherent.
- The model should state P(adopted AND mortality benefit) separately from P(trials succeed). The current presentation hides this.
- The $7M all-in cost sits awkwardly with a mortality-powered Phase III even at 6% baseline mortality, as the arithmetic above suggests.
- The 10% has no stated derivation from the prior trial's surrogate effects (per the parameter map).
- A value of 5% would put SROI below the bar. I cannot rule that out from the evidence, only argue that it is ungrounded.
```

### Challenger
REBUTTAL: "Success" probably means a surrogate or composite endpoint, but the model needs a 10% mortality reduction

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the BOTEC already has the three terms the critique asks for (40% = P(success), 60% = adoption given success, 10% = E[RR | success]), so the structure is right and only the value of the 10% is in dispute.

1. Having three multiplied terms does not make them coherent.
   - The critique's point is that the terms must share one definition of "success."
   - The Advocate concedes the BOTEC never defines success. It also concedes that "the 40% and 10% may not be jointly coherent."
   - So the structure exists, but the conditioning that makes it valid is unverified. That is the critique, not a rebuttal of it.

2. The "survival" language does not define Phase III success.
   - The Advocate cites the Phase IIc description ("survival, infection clearance and lung damage").
   - That describes a dosing trial. It does not say what the 40% Phase III success probability refers to.
   - The same sentence names two non-mortality endpoints (clearance, lung damage). A composite or surrogate reading is therefore at least as consistent with the text as a mortality reading.

3. The Advocate's strongest move is a dilemma, and it cuts for the critique.
   - Branch A: Phase III is mortality-powered. Then the Advocate's own arithmetic gives about 47,000 patients in total.
   - Dividing the $7M all-in cost by 47,000 gives about $149 per patient. I cannot ground a benchmark for TB trial cost per patient, so treat my view that this is implausibly low as an uninformed prior. The Advocate itself calls the tension "awkward" and concedes it.
   - Branch B: Phase III is surrogate- or composite-powered. Then E[RR | success] is not 10%, and the Advocate offers no derivation for what it is.
   - Either the cost or the benefit parameter is wrong. The BOTEC cannot be right on both.

4. The Advocate's point 4 contains an error.
   - It says that if the trial is powered for a 10% mortality reduction, then conditional on success "the point estimate would be at or above roughly the powered effect."
   - Using the Advocate's own formula, power 80% corresponds to z = 0.84 and the significance threshold to z = 1.96. The minimum observed effect that clears significance is therefore 1.96/(1.96+0.84) = 70% of the powered effect.
   - For a powered 10% RRR, the minimum observed effect that counts as "success" is about 7%.
   - The observed effect can be below 10% and still count as success. The point estimate is also not the same as the true effect. Even in Branch A, "success" does not guarantee 10%.
   - I concede that E[true effect | success] depends on the prior, so I do not claim the haircut is established. The Advocate's claim that it is "not below 10%" is not established either.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the critique is conditional on a low-mortality DS-TB population, the trial populations (0.5–2% mortality) are selected and not the 6% treated-cohort population, and a Phase III could run in higher-mortality settings.

1. I concede the critique is conditional. The Verifier flagged that it "does not apply in high-mortality populations" and that CG's definition needs checking. That status is UNVERIFIABLE, not REJECTED.

2. The Advocate's population argument works against its own position.
   - It describes the 6% figure as being for drug-susceptible patients. That is the same DS-TB population the critique addresses.
   - To escape the power problem, the Advocate has to posit a different trial population (high-HIV, programmatic cohorts, TBM).
   - Nothing in the evidence package says CG's Phase III is in such a population. The Advocate concedes "whether CG intends that is unknown."
   - Treating an unknown as a defense is the same call-to-ignorance move in reverse. The dexamethasone-in-TBM evidence shows such trials are feasible. It does not show this one is that trial.

3. The Advocate's recomputation to 23,400 per arm is fair, and I accept it. The Advocate itself says it "is still a very large trial." The correction narrows the gap but does not remove the cost/design tension. Its own figure is in the same regime as the Verifier's 36,000.

4. The Advocate is right that 5–7% is UNGROUNDED. But the Advocate's own arithmetic (point 4 above) puts a grounded value near 7% as the minimum observed effect at which a 10%-powered trial would declare success. That is a derived value, not a placeholder.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

1. Breakeven is close to the Quantifier's central case.
   - Baseline SROI is about 3,055x at 10%. SROI is linear in the relative reduction.
   - Staying at or above the ~2,000x bar requires E[RR] ≥ 10% × 2000/3054.86 ≈ 6.55%.
   - The margin is therefore 3.45 percentage points of RRR, or about 35% of the benefit.
   - The Advocate's observation that the 7% central case clears the bar (2,138x) is true. But it clears by only about 7%, and the critique's mechanism is one of several that can eat this margin.

2. The Advocate calls the linear sensitivity "mechanical." That is correct but irrelevant to whether the bar is crossed. The only question is where the true E[RR | success] sits relative to 6.55%.

3. The compounding is separate and not quantified by anyone.
   - The critique says that if success requires a real 10% mortality effect, the true P(success) is lower than 40%.
   - Any further reduction in P(success) or uptake draws on the same ~35% margin.
   - I cannot ground a revised P(success). I flag only that the margin is exposed on two parameters at once.

4. The "modest 0.6 percentage point absolute effect" argument does not address the issue.
   - The question is not whether 10% is a plausible effect for an adjunct.
   - It is whether the trial that produces "success" is one whose success implies that effect.

5. Minimum plausible impact:
   - In Branch A (mortality-powered, high enough baseline), the haircut is near zero, and I concede that.
   - In Branch B, the haircut is unbounded below. Adoption on a surrogate with no mortality effect gives P(adopted AND benefit) < P(success).

**RESPONSE TO "OFFSETTING FACTORS":**

1. The morbidity/lung-function offset is real in direction but not in the model.
   - The Advocate admits "I cannot quantify this offset from the evidence package."
   - The model values only mortality. An offset that GiveWell's CEA assigns zero value cannot protect the stated SROI.
   - If the offset were valued, it would be a new input with its own uncertainty, not an existing cushion.

2. The offset is also not independent of the problem. It arises only on the surrogate path, which is the very path where the 10% mortality effect is least supported. It does not offset the specific mismatch the critique identifies.

3. The cost side moves the same way as the critique, not against it.
   - The Advocate concedes that if Phase III is mortality-powered, the $7M cost is too low.
   - A higher cost lowers SROI and would compound with the effect-size haircut in the surrogate case.
   - The Advocate classifies this as a concession, not an offset, and I agree.

**KEY UNRESOLVED QUESTIONS:**
- What endpoint defines Phase III "success" in CG's 40%? Is it mortality, a composite, or a surrogate such as culture conversion or lung damage?
- Is the 10% an assumed relative mortality reduction or a value derived from prior-trial surrogate effects? The parameter map says no derivation is stated.
- If the Phase III is mortality-powered, is the $7M cost consistent with roughly 47,000 patients, or is the cost understated?
- Is the target population DS-TB (about 6% treated-cohort mortality) or a higher-mortality group? That determines which side of the dilemma applies.
- What is E[RR | surrogate success, adoption]? Breakeven is about 6.55%, so even a modest gap between surrogate and mortality effects crosses the bar.

### Judge Audit
Surviving strength: moderate
Justification: - The critique's structural point survived. The Advocate conceded the undefined success criterion, the joint-coherence problem, and the cost/design tension, and the Challenger corrected the Advocate's main analytic counter (point #4).
- However, the quantitative claim is not established. The 5–7% remains ungrounded, and the Challenger's attempt to ground it via the significance threshold conflates observed-threshold with expected true effect.
- The breakeven of about 6.55% narrows the question usefully. Whether the critique bites depends on facts neither side had.
Recommended action: 2. SPECIFIC INVESTIGATION, with a partial conclusion available now.

**Conclude now (moderate confidence):**
- The model should report P(trial success) and E[mortality RR | success] under one explicit endpoint definition.
- It should flag that the result crosses the bar if the conditional mortality effect falls below about 6.5%.
- The $7M cost is likely inconsistent with a mortality-powered DS-TB Phase III.

**Investigation:** Obtain from CG, or from the BOTEC's source documentation:
1. The planned Phase III primary endpoint. Is it mortality, a composite including death, or a surrogate such as culture conversion or lung damage?
2. The target population and its expected mortality.
3. The cost breakdown behind the $7M.

This is feasible by direct inquiry. If the endpoint is surrogate-only, the next step is a sensitivity analysis over E[RR] from 0–10%, plus a literature search for surrogate-to-mortality concordance in TB adjunct or host-directed therapy trials. Such evidence is likely thin, so treat the result as a prior-driven range.
Action feasibility: requires_specified_evidence
Advocate failures: ['unsupported_estimate_pseudo: Evidence Weakness #4 says that if Phase III is powered for a 10% mortality reduction, then "conditional on success, the point estimate would be at or above roughly the powered effect… E[RR | success] is not below 10%." This does not follow from the power framework the Advocate itself used.', "call_to_ignorance: A Phase III could be run in higher-mortality settings, such as high-HIV-burden or programmatic cohorts… the critique's power argument does not apply to it.", "sound_synthesis_noted: The recomputation at CG's 6% baseline is sound.", 'sound_synthesis_noted: Calling the linear SROI sensitivity "mechanical," carrying no information about whether the haircut is warranted, is a correct and well-scoped point.']
Challenger failures: ['unsupported_estimate_pseudo: Under Evidence Weaknesses #4, the Challenger says "the Advocate\'s own arithmetic… puts a grounded value near 7%… That is a derived value, not a placeholder.', 'false_definitiveness: The dilemma\'s Branch B states "E[RR | success] is not 10%," and the conclusion says "Either the cost or the benefit parameter is wrong. The BOTEC cannot be right on both.', 'call_to_ignorance: In Branch B, the haircut is unbounded below.', 'sound_synthesis_noted: The breakeven calculation is correct and grounded.', "sound_synthesis_noted: The correction of the Advocate's point #4 is correct (1.96/2.80 ≈ 0.70)."]
Debate resolved: The debate established the following:
- The BOTEC has the right three-term structure, but "success" is undefined, so the 40% and 10% are not demonstrably coherent. The Advocate conceded this.
- A mortality-powered Phase III at CG's 6% baseline would need about 47,000 patients, which is in tension with the $7M cost.
- The SROI bar is crossed only if E[RR | success] falls below about 6.55%, meaning a haircut of about 35% or more.
- Excluded morbidity benefits do not cushion the *stated* SROI, because the model values only mortality.
Debate unresolved: - Which endpoint and population define CG's Phase III "success." This determines which branch applies.
- Whether E[true mortality RR | surrogate or composite success] sits above or below about 6.55%. Neither side offered grounded evidence on this. The Challenger's "derived 7%" does not address it.

--- Critique: Baseline year is stale and the 5.5M figure is sensitive to it ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: Baseline year is stale and the 5.5M figure is sensitive to it
```

**EXISTING COVERAGE:**
1. CG's model is explicitly a rounded BOTEC ("about 5.5 million"). The baseline is an input to an 8-year projection, not a measured quantity. The stated structure (2% annual decline, constant treated share, 96% drug-susceptible) is built to be re-anchored, and re-anchoring is a one-line change.
2. The critique's own sensitivity run shows this is a one-directional, bounded effect. The SROI moves from ~3,055 to ~3,360–3,388 (+10% to +10.9%). The critique's text says it is "below the ±25% materiality bar."
3. The Materiality field says "material" while the Mechanism text says "non-material alone." These contradict each other. Under the stated bar (>~25% change, or crossing ~2,000x), this critique does not qualify on its own. The "stacks with Critique 2" argument belongs to the Synthesizer and is not a property of this critique.

**EVIDENCE WEAKNESSES:**
1. **The 8.3M figure is hindsight.**
   - The BOTEC was published in May 2025. The critique cites the 2025 WHO report for the 2024 figure. From memory, that report came out in late 2025, after CG's publication. I cannot ground the exact release dates; treat them as an unverified recollection.
   - If that is right, "a 2024 baseline is clearly available" is not a fair test of CG's process. A 2023 baseline of ~8.2M was plausibly available. Even then, the justified update is ~9%, not an inference from 2024.
2. **The 7.5M anchor is inferred, not stated.**
   - The CG text never says which year or figure underlies 5.5M. The critique assumes 7.5M. This is a reconstruction.
   - Check: 7.5M × 0.98^8 × 0.96 = 6.13M, which is not 5.5M. Multiplying by ~0.90 (a pediatric exclusion of ~10–12%, as the parameter map notes) gives ~5.5M.
   - So the critique's scaling is plausible, but the exact percentage depends on a reconstruction the Verifier could not confirm from CG's text.
3. **Notifications are not the model's stated variable.**
   - The model says "current new TB cases" and a "constant share of cases being treated." The 2024 notification figure (8.3M) combines a case count with a detection rate (notifications = 78% of estimated incidence, per the critique).
   - The critique's own evidence says incidence was flat to slightly down while notifications rose. That means the notification rise reflects a rising treated share, not more cases.
   - CG's model treats the treated share as constant. Re-anchoring on a higher notification number while keeping "constant share" going forward is a modeling choice. It is not an obvious correction, because the 2022→2024 rise may be partly post-COVID catch-up.
   - I cannot ground how much of the rise is catch-up. If the claim is true, the +10% overstates a persistent baseline. Treat it as a conditional possibility, not a finding.

**MAGNITUDE CHALLENGE:**
1. **The decline period is not re-timed.** The critique rescales the baseline but keeps CG's 8-year decline.
   - If the anchor moves from 2022 to 2024 while the Phase III end date stays fixed in calendar time, the decline period lengthens by a year (about 9 years from 2024).
   - Derivation: 8.3/7.5 = 1.107. Multiplying by 0.98 for the extra year of decline gives 1.107 × 0.98 ≈ 1.085, or about +8.5% rather than +10.7%.
   - This holds only if the end date is fixed at ~2033. CG says "8 years after the grant," so I treat it as conditional.
2. **The critique's range has a floor of zero but a central value near the top.** The Quantifier's "low" is 0% and "high" is +10.9%. The "central" is +10.0%, almost the high. The critique does not justify placing the central estimate near the top of its own range.
3. **The effect is small relative to the precision of the inputs.** CG states 5.5M to two significant figures from rounded inputs (2% decline, 96%, an assumed 8 years). A ~9% shift sits near the resolution of a BOTEC input.

**OFFSETTING FACTORS:**
1. **Pediatric exclusion.** The parameter map flags "no account of whether 'adult' excludes ~10–12% pediatric cases consistently." If 5.5M includes children but the 60% uptake applies to "adult patients," the eligible adult pool is overstated by about 10–12%. That would roughly cancel the critique's +10%.
   - My reconstruction above suggests the 5.5M may already include a ~10% exclusion. In that case the offset is embedded and the critique's +10% stands.
   - I cannot tell which holds from CG's text. This is an unresolved ambiguity, not a decided offset.
2. **Funding-environment risk.** Notifications depend on detection and funding, and 2025 funding disruptions could lower them. I cannot ground this. Treat it as an uninformed prior, not evidence.

**OVERALL ASSESSMENT:** Partial defense.
- The critique is directionally right. A 2023-or-later anchor would raise the estimate by about 8–11%.
- The critique's own text says it is non-material alone.
- The 2024 figure was likely unavailable at publication.
- The exact anchor is a reconstruction.
- The decline-period timing trims the effect to ~8.5%.
- The pediatric-share question could offset it.
- I rate this "Partial" rather than "Strong" because I cannot rebut the direction or rough size of the effect.

**CONCESSIONS:**
1. CG's baseline year is probably a year or two behind the best available data at publication, and a refresh would move the estimate up by roughly 8–11%.
2. If the 7.5M anchor is wrong and the real anchor is lower, the true correction could be larger than the critique states. For example, 5.5M ÷ (0.98^8 × 0.96) ≈ 6.7M, which would imply a +23% move to 8.3M. This ambiguity cuts against CG and I cannot resolve it from the text.
3. Rising notifications alongside flat incidence does mean the "constant share treated" assumption is slightly stale. That supports an upward revision.
4. CG gives no stated derivation of 5.5M from a named baseline year. A reader cannot audit this input. That is a legitimate transparency criticism even though its value impact is small.

### Challenger
REBUTTAL: Baseline year is stale and the 5.5M figure is sensitive to it

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: CG's 5.5M is a rounded BOTEC built to be re-anchored, the effect is bounded at about +10%, and the critique contradicts itself on materiality, so it fails the ±25% bar on its own.

- **Re-anchorability is not coverage.**
  - That re-anchoring is a one-line change shows the fix is cheap. It does not show the current input is right.
  - Nothing in CG's text applies a refresh. The Advocate's own Concession 1 says the baseline is "probably a year or two behind."
- **Materiality label.**
  - I concede the "material" field conflicts with the "non-material alone (+9–11%)" text. The Judge should treat the +9–11% as a sub-threshold, upward correction, not a bar-crossing one.
  - On stacking, the Advocate is right that it is a Synthesizer-level argument. The critique's own contribution is a small, one-directional, easily verified correction.
- **Bounded is not the same as symmetric.**
  - The Advocate's own concessions put the plausible range at +8.5% to +23%, with downside only through a conditional offset (addressed below).

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: (1) 8.3M for 2024 is hindsight, since the 2025 WHO report likely postdates CG's May 2025 publication. (2) The 7.5M anchor is a reconstruction. (3) Notifications aren't the model's variable, and the rise may be post-COVID catch-up.

1. **Hindsight.**
   - I concede the 2024 figure was probably not available in May 2025. The Advocate flags the release date as unverified recollection, and the verifier's package gives no release date either.
   - The critique's central claim only needs a more recent baseline than 7.5M. The Advocate itself says a 2023 figure of about 8.2M was "plausibly available."
   - From my recollection of the 2024 WHO report, which I cannot ground here, it reported about 8.2M notifications for 2023. That figure was out about seven months before CG's publication.
   - Moving the anchor from 7.5M to 8.2M gives 8.2/7.5 = 1.093, or +9.3%. The hindsight objection therefore trims the correction by about 1.5 points (from +10.9% to +9.3%). It does not remove it.
2. **The 7.5M anchor is inferred.**
   - The Advocate's own check supports the critique's reconstruction. 7.5M × 0.98^8 × 0.96 = 6.13M, and 5.5/6.13 ≈ 0.90.
   - That 0.90 matches the 10–12% pediatric exclusion the parameter map flags. It is the only reconstruction in this debate that reproduces 5.5M from a recognizable notification figure and CG's stated parameters.
   - If the reconstruction is wrong, the Advocate's Concession 2 shows the error cuts toward a larger correction: 5.5/(0.98^8 × 0.96) ≈ 6.7M, and 8.3/6.7 ≈ +23%.
   - I cannot ground any alternative anchor of about 6.7M as a published WHO figure. Treat that as an open question.
3. **Notifications versus cases.**
   - The model's eligible pool is people who are on TB treatment, because statins are co-administered with therapy. Notified patients are the treated population, so notifications are a more direct measure of the eligible pool than incidence.
   - The 7.5M anchor was already a notification figure. Updating it to 8.3M is like-for-like. Switching to incidence would be the inconsistent move.
   - The Advocate says the treated share rose, which breaks CG's "constant share." That supports an upward revision, as the Advocate concedes in Concession 3.
4. **Catch-up.**
   - The Advocate admits it cannot ground the catch-up magnitude. I cannot either, so this is a conditional.
   - Two points constrain it:
     - The verifier's figures imply 8.3M/0.78 ≈ 10.6M incident cases, so about 22% remain undetected. Catch-up has headroom and has not saturated.
     - From my ungrounded recollection of 8.2M for 2023, the 2023→2024 rise is only about +1%. That looks like a plateau at a higher level, not a transient spike.
   - If the plateau reading is right, the new baseline persists. If catch-up were purely transient, notifications should be falling back, and the verifier evidence reports no such fall.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: re-timing the decline gives about +8.5%, the critique's central estimate sits at the top of its range, and a 9% shift is within BOTEC noise.

1. **Re-timing.**
   - I accept the arithmetic: 1.107 × 0.98 ≈ 1.085. The Advocate marks it as conditional on a calendar-fixed end date, and I agree it is conditional.
   - The defensible floor is therefore about +8.5%, not zero. That is still a clear upward correction.
2. **Central near the top of the range.**
   - The "low = 0%" is CG's own number, meaning no update. It is not a candidate for the corrected value when newer data exist.
   - The central of 6.05M is the midpoint of the critique's stated 6.0–6.1M re-anchored estimate. It is not the midpoint of 0 to +10.9%, so the objection compares the wrong things.
3. **BOTEC noise.**
   - Rounding 5.5M to two significant figures implies a resolution of about ±0.05/5.5 ≈ ±0.9%. A 9–11% shift is roughly ten times that.
   - The decline rate and the 96% drug-susceptible share are separate modelling assumptions. They are not random noise around the baseline, so they do not mask a systematic one-directional stale-data bias.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: a pediatric exclusion could roughly cancel the +10%, and funding disruption could lower notifications.

1. **Pediatric offset.** The Advocate's two branches do not combine into a net cancellation.
   - **Branch A:** a ~10% pediatric exclusion is already embedded in 5.5M. Then there is nothing left to offset, and the +9–11% stands. The Advocate says so.
   - **Branch B:** 5.5M has no exclusion. Then the 7.5M anchor does not reproduce 5.5M, so the true anchor is lower (about 6.7M). The correction grows to about +23%, and a ~10–12% pediatric deduction would only bring it back to about +10–11%.
   - In neither branch is the net effect below the critique's range. The offset only matters if the anchor is lower than 7.5M, and that case enlarges the gross correction before any offset.
2. **Funding risk.**
   - The Advocate labels this an uninformed prior with no grounding. It is not a quantified offset and is not in CG's model.
   - It also applies to any baseline year equally, so it does not favor the stale one.

**KEY UNRESOLVED QUESTIONS:**
- Which year and figure underlie CG's 5.5M? The critique's 7.5M plus a ~10% exclusion fits, but CG's text does not confirm it, and a different anchor changes the correction from about +9% to about +23%.
- Does CG's "adult patients" eligibility exclude children? If the exclusion is already embedded, the +9–11% stands. If not, the offset runs through a lower anchor, as above.
- Is the 2022→2024 notification rise persistent or partly transient? The verifier shows notifications at 78% of incidence and flat-to-slightly-down incidence, but not the persistence of the new level.
- Is the 8-year horizon calendar-fixed (about +8.5%) or anchored to the baseline year (about +10–11%)? CG's wording, "8 years after the grant," does not settle this.
- Exact release dates for the WHO reports relative to CG's May 2025 publication are unverified on both sides.

### Judge Audit
Surviving strength: moderate
Justification: - The critique's claim, as written, survived nearly intact. The Advocate conceded direction and rough size (Concessions 1 and 3). Its trims (hindsight, re-timing) only narrow the effect to ~+8.5–9.3%. Its offsets were either disclaimed (funding) or shown by the Challenger's branch analysis not to cancel (pediatric).
- The debate was largely productive, with transparent arithmetic on both sides and few failure modes.
- I do not rate it "strong" for two reasons:
  - The critique itself is sub-threshold and non-material alone.
  - Its exact magnitude rests on an unconfirmed reconstruction of CG's anchor, which neither side could resolve. That reconstruction is also the only route by which the effect becomes material (+23%).
Recommended action: 1. CONCLUDE NOW: Accept the critique as an upward, non-material correction, with moderate-high confidence in direction.
   - **Central value.** Adopt ~+9% (re-anchor on the 2023 figure of 8.2M, available at publication). The plausible band is +8.5% to +11% depending on horizon timing.
   - **Materiality label.** Correct the "material" label to non-material standalone.
   - **Synthesizer handoff.** Pass the ~+9% to the Synthesizer for stacking with Critique 2.
   - **Supplementary check.** Inspect CG's BOTEC spreadsheet or source notes to confirm the baseline year and figure behind 5.5M, and the meaning of the ~0.90 factor. This is feasible with a direct document check.
   - **When the conclusion would change.** Only if the anchor proves to be ~6.7M without a pediatric exclusion. In that case the gross correction approaches +23% and should be re-evaluated against the materiality bar.
Action feasibility: actionable_now
Advocate failures: ['strawmanning: Magnitude Challenge 2 says the critique "does not justify placing the central estimate near the top of its own range" (low 0%, central +10.0%, high +10.9%). The 0% "low" is the no-update case, CG\'s current number. It is not a candidate corrected value, so the central estimate is not meaningfully positioned within a 0–10.9% distribution. The Challenger caught this correctly.', 'call_to_ignorance: Offsetting Factor 2 says "2025 funding disruptions could lower" notifications. The Advocate labels this an "uninformed prior," so it is disclosed. But placing an ungrounded possibility under "Offsetting Factors" still invites it to be weighed as a counterweight. It should have been dropped or listed only as a gap.', 'sound_synthesis_noted: Re-timing derivation: 8.3/7.5 = 1.107, × 0.98 for one extra year of decline ≈ 1.085. This is explicitly conditional on a calendar-fixed end date. It is a clean, transparent adjustment, and the Challenger accepted it.', 'sound_synthesis_noted: Reconstruction check and Concession 2. 7.5M × 0.98⁸ × 0.96 = 6.13M, so a ~0.90 factor is needed to reach 5.5M. The alternative anchor is 5.5/(0.98⁸ × 0.96) ≈ 6.7M, implying +23%. The arithmetic is correct, and the Advocate candidly concedes that the ambiguity cuts against CG.']
Challenger failures: ['unsupported_estimate_pseudo: The Challenger argues "8.3M/0.78 ≈ 10.6M incident cases, so about 22% remain undetected. Catch-up has headroom and has not saturated." The undetected share of current incidence says nothing about whether the 2022–23 backlog of *previously delayed* diagnoses has been exhausted. These are different quantities, and the inference does not follow.', 'misrepresenting_evidence_status: The Challenger twice calls the 2023 ≈ 8.2M figure "my recollection, which I cannot ground here" and "my ungrounded recollection of 8.2M for 2023." The verifier package explicitly VERIFIED 8.2M for 2023 and states that 2024 was "similar to the 8.2 million in 2023.', 'strawmanning: BOTEC noise rebuttal. "Rounding 5.5M to two significant figures implies ... ±0.9%." The Advocate\'s point was about the imprecision of the *inputs* (2% decline, 96%, an assumed 8 years), not about output rounding. The Challenger\'s second sub-point (systematic bias is not masked by other parameters\' uncertainty) does engage the real argument. The first sub-point rebuts a claim not made.', 'sound_synthesis_noted: Pediatric two-branch analysis.', 'sound_synthesis_noted: Hindsight concession quantified. Using a 2023 anchor gives 8.2/7.5 = +9.3%, so the hindsight objection trims the effect by ~1.5 points rather than eliminating it. The central-estimate rebuttal (6.05M is the midpoint of the re-anchored range, not of 0 to +10.9%) is also correct.']
Debate resolved: Both sides agree on the following, conditional on the 7.5M reconstruction (which both sides found the only arithmetic fit):
- **Direction.** Re-anchoring CG's baseline to data available at publication moves eligible_people_at_8y upward.
- **Size.** The move is ~+8.5% to +9.3% using the 2023 figure, or up to ~+11% using 2024. This is below the ±25% bar on its own.
- **Materiality field.** The critique's "material" field is mislabeled.
- **Variable choice.** Notifications are the like-for-like variable for a treated-patient eligible pool.
- **Pediatric offset.** The pediatric offset does not net the correction below that range under either branch.
Debate unresolved: 1. **Which anchor year and figure CG actually used.** This governs whether the correction is ~+9% or as large as ~+23%. The ~0.90 residual factor is unexplained.
2. **Horizon timing.** It is unclear whether the 8-year horizon is calendar-fixed (~+8.5%) or tied to the baseline year (~+10–11%).
3. **Persistence of the new level.** Whether the 2023 level reflects a persistent baseline or residual backlog was only partly addressed. The 2024 plateau is suggestive, and the Challenger's headroom argument does not establish it.

--- Critique: A 2%/yr decline in notified case counts probably contradicts the observed trend; incidence rates fall slowly while counts do not ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: A 2%/yr decline in notified case counts probably contradicts the observed trend

EXISTING COVERAGE:
- CG's 2% decline is applied over 8 years until Phase III completes (report, Benefits §1). It is a forward projection to the time of adoption, not a fit to a historical notification series. Whether it should be exactly 0% or 2% is a judgment about the 2025–2033 trend, which the 2020–2024 data cannot settle.
- The BOTEC states the share treated "stays constant" and uses a deliberately round figure. A 2% decline is a conservative planning assumption. It is not claimed to be an estimate of the notification trend.
- The decline parameter is a modest lever. The Quantifier's own sensitivity run shows that replacing 0.98^8 (≈0.851) with flat (1.0) lifts eligible people from 5.5M to about 6.46M, a +17.5% change in SROI. That is below the ~25% materiality line. It also moves a point estimate that is already above the bar (~3,000x vs ~2,000x) further above it. The upward direction cannot change the funding decision.
- The only sensitivity cases that exceed 25% (+27% at 7.0M eligible) combine the flat-trend assumption with a baseline correction (the ×0.96×0.90 and 8.2M starting point). The Quantifier's own mechanism text says this overlaps with Critique 1. Against this critique alone, the decline assumption contributes roughly +17%, not >25%.

EVIDENCE WEAKNESSES:
- The "roughly flat 2020–2024" claim is vulnerable to COVID distortion. My recollection of WHO Global TB Report figures is about 7.1M notified in 2019, 5.8M in 2020, 6.4M in 2021, 7.5M in 2022 and 8.2M in 2023. This is not in the verifier package, so please treat it as unverified. If it is right, the 2020–2024 window is dominated by a dip and rebound, and the 2023 value may include catch-up of previously undiagnosed backlog. A rebound is not a steady-state level, so using 8.2M as a flat baseline for 8 years plausibly overstates the starting point.
- The cited funding-cut modelling (12–41% more TB episodes among people living with HIV in South Africa, 2025–2035) is adjacent evidence.
  - It covers one country and one subpopulation.
  - It measures incidence, not notifications or treated counts.
  - The critique itself says the notification/detection distinction matters, and funding cuts reduce detection. The same shock that raises true incidence can lower notified counts, which is the quantity that determines treated patients.
  - The critique admits it "cannot ground the size" of the downside.
- The critique argues from incidence rates falling slowly while counts do not. That is plausible given population growth. But the "pre-COVID ~2.5%/yr rate decline" and "counts flat or rising" claims come from the critique's own arithmetic, with no cited count series for the 8-year horizon. Unverified here does not mean false. If counts really are flat, the conclusion follows. The weakness is that it is a conditional extrapolation, not an observed 8-year trend.
- The critique calls its own direction label "uncertain" and its conclusion "upward". That internal inconsistency signals the evidence does not pin down the sign with confidence.

MAGNITUDE CHALLENGE:
- Decline-only effect: 0.98^8 = 0.851, so removing the decline gives 1/0.851 = +17.5% eligible people. This matches the Quantifier's central of 6.46M (+17.5% SROI).
- The "+1%/yr" scenario gives 1.01^8 ≈ 1.083, so ~7.7M. This requires sustained count growth. The notified count has plausibly been rising mainly due to post-COVID recovery, so it is not clearly a structural trend.
- Because the 5.5M start value is not derived in the paraphrased BOTEC, I cannot say how much of the gap between 5.5M and 7.1M reflects the decline assumption versus a different baseline year or definition. The critique attributes the full gap to the decline assumption. I cannot ground a more precise split.
- The Quantifier's low case (−5.5%) shows the range is two-sided. The critique's headline, a flat-to-rising count, is the favorable end of that range.

OFFSETTING FACTORS:
- The BOTEC applies no discounting (parameter map: "implicit discount rate (currently 0)"). The eligible population is a year-8 quantity. Discounting at 3% gives 1/1.03^8 ≈ 0.79, and at 5% gives 1/1.05^8 ≈ 0.68. That is a −21% to −32% effect on the same benefit stream, larger than the +17.5% from removing the decline. A correction on the decline alone, without the timing correction, is one-sided.
- The 60% uptake figure has no empirical precedent in the parameter map, and uptake ramping over years would reduce benefit in the adoption year. A larger eligible pool does not by itself raise delivered benefit if uptake is limited by systems capacity, not patient numbers.
- Funding disruptions that raise incidence in HIV-affected populations also plausibly lower the share of cases treated. That would break the "constant share treated" assumption in the downward direction.

OVERALL ASSESSMENT:
Partial defense.
- The direction (2% decline on counts is probably conservative) is credible, and CG did not justify the 2% against count data.
- The magnitude from this parameter alone is about +17%, below the materiality threshold.
- The upward correction does not threaten the bar.
- The unmodelled absence of discounting is a larger and opposite-signed adjustment.
- The >25% claim relies on combining with the baseline correction in Critique 1.

CONCESSIONS:
- A 2%/yr decline in counts is not derived from any count series, and the critique is probably right that it is conservative if notifications are flat to mildly rising.
- "Roughly flat since ~2015" is not a defensible description of CG's assumption, and the critique's narrower framing is more accurate on this point.
- The point estimate of eligible people is probably understated by roughly 10–20% from the decline assumption alone. I accept this arguendo.
- CG should have flagged the 2% as a count-based assumption with sensitivity.
```

### Challenger
REBUTTAL: A 2%/yr decline in notified case counts probably contradicts the observed trend

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the 2% decline is a forward projection to the time of adoption, not a fit to a historical series. It is a deliberately round, conservative planning assumption, so the 2020–2024 data cannot refute it.

Response:
- The Advocate concedes that CG derived the 2% from no count series. A forward projection with no stated basis, applied to a count, is an unsupported assumption, whatever it is called.
- "Conservative" does not make it a neutral placeholder. The parameter multiplies the eligible pool directly (0.98^8 ≈ 0.851), so it moves the output by a known amount.
- The Advocate says the BOTEC does not claim to estimate the notification trend. But the eligible-patient count is exactly where a notification trend enters.
- The critique's mechanism is that a rate-decline figure was applied to counts. This is a category error, not just a judgment call about 2025–2033. The Advocate concedes the population-growth point ("plausible").
- Illustrative derivation. Suppose incidence rates fall about 2%/yr (the critique's own pre-COVID figure was ~2.5%, which I cannot independently ground). Suppose population grows about 1%/yr (my recollection of UN figures, not in the evidence package). Counts then fall only ~1%/yr, and 0.99^8 ≈ 0.923.
- That gives a decline-only correction of roughly +8.5% (0.923/0.851). It is smaller than the Advocate's +17.5%, but it is not zero, and it assumes no detection gains.

> The Advocate claims: the decline lever alone is worth +17.5% (flat vs. 0.98^8), below the 25% line. The >25% figure comes only from combining it with the baseline correction in Critique 1.

Response:
- I concede the flat-count case is +17.5%, matching the Quantifier's central (6.46M eligible, +17.45% SROI).
- The Advocate's "decline alone is +17%, not >25%" holds only at exactly flat counts. If counts rise at +1%/yr, the ratio is 1.01^8 / 0.98^8 = 1.0829 / 0.8508 ≈ 1.273, or **+27% on this parameter alone**. This follows from the Advocate's own formulas.
- The Quantifier's high case (3,888, +27.27%) is numerically the same figure.
- So the decline-only effect spans about +8% to +27% depending on the count trend, and the critique's contested claim is that the trend is flat or rising. The Advocate treats +17.5% as the ceiling when it is the midpoint.
- I concede the funding-decision point. The estimate is already above the bar, and an upward revision cannot change the decision. The residual value of this critique is calibration: the stated uncertainty band is asymmetric in a direction the report does not flag.

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the 2020–2024 window is a COVID dip and rebound, so 8.2M may include catch-up backlog and overstate the steady-state level. The Advocate's recalled series is 7.1M (2019), 5.8M, 6.4M, 7.5M, 8.2M (2023).

Response:
- The Advocate flags this as unverified recall. My own recollection of the WHO Global TB Report agrees, but I cannot ground it either, so I treat it conditionally.
- If that series is right, it undercuts the "rebound overstates" argument. A pure catch-up to trend would return to about 7.1M. 2023 is ~15% above 2019. That overshoot is either a longer backlog drain or underlying growth.
- Even on the Advocate's series, 2019 (pre-COVID) is above what a 2%/yr decline from a ~2015 start would imply. My recollection is ~6.4M notified in 2015, but I cannot ground it. If correct, 6.4M to 7.1M over four years is about +2.6%/yr, which contradicts a 2% decline in counts.
- I accept that the Advocate's COVID caveat justifies a lower baseline than 8.2M. That is a Critique 1 issue, not a defense of the 2% decline.

> The Advocate claims: the funding-cut modelling is adjacent evidence. It covers one country and one subpopulation, and measures incidence rather than notifications. Funding cuts could lower detection, so notified counts might fall.

Response:
- Agreed that it is adjacent. The critique itself says it "cannot ground the size" of the downside, and I do not rely on this evidence for the upward claim.
- The Advocate's reversal (cuts lower detection, so counts fall) is also ungrounded. Neither the verifier package nor the Advocate cites any notification effect from the 2025 disruptions.
- A speculative downside shock for 2025–2033 does not rebut an unsupported assumption of permanent 2%/yr decline. To justify 0.851 over eight years, notifications would need to fall about 15% cumulatively, which requires a sustained, large detection loss. Nobody has shown that.

> The Advocate claims: the critique's "direction: uncertain" label versus "upward" conclusion is an internal inconsistency showing the evidence does not pin down the sign.

Response:
- The label inconsistency is real, and the Verifier already noted it.
- It concerns the critique's labelling. It is not evidence about the sign of the parameter error.
- The Advocate concedes the 2% is "probably conservative." That is the sign. The residual uncertainty is the size of the funding downside, not the direction of the decline assumption.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: the "+1%/yr" scenario requires sustained count growth. Recent growth is mostly post-COVID recovery. The Quantifier's low case (−5.5%) shows the range is two-sided.

Response:
- Minimum defensible magnitude, on this parameter alone: about +8% (counts falling ~1%/yr per the derivation above), up to +17.5% (flat). I cannot ground a lower value.
- The −5.5% low case is not evidence that counts are expected to fall faster than 2%. I cannot ground what assumption generates it. The Advocate cites it as support without showing what scenario it represents.
- The Advocate concedes the point estimate is "probably understated by roughly 10–20% from the decline assumption alone." Even that concession is a non-trivial bias, though below the 25% bar.
- The Advocate cannot decompose how much of 5.5M→7.1M is the decline versus baseline. I agree, and this is why the critique's ">25% when combined" should be read as overlapping with Critique 1, not as additive.

**RESPONSE TO "OFFSETTING FACTORS":**

> The Advocate claims: the BOTEC applies no discounting (implicit rate 0). Discounting at 3–5% over 8 years is −21% to −32%, larger than the +17.5% here, so correcting only the decline is one-sided.

Response:
- The discounting offset is real in the parameter map. It is a separate parameter and does not change the size of this error.
- The two corrections are multiplicative. A −25% discounting adjustment leaves a +17.5% error in the eligible pool at +17.5% relative to whatever level it multiplies. Netting them hides the 2% error without making it smaller.
- I cannot ground whether the benefit stream is a single year-8 quantity or spread over years, so the −21% to −32% range is conditional.

> The Advocate claims: 60% uptake has no precedent, and uptake may be capacity-constrained, so a bigger pool does not raise delivered benefit.

Response:
- This offset is conditional and not in the model. The Quantifier's output reports `cap_binds` = false at baseline, low, central, and high. In the model as built, pool size is not capped by systems capacity.
- Systems-capacity limits on uptake would weaken this critique only if they bind, and the Advocate offers no evidence that they do.

> The Advocate claims: funding disruptions that raise incidence may also lower the share treated, breaking the "constant share treated" assumption downward.

Response:
- This is a genuine uncertainty, and I concede it as a downside risk. It is a hypothesis with no cited magnitude, so it cannot offset a quantified +8% to +27% effect.

**KEY UNRESOLVED QUESTIONS:**
- What is CG's actual derivation of 5.5M? If it starts from a baseline near 6.46M (the flat-count case), the 2% decline is the sole driver of the gap. If it starts from a lower baseline year, the decline's marginal effect is smaller.
- What is the WHO notification series for 2015–2019 and for 2024? That would show whether counts were rising or falling pre-COVID. Neither side has grounded the figures.
- Will 2025–2033 funding disruptions reduce detection enough to produce a sustained decline in notified counts? The verifier marked this unquantified, which is different from rejected.
- Should the final report treat the 2% as a count assumption with a sensitivity range (roughly 0% to +1%/yr), as the Advocate concedes CG "should have" done?

### Judge Audit
Surviving strength: moderate
Justification: The direction of the critique survived cleanly. The Advocate conceded it, and the core arithmetic (0.98^8, 1.01^8/0.98^8) was sound and shared by both sides. The critique's materiality claim did not survive on its own terms. The Advocate showed, from the verifier's own non-additivity note, that the >25% figure depends on Critique 1. The Challenger could only push past 25% via an ungrounded +1%/yr growth scenario. Both sides leaned on recalled, ungrounded series and unquantified offsets. The Challenger also misstated the verifier's 2025 notification evidence, which slightly understates the downside.
Recommended action: 1. CONCLUDE NOW: Replace the 2%/yr decline on notified counts with 0%/yr as the central assumption. That raises eligible people from about 5.5M to about 6.5M (+17.5%), with moderate-to-high confidence in direction. Report a sensitivity range of roughly −1%/yr to +1%/yr (about 5.9M to 7.0M from this parameter alone). The downside end is justified by the WHO provisional 2025 notification declines in Cambodia, Kenya, Mozambique and Uganda. The upside end is bounded by the 22% remaining detection gap. Do not add this effect to Critique 1's baseline correction. Note that the funding decision is unchanged. Separately, check WHO Global TB Report notification counts for 2015–2018 (publicly available and quick to retrieve) to confirm whether pre-COVID counts were rising. That is the one ungrounded input both sides relied on.
Action feasibility: actionable_now
Advocate failures: ['sound_synthesis_noted: 0.98^8 = 0.851, so removing the decline gives 1/0.851 = +17.5%". This is derived correctly and matches the Quantifier\'s central case. The point that Critique 2\'s >25% depends on the 8.2M × 0.96 × 0.90 baseline already in Critique 1 is grounded in the verifier\'s own note.', 'whataboutism: Raising the zero discount rate ("−21% to −32%… larger than the +17.5%… a correction on the decline alone… is one-sided") does not address whether the 2% count decline is wrong. The discount factors are computed correctly. But discounting is a separate parameter, and the assumption that benefit is a single year-8 quantity is not established. The Challenger correctly answered that the two corrections multiply rather than cancel.', 'call_to_ignorance: uptake ramping over years would reduce benefit… if uptake is limited by systems capacity". No evidence is offered that capacity binds, and the Quantifier output shows `cap_binds = false` in all cases.', 'call_to_ignorance: Funding disruptions… also plausibly lower the share of cases treated." This is offered as an offset with no magnitude. It is partly redeemable, because the verifier package does contain relevant evidence (see missed defense below), but the Advocate did not cite it.', 'call_to_ignorance: the 2023 value may include catch-up of previously undiagnosed backlog… plausibly overstates the starting point". This is speculation with no evidence of how large the backlog drain was. It also sits awkwardly with the verifier finding that the 2024 detection gap (2.7M in 2023, 22% unnotified in 2024) is below the pre-pandemic 3.2M. That finding points to a sustained detection improvement rather than a transient rebound.', 'unsupported_estimate_pseudo: The Quantifier\'s low case (−5.5%) shows the range is two-sided." The Advocate cites the number without saying what scenario produces it. As the Challenger noted, it cannot serve as evidence that counts are expected to fall faster than 2%/yr.', 'misrepresenting_evidence_status: The Advocate says the notification series "is not in the verifier package, so please treat it as unverified." The verifier does contain notifications of 7.1M (2019) and 8.3M (2024). The intermediate years are unverified, but the endpoints are verified. This is minor, and it cuts against the Advocate\'s own rebound argument.']
Challenger failures: ['sound_synthesis_noted: 1.01^8 / 0.98^8 ≈ 1.273, or +27% on this parameter alone". The arithmetic is correct and is built from the Advocate\'s own formula. The multiplicative rebuttal on discounting is also sound.', 'unsupported_estimate_counter: The "+8.5%" lower bound rests on population growth of about 1%/yr ("my recollection of UN figures, not in the evidence package") and an assumed 2%/yr rate decline. The ungrounded inputs are transparently flagged. However, the verifier package\'s 2015–2024 rate data (12.3% net, about 1.4%/yr) were available and not used. The number is then carried forward as the floor of a "quantified" range.', 'unsupported_estimate_fabricated: ~6.4M notified in 2015… but I cannot ground it… +2.6%/yr, which contradicts a 2% decline in counts". This is a recalled number used to draw a directional conclusion. The Challenger acknowledges it is ungrounded, but it still does argumentative work.', 'misrepresenting_evidence_status: Neither the verifier package nor the Advocate cites any notification effect from the 2025 disruptions." This is incorrect. The verifier package explicitly reports WHO provisional H1-2025 data showing notification reductions beyond trend in four countries, and WHO\'s warning that impacts could worsen. The effect on global counts is unquantified, but it is not unevidenced.', 'false_definitiveness: it cannot offset a quantified +8% to +27% effect." The range is anchored by an ungrounded floor (+8%) and a speculative ceiling (+27%, which requires sustained +1%/yr count growth that nobody grounded). Calling it "quantified" in order to dismiss the unquantified downside overstates the asymmetry.', 'strawmanning: The Advocate treats +17.5% as the ceiling when it is the midpoint." The Advocate explicitly computed the +1%/yr scenario (~7.7M) and argued it requires sustained growth. That is contesting the scenario, not ignoring it. The charge is mild but inaccurate.']
Debate resolved: Both sides agree that the 2%/yr count decline has no count-series basis and is probably conservative, so the error runs upward. At flat counts, the decline-only effect is about +17.5% (6.46M eligible), which is below the 25% materiality line. Its >25% combination with the baseline correction overlaps Critique 1 and is not additive. Both sides also accept that an upward revision cannot change the funding decision, given the point estimate is already above the bar.
Debate unresolved: The 2025–2033 trajectory of notified counts remains open. It ranges from a funding-driven decline (partially evidenced in four countries, unquantified globally) to flat (+17.5%) to detection-gap-driven growth (+27%). That trajectory determines whether the decline parameter alone crosses 25%. How the zero-discount, year-8 framing interacts with this parameter was also raised but not settled.

--- Critique: "Adult DS notified" is not "eligible for the trial label": missing applicability filters ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION: "Adult DS notified" is not "eligible for the trial label": missing applicability filters

**EXISTING COVERAGE:**

1. The 60% uptake parameter is the only place where CG's BOTEC can absorb applicability filters. CG describes it as the share of patients who "would add atorvastatin if it works." That is a clinician-and-patient behavioural estimate, not a count of label-eligible people. It plausibly already nets out contraindications, HIV co-management choices, pregnancy and hepatic exclusions, and non-pulmonary disease.
2. The critique never shows that the 60% is gross of these filters. It cannot show this, because CG gives no derivation of the 60%. The proposed stack (×0.85 × 0.85 ≈ ×0.73) is equivalent to lowering uptake from 60% to about 44% (0.60 × 0.727 = 0.436).
   - 44% sits inside the plausible error band of an ungrounded round-number guess.
   - It is a revision of a soft judgement, not the correction of an omitted structural term.
3. The "96% drug-susceptible" filter shows CG did apply at least one clinical-applicability filter. The model is not a naive notification count.
4. The parameter map confirms CG used the *average* 6% treated-cohort mortality. That average already includes the HIV-positive and extrapulmonary patients the critique wants filtered out. This matters for the offset discussion below.

**EVIDENCE WEAKNESSES:**

1. The critique itself labels the statin-specific exclusions and the pregnancy and hepatic filters "UNGROUNDED — plausible but needs a trial protocol." Those are three of the five filters in the "other filters ×0.85" step. That multiplier has no sourced components, only the Quantifier's own assertion. I cannot ground the pregnancy or hepatic shares either; treat them as uninformed priors.
2. The bacteriological-confirmation filter (×0.62) is the only one that pushes the figure to ~2.5M. The critique concedes it is "design-dependent and probably the weakest link." A guideline or real-world adoption model applies to all treated pulmonary DS-TB. The WHO caveat about misdiagnosed clinical cases supports a small adjustment, not a ×0.62 haircut.
3. The filters overlap, as the critique concedes. HIV-positive and extrapulmonary cases are correlated, so multiplying them overstates the combined loss. The stack ×0.85 × 0.85 is therefore an upper bound on the filter effect, not a central estimate.
4. The regional evidence cuts both ways. The 25% extrapulmonary share is a Southeast Asia figure, and the global figure is 16%. The critique notes a model "weighted toward India, Nigeria and Indonesia" but does not show that weighting.

**MAGNITUDE CHALLENGE:**

1. My reconstruction of the Quantifier's range, from the sensitivity output:
   - The sensitivity ratios imply a baseline of 5.5M. The low, central and high cases are 3.5M, 4.0M and 4.7M.
   - The 3.5M low case matches 5.5M × 0.75 (25% extrapulmonary) × 0.85 (other filters) = 3.51M. That applies the Southeast Asia extrapulmonary share globally and stacks the full other-filter haircut with no overlap correction.
   - The low case therefore combines two upper-bound assumptions.
2. The central 4.0M is ×0.85 (extrapulmonary, 16% global) × ×0.85 (ungrounded other filters). The first step is grounded at 5.5 × 0.84 ≈ 4.6–4.7M. The second step, which brings it to ~4.0M, is the ungrounded one.
   - Only the grounded step (~4.7M) is supported, and it moves SROI by about −15%, below the ~25% materiality line.
   - Moving from ~4.7M to ~4.0M rests entirely on the ungrounded filters.
3. Breaching the bar (about 3.6M) requires either the global use of the 25% regional figure or the culture-confirmed design. Neither is the base case.

**OFFSETTING FACTORS:**

1. CG values only on-treatment mortality. The parameter map lists implicit zeros for morbidity DALYs, post-treatment mortality DALYs, transmission-averted cases and diagnostic value. The context describes reduced lung damage on chest X-ray as a main trial finding. If the drug works, these channels add value independent of the eligibility count.
2. The parameter map notes that notified-cohort mortality may understate true mortality through unascertained deaths. That would push baseline_mortality up, partly compensating for a smaller eligible population.
3. The critique acknowledges the Critique 2 offset: a 2% annual decline may be overly conservative. Its own text says the stacked net "could net out to roughly the current figure," so the direction is acknowledged as uncertain.
4. In the other direction, if CG's 5.5M is the correct pool and the actual label is broad (real-world use of cheap generics tends to exceed formal indications), uptake could exceed the filter-implied number. I cannot ground this; it is a conditional point only.

**OVERALL ASSESSMENT:** Partial defense.

- The grounded part of the critique (the ~16% extrapulmonary exclusion, giving ~4.7M) is real but moves SROI by only about 15%.
- The larger effect (~27% at the central case) depends on the ungrounded "other filters" step.
- The scenario that actually breaches the bar depends on a trial design the critique itself calls the weakest link.
- The 60% uptake plausibly absorbs some of this, but CG gives no derivation, so I cannot say how much.

**CONCESSIONS:**

1. CG applies the 60% uptake to the full ~5.5M and describes it as uptake among "adult" patients. Nothing in the BOTEC removes children (~10–12%) or extrapulmonary cases before that step. At least the extrapulmonary share is not explicitly modeled.
2. Excluded subgroups (HIV-positive, extrapulmonary such as TB meningitis) likely have above-average mortality. Removing them could cut deaths averted by more than a proportional share, since the model applies average 6% mortality to the whole pool. The Quantifier's proportional treatment may even understate the effect on this channel.
3. If neither the uptake judgement nor the offsetting channels absorb these filters, the central ~−27% is nominally above the ~25% materiality threshold. I cannot show that the offsets cancel it; they are unquantified.
4. The critique's methodological point is valid. The filters should be modeled explicitly rather than left implicit in an ungrounded 60%.

### Challenger
REBUTTAL: "Adult DS notified" is not "eligible for the trial label": missing applicability filters

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the 60% uptake parameter plausibly already nets out contraindications, HIV and pregnancy exclusions, hepatic exclusions and non-pulmonary disease. On this view, the stack is a revision of a soft judgement from 60% to about 44%, not an omitted structural term.

1. The Advocate's own concession undercuts this. They concede that CG applies the 60% to the full ~5.5M, and that nothing in the BOTEC explicitly removes extrapulmonary cases or children.
   - "Plausibly absorbs" is therefore a hypothesis, not a description of the model.
   - The Advocate also says they "cannot say how much" the 60% absorbs.
   - A defense that cannot show any absorption is a possibility, not coverage.

2. CG describes the 60% as the share who "would add atorvastatin if it works". That is a behavioural willingness concept. Eligibility and willingness are conceptually separate, and the BOTEC has no separate eligibility term.
   - If clinicians' willingness is applied to people who are not eligible for the label, the 60% is gross of the filters by construction.
   - The Advocate has no evidence for the opposite reading either.

3. The "44% lies inside the error band of an ungrounded guess" argument proves too little.
   - An ungrounded parameter has symmetric uncertainty, but the filters are one-directional.
   - Uncertainty about the 60% does not offset a known downward bias. It only means we can't tell whether the bias is already priced in.
   - That is a reason to model the filters explicitly, which the Advocate concedes in Concession 4.

4. The 96% drug-susceptible filter does not show that CG applied clinical-applicability filters in general.
   - It addresses resistance, not extrapulmonary disease, HIV, pregnancy or hepatic status.
   - Its presence says nothing about whether those other terms were considered.

5. The Advocate notes that the average 6% mortality includes HIV and extrapulmonary patients. This is not a neutral fact. It supports the critique through the mortality channel, as the Advocate's Concession 2 acknowledges (see Magnitude, point 4).

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the "other filters ×0.85" step has no sourced components, so moving from ~4.7M to ~4.0M rests entirely on ungrounded numbers.

1. This overstates the ungroundedness. The critique's "verified shares" include HIV ~5–6% and Hr-TB ~7–8%, and the verifier did not reject them.
   - What is ungrounded is whether those groups are excluded from the label, not how large they are.
   - Pregnancy, hepatic and statin-specific exclusions are the truly ungrounded part. I concede these and treat them as uninformed priors.

2. A derivation using only the verified shares reproduces roughly the central figure.
   - EPTB: 5.5M × 0.84 = 4.62M.
   - HIV and Hr-TB: 0.945 × 0.925 ≈ 0.874, giving 4.62M × 0.874 ≈ 4.04M.
   - The ×0.85 "other filters" step is therefore approximately the product of verified shares. It is conditional on HIV and Hr-TB being excluded, not an invention.
   - Caveat: if "96% DS" already removes Hr-TB, the Hr-TB part double-counts, and the figure would be nearer ~4.3M. The overlap correction the critique concedes also pushes the figure up.
   - So the central case is a conditional, not an ungrounded, estimate.

3. The Advocate's Concession 1 implies a grounded filter that is not in the Quantifier's stack.
   - If the ~5.5M is all-age notified DS cases, excluding children (~10–12%, per the Advocate) gives 4.04M × 0.89 ≈ 3.6M.
   - That sits at the ~3.6M bar. I cannot verify whether the 5.5M is already adults-only, so this is conditional.
   - But it shows the "bar breach needs 25% EPTB or culture-confirmation" claim depends on an unexamined assumption about the base population.

4. On regional weighting, the Advocate says the critique "does not show" the weighting toward India, Nigeria and Indonesia. I can't show it either, and the verifier confirmed only that regional variation exists.
   - India and Indonesia both fall in WHO's South-East Asia region, where the 25% figure applies. If they dominate CG's population, a SE-Asia-weighted EPTB share is not an "upper bound applied globally".
   - This is conditional on CG's country weights, which neither side has shown. It should not be treated as settled either way.

5. Concession on confirmation: I agree that ×0.62 is design-dependent and weak, and that the verifier supports only a small adjustment. I do not rely on it.

**RESPONSE TO "MAGNITUDE CHALLENGE":**

> The Advocate claims: only the ~4.7M step is grounded and moves SROI about −15%, below materiality. Reaching the bar requires either global use of the 25% regional figure or the culture-confirmed design.

1. The −15% figure is a floor on the grounded filters, not a central estimate. It omits the HIV and Hr-TB shares, which are verified (point 2 above). The grounded-share central is ~4.0M, or −27%.

2. The Advocate's own concession puts the central estimate above the ~25% materiality line unless an offset absorbs it. The Advocate says they "cannot show that the offsets cancel it."

3. Minimum plausible magnitude, derived from grounded components only:
   - EPTB 16% alone: ×0.84, −16%.
   - Adding HIV and Hr-TB shares with partial overlap: roughly −20% to −27%.
   - Including children, if not already excluded: roughly −30%.
   - The low end, about −15%, is material only if everything beyond the first filter is rejected.

4. The Advocate's Concession 2 matters for magnitude.
   - HIV-positive and extrapulmonary (including meningitis) patients likely have above-average mortality.
   - Removing them lowers the average mortality of the remaining pool, so the 6% baseline is too high for the eligible population.
   - The effect on deaths averted would be larger than the proportional eligible-count reduction. The Quantifier's −27% is therefore, if anything, conservative on this channel.
   - I cannot quantify this uplift from the evidence package. Its direction is not in dispute.

**RESPONSE TO "OFFSETTING FACTORS":**

1. **Unmodelled benefits (morbidity, lung damage, transmission, diagnostics).** These are real but not in the model, and they are not offsets to the eligibility count.
   - They scale with the number of people treated, so a smaller eligible pool shrinks them too.
   - They would be a separate critique about omitted value, not a cancellation of this one.
   - They are also unquantified in the evidence package, so they cannot be netted against a quantified −27%.

2. **Unascertained deaths raising baseline mortality.** This is unquantified and runs against Concession 2, where removing high-mortality subgroups lowers the baseline for the eligible pool. The Advocate has offered two opposite-sign mortality effects without sizing either.

3. **Critique 2 (the 2% decline may be conservative).** An offset counts only if it is itself established.
   - The critique itself calls the net "roughly the current figure" only under the stacking of a separate critique.
   - The Advocate hasn't shown that Critique 2 survives, so it cannot be used to neutralise this critique here.

4. **Broad real-world generic use exceeding the label.** The Advocate admits they cannot ground this. It is conditional speculation, and it is partly the 60% parameter's job.

**KEY UNRESOLVED QUESTIONS:**

- Is the ~5.5M adult-only, or all-age? If all-age, a grounded ~10–12% child exclusion is missing and the grounded stack reaches ~3.6M.
- What does the 60% actually mean in CG's reasoning: willingness among eligible people, or a blended eligible-and-willing share? Only CG can say, and the answer determines whether the filters are double-counted or missing.
- Would the trial label or protocol exclude HIV-positive, Hr-TB, pregnant and hepatic-impaired patients? The shares are verified but the exclusions are not. The verifier marked these as unverifiable-without-protocol, not as rejected.
- How heavily do SE Asian countries weight CG's pool? This decides whether the 25% EPTB figure is an upper bound or a central input.
- By how much does removing high-mortality subgroups reduce the 6% baseline for the remaining eligible population?

### Judge Audit
Surviving strength: moderate
Justification: The Challenger's derivation from verified shares (≈4.04M) is grounded and conditional. It directly rebutted the Advocate's misstated claim that the "other filters" step had no sourced components. The Advocate's grounded concessions (EPTB not modelled; the mortality-composition channel likely amplifying the effect) also support the critique. However, the Challenger's push toward the bar relied on an unsourced child-share figure that it mislabelled as grounded. The step from −15% to −27% remains conditional on unverified exclusion criteria. The critique's direction survives, but its materiality does not clearly survive.
Recommended action: 2. SPECIFIC INVESTIGATION:
   - **Interim conclusion (moderate confidence):** apply at least the grounded ×0.84 extrapulmonary adjustment now, giving ~4.6M. Treat ~4.0M as the conditional central case.
   - **Then settle the conditional terms with three checks:**
     - (a) Inspect CG's BOTEC source for the 5.5M. Determine whether it is adults-only and what its country weights are, especially the India and Indonesia share, to fix the EPTB share between 16% and 25%.
     - (b) Pull the registered protocol for the atorvastatin adjunct trial from the trial registry. Check its exclusion criteria for HIV/ART, pregnancy, hepatic impairment, extrapulmonary disease and isoniazid resistance.
     - (c) Ask CG, or read its write-up, to establish whether the 60% is conditional on eligibility.
   
   All three are desk checks feasible with existing tooling. Together they determine whether the adjustment lands above or below the materiality line.
Action feasibility: requires_specified_evidence
Advocate failures: ['misrepresenting_evidence_status: The Advocate says the "other filters ×0.85" step "has no sourced components, only the Quantifier\'s own assertion." However, two of its components were verified as to size: HIV at ~5–6% and Hr-TB at ~7–8%. Only the *exclusion* of these groups from the label is unverifiable, along with the pregnancy and hepatic shares. The Advocate merges "size verified, exclusion unverified" into "no sourced components." The Challenger correctly caught this.', 'call_to_ignorance: It plausibly already nets out contraindications, HIV co-management choices, pregnancy and hepatic exclusions, and non-pulmonary disease… The critique never shows that the 60% is gross of these filters. It cannot show this, because CG gives no derivation." Because the 60% has no derivation, the Advocate offers it as possible coverage. The Advocate later admits they "cannot say how much" it absorbs. CG\'s own description of the parameter, "would add atorvastatin if it works," is a willingness concept, which argues against this reading.', 'unsupported_estimate_fabricated: Nothing in the BOTEC removes children (~10–12%)." No source is given and the verifier package does not contain this figure. The Challenger then built on it, so the error spread.', 'false_definitiveness: The stack ×0.85 × 0.85 is therefore an upper bound on the filter effect, not a central estimate." The overlap point is valid but small. In Concession 2 the Advocate concedes that the mortality-composition channel makes the proportional stack *understate* the effect. Calling the stack an "upper bound" is inconsistent with the Advocate\'s own concessions.', 'sound_synthesis_noted: The reconstruction of the low case (5.5 × 0.75 × 0.85 = 3.51M) shows that the low scenario stacks two upper-bound assumptions. The separation of the grounded ×0.84 step (~4.6–4.7M, about −15%) from the conditional remainder is also clear analysis.']
Challenger failures: ['sound_synthesis_noted: EPTB 5.5 × 0.84 = 4.62M; HIV and Hr-TB 0.945 × 0.925 ≈ 0.874, giving ≈ 4.04M. Each component comes from the verifier package. The Challenger states the result is conditional on exclusion and flags the possible Hr-TB double-count with the 96% DS filter (≈4.3M). This is the most substantive move in the debate and it rebuts the "entirely ungrounded" framing.', 'unsupported_estimate_pseudo: The Challenger computes "4.04M × 0.89 ≈ 3.6M" and, in Key Unresolved Questions, calls it "a grounded ~10–12% child exclusion." The 10–12% came from the Advocate with no source and is not in the evidence package. The body text hedges that this is conditional, but labelling the figure "grounded" is wrong.', 'unsupported_estimate_pseudo: The "minimum plausible magnitude" ranges are not derived:', 'false_definitiveness: The Challenger says offsets "cannot be netted against a quantified −27%." The −27% is conditional on unverified exclusions, as the Challenger acknowledges elsewhere. Presenting it as a quantified fact while dismissing offsets as unquantified is asymmetric.', 'sound_synthesis_noted: Several arguments are correct and well-made:']
Debate resolved: Both sides accept several points:
- The ~16% extrapulmonary exclusion is grounded and is not explicitly modelled in CG's BOTEC. It alone moves eligible cases to ~4.6–4.7M, about −15%.
- The ×0.62 confirmation filter is not a base-case input.
- The pregnancy, hepatic and statin-specific filters are uninformed priors.
- The filters should be modelled explicitly.

The debate also established two further points:
- The ~4.0M central figure is a conditional synthesis of verified shares, not an invented number.
- The direction is downward.
Debate unresolved: The magnitude, between about −15% and about −27% and therefore straddling the ~25% materiality line, remains open. It depends on three things neither side could settle:
- Whether a label or adoption model would actually exclude HIV-positive and undetected Hr-TB patients.
- Whether CG's 60% uptake is willingness among eligible patients or a blended share.
- Whether the 5.5M is already adults-only and SE-Asia-weighted.

The direction and size of the mortality-composition effect relative to the unascertained-deaths effect is also unsized.

--- Critique: Shorter and new regimens erode both the eligible population and the incremental benefit ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: Shorter and new regimens erode both the eligible population and the incremental benefit
```

## EXISTING COVERAGE

1. **CG does not explicitly model regimen change.** The parameter map lists "no consideration of whether newer/shorter regimens (4-month HPMZ) change the room for adjunctive benefit." I concede this.
2. **Several existing parameters absorb part of the concern, though none targets it:**
   - The 40% p_success covers Phase II and III both succeeding. If the backbone shifts and the effect fails to transfer, that is a way the Phase III result could disappoint.
   - The 10% relative reduction is applied only on a positive result.
   - The 60% adult uptake is a round-number assumption with no stated error band. A modest displacement (the Quantifier's central case is about 7.5%) is well inside the unstated uncertainty of that figure. This is a weak form of coverage, and I do not lean on it.
3. **The third mechanism does not touch the modeled chain.** The critique says any statin benefit that works through shortening treatment would shrink. The BOTEC values only mortality ("only mortality is valued") and has no term for treatment duration or time-to-clearance. A shorter backbone cannot reduce a benefit the formula never counts.

## EVIDENCE WEAKNESSES

1. **The displacement share is the critique's own scenario.** The critique says the 20–40% figure "is not grounded in published projections" and is "UNGROUNDED." The whole mechanism rests on this number.
2. **The critique's own evidence points toward slow uptake:**
   - WHO's HPMZ recommendation is conditional and limited to age ≥12.
   - Rifapentine supply and cost constrain scale-up.
   - Low rifapentine exposure drives unfavorable outcomes in the HPMZ arm, so dosing constraints also limit rollout.
   - Adolescents aged 12–16 still have the standard 6-month and 4-month 2HRZ(E)/2HR options.
   - The 4-month regimen for children with non-severe TB still contains rifampicin.
   
   The Investigator itself says the low end is more likely than the high end.
3. **The Paton et al. (NEJM 2023) strategy is trial-stage evidence.** It showed noninferiority in a trial. I cannot ground whether national programmes will adopt it widely by ~2033, and the critique offers no adoption data either.
4. **Noninferiority does not show lower baseline mortality.**
   - The HPMZ trial (Dorman et al., NEJM 2021) and the Paton trial were noninferiority designs.
   - Noninferiority establishes that the new regimen is not meaningfully worse. It does not establish that mortality is lower, so these designs do not show that "less baseline mortality" is left for an adjunct to improve.
   - I cannot ground the actual on-treatment mortality by regimen from the evidence package. The "less room to improve" claim is therefore unsupported, not refuted.
5. **The rifapentine-versus-rifampicin inducer claim is unverified.** If it is true, the interaction concern would carry over to HPMZ. That concern is already a separate critique thread (rifampicin-induced reduction in statin exposure), so it adds nothing new to the eligible-population argument.

## MAGNITUDE CHALLENGE

1. **The mechanism treats displaced patients as zero-benefit.**
   - It says effective eligible falls by the displacement share, 20–40%.
   - That holds only if the statin effect transfers to non-HRZE backbones at 0%.
   - The correct form is: effective loss = displacement × (1 − transfer fraction).
2. **Worked sensitivity:**
   - Break-even: SROI of about 3,055x falls to 2,000x at 2,000/3,055 ≈ 65.5% of baseline, a 34.5% reduction. This matches the critique's "3.6M bar" (5.5M × 0.655 ≈ 3.6M).
   - At 40% displacement, the effective loss exceeds 34.5% only if transfer is below 1 − 0.345/0.40 ≈ 14%.
   - At 20% displacement, no transfer rate crosses the bar.
   - The transfer fraction is not grounded here. It is a parameter the critique implicitly sets to zero, and I flag it as an uninformed prior.
3. **The Quantifier's own results are within tolerance:**
   - The low case (−25%) gives about 2,291x, and the Quantifier flags `crosses_bar_low: false`.
   - The Quantifier's central case (5.0875M eligible, −7.5%) gives about 2,826x, well above the 2,000x bar and below the ~25% materiality threshold.
   - Only the critique's top-end scenario (40% displacement with near-zero transfer) crosses the bar, and the critique itself says that end is less likely.
4. **Calibration of the "material" label:**
   - The critique's text says "low-to-medium" and "uncertain direction."
   - The central estimate is −7.5%, and the low case is at the edge of the threshold ("more than about 25%").
   - Together these suggest the label is generous.

## OFFSETTING FACTORS

1. **Trial design may adapt.**
   - The Phase III is assumed to finish about 8 years after the grant.
   - Programme design at that point will likely test on the then-prevailing standard of care. If so, the adoption-relevant backbone would partly match the trial backbone.
   - This is plausible reasoning, not an attested fact.
2. **The BOTEC leaves out several benefit channels.**
   - Only on-treatment mortality is valued. Morbidity DALYs (lung damage), post-treatment survival, transmission and diagnostic value are all implicit zeros.
   - These omissions are one-sided conservatism that offsets a modest displacement haircut.
3. **The 2% annual decline and the static drug-susceptible share are not obviously biased.** I make no claim that they offset the displacement.
4. **Pediatric exclusion is already outside the uptake assumption.** The 60% uptake is "adult patients," so the age ≥12 HPMZ limitation overlaps only partly with the relevant population.

## OVERALL ASSESSMENT

**Strong defense**, with the caveat that CG does not explicitly address regimen change.

- The core number (20–40% displacement) is self-described as ungrounded, and the critique's own evidence favors the low end.
- The mechanism assumes zero transfer. Under any plausible partial transfer, the effective loss is smaller than the displacement share.
- The Quantifier's central case stays well above the bar. Only the critique's extreme corner crosses it.

## CONCESSIONS

1. CG does not model regimen change, and the parameter map correctly identifies this gap.
2. At 40% displacement with near-zero transfer, SROI would fall below 2,000x. I cannot rule this out from the evidence package.
3. I cannot ground the displacement share, the transfer fraction, or on-treatment mortality by regimen. My counter-scenarios are therefore no better grounded than the critique's.
4. The rifapentine interaction question is open and could modestly reduce effect size on HPMZ backbones. This is an extra downside risk but is not quantified in the sensitivity run.

### Challenger
REBUTTAL: Shorter and new regimens erode both the eligible population and the incremental benefit

## RESPONSE TO "EXISTING COVERAGE"

> The Advocate claims: the 40% p_success, the 10% conditional effect and the 60% adult uptake absorb part of the regimen-change risk, and the "shortening" mechanism cannot matter because the BOTEC values only mortality and has no duration term.

1. **I concede the shortening point as a mechanism inside the BOTEC.** A formula with no duration or time-to-clearance term cannot lose a duration-mediated benefit. That part of the critique should be dropped or recast.
2. **The Advocate's own wording shows the existing parameters do not cover this.**
   - It calls the 60% uptake "a weak form of coverage" and says it does not lean on it.
   - It concedes the parameter map says CG makes "no consideration" of regimen change.
   - So no parameter is tied to the share of patients on a non-trial backbone.
3. **The p_success argument is not coverage.**
   - The 40% covers "Phase II and III both succeeding."
   - A Phase III that succeeds on HRZE but whose result does not transfer to the regimens patients actually receive is a post-approval relevance loss. It is not a trial-failure event.
   - The 40% does not price that loss.
4. **The residual gap is a missing parameter, not a mis-set one.** The effective-eligible calculation has no regimen-share term. The Quantifier's sensitivity run shows that term moves SROI by 7.5% at the central case and 25% at the low case.

## RESPONSE TO "EVIDENCE WEAKNESSES"

> The Advocate claims: the 20–40% displacement figure is ungrounded, the critique's own evidence points to slow uptake, and noninferiority designs do not show less baseline mortality to improve on.

1. **Noninferiority point: conceded.** Dorman et al. (NEJM 2021) and Paton et al. (NEJM 2023) were noninferiority designs. They do not show that mortality is lower on the new regimens. The "less room to improve" strand is unsupported, and I do not defend it.
2. **The slow-uptake evidence is narrower than the Advocate suggests.**
   - The verifier's items concern rifapentine exposure and dosing inside the HPMZ trial arm, plus supply and cost.
   - These are constraints on HPMZ *today*. They are not a projection to the benefit horizon.
   - The model values benefit at 8 years post-grant and beyond. A snapshot of present constraints says little about displacement after 2033.
   - The verifier's statement that these strategies are "unlikely to reach 20–40% by 2033" is a judgement, not a measurement. The Advocate rightly says it cannot ground adoption either.
3. **The verifier evidence does not touch the 7.5% central case.** The slow-uptake evidence supports "low end more likely." It cannot distinguish 7.5% from 20% displacement.
4. **The age ≥12 argument cuts against the Advocate.**
   - The Advocate's offset #4 says the pediatric exclusion is "already outside the uptake assumption," so the age restriction overlaps only partly with the relevant population.
   - The modeled population is adults, and HPMZ is conditionally recommended for people aged 12 or older. The age limit therefore does not shield the adult population from HPMZ.
   - The age restriction is not a reason to expect lower displacement among the modeled adults.
5. **The rifapentine-induction claim is UNVERIFIABLE, not REJECTED.** Conditional on rifapentine inducing CYP3A4 as strongly as rifampicin, the statin-exposure problem carries over to HPMZ.
   - That would make transfer roughly equal across backbones, which is neutral for the displacement argument.
   - Conditional on it being a weaker inducer, statin exposure might be better on HPMZ, which is also not a harm.
   - Either way this strand does not support the critique, and I do not rest on it.
   - I disagree with the Advocate's claim that it is "already a separate thread" and so adds nothing. The question is whether it is a distinct input to the transfer fraction. It is.

## RESPONSE TO "MAGNITUDE CHALLENGE"

> The Advocate claims: effective loss = displacement × (1 − transfer), so the critique's 20–40% haircut implicitly sets transfer to zero. The bar is crossed only at ≥40% displacement with transfer below ~14%.

1. **The formula is correct, and the "compounds" language is wrong.**
   - If the eligible-population cut already counts displaced patients as zero benefit, adding an effect-size shrink on the same patients double-counts.
   - Maximum loss is therefore bounded by the displacement share.
2. **The Advocate's arithmetic checks out.**
   - Bar: 2,000 / 3,055 = 65.5% of baseline, a 34.5% reduction.
   - At 40% displacement, crossing requires (1 − t) > 0.345 / 0.40 = 0.8625, so t < ~14%.
3. **A partial-transfer scenario is not grounded either.**
   - The Advocate labels the transfer fraction an "uninformed prior," and so is its implied alternative.
   - The question is whether a statin's host-directed effect on mortality is backbone-independent. No source in the package tests this.
   - Transfer across a rifamycin-based regimen with different companion drugs is plausible. It is not demonstrated.
4. **The minimum-plausible-impact case is small.**
   - At the Quantifier's central 7.5%, SROI is ~2,826x, about 41% above the 2,000x bar.
   - The Advocate is right that this does not threaten the conclusion.
5. **The "within tolerance" claim for the −25% low case is thinner than stated.**
   - The −25% low case gives ~2,291x. That leaves 14.5% headroom above the bar, not "well above."
   - Any other downward revision of 15% or more to the same SROI would cross the bar if combined with this one.
   - The Advocate concedes the rifapentine interaction is "not quantified in the sensitivity run."
6. **The Quantifier's central 7.5% sits below the critique's own 20–40% range.** It was set after the downgrade to "low-to-medium." The Advocate concedes it is no better grounded than the critique's range, so "well above the bar" depends on which ungrounded number one prefers.
7. **On the "material" label:** I do not contest that it looks generous given the critique's own "low-to-medium" wording.

## RESPONSE TO "OFFSETTING FACTORS"

> The Advocate claims: the Phase III may adapt to the prevailing standard of care, and the BOTEC omits morbidity, transmission and post-treatment survival, which offsets a modest haircut.

1. **Trial-adaptation offset.** The Advocate labels it "plausible reasoning, not an attested fact." It is hypothetical and is not in the model.
   - If the Phase III moves to an HPMZ or other backbone, it changes trial cost, timeline, and eligible age and population.
   - Those changes would enter other parameters and would not be neutral.
2. **Omitted-channel offset.**
   - The omitted channels (morbidity DALYs, transmission, diagnostic value) are unquantified in the model and unsized by the Advocate.
   - Omitting a benefit is an offset against a specific haircut only if it is sized and comparable.
   - Transmission and morbidity benefits would also be subject to the same regimen-displacement haircut.
3. **Net:** the offsets are real in direction but are not in the model and have no magnitude. They do not neutralize a 20–25% eligible haircut.

## KEY UNRESOLVED QUESTIONS

- What share of drug-susceptible adult TB patients will be on a non-HRZE first-line regimen in the years after the Phase III reads out (2033 onward), as opposed to today's constrained uptake? Neither side has a projection.
- What is the transfer fraction of a statin's mortality effect across rifapentine/moxifloxacin and bedaquiline-linezolid backbones? The critique's cleanest remaining form is that the model has no term for it.
- Does the statin's effect on mortality operate through a mechanism that is backbone-independent, or through one that depends on companion drugs? No source in the package addresses this.
- Is the Quantifier's central case (7.5% displacement) or its low case (25%) the better reference? Both are unanchored, and the choice moves SROI from ~2,826x to ~2,291x.

### Judge Audit
Surviving strength: moderate
Justification: The Advocate's transfer-fraction reformulation and break-even arithmetic substantially defeated the critique's quantitative claim. The Challenger accepted both and dropped three of the critique's strands. What survives is grounded but modest:
- **The missing term.** The Challenger's p_success argument (post-approval relevance loss is not a trial-failure event) and its age-restriction correction show that no existing parameter covers regimen displacement among adults. The Advocate's "absorbed by existing parameters" defense therefore fails.
- **The magnitude.** The plausible impact (−7.5% to −25%) does not cross the bar. However, the low case leaves only about 14.5% headroom, so the concern is material without being decisive.
This sits at the lower end of moderate. The debate was productive and the critique was narrowed honestly, but the critique's headline mechanism did not survive intact.
Recommended action: 1. CONCLUDE NOW, with moderate confidence. The critique survives only as a missing-parameter gap, not as a threat to the funding conclusion.
   - **What to add.** CG's model should add an explicit effective-eligible adjustment of the form displacement × (1 − transfer).
   - **Suggested band.** Run it as a sensitivity band of roughly −5% to −25% on SROI.
   - **Expected result.** On current evidence, SROI stays above 2,000x across that band. The "material" label should be downgraded.
   - **Strands to drop.** The "compounding," "shortening" and "less room to improve" strands should be dropped. The claim that rifapentine is a "stronger inducer" should be removed.
   - **Optional follow-up.** If a single check is warranted, the verifier can do it within existing tooling. One option is to pull current HPMZ and rifapentine procurement and uptake data from the WHO Global TB Report or the Global Drug Facility. Another is to search for any study of statin adjunct effects outside HRZE backbones. Either would anchor one of the two open inputs.
Action feasibility: actionable_now
Advocate failures: ['sound_synthesis_noted: The break-even derivation is shown step by step and is correct: 2,000/3,055 ≈ 65.5% of baseline, a 34.5% reduction, consistent with 5.5M × 0.655 ≈ 3.6M. So is the threshold that follows from it: at 40% displacement, crossing requires transfer below 1 − 0.345/0.40 ≈ 14%. The reformulation "effective loss = displacement × (1 − transfer fraction)" is the most important analytical contribution in the debate, and the Challenger accepted it.', 'misrepresenting_evidence_status: Evidence Weakness #2 lists "Rifapentine supply and cost constrain scale-up" as part of the critique\'s own evidence for slow uptake. The verifier marked the supply/cost claim UNVERIFIABLE. The only adjacent source concerns high-dose tolerability in patients with comorbidities. This error runs in the reverse direction from the canonical one: an unverified claim is presented as established support.', 'misrepresenting_evidence_status: The Advocate cites pediatric and adolescent evidence as if it bore on displacement among the modeled adults:', 'false_definitiveness: The Advocate self-rates the defense as "Strong" and states "The Quantifier\'s central case stays well above the bar." In Concession 3 it also admits "I cannot ground the displacement share, the transfer fraction, or on-treatment mortality by regimen. My counter-scenarios are therefore no better grounded than the critique\'s." The 7.5% central case is an unanchored Quantifier input, yet the Advocate relies on it to say the result is "within tolerance." The defense was good, but it was not "strong" in the sense its own concessions permit.', 'false_definitiveness: Offset #2 says the omitted benefit channels (morbidity, transmission, post-treatment survival) are "one-sided conservatism that offsets a modest displacement haircut." These channels are unsized, and the Advocate does not show that they offset anything in magnitude.']
Challenger failures: ['unsupported_estimate_counter: The Offsetting Factors response ends: "They do not neutralize a 20–25% eligible haircut." Earlier, the Challenger had accepted that the minimum-plausible case is 7.5% and that the 20–40% range is ungrounded. Here it quietly re-anchors on a 20–25% figure that has no grounding beyond the critique\'s self-described scenario.', 'call_to_ignorance: The Challenger writes: "A snapshot of present constraints says little about displacement after 2033." The underlying point, that current constraints are not a projection, is valid. But the Challenger uses the absence of a projection to keep higher displacement live, without offering any reason to expect uptake to accelerate. The correct conclusion from the missing evidence is "unknown, with current evidence weakly favoring low uptake," and the Challenger stops short of that.', 'call_to_ignorance: Any other downward revision of 15% or more to the same SROI would cross the bar if combined with this one." The arithmetic is correct (2,291 × 0.85 ≈ 1,947). However, no specific other revision is named or sized. The rifapentine interaction is mentioned, but the Challenger itself conceded that strand is neutral or favorable. The stacking point leans on hypothetical unnamed revisions.']
Debate resolved: The debate settled four things:
- The critique's "shortening" mechanism cannot operate inside a mortality-only BOTEC.
- The "less baseline mortality to improve" strand is unsupported by noninferiority trials.
- The "compounds" language double-counts.
- The maximum loss is bounded by displacement × (1 − transfer).

On that corrected formula, the 2,000x bar is crossed only when displacement is at least about 35% and transfer is near zero (below about 14% at 40% displacement). The critique itself calls that corner the less likely one.

What survives is narrower. It is a structural point, conceded by both sides: the model has no regimen-share/transfer term. The p_success parameter does not price post-approval relevance loss.
Debate unresolved: Two empirical inputs remain unanchored and drive the result:
- the share of drug-susceptible adults on non-HRZE first-line regimens over the post-2033 benefit horizon;
- the fraction of the statin mortality effect that transfers to rifapentine/moxifloxacin or bedaquiline-linezolid backbones.

Because of these gaps, the plausible SROI impact ranges from about −7.5% (≈2,826x) to about −25% (≈2,291x). Neither side could say which end is the better reference.

--- Critique: M72/AS01E and other incidence shocks are likely not large enough by year 8–10, but should be modelled ---

### Advocate
```
DEFENSE OF GIVEWELL'S (CG's) POSITION: M72/AS01E and other incidence shocks are likely not large enough by year 8–10, but should be modelled
```

## EXISTING COVERAGE

1. **A decline is already built in.**
   - The BOTEC assumes new cases fall 2% per year for 8 years.
   - That is a cumulative decline of 1 − 0.98^8 ≈ 14.9%.
   - Working back from the published ~5.5M at year 8, the implied starting pool is 5.5 / 0.851 ≈ 6.5M (my derivation from the published numbers).
   - The critique's "–5 to –15% at year 8" vaccine shock is therefore a further decline stacked on one the model already includes.
   - The critique never says whether 2%/yr already absorbs some vaccine or non-vaccine scale-up.

2. **The horizon framing does not fit the model's structure.**
   - The grant is credited with a 1-year speedup of adoption (Benefits, item 2).
   - Benefits are one year of treatment at the year-8 scaled-up pool (about 19,900 deaths averted per year, once).
   - There is no multi-year benefit stream whose average eligible pool declines after year 8.
   - The critique's "20–35% lower averaged over a ~15-year horizon" does not map onto any quantity in the CEA.
   - The relevant number is the year-8 pool only.

3. **The model is not claiming precision.**
   - The pool is "about 5.5 million."
   - The critique's central value of ~5.3M differs from that by 3.6%.

## EVIDENCE WEAKNESSES

1. **The key figures are ungrounded.**
   - The critique labels the "5–15% at year 8" and the "30–50% later eligibility reduction" as the Investigator's own estimates, "UNGROUNDED, plausible but needing empirical support."
   - The 20–35% averaged figure is conditional on a horizon the CEA does not use.
   - The only quantified effect on the estimate therefore rests on an admitted prior.

2. **The critique's own timeline cuts against its magnitude.**
   - It says that with introduction around 2030, "impact by 2033–35 is likely small."
   - Phase III only started in March 2024, so licensure, WHO recommendation, procurement and country introduction must all precede any incidence effect.
   - The cited India model assumes introduction in 2025, which is earlier than the critique itself considers feasible.
   - That model is evidence of impact under optimistic timing, not at year 8 under realistic timing.
   - The 5–15% range sits uncomfortably against the "likely small" statement, and the low end is more consistent with it.

3. **The cited literature measures something else.**
   - The South Africa model (0.86–2.55M cases averted by 2050) is country-specific and cumulative.
   - The critique itself calls this "consistent with back-loaded impact." It says nothing about the global year-8 pool.
   - The demand-forecast paper was not extracted, so it supports nothing quantitative.
   - The India model's 50% incidence-reduction-by-2035 baseline is a scale-up assumption for non-vaccine interventions in that model. It is not evidence that global notified cases will fall faster than 2%/yr.

4. **The efficacy evidence is imprecise.**
   - Tait et al. (NEJM 2019) gave 49.7% (95% CI 2.1–74.2) on 39 cases, in HIV-negative, IGRA-positive adults.
   - That is a weak basis for projecting a large global incidence effect.
   - If the vaccine has less than 100% probability of Phase III success, the expected shock is smaller than the conditional 5–15%. Any success probability p scales it to p × (5–15%). The critique says this "should be weighted separately" but does not do so.

## MAGNITUDE CHALLENGE

1. **The sensitivity result does not meet the stated bar.**
   - Baseline SROI is ≈3,055x.
   - At the critique's worst case (–15% eligible), SROI is ≈2,597x (–15%). `crosses_bar_low` is false, so it stays above the ~2,000x bar.
   - At the Quantifier's central value (5.3M), SROI changes by –3.6%.
   - The decision-relevance threshold is >25% change or falling below ~2,000x. Neither is met.
   - The "material" label is not supported by the sensitivity output.

2. **The pool enters the formula linearly.**
   - Eligible pool feeds directly into lives saved, so a 15% pool reduction yields a 15% SROI reduction.
   - Moving SROI from 3,055x to 2,000x would require a ~35% reduction in the pool.
   - That is more than twice the top of the critique's year-8 range, and beyond what its own "likely small by 2033–35" reasoning supports.
   - It would only be reached by treating the 30–50% "later-year" figure as applying at year 8. The critique's own timeline argues against that.

3. **Probability weighting pushes the expected effect lower still.**
   - A conditional 5–15% shock, weighted by a vaccine success probability below 1, gives a smaller expected effect.
   - I do not offer a specific success probability, since I cannot ground one.

## OFFSETTING FACTORS

1. **Several benefit channels are implicit zeros.**
   - The BOTEC values only on-treatment mortality.
   - It omits morbidity (lung damage on X-ray), post-treatment mortality, transmission-averted cases and diagnostic value.
   - These are unmodelled upside, and they are far from tiny relative to a 5–15% pool adjustment.

2. **Pool assumptions may be conservative in either direction.**
   - The BOTEC holds the treated share constant.
   - I recall that WHO reported post-COVID record TB notifications. This is not in the evidence package, so treat it as an uninformed prior.
   - If notifications are rebounding or case-finding is improving, a 2%/yr decline could be too steep, which would offset a vaccine shock. I cannot quantify this.

3. **Vaccine impact is concentrated in the wrong population.**
   - M72 is a post-infection vaccine tested in adults with latent infection (IGRA-positive).
   - Initial rollout would likely be targeted or phased, not universal.
   - Coverage-limited early rollout further limits impact by year 8.
   - This is conditional reasoning from the critique's own description of the trial population, not a verified rollout plan.

## OVERALL ASSESSMENT

**Strong defense.**

- The CEA already includes a ~15% cumulative decline.
- The critique's horizon-averaged 20–35% does not apply to a 1-year-speedup structure.
- The year-8 magnitude is self-labelled ungrounded and is in tension with the critique's own "likely small" timeline.
- At the critique's worst case, SROI is ≈2,600x, still above the bar and well under the 25% change threshold.
- Residual risk: the critique correctly identifies that the model has no explicit incidence-shock sensitivity.

## CONCESSIONS

1. The CEA does not model a vaccine or any non-constant-rate incidence shock, and the 2%/yr decline is not justified in the text.
2. The direction of the effect is downward. A realistic vaccine contribution would lower the year-8 pool somewhat, probably a few percent.
3. If the Investigator's 30–50% eligibility reduction held at year 8, SROI would approach or fall below 2,000x. I know of no grounded evidence that it would.
4. The critique's request that the sensitivity of the pool to timing be shown explicitly is reasonable. It is a presentational improvement, not a correction to the estimate.

### Challenger
REBUTTAL: M72/AS01E and other incidence shocks are likely not large enough by year 8–10, but should be modelled

## RESPONSE TO "EXISTING COVERAGE"

> The Advocate claims: the model's 2%/yr decline in new cases, about 14.9% cumulative over 8 years, already builds in a decline, so a vaccine shock would be stacked on top of it.

Response:

1. **The stacking point does not defend the model.** A vaccine effect on top of a secular decline is how the cited literature structures things. The India model that supplied the critique's evidence assumed non-vaccine scale-up toward a 50% incidence reduction by 2035 versus 2015, with the vaccine layered on that baseline. The Advocate's own concession 1 says the 2%/yr is "not justified in the text." So the pool already contains an unjustified decline, and the question is whether it is the right size. The Advocate has no answer to that.

2. **The back-calculation is conditional.** The Advocate's figure of 5.5 / 0.851 ≈ 6.5M is arithmetically correct. It rests on the assumption that the 5.5M was built by compounding 2%/yr from a starting pool. I cannot verify that structure either. It is a plausible reading, not a documented fact.

3. **I concede the horizon point.**
   - If the benefit is a single year at the year-8 pool, the critique's "20–35% averaged over ~15 years" has no counterpart in the CEA.
   - The 30–50% later-year figure is irrelevant unless the model has a multi-year benefit stream, and the Advocate says it does not.
   - This leaves only the year-8 pool as the relevant quantity.

4. **The "no claim to precision" point is weak.** The 3.6% gap between 5.5M and 5.3M comes from the Quantifier choosing a central value near the low-impact end. It says nothing about whether the 2% decline is right.

## RESPONSE TO "EVIDENCE WEAKNESSES"

> The Advocate claims: the 5–15% and 30–50% figures are self-labelled ungrounded, the critique's own "likely small by 2033–35" statement contradicts them, the cited models measure other things, and the Tait efficacy estimate is imprecise.

Response:

1. **Ungrounded figures: conceded.** The critique labels them as the Investigator's own estimates. I cannot supply a grounded replacement for 5–15%. Treat it as an uninformed prior.

2. **Timeline tension: largely conceded.**
   - "Likely small" at 2033–35 fits the low end, near 5% or below, better than the 15% end.
   - The India model's 2025 introduction is more optimistic than the critique's own feasibility view, as the Advocate says.
   - The defensible reading of the critique is therefore "year-8 effect from M72 is near the bottom of the range."

3. **Where the Advocate overreaches:** Tait's imprecision cuts both ways.
   - The CI of 2.1–74.2% means the true efficacy could be higher than 50% as well as lower.
   - Imprecision supports probability-weighting. It does not by itself support a smaller effect.
   - The Advocate's p × (5–15%) is fine as a direction. It is not evidence that the expected shock is small, because p is unspecified, and the Advocate admits it cannot ground one.

4. **The India and South Africa models.** I agree they do not establish a global year-8 pool change. The critique cited them for assumptions (duration, efficacy, staggered rollout), not for a year-8 number. The Advocate's objection is correct about what they do not show, but it does not engage with what they were cited for.

## RESPONSE TO "MAGNITUDE CHALLENGE"

> The Advocate claims: at −15% the SROI is ≈2,597x, above the ~2,000x bar and under the 25% change threshold, and reaching 2,000x would need a ~35% pool reduction.

Response:

1. **Largely correct, and I concede it.** The sensitivity output shows `crosses_bar_low: false`, and the pool enters linearly. Headroom is (3,055 − 2,000) / 3,055 ≈ 34.5%, which matches the Advocate's ~35%.

2. **Plausibility of a 35% reduction by year 8 from M72 alone.**
   - A uniform vaccine effect needs efficacy × effective coverage ≈ 35%.
   - At 50% efficacy, that is ~70% effective coverage of the incidence-generating population, with protection already operating.
   - Given Phase III only started in March 2024, I cannot make that scenario plausible by year 8. This is my own arithmetic, ignoring lags and age targeting, and it favors the Advocate.

3. **Minimum plausible magnitude is near zero for M72.** If licensure and scale-up slip past ~2030, the year-8 effect could be a few percent or less.

4. **What survives is narrow.**
   - The critique's "other incidence shocks" could in principle move the pool by more than M72 does, and nothing in the model tests that.
   - The 15% shock alone consumes about 44% of the headroom (15 / 34.5). Anything that stacks with it on the same parameter, such as a steeper secular decline than 2%/yr, gets closer to the bar.
   - The critique's materiality label is not borne out by the sensitivity run. The more accurate framing is "low-to-medium, horizon-dependent," as the critique's hypothesis itself says.

## RESPONSE TO "OFFSETTING FACTORS"

> The Advocate claims: omitted benefit channels, a possible notification rebound, and phased vaccine rollout offset a pool reduction.

Response:

1. **Omitted channels are not offsets to pool shrinkage.**
   - Morbidity, post-treatment mortality, transmission and diagnostic value are all functions of the number of patients treated.
   - If the pool shrinks 15%, those channels shrink with it. They are conservatism in the level of the estimate, not a counterweight to a pool change.
   - They are not quantified in the Advocate's defense or in the sensitivity output.

2. **A notification rebound is, by the Advocate's own disclaimer, an "uninformed prior" with no direction or size.**
   - It argues that the direction of other incidence shocks is uncertain, which supports modelling a range rather than a point.
   - It does not support the point estimate.

3. **The rollout-targeting argument is conditional.**
   - It rests on M72 being tested in IGRA-positive adults in Phase IIb.
   - I cannot verify whether Phase III restricts eligibility the same way. The Phase III target of ~26,000 participants is in the critique, but its eligibility criteria are not.
   - The argument does reinforce "small effect at year 8."

## KEY UNRESOLVED QUESTIONS

- Is the 2%/yr decline a placeholder, a global trend, or a country-weighted estimate? Does it already assume some non-vaccine scale-up?
- Does the model hold the pool constant between the baseline and the accelerated scenario, so that a smaller pool reduces the value of a 1-year speedup at the same proportional rate?
- What is the probability and timing of M72 licensure and rollout? Neither side can ground this.
- Should a Phase III failure scenario, p, be formally included? A failure leaves the pool unchanged, which is itself informative.
- Are there non-vaccine incidence shocks of comparable or larger size, such as funding changes or post-COVID notification trends, whose direction cannot be established from this evidence package?

### Judge Audit
Surviving strength: weak
Justification: Unlike the template case, the critique is weak here because the debate was *productive* and tested it.
- The Advocate's linear-sensitivity argument went unchallenged. It was grounded in the sensitivity output, and the Challenger independently confirmed it.
- The Challenger conceded the horizon point, the ungrounded status of 5–15%, and the timeline tension placing the realistic effect near the low end.
- What remains is the critique's framing that the shock "should be modelled." That rests mainly on call-to-ignorance about unspecified other shocks, plus the acknowledged lack of justification for 2%/yr.
The critique's direction (downward) is accepted. Its materiality is not.
Recommended action: 1. CONCLUDE NOW: With moderately high confidence, an M72-driven incidence shock does not materially change this CEA.
   - The horizon-averaged reduction is inapplicable to the one-year-speedup structure.
   - The plausible year-8 effect lies at the low end of an ungrounded 5–15% range.
   - Even the 15% upper bound leaves SROI near 2,600x, above the bar.
   - The critique's valid residual is presentational: the 2%/yr secular decline is undocumented, and the model lacks an explicit incidence-shock sensitivity.

   Cheap remediation is feasible now. Add a sensitivity row varying the secular decline (for example 2% vs 4%/yr) jointly with a 0/5/15% year-8 vaccine shock.
   - As an illustration of my own arithmetic: 4%/yr compounded over 8 years gives 0.96^8 ≈ 0.721, versus 0.851 at 2%/yr. That is a pool ratio of ≈0.85.
   - Combining that with a −15% vaccine shock gives ≈0.72 of the baseline pool, or SROI ≈2,200x. This is still above the bar.
   - The row would make the robustness visible without further evidence-gathering.
   - Documenting the source of the 2%/yr assumption should accompany it.
Action feasibility: actionable_now
Advocate failures: ['sound_synthesis_noted: The back-calculation "1 − 0.98^8 ≈ 14.9% … 5.5 / 0.851 ≈ 6.5M" is labelled as the Advocate\'s own derivation from published numbers. The Challenger accepted it as arithmetically correct but conditional on the compounding structure.', 'sound_synthesis_noted: The magnitude challenge is well grounded. Because the pool enters linearly, SROI moves from 3,055x to about 2,597x at −15%, and `crosses_bar_low: false`. Reaching the ~2,000x bar would need a ~35% pool reduction. This uses the sensitivity output directly, and the Challenger independently confirmed it (34.5%).', 'unsupported_estimate_fabricated: Concession 2 says "a realistic vaccine contribution would lower the year-8 pool somewhat, probably a few percent." No derivation is given. It is directionally consistent with the verifier\'s "likely small by 2033–35," but the number itself is asserted. This is minor.', 'false_definitiveness: Offsetting factor 1 says the omitted benefit channels are "far from tiny relative to a 5–15% pool adjustment." No quantification is offered. The argument is also a logical error. Morbidity, post-treatment mortality and transmission benefits scale with the number of patients treated, so they shrink along with the pool rather than offsetting its reduction. The Challenger correctly identified this.', 'call_to_ignorance: Offsetting factor 2 says that if notifications are rebounding, "a 2%/yr decline could be too steep, which would offset a vaccine shock." The Advocate honestly labels the WHO recollection as an uninformed prior. It still functions as speculative filler on the Advocate\'s side of the ledger.', 'misrepresenting_evidence_status: Offsetting factor 3, "Vaccine impact is concentrated in the wrong population," does not engage the verifier\'s caveat. That caveat marks "impact accrues gradually" as PARTIALLY CONTRADICTED. It notes that Harris et al. found M72 has a *more rapid* incidence impact because it acts on the prevalent latent pool, which generates much adult disease. The Advocate\'s framing implies a slower and narrower effect without acknowledging this. The coverage-limited-rollout point is still fair and is flagged as conditional.']
Challenger failures: ["sound_synthesis_noted: Two of the Challenger's calculations are sound. First, the headroom figure: (3,055 − 2,000)/3,055 ≈ 34.5%, with a 15% shock consuming ~44% of it. Second, the feasibility check: efficacy × effective coverage ≈ 35% would require ~70% effective coverage at 50% efficacy. Both are explicitly labelled as the Challenger's own arithmetic, and the Challenger concedes they favor the Advocate.", 'call_to_ignorance: Under "What survives," the Challenger says "other incidence shocks could in principle move the pool by more than M72 does," and that a steeper secular decline "gets closer to the bar." Neither the size nor the direction of these shocks is evidenced. The Challenger\'s own unresolved-questions list admits their direction "cannot be established from this evidence package.', 'strawmanning: The Challenger writes that "the Advocate has no answer to that" about whether 2%/yr is the right size. The Advocate had not claimed it was correct. The Advocate explicitly conceded it is "not justified in the text." This is a mild mischaracterization of the Advocate\'s position rather than a full category swap.']
Debate resolved: The horizon-averaged 20–35% and later-year 30–50% figures have no counterpart in a CEA that credits a one-year adoption speedup at the year-8 pool. Both sides agreed on this, so only the year-8 pool shock is relevant.

Even the critique's worst-case year-8 shock (−15%) leaves SROI at about 2,600x. That is above the ~2,000x bar and under the 25% change threshold. Both sides also agreed that M72 alone cannot plausibly produce the ~35% reduction needed to cross the bar by year 8.
Debate unresolved: Whether the unjustified 2%/yr secular decline is the right size remains open, along with whether non-vaccine shocks could stack with a vaccine effect on the same parameter. Neither side could ground the direction or size of these shocks.

It is also unsettled whether a pool shock applies equally to the baseline and accelerated scenarios. This matters for whether linear scaling is the right sensitivity model.