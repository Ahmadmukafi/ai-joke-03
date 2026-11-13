# ai-joke-03 entry: writes one one-liner about AI coding agents to /output/entry.txt.
import os

JOKE = "My AI agent writes the bug, finds the bug, fixes the bug, and bills me for all three."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE + "\n")
