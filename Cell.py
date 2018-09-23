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

class Floor (Cell):
	occupying = None 	#entity on the floor
	item = None			#item on the floor
	def __init__(self, x, y, occupying):
		self.occupying = occupying
		Cell.__init__(self,x,y)
	def canCross(self):
		print (self.occupying is None)
		return self.occupying is None;
	def interract():
		if self.occupying is not None:
			return occupying.interract(self)
		if self.occupying is not None:
			return occupying.interract(self)

class Wall (Cell):
	occupying = None 	#entity on the floor
	item = None			#item on the floor
	def __init__(self, x, y):
		Cell.__init__(self,x,y)
	def canCross(self):
		return False;
	def interract():
		return;

class WoodenFloor(Floor):
	sprite_path = os.path.join(resource_path, 'floor.png') # The image folder path
class StairUp(Floor):
	sprite_path = os.path.join(resource_path, 'stairUp.png') # The image folder path
class StairDown(Floor):
	sprite_path = os.path.join(resource_path, 'stairDown.png') # The image folder path
class BrickWall(Wall):
	sprite_path = os.path.join(resource_path, 'wall.png') # The image folder path
