"""
ExperimentTracker: Tracks experiment configs, seeds, and results
"""
from typing import Dict, Any
import json

class ExperimentTracker:
    def __init__(self, output_path: str):
        self.output_path = output_path
        self.records = []

    def log(self, record: Dict[str, Any]):
        self.records.append(record)
        with open(self.output_path, "w") as f:
            json.dump(self.records, f, indent=2)
