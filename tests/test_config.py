"""Tests for per-intervention verifier overrides."""
from __future__ import annotations

from pipeline.config import (
    COST_WARNING_PER_INTERVENTION,
    MAX_TOKENS_VERIFIER,
    VERIFIER_ALLOWED_DOMAINS,
    VERIFIER_MAX_SEARCHES,
    get_verifier_settings,
)
from pipeline.schemas import PipelineStats


class TestVerifierSettingsDefaults:
    """Interventions without overrides receive module-level defaults."""

    def test_water_chlorination_uses_defaults(self):
        s = get_verifier_settings("water-chlorination")
        assert s["max_searches"] == VERIFIER_MAX_SEARCHES
        assert s["max_tokens"] == MAX_TOKENS_VERIFIER
        assert s["cost_warning"] == COST_WARNING_PER_INTERVENTION
        assert s["allowed_domains"] == VERIFIER_ALLOWED_DOMAINS

    def test_itns_uses_defaults(self):
        s = get_verifier_settings("itns")
        assert s["max_searches"] == VERIFIER_MAX_SEARCHES
        assert s["allowed_domains"] == VERIFIER_ALLOWED_DOMAINS

    def test_smc_uses_defaults(self):
        s = get_verifier_settings("smc")
        assert s["max_searches"] == VERIFIER_MAX_SEARCHES

    def test_unknown_intervention_uses_defaults(self):
        s = get_verifier_settings("nonexistent")
        assert s["max_searches"] == VERIFIER_MAX_SEARCHES
        assert s["cost_warning"] == COST_WARNING_PER_INTERVENTION


class TestVerifierSettingsVAS:
    """VAS overrides apply correctly."""

    def test_vas_max_searches_raised(self):
        assert get_verifier_settings("vas")["max_searches"] == 8

    def test_vas_max_tokens_raised(self):
        assert get_verifier_settings("vas")["max_tokens"] == 6144

    def test_vas_cost_warning_raised(self):
        assert get_verifier_settings("vas")["cost_warning"] == 40.0

    def test_vas_includes_dhs(self):
        assert "dhsprogram.com" in get_verifier_settings("vas")["allowed_domains"]

    def test_vas_includes_grantees(self):
        domains = get_verifier_settings("vas")["allowed_domains"]
        assert "helenkellerintl.org" in domains
        assert "nutritionintl.org" in domains

    def test_vas_includes_ihme(self):
        domains = get_verifier_settings("vas")["allowed_domains"]
        assert "healthdata.org" in domains

    def test_vas_retains_default_domains(self):
        """Override should be additive, not replacement."""
        domains = get_verifier_settings("vas")["allowed_domains"]
        for default_domain in VERIFIER_ALLOWED_DOMAINS:
            assert default_domain in domains, f"Lost default: {default_domain}"


class TestPipelineStatsCostThreshold:
    """Cost warning threshold is set per-intervention via PipelineStats."""

    def test_default_threshold(self):
        stats = PipelineStats()
        assert stats.cost_warning_threshold == 15.0

    def test_vas_threshold_from_settings(self):
        stats = PipelineStats()
        stats.cost_warning_threshold = get_verifier_settings("vas")["cost_warning"]
        assert stats.cost_warning_threshold == 40.0

    def test_itns_threshold_unchanged(self):
        stats = PipelineStats()
        stats.cost_warning_threshold = get_verifier_settings("itns")["cost_warning"]
        assert stats.cost_warning_threshold == COST_WARNING_PER_INTERVENTION
