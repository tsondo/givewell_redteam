#!/usr/bin/env python3
"""
Extract graph.json from pipeline stage outputs.

Reads stage JSON files from a pipeline results directory and produces
a graph.json conforming to the red_team_explorer schema v0.2.

Usage:
    python extract.py --input-dir results/vas --run-id vas-2026-04-13
    python extract.py --input-dir results/vas --run-id vas-2026-04-13 \
        --output-dir ../red_team_explorer/static/runs
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


SCHEMA_VERSION = "0.2"
PIPELINE_VERSION = "givewell_redteam@unknown"

STOP_WORDS = frozenset({
    "a", "an", "and", "at", "by", "for", "from", "in",
    "of", "on", "or", "the", "to", "vs", "with",
})

VERIFIER_CONFIDENCE = {
    "verified": 0.9,
    "partially_verified": 0.7,
    "unverified": 0.4,
    "rejected": 0.1,
}

STRENGTH_BASE = {"strong": 0.75, "moderate": 0.55, "weak": 0.35}
FINDING_CONFIDENCE = {"strong": 0.75, "moderate": 0.55, "weak": 0.25}

FAILURE_PENALTY = 0.1
FAILURE_PENALTY_CAP = 0.5

LINKER_WEIGHT = {"high": 0.9, "medium": 0.6, "low": 0.3}

ACTION_KIND_MAP = {
    "conclude": "conclude_now",
    "conclude now": "conclude_now",
    "specific investigation": "specific_investigation",
    "investigate further": "specific_investigation",
    "investigate": "specific_investigation",
    "open question": "open_question",
}

AGGREGATION_CONFIG = {
    "claim_from_grounding": "direct",
    "argument_from_claims": "min",
    "critique_from_arguments": "judge_verdict_weighted",
    "finding_from_critiques": "weighted_average",
    "failure_flag_penalty_per_instance": FAILURE_PENALTY,
    "failure_flag_penalty_cap": FAILURE_PENALTY_CAP,
    "quality_flag_bonus_per_instance": 0.05,
    "quality_flag_bonus_cap": 0.2,
    "linker_confidence_to_weight": LINKER_WEIGHT,
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def slugify(title, max_words=5):
    """Convert a title to a content-derived slug."""
    text = title.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    words = [w for w in text.split() if w not in STOP_WORDS]
    return "_".join(words[:max_words])


def strip_stars(text):
    """Strip orphan ** markers (P-001 pipeline bug)."""
    if not text:
        return text
    text = re.sub(r"^\*\*\s*", "", text)
    text = re.sub(r"\s*\*\*$", "", text)
    return text.strip()


def parse_verifier_status(caveat_text):
    """Return normalised verifier_status from a caveat string."""
    patterns = [
        (r"VERIFIED", "verified"),
        (r"PARTIALLY[\s_]*VERIFIED", "partially_verified"),
        (r"MIXED", "partially_verified"),
        (r"PLAUSIBLE", "partially_verified"),
        (r"UNVERIFIABLE", "unverified"),
        (r"UNVERIFIED", "unverified"),
        (r"DISPUTED", "rejected"),
        (r"REJECTED", "rejected"),
    ]
    upper = caveat_text.upper()
    # Match *after* the colon or **: to avoid hitting the word inside claim text
    colon_pos = caveat_text.find(":")
    search_region = upper[colon_pos:] if colon_pos >= 0 else upper
    for pat, status in patterns:
        if re.search(r"\b" + pat + r"\b", search_region):
            return status
    return "unverified"


def parse_claim_text_from_caveat(caveat):
    """Extract the claim's display text from a caveat string."""
    # "Claim text**: STATUS - detail" or "Claim text: STATUS - detail"
    m = re.match(
        r"^(.+?)(?:\*\*)?:\s*(?:VERIFIED|PARTIALLY|UNVERIFIABLE|UNVERIFIED|PLAUSIBLE|MIXED|REJECTED|DISPUTED)\b",
        caveat,
        re.IGNORECASE,
    )
    if m:
        return strip_stars(m.group(1).strip())
    return strip_stars(caveat.split(":")[0].strip())


def parse_caveat_detail(caveat):
    """Extract detail text after the status marker."""
    m = re.search(
        r"(?:VERIFIED|PARTIALLY\s*VERIFIED|UNVERIFIABLE|UNVERIFIED|PLAUSIBLE|MIXED|REJECTED|DISPUTED)"
        r"\s*[-.:]\s*(.*)",
        caveat,
        re.IGNORECASE | re.DOTALL,
    )
    return m.group(1).strip() if m else ""


def parse_action_kind(text):
    """Map a recommended-action prefix to schema enum."""
    upper = text.upper().strip()
    for prefix, kind in ACTION_KIND_MAP.items():
        if upper.startswith(prefix.upper()):
            return kind
    return "open_question"


def strip_action_prefix(text):
    """Remove the KIND: prefix from a recommended-action string."""
    m = re.match(r"^[A-Z_ ]+:\s*", text)
    return text[m.end():] if m else text


# ---------------------------------------------------------------------------
# Stage loaders
# ---------------------------------------------------------------------------

def load_stages(input_dir):
    """Load required and optional stage JSONs. Exit on missing required files."""
    p = Path(input_dir)
    stages = {}

    required = ["05-adversarial.json", "03-verifier-rejected.json", "06-synthesizer.json"]
    for name in required:
        path = p / name
        if not path.exists():
            print(f"ERROR: Required file not found: {path}", file=sys.stderr)
            sys.exit(1)
        with open(path) as f:
            stages[name] = json.load(f)

    linker = p / "05b-linker.json"
    if linker.exists():
        with open(linker) as f:
            stages["05b-linker.json"] = json.load(f)

    return stages


def require_judge_audit(adversarial):
    """Abort if the adversarial stage lacks judge_audit (pre-judge pipeline)."""
    if not adversarial:
        return
    sample = adversarial[0]
    if "judge_audit" not in sample:
        print(
            "ERROR: 05-adversarial.json lacks judge_audit fields.\n"
            "This run was produced by a pipeline version before the judge stage.\n"
            "Re-run the pipeline through the judge stage before extracting.\n"
            "Schema v0.2 requires judge_verdict, judge_rationale, debate_resolved,\n"
            "debate_unresolved, recommended_action, and failure/quality flags.",
            file=sys.stderr,
        )
        sys.exit(1)


# ---------------------------------------------------------------------------
# Node extraction
# ---------------------------------------------------------------------------

def _has_status_marker(text):
    """Check whether a caveat entry contains a verifier status keyword."""
    return bool(re.search(
        r"\b(?:VERIFIED|PARTIALLY[\s_]*VERIFIED|UNVERIFIABLE|UNVERIFIED|"
        r"PLAUSIBLE|MIXED|REJECTED|DISPUTED)\b",
        text, re.IGNORECASE,
    ))


def _parse_status_for_entry(text):
    """Return verifier status for a caveat entry.
    Entries with explicit markers get parsed; entries without default to
    'partially_verified'.  'PLAUSIBLE … NOT FOUND' downgrades to 'unverified'."""
    if not _has_status_marker(text):
        return "partially_verified"
    upper = text.upper()
    # Check for negative overrides first
    if re.search(r"\bNOT\s+FOUND\b", upper) or re.search(r"\bNOT\s+VERIFIED\b", upper):
        if "PLAUSIBLE" in upper:
            return "unverified"
    return parse_verifier_status(text)


def _claim_text_for_entry(text, has_marker):
    """Extract display text for a claim from a caveat entry."""
    if has_marker:
        result = parse_claim_text_from_caveat(text)
        # If parsing produces nothing (e.g. entry starts with ": STATUS"),
        # use the full trimmed text so the claim isn't dropped.
        return result if result else strip_stars(text.strip())
    # Continuation entry: use the entire text, trimmed
    return strip_stars(text.strip())


def extract_claims(adversarial):
    """Build Claim nodes from verifier caveats nested inside adversarial data.
    Every non-empty caveat array entry produces one Claim."""
    claims = []
    claim_map = {}  # critique_index -> [claim_ids]
    claim_counter = 0

    for crit_idx, item in enumerate(adversarial):
        verifier = item["critique"]["critique"]
        caveats = verifier.get("caveats", [])
        evidence = verifier.get("evidence_found", [])
        evidence_text = " ".join(
            e.strip().rstrip(".") for e in evidence
            if e.strip() and e.strip() != "."
        )

        crit_claims = []
        for caveat in caveats:
            caveat = caveat.strip() if caveat else ""
            if not caveat:
                continue

            has_marker = _has_status_marker(caveat)
            text = _claim_text_for_entry(caveat, has_marker)
            if not text:
                continue

            claim_counter += 1
            cid = f"clm_{claim_counter:03d}"

            status = _parse_status_for_entry(caveat)
            detail = parse_caveat_detail(caveat) if has_marker else ""
            grounding_parts = [p for p in [detail, evidence_text] if p]
            grounding = " ".join(grounding_parts) if grounding_parts else ""
            conf = VERIFIER_CONFIDENCE.get(status, 0.4)

            claims.append({
                "id": cid,
                "text": text,
                "verifier_status": status,
                "grounding": grounding,
                "grounding_citations": [],
                "confidence": conf,
                "confidence_justification": (
                    f"Verifier marked this claim '{status}'. "
                    f"Grounding prior {conf} assigned by extractor."
                ),
            })
            crit_claims.append(cid)

        claim_map[crit_idx] = crit_claims

    return claims, claim_map


def extract_arguments_and_flags(adversarial):
    """Build Argument nodes and failure/quality flag lists."""
    arguments = []
    failure_flags = []
    quality_flags = []
    fflag_counter = 0
    qflag_counter = 0

    for crit_idx, item in enumerate(adversarial):
        title = item["critique"]["critique"]["original"]["title"]
        slug = slugify(strip_stars(title))
        crt_id = f"crt_{slug}"
        strength = item["surviving_strength"].lower()
        base_conf = STRENGTH_BASE.get(strength, 0.35)

        audit = item["judge_audit"]
        verdict_just = audit.get("verdict_justification", "")
        resolved = audit.get("debate_resolved", "")
        unresolved = audit.get("debate_unresolved", "")
        rec_text = audit.get("recommended_action", item.get("recommended_action", ""))
        feasibility = audit.get("action_feasibility", "open_question")

        rec_action = {
            "kind": parse_action_kind(rec_text),
            "text": strip_action_prefix(rec_text),
            "feasibility": feasibility,
        }

        adv_failures = audit.get("advocate_failures", [])
        chl_failures = audit.get("challenger_failures", [])

        # --- Advocate argument ---
        adv_id = f"arg_adv_{slug}_r1"
        adv_penalty = min(len(adv_failures) * FAILURE_PENALTY, FAILURE_PENALTY_CAP)
        adv_conf = round(base_conf - adv_penalty, 2)

        arguments.append({
            "id": adv_id,
            "critique_id": crt_id,
            "role": "advocate",
            "round": 1,
            "text": item["advocate_defense"],
            "summary": f"Advocate defense of: {strip_stars(title)}",
            "self_assessment": item.get("advocate_self_assessment"),
            "judge_verdict": strength,
            "judge_rationale": verdict_just,
            "debate_resolved": resolved,
            "debate_unresolved": unresolved,
            "recommended_action": rec_action,
            "confidence": adv_conf,
            "confidence_justification": (
                f"Judge surviving strength '{strength}' (base {base_conf}); "
                f"{len(adv_failures)} advocate failures → penalty {adv_penalty}."
            ),
        })

        for fail_text in adv_failures:
            fflag_counter += 1
            ftype, evidence = _parse_flag(fail_text)
            failure_flags.append({
                "id": f"fflag_{fflag_counter:03d}",
                "argument_id": adv_id,
                "type": ftype,
                "evidence": evidence,
                "judge_rationale": None,
            })

        # --- Challenger argument ---
        chl_id = f"arg_chl_{slug}_r1"
        chl_penalty = min(len(chl_failures) * FAILURE_PENALTY, FAILURE_PENALTY_CAP)
        chl_conf = round(base_conf - chl_penalty, 2)

        arguments.append({
            "id": chl_id,
            "critique_id": crt_id,
            "role": "challenger",
            "round": 1,
            "text": item["challenger_rebuttal"],
            "summary": f"Challenger rebuttal on: {strip_stars(title)}",
            "self_assessment": None,
            "judge_verdict": strength,
            "judge_rationale": verdict_just,
            "debate_resolved": resolved,
            "debate_unresolved": unresolved,
            "recommended_action": rec_action,
            "confidence": chl_conf,
            "confidence_justification": (
                f"Judge surviving strength '{strength}' (base {base_conf}); "
                f"{len(chl_failures)} challenger failures → penalty {chl_penalty}."
            ),
        })

        for fail_text in chl_failures:
            fflag_counter += 1
            ftype, evidence = _parse_flag(fail_text)
            failure_flags.append({
                "id": f"fflag_{fflag_counter:03d}",
                "argument_id": chl_id,
                "type": ftype,
                "evidence": evidence,
                "judge_rationale": None,
            })

    return arguments, failure_flags, quality_flags


KNOWN_FLAG_TYPES = {
    "unsupported_estimate_fabricated",
    "unsupported_estimate_pseudo",
    "unsupported_estimate_counter",
    "whataboutism",
    "call_to_ignorance",
    "strawmanning",
    "false_definitiveness",
    "generic_recommendation",
    "misrepresenting_evidence_status",
}


def _parse_flag(flag_text):
    """Parse 'type: evidence' from a judge-audit failure string."""
    for ft in KNOWN_FLAG_TYPES:
        if flag_text.lower().startswith(ft):
            rest = flag_text[len(ft):].lstrip(":").strip()
            return ft, rest[:500]
    # Fallback: try splitting on first colon
    parts = flag_text.split(":", 1)
    candidate = parts[0].strip().lower().replace(" ", "_")
    if candidate in KNOWN_FLAG_TYPES:
        return candidate, parts[1].strip()[:500] if len(parts) > 1 else flag_text[:500]
    return "unsupported_estimate_fabricated", flag_text[:500]


def extract_surviving_critiques(adversarial):
    """Build SurvivingCritique nodes."""
    critiques = []
    for item in adversarial:
        verifier = item["critique"]["critique"]
        original = verifier["original"]
        title = strip_stars(original["title"])
        slug = slugify(title)
        strength = item["surviving_strength"].lower()
        raw_mat = (item["critique"].get("materiality") or "marginal").lower()
        # Normalize non-standard pipeline values to schema enum
        materiality = {"notable": "material", "significant": "material"}.get(raw_mat, raw_mat)
        if materiality not in ("material", "marginal", "immaterial"):
            print(f"WARNING: Unknown materiality '{raw_mat}' for '{title}', defaulting to 'marginal'",
                  file=sys.stderr)
            materiality = "marginal"

        verdict = verifier.get("verdict", "unverified")
        if verdict == "partially_verified":
            verifier_prior = VERIFIER_CONFIDENCE["partially_verified"]
        else:
            verifier_prior = VERIFIER_CONFIDENCE.get(verdict, 0.4)
        judge_prior = STRENGTH_BASE.get(strength, 0.35)
        conf = round((verifier_prior + judge_prior) / 2, 2)

        critiques.append({
            "id": f"crt_{slug}",
            "title": title,
            "hypothesis": strip_stars(original.get("hypothesis", "")),
            "mechanism": strip_stars(original.get("mechanism", "")),
            "judge_surviving_strength": strength,
            "materiality": materiality,
            "confidence": conf,
            "confidence_justification": (
                f"Verifier verdict '{verdict}' (prior {verifier_prior}) "
                f"blended with judge surviving strength '{strength}' (prior {judge_prior})."
            ),
        })
    return critiques


def extract_rejected_critiques(rejected_data):
    """Build RejectedCritique nodes."""
    critiques = []
    for item in rejected_data:
        original = item["original"]
        title = strip_stars(original["title"])
        slug = slugify(title)
        verdict = item.get("verdict", "unverified").lower()
        if verdict not in ("unverified", "rejected"):
            verdict = "unverified"

        # Build verifier_reasoning from evidence and caveats
        evidence_parts = [e.strip().rstrip(".") for e in item.get("evidence_found", [])
                          if e.strip() and e.strip() != "."]
        counter_parts = [e.strip().rstrip(".") for e in item.get("counter_evidence", [])
                         if e.strip() and e.strip() != "."]
        reasoning_parts = evidence_parts + counter_parts
        if not reasoning_parts:
            # Try to get reasoning from caveats
            caveats = item.get("caveats", [])
            for c in caveats:
                detail = parse_caveat_detail(c)
                if detail:
                    reasoning_parts.append(detail)

        verifier_reasoning = " ".join(reasoning_parts) if reasoning_parts else (
            f"Verdict: {verdict}. No detailed reasoning available."
        )

        conf = VERIFIER_CONFIDENCE.get(verdict, 0.4)
        label = "live assumption, neither confirmed nor denied" if verdict == "unverified" \
            else "contradicting evidence found; adjustable for what-if exploration"

        critiques.append({
            "id": f"rcrt_{slug}",
            "title": title,
            "hypothesis": strip_stars(original.get("hypothesis", "")),
            "mechanism": None,
            "verdict": verdict,
            "verifier_reasoning": verifier_reasoning,
            "confidence": conf,
            "confidence_justification": f"Default {conf} for '{verdict}' verdict ({label})",
        })
    return critiques


# ---------------------------------------------------------------------------
# Synthesizer report parsing
# ---------------------------------------------------------------------------

def extract_findings_from_report(report_text, surviving_critiques):
    """Parse synthesizer markdown report into Finding nodes."""
    crt_by_title = {c["title"].lower(): c for c in surviving_critiques}
    findings = []
    sections = _split_finding_sections(report_text)

    for section in sections:
        title = section["title"]
        slug = slugify(title)
        strength = section["strength"]
        conf = FINDING_CONFIDENCE.get(strength, 0.25)

        if strength in ("strong", "moderate"):
            fields = _parse_structured_finding(section["body"])
            conditional_tag = False
            conditional_note = None
            cond_match = re.search(
                r"\*\*(?:Conditional on|Conditional):\*\*\s*(.+?)(?:\n|$)",
                section["body"],
            )
            if cond_match:
                conditional_tag = True
                conditional_note = cond_match.group(1).strip()

            findings.append({
                "id": f"fnd_{slug}",
                "title": title,
                "surviving_strength": strength,
                "text": section["body"].strip(),
                "impact": fields.get("impact"),
                "evidence": fields.get("evidence"),
                "givewell_defense": fields.get("givewell_defense"),
                "why_it_survives": fields.get("why_it_survives"),
                "recommended_action": fields.get("recommended_action"),
                "key_unresolved_question": fields.get("key_unresolved_question"),
                "synthesizer_conditional_note": conditional_note,
                "synthesizer_conditional_tag": conditional_tag,
                "conditional_on": [],
                "confidence": conf,
                "confidence_justification": f"Seed confidence {conf} from surviving strength '{strength}'.",
            })
        else:
            # Weak finding — unstructured paragraph
            findings.append({
                "id": f"fnd_{slug}",
                "title": title,
                "surviving_strength": "weak",
                "text": section["body"].strip(),
                "impact": None,
                "evidence": None,
                "givewell_defense": None,
                "why_it_survives": None,
                "recommended_action": None,
                "key_unresolved_question": None,
                "synthesizer_conditional_note": None,
                "synthesizer_conditional_tag": False,
                "conditional_on": [],
                "confidence": FINDING_CONFIDENCE["weak"],
                "confidence_justification": "Seed confidence 0.25 from surviving strength 'weak'.",
            })

    return findings


def _split_finding_sections(report):
    """Split the synthesizer report into individual finding sections."""
    sections = []
    current_strength = None

    # Identify section boundaries
    strong_header = re.search(
        r"##\s+Critical Findings\s*\(surviving strength:\s*STRONG\)", report, re.IGNORECASE
    )
    moderate_header = re.search(
        r"##\s+Significant Findings\s*\(surviving strength:\s*MODERATE\)", report, re.IGNORECASE
    )
    weak_header = re.search(
        r"##\s+Minor Findings\s*\(surviving strength:\s*WEAK\)", report, re.IGNORECASE
    )

    # Extract strong findings
    if strong_header:
        end = moderate_header.start() if moderate_header else (weak_header.start() if weak_header else len(report))
        _extract_findings_from_block(report[strong_header.end():end], "strong", sections)

    # Extract moderate findings
    if moderate_header:
        end = weak_header.start() if weak_header else len(report)
        _extract_findings_from_block(report[moderate_header.end():end], "moderate", sections)

    # Extract weak findings
    if weak_header:
        # Find next ## section
        rest = report[weak_header.end():]
        next_section = re.search(r"\n##\s+", rest)
        block = rest[:next_section.start()] if next_section else rest
        _extract_weak_findings(block, sections)

    return sections


def _extract_findings_from_block(block, strength, sections):
    """Extract ### Finding N: Title sections from a strength block."""
    # Split on ### headers
    parts = re.split(r"###\s+(?:Finding\s+\d+:\s*)?", block)
    for part in parts:
        part = part.strip()
        if not part:
            continue
        # Skip italicised notes like "*No critiques achieved STRONG rating...*"
        if part.startswith("*") and not part.startswith("**"):
            continue
        lines = part.split("\n", 1)
        title = lines[0].strip()
        # Strip trailing markers like "[CONDITIONAL — see dependencies]"
        title = re.sub(r"\s*\[.*?\]\s*$", "", title)
        if not title:
            continue
        body = lines[1].strip() if len(lines) > 1 else ""
        sections.append({"title": title, "strength": strength, "body": body})


def _extract_weak_findings(block, sections):
    """Extract weak findings — supports both ### headers and bullet lists."""
    # Try ### headers first
    header_parts = re.split(r"###\s+", block)
    found_headers = False
    for part in header_parts:
        part = part.strip()
        if not part:
            continue
        lines = part.split("\n", 1)
        title = lines[0].strip()
        if not title or title.startswith("##"):
            continue
        body = lines[1].strip() if len(lines) > 1 else ""
        sections.append({"title": title, "strength": "weak", "body": body})
        found_headers = True

    if found_headers:
        return

    # Fallback: bullet list format "- **Title**: description"
    for m in re.finditer(r"-\s+\*\*(.+?)\*\*:\s*(.+?)(?=\n-\s+\*\*|\n\n|$)", block, re.DOTALL):
        title = m.group(1).strip()
        body = m.group(2).strip()
        sections.append({"title": title, "strength": "weak", "body": body})


def _parse_structured_finding(body):
    """Parse **Field:** values from a finding body."""
    fields = {}
    field_map = {
        "Impact": "impact",
        "Evidence": "evidence",
        "GiveWell's best defense": "givewell_defense",
        "GiveWell\u2019s best defense": "givewell_defense",
        "Why it survives": "why_it_survives",
        "Recommended action": "recommended_action",
        "Key unresolved question": "key_unresolved_question",
    }
    for label, key in field_map.items():
        pattern = rf"\*\*{re.escape(label)}:\*\*\s*(.+?)(?=\n\*\*[A-Z]|\Z)"
        m = re.search(pattern, body, re.DOTALL | re.IGNORECASE)
        if m:
            fields[key] = m.group(1).strip()
    return fields


# ---------------------------------------------------------------------------
# Edges
# ---------------------------------------------------------------------------

def build_edges(claims_map, arguments, surviving_critiques, rejected_critiques,
                findings, linker_data):
    """Construct all five edge types."""
    edges = {
        "claim_used_by_argument": [],
        "argument_rebuts_argument": [],
        "argument_belongs_to_critique": [],
        "critique_dependency": [],
        "critique_rolls_up_to_finding": [],
    }
    edge_counter = 0

    # Index arguments by critique_id
    args_by_crt = {}
    for arg in arguments:
        crt_id = arg["critique_id"]
        if crt_id not in args_by_crt:
            args_by_crt[crt_id] = []
        args_by_crt[crt_id].append(arg)

    # Index findings by slug-matched title
    fnd_by_slug = {slugify(f["title"]): f for f in findings}

    # Index critiques and rejected by title
    crt_by_title = {c["title"].lower(): c for c in surviving_critiques}
    rcrt_by_title = {c["title"].lower(): c for c in rejected_critiques}

    # 1) claim_used_by_argument: each claim -> both advocate and challenger for that critique
    for crit_idx, claim_ids in claims_map.items():
        crt_slug = slugify(surviving_critiques[crit_idx]["title"])
        crt_id = f"crt_{crt_slug}"
        crt_args = args_by_crt.get(crt_id, [])
        for claim_id in claim_ids:
            for arg in crt_args:
                edge_counter += 1
                edges["claim_used_by_argument"].append({
                    "id": f"e_{edge_counter:03d}",
                    "source_node_id": claim_id,
                    "target_node_id": arg["id"],
                    "weight": 0.7,
                    "weight_justification": (
                        "Default weight 0.7: claim is part of the critique's evidence base "
                        "used by both sides. Extractor cannot determine per-claim centrality "
                        "from current pipeline output."
                    ),
                })

    # 2) argument_rebuts_argument: challenger -> advocate for each debate
    for crt_id, crt_args in args_by_crt.items():
        adv = [a for a in crt_args if a["role"] == "advocate"]
        chl = [a for a in crt_args if a["role"] == "challenger"]
        for c in chl:
            for a in adv:
                edge_counter += 1
                edges["argument_rebuts_argument"].append({
                    "id": f"e_{edge_counter:03d}",
                    "source_node_id": c["id"],
                    "target_node_id": a["id"],
                    "weight": 1,
                    "weight_justification": "Direct rebuttal pair from adversarial stage.",
                    "relation": "rebuts",
                })

    # 3) argument_belongs_to_critique: each argument -> its critique
    for arg in arguments:
        edge_counter += 1
        edges["argument_belongs_to_critique"].append({
            "id": f"e_{edge_counter:03d}",
            "source_node_id": arg["id"],
            "target_node_id": arg["critique_id"],
            "weight": 1,
            "weight_justification": "Containment edge.",
        })

    # 4) critique_dependency: from linker
    if linker_data:
        deps = linker_data.get("dependencies", [])
        for dep in deps:
            surv_title = dep["surviving_critique_title"].lower()
            rej_title = dep["rejected_critique_title"].lower()
            surv_crt = crt_by_title.get(surv_title)
            rej_crt = rcrt_by_title.get(rej_title)
            if not surv_crt or not rej_crt:
                print(
                    f"WARNING: Linker dependency references unknown critique: "
                    f"'{dep['surviving_critique_title']}' -> '{dep['rejected_critique_title']}'",
                    file=sys.stderr,
                )
                continue
            conf_level = dep.get("confidence", "medium").lower()
            weight = LINKER_WEIGHT.get(conf_level, 0.6)
            edge_counter += 1
            edges["critique_dependency"].append({
                "id": f"e_dep_{edge_counter:03d}",
                "source_node_id": surv_crt["id"],
                "target_node_id": rej_crt["id"],
                "relationship": dep.get("relationship", "engages_with"),
                "linker_confidence": conf_level,
                "weight": weight,
                "weight_justification": (
                    f"{conf_level} linker confidence mapped to {weight} "
                    f"via aggregation_config."
                ),
            })

    # 5) critique_rolls_up_to_finding: match by title slug
    for crt in surviving_critiques:
        slug = slugify(crt["title"])
        fnd = fnd_by_slug.get(slug)
        if fnd:
            edge_counter += 1
            edges["critique_rolls_up_to_finding"].append({
                "id": f"e_{edge_counter:03d}",
                "source_node_id": crt["id"],
                "target_node_id": fnd["id"],
                "weight": 1,
                "weight_justification": "1:1 roll-up: synthesizer finding is named identically to critique.",
            })
        else:
            print(
                f"WARNING: No finding matched for critique '{crt['title']}' (slug: {slug})",
                file=sys.stderr,
            )

    return edges


# ---------------------------------------------------------------------------
# Pipeline summary
# ---------------------------------------------------------------------------

def build_pipeline_summary(adversarial, rejected_data, linker_data):
    """Compute pipeline summary from data counts (more reliable than parsing markdown)."""
    n_surviving = len(adversarial)
    n_rejected = len(rejected_data)
    n_total = n_surviving + n_rejected
    n_deps = 0
    if linker_data:
        n_deps = linker_data.get("n_dependencies_found", len(linker_data.get("dependencies", [])))

    # Count unique investigation threads
    threads = set()
    for item in adversarial:
        thread = item["critique"]["critique"]["original"].get("thread_name")
        if thread:
            threads.add(thread)
    for item in rejected_data:
        thread = item["original"].get("thread_name")
        if thread:
            threads.add(thread)

    from math import gcd
    if n_total > 0:
        g = gcd(n_surviving, n_total)
        signal_rate = f"{n_surviving}/{n_total} = {n_surviving // g}/{n_total // g}"
    else:
        signal_rate = "0/0"

    return {
        "investigation_threads_examined": len(threads),
        "candidate_critiques_generated": n_total,
        "verified_critiques": n_surviving,
        "rejected_by_verifier": n_rejected,
        "critiques_surviving_adversarial_review": n_surviving,
        "dependencies_identified": n_deps,
        "signal_rate": signal_rate,
    }


# ---------------------------------------------------------------------------
# Topic extraction
# ---------------------------------------------------------------------------

def extract_topic(report_text):
    """Extract topic from synthesizer report title."""
    m = re.search(r"^#\s+Red Team Report:\s*(.+)$", report_text, re.MULTILINE)
    if m:
        topic = m.group(1).strip()
        # Strip trailing parenthetical abbreviations like "(ITNs)"
        return f"GiveWell {topic}"
    return "Unknown Topic"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def extract(input_dir, run_id, topic_override=None):
    """Run the full extraction pipeline."""
    stages = load_stages(input_dir)
    adversarial = stages["05-adversarial.json"]
    rejected_data = stages["03-verifier-rejected.json"]
    synth_report = stages["06-synthesizer.json"].get("report", "")
    linker_data = stages.get("05b-linker.json")

    require_judge_audit(adversarial)

    # --- Nodes ---
    claims, claims_map = extract_claims(adversarial)
    arguments, failure_flags, quality_flags = extract_arguments_and_flags(adversarial)
    surviving_critiques = extract_surviving_critiques(adversarial)
    rejected_critiques = extract_rejected_critiques(rejected_data)
    findings = extract_findings_from_report(synth_report, surviving_critiques)

    # --- Edges ---
    edges = build_edges(
        claims_map, arguments, surviving_critiques, rejected_critiques,
        findings, linker_data,
    )

    # --- Top-level ---
    topic = topic_override or extract_topic(synth_report)
    summary = build_pipeline_summary(adversarial, rejected_data, linker_data)

    graph = {
        "schema_version": SCHEMA_VERSION,
        "run_id": run_id,
        "topic": topic,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "pipeline_version": PIPELINE_VERSION,
        "pipeline_summary": summary,
        "nodes": {
            "claims": claims,
            "arguments": arguments,
            "surviving_critiques": surviving_critiques,
            "rejected_critiques": rejected_critiques,
            "findings": findings,
        },
        "edges": edges,
        "quality_flags": quality_flags,
        "failure_flags": failure_flags,
        "aggregation_config": AGGREGATION_CONFIG,
    }

    return graph


def main():
    parser = argparse.ArgumentParser(
        description="Extract graph.json from pipeline stage outputs."
    )
    parser.add_argument(
        "--input-dir", required=True,
        help="Path to pipeline results directory (e.g. results/vas)",
    )
    parser.add_argument(
        "--run-id", required=True,
        help="Run identifier (e.g. vas-2026-04-13)",
    )
    parser.add_argument(
        "--output-dir", default=None,
        help="Output directory for runs/<run_id>/graph.json. "
             "Defaults to writing graph.json in current directory.",
    )
    parser.add_argument(
        "--topic", default=None,
        help="Override the auto-detected topic string.",
    )
    args = parser.parse_args()

    graph = extract(args.input_dir, args.run_id, args.topic)

    if args.output_dir:
        out_dir = Path(args.output_dir) / args.run_id
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "graph.json"
    else:
        out_path = Path("graph.json")

    with open(out_path, "w") as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)

    n_claims = len(graph["nodes"]["claims"])
    n_args = len(graph["nodes"]["arguments"])
    n_surv = len(graph["nodes"]["surviving_critiques"])
    n_rej = len(graph["nodes"]["rejected_critiques"])
    n_fnd = len(graph["nodes"]["findings"])
    n_flags = len(graph["failure_flags"])
    n_edges = sum(len(v) for v in graph["edges"].values())

    print(f"Wrote {out_path}")
    print(f"  claims={n_claims}  arguments={n_args}  surviving={n_surv}  "
          f"rejected={n_rej}  findings={n_fnd}")
    print(f"  edges={n_edges}  failure_flags={n_flags}")


if __name__ == "__main__":
    main()
