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
        # return card to be played
    def findCardToPlay(self,playableCards,typeOfCards):
        if(typeOfCards=="Normal"):
            # call the functions you need or write the logic for this case
            print("Normal")
        elif(typeOfCards=="Mixed"):
            # call the functions you need or write the logic for this case
            print("Mixed")
        elif(typeOfCards=="Special"):
            # call the functions you need or write the logic for this case
            print("Special")
            if(playableCards.has_key("Skip")):
                return playableCards["Skip"]
            elif(playableCards.has_key("Reverse")):
                return playableCards["Reverse"]
            elif(playableCards.has_key("Wild")):
                return playableCards["Wild"]
            elif(playableCards.has_key("Draw4")):
                return playableCards["Draw4"]
            elif(playableCards.has_key("Draw")):
                return playableCards["Draw"]
            



    def performMove(self):
        from utilities.classes.game.Game import Game as Game_t
        # reads the type of playable cards to be used to decide which case we're at 
        cardsType = self.TypeHand(self.updatePlayableCards().values())
        for key,value in self.updatePlayableCards().items():
             print(key, ' : ', value)

        # self.findCardToPlay(cardsType)
        for i in range(len(self.getHand())):
            if self.getHand()[i].compareSingleCard():
                # pop a card to play from the Ai's hand
                cardToPlay = self.getHand().pop(i)
                cardToPlay.applyEffect()
                # set the last played card to be this card
                Game_t.setState("lastPlayedCard",cardToPlay)
                # add cardToPlay to deck of played cards
                Game_t.playedCards[cardToPlay.getId()]=cardToPlay
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
    