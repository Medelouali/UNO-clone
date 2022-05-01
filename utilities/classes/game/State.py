
class State:
    def __init__(self):
        self.state={
            "rotation": 1,
            "unoWasSaid": False,
            "winner": None,
        }
        
    def setState(self, key, value):
        if(key in self.state.keys()):
            self.state[key]=value
       
    def getState(self, key):
        if(key in self.state.keys()):
            return self.state[key]
        return None