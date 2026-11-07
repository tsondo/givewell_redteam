--- Thread: Translating surrogate endpoints into a 10% mortality reduction, and coherence with p_success ---

# Investigator Output: Surrogate-to-Mortality Translation and `p_success` Coherence

Across the critiques below, SROI appears to scale linearly with `relative_reduction`. This follows from the thread's own figures: 0.0655 gives 2,000x and 0.05 gives about 1,530x, so SROI ≈ 30,500 × rr. I use that scaling throughout.

---

CRITIQUE 1: Selection-on-success makes the "conditional 10%" an upward-biased estimate (winner's curse), and it is not shrunk

HYPOTHESIS: CG applies 10% only in the success branch (p = 0.40). But "success" means the Phase IIb/III results cleared a significance or efficacy bar, and the effect size conditional on clearing that bar is systematically larger than the true mean effect. The Phase IIa/b trial was small and powered for surrogates (culture conversion, CXR damage), not mortality. Any effect estimates from it are therefore noisy and, if they drove the 10% figure, inflated. The 10% should be treated as the *true* mortality effect given the drug "works" on surrogates. There is no basis for assuming the true mortality effect is as large as the effect that got the drug past the surrogate hurdle.

MECHANISM: `relative_reduction` is too high. A plausible shrinkage factor on the surrogate-derived effect is 0.5–0.8, which gives an effective rr of 0.05–0.08 and an SROI of about 1,500–2,400x. Magnitude is uncertain and requires a sensitivity analysis. The 0.5–0.8 range is my own inference from standard regression-to-the-mean reasoning, not from a TB-specific source.

EVIDENCE: Logical and statistical argument (selection on significance in underpowered trials). I cannot cite a TB-specific source quantifying shrinkage for adjunct trials. The verifier should confirm the sample size and CIs of the Phase IIa/b trial. I believe it is a few hundred participants at most, but I cannot give the exact trial identity or numbers (UNGROUNDED).

STRENGTH: MEDIUM.

--- Thread: Realism of the $7M all-in cost, given what a Phase III would need to show ---

**Caveats.** I did not receive the CEA or the grant documents, so I don't know what the $7M covers, what the Phase IIc endpoint is, or what the sweat-diagnostic workstream is. Where I rely on recalled trial sizes or cost figures, I say so. All arithmetic is my own.

---

CRITIQUE 1: A mortality-powered Phase III costs several multiples of $7M, and trial-population mortality makes it worse

HYPOTHESIS: The CEA's benefit is a roughly 10% relative mortality reduction (6.0% → 5.4%). Detecting that effect requires a very large trial. Adding the other all-in components (guideline work, dissemination, validation) to a trial of this size cannot plausibly fit in $7M. Baseline mortality inside trials is usually lower than community case-fatality, because of exclusions, closer monitoring and better adherence. Lower event rates push the required sample size up further.

MECHANISM: `all_in_cost` rises. My calculation, standard two-proportion, α = 0.05 two-sided, 80% power:
- At 6.0% vs 5.4%, n ≈ 7.84 × (0.06×0.94 + 0.054×0.946) / 0.006² ≈ 23,400 per arm, about 47,000 total.
- If trial-arm mortality is 3% (a 10% relative reduction is then 3.0% → 2.7%), n ≈ 48,000 per arm, about 96,000 total.
- At $500 per participant, 47,000 participants cost about $23.5M. At $1,000 per participant it is about $47M. The 96,000-participant case at $500 is about $48M.
- Even the low case (about $24M) pushes `all_in_cost` far past the $10.7M "below the bar" line. SROI would fall roughly in proportion, by about 70% or more.

EVIDENCE:
- The sample-size arithmetic is a logical argument and is verifiable.
- The recalled comparison is that recent pivotal TB regimen trials enrolled roughly 450–2,500 people (Study 31/A5349 about 2,500; REMoxTB about 1,900; TRUNCATE-TB, RIFASHORT and SimpliciTB several hundred each). I believe this is right but the Verifier should check it. Those trials were powered on non-inferiority for unfavorable outcome, not mortality.
- A per-participant cost for large TB trials: UNGROUNDED. I believe $500 is likely low for a multi-country trial with follow-up, but I cannot cite a source.

STRENGTH: HIGH. The arithmetic is simple and the gap is more than 3×, well above materiality. It is conditional on the Phase III actually being mortality-powered, which Critique 2 addresses.

NOVELTY CHECK: Not on the exclusion list. It is distinct from the "trial may fail" (60%) and "10% is an assumption" items. I take the 10% as given and ask only whether the cost is consistent with it.

---

CRITIQUE 2: If Phase III is surrogate-powered, costs and benefits describe different interventions

HYPOTHESIS: The only way to keep a Phase III near $7M is to power it on a surrogate or composite endpoint: culture conversion, unfavorable outcome, relapse, lung function or a composite. The CEA then credits a 10% mortality reduction that the funded trial never tests. The cost side buys a surrogate-endpoint trial, and the benefit side assumes a mortality-endpoint result. If the cost reflects a surrogate design, the 10% mortality benefit has to be imported from outside the trial. WHO's GRADE process rates certainty down for indirectness when the outcome is a surrogate. A recommendation would then be conditional or slow to be adopted, or not made at all.

MECHANISM:
- `all_in_cost` is cheap only if the trial is surrogate-powered.
- Benefits are credited as if a mortality-powered trial had been run.
- The cost is therefore not consistent with the benefit. Either cost goes up (Critique 1) or benefit/adoption goes down.
- The cost of closing the gap is a follow-on mortality trial, or a longer `speedup_years` delay while mortality evidence accrues post-guideline.
- I can't give a clean magnitude. If WHO requires mortality evidence, the scenario collapses into Critique 1. If WHO accepts a surrogate, adoption speed and scale (`speedup_years`, coverage) are plausibly lower than in the base case. That needs CEA sensitivity analysis.

EVIDENCE:
- GRADE indirectness for surrogate outcomes is standard WHO guideline-methods practice (institutional guidance). The Verifier should check the WHO Handbook for Guideline Development.
- My inference is that adjunctive-therapy recommendations such as corticosteroids in TB meningitis and pericarditis rested on mortality or clinical-outcome trials. I cannot cite specifics.
- Whether this grant's Phase III is surrogate-powered: UNGROUNDED, since I haven't seen the design.

STRENGTH: MEDIUM-HIGH. The logic is strong and the structural inconsistency is real. The size depends on facts I don't have.

NOVELTY CHECK: This is not "trial fails" (a failed trial is a negative result). It is a trial that "succeeds" on an endpoint that doesn't establish the modeled benefit. It overlaps with Threads 1 and 5 (adoption and speed), and I limit it to the cost–endpoint consistency link.

---

CRITIQUE 3: WHO is unlikely to rely on a single trial