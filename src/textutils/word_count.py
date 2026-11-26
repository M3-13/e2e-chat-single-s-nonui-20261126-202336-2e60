"""Count the words of a text."""


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in ``text``.

    Raises ``TypeError`` if ``text`` is not a ``str``.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    return len(text.split())
