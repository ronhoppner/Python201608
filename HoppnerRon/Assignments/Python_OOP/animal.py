class Animal:
	def __init__(self, name):
		self.name = name
		self.health = 100
		print name

	def walk(self):
		print "Walkin'..."
		self.health -= 1
		return self

	def run(self):
		print "Running..."
		self.health -= 5
		return self

	def display_health(self):
		print 'Current health is: ' + str(self.health)

class Dog(Animal):
	def __init__(self, name):
		self.health = 150
		print name

	def pet(self):
		print "Good boy!"
		self.health += 5
		return self

class Dragon(Animal):
	def __init__(self, name):
		self.health = 170
		print name

	def fly(self):
		print 'I\'m flying!'
		self.health -= 10
		return self


animal = Animal('PetName')
animal.walk().walk().walk().run().run().display_health()

dog = Dog('ImADog')
dog.walk().walk().walk().run().run().pet().display_health()

dragon = Dragon('ImADragon')
dragon.walk().walk().walk().run().run().fly().fly().display_health()
