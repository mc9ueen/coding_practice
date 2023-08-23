# https://leetcode.com/problems/is-subsequence/
def is_subsequence(s: str, t: str):
    s_index: int = 0
    t_index: int = 0
    while s_index < len(s) and t_index < len(t):
        if s[s_index] == t[t_index]:
            s_index += 1
        t_index += 1
    return s_index == len(s)
