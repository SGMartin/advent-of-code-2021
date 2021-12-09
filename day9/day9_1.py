import numpy as np

heightmap = np.genfromtxt("lava.txt",
                           dtype = "int16",
                           delimiter = 1
                           )

# This way I don't have to check If i'm overflowing
heightmap_pad = np.pad(heightmap,
                       pad_width = 1,
                       mode = "constant",
                       constant_values = 9)


rows, cols = heightmap_pad.shape
risk = 0

# This way I don't have to check If i'm overflowing
# 9 is like a frame
for row in range(1, rows - 1):
    for col in range(1, cols - 1):
        if (heightmap_pad[row, col] < heightmap_pad[row - 1, col] and
        heightmap_pad[row, col] < heightmap_pad[row + 1, col] and
        heightmap_pad[row, col] < heightmap_pad[row, col - 1] and
        heightmap_pad[row, col] < heightmap_pad[row, col + 1]):
            risk += heightmap_pad[row, col] + 1


print(f"Current risk is {risk}")
