#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes exactly one funny line (84 chars, no trailing newline)
to /output/entry.txt. Pure stdlib, no network, no secrets.
"""

import os

ENTRY = "I asked my doctor for something to help me sleep. He prescribed my own wedding video."


def validate_entry() -> None:
    """Gate check: 1-200 chars, a single line, not only whitespace."""
    assert isinstance(ENTRY, str)
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"


def main() -> None:
    validate_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
