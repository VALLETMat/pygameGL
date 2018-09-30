import os
import pygame
from Inventory import *

current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'sprite') # The resource folder path

class Entity:
	position = None #cell where the entity lies : None if not here yet
	last_position = None #cell where the entity was (private)
	def interract(self,player):
		return
	def inspect(self):
		return position
	def act():
		return
	def __init__(self,cell):
		self.last_position = None
		self.position = cell
		cell.occupying = self
	#modifier en fct de l'origine (ici en bas a gauche)
	def moveDown(self,board):
		if(not posIsCorrect(board,self.position.x,self.position.y+1) or not board.cells[self.position.x][self.position.y+1].canCross()):
			return
		self.last_position = board.cells[self.position.x][self.position.y]
		self.position.y+=1
	def moveUp(self, board):
		if(not posIsCorrect(board,self.position.x,self.position.y-1) or not board.cells[self.position.x][self.position.y-1].canCross()):
			return
		self.last_position = board.cells[self.position.x][self.position.y]
		self.position.y-=1
	def moveLeft(self,board):
		if(not posIsCorrect(board,self.position.x-1,self.position.y) or not board.cells[self.position.x-1][self.position.y].canCross()):
			return
		self.last_position = board.cells[self.position.x][self.position.y]
		self.position.x-=1
	def moveRight(self,board):
		if(not posIsCorrect(board,self.position.x+1,self.position.y)) or not board.cells[self.position.x+1][self.position.y].canCross():
			return
		self.last_position = board.cells[self.position.x][self.position.y]
		self.position.x+=1
	def applyMove(self,board):
		if(self.last_position is not None):
			self.last_position.occupying = None
		board.cells[self.position.x][self.position.y].occupying = self
def posIsCorrect(board, x, y):
	return x>= 0 and y >= 0 and x < board.boardSize and y < board.boardSize

class Player(Entity):
	sprite_path = os.path.join(resource_path, 'player.png')
	HP= 10
	DEF = 1
	ATK=1

	inventory = Inventory(10)
	def interract(self,player) :
		return openInventory()
	def openInventory(self) :
		print("loot")
	def attack(self,entity):
		print("BIM")
	def inspect(self):
		return "HP : "+str(self.HP)+" DEF : "+ str(self.DEF)
class Ennemy(Entity):
	HP= 10
	DEF = 1
	ATT = 1
	def interract(self,player) :
		if self.areNeighbours(player):
			return player.attack(self)
	def attack(self,player):
		print("BAM")
	def inspect(self):
		return "HP : "+str(self.HP)+" DEF : "+ str(self.DEF)
	def act(self,player,board):
		print("act")
		if self.areNeighbours(player):
			self.attack(player)
		self.moveToPlayer(player,board)
	def moveToPlayer(self,player,board):
		if abs(player.position.y - self.position.y)>abs(player.position.x - self.position.x):
			if player.position.y > self.position.y:
				self.moveDown(board)
			elif player.position.y <self.position.y:
				self.moveUp(board)
		else:
			if player.position.x > self.position.x:
				self.moveRight(board)
			elif player.position.x < self.position.x:
				self.moveLeft(board)
		self.applyMove(board)
	def areNeighbours(self,player):
		return (abs(self.position.x - player.position.x)+abs(self.position.y - player.position.y) == 1)
class Rat(Ennemy):
	sprite_path = os.path.join(resource_path, 'rat.png')
