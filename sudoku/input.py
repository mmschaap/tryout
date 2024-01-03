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
        # 7 => [2][1] 
        #
        block_row = int( i / 3 )

        for j in range( 0, 9 ):
            block_column = int( j / 3 )
            cell_column = j - int( j / 3 ) * 3
            cell_row = i - int( i / 3 ) * 3

            sudoku[block_row][block_column][cell_row][cell_column] = parsed_line[j]  

    #
    # Check for duplicates in rows and columns
    #
    check_passed = True

    for i in range( 0, 9 ):
        for j in range( 0, 9 ):
            block_column_source = int( i / 3 )  
            block_row_source =    int( j / 3 )
            cell_column_source =  i - int( i / 3 ) * 3
            cell_row_source =     j - int( j / 3 ) * 3

            for k in range( j+1, 9-j ):
                block_column = block_column_source
                block_row =    int( k / 3 )
                cell_column =  cell_column_source
                cell_row =     k - int(  k / 3 ) * 3

                if sudoku[block_row_source][block_column_source][cell_row_source][cell_column_source] != '.' and \
                    sudoku[block_row_source][block_column_source][cell_row_source][cell_column_source] == \
                    sudoku[block_row][block_column][cell_row][cell_column] and check_passed == True:
                    print( "Inconsistent Sudoku specified." )
                    check_passed = False

            if check_passed == True:
                for l in range( i+1, 9-i ):
                    block_column = int( l / 3 )  
                    block_row = block_row_source
                    cell_column = l - int( l / 3 ) * 3
                    cell_row = cell_row_source

                    if sudoku[block_column_source][block_row_source][cell_column_source][cell_row_source] != '.' and \
                        sudoku[block_column_source][block_row_source][cell_column_source][cell_row_source] == \
                        sudoku[block_column][block_row][cell_column][cell_row] and check_passed == True:
                        print( "Inconsistent Sudoku specified." )
                        check_passed = False                        
                        
    #
    # Check for duplicates in a cell of 9 figures
    #
    cell_figures = ['.' for _ in range( 9 )]
    check_passed = True
                    
    for i in range( 0, 3 ):
        for j in range( 0, 3 ):
            if check_passed == True:
                for k in range( 0, 3 ):
                    for l in range( 0, 3 ):
                        cell_figures[ k * 3 + l ] = sudoku[i][j][k][l]

                cell_figures.sort()

                for m in range( 0, 8 ):
                    if cell_figures[ m ] != '.' and cell_figures[ m ] == cell_figures[ m + 1 ] and check_passed == True:
                        print( "Inconsistent Sudoku specified." )
                        check_passed = False