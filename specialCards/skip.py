def skip (game , player =[]):
	temp = game.getState("rotation")
 	game.setState("rotation",game.getState("rotation")*2)
    if (game.getState("activePlayer") == len(players)-1 or game.getState("activePlayer") == len(players)-2) and rotation == 2:
    	if game.getState("activePlayer") == len(players)-1: game.setState("activePlayer",1)
        if game.getState("activePlayer") == len(players)-2: game.setState("activePlayer",0)
    else : 
    game.setState("activePlayer",getState("activePlayer")+ getState("rotation"))
    
    game.setState("rotation",temp)  	