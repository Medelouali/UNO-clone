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

    # The game loop
    is_running = True
    scene = {}  # the scene describes the game at any given point

    while is_running:
        # this would kinda unrender the game on each iteration
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            stage = event_handler(event)
            is_running = stage[0]
            # This would add/change new details to/in the scene
            for key, value in stage[1].items():
                scene[key] = value
        render(screen, scene, dimensions)
        pygame.display.update()


if(__name__ == '__main__'):
    game()
