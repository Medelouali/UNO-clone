
class Object:
    def __init__(self, isVisible=False, coordinates=[0, 0], dimensions=[1, 1], icon=None):
        self.isVisible=isVisible
        self.coordinates=coordinates
        self.dimensions=dimensions # width, height
        self.icon=icon

    def render(self):
        pass