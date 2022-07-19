import game
import main
import credits
from tkinter import *

root = Tk()
root.geometry('400x430')
root.title('P')

main.self.frame = Frame(root, width=100, height=200)
main.self.frame.pack_propagate(0)
credits.self.frame = Frame(root)
main.create()
game.self.frame = Frame(root)
main.self.frame.pack(expand='True')

root.mainloop()