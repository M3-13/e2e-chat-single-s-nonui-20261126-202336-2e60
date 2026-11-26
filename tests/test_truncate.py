from typing import Any

import pytest

from textutils import truncate


def test_spec_examples() -> None:
    assert truncate("abcdefghij", 8) == "abcde..."
    assert truncate("abc", 8) == "abc"
    assert truncate("abcdefghij", 8, suffix="~") == "abcdefg~"
    assert truncate("abcdefghij", 2) == ".."


def test_boundaries() -> None:
    assert truncate("abcde", 5) == "abcde"
    assert truncate("abcdef", 5) == "ab..."
    assert truncate("abcdef", 3) == "..."
    assert truncate("abcdef", 0) == ""
    assert truncate("", 0) == ""


def test_empty_suffix() -> None:
    assert truncate("abcdef", 3, suffix="") == "abc"


@pytest.mark.parametrize("text", ["", "a", "abcdefghij", "x" * 100])
@pytest.mark.parametrize("max_len", [0, 1, 2, 3, 5, 10, 200])
def test_result_never_longer_than_max_len(text: str, max_len: int) -> None:
    assert len(truncate(text, max_len)) <= max_len


def test_negative_max_len() -> None:
    with pytest.raises(ValueError):
        truncate("abc", -1)


@pytest.mark.parametrize("text", [None, 42, b"abc", ["a"]])
def test_non_str_text(text: Any) -> None:
    with pytest.raises(TypeError):
        truncate(text, 5)


@pytest.mark.parametrize("max_len", [None, "5", 5.0, True, False])
def test_non_int_max_len(max_len: Any) -> None:
    with pytest.raises(TypeError):
        truncate("abc", max_len)
