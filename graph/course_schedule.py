#!/usr/bin/python3

# Course Schedule
# You are given:
# * An integer numCourses representing the total number of courses labeled from 0 to numCourses - 1
# * A list of prerequisites where each pair [a, b] means:
#   "To take course a, you must first take course b"
# Task: Determine if it is possible to finish all courses (return True/False).

# Key Insight: This is a cycle detection problem in a directed graph:
# * Courses = nodes
# * Prerequisites = directed edges
# * If there is a cycle → impossible to finish

# Example 1
# * numCourses = 2
# * prerequisites = [[1, 0]]
# Explanation:
# * To take course 1 → you need course 0
# * Valid order: 0 → 1
# Output: True

# Example 2 (Cycle)
# # numCourses = 2
# # prerequisites = [[1, 0], [0, 1]]
# Explanation:
# * 1 depends on 0
# * 0 depends on 1
# * cycle → impossible
# Output: False

# Soulution:
# Core Idea: This is cycle detection in a directed graph.
# * If there’s a cycle → you cannot finish all courses
# * If no cycle → you can
# We'll use DFS with 3 states:
# 0 = unvisited
# 1 = visiting (currently in recursion path)
# 2 = visited (fully processed)
# The key trick: If you ever revisit a node in state 1 → cycle detected

# Logic (simple)
# * indegree[i] = how many prerequisites course "i" still needs
# * Start with all courses that need none
# * Each time you “take” a course:
#   * Reduce indegree of its neighbors
# * If something never reaches indegree 0 → it’s stuck in a cycle
# Intuition in one line: "Keep removing courses with no dependencies—if something remains, it’s a cycle"

# Time: O(V + E): process each course and each edge once
# Space: O(V + E): graph gives O(E), indegree array + stack = O(V)
def can_finish(num_courses, prereqs):
    # Create adjacency list {course: [list of courses that depend on it}
    graph = {i: [] for i in range(num_courses)}

    indegree = [0] * num_courses  # indegree[i] = number of prerequisites course "i" still needs

    # Build the graph:
    # * b -> a (to take a, you must take b)
    # * Increase indegree of a
    for a, b in prereqs:
        graph[b].append(a)
        indegree[a] += 1

    stack = []  # Stack will store courses with no remaining prerequisites
    # Initialize stack with courses that can be taken immediately
    for i in range(num_courses):
        if indegree[i] == 0:
            stack.append(i)

    completed = 0  # Count how many courses we successfully “take”

    # Process courses while we have available ones
    while stack:
        course = stack.pop()  # Take one course (LIFO order)
        completed += 1        # Mark it as completed

        # Look at courses that depend on this one
        for neighbor in graph[course]:
            indegree[neighbor] -= 1     # Remove this prerequisite (we just completed it)

            # If a course now has no prerequisites → it’s ready to take → push to stack
            if indegree[neighbor] == 0:
                stack.append(neighbor)

    # Final check: If we completed all courses → no cycle, otherwise a cycle exists
    return completed == num_courses


num_courses = 4
prereqs = [[1,0],[2,1],[3,2]]
print(can_finish(num_courses, prereqs))
