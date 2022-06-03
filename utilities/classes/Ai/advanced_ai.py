from inspect import getcomments
from turtle import color
from utilities.classes.object.player.Player import Player

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
        
        if(typeOfCards=="Normal"):
            # call the functions you need or write the logic for this case
            print("Normal")
        # get rid of the color you have the most 





        elif(typeOfCards=="Mixed"):
            # call the functions you need or write the logic for this case
            print("Mixed")
        elif(typeOfCards=="Special"):
            # call the functions you need or write the logic for this case
            print("Special")
            # play skip or reverse cards when opponent has less cards than ai 
            if(playableCards.has_key("Skip")):
                if(len(opponent.getHand())<len(self.getHand()) or len(playableCards)==1):
                    return playableCards["Skip"]
            elif(playableCards.has_key("Reverse")):
                if(len(opponent.getHand())<len(self.getHand()) or len(playableCards)==1):
                    return playableCards["Reverse"]
            elif(playableCards.has_key("Draw4")):
                return playableCards["Draw4"]
            elif(playableCards.has_key("Draw")):
                return playableCards["Draw"]
            elif(playableCards.has_key("Wild")):
                return playableCards["Wild"]
            

    def performMove(self):
            from utilities.classes.game.Game import Game as Game_t
            #     # reads the type of playable cards to be used to decide which case we're at 
            # cardsType = self.TypeHand(self.updatePlayableCards().values())
            # for key,value in self.updatePlayableCards().items():
            #     print(key, ' : ', self.getHand()[value].getColor())
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
                    return 
            if(Game_t.deck.getSize()>=1):
                # print("I'm drawing")
                Game_t.deck.draw()
                Game_t.rotate()
            else :
                print("Can't draw no more")
                print(Game_t.deck.getSize()) 
