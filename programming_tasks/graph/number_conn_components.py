#!/usr/bin/python3

# Number of Connected Components
# You are given:
# * An integer n representing the number of components (labeled 0 to n-1)
# * A list of connections where each pair [a, b] means:
#   * Component a is directly connected to component b
# * All connections are undirected.

# Task: Return the number of connected components
# (i.e., groups of computers that can reach each other).

# Example
# n = 5
# connections = [[0,1], [1,2], [3,4]]
# Explanation
# * Group 1: 0 ↔ 1 ↔ 2
# * Group 2: 3 ↔ 4
# Output: 2

# Edge Case
# n = 4
# connections = []
# Output: 4 (Each computer is isolated)

# Explanation:
# Core idea:
# * Build a graph
# * Traverse it
# * Count how many times you start a new traversal
# ! Each new traversal = new connected component

# Solution logic (simple):
# 1. Build adjacency list
# 2. Loop through all nodes
# 3. If node not visited:
#   * Start DFS
#   * Mark all reachable nodes
#   * Increment component count
# Intuition in one line: “Each time I discover a new unvisited node, I found a new group”

# Time Complexity: O(V + E): Visit each node once → O(V), traverse each edge once → O(E)
# Space Complexity: O(V + E): Graph storage → O(E), visited set → O(V), stack → up to O(V)
def count_components(n, connections):
    # build graph
    graph = {i: [] for i in range(n)}
    # populate it with component: [compontents it depends on]
    # the connections are bidirectional in this task
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)

    # to track visited nodes (i.e. to avoid loops)
    # we use the visited set
    visited = set()
    count = 0  # compontent count

    for node in range(n):
        if node not in visited:
            count += 1
            stack = [node]  # to handle all neighbors

            while stack:
                curr = stack.pop()

                if curr not in visited:
                    visited.add(curr)

                    # add all neighbors
                    for neighbor in graph[curr]:
                        stack.append(neighbor)

    return count


n = 5
connections = [[0,1], [1,2], [3,4]]
print(count_components(n, connections))
