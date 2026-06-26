#!/usr/bin/python3
# Remove duplicates from a linked list.
# You're given a head of a singly linked list
# whose nodes are in sorted order with respect
# to their values.
# Your function should return a modified
# version of the list that doesn't contain
# any duplicates.
# The list must be modified in-place.
# Nodes must continue be sorted.

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

node1 = Node(1)
node2 = Node(1)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4

# * We use 2 pointers: cur_node and next_dist_node.
# * We iterate through nodes while cur_node is not None
# * Within an inner while loop, we use next_dist_node
#   checking if the next node has same value, we'll move it further.
# * When we encounter the distinct value,
#   we'll reassign the "next" pointer of cur_node to next_dist_node
#   and then
# * reassign cur_node to point to next_disctinct_node.

# O(n) Time
# O(1) Space
def remove_dup_from_ll(head):
    cur_node = head

    while cur_node is not None:
        next_dist_node = cur_node.next

        while next_dist_node is not None and next_dist_node.value == cur_node.value:
            next_dist_node = next_dist_node.next
            cur_node.next = next_dist_node
            cur_node = next_dist_node

    return head


my_list_head = remove_dup_from_ll(node1)
while my_list_head is not None:
    print(my_list_head.value)
    my_list_head = my_list_head.next


# Time O(N)
# Space O(1)
def remove_duplicates_from_list(head):
    current = head

    while current and current.next:
        # Compares each node value with the next one
        if current.value == current.next.value:
            # If duplicate, skip it
            current.next = current.next.next
        else:
            # Otherwise, move forward
            current = current.next

    return head
