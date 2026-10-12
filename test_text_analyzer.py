"""Unit tests for text_analyzer."""

import math

import pytest

from text_analyzer import (
    analyze_numbers,
    average_word_length,
    count_characters,
    count_sentences,
    count_words,
    most_common_words,
    text_statistics,
    validate_text,
    word_frequency,
)


def test_validate_text_accepts_valid_text():
    """Valid text should be accepted."""
    assert validate_text("Hello world") is True


def test_validate_text_rejects_non_string():
    """Non-string input should raise TypeError."""
    with pytest.raises(TypeError):
        validate_text(123)


def test_validate_text_rejects_empty_string():
    """Empty text should raise ValueError."""
    with pytest.raises(ValueError):
        validate_text("")


def test_count_characters():
    """Character count should include spaces by default."""
    assert count_characters("Hello world") == 11


def test_count_characters_without_spaces():
    """Character count can exclude whitespace."""
    assert count_characters(
        "Hello world",
        include_spaces=False,
    ) == 10


def test_count_words():
    """Word count should work with normal text."""
    assert count_words("Hello world this is Python") == 5


def test_count_sentences():
    """Sentence counting should recognize punctuation."""
    text = "Hello! How are you? I am fine."
    assert count_sentences(text) == 3


def test_word_frequency():
    """Word frequency should be case-insensitive."""
    result = word_frequency("Hello hello HELLO world")

    assert result["hello"] == 3
    assert result["world"] == 1


def test_most_common_words():
    """Most common words should be sorted by frequency."""
    result = most_common_words(
        "apple apple apple banana banana orange",
        limit=2,
    )

    assert result == [
        ("apple", 3),
        ("banana", 2),
    ]


def test_average_word_length():
    """Average word length should be calculated correctly."""
    assert average_word_length("aa bbbb") == 3.0


def test_text_statistics():
    """Text statistics should contain all expected fields."""
    result = text_statistics("Hello world!")

    assert result["words"] == 2
    assert result["sentences"] == 1
    assert result["characters"] == 12


def test_analyze_numbers():
    """Numeric statistics should be calculated correctly."""
    result = analyze_numbers([1, 2, 3, 4, 5])

    assert result["minimum"] == 1
    assert result["maximum"] == 5
    assert result["sum"] == 15
    assert result["average"] == 3


def test_analyze_numbers_with_infinity():
    """Infinity should be handled explicitly."""
    result = analyze_numbers([1, 2, float("inf")])

    assert result["contains_infinity"] is True


def test_analyze_numbers_with_nan():
    """NaN should be detected explicitly."""
    result = analyze_numbers([1, 2, float("nan")])

    assert result["contains_nan"] is True


def test_analyze_numbers_with_negative_values():
    """Negative numbers should be supported."""
    result = analyze_numbers([-10, -5, 0, 5, 10])

    assert result["minimum"] == -10
    assert result["maximum"] == 10
def test_chinese_characters():
    """Chinese Unicode characters should be processed."""
    text = "你好世界"

    assert count_words(text) > 0
    assert count_characters(text) == 4


def test_arabic_characters():
    """Arabic Unicode characters should be processed."""
    text = "مرحبا بالعالم"

    assert count_words(text) > 0
    assert count_characters(text) == len(text)


def test_emoji():
    """Emoji should not cause the analyzer to crash."""
    text = "Hello 😊 world 🌍"

    assert count_characters(text) == len(text)
    assert count_words(text) >= 2


def test_accented_characters():
    """Accented Latin characters should be supported."""
    text = "Café résumé naïve"

    assert count_words(text) == 3


def test_very_long_string():
    """Very long input should be processed."""
    text = "hello " * 100_000

    assert count_words(text) == 100_000


def test_multiple_spaces():
    """Multiple whitespace characters should be handled."""
    text = "hello     world"

    assert count_words(text) == 2


def test_newlines_and_tabs():
    """Newlines and tabs should be handled."""
    text = "hello\tworld\npython"

    assert count_words(text) == 3