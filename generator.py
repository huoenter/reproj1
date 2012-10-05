import json
class Generator(object):

	def __init__(self, f):
		self.data = json.loads(open(f).read())

	def parse(self):
		print self.data


g = Generator("instructions.json")
g.parse()
