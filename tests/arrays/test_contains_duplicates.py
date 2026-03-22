import pytest

from src.arrays.contains_duplicates import (
    contains_duplicates_217_v1,
    contains_duplicates_217_v2,
    contains_duplicates_217_v3,
)


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], False),
        ([1, 2, 3, 3], True),
        ([10], False),
        ([], False),
        ([1, 1, 1, 1, 2, 2, 3, 3, 4, 1], True),
    ],
)
def test_contains_duplicates_v1(nums: list[int], expected: bool) -> None:
    assert contains_duplicates_217_v1(nums) == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], False),
        ([1, 2, 3, 3], True),
        ([10], False),
        ([], False),
        ([1, 1, 1, 1, 2, 2, 3, 3, 4, 1], True),
    ],
)
def test_contains_duplicates_v2(nums: list[int], expected: bool) -> None:
    assert contains_duplicates_217_v2(nums) == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], False),
        ([1, 2, 3, 3], True),
        ([10], False),
        ([], False),
        ([1, 1, 1, 1, 2, 2, 3, 3, 4, 1], True),
    ],
)
def test_contains_duplicates_v3(nums: list[int], expected: bool) -> None:
    assert contains_duplicates_217_v3(nums) == expected
