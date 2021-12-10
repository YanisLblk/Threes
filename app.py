from ui.PlayDisplay import display
from game.Play import createNewPlay, getScore
from ui.UserEntries import getUserMenu
from life_cycle.Play import playCycle, saveGame, restoreGame

def threes():
    partie=None
    menu = getUserMenu(partie)
    if menu == 'N':
        partie = createNewPlay()
    elif menu == 'L':
        partie = restoreGame()
    jeu=False
    while jeu!=True:
        jeu = playCycle(partie)

        if jeu == False: #Si le menu est séléctionner en pleine partie.
            menu = getUserMenu(partie)
            if menu == 'S':
                saveGame(partie)
                return('Partie sauvegarder')
            elif menu == 'Q':
                saveGame(createNewPlay())
                return('fin du jeu')

        elif jeu == True:
            saveGame(createNewPlay())
            replay=''
            while replay != 'r' and replay != 'p':
                print('rejouer r/p')
                replay = str(input())
                replay = replay.lower()
            if replay=='r':
                jeu = False
                partie = createNewPlay()
            else:
                return('fin du jeu')
        elif jeu == 'Game Over !':
            display(partie['board'])
            partie['score'] = getScore(partie['board'])
            print('Votre score est de ', partie['score'] , 'points.')
            return jeu


print("     _   _____   _   _        _____   _   _   _____    _____   _____   _____  ")
print("    | | | ____| | | | |      |_   _| | | | | |  _  \  | ____| | ____| /  ___/ ")
print("    | | | |__   | | | |        | |   | |_| | | |_| |  | |__   | |__   | |___  ")
print(" _  | | |  __|  | | | |        | |   |  _  | |  _  /  |  __|  |  __|  \___  \ ")
print("| |_| | | |___  | |_| |        | |   | | | | | | \ \  | |___  | |___   ___| | ")
print("\_____/ |_____| \_____/        |_|   |_| |_| |_|  \_\ |_____| |_____| /_____/ ")
print(threes())