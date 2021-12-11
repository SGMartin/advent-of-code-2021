import numpy as np

dumbos = np.genfromtxt("dumbos.txt", delimiter=1, dtype="int16")

lights = 0
steps = 100


def get_neighbors(arr, cell):
    adj = []

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            rangeX = range(0, arr.shape[0])  # X bounds
            rangeY = range(0, arr.shape[1])  # Y bounds

            (newX, newY) = (cell[0] + dx, cell[1] + dy)  # adjacent cell

            if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
                adj.append((newX, newY))

    return adj


def get_flash_chain(arr):

    total_flashes = 0
    current_flashes = 0
    this_arr = arr

    can_flash = this_arr > 9
    current_flashes = can_flash.sum()

    if current_flashes > 0:
        ## Get all neighbors
        row, col = np.where(can_flash)
        rc = zip(row, col)
        for r, c in rc:
            neighbors = get_neighbors(this_arr, (r, c))
            for neighbor in neighbors:
                if not can_flash[neighbor[0], neighbor[1]]:  # unflashed neighbor
                    this_arr[neighbor[0], neighbor[1]] += 1

        # Clear this it. of flashes
        this_arr[can_flash] = 0

        # Do we have flashes left)
        even_more_flashes, updated_arr = get_flash_chain(this_arr)

        # Compare our initial array with the updated one. ANY flashed must be
        # reset again to 0.
        updated_arr[can_flash] = 0
        this_arr = updated_arr

        # Finally, update the score
        current_flashes = current_flashes + even_more_flashes

    total_flashes = total_flashes + current_flashes

    return (total_flashes, this_arr)


for step in range(0, steps):
    dumbos += 1

    flashes, dumbos = get_flash_chain(dumbos)
    lights = lights + flashes


print(f"We have a grand total of {lights} flashes")
