import random
from utilities.classes.Ai.bot_player import bot_player


class random_ai(bot_player):  
     # Return a card to be played by the bot's player
    def getCardToPlay(self,playableCards):
        # from utilities.classes.game.Game import Game as Game_t
        index =random.choice(list(playableCards.values()))    
        return index
    
            
               





