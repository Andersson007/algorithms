#!/usr/bin/python3
# Search In Rotated Sorted Array
# You are given a sorted array of distinct integers
# that has been rotated at an unknown pivot.
# For example, an originally sorted array like [0,1,2,4,5,6,7]
# might become [4,5,6,7,0,1,2] after rotation.
# You are also given a target value.
# Your task is to return the index of the target
# if it is present in the array. If it is not present, return -1.

# Your solution must run in O(log n) time.
# You may assume all values in the array are unique.”

nums = [4,5,6,7,0,1,2]
# if target = 0 -> output: 4
# Notice that the left side of the mid point here is sorted,
# but the right side is not (7, 0, ...)

# Time O(log N)
# Space O(1)
def search_in_rotated_array(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Check if left half is sorted
        # uses <= (not <) so it still works
        # when left == mid (small ranges)
        if nums[left] <= nums[mid]:
            # Target is in the left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            # Target is in the right half
            else:
                left = mid + 1

        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


print(search_in_rotated_array(nums, 0))
