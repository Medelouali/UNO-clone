
from utilities.classes.object.player.Player import Player
class bot_player(Player):  
    def __init__(self, id):
        # calling the parent constructor to take care of initialization of attrs that are common to all players
        super().__init__(id)
    # Returns a list of playable cards indexes
    def updatePlayableCards(self):
        playableCards = {}
        for i in range(len(self.getHand())):
            if(self.getHand()[i].compareSingleCard()):
                playableCards[self.getHand()[i].getCardType()]=i
        return playableCards
    # Get common color in a list of cards
    def getCommonColor(self,cards):
        colors={}
        for i in cards:
            try:
                colors[self.getHand()[i].getColor()] = colors[self.getHand()[i].getColor()] + 1
            except KeyError:
                colors[self.getHand()[i].getColor()] = 1
            if(colors):
                return max(colors,key=colors.get)
    # Get common number in a list of cards
    def getCommonNumber(self,cards):
        numbers={}
        for i in cards:
            try:
                numbers[self.getHand()[i].getNumber()] = numbers[self.getHand()[i].getNumber()] + 1
            except KeyError:
                numbers[self.getHand()[i].getNumber()] = 1
            if(numbers):
                return max(numbers,key=numbers.get)
    # method to be implemented by subclasses
    def getCardToPlay(self,playableCards):
        pass
    # for the bot to play a card
    def performMove(self):
            from utilities.classes.game.Game import Game as Game_t
            playableCards = self.updatePlayableCards()
            if(playableCards):
                    cardToPlay = self.getHand().pop(self.getCardToPlay(playableCards))
                    # set last played card to card to play
                    Game_t.setState("lastPlayedCard",cardToPlay)
                    # after picking a card , its effect should be applied
                    Game_t.getState("lastPlayedCard").applyEffect()
                    # add cardToPlay to deck of played cards
                    Game_t.playedCards[cardToPlay.getId()]=cardToPlay
                    # end the current player's turn and move to the next
                    Game_t.rotate()
                    return 
            # Check if deck is empty before drawing
            if(Game_t.deck.getSize()>=1):
                Game_t.deck.draw()
                Game_t.setState("message", "Opponent drew a card")
                Game_t.rotate()
            else :
                print("Can't draw no more")
                print(Game_t.deck.getSize()) 


