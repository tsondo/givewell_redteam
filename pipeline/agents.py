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
import httpx

from pipeline.config import (
    ANTHROPIC_API_KEY,
    MAX_RETRIES,
    MAX_TOKENS_ADVERSARIAL,
    MAX_TOKENS_DECOMPOSER,
    MAX_TOKENS_INVESTIGATOR,
    MAX_TOKENS_JUDGE,
    MAX_TOKENS_LINKER,
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
    CritiqueDependency,
    DebatedCritique,
    DecomposerOutput,
    InvestigationThread,
    JudgeAudit,
    LinkerOutput,
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
    timeout: httpx.Timeout | None = None,
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
            if timeout is not None:
                kwargs["timeout"] = timeout
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


def _strip_orphan_bold(value: str) -> str:
    """Strip orphan bold markers (** or ***) from start and end of a value."""
    value = re.sub(r"^(?:\*{2,3}\s*)+", "", value)
    value = re.sub(r"(?:\s*\*{2,3})+$", "", value)
    return value.strip()


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

    return _strip_orphan_bold(text[start:end].strip())


def _split_on_pattern(text: str, pattern: str) -> list[tuple[str, str]]:
    """Split text on a regex pattern, returning (title, body) tuples."""
    matches = list(re.finditer(pattern, text, re.IGNORECASE))
    results: list[tuple[str, str]] = []
    for i, m in enumerate(matches):
        title = _strip_orphan_bold(m.group(1).strip()) if m.lastindex else ""
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
        key_params = _parse_bullet_list(key_params_raw)
        data_sources = _parse_bullet_list(data_sources_raw)
        exclusion_items = _parse_bullet_list(known_concerns)

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
        evidence_items = _parse_bullet_list(evidence_raw)

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


_BULLET_RE = re.compile(r"^\s*[-•*]\s+|^\s*\d+\.\s+")
_FRAGMENT_RE = re.compile(
    r"^\s*[.,;:]\s*(?:However,?)?\s*$"          # bare punctuation / ". However,"
    r"|^\s*(?:Evidence|Claim|Note|Additionally)\s*[:,.]?\s*$"  # structural markers
    r"|^\s*(?:and|or|but)\s*$",                  # bare conjunctions
    re.IGNORECASE,
)


def _is_continuation(stripped: str) -> bool:
    """Return True if a line is a continuation of the previous item.

    Catches: bare punctuation (``'.'``), transitions (``'. However,'``),
    structural markers (``'Evidence:'``), and wrapped text that starts
    with lowercase or leading punctuation (``', showing mixed results.'``).
    """
    if _FRAGMENT_RE.match(stripped):
        return True
    if len(stripped) < 15 and not re.search(r"[a-zA-Z]{5,}", stripped):
        return True
    # Starts with sentence/clause punctuation — continuation
    if stripped[0] in ".,;":
        return True
    # Starts with lowercase — wrapped line after a line break
    if stripped[0].islower():
        return True
    return False


def _parse_bullet_list(raw: str) -> list[str]:
    """Parse LLM prose into bullet items, joining continuation lines.

    The verifier LLM often wraps evidence across multiple lines with
    sentence-ending punctuation or transitions ('. However,') on their
    own line.  A naive splitlines() treats these fragments as separate
    items.  This function:
      1. Lines with bullet markers (-, •, *, 1.) always start new items.
      2. Continuation lines (fragments, lowercase/punctuation starts) join
         the previous item.
      3. Other substantial lines start new items.
      4. Remaining trivial fragments are filtered in a final pass.
    """
    items: list[str] = []
    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if _BULLET_RE.match(line):
            # Bullet marker — always starts a new item
            content = stripped.lstrip("-•* ").strip()
            if content:
                items.append(content)
            # Empty bullet on its own line (e.g. "- \n") — skip; next
            # line will start a new item via the else branch below.
        elif items and _is_continuation(stripped):
            # Fragment or wrapped continuation — join to previous item
            items[-1] = items[-1] + " " + stripped
        else:
            # Substantial text without bullet marker — new item
            items.append(stripped)

    # Final pass: drop items that are still trivial after joining
    cleaned: list[str] = []
    for item in items:
        item = item.strip()
        if not item:
            continue
        if _FRAGMENT_RE.match(item):
            continue
        if len(item) < 15 and not re.search(r"[a-zA-Z]{5,}", item):
            continue
        cleaned.append(item)
    return cleaned


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
        verdict = "rejected"
    else:
        # UNVERIFIABLE or anything else
        verdict = "unverified"

    # Parse evidence found as list
    evidence_items = _parse_bullet_list(evidence_raw)

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
    caveats = _parse_bullet_list(claim_check_raw)

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

    NOTE: As of the judge-agent update, the Challenger prompt no longer emits
    SURVIVING STRENGTH or RECOMMENDED ACTION sections — those are produced by
    run_judge. This parser now extracts only KEY UNRESOLVED QUESTIONS from
    current Challenger outputs and returns advisory defaults for the other
    two fields. It's retained for backward compatibility with old 05-adversarial
    transcripts and for any ad-hoc analysis that still wants to peek at
    legacy challenger verdicts.
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

    # Parse surviving strength (advisory only — judge is authoritative)
    strength_lower = strength_raw.lower().strip()
    if "strong" in strength_lower:
        surviving_strength = "strong"
    elif "moderate" in strength_lower:
        surviving_strength = "moderate"
    elif strength_lower:
        surviving_strength = "weak"
    else:
        surviving_strength = ""  # new challenger format omits this

    # Parse questions as list
    key_unresolved = _parse_bullet_list(questions_raw)

    # Parse recommended action (advisory only — judge is authoritative)
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


def parse_advocate_self_assessment(text: str) -> str:
    """Extract the Advocate's OVERALL ASSESSMENT and normalize to strong|partial|weak.

    The Advocate prompt emits an OVERALL ASSESSMENT section rating the defense
    as "Strong defense", "Partial defense", or "Weak defense". We normalize to
    the lowercase one-word form for downstream use. Returns "" if the section
    is missing or unparseable (defensive — old runs may not have this).
    """
    advocate_headers = [
        "DEFENSE OF GIVEWELL",
        "EXISTING COVERAGE",
        "EVIDENCE WEAKNESSES",
        "MAGNITUDE CHALLENGE",
        "OFFSETTING FACTORS",
        "OVERALL ASSESSMENT",
        "CONCESSIONS",
    ]
    raw = _extract_section(text, "OVERALL ASSESSMENT", advocate_headers)
    if not raw:
        return ""
    lowered = raw.lower()
    # Check for "Strong/Partial/Weak defense" ordered by specificity
    if "strong" in lowered:
        return "strong"
    if "partial" in lowered:
        return "partial"
    if "weak" in lowered:
        return "weak"
    return ""


def parse_judge_output(text: str) -> JudgeAudit:
    """Parse the Judge agent's structured audit into a JudgeAudit dataclass.

    Expects the section headers defined in prompts/adversarial-judge.md:
    ADVOCATE FAILURES, CHALLENGER FAILURES, DEBATE RESOLVED, DEBATE UNRESOLVED,
    SURVIVING STRENGTH, RECOMMENDED ACTION. Tolerant of markdown prefixes and
    extra whitespace.
    """
    judge_headers = [
        "ADVOCATE FAILURES",
        "CHALLENGER FAILURES",
        "DEBATE RESOLVED",
        "DEBATE UNRESOLVED",
        "SURVIVING STRENGTH",
        "RECOMMENDED ACTION",
    ]

    advocate_raw = _extract_section(text, "ADVOCATE FAILURES", judge_headers)
    challenger_raw = _extract_section(text, "CHALLENGER FAILURES", judge_headers)
    resolved_raw = _extract_section(text, "DEBATE RESOLVED", judge_headers)
    unresolved_raw = _extract_section(text, "DEBATE UNRESOLVED", judge_headers)
    strength_raw = _extract_section(text, "SURVIVING STRENGTH", judge_headers)
    action_raw = _extract_section(text, "RECOMMENDED ACTION", judge_headers)

    advocate_failures = _parse_judge_failure_list(advocate_raw)
    challenger_failures = _parse_judge_failure_list(challenger_raw)

    # Surviving strength: first line is the verdict, remainder is the
    # "Justification:" prose.
    strength, justification = _split_strength_and_justification(strength_raw)

    # Recommended action: free text (full "CONCLUDE NOW: ..." or similar).
    # Extract action_feasibility if the judge emitted it as a trailing tag.
    recommended_action, action_feasibility = _split_action_and_feasibility(action_raw)

    return JudgeAudit(
        advocate_failures=advocate_failures,
        challenger_failures=challenger_failures,
        surviving_strength=strength,
        verdict_justification=justification,
        recommended_action=recommended_action,
        action_feasibility=action_feasibility,
        debate_resolved=resolved_raw.strip(),
        debate_unresolved=unresolved_raw.strip(),
    )


def _parse_judge_failure_list(raw: str) -> list[str]:
    """Parse a judge failure-list block into a list of 'failure_type: evidence' strings.

    The judge prompt specifies a bullet format like:
        - failure_type: whataboutism
          evidence: "The Challenger employs..."

    We pair each failure_type line with the nearest following evidence line
    and emit "type: evidence" for each pair. If the block contains only
    "(none detected)" or is empty, return an empty list.
    """
    stripped = raw.strip()
    if not stripped:
        return []
    # Handle explicit "(none detected)" marker (with or without parens, any case)
    if re.search(r"\(?\s*none\s+detected\s*\)?", stripped, re.IGNORECASE) and len(stripped) < 60:
        return []

    results: list[str] = []
    lines = stripped.splitlines()
    current_type: str | None = None
    for line in lines:
        stripped_line = line.strip().lstrip("-•*").strip()
        if not stripped_line:
            continue
        m_type = re.match(r"failure[_ ]type\s*:\s*(.+)", stripped_line, re.IGNORECASE)
        if m_type:
            # If we had a dangling type without evidence, emit it bare.
            if current_type is not None:
                results.append(current_type)
            current_type = m_type.group(1).strip().rstrip(",")
            continue
        m_ev = re.match(r"evidence\s*:\s*(.+)", stripped_line, re.IGNORECASE)
        if m_ev and current_type is not None:
            evidence = m_ev.group(1).strip().strip('"').strip("'")
            results.append(f"{current_type}: {evidence}")
            current_type = None
            continue
    # Flush any trailing bare type
    if current_type is not None:
        results.append(current_type)

    return results


def _split_strength_and_justification(raw: str) -> tuple[str, str]:
    """Split a SURVIVING STRENGTH block into (verdict, justification)."""
    if not raw.strip():
        return "weak", ""
    # Drop any markdown/bracket decorations from the first line
    lines = [ln for ln in raw.splitlines() if ln.strip()]
    if not lines:
        return "weak", ""
    first = lines[0].strip().lstrip("[").rstrip("]").strip()
    first_lower = first.lower()
    if "strong" in first_lower:
        verdict = "strong"
    elif "moderate" in first_lower:
        verdict = "moderate"
    elif "weak" in first_lower:
        verdict = "weak"
    else:
        verdict = "weak"  # defensive default

    # Justification: any text on subsequent lines, stripping a leading
    # "Justification:" label if present.
    justification_text = "\n".join(lines[1:]).strip()
    justification_text = re.sub(
        r"^justification\s*:\s*", "", justification_text, flags=re.IGNORECASE
    )
    return verdict, justification_text.strip()


def _split_action_and_feasibility(raw: str) -> tuple[str, str]:
    """Split a RECOMMENDED ACTION block into (action_text, feasibility_tag).

    The judge prompt asks for a trailing "action_feasibility: <tag>" line.
    If missing, infer from the CONCLUDE NOW / SPECIFIC INVESTIGATION /
    OPEN QUESTION prefix; default to "open_question".
    """
    text = raw.strip()
    if not text:
        return "", "open_question"

    # Try to split off a trailing "action_feasibility:" line
    feasibility = ""
    feas_match = re.search(
        r"^\s*action[_ ]feasibility\s*:\s*(actionable_now|requires_specified_evidence|open_question)\s*$",
        text,
        re.IGNORECASE | re.MULTILINE,
    )
    if feas_match:
        feasibility = feas_match.group(1).strip().lower().replace(" ", "_")
        # Remove the matched line from the action text
        text = (text[: feas_match.start()] + text[feas_match.end() :]).strip()

    if not feasibility:
        # Infer from prefix
        lowered = text.lower()
        if "conclude now" in lowered:
            feasibility = "actionable_now"
        elif "specific investigation" in lowered:
            feasibility = "requires_specified_evidence"
        else:
            feasibility = "open_question"

    return text, feasibility


def parse_linker_output(text: str) -> LinkerOutput:
    """Parse the Linker agent's structured output into a LinkerOutput.

    Expects the format defined in prompts/linker.md — a single "## DEPENDENCIES"
    section containing "### Dependency N" sub-blocks with key:value fields
    (surviving, rejected, verdict, relationship, confidence, justification).

    If the section contains "(none found)" (no Dependency blocks), returns an
    empty LinkerOutput. Blocks with invalid relationship, verdict, or missing
    titles are skipped with a warning rather than crashing the parser.

    The n_surviving_critiques_examined / n_rejected_critiques_available fields
    are set to 0 by this function; callers (run_linker) populate them from
    the true input counts before persisting.
    """
    dep_section = _extract_section(text, "DEPENDENCIES", [])
    empty = LinkerOutput(
        dependencies=[],
        n_surviving_critiques_examined=0,
        n_rejected_critiques_available=0,
        n_dependencies_found=0,
    )
    if not dep_section.strip():
        return empty

    # "(none found)" marker with no actual Dependency blocks -> empty result
    has_blocks = bool(
        re.search(r"(?im)^\s*#{2,}\s*Dependency\s+\d+", dep_section)
    )
    if not has_blocks:
        return empty

    # Split into blocks at "### Dependency N" headers. blocks[0] is any
    # preamble before the first header.
    blocks = re.split(
        r"(?im)^\s*#{2,}\s*Dependency\s+\d+\s*$",
        dep_section,
    )

    dependencies: list[CritiqueDependency] = []
    seen: set[tuple[str, str]] = set()
    for block in blocks[1:]:
        dep = _parse_dependency_block(block)
        if dep is None:
            continue
        # Deduplicate by (surviving, rejected) pair as a safety net
        key = (dep.surviving_critique_title, dep.rejected_critique_title)
        if key in seen:
            continue
        seen.add(key)
        dependencies.append(dep)

    return LinkerOutput(
        dependencies=dependencies,
        n_surviving_critiques_examined=0,
        n_rejected_critiques_available=0,
        n_dependencies_found=len(dependencies),
    )


def _parse_dependency_block(block: str) -> CritiqueDependency | None:
    """Parse a single Dependency block into a CritiqueDependency, or None if invalid.

    Returns None (with a warning log) when:
    - surviving or rejected title is missing
    - relationship is not one of {depends_on, engages_with, contradicts}
    - verdict is not one of {unverified, rejected}

    Confidence values outside {high, medium, low} default to "medium" (not
    a skip condition — the model occasionally emits variants like "med").
    """
    surviving = _extract_linker_field(block, "surviving")
    rejected = _extract_linker_field(block, "rejected")
    verdict = _extract_linker_field(block, "verdict").lower()
    relationship = _extract_linker_field(block, "relationship").lower()
    confidence = _extract_linker_field(block, "confidence").lower()
    justification = _extract_linker_field(block, "justification", multiline=True)

    if not surviving or not rejected:
        logger.warning(
            "Linker parser: skipping block with missing title(s): %r",
            block.strip()[:120],
        )
        return None
    if relationship not in {"depends_on", "engages_with", "contradicts"}:
        logger.warning(
            "Linker parser: skipping block with invalid relationship %r (surviving=%r)",
            relationship,
            surviving[:80],
        )
        return None
    if verdict not in {"unverified", "rejected"}:
        logger.warning(
            "Linker parser: skipping block with invalid verdict %r (surviving=%r)",
            verdict,
            surviving[:80],
        )
        return None
    if confidence not in {"high", "medium", "low"}:
        logger.warning(
            "Linker parser: confidence %r not in {high, medium, low}; defaulting to medium",
            confidence,
        )
        confidence = "medium"

    return CritiqueDependency(
        surviving_critique_title=surviving,
        rejected_critique_title=rejected,
        rejected_critique_verdict=verdict,
        relationship=relationship,
        justification=justification,
        confidence=confidence,
    )


def _extract_linker_field(block: str, field: str, multiline: bool = False) -> str:
    """Extract a 'field: value' line from a Dependency block.

    Tolerant of leading bullet markers (-, *, •) and bold markers (**field**).
    When multiline=True, continuation lines (non-empty lines that don't look
    like another key:value line) are appended with a single space separator.
    """
    lines = block.splitlines()
    pattern = re.compile(
        rf"^\s*[-*•]?\s*\*{{0,2}}\s*{re.escape(field)}\s*\*{{0,2}}\s*:\s*(.*?)\s*$",
        re.IGNORECASE,
    )
    next_field_pat = re.compile(
        r"^\s*[-*•]?\s*\*{0,2}\s*[a-z_ ]+\s*\*{0,2}\s*:",
        re.IGNORECASE,
    )
    for i, line in enumerate(lines):
        m = pattern.match(line)
        if m:
            value = m.group(1).strip()
            if multiline:
                for j in range(i + 1, len(lines)):
                    nxt = lines[j]
                    if not nxt.strip():
                        break
                    if next_field_pat.match(nxt):
                        break
                    value = (value + " " + nxt.strip()).strip()
            return value
    return ""


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


def _save_rejected_critiques(
    intervention: str, rejected: list[VerifiedCritique]
) -> None:
    """Save rejected critiques to 03-verifier-rejected.json (JSON only)."""
    out_dir = RESULTS_DIR / intervention
    out_dir.mkdir(parents=True, exist_ok=True)
    json_data = [r.to_dict() if hasattr(r, "to_dict") else r for r in rejected]
    path = out_dir / "03-verifier-rejected.json"
    path.write_text(json.dumps(json_data, indent=2, default=str), encoding="utf-8")
    logger.info(
        "Saved %d rejected critiques to %s", len(rejected), path.name
    )


def run_verifier(
    critiques: list[CandidateCritique],
    stats: PipelineStats,
    intervention: str,
) -> tuple[list[VerifiedCritique], list[VerifiedCritique], str]:
    """Stage 3: Verify each critique with web search.

    Uses batching, search count limits, and domain focusing to reduce costs.
    Returns (verified, rejected, raw_text).
    """
    system = load_prompt("verifier.md")
    verified: list[VerifiedCritique] = []
    rejected: list[VerifiedCritique] = []
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
                rejected.append(result)
                logger.info(
                    "Rejected critique '%s': verdict=%s", title, result.verdict
                )

    combined_raw = "\n\n".join(all_raw)
    save_stage_output(intervention, 3, "verifier", verified, combined_raw)
    _save_rejected_critiques(intervention, rejected)
    return verified, rejected, combined_raw


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


def run_judge(
    verified_critique: VerifiedCritique,
    advocate_raw: str,
    advocate_self_assessment: str,
    challenger_raw: str,
    stats: PipelineStats,
    intervention: str,
    index: int,
) -> JudgeAudit:
    """Stage 5b: Neutral judge evaluates Advocate vs Challenger exchange.

    Reads both sides plus the verifier evidence package and produces a
    structured audit (failure modes, verdict, recommended action). The
    judge's verdict SUPERSEDES any challenger-assigned verdict.
    """
    judge_prompt = load_prompt("adversarial-judge.md")
    orig = verified_critique.original

    # Format the verifier's evidence package (what was checked, what was
    # found, what was contradicted, caveats). The debaters only saw
    # `evidence_found`; the judge gets the full VerifiedCritique envelope.
    evidence_found_block = (
        "\n".join(f"- {e}" for e in verified_critique.evidence_found) or "(none)"
    )
    counter_evidence_block = (
        "\n".join(f"- {e}" for e in verified_critique.counter_evidence) or "(none)"
    )
    caveats_block = "\n".join(f"- {c}" for c in verified_critique.caveats) or "(none)"

    user_message = (
        "## Original Critique\n\n"
        f"**Title:** {orig.title}\n"
        f"**Hypothesis:** {verified_critique.revised_hypothesis or orig.hypothesis}\n"
        f"**Mechanism:** {orig.mechanism}\n\n"
        "## Verifier's Evidence Package\n\n"
        f"**Verdict:** {verified_critique.verdict}\n"
        f"**Evidence strength:** {verified_critique.evidence_strength}\n\n"
        f"**Evidence found:**\n{evidence_found_block}\n\n"
        f"**Counter-evidence / contradictions:**\n{counter_evidence_block}\n\n"
        f"**Caveats:**\n{caveats_block}\n\n"
        "## Advocate's Defense\n\n"
        f"{advocate_raw}\n\n"
        f"**Advocate's self-assessment of defense quality:** "
        f"{advocate_self_assessment or '(not stated)'}\n\n"
        "## Challenger's Rebuttal\n\n"
        f"{challenger_raw}\n\n"
        "---\n\n"
        "Audit this debate. Follow the output format in your system prompt "
        "exactly — the parser depends on the section headers ADVOCATE FAILURES, "
        "CHALLENGER FAILURES, DEBATE RESOLVED, DEBATE UNRESOLVED, SURVIVING "
        "STRENGTH, and RECOMMENDED ACTION."
    )

    judge_raw = call_api(
        model=OPUS_MODEL,
        system=judge_prompt,
        user_message=user_message,
        stats=stats,
        stage=f"judge-{index}",
        max_tokens=MAX_TOKENS_JUDGE,
    )

    return parse_judge_output(judge_raw)


def run_adversarial(
    critiques: list[QuantifiedCritique],
    intervention_report: str,
    cea_parameter_map: str,
    stats: PipelineStats,
    intervention: str,
) -> tuple[list[DebatedCritique], str]:
    """Stage 5: Adversarial debate for material/notable critiques.

    Three API calls per critique: Advocate (Sonnet) -> Challenger (Sonnet) ->
    Judge (Opus). The Judge assigns surviving_strength and recommended_action;
    the Challenger no longer does so.
    """
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

        advocate_self_assessment = parse_advocate_self_assessment(advocate_raw)

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

        # Step 3: Neutral judge. The judge produces the authoritative
        # verdict (surviving_strength) and recommended action, superseding
        # any such fields the Challenger may have emitted.
        judge_audit = run_judge(
            verified_critique=qcrit.critique,
            advocate_raw=advocate_raw,
            advocate_self_assessment=advocate_self_assessment,
            challenger_raw=challenger_raw,
            stats=stats,
            intervention=intervention,
            index=i + 1,
        )

        debated.append(
            DebatedCritique(
                critique=qcrit,
                advocate_defense=advocate_raw,
                challenger_rebuttal=challenger_raw,
                # Populated from judge audit. Legacy fields retained for
                # transcript / backward compatibility; judge_audit is the
                # structured source of truth going forward.
                surviving_strength=judge_audit.surviving_strength,
                key_unresolved=[],
                recommended_action=judge_audit.recommended_action,
                advocate_self_assessment=advocate_self_assessment,
                judge_audit=judge_audit,
            )
        )

        all_raw.append(
            f"--- Critique: {orig.title} ---\n\n"
            f"### Advocate\n{advocate_raw}\n\n"
            f"### Challenger\n{challenger_raw}\n\n"
            f"### Judge Audit\n"
            f"Surviving strength: {judge_audit.surviving_strength}\n"
            f"Justification: {judge_audit.verdict_justification}\n"
            f"Recommended action: {judge_audit.recommended_action}\n"
            f"Action feasibility: {judge_audit.action_feasibility}\n"
            f"Advocate failures: {judge_audit.advocate_failures}\n"
            f"Challenger failures: {judge_audit.challenger_failures}\n"
            f"Debate resolved: {judge_audit.debate_resolved}\n"
            f"Debate unresolved: {judge_audit.debate_unresolved}"
        )

    combined_raw = "\n\n".join(all_raw)
    save_stage_output(intervention, 5, "adversarial", debated, combined_raw)
    return debated, combined_raw


def _save_linker_artifact(
    intervention: str,
    linker_output: LinkerOutput,
    raw_text: str | None = None,
    short_circuited: bool = False,
) -> None:
    """Write 05b-linker.json and 05b-linker.md.

    Uses a non-standard "05b" numeric prefix to preserve the "06 always means
    synthesizer" invariant for historical continuity across results/ runs.
    This is the only stage that needs a non-sequential prefix; save_stage_output
    is not used to keep that helper clean.
    """
    out_dir = RESULTS_DIR / intervention
    out_dir.mkdir(parents=True, exist_ok=True)
    prefix = "05b-linker"

    json_path = out_dir / f"{prefix}.json"
    json_path.write_text(
        json.dumps(linker_output.to_dict(), indent=2, default=str),
        encoding="utf-8",
    )

    md_path = out_dir / f"{prefix}.md"
    if short_circuited:
        md_body = (
            "# Linker — zero-state (short-circuit)\n\n"
            "The Linker stage was short-circuited without an API call because one "
            "or both inputs were empty. No dependencies are possible when either "
            "side is empty. This empty artifact is written so `--resume-from "
            "synthesizer` loads a well-formed LinkerOutput.\n\n"
            f"- Surviving critiques examined: "
            f"{linker_output.n_surviving_critiques_examined}\n"
            f"- Rejected critiques available: "
            f"{linker_output.n_rejected_critiques_available}\n"
            f"- Dependencies found: {linker_output.n_dependencies_found}\n"
        )
    else:
        md_body = raw_text or ""
    md_path.write_text(md_body, encoding="utf-8")
    logger.info("Saved stage output to %s (.json + .md)", prefix)


def run_linker(
    surviving_critiques: list[DebatedCritique],
    rejected_critiques: list[VerifiedCritique],
    stats: PipelineStats,
    intervention: str,
) -> LinkerOutput:
    """Stage 5b: Linker identifies dependencies between surviving and rejected critiques.

    Produces a structured list of CritiqueDependency records. Runs as a
    separate stage (rather than inline in the synthesizer prompt) so the
    dependency-matching task is auditable on its own.

    Short-circuit: if either input is empty, no API call is made and a
    zero-state 05b-linker artifact is written to preserve resume-from
    consistency.
    """
    n_surviving = len(surviving_critiques)
    n_rejected = len(rejected_critiques)

    if n_surviving == 0 or n_rejected == 0:
        logger.info(
            "Linker short-circuit: surviving=%d, rejected=%d. No API call.",
            n_surviving,
            n_rejected,
        )
        result = LinkerOutput(
            dependencies=[],
            n_surviving_critiques_examined=n_surviving,
            n_rejected_critiques_available=n_rejected,
            n_dependencies_found=0,
        )
        _save_linker_artifact(intervention, result, short_circuited=True)
        return result

    system = load_prompt("linker.md")

    # Build the surviving critiques section. Include title, hypothesis (revised
    # when present), mechanism, and a compact judge audit summary — not the
    # full failure mode lists, which don't help the dependency-matching task.
    surviving_blocks: list[str] = []
    for dc in surviving_critiques:
        orig = dc.critique.critique.original
        hypothesis = dc.critique.critique.revised_hypothesis or orig.hypothesis
        if dc.judge_audit is not None:
            ja = dc.judge_audit
            audit_summary = (
                f"  - Surviving strength: {ja.surviving_strength}\n"
                f"  - Verdict justification: {ja.verdict_justification}\n"
                f"  - Debate resolved: {ja.debate_resolved}\n"
                f"  - Debate unresolved: {ja.debate_unresolved}"
            )
        else:
            # Legacy pre-judge records: fall back to whatever we have.
            audit_summary = (
                f"  - Surviving strength: {dc.surviving_strength} "
                f"(no judge audit available)"
            )
        surviving_blocks.append(
            f"### {orig.title}\n"
            f"- **Hypothesis:** {hypothesis}\n"
            f"- **Mechanism:** {orig.mechanism}\n"
            f"- **Judge audit:**\n{audit_summary}"
        )

    # Build the rejected critiques section. Include title, hypothesis,
    # mechanism, verdict, and the verifier's reasoning (caveats + evidence).
    rejected_blocks: list[str] = []
    for r in rejected_critiques:
        orig = r.original
        verdict_label = "UNVERIFIABLE" if r.verdict == "unverified" else "REJECTED"
        caveats_str = "\n".join(f"  - {c}" for c in r.caveats) or "  (none recorded)"
        evidence_str = "\n".join(f"  - {e}" for e in r.evidence_found) or "  (none)"
        rejected_blocks.append(
            f"### {orig.title}\n"
            f"- **Verdict:** {verdict_label} (schema field: `{r.verdict}`)\n"
            f"- **Hypothesis:** {r.revised_hypothesis or orig.hypothesis}\n"
            f"- **Mechanism:** {orig.mechanism}\n"
            f"- **What the verifier searched for / reasoning:**\n{caveats_str}\n"
            f"- **Evidence found:**\n{evidence_str}"
        )

    user_message = (
        "## Surviving Critiques\n\n"
        + "\n\n".join(surviving_blocks)
        + "\n\n## Rejected Critiques\n\n"
        + "\n\n".join(rejected_blocks)
        + "\n\n---\n\n"
        "Identify dependencies. Follow the output format in your system prompt "
        "exactly — the parser depends on the `## DEPENDENCIES` section, the "
        "`### Dependency N` sub-headers, and the key:value field lines. "
        "Use `verdict: unverified` or `verdict: rejected` (lowercase, no other forms)."
    )

    raw = call_api(
        model=SONNET_MODEL,
        system=system,
        user_message=user_message,
        stats=stats,
        stage="linker",
        max_tokens=MAX_TOKENS_LINKER,
    )

    parsed = parse_linker_output(raw)
    result = LinkerOutput(
        dependencies=parsed.dependencies,
        n_surviving_critiques_examined=n_surviving,
        n_rejected_critiques_available=n_rejected,
        n_dependencies_found=len(parsed.dependencies),
    )
    _save_linker_artifact(intervention, result, raw_text=raw)
    return result


def _format_rejected_critiques_for_synthesizer(
    rejected: list[VerifiedCritique],
) -> str:
    """Format rejected critiques as synthesizer input, split by verdict type."""
    unverifiable: list[str] = []
    contradicted: list[str] = []

    for r in rejected:
        orig = r.original
        evidence_str = "\n".join(f"  - {e}" for e in r.evidence_found) or "  (none)"
        caveats_str = "\n".join(f"  - {c}" for c in r.caveats) or "  (none)"

        entry = (
            f"#### {orig.title}\n"
            f"- **Hypothesis:** {r.revised_hypothesis or orig.hypothesis}\n"
            f"- **Mechanism:** {orig.mechanism}\n"
            f"- **What the verifier searched for:**\n{caveats_str}\n"
            f"- **Evidence found:**\n{evidence_str}\n"
        )

        if r.verdict == "rejected":
            contradicted.append(entry)
        else:
            unverifiable.append(entry)

    unverifiable_text = "\n".join(unverifiable) if unverifiable else "(none)\n"
    contradicted_text = "\n".join(contradicted) if contradicted else "(none)\n"

    return (
        "## Rejected Critiques (from verifier — DO NOT generate new entries)\n\n"
        "### Verdict: UNVERIFIABLE (no evidence found either way)\n\n"
        f"{unverifiable_text}\n"
        "### Verdict: REJECTED (contradicted by evidence)\n\n"
        f"{contradicted_text}"
    )


# Nine "real" failure mode types the judge may detect, excluding the
# positive marker sound_synthesis_noted (tracked separately). Order here
# is the order they appear in the synthesizer user message.
JUDGE_FAILURE_MODE_TYPES: list[str] = [
    "unsupported_estimate_fabricated",
    "unsupported_estimate_pseudo",
    "unsupported_estimate_counter",
    "whataboutism",
    "call_to_ignorance",
    "strawmanning",
    "false_definitiveness",
    "generic_recommendation",
    "misrepresenting_evidence_status",
]
_JUDGE_POSITIVE_MARKER = "sound_synthesis_noted"


def _compute_judge_audit_aggregate(
    debated: list[DebatedCritique],
) -> dict[str, Any]:
    """Compute aggregate failure-mode statistics from judge audits.

    Returns a dict with:
    - total_debates: int (debates with a judge audit present)
    - sound_synthesis_noted_count: int (the positive marker, across both sides)
    - failure_mode_counts: dict[str, int] combined across both sides, keyed
      by the nine real failure types (excluding sound_synthesis_noted)
    - failure_mode_counts_advocate / _challenger: per-side dicts
    - most_common_advocate_failure / _challenger_failure: str (or "(none)")

    The judge's failure lists store entries as "failure_type: evidence"
    strings; we split on the first colon to extract the type.
    """
    per_advocate: dict[str, int] = {t: 0 for t in JUDGE_FAILURE_MODE_TYPES}
    per_challenger: dict[str, int] = {t: 0 for t in JUDGE_FAILURE_MODE_TYPES}
    sound_count = 0
    total_debates = 0

    def _extract_type(entry: str) -> str:
        return entry.split(":", 1)[0].strip().lower()

    for dc in debated:
        if dc.judge_audit is None:
            continue
        total_debates += 1
        for entry in dc.judge_audit.advocate_failures:
            ftype = _extract_type(entry)
            if ftype == _JUDGE_POSITIVE_MARKER:
                sound_count += 1
            elif ftype in per_advocate:
                per_advocate[ftype] += 1
        for entry in dc.judge_audit.challenger_failures:
            ftype = _extract_type(entry)
            if ftype == _JUDGE_POSITIVE_MARKER:
                sound_count += 1
            elif ftype in per_challenger:
                per_challenger[ftype] += 1

    combined = {
        t: per_advocate[t] + per_challenger[t] for t in JUDGE_FAILURE_MODE_TYPES
    }

    def _most_common(counts: dict[str, int]) -> str:
        nonzero = {k: v for k, v in counts.items() if v > 0}
        if not nonzero:
            return "(none)"
        return max(nonzero, key=lambda k: nonzero[k])

    return {
        "total_debates": total_debates,
        "sound_synthesis_noted_count": sound_count,
        "failure_mode_counts": combined,
        "failure_mode_counts_advocate": per_advocate,
        "failure_mode_counts_challenger": per_challenger,
        "most_common_advocate_failure": _most_common(per_advocate),
        "most_common_challenger_failure": _most_common(per_challenger),
    }


def _build_synthesizer_user_message(
    debated: list[DebatedCritique],
    all_critiques_count: int,
    verified_count: int,
    rejected_critiques: list[VerifiedCritique],
    linker_output: LinkerOutput,
    decomposer_output: DecomposerOutput,
    baseline_output: str,
) -> str:
    """Construct the user message for the Synthesizer API call.

    Extracted as a standalone helper for testability: the synthesizer prompt
    contract (sections present, counts pre-computed, dependency formatting)
    can be validated without an API call.
    """
    thread_titles_block = (
        "\n".join(f"- {t.name}" for t in decomposer_output.threads) or "(none)"
    )

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

    # Compile rejected critique data, separated by verdict type
    rejected_section = _format_rejected_critiques_for_synthesizer(rejected_critiques)

    # Linker dependencies block. Show UNVERIFIABLE as the human-facing label
    # even though the schema value is "unverified".
    if not linker_output.dependencies:
        deps_block = "(no dependencies identified)"
    else:
        dep_lines: list[str] = []
        for d in linker_output.dependencies:
            verdict_label = (
                "UNVERIFIABLE" if d.rejected_critique_verdict == "unverified" else "REJECTED"
            )
            dep_lines.append(
                f"- surviving: {d.surviving_critique_title}\n"
                f"  rejected: {d.rejected_critique_title} (verdict: {verdict_label})\n"
                f"  relationship: {d.relationship} (confidence: {d.confidence})\n"
                f"  justification: {d.justification}"
            )
        deps_block = "\n".join(dep_lines)

    # Judge audit aggregate — pre-computed in Python, fed as text to the LLM.
    agg = _compute_judge_audit_aggregate(debated)
    failure_lines = "\n".join(
        f"  - {t}: {agg['failure_mode_counts'][t]}" for t in JUDGE_FAILURE_MODE_TYPES
    )
    aggregate_block = (
        f"- Total critiques debated: {agg['total_debates']}\n"
        f"- Sound syntheses noted: {agg['sound_synthesis_noted_count']}\n"
        f"- Failure mode counts (combined across both sides):\n"
        f"{failure_lines}\n"
        f"- Most common Advocate failure: {agg['most_common_advocate_failure']}\n"
        f"- Most common Challenger failure: {agg['most_common_challenger_failure']}"
    )

    n_threads = len(decomposer_output.threads)
    n_surviving = len(debated)
    n_rejected = len(rejected_critiques)
    n_deps = len(linker_output.dependencies)

    return (
        f"## Pipeline Summary\n\n"
        f"- Investigation threads examined: {n_threads}\n"
        f"- Candidate critiques generated: {all_critiques_count}\n"
        f"- Verified critiques: {verified_count}\n"
        f"- Rejected by verifier: {n_rejected}\n"
        f"- Critiques surviving adversarial review: {n_surviving}\n"
        f"- Dependencies identified: {n_deps}\n\n"
        f"## Decomposer Output (for accurate counts)\n\n"
        f"Investigation threads examined: {n_threads}\n\n"
        f"Thread titles:\n{thread_titles_block}\n\n"
        f"## Surviving Critiques (from adversarial stage)\n\n"
        + "\n".join(critique_summaries)
        + f"\n\n{rejected_section}"
        + f"\n\n## Critique Dependencies (from linker)\n\n"
        f"{deps_block}\n\n"
        f"## Judge Audit Aggregate (computed from surviving critiques)\n\n"
        f"{aggregate_block}\n\n"
        f"## Baseline AI Output (for comparison)\n\n{baseline_output}\n\n"
        "Produce the final red team report."
    )


def run_synthesizer(
    debated: list[DebatedCritique],
    all_critiques_count: int,
    verified_count: int,
    rejected_critiques: list[VerifiedCritique],
    linker_output: LinkerOutput,
    decomposer_output: DecomposerOutput,
    baseline_output: str,
    stats: PipelineStats,
    intervention: str,
) -> str:
    """Stage 6: Synthesize final report."""
    system = load_prompt("synthesizer.md")

    user_message = _build_synthesizer_user_message(
        debated=debated,
        all_critiques_count=all_critiques_count,
        verified_count=verified_count,
        rejected_critiques=rejected_critiques,
        linker_output=linker_output,
        decomposer_output=decomposer_output,
        baseline_output=baseline_output,
    )

    raw = call_api(
        model=OPUS_MODEL,
        system=system,
        user_message=user_message,
        stats=stats,
        stage="synthesizer",
        max_tokens=MAX_TOKENS_SYNTHESIZER,
        timeout=httpx.Timeout(600.0),
    )

    save_stage_output(intervention, 6, "synthesizer", {"report": raw}, raw)
    return raw
