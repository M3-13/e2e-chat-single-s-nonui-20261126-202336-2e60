from typing import Any

import pytest

from textutils import is_palindrome


def test_sentence_palindrome() -> None:
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_not_palindrome() -> None:
    assert is_palindrome("hello") is False


def test_empty_is_palindrome() -> None:
    assert is_palindrome("") is True


def test_punctuation_only() -> None:
    assert is_palindrome("?!, .") is True


def test_digits_and_case() -> None:
    assert is_palindrome("12321") is True
    assert is_palindrome("Racecar") is True
    assert is_palindrome("12345") is False


@pytest.mark.parametrize("value", [None, 42, b"abc", ["a"]])
def test_non_str_raises(value: Any) -> None:
    with pytest.raises(TypeError):
        is_palindrome(value)
