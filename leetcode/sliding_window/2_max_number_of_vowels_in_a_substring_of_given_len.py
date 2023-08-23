def max_vowels(s: str, k: int) -> int:
    vowels: tuple = ('a', 'e', 'i', 'o', 'u')
    count_vowels: int = 0

    for current_letter in range(k):
        if s[current_letter] in vowels:
            count_vowels += 1

    max_vowels: int = count_vowels

    for current_letter in range(k, len(s)):
        count_vowels += int(s[current_letter] in vowels)
        count_vowels -= int(s[current_letter - k] in vowels)
        max_vowels = max(max_vowels, count_vowels)

    return max_vowels


def test() -> None:
    assert max_vowels('abciiidef', k = 3) == 3
    assert max_vowels('aeiou', k = 2) == 2
    assert max_vowels('leetcode', k = 3) == 2


test()
