def trappingRainwater(height: list[int]):
    total_water, n = 0, len(height)
    left, right = 0, n - 1
    maxLeft, maxRight = 0, 0

    while left < right:
        if height[left] <= height[right]:
            if height[left] >= maxLeft:
                maxLeft = height[left]
            else:
                totalWater += maxLeft - height[left]
            left += 1
        else:
            if height[right] >= maxRight:
                maxRight = height[right]
            else:
                totalWater += maxRight - height[right]
            right -= 1

    return total_water
