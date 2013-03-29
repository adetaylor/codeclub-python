#!/usr/bin/env python

#######################################################################################
# CodeClub Ball exercise
#######################################################################################

import pygame
from pygame.locals import *
import os.path

# Set up a variable containing the location of this 'ball.py' file on disk.
# We assume all the images are nearby in a folder called 'data'.
main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'data', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert_alpha()

SCREENRECT     = Rect(0, 0, 640, 480)

pygame.init()

winstyle = 0 # or, could use FULLSCREEN instead of 0
bestdepth = pygame.display.mode_ok(SCREENRECT.size, 0, 32)
screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

all = pygame.sprite.RenderUpdates()

BALL_IMAGE = load_image('ball.png')

class Ball(pygame.sprite.Sprite):
    speed = 5

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, all)
        self.image = BALL_IMAGE
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)

icon = pygame.transform.scale(BALL_IMAGE, (32, 32))
pygame.display.set_icon(icon)
pygame.display.set_caption('Pygame Ball')
pygame.mouse.set_visible(0)

clock = pygame.time.Clock()

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

    #cap the framerate
    clock.tick(40)


