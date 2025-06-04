#!/usr/bin/python3
# BST Construction.
# * Write a BST class that support insert, remove,
#   and contains methods.
# * Note that you can't remove values from a single-node
#   tree. I.e., calling the remove method on a single-node
#   tree should simply do nothing.
# * Each BST node has an int "value", a "left" child node,
#   and a "right" child node.
# * A node is said to be a valid BST node if and only if
#   it satisfies the BST property:
#   * its "value" is strictly greater than the values of
#     every node to its left;
#   * its "value" is less than or equal to the values of
#     every node to its right;
#   * its children nodes are either valid BST nodes
#     themselves or None.
# * If you remove root, you need to grab the smallest
#   value in the right subtree. It's also fair when we
#   want to remove a node with both child are not None

# Time: O(log N) for all the methods as we
#  eliminate a half of elements each time.
#       O(N) Time worst-case when the tree is liniar.
# Space: O(1) when we use iterative approach (like here)

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


bst = BST(5)
bst.insert(1)
bst.insert(3)
bst.insert(4)
bst.insert(6)
bst.insert(7)

print(bst.value)
