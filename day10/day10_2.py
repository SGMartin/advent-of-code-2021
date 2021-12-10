import numpy as np

with open("subsystem.txt", "r") as raw_lines:
    lines_to_check = [line.strip() for line in raw_lines.readlines()]


opening_chunks = {"}":"{",
                "]":"[",
                ">":"<",
                ")":"("}

closing_chunks = {"{":"}",
                "[":"]",
                "<":">",
                "(":")"}

scoring = {")": 1, "]": 2, "}": 3, ">": 4}

lines_scores = []

def get_scoring(chars):
    score = 0
    for char in chars:
        score = 5 * score + scoring[char]

    return score

# Reuse the previous answer to get corrupt lines
for line in lines_to_check:
    cur_block = []
    is_incomplete  = True
    for char in line:
        # keys = valid closing chars
        if char in opening_chunks.keys():
            if len(cur_block) == 0:
                ## Missing opening char?
                is_incomplete = False
                break

            this_char = cur_block.pop()

            if this_char != opening_chunks[char]:
                # Missmatching opening/closing
                is_incomplete = False
                break
        else:
            cur_block.append(char)

    if not is_incomplete: # Skip the line as it is corrupt
        continue

        # If we arrive here, the line is indeed incomplete
        # and the cur_block list contains all open blocks
    closing_blocks = [closing_chunks[char] for char in reversed(cur_block)]
    lines_scores.append(get_scoring(closing_blocks))


median_score = int(round(np.median(lines_scores)))

print(f"Median score is {median_score}")





