"""Experiment orchestrator for reproducible multi-run evaluation."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from src.orchestrator.pipeline import PipelineOrchestrator
from src.utils.experiment_tracker import ExperimentTracker


class ExperimentOrchestrator:
    """Run experiment entries from a manifest and track all outputs."""

    def __init__(self, manifest: Any):
        self.manifest = manifest

    def _load_yaml(self, path: str) -> dict[str, Any]:
        with open(path, encoding="utf-8") as file:
            return yaml.safe_load(file) or {}

    def run(self) -> list[dict[str, Any]]:
        experiments = self.manifest.get("experiments", [])
        tracker = ExperimentTracker("reports/experiment_tracker.json")
        results: list[dict[str, Any]] = []

        for experiment in experiments:
            config_path = experiment.get("config")
            if not config_path or not Path(config_path).exists():
                tracker.log({"name": experiment.get("name", "unknown"), "status": "skipped"})
                continue

            config = self._load_yaml(config_path)
            config.setdefault("extractor", {})["model_path"] = experiment.get(
                "dataset", config.get("extractor", {}).get("model_path", "")
            )
            config["output_dir"] = experiment.get("output_dir", f"reports/{experiment.get('name', 'run')}")
            if "seed" in experiment:
                config["seed"] = experiment["seed"]

            summary = PipelineOrchestrator(config).run()
            summary["experiment_name"] = experiment.get("name", "unnamed")
            tracker.log(summary)
            results.append(summary)

        return results
