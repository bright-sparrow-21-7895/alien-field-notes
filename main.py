# The alien tourist's one-line review of Earth, filed on day two of the visit.
ENTRY = "Day two: the humans still pretend the small glowing rectangle is not their leader. We will wait."


def main():
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
