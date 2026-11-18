def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in ``text``."""
    return len(text.split())


def average_word_length(text: str) -> float:
    """Return the average length of the words in ``text``."""
    words = text.split()
    return sum(len(w) for w in words) / len(words)
