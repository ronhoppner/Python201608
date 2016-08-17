#SECTION 1

class MathDojo:
	def __init__(self):
		self.total = 0
		
	def add(self, *args):
		for a in args:
			self.total += a
		return self
		
	def subtract(self, *args):
		for a in args:
			self.total -= a
		return self
	
	def result(self):
		print self.total
		return self

md = MathDojo()
md.add(2).add(2,3).subtract(3,2).result()

#SECTION 2 - modified to accept listes and tuples as values for addition/subtraction

class MathDojo2:
	def __init__(self):
		self.total = 0
	
	def add(self, *args):
		for a in args:
			if type(a) is int:
				self.total += a
		for a in args:
			if type(a) is list:
				for i in a:
					self.total += i
		for a in args:
			if type(a) is tuple:
				for i in a:
					self.total += i
		return self
		
	def subtract(self, *args):
		for a in args:
			if type(a) is int:
				self.total -= a
		for a in args:
			if type(a) is list:
				for i in a:
					self.total -= i
		for a in args:
			if type(a) is tuple:
				for i in a:
					self.total -= i
		return self
	
	def result(self):
		print self.total
		return self

md2 = MathDojo2()
md2.add([1],3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()