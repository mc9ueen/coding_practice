def fruits_into_baskets(fruits: list) -> int:
    start: int = 0
    fruit_frequency = dict()
    max_length: int = 0

    for end in range(len(fruits)):
        right_fruit = fruits[end]
        if right_fruit not in fruit_frequency:
            fruit_frequency[right_fruit] = 0
        fruit_frequency[right_fruit] += 1

        while len(fruit_frequency) > 2:
            left_fruit = fruits[start]
            fruit_frequency[left_fruit] -= 1
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length


def test() -> None:
    first_call = fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])
    assert first_call == 3, f'Method result {first_call} does not equal 3'
    second_call = fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])
    assert second_call == 5, f'Method result {second_call} does not equal 5'


test()
