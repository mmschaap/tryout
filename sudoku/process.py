#
# Function get_input
#
# Solve a Sudoku puzzle
# by Martin Schaap
#
from input import print_sudoku
from display import sudoku_to_html

def process_sudoku( sudoku, can_be ):
    solve_sudoku(sudoku)
 
    # Display the sudoku before solving
    print("Sudoku after solving:")
    print_sudoku(sudoku)
    # Display solved sudoku in browser
    sudoku_to_html(sudoku)
    return

def is_valid(sudoku, block_row, block_col, cell_row, cell_col, num):
    num = str(num)
    # Check row
    for bc in range(3):
        for cc in range(3):
            if sudoku[block_row][bc][cell_row][cc] == num:
                return False
    # Check column
    for br in range(3):
        for cr in range(3):
            if sudoku[br][block_col][cr][cell_col] == num:
                return False
    # Check 3x3 block
    for cr in range(3):
        for cc in range(3):
            if sudoku[block_row][block_col][cr][cc] == num:
                return False
    return True

def solve_sudoku(sudoku):
    for block_row in range(3):
        for block_col in range(3):
            for cell_row in range(3):
                for cell_col in range(3):
                    if sudoku[block_row][block_col][cell_row][cell_col] == ".":
                        for num in range(1, 10):
                            if is_valid(sudoku, block_row, block_col, cell_row, cell_col, num):
                                sudoku[block_row][block_col][cell_row][cell_col] = str(num)
                                if solve_sudoku(sudoku):
                                    return True
                                sudoku[block_row][block_col][cell_row][cell_col] = "."
                        return False
    return True