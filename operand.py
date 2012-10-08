class Operand(object):
	def __init__(self, name, t, pos):
		self.__dict__.update(locals())
		del self.self

	def toJson(self):
		d = {"name" : self.name,
			 "type" : self.t,
			 "pos" :  self.pos}
		return d
