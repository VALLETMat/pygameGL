from Cell import *
from Inventory import *

class Board():

	boardSize = 10
	cells = None
	def __init__(self, size):
		self.boardSize = size
		self.cells = [None] * self.boardSize

		for i in range(self.boardSize):
			self.cells[i] = [None] * self.boardSize

		self.cells[8][8] = StairDown(8,8,None)
		self.cells[4][4] = BrickWall(4,4)
		self.cells[1][1] = StairUp(1,1,None)
		for i in range (self.boardSize):
			for j in range (self.boardSize):
				if self.cells[i][j] is None:
					self.cells[i][j] = WoodenFloor(i,j,None)
		self.cells[3][3].item = LongSword()
