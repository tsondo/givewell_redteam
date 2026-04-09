"""Main pipeline orchestrator. Run with: python -m pipeline.run_pipeline water-chlorination"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

from pipeline.config import (
    COST_WARNING_PER_INTERVENTION,
    DATA_DIR,
    INTERVENTION_URLS,
    RESULTS_DIR,
    get_verifier_settings,
)
from pipeline.schemas import (
    CandidateCritique,
    DebatedCritique,
    DecomposerOutput,
    PipelineStats,
    QuantifiedCritique,
    VerifiedCritique,
)
from pipeline.agents import (
    fetch_web_content,
    run_adversarial,
    run_decomposer,
    run_investigators,
    run_quantifier,
    run_synthesizer,
    run_verifier,
)
from pipeline.spreadsheet import ITNCEA, MalariaCEA, VASCEA, WaterCEA

logger = logging.getLogger("pipeline")

STAGES = [
    "decomposer",
    "investigators",
    "verifier",
    "quantifier",
    "adversarial",
    "synthesizer",
]


# ---------------------------------------------------------------------------
# Logging setup
# ---------------------------------------------------------------------------


def setup_logging(intervention: str) -> None:
    """Configure logging to both console and file."""
    out_dir = RESULTS_DIR / intervention
    out_dir.mkdir(parents=True, exist_ok=True)

    root_logger = logging.getLogger("pipeline")
    root_logger.setLevel(logging.DEBUG)

    # Avoid adding duplicate handlers on repeated calls
    if root_logger.handlers:
        return

    fmt = logging.Formatter("%(asctime)s %(levelname)s %(message)s", datefmt="%H:%M:%S")

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(fmt)
    root_logger.addHandler(console_handler)

    # File handler
    log_path = out_dir / "pipeline.log"
    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(fmt)
    root_logger.addHandler(file_handler)


# ---------------------------------------------------------------------------
# Stage loading for --resume-from
# ---------------------------------------------------------------------------


def load_stage_json(intervention: str, stage_num: int, stage_name: str) -> dict | list:
    """Load a stage's JSON output from disk for resume."""
    path = RESULTS_DIR / intervention / f"{stage_num:02d}-{stage_name}.json"
    if not path.exists():
        raise FileNotFoundError(
            f"Cannot resume: expected stage output not found at {path}. "
            f"Run the pipeline from an earlier stage first."
        )
    return json.loads(path.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Main pipeline function
# ---------------------------------------------------------------------------


def run_pipeline(intervention: str, resume_from: str | None = None) -> None:
    """Orchestrate all six pipeline stages sequentially."""
    if intervention not in INTERVENTION_URLS:
        raise ValueError(
            f"Unknown intervention '{intervention}'. "
            f"Choices: {list(INTERVENTION_URLS.keys())}"
        )

    urls = INTERVENTION_URLS[intervention]
    stats = PipelineStats()
    stats.cost_warning_threshold = get_verifier_settings(intervention)["cost_warning"]

    start_idx = STAGES.index(resume_from) if resume_from else 0
    logger.info(
        "Starting pipeline for '%s' from stage '%s' (index %d)",
        intervention,
        resume_from or STAGES[0],
        start_idx,
    )

    # ------------------------------------------------------------------
    # Load CEA spreadsheet
    # ------------------------------------------------------------------
    spreadsheet_path = DATA_DIR / urls["spreadsheet"]
    logger.info("Loading CEA spreadsheet: %s", spreadsheet_path)
    cea_classes = {
        "water-chlorination": WaterCEA,
        "itns": ITNCEA,
        "smc": MalariaCEA,
        "vas": VASCEA,
    }
    cea_cls = cea_classes.get(intervention, WaterCEA)
    cea = cea_cls(spreadsheet_path)
    cea_summary = cea.get_parameter_summary()
    logger.info("CEA spreadsheet loaded.")

    # ------------------------------------------------------------------
    # Fetch web content if starting from stage 0
    # ------------------------------------------------------------------
    intervention_report: str = ""
    baseline_output: str = ""

    if start_idx == 0:
        logger.info("Fetching intervention report from %s", urls["report"])
        intervention_report = fetch_web_content(urls["report"], stats)
        logger.info("Fetching baseline output from %s", urls["baseline"])
        baseline_output = fetch_web_content(urls["baseline"], stats)

    # ------------------------------------------------------------------
    # Stage 1: Decomposer
    # ------------------------------------------------------------------
    decomposer_output: DecomposerOutput

    if start_idx <= 0:
        logger.info("=== Stage 1: Decomposer ===")
        decomposer_output, _ = run_decomposer(
            intervention_report=intervention_report,
            cea_summary=cea_summary,
            baseline_output=baseline_output,
            stats=stats,
            intervention=intervention,
        )
        logger.info(
            "Decomposer produced %d investigation threads.", len(decomposer_output.threads)
        )
    else:
        logger.info("Loading Stage 1 (decomposer) from disk.")
        data = load_stage_json(intervention, 1, "decomposer")
        assert isinstance(data, dict)
        decomposer_output = DecomposerOutput.from_dict(data)
        logger.info(
            "Loaded %d investigation threads from disk.", len(decomposer_output.threads)
        )

    # ------------------------------------------------------------------
    # Stage 2: Investigators
    # ------------------------------------------------------------------
    candidate_critiques: list[CandidateCritique]

    if start_idx <= 1:
        logger.info("=== Stage 2: Investigators ===")
        candidate_critiques, _ = run_investigators(
            threads=decomposer_output.threads,
            exclusion_list=decomposer_output.exclusion_list,
            stats=stats,
            intervention=intervention,
        )
        logger.info("Investigators produced %d candidate critiques.", len(candidate_critiques))
    else:
        logger.info("Loading Stage 2 (investigators) from disk.")
        data = load_stage_json(intervention, 2, "investigators")
        assert isinstance(data, list)
        candidate_critiques = [CandidateCritique.from_dict(d) for d in data]
        logger.info("Loaded %d candidate critiques from disk.", len(candidate_critiques))

    # ------------------------------------------------------------------
    # Stage 3: Verifier
    # ------------------------------------------------------------------
    verified_critiques: list[VerifiedCritique]
    rejected_critiques: list[VerifiedCritique] = []

    if start_idx <= 2:
        logger.info("=== Stage 3: Verifier ===")
        verified_critiques, rejected_critiques, _ = run_verifier(
            critiques=candidate_critiques,
            stats=stats,
            intervention=intervention,
        )
        logger.info(
            "Verifier passed %d / %d critiques (%d rejected).",
            len(verified_critiques),
            len(candidate_critiques),
            len(rejected_critiques),
        )
    else:
        logger.info("Loading Stage 3 (verifier) from disk.")
        data = load_stage_json(intervention, 3, "verifier")
        assert isinstance(data, list)
        all_verified = [VerifiedCritique.from_dict(d) for d in data]
        # Filter for passing verdicts (same logic as run_verifier)
        verified_critiques = [
            v for v in all_verified if v.verdict in ("verified", "partially_verified")
        ]
        # Load rejected critiques if available
        rejected_path = RESULTS_DIR / intervention / "03-verifier-rejected.json"
        if rejected_path.exists():
            rejected_data = json.loads(rejected_path.read_text(encoding="utf-8"))
            rejected_critiques = [VerifiedCritique.from_dict(d) for d in rejected_data]
        logger.info(
            "Loaded %d verified critiques (%d passing, %d rejected) from disk.",
            len(all_verified),
            len(verified_critiques),
            len(rejected_critiques),
        )

    # ------------------------------------------------------------------
    # Stage 4: Quantifier
    # ------------------------------------------------------------------
    quantified_critiques: list[QuantifiedCritique]

    if start_idx <= 3:
        logger.info("=== Stage 4: Quantifier ===")
        quantified_critiques, _ = run_quantifier(
            critiques=verified_critiques,
            cea=cea,
            cea_parameter_map=decomposer_output.cea_parameter_map,
            stats=stats,
            intervention=intervention,
        )
        logger.info("Quantifier processed %d critiques.", len(quantified_critiques))
    else:
        logger.info("Loading Stage 4 (quantifier) from disk.")
        data = load_stage_json(intervention, 4, "quantifier")
        assert isinstance(data, list)
        quantified_critiques = [QuantifiedCritique.from_dict(d) for d in data]
        logger.info("Loaded %d quantified critiques from disk.", len(quantified_critiques))

    # ------------------------------------------------------------------
    # Ensure intervention_report is available for adversarial stage
    # ------------------------------------------------------------------
    if start_idx > 0 and not intervention_report:
        logger.info(
            "Re-fetching intervention report for adversarial stage from %s", urls["report"]
        )
        intervention_report = fetch_web_content(urls["report"], stats)

    # ------------------------------------------------------------------
    # Stage 5: Adversarial
    # ------------------------------------------------------------------
    debated_critiques: list[DebatedCritique]

    if start_idx <= 4:
        logger.info("=== Stage 5: Adversarial ===")
        debated_critiques, _ = run_adversarial(
            critiques=quantified_critiques,
            intervention_report=intervention_report,
            cea_parameter_map=decomposer_output.cea_parameter_map,
            stats=stats,
            intervention=intervention,
        )
        logger.info("Adversarial stage produced %d debated critiques.", len(debated_critiques))
    else:
        logger.info("Loading Stage 5 (adversarial) from disk.")
        data = load_stage_json(intervention, 5, "adversarial")
        assert isinstance(data, list)
        debated_critiques = [DebatedCritique.from_dict(d) for d in data]
        logger.info("Loaded %d debated critiques from disk.", len(debated_critiques))

    # ------------------------------------------------------------------
    # Stage 6: Synthesizer
    # ------------------------------------------------------------------
    if start_idx <= 5:
        logger.info("=== Stage 6: Synthesizer ===")
        if start_idx > 0 and not baseline_output:
            logger.info(
                "Fetching baseline output for synthesizer from %s", urls["baseline"]
            )
            baseline_output = fetch_web_content(urls["baseline"], stats)

        final_report = run_synthesizer(
            debated=debated_critiques,
            all_critiques_count=len(candidate_critiques),
            verified_count=len(verified_critiques),
            rejected_critiques=rejected_critiques,
            baseline_output=baseline_output,
            stats=stats,
            intervention=intervention,
        )
        logger.info("Synthesizer produced final report (%d chars).", len(final_report))
    else:
        logger.info("Stage 6 (synthesizer) already complete; skipping.")

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    logger.info("=== Pipeline Complete ===")
    logger.info(
        "Total tokens: %d in / %d out",
        stats.total_input_tokens,
        stats.total_output_tokens,
    )
    logger.info("Total cost: $%.4f", stats.total_cost)
    if stats.total_cost > COST_WARNING_PER_INTERVENTION:
        logger.warning(
            "Total cost $%.2f exceeded warning threshold $%.2f",
            stats.total_cost,
            COST_WARNING_PER_INTERVENTION,
        )

    for stage_name, stage_cost in sorted(stats.stage_costs.items()):
        logger.info("  [%s] $%.4f", stage_name, stage_cost)

    # Save pipeline stats
    stats_path = RESULTS_DIR / intervention / "pipeline-stats.json"
    stats_dict = {
        "total_input_tokens": stats.total_input_tokens,
        "total_output_tokens": stats.total_output_tokens,
        "total_cost": stats.total_cost,
        "stage_costs": stats.stage_costs,
    }
    stats_path.write_text(json.dumps(stats_dict, indent=2), encoding="utf-8")
    logger.info("Pipeline stats saved to %s", stats_path)


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the red teaming pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Example: python -m pipeline.run_pipeline water-chlorination",
    )
    parser.add_argument(
        "intervention",
        choices=list(INTERVENTION_URLS.keys()),
        help="Which intervention to analyse",
    )
    parser.add_argument(
        "--resume-from",
        choices=STAGES,
        default=None,
        metavar="STAGE",
        help=(
            "Resume from a specific stage, loading prior stages from disk. "
            f"Choices: {', '.join(STAGES)}"
        ),
    )

    args = parser.parse_args()
    setup_logging(args.intervention)
    run_pipeline(args.intervention, resume_from=args.resume_from)


if __name__ == "__main__":
    main()
