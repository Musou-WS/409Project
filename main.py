from tkinter import *
from functools import partial
from itertools import product

import game

class self:
	frame = None
	start = None

def reinit():
	clear()
	create()

def clear():
	if self.frame != None:
		for item in self.frame.winfo_children():
			item.destroy()

def create():
	self.start = Button(self.frame, command=partial(show), text="start")
	self.start.pack()

def show():
	game.reinit()
	self.frame.pack_forget()
	game.self.frame.pack(fill='both', expand='True')