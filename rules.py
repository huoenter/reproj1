import json
from operand import Operand

class INS(object):
	def __init__(self):
		self.name = str(self.__class__).split(".")[1].split("'")[0]
		self.tap = []
		self.sink = []
		self.dependency = []

	def toJson1(self, lst):
		return [e.toJson() for e in lst] 

	def toJson(self):
		d = {
			"name" : self.name,
			"tap" : self.toJson1(self.tap),
			"sink" : self.toJson1(self.sink),
			"dependency" : self.toJson1(self.dependency)
			}

		f = open("rules/%s.json" % self.name, "w")
		f.write(json.dumps(d, indent=1))
		f.close()

class ADD(INS):
	def __init__(self):
		super(ADD, self).__init__()
		self.tap = [
						Operand("dest", 6, 0), 
						Operand("source", 7, 1)
					]
		self.sink = [
						Operand("dest", 6, 0), 
						Operand("eflags", -1, -1)
					]

ADD().toJson()


class ADC(ADD):
	def __init__(self):
		super(ADC, self).__init__()
		self.tap.append(Operand("CX", -1, 2))

ADC().toJson()
