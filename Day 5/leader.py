def find_leaders(array):
    n = len(array)
    leaders = []
    right_element = array[-1]
    leaders.append(right_element)

    for i in range(n - 2, -1, -1):
        if array[i] > right_element:
            right_element = array[i]
            leaders.append(right_element)

    leaders.reverse()
    return leaders


print(find_leaders([16, 17, 4, 3, 5, 2]))
