def hash_func(string: str, a: int, m: int):
    if not string:
        return 0
    string = string[::-1]
    acc = ord(string[0])
    size = a
    for i in range(1, len(string)):
        acc += size * ord(string[i])
        acc %= m
        size = size * a % m
    return acc


if __name__ == "__main__":
    a = int(input())
    m = int(input())
    word = input()
    print(hash_func(word, a, m))
