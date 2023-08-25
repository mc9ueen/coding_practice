def get_amount_of_unis(unis: list, length: int, amount: int):
    unis_amounts = dict()
    result = []
    for i in range(length):
        if unis_amounts.get(unis[i]):
            unis_amounts[unis[i]] = unis_amounts[unis[i]] + 1
        else:
            unis_amounts[unis[i]] = 1
    unis_amounts = {k: v for k, v in sorted(unis_amounts.items(), key=lambda x: x[1], reverse=True)}
    return tuple(unis_amounts.keys())[:amount]


if __name__ == "__main__":
    amount_of_students = int(input())
    uni_IDs = [int(i) for i in input().split()]
    result_size = int(input())
    print(*get_amount_of_unis(uni_IDs, amount_of_students, result_size))