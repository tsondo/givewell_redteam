"""Pipeline configuration. API keys loaded from .env via python-dotenv."""

import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

load_dotenv()

# API
ANTHROPIC_API_KEY: str = os.environ["ANTHROPIC_API_KEY"]
OPUS_MODEL: str = "claude-opus-4-20250514"
SONNET_MODEL: str = "claude-sonnet-4-20250514"

# Paths
REPO_ROOT: Path = Path(__file__).parent.parent
PROMPTS_DIR: Path = REPO_ROOT / "prompts"
DATA_DIR: Path = REPO_ROOT / "data"
RESULTS_DIR: Path = REPO_ROOT / "results"

# Pipeline settings
MAX_RETRIES: int = 2
MAX_TOKENS_DECOMPOSER: int = 8192
MAX_TOKENS_INVESTIGATOR: int = 4096
MAX_TOKENS_VERIFIER: int = 4096
MAX_TOKENS_QUANTIFIER: int = 8192
MAX_TOKENS_ADVERSARIAL: int = 3072
MAX_TOKENS_SYNTHESIZER: int = 8192

# Verifier web search settings
VERIFIER_MAX_SEARCHES: int = 5  # max web searches per verifier call
VERIFIER_BATCH_SIZE: int = 3   # critiques per verifier API call
VERIFIER_ALLOWED_DOMAINS: list[str] = [
    "givewell.org",
    "who.int",
    "ncbi.nlm.nih.gov",
    "pubmed.ncbi.nlm.nih.gov",
    "scholar.google.com",
    "thelancet.com",
    "bmj.com",
    "nature.com",
    "cochranelibrary.com",
    "worldbank.org",
    "unicef.org",
]

# ---------------------------------------------------------------------------
# Per-intervention verifier overrides
# ---------------------------------------------------------------------------
# Each intervention may override any of: allowed_domains, max_searches,
# max_tokens, cost_warning. Keys not present fall back to the module-level
# defaults above. This exists because different interventions need different
# evidence-quality / cost trade-offs (e.g., VAS depends on DHS prevalence
# data and grantee implementation reports that aren't on the default list).

INTERVENTION_VERIFIER_OVERRIDES: dict[str, dict[str, Any]] = {
    "vas": {
        "allowed_domains": [
            # Defaults retained
            "givewell.org",
            "who.int",
            "ncbi.nlm.nih.gov",
            "pubmed.ncbi.nlm.nih.gov",
            "scholar.google.com",
            "thelancet.com",
            "bmj.com",
            "nature.com",
            "cochranelibrary.com",
            "worldbank.org",
            "unicef.org",
            # Tier 1 — prevalence and implementation data
            "dhsprogram.com",
            "childmortality.org",
            "healthdata.org",
            "ghdx.healthdata.org",
            "helenkellerintl.org",
            "nutritionintl.org",
            # Tier 2 — expanded biomedical access
            "europepmc.org",
            "nejm.org",
            "ajcn.nutrition.org",
            "journals.plos.org",
            "micronutrient.org",
            "micronutrientforum.org",
            # Tier 3 — structural debate sources
            "lshtm.ac.uk",
            "jhsph.edu",
            "gainhealth.org",
            "advancingnutrition.org",
        ],
        "max_searches": 8,
        "max_tokens": 6144,
        "cost_warning": 40.0,
    },
}


def get_verifier_settings(intervention: str) -> dict[str, Any]:
    """Return verifier settings for an intervention, merging overrides with defaults.

    Always returns a dict with all four keys populated. Interventions without
    an override entry receive the module-level defaults unchanged.
    """
    overrides = INTERVENTION_VERIFIER_OVERRIDES.get(intervention, {})
    return {
        "allowed_domains": overrides.get("allowed_domains", VERIFIER_ALLOWED_DOMAINS),
        "max_searches": overrides.get("max_searches", VERIFIER_MAX_SEARCHES),
        "max_tokens": overrides.get("max_tokens", MAX_TOKENS_VERIFIER),
        "cost_warning": overrides.get("cost_warning", COST_WARNING_PER_INTERVENTION),
    }


# Cost thresholds (warn, don't stop)
COST_WARNING_PER_INTERVENTION: float = 15.0

# Materiality thresholds
MATERIALITY_THRESHOLD: float = 0.01  # 1% change = "notable"
HIGH_MATERIALITY_THRESHOLD: float = 0.10  # 10% change = "material"

# Pricing per million tokens (as of 2025)
PRICING: dict[str, dict[str, float]] = {
    OPUS_MODEL: {"input": 15.0, "output": 75.0},
    SONNET_MODEL: {"input": 3.0, "output": 15.0},
}

# Intervention source URLs
INTERVENTION_URLS: dict[str, dict[str, str]] = {
    "water-chlorination": {
        "report": "https://www.givewell.org/international/technical/programs/water-quality-interventions",
        "baseline": "https://docs.google.com/document/d/1l8baZ_9zQ3FDmmEI50L0T2KqzoEhow6lNXjgLKUhGUg/",
        "spreadsheet": "WaterCEA.xlsx",
    },
    "itns": {
        "report": "https://www.givewell.org/international/technical/programs/insecticide-treated-nets",
        "baseline": "https://docs.google.com/document/d/16iIzH_KneLjlRSAc-2ZLO4aWdNB48CZ0LWH7sRe8yFo/",
        "spreadsheet": "InsecticideCEA.xlsx",
    },
    "smc": {
        "report": "https://www.givewell.org/international/technical/programs/seasonal-malaria-chemoprevention",
        "baseline": "https://docs.google.com/document/d/1562HtXfGOQ3EYOWgDnCAV_s6uF2zbPmRAqZ817_lNpA/",
        "spreadsheet": "MalariaCEA.xlsx",
    },
}
