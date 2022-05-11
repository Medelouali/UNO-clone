def skip (game , players):
    temp = game.getState("rotation")
    game.setState("rotation",game.getState("rotation")*2)
    if temp == 2:
    	if game.getState("activePlayer") == len(players)-1: 
            game.setState("activePlayer",1)
        if game.getState("activePlayer") == len(players)-2: 
            game.setState("activePlayer",0)
    else : 
        game.setState("activePlayer",game.getState("activePlayer")+ game.getState("rotation"))
    
    game.setState("rotation",temp)  	
