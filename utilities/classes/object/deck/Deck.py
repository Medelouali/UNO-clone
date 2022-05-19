from random import randint
from utilities.functions.path import getPath
from utilities.classes.object.card.Card import Card
# from utilities.classes.game.Game import Game

class Deck():
    cardsColors=[ "Green", "Blue", "Red", "Yellow"]
    numbersRange=list(range(0,10)) #rang des number-cards (0-9 cards)
    coloredTypes=["Skip", "Reverse", "Draw 2", "Draw 4"]
    
    def __init__(self):
        self.normalCards=self.createNrmlCards()
        self.specialCards=self.createSpecialCards()
        self.deck=self.normalCards + self.specialCards
        self.size=len(self.deck)
        self.isEmpty=False
        self.shuffleDeck()
        
    # it means nothing to make this method a class method
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
<<<<<<< HEAD
    def Draw(self, handOfPlayer, numberOfCards):
             #liste pour stocker les cartes supprimées par pop()
               for i in range(0,numberOfCards):
                    temp = self.deck.pop()
                 #on ajoute les cartes piochées dans la main du joueur
                    handOfPlayer.append(temp)
                  # add card to ObjectGroup 
                  # add is a setter 
                    object.add(temp)
                  #La diminution de la taille du deck
                    self.taille
    
    #Tester si le deck est vide et changer la valeur de l'attr. vide de l'instance
=======
    def draw(self, handOfPlayer, numberOfCards):
            for i in range(0, numberOfCards):
                handOfPlayer.append(self.deck.pop())
                self.size-=1

    #Tester si le deck est isEmpty et changer la valeur de l'attr. isEmpty de l'instance
>>>>>>> 941e77904001d04579f676b8f8ec96795f9b33ed
    def isEmpty(self):
        if self.size==0:
            self.isEmpty=True
        return self.isEmpty
    
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
        return self.cloneCards(listOfWildCards, numberOfwildCards)

    def createNrmlCards(self):
        subDeck1=self.createCards(Deck.cardsColors, Deck.numbersRange)
        subDeck=self.cloneCards(subDeck1[4:],2)
        return subDeck + subDeck1[:4]

    def createSpecialCards(self):
        subDeck1=self.createCards(Deck.cardsColors, Deck.numbersRange, Deck.coloredTypes)
        subDeckWild=self.createWildCards(4)
        subDeckSpecial=self.cloneCards(subDeck1)
        return subDeckSpecial + subDeckWild
    
    # Game_t.Game.getState("playersList") cercular import bug should be fixed
    # fixed the method :D 
    def distributeCard(self, number=7):
        import utilities.classes.game.Game as Game_t
        for i in range(len(Game_t.Game.getState("playersList"))):
            self.draw(Game_t.Game.getState("playersList")[i].getHand(), number)

        
