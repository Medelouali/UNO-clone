import pygame
from utilities.functions.render import render
from utilities.functions.events import event_handler


def game():
    # Initializing pygame
    pygame.init()

    # Initializing the screen
    dimensions = (1280, 700)
    screen = pygame.display.set_mode(dimensions)

    # Setting title and the logo of the game
    pygame.display.set_caption('Cards Combat')
    pygame.display.set_icon(pygame.image.load('assets/game-logo.png'))

    is_running = True
    # the scene describes the game at any given point
    scene = []
    # This scene array would be in the form [Object(args), ...]
    # The Object instances let you manipulates the current object, view the Object class for more info

    # The game loop
    while is_running:
        # this would kinda unrender the game on each iteration
        # screen.fill((255, 255, 255))
        for event in pygame.event.get():
            is_running = event_handler(event, scene)

        render(screen, scene, dimensions)
        pygame.display.update()


if(__name__ == '__main__'):
    game()
