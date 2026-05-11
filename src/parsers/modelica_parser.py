"""Modelica parser for lightweight structural extraction.

This parser intentionally focuses on structural elements that are needed by the
transformation pipeline: model name, parameters, components, connections, and
equations.
"""

from __future__ import annotations

import re
from typing import Any


class ModelicaParser:
    """Parse Modelica text into a simplified AST-like dictionary."""

    _MODEL_RE = re.compile(r"\bmodel\s+([A-Za-z_][A-Za-z0-9_]*)")
    _PARAM_RE = re.compile(
        r"\bparameter\s+([A-Za-z_][A-Za-z0-9_]*)\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*([^;]+);"
    )
    _COMPONENT_RE = re.compile(
        r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s+([A-Za-z_][A-Za-z0-9_]*)\s*;\s*$"
    )
    _CONNECT_RE = re.compile(r"\bconnect\s*\(\s*([^,\s]+)\s*,\s*([^\)\s]+)\s*\)\s*;")
    _EQUATION_RE = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_\.]*)\s*=\s*([^;]+);\s*$")

    def parse(self, modelica_code: str) -> Any:
        """Parse Modelica code into a dict with structural sections."""
        model_match = self._MODEL_RE.search(modelica_code)
        model_name = model_match.group(1) if model_match else "UnknownModel"

        parameters = []
        for ptype, name, value in self._PARAM_RE.findall(modelica_code):
            parameters.append({"name": name, "type": ptype, "value": value.strip()})

        components = []
        in_equation = False
        for line in modelica_code.splitlines():
            line_stripped = line.strip()
            if not line_stripped or line_stripped.startswith("//"):
                continue
            if line_stripped == "equation":
                in_equation = True
                continue
            if line_stripped.startswith("parameter ") or line_stripped.startswith("model "):
                continue
            if line_stripped.startswith("end "):
                continue
            if in_equation:
                continue
            comp_match = self._COMPONENT_RE.match(line)
            if comp_match:
                ctype, name = comp_match.groups()
                components.append({"name": name, "type": ctype})

        connections = []
        for src, dst in self._CONNECT_RE.findall(modelica_code):
            connections.append({"from": src, "to": dst})

        equations = []
        for line in modelica_code.splitlines():
            eq_match = self._EQUATION_RE.match(line)
            if eq_match:
                lhs, rhs = eq_match.groups()
                equations.append({"lhs": lhs.strip(), "rhs": rhs.strip()})

        hierarchy = {
            "model": model_name,
            "children": [component["name"] for component in components],
        }

        return {
            "model_name": model_name,
            "components": components,
            "connections": connections,
            "parameters": parameters,
            "equations": equations,
            "hierarchy": hierarchy,
        }
