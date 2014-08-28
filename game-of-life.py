#!/usr/bin/python

from random import randint
from Tkinter import *

taille=70 #la taille de la matrice
k=1 #On aura 1/(k+1) cellules en vie au depart
largeurCellule=8
temps=150 #intervalle de temps entre chaque rafraichissement

def mat(): #On genere la matrice
	matrice=[]
	for i in range(taille):
		ligne=[]
		for j in range(taille):
			ligne.append(randint(0,k)==0) #On tire au hasard entre 0 et k. Si ca vaut 0 c'est True, sinon c'est False
		matrice.append(ligne)
	return matrice

def evolution(m): #On evolue a la generation suivante
	matrice=[]
	for i in range(taille):
		ligne=[]
		for j in range(taille):
			etat=m[i][j] #etat de la cellule dans l'ex-matrice m
			nb=m[(i-1)%taille][(j-1)%taille]+m[(i-1)%taille][j]+m[(i-1)%taille][(j+1)%taille]+m[i][(j-1)%taille]+m[i][(j+1)%taille]+m[(i+1)%taille][(j-1)%taille]+m[(i+1)%taille][j]+m[(i+1)%taille][(j+1)%taille] #nb est le nombre de cellules voisines en vie
			if etat and nb in (2,3): k=True #les regles du jeu
			elif not etat and nb==3: k=True
			else: k=False
			ligne.append(k)
		matrice.append(ligne)
	return matrice

class fenetre(): #la fenetre avec le resultat
	def __init__(main):
		main.root=Tk()
		main.pas=1

		main.menu=Frame(main.root) #le menu
		main.btnNouveau=Button(main.menu,text="Nouvelle simulation",command=main.nouveau)
		main.btnPP=Button(main.menu,text="Lecture / Pause",command=main.pp)
		main.btnQuitter=Button(main.menu,text="Quitter",command=main.root.quit)

		main.can=Canvas(main.root, width=largeurCellule*taille, height=largeurCellule*taille, bg="#444334") #On cree la fenetre

		main.btnNouveau.pack(side="left") #on pack le tout
		main.btnPP.pack(side="left")
		main.btnQuitter.pack()
		main.menu.pack()
		main.can.pack()

		main.matrice=mat() #On cree la matrice
		main.rendu() #On demande le dessin des rectangles
		main.root.after(temps,main.animation)
		main.root.mainloop()

	def nouveau(main):
		main.matrice=mat() #On cree une matrice toute neuve

	def pp(main): #la fonction Play/Pause
		if main.pas==1:
			main.pas=0
		else:
			main.pas=1

	def animation(main): #on raffraichi l'apercu tous les pas
		for x in range(main.pas):
			main.matrice=evolution(main.matrice)
		main.rendu()
		main.root.after(temps,main.animation)

	def rendu(main): #On dessine les rectangles
		main.can.delete(ALL)
		x,y=0,0
		for i in main.matrice:
			for j in i:
				if j: #Si la cellule est a True, on cree un rectangle
					main.can.create_rectangle(x,y,x+largeurCellule,y+largeurCellule,fill="#CF9130")
				x+=largeurCellule
			y+=largeurCellule
			x=0

fenetre()
