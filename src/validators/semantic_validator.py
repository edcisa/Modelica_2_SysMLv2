"""Semantic validation for transformation quality control."""

from __future__ import annotations

from typing import Any


class SemanticValidator:
    """Check whether key semantics from source IR are preserved in generated code."""

    def validate(self, modelica_ir: Any, sysml_code: str) -> bool:
        if not sysml_code.strip():
            return False

        equations = modelica_ir.get("equations", [])
        if not equations:
            return True

        preserved = 0
        for equation in equations:
            lhs = str(equation.get("lhs", "")).strip()
            rhs = str(equation.get("rhs", "")).strip()
            if lhs and rhs and lhs in sysml_code and rhs in sysml_code:
                preserved += 1

        return preserved == len(equations)
