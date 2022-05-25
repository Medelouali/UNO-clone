import pygame,sys
pygame.init()
from MainMenu import MainMenu
pygame.display.set_caption('UNO')
# setting the variables 
ActMenu=""#to mark the menu
RectDic ={}# to mark the existing Rect's

MainMenu(ActMenu,RectDic)


