# Lees een inputregel van het scherm
def getRightLineInput(rowIndex:int)->str:
    line = ""

    ## True + True = 2
    while len(line)==0 or line.count(',')!=8 or sum([i in "1234567890." for i in line.split(",")]) < 9:
        line = input(f"Enter line {rowIndex + 1} of the Sudoku: ")
    
    return line.replace(" ","").split(",")

## Geeft alle waardes uit de kolom terug die geen '.' zijn
def getColumnNumbers(sudoku,block_column,cell_column):
    return [sudoku[int( i / 3 )][block_column][i - int( i / 3 ) * 3][cell_column] \
            for i in range(9) if sudoku[int( i / 3 )][block_column][i - int( i / 3 ) * 3][cell_column] != '.']

## Geeft alle waardes uit de rij terug die geen '.' zijn
def getRowNumbers(sudoku,block_row,cell_row):
    return [sudoku[block_row][int( i / 3 )][cell_row][i - int( i / 3 ) * 3] \
            for i in range(9) if sudoku[block_row][int( i / 3 )][cell_row][i - int( i / 3 ) * 3] != '.']

## Geeft alle waardes uit het blok terug die geen '.' zijn
def getBlockNumbers(sudoku,block_row,block_column):
    return [sudoku[block_row][block_column][int( i / 3 )][i - int( i / 3 ) * 3] \
            for i in range(9) if sudoku[block_row][block_column][int( i / 3 )][i - int( i / 3 ) * 3] != '.']

# Controleer of er in de input duplicaten zitten in de kolommen en de rijen
def hasDuplicatesInRowsOrColumns(sudoku):
    for i in range(9):
        column = getColumnNumbers(sudoku, int( i / 3 ), i - int( i / 3 ) * 3)
        ## set geeft unieke entries in een lijst
        if len(column) != len(set(column)):
            return True
        
        row = getRowNumbers(sudoku, int( i / 3 ), i - int( i / 3 ) * 3)
        if len(row) != len(set(row)):
            return True
    return False

# Controleer of er in de input duplicaten zitten in een blok
def hasDuplicatesInBlocks(sudoku):
    for i in range( 3 ):
        for j in range( 3 ):
            block = getBlockNumbers(sudoku, i, j)
            ## set geeft unieke entries in een lijst
            if len(block) != len(set(block)):
                return True
    return False

# Verwerk een inputregel
def parseLine(sudoku, rowIndex, inputLine):
    #
    # 0 => [0][0] 
    # 2 => [0][2] 
    # 7 => [2][1] 
    #
    block_row = int( rowIndex / 3 ) # rowIndex//3 => int devide, (1//3 = 0, 2//3 = 0 3//3 = 1)
    cell_row = rowIndex - int( rowIndex / 3 ) * 3 # rowIndex%3 werkt ook

    for j in range( 9 ):
        block_column = int( j / 3 ) # j//3 => int devide
        cell_column = j - int( j / 3 ) * 3 # j%3 werkt ook

        sudoku[block_row][block_column][cell_row][cell_column] = inputLine[j]
    return sudoku

# Stel een test sodoku ter beschikking, dan is het niet nodig om deze in te voeren.
def provideTestData(sudoku):
    sudoku = parseLine( sudoku=sudoku, rowIndex=0, inputLine="1,.,.,.,8,9,.,.,7".split(",") )
    sudoku = parseLine( sudoku=sudoku, rowIndex=1, inputLine="4,8,.,.,.,7,.,.,.".split(",") )
    sudoku = parseLine( sudoku=sudoku, rowIndex=2, inputLine=".,6,7,.,2,.,4,8,9".split(",") )
    sudoku = parseLine( sudoku=sudoku, rowIndex=3, inputLine="2,.,.,.,.,8,6,7,5".split(",") )
    sudoku = parseLine( sudoku=sudoku, rowIndex=4, inputLine="3,.,.,6,.,.,2,1,.".split(",") )
    sudoku = parseLine( sudoku=sudoku, rowIndex=5, inputLine="6,7,5,.,.,.,3,9,8".split(",") )
    sudoku = parseLine( sudoku=sudoku, rowIndex=6, inputLine="8,3,1,.,4,2,.,.,6".split(",") )
    sudoku = parseLine( sudoku=sudoku, rowIndex=7, inputLine="9,.,.,7,.,.,8,.,1".split(",") )
    sudoku = parseLine( sudoku=sudoku, rowIndex=8, inputLine=".,.,6,8,3,1,.,.,2".split(",") )
    return sudoku