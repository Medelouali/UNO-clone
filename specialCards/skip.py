from utilities.classes.game import Game

def skip (players):
    temp = Game.getState("rotation")
    Game.setState("rotation",Game.getState("rotation")*2)
    if Game.getState ("rotation") == 2:
    	if Game.getState("activePlayer") == len(players)-1: 
            Game.setState("activePlayer",1)
        if Game.getState("activePlayer") == len(players)-2: 
            Game.setState("activePlayer",0)

    else : 
        Game.setState("activePlayer",Game.getState("activePlayer")+ Game.getState("rotation"))
    
    Game.setState("rotation",temp)  	
