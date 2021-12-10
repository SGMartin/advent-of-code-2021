from collections import Counter


def get_support_system(lf_system: str) -> str:

    with open("diagnostics.txt", "r") as raw_diagnostics:
        bit_rows = raw_diagnostics.readlines()

    if lf_system == "oxygen":
        lf_system = 1
    else:
        lf_system = 0

    for i in range(12):  # each row has 12 bits
        counter = Counter(bit[i] for bit in bit_rows)
        bit_rows = [
            bit
            for bit in bit_rows
            if (bit[i] == "1")
            != (counter["1"] >= counter["0"])
            ^ lf_system  # The truth table of A XOR B shows that it outputs true whenever the inputs differ:
        ]
        if len(bit_rows) == 1:
            return bit_rows[0]


oxygen = int(get_support_system("oxygen"), 2)
co2 = int(get_support_system("co2"), 2)

print(f"Oxygen is: {oxygen}")
print(f"co2 is: {co2}")
print(f"Life support: {oxygen*co2}")
