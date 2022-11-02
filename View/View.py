import sys
import xml.dom.minidom

import pygame

from View.spritesheet import spriteSheet


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

        # Code to show one image in a spritesheet
        ss = spriteSheet('Resources/SpriteCollab-master/sprite/0001/Idle-Anim.png')
        image = ss.image_at((0, 0, 32, 32))
        image = pygame.transform.scale(image, (520,520))
        images = []

        images.append(ss.image_at((0,0,32,32)))
        images.append(ss.image_at((33,0,32,32)))

        doc = xml.dom.minidom.parse('Resources/SpriteCollab-master/sprite/0001/AnimData.xml')

        self.screen.blit(image, (100,100))

        pygame.display.flip()

        # Loop to keep the window running
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.update()
