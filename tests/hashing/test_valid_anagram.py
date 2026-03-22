import pytest

from src.hashing.valid_anagram import (
    valid_anagram_242_v1,
    valid_anagram_242_v2,
    valid_anagram_242_v3,
    valid_anagram_242_v4,
)


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("racecar", "carrace", True),
        ("jar", "jam", False),
        ("anagram", "nagaram", True),
        ("rat", "car", False),
    ],
)
def test_valid_anagram_v1(s: str, t: str, expected: bool) -> None:
    assert valid_anagram_242_v1(s, t) == expected


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("racecar", "carrace", True),
        ("jar", "jam", False),
        ("anagram", "nagaram", True),
        ("rat", "car", False),
    ],
)
def test_valid_anagram_v2(s: str, t: str, expected: bool) -> None:
    assert valid_anagram_242_v2(s, t) == expected


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("racecar", "carrace", True),
        ("jar", "jam", False),
        ("anagram", "nagaram", True),
        ("rat", "car", False),
    ],
)
def test_valid_anagram_v3(s: str, t: str, expected: bool) -> None:
    assert valid_anagram_242_v3(s, t) == expected


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("racecar", "carrace", True),
        ("jar", "jam", False),
        ("anagram", "nagaram", True),
        ("rat", "car", False),
    ],
)
def test_valid_anagram_v4(s: str, t: str, expected: bool) -> None:
    assert valid_anagram_242_v4(s, t) == expected
