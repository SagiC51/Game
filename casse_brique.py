import tkinter as tk
import random as rd
fenetre = tk.Tk()
CANVAS_WIDTH = CANVAS_HEIGHT = 500
X1 = 0
X2 = 500
Y1 = Y2 = 500-50
XBRICK = 510
YBRICK = 140
SPEED = 5

direction = 0
en_cours= False

######################## Partie Fonction ############################

def On_Off():
    global en_cours
    if en_cours == False : 
        B_Start['text'] = 'Pause'
        en_cours = True
        moveballe()
        moveplayer()
    else: 
        B_Start['text'] = 'Play'
        en_cours = False

def Brick():
    Color = ['red','blue','green','yellow','purple']
    i = rd.randint(0,4)
    xh = yh = 2 
    xb = 50
    yb = 20
    C.create_rectangle(xh,yh,xb,yb,fill=Color[i],outline='black')
    while yb != YBRICK:
        if xb > XBRICK-12:
            xh= 2
            xb = 50
            yh=yb
            yb +=20 
            C.create_rectangle(xh,yh,xb,yb,fill=Color[i],outline='black')
            i= rd.randint(0,4)
        while xb < XBRICK-12: 
            xh=xb
            xb +=50   
            C.create_rectangle(xh,yh,xb,yb,fill=Color[i],outline='black')
            i= rd.randint(0,4)

def player():
    x, y= X2/2, Y2-30
    dx = 0
    dy = 0
    rectangle = C.create_rectangle(x-25, y-5,x+25, y+5,fill="grey")
    return [rectangle, dx, dy]

def right(event): 
    player[1]= SPEED
    print ("Droite")
    
def left(event): 
    player[1]= -SPEED
    print ("gauche")

def bord():
    pass   

def moveplayer():
    if en_cours == True:
        C.move(player[0], player[1], player[2])
        C.after(20, moveplayer)
    
def balle():
    x, y = X2/2,Y2-50
    dx = dy = SPEED 
    rayon = 8
    cercle = C.create_oval(x-rayon, y-rayon,x+rayon, y+rayon,fill="blue")
    return [cercle, dx, dy]

def moveballe():
    if en_cours == True:
        rebond()
        C.move(balle[0], balle[1], balle[2])
        C.after(20, moveballe)

def rebond():
    xb0, yb0, xb1, yb1 = C.coords(balle[0])
    xp0, yp0, xp1, yp1 = C.coords(player[0])
    if xb0 <= X1 or xb1 >=XBRICK :
        balle[1] = -balle[1]
    if yb0 <= yp0 and yb1 >= yp1:
        balle[2] = -balle[2]
    if yb0 <= YBRICK or yb1 >= Y1:
        balle[2] = -balle[2]

def destroy():
    pass

######################### Code Principale ###########################

C = tk.Canvas(background = 'white', width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
C.create_line(X1,Y1,X2,Y2,fill='red',width=5)
grille = Brick()
balle = balle()
player = player()
B_Start = tk.Button(text = "Démarrer",command=On_Off)
fenetre.bind("<KeyPress-Right>",right)
fenetre.bind("<KeyPress-Left>",left)
############## Placement des différents éléments ####################

C.grid(row = 1, column = 0, columnspan = 4)
B_Start.grid(row = 0, column=0,columnspan = 4)

####################### Fin du programme  ###########################

fenetre.mainloop()