# Note:
# lorsque tu utilise global pour faire appel à une variable global depuis une fonction tu peux modifier la valeur de cette variable
# ce qui serait impossible si tu passais juste les arguments en parametre de la fonction

from tkinter import *
from random import randrange

def drawline():
    # Tracé d'une ligne dans le canevas can1"
    global x1, y1, x2, y2, coul
    # `(50, 50, 250, 150)`: These are the coordinates of the rectangle. `(50, 50)` is the top-left corner (x1, y1), and `(250, 150)` is the bottom-right corner (x2, y2).
    can1.create_line(x1, y1, x2, y2, width=1, fill=coul)
    # can1.create_arc(x1, y1, x2, y2, width=1, fill=coul)
    # can1.create_oval(x1, y1, x2, y2, width=1, fill=c
    # oul)
    # can1.create_polygon(x1, y1, x2, y2, width=1, fill=coul)
    # modification des coordonnées pour la ligne suivante :
    y2, y1 = y2 + 10, y1 + 10

    # Lignes horizontales et parallèles

def drawline_ne2():
    global a, b, c, d, coul, q, w, e, r
    print(a, b, c, d)
    can1.create_line(a, b, c, d, width=1, fill="red")
    can1.create_line(q, w, e, r, width=1, fill="blue")

def draw(arg) -> None:
    print(arg)
    global x1, y1, x2, y2, coul
    swticher: any = {
        "rectangle": lambda: can1.create_rectangle(x1, y1, x2, y2, width=1, fill=coul),
        "arc": lambda: can1.create_arc(x1, y1, x2, y2),
        "oval": lambda: can1.create_oval(x1, y1, x2, y2),
        "polygon": lambda: can1.create_polygon(100, 100, 200, 100, 150, 150, fill=coul)
    }
    func = swticher.get(arg)
    if func:
        func()
    y2, y1 = y2 + 10, y1 + 10

def changecolor():
    "Changement retaliatory de la couleur du tracé"
    global coul
    pal = ['purple', 'cyan', 'maroon', 'green',
           'red', 'blue', 'orange', 'yellow']
    c = randrange(8)  # => génère un nombre aléatoire de 0 à 7
    coul = pal[c]

# ------ Programme principal -------
# les variables suivantes seront utilisées de manière globale :
x1, y1, x2, y2 = 10, 190, 190, 9  # coordonnées de la ligne
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

bou2 = Button(fen1, text='Tracer une ligne', command=lambda: drawline())
bou2.pack()

bou_rectangle = Button(fen1, text='Tracer un rectangle', command=lambda: draw('rectangle'))
bou_rectangle.pack()

bou_arc = Button(fen1, text='Tracer un arc', command=lambda: draw('arc'))
bou_arc.pack()

bou_oval = Button(fen1, text='Tracer un oval', command=lambda: draw('oval'))
bou_oval.pack()

bou_polygon = Button(fen1, text='Tracer un polygon', command=lambda: draw('polygon'))
bou_polygon.pack()

bout = Button(fen1, text='Viseur', command=drawline_ne2)
bout.pack()

bou3 = Button(fen1, text='Autre couleur', command=changecolor)
bou3.pack()

fen1.mainloop()  # démarrage du réceptionnaire d’événements
fen1.destroy()  # destruction (fermeture) de la fenêtre
