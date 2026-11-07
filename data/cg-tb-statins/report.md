# Context for this analysis (read first)

This red-team pipeline was built for GiveWell's cost-effectiveness spreadsheets. In this run it is
applied to an analysis by a different funder in a different format. Read every instruction with
these substitutions:

1. **Funder.** Wherever the instructions say "GiveWell", read "Coefficient Giving (CG)", formerly
   Open Philanthropy. "GiveWell's intervention report" means the CG text below. There is no prior
   AI red-teaming output from CG; that input is empty.
2. **Model format.** The CEA is a short prose back-of-the-envelope calculation (BOTEC), not a
   spreadsheet. The CEA Parameter Summary lists its parameters by name; those names are the
   "cells". The quantifier's sensitivity analysis runs on an exact replica of the formula chain.
3. **Units.** CG measures value in "Open Phil dollars" ($OP): the value of giving $1 to someone
   earning $50,000/year in the US. One DALY averted = $OP 100,000. The output is social return on
   investment (SROI): expected $OP per dollar of all-in cost. Higher is better. This is not
   "multiples of cash" or "cost per DALY".
4. **Bar and materiality.** CG's Global Health and Wellbeing bar is about 2,000x; the published
   estimate is about 3,000x. A finding is decision-relevant if it could move SROI below ~2,000x or
   change it by more than about 25% in either direction. Findings that RAISE the estimate count:
   the goal is an accurate estimate, not only reasons the grant looks worse.
5. **Grant type.** This is an R&D grant (a Phase IIc clinical trial). Value comes from bringing
   forward the adoption of a treatment. "Implementation" covers trial execution, the path to
   guideline adoption, and real-world uptake.

---

# Coefficient Giving BOTEC: Trialing statins for treating tuberculosis

Source: Coefficient Giving (then Open Philanthropy), "How we use back-of-the-envelope calculations in our grantmaking", May 2025, sample BOTEC 1. Text below is a close paraphrase captured by web fetch; all numbers are as published.

## Units and bar
- Unit of value: the "Open Phil dollar" ($OP), the value of giving $1 to someone earning $50,000/year in the US. Income gains are valued with log utility.
- One DALY averted = $OP 100,000.
- Global Health and Wellbeing funding bar: about 2,000x, i.e. each dollar granted should create value equal to giving about $2,000 to a $50,000/year US earner.
- Social return on investment (SROI) = expected $OP of benefit per dollar of all-in cost.

## Context
Global health R&D grant. A recent Phase IIa/b trial suggested atorvastatin (a generic, cheap cholesterol drug) could speed clearance of TB infection and reduce lung damage on chest X-ray. The grant funds a Phase IIc trial testing dosing strategies for survival, infection clearance and lung damage, plus work on a sweat-based TB diagnostic. TB kills more than a million people a year.

## Benefits
1. People who could benefit: start from current new TB cases and assume
   - new cases fall 2% per year until a Phase III trial finishes, assumed 8 years after the grant;
   - the share of cases being treated stays constant;
   - 96% of cases are drug-susceptible.
   Result: about 5.5 million people (per year, at the time of adoption).
2. Speedup: the grant accelerates atorvastatin adoption by 1 year.
3. Effectiveness: mortality among treated drug-susceptible patients is about 6%. A positive result is assumed to cut that by 10% relative, i.e. 0.6 percentage points absolute.
4. Uptake: 60% of adult patients would add atorvastatin if it works (generic and cheap). 60% of 5.5 million = about 3.3 million people.
5. Lives saved: 0.6 percentage points x 3.3 million = about 19,900 TB deaths prevented per year once scaled up.
6. DALYs: 19,900 deaths x 27 DALYs per TB death (remaining healthy life expectancy) = about 539,500 DALYs.
7. Value: 539,500 DALYs x $OP 100,000 = $OP 54 billion.
Total benefit: $OP 54 billion.

## Costs
- The current trial costs $320,000.
- Including later Phase III trials, guideline changes, dissemination and validation, all-in costs are about $7 million.
- Open Phil's share is about 4.5% of all-in costs, so it credits itself with about 4.5% of benefits (SROI is therefore computed on all-in costs and all-in benefits).

## Probability of success
40% that Phase II and Phase III trials both succeed.

## Bottom line
SROI = ($OP 54 billion / $7 million) x 40% = about 3,000x, above the ~2,000x bar.
