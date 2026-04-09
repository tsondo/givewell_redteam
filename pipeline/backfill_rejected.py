"""One-shot backfill: reconstruct 03-verifier-rejected.json for prior runs.

Parses existing 03-verifier.md files (raw API responses) to extract
critiques that were dropped by the verifier's verdict filter (UNVERIFIABLE
or REJECTED), and saves them as structured JSON alongside the existing
03-verifier.json files.

Usage:
    python -m pipeline.backfill_rejected          # all runs
    python -m pipeline.backfill_rejected vas      # single run
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from pipeline.agents import parse_verifier_output
from pipeline.schemas import CandidateCritique, VerifiedCritique

RESULTS_DIR = Path("results")
RUNS = ["water-chlorination", "itns", "smc", "vas"]


def _load_investigators(run: str) -> dict[str, CandidateCritique]:
    """Load investigators JSON and return title -> CandidateCritique map."""
    path = RESULTS_DIR / run / "02-investigators.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    return {c["title"]: CandidateCritique.from_dict(c) for c in data}


def _load_verified_titles(run: str) -> set[str]:
    """Load verifier JSON and return set of titles that passed."""
    path = RESULTS_DIR / run / "03-verifier.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    return {c["original"]["title"] for c in data}


def _extract_critique_section(
    raw_md: str, title: str, batch_titles: list[str]
) -> str | None:
    """Find the ## Critique N: section for a given title within its batch response.

    The raw .md has sections delimited by '--- Critique: {title} ---'.
    Each such section contains the full batch API response, which has
    '## Critique N:' subsections. We find the batch response that contains
    our title as a delimiter, then extract the right subsection by position.
    """
    # Find the batch response section for this title
    delimiter = f"--- Critique: {title} ---"
    idx = raw_md.find(delimiter)
    if idx == -1:
        return None

    # Get the batch response text (from after the delimiter to next delimiter)
    start = idx + len(delimiter)
    next_delim = raw_md.find("\n--- Critique:", start)
    if next_delim == -1:
        batch_text = raw_md[start:]
    else:
        batch_text = raw_md[start:next_delim]

    # For multi-critique batches, try to find the right ## Critique N: section
    if title in batch_titles and len(batch_titles) > 1:
        target_n = batch_titles.index(title) + 1  # 1-indexed

        split_pattern = re.compile(
            r"(?:^|\n)\s*#{1,3}\s*Critique\s+(\d+)\s*[:\-]",
            re.IGNORECASE | re.MULTILINE,
        )
        matches = list(split_pattern.finditer(batch_text))

        for i, m in enumerate(matches):
            if int(m.group(1)) == target_n:
                section_start = m.end()
                section_end = matches[i + 1].start() if i + 1 < len(matches) else len(batch_text)
                return batch_text[section_start:section_end].strip()

    # Fallback: single-critique batch, or batch processed as individual calls
    # (no ## Critique N: headers found). Use the full section text.
    return batch_text.strip()


def _determine_batch_titles(
    all_titles: list[str], batch_size: int = 3
) -> dict[str, list[str]]:
    """Map each title to the list of titles in its batch."""
    result = {}
    for start in range(0, len(all_titles), batch_size):
        batch = all_titles[start : start + batch_size]
        for title in batch:
            result[title] = batch
    return result


def backfill_run(run: str) -> None:
    """Reconstruct 03-verifier-rejected.json for a single run."""
    investigators = _load_investigators(run)
    verified_titles = _load_verified_titles(run)
    all_titles = list(investigators.keys())  # preserves insertion order from JSON

    dropped_titles = [t for t in all_titles if t not in verified_titles]
    if not dropped_titles:
        print(f"  {run}: no dropped critiques, skipping")
        return

    raw_md_path = RESULTS_DIR / run / "03-verifier.md"
    raw_md = raw_md_path.read_text(encoding="utf-8")

    batch_map = _determine_batch_titles(all_titles)
    rejected: list[VerifiedCritique] = []

    for title in dropped_titles:
        batch_titles = batch_map.get(title, [])
        section = _extract_critique_section(raw_md, title, batch_titles)

        if section is None:
            print(f"  WARNING: could not extract section for '{title}' — skipping")
            continue

        result = parse_verifier_output(section, investigators[title])
        rejected.append(result)
        print(f"  {title}: verdict={result.verdict}")

    # Save
    out_path = RESULTS_DIR / run / "03-verifier-rejected.json"
    json_data = [r.to_dict() for r in rejected]
    out_path.write_text(json.dumps(json_data, indent=2, default=str), encoding="utf-8")
    print(f"  Saved {len(rejected)} rejected critiques to {out_path}")

    # Verify counts
    total_investigators = len(investigators)
    total_verified = len(verified_titles)
    total_rejected = len(rejected)
    total_accounted = total_verified + total_rejected
    print(
        f"  Count check: {total_investigators} investigators, "
        f"{total_verified} verified, {total_rejected} rejected, "
        f"{total_accounted} accounted for "
        f"({'OK' if total_accounted == total_investigators else 'MISMATCH'})"
    )


def main() -> None:
    runs = sys.argv[1:] if len(sys.argv) > 1 else RUNS
    for run in runs:
        print(f"\n=== {run} ===")
        backfill_run(run)


if __name__ == "__main__":
    main()
