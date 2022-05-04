from object.player import Player
import object.card as cards
import random
class Ai(Player):
  
    def __init__(self):
        # calling the parent constructor to take care of initialization of attrs that are common to all players
        Player.__init__(self)
        # intializing the list of playabale cards to an empty list
        self.playableCards = []
    # To compare two cards , a card in the player's hand and last played card 
    def compareSingleCard(self,lastPlayedCard,cardAtHand):
        # TO-DO : once a card's type is also defined we need to compare the type of the cards before comparing its value & color
        # To compare normal cards , we compare number and color of the two cards
        if(lastPlayedCard.getColor()==cardAtHand.getColor() and 
        lastPlayedCard.getNumbers()==cardAtHand.getNumbers()):
            self.playableCards.append(cardAtHand)
    # To update the list of playable cards by comparing every card against the last played card
    def updatePlayableCards(self,lastPlayedCard):
        # to check every card in the Ai's hand
        for card in self.hand:
            self.compareSingleCard(lastPlayedCard,card)
    # Overloading the throwCard method for Ai
    # After checking if it's an Ai and not a real player this method will be called automatically
    # We don't need to pass in a card to be thrown since for Ai the card will be picked randomly from a list of playableCards
    def throwCard(self,playedCards):
            cardToPlay = random.choice(self.playableCards)
            card = self.hand.pop(cardToPlay)
            playedCards.push(card)







