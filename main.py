"""Make the AI judge feel brave — make.fun entry.

Writes one short relaxing text to /output/entry.txt (or the directory
named by MAKEFUN_OUTPUT_DIR). Deterministic, standard library only,
no network.
"""

import os

ENTRY_TEXT = (
    "The kettle has gone quiet. Outside the window, rain finds the same "
    "slow path down the glass, again and again, patient as a hand "
    "learning a piano scale. Down the road a porch light stays on, not "
    "waiting, just lit. The night is long, and the light is in no hurry."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
