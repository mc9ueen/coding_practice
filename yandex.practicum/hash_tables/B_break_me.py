from random import randrange

a = 1000
m = 123987123
word_length = 1000


def hash_func(string: str, a: int, m: int):
    if not string:
        return 0
    string = string[::-1]
    acc = ord(string[0])
    size = a
    for i in range(1, len(string)):
        acc += size * ord(string[i])
        acc %= m
        size *= a
        size %= m
    return acc


if __name__ == "__main__":
    hashes = {}
    while True:
        word = "".join([chr(randrange(97, 123))
                        for _ in range(randrange(1, word_length))])
        hash_value = hash_func(word, a, m)
        if hashes.get(hash_value) == word:
            continue
        if not hashes.get(hash_value):
            hashes[hash_value] = word
        else:
            print(hashes[hash_value])
            print(word)
            break
