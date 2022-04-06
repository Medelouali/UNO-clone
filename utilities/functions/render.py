import pygame

# This would render the scene at any given point depending on the scene where the game is at
import os
from utilities.classes.Object import Object


def get_image(image_name, dirs=[]):
    return os.path.join(os.getcwd(), 'assets', os.path.sep.join(dirs), image_name)


background_image = pygame.image.load(get_image('logo.png'))


def render(screen, scene, dimensions):
    # just for testing, this would go in the event_handler
    obj = Object(100, 100, 200, get_image(
        'logo.png'), screen, scene, dimensions)
    obj2 = Object(200, 500, 400, get_image(
        'logo.png'), screen, scene, dimensions)
    obj.render()
    obj2.render()
    pass
