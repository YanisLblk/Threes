# Fonction de la partie 1

def simple_display(plateau):#affichage simple du plateau sans limitation des zones.
    n = plateau['n'] #je rentre la taille du tableau dans une variable.
    tab = plateau['tiles']
    valeur = 0
    i = 0
    while i<n:
        j = 0
        while j<n:
            point = str(tab[valeur]) # Je transforme les valeurs en chaîne de caractère
            res = point.center(6) # je les recentres.
            if j<n-1:
                print(res, end='') # affiche la valeur et laisse le prochain print sur la même ligne.
            else:
                print(res)# La dernière valeur de chaque ligne
            valeur += 1 # Incrément l'indice pour ajouter toute les valeurs.
            j += 1
        i += 1

def medium_display(plateau):# Un affichage avec des delimitations entre les valeurs.
    n = plateau['n']
    tab = plateau['tiles']
    valeur = 0
    i = 0
    while i<n:
        # Encadrer le tableau aves des asterix.
        print(37*'*')
        ligne = 4*("|"+8*" ")+"|"
        print(ligne)
        j = 0
        while j<n:
            point = str(tab[valeur])
            res = point.center(8)
            if j<n-1:
                res = "|"+point.center(8)
                print(res, end='')
            else:
                # Séparation des valeurs avec |
                case = '|'+res+'|'
                print(case)
            valeur += 1
            j += 1
        print(ligne)
        i += 1
    print(37*'*')

def medium_alt_display(plateau):
    n = plateau['n']
    tab = plateau['tiles']
    valeur = 0
    i = 0
    while i<n:
        print(29*'*')
        j = 0
        while j<n:
            if j==n-1:
                if tab[valeur]>999:
                    print('|',tab[valeur],'|')
                elif tab[valeur]>99:
                    print('|',tab[valeur],' |')
                elif tab[valeur]>9:
                    print('| ',tab[valeur],' |')
                else:
                    print('|  ',tab[valeur],' |')
            else:
                if tab[valeur]>999:
                    print('|',tab[valeur], end=' ')
                elif tab[valeur]>99:
                    print('|',tab[valeur], end='  ')
                elif tab[valeur]>9:
                    print('| ',tab[valeur], end='  ')
                else:
                    print('|  ',tab[valeur], end='  ')
            valeur += 1
            j += 1
        i += 1
    print(29*'*')
