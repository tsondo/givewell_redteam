# Engagement Playbook

How we go from "interesting org" to "delivered red-team analysis they actually use." Modeled on the GiveWell run. Iterate this doc after every engagement.

## Principles

These override anything below if they conflict.

1. **Demonstrate before pitching.** Never email an org until we have a real artifact to put in front of them. A drafted critique beats a hundred "I could help you" emails.
2. **Make haste slowly.** Each phase informs the next. Resist the urge to broaden until the current case is deep and has genuine, verified results.
3. **Architectural critique, not model critique.** We frame findings as structural patterns in their methodology, not errors in their work. This lands better and is more defensible.
4. **Organizational benefit before self-promotion.** Every external communication leads with what they get, not what we want.
5. **Parallel engagement should be diplomatic.** Be aware of and avoid the appearance of "shopping around." Ok to engage with new orgs during "waiting phases" or between runs.

## Phase 0 — Candidate Discovery

**Goal:** Maintain a ranked backlog of orgs we could realistically help. Refresh quarterly or whenever the current engagement is at a natural wait point or complete.

**Criteria for an org to make the backlog:**
- Publishes cost-effectiveness analyses or structured impact models as public artifacts (spreadsheets preferred, PDFs acceptable, narrative-only is hardest)
- Methodology is self-documented (we need to know what their CEAs are *trying* to do before we can critique how they do it)
- Small enough that one substantive memo reaches the right desk, or large enough that they have a dedicated methodology team
- Either explicitly asks for outside scrutiny, or has a public track record of engaging with critique
- Mission-aligned with EA-adjacent global-health/welfare work (for now — broaden only after the case base supports it)

**What goes in the backlog entry:**
- Org name, primary contact (if known), source of the lead
- Artifact format (xlsx, Google Sheets, Guesstimate, PDF, mixed)
- Estimated number of public CEAs / reports
- Open methodology questions they have publicly acknowledged (these are gold — they pre-validate the value of the work)
- Strategic notes on cultural/relationship considerations
- Tier: 1 (direct fit), 2 (public models but harder), 3 (adjacent, only if we run out of 1 and 2 or find a compelling case to expand)

**Current backlog** (as of the GiveWell engagement):
1. **GiveWell** — IN PROGRESS
2. **Charity Entrepreneurship / AIM** — NEXT
3. **Animal Charity Evaluators** — Tier 1, after CE
4. **Founders Pledge** — Tier 1, lower priority
5. **Happier Lives Institute** — Tier 2, methodologically novel
6. **Open Philanthropy** — Tier 2, harder targeting
7. **Center for Global Development** — Tier 3, more academic than charity-evaluator

**Anti-criteria — do not pursue:**
- Orgs whose models are entirely internal
- Orgs whose public CEAs are marketing artifacts rather than decision tools
- Any org where we'd be a competitor rather than a collaborator
- Orgs we have no plausible warm path into and no compelling cold-pitch angle

## Phase 1 — Reconnaissance

**Goal:** Understand the org's methodology well enough to know whether the pipeline can give them value, and what shape the deliverable should take. **Do not run the pipeline yet.**

**Outputs of this phase:**
- A short memo (1-2 pages, internal only) covering the items below
- A go/no-go decision on advancing to Phase 2
- An inventory file listing every public artifact we found, with URLs and format

**What to gather:**
1. **Methodology documents.** How does this org build CEAs? What software? What units? What review process? Read these *before* looking at any individual CEA.
2. **Public artifact inventory.** Every CEA, report, model we can access. Note format, year, intervention, depth. This is the equivalent of the spreadsheet inspection step before a pipeline run — it tells us what we're working with before we commit code.
3. **Open questions they have publicly acknowledged.** EA Forum posts, blog posts, their own methodology docs. Anything where they say "we know this is a weakness" or "we'd welcome scrutiny on X." These are pre-validated value propositions.
4. **Recent external critiques of their work.** Who has already red-teamed them? What did the org's response look like? This tells us both what's been said and how the org receives criticism.
5. **Cultural read.** Are they methodologically self-aware? Do they engage substantively with critique or get defensive? Small-team scrappy or large-org formal?
6. **Warm path, if any.** Mutual contacts, EA Forum interactions, conference overlap.

**Go/no-go gate questions:**
- Can we name a specific deliverable that addresses a specific question this org has?
- Is the artifact format something the pipeline can consume with reasonable adapter work (less than ~3 days of engineering)?
- Is there a plausible path to the right person seeing the work?

If any answer is no, stop and either re-scope or move to the next backlog entry.

## Phase 2 — Project Selection

**Goal:** Pick *one* deliverable at a time. Build carefully. Let each step inform the next.

**Deliverable types, ranked by leverage (best first):**

1. **Cross-artifact meta-analysis.** Run the pipeline on N artifacts from the same org and surface structural patterns that recur across them. This is our signature strength — the chlorination/ITN/SMC runs proved it. Highest value because the findings affect every future CEA the org produces, not just the ones we ran.
2. **Targeted methodology audit answering an open question they've acknowledged.** Narrower scope, faster to produce, and lands directly on a question they've already said they care about. Best *first* deliverable for a new org, because it's defensible and doesn't require them to trust us before they've seen results.
3. **Single high-stakes CEA red team.** Run the pipeline on one current, important model. Useful as a demo, lower leverage than the first two because it only affects one decision.
4. **Bayesian optimization or sensitivity extension** on an existing model. Higher engineering cost, only worth doing after we've established credibility with the org through a smaller deliverable first. This is the path the GiveWell ITN work took.

**Heuristics for picking among them:**
- For a *new* org we have no relationship with: lead with #2. Tight scope, clear question, defensible scale.
- For an org where we have a foot in the door: #1 is the bigger swing.
- #3 is the right call only when there's a specific decision in the air that the deliverable could affect.
- #4 is a *second* engagement, unless specifically asked for by the org.

**Scope discipline:**
- Time-box Phase 3 to a budget of API spend and calendar days *before* starting it. The GiveWell runs came in around $16-30 each after the verifier batching optimization — use that as the baseline.
- Resist scope creep. If the analysis suggests a bigger story, note it for a follow-up engagement, don't expand the current one.

## Phase 3 — Execution

**Goal:** Produce the deliverable. This is where the existing pipeline runs.

**Pre-flight checklist** (do every time):
- [ ] Spreadsheet inspection complete on every artifact in scope. Layout, named ranges, DUMMYFUNCTION placeholders, anything that breaks programmatic access.
- [ ] Format adapters built and tested if the artifact isn't native xlsx. (Google Sheets: export to xlsx. Guesstimate: build a small adapter. PDF-only: this is a different pipeline shape. Allow extra time and check carefully.)
- [ ] API key activated (kept deactivated as default safety practice).
- [ ] Verifier batching enabled. This optimization cut per-critique cost ~70% in Phase 2 and should be applied to every run.
- [ ] Budget cap set in the orchestrator. Logged token usage per stage.
- [ ] Output directory under `results/{org}/{intervention}/` with both JSON (pipeline) and markdown (human) outputs at every stage.
- [ ] Plan for what the deliverable looks like *before* running the pipeline. Knowing the target shape makes the synthesis stage faster and avoids scope creep.

**What to produce:**
- The pipeline outputs (intermediate stages, for our records)
- A synthesis memo (the actual deliverable for the org) — paraphrased, tightly organized, leading with the findings that have the highest signal
- A methods appendix (so the org can verify our process)
- An honest cost and time accounting (this is part of the credibility story)

**Quality bar before sharing:**
- Every claim in the synthesis is traceable to a verified pipeline output
- No claim depends on a single agent's unverified assertion
- Findings are framed as structural patterns, not errors
- The memo would survive being read by a hostile reviewer in their methodology team

## Phase 4 — Approach

**Goal:** Get the deliverable in front of the right person, in a way that feels like help and not a sales pitch.

**Pre-approach checks:**
- Is the current engagement (if any) closed or stable enough that a new approach won't look like double-dipping?
- Do we have a warm path? If yes, use it. If no, is the cold-pitch angle compelling enough to land without one?
- Have we drafted the email and considered tone? First drafts may be too eager.

**The approach itself:**
- Lead with the deliverable, not the offer. The memo is the artifact. The email is just a cover letter.
- One ask, not three. "I am open short call to walk through this" or "would this be useful to your team — happy to share more if so." Ideally let them ask.
- Tone: deliberately non-pressuring. We're sharing work we did because we think it might be useful. We're not asking them to do anything except read it.
- No tier menus on first contact. Tiered engagement options (informal advisory / consulting / formal role) are for *follow-up* conversations after they've already engaged with the work.
- Sign as "Todd aka Tsondo" for professional correspondence.

**What to expect:**
- Most cold approaches go nowhere. Plan for a multi-week response window. Don't follow up more than once.
- A warm response often takes the form of a question, not a yes. Treat questions as engagement, not as objections.
- An invitation to discuss is the success state of this phase. Don't try to close anything bigger on first contact. The actual goal is to be helpful.

## Phase 5 — Engagement & Iteration

**Goal:** Actual improvment of charity efforts and cost effectiveness. Interest into a real working relationship, and learn enough to improve this playbook if and only if the help is real and appreciated.

**During the engagement:**
- Default to giving more value than asked. Cheap to do, builds trust faster than anything else.
- Ask what they'd find most useful next. Don't assume the second deliverable is the same shape as the first.
- Share code and methods, not just findings. Orgs that can reproduce our work trust it more.
- Watch for opportunities to make the relationship recurring: standing meetings, embedded work in their workflow, code in their stack.

**After the engagement (or every 90 days, whichever comes first):**
- **Retrospective.** What worked? What didn't? What would we do differently? Update this playbook.
- **Backlog review.** Does the engagement change the priority order of remaining backlog candidates?
- **Capability gaps.** Did this engagement reveal something the pipeline can't do yet that we should build?
- **Capacity check.** Are we ready to start another engagement, or does the current one need more depth first?

## Open process questions

Things we don't know yet, to revisit as we accumulate evidence:

- What's the right cadence for new engagements? Be flexible based on expressed interest and usefulness.
- At what point does parallel work across multiple orgs become tractable vs. confusing? Don't take on more than we can handle.
- When does it make sense to publish methodology results as a standalone paper vs. keeping them as private deliverables?
- What does the right relationship structure look like for orgs that want recurring red-teaming — contractor, fiscal-sponsored project, something else? Help them find the best fit for them.
- When does the pattern library across organizations become more valuable than any individual engagement, and how do we package it then?

## Changelog

- **2026-04-08** — Initial version, drafted from the GiveWell engagement and the planned Charity Entrepreneurship next step.
