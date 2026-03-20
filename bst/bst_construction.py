#!/usr/bin/python3

from .bst import BST

# The BST property:
# * All values in the left subtree of a node are less than the node value.
# * All values in the right subtree are greater than the node value.

# values = [8, 3, 10, 1, 6, 14, 4, 7, 13]

# Result:
#        8
#       / \
#      3   10
#     / \    \
#    1   6    14
#       / \   /
#      4   7 13

# Time O(N long N): because it's BST insertion complexity
# Space O(N)
def construct_bst_as_is(values):
    bst = BST(values[0])
    for i in range(1, len(values)):
        bst.insert(values[i])

    return bst


# print(construct_bst_as_is(values))


# Construct a height-balanced BST from Array:
# 1. Sort the array first.
# 2. Build a height-balanced BST by recursively picking
# the middle element as the root.

# array = [5, 8, 3, 10, 9, 25, 1, 4]

# Time O(N)
# Space O(log N): because of recursion stack
def construct_bst(array):
    if not array:
        return None

    array.sort()
    return build(array, 0, len(array) - 1)


def build(array, left, right):
    # Base case: if there are no elements
    # left in this subarray, stop and return no node,
    # i.e. when you get an invalid range where left idx > right idx
    # which means there's no element to form a node
    if left > right:
        return None

    mid = (left + right) // 2

    node = BST(array[mid])
    node.left = build(array, left, mid - 1)
    node.right = build(array, mid + 1, right)

    return node

# print(construct_bst(array))
