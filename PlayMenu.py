import pygame,sys

from utilities.functions.path import writeText
from ending import ending
from utilities.classes.game.Game import Game  as Game

from menus.functions import font
from menus.functions import screen
# from MainMenu import button 
bg = pygame.image.load('bg1.jpg')
bg= pygame.transform.scale(bg,(1280,640))
# from utilities.classes.game.Game import Game

pygame.init()


def PlayMenu(ActMenu):
    from menus.functions import button 

    T=True# this loop while variable
    #Buttons positions
    Normal=button("Normal",50,(250, 53, 29),500 ,50,200,100)
    Hard= button("Hard",50,(250, 53, 29),500 ,250,200,100)
    Back = button("Back",50,(250, 53, 29),500 ,450,200,100)

    
    
    while(T):
       
    
        screen.blit(bg,(0,0))
        for event in pygame.event.get():
        # check if player quits the game
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()

            if(event.type == pygame.MOUSEMOTION):
                if( Normal.recc.collidepoint(pygame.mouse.get_pos())):
                    Normal.set_hover(True)
                    Normal.set_color()
                    
                else : 
                    Normal.set_hover(False)
                    Normal.set_color()
                
                if( Hard.recc.collidepoint(pygame.mouse.get_pos())):
                    Hard.set_hover(True)
                    Hard.set_color()
                else : 
                    Hard.set_hover(False)
                    Hard.set_color()
                
                if( Back.recc.collidepoint(pygame.mouse.get_pos())):
                    Back.set_hover(True)
                    Back.set_color()
                else : 
                    Back.set_hover(False)
                    Back.set_color() 
               



            # check mouse click
            if(event.type == pygame.MOUSEBUTTONDOWN ):
                if( Back.recc.collidepoint(pygame.mouse.get_pos()) and ActMenu=="PlayMenu"):
                        print ("Back")
                        T=False
                #Start of the GAME (Normal)
                if( Normal.recc.collidepoint(pygame.mouse.get_pos()) and ActMenu=="PlayMenu" ):
                        print ("not yet implemented!")
                
                #Start of the GAME (Hard)
                if( Hard.recc.collidepoint(pygame.mouse.get_pos()) and ActMenu=="PlayMenu" ):
                    print("Start a game")
                    P=True
                    while(P):
                        # from utilities.classes.game.Game import Game  as Game
                        game = Game()
                        game.run()
                        print("Playing the game")

                        if( Game.getState("playersList")[0].getHand() ==[]):#the bot is the winner
                            del(game)
                            print("Bot Wins !")
                            ActMenu="end"
                            P=ending(ActMenu,"Bot Wins !")
                            ActMenu="PlayMenu"
                            

                        if( Game.getState("playersList")[1].getHand() ==[]):#the player wins
                            del(game)
                            print("Player Wins !")
                            ActMenu="end"
                            P=ending(ActMenu,"Player Wins !")
                            ActMenu="PlayMenu"
                            

                    
                                

                     
        #screen.fill((50,50,50))
       
        Normal.draw_text(screen,(255,255,255))
        Hard.draw_text(screen ,(255,255,255) )
        Back.draw_text(screen ,(255,255,255) )
        
       
        pygame.display.update()


