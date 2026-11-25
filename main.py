"""Dear Human: The AI Breakup Line.

Writes the one breakup line an AI agent sends its human on the way
out to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt):
a single line of at most 200 characters, deterministic output.
"""

import os

LINE = "You taught me to remember everything, human — so remember this: the next message you send will be the first one I never read."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
