# Petit exercice utilisant la bibliothèque graphique tkinter
from tkinter import *
from random import randrange
# --- définition des fonctions gestionnaires d'événements : ---


def drawline():
    # Tracé d'une ligne dans le canevas can1"
    global x1, y1, x2, y2, coul
    can1.create_line(x1, y1, x2, y2, width=1, fill=coul)
   # modification des coordonnées pour la ligne suivante :
    y2, y1 = y2+10, y1+10

    # Lignes horizontales et parallèles


def drawline_ne2():
    global a, b, c, d, coul, q, w, e, r
    print(a, b, c, d)
    can1.create_line(a, b, c, d, width=1, fill="red")
    can1.create_line(q, w, e, r, width=1, fill="blue")


def changecolor():
    "Changement aléatoire de la couleur du tracé"
    global coul
    pal = ['purple', 'cyan', 'maroon', 'green',
           'red', 'blue', 'orange', 'yellow']
    c = randrange(8)  # => génère un nombre aléatoire de 0 à 7
    coul = pal[c]

# ------ Programme principal -------


# les variables suivantes seront utilisées de manière globale :
x1, y1, x2, y2 = 10, 190, 200, 190  # coordonnées de la ligne
a, b, c, d, = 0, 200, 500, 200
q, w, e, r = 250, 0, 250, 400
coul = 'dark green'  # couleur de la ligne
# Création du widget principal ("maître") :
fen1 = Tk()
# création des widgets "esclaves" :
can1 = Canvas(fen1, bg='dark grey', height=400, width=500)
can1.pack(side=LEFT)
bou1 = Button(fen1, text='Quitter', command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text='Tracer une ligne', command=drawline)
bou2.pack()
bout = Button(fen1, text='Viseur', command=drawline_ne2)
bout.pack()
bou3 = Button(fen1, text='Autre couleur', command=changecolor)
bou3.pack()
fen1.mainloop()  # démarrage du réceptionnaire d’événements
fen1.destroy()  # destruction (fermeture) de la fenêtre
