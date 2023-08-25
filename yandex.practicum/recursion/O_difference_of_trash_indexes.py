def find_trash_index(areas: tuple, amount: int, target: int) -> int:
    trash_indexes = []
    for i in range(amount):
        for j in range(i + 1, amount):
            trash_indexes.append(abs(areas[i] - areas[j]))
    trash_indexes.sort()
    print(trash_indexes)
    return trash_indexes[target - 1]


if __name__ == "__main__":
    n = int(input())
    islands = tuple(sorted(int(i) for i in input().split()))
    k = int(input())
    print(find_trash_index(islands, n, k))
