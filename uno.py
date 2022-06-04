from utilities.classes.game.Game import Game
import sys

if(__name__ == '__main__'):
    argumentList = sys.argv[1:]
    game = Game(False if len(argumentList) > 0 else True)
    game.run()
