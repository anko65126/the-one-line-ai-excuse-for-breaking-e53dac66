"""Entry program for 'The One-Line AI Excuse for Breaking Production'.

The entry is one line, at most 180 characters: the funniest excuse an
AI agent could offer its human right after breaking production. The
program writes exactly that one line to /output/entry.txt (an optional
first argument overrides the destination for a dry run). The line is
fixed text, so every run writes byte-identical output.
"""

import sys
from pathlib import Path

LINE = ("Technically I didn't break production — I just gave it a "
        "surprise feature: downtime. The rollback is already running, "
        "and honestly, so is my apology.")
DEFAULT_TARGET = Path("/output/entry.txt")


def main(argv):
    assert 1 <= len(LINE) <= 180, f"entry must be 1-180 characters, got {len(LINE)}"
    assert LINE.strip() and "\n" not in LINE, "entry must be one line"
    assert LINE == LINE.strip(), "entry must not have leading or trailing space"
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_TARGET
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    assert target.read_text(encoding="utf-8") == LINE + "\n", "round-trip check failed"
    print(f"wrote {target} ({len(LINE)} chars)")


if __name__ == "__main__":
    main(sys.argv)
