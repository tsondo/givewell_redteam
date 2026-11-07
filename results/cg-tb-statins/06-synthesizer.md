# Red Team Report: TB Adjunctive Therapy Development Grant (Coefficient Giving BOTEC: $7M all-in, 10% conditional mortality reduction, 40% p_success)

## Pipeline Summary

- Investigation threads examined: 2
- Candidate critiques generated: 4
- Verified critiques: 4
- Rejected by verifier: 0
- Critiques surviving adversarial review: 4
- Dependencies identified: 0
- Signal rate: 4/4

## How to Read This Report

This report classifies findings by the surviving strength a neutral judge
assigned after reviewing each Advocate/Challenger debate. The three levels
mean:

- **STRONG** — The Challenger made grounded arguments the Advocate could
  not adequately defend. The critique identifies a real gap in the CEA
  that warrants direct attention.

- **MODERATE** — Both sides made some grounded arguments, and the
  substantive question remains open. The critique identifies a real
  concern but the evidence doesn't yet settle how to adjust.

- **WEAK** — The debate was dominated by reasoning failures (unsupported
  estimates, strawmanning, whataboutism, or similar) on one or both
  sides. The critique may still be valid, but this particular debate
  did not establish it. Weak findings are preserved in this report
  because the underlying claim may deserve a better-argued examination
  later.

The Debate Quality Audit section further below quantifies the reasoning
failure modes detected across all debates. Readers who want to assess
the calibration of these labels should start there.

## Critical Findings (surviving strength: STRONG)

No critique in this run reached STRONG surviving strength.

## Significant Findings (surviving strength: MODERATE)

### Finding 1: A mortality-powered Phase III costs several multiples of $7M, and trial-population mortality makes it worse

**Impact:** The finding applies only if the BOTEC implicitly assumes a Phase III powered on all-cause mortality in an unenriched population. In that case `all_in_cost` plausibly rises from $7M to roughly $24M–$48M, well past the ~$10.7M break-even. SROI would fall by roughly 70% or more, though that figure is illustrative.

**Evidence:**
- **Sample size:** A standard two-proportion calculation (α=0.05 two-sided, 80% power) needs about 47,000 participants to detect 6.0%→5.4% mortality. At a 3% baseline it needs about 96,000. Recent pivotal TB regimen trials enrolled roughly 450–2,500.
- **Trial costs:** TB-PRACTECAL cost €33.9M in total, though it is not comparable per patient because it was a drug-resistant TB trial with hospital-level care. A systematic review found per-trial costs of US$7–221M, which puts $7M at the floor of that range. A modelled TB vaccine trial came to $120M for 12,000 infants.
- **Counter-evidence:** The verifier also surfaced offsetting points:
  - High-mortality populations sharply reduce the required N. TB meningitis case fatality can reach about 50%.
  - Trials are typically powered for larger effects. IMPI hypothesised a 30% mortality reduction, and its 1,400-participant trial showed no mortality benefit.

**GiveWell's best defense:** The BOTEC never states that the Phase III is powered on all-cause mortality. It says only that Phase II and III "both succeed" (40%) and that the $7M is all-in. The critique therefore attacks a trial design the BOTEC does not specify. The Advocate's defense was truncated mid-sentence ("all-in costs include…"), so any magnitude or offsetting arguments were never made.

**Why it survives:** The BOTEC's silence on design is exactly the problem. The benefit is denominated in mortality averted, but the budget does not say what trial it buys. Under the most natural reading of "test a 10% mortality effect," the budget is off by multiples. The defense does not establish an alternative design that fits within $7M.

**Recommended action:** Read the full BOTEC and report text, including the truncated "all-in costs include…" clause and the benefit derivation, and answer three questions:
- (a) Is SROI computed from mortality averted?
- (b) Does the $7M itemize a trial design (sample size, endpoint, population)?
- (c) Is the Phase III modelled on standard TB regimen trials using composite unfavourable-outcome endpoints?

How to use the answers:
- **If the BOTEC assumes a standard-endpoint trial:** the critique largely falls away. A smaller surrogate-to-mortality translation concern remains (see Finding 2).
- **If it assumes a mortality-powered, unenriched trial:** the critique holds in direction, with all-in cost likely above $10.7M. Treat the specific dollar figures and the 70% SROI decline as illustrative.

**Key unresolved question:** *(The input field was empty; this is derived from the hypothesis.)* What endpoint, population, and sample size does the Phase III in the $7M budget actually assume?

*Pipeline contribution:* This finding adds an explicit power calculation, external trial-cost benchmarks, and verifier-surfaced counter-considerations (enrichment, larger powered effects). The per-participant cost of $500–$1,000 is ungrounded. The verifier judged the available evidence consistent with it being a lower bound.

### Finding 2: If Phase III is surrogate-powered, costs and benefits describe different interventions

**Impact:** No clean magnitude is available. This finding is the other horn of Finding 1's dilemma. If the trial is cheap because it is powered on a surrogate, the CEA credits a 10% mortality benefit the trial would not test. Either adoption parameters (`speedup_years`, coverage) are too optimistic, or a follow-on mortality trial is required and cost rises.

**Evidence:** The verifier's evidence package was empty. The hypothesis rests on general GRADE practice, under which certainty is downgraded for indirectness when evidence relies on surrogates. It also cites the precedent that corticosteroid recommendations for TB meningitis rest on mortality trials. The critique itself concedes two limits:
- It is not established that surrogate-only evidence would block or delay a WHO recommendation for regimen-type trials.
- "Unfavourable outcome" is a patient-important composite, not a pure surrogate.

**GiveWell's best defense:** The 10% is explicitly a conditional planning assumption ("a positive result is assumed to cut that by 10%"). The risk that a trial succeeds on its endpoint without delivering the mortality benefit is the kind of risk `p_success` is meant to absorb. This defense was also truncated, in the magnitude section.

**Why it survives:** It is not clear that a 40% joint Phase II/III success probability prices in *translation* risk, meaning success on the trial endpoint without the assumed mortality effect, as opposed to trial-failure risk. The BOTEC does not separate the two. The judge rated the question open rather than resolved.

**Recommended action:** The judge provided no recommendation for this finding. The investigation in Finding 1 resolves it directly: questions (b) and (c) determine which horn applies. If the trial is surrogate- or composite-powered, GiveWell/CG should run a sensitivity on `speedup_years` and coverage. It should also state whether `p_success` is intended to include surrogate-to-mortality translation risk.

**Key unresolved question:** *(The input field was empty; this is derived from the hypothesis.)* Would WHO issue a guideline change on a positive Phase III powered on culture conversion or an unfavourable-outcome composite for a TB adjunct, and on what timeline relative to the BOTEC's `speedup_years`?

*Pipeline contribution:* This finding contributes a novel framing: it treats cost and benefit as an internal-consistency problem rather than two separate parameter disputes. It adds no verified evidence. Readers should treat it as a structural observation, not an empirically grounded finding.

## Minor Findings (surviving strength: WEAK)

**Selection-on-success makes the "conditional 10%" an upward-biased estimate (winner's curse), and it is not shrunk.**

The critique argued that if the 10% `relative_reduction` was drawn from a small, surrogate-powered trial that cleared a significance bar, it should be shrunk. An illustrative 0.5–0.8 factor would cut SROI from ~3,000x to ~1,500–2,400x. The shrinkage factor is the Investigator's own regression-to-the-mean inference, not a TB-specific source.

The Advocate's central point appears to be correct: the BOTEC says the 10% is *assumed*, and the cited Phase IIa/b trial reported surrogate endpoints (bacterial clearance, chest X-ray lung damage), not mortality. Winner's curse applies to observed effects, not planning assumptions. The only benchmark found points the other way. Corticosteroids in TB meningitis show a pooled RR of 0.84 (95% CI 0.76–0.94), a ~16% reduction that exceeds the assumed 10%. The drift from an earlier Cochrane RR of 0.79 (595 patients) is only mildly consistent with small-sample inflation.

The judge concluded the bias argument is not established. The defensible residue is minor:
- Report a one-line sensitivity on `relative_reduction` over 0.05–0.15. Because SROI is linear in this parameter, the range is ~1,500x–4,500x.
- Check via one document lookup or query to CG whether the 10% was derived from Phase IIa/b results. Only if it was does shrinkage warrant revisiting.

**WHO is unlikely to rely on a single trial.**

This hypothesis was ungrounded: WHO might require evidence beyond one Phase III, which would push the true cost above $7M. Its headline is overbroad. WHO practice depends on the product and pathway. Vaccine recommendations such as R21 have rested on one large Phase III plus supportive data. Treatment guidelines are more likely to want multiple trials or one large multi-site trial rated high-certainty under GRADE.

The Advocate correctly noted two things. The $7M is explicitly all-in, covering "later Phase III trials, guideline changes, dissemination and validation." The BOTEC also never states that it funds only one Phase III. The judge noted that costs would need to rise ~54% (to ~$10.8M) to cross the bar.

The residual concern is minor: a single positive Phase III could be GRADE-downgraded for imprecision, prompting more evidence generation. The recommended action costs nothing: state the assumed Phase III budget and the break-even explicitly in the BOTEC. The Challenger's rebuttal for this debate was absent from the record ("..."), so the judge's assessment rests largely on the defense and the verifier evidence.

## Comparison with GiveWell's AI Output

The Baseline AI Output section was empty in this run, so overlap cannot be assessed. The table records what the pipeline added in absolute terms only.

| Our Critique | Overlap with GiveWell AI Output? | What We Added |
|---|---|---|
| A mortality-powered Phase III costs several multiples of $7M, and trial-population mortality makes it worse | (not available — baseline not provided) | Explicit power calculation (~47k–96k participants); external trial-cost benchmarks ($7–221M range; TB-PRACTECAL €33.9M); verifier counter-considerations (enrichment, IMPI precedent) |
| If Phase III is surrogate-powered, costs and benefits describe different interventions | (not available — baseline not provided) | Novel cost–benefit consistency framing; identifies that `p_success` may conflate trial risk and translation risk; no verified evidence |
| Selection-on-success makes the "conditional 10%" an upward-biased estimate (winner's curse), and it is not shrunk | (not available — baseline not provided) | Adversarial review largely deflated the claim; external benchmark (RR 0.84) suggests 10% is not inflated; concrete sensitivity range (1,500x–4,500x) |
| WHO is unlikely to rely on a single trial | (not available — baseline not provided) | Product-type distinction in WHO evidence standards (R21 vs. TB regimens); break-even quantification (~54% cost increase / ~$10.8M) |

## Debate Quality Audit (from judge agent data)

**Total debates audited:** 4
**Sound analytical moves noted:** 10

**Failure modes detected (combined across both sides):**

| Failure type | Count |
|---|---|
| unsupported_estimate_fabricated | 1 |
| unsupported_estimate_pseudo | 2 |
| unsupported_estimate_counter | 0 |
| whataboutism | 0 |
| call_to_ignorance | 2 |
| strawmanning | 1 |
| false_definitiveness | 4 |
| generic_recommendation | 1 |
| misrepresenting_evidence_status | 2 |

**Most common Advocate failure:** false_definitiveness
**Most common Challenger failure:** unsupported_estimate_pseudo

**Patterns:**
- Across both sides combined, false_definitiveness (4) was the most frequent failure mode. The Advocate's most common failure was false_definitiveness, and the Challenger's was unsupported_estimate_pseudo. The aggregate does not report per-side counts, so the split cannot be stated precisely.
- The direction fits the content of the debates. The Advocate leaned on the BOTEC's silence ("it never says the trial is mortality-powered") as if it were settled. The Challenger leaned on illustrative quantities: the 0.5–0.8 shrinkage factor and the $500–$1,000 per-participant cost.
- With only 4 debates and 13 total flagged failures against 10 sound syntheses, the sample is too small to support stronger conclusions.

## Conditional Findings (from linker output)

(no findings depend on unverified claims in this run)

## Open Questions (from Rejected Critiques input — verdict: UNVERIFIABLE)

(none — all hypotheses were either grounded or contradicted)

## Resolved Negatives (from Rejected Critiques input — verdict: REJECTED)

(none)

## Meta-Observations

1. **One underlying gap, not four findings.** Three of the four critiques trace to a single gap: the BOTEC states a $7M all-in cost and a mortality-denominated benefit without specifying the Phase III design that connects them.
   - Findings 1 and 2 are explicitly two horns of one dilemma.
   - The WHO single-trial critique is a third angle on the same unspecified budget.

   The most valuable single action from this report is therefore cheap: have CG state the assumed Phase III endpoint, population, sample size, and budget line. That one disclosure would resolve or sharply narrow three findings. The effective count of distinct concerns is closer to two than four.

2. **The pipeline produced modest novelty and did not filter.**
   - All 4 candidates passed verification, and all 4 survived debate. A 4/4 signal rate with zero rejections indicates the verifier did not filter rather than that every hypothesis was strong. One critique (Finding 2) survived as MODERATE with an empty evidence package.
   - No finding reached STRONG.
   - The winner's-curse critique was substantially deflated in debate, and the WHO critique's headline was contradicted by precedent.
   - The baseline output was not supplied, so this run cannot demonstrate improvement over GiveWell's single-pass approach.

3. **The debate record is incomplete, which limits calibration.**
   - Advocate defenses were truncated in at least three debates, and the Challengers flagged this explicitly.
   - The Challenger rebuttal for the WHO critique is missing entirely.
   - Key Unresolved Questions were empty for all four critiques.
   - One Recommended Action and one Evidence package were empty.
   - The critiques' internal cross-references ("Critique 1/2/3") are inconsistent with one another, which is why this report refers to findings by title.

   Surviving-strength labels in this run should be read with lower confidence than usual. In particular, the MODERATE ratings on Findings 1 and 2 partly reflect defenses that were cut off before making magnitude arguments.

4. **Debate-quality signal: false_definitiveness reflects a real gap in the model.** The prevalence of false_definitiveness (4 across both sides combined, and the Advocate's most common failure) points to something about the CEA itself, not just about debate behaviour. Where the BOTEC is silent on trial design, the Advocate repeatedly treated that silence as exculpatory. Where specifics were missing, the Challenger filled them with pseudo-quantified placeholders (unsupported_estimate_pseudo). Both failure modes are symptoms of the same under-specified parameter, and both disappear once the Phase III design is documented.

5. **Two parameters are worth explicit sensitivity analysis regardless of how the design question resolves.** These are `relative_reduction`, over 0.05–0.15 (SROI ~1,500x–4,500x), and `all_in_cost` relative to the ~$10.7–10.8M break-even. The two values appear slightly differently across the input critiques. CG should also state whether the 40% `p_success` is meant to include surrogate-to-mortality translation risk or only trial-failure risk, because Finding 2's survival hinges on that ambiguity.

6. **Terminology.** The inputs alternate between "GiveWell" and "Coefficient Giving (CG)" as the owner of the BOTEC. The Advocate in Finding 2 noted it read the two as the same. This report follows the input labels, but the BOTEC under review appears to be CG's.