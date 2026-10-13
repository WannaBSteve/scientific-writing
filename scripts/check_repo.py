#!/usr/bin/env python3
"""Run deterministic repository consistency checks."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    raise SystemExit(message)


def main() -> int:
    required = [
        "SKILL.md",
        "agents/openai.yaml",
        "README.md",
        "README.zh-CN.md",
        "LICENSE",
        "VERSION",
        "CITATION.cff",
    ]
    for relative in required:
        if not (ROOT / relative).is_file():
            fail(f"missing required file: {relative}")

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\n"):
        fail("SKILL.md has no YAML frontmatter")
    for relative in re.findall(r"\]\((references/[^)]+\.md)\)", skill):
        if not (ROOT / relative).is_file():
            fail(f"SKILL.md references missing file: {relative}")

    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    if f"version: {version}" not in citation:
        fail("VERSION and CITATION.cff differ")

    marker_words = ("T" + "BD", "TO" + "DO", "FIX" + "ME", "PLACE" + "HOLDER")
    placeholders = re.compile(r"\b(?:" + "|".join(marker_words) + r")\b")
    checked_suffixes = {".md", ".py", ".yaml", ".yml", ".cff"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix not in checked_suffixes:
            continue
        text = path.read_text(encoding="utf-8")
        match = placeholders.search(text)
        if match:
            fail(f"unfinished marker {match.group(0)} in {path.relative_to(ROOT)}")

        if path.suffix == ".md":
            for target in re.findall(r"\[[^]]*\]\(([^)]+)\)", text):
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                relative_target = target.split("#", 1)[0]
                if not relative_target:
                    continue
                resolved = (path.parent / relative_target).resolve()
                try:
                    resolved.relative_to(ROOT.resolve())
                except ValueError:
                    fail(f"link escapes repository in {path.relative_to(ROOT)}: {target}")
                if not resolved.exists():
                    fail(f"broken link in {path.relative_to(ROOT)}: {target}")

    print("repository consistency checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
