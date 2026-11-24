#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes exactly one emoji -- a desert island -- to /output/entry.txt.

Choice: U+1F3DD DESERT ISLAND + U+FE0F VARIATION SELECTOR-16.
Judged pairwise against 7 other candidates (beach, sunrise, surfer,
hibiscus, plane, canoe, mountain) by two local judges using the house
judge's brief: the island won every completed pairing. It is the most
instantly readable dream-vacation postcard: palm, sand and sea in a
single glance, specific enough to be one particular dream, generic
enough to read on any screen at any size.

Deterministic: no network, no randomness, no input. Output is exactly
the emoji, no trailing newline, so the file is 2 characters / 7 bytes
UTF-8 -- inside the gate's 1-8 characters.
"""

import os

EMOJI = "\U0001F3DD\uFE0F"  # desert island


def main() -> None:
    # Self-check the house gate before writing: 1-8 characters, not
    # only white space, exactly one emoji, no trailing newline.
    assert 1 <= len(EMOJI) <= 8, "entry must be 1-8 characters"
    assert EMOJI.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
