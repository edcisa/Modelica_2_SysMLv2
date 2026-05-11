"""Structural validation for generated SysML code."""

from __future__ import annotations

from typing import Any


class StructuralValidator:
    """Check that generated text references expected structural elements."""

    def validate(self, sysml_code: str, reference_ir: Any) -> bool:
        if not sysml_code.strip():
            return False

        required_names = []
        for parameter in reference_ir.get("parameters", []):
            required_names.append(parameter.get("name", ""))
        for component in reference_ir.get("components", []):
            required_names.append(component.get("name", ""))

        required_names = [name for name in required_names if name]
        return all(name in sysml_code for name in required_names)
