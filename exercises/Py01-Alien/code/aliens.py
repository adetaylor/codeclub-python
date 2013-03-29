#!/usr/bin/env python

#######################################################################################
# CodeClub Alien exercise
#######################################################################################

#######################################################################################
# Code to ignore.
# The code in this section doesn't affect the game play and CodeClubbers can safely
# ignore it. There are comments explaining what each bit does, but you can skip ahead
# to the next big comment like this.
#######################################################################################

# Our program asks for help from some other Python programs, called 'modules' or
# 'libraries'. Here is where we say what programs we need help from. That just means
# we don't have to do so much work ourselves in our program.

import random # We need use random numbers
import pygame # We are making a game. pygame draws us a window and makes it easy to
   # show sprites.
from pygame.locals import *  # And we need to get more bits of pygame too.
from aliens_dataloader import * # Finally some handy bits of code of our own,
   # which we've just put in a separate file to avoid cluttering this one.

#######################################################################################
# Basic facts about the game.
# Because these are unchanging, they are called 'constants'.
#######################################################################################

MAX_SHOTS      = 2      # no more than two player bullets can be on screen at a time
ALIEN_ODDS     = 22     # chances that a new alien appears (1 in 22 chance)
BOMB_ODDS      = 60     # chances that a new bomb will drop (1 in 60 chance)
FRAMES_BETWEEN_ALIEN_RELOAD_CHANCE   = 12 # frames between new aliens (25 frames per second, so there *might*
# be an alien every 0.5 seconds (ish) depending on the odds)
SCREENRECT     = Rect(0, 0, 640, 480)

#######################################################################################
# Setting up pygame.
# This doesn't affect the behaviour of the sprites... but there might be some things you need to look at
# here for one of the challenges...
#######################################################################################

# Check that the version of pygame on this PC is working properly.
if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")

# Set up pygame.
pygame.init()
if pygame.mixer and not pygame.mixer.get_init():
    print ('Warning, no sound')
    pygame.mixer = None

# Boring stuff related to setting up the pygame window
winstyle = 0 # or, could use FULLSCREEN instead of 0
bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

# Initialize Game Groups
# Later, when the game is running, we want to know
# if an alien has hit the player. Rather than check
# each individual alien, we can put them all into a group
# then ask pygame to check whether the player has hit
# anything in that group. We do the same with some other
# things too, and we also use these groups to ask
# everything to update.
aliens = pygame.sprite.Group()
shots = pygame.sprite.Group()
bombs = pygame.sprite.Group()
all = pygame.sprite.RenderUpdates()
lastalien = pygame.sprite.GroupSingle()

#######################################################################################
# Game objects.
#
#      *** THE FIRST IMPORTANT BIT!!! ***
#
# These are the equivalent of Scratch 'sprites'
#######################################################################################

# The big difference from Scratch sprites:
# There are 'classes' of game objects, but there may be several
# objects of that class. For example there might be several aliens
# or several bullets.
# Unlike Scratch, there's no need to copy the scripts between several
# things that behave the same way.

# Of course, for some 'classes' there might be only one - the Player
# is a good example.

# The little scripts within each class are called 'functions'
# and they start with 'def' (which is short for 'define').

# For each one, __init__ is called when the object is created.
# For the player, that would be at the beginning of the game,
# but aliens or bullets may be created later in the game.

# All of them (except the Player) have an 'update' function
# which is called regularly throughout the game. The Player
# has 'move' instead.

class Player(pygame.sprite.Sprite):
    speed = 10
    bounce = 24
    gun_offset = -11
    images = load_image_and_its_mirror_image('player1.gif', 1, 0)
    containers = all

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1

    def move(self, direction):
        if direction: self.facing = direction
        self.rect.move_ip(direction*self.speed, 0)
        self.rect = self.rect.clamp(SCREENRECT)
        if direction < 0:
            self.image = self.images[0]
        elif direction > 0:
            self.image = self.images[1]
        self.rect.top = self.origtop - (self.rect.left//self.bounce%2)

    def gunpos(self):
        "Tell something else about the location of the gun."
        # This is a function which "returns a value" - that means
        # it's a bit like a broadcast which sends a reply with
        # some information in it.
        pos = self.facing*self.gun_offset + self.rect.centerx
        return pos, self.rect.top


class Alien(pygame.sprite.Sprite):
    SPEED = 13
    FRAMES_BETWEEN_IMAGE_CHANGE = 12 # about half a second
    images = load_images('alien1.gif', 'alien2.gif', 'alien3.gif')
    containers = aliens, all, lastalien

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.facing = random.choice((-1,1)) * Alien.SPEED
        self.frame = 0
        if self.facing < 0:
            self.rect.right = SCREENRECT.right

    def update(self):
        self.rect.move_ip(self.facing, 0)
        if not SCREENRECT.contains(self.rect):
            self.facing = -self.facing;
            self.rect.top = self.rect.bottom + 1
            self.rect = self.rect.clamp(SCREENRECT)
        self.frame = self.frame + 1
        self.image = self.images[self.frame//self.FRAMES_BETWEEN_IMAGE_CHANGE%3]

class Explosion(pygame.sprite.Sprite):
    LIFETIME = 12
    FRAMES_BETWEEN_IMAGE_CHANGE = 3
    images = load_image_and_its_mirror_image('explosion1.gif', 1, 1)
    containers = all

    def __init__(self, actor):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=actor.rect.center)
        self.life_remaining = self.LIFETIME

    def update(self):
        self.life_remaining = self.life_remaining - 1
        self.image = self.images[self.life_remaining//self.FRAMES_BETWEEN_IMAGE_CHANGE%2]
        if self.life_remaining <= 0: self.kill()


class Shot(pygame.sprite.Sprite):
    speed = -11
    images = [load_image('shot.gif')]
    containers = shots, all

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=pos)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= 0:
            self.kill()


class Bomb(pygame.sprite.Sprite):
    speed = 9
    images = [load_image('bomb.gif')]
    containers = bombs, all

    def __init__(self, alien):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=
                    alien.rect.move(0,5).midbottom)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= 470:
            Explosion(self)
            self.kill()


class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 20)
        self.font.set_italic(1)
        self.color = Color('white')
        self.last_drawn_score = -1
        self.update()
        self.rect = self.image.get_rect().move(10, 450)

    def update(self):
        # Don't bother redrawing the score unless it's actually changed.
        if score != self.last_drawn_score:
            self.last_drawn_score = score
            msg = "Score: %d" % score
            self.image = self.font.render(msg, 0, self.color)

#######################################################################################
# The main game script.
#
#      *** THE SECOND IMPORTANT BIT!!! ***
#
# This is the equivalent of the Scratch 'when green flag clicked' script.
# There's only one of these, and it arranges to call all the other functions when
# necessary.
#######################################################################################

#decorate the game window
icon = pygame.transform.scale(Alien.images[0], (32, 32))
pygame.display.set_icon(icon)
pygame.display.set_caption('Pygame Aliens')
pygame.mouse.set_visible(0)

# create the background, tile the bgd image
bgdtile = load_image('background.gif')
background = pygame.Surface(SCREENRECT.size)
for x in range(0, SCREENRECT.width, bgdtile.get_width()):
    background.blit(bgdtile, (x, 0))
screen.blit(background, (0,0))
pygame.display.flip()

# load the sound effects
boom_sound = load_sound('boom.wav')
shoot_sound = load_sound('car_door.wav')
if pygame.mixer:
    music = os.path.join(main_dir, 'data', 'house_lo.wav')
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)

# Create Some Starting Values
frames_until_we_might_create_alien = FRAMES_BETWEEN_ALIEN_RELOAD_CHANCE
score = 0
kills = 0
clock = pygame.time.Clock()

#initialize our starting sprites
player = Player()
# In python, variables don't just have to be numbers or text. They can point
# to whole sprites. Here, we're created a Player and we've put it into a variable
# called 'player' so that we can ask it later for its location. Specifically
# when we want to create a bullet, we need to know where the player was.
Alien() # create the first alien. But we don't need to remember it.

if pygame.font:
    all.add(Score())

# This loop is important CodeClubbers!
while player.alive():

    # See if we want to end the game
    for event in pygame.event.get():
        if event.type == QUIT or \
            (event.type == KEYDOWN and event.key == K_ESCAPE):
                raise SystemExit
    keystate = pygame.key.get_pressed()

    # clear/erase the last drawn sprites
    all.clear(screen, background)

    # update all the sprites. This calls 'update'
    # on all the different sprites there are, because we put
    # them all into the 'all' group above.
    all.update()

    # Key states are 0 if the key isn't pressed, or 1 if key
    # is pressed. So, 'direction' will be 1 if moving right,
    # -1 if moving left. Clever but quite confusing.
    direction = keystate[K_RIGHT] - keystate[K_LEFT]
    player.move(direction)
    firing = keystate[K_SPACE]
    if not player.reloading and firing and len(shots) < MAX_SHOTS:
        Shot(player.gunpos())
        shoot_sound.play()
    player.reloading = firing

    # Create new alien, perhaps.
    if frames_until_we_might_create_alien > 0:
        frames_until_we_might_create_alien = frames_until_we_might_create_alien - 1
    elif not int(random.random() * ALIEN_ODDS):
        Alien()
        frames_until_we_might_create_alien = FRAMES_BETWEEN_ALIEN_RELOAD_CHANCE

    # Drop bombs
    if lastalien and not int(random.random() * BOMB_ODDS):
        Bomb(lastalien.sprite)

    # Detect collisions
    for alien in pygame.sprite.spritecollide(player, aliens, 1):
        boom_sound.play()
        Explosion(alien)
        Explosion(player)
        score = score + 1
        player.kill()

    for alien in pygame.sprite.groupcollide(shots, aliens, 1, 1).keys():
        boom_sound.play()
        Explosion(alien)
        score = score + 1

    for bomb in pygame.sprite.spritecollide(player, bombs, 1):
        boom_sound.play()
        Explosion(player)
        Explosion(bomb)
        player.kill()

    #draw the scene
    dirty = all.draw(screen)
    pygame.display.update(dirty)

    #cap the framerate
    clock.tick(40)

if pygame.mixer:
    pygame.mixer.music.fadeout(1000)
pygame.time.wait(1000)
pygame.quit()

