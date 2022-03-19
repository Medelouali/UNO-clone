import pygame


def event_handler(event):
    if(event.type == pygame.QUIT):
        return False, {}
    new_changes = {"cardX": 10, "cardY": 20}  # just as an example
    return True, new_changes
