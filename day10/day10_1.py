with open("subsystem.txt", "r") as raw_lines:
    lines_to_check = [line.strip() for line in raw_lines.readlines()]


legal_chunks = {"}":"{",
                "]":"[",
                ">":"<",
                ")":"("}

illegal_characters = []

scores = {")": 3, "]": 57, "}": 1197, ">": 25137}


for line in lines_to_check:
    cur_block = []
    for char in line:
        # keys = valid closing chars
        if char in legal_chunks.keys():
            if len(cur_block) == 0:
                ## Missing opening char?
                illegal_characters.append(char)
                break

            this_char = cur_block.pop()

            if this_char != legal_chunks[char]:
                # Missmatching opening/closing
                illegal_characters.append(char)
                break
        else:
            cur_block.append(char)


score = sum([scores[char] for char in illegal_characters])

print(f"Total score: {score}")
