from collections import Counter


def valid_anagram_242_v1(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    d1: dict[str, int] = {}
    d2: dict[str, int] = {}

    for i in range(len(s)):
        d1[s[i]] = d1.get(s[i], 0) + 1
        d2[t[i]] = d2.get(t[i], 0) + 1
    return d1 == d2


def valid_anagram_242_v2(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


def valid_anagram_242_v3(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    nums1 = [0] * 26
    nums2 = [0] * 26

    for i in range(len(s)):
        nums1[ord(s[i]) - ord("a")] += 1
        nums2[ord(t[i]) - ord("a")] += 1

    return nums1 == nums2


def valid_anagram_242_v4(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    nums1 = sorted(s)
    nums2 = sorted(t)

    for i in range(len(nums1)):
        if nums1[i] != nums2[i]:
            return False
    return True


if __name__ == "__main__":
    # print(valid_anagram_242_v1(s="racecar", t="carrace"))  # True
    # print(valid_anagram_242_v1(s="jar", t="jam"))  # False
    # print(valid_anagram_242_v1(s="anagram", t="nagaram"))  # True
    # print(valid_anagram_242_v1(s="rat", t="car"))  # False

    # print(valid_anagram_242_v2(s="racecar", t="carrace"))  # True
    # print(valid_anagram_242_v2(s="jar", t="jam"))  # False
    # print(valid_anagram_242_v2(s="anagram", t="nagaram"))  # True
    # print(valid_anagram_242_v2(s="rat", t="car"))  # False

    # print(valid_anagram_242_v3(s="racecar", t="carrace"))  # True
    # print(valid_anagram_242_v3(s="jar", t="jam"))  # False
    # print(valid_anagram_242_v3(s="anagram", t="nagaram"))  # True
    # print(valid_anagram_242_v3(s="rat", t="car"))  # False

    print(valid_anagram_242_v4(s="racecar", t="carrace"))  # True
    print(valid_anagram_242_v4(s="jar", t="jam"))  # False
    print(valid_anagram_242_v4(s="anagram", t="nagaram"))  # True
    print(valid_anagram_242_v4(s="rat", t="car"))  # False
