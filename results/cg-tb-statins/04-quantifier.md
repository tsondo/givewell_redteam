--- Critique: "Success" in Phase III is unlikely to be a mortality result, so the 10% mortality effect is not what a "success" would establish ---

# CRITIQUE: "Success" in Phase III is unlikely to be a mortality result, so the 10% mortality effect is not what a "success" would establish

## Parameter Mapping

| Parameter | Current value | Role |
|---|---|---|
| `relative_reduction` | 0.10 | Primary. Read as E[mortality effect \| "success"]. |
| `p_success` | 0.40 | Secondary, possible offset. A surrogate endpoint is easier to hit, so P(success) could rise as the meaning of success weakens. |
| `all_in_cost` | $7,000,000 | Noted only. A mortality-powered trial of 35k–70k participants is incompatible with this budget. That is Thread 1/cost territory and is not quantified here. |

The model is fully linear:

SROI = eligible × uptake × baseline_mortality × relative_reduction × speedup × DALYs × $OP/DALY / cost × p_success

So SROI scales 1:1 with `relative_reduction`, and with the product `relative_reduction × p_success`.

## Plausible Range

The critique's mixture is E[r | success] = (1−f)·0.10 + f·r_s, where:
- f is the share of "success" worlds that are surrogate-only.
- r_s is the true mortality effect in those worlds.

The verified evidence supports three points:
- Prior atorvastatin data are on surrogates (sputum mycobacterial load).
- The surrogate validity of 2–3-month culture status for long-term clinical outcome is contested.
- A related statin, rosuvastatin, did not move culture conversion.

The evidence does not pin down f or r_s. The value r_s = 0.03 is unsourced.

| Case | f | r_s | E[r \| success] | Notes |
|---|---|---|---|---|
| Low | 0.5 | 0 | 0.05 | The critique's own pessimistic case. A harsher f = 0.6 gives 0.04. |
| Central | ~0.4 | ~0.025 | ~0.07 | Most Phase III designs at a $7M scale would be surrogate-powered, but some surrogate wins carry a real mortality effect. |
| High | 0 | n/a | 0.10 | CG's 10% already intended as the average over whatever "success" means. |

## Sensitivity Analysis

- **Base case:** 19,800 deaths averted per year, 534,600 DALYs, SROI = 3,055x.
- **Break-even:** r = 0.0655 brings SROI to exactly the 2,000x bar.

| relative_reduction | SROI | Δ vs base |
|---|---|---|
| 0.10 (high / base) | 3,055x | 0% |
| 0.085 | 2,597x | −15% |
| 0.072 | 2,200x | −28% |
| 0.07 (central) | 2,139x | −30% |
| 0.065 (critique's f = 0.5, r_s = 0.03) | 1,986x | −35% (below bar) |
| 0.05 (low) | 1,528x | −50% |
| 0.04 (f = 0.6, r_s = 0) | 1,222x | −60% |

Joint test with the p_success offset (multiplicative, not additive):

| Scenario | SROI | Δ vs base |
|---|---|---|
| r = 0.07, p = 0.50 | 2,674x | −12% |
| r = 0.05, p = 0.50 | 1,909x | −37% |
| r = 0.05, p = 0.40 | 1,528x | −50% (pessimistic joint) |

The optimistic direction is limited. Nothing in the evidence suggests that surrogate success implies a mortality effect above 10%. The upside is therefore capped at no change, unless the critique is wrong and CG's 10% was already a blended figure.

## Bottom-Line Impact

This critique reduces SROI by 0% to 50%, with a central estimate of about 30% (3,055x → ~2,140x). Partial offset is possible if surrogate-defined success raises p_success. The SROI falls below the 2,000x bar if E[r | success] is under 0.0655.

## Materiality Verdict

**YES.** The central estimate is a 30% reduction. It sits narrowly above the bar, and plausible pessimistic values cross it.

## Code

```python
base = dict(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=1e5, speedup_years=1,
            all_in_cost=7e6, p_success=0.40)

def sroi(**kw):
    p = {**base, **kw}
    elig = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    deaths = elig * p['adult_uptake'] * p['baseline_mortality'] * p['relative_reduction']
    benefit = deaths * p['speedup_years'] * p['dalys_per_death'] * p['op_per_daly']
    return benefit / p['all_in_cost'] * p['p_success']

b = sroi()                                                        # 3054.9
for r in [0.10, 0.085, 0.072, 0.07, 0.065, 0.05, 0.04]:
    s = sroi(relative_reduction=r)
    print(r, round(s), f"{s/b-1:+.0%}")
for r, ps in [(0.07, 0.5), (0.05, 0.5), (0.05, 0.4)]:
    s = sroi(relative_reduction=r, p_success=ps)
    print(r, ps, round(s), f"{s/b-1:+.0%}")
print("breakeven r:", 0.10 * 2000 / b)                            # 0.0655
mix = lambda f, rs: (1 - f) * 0.10 + f * rs                       # E[r|success]
```

## Sensitivity Inputs

RANGE: relative_reduction | current 0.10 | low 0.05 | central 0.07 | high 0.10

--- Critique: A large share of on-treatment deaths is unreachable by a weeks-scale host-directed adjunct, and shorter regimens shrink the headroom further ---

# CRITIQUE: A large share of on-treatment deaths may be beyond the reach of a weeks-scale host-directed adjunct, and shorter regimens may shrink the headroom further

## PARAMETER MAPPING

- **relative_reduction** (primary). Current value is 0.10, applied to *all* on-treatment deaths among treated drug-susceptible patients.
  - The critique says the effective value should be (fraction of deaths reachable) × (effect among reachable deaths).
- **baseline_mortality** (secondary, HPMZ claim). Current value is 0.06.
  - The verifier flagged the HPMZ headroom claim as UNGROUNDED. Study 31 showed HPMZ was non-inferior on efficacy, with no clear mortality difference.
  - HPMZ uptake by the 8-year mark is also uncertain.
  - I therefore do **not** move baseline_mortality. I note it qualitatively only.

No other parameters are affected. The model is linear in relative_reduction, so the effect is purely multiplicative.

## PLAUSIBLE RANGE

The "25–35% unreachable" figure is ungrounded. The verifier also found that early deaths from septic shock are inflammatory and so not clearly beyond a host-directed drug's reach. I treat the reachable fraction as uncertain, as follows:

| | Reachable fraction | Effective relative_reduction | Basis |
|---|---|---|---|
| Low (pessimistic) | 0.65 | 0.065 | The critique's own upper bound on unreachable deaths (35%) |
| Central | 0.85 | 0.085 | Direction supported, magnitude unknown; partial credit for the early-inflammatory-death counterpoint |
| High | 1.00 | 0.10 | No adjustment. CG's 10% may already have been meant as a population-average effect, and early deaths may be partly reachable |

One further point applies to the high case. Lowering effective relative_reduction assumes the 10% was meant to apply to reachable deaths only. If CG intended 10% as an intention-to-treat population effect, the critique applies only as a reason to doubt the 10% itself, not as a further discount.

## SENSITIVITY ANALYSIS

```python
def sroi(eligible=5.5e6, yta=8, decline=0.02, uptake=0.60, bm=0.06,
         rr=0.10, dpd=27, opd=1e5, speed=1, cost=7e6, p=0.40):
    elig = eligible*(1-decline)**(yta-8)
    deaths = elig*uptake*bm*rr
    benefit = deaths*speed*dpd*opd
    return benefit/cost*p

base = sroi()
for label, rr in [("low",0.065),("mid",0.075),("central",0.085),("high",0.10)]:
    s = sroi(rr=rr); print(label, rr, round(s), f"{(s/base-1)*100:.1f}%")
# break-even rr for the 2,000x bar
print(0.10*2000/base)
# stress test: reach 0.65 x weaker effect 0.07 (overlaps Thread 1)
print(round(sroi(rr=0.65*0.07)))
```

Base case: SROI is about **3,055x**, from 19,800 deaths averted per year.

| relative_reduction | SROI | Δ |
|---|---|---|
| 0.065 (35% unreachable) | 1,986x | −35% |
| 0.075 (25% unreachable) | 2,291x | −25% |
| 0.085 (central) | 2,597x | −15% |
| 0.10 (no adjustment) | 3,055x | 0% |

- **Break-even:** The 2,000x bar is crossed at relative_reduction ≈ **0.0655**, which is about 34.5% of deaths unreachable.
- **Joint stress test (illustrative only, overlaps the Thread 1 effect-size critique):** 65% reach × a 7% effect among reachable deaths gives r = 0.0455 and SROI ≈ 1,390x (−55%).
- **HPMZ:** If it lowered baseline_mortality proportionally, the effect would be multiplicative with the above. It is not quantified because it is ungrounded.

## BOTTOM-LINE IMPACT

This critique could reduce SROI by roughly 0–35% (3,055x → 1,986–3,055x), with a central estimate of about −15% (≈2,600x). The SROI stays above the 2,000x bar except at the extreme end of the critique's own ungrounded range.

## MATERIALITY VERDICT

**BORDERLINE.** The central case (~−15%) leaves the grant comfortably above the bar. Only the pessimistic bound reaches the funding line. Compounded with a weaker per-patient effect (Thread 1), the grant would fall below it.

## SENSITIVITY INPUTS

RANGE: relative_reduction | current 0.10 | low 0.065 | central 0.085 | high 0.10

--- Critique: Rifampicin induction structurally limits atorvastatin exposure in routine programs, and the trial exposure does not transfer ---

# Rifampicin–Atorvastatin Exposure: Impact on Coefficient Giving's (CG) TB Statins Cost-Effectiveness Estimate

**Bottom line:** This critique could reduce SROI by about 0–50%, with a central estimate of about 15% (3,055x → about 2,600x). It crosses the 2,000x funding bar only if the effective relative reduction falls below about 0.065.

## Parameter mapping

The critique affects one model parameter:

- **relative_reduction** (primary). Current value is 0.10. This is the relative mortality reduction realized in routine programs, conditional on success.

Two other parameters are related but should not be changed here:

- **p_success.** The verifier's THP-1 evidence suggests atorvastatin's limit may be mechanism-based rather than exposure-based. That is a probability-of-efficacy question, not a realized-exposure question. Counting it here as well would double-count. I leave p_success unchanged and note the correlation qualitatively.
- **adult_uptake.** This covers whether patients take the drug at all. The critique concerns the exposure achieved among those who take it, so it belongs in relative_reduction. Adjusting adult_uptake as well would double-count.

## Plausible range

**What the verifier changed.** The prior positive signal comes from atorvastatin itself, in patients on rifampicin-containing regimens. So the critique's strongest form is removed: there is no cross-statin transfer gap.

**What remains is a trial-to-routine-program gap:**

- Co-administration gives a modest rise in AUC.
- Separated dosing gives roughly an 80% fall in AUC.
- If routine programs dose at separate times more often than the trial did, a fraction of patients get sharply reduced exposure.
- The dose-response is unknown, and the 0.5–0.8 multiplier is flagged as ungrounded.

**Derivation of the range.** Effective r = 0.10 × [1 − f × L], where:

- f is the share of patients who are dosed apart, roughly 0.1–0.5.
- L is the share of the effect lost when dosed apart, roughly 0.5–1.0, if the effect is exposure-dependent.

| Case | f | L | Loss | Effective r |
|---|---|---|---|---|
| Low | 0.5 | 1.0 | 50% | 0.05 |
| Central | 0.3 | 0.5 | 15% | 0.085 |
| High | — | — | none | 0.10 |

- The low case matches the critique's own pessimistic multiplier of 0.5.
- The central case, about 0.85, is milder than the critique's 0.5–0.8 guess. This reflects the verifier's downgrade.
- The high case assumes co-administration, which is the standard approach of taking all pills together. I do not credit an increase above 0.10. The trial already reflects co-administered exposure, so routine co-administration would at most match it, not beat it.

## Sensitivity analysis

The model is linear in relative_reduction, so the percentage change in SROI equals the percentage change in r.

| relative_reduction | Deaths averted/yr | SROI | Δ vs. base | Clears 2,000x bar? |
|---|---|---|---|---|
| 0.10 (base, high) | 19,800 | 3,055x | 0% | Yes |
| 0.09 | 17,820 | 2,750x | −10% | Yes |
| 0.085 (central) | 16,830 | 2,597x | −15% | Yes |
| 0.08 (critique's 0.8 multiplier) | 15,840 | 2,444x | −20% | Yes |
| 0.0655 (breakeven) | 12,969 | 2,000x | −34.5% | At the bar |
| 0.05 (low) | 9,900 | 1,527x | −50% | No |

- **Joint pessimistic case.** Only one parameter is affected, so the joint case equals the low case: 1,527x, a change of −50%.
- **Multiplicative interaction.** The effect is multiplicative with any other critique that also scales relative_reduction or p_success. Examples are Thread 1's unreachable-deaths share and hepatotoxicity offsets. Combined haircuts compound, so a 15% cut here plus a 30% cut elsewhere gives 0.85 × 0.70 = 0.595. That would put SROI at about 1,820x, below the bar.

## Materiality verdict: BORDERLINE

- The central case (−15%) stays well above the 2,000x bar.
- The pessimistic end (−50%) falls below it.
- The magnitude has no empirical basis, so the wide range should be reported rather than a point estimate: Δ = 0% to −50%.
- The most decision-relevant fact is that the result is fragile when combined with other relative_reduction haircuts.

## Code

```python
def sroi(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=1e5, speedup_years=1,
         all_in_cost=7e6, p_success=0.40):
    eligible = eligible_people_at_8y * (1 - decline_per_year) ** (years_to_adoption - 8)
    treated = eligible * adult_uptake
    deaths = treated * baseline_mortality * relative_reduction
    benefit = deaths * speedup_years * dalys_per_death * op_per_daly
    return deaths, benefit / all_in_cost * p_success

base = sroi()[1]
for r in [0.10, 0.09, 0.085, 0.08, 0.0655, 0.05]:
    d, s = sroi(relative_reduction=r)
    print(f"r={r}: deaths={d:,.0f}  SROI={s:,.0f}x  delta={(s/base-1)*100:+.1f}%")

# breakeven relative_reduction for the 2000x bar
print("breakeven r:", 0.10 * 2000 / base)  # ~0.0655
```

## SENSITIVITY INPUTS

RANGE: relative_reduction | current 0.10 | low 0.05 | central 0.085 | high 0.10

--- Critique: Winner's-curse and reference-class patterns imply the conditional effect should sit well below the surrogate-implied one, and r and p_success should not be independent ---

# CRITIQUE: Winner's-curse and reference-class patterns imply the conditional effect should sit well below the surrogate-implied one, and r and p_success should not be independent

## Parameter Mapping

| Parameter | Model key | Current value | Role |
|---|---|---|---|
| Conditional relative mortality reduction | `relative_reduction` | 0.10 | Primary |
| Probability Phase II and III both succeed | `p_success` | 0.40 | Secondary, through the r–p covariance |

**Model structure:**

SROI = [eligible_people_at_8y × (1−decline)^(years_to_adoption−8) × adult_uptake × baseline_mortality × **relative_reduction** × speedup_years × dalys_per_death × op_per_daly] / all_in_cost × **p_success**

SROI is strictly linear in `relative_reduction` and in `p_success`, and enters only through their product. So the covariance point can be expressed exactly as an *effective* `relative_reduction`, defined as E[r × success] / p_success, holding `p_success` at 0.40. This avoids double-counting across two parameters.

## Plausible Range

**Shrinkage component (winner's curse).** The critique proposes a factor of 0.7–0.9. The critique itself flags this as ungrounded. It is directionally supported by:
- Atorvastatin having only a Phase II surrogate signal (sputum load), with no mortality data.
- The class-adjacent rosuvastatin Phase 2b being null (HR 1.30, 95% CI 0.88–1.91).
- The broader host-directed-therapy record: vitamin D, metformin, CC-11050 and everolimus all showed surrogate or subgroup signals only.

This puts effective r at 0.07–0.09.

**Covariance component (surrogate-only "successes").** If p_success = 0.40 counts trials that succeed on a surrogate endpoint, some share q of those "successes" carry roughly zero mortality effect. A cheap ($7M all-in) Phase III makes a surrogate endpoint more likely.
- Illustrative q = 0–25%.
- E[r | counted success] = shrink × 0.10 × (1 − q).

**Resulting effective `relative_reduction`:**

| Case | Calculation | Effective r |
|---|---|---|
| Low | 0.7 × 0.75 × 0.10 | ≈ 0.05 (0.0525) |
| Central | 0.8 × 1.0 × 0.10 (shrinkage only) | 0.08 |
| High | No shrinkage, as GiveWell assumes | 0.10 |

An upward revision is not supported. Winner's-curse logic gives no reason to expect the mortality effect to exceed the surrogate-implied value.

## Sensitivity Analysis

Base case: 19,800 deaths averted/yr, benefit $OP 53.46B, **SROI = 3,055x**. Funding bar = 2,000x.

| Scenario | Effective r | SROI | Δ vs base |
|---|---|---|---|
| Base | 0.10 | 3,055x | — |
| Shrink 0.9 | 0.09 | 2,749x | −10% |
| Shrink 0.8 (central) | 0.08 | 2,444x | −20% |
| Shrink 0.7 | 0.07 | 2,138x | −30% |
| Shrink 0.8, q = 25% | 0.06 | 1,833x | −40% |
| Shrink 0.7, q = 25% (joint pessimistic) | 0.0525 | 1,604x | −47.5% |

- **Break-even:** SROI falls to the 2,000x bar at r ≈ 0.0655. That is a combined shrinkage × (1−q) factor of about 0.65.
- **Interaction:** the shrinkage and covariance effects multiply.
- **Optimistic direction:** with no shrinkage and independence (r = 0.10), SROI is unchanged.
- **If `p_success` is defined strictly as mortality success:** the covariance term vanishes (q = 0), and only shrinkage applies. In that case p_success itself might be lower, but that belongs to the p_success thread and is not counted here.

## Bottom-Line Impact

This critique could reduce SROI by 10–48% (from 3,055x to roughly 1,600–2,750x), with a central estimate of about −20% (2,444x). The pessimistic tail pushes SROI below the 2,000x bar.

## Materiality Verdict

**YES** (the central estimate is borderline relative to the bar).
- The central −20% is material in size but stays above 2,000x.
- The joint-pessimistic case crosses the bar.
- The magnitude rests on an ungrounded shrinkage factor, so these figures are illustrative ranges, not point estimates.

## Code

```python
def sroi(r=0.10, p=0.40, elig=5.5e6, yrs=8, dec=0.02, up=0.60, mort=0.06,
         dpd=27, opd=1e5, speed=1, cost=7e6):
    eligible = elig * (1 - dec) ** (yrs - 8)
    deaths = eligible * up * mort * r
    benefit = deaths * speed * dpd * opd
    return benefit / cost * p

base = sroi()
print("base", round(base))
for shrink in (0.9, 0.8, 0.7):
    for q in (0, 0.25):
        r = 0.10 * shrink * (1 - q)
        s = sroi(r=r)
        print(shrink, q, round(r, 4), round(s), f"{(s/base-1)*100:.1f}%")

print("breakeven r", 0.10 * 2000 / base)
# base 3055; 0.9/0->2749(-10%); 0.8/0->2444(-20%); 0.7/0->2138(-30%)
# 0.8/0.25->1833(-40%); 0.7/0.25->1604(-47.5%); breakeven r ≈ 0.0655
```

## Sensitivity Inputs

RANGE: relative_reduction | current 0.10 | low 0.05 | central 0.08 | high 0.10

--- Critique: Hepatotoxicity and myopathy add a negative tail, and the combined attenuations compound ---

# Quantifying the hepatotoxicity/myopathy harm tail in the TB statins CEA

## Parameter mapping

- **relative_reduction** (primary): currently 0.10, the relative mortality reduction conditional on Phase II/III success.
- **p_success** (0.40): not changed. It is relevant because a hepatotoxicity signal large enough to cause net harm would most likely be detected in the Phase IIc/III trials, sending the program down the "failure" branch. That branch already contributes zero benefit in the model.
- The compounded "reachable × PK × shrinkage" factor also acts on relative_reduction. It overlaps with Critiques 1–4 and is flagged as hypothetical, so it is reported only as an illustration and kept out of the sensitivity inputs.

## Model structure

The benefit chain is linear in relative_reduction:

- SROI = 5.5M × 0.60 × 0.06 × r × 1 × 27 × 100,000 / 7M × 0.40 = **30,549 × r**
- At r = 0.10, SROI = **3,055x**.
- To fall below the 2,000x bar, r would need to drop to **0.0655** (a 34.5% reduction).

## Plausible range for relative_reduction

The harm tail is modeled as E[r] = (1−q)·0.10 + q·h, where q is the probability that the true effect is the "harm" outcome and h is the effect size in that world.

| Scenario | q | h | E[r] |
|---|---|---|---|
| Critique's stated case | 0.10 | 0 | 0.090 |
| Mild tail | 0.05 | 0 | 0.095 |
| Pessimistic tail | 0.15 | −0.03 | 0.0805 |
| Optimistic (no tail) | 0 | – | 0.100 |

**Why the central estimate is 0.095.** The 0.10 is already conditional on trial success. A net-harmful drug reaching guidelines would require a false-positive trial, or a harm that only appears in real-world use (for example, unmonitored hepatotoxicity alongside isoniazid, rifampicin and pyrazinamide, or myopathy). Existing small trials show no hepatic signal. So the effective tail conditional on success is probably smaller than the unconditional 10% scenario. I therefore set the central value at 0.095, with 0.09 as a moderate case and about 0.08 as the pessimistic case.

## Sensitivity analysis

- **Base case:** 3,055x, with 19,800 deaths averted per year.
- **r = 0.095 (central):** 2,902x, Δ = −5%. Deaths averted fall to 18,810 per year.
- **r = 0.090:** 2,749x, Δ = −10%.
- **r = 0.080 (pessimistic):** 2,444x, Δ = −20%. Still above 2,000x.
- **r = 0.10 (optimistic, no harm tail):** 3,055x, Δ = 0%.
- **Illustrative compounded case, not additive with Critiques 1–4:** r = 0.023 to 0.054 gives SROI of 703x to 1,650x (Δ = −77% to −46%). This would cross the bar, but it double-counts the attenuations in Critiques 1–4, rests on ungrounded factor ranges, and the factors are correlated. The only grounded PK evidence is indirect: a pravastatin–rifampin interaction and metformin cutting rifampicin bioavailability by 24%.

**Interactions.** All the factors multiply r, so their effects are multiplicative on SROI, not additive. The harm tail combined with Critique 1's attenuation should be applied as a product, after removing the overlap between them.

## Bottom-line impact

The harm tail alone reduces SROI by about 0–20%, with a central estimate of about 5–10% (3,055x falls to roughly 2,750–2,900x). It does not cross the 2,000x bar. The compounded scenario (−46% to −77%) is a hypothetical upper bound only.

## Materiality verdict

**NO** for the harm tail alone. Crossing the bar would need r < 0.0655, which is outside the plausible harm-tail range. The verdict would become BORDERLINE or YES only if the compounding with Critiques 1–4 were empirically grounded, and that should be assessed in those critiques.

## Code

```python
def sroi(r=0.10, elig=5.5e6, ytA=8, dec=0.02, upt=0.60, bm=0.06,
         dpd=27, opd=1e5, spd=1, cost=7e6, p=0.40):
    eligible = elig * (1 - dec) ** (ytA - 8)
    deaths = eligible * upt * bm * r
    benefit = deaths * spd * dpd * opd
    return benefit / cost * p

base = sroi()
print("base", round(base))                      # 3055
print("r for 2000x bar", 2000 / (base / 0.10))  # 0.0655

for q, h in [(0.05, 0), (0.10, 0), (0.15, -0.03), (0, 0)]:
    r = (1 - q) * 0.10 + q * h
    s = sroi(r=r)
    print(q, h, round(r, 4), round(s), f"{s/base-1:+.1%}")

for r in [0.023, 0.054]:   # illustrative compounded case only
    s = sroi(r=r)
    print(r, round(s), f"{s/base-1:+.1%}")
```

## SENSITIVITY INPUTS

RANGE: relative_reduction | current 0.10 | low 0.08 | central 0.095 | high 0.10

--- Critique: A $7M Phase III cannot be powered on mortality, and the CEA's benefit is mortality only ---

# CRITIQUE: A $7M Phase III cannot be powered on mortality, and the CEA's benefit is mortality only

## Parameter mapping

| Parameter | Model key | Current value | Role |
|---|---|---|---|
| All-in cost (all funders, through Phase III and guideline change) | `all_in_cost` | $7,000,000 | SROI ∝ 1/cost |
| Probability Phase II and III both succeed | `p_success` | 0.40 | SROI ∝ p_success |
| Relative mortality reduction | `relative_reduction` | 0.10 | Not changed here. The critique is about whether 0.10 is *established by* the trial, not about its size. |

The critique is a fork with two mutually exclusive branches:

- **Fork A (mortality-powered Phase III):** the endpoint matches the mortality-only benefit, but `all_in_cost` is too low.
- **Fork B (surrogate or composite-endpoint Phase III):** $7M may be realistic, but "success" no longer means a mortality benefit was demonstrated. The effective probability of a real 10% mortality effect is then below 0.40. This is equivalent to lowering `p_success`.

Applying both branches at once would double-count. So I compute each branch separately, form a probability-weighted mixture, and express the result through `all_in_cost`, the critique's stated mechanism.

## Checking the critique's sample-size arithmetic

Two-proportion test, α = 0.05 two-sided, 80% power, (z_α/2 + z_β)² = 7.84:

| Baseline mortality | Treated arm (10% relative reduction) | n per arm | Total N |
|---|---|---|---|
| 5% | 4.5% | ≈ 28,400 | ≈ 57,000 |
| 6% (the CEA's own value) | 5.4% | ≈ 23,300 | ≈ 47,000 |
| 8% | 7.2% | ≈ 17,200 | ≈ 34,000 |

The critique's numbers are confirmed. At the CEA's own 6% baseline, the trial needs about 47,000 participants. $7M covers Phase IIc, Phase III, guideline change and dissemination. Even if the whole $7M went to the Phase III, that is about $150 per participant, below plausible pragmatic-trial costs in LMIC TB programmes. The internal-consistency point holds.

## Plausible ranges

**Fork A (mortality-powered):**
- Assumptions:
  - N = 34,000–57,000.
  - Pragmatic cost of $300–800 per participant, embedded in national TB programmes with registry-based death ascertainment.
  - Phase III cost of about $10–46M.
  - Plus about $3M for Phase IIc and $1–2M for guideline and dissemination.
- All-in cost ≈ $15–50M, central about $25M.
- I do not adopt the critique's thousands-of-dollars-per-participant figure because it is ungrounded.

**Fork B (surrogate endpoint):**
- Assumptions:
  - Cost stays at $7M.
  - Probability that a surrogate-positive result reflects a real ≥10% mortality effect is about 0.5–0.75. TB surrogates such as culture conversion have a poor record of predicting clinical outcomes.
- Effective `p_success` = 0.40 × (0.5–0.75) = 0.20–0.30, central about 0.24.

**Mixture:**
- Weights: 50/50. The Phase II evidence found used surrogate endpoints, which makes Fork B at least as likely as Fork A.
- The mixture SROI is expressed as an equivalent `all_in_cost` (see code).

## Sensitivity analysis

Base: benefit = 3.3M treated × 0.06 × 0.10 × 1 yr × 27 × 100,000 = $OP 53.46B. SROI = 53.46B × 0.4 / 7M = **3,055x**.

| Scenario | all_in_cost | p_success | SROI | Δ vs base |
|---|---|---|---|---|
| Base | $7M | 0.40 | 3,055x | — |
| Fork A low | $15M | 0.40 | 1,426x | −53% |
| Fork A central | $25M | 0.40 | 855x | −72% |
| Fork A high | $50M | 0.40 | 428x | −86% |
| Critique's extreme | $100M | 0.40 | 214x | −93% |
| Fork B optimistic | $7M | 0.30 | 2,291x | −25% |
| Fork B central | $7M | 0.24 | 1,833x | −40% |
| Fork B pessimistic | $7M | 0.20 | 1,527x | −50% |
| **Mixture central (50/50 A-central / B-central)** | ≈ **$16M equivalent** | 0.40 | ≈ **1,344x** | **−56%** |
| Optimistic (critique wrong, e.g., large in-kind platform contributions) | $7M | 0.40 | 3,055x | 0% |

Break-even points against the 2,000x funding bar:
- `all_in_cost` ≈ **$10.7M** (holding p_success at 0.40).
- Effective `p_success` ≈ **0.26** (holding cost at $7M).

Both branches therefore push the estimate near or below the bar under fairly modest assumptions.

Interactions: cost and p_success enter SROI multiplicatively. Combining them, for example Fork A cost with some residual surrogate risk, would compound. I do not stack them because the branches are mutually exclusive by construction.

Optimistic direction: a mortality-powered trial at $7M is possible only with substantial in-kind or platform support, or a high-risk enriched cohort. Enrichment reduces generalisability to the drug-susceptible majority, which would instead lower effective `relative_reduction` or `p_success`. I found no plausible way the critique raises SROI.

## Bottom-line impact

**This critique plausibly reduces SROI by about 25–86%. Central estimate ≈ −56% (3,055x → ≈1,340x), equivalent to raising all_in_cost from $7M to about $16M. The estimate falls below the 2,000x bar once effective all-in cost exceeds about $10.7M.**

Caveat: the specific magnitude depends on unverified per-participant costs and on the unknown breakdown of the $7M. The direction is robust.

## Materiality verdict

**YES.** Even the mildest scenario on either branch (−25%) reaches the 25% threshold, and the central case is more than double it.

## Code

```python
import math
z = 1.96 + 0.8416
def n_per_arm(p1, rr=0.10):
    p2 = p1 * (1 - rr)
    return z**2 * (p1*(1-p1) + p2*(1-p2)) / (p1 - p2)**2
for p in (0.05, 0.06, 0.08):
    print(p, round(n_per_arm(p)), round(2*n_per_arm(p)))

P = dict(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.6, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=1e5, speedup_years=1,
         all_in_cost=7e6, p_success=0.4)
def sroi(**kw):
    q = {**P, **kw}
    elig = q['eligible_people_at_8y'] * (1 - q['decline_per_year'])**(q['years_to_adoption'] - 8)
    deaths = elig * q['adult_uptake'] * q['baseline_mortality'] * q['relative_reduction']
    ben = deaths * q['speedup_years'] * q['dalys_per_death'] * q['op_per_daly']
    return ben / q['all_in_cost'] * q['p_success']

base = sroi()
for c in (15e6, 25e6, 50e6, 100e6):
    print('cost', c, round(sroi(all_in_cost=c)), f"{sroi(all_in_cost=c)/base-1:.0%}")
for p in (0.30, 0.24, 0.20):
    print('p', p, round(sroi(p_success=p)), f"{sroi(p_success=p)/base-1:.0%}")

mix = 0.5*sroi(all_in_cost=25e6) + 0.5*sroi(p_success=0.24)
print('mixture', round(mix), f"{mix/base-1:.0%}", 'equiv cost', round(7e6*base/mix))
print('break-even cost', base*7e6/2000, 'break-even p', 0.4*2000/base)
```

## Sensitivity inputs

RANGE: all_in_cost | current 7000000 | low 7000000 | central 16000000 | high 50000000

--- Critique: The all-in framing counts benefits for every treated patient but not the cost of treating them ---

# Quantified impact: delivery costs omitted from the all-in cost of the TB statins grant

## Parameter mapping

- **all_in_cost.** Current value is $7,000,000. It covers all funders through Phase III and guideline change. It includes no procurement, monitoring or health-worker costs for delivering atorvastatin.
- **Indirect only, not changed:** p_success = 0.40 and the treated cohort size. Treated = eligible_people_at_8y × adult_uptake = 5.5M × 0.6 = 3.3M patients in the single credited speed-up year (speedup_years = 1).

Delivery cost should be added only for the patients whose benefit is credited. That is 3.3M patients × 1 year, not all future years. Treating later years would be counterfactual anyway.

## A correction to the critique's arithmetic

Delivery costs occur only if the trials succeed. The model applies p_success as a multiplier on SROI:

SROI = benefit × p / cost

Adding the full delivery cost D to all_in_cost therefore implicitly charges delivery costs in the 60% of worlds where nothing is delivered. In expected-value terms the denominator should be:

7M + p_success × w × D

where w is the counterfactual value of the delivery funder's money (governments or the Global Fund) relative to Coefficient Giving (CG) dollars. So the effective all_in_cost is:

all_in_cost_eff = 7,000,000 + 0.40 × w × 3.3M × c

where c is the delivery cost per patient course.

This roughly halves the critique's stated impact. It does not remove it.

## Plausible ranges

**Per-patient cost, c: $1 to $10. Central $3.**
- Generic atorvastatin at 20–40 mg for the TB treatment course costs about $1–3 in procurement.
- Liver-function monitoring and clinic time add cost. This is the uncertain part, as the verifier noted.
- $10 is a high-monitoring scenario.

**Counterfactual weight, w: 0.3 to 1.0. Central 0.5.**
- Delivery is mostly paid by governments and the Global Fund.
- CG does not state a convention. The 0.3 value follows the critique's assumption.

Resulting all_in_cost_eff:

| Scenario | c | w | all_in_cost_eff |
|---|---|---|---|
| Low | $1 | 0.3 | $7.40M |
| Central | $3 | 0.5 | $8.98M |
| High | $10 | 1.0 | $20.2M |

## Sensitivity analysis

**Base case:** benefit × p = 5.346e10 × 0.4 = 2.1384e10. SROI = 3,055x.

**Break-even at the 2,000x bar:** all_in_cost ≤ $10.69M. That leaves $3.69M of headroom.
- With p-weighting and w = 1, D must be under $9.2M, or $2.80 per patient.
- Without p-weighting (the critique's framing), D must be under $3.7M, or $1.12 per patient.

| Scenario (c, w, p-weighted?) | all_in_cost | SROI | Δ |
|---|---|---|---|
| Base | $7.00M | 3,055x | — |
| $1, 0.3, yes | $7.40M | 2,891x | −5% |
| $3, 0.3, yes | $8.19M | 2,612x | −15% |
| **$3, 0.5, yes (central)** | **$8.98M** | **2,381x** | **−22%** |
| $1, 1.0, yes | $8.32M | 2,570x | −16% |
| $3, 1.0, yes | $10.96M | 1,951x | −36% |
| $10, 1.0, yes (pessimistic) | $20.2M | 1,059x | −65% |
| $3, 1.0, no (critique framing) | $16.9M | 1,265x | −59% |
| $10, 1.0, no (critique framing) | $40.0M | 535x | −82% |

**Optimistic direction.** Delivery costs cannot be negative, so the best case is no change. One partial exception: averted deaths and adverse-event savings could offset part of the cost. That offset is small relative to procurement and is not modeled.

**Interactions.** The effect works only through the denominator, so it is hyperbolic in D rather than linear. It is multiplicative with any reduction in p_success or relative_reduction. If those are cut, the margin above 2,000x shrinks further. For example, if another thread reduces benefit by 30%, the central case falls below the bar.

## Bottom-line impact

Counting expected delivery costs reduces SROI by about 5% to 65%, with a central estimate of about 22% (3,055x → about 2,380x). The estimate stays above the 2,000x bar unless delivery funds are valued near CG dollars and costs exceed about $2.80 per patient.

## Materiality verdict

**YES, borderline with respect to the funding bar.**
- The central change of −22% is material.
- Pessimistic but plausible assumptions (w ≈ 1, c ≥ $3) push SROI below 2,000x.
- The result depends on CG's unstated counterfactual-value convention for government and Global Fund money.

## Code

```python
base = dict(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.6, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=1e5, speedup_years=1,
            all_in_cost=7e6, p_success=0.4)

def sroi(p):
    elig = p['eligible_people_at_8y']*(1-p['decline_per_year'])**(p['years_to_adoption']-8)
    treated = elig*p['adult_uptake']
    deaths = treated*p['baseline_mortality']*p['relative_reduction']
    benefit = deaths*p['speedup_years']*p['dalys_per_death']*p['op_per_daly']
    return benefit/p['all_in_cost']*p['p_success'], treated

b, treated = sroi(base)
print(round(b))  # 3055
for c, w, pw in [(1,.3,1),(3,.3,1),(3,.5,1),(1,1,1),(3,1,1),(10,1,1),(3,1,0),(10,1,0)]:
    D = treated*c*w*(base['p_success'] if pw else 1)
    q = dict(base, all_in_cost=base['all_in_cost']+D)
    s, _ = sroi(q)
    print(c, w, pw, round(q['all_in_cost']/1e6, 2), round(s), f"{s/b-1:+.0%}")
```

## SENSITIVITY INPUTS

RANGE: all_in_cost | current 7000000 | low 7400000 | central 8980000 | high 20200000

--- Critique: Regulatory, pharmacovigilance and dissemination costs for an off-patent drug have no obvious payer, and the $7M likely under-budgets them ---

# Quantitative Impact Assessment: Off-Patent Adoption Costs and the $7M All-In Budget

**CRITIQUE:** Regulatory, pharmacovigilance and dissemination costs for an off-patent drug have no obvious payer, and the $7M likely under-budgets them

## PARAMETER MAPPING

- **all_in_cost**: $7,000,000 in the model (all funders, through Phase III and guideline change). This is the only parameter the critique changes.
- **Not mapped here:**
  - The hepatotoxicity concern bears on `relative_reduction`, through possible zero or negative net effect. That belongs to Thread 1.
  - Delivery and monitoring costs overlap with Critique 1.
  - Following the verifier, neither is counted here, to avoid double counting.
  - This assessment covers only the non-delivery adoption infrastructure: guideline change, regulatory label work, dissemination and pharmacovigilance.

## PLAUSIBLE RANGE

**all_in_cost**: current $7.0M. Plausible range is $6.5M to $12M, with a central value of $8.5M.

Basis:

- **No empirical anchor.** The verifier rated the size of the shortfall UNGROUNDED. No Unitaid, Global Fund or WHO costing was retrieved. The range is a judgement band, not an estimate.
- **Little headroom in the $7M.**
  - The ATORTUB IIc registry describes a pilot for a "fully international and multicenter" Phase III.
  - The Phase IIc itself costs about $320k.
  - A multi-country Phase III could plausibly absorb most of the $7M.
  - The low end of an add-on is therefore $0, not negative. I allow a slight optimistic case ($6.5M) because the direction is uncertain: the Phase III may be cheaper than feared, or WHO may absorb guideline work.
- **Central ($8.5M).** A modest +$1.5M for pharmacovigilance and dissemination that no commercial sponsor will fund.
- **High ($12M).** A +$5M add-on, which is the bottom of the critique's illustrative $5–20M. The illustrative top ($27M total) is reported below for transparency only. It is not adopted, per the verifier.

## SENSITIVITY ANALYSIS

The model is SROI = (eligible × uptake × baseline_mortality × relative_reduction × speedup × DALYs/death × $OP/DALY) / all_in_cost × p_success.

The benefit term is fixed at $OP 53.46B. So SROI ∝ 1/all_in_cost, and the breakeven against the 2,000x bar is 53.46B × 0.4 / 2,000 = **$10.69M**.

| all_in_cost | SROI | Δ vs base |
|---|---|---|
| $6.5M (optimistic) | 3,290x | +7.7% |
| **$7.0M (base)** | **3,055x** | — |
| $8.5M (central) | 2,516x | −17.6% |
| $10.0M | 2,138x | −30.0% |
| $10.69M (breakeven) | 2,000x | −34.5% |
| $12.0M (high) | 1,782x | −41.7% |
| $27.0M (illustrative only, ungrounded) | 792x | −74.1% |

**Interactions:**

- The effect is multiplicative with every other critique, since SROI = K × p_success / cost.
- The breakeven cost scales with the other factors. For example:
  - If `p_success` falls from 0.40 to 0.30, the breakeven cost falls to **$8.0M**.
  - If other critiques jointly cut the benefit by 30%, it falls to **$7.5M**. Even the central +$1.5M would then push SROI below the bar.
- This parameter's materiality therefore depends heavily on how the other threads resolve.

## BOTTOM-LINE IMPACT

This critique changes cost-effectiveness by between **+8% and −42%**, with a central estimate of about **−18%** (3,055x → 2,516x). On its own, it crosses the 2,000x bar only if adoption costs exceed about $3.7M. That figure has no empirical support either way.

## MATERIALITY VERDICT

**BORDERLINE.**

- The central case stays above the bar, and the evidence for any shortfall is ungrounded.
- However, the margin is thin: about $3.7M on a $7M base.
- Combined with plausible reductions from other threads (Thread 1 on `relative_reduction`, `p_success`, and Critique 1's delivery costs), modest cost overruns would become decisive.
- Obtaining a breakdown of the $7M is a high-value information request.

## CODE

```python
benefit = 5_500_000*(1-0.02)**(8-8)*0.60*0.06*0.10*1*27*100_000  # 53.46e9
p = 0.40
sroi = lambda c, p=p: benefit/c*p
base = sroi(7e6)
for c in [6.5e6, 7e6, 8.5e6, 10e6, 12e6, 27e6]:
    print(c, round(sroi(c)), f"{sroi(c)/base-1:+.1%}")
print("breakeven cost:", benefit*p/2000)          # 10.692e6
print("breakeven @p=0.30:", benefit*0.30/2000)    # 8.019e6
print("breakeven @benefit-30%:", benefit*0.7*p/2000)  # 7.484e6
```

## SENSITIVITY INPUTS

RANGE: all_in_cost | current 7000000 | low 6500000 | central 8500000 | high 12000000

--- Critique: Reference-class check: TB Phase III trials, and the evidence package WHO may require, point to more than one trial ---

# Impact of TB Phase III Reference-Class Costs on the TB-Statins SROI

## Critique

TB Phase III trials, and the evidence package WHO may require, point to a larger all-in cost than the $7M CG assumes.

## Parameter mapping

- **all_in_cost** (primary). The current value is $7,000,000, covering all funders through Phase III, guideline change and dissemination. It is the SROI denominator, so SROI scales as 1/all_in_cost.
- **p_success** (secondary, not quantified here). A cheap Phase III implies a pragmatic or surrogate-endpoint design and weaker mortality evidence. That link is speculative, so I hold p_success at 0.40 and keep this critique to the cost channel only.

## Plausible range for all_in_cost

The current value is $7.0M.

- **Low: $7M (unchanged).** The main counterargument holds. A generic oral adjunct with routine-care endpoints in drug-susceptible TB outpatient settings could be far cheaper than reference-class trials. I do not go below $7M, because CG already claims that figure includes Phase III and guideline work, and no evidence suggests it is too high.
- **Central: $20M.**
  - TB-PRACTECAL cost €33.9M (about $37M). Its €61k per patient reflects hospital-based drug-resistant TB care, so it overstates the cost for a drug-susceptible TB adjunct.
  - The Mullard/JAMA median for pivotal trials is about $19M. It is not TB-specific.
  - A single moderately sized, mortality-powered drug-susceptible TB trial plausibly costs $15–25M. The critique's own central range is $15–30M.
- **High: $40M.** This covers either one TB-PRACTECAL-scale trial, or one mid-size trial plus guideline, IPD and validation work. I excluded the multiple-trials scenario ($60M and above) because the WHO multi-trial requirement and the five named trial budgets are flagged as UNGROUNDED.

## Sensitivity analysis

**Base case.** Benefit = 5.5M × 0.6 × 0.06 × 0.10 × 1 × 27 × $100k = $OP 53.46B. SROI = 53.46B × 0.40 / 7M = **3,055x**.

| all_in_cost | SROI | Δ vs base |
|---|---|---|
| $7M (low/current) | 3,055x | 0% |
| $10M | 2,138x | −30% |
| **$10.69M (break-even at 2,000x bar)** | 2,000x | −35% |
| $15M | 1,426x | −53% |
| **$20M (central)** | **1,069x** | **−65%** |
| $30M | 713x | −77% |
| **$40M (high)** | **535x** | **−82.5%** |

**Optimistic direction.** There is no credible case for all_in_cost below $7M, so the upside is about 0%.

**Joint effect.** If a cheap design were paired with a lower p_success (for example 0.30 because only surrogate evidence is produced), SROI would be 2,291x at $7M. The two channels multiply, but the cost channel alone is the one this critique supports.

## Bottom-line impact

**This critique reduces SROI by 0% to about 83%, with a central estimate of about 65% (3,055x → about 1,070x).** Any all-in cost above about $10.7M pushes the grant below the 2,000x bar.

## Materiality verdict

**YES.** The central and high values both fall below the 2,000x funding bar. Only the scenario where CG's $7M is right keeps the grant above the bar, so the conclusion depends on this parameter.

## Code

```python
base = dict(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.6, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=1e5, speedup_years=1,
            all_in_cost=7e6, p_success=0.40)

def sroi(p):
    elig = p['eligible_people_at_8y']*(1-p['decline_per_year'])**(p['years_to_adoption']-8)
    deaths = elig*p['adult_uptake']*p['baseline_mortality']*p['relative_reduction']
    benefit = deaths*p['speedup_years']*p['dalys_per_death']*p['op_per_daly']
    return benefit/p['all_in_cost']*p['p_success']

b = sroi(base)
for c in [7e6, 10e6, 15e6, 20e6, 30e6, 40e6]:
    s = sroi({**base, 'all_in_cost': c})
    print(f"${c/1e6:.0f}M: {s:,.0f}x  Δ={100*(s/b-1):.1f}%")

benefit = b*base['all_in_cost']/base['p_success']
print("break-even cost at 2000x:", benefit*base['p_success']/2000)
```

## SENSITIVITY INPUTS

RANGE: all_in_cost | current 7000000 | low 7000000 | central 20000000 | high 40000000

--- Critique: The speedup benefit and the all-in cost come from different counterfactuals. Every coherent framing gives roughly 10–20x higher SROI. ---

# Impact assessment: speedup benefit vs. all-in cost counterfactual mismatch

## Critique

The speedup benefit and the all-in cost come from different counterfactuals. A consistent framing raises SROI under the "never" branch and is ambiguous under the "delay" branch.

## Parameter mapping

| Parameter | Current value | Role in this critique |
|---|---|---|
| `speedup_years` (primary) | 1 | Number of benefit-years credited against the all-in cost. A coherent framing changes this to "effective PV benefit-years per unit of PV cost." |
| `all_in_cost` | 7,000,000 | The cost-discount adjustment is folded into effective `speedup_years`, so `all_in_cost` is held fixed to avoid double-counting. |
| Implicit discount rate | 0 | Not a model parameter. Its effect is translated into effective `speedup_years`. |
| `decline_per_year`, `years_to_adoption` | 0.02, 8 | Used only to compute the effective benefit-year multiplier. Not varied. |

**Why `speedup_years` is the right lever.** SROI is linear in `speedup_years`. "Coherent SROI = BOTEC × (effective benefit-years × cost-discount adjustment)" is therefore exactly equivalent to setting `speedup_years` to that product.

## Deriving plausible values for effective `speedup_years`

Benefits start at year 8. With r = 4% and the 2% annual decline, the per-year ratio is 0.98/1.04 = 0.9423. Benefits are deflated by 1.04⁻⁸ = 0.731. Costs are spread over about 8 years, giving a PV factor of about 0.85.

| Framing | PV benefit-years | ÷ cost factor (0.85) | Effective `speedup_years` | SROI |
|---|---|---|---|---|
| Delay branch, other funders' dollars displaced at about the CG bar | below 1 | n/a | ~0.4–0.6 | ~1,200–1,800x |
| Delay branch, discounting only (current BOTEC framing made consistent) | 0.731 | 0.86 | ~0.86 | ~2,630x |
| BOTEC as published | 1 (undiscounted) | 1 | 1 | 3,055x |
| Never branch, 10-yr horizon (obsolescence/new regimens) | 5.67 | 6.7 | 6.7 | ~20,400x |
| Never branch, 15-yr horizon | 7.5 | 8.8 | 8.8 | ~26,900x |
| Never branch, perpetuity, 2% decline | 12.7 | 14.9 | 14.9 | ~45,500x |
| Never branch, perpetuity, no decline (r = 4%) | 25 × 0.731 = 18.3 | ~21 | ~18–21 | ~55,000–65,000x |

The "time-value-only" delay framing gives a much higher ratio. It charges only the interest on $7M (about $280k) against one discounted benefit-year, roughly 7–8× BOTEC. However, it assumes other funders' money has zero opportunity cost, which is not credible. I treat it as subsumed by the never-branch upper range rather than as a separate high case.

**Choice of range.**
- **Low = 0.5.** Delay branch with displacement charged.
- **High = 15.** Never branch, long horizon. I exclude values around 20, which require no decline, a perpetuity, and costless co-funding.
- **Central = 5.** This is a rough 50/50 weighting of the delay branch (~0.8) and a finite-horizon never branch (~9). It reflects genuine uncertainty about which counterfactual applies. CG's own 4.5% share framing hints that the trial would plausibly happen eventually without CG, which favours the delay branch.

## Sensitivity analysis

| Case | Effective `speedup_years` | SROI | Δ vs. base |
|---|---|---|---|
| Base | 1 | 3,055x | — |
| Low (displacement charged) | 0.5 | 1,527x | −50% (falls below the 2,000x bar) |
| Delay, discount only | 0.86 | 2,627x | −14% |
| Central | 5 | 15,275x | +400% |
| Never, 15-yr horizon | 8.8 | 26,880x | +780% |
| High | 15 | 45,824x | +1,400% |

**Interactions.** These multipliers are multiplicative with every other critique: p_success, relative_reduction, and uptake all scale SROI linearly. A 5–15× framing multiplier would absorb large downward revisions elsewhere. For example, relative_reduction at 0.03 with a 10× multiplier still gives about 9,000x.

**Robustness of the ranking.** The ranking "coherent ≥ BOTEC" holds whenever effective benefit-years exceed about 1. That means a never-branch horizon longer than about 2 years. It fails in the delay branch.

## Bottom-line impact

Making the counterfactual consistent changes SROI by between −50% and +1,400%, depending on the framing. Delay-branch framings give −14% to −50%. Never-branch framings give +500% to +1,400%. The central estimate is about +400% (around 15,000x), and it is highly assumption-dependent. The 30,000–55,000x figures should be reported only as a conditional upper scenario.

## Materiality verdict

**YES.** The plausible range spans the 2,000x funding bar on the low side (1,527x) and changes SROI by an order of magnitude on the high side. The direction is genuinely ambiguous. This is a structural framing issue rather than a parameter tweak.

## Code

```python
def sroi(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=1e5, speedup_years=1,
         all_in_cost=7e6, p_success=0.40):
    eligible = eligible_people_at_8y*(1-decline_per_year)**(years_to_adoption-8)
    deaths = eligible*adult_uptake*baseline_mortality*relative_reduction
    benefit = deaths*speedup_years*dalys_per_death*op_per_daly
    return benefit/all_in_cost*p_success

base = sroi()
r, g, start, cost_pv = 0.04, 0.02, 8, 0.85
q = (1-g)/(1+r); lag = (1+r)**-start
def eff_years(H=None):
    pv = (1-q**H)/(1-q) if H else 1/(1-q)
    return pv*lag/cost_pv
cases = {"low":0.5, "delay_disc":lag/cost_pv, "central":5,
         "never_10y":eff_years(10), "never_15y":eff_years(15),
         "never_perp":eff_years(), "high":15}
for k,v in cases.items():
    s = sroi(speedup_years=v)
    print(f"{k:12s} eff_years={v:5.2f} SROI={s:8.0f} delta={s/base-1:+.0%}")
```

## Sensitivity inputs

RANGE: speedup_years | current 1 | low 0.5 | central 5 | high 15

--- Critique: The funding landscape for a generic-statin TB program makes "never" a live branch. The speedup is a poor proxy for the grant's real counterfactual. ---

# CRITIQUE: The funding landscape makes "never" a live branch; the 1-year speedup is a poor proxy for the counterfactual

## Parameter Mapping

| Parameter | Model key | Current value | Role in this critique |
|---|---|---|---|
| Years of acceleration credited | `speedup_years` | 1 | Primary. Should be an expected value E[S] = q·D + (1−q)·1, where q is the probability nobody runs a statin-TB Phase III without this grant. It could be above 1 (the "never/very late" branch) or below 1 (the grant is redundant). |
| Probability Phase II and III both succeed | `p_success` | 0.40 | Secondary. The null rosuvastatin Phase 2b should lower it. |
| All-in cost | `all_in_cost` | $7,000,000 | **Not changed.** See the note on the "20×" claim below. |

**Note on the "SROI about 20× higher" claim.** $7.0M / $0.32M = 21.9×. That ratio comes only from putting the full downstream benefit over CG's own grant cost. CG's framing credits its ~4.5% cost share with ~4.5% of benefits, which leaves SROI unchanged. Crediting 100% of benefits to the $320k double-counts the other funders' $6.7M. I exclude this claim, as the critique itself recommends. Within a consistent accounting, the "never" branch can only enter through `speedup_years`.

## Plausible Ranges

**`speedup_years`: current 1; low 0.5, central 1.25, high 3.**
- **Low (0.5).** The rosuvastatin Phase 2b and NIAID-funded statin work show a live pipeline, so someone else might run a comparable trial with some delay. This is the "redundant grant" direction.
- **High (3).** Assume q ≈ 0.3–0.5 and a counterfactual delay D ≈ 5–7 years in the never/very-late branch. That gives E[S] ≈ 0.4×6 + 0.6×1 = 3.0.
  - I cap it here. With no discounting, a literal "never" branch implies an unbounded benefit stream, which is not credible given competing HDTs, regimen changes and declining incidence.
- **Central (1.25).** A modest upward expectation. The evidence base is thin: I found no registered statin-TB Phase III, but the search was not exhaustive, and q is unestimated.

**`p_success`: current 0.40; low 0.20, central 0.30, high 0.40.**
- The null rosuvastatin Phase 2b is a different statin, and the atorvastatin rationale (prior surrogate signals) partly survives. So I apply a moderate downward update rather than a collapse.
- The 2026 review notes that HDTs still lack Phase III validation. That is consistent with a lower prior.

## Sensitivity Analysis

The base case is SROI = **3,055×**. The funding bar is 2,000×. SROI is linear in both parameters, so their joint effects are **multiplicative**.

**One parameter at a time:**

| Scenario | SROI | Δ vs base |
|---|---|---|
| speedup = 0.5 | 1,527× | −50% |
| speedup = 1.25 | 3,819× | +25% |
| speedup = 3 | 9,164× | +200% |
| p_success = 0.20 | 1,527× | −50% |
| p_success = 0.30 | 2,291× | −25% |

**Both parameters together:**

| Scenario | SROI | Δ vs base | Position vs 2,000× bar |
|---|---|---|---|
| Pessimistic (S = 0.5, p = 0.2) | 764× | −75% | Below |
| Central (S = 1.25, p = 0.3) | 2,864× | −6% | Above |
| Mixed (S = 3, p = 0.2) | 4,582× | +50% | Above |
| Optimistic (S = 3, p = 0.4) | 9,164× | +200% | Above |

In absolute terms, credited benefit per $ of all-in cost ranges from $OP 764 to $OP 9,164, against the current $OP 3,055.

## Bottom-Line Impact

The central estimate is roughly neutral (−6%), because the longer expected speedup roughly offsets the lower p_success after the null rosuvastatin result. The plausible range is very wide, from −75% to +200%. The direction hinges on the unestimated q, and the speedup evidence is logic-only.

## Materiality Verdict

**BORDERLINE (leaning YES on range).**
- The central estimate barely moves the SROI and stays above the 2,000× bar.
- The joint-pessimistic case falls below the bar, as does p_success = 0.2 alone (1,527×).
- The optimistic case triples the SROI.
- The value of resolving q (is anyone else funding a statin-TB Phase III?) is high.

## Code

```python
base = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
            all_in_cost=7_000_000, p_success=0.40)

def sroi(p):
    elig = p['eligible_people_at_8y']*(1-p['decline_per_year'])**(p['years_to_adoption']-8)
    deaths = elig*p['adult_uptake']*p['baseline_mortality']*p['relative_reduction']
    benefit = deaths*p['speedup_years']*p['dalys_per_death']*p['op_per_daly']
    return benefit/p['all_in_cost']*p['p_success']

b = sroi(base)
print(f"base {b:.0f}")
for k, vals in {'speedup_years':[0.5,1.25,3], 'p_success':[0.2,0.3,0.4]}.items():
    for v in vals:
        s = sroi({**base, k:v}); print(k, v, round(s), f"{s/b-1:+.0%}")
for S, ps in [(0.5,0.2),(1.25,0.3),(3,0.2),(3,0.4)]:
    s = sroi({**base,'speedup_years':S,'p_success':ps}); print(S, ps, round(s), f"{s/b-1:+.0%}")
print("grant-only ratio (excluded):", 7_000_000/320_000)
```

## SENSITIVITY INPUTS

RANGE: speedup_years | current 1 | low 0.5 | central 1.25 | high 3
RANGE: p_success | current 0.40 | low 0.20 | central 0.30 | high 0.40

--- Critique: Discounting quantified properly with an S-curve ramp and discounted costs. The net effect is about −20% to −31%, not the benefit-only −21% to −35%. ---

# Quantification: net discounting with an S-curve ramp and discounted costs

## Parameter mapping

The model has **no discount-rate parameter**. The formula chain notes "No time discounting", which is an implicit rate of 0. Discounting multiplies the whole SROI by one net factor:

  Net factor F = DF_benefit / DF_cost

To get this into the model I apply F through **speedup_years**. That parameter enters the benefit linearly, so `speedup_years_eff = 1 × F` reproduces the discounted SROI exactly. I do not also change all_in_cost, which would double count.

**Why the uniform-over-ramp timing is the right one for this model.** CG credits a 1-year shift of the adoption curve. Shifting a ramp-then-plateau curve by one year produces an incremental benefit equal to one plateau-year of flow (19,800 deaths). That increment is spread uniformly across the ramp window [t₀, t₀+L]. The critique's formula, e^(−r·t₀)·(1−e^(−rL))/(rL), is therefore the correct benefit discount factor for this framing.

- **speedup_years:** location = benefit term; current = 1; effective value = F.

## Plausible range

The timing assumptions are illustrative and taken from the critique: ramp start t₀ = 8.5, ramp length L = 6 (or 10), costs uniform over years 0–8. Only the L = 10 ramp-length arithmetic was independently checked by the Verifier.

| Rate | L | DF_benefit | DF_cost | Net F | Penalty |
|---|---|---|---|---|---|
| 3% | 6 | 0.709 | 0.889 | 0.798 | −20.2% |
| 4% | 6 | 0.633 | 0.856 | 0.739 | −26.1% |
| 5% | 6 | 0.565 | 0.824 | 0.685 | −31.5% |
| 4% | 10 | 0.587 | 0.856 | 0.685 | −31.5% |
| 5% | 10 | 0.515 | 0.824 | 0.624 | −37.6% |

These reproduce the critique's −20% / −25 to −27% / −31%. A longer ramp (L = 10) pushes the penalty to −31% to −38%.

**Cost-timing sensitivity:**
- If costs are front-loaded (DF_cost → 1), the net penalty approaches the benefit-only figures of −29% to −44%.
- If costs are back-loaded into Phase III (years 5–8), DF_cost falls and the penalty shrinks by a few points.
- Stage-probability weighting of costs (Critique 4) shifts expected spend toward the near term. This raises DF_cost slightly and so makes the penalty slightly larger, not smaller.

## Sensitivity analysis

**Base case:** SROI = 19,800 × 1 × 27 × 100,000 / 7,000,000 × 0.4 = **3,055x**. The bar is 2,000x.

| Scenario | speedup_years (eff.) | SROI | Δ |
|---|---|---|---|
| 0% (current) | 1.00 | 3,055x | 0 |
| 3%, L = 6 | 0.798 | 2,437x | −20% |
| 4%, L = 6 | 0.739 | 2,258x | −26% |
| 5%, L = 6 | 0.685 | 2,093x | −31% |
| 4%, L = 10 | 0.685 | 2,092x | −31% |
| 5%, L = 10 (pessimistic joint) | 0.624 | 1,906x | −38% (**below the 2,000x bar**) |
| Benefit-only 4%, L = 6 (critique's comparison) | 0.633 | 1,934x | −37% |

**Interactions.** Rate and ramp length combine multiplicatively inside DF_benefit. Their combined effect on SROI is a single multiplicative factor, and it compounds multiplicatively with any other critique's adjustment.

**Optimistic direction.** Discounting can only lower SROI relative to the current zero-discount model. The upside case is the status quo (Δ = 0).

## Bottom-line impact

Consistent discounting of benefits and costs reduces SROI by **20% to 38%**, with a central estimate of about −26% (4%, L = 6, SROI ≈ 2,260x). The estimate stays above the 2,000x bar except under a 5% rate combined with a 10-year ramp.

## Materiality verdict

**BORDERLINE.**
- The central estimate (−26%) sits at the 25% threshold.
- The range runs from below it (3%: −20%) to well above it (5%/L = 10: −38%).
- Alone, it crosses the funding bar only in the most pessimistic timing case.
- Because it is multiplicative, it would push the estimate below the bar when combined with even modest adverse findings from other threads, for example a uptake or relative_reduction cut of 10% or more.
- The result is highly sensitive to the real timeline, which the CEA does not specify.

## Code

```python
import math
base = 5.5e6*0.6*0.06*0.10*1*27*1e5/7e6*0.4  # 3054.9

def df_uniform(r, a, L):  # mean of e^{-rt} over [a, a+L]
    return math.exp(-r*a)*(1-math.exp(-r*L))/(r*L)

for r, L in [(.03,6),(.04,6),(.05,6),(.04,10),(.05,10)]:
    B = df_uniform(r, 8.5, L)
    C = df_uniform(r, 0, 8)
    F = B/C
    print(r, L, round(B,3), round(C,3), round(F,3),
          round(base*F), f"{F-1:+.1%}", "benefit-only:", round(base*B))
```

## SENSITIVITY INPUTS

RANGE: speedup_years | current 1 | low 0.62 | central 0.74 | high 0.80

--- Critique: A 1-year speedup of trial results does not necessarily become a 1-year speedup of adoption, in either direction. ---

# CRITIQUE: A 1-year trial speedup need not become a 1-year adoption speedup

## Parameter mapping

| Parameter | Location | Current value | Role |
|---|---|---|---|
| `speedup_years` | Benefit term | 1 | Linear multiplier on benefit and SROI |
| `years_to_adoption` | Decline exponent | 8 | Unaffected by this critique |

On `years_to_adoption`: the critique concerns the gap between the counterfactual and actual timelines, not the absolute timing. With `years_to_adoption = 8` the exponent is 0, so this parameter does not interact here.

`adult_uptake` and the adoption-curve shape do not change the result under the model's zero discounting. If uptake ramps and the whole ramp shifts by Δt, the integrated benefit difference equals Δt × plateau deaths averted. This holds only if the full curve shifts. A downstream bottleneck that is independent of trial timing breaks this, and that bottleneck is exactly what the critique describes.

## How a downstream bottleneck shrinks the speedup

Let q be the probability (or fraction of the timeline) where a bottleneck independent of trial timing binds. Examples are national policy cycles, procurement, and drug price or availability (as documented for rifapentine). In those cases the trial speedup is absorbed. Then:

- effective speedup = (1 − q) × 1 + q × s_absorbed, where s_absorbed ≈ 0–0.3
- the upside is a missed WHO window adding to the delay. This is weakly supported: WHO acted within months for Study 31/HPMZ and BPaLM. I allow at most +0.2 years in expectation.

## Plausible range for `speedup_years`

| Case | Value | Basis |
|---|---|---|
| Low | 0.5 | q ≈ 0.6 with little residual credit. National lags are binding and unquantified (UNGROUNDED). |
| Central | 0.85 | q ≈ 0.15–0.2. WHO is responsive, with modest downstream absorption. |
| High | 1.2 | Occasional missed guideline or procurement window. Weakly supported. |

## Sensitivity analysis

Base case: deaths averted per year = 5.5M × 0.6 × 0.06 × 0.10 = 19,800. SROI = 19,800 × 1 × 27 × 100,000 / 7M × 0.4 = **3,055x**.

| `speedup_years` | SROI | Δ vs base |
|---|---|---|
| 0.50 (low) | 1,527x | −50% |
| 0.655 (break-even with 2,000x bar) | 2,000x | −35% |
| 0.85 (central) | 2,597x | −15% |
| 1.20 (high) | 3,666x | +20% |

Joint effects: SROI is linear in `speedup_years` and multiplies with every other parameter, so this effect compounds with other critiques (e.g., `relative_reduction`, `adult_uptake`). Combined with any other independent −20% haircut, the central case 0.85 gives 2,078x, close to the bar.

## Bottom-line impact

This critique moves cost-effectiveness by −50% to +20%, with a central estimate of about −15% (3,055x → ~2,600x). The direction leans downward.

## Materiality verdict

**BORDERLINE.** The central estimate stays above the 2,000x bar. However, any effective speedup below ~0.65 years, which is plausible if national adoption lags bind, pushes the grant below the bar. The national-lag evidence is UNGROUNDED, so this deserves explicit justification by Coefficient Giving.

## Code

```python
def sroi(eligible=5_500_000, yta=8, decline=0.02, uptake=0.60, mort=0.06,
         rr=0.10, dalys=27, op=100_000, speed=1.0, cost=7_000_000, p=0.40):
    elig = eligible*(1-decline)**(yta-8)
    deaths = elig*uptake*mort*rr
    return deaths*speed*dalys*op/cost*p

base = sroi()
for s in [0.5, 0.655, 0.85, 1.0, 1.2]:
    v = sroi(speed=s); print(s, round(v), f"{v/base-1:+.0%}")
print("break-even speedup:", 2000/base)  # 0.655
```

## SENSITIVITY INPUTS

RANGE: speedup_years | current 1 | low 0.5 | central 0.85 | high 1.2

--- Critique: Post-TB lung disease morbidity is likely the largest unvalued channel (~50–60k central, wide range) ---

# Post-TB Lung Disease Morbidity as an Unvalued Benefit Channel

## Parameter Mapping

The BOTEC values only on-treatment mortality ("only mortality is valued"). This critique adds a new benefit term: **post-TB lung morbidity DALYs averted**. The model has no parameter for it, so I fold it into the effective value of **`dalys_per_death`**. That is the only model parameter that scales benefit linearly without changing the mortality mechanics.

| Parameter | Current | Role |
|---|---|---|
| `dalys_per_death` | 27 | Receives the added morbidity DALYs, re-expressed per mortality death averted |
| `relative_reduction` | 0.10 | Not changed. The morbidity term uses its own 5% reduction on lung outcomes |
| `p_success` | 0.40 | Not changed. The critique's 0.45 weight is absorbed into the translation below |

**Translation into `dalys_per_death`:**

- Expected morbidity DALYs per adoption-year ÷ expected deaths averted per adoption-year (19,800 × 0.40 = 7,920) = extra DALYs per death.
- Effective `dalys_per_death` = 27 + that extra amount.
- This works because the term enters the chain multiplicatively and in parallel with mortality, so it scales SROI exactly like DALYs per death.

## Plausible Range

**Central case: about 55.7k expected DALYs.**
- Treated patients: 3.3M.
- Baseline post-TB morbidity: 0.75 DALYs per treated patient.
- Reduction attributable to the intervention: 5%.
- Probability weight: 0.45.
- This is +7.03 DALYs per death, so effective `dalys_per_death` ≈ 34.0.

**Low case: about 10k expected DALYs.**
- Uses a 2% reduction and a lower baseline (about 0.34 DALYs per patient).
- This is +1.26 DALYs per death, so effective `dalys_per_death` ≈ 28.3.

**High case: about 300k expected DALYs.**
- Uses a 15% reduction and a 1.5 DALYs per patient baseline.
- This is +37.9 DALYs per death, so effective `dalys_per_death` ≈ 64.9.
- The upside is supported by:
  - Menzies 2021: 5.8 post-TB DALYs per case.
  - 2025 Lancet Global Health: post-TB DALYs are 52.5% of total.

**Caveats:**
- The 5% reduction and the persistence of the lung-damage benefit are ungrounded. Treat the central case as illustrative.
- The Menzies scope includes post-TB mortality. Combining with Critique 2 must avoid double-counting, since both apply the same lung-damage reduction. The high case therefore should not also be stacked with a separate post-TB mortality term.

## Sensitivity Analysis

**Base case:**
- 19,800 deaths averted per year.
- 534,600 DALYs credited, or 213,840 expected DALYs after `p_success`.
- SROI = **3,055x**.

**Undiscounted (CG convention):**

| Scenario | Added expected DALYs | Eff. `dalys_per_death` | SROI | Δ |
|---|---|---|---|---|
| Low | 10,000 | 28.3 | 3,198x | +4.7% |
| Central | 55,700 | 34.0 | 3,851x | +26.0% |
| High | 300,000 | 64.9 | 7,341x | +140% |

**Discounted version (3%, morbidity stream over about 20 years; annuity factor 0.744):**
- This applies only to the long-lag morbidity stream. Mortality stays undiscounted, which is CG's convention.
- Central: about 41.4k DALYs, giving 3,647x (+19%).
- Low: 3,161x (+3.5%).
- High: 6,244x (+104%).
- Discounting removes roughly a quarter of the channel. It is partly an artifact of the no-discount convention, but it is not the dominant uncertainty. The dominant uncertainties are the reduction percentage and the baseline burden.

**Interactions:**
- The term is additive to mortality DALYs in the numerator and multiplicative with uptake, eligible patients and cost.
- If `p_success` were lowered elsewhere (for example a mortality-endpoint failure), this channel partly survives through the morbidity-only adoption branch. That makes the overall estimate more robust than the mortality-only model implies.

## Bottom-Line Impact

**Valuing post-TB lung morbidity raises SROI by about +5% to +140%, with a central estimate of about +26% (3,055x → ~3,850x), or about +19% if the morbidity stream is discounted.**

## Materiality Verdict

**NO, for the decision. BORDERLINE in the upper range.**

- The critique moves cost-effectiveness upward, from an estimate already about 1.5× the 2,000x bar, so it cannot flip the funding decision.
- The central value of about 55.7k DALYs is below the 134k threshold. The threshold is crossed only in the upper half of the range (reduction ≥ ~8% with a baseline ≥ ~1 DALY per patient).
- Its main relevance is robustness: it cushions the estimate against pessimistic Thread 1 findings on on-treatment mortality.

## Code

```python
def sroi(eligible=5.5e6, yta=8, decl=0.02, uptake=0.6, bm=0.06, rr=0.10,
         dpd=27, opd=1e5, speed=1, cost=7e6, p=0.40):
    treated = eligible*(1-decl)**(yta-8)*uptake
    deaths = treated*bm*rr
    return deaths*speed*dpd*opd/cost*p, deaths

base, deaths = sroi()                      # 3054.9, 19800
exp_deaths = deaths*0.40                   # 7920
treated = 3.3e6

def morb(baseline, red, w=0.45, disc=1.0):
    return treated*baseline*red*w*disc

ann = (1-1.03**-20)/(0.03*20)              # 0.744

for name, add in [("low", 10_000),
                  ("central", morb(0.75, 0.05)),
                  ("high", 300_000)]:
    for d in (1.0, ann):
        a = add*d
        eff = 27 + a/exp_deaths
        s, _ = sroi(dpd=eff)
        print(name, round(d, 3), round(a), round(eff, 1), round(s), f"{s/base-1:+.1%}")
```

## Sensitivity Inputs

RANGE: dalys_per_death | current 27 | low 28.3 | central 34.0 | high 64.9

--- Critique: Post-treatment excess mortality (~40–50k central) and a related sign-reversing adjustment ---

# CRITIQUE: Post-treatment excess mortality and the sign-reversing life-expectancy adjustment

## Parameter Mapping

The model values only on-treatment deaths averted. Both channels of this critique change the DALYs credited per on-treatment death averted, so both map onto one model parameter.

- **dalys_per_death** (current value 27).
  - **Channel (b)** directly lowers it. The deaths averted fall in a higher-risk subpopulation (HIV, malnutrition, advanced disease), and those people have shorter residual life expectancy.
  - **Channel (a)** adds a new benefit term: post-treatment deaths averted multiplied by DALYs per death. The formula chain has no slot for this. I converted it into an equivalent increment per on-treatment death averted, using the formula below.

> Δdalys_per_death = (post-treatment DALYs averted per patient × treated) / (on-treatment deaths averted per year)

The other parameters (relative_reduction, baseline_mortality, adult_uptake, p_success, all_in_cost) are unchanged by this critique.

### Correction to the critique's own arithmetic

The critique sets "~45k after weighting" (after the p_success discount) against "535k". But 534,600 is the model's DALYs credited **before** the p_success discount. The model applies p_success only at the SROI step.

Comparing like with like, channel (a) at the critique's illustrative values is about **+99k DALYs against 534.6k**, or +18.5%. It is not +45k. Channel (b) is −27k to −53k on the same pre-p basis.

The net range is therefore roughly **−53k to +99k**. The critique's −25k to +45k is not the right range. At the critique's own illustrative values, the net is modestly positive, not zero.

## Plausible Range

### Channel (a): post-treatment deaths averted

The critique's values give 0.10 × 0.40 × 0.05 = 0.002 deaths per patient, at 15 DALYs each. That is 0.03 DALYs per patient. Across 3.3M treated patients, it comes to 99,000 DALYs, or +5.0 DALYs per on-treatment death averted (99,000 / 19,800).

- **Low: +0.**
  - The respiratory share and the 5% reduction are UNGROUNDED.
  - A 6-month statin course has no demonstrated effect on long-run survival.
  - The verifier notes that this channel overlaps Critique 1 and the Menzies post-TB burden framework. Crediting it here risks double-counting.
- **Central: +2.5.** This halves the illustrative value to reflect the overlap and lack of grounding.
- **High: +5.0.** These are the critique's illustrative values. Romanowski 2019 (standardized mortality ratio of about 2.9) makes ~10% cumulative 10-year excess mortality plausible. The 40% respiratory share and the 5% reduction carry the uncertainty.

### Channel (b): life-expectancy overstatement

The critique proposes a reduction of 5–10%, which is UNGROUNDED. This gives a range of −2.7 to 0 DALYs per death.

- **Low: −2.7** (−10%).
- **Central: −2.0** (−7.5%).
- **High: 0.** CG describes 27 as *remaining healthy* life expectancy. At typical TB death ages of 35–50, standard life expectancy is 30–45 years, so 27 may already embed a comorbidity or morbidity haircut.

### Combined effective dalys_per_death

| Scenario | Value | Construction |
|---|---|---|
| Low | 24.3 | (b) −10%, (a) 0 |
| Central | ≈27.5 | 27 × 0.925 + 2.5 |
| High | 32.0 | (b) 0, (a) +5 |

## Sensitivity Analysis

```python
def sroi(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=1e5, speedup_years=1,
         all_in_cost=7e6, p_success=0.40):
    eligible = eligible_people_at_8y*(1-decline_per_year)**(years_to_adoption-8)
    treated = eligible*adult_uptake
    deaths = treated*baseline_mortality*relative_reduction
    dalys = deaths*speedup_years*dalys_per_death
    return dalys, dalys*op_per_daly/all_in_cost*p_success, deaths, treated

base_dalys, base, deaths, treated = sroi()          # 534,600 ; 3054.9
# Channel (a) conversion
post_dalys = 0.10*0.40*0.05*15*treated               # 99,000
add_per_death = post_dalys/deaths                    # 5.0
scen = {
 "b only -5%":   27*0.95,
 "b only -10%":  27*0.90,
 "a only +2.5":  27+2.5,
 "a only +5":    27+5.0,
 "joint pess":   27*0.90+0,
 "central":      27*0.925+2.5,
 "joint opt":    27+5.0,
 "critique pts": 27*0.925+5.0,
}
for k,d in scen.items():
    dl,s,_,_ = sroi(dalys_per_death=d)
    print(f"{k:14s} dpd={d:5.2f} DALYs={dl:9,.0f} SROI={s:7.0f} Δ={(s/base-1)*100:+.1f}%")
# break-even vs 2,000x bar
print(27*2000/base)   # 17.7
```

Base case: 534,600 DALYs credited, **SROI 3,055x**.

| Scenario | dalys_per_death | DALYs credited | SROI | Δ |
|---|---|---|---|---|
| (b) −5% | 25.65 | 507,870 | 2,902x | −5.0% |
| (b) −10% | 24.30 | 481,140 | 2,749x | −10.0% |
| (a) +2.5 | 29.50 | 584,100 | 3,338x | +9.3% |
| (a) +5 (critique values) | 32.00 | 633,600 | 3,621x | +18.5% |
| **Joint pessimistic** | 24.30 | 481,140 | **2,749x** | **−10.0%** |
| **Central** | 27.48 | 544,005 | **3,109x** | **+1.8%** |
| Joint optimistic | 32.00 | 633,600 | 3,621x | +18.5% |
| Critique's own midpoints, (b) −7.5% and (a) +5 | 29.98 | 593,505 | 3,392x | +11.0% |

**Interactions.** The two channels are additive within dalys_per_death. Their combined effect on SROI is multiplicative with every other parameter, because SROI is linear in dalys_per_death. If Thread 1 lowers relative_reduction, channel (b) scales down proportionally. Channel (a), as constructed, assumed its own 5% effect, but the conversion here ties it to on-treatment deaths, so it scales with relative_reduction too. That is a reasonable simplification if both effects depend on the same drug efficacy.

**Break-even.** SROI falls to the 2,000x bar only if dalys_per_death drops to about 17.7. That is a 35% cut, far outside this critique's range.

## Bottom-Line Impact

**This critique moves SROI by between −10% and +18.5% (about 2,750x to 3,620x). The central estimate is about +2%, so it is effectively a wash. The net sign leans positive once the critique's p_success weighting error is corrected.**

## Materiality Verdict

**BORDERLINE, leaning NO.**
- The downside (−10%) only reaches a typical 10% threshold at the extreme of an UNGROUNDED range.
- The central estimate is roughly zero.
- No scenario comes close to the 2,000x bar.
- The upside channel overlaps Critique 1 (post-TB burden), so it should be merged rather than counted separately.

## Sensitivity Inputs

RANGE: dalys_per_death | current 27 | low 24.3 | central 27.5 | high 32

--- Critique: Transmission benefit is small, with a bounded calculation (~10–30k central) ---

# Transmission benefit is small, with a bounded calculation (~10–30k central)

## Bottom line

Adding a transmission channel raises SROI by about **+0.6% to +19%**, with a central estimate of **about +5%** (3,055x → about 3,200x). The direction is upward only: this is an omitted benefit, with a floor at zero. Treat these numbers as an order of magnitude only, because every transmission input is ungrounded.

## Parameter mapping

The model has no transmission term. Its formula chain values only on-treatment mortality. The critique adds a new benefit term, which I translate into an effective `dalys_per_death`. Because benefit is linear in `dalys_per_death`, this is exact.

- **dalys_per_death:** current value 27.
  - Effective value = 27 × (534,600 + T) / 534,600.
  - T is transmission DALYs per speedup-year, conditional on success (before applying p).
- **Why T is a pre-p quantity.** The model's 534,600 credited DALYs are also conditional on success; `p_success` (0.40) is applied afterwards in the SROI step. T must be on the same basis.
  - The critique's "50k pre-p" figure is the comparable number.
  - Its "~20k after weighting" is roughly that figure × p. Using it as well would apply p twice.
- **Treated base.** The critique's 3.3M is the model's treated population: 5,500,000 × 0.60 = 3,300,000. The bases are consistent.
- **Interaction caveat.** The transmission benefit scales with faster culture conversion, not with `relative_reduction`. Expressing it through `dalys_per_death` makes it scale with mortality inputs, which it shouldn't. If another thread changes `relative_reduction` or `baseline_mortality`, the effective `dalys_per_death` here should be recomputed.

## Plausible range for T (DALYs, pre-p)

The critique's own range comes from treated × secondary cases × net reduction × DALYs per secondary case:

| Case | Inputs | T |
|---|---|---|
| Critique's mechanism, low | 3.3M × 0.3 × 0.001 × 10 | 9.9k |
| Critique's mechanism, central | 3.3M × 0.5 × 0.003 × 10 | 49.5k |
| Critique's mechanism, high | 3.3M × 1 × 0.01 × 10 | 330k (extreme tail) |
| **Adopted low** | Weak conversion signal, as in ROSETTA | **3k** |
| **Adopted central** | 50k haircut about 50% (see below) | **25k** |
| **Adopted high** | Tail capped (see below) | **100k** |

- **Why haircut the central by about 50%.** The guinea-pig data show infectiousness falls sharply with effective therapy regardless of culture status. Culture conversion is therefore a weak proxy for infectiousness, and the critique flags saturation as a further downward adjustment.
- **Why cap the high at 100k.** The MDR-TB experiment showed about 27.8% of animals infected 72 hours after treatment start, which keeps some upper tail alive. The 330k corner requires every input at its maximum at once.

## Sensitivity analysis

Base SROI is 3,054.9x. Each added DALY contributes 100,000 / 7,000,000 × 0.4 = 0.005714x.

| T (pre-p DALYs) | Effective dalys_per_death | SROI | Change |
|---|---|---|---|
| 0 (status quo) | 27.00 | 3,055x | 0% |
| 3k (low) | 27.15 | 3,072x | +0.56% |
| 25k (central) | 28.26 | 3,198x | +4.7% |
| 50k (critique's point estimate) | 29.53 | 3,340x | +9.4% |
| 100k (high) | 32.05 | 3,626x | +18.7% |
| 150k (critique's stated tail) | 34.58 | 3,912x | +28% |

- **Pessimistic direction.** The effect cannot go below zero, so the pessimistic case is T = 0, leaving SROI at 3,055x.
  - Any adverse effects (hepatotoxicity, myopathy) belong to other threads, not this transmission channel.
- **Joint effects.** The effect adds DALYs before p is applied. It then multiplies with `p_success` and `all_in_cost`, and is independent of the mortality chain.
- **Funding bar.** The recommendation does not change. The model already clears the 2,000x bar, and this channel can only increase SROI.

## Materiality verdict

**NO, or borderline at most.** The central estimate (+5%) is below a typical 10% threshold. Only the heavy upper tail (+19% to +28%) exceeds it, and that tail depends on ungrounded inputs. The direction is favorable and does not change the funding decision.

## Code

```python
base = dict(elig=5.5e6, upt=0.6, mort=0.06, rr=0.10, dpd=27, op=1e5,
            spd=1, cost=7e6, p=0.4)

def sroi(dpd=27, extra_dalys=0):
    treated = base['elig'] * base['upt']
    dalys = treated * base['mort'] * base['rr'] * base['spd'] * dpd + extra_dalys
    return dalys * base['op'] / base['cost'] * base['p'], dalys

b, D0 = sroi()                                   # 3054.86, 534600
for T in [0, 3e3, 25e3, 50e3, 100e3, 150e3]:
    s, _ = sroi(extra_dalys=T)
    eff = 27 * (D0 + T) / D0
    assert abs(sroi(dpd=eff)[0] - s) < 1e-6
    print(T, round(eff, 2), round(s, 1), f"{s/b-1:+.2%}")
```

## Sensitivity inputs

RANGE: dalys_per_death | current 27 | low 27.15 | central 28.26 | high 32.05

--- Critique: The "lung benefit without mortality benefit" scenario is structurally less valuable than a simple p_success weighting implies ---

# CRITIQUE: The "lung benefit without mortality benefit" scenario is structurally less valuable than a simple p_success weighting implies

## Parameter Mapping

This critique corrects how other critiques' **lung/morbidity add-on benefit terms** should be weighted. Those terms are not in the current model, which states that "only mortality is valued."

| Parameter | Current value | Affected? |
|---|---|---|
| p_success | 0.40 | Not changed. It gates the mortality channel, and the critique leaves the mortality branch untouched. |
| adult_uptake | 0.60 | Not changed for the mortality branch. The critique says a *separate* lung-only branch should use roughly 0.10–0.20 uptake instead of 0.60. That branch does not exist in the model. |
| Lung/morbidity benefit term | implicit 0 | This is the only target, and it is not a model parameter. |

Applied to the current CEA, the critique has **zero effect**. It only lowers the upside that a hypothetical lung-benefit add-on (Critiques 1–3) could contribute.

## Plausible Range (for the hypothetical lung-channel weight)

- **Naive weight:** 0.4 + 0.6 × P(lung holds | mortality fails) × 1.0.
  - With P = 0.3–0.5, this gives **0.58–0.70**.
- **Realistic weight:** 0.4 + 0.6 × P × (conditional adoption ÷ 0.60).
  - With adoption of 0.10–0.20 (ratio 1/6 to 1/3), this gives **0.43–0.50**.
  - My calculation implies an increment of +0.03 to +0.10. The critique states +0.02 to +0.06, and the two overlap at the low end.
- **Overstatement ratio** (naive ÷ realistic lung-channel weight): about **1.35–1.4×**. This is consistent with the critique's corrected "1.3–1.6×" figure, not "2×."

## Sensitivity Analysis

**Base case SROI:**
- 5.5M × 0.6 × 0.06 × 0.10 = 19,800 deaths averted per year.
- 19,800 × 27 × $100k = $OP 53.46B.
- $OP 53.46B ÷ $7M × 0.4 = **3,055x**.

**Effect on the current model:** none. SROI stays at 3,055x, so Δ = 0%.

**Illustrative effect if a lung add-on L were added** (L expressed as a fraction of the mortality benefit at p = 1):

| Lung add-on L | Naive SROI | Realistic SROI | Correction |
|---|---|---|---|
| 0.25 | 3,055 + 7,637 × 0.25 × (0.58–0.70) = **4,160–4,390x** | 3,055 + 7,637 × 0.25 × (0.43–0.50) = **3,880–4,010x** | −7% to −9% vs naive |
| 0.50 | about 5,270–5,730x | about 4,700–4,960x | about −11% to −13% vs naive |

The correction is a multiplicative discount on an additive term. It matters only to the extent that Critiques 1–3 add a lung channel.

## Code

```python
base = 5_500_000*0.6*0.06*0.10*1*27*100_000/7_000_000   # SROI at p=1 = 7637
sroi = base*0.4                                           # 3055
for P in (0.3, 0.5):
    for a in (0.10, 0.20):
        naive = 0.4 + 0.6*P
        real  = 0.4 + 0.6*P*(a/0.6)
        for L in (0.25, 0.5):
            print(P, a, L, round(sroi + base*L*naive), round(sroi + base*L*real),
                  round(naive/real, 2))
```

## Bottom-Line Impact

This critique has no effect on the current 3,055x SROI. It only trims a hypothetical lung-benefit add-on by about 25–35%, which reduces such an add-on's contribution to total SROI by single-digit to low-teens percent.

## Materiality Verdict

**NO.** The critique is a weighting caution for other critiques' upside and does not change any existing model parameter.

## Sensitivity Inputs

RANGE: none | The critique only re-weights a lung/morbidity benefit term that is not in the model ("only mortality is valued"); no existing parameter changes.

--- Critique: The sweat-based diagnostic carries real option value but is speculative (~10–30k central) ---

# CRITIQUE: The sweat-based diagnostic carries real option value but is speculative (~10–30k DALYs/yr central)

## Parameter Mapping

The critique proposes a benefit channel the model sets to zero ("only mortality is valued"). There is no diagnostic parameter, so the extra benefit has to be expressed through an existing parameter that scales SROI linearly. I use `relative_reduction`.

| Parameter | Model key | Current value | Role |
|---|---|---|---|
| Relative mortality reduction | `relative_reduction` | 0.10 | Vehicle for the translation: SROI = 30,549 × relative_reduction |
| Speedup credited | `speedup_years` | 1 | Diagnostic benefit gets the same 1-year acceleration credit |
| All-in cost | `all_in_cost` | $7,000,000 | Denominator. Whether it includes diagnostic costs is unresolved; not changed here |
| Probability of success | `p_success` | 0.40 | Not applied to the diagnostic term, because the critique's figure already includes P(adoption) of about 5% |

**Translation.** The added SROI is diagnostic DALYs/yr × 1 year × 100,000 ÷ 7,000,000. Because the model multiplies by p_success, the effective relative reduction is:

relative_reduction_eff = 0.10 + ΔSROI ÷ (5.5M × 0.6 × 0.06 × 27 × 100,000 × 0.4 ÷ 7M)
= 0.10 + ΔSROI ÷ 30,549

## Plausible Range

The critique's own expected value is 0.05 × 200k × 5 ≈ 50k DALYs/yr. After adjusting for adoption delay and displacement, it puts this at 10–30k, with an overall range of 0 to 100k. The evidence pulls in two directions:
- Tongue-swab PCR is WHO-recommended only for adults and adolescents, which leaves a paediatric and no-sputum gap.
- A sweat test needs its own evidence and policy pathway, which supports a low adoption probability.
- The tongue-swab and NPOC alternatives are improving fast, which pushes counterfactual displacement toward the low end.

| Scenario | Diagnostic DALYs/yr | ΔSROI | relative_reduction_eff |
|---|---|---|---|
| Low | 0 | 0 | 0.1000 |
| Central | 20k | +286x | 0.1094 |
| High (critique's central-band top) | 30k | +429x | 0.1140 |
| Extreme (critique's stated ceiling) | 100k | +1,429x | 0.1468 |

**Caveat on DALYs per case.** The critique assumes 5 DALYs per detected case (20% untreated CFR × 25). Untreated smear-positive TB CFR is often cited at around 40–70%, while treated mortality is about 6%. That would put the incremental value nearer 9–15 DALYs per case. This is a reason the critique could be low by about 2×. It is offset by the fact that P(adoption) = 5% is ungrounded.

## Sensitivity Analysis

```python
base = dict(eligible=5.5e6, decline=0.02, yta=8, uptake=0.6, mort=0.06, rr=0.10,
            dpd=27, opd=1e5, speed=1, cost=7e6, p=0.40)

def sroi(rr=0.10, extra_dalys=0, cost=7e6, **kw):
    b = dict(base, rr=rr, cost=cost, **kw)
    elig = b['eligible'] * (1 - b['decline'])**(b['yta'] - 8)
    deaths = elig * b['uptake'] * b['mort'] * b['rr']
    statin = deaths * b['speed'] * b['dpd'] * b['opd'] / b['cost'] * b['p']
    diag = extra_dalys * b['speed'] * b['opd'] / b['cost']   # P(adoption) already inside
    return statin + diag

S0 = sroi()                                   # 3054.9
k = S0 / 0.10                                 # 30,549 per unit rr
for d in [0, 10e3, 20e3, 30e3, 50e3, 100e3]:
    s = sroi(extra_dalys=d)
    print(d, round(s, 1), f"{(s/S0 - 1)*100:.1f}%", round(0.10 + (s - S0)/k, 4))
```

**Results** (base SROI 3,055x):

| Diagnostic DALYs/yr | SROI | Change |
|---|---|---|
| 10k | 3,198x | +4.7% |
| 20k (central) | 3,341x | +9.4% |
| 30k | 3,484x | +14.0% |
| 50k (critique's undiscounted figure) | 3,769x | +23.4% |
| 100k (ceiling) | 4,484x | +46.8% |

**Pessimistic direction.** The critique adds no downside. SROI falls only if diagnostic workstream costs turn out to sit outside the $7M and are then added to the denominator. For example, an extra $1M would give 2,673x (−12.5%). That is a cost-attribution question for the model, not something this critique supports, so it is excluded from the ranges.

**Interactions.** The diagnostic term adds to the statin term; it does not multiply it. It is independent of p_success and relative_reduction. It scales with speedup_years and inversely with all_in_cost, like the main term. Changes to those parameters made under other threads would therefore scale this term proportionally.

## Bottom-Line Impact

Crediting the sweat diagnostic raises SROI by about 0% to +14% (central +9%, from 3,055x to about 3,340x). The critique's ceiling implies up to +47%, but all of this rests on an ungrounded 5% adoption probability.

## Materiality Verdict

**BORDERLINE.** The central estimate is close to a typical ~10% threshold. The direction is favourable only, and it cannot change the funding decision, since the base is already 1.5× the 2,000x bar.

## Sensitivity Inputs

RANGE: relative_reduction | current 0.10 | low 0.10 | central 0.1094 | high 0.1140

--- Critique: 60% steady-state uptake has no precedent among comparable TB program additions ---

# CRITIQUE: 60% steady-state uptake has no precedent among comparable TB program additions

## Parameter mapping

| Parameter | Model key | Current value | Role in formula |
|---|---|---|---|
| Steady-state uptake ceiling | `adult_uptake` | 0.60 | `treated = eligible × adult_uptake`. SROI is strictly proportional to it. |
| Timing of adoption (ramp proxy) | `years_to_adoption` | 8 | `eligible = 5.5M × 0.98^(years_to_adoption − 8)`. A slower ramp pushes effective adoption later into a smaller incidence base. |
| `speedup_years` | `speedup_years` | 1 | Not changed. With no discounting and an infinite horizon, a one-year shift of any ramp gains about ceiling × one year of cases, so ramp shape enters only through the ceiling and incidence decline. |

**Simplification.** The model has no ramp or discounting term. I represent the ramp only by shifting `years_to_adoption`, which captures the incidence-decline effect. Discounting belongs to Thread 3 and is not double-counted here.

## Plausible ranges

**`adult_uptake`: current 0.60, plausible range 0.35–0.70, central 0.50**
- **Low (0.35).** Reflects several downward pressures:
  - HPMZ shows tolerability and supply friction: only 14% of eligible patients were prescribed it, and 64% of starters discontinued.
  - The private-sector treatment share is not covered by the model.
  - Adherence and effective dose for a daily adjunct are not modeled.
  - I do not use "stall below 50%" as support, per the Verifier.
- **Central (0.50).** WRD coverage is about 54% after roughly 10+ years and still rising. A cheap generic oral adjunct is easier to deploy than capital-intensive Xpert, but it is not adherence-free. I shade this slightly below the WRD level because "uptake among all adult patients" may be a stricter construct than "% of notified cases tested."
- **High (0.70).** The 2023 UN high-level meeting set a 100% WRD target by 2027, and a generic drug faces no supply constraint, so sustained push above 60% is feasible.

**`years_to_adoption`: current 8, plausible range 8–14, central 10**
- Evidence that new TB tools take about 10 or more years to reach about 50% coverage implies the effective centre of mass of adoption lands later than the Phase III end date.

## Sensitivity analysis

Base SROI = **3,055x**. The bar is 2,000x. The break-even `adult_uptake` is 0.393, with everything else at base.

| Scenario | SROI | Δ vs base |
|---|---|---|
| uptake = 0.35 | 1,782x | −41.7% (below bar) |
| uptake = 0.50 | 2,546x | −16.7% |
| uptake = 0.70 | 3,564x | +16.7% |
| years_to_adoption = 10 | 2,934x | −4.0% |
| years_to_adoption = 14 | 2,706x | −11.4% |
| Joint central (0.50, 10y) | 2,445x | −20.0% |
| Joint pessimistic (0.35, 14y) | 1,579x | −48.3% |
| Joint optimistic (0.70, 8y) | 3,564x | +16.7% |

The two effects are multiplicative, since both scale `treated` linearly. The ceiling dominates the timing effect by roughly 4:1 across the plausible ranges. This confirms the mechanism: ramp timing matters mainly through discounting, which this model omits.

## Bottom-line impact

This critique plausibly changes SROI by **−48% to +17%, with a central estimate of about −17% to −20%** (≈2,450–2,550x). That stays above the 2,000x bar unless steady-state uptake falls below about 0.39.

## Materiality verdict

**BORDERLINE.**
- The central case stays above the bar.
- The pessimistic end of the ceiling range (≤0.39) crosses it.
- The evidence for a ceiling that low is weak: the concern is UNGROUNDED, and the WRD data point to 54% and rising.

## Code

```python
def sroi(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=1e5, speedup_years=1,
         all_in_cost=7e6, p_success=0.40):
    elig = eligible_people_at_8y * (1 - decline_per_year) ** (years_to_adoption - 8)
    deaths = elig * adult_uptake * baseline_mortality * relative_reduction
    benefit = deaths * speedup_years * dalys_per_death * op_per_daly
    return benefit / all_in_cost * p_success

base = sroi()
print("base", round(base))
for u in [0.35, 0.39, 0.50, 0.70]:
    print("uptake", u, round(sroi(adult_uptake=u)), f"{sroi(adult_uptake=u)/base-1:+.1%}")
for y in [10, 14]:
    print("yrs", y, round(sroi(years_to_adoption=y)), f"{sroi(years_to_adoption=y)/base-1:+.1%}")
for u, y in [(0.50, 10), (0.35, 14), (0.70, 8)]:
    v = sroi(adult_uptake=u, years_to_adoption=y)
    print("joint", u, y, round(v), f"{v/base-1:+.1%}")
print("breakeven uptake", 0.60 * 2000 / base)
```

## SENSITIVITY INPUTS

RANGE: adult_uptake | current 0.60 | low 0.35 | central 0.50 | high 0.70
RANGE: years_to_adoption | current 8 | low 8 | central 10 | high 14

--- Critique: A Phase III cannot be powered on mortality, so the WHO GDG would be recommending on surrogate or composite endpoints ---

# TB statins BOTEC: impact of a mortality-underpowered Phase III (surrogate or composite endpoints) on cost-effectiveness

**Bottom line:** This critique could reduce SROI by about 0–27%, with a central estimate of about 9% (3,055x → about 2,770x). Even the pessimistic case (about 2,220x) stays above the 2,000x bar.

## Parameter mapping

| Parameter | Current value | How the critique affects it |
|---|---|---|
| `adult_uptake` (primary) | 0.60 | A conditional or subgroup-limited WHO recommendation, after an indirectness downgrade, lowers effective uptake. |
| `years_to_adoption` (secondary) | 8 | The GDG may ask for more evidence before recommending. In this model, delay only acts through the 2%/yr incidence decline, because there is no discounting and `speedup_years` stays at 1. |
| `relative_reduction` | 0.10 | Not changed, for two reasons. First, the critique raises the variance of the realized effect, not its mean, and SROI is linear in `relative_reduction`, so the expected value is unchanged. Second, any "surrogate success without mortality benefit" adjustment belongs to Thread 1 (`relative_reduction` / `p_success`). Adding it here would double-count. |

## Plausible ranges

The evidence cuts both ways:

- **Against the critique:** WHO TB GDGs routinely treat unfavourable-outcome composites that include death as critical, direct outcomes. This makes a full indirectness downgrade unlikely.
- **For the critique:** The only RCT so far (StAT-TB, Phase 2b) uses culture conversion and lung function as primary endpoints, with mortality measured only as a tolerability outcome. The observational mortality signal is confined to TB patients with ASCVD, a narrow subgroup. The uptake and timing effects themselves are ungrounded.

I modelled the outcome as a mixture of recommendation scenarios:

| Scenario | Uptake | Probability (central) | Probability (pessimistic) |
|---|---|---|---|
| Strong recommendation, composite accepted as direct | 0.60 | 75% | 50% |
| Conditional recommendation, lower uptake | about 0.35–0.40 | 25% | 30% |
| Subgroup-limited recommendation (about 1/3 of patients) | about 0.20 | 0% | 20% |

Resulting ranges:

- **`adult_uptake`:** low 0.45, central 0.55, high 0.60.
  - Central: 0.75 × 0.6 + 0.25 × 0.4 = 0.55.
  - Pessimistic: 0.5 × 0.6 + 0.3 × 0.35 + 0.2 × 0.2 ≈ 0.445.
  - I found no mechanism by which this critique raises uptake above 0.60.
- **`years_to_adoption`:** low 8, central 8.5, high 9.5.
  - The central value assumes about a 25% chance of a roughly 2-year evidence delay.
  - The high value assumes a roughly 1.5-year expected delay.

## Sensitivity analysis

Base case: 19,800 deaths averted per year, SROI 3,055x.

| Scenario | SROI | Δ |
|---|---|---|
| Uptake 0.55 | 2,800x | −8.3% |
| Uptake 0.45 | 2,291x | −25.0% |
| Years to adoption 8.5 | 3,024x | −1.0% |
| Years to adoption 9.5 | 2,964x | −3.0% |
| **Joint central** (0.55, 8.5) | **2,772x** | **−9.3%** |
| **Joint pessimistic** (0.45, 9.5) | **2,223x** | **−27.2%** |
| Optimistic (0.60, 8) | 3,055x | 0% |

The effects combine multiplicatively, because both parameters enter the formula as multiplicative factors. They are close to additive at these magnitudes.

On variance: raising the spread of `relative_reduction` around 0.10 leaves expected SROI unchanged. It only widens the outcome distribution.

## Materiality verdict

**BORDERLINE.** The central estimate (about −9%) is modest. The pessimistic case (−27%) is material but does not push SROI below 2,000x. Because the uptake mechanism is ungrounded and the WHO TB precedent of accepting composites cuts against it, the central estimate deserves more weight than the tail.

## Code

```python
def sroi(elig=5.5e6, yta=8, dec=0.02, up=0.60, bm=0.06, rr=0.10,
         dpd=27, opd=1e5, sp=1, cost=7e6, p=0.40):
    e = elig * (1 - dec) ** (yta - 8)
    deaths = e * up * bm * rr
    return deaths * sp * dpd * opd / cost * p

base = sroi()  # 3054.86
for label, kw in [("up .55", dict(up=.55)), ("up .45", dict(up=.45)),
                  ("yta 8.5", dict(yta=8.5)), ("yta 9.5", dict(yta=9.5)),
                  ("joint central", dict(up=.55, yta=8.5)),
                  ("joint pess", dict(up=.45, yta=9.5))]:
    v = sroi(**kw)
    print(label, round(v), f"{(v / base - 1) * 100:.1f}%")
```

## Sensitivity inputs

RANGE: adult_uptake | current 0.60 | low 0.45 | central 0.55 | high 0.60
RANGE: years_to_adoption | current 8 | low 9.5 | central 8.5 | high 8

--- Critique: Clinical eligibility and monitoring barriers cap the achievable prescribing share below the "generic and cheap" logic ---

# Quantitative impact of eligibility and monitoring barriers on `adult_uptake` (TB statins BOTEC)

**Critique:** Clinical eligibility and monitoring barriers cap the achievable prescribing share below what the "generic and cheap" logic implies.

## Parameter mapping

- **Primary: `adult_uptake`.** It sits in the formula chain as `treated = eligible × adult_uptake`. The current value is 0.60.
- **Not mapped: LFT monitoring and adverse-event management costs.** These are delivery costs borne by health systems. They are not in `all_in_cost` ($7M covers R&D, Phase III and guideline change), and the model has no delivery-cost term. I note this but do not quantify it.
- **Not mapped: the drug-interaction argument.** The trial statin is pravastatin, which is not substantially CYP3A4-metabolised. So the CYP3A4 and PI-boosted ART interaction argument largely falls away. The CEA text says "atorvastatin", and that mismatch should be resolved. It does not change `adult_uptake` once pravastatin is assumed.

## Plausible range for `adult_uptake`

| Scenario | Value | Basis |
|---|---|---|
| Current | 0.60 | CG assumption ("generic and cheap") |
| High | 0.57 | CG's 60% may already embed some ineligibility. Pravastatin removes most interaction exclusions, leaving only about 5% residual exclusion (decompensated liver disease, pregnancy). |
| Central | 0.51 | About 15% net exclusion, the midpoint of the critique's 10–20%. Exclusions cover liver disease, DILI-attribution reluctance and pregnancy. |
| Low | 0.42 | 20% exclusion plus a further ~12% program-reluctance and discontinuation factor where LFT monitoring is mandated but unavailable. |

The critique's 0.45–0.50 figure is flagged as **UNGROUNDED**: it is the critique's own illustrative arithmetic. The evidence supports the direction (DILI is common, about 11.5% pooled, and monitoring is "imperative"), not the magnitude. The range is therefore wide.

## Sensitivity analysis

The model is linear in `adult_uptake`, so SROI = 3,055 × (uptake / 0.60).

| `adult_uptake` | Deaths averted per year | SROI | Δ vs base |
|---|---|---|---|
| 0.60 (base) | 19,800 | 3,055x | — |
| 0.57 | 18,810 | 2,902x | −5% |
| 0.51 | 16,830 | 2,597x | −15% |
| 0.50 | 16,500 | 2,546x | −17% |
| 0.45 | 14,850 | 2,291x | −25% |
| 0.42 | 13,860 | 2,139x | −30% |

- **Break-even against the 2,000x bar:** `adult_uptake` would have to fall to about 0.393. None of the plausible values reach that.
- **Optimistic direction:** there is no evidence that uptake would exceed 0.60. The critique runs one way only, and the high case at 0.57 is essentially no change.
- **Interactions are multiplicative** with `relative_reduction`, `p_success`, `baseline_mortality` and the other critiques, because every term multiplies.
  - With central uptake of 0.51 and `relative_reduction` = 0.08, SROI is about 2,077x, near the bar.
  - With uptake of 0.42 and `relative_reduction` = 0.08, SROI is about 1,711x, below the bar.
- **Monitoring costs:** if LFT monitoring costs were attributed to the denominator, SROI would fall further. The current model structure cannot express this.

## Bottom-line impact

This critique reduces SROI by about 5–30%, with a central estimate of about 15% (3,055x → about 2,600x). On its own it does not push SROI below the 2,000x bar.

## Materiality verdict

**BORDERLINE.** The effect is above 10% in the central case, but it does not flip the funding decision by itself. Combined with Thread 1 reductions to `relative_reduction`, it could push SROI below the bar.

## Code

```python
base = dict(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=1e5, speedup_years=1,
            all_in_cost=7e6, p_success=0.40)

def sroi(p):
    elig = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    deaths = elig * p['adult_uptake'] * p['baseline_mortality'] * p['relative_reduction']
    benefit = deaths * p['speedup_years'] * p['dalys_per_death'] * p['op_per_daly']
    return deaths, benefit / p['all_in_cost'] * p['p_success']

b = sroi(base)[1]
for u in [0.60, 0.57, 0.51, 0.50, 0.45, 0.42]:
    d, s = sroi({**base, 'adult_uptake': u})
    print(u, round(d), round(s), f"{(s/b - 1)*100:.0f}%")

print("break-even uptake:", 0.60 * 2000 / b)

for u, rr in [(0.51, 0.08), (0.42, 0.08)]:
    print(u, rr, round(sroi({**base, 'adult_uptake': u, 'relative_reduction': rr})[1]))
```

## Sensitivity inputs

RANGE: adult_uptake | current 0.60 | low 0.42 | central 0.51 | high 0.57

--- Critique: Private-sector treatment share and the reach of national guidelines are not modeled ---

# Impact assessment: private-sector treatment share and guideline reach

**CRITIQUE:** Private-sector treatment share and the reach of national guidelines are not modeled.

## Parameter mapping

| Parameter | Location in model | Current value | Role |
|---|---|---|---|
| `adult_uptake` | Formula chain: treated = eligible × adult_uptake | 0.60 | Primary. The critique says the single uptake figure does not reflect private-sector reach or the effective dose delivered there. |
| `speedup_years` | benefit = deaths/yr × speedup_years × … | 1 | Secondary and qualitative. If private providers adopt atorvastatin before guidelines change, the grant's counterfactual acceleration shrinks. This is speculative, so I only test it qualitatively below. |
| `relative_reduction` | — | 0.10 | Not changed here. Non-standard private dosing lowers the realized benefit per treated patient. I fold that into an *effective* `adult_uptake` so it is not double-counted with Thread 1. |

SROI is linear in `adult_uptake`, so any percentage change in effective uptake passes one-for-one into SROI.

## Plausible range

My derivation is inference, consistent with the Verifier's "ungrounded" flag:

**Private share of the modeled base**
- The private sector handles about one-third of notified cases in India.
- India accounts for about 27% of global TB.
- Indonesia, Pakistan, the Philippines and Nigeria also have large private sectors.
- That puts private care at roughly 15–20% of the globally notified, treated drug-susceptible cohort.
- `eligible_people_at_8y` is built on treated/notified patients. Un-notified private care is therefore already outside the base, which limits the size of this effect.

**Pessimistic case**
- Assume private-sector patients get roughly 0.25–0.5 of full benefit, from unsupervised dosing and duration plus slower uptake where notification and drug linkage are weak.
- Effective benefit falls by about 15–20% × 0.5–0.75, which is about 8–15%.

**Optimistic case**
- Private providers adopt cheap generics fast, and PPSA linkage to free NTP drugs is expanding.
- Private uptake could exceed 60% with adequate dosing, giving about +5%.

**Effective `adult_uptake` range**

| Case | Effective uptake | Change |
|---|---|---|
| Low | 0.51 | −15% |
| Central | 0.57 | −5% |
| High | 0.63 | +5% |

## Sensitivity analysis

Base case: 19,800 deaths averted per year, SROI = **3,055x**. The funding bar is 2,000x.

| Scenario | `adult_uptake` | Deaths/yr | SROI | Δ |
|---|---|---|---|---|
| Base | 0.60 | 19,800 | 3,055x | — |
| Low (pessimistic) | 0.51 | 16,830 | 2,597x | −15% |
| Central | 0.57 | 18,810 | 2,902x | −5% |
| High (optimistic) | 0.63 | 20,790 | 3,208x | +5% |
| Stress test (private reach ≈ zero benefit, 25% share) | 0.45 | 14,850 | 2,291x | −25% |
| Break-even vs 2,000x bar | 0.393 | — | 2,000x | −34.5% |

**Speedup channel (qualitative only).** Suppose private pre-guideline adoption cut credited acceleration from 1 year to 0.9 years. Combined with low uptake, SROI would be about 2,337x (−23.5%). The effects are multiplicative.

**Interaction with other threads.** All terms in the chain are multiplicative, so this adjustment compounds with others. For example, if Thread 1 halved `relative_reduction` to 0.05, base SROI would be 1,527x. The low-uptake case would then give 1,298x, taking the estimate further below the bar.

## Bottom-line impact

This critique plausibly changes cost-effectiveness by **−15% to +5%**, with a central estimate of about −5% (SROI 2,597x to 3,208x, versus 3,055x). The sign is genuinely uncertain.

## Materiality verdict

**NO** on its own, and borderline only at the pessimistic end.
- No plausible value pushes SROI below the 2,000x bar. That would need effective uptake of 0.39, a 35% reduction.
- The pessimistic end (−15%) exceeds a ~10% materiality convention, so the critique matters mainly in combination with the Thread 1 and Thread 3 adjustments.

## Code

```python
base = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
            all_in_cost=7_000_000, p_success=0.40)

def sroi(p):
    elig = p['eligible_people_at_8y']*(1-p['decline_per_year'])**(p['years_to_adoption']-8)
    deaths = elig*p['adult_uptake']*p['baseline_mortality']*p['relative_reduction']
    benefit = deaths*p['speedup_years']*p['dalys_per_death']*p['op_per_daly']
    return deaths, benefit/p['all_in_cost']*p['p_success']

b = sroi(base)[1]
for u in [0.60, 0.51, 0.57, 0.63, 0.45]:
    d, s = sroi({**base, 'adult_uptake': u})
    print(u, round(d), round(s), f"{s/b-1:+.1%}")

print("break-even uptake:", 0.60*2000/b)
print("low uptake + 0.9yr speedup:", sroi({**base, 'adult_uptake': 0.51, 'speedup_years': 0.9})[1])
print("low uptake + rr=0.05:", sroi({**base, 'adult_uptake': 0.51, 'relative_reduction': 0.05})[1])
```

## Sensitivity inputs

RANGE: adult_uptake | current 0.60 | low 0.51 | central 0.57 | high 0.63

--- Critique: Zero modeled lag between Phase III completion and adoption, and a speedup that assumes trial timing is the binding constraint ---

# CRITIQUE: Zero modeled lag between Phase III completion and adoption, and a speedup that assumes trial timing is the binding constraint

## Parameter mapping

The critique touches two model parameters.

| Parameter | Role in formula | Current value |
|---|---|---|
| `years_to_adoption` | Exponent in `eligible = 5.5M × (1 − decline)^(years_to_adoption − 8)` | 8 (meaning zero lag after Phase III) |
| `speedup_years` | Linear multiplier on benefit | 1.0 |

Two other inputs matter but are not changed here:
- **Discount rate.** It is implicitly 0 and is not a model parameter. Its effect is noted qualitatively below and belongs to Thread 3.
- **`decline_per_year` (0.02).** It sets how much the lag costs, and it is held at its current value.

## Plausible range

**`years_to_adoption`: current 8. Range 8 to 13. Central 10.**
- HPMZ shows the WHO step can take weeks after publication in 2021, with consolidated guidelines in 2022. So the WHO step alone adds only about 0–1 year.
- National adoption and procurement plausibly add a further 1–4 years. Xpert is a qualitative analogy only; I found no HPMZ country-uptake data.
- I set the central case at 2 years of total post-Phase III lag. The pessimistic case is 5 years.

**`speedup_years`: current 1.0. Range 0.5 to 1.25. Central 0.9.**
- The claim that speedup is below 1 because the trial is not on the critical path is **UNGROUNDED**. No evidence identifies a different binding constraint.
- The critique itself concedes that lumpy decision cycles do not lower the *expected* speedup.
- I therefore apply only a modest central haircut (0.9). I treat 0.5 as a stress value, not an evidence-based estimate.
- The optimistic value of 1.25 is included because Phase III might not happen without the funding. In that case the speedup could exceed 1. That is also ungrounded.

## Sensitivity analysis

Base SROI = 5,500,000 × 0.6 × 0.06 × 0.10 × 1 × 27 × 100,000 / 7,000,000 × 0.4 = **3,055x**. The funding bar is 2,000x.

| Scenario | SROI | Δ vs. base |
|---|---|---|
| years_to_adoption = 10 (2-yr lag) | 2,934x | −4.0% |
| years_to_adoption = 11 (3-yr lag) | 2,875x | −5.9% |
| years_to_adoption = 12 (4-yr lag) | 2,818x | −7.8% |
| years_to_adoption = 13 (5-yr lag) | 2,761x | −9.6% |
| speedup_years = 0.5 | 1,527x | −50% |
| speedup_years = 0.9 | 2,749x | −10% |
| speedup_years = 1.25 | 3,819x | +25% |
| Joint central (10 yrs, 0.9) | 2,640x | −13.6% |
| Joint pessimistic (13 yrs, 0.5) | 1,381x | −54.8% (below bar) |
| Joint optimistic (8 yrs, 1.25) | 3,819x | +25% |

**How the effects combine.** Both parameters enter the formula as multipliers, so their effects multiply: 0.9604 × 0.9 = 0.864.

**Discounting caveat.** The model applies no discounting, so lag works only through the 2%/yr incidence decline. A 4% discount rate over 5 extra years would add roughly another −18%. That belongs to Thread 3 and cannot be expressed through these parameters.

## Bottom-line impact

- **Grounded component (adoption lag):** reduces SROI by 4–10%, central about 4–6%.
- **Including the ungrounded speedup haircut:** about −14% central, with a range of −55% to +25%.

## Materiality verdict

**BORDERLINE.**
- The evidenced lag component alone is not material. It leaves SROI at 2,760x or higher, well above 2,000x.
- Only the ungrounded speedup ≤0.65 scenario pushes SROI below the bar. Without discounting, speedup must fall below about 0.65 to cross it, and below about 0.72 at a 5-year lag.

## Code

```python
def sroi(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.6, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=1e5, speedup_years=1.0,
         all_in_cost=7e6, p_success=0.4):
    elig = eligible_people_at_8y*(1-decline_per_year)**(years_to_adoption-8)
    deaths = elig*adult_uptake*baseline_mortality*relative_reduction
    benefit = deaths*speedup_years*dalys_per_death*op_per_daly
    return benefit/all_in_cost*p_success

base = sroi()
for kw in [dict(years_to_adoption=y) for y in (10,11,12,13)] + \
          [dict(speedup_years=s) for s in (0.5,0.9,1.25)] + \
          [dict(years_to_adoption=10,speedup_years=0.9),
           dict(years_to_adoption=13,speedup_years=0.5),
           dict(years_to_adoption=8,speedup_years=1.25)]:
    v = sroi(**kw); print(kw, round(v), f"{v/base-1:+.1%}")
# breakeven speedup at 2000x: 2000/base ≈ 0.655
```

## Sensitivity inputs

RANGE: years_to_adoption | current 8 | low 13 | central 10 | high 8
RANGE: speedup_years | current 1 | low 0.5 | central 0.9 | high 1.25

--- Critique: Survivors' excess mortality and comorbidity shrink the 27 DALYs per death ---

# Survivors' excess mortality and the 27 DALYs per death: impact on the TB statins SROI

## Parameter mapping

- **dalys_per_death** (primary): current value 27, described as "remaining healthy life expectancy."
- **No other parameter is touched.** The model is a pure product chain, so SROI is exactly proportional to dalys_per_death:

  SROI = eligible × uptake × baseline_mortality × relative_reduction × speedup × dalys_per_death × op_per_daly × p_success / all_in_cost

  A given % change in dalys_per_death produces the same % change in SROI.
- **Post-TB morbidity and mortality DALYs** are an implicit-zero benefit term in this model. The verifier's evidence that 5.8 of 12.1 lifetime DALYs per case come from post-TB sequelae does not create an offset here. That would only happen if 27 itself had been built from a TB-survivor life table, which is undocumented.

## Plausible range

I modelled survivors' life expectancy with a Gompertz hazard μ(x) = a·e^{bx}, using b = 0.09. I calibrated it so that remaining life expectancy at age 40 is about 33 years, which is typical of LMIC life tables. Survivors' hazard is the population hazard multiplied by a factor k (the standardized mortality ratio, SMR).

**Life expectancy at age 40 if the SMR applies for the rest of life:**

| k (SMR) | Source | e(40) | Δ vs general population |
|---|---|---|---|
| 1.00 | General population | ~33.0 | — |
| 1.77 | 2026 cohort | ~27.4 | −17% |
| 2.21 | Romanowski lower CI | ~25.4 | −23% |
| 2.91 | Romanowski point estimate | ~23.0 | −30% |

A lifetime-constant SMR overstates the loss. Post-TB excess mortality is concentrated in the first years after treatment and attenuates with time and age. I therefore scaled the effective lifetime loss to roughly 50–70% of the constant-SMR figure:

- k ≈ 1.8 gives about −9% to −12%.
- k ≈ 2.9 gives about −15% to −21%.

A further offset is possible if 27 already reflects the age-at-death distribution or a TB-specific HALE. Its provenance is ungrounded, so the high end allows no change.

**dalys_per_death range:**

| Case | Value | Δ | Basis |
|---|---|---|---|
| Current | 27 | — | Model |
| Pessimistic | 20 | −26% | Romanowski point estimate, mostly persistent |
| Central | 24 | −11% | k ≈ 1.8–2.2, attenuating |
| Optimistic | 27 | 0% | 27 already survivor-adjusted |

## Sensitivity analysis

**Base case:** 534,600 DALYs, SROI 3,055x. The funding bar is 2,000x.

| dalys_per_death | DALYs credited | SROI | Δ |
|---|---|---|---|
| 27 (optimistic / current) | 534,600 | 3,055x | 0% |
| 24 (central) | 475,200 | 2,716x | −11% |
| 23 (k = 1.77, constant SMR) | 455,400 | 2,602x | −15% |
| 20 (pessimistic) | 396,000 | 2,263x | −26% |
| 17.7 (break-even) | 350,000 | 2,000x | −34.5% |

- **Reaching the bar:** dalys_per_death would have to fall by 34.5%. That exceeds even the constant, lifelong SMR = 2.91 case (−30%).
- **Interactions are multiplicative.** At the central value of 24, any other critique that independently cuts SROI by more than 26% (factor below 0.736) pushes the estimate below 2,000x. Examples would be relative_reduction falling from 0.10 to 0.07, or p_success falling from 0.40 to 0.29.
- **Optimistic direction:** this critique cannot raise SROI unless post-TB DALYs are added as a new benefit term. That is outside this parameter.

## Bottom-line impact

This critique reduces cost-effectiveness by 0–26%, with a central estimate of about 11% (SROI 3,055x → about 2,716x). It does not by itself push the grant below the 2,000x bar.

## Materiality verdict

**BORDERLINE.** The impact is material in size (central −11%, up to −26%). It does not cross the bar alone, but it substantially narrows the margin for other downward critiques. Because the provenance of 27 is unknown, the true effect could be zero.

## Code

```python
import numpy as np
from scipy.special import exp1

base = dict(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=1e5, speedup_years=1,
            all_in_cost=7e6, p_success=0.40)

def sroi(p):
    elig = p['eligible_people_at_8y']*(1-p['decline_per_year'])**(p['years_to_adoption']-8)
    deaths = elig*p['adult_uptake']*p['baseline_mortality']*p['relative_reduction']
    return deaths*p['speedup_years']*p['dalys_per_death']*p['op_per_daly']/p['all_in_cost']*p['p_success']

b0 = sroi(base)
print(f"base {b0:.0f}x; breakeven dalys = {27*2000/b0:.2f}")
for d in [27, 24, 23, 20, 17.7]:
    s = sroi({**base, 'dalys_per_death': d})
    print(d, round(s), f"{s/b0-1:+.1%}")

# Gompertz remaining life expectancy: e(x) = (1/b) e^M E1(M), with M = mu(x)/b
b = 0.09
M0 = 0.0324                      # calibrated so e(40) ~ 33
e = lambda M: np.exp(M)*exp1(M)/b
for k in [1, 1.77, 2.21, 2.91]:
    print(k, round(e(k*M0), 1), f"{e(k*M0)/e(M0)-1:+.0%}")
```

## Sensitivity inputs

RANGE: dalys_per_death | current 27 | low 20 | central 24 | high 27

--- Critique: The 6% is a mix of deaths, and only a fraction is reachable and modifiable by atorvastatin ---

# CRITIQUE: The 6% is a mix of deaths, and only a fraction is reachable and modifiable by atorvastatin

## Parameter mapping

The critique splits the 6% into deaths a statin could plausibly affect and deaths it could not. In the formula chain this works as a multiplier, the addressable share, applied to `baseline_mortality`.

- **baseline_mortality:** current value 0.06. This is the primary mapping.
- **relative_reduction:** current value 0.10. It sits in the same product, so a haircut on either parameter has the same effect on SROI. The rifampicin–atorvastatin exposure point is a dose-response issue that belongs to `relative_reduction` (Thread 1). I have left it out here to avoid double-counting.
- I apply the whole addressable-share haircut through `baseline_mortality` only.

The model is linear in this term: SROI ∝ baseline_mortality × relative_reduction. The haircut is therefore purely multiplicative and does not interact with other parameters.

## Plausible range

**Effective addressable share of the 6%:** low 0.50, central 0.75, high 1.00.

Basis:
- **Timing.** 55–75% of on-treatment deaths occur within 1–2 months, with a median of about 3 weeks in Zambia. If statins need several weeks to act, a large fraction of deaths is hard to reach. Two things pull the other way:
  - Statin time-to-effect is unknown, and pleiotropic or anti-inflammatory effects may be fast.
  - The verifier notes that early deaths may be partly reversible, so not all early deaths are unreachable.
- **Cause.** A non-TB-attributable share of perhaps 10–20% applies, concentrated in HIV-positive patients.
- **Double-counting caveat.** The 10% relative reduction is a stated assumption, not derived from a trial population. So the risk that it already excludes early or ineligible deaths is real but modest. I set the high end at no haircut (1.0) to reflect full double-counting or full reachability.
- **Resulting range for baseline_mortality:**
  - Low: 0.06 × 0.50 = 0.030
  - Central: 0.06 × 0.75 = 0.045
  - High: 0.06 × 1.0 = 0.060
- **Optimistic direction.** Unascertained deaths could push true mortality above 6%, perhaps to about 7%. That is a separate critique, so I note it but do not include it in this range.

## Sensitivity analysis

| baseline_mortality (effective) | Addressable share | SROI | Δ vs base |
|---|---|---|---|
| 0.060 (base) | 1.00 | 3,055x | 0% |
| 0.045 (central) | 0.75 | 2,291x | −25% |
| 0.036 (critique's illustration) | 0.60 | 1,833x | −40% |
| 0.030 (low) | 0.50 | 1,527x | −50% |
| 0.070 (optimistic, under-ascertainment; not this critique) | — | 3,564x | +17% |

**Break-even against the 2,000x bar:**
- The bar is crossed at baseline_mortality of 0.0393, which means an addressable share of 0.655.
- Equivalently, the estimate falls below the bar if the haircut exceeds about 34.5%.

**Absolute terms:**
- Deaths averted per year fall from 19,800 to 14,850 at the central value, and to 9,900 at the low value.
- DALYs credited fall from 534,600 to 400,950 (central) and 267,300 (low).

**Joint effects:** only one parameter is affected here. If Thread 1 separately cuts `relative_reduction`, the two effects multiply.

## Bottom-line impact

This critique could reduce SROI by 0% to 50%, with a central estimate of about 25% (3,055x to about 2,290x). It pushes the estimate below the 2,000x bar if more than about 35% of on-treatment deaths are unaddressable.

## Materiality verdict

**BORDERLINE (leaning YES).**
- The central estimate stays just above the bar, at 2,291x.
- The critique's own illustration (1,833x) and the low end of the range (1,527x) fall below it.
- The size of the haircut is ungrounded, so the verdict hinges on statin time-to-effect and the TB-attributable share of deaths.

## Code

```python
def sroi(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=1e5, speedup_years=1,
         all_in_cost=7e6, p_success=0.40):
    eligible = eligible_people_at_8y * (1 - decline_per_year) ** (years_to_adoption - 8)
    treated = eligible * adult_uptake
    deaths = treated * baseline_mortality * relative_reduction
    benefit = deaths * speedup_years * dalys_per_death * op_per_daly
    return benefit / all_in_cost * p_success, deaths

base, _ = sroi()
for share in [1.0, 0.75, 0.60, 0.50]:
    s, d = sroi(baseline_mortality=0.06 * share)
    print(share, round(0.06 * share, 4), round(s), round(d), f"{(s / base - 1) * 100:.1f}%")

# break-even baseline mortality for the 2,000x bar
print("break-even baseline_mortality:", 0.06 * 2000 / base)  # ~0.0393 -> share ~0.655
```

## Sensitivity inputs

RANGE: baseline_mortality | current 0.06 | low 0.030 | central 0.045 | high 0.06

--- Critique: Under-ascertained deaths push true mortality up, and the direction is the opposite of Critiques 1–2 ---

# CRITIQUE: Under-ascertained deaths push true mortality up (opposite direction to Critiques 1–2)

## Parameter Mapping

- **baseline_mortality**: the only model parameter this affects. Current value is 0.06 (mortality among treated drug-susceptible patients).
- The critique does not touch relative_reduction, dalys_per_death or any other input. The addressability caveat (a statin may not avert deaths after treatment interruption) is handled by shrinking the *effective* increment to baseline_mortality. That is equivalent to saying only on-treatment-addressable deaths count.

**Model structure:** SROI = eligible × uptake × baseline_mortality × RR × speedup × DALYs × $OP/DALY / cost × p_success. SROI is strictly linear in baseline_mortality, so %ΔSROI = %Δbaseline_mortality.

## Plausible Range

The critic's illustrative arithmetic adds +0.6 to +1.4 pp, giving 0.066–0.074. The verified evidence trims this in three ways:

1. **"Not evaluated" patients.** This group is mostly transfers and missing records, and most are likely alive. A 10–20% death rate is unsupported here, so most of this group's contribution drops out.
2. **LTFU patients.** LTFU alone is roughly 3–5% of the cohort. At 10–20% mortality, that adds about 0.3–1.0 pp of raw deaths.
3. **Addressability.** Many LTFU deaths occur after the regimen (and the statin) stops. Of the extra deaths, I assume roughly 0–50% are statin-addressable, with a central value of about 25–40%.
4. **High-mortality settings.** Rates such as South Africa's 8.6% are already inside the ~6% global average. They show heterogeneity, not a reason to raise the global mean.

Resulting effective range for baseline_mortality:

| Case | Value | Basis |
|---|---|---|
| Low | 0.060 | No addressable under-ascertained deaths |
| Central | 0.0625 | ~0.7 pp raw extra deaths × ~35% addressable |
| High | 0.068 | 1.0 pp raw extra (upper LTFU + a little not-evaluated) × ~80% addressable, or equivalently the critic's low-end figure with full addressability |
| Critic's unadjusted upper bound (reference only) | 0.074 | Full addressability, upper end of critic's arithmetic |

## Sensitivity Analysis

Base case SROI is **3,055x**: 19,800 deaths averted per year, 534,600 DALYs, $OP 53.46B benefit.

| baseline_mortality | Deaths averted/yr | SROI | Δ |
|---|---|---|---|
| 0.060 (low/base) | 19,800 | 3,055x | 0% |
| 0.0625 (central) | 20,625 | 3,182x | +4.2% |
| 0.066 | 21,780 | 3,361x | +10.0% |
| 0.068 (high) | 22,440 | 3,462x | +13.3% |
| 0.074 (critic's unadjusted max) | 24,420 | 3,768x | +23.3% |

**Pessimistic direction:** This critique cannot lower mortality below the reported 6% "died" share, so its pessimistic bound is 0% change. The downward pressure comes from Critiques 1–2 (survivor excess mortality and unreachable deaths), which act on other parameters.

**Interactions:**
- The effect is multiplicative with relative_reduction, p_success, etc. With all other parameters fixed, it is exactly proportional.
- If Critique 1 lowers effective RR by factor k, the combined effect is (1 + m) × k. Effects multiply rather than add.

## Bottom-Line Impact

This critique could **increase** cost-effectiveness by 0% to 13%, with a central estimate of about +4% (SROI from 3,055x to about 3,180x). The critic's unadjusted +10 to 23% overstates it because it ignores addressability and the likely-alive not-evaluated group.

## Materiality Verdict

**NO (borderline at the upper bound).**
- The central estimate is about 4%.
- The upper bound is about 13% and only increases SROI, which is already above the 2,000x bar.
- It does not change the funding decision. It mainly serves as a partial offset to Critiques 1–2.

## Code

```python
def sroi(bm, elig=5.5e6, yrs=8, dec=0.02, up=0.60, rr=0.10, dpd=27,
         opd=1e5, spd=1, cost=7e6, p=0.40):
    e = elig*(1-dec)**(yrs-8)
    deaths = e*up*bm*rr
    return deaths, deaths*spd*dpd*opd/cost*p

base = sroi(0.06)[1]
for bm in [0.06, 0.0625, 0.066, 0.068, 0.074]:
    d, s = sroi(bm)
    print(bm, round(d), round(s), f"{(s/base-1)*100:+.1f}%")

# effective increment: raw extra deaths x addressable share
for raw, addr in [(0.003,0),(0.007,0.35),(0.010,0.8)]:
    print(raw, addr, 0.06 + raw*addr)
```

Output: 3055 / 3182 (+4.2%) / 3361 (+10.0%) / 3462 (+13.3%) / 3768 (+23.3%).

## SENSITIVITY INPUTS

RANGE: baseline_mortality | current 0.06 | low 0.06 | central 0.0625 | high 0.068

--- Critique: Covariance between mortality and DALYs per death means the product of means is not the mean of the product ---

# Impact Assessment: Covariance Between Mortality and DALYs per Death

## Parameter mapping

The critique affects one parameter: **dalys_per_death**, currently 27, described by CG as "remaining healthy life expectancy." Nothing else changes:

- **baseline_mortality (0.06):** The mean is unchanged. Covariance does not alter average mortality, only which deaths carry the weight.
- **relative_reduction (0.10):** Not changed directly. The verifier's point is that the correct weight is *deaths averted*, not deaths. That weighting feeds into the effective dalys_per_death and is folded in below.

The issue can therefore be expressed entirely as an effective, death-averted-weighted value of dalys_per_death. SROI is linear in this parameter, so effects multiply with all other parameters.

### Is 27 already death-weighted? (the critique's own kill-switch)

- **Probably mostly yes.** "Remaining healthy life expectancy" is most naturally life expectancy at the typical age of TB death. That is a death-weighted construction, so the critique's main mechanism would largely not apply. The mechanism's example assumes 27 is a patient-weighted average, which is not how such figures are usually built.
- **Residual bias remains.** Life expectancy at the mean age of death is not the mean of life expectancy across deaths. This Jensen-type gap is a few percent and its sign is ambiguous.
- **GBD cross-check (my approximate recollection, not verified in this session).** GBD 2019 gives HIV-negative TB roughly 40M+ YLLs against ~1.2M deaths, about 33–35 YLL per death. HIV-positive TB deaths run higher per death, because they occur at younger ages. GBD uses an aspirational life table, so its figures overstate local remaining life expectancy. Even so, this does not suggest 27 is inflated by patient-weighting.

### Deaths-averted weighting (verifier's point)

If statins avert proportionally fewer deaths among the frail or elderly, the death-averted weight shifts toward younger patients. If they avert fewer among HIV+ patients or early deaths, the weight shifts toward older patients. These effects pull in opposite directions, so the sign is uncertain.

## Plausible range

**dalys_per_death:** current 27; plausible range 24–29; central 27.

- **Low (24):** The critique's illustrative calculation (≈23.8) applies only if 27 is patient-weighted *and* low-HIV settings dominate. Rounded to 24 because the premise is probably false.
- **High (29):** Applies in high-HIV deployment settings, where younger deaths dominate, or where benefit concentrates in younger patients.
- **Central (27):** Reflects unknown sign and the likelihood that 27 is already death-weighted.

## Sensitivity analysis

SROI = 5.5M × 0.6 × 0.06 × 0.10 × 1 × D × 100,000 / 7M × 0.4

| dalys_per_death | DALYs credited | SROI | Δ vs base |
|---|---|---|---|
| 27 (base) | 534,600 | 3,055x | — |
| 23.8 (critique's example) | 471,240 | 2,693x | −11.9% |
| 24 (low) | 475,200 | 2,716x | −11.1% |
| 29 (high) | 574,200 | 3,281x | +7.4% |
| 17.7 (breakeven at 2,000x bar) | — | 2,000x | −34.5% |

- **Joint pessimistic case:** Only one parameter is affected, so the joint case equals the low case at −11%.
- **Interactions with other critiques:** The effect is multiplicative. For example, a −11% here combined with a −40% cut to relative_reduction elsewhere compounds to −47%. That combined case is 1,630x, which falls below the bar. However, the joint result is driven by the other critique, not this one.

## Bottom-line impact

**This critique moves SROI by −11% to +7%, with a central estimate near 0%. Its sign is uncertain, and the effect is probably small because 27 is likely already a death-weighted figure.**

## Materiality verdict

**NO.**

- Even the pessimistic value (2,716x) clears the 2,000x bar comfortably.
- Breakeven would require dalys_per_death of about 17.7, a 34% cut, which the evidence does not support.
- The critique is a valid methodological point, but it is not decision-relevant on its own.

## Code

```python
base = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
            all_in_cost=7_000_000, p_success=0.40)

def sroi(p):
    elig = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    deaths = elig * p['adult_uptake'] * p['baseline_mortality'] * p['relative_reduction']
    benefit = deaths * p['speedup_years'] * p['dalys_per_death'] * p['op_per_daly']
    return benefit / p['all_in_cost'] * p['p_success']

b = sroi(base)
print(f"base {b:.0f}")
for d in [23.8, 24, 27, 29]:
    s = sroi({**base, 'dalys_per_death': d})
    print(d, round(s), f"{(s/b - 1)*100:+.1f}%")
print("breakeven D:", 27 * 2000 / b)

# Critique's illustrative death-weighted value
mA, dA, wA, mB, dB, wB = 0.04, 35, 0.7, 0.12, 15, 0.3
m = wA*mA + wB*mB
print("mean mort", m, "death-weighted D", (wA*mA*dA + wB*mB*dB) / m)
# -> base 3055; 23.8 -> 2693 (-11.9%); 24 -> 2716 (-11.1%); 29 -> 3281 (+7.4%); breakeven 17.7
```

## Sensitivity inputs

RANGE: dalys_per_death | current 27 | low 24 | central 27 | high 29

--- Critique: A global-average mortality may not match the countries where an atorvastatin adjunct would actually be deployed ---

# CRITIQUE: A global-average mortality may not match the countries where an atorvastatin adjunct would actually be deployed

## Parameter Mapping

- **Primary:** `baseline_mortality` (0.06), mortality among treated drug-susceptible patients. It enters the formula chain linearly: deaths/yr = treated × baseline_mortality × relative_reduction.
- **Secondary, not changed here:** `relative_reduction`. The verifier's caveat that trial patients have lower mortality than programme cohorts bears more on whether the trial's relative effect transfers to programme settings than on the baseline itself. I flag it below but do not adjust it in this assessment, to avoid double-counting with Thread 1.

## Plausible Range

Current value: 0.06 (CG's figure, described as ~6%).

| Point | Value | Basis |
|---|---|---|
| Low | 0.04 | Deployment weighted toward India-like settings (about 4–5%, unverified figure from memory). The trial-versus-programme caveat pushes it down a little further. |
| Central | 0.055 | Mild downward shift. The trial caveat and case-weighting toward large Asian burdens are partly offset by unascertained deaths among those lost to follow-up, which CG omits and which would raise true mortality. |
| High | 0.075 | Deployment mix with a large share of high-HIV countries (the critique's figure for South Africa is about 8–10%, unverified). Also includes possible upward correction for deaths missed by notification data. |

Supporting data and caveats:
- WHO reports 88% global treatment success for drug-susceptible TB in 2022–23. The remaining 12% (deaths, loss to follow-up, failure) is consistent with deaths of roughly 5–6% globally and wide spread between countries.
- The specific India and South Africa percentages remain unsourced. The range above deliberately avoids leaning on them as point values.

## Sensitivity Analysis

SROI is strictly proportional to `baseline_mortality`, with no interactions inside the formula chain. The value that exactly hits the 2,000x funding bar is 0.06 × 2000 / 3055 = 0.0393.

| baseline_mortality | Deaths averted/yr | SROI | Change vs base |
|---|---|---|---|
| 0.04 (low) | 13,200 | 2,037x | −33% |
| 0.045 | 14,850 | 2,291x | −25% |
| 0.055 (central) | 18,150 | 2,800x | −8% |
| 0.06 (base) | 19,800 | 3,055x | — |
| 0.075 (high) | 24,750 | 3,819x | +25% |
| 0.08 | 26,400 | 4,073x | +33% |

**Joint effects:**
- Because the model is multiplicative, any other critique that lowers `relative_reduction`, `adult_uptake` or `p_success` compounds with this one.
- For example, `baseline_mortality` = 0.04 combined with `relative_reduction` = 0.08 gives about 1,630x, which falls below the bar.
- On its own, the low end of this critique stays just above 2,000x.

## Bottom-Line Impact

Re-weighting baseline mortality to the deployment countries moves SROI by −33% to +25% (2,037x to 3,819x). The central estimate is about −8% (~2,800x). The direction is genuinely uncertain.

## Materiality Verdict

**BORDERLINE.**
- The swing is large: it exceeds ±10% at both ends.
- Even the pessimistic case does not cross the 2,000x bar unless baseline mortality falls below 3.9%.
- This critique becomes decision-relevant mainly when combined with downward critiques of other parameters.

## Code

```python
def sroi(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=1e5, speedup_years=1,
         all_in_cost=7e6, p_success=0.40):
    eligible = eligible_people_at_8y * (1 - decline_per_year) ** (years_to_adoption - 8)
    treated = eligible * adult_uptake
    deaths = treated * baseline_mortality * relative_reduction
    benefit = deaths * speedup_years * dalys_per_death * op_per_daly
    return deaths, benefit / all_in_cost * p_success

base = sroi()[1]
for bm in [0.04, 0.045, 0.055, 0.06, 0.075, 0.08]:
    d, s = sroi(baseline_mortality=bm)
    print(bm, round(d), round(s), f"{(s/base-1)*100:+.0f}%")

print("breakeven bm:", 0.06 * 2000 / base)
print("joint 0.04 & rr 0.08:", sroi(baseline_mortality=0.04, relative_reduction=0.08)[1])
```

## Sensitivity Inputs

RANGE: baseline_mortality | current 0.06 | low 0.04 | central 0.055 | high 0.075

--- Critique: Industry phase-transition base rates put "II and III both succeed" at roughly 15–25%, so 40% requires an unstated premium of about 1.6–2.7× ---

# Critique: Industry base rates suggest P(Phase II and III both succeed) is about 15–32%, not 40%

## Parameter mapping

- **p_success** (primary). Current value is 0.40, described as the "probability Phase II and III both succeed." It enters SROI as a final linear multiplier.
- **No other parameters are touched.** The critique's decomposition includes a third factor, P(adopted | III), of about 0.7–0.85. Adoption is plausibly already partly captured by `adult_uptake` (0.60). I do **not** fold that factor into p_success here, to avoid double-counting with the uptake critique. I note it only as a downside consideration for the low end.
- **Interaction with relative_reduction.** The model treats p_success and relative_reduction as independent. I keep relative_reduction fixed at 0.10. Because both enter multiplicatively, any joint adjustment from other critiques compounds with this one.

## Plausible range

Current p_success is 0.40. Plausible range is 0.17 to 0.40, with a central value of 0.27.

| Point | Value | Basis |
|---|---|---|
| Low | 0.17 | BIO 2011–2020: Phase II→III 28.9% × Phase III→filing 57.8% = 0.167. Hay et al. 2014 non-oncology: 34.8% × 54% = 0.188. Both put plain industry base rates at about 0.17–0.19. |
| Central | 0.27 | An infectious-disease adjustment (Phase III success about 81% in one analysis) gives about 0.25–0.32. I shade toward the lower half because the critique says the Wong 2019 figures still need checking, and because "success" may extend to a mortality endpoint or adoption, which industry "filing" does not require. |
| High | 0.40 | Current value. The Verifier noted that industry rates include business-driven terminations and use a different start point. A PK/dose-finding Phase IIc is easier to pass, and a repurposed generic carries lower safety risk. These factors could justify a premium that brings p_success back to about 0.40. Nothing in the evidence supports going above 0.40. |

**Possible downside beyond 0.17.** If CG's "success" also requires WHO adoption, multiplying by 0.7–0.85 would give about 0.12–0.14. I do not include this in the range because it overlaps with `adult_uptake`.

## Sensitivity analysis

Base SROI is 3,055x, against a funding bar of 2,000x. SROI is linear in p_success: SROI = 7,637.1 × p_success. The break-even p_success for the 2,000x bar is 0.262.

| p_success | SROI | Δ vs base | Clears 2,000x bar? |
|---|---|---|---|
| 0.17 (BIO base rate) | 1,298x | −57.5% | No |
| 0.19 (Hay 2014) | 1,451x | −52.5% | No |
| 0.20 | 1,527x | −50.0% | No |
| 0.25 | 1,909x | −37.5% | No |
| **0.27 (central)** | **2,062x** | **−32.5%** | **Barely** |
| 0.32 | 2,444x | −20.0% | Yes |
| 0.40 (current) | 3,055x | 0% | Yes |
| 0.13 (with adoption factor) | 993x | −67.5% | No |

**Absolute effect:** SROI falls from 3,055x to between 1,298x and 3,055x, with a central estimate of 2,062x.

**Joint effects:** only one parameter changes, so there is no within-critique interaction. Combined with other critiques that cut relative_reduction or adult_uptake, effects are multiplicative. For example, p_success = 0.27 together with a 20% cut to relative_reduction gives 1,650x.

**Optimistic direction:** the evidence gives no basis for p_success above 0.40, so this critique cannot raise SROI.

## Bottom-line impact

**This critique reduces SROI by 0% to 58%, with a central estimate of about 33% (3,055x → about 2,060x).** That central estimate leaves the grant just above the 2,000x bar, with almost no margin. Any p_success below 0.262 pushes it under the bar.

## Materiality verdict

**YES.** The central estimate cuts SROI by about a third and erases nearly all headroom above the bar. The lower half of the plausible range, which is supported by the plain industry base rates, crosses the bar. The result does depend on how large a repurposing/academic premium one accepts, and the Verifier rated that question unresolved.

## Code

```python
base = dict(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=1e5, speedup_years=1,
            all_in_cost=7e6, p_success=0.40)

def sroi(p):
    elig = p['eligible_people_at_8y']*(1-p['decline_per_year'])**(p['years_to_adoption']-8)
    deaths = elig*p['adult_uptake']*p['baseline_mortality']*p['relative_reduction']
    benefit = deaths*p['speedup_years']*p['dalys_per_death']*p['op_per_daly']
    return benefit/p['all_in_cost']*p['p_success']

b = sroi(base)                                   # 3055.0
print("break-even p:", 2000/(b/base['p_success']))  # 0.2619
for ps in [0.13,0.17,0.19,0.20,0.25,0.27,0.32,0.40]:
    s = sroi({**base,'p_success':ps})
    print(ps, round(s), f"{(s/b-1)*100:.1f}%", s>=2000)
```

## Sensitivity inputs

RANGE: p_success | current 0.40 | low 0.17 | central 0.27 | high 0.40

--- Critique: The TB-specific reference classes (host-directed therapy, adjunctives, regimen-shortening) have a much worse record than 40% ---

## CRITIQUE: The TB-specific reference classes (host-directed therapy, adjunctives, regimen-shortening) have a much worse record than 40%

### PARAMETER MAPPING

- **p_success** (primary). Probability that Phase II and III both succeed. Current value: **0.40**.
- **relative_reduction** (secondary, not quantified here). The critique notes that even the "successful" class member, dexamethasone in HIV-negative TB meningitis, has a modest and heterogeneous effect. That bears on effect size conditional on success. The verified evidence, however, is about the success rate, so I hold relative_reduction at 0.10 in the primary analysis and test the interaction only as an illustration.

In the model, SROI is strictly proportional to p_success:

SROI = [5.5M × 0.6 × 0.06 × RR × 1 × 27 × 100,000 / 7M] × p

### PLAUSIBLE RANGE

**p_success:** current 0.40. Plausible range is **0.15–0.35**, central **0.25**.

- **Low (0.15).** This is the critique's TB-class point estimate. The 10–20% class rate is UNGROUNDED: the list is hand-picked, there is no denominator for statins, and the endpoints are mismatched (TB meningitis mortality versus pulmonary culture or relapse). So I do not go below 0.15 or adopt the 0.10 floor.
- **Central (0.25).** This is the midpoint of the critique's blended TB-class plus industry estimate (0.2–0.3). It reflects a partial prior shift, consistent with the evidence strength being rated "moderate" and the verdict "partially verified."
- **High (0.35).** This allows that the generic prior is roughly right. The vitamin D meta-analysis showed a modest positive culture-conversion effect (OR 1.22), and selection bias in the failure list cuts against the critique. I do not go above 0.40 because no evidence suggests the TB class does better than generic.

### SENSITIVITY ANALYSIS

```python
def sroi(p=0.40, rr=0.10, elig=5.5e6, up=0.6, mort=0.06, dal=27, op=1e5,
         speed=1, cost=7e6, yrs=8, dec=0.02):
    eligible = elig*(1-dec)**(yrs-8)
    deaths = eligible*up*mort*rr
    return deaths*speed*dal*op/cost*p

base = sroi()
for p in [0.10, 0.15, 0.20, 0.25, 0.30, 0.35]:
    v = sroi(p=p)
    print(p, round(v), f"{(v/base-1)*100:.1f}%")
print("break-even p at 2000x:", 2000/sroi(p=1))
print("joint p=0.25, rr=0.07:", round(sroi(p=0.25, rr=0.07)))
```

Results (base SROI = 3,055x):

| p_success | SROI | Δ |
|---|---|---|
| 0.10 | 764x | −75% |
| 0.15 (low) | 1,146x | −62.5% |
| 0.20 | 1,527x | −50% |
| 0.25 (central) | 1,909x | −37.5% |
| 0.30 | 2,291x | −25% |
| 0.35 (high) | 2,673x | −12.5% |

- **Break-even.** SROI falls to the 2,000x bar at p_success = **0.262**. Any p_success below about 0.26 puts the grant below the bar.
- **Joint illustration.** At p = 0.25 combined with relative_reduction = 0.07 (a modest-effect shrink), SROI is 1,336x (−56%). The effects are multiplicative because both parameters enter the formula as factors.

### BOTTOM-LINE IMPACT

Replacing the generic 40% prior with a TB-adjunctive-informed prior reduces SROI by 12.5% to 62.5%, central −37.5%. That takes SROI from 3,055x to roughly 1,150x–2,670x, with a central value of about 1,900x.

### MATERIALITY VERDICT

**YES**, with the caveat that the prior is ungrounded. The central estimate (1,909x) falls just below the 2,000x bar, and the low end falls well below it. The bar is crossed whenever p_success is below about 0.26, so the conclusion depends on how much weight the selective TB reference class gets.

### SENSITIVITY INPUTS

RANGE: p_success | current 0.40 | low 0.15 | central 0.25 | high 0.35

--- Critique: "Success" probably means a surrogate or composite endpoint, but the model needs a 10% mortality reduction, so P(adopted AND 10% mortality benefit) < P(trials succeed) ---

# CRITIQUE: "Success" likely means a surrogate or composite endpoint, but the model needs a 10% mortality reduction, so P(adopted AND 10% mortality benefit) < P(trials succeed)

## Parameter mapping

| Parameter | Model key | Current value | Role |
|---|---|---|---|
| Relative mortality reduction conditional on "success" | `relative_reduction` | 0.10 | Primary. The critique says the right quantity is E[mortality RR reduction \| surrogate/composite success, adoption], which is plausibly below 0.10. |
| Probability Phase II and III both succeed | `p_success` | 0.40 | Secondary. The alternative framing is that if "success" requires a demonstrated ~10% mortality effect, p_success itself should be lower. |

**Avoiding double counting.** SROI depends on these two only through their product, p_success × relative_reduction. The critique has two framings:
- **(a)** Success is defined on a surrogate, so the expected mortality effect given success is lower.
- **(b)** Success is defined on mortality, so the probability of success is lower.

These are alternative descriptions of the same gap, not two separate haircuts. I express the critique through `relative_reduction` only. I treat a joint p_success revision as belonging to the separate p_success critique and show it only as an interaction.

**Population check.** The model uses DS-TB, with `baseline_mortality` = 0.06 among treated drug-susceptible patients. The verifier said the critique has force in low-mortality DS-TB populations and is weak in TB meningitis or advanced HIV. The model's population is the one where the critique applies. At 4–6% mortality, a 10% relative reduction implies a mortality-powered trial of tens of thousands per arm. That is far beyond a $7M all-in budget, so a surrogate or composite endpoint is very likely.

## Plausible range

**`relative_reduction`: current 0.10, low 0.05, central 0.07, high 0.10.**
- **Low (0.05).** This is the critique's lower bound: surrogate success translates into only about half the assumed mortality effect. Composite TB endpoints (failure, relapse, death) are dominated by non-death events, and surrogate-to-mortality translation in TB adjunct trials is historically weak. The figure is flagged as ungrounded, so I treat it as a bound, not an estimate.
- **Central (0.07).** This is a 30% shrinkage, the upper end of the critique's 5–7%. It reflects real but uncertain surrogate-to-mortality translation.
- **High (0.10).** No shrinkage. This applies if CG's 10% was already meant as E[mortality effect | success], or if success is defined on mortality. I cannot rule this out because CG's definition of success is unknown.

**Optimistic direction.** I considered whether a composite success could imply a mortality effect above 10%, for example through benefit concentrated in high-mortality HIV-coinfected patients. No verified evidence supports it, so I did not raise the high value above 0.10.

## Sensitivity analysis

```python
def sroi(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
         all_in_cost=7_000_000, p_success=0.40):
    eligible = eligible_people_at_8y * (1 - decline_per_year)**(years_to_adoption - 8)
    treated = eligible * adult_uptake
    deaths = treated * baseline_mortality * relative_reduction
    benefit = deaths * speedup_years * dalys_per_death * op_per_daly
    return benefit / all_in_cost * p_success, deaths

base, d0 = sroi()
print(f"base SROI {base:.0f}x, deaths/yr {d0:.0f}")
for rr in [0.05, 0.06, 0.07, 0.10]:
    s, d = sroi(relative_reduction=rr)
    print(f"RR={rr}: SROI {s:.0f}x, deaths/yr {d:.0f}, delta {100*(s/base-1):+.0f}%")
# break-even RR at 2000x bar
print("break-even RR:", 0.10 * 2000 / base)
# interaction with a p_success cut (alternative framing / separate critique)
for p in [0.30, 0.25]:
    for rr in [0.05, 0.07]:
        s, _ = sroi(relative_reduction=rr, p_success=p)
        print(f"p={p}, RR={rr}: {s:.0f}x ({100*(s/base-1):+.0f}%)")
```

**Results:**

| Scenario | Deaths averted/yr | SROI | Δ vs base |
|---|---|---|---|
| Base (RR = 0.10) | 19,800 | 3,055x | — |
| RR = 0.07 (central) | 13,860 | 2,139x | −30% |
| RR = 0.06 | 11,880 | 1,833x | −40% |
| RR = 0.05 (low) | 9,900 | 1,527x | −50% |
| RR = 0.10 (high) | 19,800 | 3,055x | 0% |

- **Break-even.** The 2,000x bar is reached at relative_reduction ≈ 0.0655, which is a 34.5% shrinkage from 0.10.
- **Interaction (multiplicative).** These cases apply only if a separate p_success critique is also accepted and is not the same gap counted twice.

| p_success | RR | SROI | Δ vs base |
|---|---|---|---|
| 0.30 | 0.07 | 1,604x | −47% |
| 0.30 | 0.05 | 1,145x | −63% |
| 0.25 | 0.05 | 955x | −69% |

The effects compound multiplicatively, because SROI is linear in each parameter.

## Bottom-line impact

This critique could reduce SROI by 0% to 50%, from 3,055x to between 3,055x and 1,527x, with a central estimate of −30% (about 2,140x). That central case sits just above the 2,000x bar. Any shrinkage beyond about 35% puts the grant below the bar.

## Materiality verdict

**BORDERLINE, leaning YES.** The thread spec does not define an explicit threshold, so I judged materiality against the 2,000x funding bar.
- A 30–50% swing is large on any reasonable standard.
- It decides whether the grant clears the 2,000x bar: the central case passes narrowly and the low case fails.
- The magnitude rests on an ungrounded surrogate-to-mortality shrinkage. It also depends on CG's undisclosed definition of "success," which could make the effect zero.

**Highest-value next step:** obtain CG's success definition and the Phase III primary endpoint.

## Sensitivity inputs

RANGE: relative_reduction | current 0.10 | low 0.05 | central 0.07 | high 0.10

--- Critique: Baseline year is stale and the 5.5M figure is sensitive to it ---

## CRITIQUE: Baseline year is stale and the 5.5M figure is sensitive to it

### PARAMETER MAPPING

- **eligible_people_at_8y** is the primary parameter. It sits at the head of the formula chain, and its current value is 5,500,000.
- **decline_per_year** (0.02) and **years_to_adoption** (8) are only indirectly involved, through how the baseline is projected forward. The formula's own decline exponent is `years_to_adoption − 8 = 0`. The 2% per year decline is therefore already baked into the 5.5M figure, and changing these two parameters in the model does nothing unless years_to_adoption ≠ 8.

**Reconstructing the 5.5M figure.** The model does not document the derivation. One plausible reconstruction is:

7.5M notifications × 0.96 drug-susceptible × ~0.90 adult × 0.98⁸ ≈ 5.51M.

This matches the stated value. The ~0.90 adult share and the anchor year are my inference, not stated by CG. The critique flags that the anchor year is an assumption.

### PLAUSIBLE RANGE

**eligible_people_at_8y:** current value is 5.5M. Plausible range is 5.5M to 6.1M, with a central value of 6.05M.

- **Low (5.5M, no change).** This applies if CG's 7.5M was already an effective near-current anchor, or if the 2023–24 rise in notifications is a one-off catch-up in case detection rather than a level that persists. Under the second reading, true incidence is flat to falling, so an equivalent future decline would offset it.
- **Central (6.05M).** This uses an 8.2–8.3M baseline with the same 0.96 × 0.90 × 0.98⁸ conversion.
- **High (6.1M).** This uses the 2024 WHO figure of 8.3M notifications (78% of incidence).

I did not extend the high end above 6.1M. A longer projection window from a 2024 anchor would push it lower, not higher. Further detection-gap closure is covered by Critique 2 and is not double-counted here.

### SENSITIVITY ANALYSIS

SROI is strictly linear in eligible_people_at_8y. There are no interactions with other parameters.

| Scenario | eligible | Deaths averted/yr | SROI | Δ |
|---|---|---|---|---|
| Base | 5.50M | 19,800 | 3,055x | — |
| Low | 5.50M | 19,800 | 3,055x | 0% |
| 8.2M baseline | 6.03M | 21,700 | 3,348x | +9.6% |
| Central | 6.05M | 21,780 | 3,360x | +10.0% |
| High (8.3M) | 6.10M | 21,960 | 3,388x | +10.9% |

**Pessimistic direction.** Suppose the notification rise is detection catch-up, and the future decline is ~3% per year instead of 2% from the new anchor. Then 8.3M × 0.96 × 0.90 × 0.97⁸ ≈ 5.6M, an SROI change of about +2%. Even the downside case does not go below the current figure. The direction is robustly upward or neutral.

**Funding bar.** The result stays far above the 2,000x bar in all cases.

### BOTTOM-LINE IMPACT

Updating the notifications baseline to 2024 (8.3M) raises SROI by about 0% to +11%, from 3,055x to roughly 3,330–3,390x, with a central estimate of +10% (~3,360x).

### MATERIALITY VERDICT

**NO.** The +9–11% change is well below the ±25% threshold. It is relevant only as an additive input that stacks with Critique 2 on detection-gap closure. Because both act multiplicatively on eligible_people_at_8y, they should be combined as a product, not double-counted.

### CODE

```python
def sroi(eligible=5.5e6, yta=8, decline=0.02, uptake=0.60, mort=0.06,
         rr=0.10, dalys=27, op=1e5, speed=1, cost=7e6, p=0.40):
    elig = eligible * (1 - decline) ** (yta - 8)
    deaths = elig * uptake * mort * rr
    benefit = deaths * speed * dalys * op
    return benefit / cost * p, deaths

base, d0 = sroi()
conv = 0.96 * 0.90 * 0.98**8          # reconstructed conversion ≈ 0.7351
print("reconstructed 5.5M:", 7.5e6 * conv)
for label, notif in [("8.2M", 8.2e6), ("8.3M", 8.3e6)]:
    e = notif * conv
    s, d = sroi(eligible=e)
    print(label, round(e), round(d), round(s), f"{s/base-1:+.1%}")
for e in [5.5e6, 6.05e6, 6.1e6]:
    s, d = sroi(eligible=e)
    print(e, round(d), round(s), f"{s/base-1:+.1%}")
# pessimistic: 3%/yr decline from 8.3M anchor
e = 8.3e6 * 0.96 * 0.90 * 0.97**8
print("pess", round(e), f"{sroi(eligible=e)[0]/base-1:+.1%}")
```

Output: base SROI is 3,054.9x. At 6.03M it is 3,348x (+9.6%), at 6.05M it is 3,360x (+10.0%), at 6.10M it is 3,388x (+10.9%), and the pessimistic case is ~5.6M (+2%).

### SENSITIVITY INPUTS

RANGE: eligible_people_at_8y | current 5500000 | low 5500000 | central 6050000 | high 6100000

--- Critique: A 2%/yr decline in notified case counts probably contradicts the observed trend; incidence rates fall slowly while counts do not ---

# Impact of the 2%/yr TB case-decline assumption on Coefficient Giving's atorvastatin SROI

**CRITIQUE:** A 2%/yr decline in notified case counts probably contradicts the observed trend; incidence rates fall slowly while counts do not.

## Parameter mapping

- **eligible_people_at_8y** (primary): currently 5,500,000. This is the only model input that moves.
- **decline_per_year** (currently 0.02) has no effect in the model as written. The formula is `eligible = eligible_people_at_8y × (1 − decline)^(years_to_adoption − 8)`. Since years_to_adoption = 8, the exponent is 0. CG's 2% decline is already baked into the 5.5M figure. Changing decline_per_year in the pipeline would therefore do nothing. The critique has to be expressed by changing eligible_people_at_8y.
- **years_to_adoption** (8) is not changed by this critique.

### Overlap with Critique 1

The critique's own scenario starts from the corrected 8.2M baseline: 8.2M × 0.96 × 0.90 → ~7.1M. That already includes Critique 1. To avoid double counting, I separate:

- **The decline component alone.** Replace CG's 0.98^8 = 0.851 count-decline factor with flat counts (1.0) or mild growth (1.01^8 = 1.083), keeping CG's implied baseline.
- **The combined figure from the critique's text** (7.1–7.7M). This is reported for information but not used as the central input.

## Plausible range for eligible_people_at_8y

| Scenario | Factor vs CG | Value |
|---|---|---|
| Downside: funding-cut disruption lowers notifications (illustrative, ungrounded) | ×0.95 | 5.2M |
| CG's 2%/yr decline is correct | ×1.00 | 5.5M |
| Flat counts over 8 years (decline component only) | ×1/0.851 = 1.175 | **6.46M** |
| Mild growth of +1%/yr (decline component only) | ×1.083/0.851 = 1.272 | 7.0M |
| Critique's combined scenario: 8.2M flat × 0.96 × 0.90 (includes Critique 1) | — | 7.1M |
| Combined with mild growth (includes Critique 1) | — | 7.7M |

Basis for the scenarios:
- The verified evidence supports flat notification counts from 2020 to 2024.
- A drug started at treatment initiation is exposed to treated counts, not the incidence-rate trend.
- Modelling of US funding cuts projects 12–41% more TB episodes among people living with HIV in South Africa. That raises incidence, but disruption could also lower notifications. The size of the downside is not grounded.

## Sensitivity analysis

SROI is linear in eligible_people_at_8y. Base SROI is 3,055x, with 19,800 deaths averted per year.

| eligible | Deaths averted/yr | SROI | Δ |
|---|---|---|---|
| 5.2M (downside) | 18,720 | 2,888x | −5.5% |
| 5.5M (base) | 19,800 | 3,055x | 0% |
| 6.46M (flat, isolated) | 23,256 | 3,588x | +17.5% |
| 7.0M (mild growth, isolated) | 25,200 | 3,888x | +27.3% |
| 7.1M (critique's combined scenario) | 25,560 | 3,944x | +29.1% |
| 7.7M (combined with growth) | 27,720 | 4,277x | +40.0% |

Notes on the results:
- There are no interactions with other parameters. The effect is purely multiplicative on the single input.
- All values stay above the 2,000x bar. Even the downside case keeps SROI near 2,900x.

## Bottom-line impact

Treating case counts as flat rather than declining 2%/yr raises SROI by about +17.5% (central), with a range of −5% to +27% for the decline component alone. When the critique's own scenario is combined with the Critique 1 baseline correction, the increase is +29% to +40%. That combined figure must not be added again on top of Critique 1.

## Materiality verdict

**BORDERLINE.**
- The isolated decline component (+17.5% central) is below the 25% threshold.
- It exceeds the threshold only under the mild-growth scenario or when combined with Critique 1.
- The direction is favourable to cost-effectiveness, so it does not threaten the funding decision.

## Code

```python
base = dict(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=1e5, speedup_years=1,
            all_in_cost=7e6, p_success=0.40)

def sroi(p):
    elig = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    deaths = elig * p['adult_uptake'] * p['baseline_mortality'] * p['relative_reduction']
    benefit = deaths * p['speedup_years'] * p['dalys_per_death'] * p['op_per_daly']
    return deaths, benefit / p['all_in_cost'] * p['p_success']

b_deaths, b = sroi(base)                                   # 19,800 ; 3054.9
flat = 5.5e6 / 0.98**8                                     # 6.46M
growth = 5.5e6 * 1.01**8 / 0.98**8                         # 7.00M
for E in [5.2e6, 5.5e6, flat, growth, 7.1e6, 7.7e6]:
    d, s = sroi({**base, 'eligible_people_at_8y': E})
    print(f"{E/1e6:.2f}M deaths={d:,.0f} SROI={s:,.0f} delta={(s/b-1)*100:+.1f}%")

# check decline_per_year is inert at years_to_adoption = 8
print(sroi({**base, 'decline_per_year': 0.0})[1] == b)     # True
```

## Sensitivity inputs

RANGE: eligible_people_at_8y | current 5500000 | low 5200000 | central 6460000 | high 7000000

--- Critique: "Adult DS notified" is not "eligible for the trial label": missing applicability filters ---

# CRITIQUE: "Adult DS notified" is not "eligible for the trial label": missing applicability filters

## Parameter mapping

- **Primary: `eligible_people_at_8y`**, currently 5,500,000 drug-susceptible TB patients per year at Phase III completion. Its own decline factor is (1−0.02)^(8−8) = 1, so this figure enters SROI directly.
- **Secondary, not changed in the inputs:**
  - **`adult_uptake` (0.60).** CG frames this as the share "of adult patients" who would add atorvastatin. Contraindications such as hepatic disease, pregnancy and interacting drugs could plausibly already sit partly inside this 40% non-uptake. If so, applying those filters again to `eligible` double-counts. I therefore discount the ungrounded filters (statin-specific, pregnancy, hepatic) rather than applying them at full strength.
  - **`baseline_mortality` (0.06).** Excluded subgroups have above-average case fatality, especially HIV-positive and extrapulmonary or meningeal TB. Removing them would lower average mortality in the remaining eligible group, which makes this critique more pessimistic than the head-count reduction alone. That direction depends on whether a trial or label actually excludes HIV-positive patients, which is unverified. I flag it but do not quantify it.

The 5.5M figure looks unfiltered. It is consistent with ~7.5–8M global notifications × 0.96 drug-susceptible × ~0.88 adult × 0.98^n decline. No pulmonary, confirmation or clinical filter appears in the formula chain.

## Plausible range for `eligible_people_at_8y`

| Scenario | Filter stack | Effective value |
|---|---|---|
| High (mild) | Pulmonary-only filter ×0.85 (extrapulmonary 16%, verified). No other exclusions. | 4.7M |
| Central | ×0.85 pulmonary; ×~0.90 for HIV, Hr-TB (7–8%) and contraindications, net of overlap and of what `adult_uptake` may already absorb; ×~0.95 partial misdiagnosis adjustment for clinically diagnosed cases (WHO), not a full confirmation filter. Product ≈ 0.73. | 4.0M |
| Low | ×0.85 × ~0.85 (all ungrounded filters applied fully, little overlap) × ~0.97. Also covers India/Nigeria/Indonesia weighting, where the extrapulmonary share runs up to ~25%. | 3.5M |
| Tail scenario (not in range) | Culture- or bacteriologically-confirmed-only label (×0.62 on top). Evidence rates this the weakest link, because real-world adoption would apply to all treated pulmonary DS-TB. | 2.5M |

## Sensitivity analysis

SROI is linear in `eligible_people_at_8y`, so the percentage change in SROI equals the percentage change in the parameter.

- Base case: 19,800 deaths averted per year, 534,600 DALYs, SROI **3,055x**.
- Break-even at the 2,000x bar: eligible = 5.5M × 2000/3055 = **3.60M**, which matches the critique's "3.6M bar".

| eligible | Deaths/yr | SROI | Δ |
|---|---|---|---|
| 5.5M (base) | 19,800 | 3,055x | — |
| 4.7M (high) | 16,920 | 2,611x | −14.5% |
| 4.2M | 15,120 | 2,333x | −23.6% |
| 4.0M (central) | 14,400 | 2,222x | −27.3% |
| 3.6M | 12,960 | 2,000x | −34.5% (break-even) |
| 3.5M (low) | 12,600 | 1,944x | −36.4% |
| 2.5M (confirmed-only) | 9,000 | 1,389x | −54.5% |

**Interactions.** All parameters in the chain are multiplicative, so this critique compounds with others.

- With `adult_uptake` cut from 0.60 to 0.50 (Thread 5), the central 4.0M gives 1,852x, below the bar.
- An offsetting decline correction (Critique 2) would scale eligible upward multiplicatively. For example, ×1.1 on 4.0M gives 4.4M and 2,444x.
- The secondary `baseline_mortality` effect would push results further down if HIV-positive patients are excluded. As an illustration, if they account for ~15% of deaths but only ~6% of cases, mortality among the remaining patients falls to about 0.054 (−10%).

## Bottom-line impact

**Explicit applicability filters reduce SROI by roughly 15–36% (central ~27%, 3,055x → ~2,220x).** The estimate stays above the 2,000x bar unless the ungrounded filters bite fully (≤3.6M) or the label is restricted to confirmed cases (−55%, ~1,390x).

## Materiality verdict

**YES** on magnitude, since the central change is about −27%. **BORDERLINE** on the funding decision: the low end of the range sits just under the bar, and the outcome depends on trial design and on whether `adult_uptake` already embeds the contraindications.

## Code

```python
def sroi(elig=5.5e6, yrs=8, dec=0.02, up=0.60, bm=0.06, rr=0.10,
         dpd=27, opd=1e5, spd=1, cost=7e6, p=0.40):
    e = elig * (1 - dec) ** (yrs - 8)
    deaths = e * up * bm * rr
    return deaths, deaths * spd * dpd * opd / cost * p

d0, base = sroi()
print(f"base deaths={d0:.0f}, SROI={base:.0f}")
print("break-even eligible:", 5.5e6 * 2000 / base)
for e in [4.7e6, 4.2e6, 4.0e6, 3.6e6, 3.5e6, 2.5e6]:
    d, s = sroi(elig=e)
    print(f"{e/1e6:.1f}M deaths={d:.0f} SROI={s:.0f} Δ={(s/base-1)*100:.1f}%")
print("4.0M & uptake 0.5:", sroi(elig=4.0e6, up=0.5)[1])
print("4.0M & bm 0.054:", sroi(elig=4.0e6, bm=0.054)[1])
```

## SENSITIVITY INPUTS

RANGE: eligible_people_at_8y | current 5500000 | low 3500000 | central 4000000 | high 4700000

--- Critique: Shorter and new regimens erode both the eligible population and the incremental benefit ---

# Impact assessment: shorter and new regimens erode the eligible population and the incremental benefit

## Parameter mapping

The SROI formula is purely multiplicative:

SROI = eligible × uptake × baseline_mortality × relative_reduction × speedup × DALYs/death × $OP/DALY ÷ cost × p_success

So the critique's mechanism (a share *s* of patients moved onto non-HRZE backbones, with a fraction *f* of the statin benefit lost on those backbones) is a single multiplicative factor, (1 − s·f). That factor can be applied to either `eligible_people_at_8y` or `relative_reduction` with the same result. I apply it **only** to `eligible_people_at_8y`, to avoid double-counting.

| Parameter | Current value | How the critique touches it |
|---|---|---|
| `eligible_people_at_8y` | 5,500,000 | Patients on HPMZ or BDQ-LZD backbones may not get the trial-demonstrated benefit |
| `relative_reduction` | 0.10 | This is the alternative channel. It is equivalent and not used separately. |

## Plausible range for the derived factor (s × f)

**Displacement share (s) of adult drug-susceptible patients on non-HRZE regimens by about 2033:**
- **0–30%. Central estimate 15%.**
- HPMZ is conditional and restricted to age ≥12.
- Rifapentine supply, cost and exposure-dependence slow its uptake.
- BDQ-LZD and TRUNCATE-type strategies are still trial-stage.
- The Investigator's 20–40% range is ungrounded. The verifier's evidence favours the low end.

**Benefit lost on those regimens (f):**
- **0–80%. Central estimate 50%.**
- The 4-month HRZ(E) regimen still contains rifampicin, so for that group f ≈ 0.
- HPMZ is still a rifamycin backbone with a CYP3A4 interaction, so the statin mechanism plausibly transfers in part.
- Shorter regimens may leave less room for benefit, but there is no evidence that the benefit drops to zero.

**Effective eligible reduction (s × f):**

| Case | Calculation | Reduction | `eligible_people_at_8y` |
|---|---|---|---|
| Low | 0 | 0% | 5.50M |
| Central | 0.15 × 0.5 | 7.5% | 5.09M |
| High | 0.30 × 0.8 | 24% (rounded to 25%) | 4.125M |
| Stress test (Investigator's own upper scenario) | 0.40 × 1.0 | 40% | 3.3M |

**Optimistic direction:** if shorter regimens have higher relapse, a statin could plausibly add more benefit. This is unevidenced, so I cap the optimistic case at no change.

## Sensitivity analysis

```python
def sroi(elig=5.5e6, yta=8, dec=0.02, up=0.6, bm=0.06, rr=0.10,
         dpd=27, opd=1e5, spd=1, cost=7e6, p=0.40):
    e = elig * (1 - dec) ** (yta - 8)
    deaths = e * up * bm * rr
    return deaths * spd * dpd * opd / cost * p

base = sroi()
for label, elig in [("low", 5.5e6), ("central", 5.0875e6),
                    ("high", 4.125e6), ("stress", 3.3e6)]:
    v = sroi(elig=elig)
    print(label, round(v), f"{(v / base - 1) * 100:.1f}%")

# Eligible population at which SROI equals the 2,000x bar
print("breakeven eligible:", 5.5e6 * 2000 / base)
```

| Scenario | `eligible_people_at_8y` | SROI | Δ vs. base |
|---|---|---|---|
| Base | 5.5M | **3,055x** | — |
| Low (no displacement) | 5.5M | 3,055x | 0% |
| Central | 5.09M | 2,826x | −7.5% |
| High | 4.125M | 2,291x | −25% |
| Stress (40% displaced, full benefit loss) | 3.3M | 1,833x | −40%, **below the bar** |

**Break-even:** SROI falls to the 2,000x bar at an eligible population of about 3.6M. That requires s × f ≈ 34.5%.

**Interactions:** the effect is multiplicative with every other critique. For example, if another thread cuts `relative_reduction` by 20%, the central case here becomes 3,055 × 0.925 × 0.8 ≈ 2,261x. Combined with the high case here, it becomes about 1,833x.

## Bottom-line impact

This critique plausibly reduces SROI by **0% to 25%**, with a central estimate of about **8%** (from 3,055x to about 2,830x). It does not push the estimate below the 2,000x bar on its own. Only the unsupported stress scenario of 40% displacement with full benefit loss does that.

## Materiality verdict

**NO on a standalone basis (BORDERLINE in combination).**
- The central effect is small, about −8%.
- Even the high case keeps SROI above the bar, at about 2,290x.
- It becomes material only when it compounds with other critiques that cut `relative_reduction` or `adult_uptake`.

## SENSITIVITY INPUTS

RANGE: eligible_people_at_8y | current 5500000 | low 4125000 | central 5087500 | high 5500000

--- Critique: M72/AS01E and other incidence shocks are likely not large enough by year 8–10, but should be modelled ---

# CRITIQUE: M72/AS01E and other incidence shocks are likely not large enough by year 8–10, but should be modelled

## Parameter mapping

The CEA credits benefit from **one accelerated year of adoption** (`speedup_years` = 1), occurring when Phase III finishes. So the only population that enters the calculation is the eligible pool **in the adoption year**. Later years are never summed. The critique's averaged 20–35% reduction over a 15+ year horizon therefore does **not** map onto this model, unless adoption is delayed into the window where vaccine effects grow.

- **`eligible_people_at_8y`** (primary): current value 5,500,000. A vaccine-driven incidence shock at year 8 enters directly here.
- **`years_to_adoption` / `decline_per_year`** (secondary): current values 8 and 0.02. The exponent is (8 − 8) = 0, so the 2% background decline is currently inactive. If adoption slips to year 10 or later, the decline exponent switches on. The vaccine shock would also be larger by then. This is a tail interaction, not the central case.
- **`p_success`** is not directly affected. The critique's point that vaccine success should be "weighted separately" is a point about the **vaccine's** success probability. That belongs inside the expected incidence shock (below), not inside the statin trial's `p_success`.

## Plausible range

The expected shock is the probability that the vaccine is licensed and rolled out by about 2033, multiplied by the incidence reduction achieved by then.

- **Timing:**
  - The Phase III began in March 2024.
  - A readout around 2028 is optimistic.
  - Licensure and WHO prequalification would then come around 2029–30, with a staggered national rollout after that.
  - At most 3–4 years of partial-coverage campaigns would run before 2033–35.
- **Efficacy:** The Phase IIb point estimate of 49.7% has a 95% CI of 2.1–74.2, based on 39 cases. Phase III success is perhaps 50–70% likely.
- **Mechanism:** M72 prevents progression in infected adults, so it can cut incidence faster than a transmission-only effect would. Even so, the published models (India; South Africa: 0.86–2.55M cases averted by 2050) are strongly back-loaded.

The resulting range for `eligible_people_at_8y`:

| Case | Shock | Value | Basis |
|---|---|---|---|
| Low (optimistic for the CEA) | 0% | 5,500,000 | No licensure by 2033, or negligible early effect |
| Central | about −4% | 5,300,000 | Probability-weighted |
| High (pessimistic) | −15% | 4,675,000 | Investigator's upper estimate; ungrounded, treated as a tail |

## Sensitivity analysis

```python
def sroi(elig=5.5e6, yta=8, dec=0.02, up=0.6, mort=0.06, rr=0.10,
         dpd=27, opd=1e5, spd=1, cost=7e6, p=0.4):
    e = elig*(1-dec)**(yta-8)
    deaths = e*up*mort*rr
    return deaths*spd*dpd*opd/cost*p

base = sroi()                                   # 3054.9
for e in [5.5e6, 5.3e6, 5.225e6, 4.675e6]:
    print(e, sroi(elig=e), sroi(elig=e)/base-1)
# Tail: adoption slips to year 10 AND a 35% vaccine shock by then
print(sroi(elig=5.5e6*0.65, yta=10))            # ~1907
# Break-even shock to hit the 2000x bar:
print(1-2000/base)                              # 0.345
```

| Scenario | SROI | Δ |
|---|---|---|
| Base (5.5M) | 3,055x | — |
| Central (5.3M, −3.6%) | 2,944x | −3.6% |
| −5% (5.225M) | 2,902x | −5% |
| −15% (4.675M) | 2,597x | −15% |
| Tail: adoption at year 10, 2% decline active, 35% vaccine shock | about 1,907x | −38% |

- **Deaths averted per year** move from 19,800 (base) to 19,080 (central) and 16,830 (pessimistic).
- **Linearity:** SROI is linear in eligible population, so effects are multiplicative with the other parameters.
- **Break-even:** It would take a shock of about 34.5% at the adoption year to push SROI below the 2,000x bar. That is only plausible in the delayed-adoption tail.

## Bottom-line impact

This critique could reduce cost-effectiveness by 0–15%, with a central estimate of about 4%. The 20–35% horizon-averaged figure does not apply, because the CEA credits only a single adoption-year speedup.

## Materiality verdict

**NO** in the central case, and **BORDERLINE** only in the delayed-adoption tail. The estimate stays above 2,000x unless adoption slips to around year 10 or later and the vaccine succeeds and scales quickly. The critique's most useful point is a coupling: the risk of adoption delay and the risk of a vaccine-driven incidence shock compound each other.

## SENSITIVITY INPUTS

RANGE: eligible_people_at_8y | current 5500000 | low 4675000 | central 5300000 | high 5500000