class Screen(object):
	def __init__(self, cfg):
		pygame.init()
		pygame.display.set_mode((cfg.width, cfg.height))
		pygame.display.set_caption(cfg.caption)
		#pygame.mouse.set_visible(False)

		self.screen = pygame.display.get_surface()
		self.backgroundImage = self.loadBackground()


		self.x = 0
		self.y = 0

	def loadBackground(self):
		return pygame.image.load(os.path.join("res", "space.bmp"))

	def draw(self):
		self.screen.blit(self.backgroundImage, (0,0))