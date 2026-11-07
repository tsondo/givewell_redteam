"""Tests for the verifier's CORE CLAIM rating and how it flows downstream."""
import pytest

from pipeline.agents import (
    _build_synthesizer_user_message,
    _format_rejected_critiques_for_synthesizer,
    parse_verifier_output,
)
from pipeline.schemas import (
    CandidateCritique,
    DebatedCritique,
    DecomposerOutput,
    LinkerOutput,
    QuantifiedCritique,
    VerifiedCritique,
)


def _candidate(title: str = "Speedup is understated") -> CandidateCritique:
    return CandidateCritique(
        thread_name="t", title=title, hypothesis="h", mechanism="m",
        parameters_affected=["speedup_years"], suggested_evidence=[],
        estimated_direction="increases", estimated_magnitude="large",
    )


def _verifier_text(support: str) -> str:
    return (
        "**CLAIM CHECK:**\n"
        "- **No commercial sponsor for generic statins:** VERIFIED.\n\n"
        "**EVIDENCE FOUND:**\n- Phase II funders are public.\n\n"
        "**CORE CLAIM:**\n"
        "- **Claim:** Without this grant the Phase III would likely never be run.\n"
        f"- **Support:** {support}\n"
        "- **Why:** No Phase III funder was found, but absence is not proof.\n\n"
        "**OVERALL VERDICT:** PARTIALLY VERIFIED.\n"
    )


@pytest.mark.parametrize(
    ("support", "expected"),
    [("SUPPORTED", "supported"), ("LOGIC ONLY", "logic_only"), ("CONTRADICTED", "contradicted")],
)
def test_core_claim_is_parsed(support: str, expected: str) -> None:
    vc = parse_verifier_output(_verifier_text(support), _candidate())
    assert vc.core_claim.startswith("Without this grant")
    assert vc.core_claim_support == expected
    assert vc.core_claim_reason.startswith("No Phase III funder")


def test_claim_check_does_not_swallow_core_claim() -> None:
    vc = parse_verifier_output(_verifier_text("LOGIC ONLY"), _candidate())
    assert not any("Without this grant" in c for c in vc.caveats)


def test_contradicted_core_claim_rejects_the_critique() -> None:
    vc = parse_verifier_output(_verifier_text("CONTRADICTED"), _candidate())
    assert vc.verdict == "rejected"


def test_missing_core_claim_is_unknown_and_verdict_unchanged() -> None:
    text = "**OVERALL VERDICT:** PARTIALLY VERIFIED.\n\n**EVIDENCE FOUND:**\n- x\n"
    vc = parse_verifier_output(text, _candidate())
    assert vc.core_claim_support == "unknown"
    assert vc.verdict == "partially_verified"


def test_old_saved_records_load_without_core_claim_fields() -> None:
    vc = VerifiedCritique.from_dict({
        "original": _candidate().to_dict(), "verdict": "verified",
        "evidence_found": [], "evidence_strength": "weak",
        "counter_evidence": [], "caveats": [], "revised_hypothesis": None,
    })
    assert vc.core_claim_support == "unknown"
    assert VerifiedCritique.from_dict(vc.to_dict()) == vc


def _debated(support: str, title: str) -> DebatedCritique:
    vc = parse_verifier_output(_verifier_text(support), _candidate(title))
    qc = QuantifiedCritique(
        critique=vc, target_parameters=[], alternative_range=[],
        sensitivity_results={}, materiality="material", interaction_effects=[],
    )
    return DebatedCritique(
        critique=qc, advocate_defense="a", challenger_rebuttal="c",
        surviving_strength="moderate", key_unresolved=[], recommended_action="r",
    )


def test_synthesizer_lists_logic_only_findings_for_open_questions() -> None:
    msg = _build_synthesizer_user_message(
        debated=[_debated("LOGIC ONLY", "Logic-only finding"), _debated("SUPPORTED", "Supported finding")],
        all_critiques_count=2, verified_count=2, rejected_critiques=[],
        linker_output=LinkerOutput(
            dependencies=[], n_surviving_critiques_examined=2,
            n_rejected_critiques_available=0, n_dependencies_found=0,
        ),
        decomposer_output=DecomposerOutput(threads=[], exclusion_list=[], cea_parameter_map=""),
        baseline_output="",
    )
    section = msg.split("## Surviving Findings Resting on Unverified Core Claims")[1].split("## Critique Dependencies")[0]
    assert "Logic-only finding" in section
    assert "Supported finding" not in section
    assert "(support: LOGIC ONLY)" in msg and "(support: SUPPORTED)" in msg


def test_rejected_entries_show_the_contradicted_core_claim() -> None:
    vc = parse_verifier_output(_verifier_text("CONTRADICTED"), _candidate())
    out = _format_rejected_critiques_for_synthesizer([vc])
    contradicted = out.split("### Verdict: REJECTED")[1]
    assert "(support: CONTRADICTED)" in contradicted


def test_synthesizer_input_lists_immaterial_and_parameter_fields() -> None:
    material = _debated("SUPPORTED", "Material finding")
    material.critique.sensitivity_results = {
        "tb_statins/p_success": {"baseline": 3055.0, "pct_change_low": -50.0, "pct_change_high": -20.0}
    }
    material.critique.alternative_range = [{"mapped": "p_success", "low": 0.2, "high": 0.32}]
    immaterial = _debated("SUPPORTED", "Small effect").critique
    immaterial.materiality = "immaterial"
    msg = _build_synthesizer_user_message(
        debated=[material],
        all_critiques_count=2, verified_count=2, rejected_critiques=[],
        linker_output=LinkerOutput(
            dependencies=[], n_surviving_critiques_examined=1,
            n_rejected_critiques_available=0, n_dependencies_found=0,
        ),
        decomposer_output=DecomposerOutput(threads=[], exclusion_list=[], cea_parameter_map=""),
        baseline_output="",
        immaterial=[immaterial],
    )
    assert "Judged immaterial by quantifier (not debated): 1" in msg
    assert "#### Small effect" in msg.split("## Critiques Judged Immaterial")[1]
    assert "**Parameters Affected:** p_success" in msg
    assert "tb_statins/p_success: 0.2 to 0.32 -> -50% to -20%" in msg
