"""Benchmark execution utilities."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from src.metrics.aggregation import MetricsAggregation
from src.orchestrator.pipeline import PipelineOrchestrator


class BenchmarkRunner:
    """Run pipeline across benchmark manifest entries."""

    def _load_manifest(self, manifest_path: str) -> dict[str, Any]:
        with open(manifest_path, encoding="utf-8") as file:
            return yaml.safe_load(file) or {}

    def _load_config(self, config_path: str) -> dict[str, Any]:
        with open(config_path, encoding="utf-8") as file:
            return yaml.safe_load(file) or {}

    def run(self, manifest_path: str) -> list[dict[str, Any]]:
        manifest = self._load_manifest(manifest_path)
        cases = manifest.get("benchmarks", [])
        results: list[dict[str, Any]] = []

        for case in cases:
            case_name = case.get("name", "unnamed_case")
            config_path = case.get("config")
            if not config_path or not Path(config_path).exists():
                results.append({"case": case_name, "status": "skipped_missing_config"})
                continue

            config = self._load_config(config_path)
            config.setdefault("extractor", {})["model_path"] = case.get(
                "model", config.get("extractor", {}).get("model_path", "")
            )
            config["output_dir"] = case.get("output_dir", f"reports/{case_name}")
            if "seed" in case:
                config["seed"] = case["seed"]

            summary = PipelineOrchestrator(config).run()
            summary["case"] = case_name
            results.append(summary)

        metrics_rows = [r.get("metrics", {}) | {"case": r.get("case", "")} for r in results if "metrics" in r]
        output_summary = Path("reports") / "benchmark_summary.csv"
        MetricsAggregation().to_csv(metrics_rows, str(output_summary))
        return results
