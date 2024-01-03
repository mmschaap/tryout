#
# main
#
# Solve a Sudoku puzzle
# by Martin Schaap
#
sudoku = [[[['.' for _ in range( 3 )] for _ in range( 3 )] for _ in range( 3 )] for _ in range( 3 )]
is_not = [[[[['X' for _ in range( 9 )] for _ in range( 3 )] for _ in range( 3 )] for _ in range( 3 )] for _ in range( 3 )]

from get_input import get_input

get_input( sudoku )
