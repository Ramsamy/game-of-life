#!/usr/bin/python

from random import randint
from Tkinter import *

size=70
k=1 # initialize 1/(k+1) live cells
cellwidth=8
time=150 # refresh time

# Generate matrix
def mat(): 
    matrix=[]
    for i in range(size):
        line=[]
        for j in range(size):
            line.append(randint(0,k)==0) 
        matrix.append(line)
    return matrix

# Evolve to next generation
def evolution(m):
    matrix=[]
    for i in range(size):
        line=[]
        for j in range(size):
            state=m[i][j]
            nb=m[(i-1)%size][(j-1)%size]+m[(i-1)%size][j]+m[(i-1)%size][(j+1)%size]+m[i][(j-1)%size]+m[i][(j+1)%size]+m[(i+1)%size][(j-1)%size]+m[(i+1)%size][j]+m[(i+1)%size][(j+1)%size] #nb est le nombre de cellules voisines en vie

            # Rules
            if state and nb in (2,3): k=True
            elif not state and nb==3: k=True
            else: k=False

            line.append(k)
        matrix.append(line)
    return matrix

class Window():
    def __init__(self):
        self.root=Tk()
        self.root.wm_title("Conways's Game of Life")
        self.step=1

        # Menu
        self.menu=Frame(self.root)
        self.btnNew=Button(self.menu,text="New run",command=self.newrun)
        self.btnPP=Button(self.menu,text="Play / Pause",command=self.pp)
        self.btnQuit=Button(self.menu,text="Quit",command=self.root.quit)
        self.can=Canvas(self.root, width=cellwidth*size, height=cellwidth*size, bg="#444334")
        self.btnNew.pack(side="left")
        self.btnPP.pack(side="left")
        self.btnQuit.pack()
        self.menu.pack()
        self.can.pack()

        # Matrix
        self.matrix=mat()
        self.render()
        self.root.after(time,self.animation)
        self.root.mainloop()

    # Init a new matrix
    def newrun(self):
        self.matrix=mat()

    # Toggle Play/Pause
    def pp(self):
        if self.step==1:
            self.step=0
        else:
            self.step=1

    # Evolve each time steps
    def animation(self):
        for x in range(self.step):
            self.matrix=evolution(self.matrix)
        self.render()
        self.root.after(time,self.animation)

    # Render computation
    def render(self): 
        self.can.delete(ALL)
        x,y=0,0
        for i in self.matrix:
            for j in i:
                if j: # Draw a live cell
                    self.can.create_rectangle(x,y,x+cellwidth,y+cellwidth,fill="#CF9130")
                x+=cellwidth
            y+=cellwidth
            x=0

Window()
