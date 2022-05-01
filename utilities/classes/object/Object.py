
import pygame


class Object(pygame.sprite.Sprite):
    def __init__(self, isVisible=False, coordinates=[10, 10], icon=None):
        super().__init__()
        self.image=pygame.image.load(icon)
        self.rect=self.image.get_rect()
        self.rect.center=coordinates
        
        self.isVisible=isVisible
        self.coordinates=coordinates
        self.icon=icon

    def update(self):
        self.rect.center=pygame.mouse.get_pos()