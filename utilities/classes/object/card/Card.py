import numbers
from utilities.classes.object.Object import Object
from utilities.functions.path import getPath
import pygame

class Card(Object):
    def __init__(self, number=None, color=None, type="Normal", coordinates=[1, 1], 
                dimensions=[100, 100], icon=getPath("images", "logo.png"), callback=None, ownerId=None):
        super().__init__(coordinates, dimensions, icon, callback=lambda : self.throwCard(1))
        #callback=lambda : self.throwCard(1) : when we click the card it must be played
        self.number = number
        self.color=color
        self.type=type
        self.icon = icon
        #to know who throwed the card (still not used)
        self.ownerId=ownerId
        self.played=False
        
    # coloredType=["Skip", "Reverse", "Draw 2", "Draw 4", "Wild"]
    
    
    # to be reviewed
    def switchCard(self):
        if(self.type=="Skip"):
            print("You choose a skip card")
        elif(self.type=="Reverse"):
            print("You choose a reverse card")
        elif(self.type=="Draw2"):
            print("You choose draw 2 card")
        elif(self.type=="Draw4"):
            print("You choose a draw 4 card")
        else:
            print("Norml card was chosen")
    # get card's type 
    def getCardType(self):
        return self.type
    # set card's color
    def setCardColor(self,color):
        self.color = color
    # if a card is played this method returns True
    def isPlayed(self):
        return self.played
    # set played attr to True when a card is played
    def setPlayed(self):
        self.played = True
    # to get position of a card 
    def getPosition(self):
        return self.rect.center
    # to set new position of a card
    def setPosition(self, coordinates):
        self.rect.center = coordinates
    #we need this return value to add the ( ex card) to the ObjGrp        
        return self # We need this return value to chain methods
    
    # to get icon from a card
    def getIcon(self):
        return self.icon
    #getter for dim
    def getDimensions(self):
        return self.dimensions


    def compareSingleCard(self):
        from utilities.classes.game.Game import Game as Game_t
        lastPlayedCard=Game_t.state["lastPlayedCard"]
        #if this the first card on the game nothing happens 
        if(not lastPlayedCard):
            return self
        
        if self.type=="Normal":
            if(lastPlayedCard.getColor()==self.getColor() or lastPlayedCard.getNumber()==self.getNumber()):
                return self
            return None
        #for wild card
        elif self.type=="Wild":
            # we will add some code here 
            return self
        #if it's a special card
        elif self.type in ["Skip", "Reverse", "Draw", "Draw4"]:
            if(lastPlayedCard.getColor()==self.getColor()):
                return self
        return None
    
    def throwCard(self, playerId):
        from utilities.classes.game.Game import Game as Game_t
    #we need the playerId in case not the activePlayer
        if playerId==Game_t.state["activePlayer"]:
            #if compareSingleCard() returns a card
            if self.compareSingleCard():
                newHand=[]
                #we want to know which cards will be in the new hand  so we
                #by detecting the clicked card 
                for card in Game_t.getState("playersList")[playerId].getHand():
                    if(card.getId()!=self.getId()):
                        newHand.append(card)
                #the nexPlayer is the same activePlayer 
                #but we want to update his hand 
                newPlayer=Game_t.getState("playersList")[playerId]
                newPlayer.hand=newHand
                Game_t.state["playersList"][playerId]=newPlayer
                Game_t.playedCards[self.getId()]=self
                Game_t.rotate()
                Game_t.state["lastPlayedCard"]=self
                pygame.time.delay(1000)
                return True
            """changes playerActive to next player hence this player's to false"""
    def getColor(self):
        return self.color
    
    def getNumber(self):
        return self.number
    def __str__(self):
        return f"Number : {self.number} Color : {self.color}"