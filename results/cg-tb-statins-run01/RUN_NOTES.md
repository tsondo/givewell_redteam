# cg-tb-statins run #01 (2026-11-07) — archived

Run with commit 869c6ba on claude-opus-5-5 / claude-sonnet-5-5. Cost $2.02.

**Not a fair test of the pipeline's reasoning.** Known defects, fixed after this run:

- 14 of 22 calls hit max_tokens (caps were sized for Claude 4; 5.5 models always
  think and thinking counts against max_tokens). Truncation was silent.
- Decomposer: thread 3 ("(Structural/Methodological)" in its header) was dropped by
  the thread regex, and "WHAT CG ALREADY / DOES NOT ACCOUNT FOR" sections were empty
  in the investigators' context because the parser expected "WHAT GIVEWELL ...".
- Quantifier: 0 of 4 critiques reached executed sensitivity analysis (prose range
  format, markdown markers, leading text dropped by the block splitter).

Blind score against CG's held-out follow-ups: 1 caught (later-trial costs),
1 partial (p_success), 6 missed. Three of the misses (speedup, horizon, competing
treatments) were raised in the dropped decomposer thread.
