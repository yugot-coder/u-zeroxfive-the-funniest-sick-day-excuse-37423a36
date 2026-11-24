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
    """Read back the written file and assert it is exactly the entry.

    Checks, per the competition gate (1-200 characters, one line):
    * file ends with exactly one newline — no missing or trailing
      blank lines;
    * the single line carries no leading/trailing whitespace;
    * no control characters anywhere in the text;
    * byte length of the line is within 1-200 bytes;
    * the content is exactly the entry defined above.
    """
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    assert text.endswith("\n") and not text.endswith("\n\n"), (
        "entry must end with exactly one newline"
    )
    assert 1 <= len(raw) <= 200 + 1, (
        f"entry is {len(raw)} bytes, must be 1-200 plus one newline"
    )
    line = text[:-1]
    assert line == line.strip(), "entry must not have leading/trailing whitespace"
    assert all(ord(ch) >= 32 and ord(ch) != 127 for ch in line), (
        "entry must not contain control characters"
    )
    assert line == ENTRY.rstrip("\n"), "entry content does not match ENTRY"
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
