"""
Determinism utilities: Set random seeds for reproducibility
"""
import random
import numpy as np
import os

def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
