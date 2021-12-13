import numpy as np
import matplotlib.pyplot as plt

with open("origami.txt", "r") as raw_folds:
    lines = [line.strip() for line in raw_folds.readlines()]

footer_start = len(lines) - lines.index("") - 1 # -1 cuz. starts from 0
folds = [line for line in lines if "fold" in line]

paper_dots = np.genfromtxt("origami.txt",
                  delimiter = ",",
                  skip_footer = footer_start,
                  dtype = "int16")

y_range = paper_dots[:,0].max() + 1
x_range = paper_dots[:,1].max() + 1

paper_grid = np.zeros((x_range,y_range), dtype = "int16")

for row, col in paper_dots:
    paper_grid[col, row] = 1

for fold in folds:    
    direction    = fold.split("along ")[-1][0]
    line_to_fold = int(fold.split("along ")[-1][2:])

    if direction == "x":
        up = paper_grid[:,0:line_to_fold]
        dn = paper_grid[:, line_to_fold + 1:]
        paper_grid = up + np.flip(dn, axis = 1)
    else:
        up = paper_grid[0:line_to_fold,:]
        dn = paper_grid[line_to_fold + 1:,]
        paper_grid = up + np.flip(dn, axis = 0)

    paper_grid[paper_grid > 1] = 1



## THE FUCK THIS IS 
## IS THIS AN ACTUAL IMG?
plt.imshow(paper_grid)
plt.show()
