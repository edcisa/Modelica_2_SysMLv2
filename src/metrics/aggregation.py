"""Aggregation helpers for benchmark and experiment metrics."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd


class MetricsAggregation:
    """Aggregate a list of metric rows and persist summaries."""

    def aggregate(self, metrics_list: list[dict[str, Any]]) -> pd.DataFrame:
        if not metrics_list:
            return pd.DataFrame()
        frame = pd.DataFrame(metrics_list)
        numeric_columns = frame.select_dtypes(include=["number"]).columns
        summary = frame[numeric_columns].mean().to_frame().T
        summary.insert(0, "cases", len(metrics_list))
        return summary

    def to_csv(self, metrics_list: list[dict[str, Any]], output_path: str) -> None:
        frame = pd.DataFrame(metrics_list)
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        frame.to_csv(output_path, index=False)
