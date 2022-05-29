import pygame,sys
pygame.init()

########screen data####################
font = pygame.font.SysFont("gillsanscondensed",70)
framesPerSecond=60
clock=pygame.time.Clock()
screenWidth=1280
screenHeight=640
screen=pygame.display.set_mode((screenWidth, screenHeight))
font = pygame.font.SysFont("gillsanscondensed",70)
screen=pygame.display.set_mode((screenWidth, screenHeight))
#######################################


def draw_text(text,font,color,surface,centerpos,RectDic):
    TextObj = font.render(text, 1, color)
    TextRect = TextObj.get_rect()
    #adding TextRects to the local dictionnary
    RectDic[text] =TextRect
    
    TextRect.center = centerpos
    pygame.draw.rect(screen,(100,0,250) , pygame.Rect(TextRect))
    surface.blit(TextObj ,TextRect)
