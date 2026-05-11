"""AST-level alignment checks between source IR and generated SysML AST."""

from __future__ import annotations

from typing import Any


class ASTValidator:
    """Compare component and parameter name sets between both ASTs."""

    def validate(self, modelica_ast: Any, sysml_ast: Any) -> bool:
        src_components = {item.get("name") for item in modelica_ast.get("components", [])}
        dst_components = {item.get("name") for item in sysml_ast.get("components", [])}

        src_parameters = {item.get("name") for item in modelica_ast.get("parameters", [])}
        dst_parameters = {item.get("name") for item in sysml_ast.get("parameters", [])}

        src_components.discard(None)
        dst_components.discard(None)
        src_parameters.discard(None)
        dst_parameters.discard(None)

        return src_components.issubset(dst_components) and src_parameters.issubset(dst_parameters)
