raw_input = open("measurements.csv")

measurements = raw_input.readlines()
measurements = [int(measurement.rstrip("\n")) for measurement in measurements]

raw_input.close()

windows_increase = 0

while len(measurements) > 3:

    first_window = measurements[0] + measurements[1] + measurements[2]
    second_window = measurements[1] + measurements[2] + measurements[3]

    if first_window < second_window:
        windows_increase += 1

    ## get rid of the first element
    measurements.pop(0)

print(f"trio increases: {windows_increase}")
