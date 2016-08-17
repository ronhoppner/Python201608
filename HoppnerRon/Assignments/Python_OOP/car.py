class Car:
	def __init__(self, price, max_speed, fuel_level, mileage):
		self.price = price
		self.max_speed = max_speed
		self.fuel_level = fuel_level
		self.mileage = mileage
		if self.price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
		self.display_all()

	def display_all(self):
		print 'Price: ' + str(self.price)
		print 'Speed: ' + str(self.max_speed) + 'MPH'
		print 'Fuel Level: ' + self.fuel_level
		print 'Mileage: ' + str(self.mileage) + 'MPG'
		print 'Tax: ' + str(self.tax)

car1 = Car(35000, 100, 'Fumes', 40)
car2 = Car(40000, 100, 'Half', 50)
car3 = Car(5000, 100, 'Fumes', 40)
car4 = Car(95000, 180, 'Battery', 310)
car5 = Car(120000, 212, 'Full', 9)
car6 = Car(65000, 140, 'Half', 18)
