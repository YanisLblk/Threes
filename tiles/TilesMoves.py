from random import randint
from tiles.TilesAcces import setValue, isRoomEmpty

def getNumberEmptyRooms(board): # Update the dictionary with the free number of boxes
    emptyTile = 0
    i = 0
    while i<len(board['tiles']):
        if board['tiles'][i]==0:
            emptyTile += 1
        i += 1
    board['numberFreeTiles'] = emptyTile
    return board['numberFreeTiles']

def getNextAleaTiles(board, stateGame): # Checks the available place for tiles during the game
    dicoTiles={'stateGame' : stateGame}
    
    tile=False
    while tile!=True:
        row = randint(0, 3)
        column = randint(0, 3)
        tile = isRoomEmpty(board, row, column)
        
        if stateGame=='inGame':
            dicoTiles['0'] = {'value': randint(
                1, 3), 'row': row, 'column': column}
        elif stateGame=='init':
            dicoTiles['0'] = {'value': randint(
                1, 2), 'row': row, 'column': column}
        
            tile = False
            while tile != True:
                row = randint(0, 3)
                column = randint(0, 3)
                tile = isRoomEmpty(board, row, column)
            dicoTiles['1'] = {'value': randint(
                1, 2), 'row': row, 'column': column}
    
    if stateGame=='inGame' or stateGame=='init':
        dicoTiles['check'] = True
    else:
        dicoTiles['check'] = False
    
    return dicoTiles

def putNextTiles(board, tiles):# Puts the values in the available tiles
    if tiles['check']==True:
        if tiles['stateGame'] == 'inGame':
            tile = tiles['0']
            newBoard = setValue(
                board, tile['row'], tile['column'], tile['value'])
        elif tiles['stateGame'] == 'init':
            tile1 = tiles['0']
            tile2 = tiles['1']
            newBoard = setValue(
                board, tile1['row'], tile1['column'], tile1['value'])
            newBoard = setValue(
                board, tile2['row'], tile2['column'], tile2['value'])
        else:
            return('Erreur')
        return newBoard
    elif tiles['check'] == False:
        return False

def rowPack(board, numberRow, start, sense): # rowPack shifts one row from the board
    table = board['tiles']
    if sense == 0:
        while start > 0:
            table[numberRow*4+start] = table[numberRow*4+start-1]
            start -= 1
    elif sense == 1:
        while start < 3:
            table[numberRow*4+start] = table[numberRow*4+start+1]
            start += 1
    table[numberRow*4+start] = 0
    return board


# columnPack shift a column from the board
def columnPack(board, numberColumn, start, sense):
    table = board['tiles']
    if sense == 0:
        while start>0:
            table[start*4+numberColumn] = table[(start-1)*4+numberColumn]
            start -= 1
    elif sense == 1:
        while start < 3:
            table[start*4+numberColumn] = table[(start+1)*4+numberColumn]
            start += 1
    table[start*4+numberColumn] = 0
    return board

def rowMove(board, numberRow, sense): # Manage the increment of board values during the horizontal offset
    table = board['tiles']
    if sense == 0:
        start = 3
        while start > 0:
            if table[numberRow*4+start] == 0:
                rowPack(board, numberRow, start, sense)
                return board

            elif table[numberRow*4+start]==table[numberRow*4+start-1] and table[numberRow*4+start]>2: # Les valeurs identiques et supérieur à 2 se somme.
                table[numberRow*4+start] += table[numberRow*4+start-1]
                table[numberRow*4+start-1] = 0

            elif (table[numberRow*4+start]==1 and table[numberRow*4+start-1]==2) or (table[numberRow*4+start]==2
            and table[numberRow*4+start-1]==1): #Les valeurs 1 et 2 se somme.
                table[numberRow*4+start] += table[numberRow*4+start-1]
                table[numberRow*4+start-1] = 0
            start -= 1
    elif sense == 1: #Décalage à gauche.
        start = 0
        while start<3:
            if table[numberRow*4+start] == 0:
                rowPack(board, numberRow, start, sense)
                return board

            elif table[numberRow*4+start] == table[numberRow*4+start+1] and table[numberRow*4+start]>2: # Les valeurs identiques et supérieur à 2 se somme.
                table[numberRow*4+start] += table[numberRow*4+start+1]
                table[numberRow*4+start+1] = 0

            elif (table[numberRow*4+start]==1 and table[numberRow*4+start+1]==2) or (table[numberRow*4+start]==2
            and table[numberRow*4+start+1]==1): #Les valeurs 1 et 2 se somme.
                table[numberRow*4+start] += table[numberRow*4+start+1]
                table[numberRow*4+start+1] = 0
            start += 1
    return board


def columnMove(Board, numberColumn, sense): # Manages the increment of board values during vertical offset
    table = Board['tiles']
    if sense == 0:
        start = 3
        while start>0:
            if table[start*4+numberColumn] == 0:
                columnPack(Board, numberColumn, start, sense)
                return Board

            elif table[start*4+numberColumn] == table[(start-1)*4+numberColumn] and table[start*4+numberColumn]>2:
                table[start*4+numberColumn] += table[(start-1)*4+numberColumn]
                table[(start-1)*4+numberColumn] = 0

            elif (table[start*4+numberColumn]==1 and table[(start-1)*4+numberColumn]==2) or (table[start*4+numberColumn]==2
            and table[(start-1)*4+numberColumn]==1):
                table[start*4+numberColumn] += table[(start-1)*4+numberColumn]
                table[(start-1)*4+numberColumn] = 0
            start -= 1
    elif sense == 1:
        start = 0
        while start<3:
            if table[start*4+numberColumn] == 0:
                columnPack(Board, numberColumn, start, sense)
                return Board

            elif table[start*4+numberColumn] == table[(start+1)*4+numberColumn] and table[start*4+numberColumn]>2:
                table[start*4+numberColumn] += table[(start+1)*4+numberColumn]
                table[(start+1)*4+numberColumn] = 0

            elif (table[start*4+numberColumn]==1 and table[(start+1)*4+numberColumn]==2) or (table[start*4+numberColumn]==2
            and table[(start+1)*4+numberColumn]==1):
                table[start*4+numberColumn] += table[(start+1)*4+numberColumn]
                table[(start+1)*4+numberColumn] = 0

            start += 1
    return Board

def rowsMove(Board, sense): # Shift of the whole board horizontally
    numberRow = 0
    while numberRow<4:
        row = rowMove(Board, numberRow, sense)
        numberRow += 1
    return row

def columnsMove(Board, sense): # Shift of the whole board vertically
    numberColumn = 0
    while numberColumn<4:
        column = columnMove(Board, numberColumn, sense)
        numberColumn += 1
    return column

def playMove(Board, sense): # Configures keyboard entries for user
	if sense == 'b':
		columnsMove(Board, 0)
	elif sense == 'h':
		columnsMove(Board, 1)
	elif sense == 'g':
		rowsMove(Board, 1)
	elif sense == 'd':
		rowsMove(Board, 0)
	return Board
