# import object.card as cards
import random
from utilities.classes.object.player.Player import Player
import pygame
from utilities.functions.path import writeText

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
    def getCommonColor(self,playableCards):
        colors={}
        for i in playableCards.values():
            try:
                colors[self.getHand()[i].getColor()] = colors[self.getHand()[i].getColor()] + 1
            except KeyError:
                colors[self.getHand()[i].getColor()] = 1
            if(colors):
                return max(colors,key=colors.get)

    def getCommonNumber(self,playableCards):
        numbers={}
        for i in playableCards.values():
            try:
                numbers[self.getHand()[i].getNumber()] = numbers[self.getHand()[i].getNumber()] + 1
            except KeyError:
                numbers[self.getHand()[i].getNumber()] = 1
            if(numbers):
                return max(numbers,key=numbers.get)
    # for the Ai to play when      
    def performMove(self):
        from utilities.classes.game.Game import Game as Game_t
        for i in range(len(self.getHand())):
            if self.getHand()[i].compareSingleCard():
                # pop a card to play from the Ai's hand
                cardToPlay = self.getHand().pop(i)
                # set the last played card to be this card
                Game_t.setState("lastPlayedCard",cardToPlay)
                Game_t.getState("lastPlayedCard").applyEffect()
                # add cardToPlay to deck of played cards
                Game_t.playedCards[cardToPlay.getId()]=cardToPlay
                Game_t.rotate()
                Game_t.colorPicker.resetPickedColor()
                return 
        if(Game_t.deck.getSize()>=1):
            # print("I'm drawing")
            Game_t.deck.draw()
            Game_t.rotate()
        else :
            print("Can't draw no more")
            print(Game_t.deck.getSize()) 
  
            
               





