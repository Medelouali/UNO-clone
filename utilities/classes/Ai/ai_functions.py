def determine_inhibit(self,players,lastPlayedCard):
        next_player=players[self.id+1]
        if len(next_player.getHand()) < len(self.getHand()):
            hand = self.getHand()
            for i in range(len(hand)):
                if self.getHand()[i].type in ["Skip", "Reverse", "Draw","Draw4"] and self.getHand()[i].getColor() ==lastPlayedCard.getColor():
                   return i
            return -1