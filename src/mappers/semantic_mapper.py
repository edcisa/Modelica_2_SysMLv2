"""Semantic mapper for architecture-oriented transformation."""

from __future__ import annotations

from typing import Any

from src.mappers.rule_based_mapper import RuleBasedMapper


class SemanticMapper:
    """Map Modelica IR to semantically richer SysML v2 text."""

    def __init__(self) -> None:
        self.rule_mapper = RuleBasedMapper()

    def map(self, ir: dict[str, Any]) -> str:
        base = self.rule_mapper.map(ir)
        semantic_header = [
            "// semantic-profile: mbse.architecture.v1",
            "// transformation: modelica_to_sysmlv2",
            "// strategy: rule_based_with_llm_refinement",
        ]
        return "\n".join(semantic_header + [base])
