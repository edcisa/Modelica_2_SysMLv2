"""
JSON Serializer for Modelica IR
"""
from typing import Any
from pydantic import BaseModel
import json

class ModelicaIR(BaseModel):
    components: list
    connections: list
    parameters: list

    class Config:
        arbitrary_types_allowed = True

class JSONSerializer:
    @staticmethod
    def serialize(ir: ModelicaIR) -> str:
        return ir.json(indent=2)

    @staticmethod
    def deserialize(data: str) -> ModelicaIR:
        return ModelicaIR.parse_raw(data)
