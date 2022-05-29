import pygame,sys
from Functions import draw_text
from Functions import font
from Functions import screen
from utilities.classes.game.Game import Game

pygame.init()


def PlayMenu(ActMenu,RectDic):

    T=True# this loop while variable
    #Buttons positions
    PlayGButton =(600 ,100)
    Test = (600 ,300)
    Backbutton=(600 ,500)
    
    while(T):

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
                if( RectDic["Difficulty settings"].collidepoint(pygame.mouse.get_pos()) and ActMenu=="PlayMenu" ):
                        print ("not yet implemented!")
                
                #    Start of the GAME
                if( RectDic["play a bit"].collidepoint(pygame.mouse.get_pos()) and ActMenu=="PlayMenu" ):
                    print("Start a game")
<<<<<<< HEAD
                    game = Game()
                    game.launch()
=======
                    if(__name__ == '__main__'):
                        game = Game()
                        game.launch()
>>>>>>> 478185237a371f8e4a11c53ebc0785fe1aa7bd0d
                                

        #Screen blit and updating                
        screen.fill((50,50,50))
        draw_text("play a bit",font,(255 ,255 ,255),screen,PlayGButton,RectDic)
        draw_text("Difficulty settings" , font , (255 ,255 ,255) ,screen ,Test,RectDic)
        draw_text("Back" , font , (255 ,255 ,255) ,screen ,Backbutton,RectDic)
        pygame.display.update()


