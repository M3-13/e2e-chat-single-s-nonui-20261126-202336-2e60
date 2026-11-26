import re
import time

import pytest

from textutils import slugify


def test_normal_case() -> None:
    assert slugify("Hello, World!") == "hello-world"


def test_accents_and_whitespace() -> None:
    assert slugify("  Crème   brûlée  ") == "creme-brulee"


def test_only_punctuation_yields_empty() -> None:
    assert slugify("!!!") == ""


def test_empty_string() -> None:
    assert slugify("") == ""


def test_collapses_runs_and_strips_edges() -> None:
    assert slugify("--a___b  --  c--") == "a-b-c"


def test_digits_kept() -> None:
    assert slugify("Python 3.12 Release") == "python-3-12-release"


@pytest.mark.parametrize("text", ["日本語", "😀😀", "한국어 😀"])
def test_non_ascii_only_yields_empty(text: str) -> None:
    assert slugify(text) == ""


@pytest.mark.parametrize("value", [None, 42, b"abc", ["a"], 1.5])
def test_non_str_raises_type_error(value: object) -> None:
    with pytest.raises(TypeError):
        slugify(value)


def test_output_alphabet_and_hyphens() -> None:
    out = slugify("Ünï-cødé ß ﬁ ① \u2013 x̀ 日本 y")
    assert re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*|", out)


def test_one_megabyte_input_is_fast() -> None:
    for text in ("a-" * 524288, " " * 1_048_576, "!?" * 524288 + "x"):
        start = time.perf_counter()
        slugify(text)
        assert time.perf_counter() - start < 2.0
