import numbers
from utilities.classes.object.Object import Object
from utilities.functions.path import getPath

class Card(Object):
    def __init__(self, number=None, color=None, type="Normal", coordinates=[1, 1], 
                dimensions=[100, 100], icon=getPath("images", "logo.png"), callback=None, ownerId=None):
        super().__init__(coordinates, dimensions, icon, callback=lambda : self.throwCard(1))
        self.number = number
        self.color=color
        self.type=type
        self.icon = icon
        self.ownerId=ownerId
        
    # coloredType=["Skip", "Reverse", "Draw 2", "Draw 4", "Wild"]
    def switchCard(self):
        if(self.type=="Skip"):
            print("You choose a skip card")
        elif(self.type=="Reverse"):
            print("You choose a reverse card")
        elif(self.type=="Draw 2"):
            print("You choose draw 2 card")
        elif(self.type=="Draw 4"):
            print("You choose a draw 4 card")
        else:
            print("Norml card was chosen")
            
    # to get position of a card 
    def getPosition(self):
        return self.rect.center
    
    # to set new position of a card
    def setPosition(self, coordinates):
        self.rect.center = coordinates
        return self # We need this return value to chain methods
    
    # to get icon from a card
    def getIcon(self):
        return self.icon
    
    def getDimensions(self):
        return self.dimensions
        
    def compareSingleCard(self):
        from utilities.classes.game.Game import Game as Game_t
        lastPlayedCard=Game_t.state["lastPlayedCard"]
        if(not lastPlayedCard): # this happens if it's the first card
            return self
        
        if self.type=="Normal":
            if(lastPlayedCard.getColor()==self.getColor() or lastPlayedCard.getNumber()==self.getNumber()):
                return self
            return None
        elif self.type=="Wild":
            # w will add some code here 
            return self
        elif self.type in ["Skip", "Reverse", "Draw 2", "Draw 4", "Wild"]:
            return self
        return None
    
    def throwCard(self, playerId):
        from utilities.classes.game.Game import Game as Game_t
        if playerId==Game_t.state["activePlayer"]:
            if self.compareSingleCard():
                newHand=[]
                for card in Game_t.getState("playersList")[playerId].getHand():
                    if(card.getId()!=self.getId()):
                        newHand.append(card)
                newPlayer=Game_t.getState("playersList")[playerId]
                newPlayer.hand=newHand
                Game_t.state["playersList"][playerId]=newPlayer
                Game_t.playedCards[self.getId()]=self
                Game_t.rotate(Game_t.state["rotation"])
                Game_t.state["lastPlayedCard"]=self
                return True
            """changes playerActive to next player hence this player's to false""" 

    def getColor(self):
        return self.color
    
    def getNumber(self):
        return self.number
    