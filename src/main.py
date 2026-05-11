"""Official CLI for the Modelica2SysMLv2 research framework."""

from __future__ import annotations

from pathlib import Path

import typer
import yaml

from src.benchmark.runner import BenchmarkRunner
from src.orchestrator.experiment import ExperimentOrchestrator
from src.orchestrator.pipeline import PipelineOrchestrator
from src.utils.logging import setup_logging

app = typer.Typer(help="Modelica2SysMLv2 orchestration CLI")


@app.command("run")
def run_pipeline(
    config: str = typer.Option(..., "--config", help="YAML config path for one pipeline execution"),
) -> None:
    setup_logging()
    with open(config, encoding="utf-8") as file:
        cfg = yaml.safe_load(file) or {}
    summary = PipelineOrchestrator(cfg).run()
    typer.echo(f"Pipeline completed with status={summary['status']}")


@app.command("benchmark")
def run_benchmark(
    manifest: str = typer.Option(..., "--manifest", help="Benchmark manifest YAML path"),
) -> None:
    setup_logging()
    results = BenchmarkRunner().run(manifest)
    typer.echo(f"Benchmark completed: {len(results)} cases")


@app.command("experiment")
def run_experiment(
    manifest: str = typer.Option(..., "--manifest", help="Experiment manifest YAML path"),
) -> None:
    setup_logging()
    with open(manifest, encoding="utf-8") as file:
        data = yaml.safe_load(file) or {}
    results = ExperimentOrchestrator(data).run()
    typer.echo(f"Experiments completed: {len(results)} runs")


@app.command("metrics")
def aggregate_metrics(
    report_dir: str = typer.Option(..., "--report-dir", help="Root folder to recursively scan metrics.csv files"),
) -> None:
    import pandas as pd

    root = Path(report_dir)
    csv_paths = sorted(root.rglob("metrics.csv"))
    if not csv_paths:
        raise typer.BadParameter(f"No metrics.csv files found under {report_dir}")

    frames = []
    for path in csv_paths:
        frame = pd.read_csv(path)
        frame.insert(0, "source", str(path))
        frames.append(frame)

    all_metrics = pd.concat(frames, ignore_index=True)
    output_path = root / "metrics_aggregated.csv"
    all_metrics.to_csv(output_path, index=False)
    typer.echo(f"Aggregated metrics written to {output_path}")


if __name__ == "__main__":
    app()
