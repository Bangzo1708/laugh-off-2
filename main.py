#!/usr/bin/env python3
"""One-Line Laugh-Off -- round 2 entry.

Writes exactly one funny line to <output dir>/entry.txt.

The line: a self-help book files a restraining order against its reader.
Setup ("I bought a self-help book") promises self-improvement; the punch
("it filed a restraining order against me") reverses it completely --
the book helps itself by getting rid of me. One twist, landing on the
last word, no wasted words. 70 characters, well inside the 1-200 gate.
"""

import os
from pathlib import Path

LINE = "I bought a self-help book and it filed a restraining order against me."

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(LINE, encoding="utf-8")
    os.chmod(entry, 0o644)

if __name__ == "__main__":
    main()
