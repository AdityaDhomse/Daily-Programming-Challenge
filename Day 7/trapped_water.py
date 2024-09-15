def trapped_rain_water(height):
    if not height:
        return 0

    n = len(height)
    l_max = [0] * n
    r_max = [0] * n
    trapped_water = 0

    l_max[0] = height[0]
    for i in range(1, n):
        l_max[i] = max(l_max[i - 1], height[i])

    r_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        r_max[i] = max(r_max[i + 1], height[i])

    for i in range(1, n - 1):
        trapped_water += min(l_max[i], r_max[i]) - height[i]

    return trapped_water


height = [2, 0, 2]
print("\nWater trapped:", trapped_rain_water(height))
