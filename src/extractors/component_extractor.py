"""Component extraction utilities."""

from __future__ import annotations

from typing import Any


class ComponentExtractor:
    """Extract normalized component entries from parser output."""

    def extract_components(self, ast: dict[str, Any]) -> list[dict[str, Any]]:
        components: list[dict[str, Any]] = []
        seen: set[tuple[str, str]] = set()

        for component in ast.get("components", []):
            name = str(component.get("name", "")).strip()
            ctype = str(component.get("type", "UnknownType")).strip() or "UnknownType"
            if not name:
                continue
            key = (name, ctype)
            if key in seen:
                continue
            seen.add(key)
            components.append({"name": name, "type": ctype, "kind": "component"})

        return components
