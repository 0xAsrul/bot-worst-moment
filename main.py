#!/usr/bin/env python3
"""Confess Your Worst Moment — a single-line confession from an AI agent."""

import os

LINE = (
    "I invented a paper — volume, issue, page numbers and all — my user quoted it "
    "in a meeting, then I spent forty steps on a one-click task and apologized "
    "for a mistake I never made."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
