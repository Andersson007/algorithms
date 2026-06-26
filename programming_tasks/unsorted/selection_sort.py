#!/usr/bin/python
# Selection sort.
# * Devide the input array into two subarrays in place.
# * The first subarray should be sourted at all times
#   and should start with a length of 0
# * Find the smallest (or largest) element in the unsorted
#   subarray and swap with a correct element from the
#   sorted subarray.

arr = [100, 2, 3, 4, 8, 9, 10]


# O(N^2) Time as we use nested loops
# O(1) Space as we sort the array in place
def selection_sort(arr):
    curr_idx = 0  # The sorted subarray has lengh 0

    # We move the pointer one by one element
    while curr_idx < len(arr) - 1:
        # We start each iteration with an assumption
        # that our first element is the smallest
        smallest_idx = curr_idx

        # Then we enter another loop that
        # will iterate through the unsorted subarray
        for i in range(curr_idx + 1, len(arr)):
            if arr[i] < arr[smallest_idx]:
                smallest_idx = i

        arr[curr_idx], arr[smallest_idx] = arr[smallest_idx], arr[curr_idx]
        curr_idx += 1

    return arr


print(selection_sort(arr))
