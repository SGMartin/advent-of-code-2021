raw_positions = open("positions.txt", "r")

positions = [pos.rstrip("\n") for pos in raw_positions]
raw_positions.close()

total_depth = 0
total_dist = 0

for command in positions:

    command = command.split(" ")
    current_direction = command[0]
    amount = int(command[1])

    if current_direction == "forward":
        total_dist = total_dist + amount
    if current_direction == "up":
        total_depth = total_depth - amount
    if current_direction == "down":
        total_depth = total_depth + amount


print(
    f"Depth: {total_depth}, Distance: {total_dist}. Product is: {total_depth * total_dist}"
)
