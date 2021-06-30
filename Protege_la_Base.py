import tkinter as tk
import random as rd
fenetre = tk.Tk()
CANVAS_WIDTH = CANVAS_HEIGHT = 500


X1_ZONE = 0
Y1_ZONE = 500-50
X2_ZONE = 500
Y2_ZONE = 500-50

x_ennemi = rd.randint(0,500)
y_ennemi = 0

def ennemi():
    global x_ennemi
    y=0
    C.create_oval(x_ennemi+50,y,x_ennemi-50,y,fill='blue')
    if y<450:
        y+10
        tk.Canvas(background = 'black', width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
        C.create_oval(x_ennemi+50,y,x_ennemi-50,y,fill='blue')



######################### Code Principale ###########################

C = tk.Canvas(background = 'black', width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
C.grid(row = 0, column = 3, columnspan = 4)
C.create_line(X1_ZONE,Y1_ZONE,X2_ZONE,Y2_ZONE,fill='red')
A = ennemi()

####################### Fin du programme  ###########################

fenetre.mainloop()