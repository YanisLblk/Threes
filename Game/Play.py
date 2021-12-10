import sys
from os.path import dirname, abspath
from Tiles.TilesMoves import getNextAleaTiles, putNextTiles, getNumberEmptyRooms

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

def initPlay(): # Creation of a dictionary indicating the number of free tiles, their value and the size of the the board
    board = {
        'n' : 4 ,
        'numberFreeTiles' : 16 ,
        'tiles' : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]
    }
    return board

def isGameOver(board): # Check if the player lost the game according to the number of free tiles
    i = 0
    while i<len(board['tiles']):
        if board['tiles'][i]==0:
            return False
        i += 1
    return True

def getScore(board): # Return the player's score by summing the board values
    score = 0
    i = 0
    while i<len(board['tiles']):
        score += board['tiles'][i]
        i += 1
    return score

def createNewPlay(): # Creates a dictionary with the initial dictionary, the next tile and the score
    initialBoard = initPlay()
    test = getNextAleaTiles(initialBoard, 'init')
    print(test)
    putNextTiles(initialBoard, test)
    play = { 'board' : initialBoard,
     'nextTile' : None,
     'score' : getScore(initialBoard) }
    getNumberEmptyRooms(play['board'])
    return play
