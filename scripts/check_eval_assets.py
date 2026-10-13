#!/usr/bin/env python3
"""Validate behavior-evaluation metadata without running a model."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "evals" / "manifest.json"
REQUIRED = {"id", "file", "mode", "criteria"}
MODES = {"plan", "draft", "revise", "audit", "respond"}


def main() -> int:
    payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 1:
        raise SystemExit("unsupported eval schema")
    cases = payload.get("cases")
    if not isinstance(cases, list) or not cases:
        raise SystemExit("manifest has no cases")

    seen: set[str] = set()
    for index, case in enumerate(cases, start=1):
        missing = REQUIRED - set(case)
        if missing:
            raise SystemExit(f"case {index} missing: {sorted(missing)}")
        if case["id"] in seen:
            raise SystemExit(f"duplicate case id: {case['id']}")
        seen.add(case["id"])
        if case["mode"] not in MODES:
            raise SystemExit(f"invalid mode for {case['id']}: {case['mode']}")
        if not isinstance(case["criteria"], list) or len(case["criteria"]) < 3:
            raise SystemExit(f"case {case['id']} needs at least three criteria")
        path = ROOT / "evals" / case["file"]
        if not path.is_file():
            raise SystemExit(f"missing case file: {path}")
        text = path.read_text(encoding="utf-8")
        if "# Task" not in text:
            raise SystemExit(f"case {case['id']} has no Task heading")

    print(f"validated {len(cases)} behavior cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
