# You are given an unsorted array of integers.
# Your task is to find the median of the array.
# The median is the middle value in an ordered list of numbers.
# If the list has an even number of elements, the median is the average of the two middle numbers.

# Implement a function that returns the median of the array without explicitly sorting the entire array.


def find_median(arr):
    n = len(arr)
    arr.sort()

    if n == 0:
        return None
    # If array is odd
    elif n % 2 == 1:
        mid_index = n // 2
        return arr[mid_index]
    # If array is even
    else:
        mid_index1 = n // 2 - 1
        mid_index2 = n // 2
        return (arr[mid_index1] + arr[mid_index2]) / 2


arr = [3, 2, 1, 5, 4, 6]
median = find_median(arr)
print(median)
