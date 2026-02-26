#!/usr/bin/env python3
"""Validate docs/research/distillation/*-concepts.md against v2.1 contract."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple


SECTION_ORDER = [
    "Source",
    "User Prompts Summary",
    "AI Response Summary",
    "Extracted Concepts",
    "Unresolved Ambiguities",
]

SOURCE_KEYS = [
    "chat_id",
    "source_path",
    "source_path_abs",
    "processed_on",
    "draft_status",
]

SUMMARY_TYPES = {
    "goal",
    "constraint",
    "request",
    "proposal",
    "decision",
    "risk",
    "next_step",
}

TITLE_RE = re.compile(r"^# I\d{2}-F\d{4}-[A-Z]+(?:-DR)? Concepts \(Draft\)$")
TOP_LINK_RE = re.compile(r"^\[Analyzed source:\s+.+\]\(.+\)\s*$")
SECTION_RE = re.compile(r"^##\s+(.+?)\s*$")
SOURCE_KEY_RE = re.compile(r"^-\s+([a-z_]+):")
DATE_RE = re.compile(r"^-\s+processed_on:\s+`?(\d{4}-\d{2}-\d{2})`?\s*$")
NUMBERED_ITEM_RE = re.compile(r"^\s*(\d+)\.\s+(.+?)\s*$")
TYPED_SUMMARY_RE = re.compile(
    r"^\[(goal|constraint|request|proposal|decision|risk|next_step)\]\s+\S.+$"
)
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\([^)]+\)")
ANCHOR_RE = re.compile(r"raw-exports/.+:\d+")
CONCEPT_HEADING_RE = re.compile(r"^###\s+C(\d{2})\.\s+.+$")
UNRESOLVED_ITEM_RE = re.compile(r"^\s*\d+\.\s+\S.+$")
EVIDENCE_ITEM_RE = re.compile(r"^\s*-\s+`raw-exports/.+:\d+`\s*$")


@dataclass
class Violation:
    path: str
    rule_id: str
    message: str
    line: Optional[int] = None

    def as_dict(self) -> Dict[str, object]:
        payload: Dict[str, object] = {
            "path": self.path,
            "rule_id": self.rule_id,
            "message": self.message,
        }
        if self.line is not None:
            payload["line"] = self.line
        return payload


def add_violation(
    out: List[Violation],
    path: Path,
    rule_id: str,
    message: str,
    line: Optional[int] = None,
) -> None:
    out.append(Violation(path=str(path), rule_id=rule_id, message=message, line=line))


def find_sections(lines: List[str]) -> Tuple[List[Tuple[str, int]], List[Violation]]:
    found: List[Tuple[str, int]] = []
    violations: List[Violation] = []
    seen: Dict[str, int] = {}

    for idx, line in enumerate(lines, start=1):
        m = SECTION_RE.match(line.strip())
        if not m:
            continue
        name = m.group(1)
        if name in SECTION_ORDER:
            found.append((name, idx))
            if name in seen:
                violations.append(
                    Violation(
                        path="",
                        rule_id="section.duplicate",
                        message=f"Duplicate section '{name}'",
                        line=idx,
                    )
                )
            seen[name] = idx
    return found, violations


def section_slice(
    lines: List[str],
    section_positions: Dict[str, int],
    name: str,
) -> Tuple[List[str], int]:
    start_line = section_positions[name]
    start_idx = start_line
    next_positions = [v for v in section_positions.values() if v > start_line]
    if next_positions:
        end_idx = min(next_positions) - 1
    else:
        end_idx = len(lines)
    return lines[start_idx:end_idx], start_line + 1


def validate_summary_section(
    path: Path,
    lines: List[str],
    section_positions: Dict[str, int],
    section_name: str,
    violations: List[Violation],
) -> None:
    body, first_line = section_slice(lines, section_positions, section_name)
    items: List[Tuple[int, int, str]] = []

    for i, line in enumerate(body):
        m = NUMBERED_ITEM_RE.match(line)
        if m:
            number = int(m.group(1))
            text = m.group(2).strip()
            items.append((number, first_line + i, text))

    if not 1 <= len(items) <= 7:
        add_violation(
            violations,
            path,
            "summary.cardinality",
            f"{section_name}: expected 1..7 items, got {len(items)}",
            first_line,
        )

    expected_numbers = list(range(1, len(items) + 1))
    actual_numbers = [n for n, _, _ in items]
    if actual_numbers != expected_numbers:
        add_violation(
            violations,
            path,
            "summary.numbering",
            f"{section_name}: numbering must be sequential from 1",
            first_line,
        )

    for _, line_no, text in items:
        if not TYPED_SUMMARY_RE.match(text):
            add_violation(
                violations,
                path,
                "summary.item.format",
                f"{section_name}: item must match 'N. [type] text' with allowed enum",
                line_no,
            )
        else:
            type_name = text.split("]", 1)[0].lstrip("[")
            if type_name not in SUMMARY_TYPES:
                add_violation(
                    violations,
                    path,
                    "summary.item.type",
                    f"{section_name}: unsupported type '{type_name}'",
                    line_no,
                )

        if MARKDOWN_LINK_RE.search(text):
            add_violation(
                violations,
                path,
                "summary.no_links",
                f"{section_name}: markdown links are not allowed",
                line_no,
            )
        if ANCHOR_RE.search(text):
            add_violation(
                violations,
                path,
                "summary.no_anchors",
                f"{section_name}: source anchors are not allowed",
                line_no,
            )


def validate_concepts_section(
    path: Path,
    lines: List[str],
    section_positions: Dict[str, int],
    violations: List[Violation],
) -> None:
    body, first_line = section_slice(lines, section_positions, "Extracted Concepts")
    heading_positions: List[Tuple[int, int]] = []

    for i, line in enumerate(body):
        if line.startswith("### "):
            m = CONCEPT_HEADING_RE.match(line)
            if not m:
                add_violation(
                    violations,
                    path,
                    "concept.heading.format",
                    "Concept heading must match '### Cnn. Title'",
                    first_line + i,
                )
                continue
            heading_positions.append((int(m.group(1)), i))

    if not heading_positions:
        add_violation(
            violations,
            path,
            "concept.none",
            "No concept blocks found",
            first_line,
        )
        return

    expected_ids = list(range(1, len(heading_positions) + 1))
    actual_ids = [cid for cid, _ in heading_positions]
    if actual_ids != expected_ids:
        add_violation(
            violations,
            path,
            "concept.sequence",
            "Concept IDs must be sequential: C01..CNN",
            first_line,
        )

    block_bounds: List[Tuple[int, int, int]] = []
    for idx, (_, start) in enumerate(heading_positions):
        if idx + 1 < len(heading_positions):
            end = heading_positions[idx + 1][1]
        else:
            end = len(body)
        block_bounds.append((idx, start, end))

    for _, start, end in block_bounds:
        block = body[start:end]
        base_line = first_line + start

        has_concept = any(line.strip().startswith("- Concept:") for line in block)
        has_why = any(line.strip().startswith("- Why it matters:") for line in block)
        evidence_idx = next(
            (i for i, line in enumerate(block) if line.strip().startswith("- Evidence:")),
            None,
        )

        if not has_concept:
            add_violation(
                violations,
                path,
                "concept.field.concept",
                "Missing required field '- Concept:'",
                base_line,
            )
        if not has_why:
            add_violation(
                violations,
                path,
                "concept.field.why",
                "Missing required field '- Why it matters:'",
                base_line,
            )
        if evidence_idx is None:
            add_violation(
                violations,
                path,
                "concept.field.evidence",
                "Missing required field '- Evidence:'",
                base_line,
            )
            continue

        evidence_tail = block[evidence_idx + 1 :]
        evidence_count = sum(1 for line in evidence_tail if EVIDENCE_ITEM_RE.match(line))
        if evidence_count == 0:
            add_violation(
                violations,
                path,
                "concept.evidence.empty",
                "Evidence list must include at least one anchor",
                base_line + evidence_idx,
            )


def validate_file(path: Path) -> List[Violation]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    violations: List[Violation] = []

    if not lines:
        add_violation(violations, path, "file.empty", "File is empty")
        return violations

    if not TITLE_RE.match(lines[0].strip()):
        add_violation(
            violations,
            path,
            "title.format",
            "Title must match '# <CHAT_ID> Concepts (Draft)'",
            1,
        )

    for idx, line in enumerate(lines[:12], start=1):
        if TOP_LINK_RE.match(line.strip()):
            add_violation(
                violations,
                path,
                "top_link.prohibited",
                "Top '[Analyzed source: ...]' link is prohibited",
                idx,
            )
            break

    found_sections, section_violations = find_sections(lines)
    for v in section_violations:
        v.path = str(path)
        violations.append(v)

    found_map: Dict[str, int] = {name: line for name, line in found_sections}

    for name in SECTION_ORDER:
        if name not in found_map:
            add_violation(
                violations,
                path,
                "section.missing",
                f"Missing section '## {name}'",
            )

    if all(name in found_map for name in SECTION_ORDER):
        positions = [found_map[name] for name in SECTION_ORDER]
        if positions != sorted(positions):
            add_violation(
                violations,
                path,
                "section.order",
                "Canonical section order is violated",
            )

    if "Source" in found_map:
        source_lines, source_start = section_slice(lines, found_map, "Source")
        keys_in_order: List[str] = []
        for i, line in enumerate(source_lines):
            m = SOURCE_KEY_RE.match(line.strip())
            if m:
                keys_in_order.append(m.group(1))

        for required in SOURCE_KEYS:
            if required not in keys_in_order:
                add_violation(
                    violations,
                    path,
                    "source.key.missing",
                    f"Missing required source key '{required}'",
                    source_start,
                )

        if len(keys_in_order) >= len(SOURCE_KEYS):
            if keys_in_order[: len(SOURCE_KEYS)] != SOURCE_KEYS:
                add_violation(
                    violations,
                    path,
                    "source.key.order",
                    "Source keys must appear in canonical order",
                    source_start,
                )
        elif keys_in_order and keys_in_order != SOURCE_KEYS[: len(keys_in_order)]:
            add_violation(
                violations,
                path,
                "source.key.order",
                "Source keys must appear in canonical order",
                source_start,
            )

        processed_on_line = next(
            (line for line in source_lines if line.strip().startswith("- processed_on:")),
            None,
        )
        if processed_on_line and not DATE_RE.match(processed_on_line.strip()):
            add_violation(
                violations,
                path,
                "source.processed_on.format",
                "processed_on must match YYYY-MM-DD",
                source_start,
            )

    if "User Prompts Summary" in found_map:
        validate_summary_section(path, lines, found_map, "User Prompts Summary", violations)
    if "AI Response Summary" in found_map:
        validate_summary_section(path, lines, found_map, "AI Response Summary", violations)
    if "Extracted Concepts" in found_map:
        validate_concepts_section(path, lines, found_map, violations)

    if "Unresolved Ambiguities" in found_map:
        unresolved_lines, unresolved_start = section_slice(
            lines, found_map, "Unresolved Ambiguities"
        )
        unresolved_count = sum(
            1 for line in unresolved_lines if UNRESOLVED_ITEM_RE.match(line)
        )
        if unresolved_count == 0:
            add_violation(
                violations,
                path,
                "unresolved.numbering",
                "Unresolved Ambiguities must be a numbered list",
                unresolved_start,
            )

    return violations


def collect_files(root: Path) -> List[Path]:
    return sorted(p for p in root.glob("*-concepts.md") if p.is_file())


def render_text(
    files_checked: int,
    files_with_violations: int,
    rule_counts: Counter,
    violations: List[Violation],
) -> str:
    lines: List[str] = []
    lines.append(f"files_checked={files_checked}")
    lines.append(f"files_with_violations={files_with_violations}")
    lines.append(f"violations_total={len(violations)}")
    lines.append("rule_counts:")
    for rule_id in sorted(rule_counts):
        lines.append(f"- {rule_id}: {rule_counts[rule_id]}")
    lines.append("violations:")
    for v in violations:
        message = v.message
        if v.line is not None:
            message = f"{message} (line {v.line})"
        lines.append(f"{v.path}:{v.rule_id}:{message}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=Path("docs/research/distillation"),
        help="Root directory with *-concepts.md files",
    )
    parser.add_argument(
        "--mode",
        choices=("report", "strict"),
        default="report",
        help="report: always exit 0; strict: exit 1 on any violation",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Output format",
    )
    args = parser.parse_args()

    files = collect_files(args.root)
    all_violations: List[Violation] = []
    file_has_violation: Dict[str, bool] = {}

    for path in files:
        violations = validate_file(path)
        if violations:
            file_has_violation[str(path)] = True
            all_violations.extend(violations)

    rule_counts = Counter(v.rule_id for v in all_violations)
    files_with_violations = len(file_has_violation)

    if args.format == "json":
        payload = {
            "files_checked": len(files),
            "files_with_violations": files_with_violations,
            "violations_total": len(all_violations),
            "rule_counts": dict(sorted(rule_counts.items())),
            "violations": [v.as_dict() for v in all_violations],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(
            render_text(
                files_checked=len(files),
                files_with_violations=files_with_violations,
                rule_counts=rule_counts,
                violations=all_violations,
            )
        )

    if args.mode == "strict" and all_violations:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
