import boards

def check_line(line, column):
    num_line = list(possibilities)
    for i in range(9):
        if solved_board[line][i] != 0:
            num_line.remove(solved_board[line][i])
    return num_line
# Iterate over the line, return only the numbers that isnt in the line
    
def check_column(line, column):
    num_column = list(possibilities)
    for i in range(9):
        if solved_board[i][column] != 0:
            num_column.remove(solved_board[i][column])
    return num_column
# Iterate over the column, return only the numbers that inst in the column

def check_block(line, column):
    num_block = list(possibilities)

    if column == 1 or column == 4 or column == 7:
        column -= 1
    if column == 2 or column == 5 or column == 8:
        column -= 2
    if line == 1 or line == 4 or line == 7:
        line -= 1
    if line == 2 or line == 5 or line == 8:
        line -= 2
    
    for i in range(3):
        for j in range(3):
            if solved_board[line][column] != 0:
                num_block.remove(solved_board[line][column])
            column += 1
        column -= 3
        line += 1

    return num_block
# Iterate over the block, return only the numbers that isnt in the block

def find_num(line, column):
    line_opt = check_line(line, column)

    column_opt = check_column(line, column)

    block_opt = check_block(line, column)

    ans = line_opt + column_opt + block_opt
    ans = set(ans)
    ans = list(ans)
# Get all possibilities. Put all in a list and remove duplicate numbers

    answer = []

    for i in ans:
        if i in line_opt and i in column_opt and i in block_opt:
            answer.append(i)
# If answer meet all the criteria, put in answer list

    if len(answer) == 1:
        return int(answer[0])
    return 0
# If has only one possibility of answer, return answer. Else, dont change

def is_complete(board):
    for line in board:
        if 0 in line:
            return False
    return True
# If has 0 in the board, isnt complete

possibilities = (1, 2, 3, 4, 5, 6, 7, 8, 9)

board = boards.hard_board
solved_board = board

while is_complete(solved_board) == False:
    for line in range(9):
        for column in range(9):
            if solved_board[line][column] == 0:
                solved_board[line][column] = find_num(line, column)
# While the board isnt complete, look for answer in every missing space

for line in solved_board:
    print(line)