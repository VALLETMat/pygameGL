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
		return self.size > len(self.items)

	def pick(self,item):
		if(self.canPick()):
			self.items.append(item)

	def equip(self,items,index):

		item = items[index]
		if(item.type == 'Armor'):
			items.remove(item)
			if(self.Armor is not None):
				items.append(self.Armor)
			self.Armor = item
		elif(item.type == 'Weapon'):
			items.remove(item)
			if(self.Weapon is not None):
				items.append(self.Weapon)
			self.Weapon = item
		elif(item.type == 'Acessory'):
			items.remove(item)
			if(self.Weapon is not None):
				items.append(self.Weapon)
			self.Weapon = item

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
	def toss(self,pos,item,board):
		cell = board.cells[pos[0]][pos[1]]
		if cell.item is None:
			return
		for space in range(self.size):
			if items[range] == item:
				items[range] = None
				cell.item  = item

	def getHP(self):
		HP = 0
		if self.Armor is not None:
			HP += self.Armor.HP
		if self.Weapon is not None:
			HP += self.Weapon.HP
		if self.Accessory is not None:
			HP += self.Accessory.HP
		return HP
	def getDEF(self):
		DEF = 0
		if self.Armor is not None:
			DEF += self.Armor.DEF
		if self.Weapon is not None:
			DEF += self.Weapon.DEF
		if self.Accessory is not None:
			DEF += self.Accessory.DEF
		return DEF
	def getATK(self):
		ATK = 0
		if self.Armor is not None:
			ATK += self.Armor.ATK
		if self.Weapon is not None:
			ATK += self.Weapon.ATK
		if self.Accessory is not None:
			ATK += self.Accessory.ATK
		return ATK
class Item():
	name = None
	HP = 0
	DEF = 0
	ATK = 0
	value = 0
	type = 'Other'
	def interract(self,cell,player):
		cell.item = None
		player.inventory.pick(self)
class Armor(Item):
	tier = 0
	type = 'Armor'
class Weapon(Item):
	tier = 0
	type = 'Weapon'
class Accessory(Item):
	type ='Accessory'
	tier = 0


class LongSword(Weapon):
	ATK = 3
	sprite_path = os.path.join(resource_path, 'sword.png') # The image folder path
	def inspect(self):
		return "a LongSword"
	def name(self):
		return "LongSword"

class Ring(Armor):
	DEF = 2
	sprite_path = os.path.join(resource_path, 'ring.png') # The image folder path
	def inspect(self):
		return "A ring"
	def name(self):
		return "Ring"

class Rags(Armor):
	sprite_path = os.path.join(resource_path, 'sword.png') # The image folder path
	def inspect(self):
		return "Rags"
	def name(self):
		return "Rags"

class Stick(Weapon):
	sprite_path = os.path.join(resource_path, 'sword.png') # The image folder path
	def inspect(self):
		return "A stick"
	def name(self):
		return "Stick"

class PlateArmor(Armor):
	DEF = 3
	sprite_path = os.path.join(resource_path, 'armor.png')
	def inspect(self):
		return "I hope it fits !"
	def name(self):
		return "Stick"
