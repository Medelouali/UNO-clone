from random import randint, random
from utilities.functions.path import getPath
from utilities.classes.object.card.Card import Card
import pygame
from utilities.classes.object.Object import Object

class Deck(Object):
    cardsColors=[ "Green", "Blue", "Red", "Yellow"]
    numbersRange=list(range(0,10)) #rank of number-cards (0-9 cards)
    coloredTypes=["Skip", "Reverse", "Draw","Draw4"]
    
    def __init__(self):
        super().__init__(callback=self.drawingCallback, icon=getPath("images", "cards", "Deck.png"))
        self.normalCards=self.createNrmlCards()
        self.specialCards=self.createSpecialCards()
        self.deck=self.normalCards + self.specialCards
        self.size=len(self.deck)
        self.isDeckEmpty=False
        self.shuffleDeck()
        print(f"Cards created {len(self.deck)}")
    #draws one card by default
    #we can choose the number of cards to draw 
    def drawingCallback(self):
        from utilities.classes.game.Game import Game
        self.draw()
        Game.rotate()
        Game.setState("timer",10)
        
    # getters for deck and size
    def getDeck(self):
        return self.deck
    #getters : numbers of card in  the deck
    def getSize(self):
        return self.size
    def setSize(self,size):
        self.size = size

    # Shuffling the deck
    def shuffleDeck(self):
        for i in range(self.size-1, 0, -1):
<<<<<<< HEAD
            j = randint(0, i+1)
=======
            j = randint(0, i)
>>>>>>> ce1c7cffa018366234d273e6097525de675a5d3d
            temp=self.deck[i]
            self.deck[i]=self.deck[j]
            self.deck[j]=temp

    # contruct the deck from the playground
    def setDeck(self, newDeckLst):
        self.deck=newDeckLst
        self.size=len(self.deck)

    # Draw a card from the deck if it's not empty
    def draw(self, numberOfCards=1, activePlayer=None):
        from utilities.classes.game.Game import Game
        # if active player is not passed as an argument get the active player from Game's state
        if(activePlayer==None):
            activePlayer=Game.getState("activePlayer")
        topCard, activeId = None, activePlayer
        #activeId :current active player
        # _ is used to replace i since we won't be using it again 
        for _ in range(numberOfCards):
           #if the deck is empty topCard =None 
            if(len(self.deck) == 0): 
                self.regenerateDeck()
                return topCard
            topCard=self.deck.pop()
             # add deck top card into player's hand
            Game.state["playersList"][activeId].hand+= [topCard]
            #decmente size of the deck
            self.size-=1
        #we will need topCard for the AI to compare when he draws the card 
        return topCard

    #Testing if the deck isEmpty and changing the value of the attribute isEmpty of the instance
    def isEmpty(self):
        if self.size==0:
            self.isDeckEmpty=True
        return self.isDeckEmpty
    
    def createCards(self, listColors, listNumbers, typesList=["Normal"]):
        listOfCards=[]
        for type in typesList:
            if(type=="Normal"):
                for number in listNumbers:
                    for col in listColors:
                        for i in range(2):
                            listOfCards.append(Card(number, col, type, 
                                icon=getPath("images", "cards", f"{col}_{number}.png")))
            else:
                for col in listColors:
                    for i in range(2):
                        listOfCards.append(Card(None, col, type,
                        icon=getPath("images","cards", f"{col}_{type}.png")))

        return listOfCards
    #create deck from the cards already played 
    def cloneCards(self, listCards, clonesPerCard=2):
        listOfCards=list(listCards)
        for item in listCards:
            j=listOfCards.index(item)
            for i in range(1, clonesPerCard):
                listOfCards.insert(j+i, item)
        return listOfCards
    # create 4 wild cards
    def createWildCards(self):
        listOfWildCards=[]
        for i in range(4):
            listOfWildCards.append(Card(type="Wild", icon=getPath("images", "cards", "Wild.png")))
            #a  wild card is created in the list
        return listOfWildCards
    
    # create 76 normal cards , 4 for each color and number
    def createNrmlCards(self):
        return self.createCards(Deck.cardsColors, Deck.numbersRange)
    
    def createSpecialCards(self):
        subDeck=self.createCards(Deck.cardsColors, [None], Deck.coloredTypes)
        subDeckWild=self.createWildCards()
        return subDeck+subDeckWild
    
    def distributeCard(self, number=7):
        import utilities.classes.game.Game as Game_t
        #we loop on the players  to distribute the card
        for _ in range(len(Game_t.Game.getState("playersList"))):
            self.draw(number)
            Game_t.Game.rotate()
            i=1
            while(self.deck[-i].type!="Normal"):
                i+=1
            Game_t.Game.setState("lastPlayedCard",self.deck.pop(-i))
        
    def regenerateDeck(self):
        import utilities.classes.game.Game as Game_t
        Game_t.Game.setState("message","Building deck ...")
        pygame.time.wait(1000)
        self.deck = list(Game_t.Game.playedCards.values())
        self.size = len(self.deck)
        print("Deck : ")
        for card in Game_t.Game.deck.getDeck():
            print(card)
        
