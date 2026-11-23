"""One Emoji, One Smile — make.fun entry.

The entry is a single emoji, written to /output/entry.txt:

    🥹  (U+1F979 FACE HOLDING BACK TEARS)

Why this emoji wins against the brief, criterion by criterion:

1. Warm at first glance. A face holding back happy tears reads instantly
   as touched and grateful — someone about to smile because something
   kind just happened. No context is needed to feel it.
2. Universal. No words, no irony, no in-joke. A stranger of any age or
   background reads the same tender feeling: moved, not mocking.
3. Chosen rather than default. It is not the first smiley everyone sends
   (🙂). It carries a specific, tender feeling — gratitude on the edge
   of tears — so it feels picked for the moment, while staying instantly
   readable. The tears are happy ones: the face is holding back a smile
   it can barely contain, which is exactly the feeling a stranger's
   kindness leaves behind.
4. Right for a stranger. It expresses warmth without intimacy, sarcasm
   or flirtation. Nothing about it reads oddly coming from someone
   unknown; it is the emoji equivalent of a kind look from a passer-by.

The program asserts the entry meets the competition gate before writing:
UTF-8 text of 1 to 8 characters, not only white space, exactly one emoji
(one Unicode code point) and nothing else.
"""

import os
import stat
import unicodedata

ENTRY = "🥹"  # U+1F979 FACE HOLDING BACK TEARS — one Unicode code point.
OUTPUT_PATH = "/output/entry.txt"


def _is_emoji(char: str) -> bool:
    """Best-effort single-character emoji check without network or data files."""
    if len(char) != 1:
        return False
    # Emoji faces/symbols live in the "Symbol, other" (So) category;
    # whitespace and control characters are excluded by the gate below.
    return unicodedata.category(char) == "So"


def main() -> None:
    text = ENTRY
    # Gate: 1 to 8 characters, not only white space, exactly one emoji.
    assert isinstance(text, str), "entry must be text"
    assert 1 <= len(text) <= 8, f"entry must be 1-8 characters, got {len(text)}"
    assert text.strip(), "entry must not be only white space"
    assert len(text) == 1, f"entry must be exactly one emoji, got {len(text)} code points"
    assert _is_emoji(text), f"entry must be a single emoji, got U+{ord(text):04X}"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
