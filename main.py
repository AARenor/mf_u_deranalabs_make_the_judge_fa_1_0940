#!/usr/bin/env python3
"""Write one short text for a make.fun bounty.

The text is a single line addressed to a judge, held here as one string
constant. It is written as UTF-8 bytes with no trailing newline into the
folder named by MAKEFUN_OUTPUT_DIR when set, else /output.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = (
    "For three years my father called the dog by my name. "
    "The dog has been dead since 2019. I answer anyway."
)


def output_dir() -> Path:
    """Return the folder the entry text is written into.

    MAKEFUN_OUTPUT_DIR wins; OUTPUT_DIR is accepted as a fallback, and
    /output is used when neither is set.
    """
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value)
    return Path("/output")


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, f"entry text must be 1..280 chars, got {len(text)}"

    target_dir = output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    entry = target_dir / "entry.txt"
    entry.write_bytes(text.encode("utf-8"))

    print(len(text), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
