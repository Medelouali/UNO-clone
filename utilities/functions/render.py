import pygame

# This would render the scene at any given point depending on the scene where the game is at
import os
from utilities.classes.Object import Object, aspect_ratio


def get_image(image_name):
    return os.path.join(os.getcwd(), 'assets', image_name)


background_image = pygame.image.load(get_image('images.jpg'))


def render(screen, scene, dimensions):
    # setting background image
    # ratio = aspect_ratio(get_image('images.jpg'))
    # img1 = pygame.transform.scale(
    #     background_image, (int(ratio*dimensions[0]), dimensions[1]))
    # screen.blit(img1, (0, 0))
    screen.fill((255, 255, 255))
    # just for testing, this would go in the event_handler
    scene.append(Object(800, 400, 100, get_image(
        'bear.png'), screen, scene, dimensions, 100))
    scene.append(Object(400, 100, 50, get_image(
        'bear.png'), screen, scene, dimensions, 100))
    scene.append(Object(100, 200, 500, get_image(
        'jocker-card (1).png'), screen, scene, dimensions, 100))

    for obj in scene:
        obj.render()
