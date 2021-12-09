import numpy as np
from scipy.ndimage import measurements


heightmap = np.genfromtxt("lava.txt",
                           dtype = "int16",
                           delimiter = 1
                           )

# If 9, it is not a basin, else TRUE.
# Every point != 9 is a member of AT MOST 1 basin

basins = np.where(heightmap == 9, False, True)

labels, n_labels = measurements.label(basins)

lab_array = range(0, n_labels + 1)

# 0s will sum 0 (they are high points)
# else it will sum to area (each basin is composed of 1)
basin_sizes = measurements.sum(basins,
                              labels,
                              index = lab_array)

# Sort in descending order and keep top 3
biggest_basins = np.sort(basin_sizes)[::-1]
biggest_basins = np.prod(biggest_basins[0:3])

print(f"Biggest basins {biggest_basins}")
