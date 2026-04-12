# CLAUDE.md

## Project

Multi-agent pipeline for AI red teaming of GiveWell's cost-effectiveness analyses. We're proving that architecture improvements (decomposition, verification, quantification, adversarial testing) beat single-pass prompting for research critique.

## Key Files — Read Before Doing Anything

- `docs/architecture.md` — Full pipeline spec. Defines all six stages, inputs/outputs, information flow rules.
- `pipeline-spec.md` — Your build spec. Contains schemas, API configuration, implementation details. **Follow the planning checklist at the bottom before writing code.**
- `prompts/` — All seven agent prompts. These are the system prompts for each API call. Do not modify them.
- `results/water-chlorination/decomposer-output.md` — Example output from Stage 1. Your pipeline should produce comparable structured output.
- `data/` — CEA spreadsheets (WaterCEA.xlsx, InsecticideCEA.xlsx, MalariaCEA.xlsx). Read-only inputs.

## Constraints

- **API key is in `.env` via python-dotenv. Do NOT use shell environment variables.**
- **Budget is $50 total.** Log token usage and estimated cost per API call. Use Sonnet where the spec says Sonnet, Opus only where specified.
- **Run Phase 1 (water chlorination) first.** Review costs before running Phase 2 and 3.
- **No git worktrees.** Work directly on the current branch. Do not use the using-git-worktrees skill.
- **No agent frameworks.** No LangChain, CrewAI, AutoGen. Direct Anthropic SDK calls.
- **No streaming.** Batch API calls.
- **Four dependencies only:** anthropic, openpyxl, pandas, python-dotenv.
- **Save intermediate outputs after every stage.** Both JSON (for pipeline) and markdown (for humans) to `results/{intervention}/`.
## Behavior

**Surgical changes.** Touch only what you must. Don't "improve" adjacent code, comments, or formatting. Don't refactor things that aren't broken. **Every changed line should trace directly to the user's request or the spec.**

**Prompts in `prompts/` are read-only.** They are the experimental treatment. Modifying them invalidates all results gathered so far and breaks comparability across runs. If a prompt seems wrong, raise it — don't edit it.

**No speculative API calls.** The pipeline has exactly the stages defined in `docs/architecture.md`. Do not add "helpful" extra LLM calls (clarification passes, meta-critiques, retries with rephrasing) that aren't in the spec. Every API call costs real money against a $50 budget and contaminates the experiment by introducing variables not in the design.

**Push back when warranted.** If the spec is ambiguous or a constraint conflicts with another, name the conflict and ask. Do not silently pick an interpretation — this is a research pipeline and silent choices become uncontrolled variables.

---
## Workflow

**Do not write code immediately.** Your process:
1. Read this file, `pipeline-spec.md`, and `docs/architecture.md` fully.
2. Produce a plan answering the six questions in the planning checklist.
3. Critique your own plan — identify failure points, bad assumptions, edge cases.
4. Iterate the plan until solid.
5. Build `spreadsheet.py` first — it's the riskiest component. Unit test it against WaterCEA.xlsx.
6. Build each agent caller in `agents.py`, test in isolation.
7. Build the orchestrator `run_pipeline.py` last.

## Code Style

- Type hints on all functions.
- Dataclasses for structured data (schemas defined in `pipeline-spec.md`).
- `pathlib.Path` for all file operations.
- Logging to both console and `results/{intervention}/pipeline.log`.
- `--resume-from` CLI flag to restart from any stage.

## What Success Looks Like

Run `python pipeline/run_pipeline.py water-chlorination` and get:
- Intermediate outputs for all six stages in `results/water-chlorination/`
- A `final-report.md` with ranked critiques, verified evidence, quantified impact, and comparison against GiveWell's published AI output
- Total cost under $15 for one intervention
