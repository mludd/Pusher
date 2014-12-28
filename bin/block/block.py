import pygame
import json
import math
import os

class Block(pygame.sprite.DirtySprite):
    def __init__(self, file, position, rotation, direction, speed):
        pygame.sprite.DirtySprite.__init__(self)
        basePath = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..'))
        
        self.position = position
        self.conf = self.load(file)
        self.image, self.rect = self.load_png(basePath+'/images/'+self.conf['image'])
        self.originalImage = self.image
        #self.rotation = self.conf['rotation']
        self.rotation = rotation
        self.oldRotation = rotation
        self.direction = direction #self.conf['direction']
        #self.speed = self.conf['speed']
        self.speed = speed
        self.screen = pygame.display.get_surface()
        self.mask = pygame.mask.from_surface(self.image)
        self.sprite = pygame.sprite.LayeredDirty(self)
        self.movable = self.conf['movable']
        self.type = self.conf['type']

    def slow(self, clock):
        td = clock.get_time()
        decrease = float(td)/ float(10000)
        if self.speed >= decrease:
            self.speed -= decrease
        else:
            self.speed = 0

    def destruct(self, surface):
        self.dirty = 1
        self.sprite.clear(self.screen, surface)
        return surface

    def update(self, surface, clock, blocks):
        self.dirty = 1
        
        self.slow(clock)
        timedelta = clock.get_time()

        position = [
            self.position[0] + (math.sin(math.radians(self.direction)) * self.speed * timedelta),
            self.position[1] + (math.cos(math.radians(self.direction)) * self.speed * timedelta)
        ]
        self.position = position

        self.oldRotation = self.rotation
        self.rect = pygame.rect.Rect(
            position[0],
            position[1],
            self.conf['dimensions'][0],
            self.conf['dimensions'][1]
        )
        self.image = self.rotate_center()
        self.mask = pygame.mask.from_surface(self.image)
        return surface, blocks

    def load(self, block):
        ''' Loads the configuration for the named block '''
        basePath = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'blocks'))
        with open(basePath+"/"+block+".js") as file:
            jsonData = file.read()
            data = json.loads(jsonData)
            return data

    def rotate_center(self):
        origRect = self.image.get_rect()
        rotatedImage = pygame.transform.rotate(self.originalImage, self.rotation + 180)
        rotatedRect = origRect.copy()
        rotatedRect.center = rotatedImage.get_rect().center
        rotatedImage = rotatedImage.subsurface(rotatedRect).copy()
        return rotatedImage

    def load_png(self, name):
        """ Load image and return image object"""
        fullname = os.path.join('data', name)
        dimensions = self.conf['dimensions']
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
