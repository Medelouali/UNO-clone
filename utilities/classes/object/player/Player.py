from utilities.classes.game import Game
from utilities.classes.game.State import State
class Player:
    def _init_(self, ID):
        self.ID = ID
        self.hand = []
        self.handCardinal = 7
        self.score = 0
    def isActive(self):
        """compare self player id with active id in state returns true or false"""
    def throwCard(self, playedCards, cardToPlay):
        if isActive(self) == True:
            card = self.hand.pop(cardToPlay) #temporary variable to hold the popped card
            playedCards.push(card)
    def screamUno(self):
        if isActive(self) == True:
            if self.handCardinal==1:
                """changes boolean unoWasSaid in state and writes uno""" 
    def getHand(self):
        return self.hand
        
            
            
            
        
