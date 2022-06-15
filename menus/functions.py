import pygame,sys
pygame.init()

########screen data####################
font = pygame.font.SysFont("Rammetto One",90)
framesPerSecond=60
clock=pygame.time.Clock()
screenWidth=1280
screenHeight=640
screen=pygame.display.set_mode((screenWidth, screenHeight))
font = pygame.font.SysFont("Rammetto One",90)
screen=pygame.display.set_mode((screenWidth, screenHeight))
#######################################

class button() :
    
    hover = False
    
    def __init__(self,text,size,color,x,y,w,h):
        self.text = text 
        self.color = color
        self.size = size
        self.font = pygame.font.SysFont("Holtwood One SC",self.size)
        self.x = x 
        self.y = y 
        self.h = h
        self.w = w
        self.recc = pygame.Rect((self.x,self.y),(self.w,self.h)) 
      
       
    
    
    def draw_text(self,surface,txt_color,centerpos):
        #drawing the outline of the button 
        pygame.draw.rect(surface,(0,0,0), pygame.Rect((self.x-4,self.y-4),(self.w+3,self.h+3))   ,0,50)
        #drawinf the button 
        pygame.draw.rect(surface,self.color,self.recc,0,50)
        #writing text on the button
        TextObj = self.font.render(self.text, 1, txt_color)
        TextRect = TextObj.get_rect()
        TextRect.center = centerpos
        surface.blit(TextObj ,TextRect)
    
    #change color of the button when hovering over it 
    def set_color(self):
        if button.hover:
            # print("Hover")
            self.color = (33, 236, 42)
        else :
            self.color=(255, 196, 0)

    
    def set_hover(self,bool):
        button.hover = bool 
    
    def get_hover (self):
        return button.hover

