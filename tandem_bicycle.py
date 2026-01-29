#!/usr/bin/python3
# Tandem Bicycle.
# * It's operated by a pair of people
# * Tandem speed == max(rider1, rider2)
# * Write a function that returns the max possible
#   total speed or a min possible total speed
#   of all of the tandem bicycles based on
#   the "pastest" parameter. If true, returns
#   max, otherwise min possible speed.
# * Total speed is defined as a sum of speeds
#   of all tandem bicycles.

rider1_speeds = [5, 5, 3, 9, 2]
rider2_speeds = [3, 6, 7, 2, 1]

# Solution:
# * To make all the bicycles most efficient,
#   we should pair the fastest rider with the slowest
#   one in each pair.
# * To organize pairs least efficiently, we should
#   do opposite: to pair the fastest ones with the
#   fastest ones from the other team.
def tandem_bicycles(rider1_speeds, rider2_speeds, fastest):
    rider1_speeds.sort()
    rider2_speeds.sort(reverse=True) if fastest else rider2_speeds.sort()

    total_speed = 0
    for r1, r2 in zip(rider1_speeds, rider2_speeds):
        total_speed += max(r1, r2)

    return total_speed

# Max possibe speed
print(tandem_bicycles(rider1_speeds, rider2_speeds, True))
# Min possible speed
print(tandem_bicycles(rider1_speeds, rider2_speeds, False))

# My solution
rider1_speeds = [5, 5, 3, 9, 2]
rider2_speeds = [3, 6, 7, 2, 1]

# Time O(N log N)
# Space O(1)
def tandem_bicycle(rider1_speeds, rider2_speeds, fastest):
    rider1_speeds.sort()
    if fastest:
        rider2_speeds.sort(reverse=True)
    else:
        rider2_speeds.sort()

    total_speed = 0
    for i in range(len(rider1_speeds)):
        total_speed += max(rider1_speeds[i], rider2_speeds[i])

    return total_speed


print(tandem_bicycle(rider1_speeds, rider2_speeds, True))
print(tandem_bicycle(rider1_speeds, rider2_speeds, False))
