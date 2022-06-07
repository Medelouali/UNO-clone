# from menus.main import main
from utilities.classes.game.Game import Game
from utilities.sockets.network import Network


if(__name__ == '__main__'):
    # menu_label = "" #to mark the menu 
    # rectangles ={} # to mark the existing Rect's
    # main(menu_label, rectangles)
    game = Game(Network())
    game.run()
