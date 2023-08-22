def longest_substring_with_k_distinct_chars(line: str, target: int) -> int:
    start: int = 0
    max_length: int = 0
    char_frequency = dict()

    for end in range(len(line)):
        right_char: str = line[end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        while len(char_frequency) > target:
            left_char: str = line[start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            start += 1
        max_length = max(max_length, end - start + 1)
    return max_length


def test() -> None:
    assert longest_substring_with_k_distinct_chars('araaci', 2) == 4
    assert longest_substring_with_k_distinct_chars('araaci', 1) == 2
    assert longest_substring_with_k_distinct_chars('cbbebi', 3) == 5


def main() -> None:
    test()


main()
