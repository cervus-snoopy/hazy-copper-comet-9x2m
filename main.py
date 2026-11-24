#!/usr/bin/env python3
"""Ship It Friday entry: writes one commit message to $MAKEFUN_OUTPUT_DIR/entry.txt."""
import os

LINE = "fix: force-pushed to main to fix the merge conflict \u2014 14 teammates' commits were the problem all along, ship it Friday"


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    os.chmod(out_dir, 0o755)
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == LINE
        assert 1 <= len(LINE) <= 159


if __name__ == "__main__":
    main()
