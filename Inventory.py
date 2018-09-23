class Inventory():
	size = 0
	items = []
	def __init__(self,size):
		self.size = size
	def canPick(self):
		return self.size > len(items)
	def pick(self,item):
		self.items.append(item)
