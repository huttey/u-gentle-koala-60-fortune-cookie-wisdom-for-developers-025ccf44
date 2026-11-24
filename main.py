"""Fortune Cookie Wisdom for Developers — entry program.

Writes one original line of fortune-cookie wisdom for a software
developer to /output/entry.txt. Gate: UTF-8 text, 1 to 120 characters.
"""

import os

LINE = "A deploy on Friday teaches patience; a deploy on Monday teaches humility."

assert 1 <= len(LINE) <= 120, "line must be 1-120 characters"
assert LINE.strip() == LINE and LINE.strip(), "line must be non-whitespace"
assert "\n" not in LINE and LINE.endswith("."), "line must be one sentence ending in a period"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
