#!/usr/bin/python3

from .bst_construction import construct_bst

array = [1, 10, 8, 3, 5]
node = construct_bst(array)

# Implement a function that determines whether a given binary
# tree is a valid Binary Search Tree (BST).
# Your function should:
# * Take in: The root node of a binary tree
# * Return: true if the tree is a valid BST, otherwise false
#
# A valid BST satisfies:
# * All values in the left subtree are strictly less than the node’s value
# * All values in the right subtree are strictly greater than the node’s value
# * Both left and right subtrees must also be valid BSTs

# The key insight is that a BST is not just about
# comparing a node to its parent - it's about respecting constraints
# from all ancestors. Each node value must lie within a valid range:
# is_valid(node, min-allowed-val, max-allowed-val)
# * For root it's (-inf, +inf)
# * And this contstraint keeps narrowing as you go down the tree
#
# Time O(N): we visit each node exactly once
# Space O(H): due to recursion stack, where H is the hight of the tree
def is_valid_bst(node, low, high):
    if node is None:
        return True

    if not (low < node.value < high):
        return False
    
    return (
        is_valid_bst(node.left, low, node.value) and
        is_valid_bst(node.right, node.value, high)
    )


print(is_valid_bst(node, float("-inf"), float("inf")))
