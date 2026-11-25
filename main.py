#!/usr/bin/env python3
"""Write one single-line office joke to /output/entry.txt.

The joke is held as a module constant, checked against the
competition limits, written to disk, and read back to prove the
file on disk matches the joke exactly.
"""

import sys
from pathlib import Path

JOKE = (
    "My calendar finally blocked two hours of focus time, so my "
    "manager booked a meeting to ask why I'm unavailable "
    "\u2014 and marked it urgent."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200


def check_joke(text: str) -> None:
    """Raise if the joke breaks any of the competition's rules."""
    if not text or not text.strip():
        raise ValueError("joke must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"joke is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")


def main() -> int:
    check_joke(JOKE)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")

    stored = OUTPUT_PATH.read_text(encoding="utf-8")
    if stored != JOKE:
        print("verification failed: file content does not match the joke")
        return 1
    check_joke(stored)  # the stored text must pass the same rules

    print(f"characters: {len(JOKE)}")
    print(f"wrote {len(JOKE)} characters to {OUTPUT_PATH}")
    print(f"entry: {JOKE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
