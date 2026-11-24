#!/usr/bin/env python3
"""One Word, One Username, One Reward -- make.fun entry.

Writes the entrant's own make.fun handle, one word and nothing else,
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Stdlib only.
"""

import os

USERNAME = "ryanefri10"


def validate(text):
    """Mirror the competition gate: UTF-8 text, 1-30 chars, one word."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) != len(text.strip()) or len(text.split()) != 1:
        raise ValueError("entry must be a single word with no padding")
    if not 1 <= len(text) <= 30:
        raise ValueError("entry must be 1-30 characters")
    return text


def main():
    entry = validate(USERNAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
