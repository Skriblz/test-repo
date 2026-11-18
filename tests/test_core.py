from textstats import average_word_length, word_count


def test_word_count_simple():
    assert word_count("hello world") == 2


def test_word_count_extra_whitespace():
    assert word_count("  hello   world \n") == 2


def test_average_word_length():
    assert average_word_length("ab abcd") == 3.0
