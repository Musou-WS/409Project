from tkinter import *
from functools import partial
from itertools import product

import game
import credits

class self:
	frame = None
	startBtn = None
	creditsBtn = None

def reinit():
	clear()
	create()

def clear():
	if self.frame != None:
		for item in self.frame.winfo_children():
			item.destroy()

def create():
	self.startBtn = Button(self.frame, command=partial(show, game), text="start")
	self.startBtn.pack(expand='True')
	self.creditsBtn = Button(self.frame, command=partial(show, credits), text="credits")
	self.creditsBtn.pack(expand='True')

def show(element):
	element.reinit()
	self.frame.pack_forget()
	element.self.frame.pack(fill='both', expand='True')