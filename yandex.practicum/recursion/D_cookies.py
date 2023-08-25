def quick_sort(arr: list):
    if len(arr) < 2:
        return arr
    pivot = arr[-1]
    left = [i for i in arr if i < pivot]
    mid = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]
    return quick_sort(left) + mid + quick_sort(right)


def get_satisfied_children(kids: list, kids_amount: int,
                           cookies: list, cookies_amount: int) -> int:
    count = 0
    kids = quick_sort(kids)
    cookies = quick_sort(cookies)
    for kid in range(kids_amount - 1, -1, -1):
        if cookies and kids[kid] <= cookies[-1]:
            count += 1
            cookies.pop()
    return count


if __name__ == "__main__":
    amount_of_children = int(input())
    greed_factors = [int(i) for i in input().split()]
    amount_of_cookies = int(input())
    cookies_sizes = [int(i) for i in input().split()]
    print(get_satisfied_children(greed_factors, amount_of_children,
                                 cookies_sizes, amount_of_cookies))
