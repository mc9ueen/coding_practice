# https://leetcode.com/problems/move-zeroes/
def move_zeroes(nums: list) -> None:
    left: int = 0
    edge: int = len(nums) - 1

    while left <= edge:
        if nums[left - 1] == 0 and left - 1 >= 0:
            left -= 1
        if nums[left] == 0 and left + 1 < len(nums):
            nums[left], nums[left + 1] = nums[left + 1], nums[left]
            for i in range(left + 1, edge):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
            edge -= 1
        left += 1
