# AI Red Teaming of Cost-Effectiveness Analyses: Multi-Agent Pipeline

A multi-agent pipeline that red teams published cost-effectiveness analyses (CEAs) for charitable grantmaking. It started with GiveWell's CEA spreadsheets and now also handles other funders' formats, such as Coefficient Giving's prose back-of-the-envelope calculations (BOTECs). The aim is to show that architecture (decomposition, verification, quantification, adversarial testing) beats single-pass prompting for research critique.

## Origin

GiveWell published a [report on AI red teaming](https://www.givewell.org/how-we-work/our-criteria/cost-effectiveness/ai-red-teaming-12-25) (January 2026) describing an experiment using ChatGPT 5 Pro with structured prompts. About 15 to 30% of the AI critiques were useful, with persistent hallucination, lost context, and unreliable quantitative estimates.

## Thesis

Those limitations come from architecture, not the model. Decomposition, verification, adversarial agent structure, scoped context, and tool-backed quantitative reasoning each improve results, and the improvements compound.

## Results

### GiveWell CEAs

Four interventions, using only public materials. Figures are from each run's latest synthesizer report; signal rate is surviving critiques over generated critiques.

| Intervention | Critiques generated → surviving | Signal rate | Cost |
|---|---|---|---|
| Water chlorination | 31 → 26 | 84% | ~$30 (v1, before verifier batching) |
| Insecticide-treated nets | 30 → 30 | 100% | $16.00 |
| Seasonal malaria chemoprevention (re-run with v2 parsers) | 28 → 19 | 68% | $15.27 |
| Vitamin A supplementation (re-run) | 32 → 28 | 88% | $6.36 |

GiveWell's single-pass baseline: about 15 to 30% useful. No hallucinated citations reached the final reports: separating hypothesis generation (Investigators) from evidence retrieval (Verifier) contains the fabrication problem.

See [conclusions](docs/conclusions.md) for the full analysis, limitations, and cross-intervention patterns.

### Coefficient Giving BOTEC: blind validation (November 2026)

Coefficient Giving (formerly Open Philanthropy) published four sample BOTECs in May 2025, and later published its own corrections to one of them: trialing statins as an adjunct TB treatment. That makes a blind test possible. The pipeline sees only the original BOTEC. CG's later limitations and revisions are held out, and the verifier's web search excludes CG's site and the EA Forum, so it cannot find them. The pipeline's findings are then scored against CG's own follow-ups.

- **Run #01** (archived in `results/cg-tb-statins-run01/`): 1 of CG's points caught, 1 partial, 6 missed. Three of the misses (adoption speedup, benefit horizon, competing treatments) were raised by the decomposer but lost to a parser bug. The run also exposed silent output truncation on the newer models. Both are fixed; see below.
- **Run #02**: in progress.

## Pipeline architecture

```
1. DECOMPOSER (Opus)            Investigation threads with scoped specs and exclusion lists
2. INVESTIGATORS (Sonnet)       Candidate critiques per thread
3. VERIFIER (Sonnet, batched)   Citations and claims checked by web search; verified, unverifiable or rejected
4. QUANTIFIER (Opus)            Sensitivity analysis run against an executable replica of the CEA
5. ADVERSARIAL (Sonnet + Opus)  Advocate defends the CEA, Challenger rebuts, a neutral Judge audits
                                the debate for reasoning failures and assigns surviving strength
5b. LINKER (Sonnet)             Marks findings that depend on unverified claims as conditional
6. SYNTHESIZER (Opus)           Ranked final report with evidence, impact, and debate-quality audit
7. EXTRACTOR (extract.py)       graph.json for the red-team-explorer viewer (no API calls)
```

Design principles:
- **Only public materials as inputs.** Improvement has to come from method, not privileged access.
- **Scoped context per agent.** Each agent gets a focused context document, not the whole filing cabinet.
- **Verification is first-class.** Every factual claim is checked by web search before it reaches a human.
- **Quantitative grounding.** Impact claims are tied to perturbations computed on a replica of the CEA's formula chain.
- **Prompts are the experimental treatment.** Files in `prompts/` are read-only so runs stay comparable. Adapting the pipeline to a new funder happens in code and input files, never in prompts.

## Supported CEA formats

| Format | Reader | Example |
|---|---|---|
| GiveWell spreadsheet (.xlsx) | `pipeline/spreadsheet.py`: `WaterCEA`, `ITNCEA`, `MalariaCEA`, `VASCEA` | water-chlorination, itns, smc, vas |
| Prose BOTEC | `pipeline/botec.py`: formula-chain replica with parameters in JSON | cg-tb-statins |

Every reader implements the `CEAReader` protocol in `spreadsheet.py` (`PROGRAMS`, `get_parameter_summary`, `compute_cost_effectiveness`, `run_sensitivity`). A reader can also supply its own `PARAM_NAME_MAP`, so the quantifier maps critique parameters onto that model's names instead of GiveWell's.

### Adding a new CEA

1. **Reader.** Write a class implementing `CEAReader`. For a BOTEC, follow `TBStatinsBOTEC`: put the published parameters in `data/<name>/botec_params.json` and reproduce the published bottom line in a test.
2. **Inputs.** In `INTERVENTION_URLS` (`pipeline/config.py`), each source can be a URL, `file:<path under data/>`, or `""` for none. A local report file can open with a short context header that maps GiveWell terms to the funder's units and funding bar; see `data/cg-tb-statins/report.md`.
3. **Verifier allowlist.** Add an `INTERVENTION_VERIFIER_OVERRIDES` entry with domains suited to the topic. For a blind test, leave out the sites that host the answer key.
4. **Register** the reader in `cea_classes` in `run_pipeline.py`.

## Recent improvements (November 2026)

Found while adapting the pipeline to Coefficient Giving's BOTEC and moving to current models:

- **Model end-of-life.** The original `claude-*-4-20250514` models reached end-of-life on 2026-06-15. Defaults are now `claude-opus-5-5` and `claude-sonnet-5-5`, overridable with `REDTEAM_OPUS_MODEL` / `REDTEAM_SONNET_MODEL` in `.env`. Results from the new models are not directly comparable with the April runs.
- **Spend tracking.** Config refuses to start if a model has no pricing entry; unknown models used to be priced at $0, which hid spend. Web search fees ($10 per 1,000 searches) are still not counted.
- **Thinking headroom.** The 5.5 models always use adaptive thinking, and thinking tokens count against `max_tokens`. With the old caps, 14 of 22 calls in run #01 were truncated. Every cap is now multiplied by `REDTEAM_TOKEN_MULTIPLIER` (default 4); you pay only for tokens used.
- **Truncation is reported, not silent.** A call that stops at `max_tokens` is logged as an error and listed under `truncated_calls` in `pipeline-stats.json`.
- **Decomposer parsing.** Annotated thread headers such as `THREAD 3 (Structural/Methodological):` were dropped, and sections like "What CG already accounts for" were blank in the investigators' context because the parser expected the word GiveWell. Both are fixed.
- **Quantifier parsing.** Prose ranges ("current value 0.10 … range is 0.05–0.10"), markdown markers, code-style parameter names, and text before the first bold header now parse, so sensitivity analysis actually executes. Re-parsing the April SMC run gives identical results.
- **SDK compatibility.** `anthropic` 2.x depends on `httpx2`, so the direct `httpx` import failed on fresh installs; the pipeline now uses `anthropic.Timeout`. Long non-streaming requests get the explicit timeout the 2.x SDK requires. Tested on `anthropic` 0.42 and 2.6.

## Viewing results

`extract.py` turns a run's stage outputs into a `graph.json` for [red-team-explorer](https://github.com/tsondo/red-team-explorer), a static viewer with a two-column debate reader and a dependency graph.

```bash
python extract.py --input-dir results/vas --run-id vas-2026-04-13 --output-dir results/vas
```

## Repository structure

```
├── README.md
├── extract.py                   # Stage 7: graph.json for red-team-explorer
├── docs/
│   ├── Architecture.md          # Pipeline design document
│   ├── conclusions.md           # Results analysis, limitations, cross-intervention patterns
│   ├── analysis-givewell.md     # Critique of GiveWell's current approach
│   ├── judge_info.md            # Judge stage: failure-mode taxonomy
│   ├── linker_info.md           # Linker stage: conditional findings
│   └── pipeline-spec.md         # Build spec with schemas and implementation details
├── prompts/                     # System prompts for each agent (read-only)
├── pipeline/
│   ├── run_pipeline.py          # Orchestrator (--resume-from support)
│   ├── agents.py                # Agent callers and output parsers
│   ├── spreadsheet.py           # GiveWell spreadsheet readers and the CEAReader protocol
│   ├── botec.py                 # Prose BOTEC readers
│   ├── schemas.py               # Dataclasses for pipeline data flow
│   └── config.py                # Models, pricing, token caps, per-intervention settings
├── data/                        # CEA inputs (read-only)
├── results/<intervention>/      # Stage outputs (.json + .md), log, and stats per run
└── tests/                       # 186 tests (readers, parsers, schemas, model-upgrade regressions)
```

## Usage

```bash
# Set up (Python 3.10+)
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# API key in .env (not a shell variable)
echo 'ANTHROPIC_API_KEY=sk-ant-...' > .env

# Run one intervention
python -m pipeline.run_pipeline vas
python -m pipeline.run_pipeline cg-tb-statins

# Resume from a specific stage
python -m pipeline.run_pipeline itns --resume-from quantifier

# Tests (no API calls)
python -m pytest tests/ -q
```

## Constraints

- **No agent frameworks.** No LangChain, CrewAI or AutoGen; direct Anthropic SDK calls only.
- **Four dependencies:** anthropic, openpyxl, pandas, python-dotenv.
- **No streaming.** Requests are batch calls.
- **Budget:** $50 for the original three GiveWell interventions. Actual spend was about $62, mostly the water v1 overrun before verifier batching; later runs came in within target.

## Key files

| File | Purpose |
|---|---|
| `results/*/06-synthesizer.md` | Final red team report for each run |
| `results/*/pipeline-stats.json` | Tokens, cost per stage, and any truncated calls |
| `docs/conclusions.md` | Cross-intervention analysis and limitations |
| `docs/Architecture.md` | Full pipeline specification |
| `pipeline/spreadsheet.py`, `pipeline/botec.py` | CEA formula-chain replicas used for sensitivity analysis |
