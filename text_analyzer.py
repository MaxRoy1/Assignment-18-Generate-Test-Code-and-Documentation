"""Text analysis utilities.

This module provides functions for analyzing text, including word
counting, character counting, sentence detection, and word frequency
analysis.
"""

import math
import re
from collections import Counter


def validate_text(text):
    """Validate that the input is a string.

    :param text: Input value to validate.
    :type text: str
    :raises TypeError: If text is not a string.
    :raises ValueError: If text is empty.
    :return: True if the text is valid.
    :rtype: bool
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not text.strip():
        raise ValueError("text cannot be empty")

    return True


def count_characters(text, include_spaces=True):
    """Count the number of characters in a text.

    :param text: Text to analyze.
    :type text: str
    :param include_spaces: Whether whitespace should be counted.
    :type include_spaces: bool
    :return: Number of characters.
    :rtype: int
    """
    validate_text(text)

    if include_spaces:
        return len(text)

    return len("".join(text.split()))


def count_words(text):
    """Count words in a text.

    Unicode letters and numbers are supported.

    :param text: Text to analyze.
    :type text: str
    :return: Number of words.
    :rtype: int
    """
    validate_text(text)

    words = re.findall(r"\b[\w'-]+\b", text, flags=re.UNICODE)

    return len(words)


def count_sentences(text):
    """Count sentences in a text.

    Sentences are detected using '.', '!' and '?'.

    :param text: Text to analyze.
    :type text: str
    :return: Number of sentences.
    :rtype: int
    """
    validate_text(text)

    sentences = re.findall(r"[.!?]+", text)

    return len(sentences)


def word_frequency(text):
    """Return the frequency of each word.

    The comparison is case-insensitive.

    :param text: Text to analyze.
    :type text: str
    :return: Dictionary containing word frequencies.
    :rtype: dict
    """
    validate_text(text)

    words = re.findall(r"\b[\w'-]+\b", text.lower(), flags=re.UNICODE)

    return dict(Counter(words))


def most_common_words(text, limit=5):
    """Return the most common words.

    :param text: Text to analyze.
    :type text: str
    :param limit: Maximum number of words to return.
    :type limit: int
    :return: List of word-frequency pairs.
    :rtype: list
    """
    validate_text(text)

    if not isinstance(limit, int):
        raise TypeError("limit must be an integer")

    if limit <= 0:
        raise ValueError("limit must be greater than zero")

    frequencies = word_frequency(text)

    return sorted(
        frequencies.items(),
        key=lambda item: (-item[1], item[0]),
    )[:limit]


def average_word_length(text):
    """Calculate the average word length.

    :param text: Text to analyze.
    :type text: str
    :return: Average word length.
    :rtype: float
    """
    validate_text(text)

    words = re.findall(r"\b[\w'-]+\b", text, flags=re.UNICODE)

    if not words:
        return 0.0

    total_length = sum(len(word) for word in words)

    return total_length / len(words)


def text_statistics(text):
    """Return a collection of statistics about the text.

    :param text: Text to analyze.
    :type text: str
    :return: Dictionary containing text statistics.
    :rtype: dict
    """
    validate_text(text)

    return {
        "characters": count_characters(text),
        "characters_without_spaces": count_characters(
            text,
            include_spaces=False,
        ),
        "words": count_words(text),
        "sentences": count_sentences(text),
        "average_word_length": average_word_length(text),
        "word_frequency": word_frequency(text),
    }


def analyze_numbers(numbers):
    """Calculate basic statistics for numeric input.

    :param numbers: A list of numeric values.
    :type numbers: list
    :raises TypeError: If numbers is not a list.
    :raises ValueError: If the list is empty.
    :return: Numeric statistics.
    :rtype: dict
    """
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")

    if not numbers:
        raise ValueError("numbers cannot be empty")

    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("all values must be numeric")

    total = sum(numbers)
    average = total / len(numbers)

    return {
        "minimum": min(numbers),
        "maximum": max(numbers),
        "sum": total,
        "average": average,
        "contains_nan": any(math.isnan(x) for x in numbers),
        "contains_infinity": any(math.isinf(x) for x in numbers),
    }


if __name__ == "__main__":
    example = (
        "Hello world! "
        "This is a small text analysis example."
    )

    print("Text statistics:")
    print(text_statistics(example))

    print("\nNumeric statistics:")
    print(analyze_numbers([1, 2, 3, 4, 5]))
    