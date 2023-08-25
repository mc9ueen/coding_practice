def get_possible_amount_of_houses(budget: int, prices: list):
    prices = sorted(prices)
    count = 0
    budget = budget
    for i in prices:
        budget -= i
        if budget < 0:
            break
        count += 1
    return count


if __name__ == "__main__":
    amount, budget = tuple(map(int, input().split()))
    prices = [int(i) for i in input().split()]
    print(get_possible_amount_of_houses(budget, prices))
