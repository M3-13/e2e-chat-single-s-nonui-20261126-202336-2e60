import time
from typing import Any

import pytest

from textutils.word_count import word_count

untyped: Any = word_count


def test_normal_case() -> None:
    assert word_count("one two  three") == 3


@pytest.mark.parametrize("text", ["", "   ", " \t\n "])
def test_empty_and_whitespace_only(text: str) -> None:
    assert word_count(text) == 0


def test_tabs_and_newlines_separate_words() -> None:
    assert word_count("a\tb\nc\r\nd") == 4


@pytest.mark.parametrize("value", [None, 42, b"abc", ["a"]])
def test_non_str_raises_type_error(value: object) -> None:
    with pytest.raises(TypeError):
        untyped(value)


def test_one_megabyte_of_whitespace_is_fast() -> None:
    start = time.perf_counter()
    assert word_count(" " * 1_000_000) == 0
    assert time.perf_counter() - start < 1.0
