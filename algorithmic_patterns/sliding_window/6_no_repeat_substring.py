def non_repeat_substring(line: str) -> int:
    start: int = 0
    max_len: int = 0
    char_index_map = dict()
    for end in range(len(line)):
        right_char: str = line[end]
        if right_char in char_index_map:
            start = max(start, char_index_map[right_char] + 1)
        char_index_map[right_char] = end
        max_len = max(max_len, end - start + 1)
    return max_len


def test() -> None:
    assert non_repeat_substring('aabccbb') == 3
    assert non_repeat_substring('abbbb') == 2
    assert non_repeat_substring('abccde') == 3


test()
