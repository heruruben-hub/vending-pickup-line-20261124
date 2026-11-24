#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt (max 200 characters, one line).
"""

import os

ENTRY = (
    "No exact change needed \u2014 just press B7. "
    "I've been humming in this hallway all day, "
    "but you walked by and now my coil won't stop spinning."
)


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 200, f"entry is {len(line)} characters"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
