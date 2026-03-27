#!/usr/bin/python3

from .bst_construction import construct_bst

array = [8, 3, 10, 1, 6, 14]
node = construct_bst(array)

# BST Level Order Traversal
# Implement a func that performs level-order traversal
# (breadth-first traversal) of a BST.
# You function should:
# Input: The root node of a BST
# Output: A list of lists containing the node values
#   level by level from top to bottom, left to right
#
# Example
#
# Input (BST):
#
#         8
#        / \
#       3   10
#      / \    \
#     1   6    14
#
# Output: [[8], [3, 10], [1, 6, 14]]

from collections import deque

# Solution: we use a queue and iteration to traverse the tree level by level.
# Core concept:
# 1. Put the root in a queue.
# 2. While the queue is not empty:
#   a. Process all nodes currently in the queue (this represents one level)
#   b. For each node:
#     * Add its value to the current level list
#     * Add its children to the queue
# 3. Store each level's value in the result.

# Intuition: Think of the queue as holding the current level of the tree.
#   Each iteration of the while loop processes one full level:
# Queue initially: [8]
#
# Process level:
# 8 → add children → [3,10]
#
# Process level:
# 3,10 → add children → [1,6,14]
#
# Process level:
# 1,6,14 → []

# Time O(N): visit each node once
# Space O(W): where W is the max width of the tree -> queue size
def level_order_traversal(node):
    if node is None:
        return []

    result = []
    # The queue holds the current level of the tree
    queue = deque([node])

    # Each iteration of the while loop
    # processes one full level
    while queue:
        cur_level = []
        size = len(queue)

        for _ in range(size):
            node = queue.popleft()
            cur_level.append(node.value)

            # Append left child if exist
            if node.left:
                queue.append(node.left)

            # Append right child if exits
            if node.right:
                queue.append(node.right)

        result.append(cur_level)

    return result


print(level_order_traversal(node))
