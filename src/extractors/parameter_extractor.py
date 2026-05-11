"""Parameter extraction utilities."""

from __future__ import annotations

from typing import Any


class ParameterExtractor:
    """Extract normalized parameter entries from parser output."""

    def extract_parameters(self, ast: dict[str, Any]) -> list[dict[str, Any]]:
        parameters: list[dict[str, Any]] = []
        seen: set[str] = set()

        for parameter in ast.get("parameters", []):
            name = str(parameter.get("name", "")).strip()
            if not name or name in seen:
                continue
            seen.add(name)
            parameters.append(
                {
                    "name": name,
                    "type": str(parameter.get("type", "Real")).strip() or "Real",
                    "value": parameter.get("value", "0"),
                    "kind": "parameter",
                }
            )

        return parameters
