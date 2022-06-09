from gettext import find
from inspect import getcomments
import re
from turtle import color
import random
from utilities.classes.object.player.Player import Player
from collections import Counter

class advanced_ai(Player):  
    def __init__(self, id):
        # calling the parent constructor to take care of initialization of attrs that are common to all players
        super().__init__(id)
        
      # a function that returns a list of playable cards indexes
    def updatePlayableCards(self):
        playableCards = {}
        for i in range(len(self.getHand())):
            if(self.getHand()[i].compareSingleCard()):
                playableCards[self.getHand()[i].getCardType()]=i
        return playableCards
    # function defining the type of hand [NormalOnly , MixedCards , SpecialOnly]
    def TypeHand(self,playableCards) :
        Normal=False
        Special=False
        hand=self.getHand()
        if(playableCards):
            for i in (playableCards) :
                if (Normal==True and Special==True):break
                if (hand[i].type =="Normal") : Normal=True 
                if (hand[i].type in ["Skip", "Reverse", "Draw","Draw4"]) : Special=True
            if(Normal==True and Special==True) : return "Mixed"
            if(Normal==True and Special==False) : return "Normal"
            if(Normal==False and Special==True) : return "Special"
        return "Empty"
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

    # return card to be played
    def findCardToPlay(self,playableCards,typeOfCards,opponent):
        # Check if we have only one card to play , and play it automatically
        if(len(playableCards) == 1):
            print("One card to play")
            return list(playableCards.values())[0]
        # if we have multuple playable cards
        else :
            # check the type of playable cards list
            if(typeOfCards=="Normal"):
                # get the most common color in player's hand
                commonColor = self.getCommonColor(playableCards)
                # get the most common number in player's hand
                commonNumber = self.getCommonNumber(playableCards)
                print("Common color in playable cards : ",commonColor)
                # get list of index of all cards with most common color
                color_index = [idx for idx, element in enumerate(playableCards.values()) if self.getHand()[element].getColor()==commonColor]
                # get list of index of all cards with most common number
                number_index =[idx for idx, element in enumerate(playableCards.values()) if self.getHand()[element].getNumber()==commonNumber]
                # decide if you should play matching number or matching color
                # if number of cards with common color is less than number of cards with common number play a matching number card
                if(len(color_index)<len(number_index)):
                    return random.choice(number_index)
                else :
                    return random.choice(color_index)
            
            elif(typeOfCards=="Mixed"):
                # call the functions you need or write the logic for this case
                # return random.choice(list(playableCards.values()))
                # get the most common color in player's hand
                commonColor = self.getCommonColor(playableCards)
                # get the most common number in player's hand
                commonNumber = self.getCommonNumber(playableCards)
                if("Skip" in playableCards):
                    if(len(opponent.getHand())<len(self.getHand()) or len(playableCards)==1):
                        #skipping when you can actually make the next player draw next round
                        if("Draw4" in playableCards or "Draw" in playableCards):
                            return playableCards["Skip"]
                elif("Reverse" in playableCards):
                    if(len(opponent.getHand())<len(self.getHand()) or len(playableCards)==1):
                        return playableCards["Reverse"]
                elif("Draw4" in playableCards):
                    if(len(opponent.getHand())<len(self.getHand()) or len(playableCards)==1):
                        return playableCards["Draw4"]
                elif("Draw" in playableCards):
                    if(len(opponent.getHand())<len(self.getHand()) or len(playableCards)==1):
                        return playableCards["Draw"]
                #need the common color here
                elif("Wild" in playableCards):
                    if(len(playableCards)==1):
                        return playableCards["Wild"]

                #sorry for stealing your code guys 
                else:
                    print("Common color in playable cards : ",commonColor)
                    # get list of index of all cards with most common color
                    color_index = [idx for idx, element in enumerate(playableCards.values()) if self.getHand()[element].getColor()==commonColor]
                    # get list of index of all cards with most common number
                    number_index =[idx for idx, element in enumerate(playableCards.values()) if self.getHand()[element].getNumber()==commonNumber]
                    # decide if you should play matching number or matching color
                    # if number of cards with common color is less than number of cards with common number play a matching number card
                    if(len(color_index)<len(number_index)):
                        return random.choice(number_index)
                    else :
                        return random.choice(color_index)
            
            elif(typeOfCards=="Special"):
                # play skip or reverse cards when opponent has less cards than ai 
                if("Skip" in playableCards):
                    if(len(opponent.getHand())<len(self.getHand()) or len(playableCards)==1):
                        return playableCards["Skip"]
                elif("Reverse" in playableCards):
                    if(len(opponent.getHand())<len(self.getHand()) or len(playableCards)==1):
                        return playableCards["Reverse"]
                elif("Draw4" in playableCards):
                    return playableCards["Draw4"]
                elif("Draw" in playableCards):
                    return playableCards["Draw"]
                elif("Wild" in playableCards):
                    return playableCards["Wild"]
            

    def performMove(self):
            from utilities.classes.game.Game import Game as Game_t
            self.printHand()
            print("------------------")
            playableCards = self.updatePlayableCards()
            # pop a card to play from the Ai's hand
            if(playableCards):
                    cardsType = self.TypeHand(playableCards.values())
                    opponent = Game_t.getState("playersList")[Game_t.getState("activePlayer")]
                    index=self.findCardToPlay(playableCards,cardsType,opponent)
                    if(index==None):
                        index =random.choice(list(playableCards.values()))
                    cardToPlay = self.getHand().pop(index)
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
