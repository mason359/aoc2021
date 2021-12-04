from aocutils import get_raw

def problem1():
    (nums, boards, sums) = parse_boards()
    for num in nums:
        for i, board in enumerate(boards):
            if contains_num(board, num):
                sums[i] -= num
                if board_is_winner(board):
                    return sums[i] * num

def problem2():
    (nums, boards, sums) = parse_boards()
    for num in nums:
        for i, board in reversed(list(enumerate(boards))):
            if contains_num(board, num):
                sums[i] -= num
                if board_is_winner(board):
                    if len(boards) == 1:
                        return sums[0] * num
                    del sums[i]
                    del boards[i]

def parse_boards():
    [nums, *boards] = get_raw(4).split('\n\n')
    nums = [int(num) for num in nums.split(',')]
    boards = [[[int(num) for num in row.split()] for row in board.splitlines()] for board in boards]
    sums = [sum([sum(row) for row in board]) for board in boards]
    return (nums, boards, sums)

def contains_num(board, drawn):
    for r, row in enumerate(board):
        for c, num in enumerate(row):
            if num == drawn:
                board[r][c] = None
                return True
    return False

def board_is_winner(board):
    rows = any([all([num is None for num in row]) for row in board])
    cols = any([all([board[r][c] is None for r in range(5)]) for c in range(5)])
    return rows or cols