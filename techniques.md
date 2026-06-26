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
