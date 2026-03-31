# GiveWell AI Red Teaming — Multi-Agent Pipeline

A proof-of-concept multi-agent pipeline that red teams GiveWell's cost-effectiveness analyses. Demonstrates that architectural improvements (decomposition, verification, quantification, adversarial testing) beat single-pass prompting for research critique.

## Origin

GiveWell published a [report on AI red teaming](https://www.givewell.org/how-we-work/our-criteria/cost-effectiveness/ai-red-teaming-12-25) (January 2026) describing their experiment using ChatGPT 5 Pro with structured prompts. Their results: ~15–30% of AI critiques were useful, with persistent hallucination, lost context, and unreliable quantitative estimates.

## Thesis

GiveWell's limitations are architecture limitations, not model limitations. Decomposition, verification pipelines, adversarial agent structure, scoped context, and tool-augmented quantitative reasoning each independently improve results — and they compound.

## Results

Three interventions analyzed using only public materials and commodity models (Claude Sonnet for most stages, Opus for decomposition and quantification):

| Intervention | Critiques | Signal Rate | Novel Findings | Cost |
|---|---|---|---|---|
| Water chlorination | 31 generated → 26 surviving | 84% | 10 novel | ~$30 (v1) |
| Insecticide-treated nets | 30 generated → 30 surviving | 100% | 9 novel | $16.00 |
| Seasonal malaria chemoprevention | 34 generated → 28 surviving | 82% | 6 novel | $15.96 |

GiveWell's baseline: ~15–30% useful. Our target: >60%. All three runs exceeded it.

Zero hallucinated citations across all runs — the architectural separation of hypothesis generation (Investigators) from evidence retrieval (Verifier) eliminated the fabrication problem.

See [conclusions](docs/conclusions.md) for full analysis, limitations, and cross-intervention patterns.

## Pipeline Architecture

```
1. DECOMPOSER (Opus)         → 11 investigation threads with scoped specs
2. INVESTIGATORS (Sonnet×11)  → ~30 candidate critiques with cited evidence
3. VERIFIER (Sonnet, batched) → Citations checked, claims grounded, or rejected
4. QUANTIFIER (Opus)          → Sensitivity analysis against actual CEA spreadsheets
5. ADVERSARIAL PAIR (Sonnet)  → Advocate + Challenger stress-test each critique
6. SYNTHESIZER (Opus)         → Ranked final report with evidence and impact estimates
```

Key design principles:
- **Only public materials as inputs.** Proves improvement comes from methodology, not privileged access.
- **Scoped context per agent.** Each agent gets a focused context document, not the whole filing cabinet.
- **Verification is first-class.** Every factual claim is independently checked via web search before reaching a human.
- **Quantitative grounding.** Impact claims are tied to computed perturbations against actual spreadsheet models.

## Repository Structure

```
├── README.md
├── docs/
│   ├── architecture.md          # Pipeline design document
│   ├── conclusions.md           # Results analysis, limitations, cross-intervention patterns
│   ├── analysis-givewell.md     # Critique of GiveWell's current approach
│   └── pipeline-spec.md         # Build spec with schemas and implementation details
├── prompts/                     # System prompts for each agent (7 files)
├── pipeline/
│   ├── run_pipeline.py          # Main orchestrator (--resume-from support)
│   ├── agents.py                # All agent callers (decomposer through synthesizer)
│   ├── spreadsheet.py           # CEA readers: WaterCEA, ITNCEA, MalariaCEA
│   ├── schemas.py               # Dataclasses for pipeline data flow
│   └── config.py                # API keys, model selection, cost thresholds
├── data/                        # CEA spreadsheets (.xlsx, read-only)
├── results/
│   ├── water-chlorination/      # All 6 stage outputs (.json + .md) + stats
│   ├── itns/                    # All 6 stage outputs (.json + .md) + stats
│   └── smc/                     # All 6 stage outputs (.json + .md) + stats
└── tests/                       # 62 tests (spreadsheet readers, parsers, schemas)
```

## Usage

```bash
# Install dependencies (anthropic, openpyxl, pandas, python-dotenv)
pip install -r requirements.txt

# Run a single intervention
python -m pipeline.run_pipeline water-chlorination
python -m pipeline.run_pipeline itns
python -m pipeline.run_pipeline smc

# Resume from a specific stage
python -m pipeline.run_pipeline itns --resume-from quantifier

# Run tests
python -m pytest tests/ -v
```

Requires an Anthropic API key in `.env`:
```
ANTHROPIC_API_KEY=sk-ant-...
```

## Constraints

- **No agent frameworks.** No LangChain, CrewAI, AutoGen — direct Anthropic SDK calls only.
- **Four dependencies:** anthropic, openpyxl, pandas, python-dotenv.
- **Budget:** $50 total across all interventions. Actual spend: ~$62 (water v1 overrun before verifier optimization; subsequent runs within target).

## Key Files

| File | Purpose |
|---|---|
| `results/*/06-synthesizer.md` | Final red team reports for each intervention |
| `docs/conclusions.md` | Cross-intervention analysis and honest limitations |
| `docs/architecture.md` | Full pipeline specification |
| `pipeline/spreadsheet.py` | Three CEA formula chain replications with sensitivity analysis |
