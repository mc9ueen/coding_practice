# https://leetcode.com/problems/valid-palindrome/
def is_palindrome(s: str) -> bool:
    from string import punctuation
    elements_to_replace = set(f'{punctuation} ')
    s: str = s.lower()

    for c in s:
        if c in elements_to_replace:
            s = s.replace(c, '')

    left: int = 0
    right: int = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
