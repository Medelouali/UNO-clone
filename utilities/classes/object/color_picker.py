from utilities.classes.object.Object import Object
from utilities.functions.path import getPath
from utilities.functions.resize import getSize




class ColorPicker():
    def __init__(self):
        self.picked_color =None
        self.colors_objects={}

    def fillColors(self):
        from utilities.classes.game.Game import Game as Game
        colors=["red", "green", "blue", "yellow"]
        for i in range(4):
            print(colors[i])
            self.colors_objects[colors[i]]=Object([Game.screenWidth/3+100*i,Game.screenHeight/2-150],
                [90, 90],icon=getPath("images", "icons", f"{colors[i]}.png"),
                callback=lambda color=colors[i]: self.setPickedColor(color)
            )
            
    def drawColors(self):
        for value in self.colors_objects.values():
            value.add()
            
    def wipeColors(self):
        from utilities.classes.game.Game import Game as Game
        for value in self.colors_objects.values():
            value.setDimensions((0, 0)).destroyObject()
            
    def setPickedColor(self, color):
        from utilities.classes.game.Game import Game as Game
        Game.setState("chosen_color", color.capitalize())
        Game.setState("message", f"You chose {color.capitalize()}")
        Game.setState("color_picked",True)
        self.wipeColors()
        Game.rotate()
        
    def resetPickedColor(self):
        from utilities.classes.game.Game import Game as Game
        Game.setState("chosen_color", None)

    def getPickedColor(self):
        return self.picked_color

