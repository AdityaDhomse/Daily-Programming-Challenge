"""
 You are given an array arr containing n-1 distinct integers. The array consists of integers
 taken from the range 1 to n, meaning one integer is missing from this sequence. Your
 task is to find the missing integer.
 
 Input:
 An integer array arr of size n-1 where the elements are distinct and taken from the
 range 1 to n.
 Example : arr = [1, 2, 4, 5]
 
 Output:
 Return the missing integer from the array.
 Example: Missing number: 3
"""

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
