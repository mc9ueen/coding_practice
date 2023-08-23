# https://leetcode.com/problems/reverse-string-ii/
def reverse_str(s: str, k: int) -> str:
    if len(s) < k:
        return s[::-1]

    line = list(s)
    first: int = 0
    second: int = k

    while second <= len(line):
        line[first:second] = line[first:second][::-1]
        first += 2 * k
        second += 2 * k
        if second > len(line):
            line[first:] = line[first:][::-1]

    return ''.join(line)
