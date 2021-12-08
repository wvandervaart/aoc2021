path = "input"
def parse_data(path): 
    with open(path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    nums = [int(num) for num in lines[0].split(",")]
    boards = []
    flags = []

    k = 2
    while k + 5 <= len(lines):
        boards.append([[int(cell) for cell in row.split()] for row in lines[k:k+5]])
        flags.append([[0 for cell in row.split()] for row in lines[k:k+5]])
        k += 6

    return boards, nums

flatten = lambda board: [i for row in board for i in row]
calculate_score = lambda board, sequence: sum(set(flatten(board)) - set(sequence))

def get_rows_cols(board): 
    rows = [i for i in board]
    cols = [list(tupp) for tupp in zip(*board)]
    return rows,cols

def check_board(board, sequence): 
    rows, cols = get_rows_cols(board) 
    rows.extend(cols) # lol 
    for i in rows: 
        if all([x in sequence for x in i]): 
            return True 
    return False

boards, nums = parse_data(path)
def solve_puzzle(boards, nums): 
    sequence = []
    solved_boards = []
    board_idx = []
    for i,n in enumerate(nums): 
        sequence.append(n) 
        for idx, board in enumerate(boards):  
            if idx not in board_idx and check_board(board, sequence): 
                solved_boards.append((calculate_score(board, sequence), i, n)) 
                board_idx.append(idx)
    return solved_boards

part1, part2 = solve_puzzle(boards, nums)[0], solve_puzzle(boards, nums)[-1] 
part1_ans = part1[0]*part1[2]
part2_ans = part2[0]*part2[2]
print("part1: " + str(part1_ans) + ":: part2: " + str(part2_ans))
