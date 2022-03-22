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


class Object:
    def __init__(self, x_axis, y_axis, width, avatar, screen, scene, dimensions, speed=10):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.aspect_ratio = aspect_ratio(avatar)
        self.width = width
        self.heigth = int(self.width/self.aspect_ratio)
        self.avatar = avatar
        self.screen = screen
        self.dimensions = dimensions
        self.speed = speed
        self.scene = scene

        self.update_scene(scene)

    def update_scene(self, scene):
        for index, obj in enumerate(scene):
            if(obj.x_axis == self.x_axis and obj.y_axis == self.y_axis):
                scene[index] = self
                break

    def get_coordinates(self):
        print(self.x_axis, self.y_axis)  # Just for testing
        return self.x_axis, self.y_axis

    # An object can be rendered and/or be rotated by degrees
    def render(self, rotate=False, degrees=0):
        if(rotate):
            img1 = pygame.image.load(self.avatar)
            img2 = pygame.transform.rotate(img1, degrees)
            img3 = pygame.transform.scale(
                img2, (self.width, self.heigth))
            self.screen.blit(img3, (self.x_axis, self.y_axis))
        else:
            img1 = pygame.image.load(self.avatar)
            img2 = pygame.transform.scale(
                img1, (self.width, self.heigth))
            self.screen.blit(img2, (self.x_axis, self.y_axis))

    # An object can move by x, and y
    def moveBy(self, x, y):
        if(self.x_axis <= self.dimensions[0]):
            self.x_axis += x
        if(self.y_axis <= self.dimensions[1]):
            self.y_axis += y
        self.update_scene(self.scene)
        return self

    # An object can move to x, and y
    def moveTo(self, x, y):
        coeff = (y-self.y_axis)/(x-self.x_axis)
        const = self.y_axis-coeff*self.x_axis
        x0 = self.x_axis
        y0 = self.y_axis
        speed = (1 if x > self.x_axis else -1) * \
            (max([x0, x])-min([x0, x]))/self.speed
        while(True):
            if(self.x_axis < min([x0, x]) or self.x_axis > max([x0, x]) or
               self.y_axis < min([y0, y]) or self.y_axis > max([y0, y])):
                break
            self.x_axis += speed
            self.y_axis += coeff*self.x_axis+const
            self.get_coordinates()
        self.update_scene(self.scene)
        return self

    # An object can move to x, and y

    def grow(self, new_width):
        self.width = new_width
        self.heigth = int(self.width/self.aspect_ratio)
        self.update_scene(self.scene)
        return self

    # An object can be resized according to a certain aspect-ratio
    def growBy(self, ratio):
        self.width = int(ratio*self.width)
        self.heigth = int(ratio*self.heigth)
        self.update_scene(self.scene)
        return self
