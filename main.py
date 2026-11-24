#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes the one-line sick-day excuse to /output/entry.txt
(or $OUTPUT_DIR/entry.txt).
Standard library only; fully deterministic: the same text every run.

A sneeze so hard the back filed a formal complaint — and now the two
of them are in mediation.
"""

import os
from pathlib import Path

ENTRY = (
    "Calling in sick \u2014 I sneezed so hard my back filed a formal "
    "complaint and now we're in mediation.\n"
)


def validate(path: Path) -> str:
    """Read back the written file and assert it is exactly one line
    of 1 to 200 characters, per the competition gate."""
    text = path.read_text(encoding="utf-8")
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    lines = text.splitlines()
    assert len(lines) == 1, f"entry must be exactly one line, got {len(lines)}"
    assert lines[0].strip(), "entry must not be only white space"
    return text


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(ENTRY, encoding="utf-8")
    validate(out_path)


if __name__ == "__main__":
    main()
