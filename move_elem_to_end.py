#!/usr/bin/python3
# Move Element To End.
# The function takes an array of ints
# and an integer. It moves all instances of that
# integer in the array to the end of the array in place
# and returns the array.

array = [2, 1, 2, 2, 2, 3, 4, 2]
num = 2
# output = [1, 3, 4, 2, 2, 2, 2, 2]


def move_elem_to_end(array, num):
    left = 0
    right = len(array) - 1
    while left < right:
        if array[right] == num:
            right -= 1
            continue

        if array[left] == num:
            array[left], array[right] = array[right], array[left]
            right -= 1

        left += 1

    return array


print(move_elem_to_end(array, 2))
