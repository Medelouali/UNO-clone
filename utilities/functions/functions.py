from utilities.classes.object.card.Card import Card
from utilities.functions.path import getPath
import utilities.variables.variables as var

def createCards(listColors, listNumbers, typesList=["Normal"]):
    #la liste des cartes a construire
    listOfCards=[]
    for type in typesList:
        for number in listNumbers:
            for col in listColors:
                listOfCards.append(Card(number, col, type, 
                    icon=getPath("images", "cards", f"{col}_{number}.png")))
    return listOfCards

#construire une liste de cartes avec des clones , par défaut on considere la valeur 2
def cloneCards(listCards, clonesPerCard=2):
    #la liste des cartes qui contiendra des clones des cartes de la liste "listCards"
    listOfCards=list(listCards)
    # l=len(listCards)
    for item in listCards:
        #index de item dans la nouvelle liste
        j=listOfCards.index(item)
        for i in range(1, clonesPerCard):
            #on insere les clones des cartes
            listOfCards.insert(j+i,item)
    return listOfCards

# creation de wild cards traitement a part (color=None, Number=None)
def createWildCards(numberOfwildCards):
    listOfWildCards=[Card(type="Wild", icon=getPath("images", "cards", "Wild.png"))]#une carte wild est crée dans la liste
    return cloneCards(listOfWildCards,numberOfwildCards)

# Construire Normal Cards
def createNrmlCards():
    #Les cartes colorées avec un Numéro 0-9
    subDeck1=createCards(var.unoColors, var.unoNumberRange)

    #Les cartes de 1:9 sont doublées =subDeck[4:]
    subDeck=cloneCards(subDeck1[4:],2)
    #fusion
    subDeck.extend(subDeck1[:4])
    #construire des cartes normales
    return subDeck

#construire des "special-cards"
def createSpecialCards():
    # Création des cartes de type "Skip" + "Reverse" +"Draw2/4"
    subDeck1=createCards(var.unoColors, var.unoNumberRange, var.coloredType)

    #Création des cartes de type "Wild"
    #creation de 4 wild cards
    subDeckWild=createWildCards(4)
    #cloner les cartes :"Draw 2/4" "Skip" "Reverse"
    subDeckSpecial=cloneCards(subDeck1)

    #special cards :subDeckSpecial + subDeckWild
    subDeckSpecial.extend(subDeckWild)
    return subDeckSpecial 
    # distribute 7 cards at the start of the game
def distributeCard(deck,listOfPlayers):
    # iterate over the list of players 
    for i in range(len(listOfPlayers)):
        # get the hand of each player
        currentPlayerHand = listOfPlayers[i].getHand()
        # call draw method on deck of cards to draw cards from it and into the hand of the current player
        deck.draw(currentPlayerHand,7)

