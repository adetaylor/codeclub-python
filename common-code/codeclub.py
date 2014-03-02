#!/usr/bin/env python
"""
Handy utilities for CodeClub and pygame.

The stuff in here is boring and should be ignored by CodeClubbers.
That's why we're hiding it in here.
"""

# Import Modules

import os, pygame
from pygame.locals import *
from math import sqrt, degrees, atan, cos, sin, radians

#######################################################################################
# Stuff about loading images and sounds.
# Scratch intrinsically knows how to show images and play sounds, but Python
# doesn't so we have to have this code to load them. However, fortunately,
# we use the services of another program called 'pygame' to do most of the work.
#######################################################################################

def load_image(name, colorkey=None):
	main_dir = os.path.split(os.path.abspath(__file__))[0]
	fullname = os.path.join(main_dir, 'data', name)
	try:
		image = pygame.image.load(fullname)
	except pygame.error as message:
		print('Cannot load image:', fullname)
		raise SystemExit(message)
	image = image.convert_alpha()
	if colorkey is not None:
		if colorkey is -1:
		    colorkey = image.get_at((0,0))
		image.set_colorkey(colorkey, RLEACCEL)
	return image #, image.get_rect()

def load_images(*files):
	imgs = []
	for file in files:
		imgs.append(load_image(file))
	return imgs

def load_image_and_its_mirror_image(file, flipx, flipy):
	img = load_image(file)
	return [img, pygame.transform.flip(img, flipx, flipy)]

def load_sound(name):
	class NoneSound:
		def play(self): pass
	if not pygame.mixer or not pygame.mixer.get_init():
		return NoneSound()
	main_dir = os.path.split(os.path.abspath(__file__))[0]
	fullname = os.path.join(main_dir, 'data', name)
	try:
		sound = pygame.mixer.Sound(fullname)
	except pygame.error as message:
		print('Cannot load sound:', fullname)
		raise SystemExit(message)
	return sound

def start_music(file):
	if pygame.mixer:
		main_dir = os.path.split(os.path.abspath(__file__))[0]
		music = os.path.join(main_dir, 'data', file)
		pygame.mixer.music.load(music)
		pygame.mixer.music.play(-1)

def aspect_scale(img,bx,by):
	""" Scales 'img' to fit into box bx/by.
	This method will retain the original image's aspect ratio """
	# Thanks to Frank Raiser (crashchaos at gmx.net)
	ix,iy = img.get_size()
	if ix > iy:
		# fit to width
		scale_factor = bx/float(ix)
		sy = scale_factor * iy
		if sy > by:
			scale_factor = by/float(iy)
			sx = scale_factor * ix
			sy = by
		else:
			sx = bx
	else:
		# fit to height
		scale_factor = by/float(iy)
		sx = scale_factor * ix
		if sx > bx:
			scale_factor = bx/float(ix)
			sx = bx
			sy = scale_factor * iy
		else:
			sy = by
	return pygame.transform.smoothscale(img, (int(sx),int(sy)))

#######################################################################################
# A sprite which knows how to do more stuff like a Scratch sprite
#######################################################################################

class CodeClubSprite(pygame.sprite.Sprite):
	def __init__(self, x_pos = 100.0, y_pos = 100.0):
		pygame.sprite.Sprite.__init__(self) #call Sprite intializer
		self.direction = 0;
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.rect = pygame.Rect(x_pos-5, y_pos-5, 10, 10)
		self.freeze_time = 0
		self.speak_time = 0
		self.speak_pos = (0,0)
		self.speak_font = pygame.font.Font(None, 36)
		self.speak_text = self.speak_font.render("Hello!!!", 1, (10, 10, 10))
		self.x_diff = self.y_diff = 0

	def set_costume(self, name, size):
		self.image = load_image(name, -1)
		self.rect = self.image.get_rect()
		self.image = self.orig_image = aspect_scale(self.image, (size, size))
		self.rect.width = self.rect.height = size

	def turn_right(self, degrees = 10):
		self.direction += degrees
		self.adjust_image_based_on_direction()

	def turn_left(self, degrees = 10):
		self.direction -= degrees
		self.adjust_image_based_on_direction()

	def point_in_direction(self, degrees):
		self.direction = degrees
		self.adjust_image_based_on_direction()

	def point_towards(self, target):
		x_diff = target.rect.center[0] - self.rect.center[0]
		y_diff = target.rect.center[1] - self.rect.center[1]
        
		if (x_diff == 0):
			if (y_diff <= 0):
				self.direction = 90
			else:
				self.direction = 270
		elif (y_diff == 0):
			if (x_diff <= 0):
				self.direction = 0
			else:
				self.direction = 180
		else:
			if (x_diff < 0) and (y_diff < 0):  #Up and left, 0 - 90 degrees
				self.direction = degrees(atan(float(y_diff) / float(x_diff)))
			if (x_diff > 0) and (y_diff < 0):  #Up and right, 90 - 180 degrees
				self.direction = 90 + degrees(atan(float(x_diff) / float(-y_diff)))
			if (x_diff > 0) and (y_diff > 0):  #Down and right, 180 - 270 degrees
				self.direction = 180 + degrees(atan(float(y_diff) / float(x_diff)))
			if (x_diff < 0) and (y_diff > 0):  #Down and left, 270 - 360 degrees
				self.direction = 270 + degrees(atan(float(-x_diff) / float(y_diff)))
		self.adjust_image_based_on_direction()

	def move_to(self, pos):
		self.rect.center = pos

	def get_position(self):
		return self.rect.center

	def get_direction(self):
		return self.direction

	def move(self, distance = 1):
		# PyGame co-ordinates are integers yet we want to be able
		# to move <1 unit, so we keep track of fractional movements
		# to do next time.
		self.x_diff -= cos(radians(self.direction)) * distance
		self.y_diff -= sin(radians(self.direction)) * distance
		self.rect.center = (self.rect.center[0] + int(self.x_diff), self.rect.center[1] + int(self.y_diff))
		self.x_diff -= int(self.x_diff)
		self.y_diff -= int(self.y_diff)
	
	def move_unless_frozen(self, distance):
		"Moves in current direction"
		if self.freeze_time == 0:
			self.move(distance)
		else:
			self.freeze_time = self.freeze_time - 1

	def freeze(self, time):
		"Stand still for the specified time"
		self.freeze_time = time

	def say(self, words, time):
		self.speak_text = self.speak_font.render(words, 1, (10, 10, 10))
		self.speak_pos = self.rect.topright
		self.speak_time = time

	def speak(self, screen):
		if self.speak_time > 0:
			self.speak_time = self.speak_time - 1
		screen.blit(self.speak_text, self.rect.topright)

	def has_caught(self, target):
		"Detect when Felix catches Herbert - only returns true when he first hits"
		hitbox = self.rect.inflate(-30, -15)
		return (hitbox.colliderect(target.rect) and self.freeze_time == 0)

	def adjust_image_based_on_direction(self):
		pass

class CodeClubLeftRightFacingSprite(CodeClubSprite):
	def __init__(self, x_pos = 100.0, y_pos = 100.0):
		CodeClubSprite.__init__(self, x_pos, y_pos)
		self.facing_right = True

	def adjust_image_based_on_direction(self):
		# Now ensure the Sprite is faceing the correct way (look left / right only)	
		if (self.rect.left > target.rect.left) and self.facing_right == True:
			self.facing_right = False
			self.image = pygame.transform.flip(self.image, 1, 0)
		if (self.rect.left < target.rect.left) and self.facing_right == False:
			self.facing_right = True
			self.image = self.orig_image

class CodeClubFreeRotatingSprite(CodeClubSprite):
	def __init__(self, x_pos = 100.0, y_pos = 100.0):
		CodeClubSprite.__init__(self, x_pos, y_pos)

	def adjust_image_based_on_direction(self):
		self.image = pygame.transform.rotate(self.orig_image, -self.direction)
