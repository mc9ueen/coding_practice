def find_available_day_to_buy_bicycle(array: list, item: int,
                                      left: int, right: int) -> int:
    """Custom binary search to find the earliest possible day to buy bicycle.
       Value in sequence can be equal or more than searched item.
    """
    if left >= right:
        return -1
    mid = (left + right) // 2
    if array[mid] >= item and (mid == 0 or array[mid - 1] < item):
        return mid + 1
    if array[mid] < item:
        return find_available_day_to_buy_bicycle(array, item, mid + 1, right)
    else:
        return find_available_day_to_buy_bicycle(array, item, left, mid)


if __name__ == "__main__":
    amount_of_days = int(input())
    days = [int(i) for i in input().split()]
    price = int(input())
    day_one = find_available_day_to_buy_bicycle(days, price, 0, amount_of_days)
    day_two = find_available_day_to_buy_bicycle(days, price * 2,
                                                0, amount_of_days)
    print(day_one, day_two)
