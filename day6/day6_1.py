with(open("fishes.txt", "r") as lines):
    raw_fishes = [int(fish) for fish in lines.read().strip().split(",")]

# There are 9 possible clock states 0-8.
# Count the n. of each state in the range 0-9
# State list
# 0 (spawn today), 1, 2, 3, 4, 5, 6, 7, 8 (alevin)
clock_states = [raw_fishes.count(state) for state in range(0, 9)]
days = 80

for day in range(0, days):

   # Shift everything to the left
    spawning = clock_states.pop(0)
    clock_states.append(spawning)

    # Now add spawned fishes
    clock_states[6] += spawning

print(f"At day {days}, there are {sum(clock_states)} fishes")
