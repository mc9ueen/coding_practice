def pair_with_targetsum(arr: list, targetsum: int) -> list:
    left: int = 0
    right: int = len(arr) - 1

    while left < right:
        if arr[left] + arr[right] == targetsum:
            return [left, right]
        if arr[left] + arr[right] > targetsum:
            right -= 1
        if arr[left] + arr[right] < targetsum:
            left += 1

    return [-1, -1]


print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
print(pair_with_targetsum([2, 5, 9, 11], 11))
