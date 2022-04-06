

import pygame
from pygame.locals import *

pygame.init()

# naming the window
pygame.display.set_caption("Movable Card Class")

# importing the background
BG = pygame.image.load(("bg1R.jpg"))

# font variable
font = pygame.font.SysFont('Constantia', 30)

#global variable
clicked = False
CardClicked = False
# screen creation
surf = pygame.display.set_mode((1390, 800))
# useful Variables
run = True

# button Class


class Button:
    button_col = (25, 190, 225)
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = (255, 255, 255)
    width = 180
    height = 70

    # button creation
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):
        global clicked
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # create rect object for the button
        button_rect = Rect(self.x, self.y, self.width, self.height)

        # checking if mouse is hovering over the button
        if button_rect.collidepoint(pos):
            # if button pressed
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
            # if button no longer pressed but have been pressed
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:  # if mouse hovering over button without clicking
                pygame.draw.rect(surf, self.click_col, button_rect)
        else:  # if mouse NOT hoverint over the button
            pygame.draw.rect(surf, self.button_col, button_rect)

        # adding text to button
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        surf.blit(text_img, (self.x + int(self.width / 2) -
                  int(text_len / 2), self.y + 25))
        return action
