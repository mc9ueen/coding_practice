def merge(arr: list, lf: int, mid: int, rg: int) -> list:
    left = arr[lf:mid]
    right = arr[mid:rg]
    l = r = k = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            arr[k] = left[l]
            l += 1
        else:
            arr[k] = right[r]
            r += 1
        k += 1
    while l < len(left):
        arr[k] = left[l]
        l += 1
        k += 1
    while r < len(right):
        arr[k] = right[r]
        r += 1
        k += 1
    return arr


def merge_sort(arr: list, lf: int, rg: int) -> None:
    if len(arr) <= 1:
        return
    temp_array = arr[lf:rg]
    middle = len(temp_array) // 2
    left = temp_array[:middle]
    right = temp_array[middle:len(temp_array)]
    merge_sort(left, 0, len(left))
    merge_sort(right, 0, len(right))
    result = merge(left + right, lf, middle, rg)
    for i in range(len(temp_array)):
        arr[i] = result[i]


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


test()
