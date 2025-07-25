#!/usr/bin/python3
# Three Number Sum.
# Your function takes in a non-empty array
# of distinct integers and a target sum.
# * The func should find all triplets in the
#   array that sum up to the target sum and
#   return a 2D array of all these triplets.
# * The numbers in each triplet must be ordered
#   in ascending order, and the triplets themselves
#   should be ordered in ascending order with
#   respect to the numbers they hold.
# * If no three numbers sum up to the target sum,
#   the func must returns an empty array.

array = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0
# output = [[-8, 2, 6], [-8, 3, 5], [6, 1, 5]]
# * Sort the array in an ascending order.
# * Use cur_num, a left and a right pointer.
# * Use two loops.
# * cur_sum = cur_num + L + R
# * If sums up, put it in a triplet.
# * If it's smaller than target, increment L
#   to get a bigger sum.
# * If it's bigger, dicrement R to get a smaller sum.


# Time O(N^2): because we use nested loops
# Space O(N): because we can create another array
#  of up to the same length as the input array.
def three_num_sum(array, target):
    array.sort()
    triplets = []

    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            cur_sum = array[i] + array[left] + array[right]
            if cur_sum == target:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif cur_sum < target:
                left += 1
            elif cur_sum > target:
                right -= 1

    return triplets


print(three_num_sum(array, target))
