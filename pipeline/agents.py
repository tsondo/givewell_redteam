"""Agent callers for all six pipeline stages.

Each stage loads a system prompt, constructs a user message, calls the
Anthropic API, parses the text response into dataclasses, and saves
intermediate outputs.
"""
from __future__ import annotations

import json
import logging
import re
import time
from pathlib import Path
from typing import Any

import anthropic

from pipeline.config import (
    ANTHROPIC_API_KEY,
    MAX_RETRIES,
    MAX_TOKENS_ADVERSARIAL,
    MAX_TOKENS_DECOMPOSER,
    MAX_TOKENS_INVESTIGATOR,
    MAX_TOKENS_QUANTIFIER,
    MAX_TOKENS_SYNTHESIZER,
    MAX_TOKENS_VERIFIER,
    OPUS_MODEL,
    PRICING,
    PROMPTS_DIR,
    RESULTS_DIR,
    SONNET_MODEL,
    VERIFIER_BATCH_SIZE,
    get_verifier_settings,
)
from pipeline.schemas import (
    CandidateCritique,
    DebatedCritique,
    DecomposerOutput,
    InvestigationThread,
    PipelineStats,
    QuantifiedCritique,
    VerifiedCritique,
)

logger = logging.getLogger("pipeline")

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)


# ---------------------------------------------------------------------------
# API utilities
# ---------------------------------------------------------------------------


def call_api(
    model: str,
    system: str,
    user_message: str,
    stats: PipelineStats,
    stage: str,
    max_tokens: int,
    tools: list[dict[str, Any]] | None = None,
) -> str:
    """Call Anthropic API with retries and cost tracking. Returns text response."""
    last_error: Exception | None = None
    for attempt in range(MAX_RETRIES + 1):
        try:
            kwargs: dict[str, Any] = {
                "model": model,
                "max_tokens": max_tokens,
                "system": system,
                "messages": [{"role": "user", "content": user_message}],
            }
            if tools:
                kwargs["tools"] = tools
            response = client.messages.create(**kwargs)

            # Extract text blocks
            text_parts: list[str] = []
            for block in response.content:
                if hasattr(block, "text"):
                    text_parts.append(block.text)
            text = "\n".join(text_parts)

            input_tokens = response.usage.input_tokens
            output_tokens = response.usage.output_tokens
            cost = stats.record_call(stage, model, input_tokens, output_tokens, PRICING)
            logger.info(
                "[%s] %s | %d in / %d out | $%.4f | cumulative $%.4f",
                stage,
                model,
                input_tokens,
                output_tokens,
                cost,
                stats.total_cost,
            )
            if stats.total_cost > stats.cost_warning_threshold:
                logger.warning(
                    "Cumulative cost $%.2f exceeds warning threshold $%.2f",
                    stats.total_cost,
                    stats.cost_warning_threshold,
                )
            return text

        except (anthropic.RateLimitError, anthropic.APIError) as exc:
            last_error = exc
            if attempt < MAX_RETRIES:
                wait = 2 ** (attempt + 1)
                logger.warning(
                    "[%s] API error (attempt %d/%d), retrying in %ds: %s",
                    stage,
                    attempt + 1,
                    MAX_RETRIES + 1,
                    wait,
                    exc,
                )
                time.sleep(wait)
            else:
                raise

    # Should not reach here, but satisfy type checker
    raise last_error  # type: ignore[misc]


def load_prompt(filename: str) -> str:
    """Load prompt from prompts/ directory."""
    path = PROMPTS_DIR / filename
    return path.read_text(encoding="utf-8")


def save_stage_output(
    intervention: str,
    stage_num: int,
    stage_name: str,
    data: Any,
    raw_text: str,
) -> None:
    """Save JSON + markdown to results/{intervention}/."""
    out_dir = RESULTS_DIR / intervention
    out_dir.mkdir(parents=True, exist_ok=True)

    prefix = f"{stage_num:02d}-{stage_name}"

    # JSON
    json_path = out_dir / f"{prefix}.json"
    if hasattr(data, "to_dict"):
        json_data = data.to_dict()
    elif isinstance(data, list):
        json_data = [
            item.to_dict() if hasattr(item, "to_dict") else item for item in data
        ]
    else:
        json_data = data
    json_path.write_text(json.dumps(json_data, indent=2, default=str), encoding="utf-8")

    # Markdown (raw API response)
    md_path = out_dir / f"{prefix}.md"
    md_path.write_text(raw_text, encoding="utf-8")

    logger.info("Saved stage output to %s (.json + .md)", prefix)


def fetch_web_content(url: str, stats: PipelineStats) -> str:
    """Fetch web content using Anthropic API with web search tool.

    Uses a simple prompt to retrieve and return page content.
    This keeps us within the 4-dependency constraint (no requests library).
    """
    return call_api(
        model=SONNET_MODEL,
        system="You are a research assistant. Retrieve and return the full content from the requested URL. Return the content as-is, without commentary.",
        user_message=f"Please retrieve and return the full content from this URL: {url}",
        stats=stats,
        stage="fetch_web",
        max_tokens=8192,
        tools=[{"type": "web_search_20250305", "name": "web_search"}],
    )


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------


def _extract_section(text: str, header: str, next_headers: list[str]) -> str:
    """Extract content between a header and the next header in next_headers.

    Uses loose regex matching with optional colon and whitespace.
    Headers are matched at the start of a line, optionally preceded by
    markdown heading markers (# / ## / ###) or bold markers (**).
    """
    # Match header at line start with optional markdown prefix
    pattern = r"^[\s#*]*" + re.escape(header) + r"\s*:?\s*"
    match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
    if not match:
        return ""

    start = match.end()

    # Find the earliest next header (must also be at line start)
    end = len(text)
    for nh in next_headers:
        nh_pattern = r"^[\s#*]*" + re.escape(nh) + r"\s*:?\s*"
        nh_match = re.search(nh_pattern, text[start:], re.IGNORECASE | re.MULTILINE)
        if nh_match:
            end = min(end, start + nh_match.start())

    return text[start:end].strip()


def _split_on_pattern(text: str, pattern: str) -> list[tuple[str, str]]:
    """Split text on a regex pattern, returning (title, body) tuples."""
    matches = list(re.finditer(pattern, text, re.IGNORECASE))
    results: list[tuple[str, str]] = []
    for i, m in enumerate(matches):
        title = m.group(1).strip() if m.lastindex else ""
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        results.append((title, body))
    return results


# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------


DECOMPOSER_THREAD_HEADERS = [
    "SCOPE",
    "KEY PARAMETERS",
    "WHAT GIVEWELL ALREADY ACCOUNTS FOR",
    "WHAT GIVEWELL DOES NOT ACCOUNT FOR",
    "DATA SOURCES TO EXAMINE",
    "MATERIALITY THRESHOLD",
    "KNOWN CONCERNS ALREADY SURFACED",
]


def parse_decomposer_output(text: str) -> DecomposerOutput:
    """Parse decomposer API response into DecomposerOutput."""
    # Split into thread sections
    thread_splits = _split_on_pattern(text, r"THREAD\s+\d+\s*:\s*(.+?)(?:\n|$)")

    threads: list[InvestigationThread] = []
    all_exclusions: list[str] = []
    all_parameters: list[str] = []

    for thread_name, thread_body in thread_splits:
        sections: dict[str, str] = {}
        for i, header in enumerate(DECOMPOSER_THREAD_HEADERS):
            remaining = DECOMPOSER_THREAD_HEADERS[i + 1:] + [
                "THREAD",
                "DEPENDENCY MAP",
                "RECOMMENDED SEQUENCING",
            ]
            sections[header] = _extract_section(thread_body, header, remaining)

        scope = sections.get("SCOPE", "")
        key_params_raw = sections.get("KEY PARAMETERS", "")
        already_accounts = sections.get("WHAT GIVEWELL ALREADY ACCOUNTS FOR", "")
        not_account = sections.get("WHAT GIVEWELL DOES NOT ACCOUNT FOR", "")
        data_sources_raw = sections.get("DATA SOURCES TO EXAMINE", "")
        materiality = sections.get("MATERIALITY THRESHOLD", "")
        known_concerns = sections.get("KNOWN CONCERNS ALREADY SURFACED", "")

        # Parse bullet lists
        key_params = [
            line.strip().lstrip("-•* ").strip()
            for line in key_params_raw.splitlines()
            if line.strip() and line.strip().lstrip("-•* ").strip()
        ]
        data_sources = [
            line.strip().lstrip("-•* ").strip()
            for line in data_sources_raw.splitlines()
            if line.strip() and line.strip().lstrip("-•* ").strip()
        ]
        exclusion_items = [
            line.strip().lstrip("-•* ").strip()
            for line in known_concerns.splitlines()
            if line.strip() and line.strip().lstrip("-•* ").strip()
        ]

        all_exclusions.extend(exclusion_items)
        all_parameters.extend(key_params)

        # Build context_md for investigators
        context_md = f"# Thread: {thread_name}\n\n"
        context_md += f"## Scope\n{scope}\n\n"
        context_md += f"## Key Parameters\n{key_params_raw}\n\n"
        context_md += f"## What GiveWell Already Accounts For\n{already_accounts}\n\n"
        context_md += f"## What GiveWell Does Not Account For\n{not_account}\n\n"
        context_md += f"## Data Sources to Examine\n{data_sources_raw}\n\n"
        context_md += f"## Materiality Threshold\n{materiality}\n\n"
        context_md += f"## Known Concerns Already Surfaced\n{known_concerns}\n"

        out_of_scope = ""
        # Check for an out-of-scope note at the end
        oos_match = re.search(r"OUT\s+OF\s+SCOPE", thread_body, re.IGNORECASE)
        if oos_match:
            out_of_scope = thread_body[oos_match.end():].strip()

        thread = InvestigationThread(
            name=thread_name,
            scope=scope,
            key_questions=[not_account] if not_account else [],
            cea_parameters_affected=key_params,
            relevant_sources=data_sources,
            out_of_scope=out_of_scope,
            context_md=context_md,
        )
        threads.append(thread)

    # Build CEA parameter map from aggregated parameters
    cea_parameter_map = "\n".join(f"- {p}" for p in all_parameters) if all_parameters else ""

    # Deduplicate exclusion list
    seen: set[str] = set()
    unique_exclusions: list[str] = []
    for e in all_exclusions:
        lower = e.lower()
        if lower not in seen:
            seen.add(lower)
            unique_exclusions.append(e)

    return DecomposerOutput(
        threads=threads,
        exclusion_list=unique_exclusions,
        cea_parameter_map=cea_parameter_map,
    )


def parse_investigator_output(
    text: str, thread_name: str
) -> list[CandidateCritique]:
    """Parse investigator API response into list of CandidateCritique."""
    critique_splits = _split_on_pattern(text, r"CRITIQUE\s+\d+\s*:\s*(.+?)(?:\n|$)")

    critiques: list[CandidateCritique] = []
    inv_headers = [
        "HYPOTHESIS",
        "MECHANISM",
        "EVIDENCE",
        "STRENGTH",
        "NOVELTY CHECK",
        "SUMMARY",
        "RECOMMENDED VERIFICATION PRIORITIES",
        "CRITIQUE",
    ]

    for title, body in critique_splits:
        hypothesis = _extract_section(body, "HYPOTHESIS", inv_headers)
        mechanism = _extract_section(body, "MECHANISM", inv_headers)
        evidence_raw = _extract_section(body, "EVIDENCE", inv_headers)
        strength_raw = _extract_section(body, "STRENGTH", inv_headers)
        # novelty_check not stored in dataclass but parsed for completeness

        # Parse evidence as list of items
        evidence_items = [
            line.strip().lstrip("-•* ").strip()
            for line in evidence_raw.splitlines()
            if line.strip() and line.strip().lstrip("-•* ").strip()
        ]

        # Infer direction from mechanism text
        mech_lower = mechanism.lower()
        if any(w in mech_lower for w in ("lower", "reduc", "decreas", "overestimat")):
            direction = "decreases"
        elif any(w in mech_lower for w in ("higher", "increas", "underestimat", "raise")):
            direction = "increases"
        else:
            direction = "uncertain"

        # Map strength to magnitude
        strength_upper = strength_raw.upper().strip()
        if "HIGH" in strength_upper:
            magnitude = "large"
        elif "MEDIUM" in strength_upper:
            magnitude = "medium"
        elif "LOW" in strength_upper:
            magnitude = "small"
        else:
            magnitude = "unknown"

        # Extract parameter names by scanning for known keywords
        known_params = [
            "relative_risk",
            "internal_validity_under5",
            "internal_validity_over5",
            "external_validity",
            "plausibility_cap",
            "internal_validity_morbidity",
            "morbidity_ext_validity",
        ]
        param_keywords = {
            "relative risk": "relative_risk",
            "mortality effect": "relative_risk",
            "internal validity": "internal_validity_under5",
            "external validity": "external_validity",
            "plausibility cap": "plausibility_cap",
            "morbidity": "internal_validity_morbidity",
        }
        found_params: list[str] = []
        full_text_lower = (title + " " + mechanism + " " + hypothesis).lower()
        for keyword, param in param_keywords.items():
            if keyword in full_text_lower and param not in found_params:
                found_params.append(param)
        # Also check for direct parameter names
        for p in known_params:
            if p.replace("_", " ") in full_text_lower and p not in found_params:
                found_params.append(p)

        critiques.append(
            CandidateCritique(
                thread_name=thread_name,
                title=title,
                hypothesis=hypothesis,
                mechanism=mechanism,
                parameters_affected=found_params if found_params else ["unknown"],
                suggested_evidence=evidence_items,
                estimated_direction=direction,
                estimated_magnitude=magnitude,
            )
        )

    return critiques


def parse_verifier_output(
    text: str, original: CandidateCritique
) -> VerifiedCritique:
    """Parse verifier API response into VerifiedCritique."""
    ver_headers = [
        "CRITIQUE",
        "CITATION CHECK",
        "CLAIM CHECK",
        "EVIDENCE FOUND",
        "OVERALL VERDICT",
        "REVISED CRITIQUE",
    ]

    verdict_raw = _extract_section(text, "OVERALL VERDICT", ver_headers)
    evidence_raw = _extract_section(text, "EVIDENCE FOUND", ver_headers)
    revised_raw = _extract_section(text, "REVISED CRITIQUE", ver_headers)
    claim_check_raw = _extract_section(text, "CLAIM CHECK", ver_headers)

    # Map verdict
    verdict_upper = verdict_raw.upper()
    if "PARTIALLY" in verdict_upper:
        verdict = "partially_verified"
    elif "VERIFIED" in verdict_upper:
        verdict = "verified"
    elif "REJECTED" in verdict_upper:
        verdict = "unverified"
    else:
        # UNVERIFIABLE or anything else
        verdict = "unverified"

    # Parse evidence found as list
    evidence_items = [
        line.strip().lstrip("-•* ").strip()
        for line in evidence_raw.splitlines()
        if line.strip() and line.strip().lstrip("-•* ").strip()
    ]

    # Determine evidence strength from context
    evidence_lower = (evidence_raw + " " + claim_check_raw).lower()
    if any(
        w in evidence_lower
        for w in ("well-established", "strong evidence", "robust", "rct", "systematic review")
    ):
        evidence_strength = "strong"
    elif any(
        w in evidence_lower
        for w in ("plausible", "uncertain", "mixed", "limited", "suggestive", "moderate")
    ):
        evidence_strength = "moderate"
    else:
        evidence_strength = "weak"

    # Caveats from claim check
    caveats = [
        line.strip().lstrip("-•* ").strip()
        for line in claim_check_raw.splitlines()
        if line.strip() and line.strip().lstrip("-•* ").strip()
    ]

    # Clean up: the header often includes "(if partially verified):" — strip that
    revised_clean = re.sub(
        r"^\(if partially verified\)\s*:?\s*", "", revised_raw, flags=re.IGNORECASE
    ).strip()
    revised_hypothesis = revised_clean if revised_clean else None

    return VerifiedCritique(
        original=original,
        verdict=verdict,
        evidence_found=evidence_items,
        evidence_strength=evidence_strength,
        counter_evidence=[],
        caveats=caveats,
        revised_hypothesis=revised_hypothesis,
    )


# Parameter name mapping from API response text to compute_cost_effectiveness kwargs.
# Keys are matched with substring search against lowercased parameter names.
# More specific keys must come before less specific ones to avoid false matches.
_PARAM_NAME_MAP: dict[str, str] = {
    "ln(rr)": "relative_risk",
    "pooled ln": "relative_risk",
    "log relative risk": "relative_risk",
    "mortality reduction": "relative_risk",
    "relative risk": "relative_risk",
    "mortality effect": "relative_risk",
    "treatment effect": "relative_risk",
    "internal validity, under": "internal_validity_under5",
    "internal validity adjustment": "internal_validity_under5",
    "internal validity": "internal_validity_under5",
    "external validity": "external_validity",
    "plausibility cap": "plausibility_cap",
    "morbidity external validity": "morbidity_ext_validity",
    "morbidity ext validity": "morbidity_ext_validity",
    "morbidity": "internal_validity_morbidity",
    "mills-reincke": "mills_reincke",
    "mills reincke": "mills_reincke",
    "indirect mortality": "mills_reincke",
    # ITN-specific parameters
    "incidence reduction": "incidence_reduction",
    "malaria incidence reduction": "incidence_reduction",
    "insecticide resistance": "insecticide_resistance",
    "resistance adjustment": "insecticide_resistance",
    "indirect deaths multiplier": "indirect_deaths_multiplier",
    "indirect deaths": "indirect_deaths_multiplier",
    "indirect malaria": "indirect_deaths_multiplier",
    "moral weight under": "moral_weight_under5",
    "moral weight over": "moral_weight_over5",
    "moral weight, over": "moral_weight_over5",
    "moral weight, under": "moral_weight_under5",
    # SMC (Malaria) parameters
    "self-report bias": "self_report_bias",
    "self report bias": "self_report_bias",
    "reporting bias": "self_report_bias",
    "coverage adjustment": "self_report_bias",
    "adherence adjustment": "adherence_adjustment",
    "adherence": "adherence_adjustment",
    "drug adherence": "adherence_adjustment",
    "social desirability bias": "social_desirability_bias",
    "social desirability": "social_desirability_bias",
    "efficacy reduction": "efficacy_reduction",
    "non-adherence efficacy": "efficacy_reduction",
    "government cost": "govt_cost_fraction",
    "total spending": "total_spending",
    "total cost": "total_spending",
    "cost per cycle": "total_spending",
}


def _map_parameter_name(raw_name: str) -> str | None:
    """Map a human-readable parameter name to a compute_cost_effectiveness kwarg."""
    lower = raw_name.lower().strip()
    for key, value in _PARAM_NAME_MAP.items():
        if key in lower:
            return value
    return None


def _is_ln_rr_value(value: float) -> bool:
    """Check if a value looks like a ln(RR) (negative, small magnitude)."""
    return value < 0 and abs(value) < 1.0


def _extract_ranges_from_text(text: str) -> list[dict[str, Any]]:
    """Extract (parameter_name, low, current, high) from varied quantifier output.

    The API uses many formats, so we try multiple strategies:
    1. "Current value = X ... range = [Y, Z]" (original rigid pattern)
    2. "Current = X. Adjusted range = [Y, Z]" or "Plausible range = [Y, Z]"
    3. Named param blocks with values like "ln(RR) = -0.132 to -0.117"
    4. Bold-header blocks: "**Pooled ln(RR)**: Current -0.146 ... range ..."
    """
    results: list[dict[str, Any]] = []

    # Split into per-parameter blocks.  The API typically uses numbered items
    # (1. / 2. / - **Name**:) or double-newline separated paragraphs.
    # Split on numbered list items or bold headers.
    block_pattern = re.compile(
        r"(?:^|\n)\s*(?:\d+\.\s+|\-\s+)"
        r"(?:\*\*(.+?)\*\*)",
        re.MULTILINE,
    )
    block_matches = list(block_pattern.finditer(text))

    blocks: list[tuple[str, str]] = []
    for i, bm in enumerate(block_matches):
        name = bm.group(1).strip().rstrip(":.")
        start = bm.end()
        end = block_matches[i + 1].start() if i + 1 < len(block_matches) else len(text)
        body = text[start:end]
        blocks.append((name, body))

    # If no bold-header blocks found, treat the whole text as one block
    # and try to infer the parameter name from content
    if not blocks:
        blocks = [("", text)]

    # Matches a number (int, float, or percent) without consuming trailing
    # sentence periods.  "\d+(?:\.\d+)?" requires digits after the dot,
    # so "0.76." only captures "0.76".
    _NUM = r"-?\d+(?:\.\d+)?%?"

    for name, body in blocks:
        merged = name + " " + body
        # Determine the CEA parameter this block maps to
        mapped = _map_parameter_name(name) if name else None

        # Strategy 1: "Current value = X ... range = [Y, Z]" or
        # "Current = X ... Plausible range = [Y, Z]"
        m = re.search(
            r"Current\s*(?:value)?\s*[:=]\s*(" + _NUM + r")"
            r".*?(?:Plausible\s+)?[Rr]ange\s*[:=]?\s*\[?\s*(" + _NUM + r")"
            r"\s*[,to\-–]+\s*(" + _NUM + r")",
            merged, re.IGNORECASE | re.DOTALL,
        )
        if m:
            current = _parse_num(m.group(1))
            low = _parse_num(m.group(2))
            high = _parse_num(m.group(3))
            if current is not None and low is not None and high is not None:
                results.append({"name": name, "current": current, "low": low,
                                "high": high, "mapped": mapped})
                continue

        # Strategy 2: "could be X to Y" or "= X to Y" patterns with a parameter name
        m = re.search(
            r"(?:could\s+be|range\s*[:=]?|adjusted\s+(?:range|ln\(rr\))\s*[:=]?)"
            r"\s*\[?\s*(" + _NUM + r")\s*(?:to|[,\-–])\s*(" + _NUM + r")\s*\]?",
            merged, re.IGNORECASE,
        )
        if m and mapped:
            low = _parse_num(m.group(1))
            high = _parse_num(m.group(2))
            # Try to find current value nearby
            cm = re.search(
                r"Current(?:\s+value)?\s*[:=]\s*(" + _NUM + r")",
                merged, re.IGNORECASE,
            )
            current = _parse_num(cm.group(1)) if cm else None
            # If no explicit current, try to infer from "currently -0.146"
            if current is None:
                cm2 = re.search(r"[Cc]urrently\s+(" + _NUM + r")", merged)
                current = _parse_num(cm2.group(1)) if cm2 else None
            if current is not None and low is not None and high is not None:
                results.append({"name": name, "current": current, "low": low,
                                "high": high, "mapped": mapped})
                continue

        # Strategy 3: look for RR values like "RR = 0.95 ... RR = 0.90 ... RR = 0.92"
        rr_values = re.findall(r"RR\s*=\s*(" + _NUM + r")", merged, re.IGNORECASE)
        rr_parsed = [v for v in (_parse_num(r) for r in rr_values) if v is not None]
        if len(rr_parsed) >= 2 and (mapped or "relative risk" in merged.lower()
                                     or "mortality" in merged.lower()):
            vals = sorted(rr_parsed)
            if not mapped:
                mapped = "relative_risk"
            # Current RR from the CEA is ~0.864
            results.append({
                "name": name or "relative_risk",
                "current": rr_parsed[0],  # usually listed first
                "low": vals[0],
                "high": vals[-1],
                "mapped": mapped,
            })
            continue

        # Strategy 4: ln(RR) values like "ln(RR) = -0.132" or "ln(RR) could be..."
        lnrr_vals = re.findall(r"ln\s*\(?RR\)?\s*(?:=|could\s+be|:)\s*(" + _NUM + r")", merged, re.IGNORECASE)
        lnrr_parsed = [v for v in (_parse_num(r) for r in lnrr_vals) if v is not None]
        if len(lnrr_parsed) >= 2:
            vals = sorted(lnrr_parsed)
            results.append({
                "name": name or "ln(RR)",
                "current": lnrr_parsed[0],
                "low": vals[0],
                "high": vals[-1],
                "mapped": "relative_risk",
                "is_ln": True,
            })
            continue

    return results


def _parse_num(s: str) -> float | None:
    """Parse a number, handling optional % suffix (converted to fraction)."""
    s = s.strip().rstrip("%")
    try:
        val = float(s)
        # If original string had %, convert to fraction
        return val
    except ValueError:
        return None


def parse_quantifier_output(
    text: str,
    critique: VerifiedCritique,
    cea: Any,
) -> QuantifiedCritique:
    """Parse quantifier API response and run actual sensitivity analysis."""
    import math

    quant_headers = [
        "CRITIQUE",
        "PARAMETER MAPPING",
        "PLAUSIBLE RANGE",
        "SENSITIVITY ANALYSIS",
        "BOTTOM-LINE IMPACT",
        "MATERIALITY VERDICT",
        "CODE",
    ]

    param_mapping_raw = _extract_section(text, "PARAMETER MAPPING", quant_headers)
    plausible_range_raw = _extract_section(text, "PLAUSIBLE RANGE", quant_headers)
    materiality_raw = _extract_section(text, "MATERIALITY VERDICT", quant_headers)

    # --- Extract named parameters from PARAMETER MAPPING ---
    target_parameters: list[dict[str, Any]] = []
    # Look for bold markdown names: **Parameter Name** or numbered + bold
    bold_params = re.findall(
        r"\*\*(.+?)\*\*",
        param_mapping_raw,
    )
    seen_params: set[str] = set()
    for bp in bold_params:
        name = bp.strip().rstrip(":.")
        mapped = _map_parameter_name(name)
        if mapped and mapped not in seen_params:
            target_parameters.append({"name": name, "mapped": mapped})
            seen_params.add(mapped)
        elif name and not any(skip in name.lower() for skip in (
            "location", "role", "current", "note", "basis", "evidence",
        )):
            # Keep un-mappable but plausible parameter names for logging
            target_parameters.append({"name": name, "mapped": mapped})

    # If no bold names found, fall back to line-level extraction
    if not target_parameters:
        for line in param_mapping_raw.splitlines():
            line = line.strip().lstrip("-•*0123456789.) ")
            if not line:
                continue
            mapped = _map_parameter_name(line)
            if mapped and mapped not in seen_params:
                target_parameters.append({"name": line[:80], "mapped": mapped})
                seen_params.add(mapped)

    # --- Extract ranges from PLAUSIBLE RANGE ---
    extracted_ranges = _extract_ranges_from_text(plausible_range_raw)
    alternative_range: list[dict[str, Any]] = []
    for er in extracted_ranges:
        alternative_range.append(er)

    # If range extraction found nothing, try to match parameter names from
    # PARAMETER MAPPING against PLAUSIBLE RANGE to find any numbers
    if not alternative_range and target_parameters:
        for tp in target_parameters:
            mapped = tp.get("mapped")
            if not mapped:
                continue
            # Search PLAUSIBLE RANGE for any section mentioning this parameter
            param_name = tp.get("name", "")
            # Look for current value and any alternative values
            section_text = plausible_range_raw
            _NUM_FB = r"-?\d+(?:\.\d+)?%?"
            current_m = re.search(
                r"(?:Current|currently)\s*[:=]?\s*(" + _NUM_FB + r")",
                section_text, re.IGNORECASE,
            )
            if not current_m:
                continue
            current_parsed = _parse_num(current_m.group(1))
            if current_parsed is None:
                continue
            current = current_parsed
            # Find any other float values that could be alternatives
            all_floats = re.findall(r"(-?[\d]+\.[\d]+)", section_text)
            floats = sorted(set(float(f) for f in all_floats))
            if len(floats) >= 2:
                alternative_range.append({
                    "name": param_name,
                    "current": current,
                    "low": floats[0],
                    "high": floats[-1],
                    "mapped": mapped,
                })

    # Map materiality verdict
    mat_upper = materiality_raw.upper().strip()
    if "YES" in mat_upper:
        api_materiality = "material"
    elif "BORDERLINE" in mat_upper:
        api_materiality = "notable"
    else:
        api_materiality = "immaterial"

    # --- Run actual sensitivity analysis using CEA ---
    sensitivity_results: dict[str, Any] = {}
    max_abs_pct_change = 0.0

    for rng in alternative_range:
        mapped_param = rng.get("mapped") or _map_parameter_name(rng.get("name", ""))
        if not mapped_param:
            continue

        low_val = rng["low"]
        current_val = rng["current"]
        high_val = rng["high"]
        is_ln = rng.get("is_ln", False)

        # If this looks like ln(RR) values but the target param is relative_risk,
        # convert from log-space to linear-space.
        if mapped_param == "relative_risk":
            if is_ln or (_is_ln_rr_value(low_val) and _is_ln_rr_value(current_val)):
                low_val = math.exp(low_val)
                current_val = math.exp(current_val)
                high_val = math.exp(high_val)

        # Ensure low <= high
        if low_val > high_val:
            low_val, high_val = high_val, low_val

        for program_key in cea.PROGRAMS:
            try:
                result = cea.run_sensitivity(
                    program_key, mapped_param, low_val, current_val, high_val
                )
                key = f"{program_key}/{mapped_param}"
                sensitivity_results[key] = result
                # Track max absolute pct change
                for label in ("low", "central", "high"):
                    pct = abs(result.get(f"pct_change_{label}", 0.0))
                    max_abs_pct_change = max(max_abs_pct_change, pct)
            except Exception as exc:
                logger.warning(
                    "Sensitivity analysis failed for %s/%s: %s",
                    program_key,
                    mapped_param,
                    exc,
                )

    # Determine materiality from actual results
    if max_abs_pct_change >= 10.0:
        materiality = "material"
    elif max_abs_pct_change >= 1.0:
        materiality = "notable"
    else:
        # Fall back to API-reported materiality if no sensitivity ran
        materiality = api_materiality if not sensitivity_results else "immaterial"

    return QuantifiedCritique(
        critique=critique,
        target_parameters=target_parameters,
        alternative_range=alternative_range,
        sensitivity_results=sensitivity_results,
        materiality=materiality,
        interaction_effects=[],
    )


def parse_challenger_output(text: str) -> tuple[str, list[str], str]:
    """Parse adversarial challenger response.

    Returns (surviving_strength, key_unresolved_questions, recommended_action).
    """
    challenger_headers = [
        "REBUTTAL",
        "RESPONSE TO",
        "KEY UNRESOLVED QUESTIONS",
        "SURVIVING STRENGTH",
        "RECOMMENDED ACTION",
    ]

    strength_raw = _extract_section(text, "SURVIVING STRENGTH", challenger_headers)
    questions_raw = _extract_section(text, "KEY UNRESOLVED QUESTIONS", challenger_headers)
    action_raw = _extract_section(text, "RECOMMENDED ACTION", challenger_headers)

    # Parse surviving strength
    strength_lower = strength_raw.lower().strip()
    if "strong" in strength_lower:
        surviving_strength = "strong"
    elif "moderate" in strength_lower:
        surviving_strength = "moderate"
    else:
        surviving_strength = "weak"

    # Parse questions as list
    key_unresolved = [
        line.strip().lstrip("-•*0123456789.) ").strip()
        for line in questions_raw.splitlines()
        if line.strip() and line.strip().lstrip("-•*0123456789.) ").strip()
    ]

    # Parse recommended action
    action_lower = action_raw.lower().strip()
    if "investigate" in action_lower:
        recommended_action = "investigate"
    elif "adjust" in action_lower:
        recommended_action = "adjust_model"
    elif "monitor" in action_lower:
        recommended_action = "monitor"
    elif "dismiss" in action_lower:
        recommended_action = "dismiss"
    else:
        recommended_action = action_raw.strip()

    return surviving_strength, key_unresolved, recommended_action


# ---------------------------------------------------------------------------
# Stage runners
# ---------------------------------------------------------------------------


def run_decomposer(
    intervention_report: str,
    cea_summary: str,
    baseline_output: str,
    stats: PipelineStats,
    intervention: str,
) -> tuple[DecomposerOutput, str]:
    """Stage 1: Decompose the intervention into investigation threads."""
    system = load_prompt("decomposer.md")
    user_message = (
        "## Intervention Report\n\n"
        f"{intervention_report}\n\n"
        "## CEA Parameter Summary\n\n"
        f"{cea_summary}\n\n"
        "## Baseline AI Output (for exclusion list)\n\n"
        f"{baseline_output}"
    )

    raw = call_api(
        model=OPUS_MODEL,
        system=system,
        user_message=user_message,
        stats=stats,
        stage="decomposer",
        max_tokens=MAX_TOKENS_DECOMPOSER,
    )

    result = parse_decomposer_output(raw)
    save_stage_output(intervention, 1, "decomposer", result, raw)
    return result, raw


def run_investigators(
    threads: list[InvestigationThread],
    exclusion_list: list[str],
    stats: PipelineStats,
    intervention: str,
) -> tuple[list[CandidateCritique], str]:
    """Stage 2: Run investigators on each thread sequentially."""
    system_template = load_prompt("investigator-template.md")
    all_critiques: list[CandidateCritique] = []
    all_raw: list[str] = []

    exclusion_text = "\n".join(f"- {e}" for e in exclusion_list)

    for i, thread in enumerate(threads):
        # Check for placeholder in template
        if "{{CONTEXT_MD}}" in system_template:
            system = system_template.replace("{{CONTEXT_MD}}", thread.context_md)
        else:
            system = system_template

        user_message = (
            "## Your Thread Assignment\n\n"
            f"{thread.context_md}\n\n"
            "## Exclusion List (do NOT re-raise these)\n\n"
            f"{exclusion_text}\n\n"
            "Generate 3-6 candidate critiques within this thread's scope."
        )

        raw = call_api(
            model=SONNET_MODEL,
            system=system,
            user_message=user_message,
            stats=stats,
            stage=f"investigator-{i + 1}",
            max_tokens=MAX_TOKENS_INVESTIGATOR,
        )

        critiques = parse_investigator_output(raw, thread.name)
        all_critiques.extend(critiques)
        all_raw.append(f"--- Thread: {thread.name} ---\n\n{raw}")

    combined_raw = "\n\n".join(all_raw)
    save_stage_output(intervention, 2, "investigators", all_critiques, combined_raw)
    return all_critiques, combined_raw


def _format_critique_for_verifier(critique: CandidateCritique, index: int) -> str:
    """Format a single critique as a numbered block for the verifier prompt."""
    return (
        f"### Critique {index}\n\n"
        f"**Title:** {critique.title}\n"
        f"**Thread:** {critique.thread_name}\n"
        f"**Hypothesis:** {critique.hypothesis}\n"
        f"**Mechanism:** {critique.mechanism}\n"
        f"**Suggested Evidence:** {', '.join(critique.suggested_evidence)}\n"
        f"**Estimated Direction:** {critique.estimated_direction}\n"
        f"**Estimated Magnitude:** {critique.estimated_magnitude}\n"
    )


def _parse_batched_verifier_output(
    raw: str,
    batch: list[CandidateCritique],
) -> list[VerifiedCritique]:
    """Parse verifier output that may contain multiple critiques.

    Splits on 'Critique N' or '--- Critique' boundaries, then parses each.
    Falls back to treating the entire response as a single critique.
    """
    # Split on section boundaries matching "## Critique 1:", "### Critique 2:", etc.
    split_pattern = re.compile(
        r"(?:^|\n)\s*#{1,3}\s*Critique\s+(\d+)\s*[:\-]",
        re.IGNORECASE | re.MULTILINE,
    )
    matches = list(split_pattern.finditer(raw))

    results: list[VerifiedCritique] = []

    if len(matches) >= 2 and len(batch) > 1:
        # Multiple sections found — parse each
        seen_indices: set[int] = set()
        for i, m in enumerate(matches):
            critique_idx = int(m.group(1)) - 1
            if critique_idx in seen_indices:
                # Model restated the header in a summary section; skip duplicate
                continue
            seen_indices.add(critique_idx)
            start = m.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(raw)
            section = raw[start:end].strip()

            if 0 <= critique_idx < len(batch):
                result = parse_verifier_output(section, batch[critique_idx])
                results.append(result)
    else:
        # Single critique or can't split — parse as one
        # If batch has multiple, attempt splitting on "---" delimiters
        if len(batch) > 1:
            parts = re.split(r"\n---+\s*\n", raw)
            for j, part in enumerate(parts):
                if j < len(batch):
                    result = parse_verifier_output(part.strip(), batch[j])
                    results.append(result)
        else:
            result = parse_verifier_output(raw, batch[0])
            results.append(result)

    return results


def run_verifier(
    critiques: list[CandidateCritique],
    stats: PipelineStats,
    intervention: str,
) -> tuple[list[VerifiedCritique], str]:
    """Stage 3: Verify each critique with web search.

    Uses batching, search count limits, and domain focusing to reduce costs.
    """
    system = load_prompt("verifier.md")
    verified: list[VerifiedCritique] = []
    all_raw: list[str] = []

    settings = get_verifier_settings(intervention)
    web_search_tool: dict[str, Any] = {
        "type": "web_search_20250305",
        "name": "web_search",
        "max_uses": settings["max_searches"],
        "allowed_domains": settings["allowed_domains"],
    }

    # Process in batches
    batch_num = 0
    for start in range(0, len(critiques), VERIFIER_BATCH_SIZE):
        batch = critiques[start : start + VERIFIER_BATCH_SIZE]
        batch_num += 1

        if len(batch) == 1:
            user_message = (
                f"## Critique to Verify\n\n"
                + _format_critique_for_verifier(batch[0], 1)
                + "\nVerify this critique. Check citations, claims, and evidence."
            )
        else:
            critique_blocks = "\n\n".join(
                _format_critique_for_verifier(c, j + 1)
                for j, c in enumerate(batch)
            )
            user_message = (
                f"## Critiques to Verify\n\n"
                f"Verify each of the following {len(batch)} critiques. "
                f"For EACH critique, provide a separate section headed "
                f"'## Critique N:' with OVERALL VERDICT, EVIDENCE FOUND, "
                f"CLAIM CHECK, and (if partially verified) REVISED CRITIQUE.\n\n"
                + critique_blocks
            )

        raw = call_api(
            model=SONNET_MODEL,
            system=system,
            user_message=user_message,
            stats=stats,
            stage=f"verifier-{batch_num}",
            max_tokens=settings["max_tokens"] * len(batch),
            tools=[web_search_tool],
        )

        results = _parse_batched_verifier_output(raw, batch)

        for result in results:
            title = result.original.title
            all_raw.append(f"--- Critique: {title} ---\n\n{raw}")
            if result.verdict in ("verified", "partially_verified"):
                verified.append(result)
            else:
                logger.info(
                    "Dropping critique '%s': verdict=%s", title, result.verdict
                )

    combined_raw = "\n\n".join(all_raw)
    save_stage_output(intervention, 3, "verifier", verified, combined_raw)
    return verified, combined_raw


def run_quantifier(
    critiques: list[VerifiedCritique],
    cea: Any,
    cea_parameter_map: str,
    stats: PipelineStats,
    intervention: str,
) -> tuple[list[QuantifiedCritique], str]:
    """Stage 4: Quantify impact of each verified critique."""
    system = load_prompt("quantifier.md")
    quantified: list[QuantifiedCritique] = []
    all_raw: list[str] = []

    cea_summary = cea.get_parameter_summary()

    for i, critique in enumerate(critiques):
        orig = critique.original
        user_message = (
            f"## Critique to Quantify\n\n"
            f"**Title:** {orig.title}\n"
            f"**Hypothesis:** {critique.revised_hypothesis or orig.hypothesis}\n"
            f"**Mechanism:** {orig.mechanism}\n"
            f"**Verdict:** {critique.verdict}\n"
            f"**Evidence Strength:** {critique.evidence_strength}\n"
            f"**Evidence Found:**\n"
            + "\n".join(f"- {e}" for e in critique.evidence_found)
            + f"\n\n## CEA Parameter Map\n\n{cea_parameter_map}\n\n"
            f"## CEA Parameter Summary\n\n{cea_summary}\n\n"
            "Quantify the impact. Map to specific parameters, provide plausible ranges, "
            "and assess materiality."
        )

        raw = call_api(
            model=OPUS_MODEL,
            system=system,
            user_message=user_message,
            stats=stats,
            stage=f"quantifier-{i + 1}",
            max_tokens=MAX_TOKENS_QUANTIFIER,
        )

        result = parse_quantifier_output(raw, critique, cea)
        logger.info(
            "  Quantifier [%d/%d] '%s': params=%d, ranges=%d, sensitivity=%d, materiality=%s",
            i + 1,
            len(critiques),
            orig.title[:50],
            len(result.target_parameters),
            len(result.alternative_range),
            len(result.sensitivity_results),
            result.materiality,
        )
        if result.sensitivity_results:
            for key, sens in result.sensitivity_results.items():
                logger.info(
                    "    %s: baseline=%.2f, low=%.2f (%.1f%%), high=%.2f (%.1f%%)",
                    key,
                    sens["baseline"],
                    sens["low"],
                    sens["pct_change_low"],
                    sens["high"],
                    sens["pct_change_high"],
                )
        quantified.append(result)
        all_raw.append(f"--- Critique: {orig.title} ---\n\n{raw}")

    combined_raw = "\n\n".join(all_raw)
    save_stage_output(intervention, 4, "quantifier", quantified, combined_raw)
    return quantified, combined_raw


def _extract_relevant_report_sections(report: str, max_chars: int = 8000) -> str:
    """Extract relevant sections from intervention report.

    Looks for section headers related to key CEA topics. Falls back to
    first max_chars characters if no headers found.
    """
    section_keywords = [
        "mortality",
        "internal validity",
        "external validity",
        "how we incorporate",
        "adjustments",
        "effect size",
        "morbidity",
        "cost-effectiveness",
    ]

    # Try to find markdown sections (## headers)
    sections: list[str] = []
    header_pattern = re.compile(r"^(#{1,3}\s+.+)$", re.MULTILINE)
    headers = list(header_pattern.finditer(report))

    if headers:
        for i, hdr in enumerate(headers):
            header_text = hdr.group(1).lower()
            if any(kw in header_text for kw in section_keywords):
                start = hdr.start()
                end = headers[i + 1].start() if i + 1 < len(headers) else len(report)
                sections.append(report[start:end].strip())

    if sections:
        result = "\n\n".join(sections)
        return result[:max_chars]

    # Fallback: return first max_chars
    return report[:max_chars]


def run_adversarial(
    critiques: list[QuantifiedCritique],
    intervention_report: str,
    cea_parameter_map: str,
    stats: PipelineStats,
    intervention: str,
) -> tuple[list[DebatedCritique], str]:
    """Stage 5: Adversarial debate for material/notable critiques."""
    advocate_prompt = load_prompt("adversarial-advocate.md")
    challenger_prompt = load_prompt("adversarial-challenger.md")
    all_raw: list[str] = []
    debated: list[DebatedCritique] = []

    # Extract relevant sections (FIX 6: don't truncate to 3000)
    report_sections = _extract_relevant_report_sections(intervention_report)

    for i, qcrit in enumerate(critiques):
        # Only debate material or notable critiques
        if qcrit.materiality not in ("material", "notable"):
            logger.info(
                "Skipping adversarial for '%s': materiality=%s",
                qcrit.critique.original.title,
                qcrit.materiality,
            )
            continue

        orig = qcrit.critique.original
        critique_summary = (
            f"**Title:** {orig.title}\n"
            f"**Hypothesis:** {qcrit.critique.revised_hypothesis or orig.hypothesis}\n"
            f"**Mechanism:** {orig.mechanism}\n"
            f"**Evidence:** {', '.join(qcrit.critique.evidence_found)}\n"
            f"**Materiality:** {qcrit.materiality}\n"
            f"**Sensitivity Results:** {json.dumps(qcrit.sensitivity_results, default=str)}"
        )

        # Step 1: Advocate defense
        advocate_user = (
            f"## Critique to Defend Against\n\n{critique_summary}\n\n"
            f"## Relevant Report Sections\n\n{report_sections}\n\n"
            f"## CEA Parameter Map\n\n{cea_parameter_map}\n\n"
            "Defend GiveWell's position against this critique."
        )

        advocate_raw = call_api(
            model=SONNET_MODEL,
            system=advocate_prompt,
            user_message=advocate_user,
            stats=stats,
            stage=f"advocate-{i + 1}",
            max_tokens=MAX_TOKENS_ADVERSARIAL,
        )

        # Step 2: Challenger rebuttal
        challenger_user = (
            f"## Original Critique\n\n{critique_summary}\n\n"
            f"## Advocate's Defense\n\n{advocate_raw}\n\n"
            f"## Evidence Found During Verification\n\n"
            + "\n".join(f"- {e}" for e in qcrit.critique.evidence_found)
            + "\n\nChallenge the advocate's defense."
        )

        challenger_raw = call_api(
            model=SONNET_MODEL,
            system=challenger_prompt,
            user_message=challenger_user,
            stats=stats,
            stage=f"challenger-{i + 1}",
            max_tokens=MAX_TOKENS_ADVERSARIAL,
        )

        # Parse challenger output
        surviving_strength, key_unresolved, recommended_action = parse_challenger_output(
            challenger_raw
        )

        debated.append(
            DebatedCritique(
                critique=qcrit,
                advocate_defense=advocate_raw,
                challenger_rebuttal=challenger_raw,
                surviving_strength=surviving_strength,
                key_unresolved=key_unresolved,
                recommended_action=recommended_action,
            )
        )

        all_raw.append(
            f"--- Critique: {orig.title} ---\n\n"
            f"### Advocate\n{advocate_raw}\n\n"
            f"### Challenger\n{challenger_raw}"
        )

    combined_raw = "\n\n".join(all_raw)
    save_stage_output(intervention, 5, "adversarial", debated, combined_raw)
    return debated, combined_raw


def run_synthesizer(
    debated: list[DebatedCritique],
    all_critiques_count: int,
    verified_count: int,
    baseline_output: str,
    stats: PipelineStats,
    intervention: str,
) -> str:
    """Stage 6: Synthesize final report."""
    system = load_prompt("synthesizer.md")

    # Compile critique data
    critique_summaries: list[str] = []
    for dc in debated:
        orig = dc.critique.critique.original
        critique_summaries.append(
            f"### {orig.title}\n"
            f"- **Surviving Strength:** {dc.surviving_strength}\n"
            f"- **Recommended Action:** {dc.recommended_action}\n"
            f"- **Hypothesis:** {dc.critique.critique.revised_hypothesis or orig.hypothesis}\n"
            f"- **Mechanism:** {orig.mechanism}\n"
            f"- **Evidence:** {', '.join(dc.critique.critique.evidence_found)}\n"
            f"- **Evidence Strength:** {dc.critique.critique.evidence_strength}\n"
            f"- **Materiality:** {dc.critique.materiality}\n"
            f"- **Sensitivity Results:** {json.dumps(dc.critique.sensitivity_results, default=str)}\n"
            f"- **Key Unresolved Questions:** {', '.join(dc.key_unresolved)}\n"
            f"- **Advocate Defense Summary:** {dc.advocate_defense[:500]}...\n"
            f"- **Challenger Rebuttal Summary:** {dc.challenger_rebuttal[:500]}...\n"
        )

    user_message = (
        f"## Pipeline Statistics\n\n"
        f"- Candidate critiques generated: {all_critiques_count}\n"
        f"- Verified critiques: {verified_count}\n"
        f"- Critiques surviving adversarial review: {len(debated)}\n\n"
        f"## Surviving Critiques\n\n"
        + "\n".join(critique_summaries)
        + f"\n\n## Baseline AI Output (for comparison)\n\n{baseline_output}\n\n"
        "Produce the final red team report."
    )

    raw = call_api(
        model=OPUS_MODEL,
        system=system,
        user_message=user_message,
        stats=stats,
        stage="synthesizer",
        max_tokens=MAX_TOKENS_SYNTHESIZER,
    )

    save_stage_output(intervention, 6, "synthesizer", {"report": raw}, raw)
    return raw
