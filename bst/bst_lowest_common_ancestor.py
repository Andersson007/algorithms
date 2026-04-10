#!/usr/bin/python3

from .bst_construction import construct_bst

array = [8, 3, 10, 1, 6, 14]
node = construct_bst(array)

# Lowest Common Ancestor (BST)
# Implement a function that finds the Lowest Common Ancestor (LCA)
# of two nodes in a Binary Search Tree.
#
# Your function should:
#   Input:
#     root — the root node of a BST
#     p - value (or node) of the first target node
#     q - value (or node) of the second target node
#
# The Lowest Common Ancestor is the lowest node in the tree
# that has both p and q as descendants (a node can be a descendant of itself).
#
# Example:
# Input (BST)
#         6
#        / \
#       2   8
#      / \ / \
#     0  4 7  9
#       / \
#      3   5
# p = 2
# q = 8
# Output: 6
# p = 2
# q = 4
# Output: 2

# Solution: Use the BST property:
# * If both p and q are smaller → go left
# * If both are larger → go right
# * Otherwise → current node is the LCA
# This works because the first node where the paths
# to p and q split is the lowest common ancestor.

# Time O(H): Move down the tree once
# Space O(1): Iterative solution
def lowest_common_ancestor(node, p, q):
    while node:
        if p < node.value and q < node.value:
            node = node.left
        elif p > node.value and q > node.value:
            node = node.right
        else:
            return node

    return None


print(lowest_common_ancestor(node, 1, 6))
print(lowest_common_ancestor(node, 1, 3))
print(lowest_common_ancestor(node, 10, 14))
