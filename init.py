import game
import main
import credits
from tkinter import *

root = Tk()
root.geometry('400x430')
root.title('P')

main.self.frame = Frame(root)
credits.self.frame = Frame(root)
main.create()
game.self.frame = Frame(root)
main.self.frame.pack(fill='both', expand='True')

root.mainloop()