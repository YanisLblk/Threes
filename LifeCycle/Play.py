import json, sys

from os.path import dirname, abspath
from Game.Play import getScore
from Tiles.TilesMoves import getNextAleaTiles, playMove, isRoomEmpty, setValue, putNextTiles, getNumberEmptyRooms
from ui.UserEntries import getUserMove
from ui.PlayDisplay import display

d = dirname(dirname(abspath(__file__)))
print(d)
sys.path.append(d)
dataPath = d+"\game\GameSaved.json"

def playCycle(dataGame): # Function that keep the game in progress
    board = dataGame['board']
    play = True
    while play != False:
        display(board)
        tile = dataGame['nextTile']
        if tile is None:
            tile = getNextAleaTiles(board, 'inGame')

        if tile['check'] == False:
            dataGame['score'] = getScore(board)
            print('score final : ', dataGame['score'])
            return True

        valueTile=tile['0']
        print('La prochaine tuile :', valueTile['value'])
        direction = getUserMove()
        if direction == 'm':
            return False

        playMove(board, direction)

        if isRoomEmpty(board, valueTile['row'], valueTile['column']) == False:
            tile2 = getNextAleaTiles(board, 'inGame')
            valueTile2 = tile2['0']
            setValue(board, valueTile2['row'],
                     valueTile2['column'], valueTile['value'])
        else:
            putNextTiles(board, tile)
        if getNumberEmptyRooms(board)<1:
            return('Game Over !')
        dataGame['nextTile'] = getNextAleaTiles(board, 'inGame')
        play = False

def saveGame(dataGame): # Save the data of the game in game_saved.json
    with open(dataPath, "w") as file:
        json.dump(dataGame, file)

def restoreGame(): # Load the data from the previous game
    with open(dataPath, "r") as file:
        return json.load(file)