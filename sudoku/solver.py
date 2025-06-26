#
# main
#
# Solve a Sudoku puzzle
# by Martin Schaap
#
sudoku = [[[['.' for _ in range( 3 )] for _ in range( 3 )] for _ in range( 3 )] for _ in range( 3 )]
can_be = [[[[[range( 1,9 )] for _ in range( 3 )] for _ in range( 3 )] for _ in range( 3 )] for _ in range( 3 )]

from input import get_input
from process import process_sudoku

get_input( sudoku )

process_sudoku( sudoku, can_be )