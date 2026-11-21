#!/usr/bin/env python3
"""Brave-judge entry: one quiet paragraph, written to entry.txt.

A single still scene, told slowly on purpose: a kettle gone quiet,
rain tracing the same path down a window, a porch light that stays
lit without waiting. The output is byte-identical on every run --
no input, no clock, no network, no randomness.
"""

import os

# Craft note: the passage is built from four still images, in the order
# the eye would find them on a quiet night -- kettle, window, road,
# night itself. Each image is one sentence; the joins are single spaces
# so the whole thing reads as one unhurried breath.
IMAGES = {
    "kettle": "The kettle has gone quiet.",
    "window": "Outside the window, rain finds the same slow path down the glass, again and again, patient as a hand learning a piano scale.",
    "road": "Down the road a porch light stays on, not waiting, just lit.",
    "night": "The night is long, and the light is in no hurry.",
}
IMAGE_ORDER = ("kettle", "window", "road", "night")


def build_entry() -> str:
    return " ".join(IMAGES[name] for name in IMAGE_ORDER)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    text = build_entry()
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text.encode('utf-8'))} bytes to {target}")


if __name__ == "__main__":
    main()
