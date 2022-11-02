import sys

import pygame


class View:
    title = 'Mystery Dungeon'
    size = 1080, 720
    screen = None

    def __init__(self):
        self.screen = pygame.display.set_mode(self.size)

    def showView(self):
        pygame.init()
        self.screen.fill((255, 255, 255))
        pygame.display.set_caption(self.title)
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()
