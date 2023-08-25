# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
def remove_duplicates(nums: list) -> int:
    left: int = 1
    right: int = 1

    while right < len(nums):
        if nums[right - 1] != nums[right]:
            nums[left] = nums[right]
            left += 1
        right += 1

    return left
