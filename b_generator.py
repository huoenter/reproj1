import json
import template

OUTPUT = "test.cpp"
RULES = "./rules"

class Generator(object):

	def __init__(self, f):
		self.data = json.loads(open(f).read())
		self.code = "%s"

	def initialize(self):
		'''Headers, globals ...''' 
		self.code = self.code % template.init

	def parse(self, out):
		d = self.data
		self._functionName(d["name"])
		self._parseINS(d["name"], d)
		self._generate(out)

	def _functionName(self, k):
		self.code = self.code % template.funcName.format(k)

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
			self._getTaintMark(t["type"], t["pos"])

	def _generateForSink(self, sinks):
		for s in sinks:
			self._setTaintMark(s["type"], s["pos"])

	def _parseType(self, t):
		tt = []
		try: t = int(t)
		except: 
			return ["eflags"]
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

	def _generate(self, out):
		out.write(self.code % "")


if __name__ == "__main__":
	f = open(OUTPUT, "w")
	f.write(template.init)
	import os
	for j in os.listdir(RULES):
		if j.endswith(".json"):
			g = Generator(os.path.join(RULES, j))
			g.parse(f)
