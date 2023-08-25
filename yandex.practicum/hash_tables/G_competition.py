def find_longest_tie_sequence(matches):
    if len(matches) == 0:
        return 0
    count = -1 if matches[0] == 0 else 1
    len_count = 0
    longest = 0
    for i in range(1, len(matches)):
        for j in range(i, len(matches)):
            if matches[j] == 0:
                count -=1
            else:
                count += 1
            len_count += 1
        len_count += 1
        if count == 0:
            if longest < len_count:
                longest = len_count
        len_count = 0
        count = -1 if matches[i] == 0 else 1
    return longest


amount = int(input())
matches = [int(i) for i in input().split()]
result = max(find_longest_tie_sequence(matches),
             find_longest_tie_sequence(matches[::-1]))
print(result)
