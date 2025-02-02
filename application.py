#import de la bibliothèque
from tkinter import *



# --------------------- Création de la fenêtre graphique --------------------- #
ma_fenetre=Tk()
ma_fenetre.title("Constructions œuvres géométriques")
ma_fenetre.geometry('1000x600')
ma_fenetre['bg']='black'

main_color = 'black'
second_color = 'blue'

# ---------------------------- Création des objets --------------------------- #

ZoneDessin=Canvas(ma_fenetre,width=800,height=600,bg=main_color, borderwidth=0, highlightthickness=0)
ZoneParam=Canvas(ma_fenetre,width=200,height=600,bg=main_color, borderwidth=0, highlightthickness=0)

titre1 = Label(ZoneParam, text="Choix de la forme", bg=main_color, fg=second_color)
forme = IntVar() #La figure sera un carre si forme = 0, sinon elle est un cercle
carre_btn = Radiobutton(ZoneParam, text="Carre", value=0, variable=forme, bg=main_color, fg=second_color)
cercle_btn = Radiobutton(ZoneParam, text="Cercle", value=1, variable=forme, bg=main_color, fg=second_color)

titre2 = Label(ZoneParam, text="Choix taille en pixel", bg=main_color, fg=second_color)
size = IntVar() #La taille d'une figure(0 -> 100)
scale = Scale(ZoneParam, orient=HORIZONTAL, from_=0, to=100, variable=size, bg=main_color, fg=second_color)

titre3 = Label(ZoneParam, text="Abscisse du centre", bg=main_color, fg=second_color)
abs_centre = Entry(ZoneParam)

titre4 = Label(ZoneParam, text="Ordonnée du centre", bg=main_color, fg=second_color)
ord_centre = Entry(ZoneParam)

titre5 = Label(ZoneParam, text="Choix de la couleur" , bg=main_color, fg=second_color)
couleurs = ["blue", "red", "green", "yellow"]
liste_couleur = Listbox(ZoneParam, selectmode = SINGLE, height=4, bg=main_color, fg=second_color)

#Init de listbox avec une liste des couleurs
for i in range(len(couleurs)):
    liste_couleur.insert(i, couleurs[i])

"""
    La fonction qui cree une figure entre les deux suivantes:
    - carre
    - cercle
    Etapes:
        1) initialization des variables a utiliser
            a - longeur/largeur d'une figure
            x0 - abs d'origine
            y0 - ord d'origine
            x1=x0+a - deuxieme abscisse
            y1=y0+a - deuxieme ordonnee
            couleur - coloration choisie

        2) Si on a choisit carre:
            a. methode .create_rectangle
        Si non:
            b. methode .create_oval 
    """
def createFigure():
    #1)
    a = size.get() * 5 #Max size peut etre 500px
    x0 = float(abs_centre.get()) #convertation de str -> float
    y0 = float(ord_centre.get())
    #Les coordonnees de 2 point(origine + cote)
    x1 = x0 + a
    y1 = y0 + a
    couleur = liste_couleur.get(ACTIVE) #Couleur d'une figure placée
    #2)
    if forme.get() == 0:
        ZoneDessin.create_rectangle(x0, y0, x1, y1, fill=couleur)
    else:
        ZoneDessin.create_oval(x0, y0, x1, y1, fill=couleur)

dessin_btn = Button(ZoneParam, text="Dessiner", command=createFigure, bg=main_color, fg=second_color)
quit_btn = Button(ZoneParam, text="Quitter", bg=main_color, fg=second_color)

# ------------------------- Positionnement des objets ------------------------ #
ZoneDessin.place(x=0,y=0)
ZoneParam.place(x=800, y=0)

titre1.pack()
carre_btn.pack()
cercle_btn.pack()

titre2.pack()
scale.pack()

titre3.pack()
abs_centre.pack()

titre4.pack()
ord_centre.pack()

titre5.pack()
liste_couleur.pack()

dessin_btn.pack()
quit_btn.pack()


# -------------------------- Lancement d'application ------------------------- #
ma_fenetre.mainloop()