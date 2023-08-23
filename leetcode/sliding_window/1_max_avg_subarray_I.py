def find_max_average(nums: list, k: int) -> float:
    start: int = 0
    max_average: float = -1.0 * 1024 * 1024 * 1024 * 4
    window_sum: int = 0
    for end in range(len(nums)):
        window_sum += nums[end]
        if end >= k - 1:
            max_average = max(max_average, window_sum / k)
            window_sum -= nums[start]
            start += 1
    return max_average
