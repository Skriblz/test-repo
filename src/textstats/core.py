import string
from collections import Counter


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in ``text``."""
    return len(text.split())


def average_word_length(text: str) -> float:
    """Return the average length of the words in ``text`` (``0.0`` if there are none)."""
    words = text.split()
    if not words:
        return 0.0
    return sum(len(w) for w in words) / len(words)


def top_words(text: str, n: int = 3) -> list[tuple[str, int]]:
    """Return the ``n`` most frequent words in ``text`` with their counts.

    Words are lowercased and stripped of leading/trailing punctuation; ties are
    broken alphabetically.
    """
    if n <= 0:
        raise ValueError("n must be positive")
    words = (w.strip(string.punctuation).lower() for w in text.split())
    counts = Counter(w for w in words if w)
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:n]
