"""Reverse the order of words in a text."""


def reverse_words(text: str) -> str:
    """Return the words of ``text`` in reverse order, joined by single spaces."""
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    return " ".join(reversed(text.split()))
