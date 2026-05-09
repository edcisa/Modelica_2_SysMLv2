"""
Benchmark Runner CLI
"""
import typer
from src.benchmark.runner import BenchmarkRunner
from src.utils.logging import setup_logging

app = typer.Typer()

@app.command()
def benchmark(manifest: str):
    """Run benchmarks from a manifest YAML file."""
    setup_logging()
    runner = BenchmarkRunner()
    runner.run(manifest)

if __name__ == "__main__":
    app()
