#
# Function get_input
#
# Solve a Sudoku puzzle
# by Martin Schaap
#
from helpers import getRightLineInput, hasDuplicatesInRowsOrColumns, hasDuplicatesInBlocks, provideTestData, parseLine

use_test_data = True

def print_sudoku(sudoku):
    for row in range(9):
        line = []
        block_row = row // 3
        cell_row = row % 3
        for col in range(9):
            block_col = col // 3
            cell_col = col % 3
            line.append(sudoku[block_row][block_col][cell_row][cell_col])
        print(" ".join(line))

def get_input( sudoku ):
    if use_test_data == False:
        for i in range( 9 ):
            entered_line = getRightLineInput( rowIndex=i )
            
            sudoku = parseLine( sudoku=sudoku, rowIndex=i, inputLine=entered_line )   
    else:
        sudoku = provideTestData(sudoku)

    #
    # Check for duplicates in rows and columns
    #
    if hasDuplicatesInRowsOrColumns(sudoku):
        print( "Inconsistent Sudoku specified." )
    else:
        if hasDuplicatesInBlocks(sudoku):
            print( "Inconsistent Sudoku specified." )

    # Display the sudoku before solving
    print("Sudoku before solving:")
    print_sudoku(sudoku)
    
