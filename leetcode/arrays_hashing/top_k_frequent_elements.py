# https://leetcode.com/problems/top-k-frequent-elements/
def top_k_frequent(nums: list, k: int) -> list:
    # Bucket Sort
        count: list = [[] for _ in range(len(nums) + 1)]
        count_digits = dict()
        result = list()

        for i in range(len(nums)):
            if nums[i] not in count_digits:
                count_digits[nums[i]] = 0
            count_digits[nums[i]] += 1

        for key, value in count_digits.items():
            count[value].append(key)


        for i in range(len(count) - 1, -1, -1):
            if count[i] and len(result) < k:
                result.extend(count[i])

        return result


if __name__ == '__main__':
    print(top_k_frequent(nums=[1, 1, 1, 2, 2, 3, 4, 4, 4], k=2))
    print(top_k_frequent(nums=[1], k=1))
