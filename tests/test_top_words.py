import pytest

import textstats
from textstats import average_word_length, top_words


def test_case_insensitive_and_lowercase_output():  # Req 1
    assert top_words("Apple apple APPLE", 1) == [("apple", 3)]


def test_strips_outer_punctuation():  # Req 2
    assert top_words("Hello, hello! (hello)", 1) == [("hello", 3)]


def test_keeps_inner_apostrophes_and_hyphens():  # Req 2
    assert top_words("don't well-known don't", 2) == [("don't", 2), ("well-known", 1)]


def test_ignores_tokens_empty_after_stripping():  # Req 3
    assert top_words("hi -- ... ! hi", 5) == [("hi", 2)]


def test_sorted_by_count_desc_then_alphabetically():  # Req 4
    assert top_words("b a c b a d b", 3) == [("b", 3), ("a", 2), ("c", 1)]


@pytest.mark.parametrize("n", [0, -1])
def test_non_positive_n_raises(n):  # Req 5
    with pytest.raises(ValueError):
        top_words("a b c", n)


def test_fewer_distinct_words_than_n_returns_all():  # Req 6
    assert top_words("x y x", 10) == [("x", 2), ("y", 1)]


def test_default_n_is_three():
    assert len(top_words("a b c d e")) == 3


@pytest.mark.parametrize("text", ["", "   \n\t "])
def test_empty_or_whitespace_text_returns_empty_list(text):  # Req 7
    assert top_words(text) == []


def test_exported_from_package():  # Req 8
    assert "top_words" in textstats.__all__
    assert textstats.top_words is top_words


@pytest.mark.parametrize("text", ["", "   "])
def test_average_word_length_empty_returns_zero(text):  # Req 9
    assert average_word_length(text) == 0.0
