import tkinter as tk

fenetre = tk.Tk()
CANVAS_WIDTH = CANVAS_HEIGHT = 500

X1 = 0
X2 = 500
Y1 = Y2 = 500-50
Color = ['red','bleu','green','yellow','purple']

def Brick():
    x0= y0=0
    x1= 510
    y1=150
    C.create_rectangle(x0,y0,x1,y1,fill='white')



######################### Code Principale ###########################

C = tk.Canvas(background = 'black', width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
C.grid(row = 0, column = 3, columnspan = 4)
C.create_line(X1,Y1,X2,Y2,fill='red')
Brick()


####################### Fin du programme  ###########################

fenetre.mainloop()