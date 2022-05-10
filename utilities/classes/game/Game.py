import pygame, sys
from utilities.classes.object.Object import Object
from utilities.functions.path import getPath
from utilities.functions.resize import getSize

pygame.init()
pygame.display.set_caption('UNO')
pygame.display.set_icon(pygame.image.load(getPath("images", "logo.png")))

class Game:
    # Class attrs
    state={
            "rotation": 1,
            "unoWasSaid": False,
            "winner": None,
            "activePlayer": None,
            "event": None,
            "gameOver": False,
        } # this dictionary will manage the whole state of the game
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
        # This is how we'll add the objects to the game
        Game.objectsGroup.add(Object(True, [100, 300], getPath('images', 'logo.png'))) # just for testing
        Game.objectsGroup.add(Object(True, [800, 300], getPath('images', 'logo.png'))) # just for testing
        Game.objectsGroup.add(Object(True, [1500, 300], getPath('images', 'logo.png'))) # just for testing
        while(True):
            for event in pygame.event.get():
                Game.setState("event", event)
                if(event.type == pygame.QUIT or Game.getState(Game, "gameOver")):
                    pygame.quit()
                    sys.exit()
                    
            pygame.display.update()
            Game.screen.blit(Game.backgroundImage, (0, 0))
            Game.objectsGroup.draw(Game.screen)
            Game.objectsGroup.update()
            self.clock.tick(Game.framesPerSecond)
         
    @classmethod # The state is modified if it does exist   
    def setState(cls, key, value):
        if(key in cls.state.keys()):
            cls.state[key]=value
       
    # None is returned implicitly if the key doesn't exist as a state
    @staticmethod
    def getState(cls, key):
        if(key in cls.state.keys()):
            return cls.state[key]