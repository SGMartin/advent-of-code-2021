with open("segments.txt", "r") as raw_signals:
    lines = raw_signals.readlines()
    inputs, outputs = map(list, zip(*(line.strip().split(" | ") for line in lines)))

decoded_values = []

for id, signal in enumerate(inputs):
    print(f"Decoding signal {id}")

    #  0000
    # 6    1
    # 6    1
    #  2222
    # 5    3
    # 5    3
    #  4444

    key_signals = {}

    segments = signal.split()

    # Find the ids for digits 1,4,7,8
    # each contains 2, 4, 3, 7 segments each.
    unique_digits = [digit for digit in segments if len(digit) in [2, 3, 4, 7]]

    # Sort them by len
    # Now the first one is 1, the second is 7, the third is 4 and the last one is 8
    unique_digits = sorted(unique_digits, key=len)

    # Sort segments DESCENDING
    segments.sort(key=len, reverse=True)

    # Store keys to decode 1,7,4,8
    for idx in [1, 7, 4, 8]:
        key_signals[idx] = unique_digits[0]

        # Update both unique digits and the segment list
        segments.pop(segments.index(unique_digits[0]))
        unique_digits.pop(0)

    six_len_segments = segments[:3]
    five_len_segments = segments[3:6]

    # Only three numbers pos: 0, 6, 9
    for segment in six_len_segments:
        # Six is the only one which does not contain one
        if not all([num in segment for num in key_signals[1]]):
            key_signals[6] = segment
        # Full overlap with 4: only 9
        elif all([num in segment for num in key_signals[4]]):
            key_signals[9] = segment
        # 0 is the only one left
        else:
            key_signals[0] = segment

    # Only three numbers pos: 2, 3, 5
    for segment in five_len_segments:
        # If it contains 7, it must be 3
        if all([num in segment for num in key_signals[7]]):
            key_signals[3] = segment
        elif all([num in key_signals[9] for num in segment]):
            key_signals[5] = segment
        else:
            key_signals[2] = segment

    ## Sort unique keys alphabetically
    for key, value in key_signals.items():
        key_signals[key] = "".join(sorted(value))

    ## Now decode the output and store it
    secret_numbers = outputs[id]  # input output ids are matched
    secret_numbers = ["".join(sorted(num)) for num in secret_numbers.split(" ")]

    translated_num = ""

    for coded_num in secret_numbers:
        for key in key_signals.keys():
            if coded_num == key_signals[key]:
                translated_num = "".join([translated_num, str(key)])

    print(translated_num)
    decoded_values.append(int(translated_num))


print(f"The sum of all numbers is {sum(decoded_values)}")
