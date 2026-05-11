"""LLM-style validator agent."""

from __future__ import annotations

from typing import Any

from .llm_agent import LLMAgent, MockLLMAgent


class ValidatorAgent(LLMAgent):
    """Create a human-readable validation summary from pipeline checks."""

    def __init__(self) -> None:
        self.backend = MockLLMAgent()

    def generate(self, prompt: str, context: dict[str, Any] | None = None) -> str:
        context = context or {}
        checks = context.get("checks", {})
        issues: list[str] = []
        for name, status in checks.items():
            if not status:
                issues.append(f"failed:{name}")

        if issues:
            return self.backend.generate("validate", {"issues": issues})
        return self.backend.generate("validate", {"issues": []})
