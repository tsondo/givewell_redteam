# Second Amendment: Add explicit timeout to synthesizer API call

> Amendment to the prior token limit amendment. The Anthropic SDK has a client-side check that requires streaming for requests where max_tokens × model-speed could exceed 10 minutes. The 12288 limit trips this check on Opus. The fix is to pass an explicit timeout to the API call, signaling "I accept the long-running request" — the actual call finishes in 1-2 minutes in practice. This project commits directly to main; do not create branches.

## Context

The SDK threshold is conservative and treats ceiling values, not expected ones. Passing an explicit timeout is the intended escape hatch when you want a max_tokens value the SDK considers potentially slow. This is a one-line addition at the synthesizer call site in `pipeline/agents.py`, not a rewrite.

Scope discipline: only the synthesizer call site gets the timeout. Do not add timeouts to other API calls. Other stages (decomposer, quantifier, judge) may trip the same threshold in the future — those will be addressed individually if needed.

## File Map

| Action | File | Change |
|--------|------|------|
| Modify | `pipeline/agents.py` | Add `timeout=httpx.Timeout(600.0)` to the synthesizer's `messages.create()` call |
| Re-run | `results/vas/06-synthesizer.{json,md}` | Regenerated complete artifact |

---

## Task 6: Add explicit timeout to synthesizer call

**Files:**
- Modify: `pipeline/agents.py`

- [ ] **Step 1: Locate the synthesizer API call**

Find the `messages.create()` invocation in `run_synthesizer` (or whatever helper it uses — possibly `call_api` with a synthesizer stage tag).

- [ ] **Step 2: Determine if `httpx` is already imported**

Check the file's imports. If `import httpx` is not present, add it at the top with the other imports. Alphabetical order, standard placement.

- [ ] **Step 3: Add the timeout parameter**

Add `timeout=httpx.Timeout(600.0)` as a parameter to the `messages.create()` call. 600 seconds = 10 minutes, matching what the SDK would have enforced with streaming. The actual call completes in 1-2 minutes in practice; this is a ceiling, not an expectation.

**Critical:** only modify the synthesizer's call. Do NOT add timeouts to advocate, challenger, judge, decomposer, quantifier, verifier, or linker calls. Each stage has different max_tokens values and the SDK threshold behavior should be handled per-stage if and when each hits the threshold.

If the synthesizer uses a shared `call_api` helper that other stages also use, the cleanest move is to add an optional `timeout` parameter to that helper (default None) and pass the 600-second value only from the synthesizer call site. Do not make the timeout mandatory or default-on for other stages.

- [ ] **Step 4: Run existing tests**

Run the full test suite. If any test fails, **stop and report**. If tests assert on the synthesizer call's exact arguments (mocked call verification), they'll need updating — include the timeout in the expected arguments.

- [ ] **Step 5: Commit the code change**

```
fix: add explicit timeout to synthesizer API call for higher max_tokens

The Anthropic SDK enforces a client-side check that requires streaming
when max_tokens × model-speed could exceed 10 minutes. Raising
MAX_TOKENS_SYNTHESIZER from 8192 to 12288 tripped this check on Opus.

Passing an explicit timeout (600 seconds, matching the SDK's streaming
threshold) is the intended escape hatch. Actual synthesizer calls
complete in 1-2 minutes; the timeout is a ceiling, not an expectation.

Scope: only the synthesizer call site. Other stages remain untouched
and will be handled individually if they hit the same threshold.
```

Use Co-Authored-By trailers as standard.

---

## Task 7: Re-run VAS synthesizer and verify full completion

Same as the prior amendment's Task 5. API spend ~$0.50–0.80.

- [ ] **Step 1: Invoke the resume**

```
python -m pipeline.run_pipeline vas --resume-from synthesizer
```

Expected runtime: 1-2 minutes. Expected cost: ~$0.50–0.80. Hard stop: $2 total cost.

- [ ] **Step 2: Verify full completion**

Load the new `results/vas/06-synthesizer.md` and confirm:

**From the original plan (still required):**
1. The "How to Read This Report" section is present and matches verbatim text from the prompt (no paraphrasing)
2. Section appears after "Pipeline Summary" and before "Critical Findings"
3. The Debate Quality Audit's Patterns subsection labels combined vs per-side counts

**Completeness checks (unchanged from prior amendment):**
4. `## Meta-Observations` section is present at the end
5. Resolved Negatives section is complete
6. The raw markdown ends cleanly (no mid-sentence termination)
7. All structural sections accounted for

If output is still truncated, **stop and report** — the problem is beyond token budget.

- [ ] **Step 3: Commit the regenerated artifact**

If all checks pass:

```
data: regenerate VAS synthesizer with rubric explainer and complete output

Re-run after raising MAX_TOKENS_SYNTHESIZER to 12288 and adding an
explicit timeout to the synthesizer API call. Produces complete
document including all sections through Meta-Observations.

Cost: ~$0.XX. Upstream stages 1-5b unchanged.

Pre-rubric backup retained locally as *.pre-rubric.* for comparison.
```

Replace `$0.XX` with the actual cost from `pipeline-stats.json`.

---

## Stop Conditions Requiring Tsondo Input

- The SDK still rejects the call with the explicit timeout (indicates a different underlying issue)
- Existing tests fail after the code change in ways that aren't about the new timeout parameter
- The regenerated output is still truncated at 12288 tokens
- Cost exceeds $2
- Verbatim rubric text appears paraphrased
- Patterns subsection still conflates combined vs per-side

## Things You Should NOT Do

- Add timeouts to any API call other than the synthesizer's
- Make the timeout a default-on parameter that affects other stages
- Refactor `call_api` beyond adding an optional timeout parameter (if shared helper is used)
- Re-run any upstream stages
- Modify the judge prompt or any other prompt
- Commit `*.pre-rubric.*` backups
- Create branches
