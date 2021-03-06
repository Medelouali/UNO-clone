import random
import time
import pygame, sys
import threading
from utilities.classes.Ai.random_ai import random_ai
from utilities.classes.object.Object import Object
from utilities.functions.path import getPath
from utilities.functions.resize import getSize
from utilities.classes.Ai.random_ai import random_ai
from utilities.classes.Ai.bot_player import bot_player
from utilities.classes.Ai.advanced_ai import advanced_ai
from utilities.classes.object.player.Player import Player
from utilities.classes.object.deck.Deck import Deck
from utilities.functions.path import writeText
from utilities.classes.object.color_picker import ColorPicker




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
            #difficulty settings :: Type of Ai
            "Difficulty" : "Normal",
            "numOfPlayers" : 2,
            "message" : "",
            "chosen_color":None
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
    colorPicker = ColorPicker()
    #running used to go from oe interface to another 
    running = True 
    # set background for game interface
    backgroundImage = pygame.image.load(getPath('images', 'cards',"Table_4.png"))
    backgroundImage = pygame.transform.scale(
    backgroundImage, getSize(getPath('images', 'backgroundCards.jpg'), screenWidth))

    def __init__(self):
    # initialize a deck of cards at the start of the game
        pass
    
    def run(self):
        # generate a list of players
        self.generatePlayers() 
        self.setUp()
        T=True
        # stock players list in a list 
        players = Game.getState("playersList")
        # affect 7 cards to each player 
        Game.deck.distributeCard()
        # a loop that keeps running as long as we're playing the game
        pygame.time.delay(1000)
        while(T):
            # Game.state["playersList"][1].hand=[] #for testing
            # if(Game.getState("lastPlayedCard")): self.applyEffect()
            # print("Last played card: ",Game.getState("lastPlayedCard"))
            self.renderPlayedCard()
            self.notify()
            # Check if the player has quit the game or if the game is over
            for event in pygame.event.get():
                    # set the occured event 
                    Game.setState("event", event)
                    # check if player quits the game
                    if(event.type == pygame.QUIT):
                    # Will add more conditions in next version
                        pygame.quit()
                        sys.exit()
                    #force the end of game
                    if(event.type == pygame.KEYDOWN or event.type == pygame.KEYUP ):
                        # if (event.type == pygame.K_p):
                            print("forcing endgame")
                            Game.getState("playersList")[1].setHand([])
                    # check if game has ended

                    if(Game.getState("gameEnded")):
                        # call displayResults()
                        Game.setState("gameEnded",False)
                        T=False
            #Verifying if a hand is empty
            if( Game.getState("playersList")[0].getHand()==[] or Game.getState("playersList")[1].getHand() ==[] ):
                Game.setState("gameEnded",True)
                # Game.setState("lastPlayedCard", None)
                # T=False
            # Check if current player is a bot 
            # self.displayWinner()
            if(isinstance(players[Game.getState("activePlayer")], bot_player)):
                # print("Ai is playing")
                # before playing a card, check if previous player has screamed UNO
                # to base screaming UNO purely on chance for the ai 
                head_or_tails = random.randint(0,1)
                if(head_or_tails):
                    self.unoScream()
                # play ai's turn
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
        # print(Game.getState("chosen_color"))
        #rotateBy 
        numOfPlayers=len(Game.getState("playersList"))
        rotateBy=Game.getState("rotation")
        activeId=Game.getState("activePlayer")
        # last = pygame.time.get_ticks()
        # cooldown = 300
        # now=pygame.time.get_ticks()
        # if now -last >=cooldown:
        #     last = now
        if(rotateBy>1 or rotateBy<-1): 
            return
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
        #show how many cards are left in the AI's hand 
        botCardsNumber=len(Game.getState("playersList")[0].getHand())
        # secondbotCardsNumber=len(Game.getState("playersList")[2].getHand())
        self.renderTimer()
        writeText(f"{botCardsNumber} Cards Left", 100, 120, 30, Game.screen)
        # writeText(f"{secondbotCardsNumber} Cards Left", 500, 120, 30, Game.screen)
        writeText("Me", Game.screenWidth-100, Game.screenHeight-120, 30, Game.screen)

        #loop to update the objects in the game 
        self.renderPlayerHand() 
        # copyList=Game.objectsGroup.values()
        for value in list(Game.objectsGroup.values()):
            value.update()
        
    def generatePlayers(self):  
                # set list of players ( Ai and real player in this case )
                Game.setState("playersList", [
                    advanced_ai(0),
                     #the human player starts first 
                     Player(1)])
       
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
            hand[i].setPosition([moveBy, Game.screenHeight-100]).setDimensions((cardWith, 100)).add()
            moveBy+=cardMargin+cardWith
            
    # adds object to the screen 
    def setUp(self):
        Object([100, 50], [100, 20],icon=getPath("images", "icons", "avatar10.png")).add()
        # Object([500, 50], [100, 20],icon=getPath("images", "icons", "avatar10.png")).add()
        Object(Game.positions["deck"], [80, 20],icon=getPath("images", "cards", "Deck.png"), 
               callback=lambda: Game.deck.drawingCallback()).add()
        Object([Game.screenWidth-100, Game.screenHeight-50], [100, 20],
               icon=getPath("images", "icons", "avatar6.png")).add()        
        Object([Game.screenWidth-100, Game.screenHeight-200], [100, 20],
               icon=getPath("images", "icons", "unoButton.png"),callback=lambda: self.unoScream()).add()  
        if(not Game.deck.isEmpty()):
            Game.setState("lastPlayedCard", Game.deck.deck.pop())
    
    # display the cards that have already been played
    def renderPlayedCard(self):
        # No need to render all the cards, just the one on the top
          if(Game.getState("lastPlayedCard")):
            Game.getState("lastPlayedCard").setPosition(Game.positions["playedCards"]).setDimensions([100, 200]).muteObject().add()
            Game.getState("lastPlayedCard").setPosition(Game.positions["playedCards"]).update()
    
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
                "unoScream":False,
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
    # to render the timer
    def renderTimer(self):
        if(Game.getState("timer")==0):
            if(Game.getState("lastPlayedCard").getCardType()=="Wild" and Game.getState("chosen_color")==None):
                Game.getState("chosen_color")=="Red"
                Game.setState("message","We picked for you , be quicker next time")
            Game.deck.draw()
            Game.setState("message","Be quicker next time")
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
    # to reset the round timer
    def resetTimer(self):
        Game.setState("timer", Game.maxWaitingTime)
        Game.setState("lastCheckedTime", 0)
    # to display a message to the player notifying them of any changes made to the game state
    def notify(self):
        writeText(Game.getState("message"), Game.screenWidth/2, 50, 30, Game.screen)
        
    # control uno scream's logic
    def unoScream(self):
        current_player =Game.getState("playersList")[Game.getState("activePlayer")]
    # in case the current player needs to scream UNO
        if(len(current_player.getHand())==1):
            Game.getState("playersList")[Game.getState("activePlayer")].screamedUno=True
            Game.setState("message","UNO !!!")
            # to check if the previous player screamed uno 
            previous_player=Game.getState("playersList")[abs(Game.getState("activePlayer")-1)]
            if(len(previous_player.getHand())==1 and previous_player.screamedUno==False):
                # if he had to scream it and haven't then he has to draw two cards
                # draw two cards
                Game.deck.draw(2,abs(Game.getState("activePlayer")-1))
            # in case the previous player screamed UNO , we reset screamUno to False again for the next turn
            else:Game.getState("playersList")[abs(Game.getState("activePlayer")-1)].screamedUno=False
    