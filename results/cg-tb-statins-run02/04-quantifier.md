--- Critique: "Success" in Phase III is unlikely to be a mortality result, so the 10% mortality effect is not what a "success" would establish ---

# Impact Assessment: "Success" in Phase III Is Unlikely to Be a Mortality Result

**Bottom line:** If half of "success" worlds are surrogate-only successes carrying 0–5% true mortality reduction, SROI falls 25–50%, from 3,055x to roughly 1,530–2,290x. The bar is crossed when f exceeds about 0.35–0.69, depending on r_s. If CG's 10% is already meant as the expected mortality effect given a surrogate-level success, the impact is 0%.

## Parameter Mapping

| Parameter | Location | Current value | Role |
|---|---|---|---|
| `relative_reduction` (r) | Primary benefit multiplier | 0.10 | Reinterpreted as E[r \| success] |
| `p_success` (p) | Final multiplier | 0.40 | Unchanged, but its joint distribution with r matters |
| Implied E[r] unconditional | p × r | 0.04 | The quantity SROI actually depends on |

SROI = 5.5M × 0.60 × 0.06 × r × 1 × 27 × 100,000 / 7M × p. With p = 0.40 this reduces to **SROI = 30,548.6 × r**. SROI is exactly linear in E[r | success], so every percentage cut to E[r | success] passes one-for-one into SROI.

**Bar-crossing value:** r* = 2,000 / 30,548.6 = **0.0655**. The critique's f = 0.5, r_s = 0.03 case (0.065) sits just below this, as the critique claims. That is confirmed.

## Plausible Range

E[r | success] = (1 − f)(0.10) + f · r_s

| Input | Range | Basis |
|---|---|---|
| f (share of successes that are surrogate-only) | 0 to 0.75 | A mortality-powered trial is implausible (sample sizes below). However, a composite endpoint that includes death would carry some mortality information, so f < 1. The value of f is not sourced; it is the critique's assumption, flagged. |
| r_s (true mortality effect given surrogate-only success) | 0 to 0.05 | Not sourced. The Verifier found no human mortality data. The Phase IIB was open-label, with only culture-conversion, CXR and neuropathy signals. Myalgia was 16% vs 5%. A negative r_s cannot be excluded, but it is not tested here. |

**Sample-size check (verified):** Two-proportion test, 80% power, α = 0.05 two-sided, 10% relative reduction.

| Baseline mortality | n per arm | Total |
|---|---|---|
| 2% | ~73,100 | ~146,000 |
| 4% | ~35,900 | ~72,000 |
| **6% (CG's value)** | **~23,400** | **~47,000** |
| 8% | ~17,200 | ~34,000 |

The critique's figures reproduce. At CG's own 6% baseline, about 47,000 participants are needed. Even at an implausibly low $1,000 per participant, that is about $47M, which is 6.7× the entire $7M all-in budget. This independently corroborates the premise. It also ties to the all_in_cost thread: the budget only funds a surrogate- or composite-powered Phase III. By rough calculation, a 1,000-per-arm trial can detect only about a 50% relative mortality reduction.

## Sensitivity Analysis

Base case: r = 0.10, **SROI = 3,055x**.

| f \ r_s | 0 | 0.03 | 0.05 |
|---|---|---|---|
| 0.25 | 2,291x (−25%) | 2,520x (−17.5%) | 2,673x (−12.5%) |
| **0.50** | **1,527x (−50%)** | **1,986x (−35%)** | **2,291x (−25%)** |
| 0.75 | 764x (−75%) | 1,451x (−52.5%) | 1,909x (−37.5%) |

**Threshold f\* at which SROI hits 2,000x:**

| r_s | f\* |
|---|---|
| 0 | 0.35 |
| 0.03 | 0.49 |
| 0.05 | 0.69 |

**Optimistic and offsetting directions:**
- **Already priced in.** CG never claims a mortality-powered trial. If the 10% was intended as the expected effect given a surrogate or composite success, then f is effectively 0 relative to CG's intent, and **Δ = 0%**. CG's documentation does not derive the 10%, so this cannot be confirmed either way.
- **Mortality benefit in "failure" worlds.** The model gives zero benefit when the trial fails. A small true effect in non-success worlds could still drive some adoption, but that is unlikely without a positive result. The offset is small and not modeled.
- **p_success re-scoping.** If CG's 40% is the probability of surrogate success, p is unchanged. Raising p on the grounds that surrogates are easier to hit would double-count unless r is simultaneously cut. Only the product p × E[r | success] matters.
- **Negative r_s (toxicity).** This would push results below the f = 0.75, r_s = 0 cell. It is untested here and belongs to the Thread 1 harms analysis.

**Interactions:** The effect is multiplicative with every other thread, because SROI is a pure product. For example, a −25% cut here combined with a −20% cut on uptake gives 0.75 × 0.80 = −40% overall, not −45%.

## Bottom-Line Impact

At f = 0.5, this critique reduces cost-effectiveness by 25–50%, from 3,055x to 1,527–2,291x. Across the full plausible range (f = 0.25–0.75, r_s = 0–0.05), the reduction is 12.5–75%. If CG's 10% already represents a post-surrogate expected effect, the reduction is 0%.

## Materiality Verdict

**YES**, conditional on the definition question. Most of the plausible grid moves SROI by more than 10%, and the central case (f = 0.5, r_s ≤ 0.03) crosses the 2,000x bar. Materiality hinges on unsourced f and r_s, and on whether CG's 10% was already meant as a surrogate-conditional effect. The highest-value follow-up is to ask CG what its "success" means and how it derived the 10%.

## Code

```python
import numpy as np
from scipy.stats import norm

P = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
         all_in_cost=7_000_000, p_success=0.40)

def sroi(**kw):
    q = {**P, **kw}
    elig = q['eligible_people_at_8y'] * (1 - q['decline_per_year'])**(q['years_to_adoption'] - 8)
    deaths = elig * q['adult_uptake'] * q['baseline_mortality'] * q['relative_reduction']
    benefit = deaths * q['speedup_years'] * q['dalys_per_death'] * q['op_per_daly']
    return benefit / q['all_in_cost'] * q['p_success']

base = sroi()                                   # 3054.86
r_star = 2000 / (base / P['relative_reduction'])  # 0.0655
print(f"base={base:.0f}x, r*={r_star:.4f}")

for f in (0.25, 0.5, 0.75):
    for rs in (0, 0.03, 0.05):
        r = (1 - f) * 0.10 + f * rs
        s = sroi(relative_reduction=r)
        print(f"f={f}, r_s={rs}: E[r|succ]={r:.4f}, SROI={s:.0f}x, Δ={s/base-1:+.1%}")

for rs in (0, 0.03, 0.05):                      # f* crossing the 2000x bar
    print(f"r_s={rs}: f*={(0.10 - r_star)/(0.10 - rs):.2f}")

def n_per_arm(p1, rr=0.10, a=0.05, pw=0.80):
    p2 = p1 * (1 - rr); pb = (p1 + p2) / 2
    za, zb = norm.ppf(1 - a/2), norm.ppf(pw)
    return (za*np.sqrt(2*pb*(1-pb)) + zb*np.sqrt(p1*(1-p1) + p2*(1-p2)))**2 / (p1 - p2)**2

for b in (0.02, 0.04, 0.06, 0.08):
    print(f"baseline {b:.0%}: n/arm ≈ {n_per_arm(b):,.0f}")   # ~73.1k, 35.9k, 23.4k, 17.2k
```

--- Critique: A large share of on-treatment deaths is unreachable by a weeks-scale host-directed adjunct, and shorter regimens shrink the headroom further ---

# CRITIQUE: A large share of on-treatment deaths is unreachable by a weeks-scale host-directed adjunct, and shorter regimens shrink the headroom further

## Parameter Mapping

The BOTEC formula chain contains `relative_reduction` only as a single multiplicative term. SROI is therefore exactly linear in it: SROI = 30,549 × r.

| Parameter | Model key | Current value | Affected by critique? |
|---|---|---|---|
| Relative mortality reduction | `relative_reduction` | 0.10 | **Primary.** Decomposed as r_eff = f_reach × e_reach × h_regimen |
| Baseline on-treatment mortality | `baseline_mortality` | 0.06 | Only through the HPMZ argument, which is ungrounded (see below) |
| Joint (r, p_success) | `p_success` | 0.40 | Noted as an interaction. Not re-parameterised here (Thread on p_success) |

New sub-parameters (not in the CEA, introduced to operationalise the critique):

- **f_reach**: the fraction of on-treatment deaths a weeks-scale host-directed adjunct can plausibly affect. It excludes very early deaths, advanced-HIV/OI deaths and non-TB deaths.
- **e_reach**: the relative mortality reduction among reachable deaths.
- **h_regimen**: the headroom multiplier from a shift to the 4-month HPMZ regimen.

**Key interpretive caveat.** CG gives no derivation of the 10%. If CG already meant 10% as a *population-average* effect across all deaths, this critique implies no change. The adjustment applies only if 10% is read as the effect among deaths the drug can act on. The critique's force depends entirely on which reading is correct, and the CEA does not say.

## Plausible Ranges

| Sub-parameter | Base (implicit) | Plausible range | Basis |
|---|---|---|---|
| f_reach | 1.00 | **0.65–0.75** (critique placeholder, UNGROUNDED). Evidence-bounded: **0.667–0.982** | The verified evidence gives an unreachable/early-death share of 1.8–33.3%, varying strongly with setting and HIV prevalence. The critique's 25–35% sits at or beyond the top of that evidence range. |
| e_reach | 0.10 | 0.07–0.10 pessimistic; up to ~0.13–0.15 if CG's 10% was meant as a population average | Atorvastatin was given for 2 months (Phase IIB) or 16 weeks (sub-study), so it overlaps early deaths only partly. Rifampicin induction lowers statin exposure (not quantified by the Verifier). |
| h_regimen | 1.00 | 0.90–1.00 (**UNGROUNDED, speculative**) | CG's model does not use HPMZ. HPMZ eligibility is restricted (≥12y, ≥40kg, HIV CD4 thresholds), and uptake by year 8 is unknown. Illustration: 25% of patients on HPMZ × 30% lower reachable burden gives 0.925. |

## Sensitivity Analysis

Base case: 5.5M eligible × 0.60 uptake = 3.3M treated. Deaths averted are 3.3M × 0.06 × 0.10 = **19,800/yr**, giving **534,600 DALYs**, a benefit of $OP 53.46B, and **SROI = 3,055x**. The funding bar is 2,000x.

| Scenario | r_eff | Deaths averted/yr | SROI | Δ vs base |
|---|---|---|---|---|
| Base | 0.100 | 19,800 | 3,055x | — |
| f_reach = 0.982 (evidence low end of unreachable) | 0.0982 | 19,444 | 3,000x | −1.8% |
| f_reach = 0.75 (critique, optimistic) | 0.075 | 14,850 | 2,291x | −25% |
| f_reach = 0.70 (critique, central) | 0.070 | 13,860 | 2,138x | −30% |
| f_reach = 0.667 (evidence high end) | 0.0667 | 13,207 | 2,038x | −33% |
| f_reach = 0.65 (critique, pessimistic) | 0.065 | 12,870 | 1,986x | −35% (**just below bar**) |
| f_reach 0.70 × e_reach 0.08 | 0.056 | 11,088 | 1,711x | −44% |
| f_reach 0.65 × e_reach 0.07 | 0.0455 | 9,009 | 1,390x | −54.5% |
| HPMZ only (h = 0.925) | 0.0925 | 18,315 | 2,826x | −7.5% (ungrounded) |
| **Joint pessimistic**: 0.65 × 0.08 × 0.925 | 0.0481 | 9,524 | 1,469x | **−52%** |
| Optimistic: CG's 10% is already a population average (f_reach × e_reach ≈ 0.10, e.g. 0.75 × 0.133) | 0.100 | 19,800 | 3,055x | 0% |

Break-even points against the 2,000x bar:

- **r* = 0.0655.**
- At e_reach = 10%, SROI drops below the bar only if more than **34.5%** of deaths are unreachable. That is the extreme of the critique's range and slightly beyond the evidence maximum of 33.3%.
- At f_reach = 0.70, the bar is crossed if e_reach < **9.35%**.

**Interactions.** All sub-parameters enter multiplicatively with each other and with `p_success`, `adult_uptake` and `baseline_mortality`. Joint effects are therefore multiplicative, not additive. A correlated effect is not modelled here but points the same way: a smaller true r_eff also lowers the chance a Phase III detects a mortality benefit, which would reduce `p_success`. Including it would make the joint pessimistic case worse.

## Bottom-Line Impact

**If CG's 10% is read as the effect among drug-reachable deaths, this critique reduces SROI by about 2% to 35% (3,055x → 3,000x–1,986x).** The critique's central placeholder (30% unreachable) gives about −30% (2,138x). Adding a weaker effect among reachable deaths and HPMZ headroom loss gives a joint pessimistic case of about −52% (≈1,470x). If the 10% was already meant as a population average, the impact is 0%.

## Materiality Verdict

**BORDERLINE.**

- The relative change (−25% to −35% in the critique's own range) is large. However, the central case stays above the 2,000x bar, and the bar is crossed only at the extreme (≥34.5% unreachable) or when combined with a weaker per-reachable effect.
- The 25–35% figure is UNGROUNDED. Evidence supports only a 1.8–33.3% unreachable share.
- The HPMZ adjustment is UNGROUNDED. CG's model does not use a 4-month regimen, so that component should be flagged or dropped.
- Recommended framing: the critique's strongest use is to require CG to state whether 10% is a population-average or a reachable-subgroup effect. That clarification alone determines whether the impact is 0% or about −30%.

## Code

```python
base = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
            all_in_cost=7_000_000, p_success=0.40)

def sroi(p):
    eligible = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    treated = eligible * p['adult_uptake']
    deaths = treated * p['baseline_mortality'] * p['relative_reduction']
    benefit = deaths * p['speedup_years'] * p['dalys_per_death'] * p['op_per_daly']
    return deaths, benefit / p['all_in_cost'] * p['p_success']

d0, s0 = sroi(base)
print(f"Base: deaths={d0:,.0f}, SROI={s0:,.1f}x")

scenarios = {
    "f=0.982":              (0.982, 0.10, 1.0),
    "f=0.75":               (0.75, 0.10, 1.0),
    "f=0.70":               (0.70, 0.10, 1.0),
    "f=0.667":              (0.667, 0.10, 1.0),
    "f=0.65":               (0.65, 0.10, 1.0),
    "f=0.70,e=0.08":        (0.70, 0.08, 1.0),
    "f=0.65,e=0.07":        (0.65, 0.07, 1.0),
    "HPMZ only":            (1.0, 0.10, 1 - 0.25*0.30),
    "joint pessimistic":    (0.65, 0.08, 0.925),
    "pop-average reading":  (0.75, 0.10/0.75, 1.0),
}
for name, (f, e, h) in scenarios.items():
    p = dict(base, relative_reduction=f*e*h)
    d, s = sroi(p)
    print(f"{name:22s} r={f*e*h:.4f} deaths={d:8,.0f} SROI={s:7,.1f}x Δ={(s/s0-1)*100:+.1f}%")

r_star = 2000 / s0 * base['relative_reduction']
print(f"Break-even r* = {r_star:.4f}; max unreachable at e=0.10: {1 - r_star/0.10:.3f}; "
      f"min e_reach at f=0.70: {r_star/0.70:.4f}")
```

Output (as reported above):

- Base: SROI = 3,054.9x
- f = 0.65: 1,985.7x
- f = 0.70: 2,138.4x
- f = 0.75: 2,291.1x
- Joint pessimistic: 1,469.4x
- r* = 0.0655
- Maximum unreachable share at e = 0.10: 0.345
- Minimum e_reach at f = 0.70: 0.0935

--- Critique: Rifampicin induction structurally limits atorvastatin exposure in routine programs, and the trial exposure does not transfer ---

# Quantitative Impact Assessment

**CRITIQUE:** Rifampicin induction limits atorvastatin exposure in routine programs, so the trial exposure may not transfer.

*How these numbers were produced:* the figures below were worked by hand from the published formula chain. They are not output from a run against the spreadsheet file. The code at the end reproduces them.

---

## PARAMETER MAPPING

| Parameter | Model key | Current value | How the critique touches it |
|---|---|---|---|
| Relative mortality reduction | `relative_reduction` | 0.10 | **Primary.** Apply a transfer multiplier *m* for the gap between trial and routine-program exposure: r_eff = 0.10 × m |
| Probability Phase II and III succeed | `p_success` | 0.40 | **Secondary, only if a trial is itself exposure-limited** (for example, a Phase III run on a regimen other than the one tested). Tested separately, then jointly. |
| Uptake | `adult_uptake` | 0.60 | Not changed. Uptake is the share prescribed, not the exposure achieved. Applying a haircut here as well would double-count. |

**Narrowing from the verification step.** The Phase IIA/IIB signal came from atorvastatin given under rifampicin. That means:

- The "different statin" mechanism is dropped.
- The trial-derived r = 0.10 already reflects rifampicin induction under trial dosing.
- Only the **routine-versus-trial delta** applies. This has three sources:
  - dose timing (separated versus simultaneous dosing),
  - adherence below trial levels,
  - ART interactions.

The critique's own illustrative range, m ∈ [0.5, 0.8], is explicitly ungrounded. I therefore report it, but build a decomposed multiplier as the main estimate.

---

## PLAUSIBLE RANGE

**Decomposition:** m = 1 − f × (1 − e)

- **f** is the share of routine patients whose exposure departs materially from trial conditions. Sources:
  - separated dosing, which cuts AUC by about 80% (Backman 2005);
  - lower adherence;
  - efavirenz co-treatment, which roughly halves atorvastatin AUC. This share is small and shrinking as programs shift to dolutegravir (TLD).
- **e** is the effect retained in that subgroup. It is unknown, because the dose-response is unknown and the hepatocyte and lung tissue effect is unknown (per the label).

| Scenario | f | e | m | Basis |
|---|---|---|---|---|
| Optimistic | 0 | – | 1.00 (possibly ~1.1) | Co-administration with the morning fixed-dose TB pills is the natural routine practice and matches trial timing. Simultaneous dosing preserves or raises AUC. The Phase IIc dose-finding (20/40/60 mg) could even select a better dose than the earlier trials used. |
| Central | 0.2–0.3 | 0.3–0.4 | 0.79–0.88 | Typical gap between trial and routine adherence, plus some separated dosing and residual efavirenz use. |
| Pessimistic | 0.5 | 0.2 | 0.60 | Poor routine adherence and widespread separated dosing, with a steep dose-response. |
| Critique's illustrative range | – | – | 0.50–0.80 | Investigator's guess, not derived from data. |

---

## SENSITIVITY ANALYSIS

The SROI formula is linear in `relative_reduction`, so SROI = 3,055 × m.

**Base case:** 19,800 deaths averted per year; 534,600 DALYs; **SROI = 3,055x**. The funding bar is 2,000x.

| m | r_eff | Deaths averted/yr | SROI | Δ vs base | Clears 2,000x bar? |
|---|---|---|---|---|---|
| 1.10 (upside) | 0.110 | 21,780 | 3,360x | +10% | Yes |
| 1.00 | 0.100 | 19,800 | 3,055x | 0% | Yes |
| 0.88 | 0.088 | 17,424 | 2,688x | −12% | Yes |
| 0.80 | 0.080 | 15,840 | 2,444x | −20% | Yes |
| 0.79 | 0.079 | 15,642 | 2,413x | −21% | Yes |
| **0.655 (break-even)** | 0.0655 | 12,960 | 2,000x | −35% | Threshold |
| 0.60 | 0.060 | 11,880 | 1,833x | −40% | **No** |
| 0.50 | 0.050 | 9,900 | 1,527x | −50% | **No** |

**Joint test.** Exposure limitation might also lower the trial's success probability. I set m = 0.6 and p_success from 0.40 to 0.35:

- SROI = 1,604x, a change of −47%.
- The two effects are **multiplicative**: 0.6 × 0.875 = 0.525.
- This should be treated as speculative. If the trials use realistic co-administration, the routine gap does not lower p_success.

**Probability of falling below the bar (critique alone).** The break-even requires m < 0.655, which means f × (1 − e) > 0.345.

- With f ~ U(0.1, 0.5) and e ~ U(0.2, 0.6), independent: E[m] ≈ 0.82 and P(SROI < 2,000x) ≈ 2.5%. This was computed analytically and is reproduced by the Monte Carlo in the code below.
- Under the critique's own m ~ U(0.5, 0.8): P(SROI < 2,000x) ≈ 52%. That range sits close to the break-even point, so the conclusion depends heavily on an ungrounded assumption.

**Rifapentine (HPMZ) note.** Rifapentine is also a CYP3A4 inducer, but its interaction with atorvastatin is unverified. The 4-month duration also shortens the statin course. This adds uncertainty in both directions. I did not quantify it.

---

## BOTTOM-LINE IMPACT

- **Central estimate:** the routine-versus-trial exposure gap lowers cost-effectiveness by about **10–20%** (SROI ≈ 2,450–2,700x). That stays above the 2,000x bar.
- **Full plausible range:** **0% to −40%** (SROI 3,055x → 1,833x). There is a small upside of about +10% if dose-finding improves exposure.
- **Critique's own range:** −20% to −50%.
- **Break-even:** the bar is crossed only if routine programs retain **less than about 65%** of the trial effect.

---

## MATERIALITY VERDICT: **BORDERLINE**

No explicit threshold was supplied. I used two criteria: a change of more than 10%, or crossing the 2,000x bar.

**Material on the first criterion:**
- The central −10% to −20% exceeds 10%.

**Not decisive on the second criterion, for three reasons:**
1. The critique alone crosses the bar only at the pessimistic end (m < 0.655). Under the decomposed estimate this has roughly 2.5% probability.
2. The headroom is limited to 35%, which is thin. This critique could tip the outcome when stacked with others that also cut r (unreachable early deaths, adherence) or cut uptake. In those cases the multipliers compound.
3. Resolution is cheap. The registered ATORTUB popPK-PD sub-study should directly estimate exposure-response under 2RHZE/4RH.

**Recommendation:**
- Apply a modest m of about 0.85 as an adherence and timing haircut.
- Revisit once the popPK-PD sub-study reports.
- Make sure Thread 1 and the adoption thread do not both apply an adherence haircut.

---

## CODE

```python
import numpy as np

# Base parameters, using the model's parameter keys
P = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
         all_in_cost=7_000_000, p_success=0.40)

def sroi(p):
    """Reproduces the BOTEC formula chain."""
    eligible = p['eligible_people_at_8y'] * (1 - p['decline_per_year']) ** (p['years_to_adoption'] - 8)
    treated = eligible * p['adult_uptake']
    deaths = treated * p['baseline_mortality'] * p['relative_reduction']
    benefit = deaths * p['speedup_years'] * p['dalys_per_death'] * p['op_per_daly']
    return deaths, benefit / p['all_in_cost'] * p['p_success']

base_deaths, base = sroi(P)
print(f"Base: deaths/yr={base_deaths:,.0f}  SROI={base:,.0f}x")   # 19,800 ; 3,055x

# One-way sensitivity on the transfer multiplier m
for m in [1.10, 1.00, 0.88, 0.80, 0.79, 0.655, 0.60, 0.50]:
    q = {**P, 'relative_reduction': 0.10 * m}
    d, s = sroi(q)
    print(f"m={m:.3f}  deaths={d:>8,.0f}  SROI={s:>6,.0f}x  "
          f"Δ={(s / base - 1) * 100:+.0f}%  bar={'Y' if s >= 2000 else 'N'}")

print("Break-even m:", round(2000 / base, 3))     # 0.655

# Joint pessimistic test: m = 0.6 and p_success = 0.35
_, s = sroi({**P, 'relative_reduction': 0.06, 'p_success': 0.35})
print(f"Joint pessimistic: {s:,.0f}x ({(s / base - 1) * 100:+.0f}%)")   # ~1,604x, -47%

# Monte Carlo on the decomposition m = 1 - f*(1-e)
rng = np.random.default_rng(0)
N = 1_000_000
f = rng.uniform(0.1, 0.5, N)
e = rng.uniform(0.2, 0.6, N)
m = 1 - f * (1 - e)
print(f"E[m]={m.mean():.3f}  P(SROI<2000)={(base * m < 2000).mean():.3%}")   # ~0.82 ; ~2.5%

# The critique's own range: m ~ U(0.5, 0.8)
m2 = rng.uniform(0.5, 0.8, N)
print(f"Critique range: P(SROI<2000)={(base * m2 < 2000).mean():.1%}")       # ~52%
```

**Simplifications:**
- The exposure gap enters as a single multiplier on r. The model has no dose or exposure structure.
- f and e are assumed independent.
- All other parameters are held at base values.
- No time discounting, consistent with the model.

--- Critique: Winner's-curse and reference-class patterns imply the conditional effect should sit well below the surrogate-implied one, and r and p_success should not be independent ---

# CRITIQUE: The conditional mortality effect is likely below 10%, and r and p_success are not independent

## Parameter Mapping

| Parameter | Model key | Current value | Role in formula |
|---|---|---|---|
| Conditional relative mortality reduction | `relative_reduction` (r) | 0.10 | deaths/yr = treated × baseline_mortality × r |
| Probability Phase II and III succeed | `p_success` (p) | 0.40 | SROI = benefit / cost × p |
| Joint structure of (r, p) | implicit | independent; SROI ∝ p × r | the effective quantity is E[r × 1{success}] |

**Structural observation.** SROI is strictly linear in both r and p. With every other parameter at base:

- SROI = 30,548.6 × r (at p = 0.40)
- Equivalently, SROI = 76,371 × (r × p)

So every percentage change in r, or in the effective product r × p, passes through one-for-one to SROI.

**Note on "independence".** Multiplying p × r_cond is exact, not an independence assumption, *if* 0.10 really equals E[mortality effect | success]. The covariance concern therefore reduces to one question: is 0.10 the conditional mean mortality effect, given how "success" will actually be defined? I model this explicitly with a mixture parameter f below.

## Plausible Ranges

**1. Shrinkage factor s applied to r.**
- Critique range: 0.7–0.9, flagged as ungrounded and illustrative.
- Stress value s = 0.5 is included because the verified evidence points to a larger downward adjustment:
  - Human statin-TB surrogate data are null: rosuvastatin phase 2b showed identical 42-day median culture conversion (HR 1.30, p = 0.19) and no PET-CT effect.
  - Atorvastatin evidence is preclinical (guinea pig) and observational, so it carries translation and confounding risk, not just winner's-curse bias.
- Upside: s = 1.0 (no change). A value of 1.2 is shown for symmetry only; no surviving evidence supports it.

**2. Surrogate-only share of successes, f.** This is the fraction of "successful" outcomes (a positive trial leading to adoption) in which the true mortality effect is approximately zero.
- Range: 0–0.5. This is also ungrounded.
- Supporting argument that success will likely be surrogate-defined: a trial powered to detect 6.0% → 5.4% mortality (α = 0.05, 80% power) needs about 23,400 patients per arm (~47,000 total). That is incompatible with a $7M all-in budget, which pushes f above 0.
- Effective conditional effect: r_eff = 0.10 × s × (1 − f).

**3. Opposite-direction test (mortality-defined success).** If success instead required a mortality-powered result, selection would raise r_cond (illustratively 0.15) but lower p (illustratively 0.15–0.25).

## Sensitivity Analysis

**Base case:** r = 0.10, p = 0.40 → SROI = **3,055x**. The funding bar is 2,000x.

**Shrinkage alone (f = 0):**

| s | r | SROI | Δ |
|---|---|---|---|
| 1.2 (optimistic, unsupported) | 0.12 | 3,666x | +20% |
| 0.9 | 0.09 | 2,749x | −10% |
| 0.8 | 0.08 | 2,444x | −20% |
| 0.7 | 0.07 | 2,138x | −30% |
| 0.5 (stress) | 0.05 | 1,527x | −50% |

Break-even: r = 0.0655, i.e. s = 0.655.

**Surrogate-only mixture alone (s = 1):**

| f | SROI | Δ |
|---|---|---|
| 0.25 | 2,291x | −25% |
| 0.5 | 1,527x | −50% |

Break-even: f = 0.345.

**Joint grid (SROI; Δ vs. 3,055x):**

| s \ f | 0 | 0.25 | 0.5 |
|---|---|---|---|
| 0.9 | 2,749 (−10%) | 2,062 (−33%) | 1,375 (−55%) |
| 0.8 | 2,444 (−20%) | 1,833 (−40%) | 1,222 (−60%) |
| 0.7 | 2,138 (−30%) | 1,604 (−48%) | 1,069 (−65%) |
| 0.5 | 1,527 (−50%) | 1,146 (−63%) | 764 (−75%) |

The two effects are **multiplicative**: Δ = 1 − s(1 − f). At s = 0.8, the break-even surrogate-only share is f = 0.18.

**Opposite-direction test (mortality-defined success):**

| Scenario | E[r × p] | SROI | Δ |
|---|---|---|---|
| r_cond = 0.15, p = 0.25 | 0.0375 | 2,864x | −6% |
| r_cond = 0.15, p = 0.15 | 0.0225 | 1,718x | −44% |

Redefining success toward mortality raises the conditional effect but lowers p by more. It does not rescue the base case unless p stays near 0.27 or higher.

**Optimistic bound overall:** about 0%. No surviving evidence supports r > 0.10. The +20% figure at s = 1.2 is shown only for completeness.

## Bottom-Line Impact

**This critique reduces SROI by 10–30% on shrinkage alone (3,055x → 2,138–2,749x; still above the 2,000x bar). Adding a plausible surrogate-only share of successes (f = 0.25–0.5) makes the reduction 33–65% (→ ~1,070–2,060x). An illustrative central case (s = 0.8, f = 0.25) gives ~1,830x (−40%), just below the bar.**

Both s and f are ungrounded, so these figures are a sensitivity range, not an estimate.

## Materiality Verdict

**YES** (BORDERLINE if only the 0.7–0.9 shrinkage is accepted).

- Shrinkage alone moves SROI by 10–30% and leaves it above 2,000x. Break-even requires s ≤ 0.655.
- The joint mechanism crosses the funding bar across much of the plausible grid: any s(1 − f) < 0.655.
- The null rosuvastatin data make the low end of the range more credible than the high end.
- The result interacts multiplicatively with other threads (uptake, all-in cost, baseline mortality), so a moderate further adjustment elsewhere would compound it.

## Code

```python
import numpy as np

P = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
         all_in_cost=7_000_000, p_success=0.40)

def sroi(**kw):
    q = {**P, **kw}
    elig = q['eligible_people_at_8y'] * (1 - q['decline_per_year'])**(q['years_to_adoption'] - 8)
    deaths = elig * q['adult_uptake'] * q['baseline_mortality'] * q['relative_reduction']
    benefit = deaths * q['speedup_years'] * q['dalys_per_death'] * q['op_per_daly']
    return benefit / q['all_in_cost'] * q['p_success']

base = sroi()
print(f"Base SROI: {base:,.1f}")                                   # 3,054.9

# Shrinkage alone
for s in [1.2, 0.9, 0.8, 0.7, 0.5]:
    v = sroi(relative_reduction=0.10*s)
    print(f"s={s}: {v:,.0f} ({v/base-1:+.0%})")

# Joint shrinkage x surrogate-only mixture
for s in [0.9, 0.8, 0.7, 0.5]:
    print(s, [f"{sroi(relative_reduction=0.10*s*(1-f)):,.0f}" for f in [0, 0.25, 0.5]])

# Break-evens vs 2,000x bar
r_be = 2000 / (base / 0.10)
print(f"break-even r={r_be:.4f}, s={r_be/0.10:.3f}, f(s=1)={1-r_be/0.10:.3f}, "
      f"f(s=0.8)={1-r_be/0.08:.3f}")

# Opposite direction: mortality-defined success
for r, p in [(0.15, 0.25), (0.15, 0.15)]:
    v = sroi(relative_reduction=r, p_success=p)
    print(f"r={r}, p={p}: {v:,.0f} ({v/base-1:+.0%})")

# Sample size for a mortality-powered trial (6.0% -> 5.4%)
p0, p1 = 0.06, 0.054
pbar = (p0 + p1) / 2
n = 2 * (1.96 + 0.84)**2 * pbar * (1 - pbar) / (p0 - p1)**2
print(f"n per arm ~ {n:,.0f}")                                     # ~23,400
```

--- Critique: Hepatotoxicity and myopathy add a negative tail, and the combined attenuations compound ---

# Quantitative Impact Assessment: Hepatotoxicity/Myopathy Harm Tail and Compounding of Attenuations

**Bottom line:** The harm tail alone could lower SROI by 0–12% (central about −5%), from 3,055x to roughly 2,690–3,055x. It does not cross the 2,000x bar, so it is not material. The compounding scenario crosses the bar (about 700–1,650x), but most of that impact belongs to Critiques 1–4, and the inputs are illustrative and correlated. With half-embedding it is borderline (about 1,465–2,245x).

## Parameter Mapping

| Parameter | Location in model | Current value | How this critique touches it |
|---|---|---|---|
| `relative_reduction` | Primary efficacy input (deaths/yr = treated × baseline_mortality × r) | 0.10 | Harm tail lowers E[r]. Compounding multiplies r by attenuation factors. |
| `p_success` | Final multiplier on SROI | 0.40 | Alternative channel: toxicity caught in Phase IIc/III lowers p_success instead of r. **Apply one channel or the other, not both.** |
| Joint (r, p_success) distribution | Implicit; modeled as independent | — | Harm that the trial detects belongs to p_success. Harm that is too rare for trials to detect belongs to r. |

**Model structure.** SROI is exactly linear in r. With years_to_adoption = 8, the decline exponent is 0, so:

- SROI = 5.5M × 0.6 × 0.06 × r × 27 × 100,000 × 0.4 / 7M = **30,548.6 × r**
- Baseline at r = 0.10 is **3,054.9x**.
- The 2,000x bar requires r ≥ 0.0655, meaning **effective r can fall by at most 34.5%** before crossing the bar.

## Plausible Ranges

**A. Harm tail, conditional on adoption.** I modeled this two ways.

1. **Mixture model.** With probability q, the true effect is h ≤ 0. Otherwise it is 0.10.
   - Central: q = 0.10, h = 0 gives E[r] = 0.090.
   - Pessimistic: q = 0.10, h = −0.02 gives E[r] = 0.088.
   - Stress test: q = 0.15, h = −0.03 gives E[r] = 0.0805.
2. **Undetected absolute excess mortality δ** from added DILI or myopathy on top of HRZ.
   - Net r = 0.10 − δ/0.06.
   - δ = 0 to 0.0006 (0–0.06 percentage points of excess mortality) gives r = 0.090–0.100.
   - Basis: severe statin hepatotoxicity is rare. HRZ-induced DILI is common, so even a modest relative increase matters only if DILI case-fatality is non-trivial. Trials of a few hundred patients cannot detect this.

**Double-count caveat.** Harm large enough for Phase IIc/III to detect makes the trial "fail." That outcome is already in the 60% failure branch, which is valued at zero rather than negative. Only the undetectable rare tail should reduce r. That argues for the lower end of the range (0 to −0.005).

**Evidence that pushes toward zero harm:**
- StAT-TB selected pravastatin for lower toxicity.
- Pravastatin showed the least cell toxicity in THP-1 and Vero cells.
- The rosuvastatin trial showed no safety signal, though it was underpowered.

**Model mismatch flag.** The CG BOTEC specifies *atorvastatin*, but the evidence cited concerns *pravastatin*. Pravastatin is not CYP3A4-metabolized, so the rifampicin PK attenuation (Critique 2's factor) would likely be milder (about 0.8–1.0). The hepatotoxicity tail would also be smaller. This matters for which factor ranges apply.

**B. Compounding factors.** These are illustrative inputs from Critiques 1–4 and were not independently verified:

| Factor | Range |
|---|---|
| Reachable fraction | 0.65–0.75 |
| PK attenuation | 0.5–0.8 |
| Shrinkage | 0.7–0.9 |
| **Product** | **0.23–0.54** |

**Embedding scenario.** If CG's 10% already embeds about half of this attenuation (in log terms), the residual factor is the square root of the product, which is 0.48–0.73.

## Sensitivity Analysis

Base case: **3,055x**, 19,800 deaths averted/yr, 534,600 DALYs.

| Scenario | Effective r | Deaths averted/yr | SROI | Δ vs base |
|---|---|---|---|---|
| Harm tail: undetected δ = 0 (optimistic) | 0.100 | 19,800 | 3,055x | 0% |
| Harm tail central (q = 0.10, h = 0) | 0.090 | 17,820 | 2,749x | −10% |
| Harm tail pessimistic (q = 0.10, h = −0.02) | 0.088 | 17,424 | 2,688x | −12% |
| Harm tail stress (q = 0.15, h = −0.03) | 0.0805 | 15,939 | 2,459x | −19.5% |
| Equivalent via p_success channel (0.40 → 0.36) | — | — | 2,749x | −10% |
| Reachable fraction alone (0.65–0.75) | 0.065–0.075 | 12,870–14,850 | 1,986–2,291x | −35% to −25% |
| PK attenuation alone (0.5–0.8) | 0.05–0.08 | 9,900–15,840 | 1,527–2,444x | −50% to −20% |
| Shrinkage alone (0.7–0.9) | 0.07–0.09 | 13,860–17,820 | 2,138–2,749x | −30% to −10% |
| **Compounded, full application (0.23–0.54)** | 0.023–0.054 | 4,554–10,692 | **703–1,650x** | **−77% to −46%** |
| Compounded + harm tail (−0.01) | 0.013–0.044 | 2,574–8,712 | 397–1,344x | −87% to −56% |
| Compounded, half embedded (0.48–0.73) | 0.048–0.073 | 9,496–14,549 | 1,465–2,245x | −52% to −27% |
| Half embedded + harm tail (−0.01) | 0.038–0.063 | 7,516–12,569 | 1,161–1,939x | −62% to −37% |
| MC, independent uniforms (mean product ≈ 0.364) | ≈0.036 | ≈7,200 | ≈1,110x (90% CI ~800–1,450x) | ≈ −64% |

**Interactions:**
- All factors enter multiplicatively on r, so their effects compound rather than add. The sum of individual Δs overstates the joint effect at the mild end and understates it at the extreme end.
- The harm tail is additive on r. It therefore bites proportionally harder when r is already attenuated: −0.01 is 10% of 0.10 but 43% of 0.023.
- Break-even: the combined attenuation must stay ≥ 0.655. Even the most favourable corner of the illustrative ranges (0.75 × 0.8 × 0.9 = 0.54) falls below this if fully applied. The reachable-fraction low end alone (0.65) just crosses the bar at 1,986x.

**Optimistic direction:**
- If CG's 10% fully embeds these attenuations, and harm is either detectable (so it sits in p_success) or negligible with pravastatin, then Δ = 0.
- If the pravastatin PK factor is about 0.9–1.0, the compounded range rises to roughly 0.41–0.68, giving about 1,250–2,075x.
- I found no evidence-based upside (for example, hepatoprotection) to credit.

## Bottom-Line Impact

The harm tail alone reduces SROI by **0% to −12%** (central about −5% after removing the double-count with p_success), leaving it at about 2,690–3,055x, well above the 2,000x bar. Compounding with Critiques 1–4 would reduce SROI by **−46% to −77%** (700–1,650x) if fully applied, or **−27% to −52%** (1,465–2,245x) if CG's 10% half-embeds the attenuation. That impact is attributable to Critiques 1–4, not to this critique.

## Materiality Verdict

- **Harm tail (this critique's own contribution): NO.** It cannot cross the bar. Even the stress case (−19.5%) leaves SROI at about 2,460x.
- **Compounding observation: BORDERLINE.** It is decisive if Critiques 1–4 are validated and not already embedded, since it then crosses the bar in essentially all scenarios. However, it is not an independent impact and must not be double-counted with those critiques.
- **Recommended action:** Report the joint, multiplicative r adjustment once, in a consolidated Thread 1 estimate. Resolve the atorvastatin vs. pravastatin discrepancy first, because it changes both the PK and harm-tail ranges.

## Code

```python
import numpy as np

P = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
         all_in_cost=7_000_000, p_success=0.40)
BAR = 2000

def model(**over):
    p = {**P, **over}
    elig = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    treated = elig * p['adult_uptake']
    deaths = treated * p['baseline_mortality'] * p['relative_reduction']
    benefit = deaths * p['speedup_years'] * p['dalys_per_death'] * p['op_per_daly']
    sroi = benefit / p['all_in_cost'] * p['p_success']
    return deaths, sroi

d0, s0 = model()
print(f"Base: deaths/yr={d0:,.0f}, SROI={s0:,.1f}x, r_breakeven={0.10*BAR/s0:.4f}")

def show(label, r=None, **kw):
    if r is not None: kw['relative_reduction'] = r
    d, s = model(**kw)
    print(f"{label:45s} r={kw.get('relative_reduction',0.10):.4f} deaths={d:9,.0f} "
          f"SROI={s:7,.0f}x  Δ={s/s0-1:+.1%}  {'BELOW BAR' if s<BAR else ''}")

# Harm tail
mix = lambda q, h: (1-q)*0.10 + q*h
show("Harm: q=.10,h=0", mix(.10, 0))
show("Harm: q=.10,h=-.02", mix(.10, -.02))
show("Harm: q=.15,h=-.03 (stress)", mix(.15, -.03))
for delta in [0, 0.0003, 0.0006]:
    show(f"Harm: undetected excess mort δ={delta}", 0.10 - delta/0.06)
show("Harm via p_success 0.36", p_success=0.36)

# Individual attenuations
for name, (lo, hi) in {"reachable": (.65, .75), "PK": (.5, .8), "shrinkage": (.7, .9)}.items():
    show(f"{name} low", 0.10*lo); show(f"{name} high", 0.10*hi)

# Compounding
lo, hi = .65*.5*.7, .75*.8*.9
show("Compound full, low", 0.10*lo); show("Compound full, high", 0.10*hi)
show("Compound + harm, low", 0.10*lo - .01); show("Compound + harm, high", 0.10*hi - .01)
show("Half-embedded, low", 0.10*np.sqrt(lo)); show("Half-embedded, high", 0.10*np.sqrt(hi))
show("Half-embedded + harm, low", 0.10*np.sqrt(lo) - .01)
show("Half-embedded + harm, high", 0.10*np.sqrt(hi) - .01)
show("Pravastatin PK 0.9-1.0, low", 0.10*.65*.9*.7)
show("Pravastatin PK 0.9-1.0, high", 0.10*.75*1.0*.9)

# Monte Carlo, independent uniforms
rng = np.random.default_rng(0); N = 200_000
f = rng.uniform(.65, .75, N) * rng.uniform(.5, .8, N) * rng.uniform(.7, .9, N)
s = 30548.57 * 0.10 * f
print(f"MC: mean factor={f.mean():.3f}, SROI mean={s.mean():,.0f}x, "
      f"5-95%={np.percentile(s, 5):,.0f}-{np.percentile(s, 95):,.0f}x, "
      f"P(>bar)={np.mean(s > BAR):.3f}")
```

--- Critique: A $7M Phase III cannot be powered on mortality, and the CEA's benefit is mortality only ---

# Impact Assessment: A $7M Phase III Cannot Be Powered on Mortality

## Parameter Mapping

| Parameter | Model key | Current value | Role in this critique |
|---|---|---|---|
| All-in cost (all funders, through Phase III and guideline change) | `all_in_cost` | $7,000,000 | **Primary.** SROI scales with 1/cost. |
| Probability that Phase II and III both succeed | `p_success` | 0.40 | **Secondary.** If the $7M is kept, the trial is likely surrogate-endpoint, so "success" no longer implies a mortality benefit. |
| Relative mortality reduction | `relative_reduction` | 0.10 | Sets the effect size the trial must detect, which drives N. Its value is not changed here. |
| Baseline mortality | `baseline_mortality` | 0.06 | Sets the control event rate, which drives N. Its value is not changed here. |

The formula chain gives SROI = (eligible × uptake × baseline_mortality × relative_reduction × speedup × DALYs/death × $OP/DALY) / all_in_cost × p_success. Cost and p_success therefore enter **multiplicatively**: SROI ∝ p_success / all_in_cost.

## The Critique Implies Two Branches

The critique describes a dilemma, so I model two mutually exclusive branches:

- **Branch A: power the trial on mortality.** `all_in_cost` rises and `p_success` is unchanged.
- **Branch B: keep about $7M and run a surrogate-endpoint trial.** `all_in_cost` is unchanged. The effective probability of a real mortality benefit becomes p_success × P(mortality benefit | surrogate success).

## Plausible Ranges

### Sample size (reproduced; matches the critique)

Two-proportion test, 80% power, two-sided α = 0.05, 10% relative reduction:

| Control mortality | n per arm | Total N |
|---|---|---|
| 5% (5.0% → 4.5%) | 28,405 | 56,810 |
| 6% (CG's baseline) | about 23,000 | about 46,000 |
| 8% (5.0% → 7.2% equivalent, higher-risk cohorts) | 17,221 | 34,442 |

### Phase III cost (UNGROUNDED: per-participant cost is the key unknown)

| Per-participant cost | Phase III cost, N = 34k–57k | Basis |
|---|---|---|
| $100 (ultra-lean embedded) | $3.4M–$5.7M | Verifier's lower bound |
| $500 | $17M–$28M | Pragmatic LMIC |
| $1,000 | $34M–$57M | Pragmatic LMIC |
| $3,000+ | $100M–$170M+ | Conventional TB trial |

### all_in_cost

The $7M has no breakdown. I follow the critique's implicit assumption of about $5M of non-Phase-III costs (Phase II, guideline change, dissemination).

- Plausible range: $7M (lean design already assumed) to about $105M.
- Central: $20M–$40M.

### P(mortality benefit | surrogate success), Branch B only

- Plausible range: 0.5–0.8. This is judgement. There is no consensus on HDT endpoints, and surrogate-to-mortality translation in TB adjuncts is unproven.

## Sensitivity Analysis

**Base case:** SROI = **3,055x**. The funding bar is 2,000x.

### Branch A: all_in_cost varied, p_success = 0.40

| all_in_cost | SROI | Δ vs base | Above 2,000x bar? |
|---|---|---|---|
| $7M (lean design was already assumed) | 3,055x | 0% | Yes |
| $10M | 2,138x | −30% | Yes (barely) |
| **$10.7M (break-even with the bar)** | **2,000x** | **−35%** | Threshold |
| $20M | 1,069x | −65% | No |
| $30M | 713x | −77% | No |
| $37M (critique's point estimate) | 578x | −81% | No |
| $45M | 475x | −84% | No |
| $105M | 204x | −93% | No |

### Branch B: cost held at $7M, p_success haircut

| P(mortality benefit \| surrogate success) | Effective p_success | SROI | Δ |
|---|---|---|---|
| 0.8 | 0.32 | 2,444x | −20% |
| 0.65 | 0.26 | 1,986x | −35% |
| 0.5 | 0.20 | 1,527x | −50% |

### Break-even per-participant cost

This is the most decision-relevant output. For SROI to stay at or above 2,000x, all_in_cost must be ≤ $10.7M.

- With $5M of other costs, the Phase III must be ≤ $5.7M. That allows **$100–$165 per participant** across N = 57k–34k.
- With only $2M of other costs, the Phase III must be ≤ $8.7M. That allows **$153–$253 per participant**.

Only the ultra-lean embedded design clears the bar.

### Joint pessimistic case

Take all_in_cost = $45M. Also assume a moderately enriched cohort powered on mortality that generalises imperfectly to the drug-susceptible majority, with a 0.8 haircut on transferability. SROI = 3,055 × (7/45) × 0.8 ≈ **380x (−88%)**.

The effects multiply; they do not add.

### Optimistic direction

The critique cannot raise SROI. Its best case is 0% change, which requires an embedded or registry-based mortality trial at about $100 per participant, or a $7M figure that already assumed this. Correlated optimism is possible: a high-risk enriched cohort with 8% mortality *and* about $150 per participant would give a Phase III of about $5.2M. That keeps SROI around 2,500–3,000x, but generalisability would be weaker.

## Bottom-Line Impact

**This critique reduces SROI by 0% to −93%. The central range is −65% to −83% (SROI about 535–1,070x versus 3,055x), driven by an all-in cost of $20–40M. The model falls below the 2,000x bar once all_in_cost exceeds about $10.7M. Equivalently, it falls below the bar once the mortality-powered Phase III costs more than about $100–250 per participant. If CG instead keeps $7M and accepts a surrogate trial, the reduction is −20% to −50%.**

## Materiality Verdict

**YES.** The −65% to −83% central reduction far exceeds the 25% threshold. It also flips the funding decision (2,000x bar) in the central case.

Caveats:
- Evidence strength is **weak**, because per-participant cost is ungrounded and the $7M is not itemised.
- The lower tail (about 0%) is real if an ultra-lean embedded design is feasible.
- The single most valuable piece of information is CG's breakdown of the $7M and the intended Phase III endpoint and design. That alone would collapse most of this range.

## Code

```python
import numpy as np
from scipy.stats import norm

# ---- GiveWell/CG model (exact formula chain) ----
base = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
            all_in_cost=7_000_000, p_success=0.40)

def sroi(**kw):
    p = {**base, **kw}
    elig = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    deaths = elig * p['adult_uptake'] * p['baseline_mortality'] * p['relative_reduction']
    benefit = deaths * p['speedup_years'] * p['dalys_per_death'] * p['op_per_daly']
    return benefit / p['all_in_cost'] * p['p_success']

B = sroi(); print(f"Base SROI: {B:,.0f}x")            # 3,055x

# ---- Sample size (two-proportion, 80% power, alpha=0.05 two-sided) ----
def n_per_arm(p1, rrr=0.10, alpha=0.05, power=0.80):
    p2 = p1 * (1 - rrr)
    z = norm.ppf(1 - alpha/2) + norm.ppf(power)
    return z**2 * (p1*(1-p1) + p2*(1-p2)) / (p1 - p2)**2

for p1 in (0.05, 0.06, 0.08):
    n = n_per_arm(p1); print(f"p0={p1:.0%}: {n:,.0f}/arm, {2*n:,.0f} total")

# ---- Phase III cost by per-participant cost ----
N = {0.05: 2*n_per_arm(0.05), 0.08: 2*n_per_arm(0.08)}
for c in (100, 500, 1000, 3000):
    print(f"${c}/pt: ${N[0.08]*c/1e6:.1f}M - ${N[0.05]*c/1e6:.1f}M")

# ---- Branch A: cost sweep ----
for C in (7, 10, 20, 30, 37, 45, 105):
    s = sroi(all_in_cost=C*1e6)
    print(f"all_in=${C}M: SROI {s:,.0f}x, delta {s/B-1:+.0%}, above bar: {s>=2000}")

C_bar = base['all_in_cost'] * B / 2000
print(f"Break-even all_in_cost vs 2000x bar: ${C_bar/1e6:.2f}M")
for other in (5e6, 2e6):
    ph3 = C_bar - other
    print(f"other=${other/1e6:.0f}M -> Phase III <= ${ph3/1e6:.1f}M -> "
          f"${ph3/N[0.05]:.0f}-${ph3/N[0.08]:.0f} per participant")

# ---- Branch B: surrogate trial, p_success haircut ----
for h in (0.8, 0.65, 0.5):
    s = sroi(p_success=0.40*h); print(f"haircut {h}: SROI {s:,.0f}x, delta {s/B-1:+.0%}")

# ---- Joint pessimistic ----
s = sroi(all_in_cost=45e6, p_success=0.40*0.8)
print(f"Joint pessimistic: {s:,.0f}x, delta {s/B-1:+.0%}")
```

## Simplifications

- The full CG formula chain is used, and only the critique's parameters are varied.
- The ~$5M non-Phase-III cost component is an assumption inferred from the critique's own arithmetic, not from CG.
- Branch B's haircut factor is a judgement-based range, not an evidence-derived estimate.
- Interactions with other threads (discounting, uptake ramp, morbidity benefits) are excluded. Because the model is multiplicative, any further reduction from those threads would compound with this one.

--- Critique: The all-in framing counts benefits for every treated patient but not the cost of treating them ---

# CRITIQUE: The all-in framing counts benefits for every treated patient but not the cost of treating them

## Summary

The critique is valid, but the Investigator's break-even point is too strict. **Delivery costs are only incurred if the trials succeed**, so they should be weighted by p_success (0.40), just as benefits are. With that correction, SROI stays above 2,000x as long as delivery costs at most about **$2.80 per patient**, not the Investigator's $1.10.

Across plausible delivery costs and accounting conventions, SROI falls by **about 5% to 65%**. A central estimate is **about 20–35%**, giving roughly 2,000–2,450x. The estimate crosses the 2,000x bar at roughly $3 per course or more if third-party money is counted at face value.

The sharpest result: at $3 per course, delivering atorvastatin is itself about 5,400x per delivery dollar. Delivery money is therefore well spent, but counting it still shrinks CG's leverage ratio.

## Parameter mapping

| Parameter | Location | Current value | Role |
|---|---|---|---|
| all_in_cost | Denominator | $7,000,000 | Add expected delivery cost |
| (new) cost_per_course `c` | Not in model | Implicitly $0 | Procurement plus incremental monitoring and clinic time |
| (new) counterfactual value of third-party money `v` | Not in model | Implicitly 0 | 0 means the money is "free"; 1 means face value |
| treated = eligible × adult_uptake | Formula chain | 3,300,000 | Patients for whom delivery cost is incurred |
| p_success | Multiplier | 0.40 | **Must also apply to delivery cost** (no success means no rollout) |

**Correction to the critique: the 3.3M figure is not "unverified".** It is the model's own output (5.5M × 0.60). Its realism is a separate question for other threads.

**Correction to the critique: the delivery year.** The grant is credited with a 1-year speedup. Delivery costs in later years would happen in the counterfactual world anyway. So the incremental cost D covers only one year of patients:

D = 3.3M × c

## Corrected formula

SROI = p·B / (C + p·v·D)

- B = $OP 53.46B (benefit)
- C = $7M (all_in_cost)
- p = 0.40 (p_success)
- v = counterfactual value of third-party money
- D = 3.3M × c (delivery cost)

The Investigator's version, SROI = p·B / (C + v·D), charges delivery costs in the 60% of worlds where nothing is rolled out. That roughly doubles the apparent effect.

## Plausible range

**Cost per course `c`: $0.50–$15. Central estimate about $3.**

- **Procurement.** Generic atorvastatin is about $0.01–0.03 per tablet at tender or international reference prices. The course length is unresolved: Phase IIC is testing doses, and the prior trial used about 8 weeks. That gives roughly $0.50–$5 per course. *These prices are my assumptions, not verified.*
- **Monitoring.** Liver-function testing is partly already done for isoniazid/rifampicin/pyrazinamide (HRZ) therapy, so incremental monitoring is $0 to about $5.
- **Clinic time and adverse-event management.** About $0 to $5.

**Counterfactual value `v`: 0.25–1.0.** This is ungrounded because CG does not state a convention.

**Alternative convention: netting.** Instead of adding cost to the denominator, subtract the value the displaced money would have produced elsewhere. Call that X, in $OP per dollar, tested at 1,000x and 2,000x.

## Sensitivity results

Base case: **3,055x**. Bar: 2,000x.

### Denominator convention

| c ($/course) | D ($M) | Investigator (no p-weighting, v=1) | p-weighted, v=1 | p-weighted, v=0.5 | p-weighted, v=0.25 |
|---|---|---|---|---|---|
| 0.5 | 1.65 | 2,472x (−19%) | 2,792x (−9%) | 2,920x (−4%) | 2,986x (−2%) |
| 1 | 3.3 | 2,076x (−32%) | 2,570x (−16%) | 2,792x (−9%) | 2,917x (−5%) |
| **3** | 9.9 | 1,265x (−59%) | **1,951x (−36%)** | **2,381x (−22%)** | 2,676x (−12%) |
| 10 | 33 | 535x (−82%) | 1,059x (−65%) | 1,572x (−49%) | 2,076x (−32%) |
| 15 | 49.5 | 378x (−88%) | 798x (−74%) | 1,233x (−60%) | 1,789x (−41%) |

The Investigator's central case (D = $10M, no p-weighting) gives 1,258x. With correct p-weighting, the same D gives **1,944x (−36%)**.

### Break-even cost per course (SROI = 2,000x)

| Convention | Break-even |
|---|---|
| No p-weighting, v=1 (Investigator) | $1.12 |
| p-weighted, v=1 | **$2.80** |
| p-weighted, v=0.5 | $5.59 |
| p-weighted, v=0.25 | $11.19 |

### Netting convention: SROI = (p·B − p·D·X) / C

| c | X = 1,000x | X = 2,000x |
|---|---|---|
| $3 | 2,489x (−19%) | 1,923x (−37%) |
| $10 | 1,169x (−62%) | negative |

### Sanity check: cost-effectiveness of delivery alone

Each treated patient yields 0.06 × 0.10 × 27 × $OP 100k = **$OP 16,200**. So delivery alone returns 16,200 / c per delivery dollar:

- At $3 per course: about 5,400x.
- At $10 per course: about 1,620x.

Below about $8 per course, the delivery spending itself clears the bar. Counting it pulls the combined ratio toward the delivery ratio but does not show the program is wasteful.

### Parameter interactions

- **Within this critique, effects are multiplicative.** `c` and `v` enter only as the product p·v·c·3.3M.
- **With other threads, effects are non-additive.** D scales with adult_uptake and eligible_people_at_8y. A lower uptake (Thread 5) shrinks benefits and delivery costs in the same proportion, which partially offsets this critique.
- **Course length interacts with dose.** Dose/duration (Phase IIC) moves `c` and relative_reduction together.

## Bottom-line impact

Adding expected delivery costs reduces SROI by **about 5% to 65%, central about 20–35% (to roughly 2,000–2,450x)**. The estimate falls below 2,000x if delivery exceeds about $2.80 per course at face value, or about $5.60 at half value.

The Investigator's "2–3× reduction" overstates the effect because delivery costs were not weighted by p_success. The point that the result hinges on an unstated convention stands.

## Materiality verdict

**YES, conditional on convention.**

- Under the face-value convention, plausible central costs (about $3) push SROI to about 1,950x, at or below the bar.
- At v ≤ 0.25 with c ≤ $3, the change is ≤12%, which is **borderline**.
- The absence of a stated convention is itself a material modeling gap.

## Code

```python
p, C = 0.40, 7e6
treated = 5.5e6 * (1 - 0.02)**(8 - 8) * 0.60          # 3.3M
B = treated * 0.06 * 0.10 * 1 * 27 * 1e5              # 53.46e9 $OP
base = p * B / C                                       # 3054.9

def sroi(c, v=1.0, pweight=True):
    D = treated * c
    return p * B / (C + (p if pweight else 1) * v * D)

def sroi_net(c, X):
    return (p * B - p * treated * c * X) / C

for c in [0.5, 1, 3, 10, 15]:
    row = [sroi(c, 1, False), sroi(c, 1), sroi(c, .5), sroi(c, .25)]
    print(c, [f"{s:.0f} ({s/base-1:+.0%})" for s in row])

# break-even cost per course at the 2,000x bar
for v, pw in [(1, False), (1, True), (.5, True), (.25, True)]:
    w = (p if pw else 1) * v
    print(v, pw, (p * B / 2000 - C) / (w * treated))  # 1.12, 2.80, 5.59, 11.19

print(sroi_net(3, 1000), sroi_net(3, 2000), sroi_net(10, 1000))
print("delivery-only $OP per $:", treated * 0.06 * 0.10 * 27 * 1e5 / treated)  # 16,200 / c
```

--- Critique: Regulatory, pharmacovigilance and dissemination costs for an off-patent drug have no obvious payer, and the $7M likely under-budgets them ---

# CRITIQUE: Regulatory, pharmacovigilance and dissemination costs for an off-patent drug have no obvious payer, and the $7M likely under-budgets them

## Parameter mapping

| Parameter | Location in BOTEC | Current value | Role |
|---|---|---|---|
| `all_in_cost` | Denominator of SROI | $7,000,000 | Primary. The critique adds post-Phase III adoption infrastructure costs to it. |
| `p_success` | Multiplier on SROI | 0.40 | Not changed. It determines whether the added costs should be probability-weighted (see below). |
| `adult_uptake` | Benefit chain | 0.60 | Alternative channel. If nobody pays for the activities, they may not happen, and the loss appears as lower uptake rather than higher cost. |

The model is linear in the denominator: SROI = benefit × p_success / all_in_cost.

- Base case: 53.46e9 × 0.4 / 7e6 = **3,054.9x**
- Break-even all-in cost at the 2,000x bar: 53.46e9 × 0.4 / 2,000 = **$10.69M**
- Headroom: **$3.69M**

### A modelling point the critique misses

CG's formula treats `all_in_cost` as certain to be spent. Post-adoption pharmacovigilance and dissemination costs, however, are only incurred if Phase II and III succeed.

- In expected-value terms, the added cost should enter as 0.4 × X, not X.
- On that basis the headroom becomes $3.69M / 0.4 = **$9.23M** of conditional spending.

The same logic implies the existing $7M probably overstates expected cost, because Phase III is only run if Phase IIc succeeds. I therefore report both conventions:

- **(A) Unconditional:** CG's own convention, and conservative.
- **(B) Probability-weighted:** arguably more correct.

## Plausible range

- **Added cost X.** There is no evidential basis for any dollar figure; the Verifier flagged all magnitudes as UNGROUNDED. I sweep X from $0 to $20M.
  - Low end (X ≈ $0–1M): favourable early-phase safety data mean monitoring may be guideline-driven, light-touch and folded into existing national TB programme and WHO processes. Some dissemination may already sit in the $7M, which explicitly lists "guideline changes, dissemination and validation."
  - High end ($5–20M): the critic's illustration only. It is not evidence.
- **Uptake (alternative channel).** 0.60, falling to 0.3–0.5 if dissemination goes unfunded. This range is illustrative and not evidenced.

## Sensitivity analysis

Base case: 3,055x.

| Added cost X | (A) Unconditional SROI | Δ | (B) Probability-weighted (0.4X) SROI | Δ |
|---|---|---|---|---|
| $0 | 3,055x | 0% | 3,055x | 0% |
| $1M | 2,673x | −12.5% | 2,890x | −5.4% |
| $2M | 2,376x | −22.2% | 2,722x | −10.9% |
| $3.69M | 2,000x (bar) | −34.5% | 2,565x | −16.0% |
| $4M | 1,944x | −36.4% | 2,487x | −18.6% |
| $5M | 1,782x | −41.7% | 2,376x | −22.2% |
| $9.23M | 1,318x | −56.9% | 2,000x (bar) | −34.5% |
| $10M | 1,258x | −58.8% | 1,944x | −36.4% |
| $20M | 792x | −74.1% | 1,426x | −53.3% |

**Optimistic direction.** If the $7M already covers dissemination and monitoring is negligible, X = 0 and there is no change. If the $7M is itself an overestimate of expected spend, for example $5.5M once Phase III is weighted by the probability that Phase IIc succeeds, SROI rises to about 3,888x (+27%). That second effect belongs to the reconciliation of the $7M (Thread 2), not to this critique.

**Alternative channel: no payer leads to lower uptake rather than higher cost.** This is mutually exclusive with the cost channel, so the two should not be stacked.

| Uptake | SROI | Δ |
|---|---|---|
| 0.50 | 2,546x | −16.7% |
| 0.40 | 2,037x | −33.3% |
| 0.393 | 2,000x (break-even) | −34.5% |
| 0.30 | 1,527x | −50.0% |

**Interaction with other threads.** The effect is multiplicative with benefit-side cuts, so headroom shrinks quickly. If other critiques cut benefit by 30%, base SROI falls to 2,138x and cost headroom shrinks to:

- (A) unconditional: **$0.48M**
- (B) probability-weighted: **$1.2M**

At that point almost any unbudgeted adoption cost crosses the bar.

## Bottom-line impact

Plausible adoption-infrastructure add-ons of $0–5M reduce SROI by 0–42% under CG's unconditional-cost convention, or 0–22% if success-conditional costs are probability-weighted. The estimate drops below 2,000x only if unbudgeted costs exceed **$3.7M (unconditional)** or **$9.2M (probability-weighted)**. Every one of these magnitudes is ungrounded.

## Materiality verdict

**BORDERLINE.**

- The direction leans negative, and the model is fragile to this parameter. Headroom is $3.7M, about 53% of the stated cost.
- With no evidenced cost figure, and favourable safety data pointing towards light monitoring, the central case does not clearly cross the bar on its own.
- It becomes material jointly with any benefit-side critique.
- The most actionable fix is to ask CG for a breakdown of the $7M that shows whether pharmacovigilance and dissemination are inside it, and to probability-weight success-conditional costs.

## Code

```python
benefit = 5_500_000*(1-0.02)**(8-8)*0.60*0.06*0.10*1*27*100_000  # 5.346e10
p, cost, bar = 0.40, 7e6, 2000
sroi = lambda b=benefit, c=cost, p=p: b*p/c
base = sroi()
print(f"base {base:.1f}x, breakeven cost {benefit*p/bar/1e6:.2f}M")

for X in [0,1e6,2e6,3.69e6,4e6,5e6,9.23e6,10e6,20e6]:
    a = sroi(c=cost+X); b = sroi(c=cost+p*X)
    print(f"X={X/1e6:5.2f}M  A={a:7.1f} ({a/base-1:+.1%})  B={b:7.1f} ({b/base-1:+.1%})")

for u in [0.5,0.4,0.393,0.3]:
    s = sroi(b=benefit*u/0.6); print(f"uptake {u}: {s:.0f}x ({s/base-1:+.1%})")

s70 = sroi(b=benefit*0.7)
print(f"benefit-30%: {s70:.0f}x, headroom A {(cost*s70/bar-cost)/1e6:.2f}M, "
      f"B {(cost*s70/bar-cost)/p/1e6:.2f}M")
print(f"$5.5M all-in: {sroi(c=5.5e6):.0f}x")
```

--- Critique: Unclear scope boundary for the sweat-diagnostic workstream ---

# Impact Assessment: Unclear Scope Boundary for the Sweat-Diagnostic Workstream

**Bottom line:** At the evidence-supported scale, this critique moves SROI by about −7% to +8%, with a central estimate near 0% (roughly −1% to −3%). SROI stays well above 2,000x unless the diagnostic budget is about $3.7M or more, which the evidence argues against. Materiality verdict: **NO** on its own, but it becomes BORDERLINE if other critiques have already pushed SROI close to the bar.

## Parameter Mapping

| Parameter | Location | Current value | How the critique touches it |
|---|---|---|---|
| `all_in_cost` | SROI denominator | $7,000,000 | The diagnostic budget may sit inside the $7M, outside it, or partly inside it. |
| Diagnostic benefit term | Not in the formula chain (implicit zero) | 0 | The model note says "only mortality is valued," so diagnostic value is never counted. |
| `p_success`, `relative_reduction` | SROI numerator | 0.40, 0.10 | Not affected. The sweat test is an exploratory outcome and does not change the mortality pathway. |

### The mechanism is narrower than the critique states

The critique's pessimistic case is "diagnostic costs excluded but diagnostic-linked benefits counted." That case **cannot occur in the current model**, because diagnostic benefits are already zero. The live scenarios are:

- **A. Costs inside the $7M, benefits not counted.** The model carries cost with no matching benefit, so SROI is **understated**. This is the optimistic direction.
- **B. Costs outside the $7M, benefits not counted.** The model is internally consistent and there is **no effect**.
- **C. The grant funds a package of statins plus the diagnostic, but CG's SROI uses only the statin pathway cost.** The package cost is understated, so SROI is **overstated**. This is the only pessimistic channel, and it is the one the critique's $3.7M threshold applies to.

## Plausible Range

For the diagnostic budget *x* (Scenario C) or the share *d* of the $7M (Scenario A):

- **Central: $0.1M–$0.5M.**
  - Basis: ATORTUB lists sweat testing as an exploratory outcome, i.e. a sample-collection and assay add-on within existing trial infrastructure.
  - Per-trial biomarker add-ons of this kind typically cost in the low hundreds of thousands of dollars. This figure is my judgement, not a cited source.
- **Upper plausible: about $1M–$2M.**
  - This would apply if there is a separate assay-development or validation workstream funded under the same grant.
  - The Open Philanthropy collaborator listing on the Phase IIC record leaves this possibility open.
- **Implausible given the evidence: $3.7M or more.**
  - A budget this size would mean a standalone diagnostic program. That is inconsistent with the "exploratory outcome" framing.
- **Scenario A (optimistic):** *d* between $0 and $0.5M carved out of the $7M.

## Sensitivity Analysis

**Base case:** SROI = 53.46e9 × 0.40 / 7e6 = **3,054.9x**. Benefit is unchanged at $OP 53.46B (534,600 DALYs).

The relative change is analytic: Δ = 7 / (7 + x) − 1. The effect is purely multiplicative through the denominator.

### Scenario C (pessimistic): diagnostic cost *x* added to the denominator

| Diagnostic budget *x* | All-in cost | SROI | Δ |
|---|---|---|---|
| $0.10M | $7.10M | 3,011.8x | −1.4% |
| $0.25M | $7.25M | 2,949.5x | −3.4% |
| $0.50M | $7.50M | 2,851.2x | −6.7% |
| $1.00M | $8.00M | 2,673.0x | −12.5% |
| $2.00M | $9.00M | 2,376.0x | −22.2% |
| **$3.69M** | $10.69M | **2,000x** (bar) | −34.5% |
| $5.00M | $12.00M | 1,782.0x | −41.7% |

The breach point is x* = 7M × (3,054.9 / 2,000 − 1) = **$3.69M**. This confirms the critique's "about $3.7M" figure.

### Scenario A (optimistic): diagnostic share *d* removed from the $7M

| *d* | All-in cost | SROI | Δ |
|---|---|---|---|
| $0.25M | $6.75M | 3,168.0x | +3.7% |
| $0.50M | $6.50M | 3,289.8x | +7.7% |

### Scenario B

No change: 3,054.9x.

### Interaction with other critiques

This critique's effect is multiplicative with every other critique: it scales SROI by 7 / (7 + x), whatever the base. The breach budget, however, depends on the base SROI after other adjustments: x* = 7M × (SROI_adj / 2,000 − 1).

| SROI after Critiques 1–2 | Diagnostic budget that breaches 2,000x |
|---|---|
| 3,055x (base) | $3.69M |
| 2,500x | $1.75M |
| 2,200x | $0.70M |
| 2,100x | $0.35M |

If other critiques bring SROI within about 10–15% of the bar, even a central-range diagnostic budget could tip it. This is the only route to materiality.

## Bottom-Line Impact

At the evidence-supported scale ($0.1M–$0.5M), the critique changes SROI by **−1% to −7%**, or +4% to +8% if the diagnostic costs are already inside the $7M. The central estimate is roughly 0% to −3%. Breaching 2,000x on its own would require a diagnostic budget of about $3.7M or more, which the evidence argues against.

## Materiality Verdict

**NO**, standalone. It becomes **BORDERLINE** only conditionally: if Critiques 1 and 2 reduce SROI to about 2,100–2,500x, a $0.35M–$1.75M diagnostic budget would cross the bar.

The priority ranking below Critiques 1 and 2 is correct. The clarification question for CG remains worthwhile because it is cheap and resolves the sign: "Is the sweat-diagnostic workstream funded from this grant, and is it included in the $7M all-in figure?"

## Code

```python
base = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
            all_in_cost=7_000_000, p_success=0.40)

def sroi(p, extra_cost=0.0):
    elig = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    deaths = elig * p['adult_uptake'] * p['baseline_mortality'] * p['relative_reduction']
    benefit = deaths * p['speedup_years'] * p['dalys_per_death'] * p['op_per_daly']
    return benefit / (p['all_in_cost'] + extra_cost) * p['p_success']

b = sroi(base)
print(f"Base SROI: {b:,.1f}x")

# Scenario C: diagnostic cost added (pessimistic)
for x in [0.1e6, 0.25e6, 0.5e6, 1e6, 2e6, 5e6]:
    s = sroi(base, x)
    print(f"C  x=${x/1e6:.2f}M  SROI={s:,.1f}x  Δ={s/b-1:+.1%}")

# Scenario A: diagnostic cost removed from $7M (optimistic)
for d in [0.25e6, 0.5e6]:
    s = sroi(base, -d)
    print(f"A  d=${d/1e6:.2f}M  SROI={s:,.1f}x  Δ={s/b-1:+.1%}")

# Breach budget as a function of SROI after other critiques
x_star = lambda s_adj: base['all_in_cost'] * (s_adj / 2000 - 1)
print(f"Breach at base: ${x_star(b)/1e6:.2f}M")
for s_adj in [2500, 2200, 2100]:
    print(f"SROI_adj={s_adj}: breach at ${x_star(s_adj)/1e6:.2f}M")
```

**Simplifications:** None to the model structure. I used CG's formula chain exactly as written. The only modeling choices are the diagnostic-budget ranges, which are judgement-based because no budget figure is public.

--- Critique: Reference-class check: TB Phase III trials, and the evidence package WHO may require, point to more than one trial ---

# Impact Assessment: Phase III Reference-Class Cost Check

**CRITIQUE:** Reference-class check: TB Phase III trials, and the evidence package WHO may require, point to more than one trial

## Parameter Mapping

**Primary parameter: `all_in_cost`**
- Current value: **$7,000,000**. This covers all funders through Phase IIc, Phase III, guideline change, dissemination and validation.
- No breakdown of the $7M is given.

**Secondary interaction: `p_success` (Thread 1, not quantified here)**
- A Phase III that stays near $7–15M must use a surrogate or composite endpoint.
- That raises the chance that "success" will not show the mortality effect the model values.
- That risk belongs in `p_success` or adoption, not in cost. I note it below but do not double-count it.

**Not affected by this critique:** delivery, procurement and adverse-event costs. These are separate parameter-map items, so no change is made here.

**Model structure:**
- SROI = Benefit × p_success / all_in_cost.
- Benefit is fixed at $OP 53.46B, so SROI = 21.384×10⁹ / all_in_cost.
- SROI is exactly inversely proportional to cost. The relative change is Δ = 7M / C_new − 1.

## Plausible Range for `all_in_cost`

**Evidence base (from the verified critique):**
- Phase III median is about $19M.
- Anti-infective Phase III trials cost about $23M.
- TB-PRACTECAL cost €33.9M, roughly $37M. It is an atypical MDR trial whose cost included infrastructure.
- The full range is $7–221M.
- The Verifier accepted that a cheap oral adjunct using a routine-care endpoint could cost well below $20M.
- The "multiple trials" multiplier is UNGROUNDED.
- The endTB $60M figure is dropped as a trial cost.

**Independent sanity check: what endpoint can be powered?**
(Two-arm comparison, α = 0.05, 80% power.)

| Endpoint | Event rate, control → statin | n per arm | Total N | Cost at $1–2.5k per patient |
|---|---|---|---|---|
| All-cause mortality, 10% RRR (CG's effect) | 6.0% → 5.4% | ~2.3 million | ~4.7M | Infeasible at any budget |
| All-cause mortality, 25% RRR | 6.0% → 4.5% | ~3,460 | ~6,900 | $7–17M |
| Composite unfavourable outcome, 10% RRR | 20% → 18% | ~6,030 | ~12,000 | $12–30M |

**Implications:**
- No trial at any budget can confirm CG's assumed 10% mortality effect directly.
- A realistic pragmatic Phase III in drug-susceptible TB, powered on a composite endpoint, lands in roughly the **$10–30M** range for the trial alone.
- Add Phase IIc, guideline and dissemination costs (assumed $2–5M; no source available).

**Ranges used:**

| Case | all_in_cost | Basis |
|---|---|---|
| Optimistic | $5M | Embedded in an existing platform or network trial; low probability |
| CG base | $7M | Bottom of the reference class; possible but not typical |
| Low-cost pragmatic | $10M | Small pragmatic trial plus minimal add-ons |
| **Central** | **$15M** | Pragmatic composite-endpoint trial (~$10–12M) plus Phase IIc and adoption (~$3–5M) |
| Reference-class median | $23M | $19M Phase III median + ~$4M other |
| Upper single-trial | $38M | TB-PRACTECAL-like cost + ~$4M |
| Multiple trials | $60M | Ungrounded; bounding case only |

## Sensitivity Analysis

Base case: SROI = **3,055x**. Funding bar: 2,000x.

| all_in_cost | SROI | Δ vs base | Above 2,000x bar? |
|---|---|---|---|
| $5M | 4,277x | +40% | Yes |
| **$7M (base)** | **3,055x** | — | Yes |
| **$10.69M (break-even)** | **2,000x** | **−35%** | Threshold |
| $10M | 2,138x | −30% | Yes (barely) |
| **$15M (central)** | **1,426x** | **−53%** | **No** |
| $19M | 1,125x | −63% | No |
| $23M | 930x | −70% | No |
| $30M | 713x | −77% | No |
| $38M | 563x | −82% | No |
| $60M (ungrounded) | 356x | −88% | No |

The critique's 350–1,000x figure is reproduced at $20–60M. As the critique notes, that range relies on the reference-class costs. It also relies, at the top, on the ungrounded multiple-trial case.

**Probabilistic central estimate**
- Assume all_in_cost is lognormal, median $15M, 90% CI about $7–33M (σ = 0.48).
- P(all_in_cost < $10.69M), i.e. still clearing the bar, is about **24%**.
- SROI at expected cost (E[C] = $16.8M) is about **1,270x**.
- E[SROI], the expectation of the ratio, is about **1,600x**. It is higher because 1/C is convex.
- Either convention gives a central estimate of roughly **1,300–1,600x**, a change of about −48% to −58%.

**Joint with the Thread 1 endpoint interaction (illustrative only)**
- The effects are multiplicative, not additive.
- Example: cost $15M and p_success 0.40 → 0.30, reflecting surrogate-endpoint risk. SROI = 1,069x, a change of −65%.
- I report this only to show how the effects compound. The `p_success` adjustment belongs to Thread 1.

## Bottom-Line Impact

**Replacing $7M with a reference-class-informed all-in cost reduces SROI by roughly 30–80%** for plausible single-trial costs of $10–38M. The **central estimate is about −53% (≈1,400x; 1,300–1,600x under different aggregation conventions).** The optimistic tail is +40% if the work is embedded in a platform trial.

The grant falls below CG's 2,000x bar whenever all_in_cost exceeds about **$10.7M**. That is only ~53% above CG's figure and at the low end of even a pragmatic-trial budget.

## Materiality Verdict

**YES.**
- The central and most plausible values more than halve SROI.
- They also flip the estimate from above to below the 2,000x funding bar.
- Only about a quarter of my cost distribution keeps SROI above 2,000x.
- The verdict holds even after excluding the ungrounded multiple-trial multiplier and the endTB $60M figure.
- **Main caveat:** the central $15M rests on my per-patient cost assumptions ($1–2.5k) and the add-on cost ($2–5M). A CG cost breakdown would resolve this quickly.
- **Highest-value follow-up:** ask CG what endpoint and sample size its Phase III budget assumes.

## Code

```python
import numpy as np
from scipy.stats import norm

# --- CG model (exact formula chain) ---
P = dict(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=1e5, speedup_years=1,
         all_in_cost=7e6, p_success=0.40)

def sroi(**kw):
    p = {**P, **kw}
    eligible = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    deaths = eligible * p['adult_uptake'] * p['baseline_mortality'] * p['relative_reduction']
    benefit = deaths * p['speedup_years'] * p['dalys_per_death'] * p['op_per_daly']
    return benefit / p['all_in_cost'] * p['p_success']

base = sroi()                                             # 3054.9
breakeven = sroi() * P['all_in_cost'] / 2000              # $10.69M
for c in [5e6, 7e6, 10e6, 15e6, 19e6, 23e6, 30e6, 38e6, 60e6]:
    s = sroi(all_in_cost=c)
    print(f"${c/1e6:>4.0f}M  SROI={s:7.0f}x  Δ={s/base-1:+.0%}")

# --- Sample size check (two proportions, alpha=.05, power=.8) ---
def n_per_arm(p1, p2, z=1.96 + 0.8416):
    return z**2 * (p1*(1-p1) + p2*(1-p2)) / (p1 - p2)**2
print(n_per_arm(0.06, 0.054), n_per_arm(0.06, 0.045), n_per_arm(0.20, 0.18))
# ~2.34M, ~3,460, ~6,030 per arm

# --- Lognormal cost uncertainty ---
med, hi = 15e6, 33e6
sigma = np.log(hi/med) / 1.645                            # 0.479
E_cost = med * np.exp(sigma**2/2)                         # $16.8M
print("SROI at E[cost]:", sroi(all_in_cost=E_cost))       # ~1,271x
print("E[SROI]:", sroi(all_in_cost=med) * np.exp(sigma**2/2))   # ~1,599x
print("P(cost<breakeven):", norm.cdf(np.log(breakeven/med)/sigma))  # ~0.24

# --- Joint illustrative (Thread 1 interaction) ---
print(sroi(all_in_cost=15e6, p_success=0.30))             # ~1,069x
```

--- Critique: The speedup benefit and the all-in cost come from different counterfactuals. Every coherent framing gives roughly 10–20x higher SROI. ---

# CRITIQUE: The speedup benefit and the all-in cost come from different counterfactuals. Coherent framings give roughly 4–22x higher SROI.

## 1. Reproducing the base case

From the CEA formula chain:

- eligible = 5,500,000 × 0.98^(8−8) = 5,500,000
- treated = 5,500,000 × 0.60 = 3,300,000
- deaths averted per year = 3,300,000 × 0.06 × 0.10 = **19,800**
- DALYs = 19,800 × 1 yr × 27 = **534,600**
- Benefit = 534,600 × $OP 100,000 = **$OP 53.46B**
- SROI = 53.46B / 7M × 0.40 = **3,055x**. This matches the published figure of about 3,000x.

## 2. Formalising the critique

Let B_t be the expected annual mortality benefit in year t after adoption, and C_t be the all-in cost stream.

| Counterfactual | Incremental benefit | Incremental cost | Ratio |
|---|---|---|---|
| "Never happens" without the grant | PV_B | PV_C | PV_B/PV_C |
| Pure 1-year time-shift | PV_B·(1−δ) | PV_C·(1−δ), where δ = 1/(1+r) | **PV_B/PV_C** |
| Any mixture of the two | weighted sum | weighted sum | **PV_B/PV_C** |
| **BOTEC as built** | B_0 × 1 year | full C (time-shift benefit, "never" cost) | B_0/C |

The algebra confirms the critique. The BOTEC pairs a time-shift benefit (one year) with a "never" cost (the full $7M), and no single counterfactual produces that pairing.

Under a pure time-shift, the full cost is only *delayed*, not avoided. The incremental cost is therefore C·r/(1+r), and at the BOTEC's own r = 0 it is zero.

The confirmation the critique asked for is provided by the formula chain: `benefit = deaths/yr × speedup_years × ...` divided by `all_in_cost`. The inconsistency is real.

All other parameters (p_success, relative_reduction, uptake, mortality, DALYs) scale both framings equally, so they cancel out of the multiple. The multiple is:

**Multiple = [Σ_k f_k · g^k / (1+r)^(8+k)] / [PV_C / C]**

where:
- g = 0.98 is the continued case decline,
- f_k is the uptake ramp fraction in year k,
- k runs over the benefit horizon H.

## 3. Parameter mapping

| Parameter | Location | Current | Role in this critique |
|---|---|---|---|
| speedup_years | benefit formula | 1 | Replaced by PV benefit-years under a coherent framing |
| all_in_cost | SROI denominator | $7M, undiscounted | Replaced by PV_C. The timing factor PV_C/C is new. |
| discount rate | implicit | 0 | New parameter: 0%, 4%, or 6% |
| years_to_adoption | decline exponent | 8 | Now also sets the discount delay 1/(1+r)^8 |
| decline_per_year | eligible | 0.02 | Tested both as continuing after adoption and stopping |
| benefit horizon H | not in model | ∞ / implicit 1 yr | New parameter: 5, 10, 20 years, or ∞. Captures obsolescence, e.g. new 4-month regimens. |
| adoption ramp | not in model | step to 60% | New: none, or linear over 5 years |
| displacement s_alt | not in model | 0 | New: opportunity-cost SROI of the 95.5% non-CG dollars |

## 4. Plausible ranges

- **r: 0% / 4% / 6%.** 0% is the BOTEC's own convention. 4% is a standard social rate. 6% adds a hedge for obsolescence and catastrophic risk.
- **H: 5 / 10 / 20 years / ∞.** Shorter horizons reflect regimen change, such as 4-month HPMZ, or uncertainty about a statin class or dose effect (ROSETTA was null on culture conversion).
- **PV_C/C: 0.82–1.0.** 0.875 assumes costs spread evenly over years 0–7 at 4%. 1.0 assumes all costs up front.
- **Ramp:** none, or linear 20%→100% over 5 years.
- **s_alt: 0 / 2,000x / 3,055x.** These correspond to free money, the CG funding bar, and money as good as the BOTEC estimate.

## 5. Sensitivity results

**Base:** BOTEC SROI 3,055x, multiple 1.0.

### Single-factor: horizon and discount rate
Settings: decline continues, no ramp, no displacement, PV_C/C at an even spread.

| r | H | PV benefit-yrs | PV_C/C | Multiple | Coherent SROI | Δ vs BOTEC |
|---|---|---|---|---|---|---|
| 0% | 10 | 9.15 | 1.00 | 9.1x | 27,900x | +815% |
| 0% | 20 | 16.6 | 1.00 | 16.6x | 50,800x | +1,560% |
| 0% | ∞ | → ∞ | 1.00 | unbounded | — | — |
| 4% | 5 | 3.26 | 0.875 | 3.7x | 11,400x | +272% |
| 4% | 10 | 5.67 | 0.875 | 6.5x | 19,800x | +548% |
| 4% | 20 | 8.81 | 0.875 | 10.1x | 30,700x | +906% |
| **4%** | **∞** | **12.67** | **0.875** | **14.5x** | **44,200x** | **+1,347%** |
| 4% | ∞, no post-adoption decline | 19.0 | 0.875 | 21.7x | 66,300x | +2,071% |
| 6% | ∞ | 8.31 | 0.823 | 10.1x | 30,900x | +910% |

### Additional factors applied to the central case (r = 4%, H = ∞)
- 5-year linear uptake ramp: multiple 12.9x → **39,400x** (−11% vs central).
- Costs all up front (PV_C/C = 1): multiple 12.7x → **38,700x** (−12%).
- Displacement, s_alt = 2,000x: subtract 2,000 × 0.955 = 1,910 → **42,300x** (−4%).
- Displacement, s_alt = 3,055x: subtract 2,918 → **41,300x** (−7%).

### Joint scenarios
- **Moderate pessimistic** (r = 4%, H = 20, ramp, s_alt = 3,055): **23,000x** (+654% vs BOTEC).
- **Strong pessimistic** (r = 6%, H = 10, ramp, s_alt = 3,055): **9,500x** (+212%).
- **Extreme pessimistic** (r = 6%, H = 5, ramp, s_alt = 3,055): **2,780x** (−9% vs BOTEC). This is still above the 2,000x bar.
- **Optimistic** (r = 4%, H = ∞, no decline after adoption, no ramp, no displacement): **66,300x** (+2,071%).

### Interactions
Horizon, discount, ramp, and cost timing combine multiplicatively, through the numerator and the denominator. Displacement is subtractive, so its proportional bite grows as the other factors push the coherent SROI down.

### Break-even
The coherent framing equals the BOTEC when PV benefit-years ≈ PV_C/C ≈ 0.85–1.0. That works out to roughly **1.2 years of effective benefit at r = 4%**. This is consistent with the critique's claim of "about 1.5–2 years". Only implausibly short horizons combined with high discounting and displacement get there.

## 6. Bottom line

**BOTTOM-LINE IMPACT:** Correcting the counterfactual mismatch raises SROI from 3,055x to roughly **11,000–66,000x** (Δ = +270% to +2,070%) across plausible horizons and discount rates. The central estimate is about **40,000–44,000x (≈13–14x)** at r = 4% with an unbounded horizon. Under strong joint pessimism it falls to roughly 2,800–9,500x (−9% to +210%).

I recommend reporting this as an illustrative range, not a point estimate. Under r = 0, the BOTEC's own convention, the multiple is simply the effective benefit horizon in years, so the result depends almost entirely on H.

**MATERIALITY VERDICT: YES** for the estimate itself, which changes by multiples. It is **NO for the funding decision**. The direction is upward, and even the extreme pessimistic case (≈2,780x) stays above the 2,000x bar.

Two caveats:
1. **Displacement could matter far more than modelled here.** If other funders' dollars would otherwise fund TB research comparable to this project (s_alt ≈ 40,000x), the attributable value collapses toward CG's own share. That is an attribution question, separate from this critique.
2. **Upstream critiques compress the level, not the multiple.** Critiques of p_success and relative_reduction scale both framings equally.

## 7. Code

```python
import numpy as np

# ---- Base BOTEC (CEA formula chain) ----
P = dict(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=1e5, speedup_years=1,
         all_in_cost=7e6, p_success=0.40)

def botec(p):
    elig = p['eligible_people_at_8y']*(1-p['decline_per_year'])**(p['years_to_adoption']-8)
    deaths = elig*p['adult_uptake']*p['baseline_mortality']*p['relative_reduction']
    ben = deaths*p['speedup_years']*p['dalys_per_death']*p['op_per_daly']
    return ben/p['all_in_cost']*p['p_success']

BASE = botec(P)   # 3054.86

# ---- Coherent PV_B/PV_C framing ----
def ramp(k, years=5):
    return min(1.0, (k+1)/years) if years else 1.0

def coherent(r=0.04, H=None, g=0.98, ramp_years=0, cost_timing='even',
             s_alt=0.0, other_share=0.955, T=8, Hmax=2000):
    H = Hmax if H is None else H
    ks = np.arange(H)
    ben_yrs = sum(ramp(k, ramp_years)*g**k/(1+r)**(T+k) for k in ks)
    if cost_timing == 'even':      # costs spread evenly over years 0..T-1
        fC = np.mean([(1+r)**-t for t in range(T)])
    else:                          # all costs up front
        fC = 1.0
    mult = ben_yrs/fC
    return mult, BASE*mult - s_alt*other_share

cases = {
 'r0 H10':            dict(r=0, H=10),
 'r0 H20':            dict(r=0, H=20),
 'r4 H5':             dict(H=5),
 'r4 H10':            dict(H=10),
 'r4 H20':            dict(H=20),
 'r4 Hinf (central)': dict(),
 'r4 Hinf no decline':dict(g=1.0),
 'r6 Hinf':           dict(r=0.06),
 'central+ramp':      dict(ramp_years=5),
 'central upfront C': dict(cost_timing='upfront'),
 'central s_alt2000': dict(s_alt=2000),
 'central s_alt3055': dict(s_alt=BASE),
 'mod pess':          dict(H=20, ramp_years=5, s_alt=BASE),
 'strong pess':       dict(r=0.06, H=10, ramp_years=5, s_alt=BASE),
 'extreme pess':      dict(r=0.06, H=5, ramp_years=5, s_alt=BASE),
}
print(f"BOTEC base SROI: {BASE:,.0f}")
for name, kw in cases.items():
    m, s = coherent(**kw)
    print(f"{name:22s} multiple={m:6.2f}  SROI={s:8,.0f}  Δ={100*(s/BASE-1):+7.0f}%")
```

**Simplifications:**
- Benefits are counted as a discrete annual stream starting at year 8. The pre-adoption case decline is unchanged; the 2% decline either continues after adoption or stops.
- The cost timing is assumed, because the $7M is not broken down.
- Displacement is modelled as a flat per-dollar opportunity cost on the 95.5% of costs borne by non-CG funders.
- All other CEA parameters cancel out of the multiple and are held at their CEA values.

--- Critique: The funding landscape for a generic-statin TB program makes "never" a live branch. The speedup is a poor proxy for the grant's real counterfactual. ---

# Impact Assessment: Counterfactual Branches ("Never" / Delay / Redundant) for the TB-Statin Grant

## Summary

Treating `speedup_years` as an expected value over three branches (redundant, delayed, never) moves the SROI anywhere from about **−80% to +520%**.

- The direction depends on two inputs that have not been quantified: whether ATORTUB is the same trial as the Coefficient Giving (CG) grant or a competitor, and how likely the "never" branch is.
- The SROI falls below the 2,000× bar if the expected speedup is under **0.65 years**.
- The "20× higher SROI" claim does not hold under a consistent attribution rule.

## Parameter Mapping

| Parameter | Location | Current value | Role in this critique |
|---|---|---|---|
| `speedup_years` | Benefit multiplier | 1 | **Primary.** Should be E[years of benefit gained] = Σ (branch probability × years gained). SROI is linear in it. |
| `all_in_cost` | SROI denominator | $7,000,000 | **Secondary.** The "20×" claim swaps this for CG's ~$320k. |
| `p_success` | SROI multiplier | 0.40 | **Secondary.** The ROSETTA null result plausibly lowers it. |
| `decline_per_year` | New use | 0.02 | Governs the benefit stream in the "never" branch. |
| Implicit discount rate | Not in model | 0 | Becomes material once multi-year horizons are credited. |

## Plausible Ranges

**Branch structure.** Expected speedup is:

E[speedup] = q_red × 0 + q_delay × k + q_never × S(H)

where S(H) is the sum of 0.98^t for t from 0 to H−1. This is the number of incidence-weighted benefit-years gained if, without the grant, the trial is never run and benefits accrue over a horizon of H years.

| Input | Range | Basis |
|---|---|---|
| q_red (redundant) | 0.1–0.6 | ATORTUB is a registered Phase IIC trial. If it is the same trial as the CG grant, or an adequately funded competitor, q_red rises steeply. Not yet resolved. |
| k (delay years if not redundant) | 0.5–2 | A real Phase II pipeline exists (NIAID, EDCTP, Wellcome), so long delays are less likely. |
| q_never | 0–0.3 | No Phase III funder was found and generics have no commercial sponsor. Phase II funding does exist, and the ROSETTA null result lowers class appetite. Ungrounded either way. |
| H (horizon if "never") | 10–20 years | Before supersession by new regimens or HDTs. This is an assumption. |
| p_success | 0.30–0.40 | ROSETTA null result. Judgment call. |

## Sensitivity Analysis

**Base case:** 19,800 deaths averted per year; benefit $OP 53.46B; **SROI 3,055×**.

### Deterministic speedup

| `speedup_years` | SROI | Δ |
|---|---|---|
| 0 (fully redundant) | 0× | −100% |
| 0.3 | 916× | −70% |
| 0.5 | 1,527× | −50% |
| **0.655 (breakeven)** | **2,000×** | **−35%** |
| 2 | 6,110× | +100% |
| 3 | 9,165× | +200% |

### Expected-value scenarios (undiscounted)

| Scenario | q_red / q_delay (k) / q_never (H) | E[speedup] | SROI | Δ |
|---|---|---|---|---|
| Redundancy-dominant (ATORTUB ≈ same trial) | 0.6 / 0.4 (0.5) / 0 | 0.20 | 611× | −80% |
| Mild pessimistic | 0.5 / 0.45 (1) / 0.05 (10) | 0.91 | 2,772× | −9% |
| Central (illustrative) | 0.25 / 0.6 (1.5) / 0.15 (15) | 2.86 | 8,739× | +186% |
| Optimistic | 0.1 / 0.6 (2) / 0.3 (20) | 6.19 | 18,897× | +519% |

### Joint scenarios with ROSETTA-adjusted `p_success` = 0.30

- Redundancy-dominant: 458× (−85%).
- Central: 6,554× (+115%).
- The effects are **multiplicative**: SROI ∝ E[speedup] × p_success.

### Discounting check (4%/yr from grant date, applied consistently)

- Base: 2,232× (−27%).
- Central: 5,432×. That is +78% vs. the undiscounted base and +143% vs. the discounted base.
- Discounting cuts the "never" branch's contribution most. The undiscounted optimistic figures overstate it.

### The "20×" claim

- 7,000,000 / 320,000 = 21.9×, which implies an SROI of about 66,800×.
- This credits CG with the full counterfactual benefit while dividing only by its own cost. That double-counts the other $6.68M of funders, who are also necessary.
- Under any consistent rule (CG share of costs paired with the same share of benefits, as CG states it does at ~4.5%/4.5%), the ratio equals the all-in SROI and does not change.
- Leverage only exists if CG's grant causes the downstream $6.68M to be spent. That is what the q_never branch already captures through E[speedup]. It is not a separate 20× multiplier.
- **Drop the 20× figure.**

## Bottom Line

**This critique could move cost-effectiveness by −80% to +520%, i.e., from about 611× to 18,900×.**

- The sign depends on whether ATORTUB duplicates the CG trial (strongly down) or whether no Phase III would otherwise happen (strongly up).
- The central illustrative estimate is about +190% undiscounted, or about +80% with 4% discounting.
- This should not be read as a point estimate because q_never is unquantified.

## Materiality Verdict

**YES** for magnitude, with an uncertain direction.

- Every plausible scenario moves SROI by well over 10%.
- The redundancy branch alone takes the grant below the 2,000× bar. The breakeven E[speedup] is 0.655 years.
- **Priority action:** check ATORTUB against the CG grant (registry ID, PI, sites, arms). That single fact shifts the range more than any other input.

## Code

```python
import numpy as np

P = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
         all_in_cost=7_000_000, p_success=0.40)

def sroi(p, speedup=None, cost=None, ps=None):
    elig = p['eligible_people_at_8y']*(1-p['decline_per_year'])**(p['years_to_adoption']-8)
    deaths = elig*p['adult_uptake']*p['baseline_mortality']*p['relative_reduction']
    s = p['speedup_years'] if speedup is None else speedup
    benefit = deaths*s*p['dalys_per_death']*p['op_per_daly']
    return benefit/(cost or p['all_in_cost'])*(ps or p['p_success'])

base = sroi(P); print(f"base {base:,.0f}x")                 # 3,055x
print("breakeven speedup", 2000/base)                         # 0.655

def S(H, d=0.02, r=0.0, start=0):
    t = np.arange(H)
    return np.sum((1-d)**t/(1+r)**(t+start))

def E_speed(q_red, q_del, k, q_nev, H, r=0.0):
    disc8 = (1+r)**-8
    return q_del*k*disc8 + q_nev*S(H, r=r)*disc8

for s in [0, .3, .5, 2, 3]:
    v = sroi(P, s); print(s, f"{v:,.0f}", f"{v/base-1:+.0%}")

scen = {"redundant":(0.6,0.4,0.5,0.0,10), "mild_pess":(0.5,0.45,1,0.05,10),
        "central":(0.25,0.6,1.5,0.15,15), "optimistic":(0.1,0.6,2,0.3,20)}
for n,a in scen.items():
    e = E_speed(*a); v = sroi(P, e); v3 = sroi(P, e, ps=0.30)
    print(n, round(e,2), f"{v:,.0f} ({v/base-1:+.0%})", f"p=.3: {v3:,.0f} ({v3/base-1:+.0%})")

# discounting at 4%
bd = sroi(P, 1.04**-8); cd = sroi(P, E_speed(*scen["central"], r=0.04))
print(f"disc base {bd:,.0f}  disc central {cd:,.0f} ({cd/base-1:+.0%} vs undisc base, {cd/bd-1:+.0%} vs disc base)")

# '20x' claim (invalid attribution)
print(f"CG-cost-only SROI {sroi(P, cost=320_000):,.0f}x, ratio {7e6/320e3:.1f}")
```

--- Critique: Discounting quantified properly with an S-curve ramp and discounted costs. The net effect is about −20% to −31%, not the benefit-only −21% to −35%. ---

# Impact Assessment: Discounting with an S-Curve Adoption Ramp and Discounted Costs

## Bottom line

**This critique could reduce SROI by about 20% to 37%. The central estimate is about −26% (≈2,270x vs. 3,055x) at a 4% rate with a 6-year ramp and costs spread over years 1–8.** It crosses the 2,000x bar only in pessimistic corners:

- a 10-year ramp at 5%;
- front-loaded costs at a rate of 4% or more;
- applying the CEA's own 2%/yr case decline to the later benefit years at 5%.

The result depends more on assumed timing than on the discount rate. All timing assumptions are illustrative, not taken from the CEA.

---

## Parameter mapping

| Parameter | Model key | Current value | Role |
|---|---|---|---|
| Discount rate | *(implicit)* | 0% ("No time discounting") | Primary. New term. |
| Timing of benefits | `years_to_adoption`, `speedup_years` | Step adoption at year 8; 1 year of benefit | Sets where discounting bites |
| Timing of costs | `all_in_cost` | $7M, undated | Sets the cost-side offset |
| Case decline | `decline_per_year` (via exponent `years_to_adoption − 8`) | 0.02, exponent 0 | Interaction: later benefits mean fewer cases |
| Bar | — | 2,000x | Threshold = 2,000 / 3,055 → **−34.5%** |

**Base case (reproduced):** 5.5M × 0.6 × 0.06 × 0.10 = 19,800 deaths/yr. Then 19,800 × 1 × 27 × $OP100k = $OP 53.46B. Then 53.46B / 7M × 0.4 = **3,054.9x**.

**A structural point the critique implies but doesn't state.** In the speedup framing, shifting the whole adoption curve 1 year earlier yields exactly 1 year of full uptake, undiscounted, whatever the curve's shape. The S-curve ramp therefore has **zero effect at r = 0**. It matters only through discounting, because it pushes the benefit centroid later. This avoids double-counting with the adult_uptake/ramp thread, but only if that thread does not also apply a ramp penalty in the speedup framing.

---

## Model specification (stated simplifications)

**Benefit timing.** The ramp is linear from T0 = 8.5 over L years, which approximates the S-curve. The 1-year shift is spread over a year. Benefit time is therefore t = T0 + U₁·L + U₂, with U₁, U₂ ~ Uniform(0,1).

- Centroid = T0 + L/2 + 0.5, which is 12 years for L = 6 and 14 for L = 10.
- This spec reproduces the critique's stated L = 10 factors (0.57 / 0.51) to within 0.01.
- The closed form uses continuous discounting with δ = ln(1+r):

  F_B = e^(−δ·T0) · (1−e^(−δL))/(δL) · (1−e^(−δ))/δ

**Cost timing.** The default is uniform spend at the end of years 1–8, discounted annually. Two alternatives are tested:
- front-loaded (all at t = 0, i.e. benefit-only discounting);
- back-loaded (years 4–8, Phase-III-heavy).

**Net effect.** Net factor = F_B / F_C, applied multiplicatively to SROI.

**Out of scope.** Stage-probability-weighting of costs (the critique's "Critique 4" link) is not modeled. It changes expected cost, which is a different parameter.

---

## Sensitivity results

### A. Core critique scenarios (uniform costs, years 1–8)

| r | F_C | L=6: F_B | L=6: Net Δ | L=6: SROI | L=10: F_B | L=10: Net Δ | L=10: SROI |
|---|---|---|---|---|---|---|---|
| 0% (CG) | 1.000 | 1.000 | 0% | 3,055x | 1.000 | 0% | 3,055x |
| 3% | 0.877 | 0.702 | **−20.0%** | 2,445x | 0.664 | −24.4% | 2,310x |
| 4% | 0.842 | 0.626 | **−25.6%** | 2,273x | 0.581 | −30.9% | 2,110x |
| 5% | 0.808 | 0.559 | **−30.8%** | 2,113x | 0.510 | **−36.9%** | **1,929x ✗** |

These confirm the critique's −20 / −27 / −31% figures (mine: −20.0 / −25.6 / −30.8%). They also confirm the verifier's ≈1,900x for L = 10 at 5%.

### B. Cost-timing sensitivity (L = 6)

| r | Front-loaded (t=0; benefit-only) | Uniform yrs 1–8 | Back-loaded yrs 4–8 |
|---|---|---|---|
| 3% | −29.8% (2,145x) | −20.0% (2,445x) | −16.2% (2,560x) |
| 4% | −37.4% (**1,913x ✗**) | −25.6% (2,273x) | −20.9% (2,416x) |
| 5% | −44.1% (**1,707x ✗**) | −30.8% (2,113x) | −25.3% (2,282x) |

**Discrepancy with the critique's framing.** With this ramp, benefit-only discounting gives −30% to −44%, not the critique's −21% to −35%. The critique's benefit-only range matches a point benefit at about year 8–9, which is the CEA-literal step timing, not the ramp. So the critique's "benefit-only" and "net" figures rest on different timing assumptions. Whether costs are discounted moves the result by 10–13 percentage points. This is as large as the gap between 3% and 5%.

### C. CEA-literal timing (step adoption, benefit at year 8, uniform costs)

| r | F_B | Net Δ | SROI |
|---|---|---|---|
| 3% | 0.789 | −10.0% | 2,749x |
| 4% | 0.731 | −13.2% | 2,652x |
| 5% | 0.677 | −16.2% | 2,559x |

This is the optimistic end. It takes the CEA's stated 8-year timeline at face value.

### D. Interaction: continuing the 2%/yr case decline into the ramp years (uniform costs)

The CEA's formula already scales eligible cases by (0.98)^(t−8). If benefits are moved to years 9–16 for discounting, consistency suggests also applying the decline.

| r | L=6: Δ | L=6: SROI | L=10: Δ | L=10: SROI |
|---|---|---|---|---|
| 3% | −26.0% | 2,261x | −32.6% | 2,060x |
| 4% | −31.2% | 2,103x | −38.3% | **1,885x ✗** |
| 5% | −36.0% | **1,956x ✗** | −43.5% | **1,726x ✗** |

The effect is multiplicative. It is the same as raising the benefit discount rate by about 2 points. This is the critique's most important omission, though it depends on the decline persisting.

### Optimistic direction

- At r = 0, which is CG's current convention, the impact is 0%.
- No scenario increases SROI. Discounting can only shrink the ratio, because benefits always come later than costs.
- The smallest plausible penalty is −10% (CEA-literal timing, 3%).

---

## Materiality verdict: **BORDERLINE**

**Against a 25% materiality line: YES at 4–5%** (−26% to −31% in the central ramp case) and **NO at 3%** (−20%).

**Against the decision-relevant bar (2,000x, i.e. −34.5%): NO in the central case** (2,273x). It is **YES only in these scenarios:**
- L = 10 at 5%;
- front-loaded costs at 4% or more;
- the decline-adjusted cases at 4–5%.

**Key uncertainties to resolve, which dominate the rate choice:**
1. **The actual adoption timeline.** The benefit centroid at year 8 vs. year 12 is worth about 15 percentage points.
2. **When the $7M is spent and by whom.** CG's ~4.5% share is near t = 0, while the Phase III money comes later.
3. **Whether CG's 2,000x bar is defined in discounted terms (UNGROUNDED).** If the bar's comparators, such as GiveDirectly, are also undiscounted, applying discounting to this BOTEC alone would bias the comparison against it.

I agree with the critique that framing (speedup vs. counterfactual PV) is likely first-order and discounting second-order. That claim was not quantified here.

---

## Code

```python
import math

# ---- CEA base (from parameter summary) ----
P = dict(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=1e5, speedup_years=1,
         all_in_cost=7e6, p_success=0.40)

def sroi(p):
    elig = p['eligible_people_at_8y']*(1-p['decline_per_year'])**(p['years_to_adoption']-8)
    deaths = elig*p['adult_uptake']*p['baseline_mortality']*p['relative_reduction']
    ben = deaths*p['speedup_years']*p['dalys_per_death']*p['op_per_daly']
    return ben/p['all_in_cost']*p['p_success']

BASE = sroi(P)   # 3054.857

# ---- benefit discount factor: linear ramp from T0 over L yrs, 1-yr shift ----
# t = T0 + U1*L + U2 ; E[exp(-d t)] closed form (product of uniform MGFs)
def FB(r, T0=8.5, L=6, decline=0.0, ref=8):
    d = math.log(1+r)
    g = -math.log(1-decline) if decline else 0.0
    k = d + g
    if k == 0:
        return 1.0
    f = math.exp(-k*T0) * (1-math.exp(-k*L))/(k*L) * (1-math.exp(-k))/k
    return f * math.exp(g*ref)          # re-normalise decline to year 8

def FB_point(r, t=8):
    return (1+r)**-t

# ---- cost discount factors ----
def FC_uniform(r, years=range(1, 9)):
    ys = list(years)
    return sum((1+r)**-t for t in ys)/len(ys)

FC_front = lambda r: 1.0
FC_back = lambda r: FC_uniform(r, range(4, 9))

def report(label, fb, fc):
    net = fb/fc
    print(f"{label:38s} FB={fb:.3f} FC={fc:.3f} net={net:.3f} "
          f"d={100*(net-1):6.1f}% SROI={BASE*net:7.0f}x "
          f"{'BELOW BAR' if BASE*net < 2000 else ''}")

print(f"Base SROI = {BASE:.1f}x; bar threshold = {100*(2000/BASE-1):.1f}%")
for r in (0.03, 0.04, 0.05):
    for L in (6, 10):
        report(f"A r={r:.0%} L={L} uniform", FB(r, L=L), FC_uniform(r))
    report(f"B r={r:.0%} L=6 front-loaded", FB(r), FC_front(r))
    report(f"B r={r:.0%} L=6 back-loaded", FB(r), FC_back(r))
    report(f"C r={r:.0%} step@yr8 uniform", FB_point(r), FC_uniform(r))
    for L in (6, 10):
        report(f"D r={r:.0%} L={L} +2% decline", FB(r, L=L, decline=0.02), FC_uniform(r))
```

The outputs match the tables above. They were checked by hand against the closed form, for example F_B(4%, L=6) = 0.7165 × 0.8911 × 0.9807 = 0.626.

--- Critique: Probability weighting is asymmetric between benefit and cost. ---

# CRITIQUE: Probability weighting is asymmetric between benefit and cost

## Parameter mapping

The model computes `SROI = benefit / all_in_cost × p_success`. Benefits are probability-weighted by `p_success` (0.40). The denominator `all_in_cost` ($7,000,000) appears to enter as a nominal, unweighted sum. If that is right, the denominator assumes all downstream spending happens with certainty, while the numerator is discounted for failure.

Affected parameters:

| Parameter | Location | Current value | Role |
|---|---|---|---|
| `all_in_cost` | denominator of SROI | $7,000,000 | Should become the *expected* cost |
| `p_success` | multiplier on benefit | 0.40 | Unchanged on the benefit side. Its decomposition (P(IIc) × P(III)) sets the cost-gating probabilities. |
| *New, implicit:* `ungated_cost` (U) | part of the $7M | not specified (≥ $0.32M) | Phase IIc spend, incurred regardless of outcome |
| *New, implicit:* `s` = P(Phase III is actually run) | not in model | implicitly 1.0 | Gates Phase III cost |
| *New, implicit:* `post_cost` (guideline change, dissemination) | part of the $7M | not specified | Gated by `p_success` itself, since it only happens after Phase III succeeds |

Structural note: the correction factor is `7 / E[cost]`. It does not depend on any benefit-side parameter (uptake, mortality, relative reduction, DALYs). It is therefore **purely multiplicative** with every other critique in the thread.

## Plausible range

| Parameter | Current | Plausible range | Basis |
|---|---|---|---|
| s, the gating probability on Phase III cost | 1.0 (implicit) | 0.5 – 1.0; central about 0.65 | If p_success = P(IIc) × P(III) = 0.40 and the two are roughly symmetric, P(IIc) ≈ 0.63. Late Phase III failure still incurs full cost, so s = P(IIc), not 0.40. The critique's s = 0.4 lower bound is structurally implausible: it would mean Phase III cost is incurred only when Phase III succeeds. |
| U, ungated (Phase IIc) cost | $0.32M (critique's assumption) | $0.32M – $2.0M | $0.32M matches CG's ~4.5% share of $7M, which may be CG's grant rather than the full Phase IIc cost. A larger U shrinks the effect. |
| post_cost, guideline/dissemination | inside $7M | $0 – $1.0M | Gated at 0.40, so it adds some upside even when s is high. |
| Whether $7M is already expected cost | unknown | binary | The verifier could not inspect the cost build-up. If it is already expected, the effect is 0. |

## Sensitivity analysis

**Base case:** benefit = $OP 53.46B. SROI = 53.46e9 × 0.40 / 7.0e6 = **3,055x**. Funding bar is 2,000x.

**Simple two-tier model, E[cost] = U + s × (7 − U)**

| U \ s | 1.0 | 0.9 | 0.8 | 0.7 | 0.6 | 0.5 | 0.4 |
|---|---|---|---|---|---|---|---|
| $0.32M | 3,055 (0%) | 3,377 (+11%) | 3,775 (+24%) | 4,280 (+40%) | 4,941 (+62%) | 5,842 (+91%) | 7,147 (+134%) |
| $1.0M | 3,055 (0%) | 3,341 (+9%) | 3,687 (+21%) | 4,112 (+35%) | 4,649 (+52%) | 5,348 (+75%) | 6,290 (+106%) |
| $2.0M | 3,055 (0%) | 3,290 (+8%) | 3,564 (+17%) | 3,888 (+27%) | 4,277 (+40%) | 4,752 (+56%) | 5,346 (+75%) |

**Three-tier structured model, E[cost] = U + P(IIc) × C_III + p_success × C_post**

| Scenario | U | C_III | C_post | P(IIc) | E[cost] | SROI | Δ |
|---|---|---|---|---|---|---|---|
| Null: $7M already expected, or s = 1 with no gating | — | — | — | — | $7.00M | 3,055x | 0% |
| Low effect (most spend unavoidable) | 0.32 | 6.18 | 0.50 | 0.85 | $5.77M | 3,704x | +21% |
| Central A | 0.32 | 5.68 | 1.00 | 0.65 | $4.41M | 4,847x | +59% |
| Central B (larger Phase IIc) | 1.00 | 5.00 | 1.00 | 0.65 | $4.65M | 4,599x | +51% |
| High effect | 0.32 | 5.68 | 1.00 | 0.50 | $3.56M | 6,007x | +97% |
| Critique's extreme (s = 0.4) | 0.32 | 6.68 | 0 | 0.40 | $2.99M | 7,147x | +134% |

**Both directions.** This critique can only raise SROI or leave it unchanged. There is no pessimistic reading: if the $7M is already an expected value, the correct adjustment is zero, not negative. The "pessimistic" bound is therefore Δ = 0%.

**Joint/interaction.** The factor is multiplicative with all benefit-side critiques. It also interacts with the separate all_in_cost critique. If a realistic TB Phase III costs far more than $7M (e.g., $20–40M), the nominal-versus-expected distinction scales with it. For example, with C_III = $30M and P(IIc) = 0.65, expected cost is about $20M rather than $31M, a factor of about 1.5x. So this correction partly cushions any upward cost revision.

**Decision relevance.** The base case (3,055x) is already above the 2,000x bar, so this upward correction cannot change the decision by itself. It matters as a buffer: other critiques can cut SROI by 1 − 2000/(3055 × r) before it falls below the bar. Without this correction that tolerance is 35%. With a factor of 1.2 it is 45%; with 1.5 it is 56%; with 2.0 it is 67%.

## Bottom-line impact

If the $7M is a nominal sum, the critique would raise SROI by roughly +20% to +60% (central about +50%, giving about 4,600x instead of 3,055x). The structurally implausible s = 0.4 extreme gives +134%. If the $7M is already an expected cost, the effect is 0%. Weighting by an unknown, roughly even chance that it is nominal, the unconditional central estimate is about +25%.

## Materiality verdict

**BORDERLINE.**

- **Magnitude:** above any typical ~10% threshold if the cost is nominal.
- **Direction:** favorable only. Since the base case already clears 2,000x, this cannot flip the funding decision.
- **Main value:** it offsets downward critiques (relative_reduction, uptake, all_in_cost) when the thread's effects are combined.
- **Resolution:** a single inspection of how CG built the $7M settles it. That check should come before this factor is applied in any combined estimate.

## Code

```python
# Baseline replication of CG TB-statins BOTEC
p = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
         all_in_cost=7_000_000, p_success=0.40)

def benefit(p):
    elig = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    deaths = elig * p['adult_uptake'] * p['baseline_mortality'] * p['relative_reduction']
    return deaths * p['speedup_years'] * p['dalys_per_death'] * p['op_per_daly']

def sroi(p, cost=None):
    return benefit(p) * p['p_success'] / (cost if cost is not None else p['all_in_cost'])

base = sroi(p)
print(f"Benefit {benefit(p):,.0f}  base SROI {base:,.0f}x")   # 53,460,000,000 ; 3,055x

# Two-tier expected cost: E[c] = U + s*(7M - U)
for U in (0.32e6, 1.0e6, 2.0e6):
    row = []
    for s in (1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4):
        ec = U + s * (p['all_in_cost'] - U)
        v = sroi(p, ec)
        row.append(f"s={s}: {v:,.0f}x ({v/base-1:+.0%})")
    print(f"U=${U/1e6:.2f}M | " + " | ".join(row))

# Three-tier: E[c] = U + P(IIc)*C_III + p_success*C_post
scen = {
    "low":       (0.32e6, 6.18e6, 0.5e6, 0.85),
    "central_A": (0.32e6, 5.68e6, 1.0e6, 0.65),
    "central_B": (1.00e6, 5.00e6, 1.0e6, 0.65),
    "high":      (0.32e6, 5.68e6, 1.0e6, 0.50),
    "extreme":   (0.32e6, 6.68e6, 0.0,   0.40),
}
for k, (U, C3, Cp, p2) in scen.items():
    ec = U + p2 * C3 + p['p_success'] * Cp
    v = sroi(p, ec)
    print(f"{k:10s} E[cost]=${ec/1e6:.2f}M  SROI={v:,.0f}x  Δ={v/base-1:+.0%}")

# Headroom for other critiques before SROI falls below the 2,000x bar
for r in (1.0, 1.2, 1.5, 2.0):
    print(f"factor {r}: tolerable cut = {1 - 2000/(base*r):.0%}")
```

--- Critique: A 1-year speedup of trial results does not necessarily become a 1-year speedup of adoption, in either direction. ---

# Impact Assessment: Speedup Pass-Through to Adoption

**CRITIQUE:** A 1-year speedup of trial results does not necessarily become a 1-year speedup of adoption, in either direction.

---

## Parameter Mapping

| Parameter | Location in model | Current value | Role |
|---|---|---|---|
| `speedup_years` (primary) | Benefit term: `deaths/yr × speedup_years × dalys_per_death × op_per_daly` | 1.0 | Enters SROI linearly. SROI ∝ speedup_years. |
| `years_to_adoption` (secondary) | Decline exponent `(1−0.02)^(years_to_adoption−8)` | 8 | Shifting adoption timing changes the eligible pool by about 2% per year. This is second-order. |
| Implicit discount rate (interaction only) | Not in model; formula notes "No time discounting" | 0 | Determines whether the shape of the adoption curve matters. That analysis belongs to Thread 3. |

The critique decomposes the effective speedup as:

**s_eff = 1 − (WHO-stage absorption) − (national/procurement absorption) + (lost-cycle gain) ± (trial-date definition ambiguity)**

---

## Plausible Range

**WHO-stage absorption: 0 to 0.15 yr.**
- Basis: WHO's guideline group acted roughly 1–2 months after data were shared for two recent TB regimens, including BPaLM on interim data.
- So the WHO stage passes through nearly the full speedup.
- I widen the range slightly because a "generic adjunct" may get lower priority than sponsor-backed regimens.

**National/procurement absorption: 0 to 0.40 yr (mode about 0.1).**
- Basis: the verifier found no source quantifying these lags.
- The wide range reflects the absence of evidence, not evidence of absorption.

**Lost-cycle gain: 0, or occasionally +0.25 to +0.75 yr.**
- I treat this as a low-probability event (about 15%), because the verifier rated the lumpy-cycle claim UNGROUNDED for TB.

**Composite `speedup_years`:**
- Plausible band: **[0.45, 1.25]**
- Central estimate: about **0.83–0.95**

---

## Sensitivity Analysis

**Base case**
- Deaths averted per year: 19,800
- DALYs credited: 534,600
- Benefit: $OP 5.346 × 10¹⁰
- SROI: 5.346e10 / 7e6 × 0.40 = **3,055x**

Because SROI is linear in speedup, **SROI = 3,055 × s**.

**Break-even against the 2,000x bar:** s* = 2,000 / 3,055 = **0.655 yr**. This matches the critique's stated threshold.

| `speedup_years` | Scenario | SROI | Δ vs base |
|---|---|---|---|
| 0.45 | Joint pessimistic (WHO 0.10 + national 0.35 + date 0.10 absorbed) | 1,375x | −55% (below bar) |
| 0.50 | National stage slack-bound half the year | 1,527x | −50% (below bar) |
| 0.655 | Break-even | 2,000x | −35% |
| 0.75 | Moderate national absorption | 2,291x | −25% |
| 0.85 | Mild absorption (evidence-favoured) | 2,597x | −15% |
| 0.95 | WHO lag only (about 2 months... partially absorbed) | 2,902x | −5% |
| 1.00 | Base (full pass-through) | 3,055x | 0% |
| 1.25 | One lost cycle avoided (optimistic) | 3,819x | +25% |
| 1.50 | Large lost-cycle gain (not supported for TB) | 4,582x | +50% |

**Individual vs joint effects**
- The absorption components are **additive in s**. Because SROI is linear in s, they are also additive in SROI.
- There is no multiplicative compounding within this critique.
- Joint effects with other threads are multiplicative: relative_reduction, p_success, adult_uptake and all_in_cost all multiply with s in the formula.

**Distributional view**

Because SROI is linear in s, **expected SROI depends only on E[s]**. The shape of the distribution affects risk, not the expected value.

Under the stated distributions (see code):

- **E[s]** = 1 − 0.075 − 0.167 + 0.15 × 0.5 = **0.833**
- **E[SROI]** ≈ **2,546x** (−17%)
- **P(s < 0.655)** ≈ 0.85 × 0.156 ≈ **13%**, computed analytically below. The Monte Carlo reproduces this within sampling error.

**Second-order effects**
- **Decline exponent:** moving adoption one year earlier raises eligible patients by about 2%, which raises SROI by about 2% per year of shift. This is negligible relative to the band above.
- **Adoption-curve shape:** with no discounting and a fixed eventual plateau, a time-shift of a ramp-up curve yields exactly s × plateau benefit. So ramp shape does **not** affect this result at r = 0. It matters only once Thread 3 introduces discounting.

---

## Bottom-Line Impact

**This critique moves SROI by roughly −55% to +25% (1,375x–3,819x) across the plausible band, with a central estimate of −5% to −17% (about 2,550–2,900x).** The evidence leans toward a speedup near 1 year at the WHO stage. The downside risk comes almost entirely from untested national and procurement lags.

---

## Materiality Verdict: **BORDERLINE**

- The central estimate stays above the 2,000x bar.
- About 13% of the probability mass under my assumed distribution falls below the bar. That figure depends on an unevidenced national-lag distribution.
- The critique's main contribution is therefore methodological: replace the point value with a band, roughly [0.5, 1.25] with mean about 0.85.
- Combined with any other thread that cuts SROI by 20% or more, a speedup of 0.85 would push the estimate below the bar. Example: 3,055 × 0.85 × 0.75 ≈ 1,950x.
- Two items would resolve most of the uncertainty:
  - Defining the trial-result date as either "data available to WHO" or "published".
  - Finding any precedent for national adoption lags of adjunct or host-directed TB therapies.

---

## Code

```python
import numpy as np

# --- GiveWell/CG model, replicated exactly ---
P = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=100_000, speedup_years=1.0,
         all_in_cost=7_000_000, p_success=0.40)

def sroi(**kw):
    p = {**P, **kw}
    eligible = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    deaths = eligible * p['adult_uptake'] * p['baseline_mortality'] * p['relative_reduction']
    benefit = deaths * p['speedup_years'] * p['dalys_per_death'] * p['op_per_daly']
    return benefit / p['all_in_cost'] * p['p_success']

base = sroi()
print(f"Base SROI: {base:,.0f}x")                       # 3,055x
print(f"Break-even speedup: {2000/base:.3f} yr")        # 0.655

# --- One-way sensitivity on speedup_years ---
for s in [0.45, 0.5, 0.655, 0.75, 0.85, 0.95, 1.0, 1.25, 1.5]:
    v = sroi(speedup_years=s)
    print(f"s={s:5.3f}  SROI={v:7,.0f}x  Δ={100*(v/base-1):+6.1f}%")

# --- Second-order: earlier adoption enlarges eligible pool (decline exponent) ---
print(f"Adoption at yr 7 vs 8: Δ={100*(sroi(years_to_adoption=7)/base-1):+.1f}%")  # ~+2%

# --- Monte Carlo on decomposed effective speedup ---
rng = np.random.default_rng(0)
N = 1_000_000
who_abs   = rng.uniform(0, 0.15, N)                    # WHO GDG lag absorption
nat_abs   = rng.triangular(0, 0.10, 0.40, N)           # national/procurement (unevidenced)
cycle     = (rng.random(N) < 0.15) * rng.uniform(0.25, 0.75, N)  # lost-cycle gain (ungrounded for TB)
s_eff = 1 - who_abs - nat_abs + cycle

sroi_draws = base * s_eff        # SROI is linear in speedup
print(f"E[s]={s_eff.mean():.3f}  E[SROI]={sroi_draws.mean():,.0f}x  "
      f"P5/P50/P95 = {np.percentile(sroi_draws,[5,50,95]).round(0)}")
print(f"P(SROI < 2000x) = {(sroi_draws < 2000).mean():.3f}")   # ≈ 0.13

# Analytic check of P(s<0.655) with no cycle gain:
# P = (1/0.15)∫_0^0.15 (0.055+w)^2/0.12 dw = ((0.205^3-0.055^3)/3)/(0.15*0.12) ≈ 0.156
# overall ≈ 0.85 * 0.156 ≈ 0.13 (with a cycle gain, s cannot fall below 0.655)
```

--- Critique: Post-TB lung disease morbidity is likely the largest unvalued channel (~50–60k central, wide range) ---

# CRITIQUE: Post-TB lung disease morbidity is the largest unvalued channel

## Summary

Measured consistently, the central estimate (+23–26% SROI) sits right at the materiality threshold. The critique compared a probability-weighted 55k against the 134k threshold, which counts DALYs before weighting by p_success. On a like-for-like basis, the central estimate is borderline. The critique's two other claims also change under the numbers:

- **ROSETTA:** Adjusting for ROSETTA's null lung result roughly halves the central impact.
- **Discounting:** Consistent discounting does not shrink this channel relative to the mortality term.

## Parameter Mapping

The model has no cell for this channel. I added a new term, structured in parallel with the mortality term:

`morb_DALYs = treated × B_morb × r_morb × speedup_years`, then `SROI_add = morb_DALYs × op_per_daly / all_in_cost × p_morb`

| Parameter | Location | Current value | Proposed central |
|---|---|---|---|
| treated = eligible_people_at_8y × (0.98)^0 × adult_uptake | existing | 3,300,000 | unchanged |
| B_morb (post-TB morbidity DALYs per treated patient) | **new** | 0 (implicit) | 0.75 |
| r_morb (relative reduction in post-TB morbidity) | **new** | 0 | 0.05 |
| p_morb (probability weight) | p_success, or a new parameter | 0.40 | 0.40–0.45 |
| speedup_years, op_per_daly, all_in_cost | existing | 1, 100,000, $7M | unchanged |

## Plausible Ranges

- **B_morb:**
  - Current value is 0. Plausible range is **0.45–1.5**.
  - Basis: about 30% of patients are impaired, with a disability weight of 0.1–0.2 over 15–25 years. That gives 1.5–5 DALYs per affected patient, or 0.45–1.5 per treated patient.
  - Menzies's 5.8 post-TB DALYs per case is a ceiling. It includes post-TB excess mortality, which overlaps with Critique 2, so I use it only as a double-counting stress test.
- **r_morb:**
  - Current value is 0. Plausible range is **0.02–0.15**, with 0.05 central.
  - The "lung signal" premise is unverified, and ROSETTA (x-ray, spirometry, PET-CT) was null. So I also report an evidence-adjusted r_eff = r × P(lung effect real | success), with P in the range 0.3–0.7 and 0.5 central. This gives r_eff ≈ 2.5% at central.
- **p_morb:**
  - Range is **0.40–0.45**.
  - The 0.45 figure assumes a "lung benefit without mortality benefit still gets adopted" branch. ROSETTA makes that branch less credible, so 0.40 is the defensible central value.

## Sensitivity Analysis

### Baseline

Taken from the model:

| Output | Value |
|---|---|
| Deaths averted per year | 19,800 |
| DALYs credited | 534,600 (213,840 after the 0.40 probability weight) |
| SROI | **3,055x** |

### Unit check on materiality

- The threshold of 133,650 is exactly 25% × 534,600. It is therefore defined on DALYs *before* applying p_success.
- The critique's "55k vs 134k" compares a weighted number with an unweighted threshold.
- Like-for-like:
  - Unweighted, the new term is 123,750 vs 133,650, which is 23.1% of the mortality term.
  - Weighted, it is 49,500–55,700 vs a weighted threshold of 53,460, which is 23–26%.
- **Both sides of the comparison are about 25%: borderline, not clearly below.**

### Individual and joint variation (p_morb = 0.40; multiply the increment by 1.125 for p = 0.45)

| B_morb \ r_morb | 0.02 | 0.05 | 0.15 |
|---|---|---|---|
| 0.45 | 3,225x (+5.6%) | 3,479x (+13.9%) | 4,328x (+41.7%) |
| **0.75** | 3,338x (+9.3%) | **3,762x (+23.1%)** | 5,176x (+69.4%) |
| 1.5 | 3,621x (+18.5%) | 4,469x (+46.3%) | 7,298x (+138.9%) |

The effects are **multiplicative**: the term is a product of B, r and p. So the joint extremes span roughly two orders of magnitude, from +5.6% to +139%, or up to +156% at p = 0.45.

### Other scenarios

| Scenario | Morbidity DALYs (weighted) | SROI | Δ vs base |
|---|---|---|---|
| Critique central (B 0.75, r 5%, p 0.45) | 55,688 | 3,850x | +26.0% |
| Central at p = 0.40 | 49,500 | 3,762x | +23.1% |
| **ROSETTA-adjusted central** (r_eff 2.5%, p 0.40) | 24,750 | 3,409x | **+11.6%** |
| ROSETTA-adjusted range (P = 0.3–0.7) | 14,850–34,650 | 3,267–3,550x | +6.9% to +16.2% |
| Critique low (B 0.4, r 2%, p 0.40) | 10,560 | 3,206x | +4.9% |
| Critique high (B 1.5, r 15%, p 0.45) | 334,125 | 7,828x | +156% |
| Menzies stress test (B 5.8, r 5%, p 0.45), double-counts with Critique 2 | 430,650 | 9,207x | +201% |

### Pessimistic direction (offset)

- Each death averted creates a survivor who carries post-TB morbidity.
- Calculation: 19,800 extra survivors × 0.75 DALYs ≈ 14,850 DALYs, about **−2.8%** of the mortality term.
  - This applies only if the 27 DALYs per death is treated as fully healthy life expectancy.
- This offset is the only way this channel can lower SROI. Net central effect: about **+20%**.

### Discounting

Report both versions:

- **Undiscounted (CG convention):** as in the tables above.
- **Discounted at 4% (morbidity over ~20 years after treatment):** the morbidity term falls to about 0.68× its value.
  - The 27 DALYs per death are *also* a long tail. Their discount factor at 4% over 27 years is about 0.605.
  - Relative to the mortality term, the morbidity channel therefore rises slightly: from +23.1% to about +26%.
- If impairment is back-loaded (worsening with age), the factor drops to about 0.5, giving about +19%.
- **The critique's claim that this channel is "partly an artifact of no-discounting" does not hold in relative terms.** Discounting lowers absolute SROI for both terms (the full-model effect belongs to Thread 3). It does not selectively penalize morbidity.

## Bottom-Line Impact

Adding post-TB morbidity raises SROI by about **+12% (evidence-adjusted for ROSETTA) to +26% (critique central)**, with a full range of **+5% to +156%**.

- The direction is upward only, apart from a roughly −3% survivor-morbidity offset.
- The figure of +200% or more from Menzies baselines double-counts with Critique 2.

## Materiality Verdict

**BORDERLINE.**

- The critique's central estimate (+23–26%) sits at the 25% threshold once units are consistent. The original "below threshold" conclusion relied on a weighted-versus-unweighted comparison.
- The evidence-adjusted central estimate (+12%) is below the threshold. The threshold is crossed only if B ≥ about 0.8 with r = 5%, or if r ≥ about 5.4% at B = 0.75.
- Decision relevance is limited. Base SROI (3,055x) already clears the 2,000x bar, and this channel can only push it further up. It matters as a **robustness buffer** if Thread 1 cuts the mortality relative_reduction.
  - Example: if relative_reduction falls to 5%, base SROI is about 1,527x. The central morbidity term (+707x) would restore it to about 2,234x.

## Code

```python
base = dict(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=1e5, speedup_years=1,
            all_in_cost=7e6, p_success=0.40)

def model(p, B_morb=0.0, r_morb=0.0, p_morb=None, survivor_offset=False):
    elig = p['eligible_people_at_8y']*(1-p['decline_per_year'])**(p['years_to_adoption']-8)
    treated = elig*p['adult_uptake']
    deaths = treated*p['baseline_mortality']*p['relative_reduction']
    mort_dalys = deaths*p['speedup_years']*p['dalys_per_death']
    morb_dalys = treated*B_morb*r_morb*p['speedup_years']
    if survivor_offset:
        mort_dalys -= deaths*B_morb*p['speedup_years']
    pm = p['p_success'] if p_morb is None else p_morb
    sroi = (mort_dalys*p['p_success'] + morb_dalys*pm)*p['op_per_daly']/p['all_in_cost']
    return sroi, morb_dalys, morb_dalys*pm

s0, _, _ = model(base)
print(f"base SROI {s0:.0f}; threshold DALYs {0.25*534600:.0f}")

for B in (0.45, 0.75, 1.5):
    for r in (0.02, 0.05, 0.15):
        s, u, w = model(base, B, r)
        print(B, r, f"{s:.0f}x {100*(s/s0-1):+.1f}% weighted={w:.0f}")

scen = {'crit_central': (0.75, .05, .45), 'central_p40': (0.75, .05, .40),
        'rosetta_adj': (0.75, .025, .40), 'ros_lo': (0.75, .015, .40), 'ros_hi': (0.75, .035, .40),
        'low': (0.4, .02, .40), 'high': (1.5, .15, .45), 'menzies': (5.8, .05, .45)}
for k, (B, r, pm) in scen.items():
    s, u, w = model(base, B, r, pm)
    print(k, f"{s:.0f}x {100*(s/s0-1):+.1f}% weighted DALYs={w:.0f}")

s, _, _ = model(base, 0.75, 0.05, 0.40, survivor_offset=True)
print("net with survivor offset", f"{100*(s/s0-1):+.1f}%")

# Discounting: annuity factor per DALY, relative comparison
af = lambda r, n: (1-(1+r)**-n)/r/n
f_morb, f_mort = af(0.04, 20), af(0.04, 27)
print(f"disc factors morb {f_morb:.3f} mort {f_mort:.3f}; "
      f"relative increment {23.1*f_morb/f_mort:.1f}%")

# Robustness buffer if Thread 1 halves relative_reduction
b2 = dict(base, relative_reduction=0.05)
print(model(b2)[0], model(b2, 0.75, 0.05)[0])
```

--- Critique: Post-treatment excess mortality (~40–50k central) and a related sign-reversing adjustment ---

# Impact Assessment: Post-treatment excess mortality and a sign-reversing adjustment

## Critique

Post-treatment excess mortality (upside channel) netted against a life-expectancy adjustment (downside channel).

---

## Parameter Mapping

The CG model is linear in DALYs. SROI = (DALYs × op_per_daly / all_in_cost) × p_success. Both channels therefore act on the DALY term.

| Parameter | Location | Current value | Channel |
|---|---|---|---|
| `dalys_per_death` | Benefit line | 27 | **(b) Downside.** Survivors' excess mortality lowers the years gained per on-treatment death averted. |
| New term: post-treatment DALYs | Added to the DALY total | 0 (implicit) | **(a) Upside.** = treated × excess_mort × resp_share × effect × DALYs_per_late_death |
| `p_success` | SROI line | 0.40 | Applied to both channels. The upside effect is conditional on success, like `relative_reduction`. |
| `eligible_people_at_8y` × `adult_uptake` | Treated cohort | 3.3M | Base population for the upside channel |

### Unit inconsistency in the critique

The 534,600 DALY baseline is **pre-p_success**. You can confirm this from 19,800 × 27 = 534,600, with p applied only at the SROI step.

The critique compares its "~45k after weighting" upside against the pre-p 535k downside base. The correctly comparable upside figure is **~99k pre-p**. That is +18.5% of the DALY total, not ~+8%.

The critique's "nearly cancel" conclusion depends on this mismatch. Once corrected, the central net is **mildly positive**, not zero.

---

## Plausible Ranges

| Input | Critique value | Plausible range | Basis |
|---|---|---|---|
| 10-yr cumulative excess mortality among survivors | 0.10 | 0.05–0.15 | Romanowski 2019 pooled SMR ≈ 2.9. LMIC adult 10-yr background mortality is roughly 5–8%, so excess ≈ 1.9 × background ≈ 9–15%. Cerqueira-Silva supports a real pool. |
| Respiratory/lung share of excess | 0.40 | 0.0–0.5 | **UNGROUNDED.** No source supplied. The lower bound of 0 covers "statin does not touch this pool." |
| Effect of 6-month atorvastatin on that pool (given success) | 0.05 | 0–0.05 (extreme 0.10) | **UNGROUNDED.** Capped at half of `relative_reduction` for the base range, because a 6-month adjunct acting on deaths up to 10 years later should plausibly be weaker than its on-treatment effect. |
| DALYs per late death | 15 | 10–20 | Older age at death plus residual excess risk |
| LE reduction applied to `dalys_per_death` | 5–10% | 5–10% (extended 5–25%) | See derivation below. |

### Derivation of the extended downside range

Under Gompertz mortality (b ≈ 0.085), a lifelong hazard multiplier of 2.9 is equivalent to aging ln(2.9)/0.085 ≈ 12.5 years. That cuts remaining LE at age ~40 by about 30%.

Excess risk decays over time, though. An effective lifetime multiplier of ~1.5 is equivalent to aging about 5 years, a ~10–12% LE cut. In addition, 27 DALYs may already be below standard LE.

On that basis I treat 5–10% as central and 25% as a pessimistic bound.

---

## Sensitivity Analysis

Base case: **534,600 DALYs, SROI 3,055x.** The 2,000x bar requires a −34.5% drop.

### Individual channels

| Scenario | DALYs (pre-p) | SROI | Δ |
|---|---|---|---|
| Upside, critique central (0.10 × 0.4 × 0.05 × 15) | +99,000 → 633,600 | 3,621x | **+18.5%** |
| Upside, as critique stated it (45k, unit-mismatched) | +45,000 → 579,600 | 3,312x | +8.4% |
| Upside, low (share or effect = 0) | +0 | 3,055x | 0% |
| Upside, plausible high (0.15 × 0.5 × 0.05 × 15) | +185,625 | 4,116x | +34.7% |
| Upside, extreme (0.15 × 0.5 × 0.10 × 20) | +495,000 | 5,883x | +92.6% |
| Downside, −5% (`dalys_per_death` = 25.65) | 507,870 | 2,902x | −5.0% |
| Downside, −10% (24.3) | 481,140 | 2,749x | −10.0% |
| Downside, −25% (20.25), extended | 400,950 | 2,291x | −25.0% |

### Joint scenarios

The two channels are additive in DALY space. The downside multiplies only the existing on-treatment term, and the upside's 15 DALYs per death already reflect survivors' shortened LE.

| Scenario | SROI | Δ |
|---|---|---|
| Critique central, corrected (upside 99k, downside −7.5%) | 3,391x | **+11.0%** |
| Pessimistic within critique bounds (upside 0, downside −10%) | 2,749x | −10.0% |
| Pessimistic extended (upside 0, downside −25%) | 2,291x | −25.0% |
| Optimistic plausible (upside high 185.6k, downside −5%) | 3,963x | +29.7% |
| **De-duplicated with Critique 1** (upside → 0 because Menzies post-TB DALYs already include post-TB mortality; downside only) | 2,749–2,902x | **−5% to −10%** (extended −25%) |

**Break-even check.** Downside alone would need `dalys_per_death` ≈ 17.7, a 34.5% LE cut, to reach the 2,000x bar. That is outside even the extended range. No scenario crosses the bar.

---

## Bottom-Line Impact

**Standalone, this critique moves SROI by roughly −25% to +35%, with a corrected central estimate of about +11%. The critique's "net ≈ 0" rests on a pre-p vs post-p unit mismatch.**

Once the upside is merged into Critique 1 to avoid double-counting, the residual effect of this critique is the life-expectancy adjustment: **−5% to −10%** (extended to −25%). That is about 3,055x → 2,750–2,900x. It does not approach the 2,000x bar.

---

## Materiality Verdict

**BORDERLINE.** No materiality threshold was given in the thread spec, so I assumed a ±10% change or a bar crossing.

- **Against materiality:**
  - The de-duplicated residual (−5% to −10%) sits at the edge of the threshold.
  - No plausible scenario crosses 2,000x.
- **For materiality:**
  - The standalone range exceeds ±10% in both directions.
  - The extended downside (−25%) is material.

**Recommendations:**
1. Fold the upside into Critique 1's post-TB DALY term.
2. Carry the LE adjustment as a −5% to −10% haircut on `dalys_per_death` that applies to *all* mortality critiques.
3. Do not report a net-zero outcome.

---

## Code

```python
# Reproduces CG TB-statins BOTEC and tests critique scenarios.
base = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
            all_in_cost=7_000_000, p_success=0.40)

def model(p, extra_dalys=0.0, le_cut=0.0):
    eligible = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    treated = eligible * p['adult_uptake']
    deaths = treated * p['baseline_mortality'] * p['relative_reduction']
    dalys = deaths * p['speedup_years'] * p['dalys_per_death'] * (1 - le_cut) + extra_dalys
    sroi = dalys * p['op_per_daly'] / p['all_in_cost'] * p['p_success']
    return treated, dalys, sroi

treated, D0, S0 = model(base)
print(f"Base: treated={treated:,.0f} DALYs={D0:,.0f} SROI={S0:,.0f}x")

def upside(excess, share, effect, dpd):          # pre-p_success DALYs (speedup_years=1)
    return treated * excess * share * effect * dpd

scen = {
 "Upside central (corrected 99k)": (upside(.10,.4,.05,15), 0),
 "Upside as stated (45k)":         (45_000, 0),
 "Upside plausible high":          (upside(.15,.5,.05,15), 0),
 "Upside extreme":                 (upside(.15,.5,.10,20), 0),
 "Downside -5%":                   (0, .05),
 "Downside -10%":                  (0, .10),
 "Downside -25% (extended)":       (0, .25),
 "Joint central":                  (upside(.10,.4,.05,15), .075),
 "Joint pessimistic (bounds)":     (0, .10),
 "Joint pessimistic (extended)":   (0, .25),
 "Joint optimistic plausible":     (upside(.15,.5,.05,15), .05),
}
for k, (ex, cut) in scen.items():
    _, D, S = model(base, ex, cut)
    print(f"{k:32s} DALYs={D:>9,.0f}  SROI={S:>6,.0f}x  Δ={100*(S/S0-1):+6.1f}%")

# Break-even dalys_per_death for 2,000x bar
print("Break-even dalys_per_death:", round(27 * 2000 / S0, 1))

# Gompertz LE shift for hazard multiplier k (b=0.085)
import math
for k in (1.5, 2.9):
    print(f"SMR {k}: equivalent age shift {math.log(k)/0.085:.1f} yrs")
```

**Output:**

```
Base: treated=3,300,000 DALYs=534,600 SROI=3,055x
Upside central (corrected 99k)   DALYs=  633,600  SROI= 3,621x  Δ= +18.5%
Upside as stated (45k)           DALYs=  579,600  SROI= 3,312x  Δ=  +8.4%
Upside plausible high            DALYs=  720,225  SROI= 4,116x  Δ= +34.7%
Upside extreme                   DALYs=1,029,600  SROI= 5,883x  Δ= +92.6%
Downside -5%                     DALYs=  507,870  SROI= 2,902x  Δ=  -5.0%
Downside -10%                    DALYs=  481,140  SROI= 2,749x  Δ= -10.0%
Downside -25% (extended)         DALYs=  400,950  SROI= 2,291x  Δ= -25.0%
Joint central                    DALYs=  593,505  SROI= 3,391x  Δ= +11.0%
Joint pessimistic (bounds)       DALYs=  481,140  SROI= 2,749x  Δ= -10.0%
Joint pessimistic (extended)     DALYs=  400,950  SROI= 2,291x  Δ= -25.0%
Joint optimistic plausible       DALYs=  693,495  SROI= 3,963x  Δ= +29.7%
Break-even dalys_per_death: 17.7
SMR 1.5: equivalent age shift 4.8 yrs
SMR 2.9: equivalent age shift 12.5 yrs
```

---

## Simplifications

- **Model scope.** I used CG's actual formula chain. The new upside term is an additive DALY line that I constructed, because the model has none.
- **Timing.** No time discounting, consistent with CG. Post-treatment deaths fall 1–10 years after treatment, so discounting (Thread 3) would shrink the upside channel more than the downside.
- **Shared multipliers.** p_success and speedup_years are applied identically to both channels. In practice, a 6-month statin effect on late deaths may have a lower success probability than the on-treatment endpoint. That would push the upside further toward zero.

--- Critique: Transmission benefit is small, with a bounded calculation (~10–30k central) ---

# CRITIQUE: Transmission benefit is small, with a bounded calculation (~10–30k central)

**Note on scope.** This critique proposes a new, additive benefit term. It does not modify an existing parameter. It belongs to the "new benefit terms" thread, where the model currently has implicit zeros for morbidity, post-treatment mortality, transmission and diagnostics. The label "post-TB lung disease" is a mislabel; that is a separate channel. The direction of the effect can only be zero or upward.

---

## PARAMETER MAPPING

| Parameter | Location in model | Current value | Role here |
|---|---|---|---|
| `transmission_DALYs` (new) | New term added to `benefit` | Implicit 0 | Primary |
| `treated` = eligible_people_at_8y × (1−decline)^(yta−8) × adult_uptake | Formula chain | 5.5M × 1 × 0.6 = **3.3M** | Base population for the new term |
| `speedup_years` | Benefit multiplier | 1 | Applies equally to the new term (one year of accelerated cohort) |
| `p_success` | SROI multiplier | 0.40 | Applies to the new term |
| `all_in_cost`, `op_per_daly` | SROI | $7M, 100,000 | Unchanged |

**Proposed new term (pre-p_success):**

transmission_DALYs = treated × secondary_cases × post_start_share × conversion_reduction × mapping_factor × DALYs_per_secondary × speedup_years

**Unit-reconciliation finding.** The critique's "~50k pre-p → ~20k after weighting" is consistent with the model:

- 3.3M × 0.5 × 0.003 × 10 = 49,500 DALYs before p_success.
- 49,500 × 0.4 = 19,800 after p_success.

The comparable figure in the model is 534,600 mortality DALYs before p_success. All percentage changes below are therefore computed as transmission_DALYs / 534,600.

---

## PLAUSIBLE RANGE

All inputs below are **UNGROUNDED** (Investigator inference). The Verifier confirmed only the qualitative claim that on-treatment infectiousness is short-lived and dominated by the pre-diagnosis window (PMC4015982, PMC9907102, PMC12054730).

| Input | Low | Central | High | Basis |
|---|---|---|---|---|
| Secondary disease cases per index case | 0.3 | 0.5 | 1.0 | Inference |
| Share of lifetime transmission after treatment start | 1% | 3% | 5% | Inference; directionally supported by Dowdy-type analyses |
| Reduction in that share from faster conversion | 10% | 15% | 20% | Inference |
| Net transmission reduction (share × reduction) | 0.1% | 0.3% (critique) / 0.45% (midpoints) | 1.0% | Derived |
| Conversion → infectiousness mapping factor | 0.25 | 0.5 | 1.0 | Critique's adjustment 1; culture conversion at week 8 is not equivalent to infectiousness |
| P(culture-conversion effect exists, given mortality "success") | 0.3 | 0.5 | 1.0 | ROSETTA found no conversion effect; the benefit may be lung-sparing rather than bactericidal |
| DALYs per secondary case | ~10 | 10 | ~10 | Held fixed: 6% case fatality × 27 DALYs ≈ 1.6, plus morbidity and onward chains. 10 is generous. |

---

## SENSITIVITY ANALYSIS

**Base case:** SROI = 53.46e9 / 7e6 × 0.4 = **3,055x**.

Each 1,000 pre-p transmission DALYs adds 1,000 × 100,000 / 7,000,000 × 0.4 = **+5.71x**.

| Scenario | Pre-p DALYs | Post-p DALYs | SROI | Δ |
|---|---|---|---|---|
| Zero (no conversion effect; ROSETTA-consistent) | 0 | 0 | 3,055x | 0% |
| All low (0.3 × 0.1% × 10) | 9,900 | 3,960 | 3,111x | +1.9% |
| Critique central, with both downward adjustments (×0.5 × 0.5) | 12,375 | 4,950 | 3,126x | +2.3% |
| Critique's suggested lowered central (~10k post-p) | 25,000 | 10,000 | 3,198x | +4.7% |
| **Critique central, unadjusted** (0.5 × 0.3% × 10) | **49,500** | **19,800** | **3,338x** | **+9.3%** |
| Midpoints, unadjusted (0.5 × 0.45% × 10) | 74,250 | 29,700 | 3,479x | +13.9% |
| All high jointly (1.0 × 1.0% × 10) | 330,000 | 132,000 | 4,941x | +61.7% |

**Pessimistic direction.** There is no plausible downside below the base case. The worst case is a zero transmission effect, which leaves SROI at 3,055x. A statin hepatotoxicity or adherence penalty could in principle prolong infectiousness, but that is negligible and belongs to Thread 1.

**Interactions.**

- The inputs are multiplicative within the term, so the tails compound.
- The joint-high case of +62% requires all three ungrounded inputs at their maxima simultaneously. That is implausible, and the evidence argues against it: diagnostic delay dominates transmission, and the adjunct does not shorten it.
- The new term is additive to the mortality benefit. It is correlated with `relative_reduction` only through the shared p_success.
- Applying p_success is appropriate, since there is no transmission benefit if the drug fails. However, the ROSETTA null means that a conversion effect is not implied even conditional on mortality success. This justifies the extra 0.3–1.0 factor.

**Approximate Monte Carlo** (independent uniform distributions on the ranges above, including both adjustment factors). The mean is ≈ 96k × 0.625 × 0.65 ≈ 39k pre-p DALYs (~+7%). The median is lower, around 20–25k (~+4–5%). The upper 95th percentile is roughly 100–130k (~+20–25%). These figures are analytic approximations and should be confirmed by running the code below.

---

## BOTTOM-LINE IMPACT

**Adding a transmission term would raise SROI by roughly 0% to +10%, with a central estimate of about +2–5% (3,055x → ~3,120–3,200x). An unadjusted central gives +9%, and a joint-extreme tail reaches +60%.** It cannot lower cost-effectiveness.

---

## MATERIALITY VERDICT

**NO.** It is borderline only if the unadjusted central of +9.3% is accepted against a ~10% threshold.

- The thread spec does not state an explicit threshold. Against a conventional ~10% threshold, the adjusted central is well below it.
- This is decision-irrelevant. The base case is already 3,055x against a 2,000x bar, and this term can only increase it.
- The critique's own recommendation is reasonable: lower the central to ~10k post-p (~25k pre-p) and set the floor at zero.
- If included, the term should be labeled UNGROUNDED, filed under the "new benefit terms" thread rather than "post-TB lung disease," and presented as a minor upside channel.

---

## CODE

```python
import numpy as np

# --- Base model (GiveWell/CG formula chain) ---
P = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
         all_in_cost=7_000_000, p_success=0.40)

def treated(p):
    elig = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    return elig * p['adult_uptake']

def sroi(p, tx_dalys_pre_p=0.0):
    deaths = treated(p) * p['baseline_mortality'] * p['relative_reduction']
    mort_dalys = deaths * p['speedup_years'] * p['dalys_per_death']
    benefit = (mort_dalys + tx_dalys_pre_p) * p['op_per_daly']
    return benefit / p['all_in_cost'] * p['p_success'], mort_dalys

base, mort_dalys = sroi(P)
print(f"Base SROI {base:,.0f}x; mortality DALYs {mort_dalys:,.0f}")  # 3,055x ; 534,600

def tx_dalys(p, sec, share, red, mapping=1.0, p_conv=1.0, dalys_per_case=10):
    return treated(p) * sec * share * red * mapping * p_conv * dalys_per_case * p['speedup_years']

scen = {
 "zero":                 0.0,
 "all_low":              tx_dalys(P, 0.3, 0.01, 0.10),
 "critique_adj":         treated(P)*0.5*0.003*10*0.5*0.5,
 "suggested_25k":        25_000,
 "critique_central":     treated(P)*0.5*0.003*10,
 "midpoints":            tx_dalys(P, 0.5, 0.03, 0.15),
 "all_high":             tx_dalys(P, 1.0, 0.05, 0.20),
}
for k, d in scen.items():
    s, _ = sroi(P, d)
    print(f"{k:18s} preP={d:>9,.0f} postP={d*P['p_success']:>9,.0f} "
          f"SROI={s:,.0f}x  Δ={(s/base-1)*100:+.1f}%")

# --- Monte Carlo ---
rng = np.random.default_rng(0); N = 200_000
d = tx_dalys(P, rng.uniform(0.3, 1.0, N), rng.uniform(0.01, 0.05, N),
             rng.uniform(0.10, 0.20, N), rng.uniform(0.25, 1.0, N),
             rng.uniform(0.3, 1.0, N))
pct = d / mort_dalys * 100
print("MC Δ% mean/median/p5/p95:", pct.mean().round(1), np.median(pct).round(1),
      np.percentile(pct, 5).round(1), np.percentile(pct, 95).round(1))
```

**Simplifications.**

- DALYs per secondary case are held fixed at 10. This is likely generous, since direct case-fatality DALYs are only about 1.6.
- No discounting, consistent with the CG model. Discounting would further shrink a benefit that accrues in later years.
- The uniform priors on ungrounded inputs are illustrative, not evidence-based.

--- Critique: The "lung benefit without mortality benefit" scenario is structurally less valuable than a simple p_success weighting implies ---

# CRITIQUE: The "lung benefit without mortality benefit" scenario is structurally less valuable than a simple p_success weighting implies

## Summary up front

This critique **does not change the current CEA at all (Δ = 0%)**, because the BOTEC values only mortality and has no lung channel. Its value is as a constraint on any future augmentation (Thread 4) that adds a lung or morbidity term.

Whether that constraint matters depends almost entirely on an unmodeled quantity, *m*: the conditional value of the lung benefit relative to the mortality benefit. Because *m* is unknown, I report results across a grid of *m* values rather than as a point estimate.

## PARAMETER MAPPING

| Parameter | Location | Current value | Role in this critique |
|---|---|---|---|
| `p_success` | Final multiplier in SROI | 0.40 | Weight on the "both phases succeed" branch, where the lung benefit is adopted along with the mortality benefit |
| `adult_uptake` | treated = eligible × uptake | 0.60 | Main-case uptake. The critique says the lung-only branch earns only a fraction *a* of this |
| *(new)* P(lung holds \| mortality fails), *P* | Not in model | implicit 0 | Probability of the lung-only branch |
| *(new)* lung-only adoption ratio, *a* | Not in model | implicit 0 | Lung-only uptake ÷ main uptake. The critique gives 0.10–0.20, which is **ungrounded** |
| *(new)* lung value ratio, *m* | Not in model; benefit chain counts mortality only | implicit 0 | Lung or morbidity $OP benefit per success ÷ mortality $OP benefit per success |

**Effective probability weight on a lung channel:**
- Naive weighting (full uptake in the lung-only branch): w_naive = 0.4 + 0.6·P
- Realistic weighting (adoption-discounted): w_real = 0.4 + 0.6·P·a

**Augmented SROI:** SROI = 7,637 × (0.4 + m · w), where 7,637 is the SROI before multiplying by p_success.

## PLAUSIBLE RANGE

- **P(lung holds | mortality fails): 0.3–0.5.** This is the critique's range. FEV1 is an accepted Phase 2 host-directed-therapy outcome (CC-11050/everolimus trial), so P is non-trivial. There is no direct evidence on its exact value.
- **a (lung-only adoption ratio): 0.10–0.20 per the critique, which is UNGROUNDED.** No evidence was found on how WHO guideline groups weigh lung-function surrogates. I also test a = 0.5 as an unfavourable-to-critique sensitivity.
- **m (lung value ratio): 0–1, tested at 0.1, 0.25, 0.5 and 1.0.** No basis exists in the CEA. Post-TB lung disease is a substantial burden in the literature, but the share a statin could avert is unknown. This is the dominant uncertainty.

## SENSITIVITY ANALYSIS

**Base case:** 19,800 deaths averted/yr, 534,600 DALYs, benefit $OP 53.46B, **SROI = 3,055x**. The funding bar is 2,000x.

**Check on the critique's arithmetic:**

| Quantity | P = 0.3 | P = 0.5 | Comment |
|---|---|---|---|
| w_naive | 0.58 | 0.70 | |
| w_real (a = 0.1–0.2) | 0.418–0.436 | 0.430–0.460 | The critique's "+0.02 to 0.06" is confirmed |
| w_naive / w_real | 1.33–1.39× | 1.52–1.63× | |

The critique says the naive weighting is "up to ~2×". That only holds if P ≳ 0.8 (with P = 1, w_naive = 1.0, a 2.5× ratio). **Within the critique's own P range, the overstatement is 1.3–1.6×, not 2×.**

**Gap between naive and realistic weighting:**

Δw = 0.6·P·(1−a), which ranges from 0.144 to 0.270.

As a share of baseline SROI, the gap is 2.5·m·Δw = **m × (36%–68%)**.

**Augmented SROI by lung value ratio (P 0.3–0.5, a 0.1–0.2):**

| m | SROI, realistic weighting | SROI, naive weighting | Overstatement avoided (% of base SROI) |
|---|---|---|---|
| 0 (current CEA) | 3,055x | 3,055x | 0% |
| 0.10 | 3,374x–3,407x (+10–12%) | 3,498x–3,590x (+15–18%) | 4–7% |
| 0.25 | 3,853x–3,933x (+26–29%) | 4,163x–4,391x (+36–44%) | 9–17% |
| 0.50 | 4,651x–4,812x (+52–58%) | 5,270x–5,728x (+73–88%) | 18–34% |
| 1.00 | 6,247x–6,569x (+104–115%) | 7,485x–8,401x (+145–175%) | 36–68% |

**Testing both directions:**
- **Pessimistic (a → 0, lung-only branch worthless):** the lung channel is weighted at 0.40 only. SROI = 3,055 × (1 + m), which is still ≥ baseline.
- **Optimistic (a = 0.5, P = 0.5):** w = 0.55, and the overstatement avoided is m × 37.5%.
- **No setting of these parameters lowers SROI below the current 3,055x.** The critique only caps upside from a channel the model does not yet include.

**Interactions:** The effects are multiplicative in P × a × m and additive with the existing mortality term.

There is one adjacent interaction worth flagging (Thread 7). If the current 40% `p_success` already counts some surrogate-only "successes" in which relative_reduction is actually 0, the mortality term is overstated by a factor of (1 − f), where f is that share. This is a separate critique, but it is the same definitional gap: "success" is undefined in the CEA.

## BOTTOM-LINE IMPACT

**On the current CEA, the impact is 0%, because there is no lung channel to reweight.**

If a lung or morbidity channel is added, adoption-discounting the lung-only branch reduces that channel's contribution by 25–40% compared with naive full-uptake weighting. That equals **m × 36–68% of baseline SROI**:
- roughly 4–7% if lung value is a tenth of mortality value
- roughly 9–17% at m = 0.25

The critique's "~2×" framing overstates the gap. It is 1.3–1.6× within its own P range.

## MATERIALITY VERDICT

**NO for the current model.** There is no change, and the direction is never downward from 3,055x, so there is no risk of crossing the 2,000x bar.

It becomes **BORDERLINE** as a guardrail on Thread 4. It matters only if a lung channel is added with m ≥ ~0.25. The key input, a, remains ungrounded.

The critique's own magnitude label of "small, not medium" is correct for the CEA as it stands.

## CODE

```python
import itertools
P = dict(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=1e5, speedup_years=1, all_in_cost=7e6, p_success=0.40)

def mortality_benefit(p):
    elig = p['eligible_people_at_8y']*(1-p['decline_per_year'])**(p['years_to_adoption']-8)
    deaths = elig*p['adult_uptake']*p['baseline_mortality']*p['relative_reduction']
    return deaths*p['speedup_years']*p['dalys_per_death']*p['op_per_daly']

base_unweighted = mortality_benefit(P)/P['all_in_cost']          # 7637
base = base_unweighted*P['p_success']                             # 3055
print(f"deaths/yr={mortality_benefit(P)/27/1e5:,.0f}  SROI={base:,.0f}x")

def sroi_aug(m, Pl, a, naive=False):
    ps = P['p_success']
    w = ps + (1-ps)*Pl*(1.0 if naive else a)
    return base_unweighted*(ps + m*w), w

for Pl in (0.3, 0.5):
    for a in (0.1, 0.2):
        _, wr = sroi_aug(1, Pl, a); _, wn = sroi_aug(1, Pl, a, naive=True)
        print(f"P={Pl} a={a}: w_real={wr:.3f} w_naive={wn:.3f} ratio={wn/wr:.2f}")

for m in (0, 0.1, 0.25, 0.5, 1.0):
    real = [sroi_aug(m,Pl,a)[0] for Pl,a in itertools.product((0.3,0.5),(0.1,0.2))]
    naiv = [sroi_aug(m,Pl,a,True)[0] for Pl in (0.3,0.5) for a in (0,)]
    gap = [(sroi_aug(m,Pl,a,True)[0]-sroi_aug(m,Pl,a)[0])/base
           for Pl,a in itertools.product((0.3,0.5),(0.1,0.2))]
    print(f"m={m}: real {min(real):,.0f}-{max(real):,.0f}x ({min(real)/base-1:+.0%} to {max(real)/base-1:+.0%}); "
          f"naive {min(naiv):,.0f}-{max(naiv):,.0f}x; gap {min(gap):.0%}-{max(gap):.0%} of base")
```

--- Critique: The sweat-based diagnostic carries real option value but is speculative (~10–30k central) ---

# Impact Assessment: The Sweat-Based Diagnostic's Option Value Is Real but Speculative

## Parameter Mapping

The current model has no parameter for the diagnostic. Its value is an implicit zero. Quantifying the critique therefore needs a new additive benefit term, plus a possible cost term in the denominator.

| Parameter | Location | Current value | Role |
|---|---|---|---|
| `diag_dalys_per_yr` (new) | additive benefit term | 0 (implicit) | Primary: the critique's 10–30k DALYs/yr |
| `speedup_years` | benefit multiplier | 1 | Years of diagnostic benefit credited to the grant, applied for consistency with the statin arm |
| `all_in_cost` | denominator | $7,000,000 | Whether diagnostic workstream cost sits inside the $7M is unknown |
| `p_success` | multiplier | 0.40 | Should not apply to the diagnostic term, which has its own ~5% P(adoption) built in |
| `op_per_daly` | conversion | 100,000 | Unchanged |

**Modified formula:**

SROI = [p_success × benefit_statin + diag_dalys_per_yr × speedup_years × op_per_daly] / (all_in_cost + diag_extra_cost)

**Simplifications:**
- The diagnostic is credited the same 1-year speedup as the statin arm. It is not credited "never happens otherwise," because about 100 diagnostics are in the pipeline and the 2026 WHO tongue-swab and near-point-of-care NAAT recommendations make the counterfactual a delay rather than a loss.
- No discounting, matching the model.
- The diagnostic term is treated as statistically independent of statin trial success.

## Plausible Range

**diag_dalys_per_yr.** This is UNGROUNDED, as the critique itself states. The components are:
- P(adoption): 2–10%, central 5%.
- Incremental cases beyond tongue-swab PCR: 50k–300k, central 200k.
- DALYs per additional case treated: 3–6, central 5. This is consistent with the model's 27 DALYs/death × roughly 20% untreated excess fatality.

Taking the product of the components:
- Low: 0.02 × 50k × 3 ≈ 3k
- Central (undiscounted): 0.05 × 200k × 5 = 50k
- High: 0.10 × 300k × 6 ≈ 180k

The critique's own discounted central range is 10–30k, with an outer range of 0–100k. The verified evidence (2026 WHO recommendations and crowding) pushes toward the low end. **Working range: 0 / 10k / 30k (central band), with 100k as an upper stress test.**

**diag_extra_cost.** This is unknown. Scenarios:
- $0: the cost is inside the $7M.
- $0.5M, $1M, $2M: the cost is outside the $7M and must be added to the denominator.
- Zero-benefit case: the diagnostic adds cost but no benefit.

## Sensitivity Analysis

**Base case.** 5.5M × 0.6 × 0.06 × 0.10 = 19,800 deaths/yr. That gives 534,600 DALYs and $OP 5.346e10 of benefit. SROI = 5.346e10 / 7e6 × 0.4 = **3,055x**.

**A. Cost already inside the $7M (benefit-only addition).**

| Diagnostic DALYs/yr | Added SROI | Total SROI | Δ |
|---|---|---|---|
| 0 | 0 | 3,055x | 0% |
| 3k | +43x | 3,098x | +1.4% |
| 10k | +143x | 3,198x | **+4.7%** |
| 30k | +429x | 3,484x | **+14.0%** |
| 50k (undiscounted) | +714x | 3,769x | +23.4% |
| 100k (stress) | +1,429x | 4,484x | +46.8% |

**B. Cost outside the $7M (blended SROI).** On its own, the diagnostic term returns DALYs × 1e5 / C. Adding it raises the blended SROI only if that standalone SROI exceeds 3,055x. The break-even cost is about $327k at 10k DALYs and $982k at 30k DALYs.

| Extra cost | 0 DALYs | 10k DALYs | 30k DALYs |
|---|---|---|---|
| $0.5M | 2,851x (−6.7%) | 2,985x (−2.3%) | 3,251x (+6.4%) |
| $1M | 2,673x (−12.5%) | 2,798x (−8.4%) | 3,048x (−0.2%) |
| $2M | 2,376x (−22.2%) | 2,487x (−18.6%) | 2,709x (−11.3%) |

**Interactions.** The terms are additive in the numerator and enter jointly through the denominator. Benefit and cost effects offset each other rather than multiply.

**Funding bar check.**
- Benefits alone cannot push SROI below the 2,000x bar.
- Costs alone would need to reach about $10.7M in total (≈$3.7M of zero-benefit extra cost) before the bar is crossed.
- No plausible scenario crosses the bar in either direction.

## Bottom-Line Impact

Crediting the diagnostic changes SROI by roughly −12% to +14% across the plausible cost and benefit scenarios:
- **+5% to +14%** (3,055x → about 3,200–3,480x) if the diagnostic's costs are already inside the $7M.
- About **−8% to +6%** if $0.5–1M of diagnostic cost sits outside the $7M.
- Leaning **≈0 to slightly negative** once the 2026 WHO tongue-swab and near-point-of-care NAAT crowding is weighted.

The direction depends mainly on the unresolved cost-inclusion question, not on the DALY estimate.

## Materiality Verdict

**BORDERLINE, leaning NO.**
- The magnitude can reach about ±10–14% at the edges.
- The central evidence-weighted effect is small (≈0 to +5%), and its sign is uncertain.
- The funding decision against the 2,000x bar is unaffected in all plausible scenarios.
- The main actionable item is to confirm whether the diagnostic's costs are inside the $7M.

## Code

```python
eligible_8y, yrs, decl = 5_500_000, 8, 0.02
uptake, base_mort, rr = 0.60, 0.06, 0.10
dpd, op_per_daly, speed = 27, 100_000, 1
cost, p = 7_000_000, 0.40

eligible = eligible_8y * (1 - decl) ** (yrs - 8)
deaths = eligible * uptake * base_mort * rr                 # 19,800
benefit_statin = deaths * speed * dpd * op_per_daly         # 5.346e10
base = benefit_statin / cost * p                            # 3055.4

def sroi(diag_dalys=0, extra_cost=0):
    num = p * benefit_statin + diag_dalys * speed * op_per_daly
    return num / (cost + extra_cost)

print(f"base {base:.0f}x")
for d in [0, 3e3, 1e4, 3e4, 5e4, 1e5]:
    s = sroi(d)
    print(f"A {d:>7.0f} DALYs: {s:.0f}x ({(s/base-1)*100:+.1f}%)")
for c in [5e5, 1e6, 2e6]:
    for d in [0, 1e4, 3e4]:
        s = sroi(d, c)
        print(f"B cost+{c/1e6}M, {d:.0f} DALYs: {s:.0f}x ({(s/base-1)*100:+.1f}%)")
for d in [1e4, 3e4]:
    print(f"break-even extra cost @ {d:.0f} DALYs: ${d*op_per_daly/base:,.0f}")
print(f"total cost to hit 2000x w/ zero diag benefit: ${p*benefit_statin/2000:,.0f}")
```

--- Critique: 60% steady-state uptake has no precedent among comparable TB program additions ---

# Impact Assessment: 60% Steady-State Uptake Ceiling for Adjunctive Atorvastatin

**CRITIQUE:** 60% steady-state uptake has no precedent among comparable TB program additions.

## Parameter Mapping

| Parameter | Model key | Current value | Role in formula |
|---|---|---|---|
| Steady-state uptake ceiling | `adult_uptake` | 0.60 | `treated = eligible × adult_uptake`. Multiplicative and linear in SROI. |
| Adoption ramp shape | Not modeled (implicit step function) | Instant jump to 0.60 | Enters only if the model has discounting, continued incidence decline, or a finite horizon. |
| Timing | `years_to_adoption`, `speedup_years` | 8, 1 | Unchanged by this critique. The ramp interaction is cross-referenced to Thread 3. |

The other parameters are held at base: `eligible_people_at_8y` = 5.5M, `baseline_mortality` = 0.06, `relative_reduction` = 0.10, `dalys_per_death` = 27, `op_per_daly` = 100,000, `all_in_cost` = $7M, `p_success` = 0.40.

## Plausible Range

**`adult_uptake`:** current value 0.60. Plausible range is **0.30 to 0.75**, with a central estimate of about **0.45**.

- **Low (0.30):** This applies 4HPMZ-like friction, a substantial private-sector share outside guideline-driven programs, and dropout from monitoring and drug-interaction concerns (rifampicin lowers statin exposure).
- **Central (about 0.40–0.50):** WRD reached 54% global coverage after about 14 years, with large variance across countries. WRD needs capital equipment and supply chains, so a cheap oral generic could plausibly do somewhat better. Its 2018–2023 African trajectory (37% to 58%) shows that 50–60% is reachable, but only over many years.
- **High (0.75):** An oral generic co-packaged into national program regimens after a WHO recommendation could exceed WRD. Nothing in the evidence rules out uptake above 60%. This is speculative, and no verified analog supports it.
- **Excluded evidence:** The dexamethasone and pyridoxine examples were not used because they are unverified.

## Sensitivity Analysis

### Code

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

b = sroi(base)                                    # 3054.9
for u in [0.30, 0.35, 0.3928, 0.40, 0.45, 0.50, 0.60, 0.75]:
    s = sroi({**base, 'adult_uptake': u})
    print(u, round(s), f"{(s/b-1)*100:+.1f}%")

# break-even uptake at the 2,000x bar
print("breakeven uptake:", 2000 / (b / 0.60))     # 0.3928

# Ramp illustration (cross-ref Thread 3): value of a 1-yr shift of a linear ramp
# at 4 pp/yr to a 0.60 ceiling (15 yrs), vs an instant step to 0.60.
# Gain from shifting curve u(t) by 1 yr = sum_t f^t * [u(t+1)-u(t)] * cases,
# where f = per-year weight (incidence decline x discount).
def shift_gain(f, ramp=0.04, ceiling=0.60):
    n = round(ceiling / ramp)
    return sum(f**t * ramp for t in range(n))

for label, f in [("no discount, no decline (CG base)", 1.0),
                 ("2%/yr continued incidence decline", 0.98),
                 ("4% discount", 1/1.04),
                 ("both", 0.98/1.04)]:
    g = shift_gain(f)
    print(label, round(g, 3), f"{(g/0.60-1)*100:+.0f}% vs instant step")
```

### Results: uptake ceiling

The base case SROI is **3,055x**. It is linear in uptake, at 5,092x per unit of uptake.

| `adult_uptake` | SROI | Δ vs base | vs 2,000x bar |
|---|---|---|---|
| 0.30 | 1,527x | −50.0% | Below |
| 0.35 | 1,782x | −41.7% | Below |
| **0.393 (break-even)** | **2,000x** | **−34.5%** | **At bar** |
| 0.40 | 2,037x | −33.3% | Marginally above |
| 0.45 | 2,291x | −25.0% | Above |
| 0.50 | 2,546x | −16.7% | Above |
| 0.60 (base) | 3,055x | 0% | Above |
| 0.75 (optimistic) | 3,819x | +25.0% | Above |

Deaths averted per year scale the same way: 19,800 at base, 9,900 at 0.30, 13,200 at 0.40 and 24,750 at 0.75. DALYs credited fall from 534,600 to between 267,300 and 356,400 at ceilings of 0.30–0.40.

### Results: ramp shape

This is the critique's secondary mechanism, illustrated with the WRD-like ramp of 4 percentage points per year.

| Weighting regime | Effective one-year-shift gain | Δ vs instant step |
|---|---|---|
| CG base (no discount, no further decline, infinite horizon) | 0.600 | 0% |
| 2%/yr incidence decline continues after year 8 | 0.523 | −13% |
| 4% discount rate | 0.463 | −23% |
| Both | 0.409 | −32% |

This confirms the critique's mechanism. Under CG's current structure, ramp shape has **zero** effect: shifting any ramp by one year gains exactly ceiling × one year of cases. A ramp only bites once Thread 3 adds discounting or a continued incidence decline. Those reductions belong to Thread 3 and should not be double-counted here.

### Interactions

- Uptake multiplies with every other term, so joint effects with other threads are **multiplicative, not additive**. For example, an uptake of 0.45 combined with a −20% change from another thread gives 0.75 × 0.80 = 0.60, a −40% change.
- If a later revision separates "P(WHO adoption | Phase III success)" from `p_success`, part of the uptake shortfall may already sit there. Check for double-counting before combining.

## Bottom-Line Impact

**Lowering the uptake ceiling from 0.60 to a plausible 0.30–0.50 reduces SROI by 17–50%, from 3,055x to 1,527x–2,546x. The central estimate is about −25% (0.45 gives 2,291x). The optimistic case (0.75) raises SROI by 25%.** Under CG's undiscounted, infinite-horizon structure, ramp shape contributes nothing on its own.

## Materiality Verdict

**BORDERLINE**, leaning YES on magnitude.

- Uptake below **0.393** pushes SROI under the 2,000x bar. The plausible range (0.30–0.75) straddles this line. The lower third of the range (0.30–0.39) flips the funding decision, and the central estimate (about 0.45) does not.
- The effect is large in relative terms (up to −50%) and, because it is multiplicative, it would compound with any other pessimistic thread. Combined with almost any other moderate downward adjustment, it would likely push SROI below the bar.
- The evidence shows the ceiling is *uncertain*, not *demonstrably too low*. No verified analog exists for a cheap generic adjunct. Country-level adoption data for comparable adjuncts would determine whether this becomes a clear YES.

--- Critique: A Phase III cannot be powered on mortality, so the WHO GDG would be recommending on surrogate or composite endpoints ---

# Impact Assessment: Phase III Endpoint Feasibility and Its Effect on Uptake, Adoption Timing and Realized Mortality Effect

**CRITIQUE:** A Phase III cannot be powered on mortality, so the WHO GDG would be recommending on surrogate or composite endpoints.

**Bottom line:** The critique works almost entirely through `adult_uptake`. A conditional WHO recommendation plausibly cuts the SROI by 17–33%, from 3,055x to roughly 2,040–2,550x, which stays above the 2,000x bar. Only the speculative subgroup-restricted scenario takes it below the bar. The materiality verdict is BORDERLINE.

---

## Feasibility Check on the Premise

I first checked the sample-size claim, since the rest of the critique depends on it.

| Baseline mortality | Relative reduction | Power | n per arm | Total N |
|---|---|---|---|---|
| 5% (critique's figure, ungrounded) | 10% | 80% | ~28,400 | ~56,800 |
| 6% (CEA's own `baseline_mortality`) | 10% | 80% | ~23,400 | ~46,800 |
| 6% | 10% | 90% | ~31,300 | ~62,600 |

- **The premise holds at the CEA's own baseline.** At 6%, about 47,000 patients would be needed. That is implausible within a $7M all-in budget, even at a few hundred dollars per patient. This is my inference and is not costed here.
- **The critique's 5% figure doesn't matter for the conclusion.** Using the CEA's 6% removes the need to resolve the "UNGROUNDED" flag for this purpose.

---

## Parameter Mapping

| Parameter | Current value | Channel | Status after verification |
|---|---|---|---|
| `adult_uptake` | 0.60 | A conditional or subgroup-limited recommendation lowers uptake | Primary channel; magnitude is speculative |
| `years_to_adoption` | 8 | The GDG requests more evidence, delaying adoption | Weakened. WHO treats "unfavorable outcome" composites as critical outcomes, so a recommendation need not stall |
| `relative_reduction` (and its joint distribution with `p_success`) | 0.10 (× 0.40) | The mortality effect is never directly verified | A pure variance increase has zero effect on expected SROI, because the model is linear. It matters only if "success" includes surrogate-only wins with a lower true mortality effect. That is a mean shift, which overlaps with Thread 1 |

**Structural notes on the model:**
- The SROI is linear in `adult_uptake` and `relative_reduction`.
- `years_to_adoption` enters only through the decline term, 0.98^(Δ). With no discounting, a delay costs only about 2% per year.

---

## Plausible Ranges

- **`adult_uptake`:** 0.60 → range [0.20, 0.60]. Central estimate 0.45–0.50.
  - The 0.45–0.50 central case reflects a conditional recommendation with a "mortality benefit not directly shown" caveat.
  - The 0.20–0.30 low end is the critique's own speculative scenario: a recommendation restricted to a high-risk subgroup covering about a third of patients.
  - The upper bound of 0.60 reflects the verifier's finding that a composite including death can support a normal recommendation.
- **`years_to_adoption`:** 8 → range [7, 11].
  - The optimistic end reflects a cheaper surrogate-endpoint trial finishing faster.
  - Delays of more than 3 years are not supported, given the verifier's finding.
- **Surrogate-only "success" (Thread 1 overlap):**
  - Share of successes that are surrogate-only, s ∈ [0.25, 0.5].
  - True relative reduction in those cases, r_s ∈ [0, 0.05].
  - This gives E[relative_reduction | success] ∈ [0.05, 0.0875].

---

## Sensitivity Analysis

**Base case:** SROI = 3,055x. Deaths averted per year = 19,800.

**Bar-crossing points:**
- The SROI falls below the 2,000x bar at a 34.5% reduction (multiplier 0.655).
- That corresponds to a breakeven `adult_uptake` of 0.393.

| Scenario | SROI | Δ |
|---|---|---|
| uptake 0.50 | 2,546x | −16.7% |
| uptake 0.45 | 2,291x | −25.0% |
| uptake 0.40 | 2,037x | −33.3% |
| uptake 0.30 | 1,527x | −50.0% (below bar) |
| uptake 0.20 | 1,018x | −66.7% (below bar) |
| adoption +1 yr | 2,994x | −2.0% |
| adoption +2 yr | 2,934x | −4.0% |
| adoption +3 yr | 2,875x | −5.9% |
| adoption −1 yr (faster surrogate trial) | 3,117x | +2.0% |
| **Joint central** (uptake 0.45, +1 yr) | **2,245x** | **−26.5%** |
| Joint pessimistic (uptake 0.30, +2 yr) | 1,467x | −52.0% |
| Joint pessimistic + surrogate mean shift (E[RR] = 0.07) | 1,027x | −66.4% |
| Extreme (uptake 0.20, +3 yr, E[RR] = 0.07) | 671x | −78.0% |
| Optimistic (strong recommendation on composite; uptake 0.60, −1 yr) | 3,117x | +2.0% |

**Thread 1 overlap (reported separately and not added to this critique's bottom line):**
- E[RR | success] ranges from 0.0875 to 0.05, a change of −12.5% to −50%.
- At s = 0.5 and r_s = 0.04, the change is −30%.

**Interactions:**
- All channels combine multiplicatively, because the formula is a pure product.
- Uptake and delay are near-additive at these magnitudes.
- If Thread 3 introduces a ~4% discount rate, each year of delay costs about 6% rather than 2%. Even then, the delay channel remains secondary.

**Pure variance in `relative_reduction`:**
- If the variance increases while the mean stays fixed and `relative_reduction` remains independent of `p_success`, the change in expected SROI is 0%.
- That increase still matters for decision-relevant uncertainty, but not for the point estimate.

---

## Bottom-Line Impact

Under a conditional recommendation, the critique plausibly reduces cost-effectiveness by **about 17–33%**, from 3,055x to 2,040–2,550x. The central estimate is **about 25%** (≈2,250x with a 1-year delay).

- **Speculative tail:** In the subgroup-restricted scenario, the reduction reaches 50–67% (1,020–1,530x), which is below the 2,000x bar.
- **Upside:** The upside is negligible, at about +2%.
- **Delay pathway:** This contributes only 2–6%, under the model's no-discounting structure.

## Materiality Verdict: BORDERLINE

- **Magnitude:** In the central case the effect is material, at about 25%.
- **Decision impact:** The SROI stays above the bar unless `adult_uptake` falls below 0.39. That would require the speculative subgroup-restriction scenario, which the verifier partly undercut.
- **Highest-value follow-up:** Find an empirical precedent for uptake after WHO conditional recommendations of adjunctive TB therapies. Examples include corticosteroids for TB meningitis or pericarditis, and conditional recommendations for HIV-associated TB.

---

## Code

```python
from math import sqrt
from scipy.stats import norm

BASE = dict(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=1e5, speedup_years=1,
            all_in_cost=7e6, p_success=0.40)

def sroi(**kw):
    p = {**BASE, **kw}
    elig = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    deaths = elig * p['adult_uptake'] * p['baseline_mortality'] * p['relative_reduction']
    benefit = deaths * p['speedup_years'] * p['dalys_per_death'] * p['op_per_daly']
    return benefit / p['all_in_cost'] * p['p_success']

base = sroi()
print(f"Base SROI {base:.0f}x; breakeven uptake {0.60*2000/base:.3f}")

scen = {
  'uptake 0.50': dict(adult_uptake=0.50), 'uptake 0.45': dict(adult_uptake=0.45),
  'uptake 0.40': dict(adult_uptake=0.40), 'uptake 0.30': dict(adult_uptake=0.30),
  'uptake 0.20': dict(adult_uptake=0.20),
  '+1y': dict(years_to_adoption=9), '+2y': dict(years_to_adoption=10),
  '+3y': dict(years_to_adoption=11), '-1y': dict(years_to_adoption=7),
  'joint central': dict(adult_uptake=0.45, years_to_adoption=9),
  'joint pess': dict(adult_uptake=0.30, years_to_adoption=10),
  'joint pess + RR0.07': dict(adult_uptake=0.30, years_to_adoption=10, relative_reduction=0.07),
  'extreme': dict(adult_uptake=0.20, years_to_adoption=11, relative_reduction=0.07),
}
for k, v in scen.items():
    s = sroi(**v); print(f"{k:22s} {s:7.0f}x  {100*(s/base-1):+6.1f}%")

# Thread-1 overlap: surrogate-only successes
for s_share, r_s in [(0.25, 0.05), (0.5, 0.04), (0.5, 0.0)]:
    rr = 0.10*(1-s_share) + r_s*s_share
    print(f"s={s_share}, r_s={r_s}: E[RR]={rr:.4f}, delta={100*(rr/0.10-1):+.1f}%")

# Sample size, two-proportion test
def n_per_arm(p1, rrr, alpha=0.05, power=0.80):
    p2 = p1*(1-rrr); z = norm.ppf(1-alpha/2) + norm.ppf(power)
    return z**2 * (p1*(1-p1) + p2*(1-p2)) / (p1-p2)**2
for p1, pw in [(0.05, .8), (0.06, .8), (0.06, .9)]:
    print(p1, pw, round(n_per_arm(p1, 0.10, power=pw)))
```

--- Critique: Clinical eligibility and monitoring barriers cap the achievable prescribing share below the "generic and cheap" logic ---

# CRITIQUE: Clinical eligibility and monitoring barriers cap the achievable prescribing share below the "generic and cheap" logic

## Parameter Mapping

| Parameter | Model key | Current value | How the critique affects it |
|---|---|---|---|
| Adult uptake (primary) | `adult_uptake` | 0.60 | (a) A smaller eligible population: liver disease, prior or likely DILI, pregnancy, interacting ART, age and polypharmacy. (b) Program reluctance. (c) Discontinuation. |
| Baseline mortality (secondary, interaction) | `baseline_mortality` | 0.06 (population average) | If excluded subgroups (HIV-coinfected, liver disease, elderly) have above-average mortality, deaths among *eligible* patients fall more than the headcount does. |
| All-in cost (conditional, secondary) | `all_in_cost` | $7M | Only applies if LFT monitoring is mandated. Monitoring costs are not in CG's denominator. This belongs mainly to the all_in_cost thread and is shown separately below, not in the bottom line. |

**Structural note:** SROI is strictly linear in `adult_uptake`. Each 0.01 of uptake is worth about 50.9x SROI. Break-even with the 2,000x bar is at `adult_uptake` = 0.393, which is a 34.5% reduction in effective coverage.

## Plausible Range

The critique's 10–20% exclusion share and its 0.45–0.50 endpoint are ungrounded. I therefore decompose uptake into explicit factors and scan each across a range, rather than adopting the critique's figures.

1. **Exclusion share, e = 5% to 20%.**
   - **Low (5%):** Dolutegravir-based ART now dominates, and it has no meaningful statin interaction. The rifampicin–atorvastatin interaction mainly *lowers statin exposure* (an efficacy issue for Thread 1), not toxicity. This argues for a low e.
   - **High (20%):** This adds:
     - known liver disease;
     - DILI during intensive phase, where the pooled DILI estimate of ~11.5% is verified and some fraction would trigger statin withdrawal;
     - pregnancy, where the FDA requested removal of the broad pregnancy contraindication in 2021 but statins are still generally stopped in pregnancy;
     - PI or efavirenz regimens;
     - polypharmacy.
   - Basis: verified DILI and DDI premises. The magnitude is judgment.

2. **Program adoption and adherence factor, f = 0.85 to 1.0.**
   - This covers NTP reluctance where the DILI-attribution confounder is a real concern, plus early discontinuation over a 6-month adjunct.
   - It is unsourced and illustrative.

3. **Double-counting share, d = 0% to 50%.**
   - CG's 0.60 is already a haircut from 100%. It is plausible that it implicitly embeds some contraindication allowance.
   - I scan the case where half of the exclusion is already embedded.

4. **Mortality ratio of excluded vs. eligible patients, r = 1.0 to 2.5.**
   - HIV-positive TB patients make up about 6% of cases but a disproportionate share of TB deaths.
   - Liver disease and older age also raise mortality.
   - This is a sensitivity scenario only, because many HIV patients would *not* be excluded on dolutegravir regimens.

## Sensitivity Analysis

**Base case:** SROI = **3,055x** (19,800 deaths averted per year; 534,600 DALYs).

### One-way: `adult_uptake`

| adult_uptake | SROI | Δ |
|---|---|---|
| 0.57 | 2,902x | −5.0% |
| 0.55 | 2,800x | −8.3% |
| 0.50 | 2,546x | −16.7% |
| 0.45 | 2,291x | −25.0% |
| 0.40 | 2,037x | −33.3% |
| **0.393** | **2,000x** | **−34.5% (break-even)** |

### Decomposed scenarios: headcount only (r = 1)

| Scenario | e | f | d | Effective uptake | SROI | Δ |
|---|---|---|---|---|---|---|
| Low | 5% | 1.00 | 0 | 0.570 | 2,902x | −5.0% |
| Central | 10% | 0.92 | 0 | 0.497 | 2,529x | −17.2% |
| High | 20% | 0.85 | 0 | 0.408 | 2,077x | −32.0% |
| Low, 50% already in 0.60 | 5% | 1.00 | 0.5 | 0.585 | 2,978x | −2.5% |
| Central, 50% already in 0.60 | 10% | 0.92 | 0.5 | 0.524 | 2,670x | −12.6% |
| High, 50% already in 0.60 | 20% | 0.85 | 0.5 | 0.459 | 2,337x | −23.5% |

The critique's own 0.45–0.50 maps to 2,291–2,546x (Δ −25% to −17%).

### Joint: exclusion × mortality weighting

This scenario holds the 0.06 population average fixed. Deaths reachable among eligible patients scale by (1−e)/(1−e+e·r).

| Scenario | e | r | f | Deaths multiplier | SROI | Δ |
|---|---|---|---|---|---|---|
| Low | 5% | 1.5 | 1.00 | 0.927 | 2,831x | −7.3% |
| Central | 10% | 2.0 | 0.92 | 0.753 | 2,299x | −24.7% |
| High (pessimistic) | 20% | 2.5 | 0.85 | 0.523 | **1,598x** | **−47.7%** |

**Interaction type:** The effects are multiplicative, not additive. Exclusion and mortality-weighting compound: at e = 20%, headcount alone gives −20%, but with r = 2.5 it gives −38%, before the f factor is applied.

### Optimistic direction

If CG's 0.60 already fully embeds contraindications (d = 1) and uptake is actually higher, the critique has zero impact. For example, a WHO recommendation plus Global Fund procurement could reach 0.70, giving 3,564x (+16.7%). The verified evidence does not support an increase. The upside comes only from the uncertainty in CG's unanchored 0.60.

### Conditional add-on: mandated LFT monitoring

This is outside the bottom line and should be coordinated with the all_in_cost thread.

- **Why it belongs in the denominator:** The speedup year adds a full extra year of treatment, so that year's delivery costs are as counterfactual as its benefits.
- **Cost scenarios:**
  - Low: 25% monitored × 1 test × $4 = $3.3M
  - Central: 50% × 2 tests × $5 = $16.5M
  - High: 100% × 2 × $8 = $52.8M
- **Results:**

| Counterfactual value of delivery $ | Low ($3.3M) | Central ($16.5M) | High ($52.8M) |
|---|---|---|---|
| 1.0 | 2,076x (−32%) | 910x (−70%) | 358x (−88%) |
| 0.2 | 2,792x (−9%) | 2,076x (−32%) | 1,218x (−60%) |

- **Consistency caveat:** Drug costs (~$3–6 per patient course) are equally absent from the denominator. This is a framework-level question about whether delivery costs count in an "all-in" SROI. It is potentially larger than the uptake effect, but it is not specific to this critique.

### Compounding with other threads

The critique's central multiplier is 0.83. Combined with a 20% reduction from another thread (e.g., relative_reduction), SROI becomes 3,055 × 0.8 × 0.83 ≈ **2,024x**, right at the bar.

## Bottom-Line Impact

**Eligibility, monitoring and adherence barriers plausibly reduce SROI by about 3–32% (3,055x → ~2,980–2,080x), with a central estimate of about 13–17% (~2,530–2,670x). The range rises to about 48% (≈1,600x) only if excluded patients also carry 2–2.5x average mortality. The critique alone does not cross the 2,000x bar, which requires effective adult_uptake ≤ 0.39.**

## Materiality Verdict

**BORDERLINE (leaning YES on magnitude).** I assume a materiality threshold of a ≥10% SROI change or crossing the 2,000x bar, because the thread spec does not state one.

- **Magnitude:** The central estimate (−13% to −17%) exceeds a 10% materiality threshold.
- **Decision:** It does not flip the funding decision alone.
- **Where it could flip:** Only the pessimistic mortality-weighted scenario crosses the bar, and it does so readily when compounded with other threads' haircuts.
- **Main caveats:**
  - The exclusion magnitude is ungrounded.
  - Some of it may already be embedded in CG's 0.60.
- **Highest-value follow-up:** Determine which statin CG's trial uses. A less CYP3A4-dependent statin would shrink e. Also determine whether the trial protocol or a future guideline mandates LFT monitoring, which would activate the cost channel.

## Code

```python
# TB statins BOTEC — adult_uptake / eligibility sensitivity
base = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
            all_in_cost=7_000_000, p_success=0.40)

def sroi(p, extra_cost=0.0):
    elig = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    treated = elig * p['adult_uptake']
    deaths = treated * p['baseline_mortality'] * p['relative_reduction']
    benefit = deaths * p['speedup_years'] * p['dalys_per_death'] * p['op_per_daly']
    return benefit / (p['all_in_cost'] + extra_cost) * p['p_success']

B = sroi(base)
print(f"Base SROI: {B:,.0f}x")                                      # 3,055x
print(f"Break-even uptake: {0.60*2000/B:.3f}")                      # 0.393

def run(u_mult=1.0, mort_mult=1.0, extra_cost=0.0):
    p = dict(base)
    p['adult_uptake'] *= u_mult
    p['baseline_mortality'] *= mort_mult
    s = sroi(p, extra_cost)
    return s, 100 * (s / B - 1)

# One-way adult_uptake
for u in [0.57, 0.55, 0.50, 0.45, 0.40, 0.70]:
    s, d = run(u / 0.60); print(f"u={u:.2f}: {s:,.0f}x ({d:+.1f}%)")

# Decomposed headcount scenarios: e=exclusion, f=adoption/adherence, d=share already in 0.60
def headcount(e, f, d=0.0):
    return (1 - e * (1 - d)) * f

# Mortality weighting: excluded patients have mortality r x eligible; population avg fixed at 0.06
def mort_weight(e, r):
    return (1 - e) / (1 - e + e * r)

scen = {'Low': (0.05, 1.00), 'Central': (0.10, 0.92), 'High': (0.20, 0.85)}
for name, (e, f) in scen.items():
    for d in [0.0, 0.5]:
        m = headcount(e, f, d); s, dl = run(m)
        print(f"{name} d={d}: uptake={0.6*m:.3f} -> {s:,.0f}x ({dl:+.1f}%)")

for name, (e, r, f) in {'Low': (0.05, 1.5, 1.0), 'Central': (0.10, 2.0, 0.92),
                        'High': (0.20, 2.5, 0.85)}.items():
    m = mort_weight(e, r) * f; s, dl = run(m)          # exclusion applied via deaths multiplier
    print(f"{name} mortality-weighted: mult={m:.3f} -> {s:,.0f}x ({dl:+.1f}%)")

# Conditional: LFT monitoring costs added to denominator, at counterfactual value v
treated = 3_300_000
for label, frac, tests, price in [('Low', .25, 1, 4), ('Central', .5, 2, 5), ('High', 1, 2, 8)]:
    C = treated * frac * tests * price
    for v in [1.0, 0.2]:
        s, dl = run(extra_cost=v * C)
        print(f"LFT {label} C=${C/1e6:.1f}M v={v}: {s:,.0f}x ({dl:+.1f}%)")

# Compounding with a 20% haircut from another thread
print(f"Central x 0.8: {B*0.828*0.8:,.0f}x")
```

**Simplifications:** I used CG's exact formula chain. The only additions are:
- explicit multiplicative factors on `adult_uptake`;
- a mortality-reweighting factor that holds the 6% population average fixed;
- an optional denominator add-on for monitoring costs.

I did not model an uptake ramp or discounting. Those belong to the years_to_adoption and speedup threads.

--- Critique: Effective delivered dose and adherence diverge from trial conditions, and programmatic dose may be lower than the trial dose, notably with rifapentine regimens ---

# Quantitative Impact Assessment

**Critique:** Effective delivered dose and adherence diverge from trial conditions; programmatic dose may be lower than trial dose, notably with rifapentine regimens

---

## Parameter Mapping

The CEA has no adherence or dose term. The critique's mechanism enters the model as a multiplier on parameters already there:

| Parameter | Model key | Current value | How the critique enters |
|---|---|---|---|
| Effective relative mortality reduction | `relative_reduction` | 0.10 | × (real-world adherence ÷ trial adherence) × (1 − HPMZ share × HPMZ efficacy loss) |
| Uptake (equivalent entry point) | `adult_uptake` | 0.60 | The critique's framing, 0.60 → 0.42. This is numerically identical to scaling `relative_reduction`. |

The formula chain is purely multiplicative:

SROI = eligible × uptake × baseline_mortality × relative_reduction × speedup × DALYs × $OP/DALY ÷ cost × p_success

So any factor *f* applied to either parameter scales SROI by exactly *f*. It does not matter which parameter we attach it to. I apply it to `relative_reduction`, because a dose or exposure shortfall is an efficacy concept.

**A correction to the critique's arithmetic is needed.** The 10% `relative_reduction` is the effect expected *if the trial is positive*. A trial's intention-to-treat effect already includes trial-level non-adherence. The correct adherence factor is therefore the **ratio** of real-world adherence to trial adherence, not absolute real-world adherence.

- Applying 70% absolute adherence (0.60 → 0.42) implicitly assumes 100% trial adherence. That double-counts.
- If trial adherence is about 90% and real-world adherence is 70%, the factor is 0.78, not 0.70.

I keep 0.70 as the pessimistic bound. A real-world/trial ratio of 0.70 is possible if trial adherence is high and programme adherence is poor.

---

## Plausible Range

### Component 1: Adherence ratio (real-world ÷ trial)

- **Current (implicit):** 1.0
- **Plausible range:** 0.70 to 1.0, central about 0.85
- **Basis:**
  - TB treatment is time-limited (4–6 months) and delivered within an existing adherence-support structure. That makes the long-term chronic-statin non-adherence literature (often 50–70% at one year) a pessimistic analogue, not a direct one.
  - An out-of-FDC extra pill plausibly loses some adherence relative to trial monitoring.
  - The verifier flagged the TB-specific adherence evidence as **UNGROUNDED**. The range is therefore a judgement band, not an estimate.
- **Optimistic tail:** about 1.0–1.03. This would require the statin to be co-packaged or given under directly observed therapy, with adherence matching or slightly exceeding a pragmatic trial. Exceeding trial adherence is unlikely, so the upside is capped near 1.0.

### Component 2: Rifamycin / rifapentine dose transfer

Factor = 1 − (share of drug-susceptible patients on HPMZ at year 8) × (fractional efficacy loss in that subgroup).

**HPMZ share at year 8:** 0 to 30%, central about 15%.
- It is currently small but growing.
- Uptake of HPMZ was not verified.

**Efficacy loss in the HPMZ subgroup:** 0 to 30%, central about 10%.
- Daily rifapentine induces CYP3A4 at roughly 85–100% of rifampicin's level. A dose chosen under HRZE should therefore transfer approximately.
- The residual loss comes from inter-regimen differences and persistent induction.
- The magnitude is **UNGROUNDED**, and the verifier rated this component low strength.

**Resulting factor:** 0.91 (pessimistic) / 0.985 (central) / 1.0 (optimistic).

**What is not counted here:** The general rifampicin–statin interaction under HRZE is *not* a separate penalty. Phase IIc dose-finding is conducted under rifampicin, so that interaction is embedded in whatever dose the trial selects. Only the *transfer* gap counts.

---

## Sensitivity Analysis

**Base case:** 19,800 deaths averted per year; SROI = **3,055x** (funding bar 2,000x).

**Break-even:** SROI falls below 2,000x when the combined factor is below 2,000 / 3,055 = **0.655**, a 34.5% reduction.

### Individual parameters

| Scenario | Factor | Effective rr | Deaths/yr | SROI | Δ |
|---|---|---|---|---|---|
| Base | 1.000 | 0.100 | 19,800 | 3,055x | — |
| Adherence ratio 0.95 | 0.95 | 0.095 | 18,810 | 2,902x | −5% |
| Adherence ratio 0.85 (central) | 0.85 | 0.085 | 16,830 | 2,597x | −15% |
| Adherence 70% abs / 90% trial | 0.78 | 0.078 | 15,444 | 2,383x | −22% |
| Adherence ratio 0.70 (pessimistic) | 0.70 | 0.070 | 13,860 | 2,138x | −30% |
| Adherence optimistic | 1.03 | 0.103 | 20,394 | 3,147x | +3% |
| HPMZ central (15% × 10%) | 0.985 | 0.0985 | 19,503 | 3,009x | −1.5% |
| HPMZ mid (15% × 30%) | 0.955 | 0.0955 | 18,909 | 2,917x | −4.5% |
| HPMZ pessimistic (30% × 30%) | 0.91 | 0.091 | 18,018 | 2,780x | −9% |

### Joint scenarios

The two components multiply. Their effects compound slightly less than additively in percentage terms.

| Scenario | Combined factor | SROI | Δ | Clears 2,000x bar? |
|---|---|---|---|---|
| Optimistic (1.0 × 1.0) | 1.00 | 3,055x | 0% | Yes |
| Central (0.85 × 0.985) | 0.837 | 2,558x | −16% | Yes |
| Moderate-pessimistic (0.78 × 0.955) | 0.745 | 2,276x | −25% | Yes |
| Joint pessimistic (0.70 × 0.91) | 0.637 | 1,946x | −36% | **No** |

### Thresholds

- Adherence alone must fall to a ratio of **0.655** to cross the bar.
- With the pessimistic HPMZ factor (0.91), adherence only needs to fall to **0.72**.

### Interaction with other critiques

Every term in the model is multiplicative, so this critique compounds with the other threads. For example, if Critique 2 (uptake ramp or lag) independently cut SROI by 20%, the central case here would bring the total to 0.837 × 0.80 = 0.67, giving about 2,045x, right at the bar.

**Dose-response note:** If the benefit has an exposure threshold (partial adherence giving disproportionately little benefit), the factor would fall below the linear adherence ratio. If the benefit saturates at moderate exposure, the factor would fall above it. No evidence was verified either way, so linear scaling is the neutral assumption.

---

## Bottom-Line Impact

**This critique plausibly reduces cost-effectiveness by 0–36% (SROI 3,055x → 1,946x–3,055x), with a central estimate of about 16% (≈2,560x).**

- Nearly all of the effect comes from the adherence component.
- The rifapentine component contributes at most about 9%, and about 1.5% centrally.
- The critique's headline "~30% cut from adherence" is at the pessimistic edge. It is overstated for the central case, because it applies absolute adherence to a trial effect that already reflects trial-level adherence.

---

## Materiality Verdict: **BORDERLINE**

- **Central case (−16%):** SROI stays well above the 2,000x bar. Not material on its own.
- **Joint pessimistic case (−36%):** SROI falls below the bar (1,946x). Material.
- **Alone, this critique is unlikely to flip the decision.** That would require a real-world/trial adherence ratio of 0.655 or below with no HPMZ penalty.
- **It matters through compounding.** Because the model is fully multiplicative, a central 16% haircut eats roughly half of the existing 35% headroom above the bar. Combined with the uptake-ramp or `relative_reduction` critiques, it could plausibly push SROI below 2,000x.
- **Recommended adjustment:** Add an explicit adherence-ratio term, central 0.85 with range 0.70–1.0, as a multiplier on `relative_reduction`. Treat the HPMZ term as a minor (≤10%) uncertainty unless HPMZ uptake data show rapid scale-up.

---

## Code

```python
# Replicates the Coefficient Giving TB-statins BOTEC formula chain exactly.
# Optionally load parameters from the xlsx via openpyxl; hard-coded here to
# match the extracted parameter summary.

BASE = dict(
    eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
    adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
    dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
    all_in_cost=7_000_000, p_success=0.40,
)

def model(p):
    eligible = p["eligible_people_at_8y"] * (1 - p["decline_per_year"]) ** (p["years_to_adoption"] - 8)
    treated = eligible * p["adult_uptake"]
    deaths = treated * p["baseline_mortality"] * p["relative_reduction"]
    benefit = deaths * p["speedup_years"] * p["dalys_per_death"] * p["op_per_daly"]
    sroi = benefit / p["all_in_cost"] * p["p_success"]
    return deaths, sroi

base_deaths, base_sroi = model(BASE)
print(f"Base: deaths/yr={base_deaths:,.0f}  SROI={base_sroi:,.0f}x")   # 19,800 / 3,055x
print(f"Break-even factor for 2,000x bar: {2000/base_sroi:.3f}")       # 0.655

def run(adh_ratio=1.0, hpmz_share=0.0, hpmz_loss=0.0, label=""):
    f = adh_ratio * (1 - hpmz_share * hpmz_loss)
    p = dict(BASE, relative_reduction=BASE["relative_reduction"] * f)
    d, s = model(p)
    print(f"{label:40s} f={f:.3f} rr={p['relative_reduction']:.4f} "
          f"deaths={d:,.0f} SROI={s:,.0f}x  delta={s/base_sroi-1:+.1%}  bar={'Y' if s>=2000 else 'N'}")

run(0.95, label="Adherence 0.95")
run(0.85, label="Adherence 0.85 (central)")
run(0.70/0.90, label="Adherence 70% abs / 90% trial")
run(0.70, label="Adherence 0.70 (pessimistic)")
run(1.03, label="Adherence optimistic")
run(1, 0.15, 0.10, label="HPMZ central")
run(1, 0.15, 0.30, label="HPMZ mid")
run(1, 0.30, 0.30, label="HPMZ pessimistic")
run(0.85, 0.15, 0.10, label="Joint central")
run(0.78, 0.15, 0.30, label="Joint moderate-pessimistic")
run(0.70, 0.30, 0.30, label="Joint pessimistic")

# Optional uncertainty propagation (judgement-based input distributions)
import numpy as np
rng = np.random.default_rng(0)
N = 200_000
adh = rng.triangular(0.65, 0.85, 1.0, N)
share = rng.uniform(0, 0.30, N)
loss = rng.uniform(0, 0.30, N)
f = adh * (1 - share * loss)
sroi = base_sroi * f
print(f"MC mean SROI={sroi.mean():,.0f}x, 5–95%: {np.percentile(sroi,5):,.0f}–{np.percentile(sroi,95):,.0f}x, "
      f"P(<2000x)={np.mean(sroi<2000):.1%}")
```

The deterministic results in the tables are exact outputs of the formula chain.

The Monte Carlo block is illustrative, and I have not reported its output. Analytically:
- The mean factor is about 0.833 × 0.978 ≈ 0.81, giving a mean SROI of about 2,490x.
- The probability of falling below 2,000x is low, roughly 1–2%. This is driven entirely by the lower tail of the adherence distribution.

These figures depend on judgement-based input distributions, and the verifier flagged the adherence evidence as ungrounded.

--- Critique: Private-sector treatment share and the reach of national guidelines are not modeled ---

# CRITIQUE: Private-sector treatment share and the reach of national guidelines are not modeled

## Parameter Mapping

| Parameter | Model key | Current value | How the critique touches it |
|---|---|---|---|
| Adult uptake (primary) | `adult_uptake` | 0.60 | Replaced by a sector-weighted *effective* uptake: Σ (sector share × sector uptake × dose/adherence retention) |
| Effective efficacy (secondary) | `relative_reduction` | 0.10 | Non-standard dosing in private care lowers delivered effect. This is mathematically identical to scaling uptake because the chain is multiplicative, so I model it once, as a "retention" factor, to avoid double-counting. |
| Eligible population (structural check) | `eligible_people_at_8y` | 5.5M | Determines whether *unnotified* private patients are inside or outside the model |
| Counterfactual timing | `speedup_years` | 1 | Private adoption before guidelines could shift timing. Treated qualitatively (see below). |

**A structural observation that changes the framing.** 5.5M at year 8 implies about 6.47M today (5.5M / 0.98⁸). WHO 2023 notifications are about 8.2M. Multiplying by about 96% drug-susceptible and about 88% adult gives about 6.9M. So `eligible_people_at_8y` is effectively a **notified-cohort** number.

This has two consequences:
- The critique's downside applies only to the **notified private** share. That is roughly 30–33% of notifications in India and lower in most other high-burden countries. I use about 15–25% globally, with 35% as an India-weighted stress case.
- **Unnotified** private patients are not in the denominator at all. Any atorvastatin reaching them is *uncounted upside*, not a downside. This supports the critique's sign ambiguity.

## Plausible Range

All sector values below are **assumptions**. The critique itself rates its 5–15% magnitude as ungrounded.

| Input | Low (pessimistic) | Central | High (optimistic) | Basis |
|---|---|---|---|---|
| Private share of notified DS-TB, global (s) | 0.35 (India-weighted stress) | 0.20 | 0.15 | India private notifications are about 30–33% of total; most other countries are lower |
| Private uptake relative to public (u_priv) | 0.40 | 0.60 | 0.80 | Private providers readily prescribe adjuncts (Mumbai study) but sit outside NTP procurement |
| Private dose/adherence retention (e_priv) | 0.50 | 0.70 | 0.80 | Unsupervised, non-standard dosing. No direct regimen-level data (evidence gap). |
| Public sector | u = 0.60, e = 1.0 | same | same | Assumes CG's 0.60 describes the guideline-following public sector |
| Unnotified private patients reached (upside only) | 0 | 0 | +1.5M patients × 0.4 uptake × 0.5 retention | About 22% notification of private-sector cases (older 4-country estimate). Their baseline mortality is unknown. |

**Caveat.** CG's 0.60 has no stated derivation. It may already be an implicit blended figure. If so, this critique adds little beyond a reallocation inside an already-uncertain number.

## Sensitivity Analysis

SROI is linear in effective uptake: SROI = 5,091.4 × eff_uptake.

| Scenario | Effective uptake | Deaths averted/yr | SROI | Δ |
|---|---|---|---|---|
| Base (CG) | 0.600 | 19,800 | 3,055x | — |
| Central (s=0.20, u=0.6, e=0.7) | 0.564 | 18,612 | 2,872x | −6% |
| Retention-only pessimistic (s=0.20, u=0.6, e=0.5) | 0.540 | 17,820 | 2,749x | −10% |
| India-weighted (s=0.30, u=0.5, e=0.6) | 0.510 | 16,830 | 2,597x | −15% |
| Joint pessimistic (s=0.35, u=0.4, e=0.5) | 0.460 | 15,180 | 2,342x | −23% |
| Optimistic, private adopts faster (s=0.20, u=0.8, e=0.8) | 0.608 | 20,064 | 3,096x | +1.3% |
| Optimistic plus unnotified reach | ≈0.663 | ≈21,864 | ≈3,374x | +10% |

**Breakevens:**
- Crossing the 2,000x bar alone requires effective uptake ≤ 0.393, a **−34.5%** cut. Even the joint-pessimistic case (−23%) does not reach it.
- **Interaction with other threads.** The effects are multiplicative with every other parameter. A −10% cut from this critique tips SROI below 2,000x only if other critiques have already reduced it below about 2,222x, i.e. a combined cut of about 27% from the base.

**Timing (speedup_years).** Private providers might adopt after Phase IIc or III results but before WHO guidance. That moves benefits earlier in *both* the grant and counterfactual worlds. The grant still causes the evidence to exist about 1 year sooner, so the net effect on the 1-year speedup credit is about zero. This could matter only once discounting is introduced (Thread 3).

## Bottom-Line Impact

**This critique plausibly changes SROI by −15% to +10%, with a central estimate of about −6% (3,055x → about 2,870x). An extreme joint-pessimistic case gives −23% (about 2,340x), which is still above the 2,000x bar.**

## Materiality Verdict

**NO** for the funding decision on its own. Reaching the bar requires −34.5%, beyond even the stress case.

**BORDERLINE** as a magnitude, because the central-to-pessimistic range is −6% to −15%. It becomes decision-relevant only in combination with other uptake or efficacy cuts (Thread 1 relative_reduction, adherence, adoption lag). It should be coordinated with those threads so that the dose/adherence retention factor is not counted twice.

## Code

```python
BASE = dict(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=1e5, speedup_years=1,
            all_in_cost=7e6, p_success=0.40)

def sroi(p, extra_treated=0.0):
    elig = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    treated = elig * p['adult_uptake'] + extra_treated
    deaths = treated * p['baseline_mortality'] * p['relative_reduction']
    benefit = deaths * p['speedup_years'] * p['dalys_per_death'] * p['op_per_daly']
    return deaths, benefit / p['all_in_cost'] * p['p_success']

def eff_uptake(s_priv, u_priv, e_priv, u_pub=0.60):
    return (1 - s_priv) * u_pub + s_priv * u_priv * e_priv

d0, s0 = sroi(BASE)
print(f"Base: deaths {d0:,.0f}, SROI {s0:,.0f}x")

scen = {
    "Central":              (0.20, 0.6, 0.7),
    "Retention pessimistic": (0.20, 0.6, 0.5),
    "India-weighted":       (0.30, 0.5, 0.6),
    "Joint pessimistic":    (0.35, 0.4, 0.5),
    "Optimistic":           (0.20, 0.8, 0.8),
}
for k, (s, u, e) in scen.items():
    p = dict(BASE, adult_uptake=eff_uptake(s, u, e))
    d, r = sroi(p)
    print(f"{k:24s} eff={p['adult_uptake']:.3f} deaths={d:,.0f} SROI={r:,.0f}x Δ={r/s0-1:+.1%}")

# Optimistic + unnotified private patients (outside notified denominator)
p = dict(BASE, adult_uptake=eff_uptake(0.20, 0.8, 0.8))
d, r = sroi(p, extra_treated=1.5e6 * 0.4 * 0.5)
print(f"Optimistic+unnotified    deaths={d:,.0f} SROI={r:,.0f}x Δ={r/s0-1:+.1%}")

# Breakevens
be_uptake = 0.60 * 2000 / s0
print(f"Breakeven eff. uptake {be_uptake:.3f} ({be_uptake/0.6-1:+.1%})")
print(f"Prior SROI at which a -10% cut crosses 2000x: {2000/0.9:,.0f}x")
```

**Output:**
```
Base: deaths 19,800, SROI 3,055x
Central                  eff=0.564 deaths=18,612 SROI=2,872x Δ=-6.0%
Retention pessimistic    eff=0.540 deaths=17,820 SROI=2,749x Δ=-10.0%
India-weighted           eff=0.510 deaths=16,830 SROI=2,597x Δ=-15.0%
Joint pessimistic        eff=0.460 deaths=15,180 SROI=2,342x Δ=-23.3%
Optimistic               eff=0.608 deaths=20,064 SROI=3,096x Δ=+1.3%
Optimistic+unnotified    deaths=21,864 SROI=3,373x Δ=+10.4%
Breakeven eff. uptake 0.393 (-34.5%)
Prior SROI at which a -10% cut crosses 2000x: 2,222x
```

**Simplifications:**
1. The global private share is a single weighted number rather than a country-by-country model.
2. Unnotified patients are assumed to have the same 6% baseline mortality, which is unknown and possibly higher.
3. Dose retention is applied through uptake rather than `relative_reduction`. The result is identical given the multiplicative chain.

--- Critique: Zero modeled lag between Phase III completion and adoption, and a speedup that assumes trial timing is the binding constraint ---

# Quantitative Impact Assessment: Zero Post-Phase III Adoption Lag and a Speedup That Assumes the Trial Is the Binding Constraint

## Critique

**Zero modeled lag between Phase III completion and adoption, and a speedup that assumes trial timing is the binding constraint.**

The critique has two separable parts:

- **(A) Lag.** Adding post-Phase III lag to `years_to_adoption`.
- **(B) Critical path.** Reducing expected `speedup_years` below 1, on the grounds that the trial may not be the binding constraint.

## Parameter Mapping

| Parameter | Model key | Current value | How it enters |
|---|---|---|---|
| Years from grant to adoption | `years_to_adoption` | 8 | `eligible = 5.5M × 0.98^(years_to_adoption − 8)` |
| Years of acceleration credited | `speedup_years` | 1 | Linear multiplier on benefit |
| Annual case decline | `decline_per_year` | 0.02 | Base of the lag penalty (held fixed here) |
| Discount rate | implicit | 0 | Owned by Thread 3; shown only as a cross-reference |

A structural point matters for (A). In a speedup framing, a post-Phase III lag delays adoption equally in the grant and no-grant worlds. So the lag does **not** remove the credited year. It only shifts that year to a later calendar time. Under the current formula, the only penalty is that fewer people have TB by then (the 2% per year decline), plus discounting if Thread 3 adds it. The formula captures this correctly.

## Plausible Ranges

**(A) Lag after Phase III: 0 to 5 years, central about 1 to 2 years.**

- **Low end (0 to 1 year).** HPMZ went from NEJM publication in May 2021 to a WHO rapid communication in June 2021. WHO endorsement was not the bottleneck.
- **High end (3 to 5 years).** National guideline adoption, procurement, and programme rollout plausibly add delay. The critique says HPMZ uptake was limited by cost and availability. That constraint applies less to generic atorvastatin, which caps the plausible lag.
- The Xpert precedent is unverified, so it is not used to set the range.

**(B) Expected speedup: 0.5 to 1.0 (pessimistic), central about 0.8 to 1.0. Optimistic range above 1.**

- **Why the downside is ungrounded.** It rests on Phase III funding or another factor being the gating step. The critique offers no evidence for this.
- **The verified evidence points the other way.** It says the delay in the HPMZ case "lay in trial execution and rapid generation of results." That supports the trial *being* on the critical path, which supports a speedup near 1.
- **Optimistic case.** If, without the grant, the Phase IIc would be delayed by more than one year or never run, the expected speedup could exceed 1. I test 1.5.
- **Lumpiness.** As the critique itself notes, lumpy decision cycles do not lower the expected speedup. I therefore apply no adjustment for it.

## Code

```python
import math

base = dict(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=1e5, speedup_years=1.0,
            all_in_cost=7e6, p_success=0.40)

def sroi(p, disc=0.0, lag=0):
    elig = p['eligible_people_at_8y']*(1-p['decline_per_year'])**(p['years_to_adoption']-8)
    deaths = elig*p['adult_uptake']*p['baseline_mortality']*p['relative_reduction']
    benefit = deaths*p['speedup_years']*p['dalys_per_death']*p['op_per_daly']
    benefit /= (1+disc)**lag          # discount only the added lag (Thread 3 cross-ref)
    return benefit/p['all_in_cost']*p['p_success']

B = sroi(base)
print(f"Base SROI {B:.0f}")
def run(lag=0, s=1.0, disc=0.0):
    p = dict(base, years_to_adoption=8+lag, speedup_years=s)
    v = sroi(p, disc, lag); return v, 100*(v/B-1)

for lag in [1,2,3,5]:
    print("lag",lag, "%.0f (%.1f%%)" % run(lag=lag), "| w/4%% disc %.0f (%.1f%%)" % run(lag=lag,disc=0.04))
for s in [0.5,0.7,0.8,0.9,1.5]:
    print("speedup",s,"%.0f (%.1f%%)" % run(s=s))
for lag,s in [(1,0.9),(2,0.8),(3,0.7),(5,0.5)]:
    print("joint",lag,s,"%.0f (%.1f%%)" % run(lag,s))
# break-even vs 2000x bar
m = 2000/B
print("speedup break-even", m, "| lag-only break-even yrs", math.log(m)/math.log(0.98))
for lag in [3,5]: print("speedup break-even at lag",lag, m/0.98**lag)
```

## Sensitivity Analysis

**Base case:** SROI 3,055x. Deaths averted 19,800 per year. Benefit $OP 53.46B. The funding bar is 2,000x.

### (A) Lag alone

| Added lag | SROI | Δ | With 4% discounting on the lag (Thread 3 cross-reference) |
|---|---|---|---|
| 1 yr | 2,994 | −2.0% | 2,879 (−5.8%) |
| 2 yr | 2,934 | −4.0% | 2,713 (−11.2%) |
| 3 yr | 2,875 | −5.9% | 2,556 (−16.3%) |
| 5 yr | 2,761 | −9.6% | 2,270 (−25.7%) |

Even with discounting included, SROI stays above 2,000x at 5 years of lag. With no discounting, the lag would have to reach about 21 years to push SROI below the bar.

### (B) Speedup alone

SROI is linear in the speedup.

| Speedup | SROI | Δ |
|---|---|---|
| 1.5 (optimistic) | 4,582 | +50% |
| 0.9 | 2,749 | −10% |
| 0.8 | 2,444 | −20% |
| 0.7 | 2,138 | −30% |
| 0.5 | 1,527 | −50% |

SROI falls below the 2,000x bar if the speedup is below **0.655**.

### Joint scenarios

The two effects multiply rather than add.

| Scenario (lag, speedup) | SROI | Δ |
|---|---|---|
| Mild (1 yr, 0.9) | 2,694 | −11.8% |
| Central-pessimistic (2 yr, 0.8) | 2,347 | −23.2% |
| Pessimistic (3 yr, 0.7) | 2,013 | −34.1%, at the bar |
| Extreme (5 yr, 0.5) | 1,381 | −54.8% |

Break-even speedup rises as lag increases:

- 0.655 with no added lag.
- 0.696 with 3 years of lag.
- 0.724 with 5 years of lag.

## Bottom-Line Impact

- **Lag component.** It reduces SROI by 2–10% across 1–5 years of lag (central about 2–4%). It does not threaten the 2,000x bar unless combined with heavy discounting, which belongs to Thread 3.
- **Critical-path component.** It is the only part that could be material. SROI moves 1:1 with expected speedup, giving a change of −50% to +50% across speedup 0.5–1.5. The downside is supported by no verified evidence, and the verified HPMZ evidence leans toward the trial being the binding constraint.
- **Combined.** A defensible central estimate is about 0 to −20% (SROI about 2,450–3,050x). The pessimistic joint case only reaches the bar at roughly 3 years of lag plus a speedup of 0.7.

## Materiality Verdict

**BORDERLINE.**

- **Lag alone: NO.** It is at most about 10% and has no effect on the decision.
- **Speedup: potentially YES.** It is decision-relevant only if the expected speedup is at or below about 0.65–0.72. Nothing in the verified evidence supports a speedup that low.

The highest-value follow-up is to establish what gates Phase III: funding for a generic drug, sponsor availability, or trial-site capacity. Only that evidence could move this critique from borderline to material.

--- Critique: Survivors' excess mortality and comorbidity shrink the 27 DALYs per death ---

# CRITIQUE: Survivors' excess mortality and comorbidity shrink the 27 DALYs per death

## Parameter mapping

| Parameter | Location | Current value | Affected? |
|---|---|---|---|
| `dalys_per_death` | Benefit line: deaths/yr × speedup × **dalys_per_death** × op_per_daly | 27 | **Primary** |
| `baseline_mortality` | Deaths/yr line | 0.06 | No. The critique concerns post-treatment survival, not on-treatment deaths. |
| All others | — | — | No |

**Model structure that matters:** SROI is strictly linear in `dalys_per_death`. No other term depends on it. So:

- SROI = 113.14 × `dalys_per_death`
- 3,054.9 / 27 = 113.14 SROI per DALY-per-death

The percentage change in `dalys_per_death` passes one-for-one into SROI. The break-even value against the 2,000x bar is:

- 27 × 2,000 / 3,054.9 = **17.68**, which is a **−34.5%** reduction.

This is the "17.7 threshold" the critique cites.

## Plausible range

The adjustment multiplier is m = (remaining healthy life expectancy of a TB survivor) / (the figure the 27 was built on).

**Gompertz effective ageing:** Δage = ln(SMR) / b.

| SMR (Romanowski 2019) | b = 0.09 | b = 0.10 |
|---|---|---|
| 2.21 (low CI) | 8.8 yr | 7.9 yr |
| 2.91 (pooled) | 11.9 yr | 10.7 yr |
| 3.84 (high CI) | 15.0 yr | 13.5 yr |

**Translating ageing into life-expectancy loss** (approximate LMIC life-table values, e.g. India or SSA WHO GHO tables, not taken from the CEA):

- e40 ≈ 30–34
- e48 ≈ 25–28
- e52 ≈ 22–25
- e55 ≈ 20–23

This implies a loss of about 17% at SMR 2.21, 20–27% at SMR 2.91, and 30–35% at SMR 3.84. These figures assume the SMR is constant for life.

**Moderating factors (push m toward 1):**
- The SMR plausibly attenuates with time since treatment and is typically lower at older ages, where baseline hazard is high.
- Part of the excess reflects HIV, smoking, alcohol and poverty, which an LMIC table already partly embeds.
- If 27 comes from a normative reference table (GBD convention), adjusting it for SMR is a methodological choice rather than a correction.

**Amplifying factors (push m below the SMR-only estimate):**
- Post-TB lung disease adds disability weight on the survived years. This matters if 27 is truly "healthy" life expectancy.
- Deaths averted by an adjunctive anti-inflammatory therapy are likely concentrated in the sickest patients, who are likely sicker than the average survivor in the SMR cohorts.
- If 27 corresponds to an older decedent (it equals roughly e62 on the GBD reference table), an 11-year shift gives about a −37% loss.

**Ranges used:**

| Scenario | Δ dalys_per_death | Value | Basis |
|---|---|---|---|
| Optimistic | 0% | 27 | 27 already reflects TB-cohort or LMIC mortality, or a normative table is deliberately kept |
| Mild | −5% to −10% | 24.3–25.7 | SMR attenuates or is partly embedded already |
| Central | −20% to −27% | 19.7–21.6 | Constant pooled SMR 2.91, Gompertz b = 0.09–0.10 |
| Pessimistic | −33% to −38% | 16.7–18.1 | SMR 3.84 (upper CI), plus about 5% post-TB disability |

No upward adjustment is supported by this critique. The "optimistic" case is simply no change.

## Sensitivity analysis

Base case: 19,800 deaths/yr, 534,600 DALYs, benefit $OP 53.46B, **SROI 3,055x**.

| dalys_per_death | DALYs credited | SROI | Δ vs base | vs 2,000x bar |
|---|---|---|---|---|
| 27.0 | 534,600 | 3,055x | 0% | 1.53× |
| 25.7 (−5%) | 508,900 | 2,902x | −5% | above |
| 24.3 (−10%) | 481,100 | 2,749x | −10% | above |
| 21.6 (−20%) | 427,700 | 2,444x | −20% | above |
| 19.7 (−27%) | 390,100 | 2,229x | −27% | above (by 11%) |
| 18.1 (−33%) | 358,400 | 2,047x | −33% | barely above |
| 17.68 (−34.5%) | 350,100 | 2,000x | −34.5% | **break-even** |
| 16.7 (−38%) | 330,700 | 1,890x | −38% | **below** |

**Joint effects.** Only one parameter is moved by this critique. Its interaction with other critiques is **multiplicative**, because every term in the formula chain is a product.

Additional reduction from other critiques needed to cross 2,000x, given this critique's adjustment:

| This critique's adjustment | Additional reduction needed |
|---|---|
| None | ≥34.5% |
| −10% (SROI 2,749x) | ≥27% |
| −20% (2,444x) | ≥18% |
| −27% (2,229x) | ≥10% |

Some examples of what would supply that reduction:
- `relative_reduction` falling from 0.10 to 0.08 is −20%.
- `adult_uptake` falling from 0.60 to 0.50 is −17%.
- A modest discount rate over the 8-year horizon would also contribute.

## Bottom-line impact

**This critique plausibly reduces SROI by 0–38%, with a central estimate of −20% to −27% (3,055x → about 2,230–2,440x).** On its own it crosses the 2,000x bar only at the pessimistic tail (constant upper-CI SMR plus disability). Combined with any other ≥10–18% downward adjustment, it does cross the bar.

## Materiality verdict

**YES on magnitude, BORDERLINE on decision relevance.**

- The central effect of about 20–27% is well above a typical 10% materiality line.
- It does not flip the funding decision alone; that requires a reduction of at least 34.5%.
- It substantially narrows the margin for other critiques.
- Resolving how 27 was derived is the highest-value check:
  - an LMIC general-population HALE at age about 40 implies the central case applies;
  - a GBD reference table at age about 60 implies the pessimistic case, but it is arguably exempt by convention;
  - a TB-cohort table implies about 0%.

## Code

```python
import numpy as np

# Base parameters from the CEA
P = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
         all_in_cost=7_000_000, p_success=0.40)

def sroi(p):
    # Replicates the CEA formula chain
    elig = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    deaths = elig * p['adult_uptake'] * p['baseline_mortality'] * p['relative_reduction']
    dalys = deaths * p['speedup_years'] * p['dalys_per_death']
    benefit = dalys * p['op_per_daly']
    return deaths, dalys, benefit / p['all_in_cost'] * p['p_success']

d0, D0, S0 = sroi(P)
print(f"Base: deaths={d0:,.0f} DALYs={D0:,.0f} SROI={S0:,.1f}x")  # 19,800 / 534,600 / 3,054.9x
print("Break-even dalys_per_death:", 27 * 2000 / S0)               # 17.68

# Gompertz effective ageing for each SMR and slope b
for smr in (2.21, 2.91, 3.84):
    for b in (0.09, 0.10):
        print(f"SMR {smr}, b={b}: shift = {np.log(smr)/b:.1f} yr")

# Life-expectancy loss under a Gompertz-Makeham table calibrated to e40 ~ 32
def e_x(x, A=0.004, B=4.5e-5, b=0.095, k=1.0, maxage=110):
    ages = np.arange(x, maxage, 0.1)
    mu = k * (A + B * np.exp(b * ages))
    S = np.exp(-np.cumsum(mu) * 0.1)
    return S.sum() * 0.1

for k in (1.0, 2.21, 2.91, 3.84):
    print(f"k={k}: e40={e_x(40, k=k):.1f}  ratio={e_x(40, k=k)/e_x(40):.2f}")
# Note: applying a constant multiplier to the Makeham term as well slightly overstates the loss

# SROI under each scenario
for pct in (0, -0.05, -0.10, -0.20, -0.27, -0.33, -0.345, -0.38):
    q = dict(P, dalys_per_death=27 * (1 + pct))
    _, D, S = sroi(q)
    print(f"{pct:+.1%}: dpd={q['dalys_per_death']:.1f} DALYs={D:,.0f} "
          f"SROI={S:,.0f}x  Δ={S/S0-1:+.1%}")

# Additional reduction needed from other critiques to reach the 2,000x bar
for pct in (0, -0.10, -0.20, -0.27):
    S = S0 * (1 + pct)
    print(f"after {pct:+.0%}: additional cut to bar = {1 - 2000/S:.1%}")
```

**Simplifications:**
- The life-table step uses a calibrated Gompertz-Makeham table and approximate WHO LMIC values, not a country-specific table. The SMR-to-life-expectancy mapping is therefore approximate to about ±3 percentage points.
- The SROI step reproduces the CEA formula exactly.

--- Critique: The 6% is a mix of deaths, and only a fraction is reachable and modifiable by atorvastatin ---

# Impact Assessment: Addressable Share of the 6% Baseline Mortality

## Parameter mapping

The BOTEC is a pure product chain:

SROI = eligible × uptake × **baseline_mortality** × **relative_reduction** × speedup × DALYs × $/DALY ÷ cost × p_success

The critique adds an addressable-share multiplier, *h*. Because baseline_mortality and relative_reduction sit in the same product, applying *h* to either one gives the same result. The critique is therefore really a question about what population the 10% applies to.

The affected parameters are:

- **baseline_mortality** (current 0.06) becomes 0.06 × *h*
- **relative_reduction** (current 0.10) becomes 0.10 × *h*, which is the same thing
- *h* = s_timing × s_TB-attributable × s_eligible, a new parameter that is implicitly 1.0 in the current model.

Baseline SROI is **3,055x**: 5.5M × 0.6 × 0.06 × 0.10 = 19,800 deaths/yr → 534,600 DALYs → $OP 53.46B ÷ $7M × 0.4.

**Break-even.** SROI reaches the 2,000x bar at *h* = 2,000 / 3,055 = **0.655**. That is an effective baseline of **3.93%**, which confirms the critique's 3.9% figure. If more than about 35% of the 6% is unaddressable, the grant falls below the bar, with everything else held at CG values.

## Plausible ranges

These ranges are informed by the verified evidence but remain judgment-based. The critique itself labels its shares as placeholders.

| Component | Low | Central | High | Basis |
|---|---|---|---|---|
| s_timing (deaths after statin could act) | 0.5 | 0.8 | 1.0 | About 75% of on-treatment deaths fall in months 1–2 in Zambia; Ethiopia and Cameroon show a similar pattern. However, atorvastatin starts on day 1, so only the very earliest deaths (roughly weeks 0–3) are plausibly unreachable. The direction of the rifampicin interaction is UNGROUNDED. 1.0 = statin acts immediately. |
| s_TB (TB-attributable and statin-responsive) | 0.7 | 0.85 | 1.0 | In HIV-coinfected cohorts, a substantial share of deaths are HIV-, comorbidity- or other-cause. TB is frequently contributory, so 1.0 is not excluded. |
| s_eligible (deaths occurring in statin-eligible patients) | 0.8 | 0.9 | 1.0 | Groups excluded on safety grounds (liver disease, pregnancy, critically ill, boosted-PI ART) are a small share of patients. They are over-represented among deaths, as the Taiwan malnutrition data confined to the first 8 weeks suggests. |
| **h (product)** | **0.28** | **0.61** | **1.0** | Multiplicative |

**Double-counting switch, q.** This is the probability that the haircut legitimately applies, meaning the 10% represents the effect among reachable deaths rather than a cohort-wide average. The 10% has no stated derivation; the prior trial measured surrogates, not mortality. As a result, q cannot be pinned down. I sweep q from 0 to 1.

## Sensitivity analysis

SROI = 3,055 × *h*. All values below are exact for this linear model.

**Individual components (others held at 1.0):**

| Scenario | Effective baseline | SROI | Δ |
|---|---|---|---|
| Base | 6.00% | 3,055x | — |
| s_timing = 0.5 / 0.8 | 3.00% / 4.80% | 1,527x / 2,444x | −50% / −20% |
| s_TB = 0.7 / 0.85 | 4.20% / 5.10% | 2,138x / 2,597x | −30% / −15% |
| s_eligible = 0.8 / 0.9 | 4.80% / 5.40% | 2,444x / 2,749x | −20% / −10% |

**Joint scenarios (effects are multiplicative, not additive):**

| Scenario | h | Effective baseline | SROI | Δ |
|---|---|---|---|---|
| All central | 0.612 | 3.67% | 1,870x | −38.8% |
| Critique's illustration (0.7 × 0.85) | 0.595 | 3.57% | 1,818x | −40.5% |
| All pessimistic | 0.28 | 1.68% | 855x | −72% |
| Optimistic (no haircut / already embedded in the 10%) | 1.0 | 6.00% | 3,055x | 0% |

**Optimistic direction.** I tested this to apply the rule of testing both directions:

- **Statin reaches early deaths** (s_timing = 1, others central): h = 0.765 → **2,337x** (−23.5%).
- **Unascertained deaths raise the true baseline to 7%,** combined with central h: effective baseline is 4.28% → **2,182x** (−28.6%). Under-ascertainment partly offsets the haircut.

**Probability-weighting over the double-counting question,** using E[m] = q·h + (1−q):

| q | Central h = 0.612 | Pessimistic h = 0.28 |
|---|---|---|
| 0.25 | 2,759x (−9.7%) | 2,505x (−18%) |
| 0.50 | 2,462x (−19.4%) | 1,955x (−36%) |
| 0.75 | 2,166x (−29.1%) | 1,405x (−54%) |

The bar is crossed when q > 0.89 with central h, or when q > 0.48 with pessimistic h.

**Interaction with other threads.** Because everything is multiplicative, any other critique that independently cuts SROI by a factor *k* raises the break-even *h* to 0.655 / *k*. For example, a 20% cut from an uptake ramp or discounting means *h* must stay at or above 0.82. Under that condition, even the central haircut (0.61) is well below the bar.

## Bottom-line impact

If CG's 10% is read as the effect among statin-reachable deaths, this critique reduces SROI by **20–72%**, with a central estimate of **−39%** (3,055x → ~1,870x, below the 2,000x bar). If the 10% is already a cohort-average effect, the impact is **0%**. Weighting the two readings 50/50 gives a central estimate of about **−19%** (~2,460x), with a range of **−10% to −54%** across q and h.

## Materiality verdict: YES (conditional)

- The plausible range clearly straddles the 2,000x bar.
- The central joint haircut alone pushes the estimate below the bar.
- The break-even addressable share (65.5%) sits inside the plausible range of 28–100%.

The decisive unknown is not the decomposition shares. It is what population CG's 10% refers to. CG should either:

1. state that the 10% is a cohort-wide average effect on all on-treatment deaths and defend it as such, which absorbs this critique into Thread 1 (relative_reduction); or
2. adopt an explicit addressable-share term.

Until then, the BOTEC cannot be said to clear the bar robustly on this dimension. This is especially true once the multiplicative interaction with other threads is considered.

## Code

```python
import numpy as np

P = dict(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=1e5, speedup_years=1,
         all_in_cost=7e6, p_success=0.40)

def sroi(p, h=1.0):
    elig = p['eligible_people_at_8y']*(1-p['decline_per_year'])**(p['years_to_adoption']-8)
    treated = elig*p['adult_uptake']
    deaths = treated*p['baseline_mortality']*h*p['relative_reduction']
    benefit = deaths*p['speedup_years']*p['dalys_per_death']*p['op_per_daly']
    return benefit/p['all_in_cost']*p['p_success']

base = sroi(P)                         # 3054.9
print("base", round(base), "break-even h", round(2000/base, 3))  # 0.655

comps = {'timing':(0.5,0.8,1.0), 'tb':(0.7,0.85,1.0), 'elig':(0.8,0.9,1.0)}
for k,(lo,c,hi) in comps.items():
    for v in (lo,c):
        s = sroi(P, v); print(k, v, round(s), f"{s/base-1:+.1%}")

for name,h in [('central',0.8*0.85*0.9),('illustrative',0.7*0.85),
               ('pessimistic',0.5*0.7*0.8),('early-reach',1*0.85*0.9)]:
    s = sroi(P,h); print(name, round(h,3), f"{0.06*h:.2%}", round(s), f"{s/base-1:+.1%}")

# under-ascertainment offset
P7 = dict(P, baseline_mortality=0.07)
print("7% baseline, central h:", round(sroi(P7, 0.612)))   # ~2182

# double-counting weighting
for q in (0.25,0.5,0.75):
    for h in (0.612,0.28):
        m = q*h+(1-q); print(q,h,round(base*m), f"{m-1:+.1%}")
print("q break-even central:", (1-2000/base)/(1-0.612))   # ~0.89

# Optional Monte Carlo (triangular components, independent)
rng = np.random.default_rng(0); N = 200_000
h = (rng.triangular(0.5,0.8,1.0,N)*rng.triangular(0.7,0.85,1.0,N)
     *rng.triangular(0.8,0.9,1.0,N))
print("MC mean SROI", round(base*h.mean()), "P(>=2000x)", (base*h>=2000).mean())
```

I computed the deterministic figures above by hand from the formula chain. The Monte Carlo was not executed here. Analytically, its mean is about 0.587 × 3,055 ≈ 1,790x, and I expect P(SROI ≥ 2,000x) to come out roughly in the 0.2–0.35 range. Re-run the code to confirm.

--- Critique: Under-ascertained deaths push true mortality up, and the direction is the opposite of Critiques 1–2 ---

# Impact Assessment: Under-ascertained deaths among LTFU and not-evaluated patients

## Parameter mapping

| Parameter | Model key | Current value | Affected? |
|---|---|---|---|
| Mortality among treated DS-TB patients | `baseline_mortality` | 0.06 | **Primary.** The critique argues the true value is higher. |
| Statin-reachable share of the added deaths | none (implicit 1.0) | n/a | **New modifier.** Deaths after treatment interruption are probably not fully reachable by an adjunct that is also interrupted. |
| Relative reduction | `relative_reduction` | 0.10 | Only via the modifier above. I fold the modifier into an effective Δ`baseline_mortality` rather than changing `relative_reduction`, so the base-cohort effect is untouched. |

**Model structure check.** The formula chain is fully multiplicative. With `years_to_adoption` = 8, the decline term is (0.98)^0 = 1. So:

SROI = 5.5M × 0.6 × m × 0.10 × 1 × 27 × 100,000 / 7M × 0.4 = **50,915 × m**

- That is **509.1x per percentage point** of mortality.
- SROI is exactly proportional to `baseline_mortality`, so relative changes in SROI equal relative changes in m.

## Plausible range

I model the effective mortality as:

m_eff = 0.06 + (LTFU+NE share) × (mortality among LTFU+NE) × f

where f is the fraction of those added deaths that a statin adjunct could plausibly prevent.

**LTFU + not-evaluated share: 6% to 8.4%.**
- The Kenyan surveillance figure is 8.4% (verified).
- The critique's 6–7% is illustrative.
- The global WHO share is UNVERIFIED.

**Mortality among LTFU + NE: 5% to 20%.**
- Kilifi tracing found about 10%. This is DS-dominant and the most applicable source.
- The DR-TB figures (23–30%) are not applicable to a DS-only model, so I cap at 20%.
- The lower bound of 5% allows for NE patients, who are often transfers and have lower risk.

**Raw Δm: +0.3 to +1.4 pp.** This is the critique's range and is consistent with 8.4% × 10% = 0.84 pp.

**Attribution f: 0 to 1, central 0.3–0.5.**
- The Verifier noted that the timing of deaths among LTFU patients undermines on-treatment attribution.
- Patients who drop TB drugs very likely drop the adjunct statin too.
- Some deaths will occur before LTFU while the patient is still taking the statin, so f is greater than 0.

## Sensitivity analysis

**Base case:** 19,800 deaths averted per year, 534,600 DALYs, **SROI = 3,055x**.

**One-way, Δm with full attribution (f = 1):**

| Raw Δm | m | Deaths/yr | SROI | Δ |
|---|---|---|---|---|
| +0.3 pp | 6.3% | 20,790 | 3,208x | +5.0% |
| +0.6 pp | 6.6% | 21,780 | 3,360x | +10.0% |
| +0.84 pp (Kenya 8.4% × 10%) | 6.84% | 22,572 | 3,483x | +14.0% |
| +1.4 pp | 7.4% | 24,420 | 3,768x | +23.3% |

**Joint, Δm × f (the effects multiply because the model is linear in m):**

| f | Δm = 0.3 pp | Δm = 0.84 pp | Δm = 1.4 pp |
|---|---|---|---|
| 0 | 3,055x (0%) | 3,055x (0%) | 3,055x (0%) |
| 0.25 | 3,093x (+1.3%) | 3,162x (+3.5%) | 3,233x (+5.8%) |
| 0.5 | 3,131x (+2.5%) | 3,269x (+7.0%) | 3,411x (+11.7%) |
| 1.0 | 3,208x (+5.0%) | 3,483x (+14.0%) | 3,768x (+23.3%) |

**Central estimate** (Δm ≈ 0.84 pp, f ≈ 0.3–0.5): SROI ≈ **3,183x–3,269x (+4% to +7%)**.

**Both directions:**
- **Upward:** the most favourable case is +23%, which requires Δm = 1.4 pp and full attribution.
- **Downward:** this critique has no downward channel. Its floor is 0% when f = 0.
  - It can only lower SROI indirectly, if correcting the cohort data also revealed that the 6% overstates on-treatment deaths. That belongs to Critiques 1–2, not this one.
  - If the global WHO "died" share is actually below 6%, it compounds with those critiques rather than with this one.

**Interaction with Critiques 1–2 (opposite direction):**
- Effects combine multiplicatively on m.
- For example, a −15% adjustment from Critiques 1–2 combined with +7% here gives a net effect of about −9%: 0.85 × 1.07 = 0.91, so SROI ≈ 2,778x.
- This critique therefore partially offsets, but does not cancel, plausible downward adjustments.

**Funding bar:**
- SROI would need to fall 34.5% to reach 2,000x, which requires m below 3.93%.
- This critique moves SROI away from the bar, so it cannot change a funding decision on its own.

## Bottom-line impact

**This critique could raise SROI by 0% to +23% (3,055x → up to 3,768x), with a central estimate of about +4% to +7% (≈3,180x–3,270x) once the statin-attributable share of post-interruption deaths is discounted.**

## Materiality verdict

**BORDERLINE, leaning NO.**

- The thread spec's threshold was not supplied. I assumed roughly 10% change in SROI or any change in the decision relative to the 2,000x bar.
- The upper bound (+23%) clears a 10% threshold, but it requires full attribution, which the Verifier's own evidence undermines.
- The central estimate (+4% to +7%) is below 10%.
- The direction is favourable to the grant, so it cannot flip the decision.
- Its main value is as a **partial offset** to Critiques 1–2 when the mortality adjustments are netted.
- The highest-value follow-up is an estimate of f: the share of deaths among LTFU patients that occur while they are still on treatment. The verification step did not produce this, and it was not available to me. The LTFU fraction is a secondary priority.

## Code

```python
import itertools

P = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
         all_in_cost=7_000_000, p_success=0.40)

def sroi(p):
    eligible = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    treated = eligible * p['adult_uptake']
    deaths = treated * p['baseline_mortality'] * p['relative_reduction']
    benefit = deaths * p['speedup_years'] * p['dalys_per_death'] * p['op_per_daly']
    return benefit / p['all_in_cost'] * p['p_success'], deaths

base, d0 = sroi(P)
print(f"Base: deaths/yr={d0:,.0f}  SROI={base:,.1f}x")   # 19,800 ; 3,054.9x

def run(dm_pp, f=1.0):
    q = dict(P); q['baseline_mortality'] = 0.06 + dm_pp/100 * f
    s, d = sroi(q)
    return s, d, (s/base - 1)*100

print("\nOne-way (f=1):")
for dm in [0.3, 0.6, 0.84, 1.0, 1.4]:
    s, d, pct = run(dm)
    print(f"  dm=+{dm:.2f}pp  m={6+dm:.2f}%  deaths={d:,.0f}  SROI={s:,.0f}x  ({pct:+.1f}%)")

print("\nJoint dm x f:")
for f in [0, 0.25, 0.5, 1.0]:
    row = [f"{run(dm, f)[0]:,.0f}x ({run(dm, f)[2]:+.1f}%)" for dm in [0.3, 0.84, 1.4]]
    print(f"  f={f:<4}", " | ".join(row))

# Derived range from component ranges
print("\nComponent-derived dm (pp):")
for share, mort in itertools.product([0.06, 0.084], [0.05, 0.10, 0.20]):
    print(f"  LTFU+NE={share:.1%} x mort={mort:.0%} -> +{share*mort*100:.2f}pp")

# Distance to funding bar
print(f"\nm needed for SROI=2000x: {2000/base*0.06:.4f}  (SROI drop needed: {(1-2000/base)*100:.1f}%)")

# Netting with a hypothetical -15% from Critiques 1-2
print(f"Net with -15% (C1-2) and +7% (this): {base*0.85*1.07:,.0f}x")
```

--- Critique: Covariance between mortality and DALYs per death means the product of means is not the mean of the product ---

# CRITIQUE: Covariance between mortality and DALYs per death means the product of means is not the mean of the product

## Parameter mapping

The model computes `benefit = treated × baseline_mortality × relative_reduction × dalys_per_death × …`. Every term is multiplicative, so SROI is exactly linear in `dalys_per_death`. The critique therefore maps onto one effective parameter: DALYs per averted death, D_eff.

| Parameter | Location | Current value | How the critique affects it |
|---|---|---|---|
| `dalys_per_death` | Benefit term | 27 | Should be weighted by averted deaths, not by persons |
| `baseline_mortality` | Deaths/yr term | 0.06 | Unchanged as an aggregate, but its distribution across subgroups drives the weighting |
| `relative_reduction` | Deaths/yr term | 0.10 | If it varies by subgroup, it re-weights D_eff (secondary channel) |

The correct quantity is:

  D_eff = Σ nᵍ·mᵍ·rᵍ·Dᵍ / Σ nᵍ·mᵍ·rᵍ

where, for subgroup g, n is the share of treated patients, m is on-treatment mortality, r is the statin's relative mortality reduction and D is DALYs per death.

Suppose `relative_reduction` is interpreted as the trial's aggregate reduction in deaths. Then the deaths-averted count is unaffected, and only D_eff can be biased. The SROI multiplier is D_eff / 27.

## Plausible range

The key question is what 27 represents. I tested this with an illustrative age-stratified cohort, which reproduces about 6% mortality.

**Assumptions for the illustrative cohort.** These are not sourced data:
- Age mix and age-specific case fatality are WHO-pattern-like.
- Remaining life expectancy uses a high-burden-country life table.

**Results.**
- **Person-weighted mean D = 32.7.** This is the number you would get from an "average patient" calculation.
- **Death-weighted D = 25.3.** This is the number you would get from total DALYs divided by total deaths.
- **The ratio of the two is 0.773.**

The reported value of 27 sits close to the death-weighted figure and far from the person-weighted one. It is also well below what GBD's reference life table would give, which is in the mid-30s. This suggests 27 was derived as remaining life expectancy at a typical age of TB death, which is effectively death-weighted. That is the case where the critique says the bias "largely disappears."

This inference rests on assumed inputs. It shifts probability toward the benign case but does not settle it.

| Scenario | D_eff / 27 multiplier | Basis |
|---|---|---|
| A. 27 is already death-weighted, r homogeneous | 1.00 (±~3% Jensen gap) | Inference above |
| A + HIV (8% HIV+, 11% mortality, D≈30) | 1.026 | Global-average TB/HIV mix (illustrative) |
| A + high-HIV setting | ~1.05–1.10 | The critique's reversal case |
| A + r rising with age (0.06→0.14, rescaled to aggregate 0.10) | 0.898 | Statin benefit concentrated in older patients |
| A + r falling with age (0.14→0.06) | 1.127 | Anti-inflammatory benefit concentrated in younger patients |
| B. 27 is person-weighted (critique's illustration) | 0.88 | Critique's mechanism |
| B. 27 is person-weighted (my stratification) | 0.773 | Ratio 25.3 / 32.7 |

## Sensitivity analysis

**Base case:** 19,800 deaths averted per year × 27 = 534,600 DALYs, giving an SROI of **3,055x**. The bar is 2,000x.

| Case | Effective dalys_per_death | SROI | Δ |
|---|---|---|---|
| Base | 27.0 | 3,055x | — |
| B, critique illustration | 23.8 | 2,688x | −12% |
| B, my stratification | 20.9 | 2,361x | −23% |
| A, r rising with age | 24.2 | 2,743x | −10% |
| A, global HIV mix | 27.7 | 3,134x | +3% |
| A, r falling with age | 30.4 | 3,443x | +13% |
| **Joint pessimistic** (B 0.773 × r-rising 0.898) | 18.7 | **2,120x** | **−31%** |
| Joint pessimistic + unverified survivor-life-expectancy haircut (×0.85, a separate critique) | 15.9 | 1,802x | −41% |
| Joint optimistic (A, high-HIV, r falling with age) | ~32–33 | ~3,700x | +20% |

**Interactions.** The weighting effects are multiplicative with each other. They are fully separable from all other parameters, because SROI is linear in D_eff.

**Break-even.** SROI falls to 2,000x at dalys_per_death = 27 × 2,000 / 3,055 = **17.7**, a 34.5% reduction. No single covariance channel reaches this. Only stacking with the separate excess-mortality critique does.

## Bottom-line impact

The effect is roughly −23% to +13% on SROI from this critique alone (joint range −31% to +20%). The central estimate is about 0% to −5%, because the value of 27 looks consistent with an already death-weighted figure. If 27 was instead a person-weighted average, the impact would be −12% to −23%.

## Materiality verdict

**BORDERLINE.**
- The plausible swing (±10–25%) is large enough to matter as a modelling correction.
- However, the sign is uncertain, and the most likely derivation of 27 implies near-zero bias.
- No scenario from this critique alone pushes SROI below the 2,000x bar.
- It becomes decision-relevant only if combined with the survivors' excess-mortality adjustment and an age-gradient in statin effect.

**Resolution:** ask CG how 27 was derived. Alternatively, compute GBD age- and HIV-stratified YLL per TB death for the target countries, using local rather than reference life tables.

## Code

```python
# --- GiveWell/CG model, exact formula chain ---
P = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
         all_in_cost=7_000_000, p_success=0.40)

def sroi(p):
    elig = p['eligible_people_at_8y']*(1-p['decline_per_year'])**(p['years_to_adoption']-8)
    deaths = elig*p['adult_uptake']*p['baseline_mortality']*p['relative_reduction']
    benefit = deaths*p['speedup_years']*p['dalys_per_death']*p['op_per_daly']
    return benefit/p['all_in_cost']*p['p_success']

base = sroi(P)  # 3054.86

# --- Illustrative stratification (ASSUMED inputs, not sourced) ---
share = [.15,.22,.20,.18,.14,.11]          # age 15-24 ... 65+
mort  = [.02,.03,.045,.065,.09,.14]        # on-treatment CFR by age -> mean ~0.058
LE    = [52,43,34,26,19,12]                # remaining life expectancy at death

def d_eff(share, mort, LE, r=None):
    r = r or [1]*len(share)
    w = [s*m*ri for s,m,ri in zip(share,mort,r)]
    return sum(wi*L for wi,L in zip(w,LE))/sum(w)

person_w = sum(s*L for s,L in zip(share,LE))             # 32.7
death_w  = d_eff(share,mort,LE)                          # 25.3
r_up     = d_eff(share,mort,LE,[.06,.076,.092,.108,.124,.14])   # 22.7 (scale-invariant in r)
r_down   = d_eff(share,mort,LE,[.14,.124,.108,.092,.076,.06])   # 28.5

# HIV mix: 8% HIV+, CFR 11%, D=30
hivneg_deaths = sum(s*m for s,m in zip(share,mort))*0.92
hiv_deaths = 0.08*0.11
d_hiv = (hivneg_deaths*death_w + hiv_deaths*30)/(hivneg_deaths+hiv_deaths)  # ~25.95

mult = {
 'B_critique': 23.8/27,
 'B_strat': death_w/person_w,          # 0.773
 'A_r_up': r_up/death_w,               # 0.898
 'A_r_down': r_down/death_w,           # 1.127
 'A_hiv': d_hiv/death_w,               # 1.026
 'joint_pess': (death_w/person_w)*(r_up/death_w),   # 0.694
}
mult['joint_pess_plus_LE'] = mult['joint_pess']*0.85

for k,m in mult.items():
    q = dict(P, dalys_per_death=27*m)
    print(f"{k:22s} D={27*m:5.1f}  SROI={sroi(q):7.0f}  Δ={m-1:+.1%}")

print("break-even dalys_per_death for 2000x:", 27*2000/base)   # 17.7
```

--- Critique: A global-average mortality may not match the countries where an atorvastatin adjunct would actually be deployed ---

# CRITIQUE: A global-average mortality may not match the countries where an atorvastatin adjunct would actually be deployed

## Parameter mapping

| Parameter | Model key | Current value | Role in formula |
|---|---|---|---|
| On-treatment mortality, drug-susceptible TB | `baseline_mortality` | 0.06 | Linear multiplier on deaths averted, so SROI ∝ baseline_mortality |
| Uptake (indirect) | `adult_uptake` | 0.60 | Country-level uptake decides *which* mortality gets weighted |
| Relative reduction (indirect) | `relative_reduction` | 0.10 | Matters if higher deployment-country mortality is HIV-driven and less reachable by a statin |

**Structural point the critique does not make explicit.** `eligible_people_at_8y` (5.5M) is a global caseload. If 6% is already a case-weighted global figure, then a uniform 60% uptake everywhere makes 6% the correct input, and there is no bias. The critique only bites through **covariance between country uptake and country mortality**. So the correct formulation is:

> effective_mortality = Σ (cases_i × uptake_i × m_i) / Σ (cases_i × uptake_i)

with Σ cases_i × uptake_i held at 0.60 × total. I model it this way rather than simply swapping in a single "India" or "South Africa" figure.

## Plausible range

- **Central:** 6.0%, which is CG's value. No verified evidence moves it.
- **Pessimistic:** about 4.5%. This assumes adoption is concentrated in lower-reported-mortality, high-burden Asian settings. The critique's India figure of 4–5% is UNVERIFIED.
- **Optimistic:** about 8%. This assumes adoption is concentrated in high-HIV African settings. The critique's South Africa figure of 8–10% is UNVERIFIED. The optimistic end is partly offset if the extra deaths are HIV-related and unreachable by a statin.
- **Break-even:** baseline_mortality = 0.06 × 2000/3055 = **3.93%**. This matches the critique's 3.9% threshold.

The basis for all country figures is ungrounded. The range is a scenario band, not an evidence-derived interval.

## Sensitivity analysis

Base case: 19,800 deaths averted per year. SROI = **3,055x** against a 2,000x bar.

**A. Direct substitution of baseline_mortality (SROI is linear in it)**

| baseline_mortality | SROI | Δ vs base |
|---|---|---|
| 3.93% (break-even) | 2,000x | −34.5% |
| 4.0% | 2,037x | −33.3% |
| 4.5% (India-dominated) | 2,291x | −25.0% |
| 5.0% | 2,546x | −16.7% |
| 6.0% (base) | 3,055x | 0 |
| 7.0% | 3,564x | +16.7% |
| 8.0% (high-HIV-dominated) | 4,073x | +33.3% |
| 10.0% | 5,091x | +66.7% |

**B. Uptake–mortality covariance (the mechanism done properly)**

This is a two-group illustration. Group L holds 70% of cases at m = 4.5%. Group H holds 30% of cases at m = 9.5%. The case-weighted global average is 6.0%. Average uptake is held at 0.60 in every scenario.

| Scenario | Uptake L / H | Effective m | SROI | Δ |
|---|---|---|---|---|
| Uniform uptake | 0.60 / 0.60 | 6.00% | 3,055x | 0% |
| H adopts faster (e.g., donor-driven HIV-setting rollout) | 0.50 / 0.833 | 6.58% | 3,352x | +9.7% |
| L adopts faster | 0.70 / 0.367 | 5.42% | 2,758x | −9.7% |
| Only L adopts (extreme) | 0.857 / 0 | 4.50% | 2,291x | −25.0% |
| Only H adopts (extreme) | 0 / 1.0 (capped) | 9.5% | 4,837x* | +58% (*uptake cap binds: treated falls to 30%, so net SROI = 2,419x, −21%) |

**C. Joint test with HIV-reachability (interacts with relative_reduction)**

Take the high scenario, m = 8%. If half of the 2-point excess over 6% is HIV-attributable deaths that a statin cannot avert, effective reachable mortality is 7%. SROI is then 3,564x (+16.7%) rather than +33%. The effects are multiplicative, since deaths = treated × m × RR × reachable fraction. This roughly halves the upside but leaves the downside untouched.

## Bottom-line impact

**Δ ≈ −25% to +33% under the critique's own extreme scenarios. Under realistic uptake–mortality covariance it is about ±10%, with central estimate 0% and direction unknown.** SROI stays above the 2,000x bar unless effective mortality falls below 3.93%. That would require deployment mortality lower than even the critique's pessimistic India-dominated case.

## Materiality verdict

**BORDERLINE.**

- **Why it could be material:** the magnitude is non-trivial, with a ±10–25% swing on a linear parameter.
- **Why it does not clear the bar on its own:**
  - It does not flip the funding decision on its own.
  - It has no demonstrated direction.
  - All country inputs are ungrounded.
- **Why it matters anyway:** it compounds multiplicatively with other downside critiques. The −25% case leaves only about 13% headroom to the bar.

The verifier's retention condition still applies. Pull the WHO Global TB Report cohort outcomes (death share among evaluated new/relapse cases) for India, Indonesia, Philippines, Pakistan, Nigeria, DRC and South Africa. Also note that reported cohort death shares understate true mortality because of loss to follow-up and unevaluated cases. That understatement biases *upward* relative to reported figures, and it partially counters the pessimistic scenario.

## Code

```python
base = dict(eligible=5.5e6, years=8, decline=0.02, uptake=0.60, m=0.06,
            rr=0.10, dalys=27, op=1e5, speed=1, cost=7e6, p=0.40)

def sroi(**kw):
    q = {**base, **kw}
    elig = q['eligible'] * (1 - q['decline'])**(q['years'] - 8)
    deaths = elig * q['uptake'] * q['m'] * q['rr']
    return deaths * q['speed'] * q['dalys'] * q['op'] / q['cost'] * q['p']

B = sroi(); print(f"base {B:.0f}x, breakeven m = {0.06*2000/B:.4f}")
for m in [0.0393, 0.04, 0.045, 0.05, 0.06, 0.07, 0.08, 0.10]:
    s = sroi(m=m); print(f"m={m:.4f}: {s:.0f}x ({s/B-1:+.1%})")

# Uptake-mortality covariance, two groups, global avg m = 6%
shares, ms = [0.7, 0.3], [0.045, 0.095]
for uL, uH in [(0.6, 0.6), (0.5, 0.8333), (0.7, 0.3667), (0.857, 0.0), (0.0, 1.0)]:
    w = [shares[0]*uL, shares[1]*uH]; tot = sum(w)
    m_eff = (w[0]*ms[0] + w[1]*ms[1]) / tot
    s = sroi(m=m_eff, uptake=tot)        # uptake = realized avg uptake
    print(f"uL={uL}, uH={uH}: m_eff={m_eff:.4f}, uptake={tot:.3f}, "
          f"{s:.0f}x ({s/B-1:+.1%})")

# HIV-reachability joint test: m=8%, half of excess unreachable
m_reach = 0.06 + 0.5*(0.08 - 0.06)
print(f"reachable m={m_reach}: {sroi(m=m_reach):.0f}x ({sroi(m=m_reach)/B-1:+.1%})")
```

Output reproduces base 3,055x, break-even 0.0393, and the tables above.

--- Critique: Industry phase-transition base rates put "II and III both succeed" at roughly 15–25%, so 40% requires an unstated premium of about 1.6–2.7× ---

# CRITIQUE: Industry phase-transition base rates imply P(Phase II and III both succeed) ≈ 15–32%, below CG's 0.40

## Parameter Mapping

| Parameter | Location | Current value | Role |
|---|---|---|---|
| **p_success** (primary) | Final multiplier in the SROI formula | 0.40 | Enters linearly: SROI = benefit / all_in_cost × p_success |
| adult_uptake (secondary) | treated = eligible × adult_uptake | 0.60 | Risk of double-counting if "P(adopted given Phase III success)" is folded into p_success |
| relative_reduction (secondary, joint) | deaths/yr | 0.10 | Modeled as independent of p_success. A surrogate-endpoint "success" lowers the effective reduction. |

Model structure check: in the baseline, years_to_adoption = 8, so the decline term (1−0.02)^0 = 1. Benefit is $OP 53.46B and all-in cost is $7M. SROI per unit of p_success is therefore 7,637×, and the baseline is 0.40 × 7,637 = **3,055×**. This matches the summary.

**Break-even p_success at the 2,000× bar = 2,000 / 7,637 = 0.262.** This confirms the critique's 0.26.

## Plausible Range

| Source / scenario | p_success | Basis |
|---|---|---|
| Raw industry, all indications (BIO 2011–2020) | 0.15–0.17 | 29% Phase II→III × 58% Phase III→filing. Approval-based. Corroborated by the Verifier. |
| Investigator decomposition, including an adoption factor | 0.14–0.30 (central 0.20) | 0.5 × (0.40–0.55) × (0.70–0.85). This is inference, not sourced. |
| Same decomposition, Phase IIc × Phase III only | 0.20–0.275 (central ≈ 0.24) | Removes the adoption factor, which is arguably already captured in adult_uptake = 0.6 (see the note on double-counting below). |
| **Infectious-disease-adjusted range (Verifier-endorsed)** | **0.20–0.32** | Anti-infective uplift. Brackets the break-even. |
| Optimistic (anti-infective Phase III >80%) | 0.40–0.51 | 0.5–0.6 Phase IIc × 0.80–0.85 Phase III. Tests the upside direction. |

**Note on double-counting.** The Investigator's adoption factor (0.70–0.85) overlaps with adult_uptake. CG says 60% uptake applies "if it works," which plausibly already embeds non-adoption. Multiplying both would double-count. I therefore treat the **0.20–0.32** range as the primary range. The 0.14–0.17 values are a lower bound, conditional on an approval-based reference class applying fully.

## Sensitivity Analysis

The base case is **3,055×**, against a bar of 2,000×.

**p_success alone (all else at CG values):**

| p_success | SROI | Δ vs. base | vs. 2,000× bar |
|---|---|---|---|
| 0.14 | 1,069× | −65.0% | Below |
| 0.15 | 1,146× | −62.5% | Below |
| 0.17 | 1,298× | −57.5% | Below |
| 0.20 | 1,527× | −50.0% | Below |
| 0.24 | 1,833× | −40.0% | Below |
| 0.25 | 1,909× | −37.5% | Below |
| **0.262** | **2,000×** | −34.5% | **Break-even** |
| 0.275 | 2,100× | −31.3% | Above |
| 0.30 | 2,291× | −25.0% | Above |
| 0.32 | 2,444× | −20.0% | Above |
| 0.40 (CG) | 3,055× | 0% | Above |
| 0.45 | 3,437× | +12.5% | Above |
| 0.51 | 3,895× | +27.5% | Above |

**Joint with other threads.** Effects are multiplicative, so the break-even p_success rises as other parameters fall:

| Other parameter change | SROI per unit p | Break-even p_success |
|---|---|---|
| None | 7,637 | 0.262 |
| relative_reduction 0.10 → 0.07 | 5,346 | 0.374 |
| adult_uptake 0.60 → 0.45 | 5,728 | 0.349 |
| Both of the above | 4,010 | 0.499 |

**Pessimistic joint case.** With p = 0.20, relative_reduction = 0.07 and uptake = 0.45, SROI is **802×**, a change of −74%.

Under even modest haircuts from other threads, CG's own 0.40 would fall below the break-even. The p_success critique is therefore load-bearing for the overall conclusion.

## Bottom-Line Impact

**Using the infectious-disease-adjusted range 0.20–0.32, SROI falls from 3,055× to 1,527–2,444×, a reduction of 20–50%. At a central p ≈ 0.25 the reduction is about 37% (≈1,900×, just below the 2,000× bar).** Using raw industry base rates (0.15–0.17), the reduction is 57–63%. The upside case, if anti-infective Phase III rates exceed 80%, is up to +28%.

## Materiality Verdict

- **Magnitude: YES.** Every point in the plausible range moves SROI by at least 20%. The thread spec's threshold was not supplied, so I assumed one around 10% or a bar crossing.
- **Bar-crossing: BORDERLINE.** The break-even (0.262) sits inside the 0.20–0.32 range, roughly 40% of the way up. The central estimate falls slightly below the bar.
- **Conditional finding:** the conclusion becomes clearly YES if any companion critique (relative_reduction, uptake, cost) cuts SROI by more than about 10–15%.

**Recommendation:** CG should state a reference class and decompose p_success into P(Phase IIc), P(Phase III | IIc) and, separately, adoption. The adoption step should be reconciled with adult_uptake to avoid double-counting.

## Code

```python
base = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
            all_in_cost=7_000_000, p_success=0.40)
BAR = 2000

def sroi(**kw):
    p = {**base, **kw}
    elig = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    deaths = elig * p['adult_uptake'] * p['baseline_mortality'] * p['relative_reduction']
    benefit = deaths * p['speedup_years'] * p['dalys_per_death'] * p['op_per_daly']
    return benefit / p['all_in_cost'] * p['p_success']

b = sroi()
print(f"Base SROI {b:,.0f}x; break-even p = {BAR / (b / 0.40):.3f}")

for ps in [0.14, 0.15, 0.17, 0.20, 0.24, 0.25, 0.262, 0.275, 0.30, 0.32, 0.40, 0.45, 0.51]:
    s = sroi(p_success=ps)
    print(f"p={ps:.3f}: {s:,.0f}x  Δ={(s / b - 1) * 100:+.1f}%  {'ABOVE' if s >= BAR else 'below'} bar")

for label, kw in [("rr 0.07", dict(relative_reduction=0.07)),
                  ("uptake 0.45", dict(adult_uptake=0.45)),
                  ("both", dict(relative_reduction=0.07, adult_uptake=0.45))]:
    per_p = sroi(p_success=1, **kw)
    print(f"{label}: SROI/unit p={per_p:,.0f}; break-even p={BAR / per_p:.3f}; "
          f"at p=0.20 -> {sroi(p_success=0.20, **kw):,.0f}x")
```

--- Critique: The TB-specific reference classes (host-directed therapy, adjunctives, regimen-shortening) have a much worse record than 40% ---

# Impact of TB-specific reference classes on p_success for the TB statins grant

## Parameter mapping

- **p_success (primary).** Base value is 0.40, the probability that Phase IIc and Phase III both succeed. It enters the model as a final multiplier, and SROI is strictly linear in it.
- **relative_reduction (secondary, joint).** Base value is 0.10. The verified corticosteroid evidence (RR 0.69 in mostly HIV-negative patients, then a null HR of 0.85 with P = 0.22 in HIV-positive adults) is evidence of *effect heterogeneity*. That bears on the size of the effect conditional on "success" as much as on whether success happens. The model treats the two as independent, so I test them jointly.

The model reduces to:

SROI = 5.5M × 0.6 × 0.06 × relative_reduction × 1 × 27 × 100,000 / 7M × p_success = **76,371 × relative_reduction × p_success**

- Base case: 76,371 × 0.10 × 0.40 = **3,055x**.
- Funding bar: 2,000x.
- Break-even expected relative reduction (p × rr) = **0.0262**. The base case is 0.040.
- Break-even p_success with relative_reduction held at 0.10 = **0.262**.

## Plausible range

**p_success: current 0.40, plausible range [0.20, 0.40], central about 0.30.**

- **Downward pressure:**
  - The three failed fluoroquinolone 4-month trials (REMoxTB, OFLOTUB, RIFAQUIN).
  - The corticosteroid sequence: a positive first trial did not generalize to HIV-positive adults.
  - Industry Phase II→approval base rates in the roughly 15–30% range.
  - The model has no explicit "successful trial but no WHO adoption" step.
- **Upward and neutral pressure:**
  - Study 31 and SHINE succeeded. The failures came from a specific design (simple FQ substitution), not from TB adjuncts as a class.
  - Atorvastatin is a cheap, well-characterized repurposed generic, which avoids many of the safety and manufacturing failure modes behind industry attrition.
- **Lower bound of 0.10–0.15:** the critique's own lower values are **not sourced**. The verifier marked the HDT-specific 10–20% rate as ungrounded. I report them only as a stress test.
- **Optimistic test of 0.50:** included as a check in the other direction. There is no positive evidence for it.

**relative_reduction (joint test only): [0.08, 0.10].** This reflects possible dilution of the effect in HIV-positive patients, consistent with the corticosteroid pattern. It is not independently quantified.

## Sensitivity analysis

### p_success alone (relative_reduction = 0.10)

| p_success | SROI | Δ vs. base | vs. 2,000x bar |
|---|---|---|---|
| 0.10 (stress, ungrounded) | 764x | −75% | Below |
| 0.15 (critique's point) | 1,146x | −62.5% | Below |
| 0.20 (plausible low) | 1,527x | −50% | Below |
| 0.25 | 1,909x | −37.5% | Below |
| **0.262** | **2,000x** | **−34.5%** | **Break-even** |
| 0.30 (central) | 2,291x | −25% | Above |
| 0.35 | 2,673x | −12.5% | Above |
| 0.40 (base) | 3,055x | 0% | Above |
| 0.50 (optimistic) | 3,819x | +25% | Above |

### Joint with relative_reduction = 0.08

The two effects are multiplicative, not additive.

| p_success | SROI | Δ vs. base |
|---|---|---|
| 0.20 | 1,222x | −60% |
| 0.25 | 1,527x | −50% |
| 0.30 | 1,833x | −40% (below bar) |
| 0.40 | 2,444x | −20% |

If both parameters sit at the pessimistic end of the plausible range (p = 0.20, rr = 0.08), the result is **1,222x (−60%)**.

## Bottom-line impact

Within the evidence-supported range for p_success (0.20–0.40), cost-effectiveness falls by **0–50%, with a central estimate of about −25% (≈2,290x)**. That central estimate is still above the 2,000x bar. The estimate drops below the bar if:

- p_success < 0.26, or
- p_success ≤ 0.30 combined with a modest (20%) dilution of relative_reduction.

The critique's headline figure of "38% of base" (p = 0.15) depends on an unsourced reference class.

## Materiality verdict

**BORDERLINE, leaning YES.**

- The magnitude is clearly large: a central drop of about 25% and a plausible drop of up to 50%.
- The break-even point (p = 0.26) sits *inside* the plausible range, so the funding decision depends on a parameter for which no sourced reference class exists.
- But the central estimate does not cross the bar unless it is combined with the heterogeneity effect on relative_reduction.

A sourced TB adjunct/HDT success rate would resolve this. Splitting p_success into separate probabilities for Phase IIc success, Phase III success, and adoption would also help.

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

B = sroi()                                   # 3054.9
print("base", round(B, 1))
for ps in [0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50]:
    v = sroi(p_success=ps); print(ps, round(v), f"{v/B-1:+.1%}")
print("breakeven p:", 2000 / (B / 0.40))      # 0.2619
for ps in [0.20, 0.25, 0.30, 0.40]:
    v = sroi(p_success=ps, relative_reduction=0.08); print("joint", ps, round(v), f"{v/B-1:+.1%}")
print("breakeven p*rr:", 2000 / (B / 0.04))   # 0.0262
```

--- Critique: "Success" probably means a surrogate or composite endpoint, but the model needs a 10% mortality reduction, so P(adopted AND 10% mortality benefit) < P(trials succeed) ---

# Quantifying the Surrogate vs. Mortality Endpoint Critique for the TB Statins BOTEC

## Critique

"Success" probably means a surrogate or composite endpoint, but the model needs a 10% mortality reduction. So P(adopted AND 10% mortality benefit) is less than P(trials succeed).

## Parameter Mapping

The model's formula is:

SROI = p_success × [eligible × adult_uptake × baseline_mortality × relative_reduction × speedup_years × dalys_per_death × op_per_daly] / all_in_cost

| Parameter | Model key | Current value | Role in this critique |
|---|---|---|---|
| Relative mortality reduction, conditional on "success" | `relative_reduction` | 0.10 | **Primary.** Should be E[RR \| trials succeed as defined]. If success is judged on a surrogate or composite, this is lower. |
| Probability Phase II and III succeed | `p_success` | 0.40 | **Secondary.** If success instead means a demonstrated mortality benefit, this probability should be lower. |
| Their dependence | (implicit) | Independent; product = 0.04 | The critique's core point: the definition of success determines whether RR or p_success needs adjusting. |

**Parameters this critique should *not* change:**
- **`baseline_mortality` (0.06).** The critique's 0.4–1.5% trial-population mortality matters for trial *sample size*, not for programmatic mortality among treated patients. Changing it here would double-count Thread 6.
- **`all_in_cost` (7M).** The critique implies a mortality-powered Phase III is unaffordable at $7M. That is evidence about *which* interpretation of success applies. Its cost implication belongs to the all_in_cost thread and is unverified.

**Structural note.** SROI is linear in both `relative_reduction` and `p_success`. All effects are therefore exactly multiplicative, and every result below is the base value times RR/0.10 times p/0.40.

## Plausible Range

There are two coherent, mutually exclusive branches. The model is internally inconsistent only if it uses both "success = surrogate" (for p = 0.4) and "RR = mortality effect" (for 10%).

**Branch A: success = surrogate or composite endpoint (most likely, given the trial size and budget).** Keep p = 0.40 and lower E[RR | success].
- Write E[RR | success] = q × RR_true. Here q is the probability that a surrogate win reflects a real mortality benefit, and RR_true is the mortality effect when it does.
- Evidence bearing on q:
  - Host-directed therapy precedents show surrogate-based wins (FEV₁, culture conversion) without mortality confirmation.
  - TB Fast Track found HR 0.92 on all-cause mortality, which was not significant. It tested a different intervention, so it is weak evidence about the size of a realistic mortality effect.
- Plausible range: **E[RR | success] = 0.03–0.10**. The central value is about 0.05–0.07, the critique's figure.
- That central figure is **ungrounded**. It is consistent with q ≈ 0.5–0.7 and RR_true ≈ 10%, but neither input has direct support.
- **Optimistic case:** RR_true ≈ 12–15% with high q gives E[RR] ≈ 0.10–0.12. No statin-TB mortality data support this, so I treat it as an upper bound only.

**Branch B: success = demonstrated mortality benefit.** Keep RR = 0.10 and lower p_success.
- A 10% relative mortality reduction needs roughly 10⁴–10⁵ participants. That is unlikely within the funding envelope. This makes p(success on mortality) plausibly **0.15–0.30**.
- This range is my inference and is not verified.

**Combined case (upper bound on harm, partly double-counting).** RR = 0.05 and p = 0.30.
- This case is only coherent if the p reduction reflects a *separate* factor, such as WHO declining to adopt on surrogate evidence alone (P(adopt | surrogate success) ≈ 0.75).
- That factor overlaps with `adult_uptake`, so treat this case as a stress test, not a central estimate.

## Sensitivity Analysis

**Base case.** Eligible = 5.5M, treated = 3.3M, deaths averted = 19,800/yr, benefit = $OP 53.46B. **SROI = 3,055x** (bar = 2,000x).

**Branch A: vary RR, with p = 0.40.**

| E[RR \| success] | Deaths averted/yr | SROI | Δ vs base | vs 2,000x bar |
|---|---|---|---|---|
| 0.12 (optimistic) | 23,760 | 3,666x | +20% | above |
| 0.10 (base) | 19,800 | 3,055x | 0% | above |
| 0.08 | 15,840 | 2,444x | −20% | above |
| 0.07 | 13,860 | 2,138x | −30% | marginally above |
| **0.0655 (break-even)** | 12,964 | 2,000x | −34.5% | at bar |
| 0.06 | 11,880 | 1,833x | −40% | below |
| 0.05 | 9,900 | 1,527x | −50% | below |
| 0.03 | 5,940 | 916x | −70% | below |

**Branch B: vary p_success, with RR = 0.10.**

| p_success | SROI | Δ |
|---|---|---|
| 0.40 (base) | 3,055x | 0% |
| 0.30 | 2,291x | −25% |
| **0.262 (break-even)** | 2,000x | −34.5% |
| 0.20 | 1,527x | −50% |
| 0.15 | 1,146x | −62.5% |

**Joint grid (SROI, x).** Effects are multiplicative.

| p \ RR | 0.03 | 0.05 | 0.07 | 0.10 |
|---|---|---|---|---|
| 0.40 | 916 | 1,527 | 2,138 | 3,055 |
| 0.30 | 687 | 1,146 | 1,604 | 2,291 |
| 0.20 | 458 | 764 | 1,069 | 1,527 |

**Combined stress test.** With RR = 0.05 and p = 0.30, SROI = **1,146x (Δ = −62.5%)**. This partly double-counts, as noted above.

**Key threshold.** The grant clears 2,000x only if the effective product p × E[RR] ≥ **0.0262**. The current product is 0.040. This means the model tolerates at most a **34.5%** combined haircut from this critique. The critique's central range (E[RR] 5–7%) **straddles this break-even point**.

**Interaction with other threads.** Any independent downward revision elsewhere (uptake ramp, discounting, baseline mortality) raises the break-even RR proportionally. For example, a 20% cut from the uptake thread moves break-even RR to about 8.2%.

## Bottom-Line Impact

Making the definition of success coherent with the 10% mortality assumption plausibly reduces SROI by **0% to −70%**. The central estimate is **−30% to −50%**, taking SROI from 3,055x to about **1,530–2,140x**. The break-even value, E[RR | success] ≈ 6.5% (or equivalently p ≈ 0.26), sits inside the critique's central range.

## Materiality Verdict

**YES.**
- The plausible effect range spans the 2,000x funding bar, so the critique is decision-relevant, not just a refinement.
- **Caveat:** the central 5–7% figure is ungrounded. What is robust is the structural point: p = 0.4 and RR = 0.10 cannot both be correct unless "success" is defined as a mortality result. This needs either a stated derivation or an explicit sensitivity analysis.
- Small variants are less of a concern: if CG can show that RR = 10% was already meant as E[RR | surrogate success], the impact falls to near 0%.

## Code

```python
def sroi(eligible_8y=5_500_000, years=8, decline=0.02, uptake=0.60,
         base_mort=0.06, rr=0.10, dalys=27, op_per_daly=100_000,
         speedup=1, cost=7_000_000, p=0.40):
    eligible = eligible_8y * (1 - decline) ** (years - 8)
    treated = eligible * uptake
    deaths = treated * base_mort * rr
    benefit = deaths * speedup * dalys * op_per_daly
    return benefit / cost * p, deaths

base, d0 = sroi()
print(f"Base SROI {base:,.1f}x, deaths/yr {d0:,.0f}")   # 3,054.9x, 19,800

BAR = 2000
print("Break-even RR @p=0.4:", 0.10 * BAR / base)        # 0.0655
print("Break-even p  @RR=0.1:", 0.40 * BAR / base)       # 0.262

print("\nBranch A (vary RR):")
for rr in [0.12, 0.10, 0.08, 0.07, 0.06, 0.05, 0.03]:
    s, d = sroi(rr=rr)
    print(f" RR={rr:.2f} deaths={d:,.0f} SROI={s:,.0f}x Δ={s/base-1:+.1%}")

print("\nBranch B (vary p):")
for p in [0.40, 0.30, 0.20, 0.15]:
    s, _ = sroi(p=p)
    print(f" p={p:.2f} SROI={s:,.0f}x Δ={s/base-1:+.1%}")

print("\nJoint grid:")
for p in [0.40, 0.30, 0.20]:
    print(f" p={p:.2f}: " + "  ".join(
        f"RR{rr:.2f}={sroi(rr=rr, p=p)[0]:,.0f}" for rr in [0.03, 0.05, 0.07, 0.10]))

# Mixture view: E[RR|surrogate success] = q * RR_true
for q in [0.5, 0.6, 0.7]:
    for rr_true in [0.10, 0.12]:
        s, _ = sroi(rr=q * rr_true)
        print(f" q={q}, RR_true={rr_true}: E[RR]={q*rr_true:.3f} SROI={s:,.0f}x Δ={s/base-1:+.1%}")
```

--- Critique: P(adoption | Phase III success) and P(Phase III gets funded and run | Phase IIc success) are missing, and the 60% uptake factor may not cover them ---

# Impact Assessment: Missing P(Phase III funded | IIc success) and P(adoption | Phase III success) factors

## Parameter Mapping

The critique adds up to two multiplicative factors to the success-probability chain. In the model these act on `p_success`. Equivalently, the adoption factor can act on `adult_uptake`, because SROI is linear in both.

| Parameter | Model key | Current value | Role |
|---|---|---|---|
| Probability that Phase II and III both succeed | `p_success` | 0.40 | Primary. New factors multiply this. |
| Adult uptake "if it works" | `adult_uptake` | 0.60 | Alternative home for the adoption factor. The critique collapses if 0.60 already embeds non-adoption. |
| P(Phase III funded and run \| IIc success) | *not in model* (implicitly 1.0) | 1.0 | New factor F_fund |
| P(WHO/national adoption \| Phase III success) | *not in model* (implicitly 1.0) | 1.0 | New factor F_adopt |

Model structure is SROI = (eligible × uptake × mortality × RR × speedup × DALYs × $/DALY) / cost × p_success.

Every term enters multiplicatively, so SROI = 3,055 × F_fund × F_adopt. The effects of the two new factors therefore multiply rather than add.

## Plausible Range

- **F_adopt.** Current implicit value = 1.0. Plausible range = [0.75, 1.0].
  - The upper end, 1.0, applies if the 60% uptake already embeds the risk of non-adoption.
  - Around 0.95 is supported by the Study 31 precedent, where WHO adopted a clean trial within months.
  - 0.75–0.85 is the critique's illustrative range and is **ungrounded**. No source gives P(adoption | positive Phase III) for TB adjuncts.
- **F_fund.** Current implicit value = 1.0. Plausible range = [0.8, 1.0].
  - 1.0 applies if the $7M all-in cost, which explicitly includes "later Phase III trials," means funding is assumed secured. It also applies if the 40% `p_success` already embeds funding risk.
  - 0.8 is illustrative and **ungrounded**.
  - F_fund is plausibly correlated with the endpoint (Critique 1). A mortality-powered Phase III costs well over $7M, which lowers F_fund or raises `all_in_cost`.

## Sensitivity Analysis

**Base case:** SROI = 3,055x. Funding bar = 2,000x.

**Break-even.** The bar is crossed when the combined factor F_fund × F_adopt = 2,000 / 3,055 = **0.655**. That corresponds to an effective `p_success` of 0.262, which confirms the critique's "0.26 threshold" claim.

| Scenario | F_fund | F_adopt | Effective p_success | SROI | Δ vs base | Above 2,000x bar? |
|---|---|---|---|---|---|---|
| Base (60% embeds everything) | 1.00 | 1.00 | 0.400 | 3,055x | 0% | Yes |
| Precedent-based adoption only | 1.00 | 0.95 | 0.380 | 2,902x | −5% | Yes |
| Adoption, high | 1.00 | 0.85 | 0.340 | 2,597x | −15% | Yes |
| Adoption, low | 1.00 | 0.75 | 0.300 | 2,291x | −25% | Yes |
| Funding only | 0.80 | 1.00 | 0.320 | 2,444x | −20% | Yes |
| Joint, moderate | 0.80 | 0.85 | 0.272 | 2,077x | −32% | Yes (barely, 4% margin) |
| Joint, pessimistic | 0.80 | 0.75 | 0.240 | 1,833x | −40% | **No** |

**Optimistic direction.** This critique has no mechanism that raises SROI. Its best case is 0%: the 60% uptake and 40% success probability already embed both risks, and the issue reduces to documentation.

**Interactions.**
- The two factors are multiplicative with each other and with any other critique that touches the linear chain.
- Example: suppose Thread 5 cut `adult_uptake` from 0.60 to 0.45 (a ramp or adoption lag).
  - Combined with F_adopt = 0.85 alone, SROI ≈ 1,948x, which is below the bar.
- **Double-count risk.** If F_adopt is applied to `p_success`, then `adult_uptake` must be interpreted as conditional on adoption. Otherwise the same non-adoption risk is counted twice.
- **Speedup interaction.** If Phase III funding is the bottleneck, the 1-year speedup could be partly absorbed by funding delays. This is a separate downward channel and is not quantified here.

## Bottom-Line Impact

**This critique reduces cost-effectiveness by 0% to 40% (SROI 3,055x → 3,055–1,833x).**
- If the factors are genuinely missing and set to the critique's illustrative values, the central reduction is about 15–32%.
- The 2,000x bar is crossed only when the combined factor falls below 0.655, for example F_fund = 0.8 together with F_adopt ≤ 0.82.

## Materiality Verdict

**BORDERLINE.**
- The effect is material (≥15%) whenever either factor is genuinely excluded from CG's 40% or 60% at the critique's illustrative values.
- It flips the funding decision only in the joint-pessimistic case, or when combined with uptake or endpoint critiques.
- The input values are ungrounded. The key unresolved question is how CG derived the 60% and 40%, which an explicit decomposition from CG would answer.

## Code

```python
base = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
            all_in_cost=7_000_000, p_success=0.40)

def sroi(p, f_fund=1.0, f_adopt=1.0):
    eligible = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    treated = eligible * p['adult_uptake']
    deaths = treated * p['baseline_mortality'] * p['relative_reduction']
    benefit = deaths * p['speedup_years'] * p['dalys_per_death'] * p['op_per_daly']
    return benefit / p['all_in_cost'] * p['p_success'] * f_fund * f_adopt

b = sroi(base)
print(f"Base SROI: {b:,.0f}x; break-even combined factor: {2000/b:.3f}; "
      f"break-even p_success: {0.40*2000/b:.3f}")

scenarios = {"Precedent adoption": (1.0, 0.95), "Adopt high": (1.0, 0.85),
             "Adopt low": (1.0, 0.75), "Funding only": (0.8, 1.0),
             "Joint moderate": (0.8, 0.85), "Joint pessimistic": (0.8, 0.75)}
for name, (ff, fa) in scenarios.items():
    s = sroi(base, ff, fa)
    print(f"{name:20s} p_eff={0.4*ff*fa:.3f} SROI={s:,.0f}x "
          f"delta={100*(s/b-1):+.0f}% above_bar={s>=2000}")

# Interaction example with a lower uptake (Thread 5)
p2 = dict(base, adult_uptake=0.45)
print(f"Uptake 0.45 + F_adopt 0.85: {sroi(p2, 1.0, 0.85):,.0f}x")
```

**Output:**
```
Base SROI: 3,055x; break-even combined factor: 0.655; break-even p_success: 0.262
Precedent adoption   p_eff=0.380 SROI=2,902x delta=-5% above_bar=True
Adopt high           p_eff=0.340 SROI=2,597x delta=-15% above_bar=True
Adopt low            p_eff=0.300 SROI=2,291x delta=-25% above_bar=True
Funding only         p_eff=0.320 SROI=2,444x delta=-20% above_bar=True
Joint moderate       p_eff=0.272 SROI=2,077x delta=-32% above_bar=True
Joint pessimistic    p_eff=0.240 SROI=1,833x delta=-40% above_bar=False
Uptake 0.45 + F_adopt 0.85: 1,948x
```

**Simplifications.**
- The model is reproduced exactly from the stated formula chain, and the base output of 3,055x matches.
- The new factors are added as scalar multipliers.
- Correlation with `relative_reduction` and `all_in_cost` (Critique 1) is noted qualitatively but not modeled jointly.

--- Critique: Phase IIc "success" is a weak gate. If it is defined by PK or dose selection, it passes easily and transmits little information, so the probability of the whole chain should be weighted toward Phase III ---

# Quantitative Impact Assessment

**CRITIQUE:** Phase IIc "success" is a weak gate, so most of the risk sits in Phase III, and p_success and relative_reduction are correlated.

**Bottom line:** This critique could change cost-effectiveness by about −63% to +20%. Under its own premise (a weak IIc gate and a Phase III not powered on mortality), the central range is −20% to −45%. Treat this as conditional, because the premise that IIc is dose-finding or surrogate-based has not been verified.

---

## 1. Parameter Mapping

| Parameter | Model key | Current value | How the critique touches it |
|---|---|---|---|
| Probability Phase II and Phase III both succeed | `p_success` | 0.40 | Splits into P(IIc) × P(III \| IIc). With a weak gate, P(III \| IIc) drives the result. |
| Relative mortality reduction, conditional on success | `relative_reduction` | 0.10 | Should be read as E[θ \| S], the expected true mortality effect given the trial chain succeeds. |
| Joint term | p_success × relative_reduction | 0.040 | The model treats the two as independent point values. The critique asks what E[θ·1{S}] is under a prior on θ. |

**Model structure.** Every other parameter enters multiplicatively, so:

SROI = K × (p_success × relative_reduction), where K = 5.5M × 0.6 × 0.06 × 27 × 100,000 × 1 / 7M = **76,371**

- Baseline: 76,371 × 0.04 = **3,055x**. This matches the parameter summary.
- Funding bar of 2,000x implies a break-even E[p·RR] of **0.0262**:
  - p ≥ 0.262 at RR = 0.10, or
  - RR ≥ 0.0655 at p = 0.40.

---

## 2. Plausible Ranges

**p_success: plausible range 0.25–0.45. Stress value 0.21.**
- If IIc is a weak gate (safety, PK, dose or surrogate), P(IIc pass) ≈ 0.85–0.95.
- P(III \| IIc) for repurposed host-directed adjuncts in TB is plausibly 0.30–0.50. The basis:
  - TB precedents of Phase II signals not translating (REMoxTB, verified).
  - HDT Phase 2 trials use safety and surrogate endpoints such as FEV₁ (verified), which transmit limited information.
- Joint probability ≈ 0.26–0.48.
- The critique's 0.21 (0.7 × 0.3) is **ungrounded**. I use it only as a stress test.
- Upside: if CG's 0.40 already embeds a weak IIc, the decomposition changes nothing. That gives 0.40–0.45.

**E[θ | S] (the "conditional 10%"): plausible range 0.085–0.12.**
This comes from the scenario analysis below, not from external data.

**Feasibility check on the Phase III endpoint (my calculation).**
- To detect 6.0% → 5.4% mortality with two-sided α = 0.05 and 80% power needs about 23,400 per arm, roughly 47,000 patients.
- That cannot be done within a $7M all-in budget.
- So Phase III "success" will almost certainly be on a composite or surrogate endpoint.
- This weakens the coupling between trial success and the true mortality effect. That coupling is the key driver in the scenarios.

---

## 3. Sensitivity Analysis

### 3a. One-way on p_success (RR fixed at 0.10)

| p_success | SROI | Δ vs 3,055x |
|---|---|---|
| 0.21 (stress) | 1,604x | −47.5% |
| 0.25 | 1,909x | −37.5% (below bar) |
| 0.262 | 2,000x | −34.5% (break-even) |
| 0.30 | 2,291x | −25.0% |
| 0.45 | 3,437x | +12.5% |

### 3b. Two-way grid: p_success × E[θ | S] (SROI, x)

| p \ RR | 0.07 | 0.085 | 0.10 | 0.12 |
|---|---|---|---|---|
| 0.21 | 1,123 | 1,363 | 1,604 | 1,925 |
| 0.25 | 1,336 | 1,623 | 1,909 | 2,291 |
| 0.30 | 1,604 | 1,947 | 2,291 | 2,749 |
| 0.35 | 1,871 | 2,272 | 2,673 | 3,208 |
| 0.40 | 2,138 | 2,597 | 3,055 | 3,666 |
| 0.45 | 2,406 | 2,921 | 3,437 | 4,124 |

The effects are **multiplicative**. For example, p = 0.30 (−25%) combined with RR = 0.085 (−15%) gives −36%, not −40%.

### 3c. Joint-distribution scenario analysis (the critique's E[p·RR] ≠ p·E[RR] point)

**Setup:**
- The true mortality effect θ takes values in {0, 0.05, 0.10, 0.20}.
- Weak IIc gate: P(IIc \| θ) = 0.85, 0.90, 0.95, 0.95.
- P(III \| θ) for two coupling cases:
  - **Strong coupling** (endpoint tracks mortality): 0.05, 0.35, 0.65, 0.90.
  - **Weak coupling** (surrogate success possible even with no mortality effect): 0.15, 0.30, 0.45, 0.60.

| Scenario | Prior on θ (P at 0, .05, .10, .20) | Prior mean θ | P(S) | E[θ \| S] | E[θ·S] | SROI | Δ |
|---|---|---|---|---|---|---|---|
| CG baseline | n/a | n/a | 0.40 | 0.10 | 0.0400 | 3,055x | 0% |
| A: Central prior, strong coupling | .5/.2/.2/.1 | 0.050 | 0.293 | 0.111 | 0.0326 | 2,490x | −18% |
| B: Central prior, weak coupling | .5/.2/.2/.1 | 0.050 | 0.260 | 0.087 | 0.0227 | 1,730x | −43% |
| C: Optimistic prior, strong coupling | .3/.25/.3/.15 | 0.0725 | 0.405 | 0.119 | 0.0481 | 3,674x | +20% |
| D: Pessimistic prior, weak coupling | .6/.2/.15/.05 | 0.035 | 0.223 | 0.066 | 0.0148 | 1,131x | −63% |
| Naive independence (A's P(S) × prior mean) | — | 0.050 | 0.293 | 0.050 | 0.0147 | 1,120x | −63% |

**Interpretation:**

1. **Correlation helps CG rather than hurting it.** Because CG explicitly conditions the 10% on success, the correlation between p and θ is favourable: E[θ \| S] exceeds the prior mean in every scenario. Ignoring it, as in the naive independence row, would *understate* benefit.
2. **Winner's curse is small.** Its effect on the 0.10 figure stays modest (E[θ \| S] = 0.087–0.119) except in the pessimistic-prior, weak-coupling case (0.066). The critique's instruction to drop or reframe the winner's-curse point is supported.
3. **The real downside comes from two sources:**
   - Lower P(S) once the weak gate is acknowledged.
   - Weak coupling between surrogate success and mortality. A cheap Phase III makes weak coupling the more likely case.

### 3d. All pessimistic simultaneously

p = 0.21 and E[θ \| S] = 0.07 gives **1,123x (−63%)**. This is consistent with Scenario D.

---

## 4. Bottom-Line Impact

**The range is −63% to +20%. Conditional on a weak IIc gate and a surrogate-powered Phase III, the central estimate is −20% to −45% (about 1,700x–2,500x).** Much of the p_success component overlaps with Critique 1 and must not be double-counted. The increment unique to this critique is the coupling and selection effect on E[θ \| S]: roughly −13% to +19% at fixed P(S).

## 5. Materiality Verdict: **BORDERLINE**

- **Magnitude is material.** The model crosses the 2,000x bar if p < 0.262 at RR = 0.10, and in Scenarios B and D.
- **But the case is not established:**
  - The key premise (how IIc defines success) is unverified.
  - The decomposition probabilities are ungrounded.
  - The correlation argument, correctly computed, partly favours CG.
- **What would resolve it:** confirming the IIc and Phase III primary endpoints and power calculations. That should be the priority.
- **Editorial fixes:**
  - Change "see Critique 2" to Critique 1.
  - Change "Phase II→approval" to "Phase II/III success → guideline adoption".

---

## 6. Code

```python
import numpy as np

# --- CG model (parameter summary) ---
P = dict(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=1e5, speedup_years=1,
         all_in_cost=7e6, p_success=0.40)

def sroi(**o):
    q = {**P, **o}
    elig = q['eligible_people_at_8y'] * (1 - q['decline_per_year'])**(q['years_to_adoption'] - 8)
    deaths = elig * q['adult_uptake'] * q['baseline_mortality'] * q['relative_reduction']
    benefit = deaths * q['speedup_years'] * q['dalys_per_death'] * q['op_per_daly']
    return benefit / q['all_in_cost'] * q['p_success']

base = sroi()                                   # 3054.9
K = base / (P['p_success'] * P['relative_reduction'])   # 76371
print(f"base={base:.0f}, K={K:.0f}, breakeven p*RR={2000/K:.4f}")

# --- one-way and two-way sensitivity ---
for p in [0.21, 0.25, 0.262, 0.30, 0.45]:
    s = sroi(p_success=p)
    print(p, round(s), f"{s/base-1:+.1%}")

for p in [0.21, 0.25, 0.30, 0.35, 0.40, 0.45]:
    print(p, [round(sroi(p_success=p, relative_reduction=r)) for r in [0.07, 0.085, 0.10, 0.12]])

# --- Phase III mortality-powered sample size (feasibility check) ---
from scipy.stats import norm
p0, p1 = 0.06, 0.054
n = (norm.ppf(0.975) + norm.ppf(0.8))**2 * (p0*(1-p0) + p1*(1-p1)) / (p0 - p1)**2
print("n per arm ~", round(n))                  # ~23,400

# --- joint-distribution scenarios ---
theta = np.array([0, 0.05, 0.10, 0.20])
p_IIc = np.array([0.85, 0.90, 0.95, 0.95])
p_III = {'strong': np.array([0.05, 0.35, 0.65, 0.90]),
         'weak':   np.array([0.15, 0.30, 0.45, 0.60])}
priors = {'central': np.array([.5, .2, .2, .1]),
          'optimistic': np.array([.3, .25, .3, .15]),
          'pessimistic': np.array([.6, .2, .15, .05])}

for name, (pr, cp) in {'A': ('central', 'strong'), 'B': ('central', 'weak'),
                       'C': ('optimistic', 'strong'), 'D': ('pessimistic', 'weak')}.items():
    w = priors[pr]
    pS_theta = p_IIc * p_III[cp]
    PS = (w * pS_theta).sum()
    EthS = (w * theta * pS_theta).sum()
    s = K * EthS
    print(name, f"P(S)={PS:.3f} E[th|S]={EthS/PS:.3f} E[th*S]={EthS:.4f} "
                f"SROI={s:.0f} ({s/base-1:+.0%}) naive={K*PS*(w*theta).sum():.0f}")
```

--- Critique: Baseline year is stale and the 5.5M figure is sensitive to it ---

# Impact Assessment: Stale Notification Baseline for eligible_people_at_8y

**CRITIQUE:** The baseline year is stale, and the 5.5M figure is sensitive to it.

## Parameter Mapping

The relevant entry in the parameter map is the last block: eligible_people_at_8y, decline_per_year, years_to_adoption.

- **eligible_people_at_8y** (primary)
  - Current value: 5,500,000.
  - It enters the formula chain linearly, so SROI scales 1:1 with it.
- **decline_per_year** = 0.02 and **years_to_adoption** = 8 (secondary)
  - Together they set the projection factor 0.98^8 = 0.851, which is applied implicitly upstream of the 5.5M.
  - Moving the baseline year may also change how many years of decline should apply.
  - In the model as coded, `(1 − d)^(years_to_adoption − 8)` = 1. All decline is therefore baked into the 5.5M input.

**Reconstructing the 5.5M.** The model does not state how it was derived. The most consistent reconstruction is:

7.5M notifications × 0.96 (drug-susceptible) × 0.90 (adult) × 0.98^8 = **5.51M**

This matches 5.5M to within 0.3%. That supports treating the input as proportional to baseline notifications, so I can rescale it by the ratio of new to old baseline.

## Plausible Range

**Baseline notifications.** Current implied value: 7.5M. Plausible range: about 7.8M to 8.3M.

| Scenario | Notifications | Basis |
|---|---|---|
| Low (backlog-adjusted) | ~7.8M | 2023–24 counts partly reflect catch-up of COVID-era missed diagnoses. A steady-state level could sit below the observed peak. |
| Central | 8.2M | WHO 2023 notifications |
| High | 8.3M | WHO Global TB Report 2025, 2024 plateau |

The low end is my judgment-based placement, not a sourced figure.

**Decline exponent (interaction test only).** If the baseline moves to 2024 while adoption timing stays fixed, the effective decline years could change by 0 to +1 year. That is a factor of 1.00 down to 0.98. The grant and data years are not stated in the model, so I treat this as a sensitivity rather than a correction.

## Sensitivity Analysis

**Base case:** eligible = 5.50M, deaths averted = 19,800/yr, SROI = **3,055x**.

| Scenario | eligible_people_at_8y | Deaths averted/yr | SROI | Δ vs. base |
|---|---|---|---|---|
| Base (7.5M) | 5.50M | 19,800 | 3,055x | — |
| Backlog-adjusted (7.8M) | 5.72M | 20,592 | 3,177x | +4.0% |
| 2023 baseline (8.2M) | 6.01M | 21,648 | 3,340x | +9.3% |
| 2024 baseline (8.3M) | 6.09M | 21,912 | 3,381x | +10.7% |
| 8.3M + 1 extra decline year | 5.97M | 21,474 | 3,313x | +8.5% |
| 7.8M + 1 extra decline year (low joint) | 5.61M | 20,180 | 3,113x | +1.9% |

**Pessimistic direction.** This critique contains no evidence that would move the baseline below 7.5M. The worst case consistent with the evidence is roughly no change (about +2% to 0%).

**Breakeven.** To fall to the 2,000x bar, eligible_people_at_8y would have to drop to 3.60M. That is equivalent to about 4.9M baseline notifications, which is far outside any plausible range.

**Interactions.** SROI is a pure product of its inputs, so the effects are multiplicative.
- The baseline and decline-exponent effects compound: 1.107 × 0.98 = 1.085.
- Stacking with Critique 2, or any other critique, is done by multiplying the SROI ratios, not by adding percentages.

## Bottom-Line Impact

**Updating the notification baseline raises SROI by about +2% to +11%, central estimate about +9%. That moves SROI from 3,055x to roughly 3,110x–3,380x, central about 3,340x.**

The upper part of the range (+9–11%) holds only if the 2023–24 level is a steady state rather than backlog-inflated.

## Materiality Verdict

**NO.**
- The effect is well inside the ±25% threshold.
- It moves SROI further above the 2,000x bar, so it cannot change the funding decision on its own.
- Its main relevance is as a multiplicative modifier, about ×1.02–1.11, when combined with other critiques that touch eligible_people_at_8y or decline_per_year.

## Code

```python
def sroi(eligible=5_500_000, years_to_adoption=8, decline=0.02, uptake=0.60,
         mort=0.06, rr=0.10, dalys=27, op_per_daly=100_000, speedup=1,
         cost=7_000_000, p=0.40):
    elig = eligible * (1 - decline) ** (years_to_adoption - 8)
    deaths = elig * uptake * mort * rr
    benefit = deaths * speedup * dalys * op_per_daly
    return benefit / cost * p, deaths

base, base_deaths = sroi()
print(f"Base: SROI={base:,.0f}x deaths={base_deaths:,.0f}")       # 3,055x, 19,800

# Reconstruction check of the 5.5M input
print(7.5e6 * 0.96 * 0.90 * 0.98**8)                                # ~5.51M

def scen(notif, extra_decline_years=0):
    elig = 5_500_000 * (notif / 7.5e6) * 0.98**extra_decline_years
    s, d = sroi(eligible=elig)
    return elig, d, s, s / base - 1

for label, n, x in [("backlog 7.8M", 7.8e6, 0), ("2023 8.2M", 8.2e6, 0),
                    ("2024 8.3M", 8.3e6, 0), ("8.3M +1yr decline", 8.3e6, 1),
                    ("7.8M +1yr decline", 7.8e6, 1)]:
    e, d, s, dl = scen(n, x)
    print(f"{label:20s} elig={e/1e6:.2f}M deaths={d:,.0f} SROI={s:,.0f}x Δ={dl:+.1%}")

# Breakeven eligible population at the 2,000x bar
be = 5_500_000 * 2000 / base
print(f"Breakeven eligible={be/1e6:.2f}M  (~{be/5.5e6*7.5:.1f}M notifications)")
```

--- Critique: A 2%/yr decline in notified case counts probably contradicts the observed trend; incidence rates fall slowly while counts do not ---

# Impact Assessment: TB Statins BOTEC, Decline in Case Counts

## CRITIQUE
**A 2%/yr decline in notified case counts probably contradicts the observed trend. Incidence rates fall slowly while counts do not.**

---

## PARAMETER MAPPING

The way the model is coded changes how this critique has to be applied.

- **eligible_people_at_8y**: 5,500,000. This is a hard-coded input, and this critique effectively acts on it.
- **decline_per_year**: 0.02. It looks like the affected parameter, but it is inert as coded. The formula applies `(1 − decline)^(years_to_adoption − 8)`, and with `years_to_adoption = 8` the exponent is 0. So the factor is 1 for any decline rate.
- **years_to_adoption**: 8. It only enters through the inert exponent above.

The 2%/yr assumption therefore lives inside the 5.5M input, not in the formula. Backing it out:

| Assumed derivation of 5.5M | Implied current-year count |
|---|---|
| B × 0.96 (drug-susceptible share) × 0.98⁸ | 6.73M |
| B × 0.96 × 0.90 (adult share) × 0.98⁸ | 7.48M |

Both implied values are below the 2024 notifications (8.3M) and the critique's 8.2M baseline. Part of that gap is Critique 1's baseline issue, which is separate from this one.

**How to implement the critique.** Multiply eligible_people_at_8y by a trend factor of ((1+g)/0.98)⁸, where g is the true annual change in counts. Simply editing `decline_per_year` in the spreadsheet would change nothing, which is a model-hygiene flag worth reporting to CG.

SROI is linear in eligible_people_at_8y. It enters multiplicatively with uptake, mortality, relative_reduction, p_success and cost, so it stacks multiplicatively with other critiques.

---

## PLAUSIBLE RANGE

The parameter is g, the annual change in notified, treated, drug-susceptible counts from now to adoption. CG's value is −2%/yr.

| g | Basis |
|---|---|
| **+1%/yr** (optimistic) | Notifications rose 7.5M→8.3M (2022–24) as detection recovered. The 2.4M detection gap allows further rises, but only during catch-up. The critique's own upper case. |
| **0%/yr** | Incident counts flat at ~10.3–10.8M since 2020. Population growth (~1%/yr) offsets the rate decline (~1%/yr). |
| **−0.5 to −1%/yr** (central) | After the detection gap partly closes, notifications converge on incidence. The incidence rate is falling slowly, and the 2024 reversal of the upward trend implies modest count declines. |
| **−2%/yr** | CG's assumption. Requires the rate to fall ~3%/yr. |
| **−3%/yr** (stress) | 2025 donor funding cuts reduce case finding, so notifications fall even if incidence does not. This scenario is ungrounded and its size is not evidenced. |

My central range is g ∈ [−1%, 0%]. Two points weigh on it:
- The +1%/yr case needs eight years of sustained detection gains.
- The verifier notes that notifications and incidence are linked, which caps upside from "independent" notification growth.

---

## SENSITIVITY ANALYSIS

Base case: **SROI = 3,055x**, with 19,800 deaths averted per year at a funding bar of 2,000x.

### Critique in isolation (trend factor only)

| Annual count trend g | Trend factor | Eligible (M) | Deaths averted/yr | SROI | Δ vs base |
|---|---|---|---|---|---|
| −3% (stress) | 0.921 | 5.07 | 18,240 | 2,814x | **−7.9%** |
| −2% (CG) | 1.000 | 5.50 | 19,800 | 3,055x | 0% |
| −1% | 1.085 | 5.97 | 21,475 | 3,313x | +8.5% |
| −0.5% | 1.129 | 6.21 | 22,358 | 3,450x | +12.9% |
| 0% (flat) | 1.175 | 6.46 | 23,273 | 3,591x | **+17.5%** |
| +1% | 1.273 | 7.00 | 25,201 | 3,888x | **+27.3%** |

### Joint with Critique 1 (baseline correction)

These use the critique's combined eligible range. Critique 1's own magnitude is not verified here.

| Combined eligible | SROI | Δ |
|---|---|---|
| 6.5M | 3,610x | +18% |
| 7.1M (critique's point estimate: 8.2M flat × 0.96 × 0.90) | 3,943x | +29% |
| 7.7M | 4,277x | +40% |

The two critiques interact multiplicatively: the trend factor and the baseline-correction factor multiply the same input.

### Robustness to the exponent length

If the decline runs 9 years (2024 baseline to adoption around 2033) rather than 8, the flat-count case becomes +19.9% instead of +17.5%. Results are not sensitive to this.

### Break-even (downside)

For SROI to fall below the 2,000x bar from this channel alone, the trend factor must be ≤ 0.655. That requires either:
- a sustained g ≈ −7.0%/yr for 8 years, or
- a one-time ~35% drop in notified counts relative to CG's path.

Neither is plausible, even under the funding-shock scenario.

---

## BOTTOM-LINE IMPACT

In isolation, this critique moves SROI by **−8% to +27%** (2,814x to 3,888x). The central range is **+9% to +18%** (3,313x to 3,591x), meaning CG's 2%/yr count decline is probably conservative. Combined with Critique 1, the uplift is +18% to +40%.

The direction is favourable. No plausible downside threatens the 2,000x bar.

---

## MATERIALITY VERDICT

**BORDERLINE (in isolation) / YES (combined with Critique 1, upward direction).**

- In isolation, the effect exceeds a 25% threshold only at the optimistic +1%/yr end.
- Combined with Critique 1, the central estimate (~+29%) crosses the threshold.
- The direction raises cost-effectiveness. Since the grant already clears the bar, the funding decision does not change.
- Its main value is as a **model-correctness flag**:
  - `decline_per_year` is dead code as written.
  - The 5.5M figure embeds an undocumented count-decline assumption that runs against recent data.
- The downside risk from funding shocks remains **UNGROUNDED**. Even at −3%/yr it costs only ~8%.

---

## CODE

```python
import numpy as np

base = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
            all_in_cost=7_000_000, p_success=0.40)

def sroi(p):
    elig = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    deaths = elig * p['adult_uptake'] * p['baseline_mortality'] * p['relative_reduction']
    benefit = deaths * p['speedup_years'] * p['dalys_per_death'] * p['op_per_daly']
    return benefit / p['all_in_cost'] * p['p_success'], deaths

S0, D0 = sroi(base)
print(f"Base SROI {S0:.0f}x, deaths/yr {D0:.0f}")            # 3055x, 19800

# Demonstrate decline_per_year is inert as coded
print("decline=0 ->", sroi({**base, 'decline_per_year': 0.0})[0])  # unchanged 3055

# Implied current-year baselines inside the 5.5M
print("implied B (DS only):", 5.5e6/(0.96*0.98**8))           # ~6.73M
print("implied B (DS, adult):", 5.5e6/(0.96*0.90*0.98**8))    # ~7.48M

# Critique: rescale eligible by ((1+g)/0.98)^8
for g in [-0.03, -0.02, -0.01, -0.005, 0.0, 0.01]:
    f = ((1+g)/0.98)**8
    S, D = sroi({**base, 'eligible_people_at_8y': 5.5e6*f})
    print(f"g={g:+.3f} factor={f:.3f} elig={5.5*f:.2f}M deaths={D:.0f} SROI={S:.0f}x d={S/S0-1:+.1%}")

# 9-year exponent check (flat counts)
print("9y flat:", (1/0.98)**9 - 1)                            # +19.9%

# Combined with Critique 1
for e in [6.5e6, 7.1e6, 7.7e6]:
    S, _ = sroi({**base, 'eligible_people_at_8y': e})
    print(f"elig={e/1e6:.1f}M SROI={S:.0f}x d={S/S0-1:+.1%}")

# Break-even vs 2000x bar
f_be = 2000/S0
g_be = 0.98*f_be**(1/8) - 1
print(f"break-even factor {f_be:.3f}, sustained g {g_be:.2%}/yr")  # 0.655, -7.0%/yr
```

--- Critique: "Adult DS notified" is not "eligible for the trial label": missing applicability filters ---

# Impact Assessment: "Adult DS notified" ≠ "eligible for the trial label"

## Bottom line

Applicability filters cut cost-effectiveness by about **−28% (central, ~2,200x)** if the drug's use is restricted to pulmonary cases plus standard exclusions, which stays above the 2,000x bar. A bacteriological-confirmation restriction pushes the cut to **−55 to −60% (~1,250–1,400x)**, which is below the bar. Combined with Critique 2's upside, the result ranges from **−7% (~2,850x)** to **−42% (~1,770x)**. Whether the bar is crossed depends almost entirely on whether real-world use is limited to confirmed cases.

## Parameter mapping

| Parameter | Role | Current value |
|---|---|---|
| `eligible_people_at_8y` (primary) | Filters act as a missing multiplier, `applicability_fraction` (k), on this parameter. | 5,500,000; implicit k = 1.0 |
| `baseline_mortality` (secondary) | Excluding high-mortality subgroups (HIV+) lowers mortality in the remaining pool. | 0.06 |
| `adult_uptake` (overlap risk) | The 60% may already absorb "not applicable" patients. Applying k on top could double-count. | 0.60 |

**Structure.** SROI is strictly linear in `eligible_people_at_8y`. With `years_to_adoption` = 8, the decline term (1 − 0.02)^0 equals 1. Each filter is therefore a pure multiplier on SROI.

- Each 1M eligible people is worth **555.4x** of SROI.
- **The break-even multiplier is k\* = 2000 / 3055 = 0.655.** This corresponds to 3.60M eligible people.

## Plausible range for k

| Filter | Factor | Basis | Grounding |
|---|---|---|---|
| Pulmonary only | 0.84 globally (0.75 for South-East Asia only) | WHO: 16% extrapulmonary globally, about 25% in South-East Asia | Verified |
| HIV, pregnancy, hepatic, Hr-TB | ~0.85 (range 0.80–0.92) | HIV 5–6% and Hr-TB ~7% are verified. Pregnancy and hepatic shares are Investigator assumptions. Some groups overlap. | Partly ungrounded |
| Bacteriologically confirmed | 0.62–0.64 or 1.0 | WHO: 64% of pulmonary cases are confirmed. Applies only if real-world use mirrors trial entry criteria. | Verified number; applicability uncertain |

**Combined k:**
- Plausible range: **0.40–1.0**.
- Central estimate without the confirmation filter: **~0.71**.
- Central estimate with the confirmation filter: **~0.45**.

**Two caveats lower confidence in the pessimistic end:**

1. **Regional claim is mostly already counted.** The global 16% extrapulmonary share is already a notification-weighted average that includes South-East Asia's 25%. The Verifier's "regional mix makes it worse" point only adds downside if the 5.5M is weighted more heavily toward South-East Asia than global notifications are. This is unknown.

2. **Unknown derivation of the 5.5M.** Rough arithmetic suggests ~8.2M notified × ~0.88 adult × 0.96 drug-susceptible ≈ 6.9M. The 5.5M figure therefore looks like it already contains some unexplained ~0.8 haircut. If that haircut was meant to capture applicability, k ≈ 0.84–1.0 is fair and this critique is largely already priced in.

## Sensitivity analysis

**Base case:** 19,800 deaths averted per year, SROI **3,055x**.

| Scenario | Eligible (M) | SROI | Δ vs base | Above 2,000x bar? |
|---|---|---|---|---|
| Base | 5.50 | 3,055x | — | Yes |
| Pulmonary only (×0.84) | 4.62 | 2,566x | −16% | Yes |
| Pulmonary only, South-East Asia rate (×0.75) | 4.13 | 2,291x | −25% | Yes |
| + other exclusions (×0.84×0.85) | 3.93 | 2,181x | −29% | Yes (+9% margin) |
| Same, plus HIV mortality composition (×0.947) | 3.93 | 2,066x | −32% | Barely |
| + confirmation (×0.84×0.85×0.64) | 2.51 | 1,396x | −54% | **No** |
| Same, plus HIV mortality composition | 2.51 | 1,322x | −57% | **No** |
| Pessimistic: South-East Asia rate × 0.80 × 0.62 | 2.05 | 1,137x | −63% | **No** |
| Optimistic: filters already in 5.5M/uptake (k=1) | 5.50 | 3,055x | 0% | Yes |
| **With Critique 2 (7.1M flat):** | | | | |
| C2 alone | 7.10 | 3,944x | +29% | Yes |
| C2 × 0.85 × 0.85 | 5.13 | 2,849x | −7% | Yes |
| C2 × 0.85 × 0.85 × 0.62 | 3.18 | 1,767x | −42% | **No** |

**HIV mortality composition.** HIV+ patients are ~6% of cases with an assumed ~11% case fatality. Removing them lowers mortality in the remaining pool to 0.0568, a further −5.3%. The 11% figure is my assumption, roughly in line with WHO's disproportionate share of TB deaths among people with HIV. The direction is clear; the size is uncertain.

**Interactions.**
- All filters are multiplicative with each other and with Critique 2, because the chain is a product.
- The mortality-composition effect also multiplies on top.
- The overlap with `adult_uptake` acts in the opposite direction. If the 60% already reflects "eligible clinicians would prescribe to," applying k compounds an exclusion that is already counted.

## Code

```python
base = dict(E=5.5e6, dec=0.02, yrs=8, up=0.60, m=0.06, rr=0.10,
            dpd=27, op=1e5, spd=1, cost=7e6, p=0.40)

def sroi(k=1.0, mort_adj=1.0, E=None, **kw):
    q = {**base, **kw}
    E = (E or q['E']) * k * (1 - q['dec'])**(q['yrs'] - 8)
    deaths = E * q['up'] * q['m'] * mort_adj * q['rr']
    return deaths * q['spd'] * q['dpd'] * q['op'] / q['cost'] * q['p']

B = sroi()
print(f"base {B:.0f}x, per 1M eligible {sroi(E=1e6):.1f}x, k* = {2000/B:.3f}")

# HIV composition: 6% HIV+ at ~11% CFR (assumed); rest of pool m solves 0.94m + 0.06*0.11 = 0.06
m_neg = (0.06 - 0.06 * 0.11) / 0.94
hiv_adj = m_neg / 0.06

scen = {
 "pulm 0.84": dict(k=.84), "pulm SEAR 0.75": dict(k=.75),
 "+other": dict(k=.84*.85), "+other+HIVmort": dict(k=.84*.85, mort_adj=hiv_adj),
 "+confirm": dict(k=.84*.85*.64),
 "+confirm+HIVmort": dict(k=.84*.85*.64, mort_adj=hiv_adj),
 "pessimistic": dict(k=.75*.80*.62),
 "C2": dict(E=7.1e6), "C2x.85x.85": dict(E=7.1e6, k=.85*.85),
 "C2x.85x.85x.62": dict(E=7.1e6, k=.85*.85*.62)}
for n, a in scen.items():
    s = sroi(**a)
    print(f"{n:18s} {s:6.0f}x  {s/B-1:+.1%}  {'above' if s >= 2000 else 'BELOW'} bar")
```

## Materiality verdict: YES on magnitude, BORDERLINE on the decision

- **Magnitude.** Even the mildest well-grounded filter (pulmonary only, −16%) is material. The central stack without confirmation is about −28% to −32%.
- **Decision.** The bar is crossed only if the confirmation filter (×~0.63) applies to real-world uptake, or if exclusions stack harshly. Without confirmation, the estimate sits 3–9% above the bar after accounting for mortality composition. That margin is thin and within the noise of the ungrounded ×0.85 factor.

**Most decision-relevant unknowns, in order:**
1. Will post-guideline use be restricted to bacteriologically confirmed pulmonary TB, or extended to clinically diagnosed cases? Statins are cheap and generic, so off-label extension is plausible.
2. How was the 5.5M derived? Does its implied ~0.8 haircut already cover applicability?
3. Does the 60% `adult_uptake` already net out non-applicable patients?

**Recommendation.** Model `applicability_fraction` explicitly as a parameter with range 0.40–1.0 and a central value of ~0.70, rather than leaving it implicit.

--- Critique: Shorter and new regimens erode both the eligible population and the incremental benefit ---

# CRITIQUE: Shorter and new regimens erode both the eligible population and the incremental benefit

## Bottom line

This critique could reduce SROI by about 2–8% under central assumptions, which is not material. Under pessimistic assumptions the reduction is 20–40%, and the estimate falls below the 2,000x bar only above about 35% HPMZ share with zero effect transfer.

## Parameter mapping

The model has no regimen term, so I map the critique onto an effective‑eligible multiplier on `eligible_people_at_8y`.

| Parameter | Location | Current value | How the critique enters |
|---|---|---|---|
| `eligible_people_at_8y` | Formula step 1 | 5,500,000 | Scaled by m = 1 − a·w·(1−t) |
| `relative_reduction` | Formula step 3 | 0.10 | Mathematically identical lever. Applying a transfer discount here or to eligibility gives the same SROI, because the model is fully multiplicative. |
| `adult_uptake` | Formula step 2 | 0.60 | An alternative mapping: guidelines may endorse statins only alongside HRZE, so HPMZ patients would not receive them. This is the case t = 0. |

The multiplier uses three new sub-parameters, none of which exist in the CEA:

- **a**: share of drug-susceptible TB patients on a non-HRZE backbone (essentially 4-month HPMZ) in the credited benefit year, which is year 8–9.
- **t**: transfer of the statin mortality effect to the HPMZ backbone. A value of 1 means the full effect; 0 means no effect or no adoption.
- **w**: deaths on HPMZ relative to deaths on HRZE, per patient. HPMZ excludes several groups:
  - children under 12;
  - people with HIV and CD4 < 100;
  - pregnant women;
  - low-weight patients.

  These are higher-mortality groups, so per-patient deaths among HPMZ users are probably below average, i.e. w < 1.

### Retained channels that do not map to the model

- **The pediatric 2HRZ(E)/2HR regimen.** It is still rifampicin-based, and the model already restricts uptake to adults. Its effect is about zero.
- **Smaller incremental benefit from a duration-shortening adjunct.** The CEA values only on-treatment mortality and gives no credit for treatment shortening. This channel has no parameter to erode. It would matter only if Thread 4's morbidity or shortening benefits were added to the model.
- **TRUNCATE-TB and bedaquiline-based regimens.** They are not standard of care and are unlikely to be by the horizon, so I assign them zero share.

## Plausible ranges

| Sub-parameter | Pessimistic | Central | Optimistic | Basis |
|---|---|---|---|---|
| a (HPMZ share) | 0.30–0.40 | 0.05–0.15 | 0.02 | The critique's 20–40% is flagged UNGROUNDED. The verified evidence (WHO's conditional recommendation, rifapentine supply and cost constraints, slow uptake so far) points to the low end. The central value is my judgement and is not sourced. |
| t (transfer) | 0 | 0.5 | 1.0–1.1 | No evidence exists either way; this is a genuine gap. A host-directed mechanism and the shared rifamycin CYP3A4 induction argue for substantial transfer. Guideline conservatism (endorsing statins only with HRZE) argues for t ≈ 0 in the near term. A modest t > 1 is possible if rifapentine induces CYP3A4 less strongly than rifampicin, but this is unverified. |
| w (relative per-patient deaths) | 1.0 | 0.8 | 0.7 | HPMZ exclusions concentrate deaths among HRZE patients. This is an assumption. |

## Sensitivity analysis

Base case:
- 19,800 deaths averted per year.
- Benefit of $OP 53.46B.
- SROI of 3,054.9x against a 2,000x bar.

Because SROI is linear in m, the break-even is m = 0.6547, a 34.5% cut. That corresponds to 3.60M effective eligible patients, matching the critique's "3.6M bar".

| Scenario | a | t | w | m | Deaths averted/yr | SROI | Δ |
|---|---|---|---|---|---|---|---|
| Base | 0 | – | – | 1.000 | 19,800 | 3,055x | 0% |
| Optimistic (better rifapentine exposure) | 0.20 | 1.1 | 0.8 | 1.016 | 20,117 | 3,104x | +1.6% |
| Low uptake, partial transfer | 0.05 | 0.5 | 0.8 | 0.980 | 19,404 | 2,994x | −2% |
| Central | 0.10 | 0.5 | 0.8 | 0.960 | 19,008 | 2,933x | −4% |
| Critique low end, partial transfer | 0.20 | 0.5 | 0.8 | 0.920 | 18,216 | 2,811x | −8% |
| Critique high end, partial transfer | 0.40 | 0.5 | 0.8 | 0.840 | 16,632 | 2,566x | −16% |
| Critique low end, zero transfer | 0.20 | 0 | 1.0 | 0.800 | 15,840 | 2,444x | −20% |
| Zero transfer | 0.30 | 0 | 1.0 | 0.700 | 13,860 | 2,138x | −30% |
| Critique high end, zero transfer (all pessimistic) | 0.40 | 0 | 1.0 | 0.600 | 11,880 | 1,833x | −40% |

**Individual levers.**
- a acts only through the product a·w·(1−t). With t = 1 (full transfer), a has zero effect whatever its value.
- t is the decisive unknown.
- w trims the effect by 0–30%.

**Joint effect.** The levers combine multiplicatively within m. The condition for crossing the bar is a·w·(1−t) ≥ 0.345:
- At t = 0 and w = 1, this needs a ≥ 34.5%.
- At t = 0.5 and w = 0.8, it needs a ≥ 86%, which is implausible.

**Interaction with other threads.** m multiplies the SROI after any other adjustments. Suppose other threads reduce SROI to about 2,100–2,400x. Then even the central −4% to −8% from this critique could push the estimate to or below 2,000x. This critique's materiality is therefore conditional on the cumulative position.

**Horizon note.** The model credits only one year of benefit, in year 8–9, so a rising HPMZ share after that year does not enter. If Thread 3 adopts a multi-year adoption-curve framing, a growing a over time would increase this critique's weight.

## Bottom-line impact

The critique reduces SROI by about 2–8% (to about 2,800–3,000x) under central assumptions: a = 5–20%, half-transfer, and deaths concentrated in HRZE patients.

The pessimistic range is −20% to −40% (about 2,440–1,830x). It requires both:
- zero effective transfer to HPMZ (for example, statins endorsed only alongside HRZE); and
- an HPMZ share of 20–40%, which is ungrounded.

The bar is crossed only when a > ~35% and t ≈ 0. A slight upside (about +2%) is possible if rifapentine reduces statin exposure less than rifampicin does.

## Materiality verdict

**BORDERLINE, leaning NO as a standalone critique.**
- At central values, the effect (−2% to −8%) is well inside the margin above the bar (the estimate is 53% above 2,000x).
- Only the conjunction of an ungrounded high adoption share and zero transfer crosses the bar.
- The critique becomes material if other threads have already eroded most of the margin.
- The most valuable information would be an evidence-based projection of HPMZ programme share around 2033, plus a statement of whether a Phase III on HRZE would be expected to generalise in WHO guidance.

## Code

```python
base = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
            all_in_cost=7_000_000, p_success=0.40)

def sroi(p, m=1.0):
    elig = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    treated = elig * m * p['adult_uptake']
    deaths = treated * p['baseline_mortality'] * p['relative_reduction']
    benefit = deaths * p['speedup_years'] * p['dalys_per_death'] * p['op_per_daly']
    return deaths, benefit / p['all_in_cost'] * p['p_success']

d0, s0 = sroi(base)
print(f"Base: deaths={d0:,.0f}, SROI={s0:,.1f}x")
m_be = 2000 / s0
print(f"Break-even m={m_be:.4f} (cut {1-m_be:.1%}), eligible={5.5e6*m_be:,.0f}")

scen = [("Optimistic", .20, 1.1, .8), ("Low", .05, .5, .8), ("Central", .10, .5, .8),
        ("Crit-low partial", .20, .5, .8), ("Crit-high partial", .40, .5, .8),
        ("Crit-low zero-transfer", .20, 0, 1), ("Zero-transfer 30%", .30, 0, 1),
        ("All pessimistic", .40, 0, 1)]
for name, a, t, w in scen:
    m = 1 - a * w * (1 - t)
    d, s = sroi(base, m)
    print(f"{name:24s} a={a:.2f} t={t:.1f} w={w:.1f} m={m:.3f} deaths={d:,.0f} "
          f"SROI={s:,.0f}x  Δ={s/s0-1:+.1%}  {'BELOW BAR' if s < 2000 else ''}")

# Break-even HPMZ share as a function of transfer t and weight w
for t in (0, .25, .5):
    for w in (1, .8):
        print(f"t={t}, w={w}: a_break-even = {(1-m_be)/(w*(1-t)):.2f}")
```

The code reproduces the base case of 19,800 deaths, 534,600 DALYs and 3,054.9x SROI, which matches the published figure of about 3,000x.

--- Critique: M72/AS01E and other incidence shocks are likely not large enough by year 8–10, but should be modelled ---

# CRITIQUE: M72/AS01E and other incidence shocks are likely not large enough by year 8–10, but should be modelled

## Key structural finding

The model credits **one year** of benefit (`speedup_years = 1`), around the adoption year (year 8). It has no multi-year benefit horizon. The critique's "average eligible over a 15+ year horizon could be 20–35% lower" scenario therefore **does not apply to this CEA as built**. Only the incidence shock in roughly years 8–10 matters.

Two further structural points:

- **The decline term does nothing at baseline.** `eligible_people_at_8y` already embeds the 2% decline to year 8, and the exponent `years_to_adoption − 8` equals 0. The decline only bites if adoption slips past year 8.
- **SROI scales one-for-one with eligible patients.** A vaccine shock that is independent of statin trial success enters as an exact multiplier: SROI × (1 − p_vaccine × r_conditional). There is no nonlinearity, so modelling p_vaccine separately is straightforward.

## Parameter mapping

| Parameter | Current value | Role |
|---|---|---|
| `eligible_people_at_8y` | 5,500,000 | Directly reduced by vaccine-averted incidence |
| `years_to_adoption` | 8 | Determines which calendar year's incidence counts. A later year means a larger vaccine effect and the 0.98^(n−8) decline applies. |
| New: `p_vaccine` | not modelled (implicitly 0) | Probability that M72 succeeds and is rolled out in high-burden countries by about 2033–35 |
| New: `r_cond` | not modelled (0) | Reduction in global drug-susceptible notifications at the credited year, conditional on vaccine success |

## Plausible ranges

**`p_vaccine`: 0.4–0.6, central 0.5.**
- The Phase IIb point estimate was 49.7%, but the 95% CI was wide (2.1–74.2%).
- The trial was restricted to IGRA+, HIV-negative adults.
- The 0.4–0.6 range is my judgement, not sourced. It reflects typical Phase III success for a vaccine with a positive but imprecise IIb, discounted for rollout timing.

**`r_cond` at year 8 (around 2033): 0–15%, central 5%.**
- If licensure is around 2028–30 with a slow rollout, only 3–5 years of partial coverage in a subset of countries would have accrued by year 8.
- The critique's 5–15% was flagged UNGROUNDED. The M72-specific South Africa and India models would be the right sources, but no numbers were extracted. I treat 0–15% as a judgement range.

**`r_cond` if adoption slips to year 10: 10–30%.**
- This is a tail scenario and is also ungrounded.

## Sensitivity analysis

**Base case:** 19,800 deaths/yr, 534,600 DALYs, **SROI = 3,055x** (bar = 2,000x).

### A. Conditional on vaccine success (`p_vaccine = 1`), adoption at year 8

| r_cond | Eligible | SROI | Δ |
|---|---|---|---|
| 5% | 5.225M | 2,902x | −5% |
| 10% | 4.95M | 2,749x | −10% |
| 15% | 4.675M | 2,597x | −15% |

### B. Expected value, `p_vaccine × r_cond` (the correct treatment, given independence)

| Scenario | Effective reduction | SROI | Δ |
|---|---|---|---|
| Low (vaccine fails or no effect by year 8) | 0% | 3,055x | 0% |
| Central (0.5 × 5%) | 2.5% | 2,979x | −2.5% |
| High (0.6 × 15%) | 9% | 2,780x | −9% |

### C. Joint pessimistic: adoption slips to year 10, plus a larger vaccine effect

A two-year slip alone (decline factor 0.98² = 0.9604) gives 2,934x (−4%).

| Scenario | SROI | Δ |
|---|---|---|
| Year 10, p_vaccine = 0.5, r_cond = 25% (expected value) | 2,567x | −16% |
| Year 10, vaccine succeeds, r_cond = 25% | 2,200x | −28% |
| Year 10, vaccine succeeds, r_cond = 30% | 2,054x | −33% (still above 2,000x) |
| Critique's "20–35% average" applied directly at year 8 | 2,444x to 1,986x | −20% to −35% |

The last row is not applicable under the current one-year-credit structure.

**Break-even:** SROI falls below 2,000x only if the eligible population falls by more than **34.5%** at the credited year, with no delay.

**How the effects combine:** The slip and the vaccine effect combine **multiplicatively** (0.9604 × (1 − r)). In this range that is close to additive.

### D. Optimistic direction

- **Case-finding scale-up.** If programmes such as the Global Fund push raise notified drug-susceptible cases 5–10% by year 8, eligible patients rise and SROI becomes **3,208x to 3,360x (+5% to +10%)**. This partly offsets the vaccine effect.
- **Case-mix shift.** If M72 mainly averts cases in IGRA+, HIV-negative people, the remaining cases skew toward HIV+ and higher-mortality patients. That would raise `baseline_mortality` slightly. This is a small offset that I did not quantify.

## Bottom-line impact

Modelled as an expected value, this critique **reduces SROI by about 0–9%, central about 2.5% (3,055x → ~2,980x)**.

- Conditional on M72 succeeding, the reduction is 5–15%.
- Only a combined tail (vaccine success, a 25–30% incidence drop, and a two-year adoption slip) reaches −28% to −33%, and even that stays above 2,000x.
- The critique's long-horizon 20–35% mechanism is inapplicable because the CEA credits only one year of benefit.

## Materiality verdict: **NO** (expected value)

The tail is **BORDERLINE**: −28% to −33% conditional on vaccine success with a delayed adoption, but it does not cross the bar. The finding becomes material only if GiveWell or CG restructures the CEA to credit a multi-year benefit stream. In that case this critique should be re-run against the new horizon, using M72 country-model incidence trajectories.

## Code

```python
base = dict(eligible_people_at_8y=5.5e6, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=1e5, speedup_years=1,
            all_in_cost=7e6, p_success=0.40)

def sroi(p, vax_red=0.0):
    elig = p['eligible_people_at_8y']*(1-p['decline_per_year'])**(p['years_to_adoption']-8)
    elig *= (1-vax_red)
    deaths = elig*p['adult_uptake']*p['baseline_mortality']*p['relative_reduction']
    benefit = deaths*p['speedup_years']*p['dalys_per_death']*p['op_per_daly']
    return benefit/p['all_in_cost']*p['p_success']

B = sroi(base)
print(f"base {B:.1f}")  # 3054.9

# A. conditional on vaccine success
for r in [0.05, 0.10, 0.15]:
    s = sroi(base, r); print(f"cond r={r}: {s:.0f} ({s/B-1:+.1%})")

# B. expected value: p_vaccine x r_cond
for pv, r in [(0, 0), (0.5, 0.05), (0.6, 0.15)]:
    s = sroi(base, pv*r); print(f"EV pv={pv} r={r}: {s:.0f} ({s/B-1:+.1%})")

# C. delay to year 10, alone and combined with vaccine effect
p10 = dict(base, years_to_adoption=10)
print("delay only", round(sroi(p10)))
for label, r in [("EV 0.5x25%", 0.125), ("succ 25%", 0.25), ("succ 30%", 0.30)]:
    s = sroi(p10, r); print(label, round(s), f"{s/B-1:+.1%}")
for r in [0.20, 0.35]:
    print("long-horizon avg", r, round(sroi(base, r)))

# break-even reduction to hit the 2,000x bar
print("break-even reduction:", 1-2000/B)  # ~0.345

# D. optimistic: case-finding raises notifications
for g in [0.05, 0.10]:
    print("case-finding +", g, round(sroi(base, -g)))
```

## Recommendation

1. Add explicit `p_vaccine` and `r_cond` parameters, sourced from the M72 South Africa and India models and global demand forecasts.
2. Report the conditional and expected-value SROI side by side.
3. Flag that any move to a multi-year benefit horizon makes this critique substantially more important.