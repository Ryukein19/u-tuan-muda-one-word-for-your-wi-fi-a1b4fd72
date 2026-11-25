import os
# One-word entry (11 chars): the word below is the whole submission.
# Writes to /output/entry.txt.
LINE = "Schrödinger"
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
