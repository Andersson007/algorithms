#!/usr/bin/python3

from .bst_construction import construct_bst

array = [1, 10, 8, 3, 5]
node = construct_bst(array)

# Max Depth of BST.
# Implement a func that computes the maximum depth (height) of a BST.
# Requirements:
# Your function should:
# * Input: The root node of a BST
# * Output: An integer representing the maximum depth of the tree
# Definition:
# * The maximum depth is the number of nodes along the longest
#   path from the root down to the farthest leaf.
# * An empty tree has depth 0.

# Time O(N): worst case in case of a very imbalanced tree
#      O(log N): in case of balanced
# Space O(H): where H is a tree height, because of the recursion call stack
def max_depth_bst(node):
    if node is None:
        return 0

    return 1 + max(
        max_depth_bst(node.left),
        max_depth_bst(node.right)
    )


print(max_depth_bst(node))
