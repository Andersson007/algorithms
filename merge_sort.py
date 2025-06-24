#!/usr/bin/python
# Merge sort.
# Uses the "Devide and Conquer" strategy.
# 1. You split the input array into 2 smaller ones.
# 2. Then you split them again and again until you have
#    a bunch of tiny arrays, each with only one element
#    (which is already sorted, right?).
# 3. Then you start merge those sorted one-element arrays back together.
#    You compare each two and put them together in sorted order
#    two make a two-element sorted arrays.
#    You repeat the process until you merge everything back.

arr = [100, 2, 3, 4, 8, 9, 10]


# Time O(N log N): most efficient in terms of time complexity
#     for a general-purpose sorting algorithm. The speed is consistent
#     because:
#     * it always devides the array evenly which takes O(log N)
#     * merge step takes O(N) because it looks at every element
#     * to construct a sorted array takes again O(log N)
# Space O(N): because we create new lists when merging
def merge_sort(arr):

    # When we split it
    # up to one element, return.
    # Used for recursion.
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from both halves
    # and collect them in order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


print(merge_sort(arr))
