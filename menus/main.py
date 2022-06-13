import pygame,sys
from menus.functions import button
from menus.functions import screen 
from menus.play import PlayMenu 
pygame.init()
bg = pygame.image.load("assets\images\pl.jpg")
bg= pygame.transform.scale(bg,(1280,640))

#Creating the buttons 
PlayButton = button("Play",50,(255, 196, 0),100 ,500,300,100)
RulesButton = button("Game Rules" , 50,(255, 196, 0) ,500 ,500,300,100)
ExitButton =button ("Exit" , 50,(255, 196, 0)  , 900 ,500,300,100)




def main(ActMenu):
    
    
    while(True):

        screen.blit(bg,(0,0))
        
        ActMenu="MainMenu"
        
        print(PlayButton.get_hover())
        

        for event in pygame.event.get():
            # check if player quits the game
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            
            #check if the mouse is hovering over the buttons 
            #and adding a  hovering color 
            if(event.type == pygame.MOUSEMOTION):
                if( PlayButton.recc.collidepoint(pygame.mouse.get_pos())):
                    PlayButton.set_hover(True)
                    PlayButton.set_color()
                    
                else : 
                    PlayButton.set_hover(False)
                    PlayButton.set_color()
                
                if( RulesButton.recc.collidepoint(pygame.mouse.get_pos())):
                    RulesButton.set_hover(True)
                    RulesButton.set_color()
                else : 
                    RulesButton.set_hover(False)
                    RulesButton.set_color()
                
                if( ExitButton.recc.collidepoint(pygame.mouse.get_pos())):
                    ExitButton.set_hover(True)
                    ExitButton.set_color()
                else : 
                    ExitButton.set_hover(False)
                    ExitButton.set_color() 
               
            
                
           
            if( event.type == pygame.MOUSEBUTTONDOWN):
               
                if( PlayButton.recc.collidepoint(pygame.mouse.get_pos())and ActMenu=="MainMenu" ):
                    print ("Play")
                    ActMenu="PlayMenu"
                    PlayMenu(ActMenu)


                if( RulesButton.recc.collidepoint(pygame.mouse.get_pos()) and ActMenu=="MainMenu"):
                        print ("Game Rules")
                    
                if (ExitButton.recc.collidepoint(pygame.mouse.get_pos()) and ActMenu=="MainMenu" ):
                        print ("Exit")
                        # quiting the game with the exit button
                        pygame.quit()
                        sys.exit()
    
        
        PlayButton.draw_text(screen ,(0,0,0),(250,550))  
        RulesButton.draw_text(screen ,(0,0,0),(650,550))
        ExitButton.draw_text(screen,(0,0,0),(1050,550))
        
        
        pygame.display.update()


