def find_missing_number(arr):
    n = len(arr) + 1
    sum = n * (n + 1) // 2

    arr_sum = 0
    for i in range(len(arr)):
        arr_sum += arr[i]

    return sum - arr_sum


arr = [1, 2, 3, 4, 5, 7, 8, 9, 10]

missing_number = find_missing_number(arr)
print(f"Missing Number is: {missing_number}")
