"""Experiment tracking helpers."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class ExperimentTracker:
    """Track experiment run metadata in a single JSON file."""

    def __init__(self, output_path: str):
        self.output_path = output_path
        self.records: list[dict[str, Any]] = []

    def log(self, record: dict[str, Any]) -> None:
        self.records.append(record)
        Path(self.output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(self.output_path, "w", encoding="utf-8") as file:
            json.dump(self.records, file, indent=2)

    def all(self) -> list[dict[str, Any]]:
        return list(self.records)
