from tkinter import *
import sys
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

N = "N : Commencer une nouvelle partie"
L = 'L : Charger une Partie'
S = 'S : Sauvegarder la partie en cours'
C = 'C : Reprendre la partie en cours'
Q = 'Q : Terminer le jeu'


def getUserMove():
    direction = ''
    while direction != "h" and direction != "b" and direction != "g" and direction != "d" and direction != "m":
        print("Les direction du plateau : haut(h), bas(b), gauche(g), droite(d)")
        print('pour ouvrir le menu:(m)')
        direction = str(input())
        direction = direction.lower()
    return direction

def getUserMenu(play):
    choix = ''
    if play is None:
        while choix != "N" and choix != "L": # Choix au debut de partie
            print(N)
            print(L)
            choix = str(input())
            choix = choix.upper() # Transformer les carctères en majuscule.
    elif play is not None:
        while choix != "S" and choix != "C" and choix != "Q": # Choix durant la partie si elle est déjâ en cours.
            print(S)
            print(C)
            print(Q)
            choix = str(input())
            choix = choix.upper() # Transformer les carctères en majuscule.
    return choix