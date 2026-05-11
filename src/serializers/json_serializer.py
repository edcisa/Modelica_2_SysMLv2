"""JSON serializers for intermediate representations."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field


class ModelicaIR(BaseModel):
    """Typed Modelica intermediate representation used across the pipeline."""

    model_name: str = "UnknownModel"
    components: list[dict[str, Any]] = Field(default_factory=list)
    connections: list[dict[str, Any]] = Field(default_factory=list)
    parameters: list[dict[str, Any]] = Field(default_factory=list)
    equations: list[dict[str, Any]] = Field(default_factory=list)
    hierarchy: dict[str, Any] = Field(default_factory=dict)
    source_path: str | None = None
    warnings: list[str] = Field(default_factory=list)


class JSONSerializer:
    """Serialize and deserialize pipeline artifacts in JSON format."""

    @staticmethod
    def serialize(ir: ModelicaIR) -> str:
        return ir.model_dump_json(indent=2)

    @staticmethod
    def deserialize(data: str) -> ModelicaIR:
        return ModelicaIR.model_validate_json(data)

    @staticmethod
    def save_dict(data: dict[str, Any], output_path: str) -> None:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def load_dict(path: str) -> dict[str, Any]:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
