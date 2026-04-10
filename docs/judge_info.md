# Judge Agent — Schema and Sample Output

## Final `JudgeAudit` dataclass

From `pipeline/schemas.py`:

```python
@dataclass
class JudgeAudit:
    """Structured audit of an adversarial debate by the neutral judge agent.

    Produced by run_judge after Advocate and Challenger have completed their
    exchange. The verdict and recommended_action fields supersede any values
    the Challenger may have produced in its own output.
    """

    # Failure modes detected, by side. Each entry is a "failure_type: evidence"
    # string (e.g., "unsupported_estimate_counter: 10-25% offered without derivation").
    advocate_failures: list[str]
    challenger_failures: list[str]
    # Verdict with explicit justification
    surviving_strength: str  # "strong" | "moderate" | "weak"
    verdict_justification: str  # 2-4 sentences citing specific debate moves
    # Recommended action with feasibility
    recommended_action: str  # concrete, NOT "investigate further" alone
    action_feasibility: str  # "actionable_now" | "requires_specified_evidence" | "open_question"
    # Honest summary of what the debate established
    debate_resolved: str  # 1-2 sentences on what (if anything) the debate settled
    debate_unresolved: str  # 1-2 sentences on what remains contested

    def to_dict(self) -> dict[str, Any]:
        return dataclasses.asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> JudgeAudit:
        return cls(
            advocate_failures=d.get("advocate_failures", []),
            challenger_failures=d.get("challenger_failures", []),
            surviving_strength=d["surviving_strength"],
            verdict_justification=d.get("verdict_justification", ""),
            recommended_action=d["recommended_action"],
            action_feasibility=d.get("action_feasibility", "open_question"),
            debate_resolved=d.get("debate_resolved", ""),
            debate_unresolved=d.get("debate_unresolved", ""),
        )
```

## Sample judge output

**Note:** No real judge API call was made during the implementation of this feature — the plan explicitly required no API access. The sample below is the test fixture `JUDGE_SAMPLE_MULTI_FAILURES` from `tests/test_parsing.py`, written against the format specified in `prompts/adversarial-judge.md` and verified end-to-end through `parse_judge_output` into a populated `JudgeAudit` dataclass. The first real judge outputs will be generated when VAS is re-run under a later plan.

### Raw judge response (as the judge agent is expected to emit it)

```
Some preamble from the judge before the structured output.

## ADVOCATE FAILURES

- failure_type: unsupported_estimate_fabricated
  evidence: "I estimate 10-25% with no derivation chain shown"
- failure_type: whataboutism
  evidence: "Points to GiveWell's Y instead of defending the specific X at issue"

## CHALLENGER FAILURES

- failure_type: strawmanning
  evidence: "Rebuts a claim about protection decline that was never made"
- failure_type: unsupported_estimate_counter
  evidence: "Offers 5-15% counter-range with no grounding of its own"

## DEBATE RESOLVED

The debate narrowed the plausible range from 5-50% to 10-25%, but did not
settle the mechanism question.

## DEBATE UNRESOLVED

Whether the threshold effect is linear or exponential remains contested.

## SURVIVING STRENGTH

moderate

Justification: The Challenger raised a grounded concern that the Advocate
only partially defended. Both sides traded unsupported counter-estimates,
but the underlying methodological critique survived substantively.

## RECOMMENDED ACTION

CONCLUDE NOW: The critique survives as a moderate concern; adjust the
parameter range in the CEA to reflect the narrowed bounds of 10-25%.

action_feasibility: actionable_now
```

### Parsed `JudgeAudit` (what `parse_judge_output` produces from the above)

```python
JudgeAudit(
    advocate_failures=[
        'unsupported_estimate_fabricated: I estimate 10-25% with no derivation chain shown',
        "whataboutism: Points to GiveWell's Y instead of defending the specific X at issue",
    ],
    challenger_failures=[
        'strawmanning: Rebuts a claim about protection decline that was never made',
        'unsupported_estimate_counter: Offers 5-15% counter-range with no grounding of its own',
    ],
    surviving_strength='moderate',
    verdict_justification=(
        'The Challenger raised a grounded concern that the Advocate only '
        'partially defended. Both sides traded unsupported counter-estimates, '
        'but the underlying methodological critique survived substantively.'
    ),
    recommended_action=(
        'CONCLUDE NOW: The critique survives as a moderate concern; adjust the '
        'parameter range in the CEA to reflect the narrowed bounds of 10-25%.'
    ),
    action_feasibility='actionable_now',
    debate_resolved=(
        'The debate narrowed the plausible range from 5-50% to 10-25%, but did '
        'not settle the mechanism question.'
    ),
    debate_unresolved='Whether the threshold effect is linear or exponential remains contested.',
)
```
