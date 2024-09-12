def merge_sorted_arrays(arr1, arr2):
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
            j += 1
        i += 1
    arr2.sort()


arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

arr3 = merge_sorted_arrays(arr1, arr2)

print("arr1: ", arr1)
print("arr2: ", arr2)
print("Merged array: ", arr3)
