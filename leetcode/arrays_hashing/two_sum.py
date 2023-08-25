def two_sum(nums: list, target: int) -> list:
    hash_map = dict()
    for i in range(len(nums)):
        tmp: int = target - nums[i]
        if nums[i] in hash_map:
            return [hash_map[nums[i]], i]
        else:
            hash_map[tmp] = i
    return []


def main():
    print(two_sum([2,7,11,15], 9))


main()
