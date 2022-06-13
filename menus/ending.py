import pygame,sys

from utilities.functions.path import writeText
from menus.functions import font
from menus.functions import screen
from menus.functions import button
from utilities.classes.game.Game import Game  as Game
# from MainMenu import button 
bg = pygame.image.load('assets\images\pl.jpg')
bg= pygame.transform.scale(bg,(1280,640))
# from utilities.classes.game.Game import Game

pygame.init()


def ending(ActMenu,txt):


    T=True# this loop while variable
    #Buttons positions
    Replay=button("Replay",50,(250, 53, 29),160 ,55,200,100)
    Exit= button("Exit",50,(250, 53, 29),160 ,255,200,100)
    exitMenu = button("Back To Menus",50,(250, 53, 29),110 ,455,300,100)



    while(T):
       
        screen.blit(bg,(0,0))

        for event in pygame.event.get():
        # check if player quits the game
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()

            if(event.type == pygame.MOUSEMOTION):
                if( Replay.recc.collidepoint(pygame.mouse.get_pos())):
                    Replay.set_hover(True)
                    Replay.set_color()

                else : 
                    Replay.set_hover(False)
                    Replay.set_color()

            if(event.type == pygame.MOUSEMOTION):
                if( Exit.recc.collidepoint(pygame.mouse.get_pos())):
                    Exit.set_hover(True)
                    Exit.set_color()

                else : 
                    Exit.set_hover(False)
                    Exit.set_color()

            if(event.type == pygame.MOUSEMOTION):
                if( exitMenu.recc.collidepoint(pygame.mouse.get_pos())):
                    exitMenu.set_hover(True)
                    exitMenu.set_color()

                else : 
                    exitMenu.set_hover(False)
                    exitMenu.set_color()

            # check mouse click
            if(event.type == pygame.MOUSEBUTTONDOWN ):
                if( Exit.recc.collidepoint(pygame.mouse.get_pos()) and ActMenu=="end"):
                    print ("Exit ")
                    pygame.quit()
                    sys.exit()

                if( exitMenu.recc.collidepoint(pygame.mouse.get_pos()) and ActMenu=="end" ):
                    print("back to the menus")
                    return False


                if( Replay.recc.collidepoint(pygame.mouse.get_pos()) and ActMenu=="end" ):
                    print("Replay")
                    return True


        Replay.draw_text(screen,(255,255,255),(250 ,100))
        exitMenu.draw_text(screen ,(255,255,255),(250 ,500))
        Exit.draw_text(screen ,(255,255,255),(250 ,300) )
        
        writeText(txt, 5*Game.screenWidth/6, 2*Game.screenHeight/5, 50, Game.screen)
        
       
        pygame.display.update()

