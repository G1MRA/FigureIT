from tkinter import *
from tkinter import ttk
#https://www.pythontutorial.net/tkinter/tkinter-color-chooser/

#-Couleurs
bleu = "#37B0D2"
orange = "#D07A39"
noir = "#28262C"
fond = "#F6FDFD"
jaune = "#E9D37B"

#--Creation de la fenetre

ma_fenetre=Tk()
ma_fenetre.title("Construction oeuvre géométriques")
ma_fenetre.geometry('1000x600')
ma_fenetre['bg']=fond

#--Creation des objets

zone_dessin = Canvas(ma_fenetre) #notre zone pour dessiner des figures

zone_param = Frame(ma_fenetre, background=bleu)
zone_figures = Frame(ma_fenetre, background=orange)
#------------------------Variables necessaires-----------------------------
param = ""
border_width = 0
colors = ["red", # couleurs qui sont proposes par defaut pour chaque peintre
          "green",
          "grey",
          "yellow"]
#------------------------Toutes les parametres-----------------------------
parameters_group = Frame(zone_param) #sert a regroupper tous les objets pour les afficher au centre

height_label = ttk.Label(parameters_group, text="height")
height_saisie = ttk.Entry(parameters_group)

width_label = ttk.Label(parameters_group, text="width")
width_saisie = ttk.Entry(parameters_group)

param_label = ttk.Label(parameters_group, text="parameter")
param_saisie = ttk.Combobox(parameters_group, textvariable=param)

border_width_label = ttk.Label(parameters_group, text="border")
border_width_scr = Scale(parameters_group, orient=HORIZONTAL, from_=0, to=100, variable=border_width)

color_label = ttk.Label(parameters_group, text = "color")
color_list = ttk.Combobox(parameters_group, values=colors)

delete_btn = ttk.Button(parameters_group, text = "erase")
#------------------------Les Canvas pour mettre les images des figures-----------------------------
figure1 = Canvas(zone_figures, background="red")
figure2 = Canvas(zone_figures, background="green")
figure3 = Canvas(zone_figures, background="yellow")
figure4 = Canvas(zone_figures, background="grey")
#------------------------Bouttons hors canvas specials-----------------------------
help_btn = ttk.Button(ma_fenetre, text = "help")
retour_btn = ttk.Button(ma_fenetre, text = "return")

#------------------------Placement des objets-----------------------------
zone_dessin.place(relx=0, rely=0, relheight=0.8, relwidth=1)

zone_param.place(relx=0.4, rely=0.8, relheight=0.2, relwidth=0.6)
zone_figures.place(relx=0, rely=0.8, relheight=0.2, relwidth=0.4)

figure1.place(relwidth=0.25, relheight=1, relx=0)
figure2.place(relwidth=0.25, relheight=1, relx=0.25)
figure3.place(relwidth=0.25, relheight=1, relx=0.5)
figure4.place(relwidth=0.25, relheight=1, relx=0.75)

parameters_group.pack(anchor=CENTER)

height_label.grid(row= 1, column=1)
height_saisie.grid(row=2, column=1)
width_label.grid(row=3, column=1)
width_saisie.grid(row=4, column=1)

param_label.grid(row=1, column=2)
param_saisie.grid(row=2, column=2)
border_width_label.grid(row=4, column=2)
border_width_scr.grid(row=3, column=2)
color_label.grid(row=1, column=3)
color_list.grid(row=2, column=3)
delete_btn.grid(row=3, column=3)

help_btn.pack(side="bottom", anchor="e")
retour_btn.pack(side="top", anchor="w")

#------------------------Partie logique-----------------------------
"""Fonction pour repartir les taches entre les methodes des figures"""
def dessiner(event):
    height = int(height_saisie.get())
    width = int(width_saisie.get())
    color = color_list.get()
    #print(event.x, " ", event.y) - test des coordonnees
    return rectangle_des(event.x, event.y, height, width, border_width, color)

"""
Une fonction pour dessiner un rectangle
cursor_x - position d'abscisse du curseur
cursor_y - position d'ordonnee du curseur
h - hauter de la figure
w - largeur de la figure
border - l'entourage de figure en px
color - couleur de la figure
param - parametre specifique de la figure
"""
def rectangle_des(cursor_x:int, cursor_y:int, h:int, w:int, border:int, col:str):
    x0 = cursor_x - w/2 #x de depart decale du centre au curseur
    y0 = cursor_y - h/2 #y de depart

    x = cursor_x + w/2 #x de la fin
    y = cursor_y + h/2 #y de la fin

    zone_dessin.create_rectangle(x0, y0, x, y, fill=col)

#--Lancement de l'application
zone_dessin.bind("<Button-1>", dessiner)
ma_fenetre.mainloop()