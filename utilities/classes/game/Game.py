from turtle import position
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
            "activePlayer": 1,#contains the id of the active player
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
    screen=pygame.display.set_mode((screenWidth, screenHeight))
    # contains all objects that are rendered at any given momment
    objectsGroup=[]
    playedCards=[]
    # set background for game interface
    backgroundImage = pygame.image.load(getPath('images', 'cards',"Table_4.png"))
    backgroundImage = pygame.transform.scale(
    backgroundImage, getSize(getPath('images', 'backgroundCards.jpg'), screenWidth))
    positions={
        "deck": (100, screenHeight/2),
        "playedCards": (screenWidth/2, screenHeight/2)
    }
   

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
                elif(Game.getState("gameEnded")):
                    # call displayResults()
                    pass
            # rendering the game
            pygame.display.update()
            Game.screen.blit(Game.backgroundImage, (0, 0))
            # self.renderPlayerHand(players[0])
            self.render()
            botCardsNumber=len(Game.getState("playersList")[0].getHand())
            writeText(f"{botCardsNumber} Cards Left", 100, 120, 30, Game.screen)
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
        
    @classmethod
    def rotate(cls, rotateBy=1):
        numOfPlayers=len(Game.getState("playersList"))
        activeId=Game.getState("activePlayer")
        if(rotateBy>1 or rotateBy<-1): return
        if(activeId + rotateBy>=numOfPlayers):
            Game.setState("activePlayer", 0)
            Game.state["rotation"]=1
            return
        if(activeId + rotateBy<0):
            Game.setState("activePlayer", numOfPlayers-1)
            Game.state["rotation"]=-1
            return
        Game.setState("activePlayer", activeId + rotateBy)
        Game.state["rotation"]=1
        
    # render every object in objectGroup 
    def render(self):
        self.regenerateDeck()
        self.renderPlayerHand()
        self.renderPlayedCards()
        self.renderDeckUnoAvatars()
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
                Game.setState("playersList", [
                    Ai(0),
                    Player(1)]
                    )
            # more than two players
            else:
                Game.setState("playersList", Game.getState("playersList") + [Player(0)])    
                Game.setState("playersList", Game.getState("playersList") + [
                    Ai(i) for i in range(1, numOfPlayers)
                ])
        # all players are real 
        else:
            Game.setState("playersList", Game.getState("playersList") + [
                Player(i) for i in range(numOfPlayers)
            ])
            
    # display player's hand
    def renderPlayerHand(self):
        hand =Game.getState("playersList")[1].getHand() # index 0 not 1, 1 is the AI
        len_t=len(hand)
        for i in range(len_t) :
            shiftX = 50
            hand[i].setPosition([Game.screenWidth/3+i*shiftX,Game.screenHeight-100]).add()
            
    # display deck icon 
    def renderDeckUnoAvatars(self):
        Object(Game.positions["deck"], [80, 20],icon=getPath("images", "cards", "Deck.png")).add()
        Object([100, 50], [100, 20],icon=getPath("images", "icons", "avatar10.png")).add()
        Object([Game.screenWidth-100, Game.screenHeight-50], [100, 20],icon=getPath("images", "icons", "avatar6.png")).add()        
        Object([Game.screenWidth-300, Game.screenHeight-100], [100, 20],icon=getPath("images", "icons", "unoButton.png")).add()        
    
    # display the results of the game
    def displayResults(self):
        pass # Will add this method later on
    
    # display the cards that have already been played
    def renderPlayedCards(self):
        # No need to render all the cards, just the one on the top
        if(Game.playedCards):
            Game.playedCards[-1].setPosition(Game.positions["playedCards"]).add()
    
    # generate a deck of cards when the deck runs out of cards
    def regenerateDeck(self):
        if(Game.deck.isEmpty()):
            Game.deck.setDeck([
                card.setPosition(Game.positions["deck"]) for card in Game.playedCards
            ])
            for card in Game.playedCards:
                card.desroyObject()
            Game.playedCards=[]
            
    @classmethod
    def ifAiPlay(cls):
        if Game.getState("activePlayer")==0:
            hasPlayed=False
            for card in Game.getState("playersList"):
                if(card.compareSingleCard()):
                    card.throwCard(0)
                    hasPlayed=True
                    break
            if(not hasPlayed):
                card=Game.deck.draw(Game.getState("playersList")[0].getHand(), 1)
                if(card.compareSingleCard()):
                    card.throwCard(0)
            Game.rotate(Game.getState("rotation"))