#
# Function get_input
#
# Solve a Sudoku puzzle
# by Martin Schaap
#
from helpers import getRightLineInput, hasDuplicatesInRowsOrColumns, hasDuplicatesInBlocks, provideTestData, parseLine

use_test_data = True

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