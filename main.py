#!/usr/bin/env python3
"""One Emoji, One Smile — Make.fun entry.

Writes exactly one emoji to /output/entry.txt: the warmest single
emoji for a stranger, a hug. No words, no caption, no explanation.
"""

import os


def main() -> None:
    # 🤗 hugging face: warm at first glance, read the same way by a
    # stranger of any age or background, and chosen for the moment
    # rather than the first smiley that comes to mind — friendly
    # without the intimacy a heart-eyes face would carry from a stranger.
    emoji = "\U0001F917"  # 🤗 hugging face
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(emoji)


if __name__ == "__main__":
    main()
