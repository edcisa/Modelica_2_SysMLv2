"""
Metrics Evaluation Script
"""
import pandas as pd
import typer

app = typer.Typer()

@app.command()
def aggregate_metrics(report_dir: str):
    """Aggregate metrics CSVs in a report directory."""
    dfs = []
    # TODO: Recursively find all metrics.csv files
    # For demo, just read one file
    df = pd.read_csv(f"{report_dir}/metrics.csv")
    dfs.append(df)
    result = pd.concat(dfs)
    print(result.describe())

if __name__ == "__main__":
    app()
