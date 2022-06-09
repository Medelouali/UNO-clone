from utilities.classes.game.Game import Game
from utilities.sockets.network import Network

# run this for development
if(__name__ == '__main__'):
    game = Game()
    game.run()