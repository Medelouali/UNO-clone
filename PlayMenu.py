import pygame,sys
from Functions import draw_text
from Functions import font
from Functions import screen
from utilities.classes.game.Game import Game
from SettingsMenu import SettingsMenu

pygame.init()


def PlayMenu(ActMenu,RectDic):

    T=True# this loop while variable
    #Buttons positions
    PlayGButton =(600 ,100)
    Settings = (600 ,300)
    Backbutton=(600 ,500)
    
    while(T):
        ActMenu="PlayMenu"
        for event in pygame.event.get():
        # check if player quits the game
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            # check mouse click
            if(event.type == pygame.MOUSEBUTTONDOWN ):
                if( RectDic["Back"].collidepoint(pygame.mouse.get_pos()) and ActMenu=="PlayMenu"):
                        print ("Back")
                        T=False
                if( RectDic["Settings"].collidepoint(pygame.mouse.get_pos()) and ActMenu=="PlayMenu" ):
                        print ("Settings")
                        ActMenu="SettingsMenu"
                        SettingsMenu(ActMenu,RectDic)
                
                #    Start of the GAME
                if( RectDic["play a bit"].collidepoint(pygame.mouse.get_pos()) and ActMenu=="PlayMenu" ):
                    print("Start a game")
                    game = Game()
                    game.launch()
                                

        #Screen blit and updating                
        screen.fill((160,160,160))
        draw_text("play a bit",font,(255 ,255 ,255),screen,PlayGButton,RectDic)
        draw_text("Settings" , font , (255 ,255 ,255) ,screen ,Settings,RectDic)
        draw_text("Back" , font , (255 ,255 ,255) ,screen ,Backbutton,RectDic)
        pygame.display.update()


