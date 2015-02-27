import pygame

class BlockGroup(pygame.sprite.Group):
	""" Custom group class that is able to remove 'dead' blocks on its own """
	def remove_dead(self):
		""" Removes destroyed blocks from the group """
		spritedict = { k : v for k, v in self.spritedict.iteritems() if k.destroy is not True }
		self.spritedict = spritedict