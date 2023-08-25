def bubble_sort(array: list, size: int):
    count = 0
    flag = False
    for i in range(size):
        for j in range(size - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                count += 1
                flag = True
        if count > 0:
            print(*array)
            count = 0
    if not flag:
        print(*array)


if __name__ == "__main__":
    length = int(input())
    numbers = [int(i) for i in input().split()]
    bubble_sort(numbers, length)
