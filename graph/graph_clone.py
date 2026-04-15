#!/usr/bin/python3

from .graph import print_graph

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

node = node1

# 1 -- 2
# |    |
# 4 -- 3

# Clone Graph
# You are given a reference to a node in a connected undirected graph.
# Each node contains:
# * an integer value val
# * a list of its neighbors neighbors
# Your task is to return a deep copy (clone) of the graph.
# A deep copy means:
# * You must create entirely new nodes (no shared references with the original graph)
# * The structure (connections) must be identical

# Input: a starting node of a graph that can be represented (for readability)
#   in the adjacency list format, e.g.:
# adj_list = [
#     [2, 4],  # Node 1
#     [1, 3],  # Node 2
#     [2, 4],  # Node 3
#     [1, 3]   # Node 4
# ]
#
# Output: a deep copy of the input graph


def clone_graph(node):
    pass


print_graph(node)
print_graph(clone_graph(node))
