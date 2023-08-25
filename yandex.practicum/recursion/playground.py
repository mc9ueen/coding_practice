def binary_search_lowest(nums: list, size: int) -> int:
    """Find index of the lowest value in sequence"""
    low = 0
    high = size - 1
    while low <= high:
        if low == high:
            return high
        mid = (low + high) // 2
        if low == mid < high:
            return low if nums[low] < nums[high] else high
        if (nums[low] < nums[mid] < nums[high]
                or nums[low] > nums[mid] < nums[high]):
            if mid - low == 1:
                return low
            if nums[mid - 1] > nums[mid] < nums[mid + 1]:
                return mid
            high = mid - 1
            continue
        if nums[low] < nums[mid] > nums[high]:
            low = mid + 1
    return -1


def broken_search(nums: list, target: int) -> int:
    """Find index of given target in rotated sorted array"""
    border = binary_search_lowest(nums, len(nums))

    def enclosing_binary_search(left: int, right: int) -> int or None:
        """Nested recursive binary search using enclosing variables"""
        if left >= right:
            return None
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        if nums[middle] < target:
            return enclosing_binary_search(middle + 1, right)
        else:
            return enclosing_binary_search(left, middle)

    left_half = enclosing_binary_search(0, border - 1)
    right_half = enclosing_binary_search(border, len(nums))

    return (0 if left_half == 0 or right_half == 0
            else left_half or right_half or -1)