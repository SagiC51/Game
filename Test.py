import tkinter as tk
fenetre = tk.Tk()
CANVAS_WIDTH = CANVAS_HEIGHT = 500

######################### Code Principale ###########################

C = tk.Canvas(background = 'black', width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
x0= y0=0
x1= 510
y1=150
C.create_rectangle(x0,y0,x1,y1,fill='white')
xh=yh=2
xb=50
yb=20
C.create_rectangle(xh,yh,xb,yb,outline='red')
while yb != y1-2:
    if xb == x1-12:
        xh= 0
        xb = 50
        yh=yb
        yb +=20 
    else:    
        xh=xb
        xb +=50
    C.create_rectangle(xh,yh,xb,yb,outline='red')
         
C.grid(row = 0, column = 3, columnspan = 4)

####################### Fin du programme  ###########################

fenetre.mainloop()