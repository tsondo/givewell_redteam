"""Tests for agent parsing functions.

Uses sample text matching the ACTUAL prompt output formats to verify
each parser extracts structured data correctly.
"""
from __future__ import annotations

from pipeline.agents import (
    parse_challenger_output,
    parse_decomposer_output,
    parse_investigator_output,
    parse_verifier_output,
)


# ---------------------------------------------------------------------------
# Sample texts
# ---------------------------------------------------------------------------

DECOMPOSER_SAMPLE = """\
THREAD 1: Mortality Effect Size and Study Quality

SCOPE: Examining the meta-analytic estimate of relative risk reduction from water chlorination, including study selection, weighting methodology, and applicability to programmatic settings.

KEY PARAMETERS:
- Pooled ln(relative risk) of all-cause mortality
- Relative risk of all-cause mortality
- Internal validity adjustment for under-5 mortality

WHAT GIVEWELL ALREADY ACCOUNTS FOR:
- Studies may have compliance issues
- Effect sizes may vary across contexts

WHAT GIVEWELL DOES NOT ACCOUNT FOR:
- Potential publication bias in the meta-analysis
- Differences in chlorine dosing between RCTs and field programs

DATA SOURCES TO EXAMINE:
- Cochrane systematic reviews on water treatment
- WHO water quality guidelines

MATERIALITY THRESHOLD: A 10% change in the relative risk parameter would shift cost-effectiveness by approximately 8-12%.

KNOWN CONCERNS ALREADY SURFACED:
- General concern about study quality in water treatment literature
- Compliance rates may differ in programmatic vs RCT settings

THREAD 2: External Validity and Contextual Adaptation

SCOPE: Whether the effect sizes from the underlying studies generalize to the specific program contexts (Kenya, Uganda, Malawi).

KEY PARAMETERS:
- External validity adjustment
- Plausibility cap
- Adult mortality scaling factor

WHAT GIVEWELL ALREADY ACCOUNTS FOR:
- Some geographic variation in baseline mortality
- Differences in water source types

WHAT GIVEWELL DOES NOT ACCOUNT FOR:
- Urban vs rural differences in water contamination
- Seasonal variation in water quality and diarrheal disease

DATA SOURCES TO EXAMINE:
- DHS surveys for program countries
- Local water quality monitoring reports

MATERIALITY THRESHOLD: Changes to external validity above 15% would be material.

KNOWN CONCERNS ALREADY SURFACED:
- Contextual adaptation is inherently uncertain
- Baseline disease burden differences across countries

DEPENDENCY MAP:
Thread 1 feeds into Thread 2 via the effect size estimate.

RECOMMENDED SEQUENCING:
Run Thread 1 first, then Thread 2.
"""

INVESTIGATOR_SAMPLE = """\
CRITIQUE 1: Publication Bias in Meta-Analytic Estimate

HYPOTHESIS: The pooled relative risk estimate used by GiveWell may be biased downward (overstating mortality reduction) due to publication bias — studies showing null or negative results for water chlorination are less likely to be published.

MECHANISM: If publication bias inflates the apparent mortality reduction, the relative risk parameter would be higher (closer to 1.0) than currently assumed. This would directly reduce the under-5 mortality benefit, which is the largest component of cost-effectiveness. The effect could lower cost-effectiveness by 15-30%.

EVIDENCE:
- Cochrane reviews have noted potential for publication bias in water treatment studies
- Funnel plot analysis of water treatment RCTs shows asymmetry (UNGROUNDED — needs verification)
- General literature on publication bias in public health interventions suggests effect sizes are commonly overstated by 10-30%

STRENGTH: HIGH

NOVELTY CHECK: The exclusion list mentions "general concern about study quality" but does not specifically address publication bias as a quantifiable source of overestimation.

CRITIQUE 2: Chlorine Decay and Residual Protection Gaps

HYPOTHESIS: The mortality reduction assumed in the CEA may overstate actual protection because chlorine residual decays rapidly in stored water, especially in warm climates, leaving households unprotected for significant portions of time between chlorination events.

MECHANISM: Reduced effective protection time would lower the real-world mortality reduction relative to RCT conditions where monitoring was more frequent. This primarily affects the internal validity adjustment and could reduce effective protection by 20-40%.

EVIDENCE:
- Studies in Kenya show free chlorine residual drops below protective levels within 24 hours in many households
- WHO guidelines recommend minimum 0.2 mg/L residual, which field programs often fail to maintain

STRENGTH: MEDIUM

NOVELTY CHECK: Not on the exclusion list. While compliance is mentioned, chlorine decay is a distinct chemical/physical limitation.

SUMMARY: The most important finding is the potential for publication bias to systematically overstate the mortality benefit.

RECOMMENDED VERIFICATION PRIORITIES: Critique 1 (publication bias) should be verified first as it could affect the core effect size estimate used throughout the model.
"""

VERIFIER_VERIFIED_SAMPLE = """\
CRITIQUE: Publication Bias in Meta-Analytic Estimate

CITATION CHECK:
- The reference to Cochrane reviews noting potential publication bias is well-established. The Clasen et al. (2015) Cochrane review of water quality interventions discusses this limitation.
- The claim about funnel plot asymmetry requires specific verification.

CLAIM CHECK:
- The general claim that publication bias can inflate effect sizes by 10-30% is plausible based on meta-research literature
- The specific magnitude estimate for water chlorination needs empirical grounding

EVIDENCE FOUND:
- Clasen et al. (2015) Cochrane systematic review acknowledges risk of publication bias
- Ioannidis (2005) documents systematic overestimation of effect sizes in published literature
- A 2018 systematic review of water treatment interventions found evidence of small-study effects consistent with publication bias

OVERALL VERDICT: VERIFIED

REVISED CRITIQUE (if partially verified):
"""

VERIFIER_PARTIAL_SAMPLE = """\
CRITIQUE: Chlorine Decay and Residual Protection Gaps

CITATION CHECK:
- The claim about chlorine residual dropping below protective levels within 24 hours is partially supported but context-dependent.

CLAIM CHECK:
- The 20-40% reduction estimate is plausible but uncertain — actual impact depends heavily on local conditions
- WHO minimum residual guidelines are accurately cited

EVIDENCE FOUND:
- Arnold & Colford (2007) found variable chlorine residual levels across field studies
- Local monitoring data from Kenya shows mixed results on residual protection

OVERALL VERDICT: PARTIALLY VERIFIED

REVISED CRITIQUE (if partially verified):
The chlorine decay concern is valid but the magnitude of impact is likely at the lower end of the estimated range (10-25% rather than 20-40%). Protection gaps exist but their effect on all-cause mortality is moderated by the fact that diarrheal disease transmission has multiple pathways.
"""

VERIFIER_UNVERIFIABLE_SAMPLE = """\
CRITIQUE: Speculative Concern About Biofilm Resistance

CITATION CHECK:
- No specific citations were provided for this claim.

CLAIM CHECK:
- The mechanism described is theoretically plausible but lacks empirical support in the water chlorination context.

EVIDENCE FOUND:
- No direct evidence found linking biofilm resistance to reduced chlorination effectiveness in household water treatment programs.

OVERALL VERDICT: UNVERIFIABLE
"""

CHALLENGER_SAMPLE = """\
REBUTTAL: Publication Bias in Meta-Analytic Estimate

RESPONSE TO "EXISTING COVERAGE": GiveWell's acknowledgment of study limitations does not specifically quantify or adjust for publication bias. Acknowledging a problem is not the same as correcting for it.

RESPONSE TO "EVIDENCE WEAKNESSES": The evidence for publication bias is well-established in meta-research literature and has been specifically identified in water treatment systematic reviews.

RESPONSE TO "MAGNITUDE CHALLENGE": Even at the conservative end of estimates, a 10% reduction in effect size would meaningfully change cost-effectiveness rankings.

RESPONSE TO "OFFSETTING FACTORS": The proposed offsetting factors (conservative modeling elsewhere) are not systematically documented and cannot be assumed to compensate for a specific, identified bias.

KEY UNRESOLVED QUESTIONS:
- What would a formal funnel plot analysis of the specific studies in GiveWell's meta-analysis show?
- Has anyone conducted a trim-and-fill analysis on this literature?
- Would pre-registered replications yield similar effect sizes?

SURVIVING STRENGTH: Moderate

RECOMMENDED ACTION: Investigate further
"""


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_parse_decomposer_output() -> None:
    result = parse_decomposer_output(DECOMPOSER_SAMPLE)

    assert len(result.threads) == 2
    assert result.threads[0].name == "Mortality Effect Size and Study Quality"
    assert result.threads[1].name == "External Validity and Contextual Adaptation"

    # Non-empty context_md
    assert result.threads[0].context_md
    assert result.threads[1].context_md

    # Exclusion list populated from KNOWN CONCERNS ALREADY SURFACED
    assert len(result.exclusion_list) > 0
    assert any("study quality" in e.lower() for e in result.exclusion_list)

    # CEA parameter map populated
    assert result.cea_parameter_map
    assert "relative risk" in result.cea_parameter_map.lower()


def test_parse_decomposer_thread_context_md() -> None:
    result = parse_decomposer_output(DECOMPOSER_SAMPLE)

    for thread in result.threads:
        # context_md should contain thread name and scope
        assert thread.name in thread.context_md
        assert "Scope" in thread.context_md or "scope" in thread.context_md.lower()


def test_parse_investigator_output() -> None:
    critiques = parse_investigator_output(INVESTIGATOR_SAMPLE, "Mortality Effect Size")

    assert len(critiques) == 2
    assert critiques[0].title == "Publication Bias in Meta-Analytic Estimate"
    assert critiques[1].title == "Chlorine Decay and Residual Protection Gaps"

    # Thread name propagated
    assert critiques[0].thread_name == "Mortality Effect Size"
    assert critiques[1].thread_name == "Mortality Effect Size"

    # Hypothesis parsed
    assert "publication bias" in critiques[0].hypothesis.lower()

    # Strength mapped to magnitude
    assert critiques[0].estimated_magnitude == "large"  # HIGH -> large
    assert critiques[1].estimated_magnitude == "medium"  # MEDIUM -> medium

    # Direction inferred from mechanism
    assert critiques[0].estimated_direction == "decreases"  # "lower" in mechanism
    assert critiques[1].estimated_direction == "decreases"  # "reduce" in mechanism


def test_parse_verifier_output_verified() -> None:
    from pipeline.schemas import CandidateCritique

    original = CandidateCritique(
        thread_name="Mortality Effect Size",
        title="Publication Bias",
        hypothesis="Test hypothesis",
        mechanism="Test mechanism",
        parameters_affected=["relative_risk"],
        suggested_evidence=["Test evidence"],
        estimated_direction="decreases",
        estimated_magnitude="large",
    )

    result = parse_verifier_output(VERIFIER_VERIFIED_SAMPLE, original)

    assert result.verdict == "verified"
    assert len(result.evidence_found) > 0
    assert any("clasen" in e.lower() for e in result.evidence_found)
    # No revised hypothesis for verified
    assert result.revised_hypothesis is None or result.revised_hypothesis == ""


def test_parse_verifier_output_partially_verified() -> None:
    from pipeline.schemas import CandidateCritique

    original = CandidateCritique(
        thread_name="Mortality Effect Size",
        title="Chlorine Decay",
        hypothesis="Test hypothesis",
        mechanism="Test mechanism",
        parameters_affected=["internal_validity_under5"],
        suggested_evidence=[],
        estimated_direction="decreases",
        estimated_magnitude="medium",
    )

    result = parse_verifier_output(VERIFIER_PARTIAL_SAMPLE, original)

    assert result.verdict == "partially_verified"
    assert result.revised_hypothesis is not None
    assert len(result.revised_hypothesis) > 0
    assert "chlorine decay" in result.revised_hypothesis.lower()


def test_parse_verifier_output_unverified() -> None:
    from pipeline.schemas import CandidateCritique

    original = CandidateCritique(
        thread_name="Mortality Effect Size",
        title="Biofilm Resistance",
        hypothesis="Test hypothesis",
        mechanism="Test mechanism",
        parameters_affected=[],
        suggested_evidence=[],
        estimated_direction="uncertain",
        estimated_magnitude="unknown",
    )

    result = parse_verifier_output(VERIFIER_UNVERIFIABLE_SAMPLE, original)

    assert result.verdict == "unverified"


def test_parse_challenger_output() -> None:
    strength, questions, action = parse_challenger_output(CHALLENGER_SAMPLE)

    assert strength == "moderate"
    assert len(questions) >= 2
    assert any("funnel plot" in q.lower() for q in questions)
    assert action == "investigate"
