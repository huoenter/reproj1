import json
import template

class Generator(object):

	def __init__(self, f):
		self.data = json.loads(open(f).read())
		self.code = "%s"

	def initialize(self):
		'''Headers, globals ...''' 
		pass

	def parse(self):
		print self.data
		for k, v in self.data.items():
			self._parseINS(k, v)

	def _parseINS(self, k, v):
#		self._checkDependency(v["dependency"])
		self._generateForTap(v["tap"])
		self._generateForSink(v["sink"])

	def _checkDependency(self, dep):
		if dep == None:
			pass
		else: pass			

	def _generateForTap(self, taps):
		for t in taps:
			for k, v in t.items():
				self._getTaintMark(v["type"], v["pos"])

	def _generateForSink(self, sinks):
		for s in sinks:
			for k, v in s.items():
				self._setTaintMark(v["type"], v["pos"])

	def _parseType(self, t):
		tt = []
		try: t = int(t)
		except: return tt
		if t & 4 != 0: tt.append("reg")
		if t & 2 != 0: tt.append("mem")
		if t & 1 != 0: tt.append("imm")
		return tt

	def _getTaintMark(self, t, p):
		l = len(self._parseType(t))
		for tt in self._parseType(t):
			self.code = self._generateGettingBody(self.code, tt, p)
			l -= 1
			if l > 0: self.code = self.code % "\nelse\n%s"
		if p > 0: self.code = self.code % (template.unknown.format(p))

	def _setTaintMark(self, t, p):
		l = len(self._parseType(t))
		for tt in self._parseType(t):
			self.code = self._generateSettingBody(self.code, tt, p)
			l -= 1
			if l > 0: self.code = self.code % "\nelse\n%s"

		if p > 0: self.code = self.code % (template.unknown.format(p))

	def _generateGettingBody(self, code, t, p):
		return self.code % (template.getMark[t].format(p))

	def _generateSettingBody(self, code, t, p):
		return self.code % (template.setMark[t].format(p))

	def generate(self):
		print self.code % ""


g = Generator("instructions.json")
g.parse()
g.generate()
