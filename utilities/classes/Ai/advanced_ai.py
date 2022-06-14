import random
import time

import pygame
from utilities.classes.object.player.Player import Player
from utilities.classes.Ai.bot_player import bot_player


class advanced_ai(bot_player):  
    # function defining the type of hand [NormalOnly , MixedCards , SpecialOnly]
    def getHandType(self,playableCards) :
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
    # Find which card is best to play
    def findCardToPlay(self,playableCards,typeOfCards,opponent):
        # Check if we have only one card to play , and play it automatically
        
        if(len(playableCards) == 1):
            # print("One card to play")
            return list(playableCards.values())[0]
        # if we have multuple playable cards
        else :
            # check the type of playable cards list
            if(typeOfCards=="Normal"):
                # get the most common color in player's hand
                commonColor = self.getCommonColor(playableCards.values())
                # get the most common number in player's hand
                commonNumber = self.getCommonNumber(playableCards.values())
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

                # get the most common color in player's hand
                commonColor = self.getCommonColor(playableCards.values())
                # get the most common number in player's hand
                commonNumber = self.getCommonNumber(playableCards.values())
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

    # Return a card to be played by the bot's player
    def getCardToPlay(self,playableCards):
        from utilities.classes.game.Game import Game as Game_t
        cardsType = self.getHandType(playableCards.values())
        opponent = Game_t.getState("playersList")[Game_t.getState("activePlayer")]
        index=self.findCardToPlay(playableCards,cardsType,opponent)
        if(index==None):
            index =random.choice(list(playableCards.values()))   
        return index 
    