def find_subarrays(arr):
    subarrays = []
    prefix_sum = 0

    sum_map = {}

    for i in range(len(arr)):
        prefix_sum += arr[i]

        if prefix_sum == 0:
            subarrays.append((0, i))

        if prefix_sum in sum_map:
            for start_index in sum_map[prefix_sum]:
                subarrays.append((start_index + 1, i))

        if prefix_sum not in sum_map:
            sum_map[prefix_sum] = []
        sum_map[prefix_sum].append(i)

    return subarrays


arr = [1, 2, -3, 3, -1, 2]
result = find_subarrays(arr)
print(result)
