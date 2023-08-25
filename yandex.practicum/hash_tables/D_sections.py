size = int(input())
result = []
for i in range(size):
    section = input()
    if section not in result:
        result.append(section)
        print(section)
