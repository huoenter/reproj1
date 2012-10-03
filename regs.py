class Reg(object):
	def __init__(self, name):
		self.__dict__.update(locals())
		del self.self
	
	def __str__(self):
		return str(self.name)
