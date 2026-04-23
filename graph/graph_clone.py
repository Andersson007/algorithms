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
# * a list of its neighbors
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

# Solution:
# The simplest way to think about this problem is:
# You’re copying a graph that may have cycles, so
# you must remember what you’ve already copied.
# Use DFS + a dictionary (hash map):
# * Key: original node
# * Value: cloned node
# Why? If you revisit a node (because of a cycle),
# you don’t want to clone it again — you just reuse the existing clone.

# DFS (Depth-first Search) is a graph traversal algorithm that
# explores as far as possible along one branch before backtracking:
# * Start from a node.
# * Visit it and mark it as visited.
# * Recursively (or using a stack) visit one unvisited neighbor at a time.
# * When no unvisited neighbors remain, backtrack and continue.
# Time complexity O(V + E): where V is a number of vertices and E is edges

# * Stack → controls DFS traversal
# * visited → ensures:
#   * each node is cloned once
#   * cycles don’t cause infinite loops
# * Edges are recreated by linking cloned nodes

# Time: O(V + E): you visit each vertex once, for each vertex, you loop
#   through its neighbors, i.e. through all edges across the graph
# Space: O(V): we store visited dictionary one entry per vertex +
#   the stack, that in worst case can hold up to all vertices +
#   the cloned graph itself = the input graph
def clone_graph(node):
    if not node:
        return None

    visited = {}
    visited[node] = Node(node.val)

    stack = [node]

    while stack:
        cur_node = stack.pop()

        for neighbor in cur_node.neighbors:
            if neighbor not in visited:
                # clone and add to stack
                visited[neighbor] = Node(neighbor.val)
                stack.append(neighbor)

            # connect the clone
            visited[cur_node].neighbors.append(visited[neighbor])

    return visited[node]


print_graph(node)
print_graph(clone_graph(node))

# DFS
# Time: O(V + E)
# Space: O(V)
def dfs(node):
    visited = set()
    stack = [node]

    while stack:
        cur_node = stack.pop()  # take last element (LIFO)

        if cur_node not in visited:
            print(cur_node.val)  # process node
            visited.add(cur_node)

            # add neighbors to stack
            stack.extend(cur_node.neighbors)

dfs(node)


# BFS:
# * Uses a queue (FIFO) instead of stack (LIFO)
# * Processes nodes livel by level:
#   * Visit the start node
#   * Then all its neighbors
#   * Then neighbors of neighbors, etc.
# Key idea: go wide first, no deep
# Time: O(V + E)
# Space: O(V)
from collections import deque

def bfs(node):
    visited = set()
    queue = deque([node])

    while queue:
        cur_node = queue.popleft()

        if cur_node not in visited:
            print(cur_node.val)  # Process the node

            visited.add(cur_node)

            queue.extend(cur_node.neighbors)

bfs(node)
