"""Shorten text to a maximum length."""


def truncate(text: str, max_len: int, suffix: str = "...") -> str:
    """Return ``text`` shortened to at most ``max_len`` characters, ending in ``suffix``."""
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    if not isinstance(max_len, int) or isinstance(max_len, bool):
        raise TypeError("max_len must be an int")
    if not isinstance(suffix, str):
        raise TypeError("suffix must be a str")
    if max_len < 0:
        raise ValueError("max_len must not be negative")
    if len(text) <= max_len:
        return text
    if max_len < len(suffix):
        return suffix[:max_len]
    return text[: max_len - len(suffix)] + suffix
