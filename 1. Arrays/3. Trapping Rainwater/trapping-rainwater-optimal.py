def trappingRainwater(height: list[int]):
    total_water, n = 0, len(height)
    left, right = 0, n - 1
    max_left, max_right = 0, 0

    while left < right:
        if height[left] <= height[right]:
            if height[left] >= max_left:
                max_left = height[left]
            else:
                totalWater += max_left - height[left]
            left += 1
        else:
            if height[right] >= max_right:
                max_right = height[right]
            else:
                totalWater += max_right - height[right]
            right -= 1

    return total_water
