#!/usr/bin/python3
# Smallest Difference.
# * The function takes two non-empty arrays of integers.
# * It finds and returns a pair of numbers
#   one from each array whose abs difference is closest to 0.
# * The first number in the ouptup array is from the first array.
# * Abs diff of -5 and 5 is 10 and abs diff of -5 and -4 is 1.
#   In other words, it's a distance between two integers.

# Solution:
# 1. Sort the arrays
# 2. Use two pointers one for each array
# 3. Iterate until one of them reaches the end
#    of one of the arrays. Each iteration check:
#  * If both the numbers are equal, return them
#    because it's our solution (0)
#  * If x(fist_ptr) < y(sec_ptr), do y - x
#  * If x > y, do x - y
#  * Update the potential smallest diff each time
#    if it's greater than the current one.

array1 = [-1, 3, 5, 10, 22, 28]
array2 = [15, 17, 26, 134, 135]
# Outpust will be [28, 26]

# Time O(N log N + M log M) as we sort both the input arrays
# Space O(1)
def smallest_diff(array1, array2):
    array1.sort()
    array2.sort()

    idx1 = 0
    idx2 = 0

    # Assing them with positive infinity.
    # It practically means that such a number
    # is greater than any finite number
    smallest_diff = float("inf")
    current_diff = float("inf")
    smallest_pair = []

    while idx1 < len(array1) and idx2 < len(array2):
        num1 = array1[idx1]
        num2 = array2[idx2]
        if num1 < num2:
            current_diff = num2 - num1
            idx1 += 1
        elif num1 > num2:
            current_diff = num1 - num2
            idx2 += 1
        else:
            return [num1, num2]

        if smallest_diff > current_diff:
            smallest_diff = current_diff
            smallest_pair = [num1, num2]

    return smallest_pair


print(smallest_diff(array1, array2))


# Mine solutions
# Time (N log N + M log M)
# Space O(1)
def smallest_diff_mine(arr1, arr2):
    arr1.sort()
    arr2.sort()

    smallest = float("inf")
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        diff = abs(arr1[i] - arr2[j])
        smallest = min(diff, smallest)

        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return smallest


# Time (N log N + M log M)
# Space O(1)
def smallest_diff_pair(arr1, arr2):
    arr1.sort()
    arr2.sort()

    pair = (None, None)
    smallest = float("inf")
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        diff = abs(arr1[i] - arr2[j])
        if diff < smallest:
            smallest = diff
            pair = (arr1[i], arr2[j])

        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return pair


print(smallest_diff_mine([1, 3, 15, 11, 2], [23, 127, 235, 19, 8]))
print(smallest_diff_pair([1, 3, 15, 11, 2], [23, 127, 235, 19, 8]))
