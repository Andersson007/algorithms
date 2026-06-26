#!/usr/bin/python3


class BST():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def contains(self, value):
        curr_node = self

        while curr_node is not None:
            if value < curr_node.value:
                curr_node = curr_node.left
            elif value > curr_node.value:
                curr_node = curr_node.right
            else:
                return True

        return False

    def insert(self, value):
        curr_node = self

        while True:
            if value < curr_node.value:
                if curr_node.left is None:
                    curr_node.left = BST(value)
                    break
                else:
                    curr_node = curr_node.left
            else:
                if curr_node.right is None:
                    curr_node.right = BST(value)
                    break
                else:
                    curr_node = curr_node.right

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
                    if cur_node.left is not None:
                        parent_node.left = cur_node.left
                    else:
                        parent_node.left = cur_node.right
                elif parent_node.right == cur_node:
                    if cur_node.right is not None:
                        parent_node.right = cur_node.right
                    else:
                        parent_node.right = cur_node.left
                break

        return self
