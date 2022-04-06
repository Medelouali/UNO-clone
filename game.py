import pygame
from utilities.functions.render import get_image, render
from utilities.functions.events import event_handler


def game():
    # Initializing pygame
    pygame.init()

    # Initializing the screen
    dimensions = (1280, 700)
    screen = pygame.display.set_mode(dimensions)

    # This prevent the while loop from going crazy, we'll limit the frames per second to 60 as rate
    clock = pygame.time.Clock()
    fps = 60

    # Setting title and the logo of the game
    pygame.display.set_caption('Cards Combat')
    pygame.display.set_icon(pygame.image.load(get_image('logo.png')))

    # Setting the background, it will be dynamic later on
    background = pygame.image.load(get_image('logo.png'))

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
        screen.blit(background, (0, 0))
        render(screen, scene, dimensions)
        pygame.display.update()
        clock.tick(fps)


if(__name__ == '__main__'):
    game()
