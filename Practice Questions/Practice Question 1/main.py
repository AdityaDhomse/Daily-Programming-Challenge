# You are given an unsorted array of integers and a positive integer K.
# Your task is to find the Kth largest element in the array.
# The Kth largest element is the element that would appear in the Kth position
# if the array were sorted in descending order.

# You need to implement a function that returns this Kth largest element
# without explicitly sorting the entire array.

# Example
# arr = [3, 2, 1, 5, 6, 4]
# k = 2
# Output: 5


def sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


array = [45, 67, 12, 64, 23, 89, 20]
k = 5


# Applied Bubble Sort
sorted_array = sort(array)

print(f"{k}th largest no. is {sorted_array[len(sorted_array) - k]}")
