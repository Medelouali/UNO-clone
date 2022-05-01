import numbers
from object.Object import Object

class Card(Object):
    def __init__(self, number, color, coordinates=[1, 1], dimensions=[0, 0], icon=None, isVisible=False):
        super().__init__(isVisible, coordinates, dimensions, icon)
        self.number = number
        self.color=color
        
    