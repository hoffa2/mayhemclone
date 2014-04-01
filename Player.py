class Player():
	def __init__(self, num, shotGroup):
		self.num = num
		self.spaceship = Spaceship(100, 100, num, -1, -1)
		self.shots = shotGroup
		self.lock = False
		
	
	def update(self):
		self.spaceship.pos += self.spaceship.vel
		self.spaceship.vel *= 0.95

	def force(self, v):
		self.spaceship.vel += v
	
	def fire(self):
		if(self.lock):
			return
		shot = Lazer(self.spaceship.pos, self.spaceship.angle)
		self.shots.add(shot)
		self.lock = True
		pygame.time.set_timer(USEREVENT+self.num, 200)
		print "player", self.num, "fire" 


	def thrust(self):
		print "player", self.num, "thrust" 
		self.spaceship.vel += (self.spaceship.vel + self.spaceship.angle).normalized()

	def turn_right(self):
		print "player", self.num, "right"
		self.spaceship.vel = self.spaceship.vel.rotate(math.radians(2.5))
		self.spaceship.angle = self.spaceship.angle.rotate(math.radians(2.5))
		#self.spaceship.vel = Vector(math.cos(tmp.angle()),-math.sin(tmp.angle()))

	def turn_left(self):
		print "player", self.num, "left" 
		self.spaceship.vel = self.spaceship.vel.rotate(math.radians(-2.5))
		self.spaceship.angle = self.spaceship.angle.rotate(math.radians(-2.5))
		# = Vector(math.cos(tmp.angle()),-math.sin(tmp.angle()))