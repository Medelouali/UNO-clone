from utilities.classes.game.Game import Game

def reverseOrder():
    StateBefore=Game.state.getState(Game.state,"rotation")
    print("getting the previous rotation state")
    Game.state.setState(Game.state,"rotation",StateBefore*(-1))
    print("setting the new rotation state")
        