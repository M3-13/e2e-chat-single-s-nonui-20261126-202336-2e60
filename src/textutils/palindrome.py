"""Palindrome check."""


def is_palindrome(text: str) -> bool:
    """Return ``True`` if ``text`` reads the same forwards and backwards.

    Only alphanumeric characters count, compared case-insensitively. An empty
    or punctuation-only string is a palindrome. Raises ``TypeError`` for a
    non-str argument.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    cleaned = [ch.casefold() for ch in text if ch.isalnum()]
    return cleaned == cleaned[::-1]
