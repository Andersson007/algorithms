#!/usr/bin/python3
# Minimum waiting time.
# * You're given a non-empty array of positive integers
#   representing the amounts of time that specific queries
#   take to execute.
# * Only one query can be executed at a time,
#   but the queries can be executed in any order.
# * A waiting time is defined as the amount of time
#   that the query must wait before its execution starts,
#   i.e. if a query is executed second, then its waiting time
#   is the duration of the first query; if a query is
#   executed third, then its waiting time is the sum
#   of the durations of the first two queries.

durations = [3, 2, 1, 5, 4]

# * We need to pick an order such that the total waiting
#   time for all the queries will be minimal.
# * We need to sort the array first because if we execute
#   it in ascending order from the fastest to the slowest
#   it'll be most effective, e.g.
#   [100, 1] min W time is 100
#   [1, 100] min W time is 1
#   So it doesn't make sense to execute the largest query first.
# * In [1, 6], the first waits 0, the second waits 1,
#   so 0 + 1 = 1

# Best explanation:
# [3, 2, 1] -> 0 + 3 + (3 + 2) = 8
# [1, 2, 3] -> 0 + 1 + (1 + 2) = 4

# Time: O(n log n) as we sort
# Space: O(1) as we don't take extra space
def min_waiting_time(durations):
    durations.sort()
    cumulative_time = 0
    total_wait_time = 0

    for time in durations[:-1]:  # We don't count the last time
        cumulative_time += time
        total_wait_time += cumulative_time

    return total_wait_time


# Option 2
# Long queries delay many future queries.
# Short queries delay fewer future queries.
# Always execute the query with the smallest
# duration next.
# A greedy algorithm:
# * Makes the best intermediate choice
# * Never revisits or undoes decisions
# * Aims to reach the optimal solution through these local choices.
# * Probably optimal for certain problems.
# The waiting time of a query is the total duration of all queries
# before it. Sorting in ascending order minimizes it.

# “I sort the queries from shortest to longest,
# then accumulate how long each query waits behind the ones before it.”
# Best explanation:
# [3, 2, 1] -> 0 + 3 + (3 + 2) = 8
# [1, 2, 3] -> 0 + 1 + (1 + 2) = 4

# Time O(N log N)
# Space O(1)
def min_wait_time(queries):
    queries.sort()
    total_wait = 0
    prev_wait = 0

    for time in queries:
        # Add the running sum of how long prev queries
        # take to the total waiting time
        total_wait += prev_wait
        # Then add the current query time to the running sum
        prev_wait += time

    return total_wait


print(min_wait_time([3, 2, 1, 2, 6]))
