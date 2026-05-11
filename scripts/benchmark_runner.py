"""
Benchmark Runner CLI
"""
from pathlib import Path
import sys

import typer

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.benchmark.runner import BenchmarkRunner
from src.utils.logging import setup_logging

app = typer.Typer()

@app.command()
def benchmark(
    manifest: str = typer.Option(..., "--manifest", help="Path to benchmark manifest YAML")
):
    """Run benchmarks from a manifest YAML file."""
    setup_logging()
    runner = BenchmarkRunner()
    results = runner.run(manifest)
    print(f"Benchmark execution completed: {len(results)} cases processed")

if __name__ == "__main__":
    app()
