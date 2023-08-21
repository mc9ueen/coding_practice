import math
import typing


def smallest_subarray_with_given_sum(target: int, arr: list):
    window_sum: int = 0
    window_start: int = 0
    min_length: int = 1024 * 1024 * 1024 * 4
    tmp = list()
    result = list()

    for window_end in range(0, len(arr)):
        window_sum += arr[window_end]
        tmp.append(arr[window_end])
        while window_sum >= target:
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                result = tmp[window_start:]
            window_sum -= arr[window_start]
            window_start += 1
    return min_length, result


def main() -> None:
    print(f'Smallest subarray (length, sequence): '
          f'{smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])}')
    print(f'Smallest subarray (length, sequence): '
          f'{smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])}')
    print(f'Smallest subarray (length, sequence): '
          f'{smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])}')


main()
