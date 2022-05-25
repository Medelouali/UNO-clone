import pygame,sys
from PlayMenu import PlayMenu
from Functions import draw_text
from Functions import font
from Functions import screen
pygame.init()

#   Buttons Positions 
PlayButton = (600 ,100)
ExitButton = (600 ,500)
RulesButton = (600 ,300)


#  Game Loop
def MainMenu(ActMenu,RectDic):

    while(True):
        ActMenu="MainMenu"
        for event in pygame.event.get():
            # check if player quits the game
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            #check mouseClick
            if(event.type == pygame.MOUSEBUTTONDOWN ):
                if( RectDic["Play"].collidepoint(pygame.mouse.get_pos()) and ActMenu=="MainMenu" ):
                    print ("Play")
                    ActMenu="PlayMenu"
                    PlayMenu(ActMenu,RectDic)


                if( RectDic["Game Rules"].collidepoint(pygame.mouse.get_pos()) and ActMenu=="MainMenu"):
                    print ("Game Rules")
                
                if ( RectDic["Exit"].collidepoint(pygame.mouse.get_pos()) and ActMenu=="MainMenu" ):
                    print ("Exit")
                    #  quiting the game with the exit button
                    pygame.quit()
                    sys.exit()



        screen.fill((50,50,50))
        
        #    drawing the buttons
        draw_text("Play" , font , (255 ,255 ,255) ,screen ,PlayButton,RectDic)
        draw_text("Game Rules" , font , (255 ,255 ,255) ,screen ,RulesButton,RectDic)
        draw_text("Exit" , font , (255 ,255 ,255) ,screen ,ExitButton,RectDic)
        
        pygame.display.update()
        


