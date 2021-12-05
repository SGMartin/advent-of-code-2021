import re
import numpy as np

thermal_reg = r"(\d+),(\d+) -> (\d+),(\d+)"

## Generates an array of 500x1 where
## each entry is a 4n tuple
thermal_vents = np.fromregex(file = "thermals.txt",
                             regexp = thermal_reg,
                             dtype = [("", int)]*4)


## Generate our map grid. max value  -> 1000
## Pretty sure I can plot this lol
depths_map = np.zeros((2, 1000, 1000))

for (x1, y1, x2, y2) in thermal_vents:
    # -1 if x2 < x1
    # +1 if x2 > x1
    # 0 if  == aka Horizontal/vertical

    x_dir = np.sign(x2 - x1)
    y_dir = np.sign(y2 - y1)

    while (x1, y1) != (x2 + x_dir, y2 + y_dir):
        depths_map[x_dir * y_dir, x1, y1] += 1
        x1 += x_dir
        y1 += y_dir

print(f"Horizontal/vertical points are: {(depths_map[0] >1).sum()}")
