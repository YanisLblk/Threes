def display(board): # this function manages the display
    n = board['n']
    tab = board['tiles']
    valeur = 0
    i = 0
    while i<n:
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
                case = '|'+res+'|'
                print(case)
            valeur += 1
            j += 1
        print(ligne)
        i += 1
    print(37*'*')