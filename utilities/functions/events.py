from types import new_class
import pygame

from utilities.classes.Object import Object


def event_handler(event, scene):
    if(event.type == pygame.QUIT):
        return False
    # Just for testing r now
    return True
