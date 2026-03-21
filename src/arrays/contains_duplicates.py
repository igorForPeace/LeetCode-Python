def contains_duplicates_217_v1(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))


def contains_duplicates_217_v2(nums: list[int]) -> bool:
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False


def contains_duplicates_217_v3(nums: list[int]) -> bool:
    s = set()
    for i in range(len(nums)):
        if nums[i] in s:
            return True
        s.add(nums[i])
    return False


if __name__ == "__main__":
    print(contains_duplicates_217_v1([1, 2, 3, 4]))  # False
    print(contains_duplicates_217_v1([1, 2, 3, 3]))  # True

    print(contains_duplicates_217_v2([1, 2, 3, 4]))
    print(contains_duplicates_217_v2([1, 2, 3, 3]))

    print(contains_duplicates_217_v3([1, 2, 3, 4]))
    print(contains_duplicates_217_v3([1, 2, 3, 3]))
