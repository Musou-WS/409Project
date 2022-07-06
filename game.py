from tkinter import *
#import qrandom

def init_game():
	root = Tk()
	root.geometry('500x500')
	width = 50
	create_panel()
	root.mainloop()

def create_panel(root):
	block = [[Button(root) for i in range(10)] for j in range(10)]
	for i in range(10):
		for j in range(10):
			block[i][j].place(x=i*50, y=j*50, width=50, height=50)

def create_grid():
	grid = [[0 for j in range(10)] for i in range(10)]
	set_bombs()

def set_bombs():
	bombNum = 0;
	while bombNum < 10:
		coordTemp = get_random_coords()
		# check if the coord already contains a bomb
		if grid[coordTemp[0]][coordTemp[1]] == 0:
			grid[coordTemp[0]][coordTemp[1]] == 1
			bombNum += 1

def get_random_coords():
	# use ANU to get quantum random numbers
	coordTemp = qrandom.sample(range(9), 2)
	return coordTemp