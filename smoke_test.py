"""Smoke test for the text analyzer."""

from text_analyzer import text_statistics


def main():
    """Validate the analyzer on a known input."""
    text = "Hello world! This is a smoke test."
    result = text_statistics(text)

    assert result["characters"] == 34
    assert result["characters_without_spaces"] == 28
    assert result["words"] == 7
    assert result["sentences"] == 2
    assert result["average_word_length"] > 0
    assert len(result["word_frequency"]) == 7

    print("Smoke test passed.")


if __name__ == "__main__":
    main()