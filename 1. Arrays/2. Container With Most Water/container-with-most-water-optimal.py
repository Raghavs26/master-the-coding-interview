from typing import List


# 1 7 5 3 9
def containerWithMostWater(height: List[int]):
    p1, p2 = 0, len(height) - 1
    res = float("-inf")
    while p1 < p2:
        current_capacity = min(height[p1], height[p2]) * (p2 - p1)
        res = max(res, current_capacity)
        if height[p1] < height[p2]:
            p1 = p1 + 1
        else:
            p2 = p2 + 1
    return res
