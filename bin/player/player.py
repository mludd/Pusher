import json
import pygame
import block

class Player(block.Block):
    def __init__(self, position, rotation, direction, speed):
        super(Player, self).__init__('player', position, rotation, direction, speed)
        print self.position

    def up(self, blocks):
        #target = [self.position[0], self.position[1] - self.rect[3]]
        target = [self.position[0], self.position[1] - 1]
        self.move(blocks, target, 'up')

    def right(self, blocks):
        #target = [self.position[0] + self.rect[2], self.position[1]]
        target = [self.position[0] + 1, self.position[1]]
        self.move(blocks, target, 'right')
    
    def left(self, blocks):
        #target = [self.position[0] - self.rect[2], self.position[1]]
        target = [self.position[0] - 1, self.position[1]]
        self.move(blocks, target, 'left')

    def down(self, blocks):
        #target = [self.position[0], self.position[1] + self.rect[3]]
        target = [self.position[0], self.position[1] + 1]
        self.move(blocks, target, 'down')

    def move(self, blocks, target, direction):
        '''
        target = [x,y]
        blocks = list(block.Block)
        direction = 'left','right','up','down'
        '''
        if self.check_move(blocks, target, direction):
            self.position = target
            self.direction= direction

    def check_move(self, blocks, target, direction):
        ''' Checks for collisions with blocks '''
        collisionBlocks = filter(lambda block: block.position[0] == target[0] and block.position[1] == target[1], blocks)
        if not collisionBlocks:
            return True

        print collisionBlocks

        if collisionBlocks[0].move(blocks, direction):
            return True

        return False

    def on_surface(self):
        if self.position[1] < 800:
            return None
        else:
            return True