from turtle import speed
import pygame
from PIL import Image

# Getting aspect-ration of an image


def aspect_ratio(image):
    img = Image.open(image)
    dims = img.size
    img.close()
    return dims[0]/dims[1]


def get_dims(image):
    img = Image.open(image)
    dims = img.size
    img.close()
    return dims

# This class generalizes objects like cards, coins...


class Object(pygame.sprite.Sprite):
    object_group = pygame.sprite.Group()  # Grouping objects

    def __init__(self, x_axis, y_axis, width, image, screen, scene, dimensions, speed=10):
        super().__init__()
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.width = width
        self.aspect_ratio = aspect_ratio(image)
        self.heigth = int(self.width/self.aspect_ratio)
        self.image = pygame.Surface([self.width, self.heigth])
        self.rect = self.image.get_rect()
        self.rect.center = [self.x_axis, self.y_axis]
        self.image.fill((23, 23, 23))  # for testing

        self.dimensions = dimensions
        self.speed = speed
        self.scene = scene
        self.screen = screen

    def get_coordinates(self):
        print(self.x_axis, self.y_axis)  # Just for testing
        return self.x_axis, self.y_axis

    # An object can be rendered and/or be rotated by degrees
    def render(self):
        self.object_group.add(self)
        self.object_group.draw(self.screen)

    # An object can move by x, and y
    def moveBy(self, x, y):
        pass

    # An object can move to x, and y
    def moveTo(self, x, y):
        pass

    # An object can move to x, and y

    def grow(self, new_width):
        pass

    # An object can be resized according to a certain aspect-ratio
    def growBy(self, ratio):
        pass
