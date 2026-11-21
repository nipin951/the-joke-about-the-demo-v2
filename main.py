"""The joke about the demo — writes one one-line joke to /output/entry.txt."""

import os

# One line, no setup beyond the crash itself: the agent's calm is the punchline.
JOKE = 'The demo crashed live in front of the whole company. My agent stayed calm: by the time I sat down it had written the postmortem, the apology email, and my resignation letter — just in case.'


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
