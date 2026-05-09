"""
CLI Entrypoint for Modelica2SysMLv2 Pipeline
"""
import typer
from src.orchestrator.pipeline import PipelineOrchestrator
from src.utils.logging import setup_logging
import yaml

app = typer.Typer()

@app.command()
def run(config: str):
    """Run the Modelica2SysMLv2 pipeline with a YAML config."""
    setup_logging()
    with open(config) as f:
        cfg = yaml.safe_load(f)
    orchestrator = PipelineOrchestrator(cfg)
    orchestrator.run()

if __name__ == "__main__":
    app()