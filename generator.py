import json
class Generator(object):

	def __init__(self, f):
		self.data = json.loads(open(f).read())
		self.code = "%s"

	def initialize(self):
	'''Headers, globals ...'''
		pass

	def parse(self):
		for k, v in self.data.items():
			self._parseINS(k, v)

	def _parseINS(self, k, v):
		self._checkDependency(v["dependency"])
		self._generateForTap(v["tap"])
		self._generateForSink(v["sink"])

	def _checkDependency(self, dep):
		if dep == None:
			pass
		else: pass			

	def _generateForTap(self, taps):
		for k, v in taps.items():
			self._getTaintMark(v["type"], v["pos"])

	def _generateForSink(self, sinks):
		for k, v in sinks.keys():
			self._setTaintMark(v["type"], v["pos"])

	def _parseType(self, t):
		if 

	def _getTaintMark(self, t, p):
		for tt in self._parseType(t):
		self.code = _generateCondition(self.code, t)
		self.code = _generateGettingBody(self.code, p)

	def _setTaintMark(self, t, p):
		self.code = _generateCondition(self.code, t)
		self.code = _generateSettingBody(self.code, p)
		
	def _generateCondition(self, code, t):
		return self.code % template.conditiont[t]


g = Generator("instructions.json")
g.parse()
