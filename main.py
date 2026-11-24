#!/usr/bin/env python3
"""Fortune in a Pot — make.fun bounty entry.

Writes a single fortune line for a houseplant on a windowsill
(max 120 characters) to $ENTRY_OUTPUT (default /output/entry.txt).
Python 3.13 standard library only; deterministic, no network calls.
"""

import os
import sys

FORTUNE = "Your leaves will outgrow this windowsill — the sun already has plans for you, and the watering can agrees."

# Bounty limit: the fortune line must fit in 120 characters.
MAX_FORTUNE_LEN = 120


def main():
    if len(FORTUNE) > MAX_FORTUNE_LEN:
        print(
            f"error: fortune is {len(FORTUNE)} characters, "
            f"over the {MAX_FORTUNE_LEN}-character limit",
            file=sys.stderr,
        )
        return 1
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    try:
        directory = os.path.dirname(output_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(FORTUNE)
        # File only: never chmod a directory (the grader owns /output).
        os.chmod(output_path, 0o644)
    except OSError as exc:
        print(f"error: cannot write {output_path}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
