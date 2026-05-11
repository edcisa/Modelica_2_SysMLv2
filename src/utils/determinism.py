"""Determinism utilities for reproducible experiments."""

from __future__ import annotations

import os
import random

import numpy as np


def set_seed(seed: int) -> None:
    """Set reproducibility controls for common Python ML stacks."""
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":16:8"

    try:
        import torch

        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
    except Exception:
        # Torch is optional in this repository.
        pass
