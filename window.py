from tkinter import *

class window:

    def __init__(self):
        self.window = Tk()
        self.window.title("Jeu Threes")
        self.window.geometry("1080x720")
        self.window.minsize(480, 360)
        self.window.iconbitmap("img/logo.ico")
        self.window.config(background="black")

    def titre(self):
        self.frameTitle = Frame(self.window)
        Label(self.frameTitle, text="Jeu Threes", font=("Courriel", 30), fg="white", bg="black").pack(side="top")
        self.frameTitle.pack(expand=YES)

    def accueil(self):
        self.frameAccueil = Frame(self.window)
        Button(self.frameAccueil, text="Commencer une nouvelle partie", font=("Courriel", 30), fg="white", bg="black", command=self.NewGame()).pack()
        Button(self.frameAccueil, text="Charger une Partie", font=("Courriel", 30), fg="white", bg="black").pack()
        Button(self.frameAccueil, text="Quitter", font=("Courriel", 30), fg="white", bg="black", command=quit).pack()
        self.frameAccueil.pack(expand=YES)
        self.window.mainloop()

    def NewGame(self):
        self.frameAccueil.pack_forget()
        self.frameInGame = Frame(self.window)
        Label(self.frameInGame, text="In Game", font=("Courriel", 30), fg="white", bg="black").pack()
        self.frameInGame.pack()
        #self.window.mainloop()