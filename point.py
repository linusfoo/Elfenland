class Point():

    def __init__(self, town, colour):
        self.colour = colour
        self.town = town

    def get_location(self):
        return self.town.width, self.town.height

    def get_colour(self):
        return self.colour

    def isTown(self,townname):
        return townname == self.town.get_name()