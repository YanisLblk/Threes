# coding:utf-8
#!usr/bin/env python

from window import *
from ui.play_display import medium_display
from tiles.game.play import create_new_play, get_score
from ui.user_entries import get_user_menu
from life_cycle.play import cycle_play, save_game, restore_game

def threes():
    partie=None
    menu = get_user_menu(partie)
    if menu == 'N':
        partie = create_new_play()
    elif menu == 'L':
        partie = restore_game()
    jeu=False
    while jeu!=True:
        jeu=cycle_play(partie)

        if jeu == False: #Si le menu est séléctionner en pleine partie.
            menu = get_user_menu(partie)
            if menu == 'S':
                save_game(partie)
                return('Partie sauvegarder')
            elif menu == 'Q':
                save_game(create_new_play())
                return('fin du jeu')

        elif jeu == True:
            save_game(create_new_play())
            replay=''
            while replay != 'r' and replay != 'p':
                print('rejouer r/p')
                replay = str(input())
                replay = replay.lower()
            if replay=='r':
                jeu = False
                partie = create_new_play()
            else:
                return('fin du jeu')
        elif jeu == 'Game Over !':
            medium_display(partie['plateau'])
            partie['score'] = get_score(partie['plateau'])
            print('Votre score est de ', partie['score'] , 'points.')
            return jeu

def threesV2(partie):
    jeu=False
    while jeu!=True:
        jeu=cycle_play(partie)
        if jeu == False: #Si le menu est séléctionner en pleine partie.
            menu = get_user_menu(partie)
            if menu == 'S':
                save_game(partie)
                return('Partie sauvegarder')
            elif menu == 'Q':
                save_game(create_new_play())
                return('fin du jeu')

        elif jeu == True:
            save_game(create_new_play())
            replay=''
            while replay != 'r' and replay != 'p':
                print('rejouer r/p')
                replay = str(input())
                replay = replay.lower()
            if replay=='r':
                jeu = False
                partie = create_new_play()
            else:
                return('fin du jeu')
        elif jeu == 'Game Over !':
            medium_display(partie['plateau'])
            partie['score'] = get_score(partie['plateau'])
            print('Votre score est de ', partie['score'] , 'points.')
            return jeu

window = window()
window.titre()
window.accueil()
"""
window = Tk()

window.title("Jeu Threes")
window.geometry("1080x720")
window.minsize(480, 360)
window.iconbitmap("img/logo.ico")
window.config(background="black")

frame_title = Frame(window, bd=4)
label_title = Label(frame_title, text="Jeu Threes", font=("Courriel", 40), fg="white", bg="black")
label_title.pack()
frame_title.pack(expand=1)

frame_button = Frame(window)
new_game_button = Button(frame_button, text="Commencer une nouvelle partie", font=("Courriel", 30), fg="white", bg="black").pack() #command=threesV2(create_new_play())
load_button = Button(frame_button, text="Charger une Partie", font=("Courriel", 30), fg="white", bg="black").pack() #command=threesV2(restore_game())
exit_button = Button(frame_button, text="Quitter", font=("Courriel", 30), fg="white", bg="black", command=quit).pack()
frame_button.pack(padx=25, fill="x", side="bottom", expand=1)

#afficher
window.mainloop()

cprint("     _   _____   _   _        _____   _   _   _____    _____   _____   _____  ", "white", "on_red")
cprint("    | | | ____| | | | |      |_   _| | | | | |  _  \  | ____| | ____| /  ___/ ", "white", "on_red")
cprint("    | | | |__   | | | |        | |   | |_| | | |_| |  | |__   | |__   | |___  ", "white", "on_red")
cprint(" _  | | |  __|  | | | |        | |   |  _  | |  _  /  |  __|  |  __|  \___  \ ", "white", "on_red")
cprint("| |_| | | |___  | |_| |        | |   | | | | | | \ \  | |___  | |___   ___| | ", "white", "on_red")
cprint("\_____/ |_____| \_____/        |_|   |_| |_| |_|  \_\ |_____| |_____| /_____/ ", "white", "on_red")
"""
#print(threes())