def checkIndex(board, index): # Returns a true boolean value if the index is between 0 and n-1 included
    if index>=0 and index<board['n']:
        return True
    else:
        return False

def checkRoom(board, row, column): # Returns a true boolean value if the lig and col parameters represent a string of the tray.
    if (row>=0 and row<board['n']) and (column>=0 and column<board['n']):
        return True
    else:
        return False

def getValue(board, row, column): # Returns the value from the coordinate
    if (row>3 or row<0) or (column>3 or column<0):
        return('Erreur')
    return board['tiles'][row*4 + column]

def setValue(board, row, column, val): # Set a value from the coordinate
    if row>3 or row<0 or column>3 or column<0 or val<0:
        return('Erreur')
    board['tiles'][row*4 + column] = val
    return board

def isRoomEmpty(board, row, column): # Check if a cell is free
    if board['tiles'][row*4 + column] != 0:
        return False
    else :
        return True
