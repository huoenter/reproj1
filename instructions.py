class INS(object):
	def __init__(self, name):
		self.__dict__.update(locals())
		del self.self
	
	def __str__(self):
		return "INS: " + self.name

class ADD(INS):
	'''
	This is a class that fits the most commonly used
	instructions implemented already.
	This class of instructions have a source and a dest
	operands or one more (ADC). 
	'''
	def __init__(self, name="ADD"):
		INS.__init__(self, name)
		self.source = ["mem", "reg", "imm"]
		self.dest = ["mem", "reg"]

class ADC(ADD):
	def __init__(self, name="ADC"):
		ADD.__init__(self, name)
		self.carry = ["reg"]

class Generator(object):
	def __init__(self, sth):
		pass

a = ADC()
print a.dest
