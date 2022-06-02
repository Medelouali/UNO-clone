def determine_inhibit(self,players,lastPlayedCard):
        next_player=players[self.id+1]
        if len(next_player.getHand()) < len(self.getHand()):
            hand = self.getHand()
            for i in range(len(hand)):
                if self.getHand()[i].type in ["Skip", "Reverse", "Draw","Draw4"] and self.getHand()[i].getColor() ==lastPlayedCard.getColor():
                   return i
            return -1

# function defining the type of hand [NormalOnly , MixedCards , SpecialOnly]
def TypeHand(self , playableCards ) :
    Normal=False
    Special=False
    hand=self.getHand
    for i in range (len(playableCards)) :
        if (Normal==True and Special==True):break
        if (self.hand[playableCards[i]].type =="Normal") : Normal=True 
        if (self.hand[playableCards[i]].type in ["Skip", "Reverse", "Draw","Draw4"]) : Special=True
    if(Normal==True and Special==True) : print("MixedCards")
    if(Normal==True and Special==False) : print ("NormalOnly")
    if(Normal==False and Special==True) : print ("SpecialOnly")
    if(Normal==False and Special==False) : print ("For Error")
