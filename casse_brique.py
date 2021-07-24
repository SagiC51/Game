import tkinter as tk
import random as rd
import pygame
fenetre = tk.Tk()

pygame.mixer.init()
pygame.mixer.music.load("Casse_brick_song.mp3")


CANVAS_WIDTH = CANVAS_HEIGHT = 500
X1 = Y1 = 0
X2 = Y2 = 500
YBRICK = 140
SPEED = 10
BG = "Black"
INV_BG = "white"

start = False
en_cours= False
Victory = False
nbr_brick = 1
nbr_brick_i = 0 
nbr_life = 3
life = nbr_life

######################## Partie Fonction ############################

def On_Off():
    global en_cours,start
    if en_cours == False : 
        if B_Start['text'] == 'Play':
            B_Start['text'] = 'Pause'
            en_cours = True
        elif B_Start['text'] == 'Démarrer':
            B_Start['text'] = 'Pause'
            en_cours = True
            start = True
        moveballe()
        moveplayer()    
        if B_Start['text'] == 'Recommencer':
            B_Start['text'] = 'Démarrer'
            restart()
    else: 
        if B_Start['text'] == 'Pause':
            B_Start['text'] = 'Play'
            en_cours = False
            start = False
    music()
    
def Brick():
    global nbr_brick,nbr_brick_i
    Color = ['red','blue','green','yellow','purple']
    c = rd.randint(0,4)
    xh = yh = 0
    xb = 50
    yb = 20
    C.create_rectangle(xh,yh,xb,yb,fill=Color[c],outline=BG,tags=("Bricks "+str(nbr_brick)))
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
    nbr_brick_i = nbr_brick

def player():
    x, y= X2/2, Y2-30
    dx = 0
    dy = 0
    rectangle = C.create_rectangle(x-25, y-5,x+25, y+5,fill="grey", outline= "Grey", tag="Player")
    return [rectangle, dx, dy]

def right(event): 
    player[1] = SPEED
    
def left(event): 
    player[1] = -SPEED

def bord():
    xp0, yp0, xp1, yp1 = C.coords(player[0])
    if xp1 < 0 or xp1 > 500:
        if xp1 < 0:
            C.create_rectangle(xp0, yp0, xp1, yp1, fill= INV_BG, outline= INV_BG)
            player[0]=C.create_rectangle(500, yp0, 500+50, yp1, fill ='grey')
        if xp0 > 500:
            C.create_rectangle(xp0, yp0, xp1, yp1, fill= INV_BG, outline= INV_BG)
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
    global life 
    angle = rd.randint(1,2)
    xb0, yb0, xb1, yb1 = C.coords(balle[0])
    xp0, yp0, xp1, yp1 = C.coords(player[0]) 
    objet_b =  C.find_overlapping(xb0+1, yb0+1, xb1-1, yb1-1)
    Brick = int (objet_b[0])
    if xb0 <= X1 or xb1 >= X2 :
        balle[1] = -balle[1]
    if yb1-1 > yp0+1:
        if (xb0>=xp0+1 and xb0<=xp1+1) or (xb1>=xp0+1 and xb1<=xp1+1) :
            if angle == 1: 
                balle[2] = -balle[2]
            elif angle == 2:
                balle[1] = -balle[1]
                balle[2] = -balle[2]
    if yb0 <= Y2 and Brick <= 70 :
        balle[2] = -balle[2]
    if yb0 < Y1:
        balle[2] = -balle[2]
    if yb0 > Y2:
        xb, yb = X2/2,Y2-50
        xp, yp = X2/2, Y2-30
        rayon = 8
        C.coords(balle[0],xb-rayon, yb-rayon, xb+rayon, yb+rayon)
        C.coords(player[0],xp-25, yp-5, xp+25, yp+5)
        player[1] = 0
        life -= 1 
        L_Life_n['text'] = str(life)
        lose()

def destroy():
    global nbr_brick
    xb0, yb0, xb1, yb1 = C.coords(balle[0])
    objet =  C.find_overlapping(xb0+1, yb0+1, xb1-1, yb1-1)
    Brick = int (objet[0])
    if Brick <= 70:
        C.itemconfigure(Brick, state="hidden")
        nbr_brick -=1
        print(nbr_brick, nbr_brick_i)
        win()
       
def win():
    global en_cours,Victory,start
    x,y = X2//2,Y2//2 
    if nbr_brick == 0:
        C.itemconfigure(msg, text ='Bravo \n Tu as gagner !', state='normal')
        B_Start['text'] = 'Recommencer'
        en_cours = False
        Victory = True
        start = False
        music()

def lose():
    global en_cours,start
    x,y = X2//2,Y2//2 
    if life == 0:
        C.itemconfigure(msg, text ='Dommage \n Tu as perdu !', state='normal')
        B_Start['text'] = 'Recommencer'
        en_cours = False
        start = False
        music()
        
def music():
    if en_cours == False :
        pygame.mixer.music.pause()
    elif en_cours == True:
        pygame.mixer.music.unpause()
    if start == True:
        pygame.mixer.music.play(-1)

def restart():
    global Victory, life, en_cours, msg, nbr_brick, nbr_brick_i
    if Victory == True :
        nbr_brick = nbr_brick_i
        xb, yb = X2/2,Y2-50
        xp, yp = X2/2, Y2-30
        rayon = 8
        life = nbr_life
        C.itemconfigure(Brick, state="normal")
        C.coords(balle[0],xb-rayon, yb-rayon, xb+rayon, yb+rayon)
        C.coords(player[0],xp-25, yp-5, xp+25, yp+5)
        player[1] = 0
        L_Life_n ['text'] = str(life)
        B_Start ['text'] = 'Démarrer'
        Victory = False
    else :
        nbr_brick = nbr_brick_i
        xb, yb = X2/2,Y2-50
        xp, yp = X2/2, Y2-30
        Color = ['red','blue','green','yellow','purple']
        c = rd.randint(0,4)
        rayon = 8
        life = nbr_life
        C.itemconfigure(msg, state='hidden')
        C.itemconfigure(Brick, state="normal")
        C.coords(balle[0],xb-rayon, yb-rayon, xb+rayon, yb+rayon)
        C.coords(player[0],xp-25, yp-5, xp+25, yp+5)
        player[1] = 0
        L_Life_n ['text'] = str(life)
        B_Start ['text'] = 'Démarrer' 
        nbr_brick = 1
        while nbr_brick != 70:
            objet = C.find_withtag(nbr_brick)
            Bricks = int (objet[0])
            C.find_withtag(Bricks)
            C.itemconfigure(Bricks, fill= Color[c])
            C.itemconfigure(Bricks, state="normal")
            c = rd.randint(0,4)
            nbr_brick += 1

def help():
    i=0
    Help = tk.Toplevel(fenetre, bg= INV_BG, width=100, height=100)
    Help.title("Aide")
    text = "Règles du Jeu : \n 1. Vous devez cassez toute les bricks pour gagner.\n 2. Si la balle sort de l'écran trois fois vous avez perdu.\n"
    text = text + "3. Utilsez les fléches de votre clavier pour déplacer le padle."
    label = tk.Label(Help, text = text, foreground= BG, font= ("Times New Roman", 15))
    label.grid(row= 0, column=0)

def A_propos():
    propos = tk.Toplevel(fenetre, bg= INV_BG, width=100, height=100)
    propos.title("A propos")
    text = "Jeu fait par\n CHRISTOPHE Pascal\n Audio: "
    text = text + "3. Utilsez les fléches de votre clavier pour déplacer le padle."
    label = tk.Label(propos, text = text, foreground= BG, font= ("Times New Roman", 15))
    label.grid(row= 0, column=0)

def quit():
    fenetre.destroy()
    

######################### Code Principale ###########################

# fenetre et canvas parametre
fenetre.title("Casse brick")
fenetre.resizable(False, False)
C = tk.Canvas(background = BG, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
# menu liste 
mon_menu = tk.Menu(fenetre)
fenetre['menu'] = mon_menu
## menu partie
party = tk.Menu(mon_menu, tearoff=0)
party.add_command(label="Nouvelle Partie", command=restart)
party.add_command(label="Quiter", command=quit)
mon_menu.add_cascade(label="Partie", menu = party)
## menu ?
Point_intero = tk.Menu(mon_menu, tearoff=0)
Point_intero.add_command(label="Aide", command=help)
Point_intero.add_command(label="A propos")
mon_menu.add_cascade(label="?", menu = Point_intero)
#construction du terrain jeu
Brick()
balle = balle()
player = player()
# element du canvas
x,y = X2//2,Y2//2
msg = C.create_text(x,y,text ='', fill= INV_BG, font="Arial 30")
B_Start = tk.Button(text = "Démarrer",command=On_Off) 
L_Life_w = tk.Label(text = "Vie : ", font="Arial 10")
L_Life_n = tk.Label(text = str(life), foreground = "red", font="Arial 10")
fenetre.bind("<KeyPress-Right>",right)
fenetre.bind("<KeyPress-Left>",left)
print(nbr_brick, nbr_brick_i)

############## Placement des différents éléments ####################

C.grid(row = 1, column = 0, columnspan = 4)
B_Start.grid(row = 0, column = 0,columnspan = 4)
L_Life_w.grid(row = 0, column = 2, columnspan = 4)
L_Life_n.grid(row = 0, column = 3, columnspan = 4)
####################### Fin du programme  ###########################

fenetre.mainloop()