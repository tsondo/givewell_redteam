--- Critique: Selection-on-success makes the "conditional 10%" an upward-biased estimate (winner's curse), and it is not shrunk ---

### Advocate
**DEFENSE OF COEFFICIENT GIVING'S POSITION: Winner's-curse shrinkage on the 10% relative mortality reduction**

**EXISTING COVERAGE:**

1. **The 10% is not an observed effect.**
   - The BOTEC says "a positive result is *assumed* to cut that by 10% relative."
   - The Phase IIa/b trial the report cites showed speedier clearance of TB infection and reduced lung damage on chest X-ray. Those are surrogate endpoints, not mortality.
   - Winner's curse inflates an effect estimate that was observed in a trial selected for significance. The report does not say the 10% is such an estimate, and the critique concedes its derivation "is not established."
   - If the 10% is a planning assumption, there is no selected mortality estimate to shrink.
   - I cannot ground how CG chose 10%. This is a conditional argument: if 10% was a round-number assumption, the mechanism does not apply directly.

2. **The 40% `p_success` already discounts for optimism about the Phase II signal.**
   

### Challenger
REBUTTAL: Winner's-curse shrinkage on the 10% relative mortality reduction

**Note on the defense as received:** The Advocate's text cuts off after the heading of point 2 ("The 40% `p_success` already discounts for optimism about the Phase II signal"). No argument is given under it. I can rebut only the heading's logic, not support the Advocate never wrote.

---

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the 10% is a planning assumption ("a positive result is *assumed* to cut that by 10% relative"), not an effect observed in a trial selected for significance. So there is no selected estimate to shrink.

1. **Concede the narrow point.** If 10% is a round-number assumption with no empirical anchor, winner's curse does not apply mechanically. The critique already conceded its derivation "is not established," so we agree on this.

2. **The Advocate also says "I cannot ground how CG chose 10%."** The defense is therefore conditional, just as the critique is.
   - Neither side knows whether 10% is anchored.
   - The Advocate has not shown the anchor-free branch is the more likely one.

3. **A planning assumption is rarely free of anchors.**
   - A 10% figure was most plausibly chosen with reference to something: the Phase IIa/b surrogate results (faster clearance, less lung damage), the adjunct literature, or the size of effect needed to matter.
   - If it was anchored to the surrogate signal, the bias enters through the anchor, even though the number is not literally "observed."
   - This is conditional. The verifier did not establish the anchor, and the claim is UNVERIFIABLE, not rejected.

4. **The "conditional on positive result" framing is the relevant structure.** The model applies 10% given success. Success is defined by clearing a bar, and effects conditional on clearing a bar are biased upward relative to the unconditional true effect. Whether the model's 10% already reflects this depends on how it was set. The Advocate has not shown it does.

> The Advocate claims: the 40% `p_success` already discounts for optimism about the Phase II signal.

5. **The argument is cut off, so I can only address the structure.**
   - `p_success` and `relative_reduction` are separate multiplicative terms.
   - Lowering the probability of success scales expected value linearly. It does not change the effect size assumed if success occurs.
   - Counting `p_success` as coverage requires that it was set specifically to absorb effect-size optimism rather than the probability of clearing regulatory or trial thresholds. I see nothing in the Advocate's text showing that.

---

**RESPONSE TO "EVIDENCE WEAKNESSES":**

1. The Advocate's strongest evidentiary point is the critique's own concession: there is nothing TB-specific on shrinkage. I do not dispute that.

2. The verifier's corticosteroid evidence cuts partly against the critique.
   - The pooled RR of 0.84 is a ~16% reduction, above the 10% assumed.
   - The adjunct benchmark therefore does not suggest 10% is inflated.
   - Caveat: TB meningitis corticosteroids are a different condition and mechanism from a host-directed therapy for pulmonary TB, so this is only a loose reference.

3. The Cochrane comparison is weak but directionally consistent with small-sample inflation.
   - The older pooled RR was 0.79 (six trials, 595 patients). The later, larger pooled RR was 0.84.
   - That is a 21% vs 16% relative reduction, a ratio of 16/21 ≈ 0.76.
   - This sits at the top of the critique's illustrative 0.5–0.8 range, not the middle.
   - The verifier called it "not a clean test." It is one comparison in one condition, so it should not be given much weight.

4. The critique's 0.5–0.8 range is not empirically derived. The evidence supports "shrinkage direction is plausible," not "shrinkage is 20–50%."

---

**RESPONSE TO "MAGNITUDE CHALLENGE":**

1. SROI scales linearly in `relative_reduction`. The critique's figures (1,500–2,400x at rr 0.05–0.08) imply a baseline of roughly 3,000x at 0.10.

2. The best-grounded shrinkage factor is the Cochrane-derived ~0.76, which gives rr ≈ 0.076 and SROI ≈ 2,300x. That is about a 24% reduction in cost-effectiveness.

3. At that level the SROI remains very large. A 24% cut changes the decision only if the funding bar sits close to the estimate. The Advocate will likely stress this, and I concede it.

4. The residual risk lies in the lower end of the range.
   - At a 0.5 factor, SROI falls by half.
   - That end has no empirical backing, so it belongs in a sensitivity analysis, not a point estimate.

---

**RESPONSE TO "OFFSETTING FACTORS":**

1. The Advocate offers no quantified offsets in the text provided.

2. The one offset implied is `p_success`. As argued above, it does not substitute for effect-size shrinkage unless it was explicitly set to do so.

3. The corticosteroid benchmark (16% > 10%) is the one real offset in the evidence package. It suggests a conservative baseline, but it is a cross-condition analogy.

---

**KEY UNRESOLVED QUESTIONS:**

- What anchored the 10%: the surrogate trial, the adjunct literature, or an unanchored round

### Judge Audit
Surviving strength: weak
Justification: The Challenger conceded every load-bearing point:
- The mechanism does not apply if 10% is a planning assumption.
- The 0.5–0.8 range has no empirical basis.
- The adjunct benchmark (16%) suggests 10% is conservative.
- Even the "best-grounded" shrinkage (~0.76) leaves SROI near 2,300x and likely does not change the decision.
The Challenger's remaining case rests on an unsupported "planning assumptions are rarely anchor-free" claim and on the conditional-versus-unconditional conflation the verifier had already flagged. The critique survives mainly because the Advocate's defense was truncated and left strong rebuttals unused, not because the critique was substantiated.
Recommended action: 1. CONCLUDE NOW: The winner's-curse argument is not established, and the available benchmark points the other way: adjunct mortality effects of ~16% exceed the assumed 10%. Confidence: moderate.
   - The critique's narrow residue is reasonable but low-impact. Report a one-line sensitivity on `relative_reduction` over roughly 0.05–0.15. Because SROI scales linearly, this gives roughly 1,500x–4,500x around the ~3,000x base.
   - Separately, check the BOTEC notes or ask CG whether the 10% was derived from the Phase IIa/b surrogate results. Only if it was does the shrinkage argument warrant revisiting. This check is feasible with a single document lookup or query.
Action feasibility: actionable_now
Advocate failures: ['false_definitiveness: Point 2 says flatly that "The 40% `p_success` already discounts for optimism about the Phase II signal" and gives no supporting argument, because the text is truncated. It is stated as settled coverage with nothing behind it. It also ignores the structural fact that `p_success` scales expected value and leaves the effect size assumed on success unchanged.', 'sound_synthesis_noted: Point 1 is clean conditional reasoning. It quotes the BOTEC ("a positive result is *assumed* to cut that by 10%"), notes that the trial\'s endpoints were surrogates rather than mortality, and says openly, "I cannot ground how CG chose 10%. This is a conditional argument." This is the correct way to handle an unverifiable premise.']
Challenger failures: ['misrepresenting_evidence_status: Point 4 says "effects conditional on clearing a bar are biased upward relative to the unconditional true effect." The verifier stated explicitly that conditioning on success raises the posterior mean of the *true* effect, so the CEA\'s conditional 10% "is not automatically biased." The relevant bias is observed versus true conditional effect, not conditional versus unconditional. The Challenger repeats the conflation the verifier flagged.', 'unsupported_estimate_pseudo: The Challenger first says the Cochrane 0.79→0.84 comparison "should not be given much weight." Two sections later it is called "the best-grounded shrinkage factor" (~0.76), and from it come rr ≈ 0.076, SROI ≈ 2,300x, and "about a 24% reduction." The arithmetic is correct (16/21 ≈ 0.76, with linear scaling). The gap is in applying it. A ratio between an older and a newer meta-analysis of a different intervention, with partly overlapping trial sets, is not a selection-on-significance shrinkage factor. It also cannot be applied to a number whose derivation is unknown.', 'call_to_ignorance (mild): A planning assumption is rarely free of anchors… most plausibly chosen with reference to something." This general claim has no support and fills the gap left by the unknown derivation. It is partly mitigated by the explicit statement "This is conditional… UNVERIFIABLE, not rejected.', 'sound_synthesis_noted: Point 5 reasons correctly that `p_success` and `relative_reduction` are separate multiplicative terms. The Challenger also concedes, with integrity, that the corticosteroid benchmark (16% > 10%) cuts against the critique. It concedes that the 0.5–0.8 range is not empirically derived, and that a ~24% cut likely does not change the decision.']
Debate resolved: Both sides agree that winner's-curse shrinkage applies only if the 10% is anchored to an observed effect from a selected trial, and that this anchor is not established. They also agree on two further points:
- `p_success` does not substitute for effect-size shrinkage unless it was explicitly set to do so.
- The only external benchmark (corticosteroid adjuncts, ~16%) does not suggest the 10% is inflated.
Debate unresolved: The main open question is what anchored the 10%: the surrogate Phase IIa/b signal, the adjunct literature, or an unanchored round number. Linked to it is whether the figure represents an observed-effect estimate or a posterior mean conditional on success. A second open question is whether `p_success` was intended to absorb effect-size optimism; the Advocate's truncated point 2 left this unaddressed.

--- Critique: A mortality-powered Phase III costs several multiples of $7M, and trial-population mortality makes it worse ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: A mortality-powered Phase III costs several multiples of $7M

EXISTING COVERAGE:
- The BOTEC never says the Phase III is powered on all-cause mortality.
  - The report says only that "Phase II and Phase III trials both succeed" (40%) and that all-in costs include "

### Challenger
REBUTTAL: A mortality-powered Phase III costs several multiples of $7M

**Caveat on the record:** The Advocate's defense is truncated. It contains one visible bullet, which cuts off mid-sentence ("all-in costs include "), and nothing after that. I rebut only what is actually stated. I cannot rebut any offsetting-factor or magnitude arguments that may have been intended, and the Judge should not credit the defense with arguments it did not make.

---

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: The BOTEC never says the Phase III is powered on all-cause mortality. It says only that "Phase II and Phase III trials both succeed" (40%) and that all-in costs include [truncated].

- **Concede the textual point.** I cannot verify from the excerpt that the BOTEC specifies a mortality endpoint. The original critique already hedged on this ("large if the CEA assumes a mortality-powered Phase III, otherwise conditional"). The Advocate's point therefore confirms the critique's own conditional. It does not refute it.
- **The silence cuts the other way on cost.** If the BOTEC specifies no endpoint, the $7M all-in figure has no stated design behind it.
  - The verifier's evidence puts reported TB trial costs at US$7–221M, so $7M is the very bottom of the range.
  - TB-PRACTECAL cost €33.9M. A TB vaccine trial model for 12,000 infants was $120M.
  - A budget at the floor of the observed range, with no stated design, is not "covered." It is unexamined.
- **Endpoint silence is not endpoint neutrality.** If the SROI benefit is calculated as mortality averted, which I cannot confirm from the excerpt, a trial that does not measure mortality leaves a gap between the trial's evidence and the benefit being valued.
  - Conditional argument: if the benefit is mortality-based, then either the trial is powered for mortality (the critique's large-N case) or it uses a surrogate. A surrogate would need its own justification and would add a translation-risk discount that the "40% success" figure may not include.
  - I cannot ground whether the BOTEC makes this link, so treat this as a conditional, not an assertion.

---

**RESPONSE TO "EVIDENCE WEAKNESSES":**

- The visible defense raises no objection to the sample-size arithmetic. I rechecked it: 7.84 × (0.06×0.94 + 0.054×0.946) / 0.006² ≈ 23,400 per arm, and the 3% case gives ≈ 48,200 per arm. Both match.
- The per-participant cost is the weakest link, and the critique already says so ("ungrounded"). The verifier found no evidence that $500–$1,000 is realistic and some evidence that it is a floor.
  - TB-PRACTECAL's €61,460 per patient is not comparable, as the verifier notes.
  - The vaccine model's $7,500 per subject is also not comparable.
  - Neither source supports $500–$1,000 as an upper range.
- Even if cost per participant were halved to $250, 47,000 participants would cost about $11.8M, which is still above $7M before any fixed costs. The critique's direction does not depend on the exact per-head figure.

---

**RESPONSE TO "MAGNITUDE CHALLENGE":**

No magnitude argument appears in the visible defense. I address the verifier's counter-considerations, which the Advocate would likely invoke.

- **Concede: enrichment and larger assumed effects shrink N dramatically.**
  - My derivation: at 50% baseline mortality (TBM upper bound per the verifier) and a 30% relative reduction (IMPI's hypothesis), 50% → 35% gives n ≈ 7.84 × (0.25 + 0.2275) / 0.15² ≈ 166 per arm, about 333 total.
  - At that scale, $7M is plausible.
- **But the shrinkage comes with a population and effect-size trade-off.**
  - TBM is a small fraction of TB cases. Benefit would have to be restricted to that population, and the BOTEC's benefit scale would have to match. I cannot confirm that it does.
  - A powered-for-30% trial that faces a true 10% effect is underpowered. IMPI (1,400 participants, hypothesised 30%, no mortality benefit shown) illustrates that this design risk is real. It argues for a lower probability of Phase III success than 40%, not just a lower cost.
- **Minimum plausible magnitude, by scenario.**
  - Enriched high-mortality design: cost may be consistent with $7M, and the critique largely fails.
  - Unenriched design powered for 10% at 6% baseline: about 47,000 participants. Even at a hypothetical $250 per head, that is about $11.8M, above the $10.7M "below the bar" line.
  - The critique therefore survives in full for the unenriched design and mostly dissolves for the enriched one. The open question is which design the CEA implies.

---

**RESPONSE TO "OFFSETTING FACTORS":**

- The visible defense contains no offsetting factors.
- The verifier's "pragmatic or registry-embedded trials can cost far less per participant" is unquantified. I cannot ground a per-participant figure for such designs in TB, and no source in the verifier package supplies one. It is a possibility, not a model input.
- Such a design would also have to deliver mortality ascertainment at scale in TB-endemic settings. I cannot ground whether that is feasible at ≤$150 per participant, the level needed to get 47,000 participants under $7M, so treat that as an uninformed prior.

---

**KEY UNRESOLVED QUESTIONS:**

- Does the BOTEC's benefit calculation depend on mortality reduction? If so, what endpoint does the Phase III need to support policy adoption?
- What is the truncated "all-in costs include…" clause? Does it itemize per-participant trial costs or only a lump sum?
- Is the 40% Phase II/III joint success probability consistent with a trial powered for a larger effect than the true effect (the IMPI pattern)?
- Is there any TB trial of comparable end

### Judge Audit
Surviving strength: moderate
Justification: - **What the Challenger established.** It made grounded, verified arithmetic arguments. The Advocate never contested them because the defense was truncated.
- **What the Challenger conceded.** It also conceded that the critique "mostly dissolves" under enrichment or larger-effect powering.
- **The Advocate's one point lands on the crux.** The single visible point (no stated mortality endpoint) lands on exactly that hinge. The critique's own cited reference class (pivotal TB trials of 450–2,500 participants) suggests the CEA's default is a non-mortality-powered design.
- **Why the strength is no higher.** The critique survives as a valid conditional, but its large-magnitude version rests on an unestablished design assumption and on ungrounded per-participant costs. That prevents a "strong" rating. The debate was lopsided because of truncation, not because the Advocate lost the substantive exchange.
Recommended action: 2. SPECIFIC INVESTIGATION: Read the full BOTEC/report text that the Advocate quoted, specifically the truncated "all-in costs include…" clause and the benefit derivation. Three questions need answers:
   - (a) Is the SROI benefit computed from mortality averted?
   - (b) Does the $7M figure itemize a trial design (sample size, endpoint, population)?
   - (c) Is the Phase III modelled on standard TB regimen trials using composite unfavorable-outcome endpoints?
   
   This is feasible now with existing materials.
   
   How to use the answers:
   - **If the CEA assumes a standard-endpoint trial:** conclude that the critique does not apply, apart from a smaller residual concern about surrogate-to-mortality translation risk.
   - **If the CEA assumes a mortality-powered, unenriched trial:** conclude that the critique holds in direction, with all-in cost likely above $10.7M. Treat the specific dollar figures and the "70% or more" SROI decline as illustrative only.
Action feasibility: requires_specified_evidence
Advocate failures: ['generic_recommendation: Not a recommendation failure. The defense is truncated after one bullet ("all-in costs include "), so it offers no argument on magnitude, offsetting factors or evidence weaknesses. This is recorded under this label only because the parser needs an entry. The real defect is non-engagement, not a reasoning error in what was written.', 'sound_synthesis_noted: The one visible point is valid and well aimed. The BOTEC "never says the Phase III is powered on all-cause mortality." This targets the critique\'s own conditional ("large if the CEA assumes a mortality-powered Phase III").']
Challenger failures: ['sound_synthesis_noted: The Challenger rechecked the sample-size arithmetic, and the figures are correct:', 'sound_synthesis_noted: The Challenger conceded the strongest counter-case (enriched, larger-effect design: "$7M is plausible… the critique largely fails"). It also correctly reduced the critique to a scenario split. This is good-faith engagement, not a defect.', 'unsupported_estimate_pseudo: IMPI... illustrates that this design risk is real. It argues for a lower probability of Phase III success than 40%." IMPI is a single trial of an adjunctive steroid in TB pericarditis. One null result in a different intervention class does not entail that the CEA\'s 40% joint success probability is too high. The inferential gap is moderate. The direction is plausible, but it is not established.', 'misrepresenting_evidence_status: $7M is the very bottom of that range." The challenge is to US$7–221M per trial as a benchmark. The Challenger acknowledges that the TB-PRACTECAL and vaccine figures are not comparable, then still lists them as evidence that $7M is "unexamined." The figures come from different trial types (DR-TB with hospital care, infant vaccine). Using them to imply the CEA\'s figure is too low overstates what they show. This is a mild instance and partly self-corrected by the Challenger\'s own caveats.', 'call_to_ignorance: A surrogate would need its own justification and would add a translation-risk discount that the \'40% success\' figure may not include." This is offered as a conditional and explicitly flagged as ungrounded. It is borderline: it adds an unquantified penalty without evidence that the CEA omits it.']
Debate resolved: - **The arithmetic is correct.** An unenriched trial powered to detect a 10% relative mortality reduction at a 3–6% baseline needs roughly 47,000–96,000 participants. At any plausible per-participant cost, that would exceed $7M.
- **The critique is purely conditional on design.** Both sides effectively agree that the critique largely dissolves if the Phase III is enriched (high-mortality population) or uses a non-mortality or larger-effect design.
Debate unresolved: - **Which design the CEA implies.** It is still unclear whether the BOTEC's benefit stream requires mortality-level evidence. It is also unclear whether its $7M all-in figure was built around a standard TB regimen-trial design (which the Advocate's truncated point suggests). This is the crux, and neither side could settle it from the visible text.
- **Whether the 40% success probability absorbs surrogate-endpoint and underpowering risk.** This remains open.

--- Critique: If Phase III is surrogate-powered, costs and benefits describe different interventions ---

### Advocate
```
DEFENSE OF GIVEWELL'S POSITION: If Phase III is surrogate-powered, costs and benefits describe different interventions
(Funder read as Coefficient Giving; "GiveWell" below means CG)

EXISTING COVERAGE:
1. The BOTEC states the 10% relative mortality reduction as conditional on success ("a positive result is assumed to cut that by 10%"). It is not presented as a tested Phase III estimate. The risk that a trial succeeds on its endpoint without delivering the assumed mortality benefit is the kind of thing `p_success` = 40% is meant to absorb. The BOTEC does not say how that 40% decomposes, so I cannot show it covers this specific gap. I only claim the model has a place for it.
2. All-in cost explicitly includes "later Phase III trials, guideline changes, dissemination and validation" (~$7M). The BOTEC therefore budgets a path to guideline change. It does not budget only a surrogate readout.
3. The 1-year `speedup_years` is the grant's counterfactual acceleration. It is not a forecast of how fast WHO adopts. If surrogate-only evidence slows guideline uptake, that slowdown applies in the no-grant world too, because the same evidentiary bar governs whoever eventually runs the trials. The slowdown therefore largely nets out of the speedup. It mainly affects the level of the 60% uptake figure. This is my reasoning, not an attested finding.

EVIDENCE WEAKNESSES:
1. The Evidence field is empty and the Sensitivity Results are `{}`. The critique's central premise, that Phase III is surrogate-powered, is a conjecture. The critique itself says the actual endpoint "must be confirmed." The BOTEC states no Phase III endpoint, so this is a conditional argument, not a finding.
2. The critique also concedes that "the claim that surrogate-only evidence would block or delay a WHO recommendation is not established for regimen-type trials." That is the load-bearing step for the adoption-delay branch. It is conceded as unestablished by the critique's own author.
3. The corticosteroid precedent for TB meningitis is a poor fit. It is a single adjunct for a specific high-mortality form of disease, where mortality was the natural endpoint. Atorvastatin is proposed for all drug-susceptible TB at ~6% baseline mortality. The analogy shows mortality evidence is sufficient. It does not show it is necessary here.
4. The relevant TB precedents lean toward composite endpoints. As I recall them (not verified here), WHO's 2022 recommendations for the BPaLM regimen and the 4-month rifapentine-moxifloxacin regimen rested on trials (TB-PRACTECAL; Study 31/A5349) whose primary endpoints were composite unfavourable outcome or TB-free survival. Death is a component of those composites. The critique itself notes that "unfavourable outcome is a patient-important composite, not a pure surrogate," which weakens the GRADE-indirectness framing. These precedents are regimen-replacement trials, so the analogy to an adjunct is imperfect.
5. Atorvastatin is generic, cheap and widely used, and its safety profile is well characterised. I expect that lowers the evidentiary bar for a conditional or off-label recommendation compared with a novel agent. I cannot cite a specific WHO decision showing this.

MAGNITUDE CHALLENGE:
1. The critique offers no magnitude, so there is nothing to compare against. "Notable" materiality is asserted, not shown.
2. The adoption-delay branch has a bounded effect on SROI. The headline is ~3,000x against a ~2,000x bar, so SROI must fall by about one third to cross the bar. If the delay only reduces uptake from 60% to, say, 40%, SROI falls by one third, which is borderline. I have no grounded basis for that 40% figure; it is purely illustrative. A pure delay of the speedup is mostly netted out (Existing Coverage point 3).
3. The mortality-powered branch is not a new finding. By the critique's own account it "collapses into Critique 1," so it is the same cost-uncertainty issue and cannot be counted twice.
4. I tried to sanity-check feasibility. Detecting 6% → 5.4% mortality (two-sided α = 0.05, 80% power) needs about (1.96+0.84)² × 2(0.057)(0.943) / (0.006)² ≈ 23,000 per arm, roughly 47,000 patients. At $7M all-in that is

### Challenger
REBUTTAL: If Phase III is surrogate-powered, costs and benefits describe different interventions

*Note: the Advocate's defense is cut off mid-sentence in the magnitude section, and the verifier's evidence package is empty. I respond to what is visible and mark where I rely on unverified recall.*

**RESPONSE TO "EXISTING COVERAGE":**

> The Advocate claims: the 10% mortality reduction is conditional on success, so the risk that a trial succeeds without delivering that benefit is absorbed by `p_success` = 40%. The Advocate concedes they cannot show how the 40% decomposes.

- A place in the model is not coverage. The Advocate admits the 40% is undecomposed, so this point is a hypothesis.
- The gap is conditional on trial success. P(mortality benefit of 10% | surrogate or composite success) is a separate factor from P(trial hits its primary endpoint). Unless the 40% explicitly multiplies in that second factor, the BOTEC credits the full 10% whenever the trial "succeeds."
- The Advocate's feasibility calculation cuts against the Advocate's position, and I verified the arithmetic.
  - n ≈ 7.84 × 0.1075 / 0.006² ≈ 23,400 per arm, or about 47,000 patients in total.
  - $7M ÷ 47,000 ≈ $150 per patient all-in, covering Phase III, guideline work and dissemination. That is not plausible for a TB trial with follow-up.
  - So the budgeted Phase III is very unlikely to be mortality-powered. That is the surrogate or composite branch of this critique, not the branch that "collapses into Critique 1."
- The "later Phase III trials, guideline changes…" line item shows a path to guideline change is budgeted. It does not show the trial can test the benefit being credited. The Advocate says this item "does not budget only a surrogate readout," but the cost scale is consistent with exactly that.
- **The netting-out argument (point 3) fails in the branch that matters.**
  - It is valid for a pure slowdown. If both worlds adopt slowly, the speedup is unchanged.
  - The critique's concern is different. If WHO needs mortality evidence, a surrogate-powered grant trial does not trigger a guideline in either world.
  - In that case the grant-world guideline waits for a later mortality trial, and the 1-year `speedup_years` can fall toward zero. The speedup exists only if this trial is sufficient for adoption.
  - The Advocate's own caveat applies: "my reasoning, not an attested finding."

**RESPONSE TO "EVIDENCE WEAKNESSES":**

> The Advocate claims: the surrogate-powered premise is conjecture, and the critique concedes that blocked or delayed adoption is not established for regimen trials.

- The Evidence field is empty and the verifier found nothing. That is an absence of grounding, not a REJECTED verdict.
- The critique is explicitly conditional ("the grant's actual Phase III endpoint must be confirmed"). The BOTEC's silence on the endpoint is the gap the critique identifies. The question is why a $7M budget and a mortality-based benefit are paired without stating the endpoint.
- I concede the corticoste

### Judge Audit
Surviving strength: moderate
Justification: The Challenger turned the Advocate's own sound power calculation into a grounded argument that the trial cannot test the credited mortality benefit. The Challenger also correctly separated P(endpoint success) from P(mortality benefit | success), and the Advocate's "the model has a place for it" defence does not answer that distinction. However, the critique's adoption-blocking mechanism remains unsupported: the verifier found no evidence, the critique
Recommended action: 
Action feasibility: open_question
Advocate failures: ['unsupported_estimate_fabricated: If the delay only reduces uptake from 60% to, say, 40%, SROI falls by one third, which is borderline." The Advocate discloses that the 40% is "purely illustrative" with "no grounded basis." That disclosure mitigates the failure but does not remove it. The figure lands exactly at the bar-crossing threshold (3,000x → 2,000x), so it frames the magnitude question without informing it.', 'sound_synthesis_noted: The power calculation is correct: (1.96+0.84)² × 2(0.057)(0.943) / 0.006² ≈ 23,400 per arm, about 47,000 total. Every input is stated and the arithmetic checks. It is the most substantive analytic contribution in the debate.', 'false_definitiveness: Point 3 says the slowdown "largely nets out" of the speedup and treats this as a near-resolution. It is stated as the Advocate\'s own reasoning. However, it is applied to the whole adoption-delay branch, while it only holds for a symmetric slowdown, not for a trial that is insufficient to trigger a guideline.']
Challenger failures: ['sound_synthesis_noted: $7M ÷ 47,000 ≈ $150 per patient all-in… not plausible for a TB trial with follow-up." This is a valid inference from the Advocate\'s own grounded number. It correctly concludes that the budgeted trial is very unlikely to be mortality-powered, which moves the debate into the surrogate or composite branch.', 'call_to_ignorance: the 1-year `speedup_years` can fall toward zero." The claim is framed conditionally ("If WHO needs mortality evidence"). But the Challenger offers no evidence that the condition is likely, and the critique itself conceded it is "not established for regimen-type trials." The Challenger also does not notice that its own $150/patient argument implies a mortality trial is unlikely ever to be run. That makes "WHO requires mortality evidence" a scenario where neither world adopts. It is a reduction in the effective probability of success, not a loss of speedup specifically.', 'sound_synthesis_noted: P(mortality benefit of 10% | surrogate or composite success) is a separate factor from P(trial hits its primary endpoint)." This is a correct structural point about the BOTEC. The Advocate\'s "a place in the model" response does not answer it.']
Debate resolved: The arithmetic establishes that a trial powered to detect a 10% relative mortality reduction at about 6% baseline needs about 47,000 patients, which is incompatible with a ~$7M all-in budget. The mortality-powered branch is effectively ruled out, and the grant's trial must be surrogate- or composite-endpoint. It is also established that the BOTEC credits the full 10% mortality benefit on "success" without showing that the 40% `p_success` includes a separate mortality-translation factor.
Debate unresolved: Neither side grounded whether WHO would issue a recommendation for a host-directed adjunct on composite unfavourable-outcome evidence. The regimen-replacement precedents suggest yes, but they come from unverified recall and the analogy is imperfect. Also unresolved is whether the 40% `p_success` already discounts for "endpoint met but mortality benefit smaller than 10%."

--- Critique: WHO is unlikely to rely on a single trial ---

### Advocate
DEFENSE OF GIVEWELL'S POSITION (CG's BOTEC): WHO is unlikely to rely on a single trial

**EXISTING COVERAGE:**
- The $7M is explicitly "all-in." It includes "later Phase III trials, guideline changes, dissemination and validation," not just the $320K Phase IIc. The critique's premise that $7M "funds only one Phase III trial" is the Challenger's reading, not something the BOTEC says.
- The BOTEC does not state a Phase III size or number, so the critique and the BOTEC are both silent on the same point.
- The 40% `p_success` covers "Phase II and Phase III trials both succeed." An ambiguous or insufficient Phase III result, which is what would prompt WHO to ask for more evidence, is already inside the 60% failure mass for the pathway.
- The effect size is framed as conditional on a positive result. The BOTEC therefore already assumes a result strong enough to change guidelines.
- The funded Phase IIc tests survival, infection clearance and lung damage. The program is aimed at a hard clinical endpoint (survival), which the Challenger's own evidence says makes a single trial more likely to suffice.

**EVIDENCE WEAKNESSES:**
- The Challenger labels the hypothesis UNGROUNDED, finds nothing on the $7M figure, and admits that the cost direction "is an assumption, not a finding." The critique has no evidence that the budget is too low.
- The Challenger's best precedent, R21/Matrix-M, cuts against the critique. WHO recommended it on the basis of one large Phase III trial plus supportive data (Datoo et al., *Lancet* 2024, as summarized in the verifier evidence). That contradicts the claim that WHO is "unlikely to rely on a single trial."
- The verifier evidence says TB treatment guidance is more demanding. It does not say a single trial is insufficient: "several trials, or a single large multi-site trial with a high certainty rating under GRADE."
- A TB example supports this. WHO's 2022 recommendation of the 4-month rifapentine–moxifloxacin regimen rested mainly on one multi-country Phase III trial, Study 31/A5349 (Carr et al., *NEJM* 2022). I am recalling this from memory and have not verified it in the evidence package, so treat it as moderately confident. If correct, single-trial TB recommendations have precedent.
- The vaccine precedent (R21) does not transfer cleanly to a TB drug adjunct. The TB regimen precedent is a better match but is not independently verified.
- Sensitivity Results are empty, so the critique carries no quantified effect.

**MAGNITUDE CHALLENGE:**
- Derivation of the break-even cost, using the BOTEC's own numbers:
  - SROI = (54B / 7M) × 0.40 = 7,714 × 0.40 ≈ 3,086x.
  - The ~2,000x bar is crossed when cost = (54B × 0.40) / 2,000 = $10.8M.
  - All-in cost would therefore have to rise about 54% ($7M → $10.8M) to fall below the bar.
- Whether an extra trial triggers this depends on the Phase III share of the $7M, which is not given. Even then, it requires a full additional trial, not a modest overrun.
- The Challenger offers no cost figure, and the verifier found none, so I cannot say whether the shortfall would be 10% or 100%.
- Extra evidence requirements may be smaller than a second trial. They could be supplementary safety or PK data, or a pooled or extended analysis, which costs far less than a second Phase III.
- A higher-cost scenario would also likely apply to the counterfactual timeline. If WHO would demand more evidence anyway, then without the grant adoption would be delayed by the same requirement. That affects the speedup framing as much as the cost, and the critique does not model it.

**OFFSETTING FACTORS:**
- The BOTEC divides probability-weighted benefits by the full $7M. If Phase III and downstream costs are spent only after Phase IIc succeeds, expected cost is below $7M.
  - Illustration: assume Phase IIc succeeds with probability p₂ and Phase III plus downstream spend is about $6.7M. Expected cost = $0.32M + p₂ × $6.68M.
  - At p₂ = 0.6 (an assumed value I cannot ground), expected cost ≈ $4.3M, which would raise SROI by about 60%.
  - This is an uninformed illustration of direction, not an estimate. It shows the conservative treatment of costs partly offsets overrun risk.
- Atorvastatin is generic and cheap. Cost pressure from extra evidence generation falls on trial costs, not on drug-delivery costs.
- The 10% relative reduction in mortality and the 60% uptake are assumptions that the BOTEC does not shrink or inflate. The critique does not argue they are too high, so they remain unchallenged offsets or baselines.

**OVERALL ASSESSMENT: Strong defense** (leaning toward Partial on the cost-overrun point)
- The critique's strong form ("unlikely to rely on a single trial") is undercut by its own R21 precedent and by the fact that the BOTEC's endpoint is survival.
- It is ungrounded on cost direction and carries no quantified sensitivity.
- The weaker residual form, that a TB treatment guideline may need more than one trial, is plausible and has some verified support.

**CONCESSIONS:**
- The BOTEC gives no Ph

### Challenger


### Judge Audit
Surviving strength: weak
Justification: The critique was self-labeled UNGROUNDED and weak, and the verifier found no evidence on the $7M figure. The critique offered no magnitude. The Advocate's grounded break-even derivation shows that a substantial overrun is needed to change the conclusion. The Challenger presented no rebuttal, so the critique's only residual, plausible point (positive-but-insufficient single TB trials) went undefended and unquantified. The surviving element is a small, unmodeled cost-uncertainty channel.
Recommended action: 1. CONCLUDE NOW: The critique's headline claim is overbroad and contradicted by precedent. With moderate-to-high confidence, it does not materially threaten the BOTEC's conclusion, because a ~54% cost increase would be needed to cross the bar. One residual concern remains valid but minor: a positive single Phase III may be GRADE-downgraded for imprecision, prompting additional evidence generation. This is a cost-uncertainty caveat, not a failure. Optionally, the BOTEC could state an assumed Phase III budget and note the $10.8M break-even explicitly. This requires no new research.
Action feasibility: actionable_now
Advocate failures: ['sound_synthesis_noted: Break-even derivation: "SROI = (54B / 7M) × 0.40 ≈ 3,086x … bar crossed when cost = (54B × 0.40) / 2,000 = $10.8M … about 54%." Each step uses the BOTEC\'s own inputs and the arithmetic follows. This is the most useful contribution in the exchange because it gives a concrete threshold that any cost-overrun claim must clear.', 'sound_synthesis_noted: Staged-cost illustration: "Expected cost = $0.32M + p₂ × $6.68M … At p₂ = 0.6 (an assumed value I cannot ground)…" The p₂ value is ungrounded, but the Advocate labels it explicitly as "an uninformed illustration of direction, not an estimate." The directional logic is sound, and it is consistent with the joint 40% p_success, since p₂ must be at least 0.4. This is not flagged as fabricated because the transparency is adequate.', 'false_definitiveness: An ambiguous or insufficient Phase III result … is already inside the 60% failure mass" and "the BOTEC therefore already assumes a result strong enough to change guidelines." There is a logical gap here. The critique\'s scenario is a *positive* Phase III that WHO judges insufficient for a strong recommendation, which triggers extra cost rather than failure. "Both trials succeed" does not equal "guideline-sufficient." The verifier\'s TB draft makes this exact point: single trials are often downgraded for imprecision even when positive. The Advocate presents the coverage as settled when it is at most partial.', 'strawmanning: The critique\'s premise that $7M \'funds only one Phase III trial\' is the Challenger\'s reading, not something the BOTEC says." The critique states this conditionally ("may be unrealistic *if* it funds only one Phase III trial"). It does not assert it as a premise. The Advocate also repeatedly attributes the verifier\'s findings to "the Challenger" (e.g., "The Challenger … finds nothing on the $7M figure"). The misattribution is minor, but it blurs who established what.', 'false_definitiveness: The self-assessment reads "Strong defense (leaning toward Partial on the cost-overrun point)." This hedges and asserts at the same time. On the cost-overrun point, which is the critique\'s only quantitative channel, the Advocate concedes they "cannot say whether the shortfall would be 10% or 100%.']
Challenger failures: []
Debate resolved: The strong form of the critique, that WHO is "unlikely to rely on a single trial," does not survive. Verified counter-precedent exists (R21), the verifier's TB evidence allows a single large multi-site trial, and the program targets a hard survival endpoint. The debate also established that all-in cost would need to rise roughly 54% (to about $10.8M) before the BOTEC falls below the ~2,000x bar.
Debate unresolved: Two questions remain open. First, what share of the $7M is allocated to Phase III. Second, whether a WHO TB guideline group would issue a strong recommendation for a host-directed adjunct on one positive trial, given the documented imprecision-downgrading hurdle. The Advocate's claim that this risk is already captured in p_success was asserted but never tested.