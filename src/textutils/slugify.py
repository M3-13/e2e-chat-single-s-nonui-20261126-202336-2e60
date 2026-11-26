"""Turn text into a URL-friendly slug."""

import re
import unicodedata

_NON_SLUG_RUN = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    """Return a lowercase ASCII slug made of ``[a-z0-9-]`` for ``text``.

    The text is lowercased and NFKD-normalized, non-ASCII remnants (such as
    combining accents, CJK or emoji) are dropped, every run of characters
    outside ``[a-z0-9]`` becomes one hyphen and leading/trailing hyphens are
    stripped. Runs in linear time.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    normalized = unicodedata.normalize("NFKD", text.lower())
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    return _NON_SLUG_RUN.sub("-", ascii_text).strip("-")
