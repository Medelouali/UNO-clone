from random import randint
from utilities.functions.path import getPath
from utilities.classes.object.card.Card import Card
# import utilities.classes.game.Game as Game_t
# from utilities.classes.game.Game import Game
from utilities.classes.object.Object import Object

class Deck(Object):
    cardsColors=[ "Green", "Blue", "Red", "Yellow"]
    numbersRange=list(range(0,10)) #rang des number-cards (0-9 cards)
    # Draw type is for drawing two , Draw4 is for drawing 4
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
        
    # it means nothing to make this method a class method

            
    def drawingCallback(self):
        from utilities.classes.game.Game import Game
        self.draw(1)
        Game.rotate()
        
    # getters for deck and size
    def getDeck(self):
        return self.deck

    def getSize(self):
        return self.size

    # Shuffling the deck
    def shuffleDeck(self):
        for i in range(self.size-1, 0, -1):
            j = randint(0, i+1) # x, y=y, x doesn't echange the value of x and y
            temp=self.deck[i]
            self.deck[i]=self.deck[j]
            self.deck[j]=temp

    # contruct the deck from the playground
    def setDeck(self, newDeckLst):
        self.deck=newDeckLst
        self.size=len(self.deck)
        self.shuffleDeck()

    #Draw une carte du deck aprés shuffling
    def draw(self, numberOfCards=1):
        from utilities.classes.game.Game import Game
        topCard=None
        activeId=Game.getState("activePlayer")
        if(self.isEmpty()): 
            print("can't draw deck's empty")
            return topCard
        print("playerHand ", len(Game.state["playersList"][activeId].hand))
        print("Deck number ", len(Game.deck.deck))
        for _ in range(numberOfCards):
            topCard=self.deck.pop()
            newHand=Game.state["playersList"][activeId].hand
            newHand.append(topCard)
            Game.state["playersList"][activeId].hand=newHand
            # print(len(Game.getState("playersList")[activeId].getHand()))
            self.size-=1
        return topCard

    #Tester si le deck est isEmpty et changer la valeur de l'attr. isEmpty de l'instance
    def isEmpty(self):
        if self.size==0:
            self.isDeckEmpty=True
        return self.isDeckEmpty
    
    def createCards(self, listColors, listNumbers, typesList=["Normal"]):
        listOfCards=[]
        for type in typesList:
            for number in listNumbers:
                for col in listColors:
                    listOfCards.append(Card(number, col, type, 
                        icon=getPath("images", "cards", f"{col}_{number}.png")))
        return listOfCards

    def cloneCards(self, listCards, clonesPerCard=2):
        listOfCards=list(listCards)
        for item in listCards:
            j=listOfCards.index(item)
            for i in range(1, clonesPerCard):
                listOfCards.insert(j+i,item)
        return listOfCards

    def createWildCards(self, numberOfwildCards):
        listOfWildCards=[Card(type="Wild", icon=getPath("images", "cards", "Wild.png"))]#une carte wild est crée dans la liste
        return self.cloneCards(listOfWildCards,numberOfwildCards)

    # create 76 normal cards , 4 for each color and number
    def createNrmlCards(self):
        subDeck1=self.createCards(Deck.cardsColors, Deck.numbersRange)
        subDeck=self.cloneCards(subDeck1[4:],2)
        return subDeck + subDeck1[:4]
    
    # create specialCards 
    def createSpecialCards(self):
        subDeck1=self.createCards(Deck.cardsColors, Deck.numbersRange, Deck.coloredTypes)
        subDeckWild=self.createWildCards(4)
        subDeckSpecial=self.cloneCards(subDeck1)
        return subDeckSpecial + subDeckWild
    
    # Game_t.Game.getState("playersList") cercular import bug should be fixed
    def distributeCard(self, number=7):
        import utilities.classes.game.Game as Game_t
        for i in range(len(Game_t.Game.getState("playersList"))):
            self.draw(number)
            Game_t.Game.rotate()