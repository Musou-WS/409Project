import game
from tkinter import *

root = Tk()
root.geometry('400x400')
game.create_panel(root)
game.create_grid()
root.mainloop()