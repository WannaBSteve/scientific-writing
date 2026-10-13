#!/usr/bin/env python3
"""Report mechanical prose signals in Markdown, LaTeX, and plain text.

The auditor is deliberately conservative. Findings are prompts for human
review, not proof that prose is wrong or AI-generated. It never edits input.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence


@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    line: int
    message: str
    excerpt: str


STAGED_PHRASES = (
    "it is important to note that",
    "it should be emphasized that",
    "it is worth noting that",
    "to be clear",
    "while it may appear",
    "this is not merely",
    "it introduces no",
    "at its core",
)

PURPOSE_VERBS = re.compile(
    r"\b(?:compute|computes|estimate|estimates|define|defines|select|selects|"
    r"choose|chooses|compare|compares|measure|measures|model|models|maximize|"
    r"maximizes|minimize|minimizes|decide|decides|determine|determines|score|"
    r"scores|publish|publishes|published|allow|allows|satisfy|satisfies|"
    r"objective|constraint)\b",
    re.IGNORECASE,
)

GENERIC_CITATION = re.compile(
    r"(?:follows?|consistent with|builds? on|based on)\s+"
    r"(?:established\s+|existing\s+|previous\s+|prior\s+)?"
    r"(?:work|practice|literature|studies|research)[^.\n]{0,80}"
    r"(?:\\cite\w*\s*\{|\[[0-9,\-\s]+\])",
    re.IGNORECASE,
)


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def compact_excerpt(text: str, limit: int = 140) -> str:
    value = re.sub(r"\s+", " ", text).strip()
    return value if len(value) <= limit else value[: limit - 1] + "…"


def mask_regions(text: str) -> str:
    """Mask code and math while retaining newlines and offsets."""

    patterns = (
        re.compile(r"```.*?```", re.DOTALL),
        re.compile(r"\\begin\{(?:table\*?|figure\*?)\}.*?"
                   r"\\end\{(?:table\*?|figure\*?)\}", re.DOTALL),
        re.compile(r"\\begin\{(?:tabularx|tabular\*?)\}.*?"
                   r"\\end\{(?:tabularx|tabular\*?)\}", re.DOTALL),
        re.compile(r"\\begin\{(?:equation\*?|align\*?|gather\*?)\}.*?"
                   r"\\end\{(?:equation\*?|align\*?|gather\*?)\}", re.DOTALL),
        re.compile(r"\$\$.*?\$\$", re.DOTALL),
        re.compile(r"\\\[.*?\\\]", re.DOTALL),
    )
    masked = list(text)
    for pattern in patterns:
        for match in pattern.finditer(text):
            for index in range(match.start(), match.end()):
                if masked[index] != "\n":
                    masked[index] = " "
    return "".join(masked)


def mask_structural_lines(text: str) -> str:
    """Mask Markdown/LaTeX scaffolding that is not running prose."""

    output: list[str] = []
    for line in text.splitlines(keepends=True):
        stripped = line.lstrip()
        is_structure = (
            stripped.startswith(("#", "|", "- ", "* ", "+ ", "\\item"))
            or bool(re.match(r"\d+[.)]\s+", stripped))
            or set(stripped.strip()) <= {"-", ":", "|", " "}
        )
        if is_structure:
            output.append("".join("\n" if char == "\n" else " " for char in line))
        else:
            output.append(line)
    return "".join(output)


def strip_markup(value: str) -> str:
    value = re.sub(r"\\(?:cite\w*|ref|eqref|label)\s*\{[^}]*\}", " ", value)
    value = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^]]*\])?", " ", value)
    value = value.replace("{", " ").replace("}", " ")
    value = re.sub(r"[`*_#>]", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def sentence_spans(text: str) -> Iterable[tuple[int, int, str]]:
    start = 0
    for match in re.finditer(r"(?<=[.!?])(?:[\"')\]]*)\s+(?=[A-Z0-9\\])", text):
        end = match.start() + 1
        yield start, end, text[start:end]
        start = match.end()
    if text[start:].strip():
        yield start, len(text), text[start:]


def audit_text(text: str, *, max_sentence_words: int = 50) -> list[Finding]:
    findings: list[Finding] = []
    masked = mask_structural_lines(mask_regions(text))
    words = re.findall(r"\b[\w'-]+\b", strip_markup(masked))
    word_count = max(len(words), 1)

    dash_matches = list(re.finditer(r"[—–]", masked))
    dense_dash_lines: dict[int, list[re.Match[str]]] = {}
    for match in dash_matches:
        dense_dash_lines.setdefault(line_number(masked, match.start()), []).append(match)
    for line, matches in dense_dash_lines.items():
        if len(matches) >= 2:
            source_line = text.splitlines()[line - 1]
            findings.append(Finding(
                "STYLE001", "warning", line,
                "Several dashes carry one sentence. Check whether periods or explicit relations would be clearer.",
                compact_excerpt(source_line),
            ))
    if len(dash_matches) >= 4 and len(dash_matches) * 1000 / word_count > 3:
        findings.append(Finding(
            "STYLE002", "info", 1,
            f"Dash density is {len(dash_matches) * 1000 / word_count:.1f} per 1,000 words. Check that it matches the author's style.",
            f"{len(dash_matches)} dashes in {word_count} words",
        ))

    semicolons = list(re.finditer(r";", masked))
    if len(semicolons) >= 3 and len(semicolons) * 1000 / word_count > 4:
        findings.append(Finding(
            "STYLE003", "info", line_number(masked, semicolons[0].start()),
            f"Semicolon density is {len(semicolons) * 1000 / word_count:.1f} per 1,000 words. Check for sentences carrying several decisions.",
            f"{len(semicolons)} semicolons in {word_count} words",
        ))

    for start, _end, raw_sentence in sentence_spans(masked):
        plain = strip_markup(raw_sentence)
        count = len(re.findall(r"\b[\w'-]+\b", plain))
        if count > max_sentence_words:
            findings.append(Finding(
                "FLOW001", "warning", line_number(masked, start),
                f"Sentence has {count} words. Check whether it contains more than one reasoning step.",
                compact_excerpt(text[start:start + len(raw_sentence)]),
            ))

    lowered = masked.lower()
    for phrase in STAGED_PHRASES:
        for match in re.finditer(r"\b" + re.escape(phrase) + r"\b", lowered):
            findings.append(Finding(
                "FLOW002", "info", line_number(masked, match.start()),
                "Check whether this framing answers a real reader question or delays the point.",
                compact_excerpt(text[match.start():match.start() + 180]),
            ))

    for match in GENERIC_CITATION.finditer(masked):
        findings.append(Finding(
            "CITE001", "warning", line_number(masked, match.start()),
            "The citation has no concrete job. State the borrowed definition, mechanism, method, or design precedent.",
            compact_excerpt(text[match.start():match.end()]),
        ))

    labels = {match.group(1): match for match in re.finditer(r"\\label\{([^}]+)\}", text)}
    refs = list(re.finditer(r"\\(?:ref|eqref|autoref|cref|Cref)\{([^}]+)\}", text))
    referenced = {match.group(1) for match in refs}
    for ref in refs:
        if ref.group(1) not in labels:
            findings.append(Finding(
                "REF001", "warning", line_number(text, ref.start()),
                f"Reference '{ref.group(1)}' has no matching label in this file.",
                compact_excerpt(ref.group(0)),
            ))
    for name, match in labels.items():
        if name not in referenced:
            findings.append(Finding(
                "REF002", "info", line_number(text, match.start()),
                f"Label '{name}' is not referenced in this file.",
                compact_excerpt(match.group(0)),
            ))

    equation_patterns = (
        re.compile(r"\\begin\{(?:equation\*?|align\*?|gather\*?)\}", re.IGNORECASE),
        re.compile(r"\$\$"),
        re.compile(r"\\\["),
    )
    equation_offsets = sorted({m.start() for p in equation_patterns for m in p.finditer(text)})
    for offset in equation_offsets:
        before = strip_markup(text[max(0, offset - 360):offset])
        previous_sentence = re.split(r"(?<=[.!?])\s+", before)[-1]
        if len(previous_sentence.split()) < 3 or not PURPOSE_VERBS.search(previous_sentence):
            findings.append(Finding(
                "EQ001", "info", line_number(text, offset),
                "Displayed equation has no nearby purpose statement. State the question or decision before the notation.",
                compact_excerpt(previous_sentence or text[offset:offset + 100]),
            ))

    paragraphs = [
        (m.start(), strip_markup(m.group(0)))
        for m in re.finditer(r"(?ms)(?:^|\n\s*\n)([^\n].*?)(?=\n\s*\n|\Z)", masked)
        if strip_markup(m.group(0))
    ]
    openings: list[tuple[int, str, str]] = []
    for offset, paragraph in paragraphs:
        tokens = re.findall(r"[A-Za-z]+", paragraph.lower())
        if len(tokens) >= 3:
            openings.append((offset, " ".join(tokens[:3]), paragraph))
    for index in range(len(openings) - 2):
        window = openings[index:index + 3]
        if len({opening for _, opening, _ in window}) == 1:
            findings.append(Finding(
                "FLOW003", "info", line_number(masked, window[0][0]),
                "Three consecutive paragraphs share the same opening. Check for mechanical rhythm or repeated setup.",
                window[0][1],
            ))

    return sorted(findings, key=lambda item: (item.line, item.code))


def render_text(path: Path, findings: Sequence[Finding]) -> str:
    if not findings:
        return f"{path}: no findings"
    lines = [f"{path}: {len(findings)} finding(s)"]
    for finding in findings:
        lines.append(
            f"{path}:{finding.line}: {finding.severity} {finding.code}: "
            f"{finding.message}\n    {finding.excerpt}"
        )
    return "\n".join(lines)


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Report mechanical scientific-prose signals without editing input."
    )
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--max-sentence-words", type=int, default=50)
    parser.add_argument(
        "--fail-on", choices=("never", "warning", "info"), default="never",
        help="Return exit status 1 when a finding at this level or higher exists.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    all_results: list[dict[str, object]] = []
    exit_code = 0
    rank = {"info": 1, "warning": 2}
    threshold = {"never": 99, "info": 1, "warning": 2}[args.fail_on]

    for path in args.paths:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            print(f"{path}: error: {error}", file=sys.stderr)
            exit_code = 2
            continue
        findings = audit_text(text, max_sentence_words=args.max_sentence_words)
        if any(rank[item.severity] >= threshold for item in findings):
            exit_code = max(exit_code, 1)
        if args.format == "json":
            all_results.append({
                "path": str(path),
                "findings": [asdict(item) for item in findings],
            })
        else:
            print(render_text(path, findings))

    if args.format == "json":
        print(json.dumps(all_results, indent=2, ensure_ascii=False))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
