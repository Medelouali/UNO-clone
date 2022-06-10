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

#Button Class
class button() :
    hover = False
    def __init__(self,text,size,color,x,y,w,h):
        self.text = text 
        self.color = color
        self.size = size
        self.font = pygame.font.SysFont("Holtwood One SC",self.size)
        #self.color = color 
        self.x = x 
        self.y = y 
        self.h = h
        self.w = w
        
        self.recc = pygame.Rect((self.x,self.y),(self.w,self.h))
        self.recc.center = (self.x,self.y)
        #making the Rec for the black Backcolor
        self.BlackRect=pygame.Rect((self.x,self.y),(self.w+5,self.h+5))
        self.BlackRect.center = (self.x,self.y)
       
    
    
    def draw_text(self,surface,txt_color):
        pygame.draw.rect(surface,(0,0,0),self.BlackRect ,0,10)

        pygame.draw.rect(surface,self.color,self.recc,0,10)

        TextObj = self.font.render(self.text, 1, txt_color)
        TextRect = TextObj.get_rect()
        TextRect.center = self.recc.center
        surface.blit(TextObj ,TextRect)
    def set_color(self):
        if button.hover:
            print("hovering")
            self.color = (11, 234, 26)
        else : 
            self.color=(250, 53, 29)

    def set_hover (self,bool):
        button.hover = bool
    def get_hover (self):
        return button.hover
