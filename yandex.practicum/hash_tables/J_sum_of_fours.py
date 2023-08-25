def find_all_fours(arr: list, target: int, size: int):
    arr = sorted(arr)
    result = []
    for first in range(size - 3):
        for second in range(size - 2):
            third = second + 1
            last = size - 1

            while third < last:
                curr_sum = arr[first] + arr[second] + arr[third] + arr[last]
                if curr_sum == target:
                    sum_sequence = (arr[first], arr[second],
                                    arr[third], arr[last])
                    if sum_sequence not in result:
                        result.append(sum_sequence)
                    third += 1
                    last -= 1
                elif curr_sum < target:
                    third += 1
                else:
                    last -= 1

    return result


if __name__ == "__main__":
    amount = int(input())
    number = int(input())
    nums = [int(i) for i in input().split()]
    nums = find_all_fours(nums, number, amount)
    print(len(nums))
    for seq in nums:
        print(*seq)
