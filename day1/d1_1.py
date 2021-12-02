raw_input = open("measurements.csv")

measurements = raw_input.readlines()
measurements = [int(measurement.rstrip("\n")) for measurement in measurements]

raw_input.close()

increased_measures = 0
this_depth = 0

for depth in measurements:

    if this_depth != 0:
        if this_depth < depth:
            increased_measures += 1

    this_depth = depth


print(f"Total increases: {increased_measures}")
