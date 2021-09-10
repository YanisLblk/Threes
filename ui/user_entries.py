from tkinter import *
import sys
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)
from tiles.tiles_moves import play_move

N = "N : Commencer une nouvelle partie"
L = 'L : Charger une Partie'
S = 'S : Sauvegarder la partie en cours'
C = 'C : Reprendre la partie en cours'
Q = 'Q : Terminer le jeu'

# Fonction partie 3
def get_user_move():
    direction = ''
    while direction != "h" and direction != "b" and direction != "g" and direction != "d" and direction != "m":
        print("Les direction du plateau : haut(h), bas(b), gauche(g), droite(d)")
        print('pour ouvrir le menu:(m)')
        direction = str(input())
        direction = direction.lower()
    return direction

def get_user_menu(partie):
    choix = ''
    if partie is None:
        while choix != "N" and choix != "L": # Choix au debut de partie
            print(N)
            print(L)
            choix = str(input())
            choix = choix.upper() # Transformer les carctères en majuscule.
    elif partie is not None:
        while choix != "S" and choix != "C" and choix != "Q": # Choix durant la partie si elle est déjâ en cours.
            print(S)
            print(C)
            print(Q)
            choix = str(input())
            choix = choix.upper() # Transformer les carctères en minuscule.
    return choix

#def get_user_menuV2(partie):
    #if partie is None :

