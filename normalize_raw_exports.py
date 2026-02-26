#!/usr/bin/env python3
"""Normalize exported conversation markdown files in raw-exports.

Transforms role/message blocks:
- #### You: / #### ChatGPT: / #### 👤 User: / #### 🤖 Assistant:
  -> <user> ... </user>, <agent> ... </agent>
- Removes unsupported-content placeholders:
  [Unsupported Content]
- Removes plugin markers:
  #### Plugin (...)\nMake sure to include ...
- Wraps thought sections:
  ## Thoughts / ## Thought / ## Thinking ... -> <agent-thoughs> ... </agent-thoughs>
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional


PLUGIN_HEADER_RE = re.compile(r"^\s*####\s*Plugin\b")
UNSUPPORTED_RE = re.compile(r"^\s*\\?\[Unsupported Content\]\s*$")
ROLE_HEADER_RE = re.compile(r"^\s*####\s*(?P<label>.+?):\s*$")
THOUGHTS_HEADER_RE = re.compile(
    r"^\s*#{2,6}\s*(?P<title>.*)\s*$"
)
MAKE_SURE_RE = re.compile(r"^\s*Make sure to include\b")


def detect_role(label: str) -> Optional[str]:
    text = label.lower()
    text_alpha = re.sub(r"[^a-zа-яё]+", " ", text)

    if any(token in text_alpha for token in ("chatgpt", "assistant", "agent", "ai")):
        return "agent"
    if any(token in text_alpha for token in ("you", "user", "пользователь")):
        return "user"
    return None


def is_thoughts_heading(line: str) -> bool:
    m = THOUGHTS_HEADER_RE.match(line)
    if not m:
        return False
    title = m.group("title").strip().lower()
    if not title:
        return False
    # Match only dedicated thought headings, not arbitrary heading text containing "think".
    return bool(
        re.fullmatch(
            r"(?:[0-9\)\.\-:\s]*)?(?:thoughts?|thinking|reasoning|analysis|размышления?|рассуждения?)",
            title,
            flags=re.IGNORECASE,
        )
    )


@dataclass
class ParseState:
    tag: Optional[str] = None
    buffer: List[str] = None

    def __post_init__(self) -> None:
        if self.buffer is None:
            self.buffer = []


def flush(out: List[str], state: ParseState) -> None:
    if state.tag is None:
        return

    meaningful = any(line.strip() for line in state.buffer)
    if meaningful:
        out.append(f"<{state.tag}>\n")
        out.extend(state.buffer)
        out.append(f"</{state.tag}>\n")

    state.buffer = []
    state.tag = None


def transform_lines(lines: Iterable[str]) -> List[str]:
    out: List[str] = []
    state = ParseState()
    lines = list(lines)
    i = 0
    total = len(lines)

    while i < total:
        line = lines[i]

        # Remove plugin header and the next "Make sure to include" line.
        if PLUGIN_HEADER_RE.match(line):
            i += 1
            if i < total and MAKE_SURE_RE.match(lines[i]):
                i += 1
            continue

        if UNSUPPORTED_RE.match(line):
            i += 1
            continue

        role_match = ROLE_HEADER_RE.match(line)
        if role_match:
            flush(out, state)
            role_label = role_match.group("label")
            tag = detect_role(role_label)
            if tag:
                state.tag = tag
            else:
                state.tag = None
                out.append(line)
            i += 1
            continue

        if is_thoughts_heading(line):
            flush(out, state)
            state.tag = "agent-thoughs"
            i += 1
            continue

        if state.tag is None:
            out.append(line)
        else:
            state.buffer.append(line)

        i += 1

    flush(out, state)
    return out


def process_file(path: Path, *, dry_run: bool) -> bool:
    original = path.read_text(encoding="utf-8")
    transformed_lines = transform_lines(original.splitlines(keepends=True))
    new_text = "".join(transformed_lines)
    if new_text == original:
        return False

    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return True


def iter_markdown_files(root: Path) -> List[Path]:
    return sorted(root.rglob("*.md"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        default="raw-exports",
        help="Root directory containing raw exports",
        type=Path,
    )
    parser.add_argument("--dry-run", action="store_true", help="Do not write changes")
    args = parser.parse_args()

    files = [p for p in iter_markdown_files(args.root) if p.is_file()]
    changed = []

    for path in files:
        if process_file(path, dry_run=args.dry_run):
            changed.append(path)

    print(f"Processed: {len(files)} files")
    print(f"Changed: {len(changed)} files")
    for path in changed:
        print(path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
