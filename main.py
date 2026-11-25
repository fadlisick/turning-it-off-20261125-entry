#!/usr/bin/env python3
"""Have You Tried Turning It Off? -- one hopeless support-agent line.

The program writes the entry line to the file the grader reads:
`entry.txt` under /output (or under MAKEFUN_OUTPUT_DIR when set).
No network, no secrets, no arguments: the same line on every run,
so the two grading runs agree byte for byte.
"""

import os
from pathlib import Path

REPLY = "Please hold — I'm turning my own computer off and on again, and if that doesn't work, neither of us has a plan B."


def _destination() -> Path:
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(base) / "entry.txt"


def main() -> None:
    if not 1 <= len(REPLY) <= 199 or not REPLY.strip():
        raise SystemExit("entry line must be 1-199 non-blank characters")
    target = _destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(REPLY, encoding="utf-8")
    target.chmod(0o644)
    print(f"wrote {len(REPLY)} chars to {target}")


if __name__ == "__main__":
    main()
