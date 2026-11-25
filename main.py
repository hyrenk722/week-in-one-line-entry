"""Write the week's one-liner to /output/entry.txt."""

import os

LINE = "Twenty-five contests, zero wins, one dog named Bu who now has a better homepage than I do."

# The gate requires 1-100 characters of UTF-8 text; the line is 90.
assert 1 <= len(LINE) <= 100

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
