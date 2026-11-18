# Design: `top_words`

## Goal
Add a function `top_words(text: str, n: int = 3) -> list[tuple[str, int]]` that returns the `n` most frequent words in `text` with their counts.

## Requirements
1. Matching is case-insensitive; returned words are lowercase.
2. Leading/trailing punctuation is stripped from words (`"Hello," -> "hello"`). Inner apostrophes and hyphens are kept (`"don't"`, `"well-known"`).
3. Tokens that are empty after stripping are ignored.
4. Sort by count descending; ties are broken alphabetically ascending.
5. `n <= 0` raises `ValueError`.
6. If there are fewer than `n` distinct words, return all of them.
7. Empty or whitespace-only text returns `[]`.
8. Export `top_words` from the package (`from textstats import top_words`).
9. Also fix: `average_word_length("")` currently raises `ZeroDivisionError`; it must return `0.0`.

## Non-goals
- No stemming, no stop-word removal, no Unicode normalization.

## Tests
Every requirement above has at least one test in `tests/`.
