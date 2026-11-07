--- Critique: Selection-on-success makes the "conditional 10%" an upward-biased estimate (winner's curse), and it is not shrunk ---

# Impact Assessment: Winner's-Curse Shrinkage on `relative_reduction`

## Parameter Mapping

| Parameter | Model key | Current value | Role in formula |
|---|---|---|---|
| Relative mortality reduction | `relative_reduction` | 0.10 | Linear multiplier on deaths averted |
| Probability Phase II and III succeed | `p_success` | 0.40 | Linear multiplier on SROI (secondary; see the interaction section) |
| Modifiable baseline mortality | `baseline_mortality` | 0.06 | Linear multiplier (secondary; joint test only) |

**Formula chain:**

SROI = [5.5M × 0.98^0 × 0.60 × 0.06 × **rr** × 1 × 27 × 100,000] / 7M × 0.40

Because `rr` enters multiplicatively, **SROI scales 1:1 with `relative_reduction`**. A shrinkage factor *k* applied to rr reduces SROI by exactly (1 − *k*).

**Reproduced base case:** 19,800 deaths averted per year, 534,600 DALYs, benefit of $OP 53.46B, and **SROI = 3,055x**. This matches the parameter summary.

## Plausible Range

**`relative_reduction`:** current value 0.10. Plausible range is **0.05–0.10** under the critique, with 0.05–0.08 if shrinkage of 0.5–0.8 applies.

- The 0.5–0.8 shrinkage factor is the critic's own assumption. It is not TB-specific evidence.
- The verified evidence offers one weak empirical anchor: the TB-meningitis corticosteroid meta-analyses. The older, smaller Cochrane pooled RR was 0.79 and the later, larger one was 0.84.
  - The implied ratio of relative reductions is 0.16 / 0.21 ≈ **0.76**.
  - The ratio on the log scale is ln(0.84) / ln(0.79) ≈ **0.74**.
  - This sits inside the critic's range, but it is a single, confounded comparison. It does not validate the range.

**Important caveat on applicability:** CG frames the 10% as an *assumed* effect conditional on a positive result, not as an observed Phase IIa/b point estimate.

- Winner's curse applies strictly to observed estimates that were selected on significance.
- If the 10% is a prior-based assumption, the bias may be smaller or absent.
- The upper end of the range (no shrinkage, rr = 0.10) is therefore retained.

**Optimistic direction:** the RR 0.84 adjunct benchmark (a 16% reduction) could be read as implying that 10% is conservative. I test rr = 0.12–0.16 for completeness. However, this critique is one-directional, and the benchmark comes from a different condition (TBM, which has much higher mortality) and a different mechanism.

## Sensitivity Analysis

**Base case:** SROI = 3,055x. Funding bar = 2,000x.

### Single-parameter tests on `relative_reduction`

| rr (shrinkage *k*) | Deaths averted/yr | SROI | Δ vs base | Above 2,000x bar? |
|---|---|---|---|---|
| 0.050 (k = 0.50) | 9,900 | 1,527x | −50% | No |
| 0.060 (k = 0.60) | 11,880 | 1,833x | −40% | No |
| **0.0655 (k = 0.655, breakeven)** | 12,960 | **2,000x** | −34.5% | Threshold |
| 0.065 (k = 0.65, mid of 0.5–0.8) | 12,870 | 1,986x | −35% | Just below |
| 0.074 (k = 0.74, TBM anchor) | 14,650 | 2,261x | −26% | Yes |
| 0.080 (k = 0.80) | 15,840 | 2,444x | −20% | Yes |
| 0.100 (no shrinkage) | 19,800 | 3,055x | 0% | Yes |
| 0.120 (optimistic) | 23,760 | 3,666x | +20% | Yes |
| 0.160 (TBM-benchmark optimistic) | 31,680 | 4,888x | +60% | Yes |

### Expected-value summaries

- *k* ~ Uniform(0.5, 0.8): mean SROI = **1,986x** (−35%).
- *k* ~ Uniform(0.5, 1.0), which allows for the possibility that no shrinkage is warranted: mean SROI = **2,291x** (−25%).

### Interactions (multiplicative, not additive)

A real winner's-curse story implies that a smaller true effect also lowers trial power. That means `p_success` should fall too, so `p_success` and `relative_reduction` are not independent.

| Scenario | SROI | Δ |
|---|---|---|
| rr = 0.065, p_success = 0.30 | 1,489x | −51% |
| rr = 0.05, p_success = 0.30 (pessimistic joint) | 1,145x | −63% |
| rr = 0.05, p_success = 0.30, baseline_mortality = 0.05 (all pessimistic) | 955x | −69% |

**Double-counting caution:** lowering both parameters is legitimate only if `p_success = 0.40` was set assuming the larger effect. If CG's 40% already reflects uncertainty about the effect's existence, then cutting both overlaps partly. The joint rows should be read as an upper bound on the downside.

## Bottom-Line Impact

**If the 10% is an unshrunk, significance-selected estimate, applying plausible shrinkage (0.5–0.8) reduces SROI by 20–50% (from 3,055x to 1,527–2,444x), with a central estimate of about −35% (≈1,990x).** The funding bar is crossed whenever shrinkage exceeds about 35% (k < 0.655).

## Materiality Verdict: **BORDERLINE (decision-relevant, but evidentially weak)**

**Why it is decision-relevant:**
- The plausible range straddles the 2,000x bar.
- The midpoint of the critic's range lands essentially *on* the bar.
- So the funding decision is sensitive to this parameter.

**Why it is not a clear YES:**
- The core premise is unestablished. It is unknown whether the 10% is a selected observed estimate or a prior assumption.
- The specific shrinkage factor is illustrative.
- The only empirical anchor (k ≈ 0.75) implies SROI ≈ 2,260x, which is still above the bar.

**Recommendation:**
- CG should state how the 10% was derived.
- CG should report SROI over rr ∈ [0.05, 0.10].
- CG should flag rr ≈ 0.065 as the breakeven point.

## Code

```python
def sroi(rr=0.10, p=0.40, bm=0.06, elig8=5_500_000, yrs=8, decl=0.02,
         uptake=0.60, dpd=27, opd=100_000, speed=1, cost=7_000_000):
    eligible = elig8 * (1 - decl) ** (yrs - 8)
    treated = eligible * uptake
    deaths = treated * bm * rr
    benefit = deaths * speed * dpd * opd
    return benefit / cost * p, deaths

base, d0 = sroi()
print(f"Base: deaths={d0:,.0f}, SROI={base:,.0f}x")   # 19,800 ; 3,055x

# Single-parameter sweep on relative_reduction
for rr in [0.05, 0.06, 0.065, 0.074, 0.08, 0.10, 0.12, 0.16]:
    s, d = sroi(rr=rr)
    print(f"rr={rr:.3f} deaths={d:,.0f} SROI={s:,.0f}x "
          f"delta={(s / base - 1) * 100:+.0f}%")

# Breakeven rr for the 2,000x bar
print("breakeven rr =", 0.10 * 2000 / base)          # ~0.0655

# Expected SROI under uniform shrinkage priors (linear, so mean k suffices)
import numpy as np
for lo, hi in [(0.5, 0.8), (0.5, 1.0)]:
    k = np.random.default_rng(0).uniform(lo, hi, 100_000)
    print(f"k~U({lo},{hi}): mean SROI={np.mean(base * k):,.0f}x")

# TBM anchor: older vs later pooled corticosteroid RR
print("anchor k (linear) =", 0.16 / 0.21,
      "| (log) =", np.log(0.84) / np.log(0.79))

# Joint tests
for kw in [dict(rr=0.065, p=0.30),
           dict(rr=0.05, p=0.30),
           dict(rr=0.05, p=0.30, bm=0.05)]:
    s, _ = sroi(**kw)
    print(kw, f"SROI={s:,.0f}x delta={(s / base - 1) * 100:+.0f}%")
```

--- Critique: A mortality-powered Phase III costs several multiples of $7M, and trial-population mortality makes it worse ---

# CRITIQUE: A mortality-powered Phase III costs several multiples of $7M, and trial-population mortality makes it worse

**Bottom line:** If the CEA assumes a Phase III powered on mortality in the general drug-susceptible TB population, SROI falls by 70–93%, to roughly 220–910x, and the grant drops below the 2,000x bar. The critique does not survive in that form if the trial is enriched, but enrichment then pushes the problem into `p_success`.

## Parameter Mapping

| Parameter | Model key | Current value | Role in this critique |
|---|---|---|---|
| All-in cost | `all_in_cost` | $7,000,000 | Primary. Phase III cost enters the denominator directly. |
| Probability of success | `p_success` | 0.40 | Secondary. This is the either/or channel: a trial powered for a larger effect is cheaper but underpowered for a true 10% effect. |
| Trial-arm baseline mortality | `baseline_mortality` | 0.06 | Sets the trial sample size, not the benefit. Benefit stays at 6% × 3.3M treated. |
| Effect size | `relative_reduction` | 0.10 | The effect the trial must detect. |
| Years to adoption | `years_to_adoption` | 8 | Tertiary. A bigger trial takes longer, and eligible patients fall 2% per year. |

Fixed quantities derived from the model:
- **Numerator:** benefit × p_success = $OP 53.46B × 0.40 = $OP 21.384B.
- **Base SROI:** 3,055x.
- **Break-even `all_in_cost` at the 2,000x bar:** $10.69M. This matches the critique's $10.7M.

## Sample Size Verification

The calculation uses two proportions, α = 0.05 two-sided, 80% power, and (1.96 + 0.84)² = 7.84.

| Trial baseline mortality | Design effect | Per arm | Total |
|---|---|---|---|
| 6.0% | 10% RRR | 23,407 | **46,814** ✔ matches the critique (~47k) |
| 3.0% | 10% RRR | 48,234 | **96,468** ✔ matches the critique (~96k) |
| 15% (enriched: HIV+ or hospitalized) | 10% RRR | 8,512 | 17,024 |
| 20% (enriched) | 10% RRR | 6,029 | 12,058 |
| 6.0% | 30% RRR (IMPI-style) | 2,338 | 4,676 |

The critique's arithmetic is correct.

## Plausible Range

**Per-participant cost: $500–$1,000 as the working range, with $1,000+ more likely.**
- The verified evidence makes $500 a floor, not a central value.
- TB-PRACTECAL cost about €61k per patient and a modelled TB vaccine trial about $7,500 per subject. Neither is comparable, but both sit far above $1,000.
- Pragmatic or registry-embedded designs could approach $500.

**How the trial cost enters `all_in_cost`.** The CEA gives no line-item breakdown, so I bracket two cases:
- **Replace:** `all_in_cost` equals the trial cost. This assumes the trial dominates all-in cost and the $7M was essentially the Phase III budget. It is the critique's framing.
- **Additive:** `all_in_cost` = $7M + trial cost. This assumes the $7M covers Phase II, guideline work and a smaller trial. It is the pessimistic case.

## Sensitivity Analysis

Base case SROI is 3,055x. Funding bar is 2,000x.

### A. Mortality-powered, general population (the critique's scenario)

| Scenario | N | Trial cost | SROI (replace) | Δ | SROI (additive) | Δ |
|---|---|---|---|---|---|---|
| 6%, $500/pt | 46,814 | $23.4M | 914x | −70.1% | 703x | −77.0% |
| 6%, $1,000/pt | 46,814 | $46.8M | 457x | −85.0% | 397x | −87.0% |
| 3%, $500/pt | 96,468 | $48.2M | 443x | −85.5% | 387x | −87.3% |
| 3%, $1,000/pt | 96,468 | $96.5M | 222x | −92.7% | 207x | −93.2% |
| Tail: 6%, $7,500/pt | 46,814 | $351M | 61x | −98.0% | 60x | −98.0% |

- Every case falls below the 2,000x bar.
- The critique's "about 70% or more" is exactly the lowest-cost replace case, so the claim is accurate as a floor.

### B. Counter-scenarios from the Verifier

**Enriched population, 10% RRR still powered:**

| Scenario | N | Trial cost | SROI (replace) | Δ | SROI (additive) | Δ |
|---|---|---|---|---|---|---|
| 15%, $500/pt | 17,024 | $8.5M | 2,512x | −17.8% | 1,379x | −54.9% |
| 15%, $1,000/pt | 17,024 | $17.0M | 1,256x | −58.9% | 890x | −70.9% |
| 20%, $500/pt | 12,058 | $6.0M | 3,547x* | +16% | 1,644x | −46.2% |
| 20%, $1,000/pt | 12,058 | $12.1M | 1,773x | −42.0% | 1,108x | −63.7% |

\*Optimistic direction: a cheap enriched trial costs less than the assumed $7M.

Enrichment has two caveats:
- Generalizing a mortality effect from high-risk patients to the 6%-mortality population is itself uncertain.
- Enrichment is the only route that keeps the grant near the bar.

**Powered for a 30% RRR at 6% baseline (N = 4,676; $2.3–4.7M):**
- Cost fits within $7M, so `all_in_cost` is unchanged or lower.
- If the true effect is 10%, power falls to about 14%, against the 80% implicitly needed.
- Scaling the trial-stage success probability by 0.14/0.80 = 0.176 gives `p_success` ≈ 0.07, which yields SROI ≈ 535x (−82%).
- This is crude: `p_success` also bundles Phase II, and guidelines might accept a surrogate endpoint.
- This is the "either/or" with Critique 3. The cost penalty and the `p_success` penalty are substitutes, not additive. Do not stack them.

### C. Interaction with trial duration
A larger trial adding about 2 years to `years_to_adoption` (8 → 10) multiplies eligible patients by 0.98² = 0.960, a −4% change. Combined with the 6%/$500 replace case, SROI is 877x (−71.3%). The effects are multiplicative, and duration is minor next to cost.

### Break-even sample sizes at the 2,000x bar

| Cost basis | $500/pt | $1,000/pt |
|---|---|---|
| Replace | 21,384 participants | 10,692 participants |
| Additive (only $3.69M headroom) | 7,384 participants | 3,692 participants |

A general-population mortality-powered trial (≥ 47k) exceeds every break-even threshold. A 15–20% mortality enriched trial (12–17k) is near the threshold only under replace accounting at about $500 per participant.

## Bottom-Line Impact

**Mortality-powered general-population case:** SROI falls from 3,055x to about 220–910x (−70% to −93%). The central estimate is about −85% (about 450x at roughly $47M).

**Cheaper designs:**
- An enriched design gives −18% to −71%, with the sign possibly positive at very low cost.
- An underpowered larger-effect design moves the loss into `p_success`, for about −80%.

## Materiality Verdict

**YES.** If the CEA assumes a mortality-powered Phase III in the general drug-susceptible TB population, every tested combination drops SROI below the 2,000x bar.

**BORDERLINE** if the design is enriched (15–20% mortality) and the $7M was essentially the Phase III budget. SROI then ranges from about 1,250x to about 3,500x, straddling the bar.

The decision-relevant unknown is the one the CEA does not state: the Phase III endpoint, sample size and cost per participant. GiveWell should request this before relying on the $7M figure.

## Code

```python
from math import sqrt
from statistics import NormalDist

# --- GiveWell/CG model, exact formula chain ---
P = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
         adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
         dalys_per_death=27, op_per_daly=100_000, speedup_years=1,
         all_in_cost=7_000_000, p_success=0.40)

def sroi(**o):
    p = {**P, **o}
    elig = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    deaths = elig * p['adult_uptake'] * p['baseline_mortality'] * p['relative_reduction']
    benefit = deaths * p['speedup_years'] * p['dalys_per_death'] * p['op_per_daly']
    return benefit / p['all_in_cost'] * p['p_success']

BASE = sroi()                                  # 3054.9
breakeven_cost = BASE * P['all_in_cost'] / 2000  # ~$10.69M

# --- Two-proportion sample size, alpha=.05 two-sided, power=.80 ---
def n_per_arm(p0, rrr, z=7.84):
    p1 = p0 * (1 - rrr)
    return z * (p0*(1-p0) + p1*(1-p1)) / (p0 - p1)**2

def power(p0, rrr_true, n):
    p1 = p0 * (1 - rrr_true)
    se = sqrt((p0*(1-p0) + p1*(1-p1)) / n)
    return NormalDist().cdf(abs(p0 - p1)/se - 1.96)

def report(label, cost):
    s = sroi(all_in_cost=cost)
    print(f"{label:38s} cost=${cost/1e6:6.1f}M SROI={s:7.0f}x Δ={s/BASE-1:+.1%}")

for p0 in (0.06, 0.03, 0.15, 0.20):
    N = 2 * n_per_arm(p0, 0.10)
    for c in (500, 1000):
        trial = N * c
        report(f"p0={p0:.2f} N={N:,.0f} ${c} replace", trial)
        report(f"p0={p0:.2f} N={N:,.0f} ${c} additive", 7e6 + trial)

report("tail 6% $7,500/pt replace", 2*n_per_arm(0.06, 0.10)*7500)

# Powered for 30% RRR, true effect 10%
n30 = n_per_arm(0.06, 0.30)                    # ~2,338/arm
pw = power(0.06, 0.10, n30)                    # ~0.14
s = sroi(p_success=0.40 * pw/0.80)
print(f"30%-powered design: power={pw:.2f}, SROI={s:.0f}x Δ={s/BASE-1:+.1%}")

# Duration interaction
trial = 2 * n_per_arm(0.06, 0.10) * 500
s = sroi(all_in_cost=trial, years_to_adoption=10)
print(f"+2y duration, 6%/$500 replace: SROI={s:.0f}x Δ={s/BASE-1:+.1%}")

# Break-even N
for c in (500, 1000):
    print(c, "replace:", breakeven_cost/c, "additive:", (breakeven_cost - 7e6)/c)
```

--- Critique: If Phase III is surrogate-powered, costs and benefits describe different interventions ---

# CRITIQUE: If Phase III is surrogate-powered, costs and benefits describe different interventions

## Framing before quantifying

**1. Delay alone barely matters in this model.** The BOTEC has no time discounting. The only penalty for later adoption is the 2%/yr decline in TB incidence, which acts through `years_to_adoption` and the `eligible` term. A 2–5 year guideline delay therefore moves SROI by only 4–10%. The critique's impact runs mainly through `adult_uptake`, `speedup_years`, `relative_reduction` and `all_in_cost`. It does not run through delay.

**2. A $7M Phase III almost certainly cannot be mortality-powered.** Detecting 6.0% → 5.4% mortality (10% relative reduction) at 80% power and two-sided α = 0.05 needs about 23,400 per arm, or about 47,000 total. At 90% power it needs about 63,000. Restricting to a high-risk subgroup with 15% mortality still needs about 17,000. Unless the budget assumes under $150 per participant, the funded trial is effectively surrogate- or composite-powered.
- This strengthens the factual premise of the critique.
- It also shows that the "mortality-powered" horn is not really a cost overrun of the grant. It is a separate, much larger follow-on trial.

**3. The two horns are mutually exclusive.** They are modelled as alternative branches, not stacked:
- **Branch A:** WHO accepts surrogate or composite evidence, with a conditional recommendation, lower uptake, and possibly less counterfactual speedup.
- **Branch B:** WHO requires mortality evidence, so a follow-on trial is needed. This overlaps with Critique 1 and must not be double-counted with it.

## PARAMETER MAPPING

| Parameter | Location in model | Current value | Branch |
|---|---|---|---|
| `adult_uptake` | treated = eligible × uptake | 0.60 | A |
| `speedup_years` | benefit multiplier | 1.0 | A |
| `years_to_adoption` | eligible = 5.5M × 0.98^(y−8) | 8 | A, B |
| `relative_reduction` | mortality effect credited on surrogate success | 0.10 | A (effect translation) |
| `all_in_cost` | SROI denominator | $7M | B |
| `p_success` (extra hurdle: mortality trial confirms) | SROI multiplier | 0.40 | B (sensitivity only) |

## PLAUSIBLE RANGES

The evidence base is weak, so these ranges are judgment-based and are flagged as such.

**`adult_uptake`: 0.60 → [0.40, 0.60], central 0.50.**
- Conditional WHO recommendations with "low/moderate certainty" ratings typically see slower and patchier national adoption than strong ones.
- An adjunctive drug also adds pill burden and drug–drug-interaction screening (rifampicin, boosted PIs).
- Upper bound unchanged: WHO has adopted regimen changes on composite "unfavourable outcome" endpoints. Examples are 4-month HPMZ (Study 31/A5349) and SHINE. This is the critique's own caveat.
- These precedents are non-inferiority shortening trials, not an adjunct claiming a mortality benefit, so they only partly transfer.

**`speedup_years`: 1.0 → [0.75, 1.0].**
- If guideline bodies wait for post-recommendation or observational mortality data, the counterfactual acceleration attributable to this trial shrinks.
- No direct evidence supports this, so the range is kept narrow.

**`years_to_adoption`: 8 → [9, 11] (Branch A); [12, 13] (Branch B).**
- Branch B assumes a follow-on mortality trial of roughly 4–5 years.

**`relative_reduction` (effective, given surrogate success): 0.10 → [0.08, 0.10].**
- This captures imperfect surrogate-to-mortality translation.
- The upper end stays at 0.10 because unfavourable outcome includes death, so it is not a pure surrogate.
- This partly overlaps with any separate "effect-size / winner's curse" critique.

**`all_in_cost`: $7M → $22M–$57M (Branch B).**
- This adds a $15–50M follow-on trial: about 47k participants at roughly $300–1,000 each, or a smaller high-risk-population trial.

**Extra hurdle in Branch B: P(mortality trial confirms | surrogate success) ∈ [0.6, 1.0].**
- Shown separately because it overlaps with the `relative_reduction` assumption.

## SENSITIVITY ANALYSIS

**Base case:** 3.3M treated, 19,800 deaths averted per year, benefit $OP 53.46B, **SROI = 3,055x**. Funding bar = 2,000x, which corresponds to a 34.5% reduction.

### One-at-a-time

| Change | SROI | Δ |
|---|---|---|
| adult_uptake 0.50 | 2,546x | −16.7% |
| adult_uptake 0.40 | 2,037x | −33.3% |
| speedup_years 0.75 | 2,291x | −25.0% |
| years_to_adoption 10 | 2,934x | −4.0% |
| years_to_adoption 12 | 2,818x | −7.8% |
| relative_reduction 0.08 | 2,444x | −20.0% |
| all_in_cost $15M | 1,426x | −53.3% |
| all_in_cost $22M | 972x | −68.2% |
| all_in_cost $47M | 455x | −85.1% |

### Branch A (surrogate accepted, conditional recommendation)

| Scenario | Parameters | SROI | Δ |
|---|---|---|---|
| Optimistic | no change (WHO treats composite as adequate) | 3,055x | 0% |
| Mild | uptake 0.55, years 9 | 2,744x | −10% |
| Central | uptake 0.50, years 10 | 2,445x | −20% |
| Pessimistic (adoption only) | uptake 0.40, speedup 0.75, years 11 | 1,438x | −53% |
| Pessimistic + effect translation | above + rr 0.08 | 1,150x | −62% |

### Branch B (follow-on mortality trial required; overlaps Critique 1)

| Scenario | Parameters | SROI | Δ |
|---|---|---|---|
| Low | cost $22M, years 12 | 897x | −71% |
| Central | cost $32M, years 12 | 616x | −80% |
| High | cost $57M, years 13 | 344x | −89% |
| Central × P(confirm) 0.7 | | 431x | −86% |

### Interactions

All parameters enter multiplicatively, except `years_to_adoption`, which enters as 0.98^Δy and is also multiplicative. Joint effects are therefore products of the individual factors, not sums. For example, Branch A pessimistic = 0.667 × 0.75 × 0.941 = 0.471.

### Break-even values for staying at or above 2,000x (single parameter)

- `adult_uptake` ≥ 0.393
- `speedup_years` ≥ 0.655
- `relative_reduction` ≥ 0.0655
- `all_in_cost` ≤ $10.7M, i.e. at most about $3.7M of extra cost

### Probability-weighted view (illustrative)

Using Branch A central (2,445x) and Branch B central (616x), expected SROI stays above the bar only if P(follow-on mortality trial required) ≤ about 24%.

## Offsetting consideration (optimistic direction)

If the trial succeeds on unfavourable outcome through reduced relapse or treatment failure, the model gives zero credit for that. It values only deaths. Relapse prevention has morbidity, mortality and transmission value that the BOTEC omits. This partly offsets Branch A losses but is not quantified here, because the model has no relapse parameter.

## BOTTOM-LINE IMPACT

- **If WHO accepts surrogate or composite evidence (Branch A, most likely):** SROI falls by 0–62%. The central estimate is about −20% (3,055x → about 2,450x), which stays above the 2,000x bar.
- **If a mortality trial is required (Branch B):** SROI falls by about 70–89% (to roughly 340–900x), well below the bar. This branch is largely Critique 1 and should not be added to it.

## MATERIALITY VERDICT: **BORDERLINE**

- **Branch A, central:** the change exceeds a ~10% materiality threshold but does not flip the funding decision.
- **Flips below 2,000x if any of the following holds:**
  - Uptake falls below about 0.39.
  - Speedup falls below about 0.66.
  - Effective mortality effect falls below about 6.5%.
  - P(follow-on trial needed) exceeds about 24%.
- **Overall:** given the weak evidence on WHO's treatment of surrogate-endpoint adjunct trials, the verdict is borderline.
- **Recommendation:** confirm the Phase III primary endpoint and sample size, and merge this with Critique 1 as a single "cost–benefit design consistency" item.

## CODE

```python
import math

BASE = dict(eligible_people_at_8y=5_500_000, years_to_adoption=8, decline_per_year=0.02,
            adult_uptake=0.60, baseline_mortality=0.06, relative_reduction=0.10,
            dalys_per_death=27, op_per_daly=100_000, speedup_years=1.0,
            all_in_cost=7_000_000, p_success=0.40)

def sroi(**ovr):
    p = {**BASE, **ovr}
    elig = p['eligible_people_at_8y'] * (1 - p['decline_per_year'])**(p['years_to_adoption'] - 8)
    deaths = elig * p['adult_uptake'] * p['baseline_mortality'] * p['relative_reduction']
    benefit = deaths * p['speedup_years'] * p['dalys_per_death'] * p['op_per_daly']
    return benefit / p['all_in_cost'] * p['p_success']

base = sroi()
def show(label, **o):
    v = sroi(**o); print(f"{label:45s} {v:8.0f}x  {100*(v/base-1):+6.1f}%")

print(f"Base {base:.1f}x")
for u in (0.5, 0.4, 0.3): show(f"uptake {u}", adult_uptake=u)
for s in (0.75, 0.5): show(f"speedup {s}", speedup_years=s)
for y in (10, 12): show(f"years {y}", years_to_adoption=y)


--- Critique: WHO is unlikely to rely on a single trial ---

# CRITIQUE: WHO is unlikely to rely on a single trial

## Parameter Mapping

The model is SROI = [eligible × uptake × baseline_mortality × relative_reduction × speedup × DALYs/death × $OP/DALY] / all_in_cost × p_success. The critique enters through three parameters:

| Parameter | Current value | How the critique affects it |
|---|---|---|
| `all_in_cost` | $7,000,000 | A second confirmatory trial, or extra safety and acceptability data, adds cost. The model counts all funders, so co-funding does not dilute the cost. |
| `p_success` | 0.40 (Phase II and III succeed jointly) | If WHO needs replication, success requires a second positive trial, which multiplies in a replication probability. |
| `years_to_adoption` | 8 | A second trial delays adoption. Under the model's 2%/yr decline in cases, fewer patients are eligible at adoption. |
| `speedup_years` (sensitivity only) | 1 | Speedup changes only if the second trial erodes the grant's counterfactual lead. If both worlds need the second trial, speedup is unchanged. |

**Not changed:** `relative_reduction`, `baseline_mortality` and `adult_uptake`. These belong to separate critiques (surrogate vs. mortality endpoint, and drug–drug interactions) and are excluded to avoid double counting.

## Plausible Ranges

The cost breakdown is not disclosed, so these are explicit assumptions rather than findings.

**`all_in_cost`: $7M base, range $7M–$14M.**
- **Low ($7M):** One trial suffices, as with the R21 precedent for vaccines.
- **Central (+$3.5M → $10.5M):** A second trial costing about the Phase III share of the budget, assumed to be 50% of $7M.
- **High ($14M):** The second trial costs as much as the whole current program.
- **Context, not counted here:** A trial powered on mortality (6% → 5.4%, 80% power, α = 0.05) needs about 23,400 per arm, roughly 47,000 total. At $500–1,500 per participant, that suggests $7M may not fund even one mortality-powered trial. That belongs to the separate powerability critique.

**`p_success`: 0.40 base, range 0.28–0.40.**
- The joint probability equals 0.40 × P(replication | first trial positive).
- A replication trial's power is about 0.8, discounted for first-trial false positives and the winner's curse. That gives P(replication) of roughly 0.70–0.85, so `p_success` falls to 0.28–0.34.

**`years_to_adoption`: 8 base, range 8–11.** A second trial adds about 2–3 years of enrolment, follow-up and review.

**`speedup_years`: 1 base, pessimistic test only at 0.75.**

## Sensitivity Analysis

**Base case:** about 19,800 deaths averted per year, benefit $OP 53.46B, **SROI = 3,055x**. The funding bar is 2,000x.

### One parameter at a time

| Scenario | SROI | Δ vs. base |
|---|---|---|
| Cost $10.5M (central second trial) | 2,036x | −33% |
| Cost $12.6M | 1,697x | −44% |
| Cost $14M (cost doubles) | 1,527x | −50% |
| p_success 0.34 | 2,597x | −15% |
| p_success 0.28 | 2,138x | −30% |
| Adoption delayed 2 years (eligible × 0.960) | 2,934x | −4% |
| Adoption delayed 3 years (eligible × 0.941) | 2,876x | −6% |
| Speedup 0.75 | 2,291x | −25% |

**Break-even points against the 2,000x bar (each parameter alone):**
- Cost above **$10.7M** (+53%).
- p_success below **0.262**, which corresponds to P(replication) below about 0.65.

### Joint scenarios

The effects are **multiplicative**, because SROI is a product and ratio of these terms.

| Scenario | Inputs | SROI | Δ vs. base |
|---|---|---|---|
| Central | $10.5M, p = 0.34, +2 years | 1,663x | −46% |
| Pessimistic | $14M, p = 0.28, +3 years | 1,006x | −67% |
| Pessimistic + speedup erosion | above, plus speedup 0.75 | 755x | −75% |
| Optimistic | One trial suffices (R21-like path) | 3,055x | 0% |

On the upside, the critique cannot raise SROI. Cost-sharing does not help because `all_in_cost` is already all-funder. Any uptake boost from stronger evidence is not modelled and is likely small.

### Probability-weighted

The verified evidence is mixed:
- WHO treatment guidelines, unlike vaccine recommendations, tend to want multiple trials or a single large multi-site trial rated high certainty under GRADE.
- A modest-effect, host-directed adjunct is less likely to earn high certainty from one trial.
- But the critique is rated weak, and a large multi-site trial with a hard mortality endpoint could suffice.

I therefore assign q = P(second trial required) = 0.25–0.50.

| q | Central conditional case | Pessimistic conditional case |
|---|---|---|
| 0.25 | 2,707x (−11%) | 2,543x (−17%) |
| 0.50 | 2,359x (−23%) | 2,031x (−34%) |

## Bottom-Line Impact

**In expectation, this critique reduces SROI by about 11–34%, from 3,055x to roughly 2,000–2,700x, with a central estimate near −20%. If a second trial is in fact required, SROI falls 33–67% (to roughly 1,000–2,000x), which is below the 2,000x bar in most conditional scenarios.**

## Materiality Verdict

**BORDERLINE, leaning YES.**
- The expected-value estimate stays at or just above the 2,000x bar.
- Conditional on WHO requiring replication, the grant likely falls below the bar. Cost alone crosses it at $10.7M.
- The result is highly sensitive to two undisclosed facts: the Phase III design (endpoint, size, sites) and the WHO pathway (a TB guideline development group, not SAGE or prequalification).
- CG should state whether $7M assumes a single trial and whether that trial is mortality-powered. If it is not mortality-powered, this critique compounds with the powerability critique.

## Code

```python
def sroi(eligible_8y=5.5e6, years_to_adoption=8, decline=0.02, uptake=0.60,
         base_mort=0.06, rel_red=0.10, dalys_per_death=27, op_per_daly=1e5,
         speedup=1.0, cost=7e6, p=0.40):
    eligible = eligible_8y * (1 - decline) ** (years_to_adoption - 8)
    deaths = eligible * uptake * base_mort * rel_red
    benefit = deaths * speedup * dalys_per_death * op_per_daly
    return benefit / cost * p

base = sroi()
print(f"Base SROI: {base:,.0f}x")

def show(label, **kw):
    v = sroi(**kw)
    print(f"{label:45s} {v:7,.0f}x  Δ={100*(v/base-1):+5.1f}%")
    return v

# One-at-a-time
for c in [10.5e6, 12.6e6, 14e6]:
    show(f"cost=${c/1e6:.1f}M", cost=c)
for p in [0.34, 0.28]:
    show(f"p_success={p}", p=p)
for y in [10, 11]:
    show(f"years_to_adoption={y}", years_to_adoption=y)
show("speedup=0.75", speedup=0.75)

# Break-evens vs. 2,000x bar
print("Cost break-even: $%.2fM" % (7 * base / 2000))
print("p_success break-even: %.3f" % (0.40 * 2000 / base))

# Joint scenarios
central = show("JOINT central", cost=10.5e6, p=0.34, years_to_adoption=10)
pess = show("JOINT pessimistic", cost=14e6, p=0.28, years_to_adoption=11)
show("JOINT pess + speedup 0.75", cost=14e6, p=0.28,
     years_to_adoption=11, speedup=0.75)

# Probability-weighted by q = P(second trial required)
for q in [0.25, 0.50]:
    for name, cond in [("central", central), ("pessimistic", pess)]:
        ev = (1 - q) * base + q * cond
        print(f"q={q}, {name}: E[SROI]={ev:,.0f}x  Δ={100*(ev/base-1):+.1f}%")

# Context: sample size for a mortality-powered trial
p1, p2 = 0.06, 0.054
n_arm = (1.96 + 0.84) ** 2 * (p1 * (1 - p1) + p2 * (1 - p2)) / (p1 - p2) ** 2
print(f"Mortality-powered n per arm ≈ {n_arm:,.0f} (total ≈ {2 * n_arm:,.0f})")
```