# 0 1 0 2 1 0 3 1 0 1 2
#
#     #       #
#   # #   # #   # #
# # # # # # # # # # # #


def trappingRainwater(arr: list[int]):
    total_water = 0
    n = len(arr)
    for i in range(n):
        p1, p2 = i, i
        max_left, max_right = 0, 0
        while p1 >= 0:
            max_left = max(max_left, arr[p1])
            p1 = p1 - 1
        while p2 < n:
            max_right = max(max_right, arr[p2])
            p2 = p2 + 1
        current_water = min(max_left, max_right) - arr[i]
        if current_water > 0:
            total_water = total_water + current_water
    return total_water


print(trappingRainwater([0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]))
