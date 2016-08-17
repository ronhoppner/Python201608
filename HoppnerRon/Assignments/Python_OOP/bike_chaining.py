class Bike:
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def displayInfo(self):
		print 'Price is $' + str(self.price)
		print 'Max speed is ' + str(self.max_speed)
		print 'Miles is ' + str(self.miles)
		return self

	def ride(self):
		print 'Riding...'
		self.miles += 10
		return self

	def reverse(self):
		print 'Riding a bike backwards for some reason...'
		if self.miles >= 5: #no negative miles
			self.miles -= 5
		return self

bike1 = Bike(1000, 50)
bike1.ride().ride().reverse().reverse().reverse().displayInfo()








# bike1.ride()
# bike1.ride()
# bike1.ride()
# bike1.reverse()
# bike1.displayInfo()

