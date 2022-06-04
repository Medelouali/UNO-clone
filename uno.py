from utilities.classes.game.Game import Game
import sys

# run this file with a flag as command line argument if you want it to be a server
# otherwise just ignore this comment

if(__name__ == '__main__'):
    argumentList = sys.argv[1:]
    game = Game(False if len(argumentList) > 0 else True)
    game.run()
