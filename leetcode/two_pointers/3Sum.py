def three_sum(nums: list) -> list:
        nums.sort()
        print(nums)
        i: int = 0
        j: int = i + 1
        possibilities = set()
        while i < len(nums):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    possibilities.add((nums[i], nums[j], nums[k]))
                j += 1
                k -= 1
            j = i + 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    possibilities.add((nums[i], nums[j], nums[k]))
                j += 1
            i += 1
        return list(map(list, possibilities))


print(three_sum([3,0,-2,-1,1,2]))
