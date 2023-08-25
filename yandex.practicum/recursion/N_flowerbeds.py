def combine_points(array: list, size: int) -> tuple:
    intersections = []
    outsiders = []
    if size == 1:
        intersections.append((array[0][0], array[0][1]))
    for i in range(size - 1):
        is_superset = array[i][0] <= array[i + 1][0] and array[i][1] >= array[i + 1][1]
        is_subset = array[i][0] < array[i + 1][0] <= array[i][1] <= array[i + 1][1]
        if is_superset:
            array[i + 1] = array[i]
            if intersections:
                if array[i][0] in intersections[-1]:
                    intersections.clear()
            intersections.append(tuple(array[i]))
            continue
        if is_subset:
            array[i] = [array[i][0], array[i][1]]
            array[i + 1][0] = array[i][0]
            if intersections:
                if array[i][0] in intersections[-1]:
                    intersections.clear()
            intersections.append(tuple(array[i + 1]))
            continue
        if array[i][1] < array[i + 1][0]:
            outsiders.append(tuple(array[i]))
            if i + 1 == len(array) - 1:
                outsiders.append(tuple(array[i + 1]))
    del array
    intersections = outsiders + intersections
    return tuple(sorted(frozenset(intersections)))


if __name__ == "__main__":
    flowerbeds = []
    size = int(input())
    for i in range(size):
        flowerbeds.append([int(i) for i in input().split()])
    flowerbeds.sort(key=lambda item: item[0])
    for i in combine_points(flowerbeds, size):
        if i[1] != 0:
            print(*i)
