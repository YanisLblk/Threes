from random import randint
from tiles_acces import get_value, set_value, is_room_empty

# Fonction de la partie 1

def get_nb_empty_rooms(plateau): # Met à jour le dictionnaire avec le nombre de case libre.
    tab = plateau['tiles'] # Rentre le tableau dans une variable
    i = 0
    case_vide = 0 # Crée une variable pour le nombre de case libre.
    while i<len(tab): # Parcours les éléments du tableau
        if tab[i]==0: # Si une valeur du tableau est égale à 0, alors c'est une case libre
            case_vide += 1 # +1 pour chaque valeur de 0
        i += 1
    plateau['nb_cases_vides'] = case_vide
    return plateau['nb_cases_vides']

# ###################################################################################################################
# ###################################################################################################################

# Fonction de la partie 2

def get_next_alea_tiles(plateau, mode): # Vérifie les Places disponible des tuiles lors de la partie.
    dico_tiles = {'mode' : mode}
    tuile = False # Variable initier pour la clé 1 présent dans les deux dictionnaires possibles.
    if mode=='encours': # Première condition pour le mode 'encours'.
        while tuile != True: # Crée des cordonnés aléatoirement jusqu'à qu'il trouve un emplacement vide
            ligne = randint(0, 3)
            colonne = randint(0, 3)
            tuile = is_room_empty(plateau, ligne, colonne)
        dico_tiles['0']= {'val': randint(1, 3), 'lig': ligne, 'col': colonne}
    elif mode=='init': # Mode qui crée deux valeur dans le plateau
        while tuile!= True: # Crée des cordonnés aléatoirement jusqu'à qu'il trouve un emplacement vide
            ligne = randint(0, 3)
            colonne = randint(0, 3)
            tuile = is_room_empty(plateau, ligne, colonne)
        dico_tiles['0']= {'val': randint(1, 2), 'lig': ligne, 'col': colonne}
        tuile1 = False
        while tuile1!= True:
            ligne1 = randint(0, 3)
            colonne1 = randint(0, 3)
            tuile1 = is_room_empty(plateau, ligne1, colonne1)
        dico_tiles['1']= {'val': randint(1, 2), 'lig': ligne1, 'col': colonne1}
    if mode=='encours' or mode=='init': # Si le mode vaut 'init' ou 'encours', alors le dictionnaire est valide.
        dico_tiles['check'] = True
    else:
        dico_tiles['check'] = False
    return dico_tiles

def get_next_alea_tiles1(plateau, mode): # Vérifie les Places disponible des tuiles lors de la partie.
    dico_tiles = {'mode' : mode}
    tuile = False # Variable initier pour la clé 1 présent dans les deux dictionnaires possibles.
    if mode=='encours': # Première condition pour le mode 'encours'.
        if is_game_over(plateau) == True:
            dico_tiles['check'] == False
        else:
            while tuile != True: # Crée des cordonnés aléatoirement jusqu'à qu'il trouve un emplacement vide
                ligne = randint(0, 3)
                colonne = randint(0, 3)
                tuile = is_room_empty(plateau, ligne, colonne)
            dico_tiles[0]= {'val': randint(1, 3), 'lig': ligne, 'col': colonne}
    elif mode=='init': # Mode qui crée deux valeur dans le plateau
        while tuile!= True: # Crée des cordonnés aléatoirement jusqu'à qu'il trouve un emplacement vide
            ligne = randint(0, 3)
            colonne = randint(0, 3)
            tuile = is_room_empty(plateau, ligne, colonne)
        dico_tiles[0]= {'val': randint(1, 2), 'lig': ligne, 'col': colonne}
        tuile1 = False
        while tuile1!= True:
            ligne1 = randint(0, 3)
            colonne1 = randint(0, 3)
            tuile1 = is_room_empty(plateau, ligne1, colonne1)
        dico_tiles[1]= {'val': randint(1, 2), 'lig': ligne1, 'col': colonne1}
    if mode=='encours' or mode=='init': # Si le mode vaut 'init' ou 'encours', alors le dictionnaire est valide.
        dico_tiles['check'] = True
    else:
        dico_tiles['check'] = False
    return dico_tiles

def put_next_tiles(plateau, tiles):# Met les valeurs dans les tuiles disponibles.
    if tiles['check']==True:
        if tiles['mode']=='encours': #Placement pour le mode 'encours'.
            d0 = tiles['0']
            plateau = set_value(plateau, d0['lig'], d0['col'], d0['val'])
        elif tiles['mode']=='init': #Placement pour le mode 'init'.
            d0 = tiles['0']
            d1 = tiles['1']
            plateau = set_value(plateau, d0['lig'], d0['col'], d0['val'])
            plateau = set_value(plateau, d1['lig'], d1['col'], d1['val'])
        else:
            return('Erreur')
        return plateau
    elif tiles['check'] == False:
        return False

def line_pack(plateau, num_lig, debut, sens): # Fonction qui décale une ligne du tableau
    tab = plateau['tiles']
    if sens == 0: # Le décalage se fait par la droite.
        while debut>0: # Le décalge à partir d'une valeur précise.
            tab[num_lig*4+debut] = tab[num_lig*4+debut-1]
            debut -= 1
    elif sens == 1: # Le décalage se fait par la gauche.
        while debut<3: # Le décalge à partir d'une valeur précise.
            tab[num_lig*4+debut] = tab[num_lig*4+debut+1]
            debut += 1
    tab[num_lig*4+debut]=0 # Faire passer la valeur de départ à 0 pour ne pas avoir de double.
    return plateau

def colum_pack(plateau, num_col, debut, sens): # fonction qui décale une colonne d'un tableau.
    tab = plateau['tiles']
    if sens == 0: #Le décalage en bas.
        while debut>0:
            tab[debut*4+num_col]=tab[(debut-1)*4+num_col]
            debut -= 1
    elif sens == 1: #Le décalage vers le haut.
        while debut<3:
            tab[debut*4+num_col]=tab[(debut+1)*4+num_col]
            debut += 1
    tab[debut*4+num_col]=0 # Faire passer la valeur de départ à 0 pour ne pas avoir de double.
    return plateau

def line_move2(plateau, num_lig, sens): #Gère l'incrémentation des valeurs du tableau lors du décalage horizontale.
    tab = plateau['tiles']
    if sens == 0:
        decale = 3
        while tab[num_lig*4+decale]!=0 and decale>0:
            decale -= 1
    elif sens == 1:
        decale = 0
        while tab[num_lig*4+decale]!=0 and decale<3:
            decale += 1
    line = line_pack(plateau, num_lig, decale, sens) #Faire le décalage avec une fonction.
    tab = line['tiles']
    if sens == 0: #Le décalage à droite.
        debut = 3
        while debut>0:
            if tab[num_lig*4+debut]==tab[num_lig*4+debut-1] and tab[num_lig*4+debut]>2: # Les valeurs identiques et supérieur à 2 se somme.
                tab[num_lig*4+debut] += tab[num_lig*4+debut-1]
                tab[num_lig*4+debut-1] = 0
                return line
            elif (tab[num_lig*4+debut]==1 and tab[num_lig*4+debut-1]==2) or (tab[num_lig*4+debut]==2
            and tab[num_lig*4+debut-1]==1): #Les valeurs 1 et 2 se somme.
                tab[num_lig*4+debut] += tab[num_lig*4+debut-1]
                tab[num_lig*4+debut-1] = 0
                return line
            debut -= 1
    elif sens == 1: #Décalage à gauche.
        debut = 0
        while debut<3:
            if tab[num_lig*4+debut] == tab[num_lig*4+debut+1] and tab[num_lig*4+debut]>2: # Les valeurs identiques et supérieur à 2 se somme.
                tab[num_lig*4+debut] += tab[num_lig*4+debut+1]
                tab[num_lig*4+debut+1] = 0
                return line
            elif (tab[num_lig*4+debut]==1 and tab[num_lig*4+debut+1]==2) or (tab[num_lig*4+debut]==2
            and tab[num_lig*4+debut+1]==1): #Les valeurs 1 et 2 se somme.
                tab[num_lig*4+debut] += tab[num_lig*4+debut+1]
                tab[num_lig*4+debut+1] = 0
                return line
            debut += 1
    return line #Retourne le dictionnaire décaler.

def line_move(plateau, num_lig, sens): #Gère l'incrémentation des valeurs du tableau lors du décalage horizontale.
    tab = plateau['tiles']
    if sens == 0: #Le décalage à droite.
        debut = 3
        while debut > 0:
            if tab[num_lig*4+debut]==0:
                line_pack(plateau, num_lig, debut, sens)
                return plateau

            elif tab[num_lig*4+debut]==tab[num_lig*4+debut-1] and tab[num_lig*4+debut]>2: # Les valeurs identiques et supérieur à 2 se somme.
                tab[num_lig*4+debut] += tab[num_lig*4+debut-1]
                tab[num_lig*4+debut-1] = 0

            elif (tab[num_lig*4+debut]==1 and tab[num_lig*4+debut-1]==2) or (tab[num_lig*4+debut]==2
            and tab[num_lig*4+debut-1]==1): #Les valeurs 1 et 2 se somme.
                tab[num_lig*4+debut] += tab[num_lig*4+debut-1]
                tab[num_lig*4+debut-1] = 0
            debut -= 1
    elif sens == 1: #Décalage à gauche.
        debut = 0
        while debut<3:
            if tab[num_lig*4+debut] == 0:
                line_pack(plateau, num_lig, debut, sens)
                return plateau

            elif tab[num_lig*4+debut] == tab[num_lig*4+debut+1] and tab[num_lig*4+debut]>2: # Les valeurs identiques et supérieur à 2 se somme.
                tab[num_lig*4+debut] += tab[num_lig*4+debut+1]
                tab[num_lig*4+debut+1] = 0

            elif (tab[num_lig*4+debut]==1 and tab[num_lig*4+debut+1]==2) or (tab[num_lig*4+debut]==2
            and tab[num_lig*4+debut+1]==1): #Les valeurs 1 et 2 se somme.
                tab[num_lig*4+debut] += tab[num_lig*4+debut+1]
                tab[num_lig*4+debut+1] = 0
            debut += 1
    return plateau #Retourne le dictionnaire décaler.


def column_move(plateau, num_col, sens): #Gère l'incrémentation des valeurs du tableau lors du décalage verticale.
    tab = plateau['tiles']
    if sens == 0:
        debut = 3
        while debut>0:
            if tab[debut*4+num_col] == 0:
                colum_pack(plateau, num_col, debut, sens)
                return plateau

            elif tab[debut*4+num_col] == tab[(debut-1)*4+num_col] and tab[debut*4+num_col]>2:
                tab[debut*4+num_col] += tab[(debut-1)*4+num_col]
                tab[(debut-1)*4+num_col] = 0

            elif (tab[debut*4+num_col]==1 and tab[(debut-1)*4+num_col]==2) or (tab[debut*4+num_col]==2
            and tab[(debut-1)*4+num_col]==1):
                tab[debut*4+num_col] += tab[(debut-1)*4+num_col]
                tab[(debut-1)*4+num_col] = 0
            debut -= 1
    elif sens == 1:
        debut = 0
        while debut<3:
            if tab[debut*4+num_col] == 0:
                colum_pack(plateau, num_col, debut, sens)
                return plateau

            elif tab[debut*4+num_col] == tab[(debut+1)*4+num_col] and tab[debut*4+num_col]>2:
                tab[debut*4+num_col] += tab[(debut+1)*4+num_col]
                tab[(debut+1)*4+num_col] = 0

            elif (tab[debut*4+num_col]==1 and tab[(debut+1)*4+num_col]==2) or (tab[debut*4+num_col]==2
            and tab[(debut+1)*4+num_col]==1):
                tab[debut*4+num_col] += tab[(debut+1)*4+num_col]
                tab[(debut+1)*4+num_col] = 0

            debut += 1
    return plateau

def column_move2(plateau, num_col, sens): #Gère l'incrémentation des valeurs du tableau lors du décalage verticale.
    tab = plateau['tiles']
    if sens == 0:
        decale = 3
        while tab[decale*4+num_col]!=0 and decale>0:
            decale -= 1
    elif sens == 1:
        decale = 0
        while tab[decale*4+num_col]!=0 and decale<3:
            decale += 1
    colum = colum_pack(plateau, num_col, decale, sens)
    if sens == 0:
        debut = 3
        while debut>0:
            if tab[debut*4+num_col] == tab[(debut-1)*4+num_col] and tab[debut*4+num_col]>2:
                tab[debut*4+num_col] += tab[(debut-1)*4+num_col]
                tab[(debut-1)*4+num_col] = 0
                return colum
            elif (tab[debut*4+num_col]==1 and tab[(debut-1)*4+num_col]==2) or (tab[debut*4+num_col]==2
            and tab[(debut-1)*4+num_col]==1):
                tab[debut*4+num_col] += tab[(debut-1)*4+num_col]
                tab[(debut-1)*4+num_col] = 0
                return colum
            debut -= 1
    elif sens == 1:
        debut = 0
        while debut<3:
            if tab[debut*4+num_col] == tab[(debut+1)*4+num_col] and tab[debut*4+num_col]>2:
                tab[debut*4+num_col] += tab[(debut+1)*4+num_col]
                tab[(debut+1)*4+num_col] = 0
                return colum
            elif (tab[debut*4+num_col]==1 and tab[(debut+1)*4+num_col]==2) or (tab[debut*4+num_col]==2
            and tab[(debut+1)*4+num_col]==1):
                tab[debut*4+num_col] += tab[(debut+1)*4+num_col]
                tab[(debut+1)*4+num_col] = 0
                return colum
            debut += 1
    return colum


def lines_move(plateau, sens): #Décalage de la totalité du plateau dans l'un des sens horizontalement.
    num_lig = 0
    while num_lig<4:
        line = line_move(plateau, num_lig, sens)
        num_lig += 1
    return line

def columns_move(plateau, sens): #Décalage de la totalité du plateau dans l'un des sens verticalement.
    num_col = 0
    while num_col<4:
        colum = column_move(plateau, num_col, sens)
        num_col += 1
    return colum

def play_move(plateau, sens): # Chaque touche décale le tableau dans un sens.
	if sens == 'b':
		columns_move(plateau, 0)
	elif sens == 'h':
		columns_move(plateau, 1)
	elif sens == 'g':
		lines_move(plateau, 1)
	elif sens == 'd':
		lines_move(plateau, 0)
	return plateau
