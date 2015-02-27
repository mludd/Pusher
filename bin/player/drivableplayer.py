import json
import pygame
import block
import player
import math
import bullet
import keymap

class DrivablePlayer(player.Player):
	def __init__(self, position, rotation, direction, speed, keyboard):
		player.Player.__init__(self, position, rotation, direction, speed)
		self.rotation = rotation
		self.oldRotation = rotation
		self.rotationDrift = 0
		self.position = position
		self.direction = direction
		self.speed = speed
		self.keymap = keymap.Keymap(keyboard)
		self.type = "player"
		self.totalTimer = 0
		self.lastShot = False

	def check_move(self):
		return True

	def accelerate(self, clock):
		td = clock.get_time()
		maxSpeed = 0.5
		radians = self.speed * 3.14159
		rate = math.cos(radians) + 0.5
		increase = rate * float(td)/float(5000)
		if self.speed + increase <= 0.4:
			self.speed += increase
		else:
			self.speed = 0.4

	def reverse(self, clock):
		td = clock.get_time()
		decrease = float(td)/float(5000)
		if self.speed - decrease >= -0.2:
			self.speed -= decrease
		else:
			self.speed = -0.2

	def left(self, clock):
		td = clock.get_time()
		self.rotation += (0.3 * td)
		if self.rotation > 360:
			self.rotation = self.rotation % 360

	def right(self, clock):
		td = clock.get_time()
		self.rotation -= (0.3 * td)
		if self.rotation < 0:
			self.rotation = (360 - self.rotation)

	def slow(self, clock):
		td = clock.get_time()
		decrease = float(td)/ float(7000)
		if self.speed >= decrease:
			self.speed -= decrease
		elif self.speed <= -decrease:
			self.speed += decrease
		else:
			self.speed = 0

	def shoot(self, clock, origin):
		td = clock.get_time()
		self.totalTimer += td
		print "totalTimer: ", self.totalTimer
		print "lastShot: ", self.lastShot
		print self.totalTimer - self.lastShot
		
		if self.totalTimer - self.lastShot > 500:
			self.lastShot = self.totalTimer
			offset = self.image.get_rect().center
			adjustedOrigin = [
				origin[0] + offset[0] + offset[0] * math.sin(math.radians(self.rotation)),
				origin[1] + offset[1] + offset[1] * math.cos(math.radians(self.rotation))
			]
			return bullet.Bullet(adjustedOrigin, self.rotation, 0.4)

	def move(self):
		pass

	def handle_collision(self, item, clock):
		td = clock.get_time()
		colliding = pygame.sprite.collide_mask(item, self)
		if colliding and item.type == 'dynamic_prop':
			print colliding

			item.position = [
				item.position[0] + (math.sin(math.radians(self.direction)) * self.speed * td),
				item.position[1] + (math.cos(math.radians(self.direction)) * self.speed * td)
			]

			item.speed = self.speed * 1
			item.direction = self.direction


	def update(self, surface, clock, blocks, keys):
		self.totalTimer += clock.get_time()
		if self.totalTimer < 0:
			self.totalTimer = 0
		for block in self.read_input(keys, clock):
			blocks.add(block)

		self.dirty = 1
		self.slow(clock)

		for block in blocks:
			self.handle_collision(block, clock)

		timedelta = clock.get_time()
		self.rotationDrift = self.oldRotation - self.rotation

		if self.rotationDrift > 0:
			drift = [
				math.sin(math.radians(self.rotation +90)) * self.speed * timedelta,
				math.cos(math.radians(self.rotation +90)) * self.speed * timedelta
			]
		else:
			drift = [
				0,
				0
			]
		position = [
			0.25 * drift[0] + self.position[0] + (math.sin(math.radians(self.rotation)) * self.speed * timedelta),
			0.25 * drift[1] + self.position[1] + (math.cos(math.radians(self.rotation)) * self.speed * timedelta)
		]
		self.position = position

		self.oldRotation = self.rotation
		self.rect = pygame.rect.Rect(
			position[0],
			position[1],
			self.conf['dimensions'][0],
			self.conf['dimensions'][1]
		)
		self.direction = self.rotation
		self.image = self.rotate_center()
		self.mask = pygame.mask.from_surface(self.image)

	def rotate_center(self):
		origRect = self.image.get_rect()
		rotatedImage = pygame.transform.rotate(self.originalImage, self.rotation + 180)
		rotatedRect = origRect.copy()
		rotatedRect.center = rotatedImage.get_rect().center
		rotatedImage = rotatedImage.subsurface(rotatedRect).copy()
		return rotatedImage

	def read_input(self, keys, clock):
		''' Handles user input '''
		createdObjects = []
		for idx, val in enumerate(keys):
			if val:
				currKey = pygame.key.name(idx)
				for action in self.keymap.actions:
					if self.keymap.actions[action] == currKey:
						if action == 'accelerate':
							self.accelerate(clock)
						if action == 'reverse':
							self.reverse(clock)
						if action == 'left':
							self.left(clock)
						if action == 'right':
							self.right(clock)
						if action == 'shoot':
							bullet = self.shoot(clock, self.position)
							if bullet is not None:
								createdObjects.append(bullet)
						else:
							self.lastShot += clock.get_time()
		return createdObjects