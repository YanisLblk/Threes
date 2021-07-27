import sys
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from tiles_moves import get_next_alea_tiles, put_next_tiles, get_nb_empty_rooms

# Fonction de la partie 1

def init_play(): # Création d'un dictionnaire indiquant le nombre de case libre, leur valeur ainsi que la taille du plateau.
    plateau = {
        'n' : 4 ,
        'nb_cases_libres' : 16 ,
        'tiles' : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]
    }
    return plateau

def is_game_over(plateau): # Vérifie si le joueur à perdu la partie en fonction du nombre de case libre.
    tab = plateau['tiles']
    i = 0
    while i<len(tab):
        if tab[i]==0: # Si une valeur du tableau est égal à 0 alors la fonction retourne False..
            return False
        i += 1
    return True

def get_score(plateau): # Retourne le score du joueur en faisant la sommes des valeur de plateau.
    tab = plateau['tiles']
    score = 0
    i = 0
    while i<len(tab):
        score += tab[i]
        i += 1
    return score # Retourne la somme de tout les valeurs du tableau

# #######################################################################################################
# #######################################################################################################

# Fonction de la partie 3

def create_new_play(): # Crée un dictionnaire avec le dictionnaire initial, la prochaine tuile et le score.
    p = init_play()
    put_next_tiles(p, get_next_alea_tiles(p, 'init'))
    play = { 'plateau' : p ,
     'next_tile' : None ,
     'score' : get_score(p) }
    get_nb_empty_rooms(play['plateau'])
    return play
