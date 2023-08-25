from collections import deque


def isValid(s: str) -> bool:
    valid_consequence = {')': '(',
                         '}': '{',
                         ']': '['}
    sequence = deque()
    for i in range(len(s)):
        if len(sequence) != 0 and s[i] in valid_consequence.keys():
            if sequence.pop() != valid_consequence[s[i]]:
                return False
        else:
            sequence.append(s[i])
    return True if len(sequence) == 0 else False

print(isValid("()}"))
