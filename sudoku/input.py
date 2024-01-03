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

                for parsed_char in parsed_line:
                    if ( len( parsed_char ) != 1 or not any(True for char in parsed_char if char in '0123456789.' ) ) and check_passed == True:
                        print( "9 individual characters (from 1 to 9 or .) seperated by commas expected." )
                        check_passed = False
                    else:
                        pass
            else:
                break

        #
        # 0 => [0][0] 
        # 2 => [0][2] 
        # 7 => [3][2] 
        #
        block_column = int( i / 3 )  
        block_row = i - int( i / 3 ) * 3

        for j in range( 0, 9 ):
            cell_column = int( j / 3 )  
            cell_row = j - int( j / 3 ) * 3

            sudoku[block_column][block_row][cell_column][cell_row] = parsed_line[j]  

    #
    # Check for duplicates
    #
    check_passed = True

    for i in range( 0, 9 ):
        block_column_source = int( i / 3 )  
        block_row_source = i - int( i / 3 ) * 3 
        for j in range( 0, 9 ):
            cell_column_source = int( j / 3 )  
            cell_row_source = j - int( j / 3 ) * 3

            for k in range( i, 9-i ):
                block_column = int( k / 3 )  
                block_row = k - int( k / 3 ) * 3 
                cell_column = cell_column_source
                cell_row = ( block_row_source + k ) - int( ( block_row_source + k ) / 3 ) * 3

                if sudoku[block_column_source][block_row_source][cell_column_source][cell_row_source] != '.' and \
                    sudoku[block_column_source][block_row_source][cell_column_source][cell_row_source] == \
                    sudoku[block_column][block_row][cell_column][cell_row] and check_passed == True:
                    print( "Inconsistent Sudoku specified." )
                    check_passed = False

            if check_passed == True:
                for l in range( i, 9-i ):
                    block_column = int( l / 3 )  
                    block_row = l - int( l / 3 ) * 3 
                    cell_column = int( block_column_source + l / 3 )  
                    cell_row = cell_row_source

                    if sudoku[block_column_source][block_row_source][cell_column_source][cell_row_source] != '.' and \
                        sudoku[block_column_source][block_row_source][cell_column_source][cell_row_source] == \
                        sudoku[block_column][block_row][cell_column][cell_row] and check_passed == True:
                        print( "Inconsistent Sudoku specified." )
                        check_passed = False                        
                        