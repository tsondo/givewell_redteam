# Manual Workflow: Running the Red Teaming Pipeline in a Claude Project

This document provides step-by-step instructions for running the multi-agent red teaming pipeline using sequential prompts in Claude. No code is required. A human copies outputs between stages.

**Time estimate:** 60–90 minutes per intervention (comparable to GiveWell's current process)

**Prerequisites:**
- A Claude account (Pro or Team)
- GiveWell's intervention report for the target intervention (text or URL)
- The CEA spreadsheet for the target intervention (open in a browser tab for reference)
- The prompt files from the `/prompts/` directory

---

## Setup

1. Start a new Claude Project (or conversation).
2. Upload the intervention report as a document, or paste the URL if it's a public webpage.
3. Have the CEA spreadsheet open in a separate browser tab — you'll reference it during the Quantifier stage.

---

## Stage 1: Decomposer (~10 minutes)

**What to do:**
1. Paste the Decomposer prompt (`prompts/decomposer.md`).
2. Below the prompt, paste or attach the intervention report.
3. Below that, add a CEA summary. You can write this yourself by skimming the spreadsheet's "Start Here" tab and key parameter sheets, OR paste the relevant sections. A good CEA summary includes:
   - What the model calculates (e.g., "units of value per dollar")
   - The major benefit categories (mortality, morbidity, development effects, etc.)
   - Key parameters and their current values
   - The main adjustments applied (internal validity, external validity, etc.)

**What you'll get:**
- 5–8 investigation threads with scoped CONTEXT.md content
- An exclusion list of already-addressed concerns
- A CEA parameter map

**What to save:** Copy the full output to a working document. You'll need the investigation threads for Stage 2 and the exclusion list + parameter map for later stages.

---

## Stage 2: Investigators (~15 minutes, done in parallel or sequence)

**What to do:**
For each investigation thread from Stage 1:

1. Start a new message (in the same conversation or a new one — same conversation preserves context but may hit length limits for later threads).
2. Paste the Investigator template prompt (`prompts/investigator-template.md`).
3. Replace `{{CONTEXT_MD}}` in the template with the specific thread's CONTEXT.md content from the Decomposer output.
4. Include the exclusion list.
5. Include relevant excerpts from the intervention report (only the sections the Decomposer flagged as relevant to this thread).

**What you'll get:**
- 3–6 candidate critiques per thread (15–36 total across all threads)

**What to save:** Collect all candidate critiques into a single document, organized by thread.

**Tip:** If you're running 6+ threads, consider using separate conversations for each to avoid context window limits. Label each conversation with the thread name.

---

## Stage 3: Verifier (~15 minutes)

**What to do:**
1. Start a new conversation (clean context is important here — the Verifier shouldn't be primed by the Investigator's reasoning).
2. Paste the Verifier prompt (`prompts/verifier.md`).
3. Feed critiques one at a time (or in small batches of 2–3). For each, paste the candidate critique and ask the Verifier to check it.

**Important:** The Verifier needs web search access. If using Claude, enable the web search feature. The Verifier's value comes from actually looking things up, not reasoning about whether something sounds true.

**What you'll get:**
- Each critique classified as VERIFIED, PARTIALLY VERIFIED, or UNVERIFIED
- Real citations and evidence for verified critiques
- Honest "not found" reports for unverified ones

**What to save:** Keep the full Verifier output. Discard UNVERIFIED critiques (or keep them in an appendix). Carry VERIFIED and PARTIALLY VERIFIED critiques forward.

---

## Stage 4: Quantifier (~15 minutes)

**What to do:**
This is the stage that differs most between the manual and automated versions. In the manual version:

1. For each verified critique, identify which CEA parameters it affects (the critique should specify this, and the Decomposer's parameter map helps).
2. Open the CEA spreadsheet in Google Sheets.
3. Make a copy (File → Make a copy) so you can edit without changing the original.
4. For each affected parameter:
   - Note the current value
   - Change it to the alternative value suggested by the critique's evidence
   - Record the new bottom-line cost-effectiveness result
   - Reset the parameter and try the next critique

**Alternatively**, if you prefer to have Claude help:
1. Paste the Quantifier prompt (`prompts/quantifier.md`).
2. Provide the verified critiques and describe the relevant CEA parameters (values, cell references, what they represent).
3. Ask Claude to help you determine what parameter changes are implied and what the sensitivity range should be.
4. Then make the actual spreadsheet changes yourself and report back the results.

**What you'll get:**
- For each critique: the change in bottom-line cost-effectiveness when the parameter moves
- Materiality classification: Material (>10%), Notable (1–10%), or Immaterial (<1%)

**What to save:** Record the parameter changes and results for each critique. Discard Immaterial critiques (or keep in appendix).

---

## Stage 5: Adversarial Pair (~10 minutes)

**What to do:**
1. Start a new conversation.
2. For each Material or Notable critique:
   a. Paste the Advocate prompt (`prompts/adversarial-advocate.md`) with the critique.
   b. Record the Advocate's defense.
   c. Then paste the Challenger prompt (`prompts/adversarial-challenger.md`) with both the critique and the Advocate's defense.
   d. Record the Challenger's rebuttal and surviving strength rating.

**Shortcut for time-constrained runs:** You can combine both roles in a single prompt: "First, construct the strongest defense of GiveWell's position. Then, rebut your own defense. Rate the surviving strength." This is less rigorous than separate agents but saves time.

**What you'll get:**
- Each critique stress-tested with a defense, rebuttal, and surviving strength rating
- Key unresolved questions identified

**What to save:** The debate record for each critique, especially the surviving strength rating and recommended action.

---

## Stage 6: Synthesizer (~10 minutes)

**What to do:**
1. Start a new conversation.
2. Paste the Synthesizer prompt (`prompts/synthesizer.md`).
3. Provide all surviving critiques with their full records from every previous stage.
4. If available, also paste GiveWell's published AI output for this intervention (for baseline comparison).

**What you'll get:**
- A ranked final report with executive summary, evidence, quantification, and debate outcomes
- A comparison against GiveWell's baseline (if provided)
- Methodological notes

**What to save:** This is your final deliverable. Save the full Synthesizer output.

---

## Output Checklist

When you're done, you should have:

- [ ] Decomposer output (threads, exclusion list, parameter map)
- [ ] Investigator outputs (candidate critiques, organized by thread)
- [ ] Verifier outputs (verification verdicts for each critique)
- [ ] Quantifier outputs (sensitivity results for verified critiques)
- [ ] Adversarial outputs (debate records for material critiques)
- [ ] Synthesizer output (final ranked report)
- [ ] Comparison scorecard (if baseline available)

---

## Tips

- **Start clean for the Verifier.** Don't run the Verifier in the same conversation as the Investigators. The Verifier should check evidence independently, not be primed by the Investigator's reasoning.
- **The Quantifier stage is where humans add the most value.** You can see the spreadsheet; the AI can't (in the manual version). Use Claude to help think through parameter implications, but make the spreadsheet changes yourself.
- **Don't skip the Adversarial stage.** It's tempting to go straight from quantification to synthesis. The debate stage is what separates critiques that sound good from critiques that ARE good.
- **Time budget:** If you only have 30 minutes, run the Decomposer, pick the 2–3 highest-priority threads, run Investigators for those, and do a quick Verifier pass. Skip the Adversarial stage. You'll still get better results than a single-pass approach.
