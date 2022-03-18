import pygame
from win32api import GetSystemMetrics

# Initializing pygame
pygame.init()

# Initializing the screen
# this would be the resolution of the screen later
windowwidth, windowheight = 800, 600
screen = pygame.display.set_mode(int(windowwidth), int(windowheight))

# Setting title and the logo of the game
pygame.display.set_caption('IslandWalkers')
icon = pygame.image.load('assets/beach.png')
pygame.display.set_icon(icon)

# The game loop
isRunning, level = True, 0
while isRunning:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            isRunning = False
    screen.fill((1, 23, 100))
    DEFAULT_IMAGE_SIZE = (120, 200)
    image = pygame.image.load('assets/island (1).png')
    image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
    screen.blit(image, (300, 200))
    pygame.display.update()
