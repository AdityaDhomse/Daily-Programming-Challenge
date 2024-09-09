"""
Problem: Sort an Array of 0s, 1s, and 2s
You are given an array arr consisting only of 0s, 1s, and 2s. The task is to sort the array in increasing order in linear time (i.e., O(n)) without using any extra space. This means you need to rearrange the array in-place.

Input :
An integer array arr of size n where each element is either 0, 1, or 2.
Example : arr = [0, 1, 2, 1, 0, 2, 1, 0]

Output :
The sorted array, arranged in increasing order of 0s, 1s, and 2s.
Example: [0, 0, 0, 1, 1, 1, 2, 2]
"""


def sort_0_1_2(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


arr = [0, 1, 2, 1, 0, 2, 1, 1, 1, 0, 2, 1, 0]
print(f"\nOriginal Array: {arr}")
sort_0_1_2(arr)
print(f"\nSorted array: {arr}")

# Test Cases
# 1. [0, 1, 2, 1, 0, 2, 1, 0]
# 2. [2, 2, 2, 2]
# 3. [0, 0, 0, 0]
# 4. [1, 1, 1, 1]
# 5. [2, 0, 1]
# 6. []
