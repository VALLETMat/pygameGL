import Entity
import os
import pygame

current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'sprite') # The resource folder path

class Cell:
	x = 0
	y = 0
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __str__(self):
		return "("+str(self.x)+","+str(self.y)+")"
	def canCross(self):
		return True
	def inspect(self):
		return
	def interract(self,player):
		return
class Floor (Cell):
	occupying = None 	#entity on the floor
	item = None			#item on the floor
	def __init__(self, x, y, occupying):
		self.occupying = occupying
		Cell.__init__(self,x,y)
	def canCross(self):
		return self.occupying is None
	def interract(self,player):
		if self.item is not None and player == self.occupying:
			return self.item.interract(player)
		if self.occupying is not None:
			return self.occupying.interract(player)
	def inspect(self):
		if self.occupying is not None:
			return self.occupying.inspect()
		if self.item is not None:
			return self.item.inspect()
		return "Nothing interresting";
class Wall (Cell):
	occupying = None 	#entity on the floor
	item = None			#item on the floor
	def __init__(self, x, y):
		Cell.__init__(self,x,y)
	def canCross(self):
		return False
	def interract(self,player):
		return

class WoodenFloor(Floor):
	sprite_path = os.path.join(resource_path, 'floor.png') # The image folder path
class StairUp(Floor):
	underneath_sprite_path = 	sprite_path = os.path.join(resource_path, 'floor.png') # The image folder path
	sprite_path = os.path.join(resource_path, 'stairUp.png') # The image folder path
class StairDown(Floor):
	sprite_path = os.path.join(resource_path, 'stairDown.png') # The image folder path
class BrickWall(Wall):
	sprite_path = os.path.join(resource_path, 'wall.png') # The image folder path
