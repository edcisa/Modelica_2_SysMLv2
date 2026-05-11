"""Precision and recall metrics for transformation output."""

from __future__ import annotations

from typing import Any


class PrecisionMetrics:
    """Compute precision/recall/F1 on normalized entities."""

    @staticmethod
    def _entity_set(payload: Any) -> set[str]:
        entities: set[str] = set()
        for component in payload.get("components", []):
            name = component.get("name")
            if name:
                entities.add(f"component:{name}")
        for parameter in payload.get("parameters", []):
            name = parameter.get("name")
            if name:
                entities.add(f"parameter:{name}")
        for connection in payload.get("connections", []):
            src = connection.get("from")
            dst = connection.get("to")
            if src and dst:
                entities.add(f"connection:{src}->{dst}")
        return entities

    def compute(self, generated: Any, reference: Any) -> dict[str, float]:
        gen_set = self._entity_set(generated)
        ref_set = self._entity_set(reference)

        if not gen_set and not ref_set:
            return {"precision": 1.0, "recall": 1.0, "f1": 1.0}

        tp = len(gen_set & ref_set)
        precision = tp / len(gen_set) if gen_set else 0.0
        recall = tp / len(ref_set) if ref_set else 1.0
        if precision + recall == 0:
            f1 = 0.0
        else:
            f1 = 2 * precision * recall / (precision + recall)

        return {
            "precision": round(precision, 4),
            "recall": round(recall, 4),
            "f1": round(f1, 4),
        }
