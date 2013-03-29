#!/usr/bin/env python

#######################################################################################
# CodeClub Ball exercise
#######################################################################################

import pygame
from pygame.locals import *
from codeclub_pygame_handy_functions import *

SCREENRECT = Rect(0, 0, 640, 480)

pygame.init()

winstyle = 0 # or, could use FULLSCREEN instead of 0
bestdepth = pygame.display.mode_ok(SCREENRECT.size, 0, 32)
screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

all = pygame.sprite.RenderUpdates()

BALL_IMAGE = load_image_from_data_directory('ball.png')

class Ball(pygame.sprite.Sprite):
    speed = 5

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, all)
        self.image = BALL_IMAGE
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)

# Create a ball
Ball()

running = True

while running: # means 'forever'

    # See if we want to end the game
    for event in pygame.event.get():
        if event.type == QUIT or \
            (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False

    # update all the sprites. This calls 'update'
    # on all the different sprites there are, because we put
    # them all into the 'all' group above.
    all.update()

    #draw the scene
    dirty = all.draw(screen)
    pygame.display.update(dirty)
