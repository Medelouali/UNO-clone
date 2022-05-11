
import pygame
from pygame.locals import *
from utilities.functions.path import getPath
pygame.init()

# naming the window
pygame.display.set_caption("Movable Card Class")

# importing the background
BG = pygame.image.load(getPath("images", "logo.png"))

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


# Card class
class Card:

    # Card creation
    def __init__(self, img, Rsize):
        self.Rsize = Rsize
        img_stock = pygame.image.load(img).convert()
        self.img = pygame.transform.scale(
            img_stock, (img_stock.get_width()*Rsize, img_stock.get_height()*Rsize))
        self.rect = self.img.get_rect()
        # self.rect.center=w//2,h//2

    def post_card(self):
        # global CardClicked
        # getting mouse position
        pos = pygame.mouse.get_pos()
        # verifying if img clicked
        if self.rect.collidepoint(pos):  # testing if mouse hovering over Card
            if pygame.mouse.get_pressed()[0] == 1:  # testing if Card clicked
                if event.type == MOUSEMOTION:  # testing if mouse moving
                    self.rect.move_ip(event.rel)
        surf.blit(self.img, self.rect)

 # create button
# button = Button(10, 710, "button test")
# create Card
card1 = Card(getPath("images", "logo.png"), 0.3)
card2 = Card(getPath("images", "logo.png"), 0.5)

# Main Loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # verifiying in the loop if the Card is clicked
        card1.post_card()
        card2.post_card()

        # if button.draw_button():
        #     print("clicked")

    surf.fill((0, 0, 0))  # unused for now
    # redrawing tge background and the Card
    surf.blit(BG, (0, 0))
    surf.blit(card1.img, card1.rect)
    surf.blit(card2.img, card2.rect)

    # updating the screen
    pygame.display.update()


# quitting
pygame.quit()
