#!/usr/bin/python3

class BST():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def contains(self, value):
        cur_node = self
        while cur_node is not None:
            if value < cur_node.value:
                cur_node = cur_node.left
            elif value > cur_node.value:
                cur_node = cur_node.right
            else:
                return True
        return False

    def insert(self, value):
        cur_node = self
        while True:
            if value < cur_node.value:
                if cur_node.left is None:
                    cur_node.left = BST(value)
                    break
                else:
                    cur_node = cur_node.left
            else:
                if cur_node.right is None:
                    cur_node.right = BST(value)
                    break
                else:
                    cur_node = cur_node.right

    def get_min_value(self):
        cur_node = self
        while cur_node.left is not None:
            cur_node = cur_node.left
        return cur_node.value

    def remove(self, value, parent_node=None):
        cur_node = self
        while cur_node is not None:
            if value < cur_node.value:
                parent_node = cur_node
                cur_node = cur_node.left
            elif value > cur_node.value:
                parent_node = cur_node
                cur_node = cur_node.right
            # When we find the node we want to remove
            else:
                # When the node has 2 child nodes
                # we need to find the smallest value of the right subtree
                # and replace node's value with it. Then remove
                # the smallest node
                if cur_node.left is not None and cur_node.right is not None:
                    cur_node.value = cur_node.right.get_min_value()
                    cur_node.right.remove(cur_node.value, cur_node)
                # When dealing with a root node
                # (doesn't have a parent node)
                elif parent_node is None:
                    if cur_node.left is not None:
                        cur_node.value = cur_node.left.value
                        cur_node.right = cur_node.left.right
                        cur_node.left = cur_node.left.left
                    elif cur_node.right is not None:
                        cur_node.value = cur_node.right.value
                        cur_node.right = cur_node.right.right
                        cur_node.left = cur_node.right.left
                    else:  # When root doesn't have child nodes
                        return self
                elif parent_node.left == cur_node:
                    parent_node.left = cur_node.left if cur_node.left is not None else cur_node.right
                elif parent_node.right == cur_node:
                    parent_node.right = cur_node.right if cur_node.right is not None else cur_node.left
                break

        return self


bst = BST(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(5)
bst.insert(1)
bst.insert(13)
bst.insert(22)
bst.insert(14)

# Find closest value in BST.
# Write a function that takes in a BST and a target int value
# and returns the closest value to that target value contained
# in BST. Assume that there'll only be one closest value.
# * Each BST value is strictly greater than the values
#   of every node to its left;
# * its value is less than or equal
#   to the values of every node to its right;
# * its children nodes are either valid BST nodes or None

# O(log N) avg Time where N is a number of nodes, O(N) if there's one branch
# O(1) Space as we do not consume any additional space depending on the input size
def bst_find_closest_val(tree, target):
        cur_node = tree
        closest_val = cur_node.value

        while cur_node is not None:
            if abs(cur_node.value - target) < abs(closest_val - target):
                closest_val = cur_node.value

            if target == cur_node.value:
                break

            elif target < cur_node.value:
                cur_node = cur_node.left

            elif target > cur_node.value:
                cur_node = cur_node.right

        return closest_val


print(bst_find_closest_val(bst, 12))
