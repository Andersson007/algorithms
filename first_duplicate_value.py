#!/usr/bin/python3
# First Duplicate Value.
# Find and returns the first element in the input array
# of integers from 1 to n inclusive where n is
# is a length of the array that appear more than once
# when the array is read from left to right.
# * If no ints appear more than once, return -1
# * You're allowed to mutate the input array.

array1 = [2, 1, 2, 1, 2, 2, 3, 4, 2]  # Returns 2
array2 = [1, 2, 3]  # No duplicate values, returns -1
# Since the ints are between 1 and the length of the array,
# you can map them to indices in the array itself by
# by subtracting 1 from them.
# Once you've mapped an int to an index in the array,
# you can mutate the value in the array at that index
# and make it negative by multiplying it by -1.
# Since integers  normally aren't negative, the first time
# that you encounter a negative value at the index that
# an integer maps to, you'll know that
# you'll have already seen that integer.

# Time O(N)
# Space O(1)
def first_duplicate_value(array):
    for val in array:
        abs_val = abs(val)
        mapped_idx = abs_val - 1
        if array[mapped_idx] < 0:
            return abs_val

        array[mapped_idx] *= -1

    return -1


print(first_duplicate_value(array1))
print(first_duplicate_value(array2))
