#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run — traffic jam entry.

Writes the two-line entry to /output/entry.txt with no trailing newline.
"""

import os

ENTRY_TEXT = (
    "A traffic jam is a herd of metal elephants that all decided to nap "
    "in the middle of the road.\n"
    "The elephants fit the slow shuffle and the way nothing can pass, but "
    "they leave out that no car is sleepy \u2014 each one is stuck because "
    "the road ahead is already full."
)
"""The entry text, kept as a documented module constant.

Line 1: one sentence, one metaphor (traffic jam = herd of metal elephants
napping in the middle of the road). Line 2: names what the metaphor maps
(the slow shuffle, nothing passing) and what it leaves out (no car is
sleepy — each is stuck because the road ahead is already full), correcting
the mistaken "decided to nap" idea instead of praising the metaphor.
"""


def _validate(text: str) -> None:
    """Gate: exactly 2 lines, 1-400 chars, non-blank, else ValueError."""
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError(f"expected 2 lines, got {len(lines)}")
    if not 1 <= len(text) <= 400:
        raise ValueError(f"expected 1-400 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be blank")


def main() -> None:
    _validate(ENTRY_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
