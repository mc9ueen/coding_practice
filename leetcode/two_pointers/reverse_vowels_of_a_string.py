# https://leetcode.com/problems/reverse-vowels-of-a-string/
def reverse_vowels(s: str) -> str:
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

    line = list(s)
    left: int = 0
    right: int = len(line) - 1

    while left < right:
        if line[left] in vowels and line[right] in vowels:
            line[left], line[right] = line[right], line[left]
            left += 1
            right -= 1
        if line[left] not in vowels:
            left += 1
        if line[right] not in vowels:
            right -= 1

    return ''.join(line)
