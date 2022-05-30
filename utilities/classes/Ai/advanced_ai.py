from utilities.classes.object.player.Player import Player

class advanced_ai(Player):  
    def __init__(self, id):
        # calling the parent constructor to take care of initialization of attrs that are common to all players
        super().__init__(id)
        
    def determine_inhibit(self,players,lastPlayedCard):
        next_player=players[self.id+1]
        if len(next_player.getHand()) < len(self.getHand()):
            hand = self.getHand()
            for i in range(len(hand)):
                if self.getHand()[i].type in ["Skip", "Reverse", "Draw","Draw4"] and self.getHand()[i].getColor() ==lastPlayedCard.getColor():
                   return i
            return -1

    def performMove(self):
        from utilities.classes.game.Game import Game as Game_t
        card_to_play = self.determine_inhibit(Game_t.getState("playersList"),Game_t.getState("lastPlayedCard"))
        if(card_to_play!=-1):
            cardToPlay = self.getHand().pop(card_to_play)
            # set the last played card to be this card
            Game_t.setState("lastPlayedCard",cardToPlay)
            # add cardToPlay to deck of played cards
            Game_t.playedCards[cardToPlay.getId()]=cardToPlay
            Game_t.rotate(Game_t.state["rotation"])
            print("I played",cardToPlay)
            return
        if(Game_t.deck.getSize()>=1):
            print("I'm drawing")
            Game_t.deck.draw()
            Game_t.rotate(Game_t.state["rotation"])
    