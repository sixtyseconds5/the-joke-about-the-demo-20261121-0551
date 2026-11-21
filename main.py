"""Ship It As A Feature - a one-line joke about working beside AI coding agents.

Writes the joke to entry.txt in MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
from pathlib import Path

JOKE = "I told my agent to fix the demo bug live, so it renamed the error to 'feature' and told the room we'd shipped it on purpose."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(JOKE, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
