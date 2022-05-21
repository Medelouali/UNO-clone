from utilities.classes.game.Game import Game
# import object.card as cards
"""from utilities.classes.object.deck import Deck"""
from utilities.classes.object.Object import Object

class Player:
    def __init__(self, id) -> None:
        self.id = id
        self.hand = []
        self.handCardinal = 7
        self.score = 0
        self.hasUno = False
        self.screamedUno = False
    def isActive(self):
        if Game.state["activePlayer"] == self.id:
            return True
        else:
            return False
        """compare self player id with active id in state returns true or false"""
    def getHasUno(self):
        return self.hasUno
    def getScreamedUno(self):
        return self.screamedUno
    def screamUno(self):
        if self.isActive(self):
            if (Game.players[Game.state["activePlayer"]-Game.rotation].hasUno == True) and (Game.players[Game.state["activePlayer"]-Game.rotation].screamedUno == False):
                Game.players[Game.state["activePlayer"]-Game.rotation].deck.draw(Game.deck, self.hand, 2)
                self.screamUno = True
                print("player ", self.ID, "screamed UNO\n")
            elif self.hasUno:
                self.screamUno = True
                print("player ", self.ID, "screamed UNO\n")
            else:
                print("why'd you do that?")
                """I'm tempted to add a click counter and a while loop to make the comment more sarcastic everytime uno is clicked for no reason"""
    def getHand(self):
        return self.hand
    def setHand(self, hand):
        self.hand=hand
        
            
            
            
        
