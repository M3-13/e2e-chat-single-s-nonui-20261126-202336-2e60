import time
from typing import Any

import pytest

from textutils.reverse_words import reverse_words


def test_basic() -> None:
    assert reverse_words("one two  three") == "three two one"


def test_surrounding_whitespace() -> None:
    assert reverse_words("  solo ") == "solo"


def test_empty() -> None:
    assert reverse_words("") == ""


def test_mixed_whitespace() -> None:
    assert reverse_words("a\tb\nc  \r\n d") == "d c b a"


@pytest.mark.parametrize("value", [None, 42, b"a b", ["a"]])
def test_non_str_raises(value: Any) -> None:
    with pytest.raises(TypeError):
        reverse_words(value)


def test_large_whitespace_is_fast() -> None:
    start = time.perf_counter()
    assert reverse_words(" " * 1_000_000) == ""
    assert time.perf_counter() - start < 1.0
