#!/usr/bin/python3
# Monolithic Array
# Check if a passed array is monolithic.
# An array is monolithic if its elements, from left to right, are
# entirely non-increasing or entirely non-decreasing. Empty arrays
# and arrays with up to two elements are considered monolithic.

array1 = [2, 1, 2, 2, 2, 3, 4, 2]  # False
array2 = [1, 2, 3]  # This and the rest
array3 = [3, 2, 1]
array4 = []
array5 = [1]
array6 = [1, 2]


# Time O(N)
# Space O(1)
def monolithic_array(array):

    if len(array) <= 2:
        return True

    # Assime both directions are possible until proven otherwise
    is_non_increasing = True
    is_non_decreasing = True

    # Iterate through the array to check for violations
    for i in range(len(array) - 1):
        # Check for a dip in a potentially non-decreasing sequence
        if array[i] > array[i + 1]:
            is_non_decreasing = False

        # Check for a rise in a potentially non-increasing sequence
        if array[i] < array[i + 1]:
            is_non_increasing = False

    # The array is monolithic if it's one OR the other
    return is_non_increasing or is_non_decreasing


print(monolithic_array(array1))
print(monolithic_array(array2))
print(monolithic_array(array3))
print(monolithic_array(array4))
print(monolithic_array(array5))
print(monolithic_array(array6))
