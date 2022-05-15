import pygame, sys
from utilities.classes.object.Object import Object
from utilities.functions.path import getPath
from utilities.functions.resize import getSize
from utilities.classes.Ai.Ai import Ai
from utilities.classes.object.player.Player import Player
from utilities.classes.object.deck.Deck import Deck

pygame.init()
pygame.display.set_caption('UNO')
pygame.display.set_icon(pygame.image.load(getPath("images", "cards", "Wild.png")))

class Game:
    # Class attrs
    state={
            "rotation": 1, # it could be 1, -1, or eventially 2
            "winner": None,
            "activePlayer": None,#contains the id of the active player
            # representes an event that player can trigger 
            "event": None, 
            # equals true when the game is finished
            "gameEnded": False,
            # list of players 
            "playersList": [],
        } # this dictionary will keep track of the game state
# iterface settings
    framesPerSecond=60
    clock=pygame.time.Clock()
    screenWidth=1280
    screenHeight=640
    screen=pygame.display.set_mode((screenWidth, screenHeight))
    # contains all objects that are rendered at any given momment
    objectsGroup=[
        Object(True, [60, 100], [100, 20], getPath('images', "cards", 'Blue_0.png')), # just for testing
        Object(True, [900, 600], [100, 30], getPath('images', "cards", 'Red_0.png')) # just for testing
    ]
    # set background for game interface
    backgroundImage = pygame.image.load(getPath('images', 'cards',"Table_4.png"))
    backgroundImage = pygame.transform.scale(
        backgroundImage, getSize(getPath('images', 'backgroundCards.jpg'), screenWidth))
    
    # initialize a deck of cards at the start of the game
    deck=Deck()

    def __init__(self):
    # Will add gameMode as attr later 
       pass
        
    
    def launch(self):
        
        # generate a list of players
        self.generatePlayers() 
        # a loop that keeps running as long as we're playing the game
        while(True):
            
            for event in pygame.event.get():
                # set the occured event 
                Game.setState("event", event)
                # check if player quits the game
                if(event.type == pygame.QUIT):
                # Will add more conditions in next version
                    pygame.quit()
                    sys.exit()
                # check if game has ended
                elif(Game.state["gameEnded"]):
                    # call displayResults()
                    pass
            # rendering the game
            pygame.display.update()
            Game.screen.blit(Game.backgroundImage, (0, 0))
            self.render()
            self.clock.tick(Game.framesPerSecond)
         
    @classmethod # modify a value in the state by passing its key ( if it exists )
    def setState(cls, key, value):
        if(key in cls.state.keys()):
            cls.state[key]=value
       
    # None is returned implicitly if the key doesn't exist in the state
    @staticmethod
    def getState(cls, key):
        if(key in cls.state.keys()):
            return cls.state[key]
    # render every object in objectGroup 
    def render(self):
        for obj in Game.objectsGroup:
            if(obj==None): # None values are objects that has been destroyed
                continue
            else:
                # render an object to the screen
                obj.update()
        
    def generatePlayers(self, numOfPlayers=2, botExists=True):
        # bot here representes Ai 
        if(botExists):    
            if(numOfPlayers==2):
                # set list of players ( Ai and real player in this case )
                Game.setState("playersList", Game.state["playersList"].extend([
                    Ai(0),
                    Player(1)
                ]))
            # more than two players
            else:
                Game.setState("playersList", Game.getState("playersList").extend([Player(0)]))    
                Game.setState("playersList", Game.getState("playersList").extend([
                    Ai(i) for i in range(1, numOfPlayers)
                ]))
        # all players are real 
        else:
            Game.setState("playersList", Game.getState("playersList").extend([
                Player(i) for i in range(numOfPlayers)
            ]))

    # display deck icon 
    def renderDeck(self):
        pass 
    # display results when the game has ended
    def displayResults(self):
        pass
    # 
    