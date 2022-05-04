class Player:
    def _init_(self, ID, hand, playerActive, score):
        self.ID = ID
        self.hand = []
        self.playerActive = False
        self.score = 0
    def isActive(self):
        return self.playerActive
    def throwCard(self, playedCards, cardToPlay):
        if self.playerActive == True:
            card = self.hand.pop(cardToPlay) #temporary variable to hold the popped card
            playedCards.push(card)
    def screamUno(self):
        if self.playerActive == True:
            if self.hand.cardinal==1:
                pass
            #print("UNO!") we can either do it automatically or
            #canClickUno= True this makes a button on screen clickable then the player can either click it or not"""
    
        
            
            
            
        
