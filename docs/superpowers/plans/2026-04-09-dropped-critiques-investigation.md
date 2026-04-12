# Investigate Where Dropped Critiques Go in the Pipeline

> **For Claude Code:** Read-only investigation, no fixes. Report findings, do not propose solutions. No API access required.

## Background

The VAS pipeline run generated 32 candidate critiques but only 28 made it to the synthesizer. The 4 dropped critiques are:

1. Accelerating Benefits from Immunological Priming Effects
2. Seasonal and Campaign-Timing Cost Variations Not Reflected
3. Short-Term Protection Window Creating Mortality Displacement
4. Threshold Effects for Herd Protection in High-Mortality Settings

These appear in `results/vas/02-investigators.json` but NOT in `results/vas/03-verifier.json`. We need to know *where* they disappeared and *why*. There are three hypotheses:

- **H1: Parser failure.** The titles appear in `results/vas/03-verifier.md` (raw API responses) but the regex parser didn't extract them. Same class of bug as the duplicate parser issue we just fixed.
- **H2: API response failure.** The titles were sent to the verifier as batch inputs, but the model's response didn't include them. Either silently dropped from the response or response was truncated.
- **H3: Upstream batching.** The titles never made it into a verifier batch at all. Some filter or off-by-one in `run_verifier` skipped them before any API call.

A second, related question: the synthesizer report's "Ungrounded Hypotheses Worth Investigating" section contains 3 entries (Frailty Selection Effects, Survivor Bias in Benefits, Household Clustering of Deaths) — none of which match the 4 dropped critiques. We need to know whether this is VAS-specific or systematic across all runs.

## Investigation tasks

### Task A: Locate the 4 VAS drops in the pipeline

For each of the 4 dropped critique titles:

1. **Confirm presence in `results/vas/02-investigators.json`.** They should all be there. If any are missing, the bug is even further upstream than expected — stop and report.

2. **Search `results/vas/03-verifier.md` (the raw API response file) for each title.** Use both exact and fuzzy match — the model may have abbreviated, paraphrased, or restated titles slightly differently.

3. **Inspect the batching logic in `pipeline/agents.py`'s `run_verifier`.** With `VERIFIER_BATCH_SIZE = 3` and 32 critiques, there should be 11 batches (the last batch having 2 critiques). Trace which batch each of the 4 dropped critiques belonged to. Are all 4 drops from the same batch, adjacent batches, or scattered?

4. **For each drop, classify into H1/H2/H3:**
   - **H1 if:** title appears in `03-verifier.md` but the parser didn't extract it (visible in raw, missing from `03-verifier.json`)
   - **H2 if:** title does NOT appear in `03-verifier.md` at all, but the surrounding batch context suggests it was sent to the API (other critiques from the same batch are present in the raw)
   - **H3 if:** title doesn't appear in `03-verifier.md` AND there's no evidence the batch containing it was ever sent (no surrounding batch context for that critique)

### Task B: Cross-run audit of the "Ungrounded Hypotheses" section

For each of the four runs (`water-chlorination`, `itns`, `smc`, `vas`):

1. Read the `06-synthesizer.md` report and extract the entries listed in the "Ungrounded Hypotheses Worth Investigating" section.
2. Compute the actually-dropped critiques: titles in `02-investigators.json` minus titles in `05-adversarial.json` (use `entry["critique"]["critique"]["original"]["title"]` for the adversarial path, as confirmed in the dedup work yesterday).
3. For each run, report:
   - Number of actually-dropped critiques
   - Number of "Ungrounded Hypotheses" entries in the synthesizer report
   - Overlap between the two sets (exact title match — fuzzy is too lenient for this question)

This tells us whether the synthesizer is hallucinating ungrounded hypotheses across all runs or just VAS.

## Report format

```
=== TASK A: VAS DROP LOCATIONS ===

Drop 1: Accelerating Benefits from Immunological Priming Effects
  In investigators: yes/no
  In verifier raw .md: yes/no (with line number if yes, or "not found" if no)
  Batch number: N (positions M-M+2 in candidate list)
  Other critiques in same batch: [titles]
  Other critiques in same batch present in raw: [titles]
  Classification: H1 / H2 / H3
  Notes: [anything notable about how the title appears or doesn't]

Drop 2: ... (same format)
Drop 3: ...
Drop 4: ...

Cross-drop pattern: [Are all 4 in the same batch? Adjacent batches?
                     Scattered across run? Same thread? Same investigator?]

=== TASK B: UNGROUNDED HYPOTHESES AUDIT ===

water-chlorination:
  Actually dropped: N critiques
  Synthesizer "ungrounded" entries: M
  Exact title overlap: K
  Dropped titles: [list]
  Synthesizer "ungrounded" titles: [list]

itns: ... (same format)
smc: ...
vas: ...

Cross-run pattern: [Is the synthesizer hallucinating across all runs,
                    just VAS, or some other pattern?]

=== HYPOTHESIS VERDICT ===

H1 (parser failure): supported / refuted / mixed
H2 (API response failure): supported / refuted / mixed
H3 (upstream batching): supported / refuted / mixed

If multiple hypotheses are supported across the 4 drops, indicate which
drop fits which hypothesis.
```

## Stop conditions

- Any of the 4 dropped titles is missing from `02-investigators.json` (means the drop happened even further upstream)
- The drops appear in `03-verifier.md` AND `03-verifier.json` (would mean the dedup script missed them, or the original analysis was wrong)
- The batching logic is more complex than `chunked(critiques, 3)` (means the trace requires actually running the code, not reading it)
- More than 5 minutes spent fuzzy-matching titles in the raw .md file — at that point report what you found and let Tsondo decide whether to keep digging

## Don't

- Propose a fix
- Modify any files
- Re-run any pipeline stages
- Activate the API key
- Generalize beyond the 4 VAS drops and the 4 cross-run audits
