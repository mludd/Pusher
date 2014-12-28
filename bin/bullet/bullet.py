import pygame
import math
import json
import os

class Bullet(pygame.sprite.DirtySprite):
	def __init__(self, position, rotation, speed):
		pygame.sprite.DirtySprite.__init__(self)
		basePath = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..'))
		self.position = position
		self.originalPosition = self.position
		self.rotation = rotation
		self.speed = speed
		self.image, self.rect = self.load_png(basePath+'/images/bullet.png')
		self.originalImage = self.image
		self.screen = pygame.display.get_surface()
		self.sprite = pygame.sprite.RenderPlain(self)
		self.distance = 0
		self.type = 'projectile'

	def destruct(self, surface):
		self.dirty = 1
		self.sprite.clear(self.screen, surface)
		return surface

	def update(self, surface, clock, blocks):
		self.dirty = 1
		timedelta = clock.get_time()
		position = [
			self.position[0] + (math.sin(math.radians(self.rotation)) * self.speed * timedelta),
			self.position[1] + (math.cos(math.radians(self.rotation)) * self.speed * timedelta),
		]
		distX = self.originalPosition[0] - position[0]
		distY = self.originalPosition[1] - position[1]
		self.distance = math.sqrt(distX*distX + distY*distY)

		newBlocks = pygame.sprite.Group()
		for block in blocks:
			if not self.handle_collision(block, clock) or (block.type == "projectile" and block.reached_limit() != True):
				newBlocks.add(block)
			else:
				surface = block.destruct(surface)
		blocks = newBlocks

		self.position = position

		self.rect = pygame.rect.Rect(
			self.position[0],
			self.position[1],
			8,
			8
		)

	def reached_limit(self):
		if self.distance >= 300:
			return True
		return False

	def handle_collision(self, item, clock):
		colliding = pygame.sprite.collide_mask(item, self)
		if colliding and item.type != "player" and item.type != 'projectile':
			print "colliding!"
			return True
		return False

	def rotate_center(self):
		rotatedImage = pygame.transform.rotate(self.image, self.rotation + 180)
		rotatedImage.move_ip(
			self.image.rect.centerx,
			self.image.rect.centery
		)
		return rotatedImage, rotatedRect


	def load_png(self, name):
		""" Load image and return image object"""
		fullname = os.path.join('data', name)
		#dimensions = self.conf['dimensions']
		dimensions = [8,8]
		try:
			image = pygame.image.load(fullname)
			if image.get_alpha is None:
				image = image.convert()
			else:
				image = image.convert_alpha()
			image = pygame.transform.smoothscale(image, (dimensions[0], dimensions[1]))
		except pygame.error, message:
			print 'Cannot load image:', fullname
			raise SystemExit, message
		return image, image.get_rect()