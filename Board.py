from Cell import *
from Inventory import *
from Entity import *

class Board():
	entities = None
	boardSize = 10
	cells = None
	def __init__(self, size):
		self.entities = []
		self.boardSize = size
		self.cells = [None] * self.boardSize

		for i in range(self.boardSize):
			self.cells[i] = [None] * self.boardSize

class Game():
	boards =  []
	def __init__(self):
		b1 = Board(10)
		b2 = Board(10)

		b1 = self.genereLevel(b1,1,1,8,8)
		b1.cells[5][4] = BrickWall(5,4)
		b1.cells[6][4] = BrickWall(6,6)
		b1.cells[7][4] = BrickWall(7,7)
		b1.cells[8][4] = BrickWall(8,4)

		b1.cells[4][4] = BrickWall(4,4)
		b1.cells[4][5] = BrickWall(4,5)
		b1.cells[4][7] = BrickWall(4,6)
		b1.cells[4][8] = BrickWall(4,7)

		for i in range (b1.boardSize):
			for j in range (b1.boardSize):
				if b1.cells[i][j] is None:
					b1.cells[i][j] = WoodenFloor(i,j,None)

		b1.cells[3][3].item = LongSword()
		b1.cells[7][2].item = Ring()
		rat1 = Rat(b1.cells[7][7])
		b1.cells[7][7].occupying = rat1
		b1.entities.append(rat1)

		b2 = self.genereLevel(b2,8,8,1,1)
		b2.cells[4][8] = BrickWall(4,8)
		b2.cells[4][7] = BrickWall(4,7)
		b2.cells[4][6] = BrickWall(4,6)
		b2.cells[4][5] = BrickWall(4,5)
		b2.cells[4][4] = BrickWall(4,4)
		b2.cells[4][3] = BrickWall(4,3)

		b2.cells[5][4] = BrickWall(5,4)
		b2.cells[6][4] = BrickWall(6,5)

		b2.cells[1][1] = StairUp(1,1,None)

		for i in range (b2.boardSize):
			for j in range (b2.boardSize):
				if b2.cells[i][j] is None:
					b2.cells[i][j] = WoodenFloor(i,j,None)

		print(b2.entities)

		b2.cells[5][5].item = PlateArmor()

		rat2 = Rat(b2.cells[5][7])
		rat3 = Rat(b2.cells[7][7])

		b2.entities.append(rat2)
		b2.entities.append(rat3)

		self.boards.append(b1)
		self.boards.append(b2)

	def genereLevel(self,b,stairUpX,stairUpY,stairDownX,stairDownY):
		b = Board(10)
		for i in range(10):
			b.cells[0][i] = BrickWall(0,i)
			b.cells[i][0] = BrickWall(i,0)
			b.cells[9][i] = BrickWall(9,i)
			b.cells[i][9] = BrickWall(i,9)
		b.cells[stairUpX][stairUpY] = StairUp(stairUpX,stairUpY,None)
		b.cells[stairDownX][stairDownY] = StairUp(stairDownX,stairDownY,None)
		return b
