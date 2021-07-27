# Fonction de la partie 1

def check_indice(plateau, indice): # Retourne une valeur booléene vrai si l'indice est compris entre 0 et n-1 inclus.
    n = plateau['n']
    if indice>=0 and indice<n: # Vérifie que l'indice est celui d'une valeur du tableau.
        return True
    else:
        return False

def check_room(plateau, lig, col): # Retourne une valeur bouléen vrai si les paramètres lig et col représente une cordonnée du plateau.
    n = plateau['n']
    if (lig>=0 and lig<n) and (col>=0 and col<n):
        return True
    else:
        return False

def get_value(plateau, lig, col): # Retourne la valeur du plateau à partir des cordonnés.
    if (lig>3 or lig<0) or (col>3 or col<0):# Retourne un message d'erreur si les paramètres sont faux.
        return('Erreur')
    tab = plateau['tiles']
    valeur = tab[lig*4 + col]
    return valeur

def set_value(plateau, lig, col, val): # Affecte une valeur à des cordonnés dans un plateau.
    if (lig>3 or lig<0) or (col>3 or col<0) or val<0:
        return('Erreur')
    tab = plateau['tiles']
    tab[lig*4 + col] = val
    return plateau

def is_room_empty(plateau, lig, col): # Vérifie si une case du tableau est nul donc libre.
    tab = plateau['tiles']
    if tab[lig*4 + col] != 0:
        return False
    else :
        return True
