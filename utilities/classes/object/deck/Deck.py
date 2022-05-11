
from utilities.functions.functions import createNrmlCards, createSpecialCards
from random import randint

class Deck():
    "Ceci est un deck de cartes"
    #construction d'un deck de cartes 
    def __init__(self):
        #la construction du deck est subdivisées

        subDeck1=createNrmlCards()
        subDeck2=createSpecialCards()
        #ce deck est Ordonné
        #Fusion des cartes normales et speciales en une seule liste
        subDeck1.extend(subDeck2)
        #construction de la liste des cartes
        self.deck=list(subDeck1)
        #Definition de la taille du deck
        self.taille=len(self.deck)
        #tester si le deck est vide
        self.vide=False
        #shuffle the deck
        self.shuffleDeck()
    @classmethod
        #Getters
    def getDeck(self):
        return self.deck
    def getTaille(self):
        return self.taille


    #shuffling
    # Une methode pour permuter le deck aprés sa construction
    # avec algorithme de Fisher–Yates
    def shuffleDeck(self):
        # Commençant par le dernier élement on permute un par un 
        for i in range(self.taille-2,0,-1):
        # indice aléatoire de 0 à i
            j = randint(0,i+1)
        # permuter self.deck[i] par celui d'indice aléatoire
            self.deck[i],self.deck[j] = self.deck[j],self.deck[i]
        print("The deck is shuffled")


    #Construction du deck à partir de la liste du terrain
    def setDeck(self,newDeckLst):
        #set la liste du deck
        self.deck=newDeckLst
        #set la taille du deck
        self.taille=len(self.deck)
        #Shuffling 
        self.deck.shuffleDeck()

    #Draw une carte du deck aprés shuffling
    def Draw(self,handOfPlayer,numberOfCards):
            #suppression du dernier element + son ajout a la main du joueur
            for i in range(0,numberOfCards):
                handOfPlayer.append(self.deck.pop())
                #La diminution de la taille du deck
                self.taille-=1

    #Tester si le deck est vide et changer la valeur de l'attr. vide de l'instance
    def isEmpty(self):
        if self.taille==0:
            self.vide=True
        return self.vide
    #Affichage des cartes du deck
    def showDeck(self):
        print("Your deck :\n {")
        for i in range(0,self.taille):
            print(" ",self.deck[i])
        print("}")
