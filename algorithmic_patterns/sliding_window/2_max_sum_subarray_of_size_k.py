def max_sum_subarray_of_size_k(size: int, arr: list) -> int:
    max_sum: int = 0
    window_sum: int = 0
    window_start: int = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= size - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum


def main() -> None:
    print(f'Max sum of a subarray of size k: {max_sum_subarray_of_size_k(3, [2, 1, 5, 1, 3, 2])}')
    print(f'Max sum of a subarray of size k: {max_sum_subarray_of_size_k(2, [2, 3, 4, 1, 5])}')


main()
