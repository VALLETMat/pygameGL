import os
import pygame


current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'sprite') # The resource folder path

class Entity:
	position = None #cell where the entity lies : None if not here yet
	def interract():
		return None
	def __init__(self,cell):
		 self.position = cell
		 cell.occupying = self
	#modifier en fct de l'origine (ici en bas a gauche)
	def moveDown(self,board):
		x = self.position.x;
		y = self.position.y;
		self.move(board,x,y+1,x,y)
	def moveUp(self, board):
		x = self.position.x;
		y = self.position.y;
		self.move(board,x,y-1,x,y)
	def moveLeft(self,board):
		x = self.position.x;
		y = self.position.y;
		self.move(board,x-1,y,x,y)
	def moveRight(self,board):
		x = self.position.x;
		y = self.position.y;
		self.move(board,x+1,y,x,y)
	def move(self,board,x,y,oldx,oldy):
		if(not posIsCorrect(board,x,y)):
			return ;
		if(not board.cells[x][y].canCross()):
			return ;
		self.position = board.cells[x][y]
		board.cells[oldx][oldy].occupying = None
		board.cells[x][y].occupying = self
def posIsCorrect(board, x, y):
	return x>= 0 and y >= 0 and x < board.boardSize and y < board.boardSize;

class Player(Entity):
	sprite_path = os.path.join(resource_path, 'player_2.png')
	PV= 10;
	DEF = 1;
	ATK=1;
	inventory = None;
	def interract(player) :
		return openInventory()
	def openInventory(player) :
		return;

class Ennemy(Entity):
	PV= 10;
	DEF = 1;
	def interract(player) :
		return self.attacked(player)
	def attacked(player):
		return attack(player);
	def attack(player):
		return;
