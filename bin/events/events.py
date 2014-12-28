import pygame

class Events:
    def __init__(self):
        pass

    def handleKeyboard(self):
        if pygame.event.poll():
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_LEFT:
                    pass
        else:
            pygame.event.pump()
