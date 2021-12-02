raw_positions = open("positions.txt", "r")

positions = [pos.rstrip("\n") for pos in raw_positions]
raw_positions.close()

aim, total_depth, total_dist = 0, 0, 0


for command in positions:
    command = command.split(" ")
    current_direction = command[0]
    amount = int(command[1])

    if current_direction == "up":
        aim = aim - amount
    if current_direction == "down":
        aim = aim + amount

    if current_direction == "forward":
        total_dist = total_dist + amount
        total_depth = total_depth + (amount * aim)


print(
    f"Depth: {total_depth}, Distance: {total_dist}. Product is: {total_depth * total_dist}"
)
