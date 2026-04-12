# BaseCEA Protocol — Implementation Plan

> **For Claude Code:** Use targeted `str_replace` edits, not full file rewrites. No API access required for any task in this plan.

**Goal:** Define an explicit interface contract for CEA reader classes (`WaterCEA`, `ITNCEA`, `MalariaCEA`, `VASCEA`) so that missing-attribute bugs surface at class-definition time rather than mid-pipeline. Prevents the class of bug that crashed the live VAS run at quantifier critique 5/31 (`PROGRAMS` attribute missing from `VASCEA`).

**Architecture:** A `typing.Protocol` named `CEAReader` in `pipeline/spreadsheet.py` declares the required interface. A test in `tests/test_spreadsheet.py` instantiates each concrete class and checks both attribute presence and basic call behavior. Using `Protocol` rather than ABC means we don't need to retrofit inheritance into existing classes — they conform structurally.

**Tech Stack:** Python 3.12, typing.Protocol, pytest

---

## File Map

| Action | File | Responsibility |
|--------|------|----------------|
| Modify | `pipeline/spreadsheet.py` | Add `CEAReader` Protocol at top of file |
| Modify | `tests/test_spreadsheet.py` | Add `TestCEAReaderInterface` test class |

---

### Task 1: Define the `CEAReader` Protocol

**Files:**
- Modify: `pipeline/spreadsheet.py`

- [ ] **Step 1: Determine the actual contract from existing usage**

Before writing the Protocol, grep the pipeline to find every attribute and method that `pipeline/agents.py` and `pipeline/run_pipeline.py` access on a CEA instance. Record the full set of accessed members. Expected (verify against the grep):

- `PROGRAMS` (class attribute, tuple of program/location keys)
- `get_parameter_summary()` → str
- `compute_cost_effectiveness(program_key, **overrides)` → float
- `detect_cap_binding(program_key, **overrides)` → bool
- `run_sensitivity(program_key, parameter_name, low, central, high)` → dict[str, Any]
- `locations` (dict, used by VAS-specific code paths)

If the grep surfaces additional members not in this list, **stop and report** before writing the Protocol. The contract should match reality, not the list above.

- [ ] **Step 2: Add the Protocol definition**

Add the following block immediately after the existing imports at the top of `pipeline/spreadsheet.py`:

```python
from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class CEAReader(Protocol):
    """Interface contract for CEA spreadsheet readers.

    Every concrete CEA class consumed by the pipeline must implement these
    members. The pipeline's quantifier stage iterates `PROGRAMS` to run
    cross-program sensitivity analysis; missing this attribute caused a
    mid-run crash on the VAS pipeline (quantifier critique 5/31, fixed in
    a prior commit). This Protocol exists to surface that class of bug at
    test time rather than at run time.

    Note: this is a structural Protocol (PEP 544), not an ABC. Existing
    classes conform automatically without inheriting — we only use it for
    isinstance checks in tests.
    """

    PROGRAMS: tuple[str, ...]

    def get_parameter_summary(self) -> str:
        """Return a markdown-formatted summary of CEA parameters for LLM agents."""
        ...

    def compute_cost_effectiveness(
        self, program_key: str, **overrides: float
    ) -> float:
        """Return the CE multiple for a program, optionally with parameter overrides.

        Implementations that read pre-computed values (rather than replicating
        the formula chain) should raise NotImplementedError if overrides are
        passed, to fail loud rather than silently returning stale values.
        """
        ...

    def detect_cap_binding(self, program_key: str, **overrides: float) -> bool:
        """Return True if the plausibility cap binds at the given parameter values."""
        ...

    def run_sensitivity(
        self,
        program_key: str,
        parameter_name: str,
        low: float,
        central: float,
        high: float,
    ) -> dict[str, Any]:
        """Run sensitivity analysis on a parameter and return structured results."""
        ...
```

If `Any` is already imported from typing, adjust the import line rather than duplicating it.

- [ ] **Step 3: Verify the Protocol imports cleanly**

Confirm `CEAReader`, `WaterCEA`, `ITNCEA`, `MalariaCEA`, and `VASCEA` all import from `pipeline.spreadsheet` without error, and that `CEAReader` is recognized as a Protocol.

---

### Task 2: Add interface conformance tests

**Files:**
- Modify: `tests/test_spreadsheet.py`

- [ ] **Step 1: Add the test class**

Append to `tests/test_spreadsheet.py`:

```python
from pipeline.spreadsheet import CEAReader, ITNCEA, MalariaCEA, VASCEA, WaterCEA


WATER_DATA_PATH = Path(__file__).parent.parent / "data" / "WaterCEA.xlsx"
ITN_DATA_PATH = Path(__file__).parent.parent / "data" / "InsecticideCEA.xlsx"
MALARIA_DATA_PATH = Path(__file__).parent.parent / "data" / "MalariaCEA.xlsx"
# VAS_DATA_PATH already defined earlier in the file


@pytest.fixture(scope="module")
def all_ceas() -> dict[str, CEAReader]:
    """Instantiate every concrete CEA class once for interface testing."""
    return {
        "water": WaterCEA(WATER_DATA_PATH),
        "itns": ITNCEA(ITN_DATA_PATH),
        "smc": MalariaCEA(MALARIA_DATA_PATH),
        "vas": VASCEA(VAS_DATA_PATH),
    }


class TestCEAReaderInterface:
    """Verify every CEA class conforms to the CEAReader Protocol.

    This catches missing-attribute bugs at test time. The original motivation
    was a mid-run crash on VAS at quantifier critique 5/31 caused by VASCEA
    missing the PROGRAMS class attribute that parse_quantifier_output iterates.
    """

    @pytest.mark.parametrize("name", ["water", "itns", "smc", "vas"])
    def test_isinstance_check(self, all_ceas: dict[str, CEAReader], name: str) -> None:
        """Each CEA class is recognized as a CEAReader by runtime isinstance."""
        cea = all_ceas[name]
        assert isinstance(cea, CEAReader), (
            f"{type(cea).__name__} does not satisfy the CEAReader Protocol. "
            f"Check that all required members are present."
        )

    @pytest.mark.parametrize("name", ["water", "itns", "smc", "vas"])
    def test_programs_is_tuple_of_strings(
        self, all_ceas: dict[str, CEAReader], name: str
    ) -> None:
        cea = all_ceas[name]
        assert isinstance(cea.PROGRAMS, tuple), (
            f"{type(cea).__name__}.PROGRAMS must be a tuple"
        )
        assert len(cea.PROGRAMS) > 0, f"{type(cea).__name__}.PROGRAMS is empty"
        assert all(isinstance(p, str) for p in cea.PROGRAMS), (
            f"{type(cea).__name__}.PROGRAMS must contain only strings"
        )

    @pytest.mark.parametrize("name", ["water", "itns", "smc", "vas"])
    def test_get_parameter_summary_returns_nonempty_string(
        self, all_ceas: dict[str, CEAReader], name: str
    ) -> None:
        cea = all_ceas[name]
        summary = cea.get_parameter_summary()
        assert isinstance(summary, str)
        assert len(summary) > 500, (
            f"{type(cea).__name__}.get_parameter_summary() returned only "
            f"{len(summary)} chars; expected > 500"
        )

    @pytest.mark.parametrize("name", ["water", "itns", "smc", "vas"])
    def test_compute_cost_effectiveness_baseline(
        self, all_ceas: dict[str, CEAReader], name: str
    ) -> None:
        """compute_cost_effectiveness returns a float for the first program key."""
        cea = all_ceas[name]
        first_program = cea.PROGRAMS[0]
        result = cea.compute_cost_effectiveness(first_program)
        assert isinstance(result, (int, float))
        assert result > 0, (
            f"{type(cea).__name__}.compute_cost_effectiveness({first_program!r}) "
            f"returned {result}; expected > 0"
        )

    @pytest.mark.parametrize("name", ["water", "itns", "smc", "vas"])
    def test_detect_cap_binding_returns_bool(
        self, all_ceas: dict[str, CEAReader], name: str
    ) -> None:
        cea = all_ceas[name]
        first_program = cea.PROGRAMS[0]
        result = cea.detect_cap_binding(first_program)
        assert isinstance(result, bool)

    def test_vas_compute_with_overrides_raises(
        self, all_ceas: dict[str, CEAReader]
    ) -> None:
        """VASCEA explicitly fails loud on overrides since it can't recompute."""
        vas = all_ceas["vas"]
        first_program = vas.PROGRAMS[0]
        with pytest.raises(NotImplementedError):
            vas.compute_cost_effectiveness(first_program, some_param=1.0)
```

- [ ] **Step 2: Run the new tests**

Expected: all tests pass. If any fail:

- **Protocol isinstance fails for an existing class** — that class is missing a member declared in the Protocol. Either add the member to the class, or (if the member shouldn't be required) remove it from the Protocol. **Stop and report** before deciding which.
- **`compute_cost_effectiveness` returns 0 or negative** — the test's "first program key" might not have valid data. Adjust the test to pick a known-good program key for that CEA.
- **`detect_cap_binding` returns non-bool** — the existing implementation returns the wrong type. Fix the implementation.

- [ ] **Step 3: Run the full test suite to confirm no regressions**

Expected: all prior tests + new interface tests all pass.

---

### Task 3: Commit

Single commit covering both files. Commit message should explain: this defines a runtime-checkable Protocol that every concrete CEA class must satisfy, motivated by the missing PROGRAMS attribute that crashed the live VAS run at quantifier critique 5/31. Uses Protocol rather than ABC so existing classes conform structurally without inheritance changes. References the prior commit that added PROGRAMS to VASCEA as a one-off fix.

---

## Stop Conditions Requiring Tsondo Input

- Grep in Task 1 Step 1 surfaces additional accessed members beyond the expected list
- Protocol conformance test fails for water/itns/smc (not VAS) — means those classes have implicit gaps that haven't surfaced yet, worth a human decision
- Any test failure that requires modifying a concrete CEA class implementation

## Things You Should NOT Do

- Modify any concrete CEA class implementations as part of this plan unless a test failure makes it strictly necessary, and even then, stop and confirm first
- Refactor the Protocol or split it across files
- Add ABC inheritance to existing classes
- Activate the API key (no API access required)
