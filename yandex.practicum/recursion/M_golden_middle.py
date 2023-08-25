if __name__ == "__main__":
    n = int(input())
    m = int(input())
    north = [int(i) for i in input().split()]
    south = [int(i) for i in input().split()]
    whole = sorted(north + south)
    if len(whole) % 2 == 0:
        median = (whole[len(whole) // 2] + whole[len(whole) // 2 - 1]) / 2
        print(int(median) if median % 1 == 0 else median)
    else:
        print(whole[len(whole) // 2])
