"""Alien Field Notes: a two-day Earth review, filed by a visiting tourist.

The joke is a travel review written in the flat, five-star tone of a
satisfied customer, except the reviewer is an alien and the planet's
quirks do the work: oceans get full marks, while the locals earn a
puzzled footnote for paying to sit in traffic inside metal boxes they
polish on weekends. The closing line — 'Would abduct again' — lands
because it keeps the review format perfectly straight while quietly
admitting what kind of tourist this was.
"""

import os

ENTRY = "Earth review: stunning oceans, five stars. The inhabitants pay to sit in traffic inside metal boxes they polish on weekends. Would abduct again."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
