class Vector(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def __repr__(self):
		return "Vector(%s, %s)" % (self.x, self.y)
			
	def __add__(self, b):
		""" Addition. Returns a new vector. """
		return Vector(self.x + b.x, self.y + b.y)

	def __sub__(self, b):
		""" Subtraction. Returns a new vector. """
		return Vector(self.x - b.x, self.y - b.y)

	def __mul__(self, b):
		""" Multiplication by a scalar
		
		Note that the scalar must be to the right.
		
		"""
		try:
			b = float(b)
			return Vector(self.x * b, self.y * b)
		except ValueError:
			print "Oops! Right value must be a float"
			raise

	def magnitude(self):
		""" Returns the magnitude of the vector. """
		return math.sqrt(self.x ** 2 + self.y ** 2)

	def normalized(self):
		""" Returns a new vector with the same direction but magnitude 1. """
		try:
			m = self.magnitude()
			return self / m
		except ZeroDivisionError:
			print "Oops! Cannot normalize a zero-vector"
			raise

	def copy(self):
		""" Returns a copy of the vector. """
		return Vector(self.x, self.y)
	def __div__(self, b):
		""" Dividing a vector by b """
		try:
			if b == 0:
				return Vector(0,0)
			b = float(b)
			return Vector(self.x/b, self.y/b)
		except ValueError:
			print "Oops! Right value must be a float"
			raise

	def __getitem__(self, key):
		""" Get item at index "key" """
		if key == 0:
			return int(self.x)
		elif key == 1:
			return int(self.y)
		else:
			print "Oops! Right value must be a float"
			raise

	def __len__(self):
		""" Get lenght of vector """
		return 2

	def diff(self, b):
		""" Get distance between two vectors """
		return (self - b).magnitude()

	def angle(self):
		""" Calculates the angle of the vector (radians) """ 
		return math.atan2(self.x, self.y)

	def rotate(self, theta):
		""" Rotatates the vector "theta" degrees (radians) """
		return Vector(self.x * math.cos(theta) - self.y * math.sin(theta), self.x * math.sin(theta) + self.y * math.cos(theta))
