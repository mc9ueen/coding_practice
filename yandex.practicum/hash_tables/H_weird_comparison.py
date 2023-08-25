def hash_func(word: str) -> int:
    count_letters = dict()
    for w in word:
        if not count_letters.get(w):
            count_letters[w] = 1
        else:
            count_letters[w] = count_letters[w] + 1
    result = 0
    for i in range(len(word)):
        result += (i + 1) * count_letters[word[i]]
    return result


if __name__ == "__main__":
    a, b = input(), input()
    print("YES") if hash_func(a) == hash_func(b) else print("NO")
