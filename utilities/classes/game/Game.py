import pygame, sys
from utilities.classes.object.Object import Object
from utilities.functions.path import getPath
from utilities.functions.resize import getSize
from utilities.classes.Ai.Ai import Ai
from utilities.classes.object.player.Player import Player
from utilities.classes.object.deck.Deck import Deck
from utilities.functions.path import writeText

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
            "playersList": []
        } # this dictionary will keep track of the game state
    # iterface settings
    framesPerSecond=60
    clock=pygame.time.Clock()
    screenWidth=1280
    screenHeight=640
    # the space of the playground once u drag the card into it u can't move anymore 
    playGround={
        "topHight": screenHeight/2-100,
        "bottomHight": screenHeight/2+100,
        "rightWidth": screenWidth/2+100,
        "leftWidth": screenWidth/2-100
    }
    screen=pygame.display.set_mode((screenWidth, screenHeight))
    # contains all objects that are rendered at any given momment
    objectsGroup=[
        Object([100,screenHeight/2], [80, 20],icon=getPath("images", "cards", "Deck.png")),
        Object([100, 50], [100, 20],icon=getPath("images", "icons", "avatar10.png")),
        Object([screenWidth-100, screenHeight-50], [100, 20],icon=getPath("images", "icons", "avatar6.png"))
    ]
    # set background for game interface
    backgroundImage = pygame.image.load(getPath('images', 'cards',"Table_4.png"))
    backgroundImage = pygame.transform.scale(
    backgroundImage, getSize(getPath('images', 'backgroundCards.jpg'), screenWidth))
    
   

    def __init__(self):
    # Will add gameMode as attr later 
       pass
    # initialize a deck of cards at the start of the game
    deck=Deck()
    def launch(self):
        # generate a list of players
        self.generatePlayers() 
        # stock players list in a list 
        players = Game.getState("playersList")
        # affect 7 cards to each player 
        Game.deck.distributeCard()
        # to add player's cards to objectsGroup
        # a loop that keeps running as long as we're playing the game
        # self.renderDeckUnoAvatars()
        # self.renderPlayerHand()
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
                elif(Game.getState("gameEnded")):
                    # call displayResults()
                    pass
            # rendering the game
            pygame.display.update()
            Game.screen.blit(Game.backgroundImage, (0, 0))
            # self.renderPlayerHand(players[0])
            self.render()
            print(len(Game.objectsGroup))
            writeText("10 Cards Left", 100, 120, 30, Game.screen)
            writeText("Me", Game.screenWidth-100, Game.screenHeight-120, 30, Game.screen)
            self.clock.tick(Game.framesPerSecond)
         
    @classmethod # modify a value in the state by passing its key ( if it exists )
    def setState(cls, key, value):
        if(key in cls.state.keys()):
            cls.state[key]=value
       
    # None is returned implicitly if the key doesn't exist in the state
    @classmethod
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
                Game.getState("playersList").extend([
                    Ai(0),
                    Player(1)])
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
    # display player's hand
    def renderPlayerHand(self):
        hand =Game.getState("playersList")[1].getHand()
        for i in range(len(hand)) :
            shiftX = 50
            Game.getState("playersList")[1].getHand()[i].setPosition([Game.screenWidth/2-i*len(hand)*10,Game.screenHeight-100])
            Game.getState("playersList")[1].getHand()[i].add()
        
            
    

    # display deck icon 
    def renderDeckUnoAvatars(self):
        pass        
    # display the results of the game
    def displayResults(self):
        pass
    