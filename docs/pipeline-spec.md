# Handoff Spec: `run_pipeline.py`

## What This Is

This spec describes an automated pipeline for AI red teaming of GiveWell's cost-effectiveness analyses. You are building `run_pipeline.py` — a Python script that orchestrates six agent stages via the Anthropic API, passes structured outputs between them, and executes quantitative analysis against real CEA spreadsheets.

**Do not write code immediately.** First: read this spec and all referenced files. Then: produce a plan. Then: critique your own plan. Iterate until the plan is solid. Then build.

---

## Repository Context

The repo should look like this when you start:

```
givewell-red-team/
├── README.md
├── docs/
│   ├── architecture.md          ← Full pipeline spec. READ THIS FIRST.
│   ├── analysis-givewell.md     ← Critique of GiveWell's approach (context only)
│   └── manual-workflow.md       ← Manual version of what you're automating
├── prompts/
│   ├── decomposer.md
│   ├── investigator-template.md
│   ├── verifier.md
│   ├── quantifier.md
│   ├── adversarial-advocate.md
│   ├── adversarial-challenger.md
│   └── synthesizer.md
├── results/
│   └── water-chlorination/
│       └── decomposer-output.md ← Already generated. Your pipeline should reproduce this.
└── data/                        ← CEA spreadsheets already here
    ├── WaterCEA.xlsx
    ├── InsecticideCEA.xlsx
    └── MalariaCEA.xlsx
```

You will create:
```
├── pipeline/
│   ├── run_pipeline.py          ← Main orchestrator
│   ├── agents.py                ← Agent call functions
│   ├── spreadsheet.py           ← CEA spreadsheet reading and sensitivity analysis
│   ├── config.py                ← API keys, model settings, file paths
│   └── schemas.py               ← Output schemas for structured data between stages
```

---

## Architecture Summary

Read `docs/architecture.md` for the full spec. The short version:

```
DECOMPOSER → INVESTIGATORS (×N) → VERIFIER → QUANTIFIER → ADVERSARIAL PAIR → SYNTHESIZER
```

Each stage is a separate API call with its own system prompt (from `prompts/`), scoped inputs, and structured outputs. The key design constraint: **no agent sees more than it needs.** Information flow is controlled.

---

## Technical Requirements

### API Calls

- Use the Anthropic Python SDK (`anthropic` package)
- Model: `claude-sonnet-4-20250514` for Investigators, Verifier, Adversarial Pair
- Model: `claude-opus-4-20250115` for Decomposer, Quantifier, Synthesizer (these need the most reasoning)
- Enable web search tool for the Verifier stage (it needs to look up papers and data)
- Set `max_tokens` appropriately per stage: Decomposer and Synthesizer need 8000+, Investigators need 4000, Verifier needs 4000 per critique, Adversarial needs 3000 per side

### Structured Output Between Stages

Each stage must produce structured output that the next stage can consume. Use XML tags in the prompt to request structured output, then parse it in Python. Define schemas in `schemas.py`.

**Decomposer output schema:**
```python
@dataclass
class InvestigationThread:
    name: str
    scope: str
    key_questions: list[str]
    cea_parameters_affected: list[str]
    relevant_sources: list[str]
    out_of_scope: str
    context_md: str  # The full CONTEXT.md for this thread

@dataclass
class DecomposerOutput:
    threads: list[InvestigationThread]
    exclusion_list: list[str]
    cea_parameter_map: str  # Keep as free text — too complex for rigid schema
```

**Investigator output schema:**
```python
@dataclass
class CandidateCritique:
    thread_name: str
    title: str
    hypothesis: str
    mechanism: str
    parameters_affected: list[str]
    suggested_evidence: list[str]
    estimated_direction: str  # "increases" | "decreases" | "uncertain"
    estimated_magnitude: str  # "large" | "medium" | "small" | "unknown"
```

**Verifier output schema:**
```python
@dataclass
class VerifiedCritique:
    original: CandidateCritique
    verdict: str  # "verified" | "partially_verified" | "unverified"
    evidence_found: list[str]
    evidence_strength: str  # "strong" | "moderate" | "weak"
    counter_evidence: list[str]
    caveats: list[str]
    revised_hypothesis: str | None
```

**Quantifier output schema:**
```python
@dataclass
class QuantifiedCritique:
    critique: VerifiedCritique
    target_parameters: list[dict]  # {name, cell_ref, current_value}
    alternative_range: list[dict]  # {name, low, central, high, justification}
    sensitivity_results: dict      # {baseline, central_alt, best_case, worst_case}
    materiality: str               # "material" | "notable" | "immaterial"
    interaction_effects: list[str]
```

**Adversarial output schema:**
```python
@dataclass
class DebatedCritique:
    critique: QuantifiedCritique
    advocate_defense: str
    challenger_rebuttal: str
    surviving_strength: str  # "strong" | "moderate" | "weak"
    key_unresolved: list[str]
    recommended_action: str  # "investigate" | "adjust_model" | "monitor" | "dismiss"
```

### Spreadsheet Analysis (Quantifier Stage)

This is the most technically complex part. `spreadsheet.py` must:

1. **Read the CEA spreadsheet** using `openpyxl` (preserves formulas and structure) and `pandas` (for data manipulation).

2. **Map the spreadsheet structure.** The CEA has multiple tabs. Key tabs to identify:
   - "Start Here" / "Notes" — documentation
   - "Results" — bottom-line cost-effectiveness output
   - "Mortality effect size" — base estimate and pooling
   - "Internal validity adjustment" — bundled treatment adjustment
   - Tabs for each country/program context
   - "User inputs" and "Moral weights" — configurable parameters

3. **Identify key cells.** For each parameter the Decomposer maps, find the corresponding cell reference. This is semi-automated: read the spreadsheet, look for named ranges or labels, and build a parameter→cell mapping. Some of this will require human verification — build in a confirmation step.

4. **Run sensitivity analysis.** For each critique, the Quantifier needs to:
   - Record the current value of affected parameters
   - Set them to alternative values (from the Verifier's evidence)
   - Recalculate the result
   
   **Important caveat:** `openpyxl` cannot evaluate Excel formulas. Options:
   
   **Option A (recommended):** Export key formula relationships into Python functions. Read the spreadsheet to understand the formula chain, then replicate the critical path in Python. This is more work upfront but gives you full control over the calculation.
   
   **Option B:** Use `xlcalc` or similar library to evaluate formulas in-memory. Less reliable but faster to implement.
   
   **Option C:** If the formulas are too complex, generate a report of "if parameter X changes from A to B, here is what the formula chain looks like" and let the human do the spreadsheet change. This is the fallback.
   
   Start with Option A for the critical path (base mortality effect → adjustments → final mortality reduction → cost-effectiveness result). You don't need to replicate every formula — just the ones on the critical path from the parameters the Decomposer identified.

5. **Handle the plausibility cap.** The CEA has a cap that binds in some contexts. Your sensitivity analysis must check whether a parameter change causes the estimate to hit the cap — this changes the interpretation.

### Web Search for Verifier

The Verifier stage needs web search to check citations and find evidence. Use the Anthropic API's tool use with web search:

```python
tools=[{"type": "web_search_20250305", "name": "web_search"}]
```

The Verifier's prompt already instructs it to search systematically. You just need to enable the tool in the API call.

### File I/O

- Read prompts from `prompts/` directory
- Read spreadsheets from `data/`
- Write all intermediate outputs to `results/{intervention}/` as both JSON (for pipeline consumption) and markdown (for human reading)
- Write final Synthesizer output to `results/{intervention}/final-report.md`

---

## Pipeline Flow in Detail

### Step 1: Decomposer
```python
def run_decomposer(intervention_report: str, cea_summary: str, baseline_output: str | None) -> DecomposerOutput:
    # Load prompts/decomposer.md as system prompt
    # Construct user message with report + CEA summary + optional baseline
    # Call API (opus)
    # Parse structured output into DecomposerOutput
    # Save to results/{intervention}/01-decomposer.json and .md
```

### Step 2: Investigators (parallel)
```python
def run_investigators(threads: list[InvestigationThread], exclusion_list: list[str]) -> list[CandidateCritique]:
    # For each thread:
    #   Load prompts/investigator-template.md
    #   Replace {{CONTEXT_MD}} with thread.context_md
    #   Include exclusion_list in the prompt
    #   Call API (sonnet)
    #   Parse output into list[CandidateCritique]
    # These CAN be run in parallel (asyncio or threading)
    # Save to results/{intervention}/02-investigators.json and .md
```

### Step 3: Verifier
```python
def run_verifier(critiques: list[CandidateCritique]) -> list[VerifiedCritique]:
    # For each critique (one at a time — isolation matters):
    #   Load prompts/verifier.md as system prompt
    #   Include the critique as user message
    #   Call API (sonnet) WITH web search tool enabled
    #   Parse output into VerifiedCritique
    # Filter: keep verified + partially_verified, log unverified
    # Save to results/{intervention}/03-verifier.json and .md
```

### Step 4: Quantifier
```python
def run_quantifier(critiques: list[VerifiedCritique], spreadsheet_path: str, parameter_map: str) -> list[QuantifiedCritique]:
    # Load and analyze the spreadsheet (spreadsheet.py)
    # For each verified critique:
    #   Load prompts/quantifier.md as system prompt
    #   Include: critique, parameter map, relevant spreadsheet data
    #   Call API (opus) — needs strong reasoning for parameter mapping
    #   Parse output
    #   Run the actual sensitivity calculation in Python
    #   Combine API reasoning with Python calculation results
    # Filter: drop immaterial critiques (but log them)
    # Save to results/{intervention}/04-quantifier.json and .md
```

### Step 5: Adversarial Pair
```python
def run_adversarial(critiques: list[QuantifiedCritique], intervention_report: str) -> list[DebatedCritique]:
    # For each material/notable critique:
    #   Load prompts/adversarial-advocate.md
    #   Call API (sonnet) with critique + report → get defense
    #   Load prompts/adversarial-challenger.md
    #   Call API (sonnet) with critique + defense → get rebuttal + surviving_strength
    #   Combine into DebatedCritique
    # Save to results/{intervention}/05-adversarial.json and .md
```

### Step 6: Synthesizer
```python
def run_synthesizer(debated: list[DebatedCritique], all_filtered: dict, baseline_output: str | None) -> str:
    # Load prompts/synthesizer.md as system prompt
    # Include all debated critiques with full metadata
    # Include the filtered/dismissed critiques log
    # Include GiveWell's baseline output if available
    # Call API (opus) — needs strong reasoning for ranking and comparison
    # Save to results/{intervention}/06-synthesizer.md (final report)
```

### Main Orchestrator
```python
def run_pipeline(intervention: str):
    # 1. Load source materials
    report = load_intervention_report(intervention)
    cea_summary = analyze_spreadsheet(intervention)  # from spreadsheet.py
    baseline = load_baseline_output(intervention)     # GiveWell's AI output, if available
    
    # 2. Run pipeline
    decomposed = run_decomposer(report, cea_summary, baseline)
    candidates = run_investigators(decomposed.threads, decomposed.exclusion_list)
    verified = run_verifier(candidates)
    quantified = run_quantifier(verified, get_spreadsheet_path(intervention), decomposed.cea_parameter_map)
    debated = run_adversarial(quantified, report)
    final = run_synthesizer(debated, get_all_filtered(), baseline)
    
    # 3. Summary
    print_summary(candidates, verified, quantified, debated)
```

---

## Configuration

`config.py` should handle:

```python
# API — loaded from .env file via python-dotenv (NOT from shell environment)
# The .env file is in the repo root, already in .gitignore.
# This keeps API credentials isolated from Claude Code's own session.
from dotenv import load_dotenv
load_dotenv()
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
OPUS_MODEL = "claude-opus-4-20250115"
SONNET_MODEL = "claude-sonnet-4-20250514"

# Paths
REPO_ROOT = Path(__file__).parent.parent
PROMPTS_DIR = REPO_ROOT / "prompts"
SOURCE_DIR = REPO_ROOT / "data"
RESULTS_DIR = REPO_ROOT / "results"

# Pipeline settings
MAX_INVESTIGATOR_THREADS = 8
MAX_RETRIES = 2
MATERIALITY_THRESHOLD = 0.01  # 1% change in cost-effectiveness = "notable"
HIGH_MATERIALITY_THRESHOLD = 0.10  # 10% = "material"
```

---

## Error Handling and Resumability

The pipeline makes many API calls. It WILL fail partway through at some point. Design for this:

1. **Save after every stage.** Each stage writes its output to disk before the next stage starts.
2. **Resume from any stage.** Accept a `--resume-from` flag: `python run_pipeline.py water-chlorination --resume-from verifier` loads the previous stages' outputs from disk and continues from the specified stage.
3. **Retry on API errors.** Wrap API calls with exponential backoff. Max 2 retries per call.
4. **Log everything.** Write a `pipeline.log` to `results/{intervention}/` with timestamps, token usage, and any errors.

---

## Testing Strategy

1. **Unit test `spreadsheet.py` first.** Load the water chlorination CEA, verify you can read key parameters, and that your sensitivity calculation matches a manual check. This is the riskiest component.

2. **Test each agent in isolation.** Run the Decomposer alone, inspect output, verify it parses correctly. Then Investigators. Etc.

3. **Run the full pipeline on water chlorination.** Compare output to the existing `decomposer-output.md` and to GiveWell's published AI output.

4. **Then run Phase 2 (ITNs) and Phase 3 (SMC)** to verify generalization.

---

## What Not to Build

- **No web UI.** This is a CLI tool.
- **No database.** JSON files on disk are sufficient.
- **No agent framework** (LangChain, CrewAI, etc.). Direct API calls with structured prompts. The overhead of a framework is not justified for a six-stage linear pipeline.
- **No streaming.** Batch calls are fine. The pipeline runs unattended.

---

## Dependencies

```
anthropic>=0.42.0
openpyxl>=3.1.0
pandas>=2.0.0
python-dotenv>=1.0.0
```

That's it. Keep it minimal.

---

## Budget

Total API credits available: $50. This should cover all three phases with room to spare, but be cost-conscious:

- **Log token usage per API call.** Print input/output tokens and estimated cost after each stage.
- **Use Sonnet where the spec says Sonnet.** Don't default to Opus for everything — Sonnet is ~5x cheaper and sufficient for Investigators, Verifier, and Adversarial stages.
- **Run water chlorination (Phase 1) first.** Review costs before committing to Phase 2 and 3.
- **Estimated cost per phase:** ~$5-15 depending on critique count and Verifier search volume.

---

## Planning Checklist

Before writing any code, produce a plan that answers:

1. How will you parse the structured output from each API call? (XML tags? JSON in the response? Separate parsing functions per stage?)
2. How will you handle the spreadsheet formula chain? Which option (A/B/C) for the Quantifier, and why?
3. How will you handle the Verifier's web search results? The API returns tool use blocks — how do you extract and pass them?
4. What's your file naming convention for intermediate outputs?
5. How will `--resume-from` work? What state needs to be serialized?
6. What's your approach to parallel Investigator calls? (asyncio, threading, or sequential?)

After your plan, critique it:
- Where are the likely failure points?
- What assumptions are you making about the spreadsheet structure?
- How will you handle it if the API returns unparseable output?
- Is your sensitivity calculation actually correct? Walk through an example.

Then iterate until the plan is solid. Then build.
