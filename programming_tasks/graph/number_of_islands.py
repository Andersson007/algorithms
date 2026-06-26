#!/usr/bin/python3

# Number of Islands
# You are given a 2D grid of size m x n where each cell is either:
# '1' → land
# '0' → water
# Your task is to count the number of islands.
# An island is:
# A group of '1's connected horizontally or vertically (not diagonally)
# Surrounded by water ('0') or edges of the grid
# Input:
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
# Expected output: 3, because
# There are 3 islands:
# * Top-left block (4 connected '1's)
# * Middle single '1'
# * Bottom-right block (2 connected '1's)

# What is evaluated:
# * Correct grid traversal (DFS or BFS)
# * Proper marking of visited cells (to avoid double counting)
# * Handling boundaries safely
# * Time/space complexity awareness

# Solution:
# Treat the grid like a graph:
# * Each '1' = land node
# * Connected neighbors (up/down/left/right) = edges
#
# Every time you find a '1', you:
# 1. Increment island count
# 2. Use DFS to mark the whole island as visited

# Logic:
# * Loop through every cell
# * When you hit land ('1'):
#   * That’s a new island
#   * Run DFS to erase the whole island (mark as '0')
# * This ensures you never count the same island twice
# Intuition in one line: “Find land → sink the whole island → repeat”

# Time: O(M x N): You process each cell once
# Space: O(M X N): In worst case (all land), the stack can grow to size of grid
def num_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for r in range(rows):
        for c in range(cols):

            # If it's land
            if grid[r][c] == "1":
                count += 1
                stack = [(r, c)]

                # Check neighbors and "sink the whole island"
                while stack:
                    row, col = stack.pop()

                    # Check bounds and if it's land
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == "1":
                        # Mark as visited
                        grid[row][col] = "0"

                        # add neighbors
                        stack.append((row + 1, col))
                        stack.append((row - 1, col))
                        stack.append((row, col + 1))
                        stack.append((row, col - 1))

    return count


print(num_islands(grid))
