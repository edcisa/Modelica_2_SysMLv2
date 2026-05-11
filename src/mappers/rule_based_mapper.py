"""Deterministic transformation from Modelica IR to SysML v2 text."""

from __future__ import annotations

from typing import Any


class RuleBasedMapper:
    """Generate a baseline SysML v2 representation from Modelica IR."""

    def map(self, ir: dict[str, Any]) -> str:
        model_name = str(ir.get("model_name", "UnnamedModel"))
        parameters = ir.get("parameters", [])
        components = ir.get("components", [])
        connections = ir.get("connections", [])
        equations = ir.get("equations", [])

        lines = [f"block {model_name} {{"]

        for parameter in parameters:
            p_name = parameter.get("name", "p")
            p_type = parameter.get("type", "Real")
            p_value = parameter.get("value", "0")
            lines.append(f"  attribute {p_name}: {p_type} = {p_value};")

        for component in components:
            c_name = component.get("name", "c")
            c_type = component.get("type", "Part")
            lines.append(f"  part {c_name}: {c_type};")

        for connection in connections:
            src = connection.get("from", "src")
            dst = connection.get("to", "dst")
            lines.append(f"  connect {src} to {dst};")

        for index, equation in enumerate(equations, start=1):
            lhs = equation.get("lhs", "lhs")
            rhs = equation.get("rhs", "rhs")
            lines.append(f"  constraint eq{index}: {lhs} == {rhs};")

        lines.append("}")
        return "\n".join(lines)
