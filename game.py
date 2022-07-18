from tkinter import *
from functools import partial
from itertools import product

import qrandom
import qiskit # call the qiskit's module
import json

class self:
	width = 50
	gridNum = 10
	trapNum = 10
	block = []
	grid = []

def create_panel(root):
	self.block = [[Button(root, command=partial(check, j, i)) for i in range(self.gridNum)] for j in range(self.gridNum)]
	for i in range(self.gridNum):
		for j in range(self.gridNum):
			self.block[i][j].place(x=i*self.width, y=j*self.width, width=self.width, height=self.width)

def create_grid():
	self.grid = [[0 for j in range(self.gridNum)] for i in range(self.gridNum)]
	set_traps()

def set_traps():
	trapCount = 0;
	while trapCount < self.trapNum:
		coordTemp = get_random_coords()
		# check if the coord already contains a trap
		if self.grid[coordTemp[0]][coordTemp[1]] == 0:
			self.grid[coordTemp[0]][coordTemp[1]] = 1
			trapCount += 1

def get_random_coords():
	# use ANU to get quantum random numbers
	coordTemp = qrandom.sample(range(self.gridNum), 2)
	return coordTemp

def check(x, y):
	if self.grid[x][y] == 1:
		if get_hadamard():
			for i in range(self.gridNum):
				for j in range(self.gridNum):
					if self.grid[i][j] == 1:
						print(i, j)
						self.block[i][j].configure(state=DISABLED, highlightbackground="red")
					else:
						self.block[i][j].configure(state=DISABLED)
		else:
			self.block[x][y].configure(state=DISABLED, highlightbackground="green")
			print ("survive")

def get_hadamard():
	qr = qiskit.QuantumRegister(1) # call a quantum bit (or qubit)
	cr = qiskit.ClassicalRegister(1) # call a clasical bit
	program = qiskit.QuantumCircuit(qr, cr) # The quantum circuit is generated from the previous qubit and bit
	program.h(qr)

	program.measure(qr,cr) # The qubit is measured and stored in the classic bit.

	job = qiskit.execute( program, qiskit.BasicAer.get_backend('qasm_simulator') )
	num0 = job.result().get_counts()['0']
	num1 = job.result().get_counts()['1']
	print(job.result().get_counts())
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
	print(job.result().get_counts())
	return num0 < num1





