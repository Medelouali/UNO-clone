
# This would render the scene at any given point depending on the scene where the game is at
import os
from utilities.classes.Object import Object


def get_image(image_name):
    return os.path.join(os.getcwd(), 'assets', image_name)


def render(screen, scene, dimensions):
    object1 = Object(800, 400, 100, get_image(
        'bear.png'), screen, dimensions, 100)
    object1.moveTo(600, 200)
    # object1.growBy(2)
