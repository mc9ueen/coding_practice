# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
def two_sum_ii(numbers: list, target: int) -> list:
    left: int = 0
    right: int = len(numbers) - 1

    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        if numbers[left] + numbers[right] > target:
            right -= 1
        if numbers[left] + numbers[right] < target:
            left += 1
    return []
