if __name__ == "__main__":
    size = int(input())
    words = input().split()
    heap = set()
    result = []
    for i in range(size):
        tmp = []
        for j in range(i, size):
            if set(words[i]) == set(words[j]) and j not in heap:
                heap.add(j)
                tmp.append(j)
        if tmp:
            result.append(tmp)
    for i in result:
        print(*i)
