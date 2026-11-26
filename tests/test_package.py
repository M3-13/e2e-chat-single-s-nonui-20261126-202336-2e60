import importlib

import pytest

NAMES = ["slugify", "truncate", "word_count", "is_palindrome", "reverse_words"]


@pytest.mark.parametrize("name", NAMES)
def test_name_is_importable_and_callable(name: str) -> None:
    module = importlib.import_module("textutils")
    assert callable(getattr(module, name))


def test_all_lists_the_five_functions() -> None:
    import textutils

    assert sorted(textutils.__all__) == sorted(NAMES)
