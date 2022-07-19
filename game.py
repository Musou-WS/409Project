from tkinter import *
# from tkmacosx import Button
from functools import partial
from itertools import product
from PIL import Image, ImageTk

import qrandom
import random
import qiskit # call the qiskit's module
import json

class self:
	width = 50
	gridNum = 8
	trapNum = 10
	block = []
	grid = []
	target = []
	restart = None
	# init images
	mud = None
	pig = None
	holeGreen = None
	holeRed = None
	# frame
	frame = None

def reinit():
	print("reinit")
	clear()
	create_panel()
	create_grid()

def create_panel():
	# init images
	mudImg = Image.open("img/mud.png")
	mudImgResize = mudImg.resize((44, 44))
	self.mud = ImageTk.PhotoImage(mudImgResize)
	pigImg = Image.open("img/pig.png")
	pigImgResize = pigImg.resize((44, 44))
	self.pig = ImageTk.PhotoImage(pigImgResize)
	holeGreenImg = Image.open("img/holeGreen.png")
	holeGreenImgResize = holeGreenImg.resize((44, 22))
	self.holeGreen = ImageTk.PhotoImage(holeGreenImgResize)
	holeRedImg = Image.open("img/holeRed.png")
	holeRedImgResize = holeRedImg.resize((44, 22))
	self.holeRed = ImageTk.PhotoImage(holeRedImgResize)

	self.block = [[Button(self.frame, command=partial(check, j, i), image=self.mud, compound="center", bg="black", disabledforeground="black") for i in range(self.gridNum)] for j in range(self.gridNum)]
	for i in range(self.gridNum):
		for j in range(self.gridNum):
			self.block[i][j].place(x=i*self.width, y=j*self.width, width=self.width, height=self.width)

	# restart button
	self.restart = Button(self.frame, command=partial(reinit), text="restart")
	self.restart.place(x=330, y=405, width=50, height=25)

def create_grid():
	self.grid = [[0 for j in range(self.gridNum)] for i in range(self.gridNum)]
	set_target()
	set_traps()

def set_target():
	self.target = get_random_coords()
	# self.block[self.target[0]][self.target[1]].configure(highlightbackground="green")

def set_traps():
	trapCount = 0;
	while trapCount < self.trapNum:
		coordTemp = get_self_random_coords()
		# check if the coord already contains a trap
		if self.grid[coordTemp[0]][coordTemp[1]] == 0 & (coordTemp[0] != self.target[0] | coordTemp[1] != self.target[1]):
			self.grid[coordTemp[0]][coordTemp[1]] = 1
			# self.block[coordTemp[0]][coordTemp[1]].configure(highlightbackground="blue")
			trapCount += 1

def get_random_coords():
	# use ANU to get quantum random numbers
	coordTemp = random.sample(range(self.gridNum), 2)
	return coordTemp

def get_self_random_coords():
	coordX = get_zero_or_one()*4 + get_zero_or_one()*2 + get_zero_or_one();
	coordY = get_zero_or_one()*4 + get_zero_or_one()*2 + get_zero_or_one();

	return [coordX, coordY]

def get_zero_or_one():
	qr = qiskit.QuantumRegister(1) # call a quantum bit (or qubit)
	cr = qiskit.ClassicalRegister(1) # call a clasical bit
	program = qiskit.QuantumCircuit(qr, cr) # The quantum circuit is generated from the previous qubit and bit
	program.h(qr)

	program.measure(qr,cr) # The qubit is measured and stored in the classic bit.

	job = qiskit.execute( program, qiskit.BasicAer.get_backend('qasm_simulator') )
	num0 = job.result().get_counts()['0']
	num1 = job.result().get_counts()['1']
	return num0 < num1

def check(x, y):
	if (x == self.target[0]) & (y == self.target[1]):
		for i in range(self.gridNum):
			for j in range(self.gridNum):
				if self.grid[i][j] == 1:
					self.block[i][j].configure(state=DISABLED, image=self.holeGreen)
				else:
					self.block[i][j].configure(state=DISABLED)
		self.block[x][y].configure(image=self.pig)
	elif self.grid[x][y] == 1:
		if get_hadamard():
			for i in range(self.gridNum):
				for j in range(self.gridNum):
					if self.grid[i][j] == 1:
						self.block[i][j].configure(state=DISABLED, image=self.holeRed)
					else:
						self.block[i][j].configure(state=DISABLED)
		else:
			self.block[x][y].configure(state=DISABLED, image=self.holeGreen)
	else:
		sideTrapCount = 0
		if get_not():
			if y == 0:
				if x == 0:
					sideTrapCount = self.grid[x+1][y] + self.grid[x][y+1] + self.grid[x+1][y+1]
				elif x == self.gridNum-1:
					sideTrapCount = self.grid[x-1][y] + self.grid[x-1][y+1] + self.grid[x][y+1]
				else:
					sideTrapCount = self.grid[x-1][y] + self.grid[x+1][y] + self.grid[x-1][y+1] + self.grid[x][y+1] + self.grid[x+1][y+1]
			elif y == self.gridNum-1:
				if x == 0:
					sideTrapCount = self.grid[x][y-1] + self.grid[x+1][y-1] + self.grid[x+1][y]
				elif x == self.gridNum-1:
					sideTrapCount = self.grid[x-1][y-1] + self.grid[x][y-1] + self.grid[x-1][y]
				else:
					sideTrapCount = self.grid[x-1][y-1] + self.grid[x][y-1] + self.grid[x+1][y-1] + self.grid[x-1][y] + self.grid[x+1][y]
			elif x == 0:
				sideTrapCount = self.grid[x][y-1] + self.grid[x+1][y-1] + self.grid[x+1][y] + self.grid[x][y+1] + self.grid[x+1][y+1]
			elif x == self.gridNum-1:
				sideTrapCount = self.grid[x-1][y-1] + self.grid[x][y-1] + self.grid[x-1][y] + self.grid[x-1][y+1] + self.grid[x][y+1]
			else:
				sideTrapCount = self.grid[x-1][y-1] + self.grid[x][y-1] + self.grid[x+1][y-1] + self.grid[x-1][y] + self.grid[x+1][y] + self.grid[x-1][y+1] + self.grid[x][y+1] + self.grid[x+1][y+1]
			self.block[x][y].configure(state=DISABLED, text = '%d' % sideTrapCount)
		else:
			self.block[x][y].configure(state=DISABLED, text = "?")
			# sideTrapCount = self.grid[x-1][y-1] + self.grid[x][y-1] + self.grid[x+1][y-1]
			# 	+ self.grid[x-1][y] + self.grid[x][y]
			# 	+ self.grid[x-1][y+1] + self.grid[x][y+1] + self.grid[x+1][y+1]

def get_hadamard():
	qr = qiskit.QuantumRegister(1) # call a quantum bit (or qubit)
	cr = qiskit.ClassicalRegister(1) # call a clasical bit
	program = qiskit.QuantumCircuit(qr, cr) # The quantum circuit is generated from the previous qubit and bit
	program.h(qr)

	program.measure(qr,cr) # The qubit is measured and stored in the classic bit.

	job = qiskit.execute( program, qiskit.BasicAer.get_backend('qasm_simulator') )
	num0 = job.result().get_counts()['0']
	num1 = job.result().get_counts()['1']
	return num0 < num1

def get_not():
	qr = qiskit.QuantumRegister(1) # call a quantum bit (or qubit)
	cr = qiskit.ClassicalRegister(1) # call a clasical bit
	program = qiskit.QuantumCircuit(qr, cr) # The quantum circuit is generated from the previous qubit and bit

	# some problems here
	program.x(qr)
	program.h(qr)

	program.measure(qr, cr)

	job = qiskit.execute( program, qiskit.BasicAer.get_backend('qasm_simulator') )
	num0 = job.result().get_counts()['0']
	num1 = job.result().get_counts()['1']
	return num0 < num1

def clear():
	for item in self.frame.winfo_children():
		item.destroy()

# def showFrame():
# 	self.frame.pack()
root = Tk()
root.geometry('400x430')
root.title('P')
self.frame = Frame(root, bg='white')
self.frame.pack_propagate(0)
self.frame.pack(fill='both', expand='True')
create_panel()
create_grid()
root.mainloop()



