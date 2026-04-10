from __future__ import annotations

import json

import pytest

from pipeline.schemas import (
    CandidateCritique,
    DebatedCritique,
    DecomposerOutput,
    InvestigationThread,
    JudgeAudit,
    PipelineStats,
    QuantifiedCritique,
    VerifiedCritique,
)


def make_investigation_thread() -> InvestigationThread:
    return InvestigationThread(
        name="Coverage assumptions",
        scope="Assess whether 80% chlorination coverage is achievable in target regions",
        key_questions=[
            "What is the actual coverage achieved in comparable programs?",
            "How does coverage decay over time?",
        ],
        cea_parameters_affected=["coverage_rate", "years_of_benefit"],
        relevant_sources=["WHO chlorination report 2022", "Cochrane review 2019"],
        out_of_scope="Water quality testing methodology",
        context_md="## Background\nGiveWell assumes 80% effective coverage.",
    )


def make_candidate_critique() -> CandidateCritique:
    return CandidateCritique(
        thread_name="Coverage assumptions",
        title="Coverage rate overestimated",
        hypothesis="Actual chlorination coverage is closer to 50%, not 80%",
        mechanism="Chlorine dissipates in storage containers; point-of-use compliance is low",
        parameters_affected=["coverage_rate"],
        suggested_evidence=[
            "Field studies in sub-Saharan Africa",
            "Compliance surveys from similar programs",
        ],
        estimated_direction="decreases",
        estimated_magnitude="large",
    )


def make_verified_critique() -> VerifiedCritique:
    return VerifiedCritique(
        original=make_candidate_critique(),
        verdict="partially_verified",
        evidence_found=[
            "A 2021 study found median coverage of 58% in Kenya",
            "Uganda pilot reported 62% compliance at 6 months",
        ],
        evidence_strength="moderate",
        counter_evidence=["Malawi program achieved 78% after supervision visits"],
        caveats=["Supervision intensity varies substantially across programs"],
        revised_hypothesis="Coverage likely 55–70% rather than 80% without strong supervision",
    )


def make_quantified_critique() -> QuantifiedCritique:
    return QuantifiedCritique(
        critique=make_verified_critique(),
        target_parameters=[
            {"name": "coverage_rate", "givewell_value": 0.80, "unit": "fraction"}
        ],
        alternative_range=[
            {"name": "coverage_rate", "low": 0.50, "mid": 0.62, "high": 0.72}
        ],
        sensitivity_results={
            "cost_per_daly_low": 45.0,
            "cost_per_daly_mid": 58.0,
            "cost_per_daly_high": 72.0,
            "givewell_cost_per_daly": 38.0,
        },
        materiality="material",
        interaction_effects=["Interacts with mortality_reduction parameter"],
    )


def make_debated_critique() -> DebatedCritique:
    return DebatedCritique(
        critique=make_quantified_critique(),
        advocate_defense=(
            "GiveWell's 80% figure is based on supervised program data, "
            "which is the relevant comparison since AMF funds supervision."
        ),
        challenger_rebuttal=(
            "Supervision quality degrades at scale; field evidence shows "
            "significant drop-off after initial implementation period."
        ),
        surviving_strength="moderate",
        key_unresolved=[
            "Long-run compliance trajectory under AMF supervision model",
            "Whether Kenya/Uganda data is comparable to target regions",
        ],
        recommended_action="investigate",
    )


# --- Round-trip tests ---

class TestInvestigationThreadRoundTrip:
    def test_round_trip(self) -> None:
        obj = make_investigation_thread()
        serialized = json.dumps(obj.to_dict())
        restored = InvestigationThread.from_dict(json.loads(serialized))

        assert restored.name == obj.name
        assert restored.scope == obj.scope
        assert restored.key_questions == obj.key_questions
        assert restored.cea_parameters_affected == obj.cea_parameters_affected
        assert restored.relevant_sources == obj.relevant_sources
        assert restored.out_of_scope == obj.out_of_scope
        assert restored.context_md == obj.context_md


class TestDecomposerOutputRoundTrip:
    def test_round_trip(self) -> None:
        thread = make_investigation_thread()
        obj = DecomposerOutput(
            threads=[thread],
            exclusion_list=["Political feasibility", "Historical context"],
            cea_parameter_map="coverage_rate -> coverage assumptions thread",
        )
        serialized = json.dumps(obj.to_dict())
        restored = DecomposerOutput.from_dict(json.loads(serialized))

        assert len(restored.threads) == 1
        assert restored.threads[0].name == thread.name
        assert restored.threads[0].key_questions == thread.key_questions
        assert restored.exclusion_list == obj.exclusion_list
        assert restored.cea_parameter_map == obj.cea_parameter_map

    def test_multiple_threads(self) -> None:
        thread1 = make_investigation_thread()
        thread2 = InvestigationThread(
            name="Mortality assumptions",
            scope="Check diarrheal mortality rates used",
            key_questions=["What data source for under-5 mortality?"],
            cea_parameters_affected=["mortality_rate"],
            relevant_sources=["GBD 2019"],
            out_of_scope="Non-diarrheal mortality",
            context_md="",
        )
        obj = DecomposerOutput(
            threads=[thread1, thread2],
            exclusion_list=[],
            cea_parameter_map="",
        )
        serialized = json.dumps(obj.to_dict())
        restored = DecomposerOutput.from_dict(json.loads(serialized))

        assert len(restored.threads) == 2
        assert restored.threads[1].name == "Mortality assumptions"


class TestCandidateCritiqueRoundTrip:
    def test_round_trip(self) -> None:
        obj = make_candidate_critique()
        serialized = json.dumps(obj.to_dict())
        restored = CandidateCritique.from_dict(json.loads(serialized))

        assert restored.thread_name == obj.thread_name
        assert restored.title == obj.title
        assert restored.hypothesis == obj.hypothesis
        assert restored.mechanism == obj.mechanism
        assert restored.parameters_affected == obj.parameters_affected
        assert restored.suggested_evidence == obj.suggested_evidence
        assert restored.estimated_direction == obj.estimated_direction
        assert restored.estimated_magnitude == obj.estimated_magnitude


class TestVerifiedCritiqueRoundTrip:
    def test_round_trip(self) -> None:
        obj = make_verified_critique()
        serialized = json.dumps(obj.to_dict())
        restored = VerifiedCritique.from_dict(json.loads(serialized))

        assert restored.verdict == obj.verdict
        assert restored.evidence_found == obj.evidence_found
        assert restored.evidence_strength == obj.evidence_strength
        assert restored.counter_evidence == obj.counter_evidence
        assert restored.caveats == obj.caveats
        assert restored.revised_hypothesis == obj.revised_hypothesis
        assert restored.original.title == obj.original.title
        assert restored.original.estimated_direction == obj.original.estimated_direction

    def test_none_revised_hypothesis(self) -> None:
        obj = make_verified_critique()
        obj.revised_hypothesis = None
        serialized = json.dumps(obj.to_dict())
        restored = VerifiedCritique.from_dict(json.loads(serialized))
        assert restored.revised_hypothesis is None


class TestQuantifiedCritiqueRoundTrip:
    def test_round_trip(self) -> None:
        obj = make_quantified_critique()
        serialized = json.dumps(obj.to_dict())
        restored = QuantifiedCritique.from_dict(json.loads(serialized))

        assert restored.materiality == obj.materiality
        assert restored.target_parameters == obj.target_parameters
        assert restored.alternative_range == obj.alternative_range
        assert restored.sensitivity_results == obj.sensitivity_results
        assert restored.interaction_effects == obj.interaction_effects
        assert restored.critique.verdict == obj.critique.verdict
        assert restored.critique.original.title == obj.critique.original.title


def make_judge_audit() -> JudgeAudit:
    return JudgeAudit(
        advocate_failures=[
            "unsupported_estimate_fabricated: I estimate 10-25% with no chain shown",
            "whataboutism: Challenger's Y also lacks rigorous testing",
        ],
        challenger_failures=["strawmanning: rebuts a category-swapped claim"],
        surviving_strength="moderate",
        verdict_justification=(
            "The Challenger raised a grounded concern that the Advocate "
            "only partially defended; both sides made some substantive moves."
        ),
        recommended_action=(
            "CONCLUDE NOW: The critique survives as a moderate concern; "
            "adjust the parameter range to reflect narrowed bounds."
        ),
        action_feasibility="actionable_now",
        debate_resolved="The debate narrowed the range from 5-50% to 10-25%.",
        debate_unresolved="Whether the threshold effect is linear or exponential.",
    )


class TestDebatedCritiqueRoundTrip:
    def test_round_trip(self) -> None:
        obj = make_debated_critique()
        serialized = json.dumps(obj.to_dict())
        restored = DebatedCritique.from_dict(json.loads(serialized))

        assert restored.advocate_defense == obj.advocate_defense
        assert restored.challenger_rebuttal == obj.challenger_rebuttal
        assert restored.surviving_strength == obj.surviving_strength
        assert restored.key_unresolved == obj.key_unresolved
        assert restored.recommended_action == obj.recommended_action
        assert restored.critique.materiality == obj.critique.materiality
        assert restored.critique.critique.verdict == obj.critique.critique.verdict
        # New fields default to neutral values for legacy-style objects.
        assert restored.judge_audit is None
        assert restored.advocate_self_assessment == ""

    def test_round_trip_with_judge_audit(self) -> None:
        obj = make_debated_critique()
        obj.judge_audit = make_judge_audit()
        obj.advocate_self_assessment = "partial"
        serialized = json.dumps(obj.to_dict())
        restored = DebatedCritique.from_dict(json.loads(serialized))

        assert restored.judge_audit is not None
        assert restored.judge_audit.surviving_strength == "moderate"
        assert restored.judge_audit.action_feasibility == "actionable_now"
        assert len(restored.judge_audit.advocate_failures) == 2
        assert restored.judge_audit.advocate_failures[0].startswith(
            "unsupported_estimate_fabricated:"
        )
        assert restored.judge_audit.challenger_failures == [
            "strawmanning: rebuts a category-swapped claim"
        ]
        assert restored.advocate_self_assessment == "partial"

    def test_backward_compat_load_without_judge_audit(self) -> None:
        """Pre-judge 05-adversarial.json files have neither judge_audit nor
        advocate_self_assessment. Loading them should succeed and populate
        the new fields with safe defaults."""
        legacy_dict = {
            "critique": make_quantified_critique().to_dict(),
            "advocate_defense": "old-format defense",
            "challenger_rebuttal": "old-format rebuttal",
            "surviving_strength": "strong",
            "key_unresolved": ["legacy q1", "legacy q2"],
            "recommended_action": "investigate",
        }
        restored = DebatedCritique.from_dict(legacy_dict)

        assert restored.surviving_strength == "strong"
        assert restored.recommended_action == "investigate"
        assert restored.judge_audit is None
        assert restored.advocate_self_assessment == ""


class TestJudgeAuditRoundTrip:
    def test_round_trip(self) -> None:
        obj = make_judge_audit()
        serialized = json.dumps(obj.to_dict())
        restored = JudgeAudit.from_dict(json.loads(serialized))

        assert restored.surviving_strength == obj.surviving_strength
        assert restored.verdict_justification == obj.verdict_justification
        assert restored.recommended_action == obj.recommended_action
        assert restored.action_feasibility == obj.action_feasibility
        assert restored.debate_resolved == obj.debate_resolved
        assert restored.debate_unresolved == obj.debate_unresolved
        assert restored.advocate_failures == obj.advocate_failures
        assert restored.challenger_failures == obj.challenger_failures

    def test_empty_failure_lists(self) -> None:
        obj = JudgeAudit(
            advocate_failures=[],
            challenger_failures=[],
            surviving_strength="weak",
            verdict_justification="Neither side made grounded arguments.",
            recommended_action="OPEN QUESTION: debate was unproductive.",
            action_feasibility="open_question",
            debate_resolved="Nothing.",
            debate_unresolved="Everything.",
        )
        serialized = json.dumps(obj.to_dict())
        restored = JudgeAudit.from_dict(json.loads(serialized))
        assert restored.advocate_failures == []
        assert restored.challenger_failures == []
        assert restored.action_feasibility == "open_question"


# --- PipelineStats tests ---

class TestPipelineStatsRecordCall:
    PRICING: dict[str, dict[str, float]] = {
        "claude-sonnet-4-5": {"input": 3.0, "output": 15.0},
        "claude-opus-4-5": {"input": 15.0, "output": 75.0},
    }

    def test_single_call_cost(self) -> None:
        stats = PipelineStats()
        cost = stats.record_call(
            stage="decomposer",
            model="claude-sonnet-4-5",
            input_tokens=1_000_000,
            output_tokens=1_000_000,
            pricing=self.PRICING,
        )
        assert cost == pytest.approx(18.0)  # $3 input + $15 output

    def test_accumulates_totals(self) -> None:
        stats = PipelineStats()
        stats.record_call("decomposer", "claude-sonnet-4-5", 500_000, 200_000, self.PRICING)
        stats.record_call("critic", "claude-opus-4-5", 100_000, 50_000, self.PRICING)

        assert stats.total_input_tokens == 600_000
        assert stats.total_output_tokens == 250_000
        expected_cost = (0.5 * 3.0 + 0.2 * 15.0) + (0.1 * 15.0 + 0.05 * 75.0)
        assert stats.total_cost == pytest.approx(expected_cost)

    def test_stage_costs_accumulated(self) -> None:
        stats = PipelineStats()
        stats.record_call("decomposer", "claude-sonnet-4-5", 1_000_000, 0, self.PRICING)
        stats.record_call("decomposer", "claude-sonnet-4-5", 1_000_000, 0, self.PRICING)

        assert stats.stage_costs["decomposer"] == pytest.approx(6.0)  # 2 * $3

    def test_unknown_model_zero_cost(self) -> None:
        stats = PipelineStats()
        cost = stats.record_call("stage", "unknown-model", 1_000_000, 1_000_000, self.PRICING)
        assert cost == pytest.approx(0.0)

    def test_returns_call_cost(self) -> None:
        stats = PipelineStats()
        cost = stats.record_call(
            stage="verifier",
            model="claude-opus-4-5",
            input_tokens=2_000_000,
            output_tokens=1_000_000,
            pricing=self.PRICING,
        )
        # $15 * 2 + $75 * 1 = $105
        assert cost == pytest.approx(105.0)
