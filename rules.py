from base import INS
from operand import Operand

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

class SUB(ADD):
	pass

SUB().toJson()
