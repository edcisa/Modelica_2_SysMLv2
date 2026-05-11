"""LLM agent abstractions and deterministic local mock adapter."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

class LLMAgent(ABC):
    """
    Abstract base class for LLM-based agents.
    """
    @abstractmethod
    def generate(self, prompt: str, context: dict[str, Any] | None = None) -> str:
        """Generate text output from a prompt and optional structured context."""
        raise NotImplementedError

class MockLLMAgent(LLMAgent):
    """Deterministic stand-in for an LLM provider.

    This keeps the repository reproducible while preserving architecture and
    integration seams for a real API-backed implementation.
    """

    def generate(self, prompt: str, context: dict[str, Any] | None = None) -> str:
        context = context or {}
        if "repair" in prompt.lower():
            candidate = str(context.get("candidate", ""))
            fixed = candidate.replace(" = ", " == ")
            return fixed if fixed else "// repaired sysml candidate"

        if "validate" in prompt.lower():
            issues = context.get("issues", [])
            if issues:
                return f"invalid: {len(issues)} issues"
            return "valid: 0 issues"

        return str(context.get("candidate", prompt))
