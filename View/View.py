import sys

import pygame


class View:
    title = 'Mystery Dungeon'
    screen = None
    spriteList = pygame.sprite.Group()

    def __init__(self, size):
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.screen = pygame.display.set_mode(self.size)

    def initWindow(self):
        self.screen.fill((255, 255, 255))
        pygame.display.set_caption(self.title)

    def showWindow(self):
        self.initWindow()
        testSprite = pygame.image.load('Resources/SpriteCollab-master/sprite/0001/Idle-Anim.png')
        self.screen.blit(testSprite, (200,200))
        pygame.display.flip()

        # Loop to keep the window running
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()

    def initSprite(self):
        pygame.sprite.Group()
