import os

# Single deterministic patch-note line, written with no trailing newline.
LINE = "Fixed sleep: you now wake up rested instead of tired, and 3 a.m. ceiling-staring is no longer a feature."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
