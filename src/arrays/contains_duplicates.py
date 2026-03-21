def contains_duplicates_217_v1(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))


if __name__ == "__main__":
    print(contains_duplicates_217_v1([1, 2, 3, 4]))  # False
    print(contains_duplicates_217_v1([1, 2, 3, 3]))  # True
    print(contains_duplicates_217_v1([]))  # False
