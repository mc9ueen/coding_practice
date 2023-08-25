def top_k_frequent_words(words: list, k: int) -> list:
    freq: list = [[] for _ in range(len(words) + 1)]
    count_words = dict()
    result = list()

    for i in range(len(words)):
        if words[i] not in count_words:
            count_words[words[i]] = 0
        count_words[words[i]] += 1

    for key, value in count_words.items():
        freq[value].append(key)

    for i in range(len(freq) - 1, -1, -1):
        if freq[i] and len(result) < k:
            result.extend(sorted(freq[i]))

    return result[:k]


if __name__ == '__main__':
    print(top_k_frequent_words(words=["i", "love", "leetcode", "i", "love", "coding"], k=2))
    print(top_k_frequent_words(words=["the","day","is","sunny","the","the","the","sunny","is","is"], k=4))
    print(top_k_frequent_words(words=["i","love","leetcode","i","love","coding"], k=1))
    print(top_k_frequent_words(words=["i","love","leetcode","i","love","coding"], k=3))
