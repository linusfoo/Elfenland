import math
class Phase6:

    def __init__(self, player):
        self.player = player
        self.finished = False


    def clickedTransportCard(self, x, y):
            index = -1
            legal = 29 # Length from center of the square
            sqx = (x - 1045)**2
            sqy = (y - 489)**2
            if math.sqrt(sqx + sqy) < legal:
                index = 0
            sqx = (x - 1128)**2
            sqy = (y - 489)**2
            if math.sqrt(sqx + sqy) < legal:
                index = 1
            sqx = (x - 1209)**2
            sqy = (y - 489)**2
            if math.sqrt(sqx + sqy) < legal:
                index = 2
            sqx = (x - 1292)**2
            sqy = (y - 489)**2
            if math.sqrt(sqx + sqy) < legal:
                index = 3
            sqx = (x - 1374)**2
            sqy = (y - 489)**2
            if math.sqrt(sqx + sqy) < legal:
                index = 4
            sqx = (x - 1018) ** 2
            sqy = (y - 741) ** 2
           
            return index

    def execute(self, index):
        self.player.transport_cards.pop(index)
        return self.player


        