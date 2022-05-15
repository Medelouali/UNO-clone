import os
import pygame
# you give this function dir1 dir2 file which are in the assets folder
# it will return the abs path of the file where you are on the 
# system(inside this project)
def getPath(*args):
    return os.path.join(os.getcwd().split(f'{os.sep}assets{os.sep}')[0], "assets", os.path.join(*args))

def writeText(string, coordx, coordy, fontSize, window):
    #set the font to write with
    font = pygame.font.Font('freesansbold.ttf', fontSize) 
    #(0, 0, 0) is black, to make black text
    text = font.render(string, True, (0, 0, 0))
    #get the rect of the text
    textRect = text.get_rect()
    #set the position of the text
    textRect.center = (coordx, coordy)
    #add text to window
    window.blit(text, textRect)
    #update window