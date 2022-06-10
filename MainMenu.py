import pygame,sys

from menus.functions import button 

#from Functions import font
from menus.functions import screen
pygame.init()
bg = pygame.image.load('bg1.jpg')
bg= pygame.transform.scale(bg,(1280,640))




#Creating buttons



#  Game Loop
def MainMenu(ActMenu):
    PlayButton = button("Play",50,(250, 53, 29),500 ,50,200,100)
    ExitButton =button ("Exit" , 50,(250, 53, 29)  , 500 ,450,200,100)
    RulesButton = button("Game Rules" , 50,(250, 53, 29) ,500 ,250,200,100)

    while(True):

        screen.blit(bg,(0,0))
        ActMenu="MainMenu"
        from PlayMenu import PlayMenu
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
                        #  quiting the game with the exit button
                        pygame.quit()
                        sys.exit()
    
        #screen.fill((64,224,208))
        
        PlayButton.draw_text(screen ,(255,255,255))  
        RulesButton.draw_text(screen ,(255,255,255))
        ExitButton.draw_text(screen,(255,255,255))
        
        
        pygame.display.update()
        
'''pygame.draw.line(surface,(0,0,0),(self.x,self.y),(self.x + self.w , self.y), 5)
        pygame.draw.line(surface, (0,0,0), (self.x, self.y - 2), (self.x, self.y + self.h), 5)
        pygame.draw.line(surface, (0,0,0), (self.x, self.y + self.h), (self.x + self.w , self.y + self.h), 5)
        pygame.draw.line(surface, (0,0,0), (self.x + self.w , self.y + self.h), [self.x + self.w , self.y], 5)'''


ActMenu=""
MainMenu(ActMenu)