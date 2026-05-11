"""
Metrics Evaluation Script
"""
from pathlib import Path
import sys

import pandas as pd
import typer

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

app = typer.Typer()

@app.command()
def aggregate_metrics(
    report_dir: str = typer.Option(..., "--report-dir", help="Root folder with metrics.csv files")
):
    """Aggregate metrics CSVs in a report directory."""
    root = Path(report_dir)
    csv_paths = sorted(root.rglob("metrics.csv"))
    if not csv_paths:
        print(f"No metrics.csv files found under: {report_dir}")
        raise typer.Exit(code=1)

    frames = []
    for csv_path in csv_paths:
        frame = pd.read_csv(csv_path)
        frame.insert(0, "source", str(csv_path))
        frames.append(frame)

    result = pd.concat(frames, ignore_index=True)
    numeric = result.select_dtypes(include=["number"])
    summary = numeric.mean().to_dict()

    output_csv = root / "metrics_aggregated.csv"
    result.to_csv(output_csv, index=False)

    print(f"Aggregated {len(csv_paths)} files")
    print(f"Saved detailed aggregation to: {output_csv}")
    print("Mean metrics:")
    for key, value in summary.items():
        print(f"- {key}: {value:.4f}")

if __name__ == "__main__":
    app()
