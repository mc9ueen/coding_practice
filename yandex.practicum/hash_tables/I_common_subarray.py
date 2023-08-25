def find_longest_common_subarray(arr, subarr, len_arr, len_subarr):
    f = [[0] * (len_subarr + 1) for _ in range(len_arr + 1)]
    for i in range(1, len_arr + 1):
        for j in range(1, len_subarr + 1):
            if arr[i - 1] == subarr[j - 1]:
                f[i][j] = 1 + f[i - 1][j - 1]
                print(arr[i-1], subarr[j - 1])
            else:
                f[i][j] = max(f[i - 1][j], f[i][j - 1])
    print(f, sep="\n")
    return f[-1][-1]


if __name__ == "__main__":
    n = int(input())
    n_arr = [int(i) for i in input().split()]
    m = int(input())
    m_arr = [int(i) for i in input().split()]
    print(find_longest_common_subarray(n_arr, m_arr, n, m))
