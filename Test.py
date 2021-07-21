import tkinter as tk
fenetre = tk.Tk()
CANVAS_WIDTH = CANVAS_HEIGHT = 500

######################### Code Principale ###########################

C = tk.Canvas(background = 'black', width = CANVAS_WIDTH, height = CANVAS_HEIGHT) 
        
         
C.grid(row = 0, column = 3, columnspan = 4)

####################### Fin du programme  ###########################

fenetre.mainloop()
