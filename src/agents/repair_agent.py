"""LLM-style repair agent."""

from __future__ import annotations

from typing import Any

from .llm_agent import LLMAgent, MockLLMAgent


class RepairAgent(LLMAgent):
    """Apply deterministic repairs while preserving LLM-compatible interface."""

    def __init__(self) -> None:
        self.backend = MockLLMAgent()

    def generate(self, prompt: str, context: dict[str, Any] | None = None) -> str:
        context = context or {}
        candidate = str(context.get("candidate", ""))
        repaired = self.backend.generate("repair", {"candidate": candidate})

        if "block" not in repaired:
            model_name = str(context.get("model_name", "RecoveredModel"))
            repaired = f"block {model_name} {{\n  // repaired\n}}"

        return repaired
