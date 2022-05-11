import pygame, sys
from utilities.classes.object.Object import Object
from utilities.functions.path import getPath
from utilities.functions.resize import getSize
from classes.ai.Ai import Ai
from classes.object.player.Player import Player

pygame.init()
pygame.display.set_caption('UNO')
pygame.display.set_icon(pygame.image.load(getPath("images", "logo.png")))

class Game:
    # Class attrs
    state={
            "rotation": 1, # it could be 1, -1, or eventially 2
            "unoWasSaid": False,
            "winner": None,
            "activePlayer": None,
            "event": None,
            "gameOver": False,
            "playersList": [],
        } # this dictionary will manage the whole state of the game
    framesPerSecond=60
    clock=pygame.time.Clock()
    screenWidth=1280
    screenHeight=640
    screen=pygame.display.set_mode((screenWidth, screenHeight))
    objectsGroup=[
        Object(True, [60, 100], getPath('images', 'logo.png')), # just for testing
        Object(True, [900, 600], getPath('images', 'logo.png')) # just for testing
    ]
    backgroundImage=pygame.image.load(getPath('images', 'backgroundCards.jpg'))
    backgroundImage = pygame.transform.scale(
        backgroundImage, getSize(getPath('images', 'backgroundCards.jpg'), screenWidth))
    
    def __init__(self, players=[]):
        Game.setState("playersList", players)
    
    def launch(self):
        # generating players
        self.generatePlayers(2)                
        while(True):
            for event in pygame.event.get():
                Game.setState("event", event)
                if(event.type == pygame.QUIT or Game.getState(Game, "gameOver")):
                    pygame.quit()
                    sys.exit()
                    
            pygame.display.update()
            Game.screen.blit(Game.backgroundImage, (0, 0))
            self.render()
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
        
    def render(self):
        for obj in Game.objectsGroup:
            if(obj==None): # None values are objects that has been destroyed
                continue
            else:
                obj.update()
        
    def generatePlayers(self, numOfPlayers=2, botExists=True):
        if(botExists):    
            if(numOfPlayers==2):
                Game.setState("playersList", Game.getState("playersList").extends([
                    Ai(0),
                    Player(1)
                ]))
            else:
                Game.setState("playersList", Game.getState("playersList").extends([Ai(0)]))    
                Game.setState("playersList", Game.getState("playersList").extends([
                    Player(i) for i in range(1, numOfPlayers)
                ]))
        else:
            Game.setState("playersList", Game.getState("playersList").extends([
                Player(i) for i in range(numOfPlayers)
            ]))