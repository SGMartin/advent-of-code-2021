import pandas as pd

raw_binay = open("diagnostics.txt", "r")
instructions = [pos.rstrip("\n") for pos in raw_binay]
raw_binay.close()

instructions_bits = [list(inst) for inst in instructions]

report = pd.DataFrame(instructions_bits)

# cast to numeric
report = report.apply(pd.to_numeric, axis=1)
most_freq = report.sum(axis=0)

gamma_rate = []
epsilon_rate = []

for sum_bits in most_freq:
    if sum_bits > (len(report.index) / 2):
        gamma_rate.append("1")
        epsilon_rate.append("0")
    else:
        gamma_rate.append("0")
        epsilon_rate.append("1")

gamma_rate = int("".join(gamma_rate), 2)
epsilon_rate = int("".join(epsilon_rate), 2)

power_con = gamma_rate * epsilon_rate

print(
    f"Gamma rate is:{gamma_rate}, epsilon rate is:{epsilon_rate}. Power is {power_con}"
)
