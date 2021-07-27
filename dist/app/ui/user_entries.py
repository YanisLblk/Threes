import sys
sys.path.insert(0, 'C:\\Users\\yanis\\Documents\\iut_informatique\\jeu_threes')
from tiles.tiles_moves import play_move

# Fonction partie 3

def get_user_move():
    direction = ''
    while direction != "h" and direction != "b" and direction != "g" and direction != "d" and direction != "m":
        print("Les direction du plateau : haut(h), bas(b), gauche(g), droite(d)")
        print('pour ouvrir le menu:(m)')
        direction = str(input())
        direction = direction.lower()
    return direction


def get_user_menu2(partie):
    print('Taper la lettre:')
    print('N : Commencer une nouvelle partie')
    print('L : Charger une Partie')
    print('S : Sauvegarder la partie en cours')
    print('C : Reprendre la partie en cours')
    print('Q : Terminer le jeu')
    choix = ''
    while choix!='N' or choix!='L' or choix!='S' or choix!='C' or choix!='Q':
        choix = str(input())
        if choix == 'n' or choix == 'N':
            return('N')
        elif choix == 'l' or choix == 'L':
            return('L')
        elif choix == 's' or choix == 'S':
            return('S')
        elif choix == 'c' or choix == 'C':
            return('C')
        elif choix == 'q' or choix == 'Q':
            return('Q')
        else:
            print('Veuiller choisir les lettres proposées.')

def get_user_menu(partie):
    choix = ''
    if partie is None:
        while choix != "N" and choix != "L": # Choix au debut de partie
            print('N : Commencer une nouvelle partie')
            print('L : Charger une Partie')
            choix = str(input())
            choix = choix.upper() # Transformer les carctères en majuscule.
    elif partie is not None:
        while choix != "S" and choix != "C" and choix != "Q": # Choix durant la partie si elle est déjâ en cours.
            print('S : Sauvegarder la partie en cours')
            print('C : Reprendre la partie en cours')
            print('Q : Terminer le jeu')
            choix = str(input())
            choix = choix.upper() # Transformer les carctères en minuscule.
    return choix
