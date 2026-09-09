# Common algorithmic techniques

## Backtracking

Backtracking is an algorithmic technique for solving problems by building a solution step by step and undoing choices ("backtracking") whenever a partial solution cannot lead to a valid complete solution.

The general idea is:
1. Make a choice.
2. Check if the choice is still valid.
3. If valid, continue exploring from that state.
4. If it leads to a dead end, undo the choice and try another option.
5. Repeat until all possibilities have been explored or a solution is found.

Conceptual pseudocode:
```
function backtrack(state):
    if state is a complete solution:
        record or return solution
        return

    for each possible choice:
        if choice is valid:
            apply choice
            backtrack(updated state)
            undo choice
```

Common use cases:
* Generating permutations and combinations
* Solving mazes
* N-Queens problem
* Subset generation

Key characteristics:
* Typically implemented using recursion (though an explicit stack can also be used).
* Explores a search tree of possible solutions.
* Prunes branches early when they cannot produce a valid solution, making it much more efficient than brute force in many cases.
* Worst-case time complexity is often exponential, but pruning can significantly reduce the actual search space.

## Dynamic programming

Dynamic Programming is a technique for solving problems by breaking them into smaller overlapping subproblems, solving each subproblem once, and storing its result so it doesn't need to be recomputed.

The general idea is:
1. Identify smaller subproblems.
2. Solve each subproblem.
3. Store the result.
4. Reuse stored results when the same subproblem appears again.
5. Combine the results to obtain the final solution.

Two common approaches:
* Top-down (memorization): Start with the main problem and recursively solve smaller problems, caching their results.
* Bottom-up (tabulation): Start with the smallest subproblems and iteratively build up to the final answer.

Key characteristics:
* Useful when a problem has overlapping subproblems.
* Usually requires storing intermediate results, so it trades memory for speed.
* Often turns an exponential recursive solution into a polynomial or linear-time solution, but at the expense of higher memory footprint.

In short: Dynamic programming means solve smaller problems once, remember their answers, and reuse them to efficiently solve the bigger problem.

Examples of classic programming tasks that use the DP technique: Longest common subsequence, Climbing stairs, Minimum coins for change, number of ways to make change.


## Sliding window

Sliding Window is an algorithmic technique for efficiently processing contiguous portions of a sequence, such as an array or string.

Instead of repeatedly examining every possible range from scratch, you maintain a window over part of the sequence and move it step by step.

General idea:
1. Start with a window covering part of the sequence.
2. Keep track of relevant information about the elements inside it (such as a sum or count).
3. Move the window by adding new elements and removing elements that are no longer inside it.
4. Update the result as the window changes.

This help us avoid recalculating the entire window.

Common use cases:
* Finding maximum/minimum values in subarrays
* Finding the longest substring meeting a condition
* Calculating sums or averages over ranges
* Finding unique elements within a range

In short: Sliding window efficiently processes contiguous ranges by reusing information as the range moves, often reducing a brute-force solution from quadratic time to linear time.
