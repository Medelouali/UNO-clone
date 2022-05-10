from utilities.classes.game import Game
import object.card as cards
from utilities.classes.object.deck import Deck
from object.Object import Object
class Player:
    def _init_(self, ID):
        self.ID = ID
        self.hand = []
        self.handCardinal = 7
        self.score = 0
        self.hasUno = False
        self.screamedUno = False
    def isActive(self, Game):
        if Game.state["activePlayer"] == self.ID:
            return True
        else:
            return False
        """compare self player id with active id in state returns true or false"""
    def compareSingleCard(self,lastPlayedCard,cardToPlay):
        if cardToPlay.type=="normal":
            if(lastPlayedCard.getColor()==cardToPlay.getColor() and lastPlayedCard.getNumbers()==cardToPlay.getNumbers()):
                return cardToPlay
            else:
                return NULL
        elif cardToPlay.type=="wild":
            return cardToPlay
        else:
            if lastPlayedCard.getColor()==cardToPlay.getColor():
                return cardToPlay
            else:
                return NULL
    def throwCard(self, playedCards, lastPlayedCard, cardToPlay, Game):
        if self.isActive(self, Game) == True:
            if self.compareSingleCard(self, lastPlayedCard, cardToPlay)== cardToPlay:
                card = self.hand.pop(hand.index(cardToPlay)) #temporary variable to hold the popped card
                playedCards.append(card)
                Game.state["activePlayer"] += Game.rotation
            """changes playerActive to next player hence this player's to false"""        
    def getHasUno(self):
        return self.hasUno
    def getScreamedUno(self):
        return self.screamedUno
    def screamUno(self, Game):
        if self.isActive(self, Game) == True:
            if (Game.players[Game.state["activePlayer"]-Game.rotation].hasUno == True) and (Game.players[Game.state["activePlayer"]-Game.rotation].screamedUno == False):
                Game.players[Game.state["activePlayer"]-Game.rotation].deck.draw(deck, self.hand, 2)
                self.screamUno = True
                print("player ", self.ID, "screamed UNO\n")
            elif self.hasUno == True:
                self.screamUno = True
                print("player ", self.ID, "screamed UNO\n")
            else:
                print("why'd you do that?")
                """I'm tempted to add a click counter and a while loop to make the comment more sarcastic everytime uno is clicked for no reason"""
    def getHand(self):
        return self.hand
        
            
            
            
        
