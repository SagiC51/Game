import tkinter as tk
import random as rd
fenetre = tk.Tk()

CANVAS_WIDTH = CANVAS_HEIGHT = 500
X1 = 0
X2 = 500
Y1 = Y2 = 500
YBRICK = 140
SPEED = 5
BG = "white"

en_cours= False
nbr_brick = 1
bricks = []
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
    global nbr_brick,bricks
    Color = ['red','blue','green','yellow','purple']
    c = rd.randint(0,4)
    xh = yh = 0
    xb = 50
    yb = 20
    rectangle = C.create_rectangle(xh,yh,xb,yb,fill=Color[c],outline=BG,tags=("Bricks "+str(nbr_brick)))
    bricks.append(rectangle)
    while yb != YBRICK:
        if xb == X2:
            xh = 0
            xb = 50
            yh = yb
            yb += 20 
            C.create_rectangle(xh,yh,xb,yb,fill=Color[c],outline=BG,tags=("Bricks "+ str(nbr_brick)))
            c= rd.randint(0,4)
            nbr_brick+=1 
        while xb != X2: 
            xh=xb
            xb +=50   
            C.create_rectangle(xh,yh,xb,yb,fill=Color[c],outline=BG,tags=("Bricks "+str(nbr_brick)))
            c= rd.randint(0,4)
            nbr_brick+=1
    return

def player():
    x, y= X2/2, Y2-30
    dx = 0
    dy = 0
    rectangle = C.create_rectangle(x-25, y-5,x+25, y+5,fill="grey",tag="Player")
    return [rectangle, dx, dy]

def right(event): 
    player[1]= SPEED
    
def left(event): 
    player[1]= -SPEED
    print ("gauche")

def bord():
    xp0, yp0, xp1, yp1 = C.coords(player[0])
    if xp1 < 0 or xp1 > 500:
        if xp1 < 0:
            C.create_rectangle(xp0, yp0, xp1, yp1, fill ='white', outline='white')
            player[0]=C.create_rectangle(500, yp0, 500+50, yp1, fill ='grey')
        if xp0 > 500:
            C.create_rectangle(xp0, yp0, xp1, yp1, fill ='white', outline='white')
            player[0]=C.create_rectangle(0, yp0, -50, yp1, fill ='grey')

def moveplayer():
    if en_cours == True:
        bord()
        C.move(player[0], player[1], player[2])
        C.after(20, moveplayer)
    
def balle():
    x, y = X2/2,Y2-50
    dx = dy = SPEED 
    rayon = 8
    cercle = C.create_oval(x-rayon, y-rayon,x+rayon, y+rayon,fill="blue",tag="Balle")
    return [cercle, dx, dy]

def moveballe():
    if en_cours == True:
        rebond()
        destroy()
        C.move(balle[0], balle[1], balle[2])
        C.after(20, moveballe)

def rebond():
    xb0, yb0, xb1, yb1 = C.coords(balle[0])
    xp0, yp0, xp1, yp1 = C.coords(player[0]) 
    objet_b =  C.find_overlapping(xb0+1, yb0+1, xb1-1, yb1-1)
    Brick = int (objet_b[0])
    if xb0 <= X1 or xb1 >= X2 :
        balle[1] = -balle[1]
    if yb1-1 >= yp0+1:
        if (xb0>=xp0+1 and xb0<=xp1+1) or (xb1>=xp0+1 and xb1<=xp1+1) :
            balle[2] = -balle[2]
    if yb0 >= 0 and Brick <= 70 :
        balle[2] = -balle[2]
    if yb0 > Y1:
        xb, yb = X2/2,Y2-50
        xp, yp = X2/2, Y2-30
        rayon = 8
        C.coords(balle[0],xb-rayon, yb-rayon, xb+rayon, yb+rayon)
        C.coords(player[0],xp-25, yp-5, xp+25, yp+5)
        player[1] = 0

def destroy():
    global nbr_brick
    xb0, yb0, xb1, yb1 = C.coords(balle[0])
    objet =  C.find_overlapping(xb0+1, yb0+1, xb1-1, yb1-1)
    Brick = int (objet[0])
    if Brick <= 70:
        C.delete(Brick)
        nbr_brick -=1
       

def win():
    pass
def lose():
    pass
def restart():
    pass


######################### Code Principale ###########################

C = tk.Canvas(background = BG, width = CANVAS_WIDTH, height = CANVAS_HEIGHT,)
Brick()
balle = balle()
player = player()
print(bricks)
B_Start = tk.Button(text = "Démarrer",command=On_Off)
fenetre.bind("<KeyPress-Right>",right)
fenetre.bind("<KeyPress-Left>",left)


############## Placement des différents éléments ####################

C.grid(row = 1, column = 0, columnspan = 4)
B_Start.grid(row = 0, column=0,columnspan = 4)

####################### Fin du programme  ###########################

fenetre.mainloop()