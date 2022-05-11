from utilities.classes.object.card.Card import Card
from utilities.classes.game.Game import Game

class Reverse(Card):
    def __init__(self, number, color, coordinates=[1, 1], dimensions=[0, 0], icon=None, isVisible=False):
        super().__init__(number, color, coordinates=[1, 1], dimensions=[0, 0], icon=None, isVisible=False)
        #in case of surcharged attribute
    def reverseOrder():
        StateBefore=state.getState(state,"rotation")
        print("getting the previous rotation state")
        state.setState(state,"rotation",StateBefore*(-1))
        print("setting the new rotation state")
        