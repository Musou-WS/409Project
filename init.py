import game
from tkinter import *

root = Tk()
root.geometry('500x500')
game.create_panel(root)
game.create_grid()
root.mainloop()