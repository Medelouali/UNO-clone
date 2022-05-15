import numbers
from utilities.classes.object.Object import Object
from utilities.functions.path import getPath
class Card(Object):
    def __init__(self, number, color, type="Normal", coordinates=[1, 1], dimensions=[0, 0], icon=getPath("images", "logo.png"), isVisible=False):
        super().__init__(isVisible, coordinates, dimensions, icon)
        self.number = number
        self.color=color
        self.type=type
        self.icon = icon
        
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
        return self.coordinates
    # to set new position of a card
    def setPosition(self,coordinates):
        self.coordinates = coordinates
    