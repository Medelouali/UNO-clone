import pygame,sys

from menus.functions import font
from menus.functions import screen
from menus.functions import button 
pygame.init() 

bg1 = pygame.image.load("assets\images\p1.jpg")
bg1= pygame.transform.scale(bg1,(1280,640))

bg2 = pygame.image.load("assets\images\p2.jpg")
bg2= pygame.transform.scale(bg2,(1280,640))
 #Creating the buttons 
NextButton = button("Next",50,(255, 196, 0),900 ,520,300,100)
#button for the first interface
Back1 = button("Back",50,(255, 196, 0),500 ,520,300,100)
#button for the second interface 
Back2 = button("Back",50,(255, 196, 0),100 ,520,300,100)

#to display the next page of the rules 
def rule2(ActMenu):
    run = True    
    while ( run ): 
        screen.blit(bg2,(0,0))
        for event in pygame.event.get():
            #check if player quits the game
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if(event.type == pygame.MOUSEMOTION):
                if( Back1.recc.collidepoint(pygame.mouse.get_pos())):
                    Back1.set_hover(True)
                    Back1.set_color()
                    
                else : 
                    Back1.set_hover(False)
                    Back1.set_color()
            if(event.type == pygame.MOUSEBUTTONDOWN ):
                if (Back1.recc.collidepoint(pygame.mouse.get_pos()) and ActMenu =="RulesMenu") :
                    run=False
        Back1.draw_text(screen,(0,0,0),(640,570))
        pygame.display.update()


def GameRules (ActMenu):

    T = True
    while (T):
        screen.blit(bg1,(0,0))
        
        
        for event in pygame.event.get():
            
            # check if player quits the game
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if(event.type == pygame.MOUSEMOTION):
                if( NextButton.recc.collidepoint(pygame.mouse.get_pos())):
                    NextButton.set_hover(True)
                    NextButton.set_color()
                    
                else : 
                    NextButton.set_hover(False)
                    NextButton.set_color()
                if( Back2 .recc.collidepoint(pygame.mouse.get_pos())):
                    Back2 .set_hover(True)
                    Back2 .set_color()
                    
                else : 
                    Back2.set_hover(False)
                    Back2.set_color()
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if (NextButton.recc.collidepoint(pygame.mouse.get_pos()) and ActMenu =="RulesMenu" ):
                    rule2(ActMenu) 
                    
                if (Back2.recc.collidepoint(pygame.mouse.get_pos())and ActMenu =="RulesMenu"):
                    print("agaiinn")
                    T=False 

            
        NextButton.draw_text(screen,(0,0,0),(1050,570))
        Back2.draw_text(screen,(0,0,0),(250,570))
        pygame.display.update()
            
