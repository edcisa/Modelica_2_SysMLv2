"""
YAML Serializer for Modelica IR
"""
from typing import Any
import yaml
from pydantic import BaseModel

class YAMLSerializer:
    @staticmethod
    def serialize(ir: BaseModel) -> str:
        return yaml.dump(ir.model_dump())

    @staticmethod
    def deserialize(data: str, model: Any) -> BaseModel:
        return model(**yaml.safe_load(data))
