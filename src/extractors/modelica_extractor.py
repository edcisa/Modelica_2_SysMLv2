"""Modelica extraction interfaces and default implementation."""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

from src.extractors.component_extractor import ComponentExtractor
from src.extractors.connection_extractor import ConnectionExtractor
from src.extractors.hierarchy_extractor import HierarchyExtractor
from src.extractors.parameter_extractor import ParameterExtractor
from src.parsers.modelica_parser import ModelicaParser

class ModelicaExtractor(ABC):
    """
    Abstract base class for Modelica model extraction.
    """
    @abstractmethod
    def extract(self, model_path: str) -> dict[str, Any]:
        """Extracts model structure from a Modelica file."""
        raise NotImplementedError

class OpenModelicaExtractor(ModelicaExtractor):
    """
    OpenModelica-based extractor (OMPython integration).
    """
    def __init__(self) -> None:
        self.parser = ModelicaParser()
        self.component_extractor = ComponentExtractor()
        self.connection_extractor = ConnectionExtractor()
        self.parameter_extractor = ParameterExtractor()
        self.hierarchy_extractor = HierarchyExtractor()

    def extract(self, model_path: str) -> dict[str, Any]:
        path = Path(model_path)

        if not path.exists():
            return {
                "model_name": path.stem or "UnknownModel",
                "components": [],
                "connections": [],
                "parameters": [],
                "equations": [],
                "hierarchy": {"model": path.stem or "UnknownModel", "children": []},
                "source_path": str(path),
                "warnings": [f"Model file not found: {path}"],
            }

        modelica_code = path.read_text(encoding="utf-8")
        ast = self.parser.parse(modelica_code)

        components = self.component_extractor.extract_components(ast)
        connections = self.connection_extractor.extract_connections(ast)
        parameters = self.parameter_extractor.extract_parameters(ast)
        hierarchy = self.hierarchy_extractor.extract_hierarchy(ast)

        return {
            "model_name": ast.get("model_name", path.stem),
            "components": components,
            "connections": connections,
            "parameters": parameters,
            "equations": ast.get("equations", []),
            "hierarchy": hierarchy,
            "source_path": str(path),
            "warnings": [],
        }
