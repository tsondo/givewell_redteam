"""Pipeline configuration. API keys loaded from .env via python-dotenv."""

import os
from pathlib import Path

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
