import itertools


with(open("segments.txt", "r") as raw_signals):
   lines = raw_signals.readlines()
   inputs, outputs = map(list, zip(*(line.strip().split(" | ") for line in lines)))

# 1, 4, 7, 8
# each contains 2, 4, 3, 7 segments each.
digits = [
    digit
    for digit in itertools.chain.from_iterable(
        [signal.split(" ") for signal in outputs]
    )
    if len(digit) in [2, 3, 4, 7]
]

print(f"Our digits of interest appear {len(digits)} times")
