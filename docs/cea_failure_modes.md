# Cost-Effectiveness Analysis Failure Modes — Reference

Source: Saulius Šimčikas, "List of ways in which cost-effectiveness estimates can be misleading," EA Forum, Aug 2019, plus selected comment additions. Intended as a checklist/retrieval source for red-teaming agents critiquing charity CEAs.

Each entry: **name** — definition — *detection heuristic* — example — citation.

---

## A. Cost-side failure modes

**A1. Leverage / perspective omission** — CEA excludes costs borne by parties other than the charity (governments, patients, partner NGOs). *Heuristic:* Check whose costs are in the denominator. Are downstream distribution, patient travel, or government co-funding excluded? Is the perspective stated? *Example:* A vaccine-purchase CEA that ignores the government's distribution cost. *Cite:* Byford & Raftery 1998; Karnofsky 2011; Snowden 2018.

**A2. Fixed/setup cost handling** — Past sunk costs included or excluded inconsistently; not annualized. *Heuristic:* Are R&D, charity-founding, or infrastructure costs amortized? Is the same convention used across compared charities? *Example:* Excluding setup costs when comparing a mature charity to a hypothetical new one in another country. *Cite:* Shrime checklist (Harvard).

**A3. Future cost omission** — Ongoing costs of monitoring, compliance enforcement, follow-up not modeled. *Heuristic:* For commitment-based or campaign interventions, is enforcement budgeted? *Example:* Corporate cage-free campaign CEAs that price the win but not multi-year compliance monitoring.

**A4. Past cost omission / temporal mismatch** — Costs and effects assigned to different periods, inflating one year. *Heuristic:* Year-by-year cost and impact alignment. *Example:* Homelessness charity builds housing year 1, places residents year 2; year 2 looks impossibly cost-effective.

**A5. Inflation / time-value not adjusted** — Multi-year costs or benefits not discounted or inflation-adjusted. *Heuristic:* Look for a stated discount rate and base year.

**A6. Overhead exclusion** — Operations, fundraising, admin, training excluded from "program cost." *Heuristic:* Compare program-only vs. fully-loaded ratio. *Cite:* Standard practice critique; see GiveWell methodology.

**A7. Costs that didn't pay off ignored** — Only successful units counted. *Heuristic:* Is the denominator "cost per *attempted* unit" or "cost per *successful* outcome"? *Example:* "$10 saves a life" framing of bednets, where most nets don't avert a death; AMF's actual cost per life saved is closer to $3,500–5,500. *Cite:* Wiblin 2017 (80,000 Hours); Sauber 2008.

**A8. Volunteer time not costed** — Labor donated in-kind treated as free. *Heuristic:* Charity volunteer-heavy? If so, shadow-price volunteer hours. *Example:* A small-budget volunteer org showing implausible cost-effectiveness because only snack budget is in the denominator.

**A9. Counterfactual labor cost (altruistic employee opportunity cost)** — Hires displace other altruistic work. *Heuristic:* Are key hires drawn from earning-to-give or other high-impact orgs? *Example:* A charity hiring a top EA researcher off a more important project.

**A10. Fundraising counterfactual / donor-pool effects** — Cost-effectiveness ignores whether the marginal dollar comes from effective or ineffective sources. *Heuristic:* Where does the funding come from — would it otherwise reach effective causes?

**A11. Evaluation overhead** — Cost of getting funded (grant writing, donor evaluation time) excluded. *Heuristic:* For small projects, is evaluation cost > project cost?

---

## B. Effectiveness-side failure modes

**B1. Indirect / flow-through effects ignored** — Second-order impacts (economic, ecological, demographic, long-term) treated as zero. *Heuristic:* Is "we don't model X" stated or just silently assumed? *Example:* Used-clothing donations damaging local textile industries. *Cite:* Hurford 2016.

**B2. Value of information ignored** — Learning value from running the intervention not credited. *Heuristic:* Pilot or novel intervention? VoI should appear. *Cite:* Wilson 2015.

**B3. Limited scope of beneficiaries** — Only directly-targeted individuals counted; family/community/animal spillovers excluded.

**B4. Goodharting / metric over-optimization** — Charity optimizes the proxy, not the goal. *Heuristic:* Could the metric be gamed without real impact? *Example:* Homelessness charity that bus-tickets people out of its measurement area. *Cite:* Goodhart's law (Halffull comment).

**B5. Counterfactual impact of beneficiaries** — Recipients would have obtained the good anyway (paid for it, or another charity would have). *Heuristic:* What's the recipient's next-best option? *Example:* Free medicine going to people who would have purchased it; the real impact is the cash they saved.

**B6. Charity-displacement counterfactual** — Another funder/org would have filled the gap. *Heuristic:* Is the funding gap real and unique?

**B7. Expected value vs. effectiveness conflation** — Probabilistic outcome (50% × 10 lives) presented as if deterministic (5 lives). *Heuristic:* Does the CEA distinguish point estimate from EV? *Example:* "Donate $7,000 to AMF and save 2 lives" framing.

**B8. Average vs. marginal cost-effectiveness** — Total budget divided by total impact, applied to next dollar. *Heuristic:* Is room-for-more-funding modeled separately? *Example:* A medicine charity that has already worked the highest-prevalence regions; marginal dollar buys lower-prevalence work.

**B9. Talent vs. funding constraint mismatch** — Marginal dollar can't be deployed because the bottleneck is hiring. *Heuristic:* Is the org talent-constrained? Then $/impact is misleading.

**B10. Health equity / fairness ignored** — All gains weighted equally; no priority for the worst off. *Cite:* Nord 2005; Cookson et al. 2017; Kamm 2015.

**B11. Means-blind consequentialism** — Tactics (deception, coercion) that boost effectiveness aren't priced morally.

**B12. Hidden moral weights** — Subjective tradeoffs between outcome types presented as parameters. *Heuristic:* Are weights like "under-5 death = 47× consumption doubling" exposed and varied in sensitivity analysis? *Cite:* GiveWell 2017 moral weights doc.

**B13. DALY/QALY blind spots** — No credit for happiness above baseline; severity weights set by general public, not patients; length/quality tradeoffs obscured. *Cite:* Dolan & Kahneman 2008; Pyne et al. 2009; Karimi et al. 2017; Farquhar & Cotton-Barratt 2015.

---

## C. Meta / analytical failure modes

**C1. Non-generalizability** — Result transported across contexts without adjustment. *Heuristic:* Is the CEA reusing effect sizes from a different country, era, or population? *Cite:* Vivalt 2019.

**C2. Atypical-period extrapolation** — Effectiveness measured during an unusual window (epidemic, pilot enthusiasm). *Heuristic:* Is the study period representative? *Example:* Deworming effect sizes from an atypical baseline disease prevalence.

**C3. Regression to the mean** — Standout past performance assumed to persist. *Heuristic:* Is the input estimate a clear outlier?

**C4. Creator bias** — Charities, researchers, or advocates have stake in a positive result. *Heuristic:* Who built the model? Whose data feeds it? Independent replication?

**C5. Publication bias** — Effective-looking interventions over-represented in the literature.

**C6. Bias toward measurable results** — Hard-to-measure interventions appear worse or are absent. *Heuristic:* Is the comparison set restricted to quantifiable interventions only?

**C7. Justification bias** — Politically contested values omitted to keep the analysis defensible. *Cite:* Davidmanheim comment (USACE example).

**C8. Optimizer's curse** — Top-ranked intervention is disproportionately likely to be the most overestimated one. *Heuristic:* How wide are confidence intervals on the winner vs. runners-up? Prefer robust > flashy. *Cite:* Karnofsky 2016.

**C9. Sensitivity to single parameters** — Result load-bearing on one or two uncertain inputs. *Heuristic:* Run one-at-a-time *and* probabilistic sensitivity analysis. Which inputs drive >80% of variance? *Cite:* Claxton 2008; Briggs et al. 2012 (Derek comment).

**C10. Deterministic vs. probabilistic analysis** — Point estimates ignore parameter interactions. *Heuristic:* Is the model Monte Carlo or single-point? *Cite:* Briggs et al. 2012.

**C11. Time discounting unstated** — Whether future costs/benefits are discounted, and at what rate, not specified.

**C12. Model uncertainty / structural misspecification** — Single model treated as ground truth. *Heuristic:* Compare against an alternative model structure.

**C13. Wrong factual assumptions** — Embedded assumptions (compliance rates, usage, take-up) untested. *Example:* Assuming 100% bednet use after distribution.

**C14. Calculation errors** — Arithmetic, unit, or upstream-study errors. *Cite:* Hurford & Davis 2018.

**C15. Missing diversification value** — Optimization for top BCR underweights portfolio robustness and correlated failure. *Cite:* Davidmanheim comment.

**C16. Feedback loops / complex systems ignored** — One-way causal chains modeled where dynamics are reciprocal. *Cite:* Halffull comment.

**C17. Threshold-based metrics** — Outcomes counted only across an arbitrary line (e.g., $1.90/day). *Heuristic:* Does the metric reward moving people just over a cutoff? *Cite:* bfinn comment.

---

## D. Donation-impact complications

**D1. Fungibility** — Restricted donations free unrestricted funds for other uses; the marginal program may not be the one named.

**D2. Donor replaceability** — Another donor would have filled this gap. *Heuristic:* Use Shapley-style credit assignment rather than pure counterfactual when multiple actors contribute. *Cite:* NunoSempere comment; Benjamin Todd comment.

**D3. Double / under counting across cooperating orgs** — Multiple orgs each claim 100% credit, or each claim 0%. *Cite:* weeatquince and Benjamin Todd comments.

**D4. Donation matching as pure leverage** — Match funds often would have been donated regardless. *Heuristic:* Is the match contingent and additional, or pre-committed?

**D5. Influence on other donors** — Grants signal legitimacy; ignored in direct CEA.

**D6. Influence on charity behavior** — Funding source shapes which programs the charity pursues and which metrics it optimizes; related to Goodhart (B4).

**D7. Cooperative-strategy penalty** — A charity taking the globally best action may look worse on its own CEA than one taking a locally optimal action. *Cite:* abrahamrowe comment (animal welfare campaign coordination).

**D8. Giving-now vs. later** — Investment returns and changing opportunity costs not modeled. *Cite:* Wise 2013.

**D9. Tax deductibility** — Effective subsidy from government changes true cost to donor.

**D10. Cost-attribution inconsistency for opportunity costs** — Lost earning-to-give or alternative-use costs sometimes counted as costs, sometimes as negative impact, never both consistently. *Cite:* Michael St Jules comment.

---

## Notes on use in the pipeline

- The four-bucket structure (A/B/C/D) maps reasonably onto agent specialization: cost auditor, effect auditor, methods/meta auditor, donation-context auditor.
- Items with explicit detection heuristics (A1, A7, B7, B8, B12, C8, C9, C10) are the most mechanically checkable against GiveWell-style spreadsheet CEAs and should be prioritized for first integration.
- Items C8 (optimizer's curse) and C9 (sensitivity) are the highest-leverage meta-checks for any ranking output the pipeline produces about its own findings.
