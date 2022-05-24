import pygame,sys
from PlayMenu import draw_text
pygame.init()

##################################    Main infos
RectDic ={}
font = pygame.font.SysFont("gillsanscondensed",70)

pygame.display.set_caption('UNO Menu')


framesPerSecond=60
clock=pygame.time.Clock()
screenWidth=1280
screenHeight=640
screen=pygame.display.set_mode((screenWidth, screenHeight))

################################### difficulty settings game loop
def Play():
    Test = (550 ,300)


    while(True):
        for event in pygame.event.get():
            # check if player quits the game
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            ##### check mouse click

            if(event.type == pygame.MOUSEBUTTONDOWN):
                if( RectDic["Play"].collidepoint(pygame.mouse.get_pos()) ):
                    print ("test")
        
        screen.fill((50,50,50))

        draw_text("test" , font , (255 ,255 ,255) ,screen ,Test)
        


        pygame.display.update()

