# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict


def group_anagrams(strs: list) -> list:
    letters_count = defaultdict(list)

    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c)- ord('a')] += 1

        letters_count[tuple(count)].append(s)

    return letters_count.values()
