import pygame, sys
from utilities.classes.object.Object import Object
from utilities.functions.path import getPath
from utilities.functions.resize import getSize
from utilities.classes.game.State import State

pygame.init()
pygame.display.set_caption('UNO')
pygame.display.set_icon(pygame.image.load(getPath("images", "logo.png")))

class Game:
    # Class attrs
    state=State() # this will manage the whole state of the game
    framesPerSecond=60
    clock=pygame.time.Clock()
    screenWidth=1280
    screenHeight=640
    screen=pygame.display.set_mode((screenWidth, screenHeight))
    objectsGroup=pygame.sprite.Group()
    backgroundImage=pygame.image.load(getPath('images', 'backgroundCards.jpg'))
    backgroundImage = pygame.transform.scale(
        backgroundImage, getSize(getPath('images', 'backgroundCards.jpg'), screenWidth))
    
    def __init__(self, players=[]):
        self.players=players # this is an array of Player objects
        self.currentPlayer=None
    
    def launch(self):
        Game.objectsGroup.add(Object(True, [20, 70], getPath('images', 'logo.png')))
        while(True):
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            pygame.display.update()
            Game.screen.blit(Game.backgroundImage, (0, 0))
            Game.objectsGroup.draw(Game.screen)
            Game.objectsGroup.update()
            self.clock.tick(Game.framesPerSecond)