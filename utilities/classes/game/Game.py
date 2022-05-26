from turtle import position
import pygame, sys
from utilities.classes.object.Object import Object
from utilities.functions.path import getPath
from utilities.functions.resize import getSize
from utilities.classes.Ai.Ai import Ai
from utilities.classes.object.player.Player import Player
from utilities.classes.object.deck.Deck import Deck
from utilities.functions.path import writeText
from utilities.functions.Reverse import reverseOrder

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
            "playersList": [],
            "lastPlayedCard": None,
        } # this dictionary will keep track of the game state
    # iterface settings
    framesPerSecond=60
    clock=pygame.time.Clock()
    screenWidth=1280
    screenHeight=640
    screen=pygame.display.set_mode((screenWidth, screenHeight))
    # contains all objects that are rendered at any given momment
    positions={
        "deck": (100, screenHeight/2),
        "playedCards": (screenWidth/2, screenHeight/2)
    }
   
    objectsGroup={} #maps ids to obj
    playedCards={} #maps ids to obj too
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
        self.setUp()
        # stock players list in a list 
        players = Game.getState("playersList")
        # affect 7 cards to each player 
        Game.deck.distributeCard()
        # a loop that keeps running as long as we're playing the game
        while(True):
            self.renderPlayedCard()
            self.applyEffect()
            # print("My hand :")
            # for card in players[Game.getState("activePlayer")].hand:
            #     print(card)  
            # Check if the player has quit the game or if the game is over
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
            # Check if current player is a bot 
            currentPlayer = players[Game.getState("activePlayer")]
            if(isinstance(currentPlayer,Ai)):
                print("Ai is playing")
                currentPlayer.performMove()
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
        # copyList=Game.objectsGroup.values()
        for value in Game.objectsGroup.values():
            value.update()
        
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
        shiftX = 110
        width = shiftX * len_t
        margin=(Game.screenWidth-width)/2
        for i in range(len_t):
            hand[i].setPosition([margin+i*shiftX, Game.screenHeight-100]).add()
            
    # setting up the game
    def setUp(self):
        Object([100, 50], [100, 20],icon=getPath("images", "icons", "avatar10.png")).add()
        Object(Game.positions["deck"], [80, 20],icon=getPath("images", "cards", "Deck.png"), 
               callback=lambda: Game.deck.drawingCallback()).add()
        Object([Game.screenWidth-100, Game.screenHeight-50], [100, 20],
               icon=getPath("images", "icons", "avatar6.png")).add()        
        Object([Game.screenWidth-100, Game.screenHeight-200], [100, 20],
               icon=getPath("images", "icons", "unoButton.png")).add()    
           
    
    # display the results of the game
    def displayResults(self):
        pass # Will add this method later on
    
    # display the cards that have already been played
    def renderPlayedCard(self):
        # No need to render all the cards, just the one on the top
          if(Game.getState("lastPlayedCard")):
            Game.getState("lastPlayedCard").setPosition(Game.positions["playedCards"]).add()
            # print(Game.getState("lastPlayedCard"))
            
    # generate a deck of cards when the deck runs out of cards
    def regenerateDeck(self):
        # Check if deck is empty
        if(Game.deck.getSize()==0):
            # set a new deck from a set of played cards
            Game.deck.setDeck(list(Game.playedCards.values()))
            # set new size for this deck
            Game.deck.setSize(len(Game.playedCards.values()))
            # shuffle the deck 
            Game.deck.shuffleDeck()
            # empty playedCards
            Game.playedCards={}
            # pick a card from new shuffeled deck to move it to terrain
            Game.setState("lastPlayedCard",Game.deck.getDeck()[-1])
            # add lastPlayedCard to deck
            Game.playedCards[Game.deck.getDeck()[-1].getId()]= Game.deck.getDeck()[-1]
            # test 
            print("Deck : ")
            for card in Game.deck.getDeck():
                print(card)
            print("Played cards : ")
            for card in Game.playedCards.values():
                print(card)
            # Game.rotate(Game.state["rotation"])
            
    # to apply last played card special effect 
    def applyEffect(self): 
        if(Game.getState("lastPlayedCard").getCardType() is not "Normal" and not Game.getState("lastPlayedCard").isPlayed()):
                print("This is a special card")
                Game.getState("lastPlayedCard").setPlayed()
                if(Game.getState("lastPlayedCard").getCardType()=="Draw"):
                    print("Next player draws 2")
                elif(Game.getState("lastPlayedCard").getCardType()=="Draw4"):
                    print("Next player draws 4")
                elif(Game.getState("lastPlayedCard").getCardType()=="Reverse"):
                    print("Reverse order")
                    reverseOrder()
                elif(Game.getState("lastPlayedCard").getCardType()=="Skip"):
                    print("Skip to next player")
                elif(Game.getState("lastPlayedCard").getCardType()=="Wild"):
                    print("I'm wild baby!")

    def showDeck(self):
        for card in self.deck:
            print(f"{card.number}_{card.color}")
