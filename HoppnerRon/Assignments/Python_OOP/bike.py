class Bike:
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def displayInfo(self):
		print 'Price is $' + str(self.price)
		print 'Max speed is ' + str(self.max_speed)
		print 'Miles is ' + str(self.miles)

	def ride(self):
		print 'Riding...'
		self.miles += 10

	def reverse(self):
		print 'Riding a bike backwards for some reason...'
		if self.miles >= 5: #no negative miles
			self.miles -= 5

bike1 = Bike(1000, 50)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(2000, 500)
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3 = Bike(100, 2)
bike3.reverse()
bike3.reverse()
bike3.displayInfo()