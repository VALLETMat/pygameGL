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
			if(self.armor is not None)
				self.unequip(self.armor)
			self.Armor = item
		if(item.type == 'Weapon'):
			if(self.armor is not None)
				self.unequip(self.Weapon)
			self.Weapon = item
		if(item.type == 'Acessory'):
			if(self.armor is not None):
				self.unequip(self.Accessory)
			self.Accessory = item

	def unequip(self,item):
		if(size == len(items))
			return
		if(item.type == 'Armor'):
			items[len(items)] = Armor
			Armor = None
		if(item.type == 'Weapon'):
			items[len(items)] = Weapon
			Weapon = None
		if(item.type == 'Acessory'):
			items[len(items)] = Accessory
			Accessory = None

class Item():
	name = None
	PV = 0
	DEF = 0
	ATT = 0
	value = 0
	type = 'Other'
class Armor(Item):
	tier = 0
	type = 'Armor'
class Weapon(Item):
	tier = 0
	type = 'Weapon'
class Accessory(Item):
	tier = 0
	type ='Accessory'
