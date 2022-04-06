from pygame.locals import *
from classes.Object import Object
from functions.render import get_image


# Card class
class Card(Object):
    # Card creation
    def __init__(self, img, Rsize, screen, dimensions):
        super().__init__(0, 0, 0, get_image('logo.png'), screen, dimensions)

    # def post_card(self):
    #     global CardClicked
    #     # getting mouse position
    #     pos = pygame.mouse.get_pos()
    #     # verifying if img clicked
    #     if self.rect.collidepoint(pos):  # testing if mouse hovering over Card
    #         if pygame.mouse.get_pressed()[0] == 1:  # testing if Card clicked

    #             if event.type == MOUSEMOTION:  # testing if mouse moving
    #                 self.rect.move_ip(event.rel)

    #     surf.blit(self.img, self.rect)
