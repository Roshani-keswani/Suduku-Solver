def solve_sudoku(puzzle):
    def is_valid(row, col, value):
        for i in range(9):
            if puzzle[row][i] == value or puzzle[i][col] == value:
                return False
        sub_row = (row // 3) * 3
        sub_col = (col // 3) * 3
        for i in range(sub_row, sub_row + 3):
            for j in range(sub_col, sub_col + 3):
                if puzzle[i][j] == value:
                    return False
        return True

    def find_empty_cell():
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == '.':
                    return i, j
        return None

    def solve():
        cell = find_empty_cell()
        if cell is None:
            return True
        row, col = cell
        for value in range(1, 10):
            if is_valid(row, col, str(value)):
                puzzle[row][col] = str(value)
                if solve():
                    return True
                puzzle[row][col] = '.'
        return False

    solve()
    return puzzle

#input
puzzle = [ ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]

solved_puzzle = solve_sudoku(puzzle)

for row in solved_puzzle:
    print(row)