def len_of_subsequence(string: str, substring: str):
    result = [[0] * (len(substring) + 1) for _ in range(len(string) + 1)]
    for i in range(1, len(string) + 1):
        for j in range(1, len(substring) + 1):
            if string[i - 1] == substring[j - 1]:
                result[i][j] = 1 + result[i - 1][j - 1]
            else:
                result[i][j] = max(result[i-1][j], result[i][j-1])
    return result[-1][-1]


if __name__ == "__main__":
    string = input()
    subsequence = set()
    results = []
    for i in range(len(string)):
        for j in range(i, len(string) + 1):
            if string[i:j] in string and len(set(string[i:j])) == len(string[i:j]):
                subsequence.add(string[i:j])
    subsequence = [i for i in subsequence if len(i) == len(max(subsequence, key=len))]
    for seq in subsequence:
        results.append(len_of_subsequence(string, seq))
    print(max(results) if results else 0)
