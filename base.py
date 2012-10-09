import json

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

