"""Hierarchy extraction utilities."""

from __future__ import annotations

from typing import Any


class HierarchyExtractor:
    """Extract a simple hierarchy tree from parser output."""

    def extract_hierarchy(self, ast: dict[str, Any]) -> dict[str, Any]:
        hierarchy = ast.get("hierarchy", {})
        if hierarchy:
            return hierarchy

        model_name = ast.get("model_name", "UnknownModel")
        children = [c.get("name") for c in ast.get("components", []) if c.get("name")]
        return {"model": model_name, "children": children}
