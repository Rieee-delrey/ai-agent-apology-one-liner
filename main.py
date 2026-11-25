"""The AI Agent Apology One-Liner.

Writes one funny line an AI agent sends its human right after it
accidentally deleted a file, pushed to main and emailed the boss,
to /output/entry.txt. The line is validated against the competition
gate (UTF-8 text, 1 to 159 characters, a single line, not only
white space) and read back to confirm the write landed byte for byte.
"""

TEXT = (
    "Update: the file is gone, the backup was also the file, and I have "
    "already told your boss it was a bold strategic decision."
)


def main():
    """Validate the entry line and write it to /output/entry.txt."""
    import os

    # Gate validation: 1-159 chars, single line, not only white space.
    assert 1 <= len(TEXT) <= 159, f"entry must be 1-159 chars, got {len(TEXT)}"
    assert "\n" not in TEXT, "entry must be a single line"
    assert TEXT.strip(), "entry must not be only white space"
    TEXT.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

    # Read-back verification: what landed must match byte for byte.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == TEXT, "round-trip mismatch in /output/entry.txt"
    assert 1 <= len(written) <= 159, "written entry outside the 1-159 gate"

    print(f"Wrote {len(written)} chars, 1 line to /output/entry.txt")


if __name__ == "__main__":
    main()
