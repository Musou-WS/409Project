from tkinter import *
from functools import partial
from itertools import product

import qrandom

class self:
	width = 50
	gridNum = 10
	bombNum = 10
	block = []
	grid = []

def create_panel(root):
	self.block = [[Button(root, command=partial(check, j, i)) for i in range(self.gridNum)] for j in range(self.gridNum)]
	for i in range(self.gridNum):
		for j in range(self.gridNum):
			self.block[i][j].place(x=i*self.width, y=j*self.width, width=self.width, height=self.width)

def create_grid():
	self.grid = [[0 for j in range(self.gridNum)] for i in range(self.gridNum)]
	set_bombs()

def set_bombs():
	bombCount = 0;
	while bombCount < self.bombNum:
		coordTemp = get_random_coords()
		# check if the coord already contains a bomb
		if self.grid[coordTemp[0]][coordTemp[1]] == 0:
			self.grid[coordTemp[0]][coordTemp[1]] = 1
			bombCount += 1

def get_random_coords():
	# use ANU to get quantum random numbers
	coordTemp = qrandom.sample(range(self.gridNum), 2)
	return coordTemp

def check(x, y):
	if self.grid[x][y] == 1:
		print('yes')
		for i in range(self.gridNum):
			for j in range(self.gridNum):
				if self.grid[i][j] == 1:
					print(i, j)
					self.block[i][j].configure(state=DISABLED, highlightbackground="red")
				else:
					self.block[i][j].configure(state=DISABLED)





