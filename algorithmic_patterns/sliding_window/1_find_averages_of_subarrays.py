def find_averages_of_subarrays(size: int, arr: list) -> list:
    result = list()
    window_start: int = 0
    window_sum: float = 0.0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= size - 1:
            result.append(window_sum / size)
            window_sum -= arr[window_start]
            window_start += 1
    return result


def main() -> None:
    result: list = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print(f'Average of subarrays of given size ({5}) is {result}')


main()
