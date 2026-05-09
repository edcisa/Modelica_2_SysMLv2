"""
MetricsAggregation: Aggregates metrics across benchmarks
"""
from typing import List, Dict
import pandas as pd

class MetricsAggregation:
    def aggregate(self, metrics_list: List[Dict[str, float]]) -> pd.DataFrame:
        return pd.DataFrame(metrics_list).mean().to_frame().T
