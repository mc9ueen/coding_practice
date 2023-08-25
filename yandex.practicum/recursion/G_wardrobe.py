def sort_wardrobe(colors: list):
    left = []
    middle = []
    right = []
    for color in colors:
        if color == "0":
            left.append(color)
        elif color == "1":
            middle.append(color)
        elif color == "2":
            right.append(color)
        else:
            print("Color doesn't fit the wardrobe")
            continue
    return left + middle + right


if __name__ == "__main__":
    n = int(input())
    arr = [i for i in input().split()]
    print(*sort_wardrobe(arr))
