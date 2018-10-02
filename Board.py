from Cell import *
from Inventory import *
from Entity import *

class Board():
	entities = []
	boardSize = 10
	cells = None
	def __init__(self, size):
		self.boardSize = size
		self.cells = [None] * self.boardSize

		for i in range(self.boardSize):
			self.cells[i] = [None] * self.boardSize

		self.cells[8][8] = StairDown(8,8,None)
		for i in range(10):
			self.cells[0][i] = BrickWall(0,i)
			self.cells[i][0] = BrickWall(i,0)
			self.cells[9][i] = BrickWall(9,i)
			self.cells[i][9] = BrickWall(i,9)

		self.cells[5][4] = BrickWall(5,4)
		self.cells[6][4] = BrickWall(6,6)
		self.cells[7][4] = BrickWall(7,7)
		self.cells[8][4] = BrickWall(8,4)

		self.cells[4][4] = BrickWall(4,4)
		self.cells[4][5] = BrickWall(4,5)
		self.cells[4][7] = BrickWall(4,6)
		self.cells[4][8] = BrickWall(4,7)
		self.cells[1][1] = StairUp(1,1,None)
		for i in range (self.boardSize):
			for j in range (self.boardSize):
				if self.cells[i][j] is None:
					self.cells[i][j] = WoodenFloor(i,j,None)
		self.cells[3][3].item = LongSword()
		self.cells[7][2].item = Ring()
		rat = Rat(self.cells[7][7])
		self.entities.append(rat)
