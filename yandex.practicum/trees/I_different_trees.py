def amount_of_all_search_trees(n: int):
    t = [1, 1, 2] + [0] * (n - 2)
    for i in range(3, n + 1):
        tmp = []
        for j in range(i + 1):
            tmp.append(t[j] * t[i - j - 1])
        t[i] = sum(tmp)
    return t[n]


def main():
    n = int(input())
    print(amount_of_all_search_trees(n))


if __name__ == "__main__":
    main()
