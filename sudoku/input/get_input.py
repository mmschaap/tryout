#
# Function get_input
#
# Solve a Sudoku puzzle
# by Martin Schaap
#

def get_input( sudoku ):
    for i in range( 0, 9 ):
        check_passed = False

        while not check_passed:
            check_passed = True
        
            line = input( "Enter line " + str( i + 1 ) + " of the Sudoku: " )

            if line.count( ',' ) != 8:
                print( "9 individual characters (from 1 to 9 or .) seperated by commas expected." )
                check_passed = False
                continue
            elif line.count( ',' ) == 8:
                parsed_line = line.replace( " ", "" ).split( "," )
                print( parsed_line )

                for parsed_char in parsed_line:
                    if ( len( parsed_char ) != 1 or not any(True for char in parsed_char if char in '0123456789.' ) ) and check_passed == True:
                        print( "9 individual characters (from 1 to 9 or .) seperated by commas expected." )
                        check_passed = False
                    else:
                        pass
                else:
                    break