import pygame
import json
import os

class Tile(pygame.sprite.Sprite):
    def __init__(self, tile, position, scale):
        pygame.sprite.Sprite.__init__(self)
        basePath = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..'))
        
        self.conf = self.load(tile)
        
        self.image, self.rect = self.load_png(basePath+'/images/'+self.conf['image'], scale)
        self.position = position
        self.speed = [0, 0]
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.sprite = pygame.sprite.RenderPlain(self)

    def load(self, tile):
        ''' Loads the configuration for the named tile '''
        basePath = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'tiles'))
        with open(basePath+"/"+tile+".js") as file:
            jsonData = file.read()
            data = json.loads(jsonData)
            return data

    def setPos(self, x, y):
        ''' Sets the tile's position '''
        self.position = [x, y]

    def load_png(self, name, scale):
        """ Load image and return image object"""
        fullname = os.path.join('data', name)
        try:
            image = pygame.image.load(fullname)
            if image.get_alpha is None:
                image = image.convert()
            else:
                image = image.convert_alpha()
            image = pygame.transform.smoothscale(image, (scale, scale))
        except pygame.error, message:
                print 'Cannot load image:', fullname
                raise SystemExit, message
        return image, image.get_rect()
