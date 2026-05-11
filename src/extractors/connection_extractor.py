"""Connection extraction utilities."""

from __future__ import annotations

from typing import Any


class ConnectionExtractor:
    """Extract normalized connection entries from parser output."""

    def extract_connections(self, ast: dict[str, Any]) -> list[dict[str, Any]]:
        connections: list[dict[str, Any]] = []
        seen: set[tuple[str, str]] = set()

        for connection in ast.get("connections", []):
            src = str(connection.get("from", "")).strip()
            dst = str(connection.get("to", "")).strip()
            if not src or not dst:
                continue
            key = (src, dst)
            if key in seen:
                continue
            seen.add(key)
            connections.append({"from": src, "to": dst, "kind": "connection"})

        return connections
