import pygame
import json
import os

class Keymap:
	def __init__(self, file):
		basePath = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..'))
		self.keys = {}
		if file is False:
			self.actions = {
				'accelerate': False,
				'reverse': False,
				'left': False,
				'right': False
			}
		else:
			self.actions = self.load(file)
			print(self.actions)

	def load(self, keymap):
		''' Loads the configuration for the specified keymap '''
		basePath = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'keymaps'))
		with open(basePath+"/"+keymap+".js") as file:
			jsonData = file.read()
			data = json.loads(jsonData)
			return data

	def map_key(self, key, action):
		self.keys[key] = action

	def get_key(self, key):
		if key in self.keys:
			return self.keys[key]
		return False
			

	@staticmethod
	def processKeyboard(self, events):
		pressedKeys = pygame.key.get_pressed()
		for pressedKey in pressedKeys:
			pass
			#if action = self.get_key(pressedKey):
			#	pass