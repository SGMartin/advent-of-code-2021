#   This could be optimized using the approach from the previous problem
#   but I'm lazy and today's cleaning day.
#

import numpy as np

with open("crabs.txt", "r") as lines:
    crabs = [int(crab) for crab in lines.read().strip().split(",")]

crabs = np.array(crabs)

lowest_fuel = 0

max_distance = max(crabs) - min(crabs)


for change in range(min(crabs), max(crabs) + 1):

    this_steps = abs(crabs - change)
    this_fuel = sum([sum(range(1, n + 1)) for n in this_steps])

    if lowest_fuel == 0:
        lowest_fuel = this_fuel
    else:
        if this_fuel < lowest_fuel:
            lowest_fuel = this_fuel


print(f"Lowest fuel is {lowest_fuel}")
