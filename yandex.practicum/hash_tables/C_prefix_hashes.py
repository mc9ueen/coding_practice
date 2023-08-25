def hash_function(string: str, a: int, m: int):
    string = string[::-1]
    acc = ord(string[0]) if len(string) > 1 else ord(string[0]) % m
    size = a
    for i in range(1, len(string)):
        acc += ord(string[i]) * size
        acc %= m
        size *= a
        size %= m
    return acc


if __name__ == "__main__":
    a = int(input())
    m = int(input())
    string = input()
    amount = int(input())
    for i in range(amount):
        l, r = input().split()
        print(hash_function(string[int(l[0]) - 1: int(r[1])], a, m))
