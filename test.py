import pygame
import random
from utilities.functions.path import getPath
# --- classes --- (UpperCaseNames)

class Test(pygame.sprite.Sprite):

    def __init__(self, w):
        super().__init__()

        self.image = pygame.image.load(getPath('images', 'logo.png'))
        self.image = pygame.transform.scale(self.image, (w, w))
        self.rect = self.image.get_rect()

        self.last = pygame.time.get_ticks()

# --- main ----

level = 1
cooldown = 1000

# - init -

pygame.init()
screen = pygame.display.set_mode((600, 600))

# - items -

background = pygame.Surface(screen.get_size())
background.fill((0, 0, 0))

screen.blit(background, (0,0))

all_sprites_list = pygame.sprite.Group()

for x in range(10):
    item = Test(random.randint(40, 60))
    item.rect.x = 40 * random.randint(0, 10)
    item.rect.y = 0
    all_sprites_list.add(item)

# - mainloop -

clock = pygame.time.Clock()

running = True

while running:

    now = pygame.time.get_ticks()

    for item in all_sprites_list:
        item.rect.y += level

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for item in all_sprites_list:
                if item.rect.collidepoint(event.pos):
                    item.kill()

    pygame.display.flip()
    all_sprites_list.clear(screen, background)
    all_sprites_list.draw(screen)
    all_sprites_list.update()