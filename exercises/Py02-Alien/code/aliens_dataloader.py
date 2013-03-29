import pygame
import os.path # We need to use images on disk, and this module helps us specify
# how to find them

#######################################################################################
# Stuff about loading images and sounds.
# Scratch intrinsically knows how to show images and play sounds, but Python
# doesn't so we have to have this code to load them. However, fortunately,
# we use the services of another program called 'pygame' to do most of the work.
#######################################################################################

# Set up a variable containing the location of this 'aliens_dataloader.py' file on disk.
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

def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs

def load_image_and_its_mirror_image(file, flipx, flipy):
    img = load_image(file)
    return [img, pygame.transform.flip(img, flipx, flipy)]

# Aha, you *are* reading this in detail.
# A 'class' in Python is a bit like a sprite in Scratch, except that it doesn't
# actually have to be something you can see on the screen. Any 'thing' can
# be a class. For example a sound can be a class. This particular 'thing'
# is an empty sound that can be played instead of a proper sound if
# the proper sound can't be loaded.
class dummysound:
    def play(self): pass

def load_sound(file):
    if not pygame.mixer: return dummysound()
    file = os.path.join(main_dir, 'data', file)
    try:
        sound = pygame.mixer.Sound(file)
        return sound
    except pygame.error:
        print ('Warning, unable to load, %s' % file)
    return dummysound()
