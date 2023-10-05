from typing import List


def twoSum(nums: List[int], target: int):
    n = len(nums)
    for p1 in range(0, n - 1):
        for p2 in range(p1 + 1, n):
            if nums[p1] + nums[p2] == target:
                return [p1, p2]
    return [-1, -1]


print(twoSum([2, 7, 11, 15], 18))
