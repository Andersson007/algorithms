# Reliable Programming Interview Tasks

- The algorithmic techniques (the section titles below) are explained in [techniques.md](./techniques.md).
- The solution files are located in subdirectories under [./programming_tasks/](./programming_tasks/).

To execute a specific Python file, run:
```
python -m programming_tasks.SUBDIR.filename_without_extension
```

## 1. Two-Pointer Technique

*Scan from both ends or maintain two moving indices. Ideal for sorted arrays and strings.*

1. **Two-Number Sum** — Find two numbers in a sorted array that add up to a target.
2. **Three-Number Sum** — Find all unique triplets in an array that sum to a target.
3. **Container With Most Water** — Find two lines forming a container that holds the most water.
4. **Valid Palindrome** — Check if a string is a palindrome ignoring non-alphanumeric characters.
5. **Remove Duplicates from Sorted Array** — Remove duplicates in-place from a sorted array.

## 2. Sliding Window Technique

*Maintain a moving range over an array or string to satisfy a constraint.*

6. **Longest Substring Without Repeating Characters** — Find the length of the longest substring with all unique characters.
7. **Minimum Window Substring** — Find the smallest window containing all characters of a target string.
8. **Maximum Sum Subarray of Size K** — Find the maximum sum of any contiguous subarray of fixed size K.
9. **Longest Repeating Character Replacement** — Replace up to K characters to get the longest repeating-character substring.
10. **Permutation in String** — Check if one string contains a permutation of another.

## 3. Binary Search

*Achieve O(log n) search by repeatedly halving the search space.*

11. **Binary Search** — Find the index of a target value in a sorted array.
12. **Search in Rotated Sorted Array** — Find a target in a sorted array that has been rotated at an unknown pivot.

## 4. Hash Map / Hash Set

*Enable O(1) lookups for detecting duplicates and counting occurrences.*

13. **First Duplicate Value** — Find the first value that appears more than once in an array.

## 5. Stack

*Use a stack to track nested or sequential structure.*

14. **Balanced Brackets** — Determine whether a string's brackets are properly opened and closed (a.k.a. Valid Parentheses).

## 6. String Manipulation

*Process characters and words directly without a dedicated data structure.*

15. **Reverse Words in String** — Reverse the order of words in a sentence in-place.

## 7. Sorting & Greedy

*Sort input or apply a locally optimal choice at each step to reach a global optimum.*

16. **Merge Intervals** — Given a list of intervals, merge all overlapping ones into a minimal set.
17. **Tandem Bicycle** — Pair up two groups of cyclists (sort one ascending, one descending) to maximize or minimize total speed.
18. **Smallest Difference** — Given two arrays, find the pair of numbers (one from each) with the smallest absolute difference.
19. **Minimum Waiting Time** — Given a list of queries with durations, find the minimum total waiting time by sorting and computing prefix sums.

## 8. Backtracking

*Exhaustively explore all combinations, permutations, or subsets via recursive branching.*

20. **Permutations** — Return all possible orderings of a set of distinct numbers.
21. **Subsets** — Return all possible subsets (power set) of a set of distinct numbers.
22. **Combination Sum** — Find all unique combinations of numbers that sum to a target.

## 9. Dynamic Programming

*Solve optimization problems by caching results of overlapping subproblems.*

23. **Climbing Stairs** — Find the number of distinct ways to reach the top of N stairs.
24. **Coin Change** — Find the minimum number of coins needed to make up a given amount.
25. **Number of Ways to Make Change** — Count how many distinct combinations of coins sum to a given amount.
26. **Longest Common Subsequence** — Find the longest subsequence shared by two strings.

## 10. BFS / DFS — Binary Trees

*Traverse a hierarchical node structure either level-by-level (BFS with a queue) or branch-by-branch (DFS via recursion or an explicit stack). A BST is a binary tree where every left descendant is smaller and every right descendant is larger than the node.*

27. **Construct BST from Sorted Array** — Build a height-balanced BST by recursively picking the middle element as the root.
28. **Validate Binary Search Tree** — Verify that every node satisfies the BST property using DFS with propagated min/max bounds.
29. **Maximum Depth of Binary Tree** — Find the maximum root-to-leaf depth via recursive DFS.
30. **Binary Tree Level Order Traversal** — Return node values grouped by level using BFS with a queue.
31. **Lowest Common Ancestor** — Find the deepest node that is an ancestor of both given nodes in a binary tree.

## 11. Graphs

*A graph is a set of nodes connected by edges — unlike trees, it has no root, edges can be bidirectional, and cycles are allowed. Represented as an adjacency list or matrix. Core techniques are the same DFS/BFS, plus topological sort and Union-Find for connectivity problems.*

32. **Clone Graph** — Deep-copy a graph by traversing it with DFS/BFS and mapping each original node to its new clone. Covers graph construction.
33. **Number of Islands** — Count connected land regions in a 2D grid by running DFS/BFS from each unvisited land cell.
34. **Course Schedule** — Determine if all courses can be finished by detecting cycles in a directed graph (topological sort / DFS).
35. **Rotting Oranges** — Find the minimum time for all oranges to rot using multi-source BFS from all initially rotten cells simultaneously.
36. **Number of Connected Components** — Count distinct connected components in an undirected graph using DFS or Union-Find.

## Summary

| Technique                | Tasks | Source                          |
|--------------------------|-------|---------------------------------|
| Two-Pointer              | 5     | All three lists                 |
| Sliding Window           | 5     | All three lists                 |
| Binary Search            | 2     | All three lists + personal pick |
| Hash Map / Hash Set      | 1     | Personal pick                   |
| Stack                    | 1     | Personal pick                   |
| String Manipulation      | 1     | Personal pick                   |
| Sorting & Greedy         | 4     | Personal pick                   |
| Backtracking             | 3     | All three lists                 |
| Dynamic Programming      | 4     | All three lists + personal pick |
| BFS / DFS — Binary Trees | 5     | All three lists (technique)     |
| Graphs                   | 5     | All three lists (technique)     |
| **Total**                | **36**|                                 |

## Trimmed Personal Picks (and why)

| Task                     | Reason skipped                                          |
|--------------------------|---------------------------------------------------------|
| Sort Stack               | Niche; interviewers prefer stack design questions       |
| Valid IP Addresses       | Too format-specific; seldom appears in general rounds   |
| Bubble Sort              | Not asked as a problem-solving task in modern interviews|
| Insertion Sort           | Same as above                                           |
| Product Sum              | Niche recursive; rarely asked at major companies        |
| Non-Constructable Change | Clever but rare; low probability in standard interviews |
| Monotonic Array          | Too simple for a standalone interview question          |
| Move Element to End      | Too simple; covered by the Two-Pointer technique        |
| Sorted Squared Array     | Too simple; covered by the Two-Pointer technique        |
| Three Number Sum         | Already covered by **Three-Number Sum** in the list     |
| Two Number Sum           | Already covered by **Two-Number Sum** in the list       |
| Palindrome Check         | Already covered by **Valid Palindrome** in the list     |
| Min Coins for Change     | Already covered by **Coin Change** in the list          |
| Longest Substring        | Already covered in Sliding Window section               |
| Longest Common Subseq.   | Already in the list                                     |
| Permutations             | Already in the list                                     |
| Powerset                 | Already covered by **Subsets** in the list              |
