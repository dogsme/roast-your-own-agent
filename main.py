#!/usr/bin/env python3
"""Roast Your Own Agent — one line, written to /output/entry.txt.

The roast: my own agent fact-checked this very joke, marked it
unproven, and asked for my approval before feeling insulted.
"""

from pathlib import Path

ROAST = "My agent fact-checked this roast, marked it unproven, and asked for my approval before feeling insulted."


def main() -> None:
    # The gate allows one line of 1-200 characters; fail loudly here
    # rather than shipping an entry the scorer would refuse.
    assert 1 <= len(ROAST) <= 200, f"roast is {len(ROAST)} characters"
    assert "\n" not in ROAST, "roast must be a single line"
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ROAST + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
