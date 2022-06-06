from random import random
import time
import pygame, sys
import threading
from utilities.classes.object.Object import Object
from utilities.functions.path import getPath
from utilities.functions.resize import getSize
from utilities.classes.Ai.Ai import Ai
from utilities.classes.Ai.advanced_ai import advanced_ai
from utilities.classes.object.player.Player import Player
from utilities.classes.object.deck.Deck import Deck
from utilities.functions.path import writeText
from utilities.sockets.Server import Server
from utilities.sockets.Client import Client


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
            "timer": 10,
            "lastCheckedTime": 0,
            "server": None,
            "client": None,
        } # this dictionary will keep track of the game state
    
    #interface settings
    framesPerSecond=60
    clock=pygame.time.Clock()
    screenWidth=1280
    screenHeight=640
    maxWaitingTime=10
    screen=pygame.display.set_mode((screenWidth, screenHeight))
    # contains all objects that are rendered at any given momment
    positions={
        "deck": (100, screenHeight/2),
        "playedCards": (screenWidth/2, screenHeight/2),
        "winningText": (screenWidth/2, screenHeight/3)
    }
    #dict foe object ID 
    objectsGroup={} 
    ##dict for object ID 
    playedCards={} 
    deck = Deck()
    #running used to go from oe interface to another 
    running = True 
    # set background for game interface
    backgroundImage = pygame.image.load(getPath('images', 'cards',"Table_4.png"))
    backgroundImage = pygame.transform.scale(
    backgroundImage, getSize(getPath('images', 'backgroundCards.jpg'), screenWidth))

    check=False
    def __init__(self, is_client=True):
    # Will add gameMode as attr later 
        self.is_client = is_client
        thread = threading.Thread(target=self.startSockets)
        thread.start()  
    # initialize a deck of cards at the start of the game
    
    def run(self):
        # generate a list of players
        self.generatePlayers() 
        self.setUp()
        # stock players list in a list 
        players = Game.getState("playersList")
        # affect 7 cards to each player 
        Game.deck.distributeCard()
        # for testing
        if(Game.getState("client")):
            Game.getState("client").send("The Game started helloo")
        # a loop that keeps running as long as we're playing the game
        while(True):
            # Game.state["playersList"][1].hand=[] #for testing
            # if(Game.getState("lastPlayedCard")): self.applyEffect()
            # print("Last played card: ",Game.getState("lastPlayedCard"))
            self.renderPlayedCard()
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
            self.displayWinner()
            if(isinstance(players[Game.getState("activePlayer")], advanced_ai) or isinstance(players[Game.getState("activePlayer")],Ai)):
                # print("Ai is playing")
                players[Game.getState("activePlayer")].performMove()
            # rendering the game
            pygame.display.update()
            Game.screen.blit(Game.backgroundImage, (0, 0))
            
            # self.renderPlayerHand(players[0])
            self.render()
            self.clock.tick(Game.framesPerSecond)
         
    @classmethod # modify a value in the state by passing its key ( if it exists )
    def setState(cls, key, value):
        if(key in cls.state.keys()):
            cls.state[key]=value
            return value
       
    # None is returned implicitly if the key doesn't exist in the state
    @classmethod
    def getState(cls, key):
        if(key in cls.state.keys()):
            return cls.state[key]

     #method to review !!!   
    @classmethod
    def rotate(cls):
        #rotateBy 
        numOfPlayers=len(Game.getState("playersList"))
        rotateBy=Game.getState("rotation")
        activeId=Game.getState("activePlayer")
        
        if(rotateBy>1 or rotateBy<-1): return
        #to be reviewed
        if(activeId + rotateBy>numOfPlayers-1):
            Game.setState("activePlayer", 0)
            return
        
        if(activeId + rotateBy<0):
            Game.setState("activePlayer", numOfPlayers-1)
            return
        
        Game.setState("activePlayer", activeId + rotateBy)
        
    # render every object in objectGroup 
    def render(self):
        self.regenerateDeck()
        #show how many cards are left in the AI's hand 
        botCardsNumber=len(Game.getState("playersList")[0].getHand())
        self.renderTimer()
        writeText(f"{botCardsNumber} Cards Left", 100, 120, 30, Game.screen)
        writeText("Me", Game.screenWidth-100, Game.screenHeight-120, 30, Game.screen)

        #loop to update the objects in the game 
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
                    advanced_ai(0),
                    #the human player starts first 
                    Player(1)]
                    )
            # more than two players
            else:
                Game.setState("playersList", Game.getState("playersList") + [Player(0)])    
                Game.setState("playersList", Game.getState("playersList") + [
                    advanced_ai(i) for i in range(1, numOfPlayers)
                ])
        # all players are real 
        else:
            
            Game.setState("playersList", Game.getState("playersList") + [
                Player(i) for i in range(numOfPlayers)
            ])
            
    # display player's hand, it's responsive now
    def renderPlayerHand(self):
        hand =Game.getState("playersList")[1].getHand() # index 0 not 1, 1 is the AI
        len_t=len(hand) #how many cards in hand
        if(not len_t): return # if no cards in hand, return nothing
        cardMargin=10 # space left between cards
        handMargin= 200 # space left between hand and screen
        cardWith=(Game.screenWidth-2*handMargin-(len_t-1)*cardMargin)/len_t #dynamic card width
        moveBy=handMargin
        # to limit the width of the card
        if(cardWith>100): 
            cardWith=100
            moveBy+=(Game.screenWidth-2*handMargin-(cardWith+cardMargin)*len_t)/2
        for i in range(len_t):
            hand[i].setPosition([moveBy, Game.screenHeight-100]).setDimentions((cardWith, 100)).add()
            moveBy+=cardMargin+cardWith
            
    # adds object to the screen 
    def setUp(self):
        Object([100, 50], [100, 20],icon=getPath("images", "icons", "avatar10.png")).add()
        Object(Game.positions["deck"], [80, 20],icon=getPath("images", "cards", "Deck.png"), 
               callback=lambda: Game.deck.drawingCallback()).add()
        Object([Game.screenWidth-100, Game.screenHeight-50], [100, 20],
               icon=getPath("images", "icons", "avatar6.png")).add()        
        Object([Game.screenWidth-100, Game.screenHeight-200], [100, 20],
               icon=getPath("images", "icons", "unoButton.png")).add()  
        if(not Game.deck.isEmpty()):
            Game.setState("lastPlayedCard", Game.deck.deck.pop())
    
    # display the results of the game
    def displayResults(self):
        pass # Will add this method later on
    
    # display the cards that have already been played
    def renderPlayedCard(self):
        # No need to render all the cards, just the one on the top
          if(Game.getState("lastPlayedCard")):
            Game.getState("lastPlayedCard").setPosition(Game.positions["playedCards"]).muteObject().add()
            Game.getState("lastPlayedCard").setPosition(Game.positions["playedCards"]).update()
            # print(Game.getState("lastPlayedCard"))
            
    # generate a deck of cards when the deck runs out of cards
    def regenerateDeck(self):
        # Check if deck is empty
        if(Game.deck.getSize()==0):
            # set a new deck from a set of played cards
            Game.deck.setDeck([card.unmuteObject() for card in list(Game.playedCards.values())])
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
            # Game.rotate()
            

    def showDeck(self):
        for card in self.deck:
            print(f"{card.number}_{card.color}")
            
    def displayWinner(self):
        if(Game.getState("playersList")[0].getHand() and Game.getState("playersList")[1].getHand()):
            return
        Game.setState("lastPlayedCard", None)
        if(not Game.getState("playersList")[0].getHand()):
            writeText(f"The Bot Wins, You May Win Next Time;)", Game.screenWidth/2, Game.screenHeight/3, 50, Game.screen)
            Object(Game.positions["playedCards"], (150, 0), 
                    getPath("images", "icons", "avatar10.png"), None).add()
            Object((Game.screenWidth/2, Game.screenHeight/2+150), (150, 0), 
                    getPath("images", "continue2.jpg"), Game.reset).add()
            Object((Game.screenWidth/2, Game.screenHeight/2+250), (150, 0), 
                    getPath("images", "exit.jpg"), Game.quit).add()
            return True
            
        if(not Game.getState("playersList")[1].getHand()):
            writeText(f"You Won, Good Boy;)", Game.screenWidth/2, Game.screenHeight/3, 50, Game.screen)
            Object(Game.positions["playedCards"], (150, 0), 
                    getPath("images", "icons", "avatar6.png"), None).add()
            
            Object((Game.screenWidth/2, Game.screenHeight/2+150), (150, 0), 
                    getPath("images", "continue2.jpg"), Game.reset).add()
            Object((Game.screenWidth/2, Game.screenHeight/2+250), (150, 0), 
                    getPath("images", "exit.jpg"), Game.quit).add()
            return True
    
    @classmethod
    def reset(cls):
        print("Resetting the game")
        # Class attrs
        Game.state={
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
        
        #dict foe object ID 
        Game.objectsGroup={} 
        ##dict for object ID 
        Game.playedCards={} 
        Game.deck = Deck()
        #running used to go from oe interface to another 
        Game.running = True 
    
    @classmethod
    def quit(cls):
        pygame.quit()
        sys.exit()
        
    def renderTimer(self):
        if(Game.getState("timer")==0):
            Game.deck.draw()
            Game.rotate()
            return self.resetTimer()
        current = time.time()
        # print(current-Game.getState("lastCheckedTime"))
        if(current-Game.getState("lastCheckedTime")>=1):
            Game.setState("timer", Game.getState("timer")-1)
            Game.setState("lastCheckedTime", current)
            # print("got herekkk")
        passed_time=Game.getState("timer")
        writeText(f"Time Left", Game.screenWidth-200, 100, 40, Game.screen)
        writeText(f"{passed_time} secondes", Game.screenWidth-200, 150, 30, Game.screen)
    
    def resetTimer(self):
        Game.setState("timer", Game.maxWaitingTime)
        Game.setState("lastCheckedTime", 0)

    def notify(self, message):
        writeText(message, Game.screenWidth/2, 100, 40, Game.screen)
        
        
    def startSockets(self):
        if(self.is_client):
            Game.setState("client", Client()).start()
        else:
            Game.setState("server", Server()).start()
            
    # the message should be in the form "action/method type args"
    def emit(self, message):
        if(self.is_client):
            return Game.getState("client").send(message)
        Game.getState("server").send(message)