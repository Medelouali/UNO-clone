import numbers
from utilities.classes.object.Object import Object
from utilities.functions.path import getPath

class Card(Object):
    def __init__(self, number=None, color=None, type="Normal", coordinates=[1, 1], dimensions=[100, 100], icon=getPath("images", "logo.png"), callback=None, ownerId=None):
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
        return self
    # to get icon from a card
    
    def getIcon(self):
        return self.icon
    
    def getDimensions(self):
        return self.dimensions
    
    def compareSingleCard(self):
        from utilities.classes.game.Game import Game as Game_t
        if(not Game_t.playedCards): # this happens if it's the first card
            return self
        lastPlayedCard=Game_t.playedCards[-1]
        if self.type=="Normal":
            if(lastPlayedCard.getColor()==self.getColor() or lastPlayedCard.getNumbers()==self.getNumbers()):
                return self
            return None
        elif self.type=="Wild":
            return self
        return None
    
    def throwCard(self, playerId):
        from utilities.classes.game.Game import Game as Game_t
        # if(self.ownerId!=playerId):
        #     return
        if playerId==Game_t.state["activePlayer"]:
            if self.compareSingleCard():
                Game_t.playedCards[self.getId()]=self
                print("it's happinning")
                Game_t.rotate(Game_t.state["rotation"])
            """changes playerActive to next player hence this player's to false""" 


    
    
