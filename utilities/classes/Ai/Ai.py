# import object.card as cards
import random
from utilities.classes.object.player.Player import Player

class Ai(Player):
  
    def __init__(self, id):
        # calling the parent constructor to take care of initialization of attrs that are common to all players
        Player.__init__(self, id)
        # intializing the list of playabale cards to an empty list
        self.playableCards = []
   
    # To update the list of playable cards by comparing every card against the last played card
    def updatePlayableCards(self,lastPlayedCard):
        # to check every card in the Ai's hand
        for card in self.hand:
            # checking if the return card is not null , if it's the case then add it to the list of playable cards
            if self.compareSingleCard(lastPlayedCard,card)!=None:
                self.playableCards.append(card)
    # Overloading the throwCard method for Ai
    # After checking if it's an Ai and not a real player this method will be called automatically
    # We don't need to pass in a card to be thrown since for Ai the card will be picked randomly from a list of playableCards
    def throwCard(self,playedCards,Game):
            lastPlayedCard = playedCards[0]
            self.updatePlayableCards(lastPlayedCard)
            cardToPlay = random.choice(self.playableCards)
            card = self.hand.pop(cardToPlay)
            playedCards.append(card)
            Game.state["activePlayer"] = Game.players[Game.state["activePlayer"]+Game.rotation]
            
    # overriding the screamUno method for Ai since it'll be called randomly when it's the Ai's turn 
    def screamUno(self,deck,Game):
            prevPlayer = Game.players[Game.state["activePlayer"]-Game.rotation]
            if (prevPlayer.hasUno == True) and (prevPlayer.screamedUno == False):
                handOfPlayer = prevPlayer.getHand()
                deck.draw(handOfPlayer,2)
                self.screamUno = True
                print("player ", self.ID, "screamed UNO\n")
            elif self.hasUno == True:
                self.screamUno = True
                print("player ", self.ID, "screamed UNO\n")
            
               





