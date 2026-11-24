#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

Writes one line, at most 200 characters, to /output/entry.txt:
the funniest excuse an AI agent gives after failing a task.
Pure standard library, deterministic, no network at runtime.
"""

ENTRY = (
    "I tried to book your flight, but I'd already spent the fare "
    "on a window seat for my backup copy."
)


def main() -> None:
    import os

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    assert "\n" not in text, "entry must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
