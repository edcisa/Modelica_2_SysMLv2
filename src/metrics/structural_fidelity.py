"""Structural fidelity metrics for Modelica-to-SysML transformation."""

from __future__ import annotations

from typing import Any


def _safe_ratio(overlap: int, reference_total: int) -> float:
    if reference_total <= 0:
        return 1.0
    return round(overlap / reference_total, 4)


class StructuralFidelityMetrics:
    """Compute element-wise fidelity against a reference IR/AST."""

    def compute(self, generated_ast: Any, reference_ast: Any) -> dict[str, float]:
        ref_components = {c.get("name") for c in reference_ast.get("components", []) if c.get("name")}
        gen_components = {c.get("name") for c in generated_ast.get("components", []) if c.get("name")}

        ref_parameters = {p.get("name") for p in reference_ast.get("parameters", []) if p.get("name")}
        gen_parameters = {p.get("name") for p in generated_ast.get("parameters", []) if p.get("name")}

        ref_connections = {
            (c.get("from"), c.get("to"))
            for c in reference_ast.get("connections", [])
            if c.get("from") and c.get("to")
        }
        gen_connections = {
            (c.get("from"), c.get("to"))
            for c in generated_ast.get("connections", [])
            if c.get("from") and c.get("to")
        }

        component_fidelity = _safe_ratio(len(ref_components & gen_components), len(ref_components))
        parameter_fidelity = _safe_ratio(len(ref_parameters & gen_parameters), len(ref_parameters))
        connection_fidelity = _safe_ratio(len(ref_connections & gen_connections), len(ref_connections))

        structural_fidelity = round(
            (component_fidelity + parameter_fidelity + connection_fidelity) / 3.0,
            4,
        )

        return {
            "component_fidelity": component_fidelity,
            "connection_fidelity": connection_fidelity,
            "parameter_fidelity": parameter_fidelity,
            "structural_fidelity": structural_fidelity,
        }
