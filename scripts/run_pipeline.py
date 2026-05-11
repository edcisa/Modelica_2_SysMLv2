"""
CLI Entrypoint for Modelica2SysMLv2 Pipeline
"""
from pathlib import Path
import sys

import typer
import yaml

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.orchestrator.pipeline import PipelineOrchestrator
from src.utils.logging import setup_logging

app = typer.Typer()

@app.command()
def run(config: str = typer.Option(..., "--config", help="Path to YAML config file")):
    """Run the Modelica2SysMLv2 pipeline with a YAML config."""
    setup_logging()
    with open(config) as f:
        cfg = yaml.safe_load(f)
    orchestrator = PipelineOrchestrator(cfg)
    orchestrator.run()

if __name__ == "__main__":
    app()