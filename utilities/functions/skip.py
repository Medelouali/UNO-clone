

 def skip (game,player,players =[]):
 	game.setState("rotation",2)
 	if getState("activePlayer") == len (players):
 		game.setState("activePlayer",0)
 	else: 
 		game.setState("activePlayer",game.getState("activePlayer")+ game.getState("rotation"))