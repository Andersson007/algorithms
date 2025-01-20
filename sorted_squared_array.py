#!/usr/bin/python
# Sorted squared array.
# A function takes a non-empty array of integers
# sorted in ascending order and returns a new array
# with the squares of the original integers also sorted
# in ascending order. The integers can be negative!

array = [-6, 3, 4, 5, 8, 9, 10]


def sorted_squared_array1(array):
    # Not optimal but simple and works with unsorted arrays
    # 1. Generate a new array not caring about the order
    # 2. Sort it in place and return
    # Time: O(n log n) as it's the sorting complexity
    # Space: O(n) as we create another array
    # of the same length
    return sorted([x ** 2 for x in array])


def sorted_squared_array2(array):
    # Works only with sorted arrays.
    # Time: O(n)
    # Space: O(n)
    out_array = [0] * len(array)

    # We need to compare absolute values:
    # the largest goes to the end
    start = 0
    end = len(array) - 1
    i = len(array) - 1

    # Iterate until the pointers meet
    while start <= end:
        if abs(array[start]) > abs(array[end]):
            out_array[i] = array[start] ** 2
            start += 1
        else:
            out_array[i] = array[end] ** 2
            end -= 1

        i -= 1

    return out_array
