## DEPENDENCIES

### Dependency 1
surviving: The sweat-based diagnostic carries real option value but is speculative (~10–30k central)
rejected: Unclear scope boundary for the sweat-diagnostic workstream
verdict: unverified
relationship: engages_with
confidence: high
justification: The surviving critique's mechanism raises the "consistency point for the Verifier" on whether the $7M all-in cost already includes the diagnostic's funding, and defers cost attribution to the model. Its omitted-benefit estimate holds either way, so it does not require the scope-boundary claim to be true.

### Dependency 2
surviving: Discounting quantified properly with an S-curve ramp and discounted costs. The net effect is about −20% to −31%, not the benefit-only −21% to −35%.
rejected: Probability weighting is asymmetric between benefit and cost.
verdict: unverified
relationship: engages_with
confidence: high
justification: The mechanism says "If costs are probability-weighted by stage (Critique 4), expected spend falls and weights toward the near term, so the cost-side offset changes only modestly." It addresses stage-weighted costs but does not depend on that claim being true.

### Dependency 3
surviving: The all-in framing counts benefits for every treated patient but not the cost of treating them
rejected: Probability weighting is asymmetric between benefit and cost.
verdict: unverified
relationship: engages_with
confidence: medium
justification: The judge audit and unresolved items note that weighting adoption cost by p_success = 0.4 was raised but never applied, and that it could cut the effect roughly in half. This is the same cost-weighting question the rejected critique raises. The core delivery-cost asymmetry stands without it.

### Dependency 4
surviving: Industry phase-transition base rates put "II and III both succeed" at roughly 15–25%, so 40% requires an unstated premium of about 1.6–2.7×
rejected: P(adoption | Phase III success) and P(Phase III gets funded and run | Phase IIc success) are missing, and the 60% uptake factor may not cover them
verdict: unverified
relationship: depends_on
confidence: high
justification: The surviving critique's decomposition (central ≈ 0.20) includes "P(adopted | III) ≈ 0.7–0.85 (Critique 4)" as an explicit factor. The judge audit lists the adoption overlap as unresolved. The sub-0.26 claim therefore rests on the adoption-gate assumption.

### Dependency 5
surviving: Industry phase-transition base rates put "II and III both succeed" at roughly 15–25%, so 40% requires an unstated premium of about 1.6–2.7×
rejected: Phase IIc "success" is a weak gate. If it is defined by PK or dose selection, it passes easily and transmits little information, so the probability of the whole chain should be weighted toward Phase III
verdict: rejected
relationship: engages_with
confidence: medium
justification: The decomposition sets "P(IIc success) ≈ 0.5… because a PK/dose-selection Phase IIc is easier to 'pass'," which borrows the weak-gate framing the verifier contradicted for TB Phase IIc. The headline claim, that 40% needs an unexplained premium over base rates, does not require that framing.

### Dependency 6
surviving: "Success" probably means a surrogate or composite endpoint, but the model needs a 10% mortality reduction, so P(adopted AND 10% mortality benefit) < P(trials succeed)
rejected: P(adoption | Phase III success) and P(Phase III gets funded and run | Phase IIc success) are missing, and the 60% uptake factor may not cover them
verdict: unverified
relationship: engages_with
confidence: medium
justification: The mechanism frames the coherent quantity as "P(trials succeed on surrogate) × P(adopted | success) × E[mortality reduction | …]." It references the adoption term but argues mainly from the surrogate-to-mortality gap, so it does not depend on the adoption claim.

### Dependency 7
surviving: A Phase III cannot be powered on mortality, so the WHO GDG would be recommending on surrogate or composite endpoints
rejected: P(adoption | Phase III success) and P(Phase III gets funded and run | Phase IIc success) are missing, and the 60% uptake factor may not cover them
verdict: unverified
relationship: engages_with
confidence: low
justification: The critique's unresolved question is whether the 40% p_success covers "trial positive, but the recommendation is narrowed." This overlaps with the rejected critique's concern that adoption after Phase III success is not modeled and may not be covered by the 60% uptake factor.

### Dependency 8
surviving: Winner's-curse and reference-class patterns imply the conditional effect should sit well below the surrogate-implied one, and r and p_success should not be independent
rejected: Phase IIc "success" is a weak gate. If it is defined by PK or dose selection, it passes easily and transmits little information, so the probability of the whole chain should be weighted toward Phase III
verdict: rejected
relationship: engages_with
confidence: medium
justification: Both argue that modeling r and p_success as independent point values is wrong and that E[r × p_success] differs from the product of means. The surviving critique's covariance and winner's-curse argument is made through the surrogate-success definition and does not require the weak-gate premise.

### Dependency 9
surviving: Rifampicin induction structurally limits atorvastatin exposure in routine programs, and the trial exposure does not transfer
rejected: Effective delivered dose and adherence diverge from trial conditions, and programmatic dose may be lower than the trial dose, notably with rifapentine regimens
verdict: rejected
relationship: engages_with
confidence: medium
justification: The surviving critique keeps "Real-world dosing adherence matters" and flags "Applicability to rifapentine-based HPMZ" as ungrounded. Its core argument is rifampicin's CYP3A4 induction, which holds regardless of the adherence claim.

### Dependency 10
surviving: Shorter and new regimens erode both the eligible population and the incremental benefit
rejected: Effective delivered dose and adherence diverge from trial conditions, and programmatic dose may be lower than the trial dose, notably with rifapentine regimens
verdict: rejected
relationship: engages_with
confidence: low
justification: The surviving critique notes "Rifapentine is a CYP3A4 inducer, so the atorvastatin interaction question carries over" and calls its strength relative to rifampicin unverified. This touches the rifapentine point the verifier mostly contradicted. The surviving critique's main displacement-and-transfer argument does not depend on it.