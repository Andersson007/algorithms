#!/usr/bin/python
# Binary search algorithm.
# The function takes in a sorted array
# and a target int, and determines if the array
# contains the target using the Binary search algorithm.

arr = [2, 3, 4, 8, 9, 10]

# Time O(log N)
# Space O(1)
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1

    return -1

print(binary_search(arr, 8))
print(binary_search(arr, 1))
