from typing import List


def twoSum(nums: List[int], target: int):
    n = len(nums)
    mp = {}
    for i in range(0, n):
        number_to_find = target - nums[i]
        if number_to_find in mp:
            return [mp[number_to_find], i]
        else:
            mp[nums[i]] = i
    return [-1, -1]


print(twoSum([2, 7, 11, 15], 18))
