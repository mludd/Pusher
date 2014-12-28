import os
import sys
import math
import time
import pygame
from pygame.locals import *

import settings
import map
import tile
import block
import bullet
import player

class Game:
    def __init__(self):
        self.settings = settings.Settings()
        self.screen = pygame.display.set_mode(self.settings.resolution)
        self.map = map.Map()
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()
        self.surface.fill((0, 0, 0))
    
    def run(self):
        ''' Main game loop '''
        # Init resources
        basePath = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..'))

        self.screen.blit(self.surface, (0,0))
        pygame.display.flip()
        print("running")
        self.map = map.Map(basePath+'/maps/default.js') # map.Map('/Users/mikael/src/Pusher/maps/default.js')
        camera = pygame.rect.Rect(0, 0, self.settings.resolution[0], self.settings.resolution[1])

        self.surface = self.map.draw_tiles(self.surface, pygame.time.Clock())
        self.screen.blit(self.surface, (0, 0))
        self.clock = pygame.time.Clock()

        # Run game
        pygame.font.init()
        menlo = pygame.font.SysFont("Menlo", 12)
        debugText = menlo.render("Player position: , Player speed: , Player rotation: ", 1, (0,0,0))

        while True:
            self.clock.tick(60)
            ## Parse input
            self.read_input()
            surface = self.surface

            # Blocks, projectiles et al
            self.map.blocks.update(self.surface, self.clock, self.map.blocks)
            self.map.blocks.clear(self.screen, self.surface)
            self.map.blocks.draw(self.screen)

            # Player
            keys = pygame.key.get_pressed()
            self.map.players.update(self.surface, self.clock, self.map.blocks, keys)
            self.map.players.clear(self.screen, self.surface)
            self.map.players.draw(self.screen)

            # Print debug
            self.render_debug(menlo, self.surface)

            ## Redraw
            pygame.display.flip()
        return 0

    def render_debug(self, font, surface):
        i = 0
        for plr in self.map.players:
            debugText = font.render("Player position: ["+('%.2f' %plr.position[0])+" "+('%.2f' % plr.position[1])+"], Player speed: "+('%.2f' % plr.speed)+", Player rotation: "+('%.2f' % plr.rotation), 1, (0,0,0), (255,255,255,255))
            textPosition = debugText.get_rect()
            textPosition.centerx = surface.get_rect().centerx
            self.screen.blit(debugText, textPosition)
            i += 12

    def read_input(self):
        ''' Checks input '''
        basePath = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..'))

        keys = pygame.key.get_pressed()
        #for idx, val in enumerate(keys):
        #print(keys)
        #self.map.players.read_input(keys)
        #for kmIdx, keymap in enumerate(self.map.keymaps):
        #    print(kmIdx)
        #        #print(pygame.key.name(pygame.))
        #    for idx, val in enumerate(keys):
        #        if val:
        #            for action in self.map.keymaps[keymap].actions:
        #                if self.map.keymaps[keymap].actions[action] == pygame.key.name(idx):
        #                    print(pygame.key.name(idx))
        #                    if action == 'accelerate':
        #                        self.map.players[kmIdx].accelerate(self.clock)
        #                    if action == 'slow':
        #                        self.map.players[kmIdx].slow(self.clock)
        #                    if action == 'left':
        #                        self.map.players[kmIdx].left(self.clock)
        #                    if action == 'right':
        #                        self.map.players[kmIdx].right(self.clock)
                        #pass
                    #print(idx)
                    #print(pygame.key.name(idx))


        
        if not keys[pygame.K_s]:
            #self.map.player.slow(self.clock)
            pass
        if keys[pygame.K_w]:
            #self.map.player.accelerate(self.clock)
            pass
        if keys[pygame.K_s]:
            #self.map.player.reverse(self.clock)
            pass
        if keys[pygame.K_a]:
            #self.map.player.left(self.clock)
            pass
        if keys[pygame.K_d]:
            #self.map.player.right(self.clock)
            pass
        
        for event in pygame.event.get():
            if event.type == QUIT:
                 sys.exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    sys.exit(0) # Quit game
                elif event.key == K_r:
                    self.map = map.Map(basePath+'/maps/default.js')
                elif event.key == K_SPACE:
                    if isinstance(self.map.player, player.DrivablePlayer):
                        origin = [
                            self.map.player.rect.centerx,
                            self.map.player.rect.centery
                        ]
                        self.map.blocks.add(self.map.player.shoot(origin))