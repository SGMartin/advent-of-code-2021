import itertools
import numpy as np


def get_bingo_board(numbers, boards) -> dict:

    board_scores = {}

    for bid, board in enumerate(boards):
        logic_board = np.full((5, 5), False)
        for nid, number in enumerate(numbers):

            res = number == board
            logic_board = (
                logic_board + res
            )  ## Bolean sum over same size np.arrays = logic |

            is_all_true_rows = logic_board.all(1).any()
            is_all_true_cols = logic_board.all(0).any()

            # Board completed, store its final numb idx
            if is_all_true_cols | is_all_true_rows:
                board_scores[bid] = (nid, logic_board)
                break

    return board_scores


raw_input = open("bingo.txt", "r")

# get the sequence of numbers called
raw_number_seq = raw_input.readline()

# Get all called numbers
numbers_called = [int(num.strip()) for num in raw_number_seq.split(",")]

# Now get all boards as matrix
all_boards = np.loadtxt(raw_input.readlines(), dtype="int16")

raw_input.close()

## Each board is 5x5, so separate them
boards = np.split(ary=all_boards, indices_or_sections=len(all_boards) / 5)


winning_combinations = get_bingo_board(numbers=numbers_called, boards=boards)


## To choose the worst board, let's use max instead of min
best_board_id = max(winning_combinations, key=lambda k: winning_combinations[k][0])

best_number_id = winning_combinations[best_board_id][0]

best_board = boards[best_board_id]
best_logic_board = winning_combinations[best_board_id][1]
last_number = numbers_called[best_number_id]

## final score = sum(unmarked numbers) * last_number
score = sum(best_board[~best_logic_board]) * last_number

print(f"Worst score is: {score}")
