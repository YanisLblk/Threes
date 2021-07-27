import json
import sys

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from tiles.game.play import get_score
from tiles.tiles_moves import get_next_alea_tiles, play_move, is_room_empty, set_value, put_next_tiles, get_nb_empty_rooms
from ui.user_entries import get_user_move
from ui.play_display import medium_display

datapath = d+"\\tiles\game\game_saved.json"
# Fonction de la partie 3

#encours = create_new_play()

def cycle_play(partie): # Fonction qui permet de maintenir la partie en cours.
    plateau = partie['plateau']
    play = True
    while play != False:
        medium_display(plateau)
        tile = partie['next_tile']
        if tile is None:
            tile=get_next_alea_tiles(plateau, 'encours')

        if tile['check']==False:
            partie['score']=get_score(plateau)
            print('score final:',partie['score'])
            return True

        val = tile['0']
        print('La prochaine tuile :', val['val'])
        direction = get_user_move()
        if direction=='m':
            return False

        play_move(plateau, direction)

        if is_room_empty(plateau, val['lig'], val['col']) == False:
            tile2 = get_next_alea_tiles(plateau, 'encours')
            val2 = tile2['0']
            set_value(plateau,val2['lig'],val2['col'],val['val'])
        else:
            put_next_tiles(plateau,tile)
        if get_nb_empty_rooms(plateau) < 1:
            return('Game Over !')
        partie['next_tile']=get_next_alea_tiles(plateau,'encours')
        play = False

def save_game(partie):
    datas = partie
    with open(datapath, "w") as file:
        json.dump(datas, file)

def restore_game():
    with open(datapath, "r") as file:
        game_save = json.load(file)
        return game_save
