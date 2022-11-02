import sys

import pygame


class View:
    title = 'Mystery Dungeon'
    size = None
    screen = None

    def __init__(self, size):
        pygame.init()
        self.size = size
        self.screen = pygame.display.set_mode(self.size)

    def initWindow(self):
        self.screen.fill((255, 255, 255))
        pygame.display.set_caption(self.title)

    def showWindow(self):
        self.initWindow()
        pygame.display.flip()

        # Loop to keep the window running
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()
