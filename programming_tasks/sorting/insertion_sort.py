#!/usr/bin/python
# Insertion Sort.
# Devide the input array into two subarrays in place.
# The first subarray should be sorted at all times
# and should start with a length of 1, while the second
# subarray should be unsorted.
# Iterate through the unsorted subarray, inserting all
# of its elements into the sorted subarray in the
# correct position by swapping them.
# Eventually the entire array will be sorted.

arr = [100, 2, 8, 1024, 10, 10, 20, 6, 55]


# O(N^2) Time where N is a length of the input array.
# O(1) Space as we sort the array in place.
def insertion_sort(arr):
    # We start with 1 as our temtative subarray length
    for i in range(1, len(arr)):
        j = i
        # j > 0 means that we haven't reached
        # the beginning of the array
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

    return arr


print(insertion_sort(arr))
