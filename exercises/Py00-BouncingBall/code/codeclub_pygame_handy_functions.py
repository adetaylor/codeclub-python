import os.path
import pygame

main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image_from_data_directory(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'data', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert_alpha()
