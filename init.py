import game
from tkinter import *

root = Tk()
game.self.frame = Frame(root)
root.geometry('400x430')
game.create_panel()
game.create_grid()
game.self.frame.pack()
root.mainloop()