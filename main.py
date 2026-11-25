#!/usr/bin/env python3
"""Entry for Alien Field Notes (u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000).

Writes one line (max 200 characters): a review of planet Earth left by an
alien tourist, to /output/entry.txt. It must first read as a genuine review
of the planet, then land the joke: originality, a real review's voice, tight
writing. No network, no randomness: every run writes the same text so both
graded runs match byte for byte.
"""
from pathlib import Path

LINE = "Three stars: the water does a charming sky trick and the locals are warm, but they spend their one short orbit fighting over lines they drew on it."


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    entry_path = out / "entry.txt"
    entry_path.write_text(text, encoding="utf-8")
    print(text, f"({len(text)} chars)")


if __name__ == "__main__":
    main()
