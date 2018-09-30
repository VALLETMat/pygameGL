import os
import pygame

current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'sprite') # The resource folder path

class Inventory():
	size = 0
	items = []
	Armor = None
	Weapon = None
	Accessory = None

	def __init__(self,size):
		self.size = size

	def canPick(self):
		return self.size > len(items)

	def pick(self,item):
		if(self.canPick()):
			self.items.append(item)

	def equip(self,item):
		if(item.type == 'Armor'):
			if(self.armor is not None):
				self.unequip(self.armor)
			self.Armor = item
		if(item.type == 'Weapon'):
			if(self.armor is not None):
				self.unequip(self.Weapon)
			self.Weapon = item
		if(item.type == 'Acessory'):
			if(self.armor is not None):
				self.unequip(self.Accessory)
			self.Accessory = item

	def unequip(self,item):
		if(self.size == len(self.items)):
			return
		if(item.type == 'Armor'):
			self.items[len(self.items)] = self.Armor
			self.Armor = None
		if(item.type == 'Weapon'):
			self.items[len(self.items)] = self.Weapon
			self.Weapon = None
		if(item.type == 'Acessory'):
			self.items[len(self.items)] = self.Accessory
			self.Accessory = None

class Item():
	name = None
	HP = 0
	DEF = 0
	ATT = 0
	value = 0
	type = 'Other'
	def interract(self,player):
		player.inventory.pick(self)
class Armor(Item):
	tier = 0
	type = 'Armor'
class Weapon(Item):
	tier = 0
	type = 'Weapon'
class Accessory(Item):
	tier = 0
	type ='Accessory'
class LongSword(Weapon):
	sprite_path = os.path.join(resource_path, 'sword.png') # The image folder path
	def inspect(self):
		return "a LongSword"

class Rags(Armor):
	def inspect():
		return "Rags"
class Stick(Weapon):
	def inspect():
		return "A stick"
