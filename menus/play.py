import pygame,sys

from menus.functions import font
from menus.functions import screen
from menus.functions import button 
from utilities.classes.game.Game import Game  as Game
from menus.ending import ending 
bg = pygame.image.load('assets\images\pl.jpg')
bg= pygame.transform.scale(bg,(1280,640))
# from utilities.classes.game.Game import Game

pygame.init()

Normal=button("Normal",50,(255, 196, 0),100 ,500,300,100)
Hard= button("Hard",50,(255, 196, 0),500 ,500,300,100)
Back = button("Back",50,(255, 196, 0),900 ,500,300,100)
def PlayMenu(ActMenu):

    T=True  #This loop while variable
    
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
                                

        #Drawing the buttons 
        Normal.draw_text(screen,(0,0,0),(250,550))
        Hard.draw_text(screen ,(0,0,0),(650,550) )
        Back.draw_text(screen ,(0,0,0), (1050,550))
        
       
        pygame.display.update()


