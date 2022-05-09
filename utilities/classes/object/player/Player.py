from utilities.classes.game import Game
from utilities.classes.game.State import State
class Player:
    def _init_(self, ID):
        self.ID = ID
        self.hand = []
        self.score = 0
    def isActive(self):
        """compare self player id with active id in state returns true or false"""
    def throwCard(self, playedCards, cardToPlay):
        if isActive(self) == True:
            card = self.hand.pop(cardToPlay) #temporary variable to hold the popped card
            playedCards.push(card)
    def screamUno(self):
        if isActive(self) == True:
            if self.hand.cardinal==1:
            #print("UNO!") we can either do it automatically or
            #canClickUno= True this makes a button on screen clickable then the player can either click it or not"""
    def getHand(self):
        return self.hand
        
            
            
            
        
