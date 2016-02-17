#!/usr/bin/python

from random import randint
from Tkinter import *

# Configuration
size=70
k=1 # initialize 1/(k+1) live cells
cellwidth=8
time=150 # refresh interval
step=1 # evolution steps between two refresh

# Global matrix
matrix=None

# Generate matrix
def mat(): 
    mat=[]
    for i in range(size):
        line=[]
        for j in range(size):
            line.append(randint(0,k)==0) 
        mat.append(line)
    return mat

# Evolve to next generation
def evolution(m):
    mat=[]
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
        mat.append(line)
    return mat

# Init a new matrix
def newrun():
    global matrix
    matrix=mat()

# Toggle Play/Pause
def pp():
    global step
    if step==1:
        step=0
    else:
        step=1

# Evolve each time steps
def animation():
    global matrix
    for x in range(step):
        matrix=evolution(matrix)
    render()
    root.after(time,animation)

# Render computation
def render():
    global matrix
    can.delete(ALL)
    x,y=0,0
    for i in matrix:
        for j in i:
            if j: # Draw a live cell
                can.create_rectangle(x,y,x+cellwidth,y+cellwidth,fill="#CF9130")
            x+=cellwidth
        y+=cellwidth
        x=0

# Main program

# Init window
root=Tk()
root.wm_title("Conways's Game of Life")

# Init menu
menu=Frame(root)
btnNew=Button(menu,text="New run",command=newrun)
btnPP=Button(menu,text="Play / Pause",command=pp)
btnQuit=Button(menu,text="Quit",command=root.quit)
can=Canvas(root, width=cellwidth*size, height=cellwidth*size, bg="#444334")
btnNew.pack(side="left")
btnPP.pack(side="left")
btnQuit.pack()
menu.pack()
can.pack()

# Matrix
matrix=mat()
render()
root.after(time,animation)
root.mainloop()

