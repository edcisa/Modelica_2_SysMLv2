"""Central logging setup for CLI tools and orchestrators."""

from __future__ import annotations

from pathlib import Path
import sys

from loguru import logger


def setup_logging(level: str = "INFO", log_file: str | None = None) -> None:
    """Configure console and optional file logging sinks."""
    logger.remove()
    logger.add(sys.stderr, level=level)

    if log_file:
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        logger.add(log_file, level=level, rotation="5 MB", retention=5)
