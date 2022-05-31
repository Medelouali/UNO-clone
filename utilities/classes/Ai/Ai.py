# import object.card as cards
import random
from utilities.classes.object.player.Player import Player

class Ai(Player):  
    def __init__(self, id):
        # calling the parent constructor to take care of initialization of attrs that are common to all players
        Player.__init__(self, id)
        # intializing the list of playabale cards to an empty list
        # self.playableCards = []
   
    # # To update the list of playable cards by comparing every card against the last played card
    # def updatePlayableCards(self, lastPlayedCard):
    #     # to check every card in the Ai's hand
    #     for card in self.hand:
    #         # checking if the return card is not null , if it's the case then add it to the list of playable cards
    #         if self.compareSingleCard(lastPlayedCard, card):
    #             self.playableCards.append(card)
    # for the Ai to play when      
    def performMove(self):
        from utilities.classes.game.Game import Game as Game_t


        for i in range(len(self.getHand())):
            if self.getHand()[i].compareSingleCard():
                # pop a card to play from the Ai's hand
                cardToPlay = self.getHand().pop(i)
                # set the last played card to be this card
                Game_t.setState("lastPlayedCard",cardToPlay)
                # add cardToPlay to deck of played cards
                Game_t.playedCards[cardToPlay.getId()]=cardToPlay
                Game_t.rotate()
                print("I played",cardToPlay)
                print("Last played card",Game_t.getState("lastPlayedCard"))
                return 
        if(Game_t.deck.getSize()>=1):
            print("I'm drawing")
            Game_t.deck.draw()
            Game_t.rotate()
        else :
            print("Can't draw no more")
            print(Game_t.deck.getSize())
        
    def printHand(self):
        for card in self.hand:
            print(card)     
    # overriding the screamUno method for Ai since it'll be called randomly when it's the Ai's turn 
    def screamUno(self,deck,Game):
            prevPlayer = Game.players[Game.state["activePlayer"]-Game.rotation]
            if (prevPlayer.hasUno) and (not prevPlayer.screamedUno):
                handOfPlayer = prevPlayer.getHand()
                deck.draw(handOfPlayer,2)
                self.screamUno = True
                print("player ", self.ID, "screamed UNO\n")
            elif self.hasUno == True:
                self.screamUno = True
                print("player ", self.ID, "screamed UNO\n")
            
               





