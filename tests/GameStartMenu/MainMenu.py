
import pygame,sys

pygame.init()


############################################################## rect's dictionnary
RectDic ={}

####################################################################  draw function
def draw_text(text,font,color,surface,centerpos):
    TextObj = font.render(text, 1, color)
    TextRect = TextObj.get_rect()
    
    #adding TextRects to the local dictionnary
    RectDic[text] =TextRect
    
    TextRect.center = centerpos
    pygame.draw.rect(screen,(100,0,250) , pygame.Rect(TextRect))
    surface.blit(TextObj ,TextRect)



#################################################################  font variable

font = pygame.font.SysFont("gillsanscondensed",70)

#################################################################### setting the variables 
pygame.display.set_caption('UNO Menu')


framesPerSecond=60
clock=pygame.time.Clock()
screenWidth=1280
screenHeight=640
screen=pygame.display.set_mode((screenWidth, screenHeight))


#######################################   Buttons Positions    ##
PlayButton = (550 ,100)
ExitButton = (550 ,500)
RulesButton = (550 ,300)


#################################################################  Game Loop
while(True):
    for event in pygame.event.get():
        # check if player quits the game
        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
        ##### check mouse click

        if(event.type == pygame.MOUSEBUTTONDOWN ):
            if( RectDic["Play"].collidepoint(pygame.mouse.get_pos()) ):
                print ("Play")

                T=True
                Test = (550 ,300)
                while(T):
                    for event in pygame.event.get():
                        # check if player quits the game
                        if(event.type == pygame.QUIT):
                            pygame.quit()
                            sys.exit()
                        ##### check mouse click
                        if(event.type == pygame.MOUSEBUTTONDOWN and pygame.MOUSEBUTTONUP):
                            if( RectDic["test"].collidepoint(pygame.mouse.get_pos()) ):
                                print ("test")
                            if( RectDic["Exit"].collidepoint(pygame.mouse.get_pos()) ):
                                print ("Exit")
                                T=False
                    if(T==False): break

                    
                    
                    screen.fill((50,50,50))

                    draw_text("test" , font , (255 ,255 ,255) ,screen ,Test)
                    draw_text("Exit" , font , (255 ,255 ,255) ,screen ,ExitButton)
                    pygame.display.update()





            
            if( RectDic["Game Rules"].collidepoint(pygame.mouse.get_pos()) ):
                print ("Game Rules")
            
            if( RectDic["Exit"].collidepoint(pygame.mouse.get_pos()) ):
                print ("Exit")
                ###############################  quiting the game with the exit button
                pygame.quit()
                sys.exit()



    screen.fill((50,50,50))

    #####################################################    drawing the buttons
    draw_text("Play" , font , (255 ,255 ,255) ,screen ,PlayButton)
    draw_text("Game Rules" , font , (255 ,255 ,255) ,screen ,RulesButton)
    draw_text("Exit" , font , (255 ,255 ,255) ,screen ,ExitButton)


    pygame.display.update()


