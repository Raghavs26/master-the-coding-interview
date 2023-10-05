from typing import List


# 1 7 5 3 9
def containerWithMostWater(height: List[int]):
    res = float("-inf")

    for p1 in range(0, len(height) - 1):
        for p2 in range(p1 + 1, len(height)):
            width = p2 - p1
            min_height = min(height[p1], height[p2])
            area = min_height * width
            res = max(res, area)

    return res
