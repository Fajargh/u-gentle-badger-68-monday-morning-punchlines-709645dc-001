"""Monday Morning Punchlines — writes one joke to /output/entry.txt."""

import os

JOKE = (
    "Monday morning is the only magic trick I know: "
    "I blink on Sunday night and wake up in a meeting "
    "I never agreed to attend."
)


def main():
    # Gate guard: the entry must be 1-200 non-whitespace characters.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
