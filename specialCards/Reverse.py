

def reverseOrder():
    from utilities.classes.game.Game import Game
    StateBefore=Game.state.getState(Game.state,"rotation")
    print("getting the previous rotation state")
    Game.state.setState(Game.state,"rotation",StateBefore*(-1))
    print("setting the new rotation state")
        