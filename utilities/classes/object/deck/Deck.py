from random import randint
from utilities.functions.path import getPath
from utilities.classes.object.card.Card import Card
# from utilities.classes.game.Game import Game

class Deck():
    cardsColors=[ "Green", "Blue", "Red", "Yellow"]
    numbersRange=list(range(0,10)) #rang des number-cards (0-9 cards)
    # Draw type is for drawing two , Draw4 is for drawing 4
    coloredTypes=["Skip", "Reverse", "Draw","Draw4"]
    
    def __init__(self):
        self.normalCards=self.createNrmlCards()
        self.specialCards=self.createSpecialCards()
        print(len(self.specialCards))
        self.deck=self.normalCards + self.specialCards
        self.size=len(self.deck)
        self.isDeckEmpty=False
        self.shuffleDeck()
        
        
    # getters for deck and size
    def getDeck(self):
        return self.deck

    def getSize(self):
        return self.size

    # Shuffling the deck
    def shuffleDeck(self):
        for i in range(self.size-1,0,-1):
            j = randint(0,i+1) # x, y=y, x doesn't echange the value of x and y
            temp=self.deck[i]
            self.deck[i]=self.deck[j]
            self.deck[j]=temp

    # contruct the deck from the playground
    def setDeck(self, newDeckLst):
        self.deck=newDeckLst
        self.size=len(self.deck)
        self.shuffleDeck()

    #Draw une carte du deck aprés shuffling
    def draw(self, handOfPlayer, numberOfCards):
        topCard=None
        for i in range(0, numberOfCards):
            topCard=self.deck.pop()
            handOfPlayer.append(topCard)
            self.size-=1
        return topCard

    #Tester si le deck est isEmpty et changer la valeur de l'attr. isEmpty de l'instance
    def isEmpty(self):
        if self.size==0:
            self.isDeckEmpty=True
        return self.isDeckEmpty
    # create cards based on a type of card
    def createCards(self, listColors, listNumbers, typesList=["Normal"]):
        listOfCards=[]
        for type in typesList:
            if(type=="Normal"):
                for number in listNumbers:
                    for col in listColors:
                        listOfCards.append(Card(number, col, type, 
                            icon=getPath("images", "cards", f"{col}_{number}.png")))
            else:
                for col in listColors:
                        listOfCards.append(Card(0, col, type,
                        icon=getPath("images","cards", f"{col}_{type}.png")))

        return listOfCards
    # once a set of cards is created , this method allows for cloning a list of cards from each type
    def cloneCards(self, listCards, clonesPerCard=2):
        listOfCards=list(listCards)
        for item in listCards:
            j=listOfCards.index(item)
            for i in range(1, clonesPerCard):
                listOfCards.insert(j+i,item)
        return listOfCards
    # create 4 wild cards
    def createWildCards(self, numberOfwildCards):
        listOfWildCards=[Card(type="Wild", icon=getPath("images", "cards", "Wild.png"))]#une carte wild est crée dans la liste
        return self.cloneCards(listOfWildCards, numberOfwildCards)
    # create 76 normal cards , 4 for each color and number
    def createNrmlCards(self):
        subDeck1=self.createCards(Deck.cardsColors, Deck.numbersRange)
        subDeck=self.cloneCards(subDeck1[4:],2)
        return subDeck + subDeck1[:4]
    # create specialCards 
    def createSpecialCards(self):
        subDeck=self.createCards(Deck.cardsColors, Deck.numbersRange, Deck.coloredTypes)
        subDeckWild=self.createWildCards(4)
        subDeckSpecial=self.cloneCards(subDeck,2)
        return subDeckSpecial + subDeckWild
    
    # Game_t.Game.getState("playersList") cercular import bug should be fixed
    # fixed the method :D 
    def distributeCard(self, number=7):
        import utilities.classes.game.Game as Game_t
        for i in range(len(Game_t.Game.getState("playersList"))):
            self.draw(Game_t.Game.getState("playersList")[i].getHand(), number)

        
