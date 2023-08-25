def compare(value_1: str, value_2: str):
    if len(value_1) == len(value_2):
        return value_1 > value_2
    return value_1 + value_2 > value_2 + value_1


def bubble_sort(array: list, size: int, key=None):
    key = key or (lambda a, b: a > b)
    for i in range(size):
        for j in range(size - i - 1):
            if key:
                if key(array[j], array[j + 1]):
                    array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == "__main__":
    size = int(input())
    sequence = input().split()
    print(*bubble_sort(sequence, size, compare)[::-1], sep="")
