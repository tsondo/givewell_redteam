# GiveWell AI Red Team — Status as of 11 April 2026

## Where we are

Plan 3 (VAS re-run) executed cleanly yesterday. All artifacts committed to main. Total cost $6.36, well under budget. Verification report completed. Mikyo has reviewed the new artifacts and responded with architectural feedback. Grok provided an independent pre/post comparative evaluation validating the architectural shift.

The pipeline is now in its stablest, most credible state to date.

## Immediate next steps (in order)

1. **Conclusions doc update.** Blocking item for the Brendan conversation. Incorporates the corrected metrics (actual pre-judge was 17/11, not 28/28), the judge audit data (156 failure modes, 0 sound syntheses), Mikyo's architectural feedback integration, and Grok's independent validation of the directional arguments. Honestly describes what each stage does (including the known limitation of the adversarial stage's "moderate" verdict bucket collapse).

2. **Label rubric explainer in the synthesizer.** Small prompt update. Adds a brief "What strong/moderate/weak mean" section at the top of the synthesis report so readers understand the rubric before encountering the findings. Committed to Mikyo.

3. **Brendan writeup.** After conclusions doc is solid. Uses the writing lessons from the blog post and social media posts — grounded in demonstrated results, not projections.

4. **Send to Brendan.** Manual step. Timing at your discretion.

## Near-term parallel work

**Two-column debate HTML renderer.** New repo. Starts today (scaffolding only, scope-bounded). First deliverable: static HTML renderer that takes existing `05-adversarial.json` and produces Mikyo's requested side-by-side point-by-point defense/rebuttal view. Committed to Mikyo as "soon."

Boundary: if scaffolding expands past a few hours, stop and return to the conclusions doc.

## Longer-term (deferred, no timeline)

**DAG of logical dependencies.** Biggest architectural improvement Mikyo has proposed. Extends verifier's claim tracking, adds provenance to each debate argument, builds graph layer. Would show which conclusions weaken if individual facts are withdrawn — "single point of failure" visibility. Multi-plan project. Committed to Mikyo as real future work, not immediate.

**Multi-round referee.** Judge flags weakness, debater gets a chance to strengthen, judge re-audits. Architecturally interesting. Cost triples per round. Parked for v2. Also worth investigating whether local models are now strong enough to make this cost-neutral.

**Taxonomy refinement.** Waiting on Mikyo's response re: three to five fallacy additions (or consolidation suggestions on the three `unsupported_estimate_*` variants). Low-friction next iteration once he replies.

## Remaining interventions (open)

CMAM (malnutrition), syphilis screening, malaria vaccines — the three GiveWell interventions not yet run. Order of operations for these is post-Brendan. Whether to run them depends on GiveWell's response.

## Open architectural flags from the re-run

- **Synthesizer patterns narrative conflates combined table counts with per-side numbers.** Small synthesizer prompt fix.
- **Empty baseline URL handling for VAS.** Small orchestrator fix (skip fetch when URL is empty).
- **Trailing `**` in critique titles from earlier pipeline stages.** Data hygiene fix needed upstream — would bite any future run where linker produces `depends_on` involving these titles.

None are blocking. All appropriate for a cleanup plan after the Brendan conversation.

## Key principles to preserve

- Make haste slowly. Sequence matters more than speed.
- Reliability over speed.
- Ground claims in demonstrated results, not projections.
- Human-in-the-loop, AI as collaborator. Interpretability is a trust prerequisite.
- External validation from domain experts (Mikyo) > internal self-assessment > LLM self-review (Grok as supplement only).

Rest well. The work is in good shape.
