import pygame
import json
import os

class Layer(pygame.sprite.Sprite):
	def __init__(self, name):
		pygame.sprite.Sprite.__init__(self)
		basePath = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..'))