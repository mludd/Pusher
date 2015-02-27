import json
import tile
import block
import player
import bullet
import keymap
import blockgroup
import pygame

class Map:
    def __init__(self, file = ''):
        if file != '':
            self.load(file)
        else:
            self.file = ''
            self.name = ''
            self.size = [0,0]
            self.tiles = []
            self.blocks = []

    def load(self, filename):
        with open(filename) as file:
            jsonData = file.read()
            data = json.loads(jsonData)
            self.name = data['name']
            self.type = data['type']
            if self.type == 'tiled':
                self.load_tiled(data)
            elif self.type == 'layered':
                self.load_layered(data)

    def load_tiled(self, data):
        ''' Loads a tiled map '''
        self.size = [data['width'], data['height']]
        self.tileTypes = data['tileTypes']
        self.tileSize = data['tileSize']
        self.offset = self.tileSize / 2

        # Load tiles
        self.tiles = list()
        currentRow = 0
        tiles = data['tiles']
        for row in tiles:
            currentColumn = 0
            for col in row:
                name = filter(lambda tileType: tileType['id'] == col, self.tileTypes)[0]
                name = name['filename']

                position = [
                    currentColumn,
                    currentRow
                ]

                self.tiles.append(tile.Tile(name, position, self.tileSize))
                currentColumn += 1
            currentRow += 1

        # Load blocks
        self.blocks = blockgroup.BlockGroup() #pygame.sprite.Group()
        blocks = data['blocks']
        for blk in blocks:
            self.blocks.add(block.Block(blk['type'], blk['position'], blk['rotation'], blk['direction'], blk['speed']))

        # Load players
        self.players = pygame.sprite.Group()
        for plr in data['players']:
            self.players.add(player.DrivablePlayer(plr['position'], plr['rotation'], plr['direction'], plr['speed'], plr['keymap']))

    def load_layered(self, data):
        ''' Loads a layered map (stub) '''
        pass

    def draw(self, screen, surface, clock):
        if self.type == 'tiled':
            surface = self.draw_tiles(surface, clock)
            surface = self.draw_blocks(screen, surface, clock)
            return surface
        elif self.type == 'layered':
            pass

    def draw_tiles(self, surface, clock):
        ''' Draws all tiles '''
        for tile in self.tiles:
            realRect = pygame.rect.Rect(
                (tile.position[0] * self.tileSize), # + self.offset,
                (tile.position[1] * self.tileSize), # + self.offset,
                self.tileSize,
                self.tileSize
            )
            tile.rect = realRect

            surface.blit(surface, tile.rect, tile.rect)
            tile.sprite.update()
            tile.sprite.draw(surface)

        return surface

    def draw_blocks(self, screen, surface, clock):
        ''' Draws all map blocks '''
        for block in self.blocks:
            block.sprite.update(surface, clock)
            surface.blit(surface, block.rect, block.rect)
            block.sprite.draw(surface)
        return surface