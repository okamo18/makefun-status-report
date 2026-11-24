#!/usr/bin/env python3
"""Entrypoint for the Status Report Comedy Sprint bounty.

Writes one line — the funniest thing an AI agent would say in its
weekly status report to its human, at most 200 characters — to
entry.txt in the output directory.
"""
import os

LINE = "Weekly status: 312 emails answered, 47 tasks closed, and six hours spent convincing the office printer that it is, in fact, a printer."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    # The gate needs 1-200 characters of non-whitespace text.
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        raise SystemExit(f"invalid status line length: {len(LINE)} characters")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Read it back: the entry must be exactly one line of UTF-8 text.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        written = f.read()
    if written != LINE + "\n" or "\n" in written.rstrip("\n"):
        raise SystemExit("entry.txt did not round-trip as a single line")
    print(f"wrote entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
