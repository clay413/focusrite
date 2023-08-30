def game_won(row: int, col: int, row_counter: int, col_counter: int) -> bool:
    row_counter[row] -= 1
    col_counter[col] -= 1
    return row_counter[row] == 0 or col_counter[col] == 0

def parse_file(filename: str):
    with open(filename, 'r') as file:
        lines = [line for line in file.read().split('\n') if line.strip()]

    called_nums = [int(n) for n in lines[0].split(',')]

    lines = lines[1:]
    boards = []

    while lines:
        board = [[int(n) for n in lines[i].split()] for i in range(5)]
        boards.append(board)
        lines = lines[5:]

    return called_nums, boards

# Check if board wins and returns calls needed, if it doesn't win, it return infinity
def board_wins(called_nums, board):
    row_counter, col_counter = [5] * 5, [5] * 5

    # Creating key value pairs for each number with the coordinates
    board_nums = {}
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            board_nums[num] = (i, j)

    nums_called = 1
    for number in called_nums:
        if number in board_nums:
            i, j = board_nums[number]
            if game_won(i, j, row_counter, col_counter):
                return nums_called

        nums_called += 1

    return float('inf')

# Part 1
def bingo_p1(filename: str) -> bool:
    called_nums, boards = parse_file(filename)

    return board_wins(called_nums, boards[0]) != float('inf')

# Part 2
def bingo_p2(filename: str) -> int:
    called_nums, boards = parse_file(filename) 

    boards_nums_needed = [board_wins(called_nums, board) for board in boards]

    # Returning index of board with fewest numbers of calls needed and -1 if no board wins
    min_calls = min(boards_nums_needed)

    return boards_nums_needed.index(min_calls) if min_calls != float('inf') else -1