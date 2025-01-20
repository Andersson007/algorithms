#!/usr/bin/python
# Two Number Sum.
# A function takes a non-empty array of distinct ints
# and an int representing a target sum.
# If there are two numbers that sum up to the target sum,
# the function should return them in a new array in any order,
# otherwise it returns an empty array.

arr = [2, 3, 5, 10, 4, 8, 9]


def two_num_sum_hash_table(array, target_sum):
    # Time complexity: O(N) as we need
    # to just traverse the array
    # Space complexity: O(N) as we use a hash table
    hash_table = set()

    for x in array:
        y = target_sum - x
        if y not in hash_table:
            hash_table.add(x)
        else:
            return [x, y]

    return []


def two_num_sum_sorted_array(array, target_sum):
    # Time: O(n log n) because it's
    # the probable complexity of array sorting
    # Space: O(1) because we sort the array in place
    array.sort()
    i = 0               # Left pointer init position
    j = len(array) - 1  # Right pointer init position
    while i < j:
        curr_sum = array[i] + array[j]
        if curr_sum == target_sum:
            return [array[i], array[j]]
        elif curr_sum > target_sum:
            j -= 1
        elif curr_sum < target_sum:
            i += 1

    return []
