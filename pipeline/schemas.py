from __future__ import annotations

import dataclasses
from dataclasses import dataclass, field
from typing import Any


@dataclass
class InvestigationThread:
    name: str
    scope: str
    key_questions: list[str]
    cea_parameters_affected: list[str]
    relevant_sources: list[str]
    out_of_scope: str
    context_md: str

    def to_dict(self) -> dict[str, Any]:
        return dataclasses.asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> InvestigationThread:
        return cls(
            name=d["name"],
            scope=d["scope"],
            key_questions=d["key_questions"],
            cea_parameters_affected=d["cea_parameters_affected"],
            relevant_sources=d["relevant_sources"],
            out_of_scope=d["out_of_scope"],
            context_md=d["context_md"],
        )


@dataclass
class DecomposerOutput:
    threads: list[InvestigationThread]
    exclusion_list: list[str]
    cea_parameter_map: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "threads": [t.to_dict() for t in self.threads],
            "exclusion_list": self.exclusion_list,
            "cea_parameter_map": self.cea_parameter_map,
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> DecomposerOutput:
        return cls(
            threads=[InvestigationThread.from_dict(t) for t in d["threads"]],
            exclusion_list=d["exclusion_list"],
            cea_parameter_map=d["cea_parameter_map"],
        )


@dataclass
class CandidateCritique:
    thread_name: str
    title: str
    hypothesis: str
    mechanism: str
    parameters_affected: list[str]
    suggested_evidence: list[str]
    estimated_direction: str  # "increases"|"decreases"|"uncertain"
    estimated_magnitude: str  # "large"|"medium"|"small"|"unknown"

    def to_dict(self) -> dict[str, Any]:
        return dataclasses.asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> CandidateCritique:
        return cls(
            thread_name=d["thread_name"],
            title=d["title"],
            hypothesis=d["hypothesis"],
            mechanism=d["mechanism"],
            parameters_affected=d["parameters_affected"],
            suggested_evidence=d["suggested_evidence"],
            estimated_direction=d["estimated_direction"],
            estimated_magnitude=d["estimated_magnitude"],
        )


@dataclass
class VerifiedCritique:
    original: CandidateCritique
    verdict: str  # "verified"|"partially_verified"|"unverified"|"rejected"
    evidence_found: list[str]
    evidence_strength: str  # "strong"|"moderate"|"weak"
    counter_evidence: list[str]
    caveats: list[str]
    revised_hypothesis: str | None

    def to_dict(self) -> dict[str, Any]:
        return {
            "original": self.original.to_dict(),
            "verdict": self.verdict,
            "evidence_found": self.evidence_found,
            "evidence_strength": self.evidence_strength,
            "counter_evidence": self.counter_evidence,
            "caveats": self.caveats,
            "revised_hypothesis": self.revised_hypothesis,
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> VerifiedCritique:
        return cls(
            original=CandidateCritique.from_dict(d["original"]),
            verdict=d["verdict"],
            evidence_found=d["evidence_found"],
            evidence_strength=d["evidence_strength"],
            counter_evidence=d["counter_evidence"],
            caveats=d["caveats"],
            revised_hypothesis=d.get("revised_hypothesis"),
        )


@dataclass
class QuantifiedCritique:
    critique: VerifiedCritique
    target_parameters: list[dict[str, Any]]
    alternative_range: list[dict[str, Any]]
    sensitivity_results: dict[str, Any]
    materiality: str  # "material"|"notable"|"immaterial"
    interaction_effects: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "critique": self.critique.to_dict(),
            "target_parameters": self.target_parameters,
            "alternative_range": self.alternative_range,
            "sensitivity_results": self.sensitivity_results,
            "materiality": self.materiality,
            "interaction_effects": self.interaction_effects,
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> QuantifiedCritique:
        return cls(
            critique=VerifiedCritique.from_dict(d["critique"]),
            target_parameters=d["target_parameters"],
            alternative_range=d["alternative_range"],
            sensitivity_results=d["sensitivity_results"],
            materiality=d["materiality"],
            interaction_effects=d["interaction_effects"],
        )


@dataclass
class DebatedCritique:
    critique: QuantifiedCritique
    advocate_defense: str
    challenger_rebuttal: str
    surviving_strength: str  # "strong"|"moderate"|"weak"
    key_unresolved: list[str]
    recommended_action: str  # "investigate"|"adjust_model"|"monitor"|"dismiss"

    def to_dict(self) -> dict[str, Any]:
        return {
            "critique": self.critique.to_dict(),
            "advocate_defense": self.advocate_defense,
            "challenger_rebuttal": self.challenger_rebuttal,
            "surviving_strength": self.surviving_strength,
            "key_unresolved": self.key_unresolved,
            "recommended_action": self.recommended_action,
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> DebatedCritique:
        return cls(
            critique=QuantifiedCritique.from_dict(d["critique"]),
            advocate_defense=d["advocate_defense"],
            challenger_rebuttal=d["challenger_rebuttal"],
            surviving_strength=d["surviving_strength"],
            key_unresolved=d["key_unresolved"],
            recommended_action=d["recommended_action"],
        )


@dataclass
class PipelineStats:
    total_input_tokens: int = 0
    total_output_tokens: int = 0
    total_cost: float = 0.0
    stage_costs: dict[str, float] = field(default_factory=dict)
    cost_warning_threshold: float = 15.0  # default; overridden per-intervention at run start

    def record_call(
        self,
        stage: str,
        model: str,
        input_tokens: int,
        output_tokens: int,
        pricing: dict[str, dict[str, float]],
    ) -> float:
        """Record a single API call and return the cost of that call.

        pricing format: {"model_id": {"input": <per_million>, "output": <per_million>}}
        """
        model_pricing = pricing.get(model, {"input": 0.0, "output": 0.0})
        input_cost = (input_tokens / 1_000_000) * model_pricing["input"]
        output_cost = (output_tokens / 1_000_000) * model_pricing["output"]
        call_cost = input_cost + output_cost

        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens
        self.total_cost += call_cost
        self.stage_costs[stage] = self.stage_costs.get(stage, 0.0) + call_cost

        return call_cost
