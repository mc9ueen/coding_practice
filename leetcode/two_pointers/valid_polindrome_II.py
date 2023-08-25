# https://leetcode.com/problems/valid-palindrome-ii/
def valid_palindrome(s: str) -> bool:
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
            left_variation_of_s = s[:left] + s[left + 1:]
            right_variation_of_s = s[:right] + s[right + 1:]
            return (left_variation_of_s == left_variation_of_s[::-1] or
                    right_variation_of_s == right_variation_of_s[::-1])
        left += 1
        right -= 1
    return s == s[::-1]

